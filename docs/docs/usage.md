---
sidebar_position: 3
---

# Usage

To use `pylocc`, run the following command:

```bash
pylocc [OPTIONS] <file_or_directory>
```
or from sources using uv: 
```bash
uv run pylocc --help
Usage: pylocc [OPTIONS] FILE

  Run pylocc on the specified file or directory.

Options:
  --by-file      Generate report by file.
  --output FILE  Stores the output report in csv format to the given path
  --help         Show this message and exit.

```

### Options

*   `--by-file`: Generate a report for each file individually.
*   `--output <path>`: Save the report to a csv file.

### Examples

*   Count lines of code in a single file:
    ```bash
    pylocc my_file.py
    ```
*   Count lines of code in a directory and all its subdirectories:
    ```bash
    pylocc my_project/
    ```
*   Generate a per-file report:
    ```bash
    pylocc --by-file my_project/
    ```
*   Save the report to a file:
    ```bash
    pylocc --output report.csv my_project/
    ```

