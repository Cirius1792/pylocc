import pytest
from pylocc.reporter import (
    prepare_by_file_report,
    create_by_file_table,
    aggregate_reports,
    create_aggregate_table,
    ReportData
)
from pylocc.processor import Report
import os
import csv

@pytest.fixture
def sample_reports():
    return {
        "file1.py": Report(file_type="Python", code=10, comments=2, blanks=3),
        "file2.py": Report(file_type="Python", code=15, comments=5, blanks=5),
        "file3.txt": Report(file_type="PlainText", code=20, comments=0, blanks=2),
    }

def test_prepare_by_file_report(sample_reports):
    report_data = prepare_by_file_report(sample_reports)
    assert isinstance(report_data, ReportData)
    assert len(report_data.rows) == 3
    assert report_data.headers == ["Provider", "File Name", "Lines", "Code", "Comments", "Blanks"]

def test_create_by_file_table(sample_reports):
    report_data = prepare_by_file_report(sample_reports)
    table = create_by_file_table(report_data)
    assert table is not None

def test_aggregate_reports(sample_reports):
    report_data = aggregate_reports(sample_reports)
    assert isinstance(report_data, ReportData)
    assert len(report_data.rows) == 3 # 2 languages + total
    assert report_data.headers == ["Language", "Files", "Lines", "Code", "Comments", "Blanks"]

def test_create_aggregate_table(sample_reports):
    report_data = aggregate_reports(sample_reports)
    table = create_aggregate_table(report_data)
    assert table is not None

def test_report_data_to_csv(tmp_path, sample_reports):
    report_data = prepare_by_file_report(sample_reports)
    file_path = tmp_path / "report.csv"
    report_data.to_csv(file_path)

    assert os.path.exists(file_path)

    with open(file_path, 'r') as csvfile:
        reader = csv.reader(csvfile)
        header = next(reader)
        assert header == ["Provider", "File Name", "Lines", "Code", "Comments", "Blanks"]
        rows = list(reader)
        assert len(rows) == 3
        assert rows[0] == ["file1.py", "file1", "15", "10", "2", "3"]