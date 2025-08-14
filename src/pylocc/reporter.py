import os
from typing import Dict, List
from pylocc.processor import Report
from rich.table import Table
import csv

# Headers
FILE_TYPE_HEADER = "Language"
FILE_PATH_HEADER = "Provider"
FILE_NAME_HEADER = "File Name"
NUM_FILE_HEADER = "Files"
TOTAL_LINE_HEADER = "Lines"
CODE_LINE_HEADER = "Code"
COMMENT_LINE_HEADER = "Comments"
BLANK_LINE_HEADER = "Blanks"

class ReportData:
    def __init__(self, headers: List[str], rows: List[List[str]]):
        self.headers = headers
        self.rows = rows

    def to_csv(self, file_path: str):
        with open(file_path, 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(self.headers)
            writer.writerows(self.rows)

def prepare_by_file_report(processed: Dict[str, Report]) -> ReportData:
    headers = [FILE_TYPE_HEADER, FILE_PATH_HEADER, FILE_NAME_HEADER, TOTAL_LINE_HEADER, CODE_LINE_HEADER, COMMENT_LINE_HEADER, BLANK_LINE_HEADER]
    rows = []
    for file_path, report_data in processed.items():
        file_name = os.path.basename(os.path.splitext(file_path)[0])
        rows.append([
            report_data.file_type.value,
            file_path,
            file_name,
            str(report_data.total),
            str(report_data.code),
            str(report_data.comments),
            str(report_data.blanks),
        ])
    return ReportData(headers, rows)

def create_by_file_table(report_data: ReportData) -> Table:
    report = Table(show_header=True, header_style="bold magenta")
    for header in report_data.headers:
        report.add_column(header, justify="right" if header not in [FILE_PATH_HEADER, FILE_NAME_HEADER] else "dim")

    for row in report_data.rows:
        report.add_row(*row)
    return report

def aggregate_reports(processed: Dict[str, Report]) -> ReportData:
    aggregated_report = {}
    files_per_type = {}
    for report_data in processed.values():
        if report_data.file_type not in aggregated_report:
            aggregated_report[report_data.file_type] = Report(file_type=report_data.file_type)
            files_per_type[report_data.file_type] = 0

        aggregated_report[report_data.file_type].increment_code(report_data.code)
        aggregated_report[report_data.file_type].increment_comments(report_data.comments)
        aggregated_report[report_data.file_type].increment_blanks(report_data.blanks)
        files_per_type[report_data.file_type] += 1

    headers = [FILE_TYPE_HEADER, NUM_FILE_HEADER, TOTAL_LINE_HEADER, CODE_LINE_HEADER, COMMENT_LINE_HEADER, BLANK_LINE_HEADER]
    rows = []
    total_files = 0
    total_lines = 0
    code_lines = 0
    comment_lines = 0
    blank_lines = 0

    for file_type, report_data in aggregated_report.items():
        rows.append([
            file_type.value,
            f"{files_per_type[file_type]:,}",
            f"{report_data.total:,}",
            f"{report_data.code:,}",
            f"{report_data.comments:,}",
            f"{report_data.blanks:,}",
        ])
        total_files += files_per_type[file_type]
        total_lines += report_data.total
        code_lines += report_data.code
        comment_lines += report_data.comments
        blank_lines += report_data.blanks
    
    rows.append([
        "Total",
        f"{total_files:,}",
        f"{total_lines:,}",
        f"{code_lines:,}",
        f"{comment_lines:,}",
        f"{blank_lines:,}",
    ])

    return ReportData(headers, rows)

def create_aggregate_table(report_data: ReportData) -> Table:
    report = Table(show_header=True, header_style="bold magenta")
    for header in report_data.headers:
        report.add_column(header, justify="right" if header != FILE_TYPE_HEADER else "dim")

    for row in report_data.rows:
        report.add_row(*row)
        
    return report
