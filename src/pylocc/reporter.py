from typing import Dict
from pylocc.processor import Report
from prettytable import PrettyTable


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
