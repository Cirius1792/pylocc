from typing import Dict
from pylocc.processor import Report
from rich.table import Table

# Language,Provider,Filename,Lines,Code,Comments,Blanks,Complexity,Bytes,ULOC
file_type_header = "Language"
file_path_header = "Provider"
num_file_header = "Files"
total_line_header = "Lines"
code_line_header = "Code"
comment_line_header = "Comments"
blank_line_header = "Blanks"


def report_by_file(processed: Dict[str, Report]) -> Table:
    """Given the report by file, prepares a table contaning the results.
    Also generates an overall report aggregating all the informations"""
    report = Table(show_header=True, header_style="bold magenta")
    report.add_column(file_path_header, style="dim")
    report.add_column(total_line_header, justify="right")
    report.add_column(code_line_header, justify="right")
    report.add_column(comment_line_header, justify="right")
    report.add_column(blank_line_header, justify="right")

    for file_path, report_data in processed.items():
        report.add_row(
            file_path,
            f"{report_data.total:,}",
            f"{report_data.code:,}",
            f"{report_data.comments:,}",
            f"{report_data.blanks:,}",
        )
    return report


def report_aggregate(processed: Dict[str, Report]) -> Table:
    """Given the report by file, prepares a table containing the overall results."""
    # Initialize accumulators for the overall aggregated numbers
    total_lines = 0
    code_lines = 0
    blank_lines = 0
    comment_lines = 0
    total_files = 0

    # Initialize the aggregators for the per file type report
    aggregated_report = {}
    files_per_type = {}
    for report_data in processed.values():
        if report_data.file_type not in aggregated_report:
            # If there is no accumulator yet, initialize it
            aggregated_report[report_data.file_type] = Report(
                file_type=report_data.file_type)
            # as well as it's corresponding file counter
            files_per_type[report_data.file_type] = 0

        # Increment the accumulators for the code statistics
        aggregated_report[report_data.file_type].increment_code(
            report_data.code)
        aggregated_report[report_data.file_type].increment_comments(
            report_data.comments)
        aggregated_report[report_data.file_type].increment_blanks(
            report_data.blanks)
        # Increment the total files counter
        files_per_type[report_data.file_type] += 1

    report = Table(show_header=True, header_style="bold magenta")
    report.add_column(file_type_header, style="dim")
    report.add_column(num_file_header, justify="right")
    report.add_column(total_line_header, justify="right")
    report.add_column(code_line_header, justify="right")
    report.add_column(comment_line_header, justify="right")
    report.add_column(blank_line_header, justify="right")

    for file_type, report_data in aggregated_report.items():
        report.add_row(
            file_type,
            f"{files_per_type[file_type]:,}",
            f"{report_data.total:,}",
            f"{report_data.code:,}",
            f"{report_data.comments:,}",
            f"{report_data.blanks:,}",
        )
        total_files += files_per_type[report_data.file_type]
        total_lines += report_data.total
        code_lines += report_data.code
        comment_lines += report_data.comments
        blank_lines += report_data.blanks

    report.add_row(
        "Total",
        f"{total_files:,}",
        f"{total_lines:,}",
        f"{code_lines:,}",
        f"{comment_lines:,}",
        f"{blank_lines:,}",
    )
    return report