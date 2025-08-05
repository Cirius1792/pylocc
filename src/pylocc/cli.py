import os
from typing import List
import click
from rich.console import Console

from pylocc.file_utils import get_all_file_paths
from pylocc.processor import Processor, ProcessorConfiguration, ProcessorConfigurationFactory
from pylocc.reporter import report_aggregate, report_by_file

import importlib.metadata

__version__ = importlib.metadata.version('pylocc')

def load_language_config() -> List[ProcessorConfiguration]:
    """Load language configurations from the packaged JSON file."""
    import json
    from importlib import resources

    try:
        # Use importlib.resources to access the file
        with resources.files('pylocc').joinpath('language.json').open('r', encoding='utf-8') as f:
            config_data = json.load(f)
        return ProcessorConfiguration.load_from_dict(config_data)
    except (FileNotFoundError, json.JSONDecodeError) as e:
        # Handle potential errors during file loading or parsing
        click.echo(f"Error loading language configuration: {e}", err=True)
        raise click.Abort()





@click.command()
@click.argument('file', type=click.Path(exists=True, dir_okay=True, readable=True), required=False)
@click.option('--by-file', is_flag=True,
              help='Generate report by file.')
@click.option('--output', type=click.Path(exists=False, dir_okay=False, readable=True, writable=True),
              help='Stores the output report in csv format to the given path')
@click.version_option(version=__version__, prog_name='pylocc')
def pylocc(file, by_file, output):
    """Run pylocc on the specified file or directory."""
    configs = load_language_config()
    supported_extensions = [
        ext for config in configs for ext in config.file_extensions]

    configuration_factory = ProcessorConfigurationFactory(configs)

    if os.path.isdir(file):
        files = get_all_file_paths(
            file, supported_extensions=supported_extensions)
    else:
        files = [file]

    processor = Processor()
    per_file_reports = {}
    for f in files:
        try:
            with open(f, 'r', encoding='utf-8', errors='ignore') as f_handle:
                content = f_handle.readlines()
            file_extension = os.path.splitext(f)[1][1:]
            file_configuration = configuration_factory.get_configuration(
                file_extension)
            if file_configuration:
                report = processor.process(
                    content, file_configuration=file_configuration)
                per_file_reports[f] = report
            else:
                click.echo(
                    f"No configuration found for file type '{file_extension}' in file {f}. Skipping...")
                continue
        except Exception as e:
            click.echo(f"Error processing file {f}: {e} Skipping...")
            continue
    if per_file_reports:
        console = Console()
        report_table = None
        if by_file:
            report_table = report_by_file(per_file_reports)
        else:
            report_table = report_aggregate(per_file_reports)
        console.print(report_table)


if __name__ == '__main__':
    pylocc()
