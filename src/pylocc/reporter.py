from typing import Dict, List
from pylocc.processor import Report
from prettytable import PrettyTable

file_path_header = "File Path"
total_file_header = "Total Files"
total_line_header = "Total Lines"
code_line_header = "Code Lines"
comment_line_header = "Comment Lines"
blank_line_header = "Blank Lines"


def report_by_file(processed: Dict[str, Report]) -> str:
    """Given the report by file, prepares a table contaning the results. 
    Also generates an overall report aggregating all the informations"""
    report = PrettyTable()
    report.field_names = [file_path_header, total_line_header,
                          code_line_header, comment_line_header, blank_line_header]
    # Initialize integer formatters for the report
    report = initialize_int_formatters(report, report.field_names[1:])
    for file_path, report_data in processed.items():
        report.add_row([
            file_path,
            report_data.total,
            report_data.code,
            report_data.comments,
            report_data.blanks
        ])
    return str(report)


def report_aggregate(processed: Dict[str, Report]) -> str:
    """Given the report by file, prepares a table containing the overall results."""
    total_lines = 0
    code_lines = 0
    blank_lines = 0
    comment_lines = 0
    total_files = len(processed)
    for report_data in processed.values():
        total_lines += report_data.total
        code_lines += report_data.code
        blank_lines += report_data.blanks
        comment_lines += report_data.comments

    report = PrettyTable()
    report.field_names = [total_file_header, total_line_header,
                          code_line_header, comment_line_header, blank_line_header]
    report = initialize_int_formatters(report, report.field_names)
    report.add_row([total_files, total_lines, code_lines, comment_lines, blank_lines])
    return str(report)


def initialize_int_formatters(t: PrettyTable, headers:List[str]) -> PrettyTable:
    """Initialize integer formatters for the provided tabel and the given headers"""
    for header in headers:
        t.custom_format[header] = format_number_with_thousand_separator
    return t


def format_number_with_thousand_separator(_, v) -> str:
    """Formats a number with a thousand separator."""
    return f"{v:,}" if isinstance(v, (int, float)) else str(v)
