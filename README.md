# Python Loc Counter - PYLOCC
![Tests](https://github.com/cirius1792/pylocc/actions/workflows/tests.yml/badge.svg) ![Coverage](https://raw.githubusercontent.com/Cirius1792/pylocc/refs/heads/main/coverage.svg)
<p align="center">
    <img src="https://cirius1792.github.io/pylocc/img/pylocc_logo_transparent.png" alt="pylocc logo" width="400"/>
</p>

`pylocc` is a command-line tool for counting lines of code in various programming languages. It helps you get a quick overview of the size and composition of your codebase.

This project draws instiparion from [scc](https://github.com/boyter/scc) and uses the same language.json file. 

## Features
Please have a look at the [documentaiton page](https://cirius1792.github.io/pylocc/) for more details. 

*   Counts lines of code, comments, and blank lines.
*   Supports a wide range of programming languages.
*   Can process single files or entire directories.
*   Provides both aggregated and per-file reports.
*   Easy to use and configure.

## Requirements

- Python >= 3.10

## Installation

### From Pypi
```bash
 pip install pylocc

 pylocc --help
 ```
### From Source

1.  Clone the repository:
    ```bash
    git clone https://github.com/your-username/pylocc.git
    ```
2.  Navigate to the project directory:
    ```bash
    cd pylocc
    ```
3.  Install the dependencies:
    ```bash
    uv run pylocc
    ```

## Usage

To use `pylocc`, run the following command:

```bash
pylocc [OPTIONS] <file_or_directory>
```
or
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
*   `--output <path>`: Save the report to a file.

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

## Configuration

`pylocc` uses a `language.json` file to define the comment syntax for different languages. You can customize this file to add new languages or modify existing ones.

Each language entry in `language.json` has the following structure:

```json
{
  "LanguageName": {
    "extensions": ["ext1", "ext2"],
    "line_comment": ["//"],
    "multi_line": [["/*", "*/"]]
  }
}
```

*   `extensions`: A list of file extensions for the language.
*   `line_comment`: A list of strings that represent single-line comments.
*   `multi_line`: A list of pairs of strings that represent the start and end of multi-line comments.

## Contributing

Contributions are welcome! Please feel free to open an issue or submit a pull request.
