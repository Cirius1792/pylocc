from typing import Dict
from pylocc.processor import Report
from prettytable import PrettyTable

total_line_header = "Total Lines"
code_line_header = "Code Lines"
comment_line_header = "Comment Lines"
def report_by_file(processed: Dict[str, Report]) -> str:
    """Given the report by file, prepares a table contaning the results. 
    Also generates an overall report aggregating all the informations"""
    report = PrettyTable()
    report.field_names = ["File Path", "Total Lines", "Code Lines", "Comment Lines"]
    for file_path, report_data in processed.items():
        report.add_row([
            file_path,
            report_data.total,
            report_data.code,
            report_data.comments
        ])
    return str(report)
def report_aggregate(processed:Dict[str, Report]) -> str:
    """Given the report by file, prepares a table containing the overall results."""
    total_lines = sum(report_data.total for report_data in processed.values())
    code_lines = sum(report_data.code for report_data in processed.values())
    comment_lines = sum(report_data.comments for report_data in processed.values())
    report = PrettyTable()
    report.field_names = [total_line_header, code_line_header, comment_line_header]
    report.custom_format[total_line_header] = format_number_with_thousand_separator
    report.custom_format[code_line_header] = format_number_with_thousand_separator
    report.custom_format[comment_line_header] = format_number_with_thousand_separator
    report.add_row(["{:,}".format(total_lines), code_lines, comment_lines])
    return str(report)

def format_number_with_thousand_separator( _, v) -> str:
    """Formats a number with a thousand separator."""
    return f"{v:,}" if isinstance(v, (int, float)) else str(v)
