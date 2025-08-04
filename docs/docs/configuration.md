---
sidebar_position: 4
---

# Configuration

`pylocc` uses a `language.json` file to define the comment syntax for different languages. 
Pylocc uses the same language configuration file of [scc](https://github.com/boyter/scc).

You can customize this file to add new languages or modify existing ones.

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

