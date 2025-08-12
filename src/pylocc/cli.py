import os
import click
from rich.console import Console

from pylocc.file_utils import get_all_file_paths
from pylocc.processor import ProcessorConfigurationFactory, count_locs, load_default_language_config
from pylocc.reporter import aggregate_reports, create_aggregate_table, prepare_by_file_report, create_by_file_table

import importlib.metadata

__version__ = importlib.metadata.version('pylocc')


@click.command()
@click.argument('file', type=click.Path(exists=True, dir_okay=True, readable=True), required=False)
@click.option('--by-file', is_flag=True,
              help='Generate report by file.')
@click.option('--output', type=click.Path(exists=False, dir_okay=False, readable=True, writable=True),
              help='Stores the output report in csv format to the given path')
@click.version_option(version=__version__, prog_name='pylocc')
def pylocc(file, by_file, output):
    """Run pylocc on the specified file or directory."""
    configs = load_default_language_config()
    supported_extensions = [
        ext for config in configs for ext in config.file_extensions]

    configuration_factory = ProcessorConfigurationFactory(configs)

    if os.path.isdir(file):
        files_gen = get_all_file_paths(
            file, supported_extensions=supported_extensions)
        files = list(files_gen)
    else:
        files = [file]

    per_file_reports = {}
    for f in files:
        try:
            file_extension = os.path.splitext(f)[1][1:]
            file_configuration = configuration_factory.get_configuration(
                file_extension=file_extension)

            if not file_configuration:
                click.echo(
                    f"No configuration found for file type '{file_extension}' in file {f}. Skipping...")
                continue

            with open(f, 'r', encoding='utf-8', errors='ignore', buffering=8192) as f_handle:
                report =count_locs(
                    f_handle, file_configuration=file_configuration)
                per_file_reports[f] = report
        except Exception as e:
            click.echo(f"Error processing file {f}: {e} Skipping...")
            continue
    if per_file_reports:
        console = Console()
        report_data = None
        if by_file:
            report_data = prepare_by_file_report(per_file_reports)
            report_table = create_by_file_table(report_data)
        else:
            report_data = aggregate_reports(per_file_reports)
            report_table = create_aggregate_table(report_data)

        if output:
            report_data.to_csv(output)
            console.print(f"Report saved to {output}")
        else:
            console.print(report_table)


if __name__ == '__main__':
    pylocc()
