from typing import Dict
from pylocc.processor import Report
from prettytable import PrettyTable

file_path_header = "File Path"
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
    report = initialize_formatters(report)
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
    total_lines = sum(report_data.total for report_data in processed.values())
    code_lines = sum(report_data.code for report_data in processed.values())
    blank_lines = sum(report_data.blanks for report_data in processed.values())
    comment_lines = sum(
        report_data.comments for report_data in processed.values())
    report = PrettyTable()
    report.field_names = [total_line_header,
                          code_line_header, comment_line_header, blank_line_header]
    report = initialize_formatters(report)
    report.add_row([total_lines, code_lines, comment_lines, blank_lines])
    return str(report)


def initialize_formatters(t: PrettyTable) -> PrettyTable:
    """Initializes the formatters for the PrettyTable."""
    t.custom_format[total_line_header] = format_number_with_thousand_separator
    t.custom_format[code_line_header] = format_number_with_thousand_separator
    t.custom_format[comment_line_header] = format_number_with_thousand_separator
    t.custom_format[blank_line_header] = format_number_with_thousand_separator
    return t


def format_number_with_thousand_separator(_, v) -> str:
    """Formats a number with a thousand separator."""
    return f"{v:,}" if isinstance(v, (int, float)) else str(v)
