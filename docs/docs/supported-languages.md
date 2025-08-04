---
sidebar_position: 2
title: Supported Languages
---

# Supported Languages

This page lists all the programming languages supported by `pylocc` and their respective configurations.

## ABAP

```json
{
  "ABAP": {
    "complexitychecks": [
      "for ",
      "for(",
      "if ",
      "if(",
      "switch ",
      "while ",
      "else ",
      "|| ",
      "&& ",
      "!= ",
      "== "
    ],
    "extensions": [
      "abap"
    ],
    "line_comment": [
      "*",
      "\\\""
    ],
    "multi_line": [],
    "quotes": []
  }
}
```

## ABNF

```json
{
  "ABNF": {
    "complexitychecks": [
      "=/ ",
      "/ ",
      "% ",
      "( "
    ],
    "extensions": [
      "abnf"
    ],
    "line_comment": [
      ";"
    ],
    "multi_line": [],
    "quotes": []
  }
}
```

## APL

```json
{
  "APL": {
    "complexitychecks": [
      ":For ",
      ":If ",
      ":Case ",
      ":CaseList ",
      ":While ",
      ":Repeat ",
      ":Else ",
      "\u2228",
      "\u2227",
      "\u2260",
      "~",
      "\u00a8",
      "=",
      ":"
    ],
    "extensions": [
      "apl",
      "aplf",
      "apln",
      "aplc",
      "dyalog"
    ],
    "line_comment": [
      "\u235d"
    ],
    "multi_line": [],
    "quotes": [
      {
        "end": "'",
        "start": "'"
      }
    ]
  }
}
```

## ASP

```json
{
  "ASP": {
    "complexitychecks": [
      "for ",
      "for(",
      "if ",
      "if(",
      "switch ",
      "while ",
      "else ",
      "|| ",
      "&& ",
      "!= ",
      "== "
    ],
    "extensions": [
      "asa",
      "asp"
    ],
    "line_comment": [
      "'",
      "REM"
    ],
    "multi_line": [],
    "quotes": []
  }
}
```

## ASP.NET

```json
{
  "ASP.NET": {
    "complexitychecks": [
      "for ",
      "for(",
      "if ",
      "if(",
      "switch ",
      "while ",
      "else ",
      "|| ",
      "&& ",
      "!= ",
      "== "
    ],
    "extensions": [
      "asax",
      "ascx",
      "asmx",
      "aspx",
      "master",
      "sitemap",
      "webinfo"
    ],
    "line_comment": [],
    "multi_line": [
      [
        "<!--",
        "-->"
      ],
      [
        "<%--",
        "-->"
      ]
    ],
    "quotes": []
  }
}
```

## ATS

```json
{
  "ATS": {
    "complexitychecks": [
      "if ",
      "if(",
      " then ",
      " else ",
      "case+ ",
      "ifcase",
      "let ",
      "and "
    ],
    "extensions": [
      "dats",
      "sats",
      "ats",
      "hats"
    ],
    "line_comment": [
      "//"
    ],
    "multi_line": [
      [
        "/*",
        "*/"
      ],
      [
        "(*",
        "*)"
      ],
      [
        "////",
        "THISSHOULDNEVERAPPEARWEHOPE"
      ]
    ],
    "quotes": [
      {
        "end": "\"",
        "start": "\""
      }
    ]
  }
}
```

## AWK

```json
{
  "AWK": {
    "complexitychecks": [
      "else ",
      "for ",
      "for(",
      "if ",
      "if(",
      "switch ",
      "switch(",
      "while ",
      "while(",
      "|| ",
      "&& ",
      "!= ",
      "== "
    ],
    "extensions": [
      "awk"
    ],
    "line_comment": [
      "#"
    ],
    "multi_line": [],
    "quotes": [
      {
        "end": "\"",
        "start": "\""
      }
    ],
    "shebangs": [
      "awk",
      "gawk",
      "mawk",
      "nawk"
    ]
  }
}
```

## ActionScript

```json
{
  "ActionScript": {
    "complexitychecks": [
      "for ",
      "for(",
      "if ",
      "if(",
      "switch ",
      "while ",
      "else ",
      "|| ",
      "&& ",
      "!= ",
      "== "
    ],
    "extensions": [
      "as"
    ],
    "line_comment": [
      "//"
    ],
    "multi_line": [
      [
        "/*",
        "*/"
      ]
    ],
    "quotes": [
      {
        "end": "\"",
        "start": "\""
      }
    ]
  }
}
```

## Ada

```json
{
  "Ada": {
    "complexitychecks": [
      "for ",
      "for(",
      "if ",
      "if(",
      "switch ",
      "while ",
      "else ",
      "|| ",
      "&& ",
      "!= ",
      "== "
    ],
    "extensions": [
      "ada",
      "adb",
      "ads",
      "pad"
    ],
    "line_comment": [
      "--"
    ],
    "multi_line": [],
    "quotes": []
  }
}
```

## Agda

```json
{
  "Agda": {
    "complexitychecks": [
      "for ",
      "for(",
      "if ",
      "if(",
      "switch ",
      "while ",
      "else ",
      "|| ",
      "&& ",
      "!= ",
      "== "
    ],
    "extensions": [
      "agda"
    ],
    "line_comment": [
      "--"
    ],
    "multi_line": [
      [
        "{-",
        "-}"
      ]
    ],
    "quotes": []
  }
}
```

## Alchemist

```json
{
  "Alchemist": {
    "complexitychecks": [
      "+",
      "->",
      "!"
    ],
    "extensions": [
      "crn"
    ],
    "line_comment": [
      "#"
    ],
    "multi_line": [],
    "quotes": []
  }
}
```

## Alex

```json
{
  "Alex": {
    "complexitychecks": [],
    "extensions": [
      "x"
    ],
    "line_comment": [],
    "multi_line": [],
    "quotes": []
  }
}
```

## Alloy

```json
{
  "Alloy": {
    "complexitychecks": [
      "implies ",
      "else ",
      "for ",
      "|| ",
      "&& ",
      "!= ",
      "== ",
      "<= ",
      ">= "
    ],
    "extensions": [
      "als"
    ],
    "line_comment": [
      "//",
      "--"
    ],
    "multi_line": [
      [
        "/*",
        "*/"
      ]
    ],
    "quotes": []
  }
}
```

## Android Interface Definition Language

```json
{
  "Android Interface Definition Language": {
    "complexitychecks": [
      "for ",
      "for(",
      "if ",
      "if(",
      "switch ",
      "while ",
      "else ",
      "|| ",
      "&& ",
      "!= ",
      "== "
    ],
    "extensions": [
      "aidl"
    ],
    "line_comment": [
      "//"
    ],
    "multi_line": [
      [
        "/**",
        "*/"
      ],
      [
        "/*",
        "*/"
      ]
    ],
    "quotes": [
      {
        "end": "\"",
        "start": "\""
      }
    ]
  }
}
```

## AppleScript

```json
{
  "AppleScript": {
    "complexitychecks": [
      "considering ",
      "ignoring ",
      "repeat ",
      "while ",
      "if ",
      "else ",
      "else if ",
      "try ",
      "on error ",
      "and ",
      "or "
    ],
    "extensions": [
      "applescript"
    ],
    "line_comment": [
      "#",
      "--"
    ],
    "multi_line": [
      [
        "(*",
        "*)"
      ]
    ],
    "quotes": [
      {
        "end": "\"",
        "start": "\""
      }
    ],
    "shebangs": []
  }
}
```

## Arturo

```json
{
  "Arturo": {
    "complexitychecks": [
      "loop ",
      "map ",
      "select ",
      "if ",
      "if? ",
      "while ",
      "function ",
      "or? ",
      "and? ",
      "not? ",
      "<> ",
      "= "
    ],
    "extensions": [
      "art"
    ],
    "line_comment": [
      ";"
    ],
    "multi_line": [],
    "quotes": [
      {
        "end": "\\\"",
        "start": "\\\""
      },
      {
        "end": "'",
        "start": "'"
      }
    ]
  }
}
```

## AsciiDoc

```json
{
  "AsciiDoc": {
    "complexitychecks": [],
    "extensions": [
      "adoc"
    ],
    "line_comment": [],
    "multi_line": [],
    "quotes": []
  }
}
```

## Assembly

```json
{
  "Assembly": {
    "complexitychecks": [
      "for ",
      "for(",
      "if ",
      "if(",
      "switch ",
      "while ",
      "else ",
      "|| ",
      "&& ",
      "!= ",
      "== "
    ],
    "extensions": [
      "s",
      "asm"
    ],
    "line_comment": [
      ";"
    ],
    "multi_line": [
      [
        "/*",
        "*/"
      ]
    ],
    "quotes": [
      {
        "end": "\\\"",
        "start": "\\\""
      },
      {
        "end": "'",
        "start": "'"
      }
    ]
  }
}
```

## Astro

```json
{
  "Astro": {
    "complexitychecks": [
      "for ",
      "for(",
      "if ",
      "if(",
      "switch ",
      "while ",
      "else ",
      "|| ",
      "&& ",
      "!= ",
      "== ",
      ".map"
    ],
    "extensions": [
      "astro"
    ],
    "line_comment": [
      "//"
    ],
    "multi_line": [
      [
        "<!--",
        "-->"
      ],
      [
        "/*",
        "*/"
      ]
    ],
    "quotes": [
      {
        "end": "\"",
        "start": "\""
      },
      {
        "end": "'",
        "start": "'"
      }
    ]
  }
}
```

## AutoHotKey

```json
{
  "AutoHotKey": {
    "complexitychecks": [
      "for ",
      "for(",
      "if ",
      "if(",
      "switch ",
      "while ",
      "else ",
      "|| ",
      "&& ",
      "!= ",
      "== "
    ],
    "extensions": [
      "ahk"
    ],
    "line_comment": [
      ";"
    ],
    "multi_line": [
      [
        "/*",
        "*/"
      ]
    ],
    "quotes": []
  }
}
```

## Autoconf

```json
{
  "Autoconf": {
    "complexitychecks": [
      "for ",
      "for(",
      "if ",
      "if(",
      "switch ",
      "while ",
      "else ",
      "|| ",
      "&& ",
      "!= ",
      "== "
    ],
    "extensions": [
      "in"
    ],
    "line_comment": [
      "#",
      "dnl"
    ],
    "multi_line": [],
    "quotes": []
  }
}
```

## Avro

```json
{
  "Avro": {
    "complexitychecks": [],
    "extensions": [
      "avdl",
      "avpr",
      "avsc"
    ],
    "line_comment": [],
    "multi_line": [],
    "quotes": []
  }
}
```

## BASH

```json
{
  "BASH": {
    "complexitychecks": [
      "for ",
      "for(",
      "if ",
      "if(",
      "switch ",
      "while ",
      "else ",
      "|| ",
      "&& ",
      "!= ",
      "== "
    ],
    "extensions": [
      "bash",
      "bash_login",
      "bash_logout",
      "bash_profile",
      "bashrc"
    ],
    "filenames": [
      ".bash_login",
      ".bash_logout",
      ".bash_profile",
      ".bashrc"
    ],
    "line_comment": [
      "#"
    ],
    "multi_line": [],
    "quotes": [
      {
        "end": "\\\"",
        "start": "\\\""
      },
      {
        "end": "'",
        "start": "'"
      }
    ],
    "shebangs": [
      "bash"
    ]
  }
}
```

## Basic

```json
{
  "Basic": {
    "complexitychecks": [
      "for ",
      "for(",
      "if ",
      "if(",
      "elseif ",
      "switch ",
      "while ",
      "else ",
      "|| ",
      "&& ",
      "!= ",
      "== "
    ],
    "extensions": [
      "bas"
    ],
    "line_comment": [
      "'"
    ],
    "multi_line": [],
    "quotes": [
      {
        "end": "\\\"",
        "start": "\\\""
      }
    ]
  }
}
```

## Batch

```json
{
  "Batch": {
    "complexitychecks": [
      "for ",
      "for(",
      "if ",
      "if(",
      "switch ",
      "while ",
      "else ",
      "|| ",
      "&& ",
      "!= ",
      "== "
    ],
    "extensions": [
      "bat",
      "btm",
      "cmd"
    ],
    "line_comment": [
      "REM",
      "::"
    ],
    "multi_line": [],
    "quotes": []
  }
}
```

## Bazel

```json
{
  "Bazel": {
    "complexitychecks": [
      "for ",
      "for(",
      "if ",
      "if(",
      "switch ",
      "while ",
      "else ",
      "|| ",
      "&& ",
      "!= ",
      "== "
    ],
    "extensions": [
      "bzl",
      "build.bazel",
      "build",
      "workspace"
    ],
    "line_comment": [
      "#"
    ],
    "multi_line": [],
    "quotes": [
      {
        "end": "\"",
        "start": "\""
      }
    ]
  }
}
```

## Bean

```json
{
  "Bean": {
    "complexitychecks": [],
    "extensions": [
      "bean",
      "beancount"
    ],
    "line_comment": [
      ";"
    ],
    "multi_line": [],
    "quotes": [
      {
        "end": "\"",
        "start": "\""
      }
    ]
  }
}
```

## Bicep

```json
{
  "Bicep": {
    "complexitychecks": [
      "@minLength(",
      "@maxLength(",
      "@secure(",
      "[for ",
      "if(",
      "if (",
      " == ",
      " != ",
      " ? ",
      "using ",
      "range(",
      "type ",
      "func "
    ],
    "extensions": [
      "bicep"
    ],
    "line_comment": [
      "//"
    ],
    "multi_line": [
      [
        "/*",
        "*/"
      ]
    ],
    "quotes": [
      {
        "end": "'",
        "start": "'"
      }
    ]
  }
}
```

## Bitbake

```json
{
  "Bitbake": {
    "complexitychecks": [
      "for ",
      "for(",
      "if ",
      "if(",
      "switch ",
      "while ",
      "else ",
      "|| ",
      "&& ",
      "!= ",
      "== "
    ],
    "extensions": [
      "bb",
      "bbappend",
      "bbclass"
    ],
    "line_comment": [
      "#"
    ],
    "multi_line": [],
    "quotes": [
      {
        "end": "\"",
        "start": "\""
      }
    ]
  }
}
```

## Bitbucket Pipeline

```json
{
  "Bitbucket Pipeline": {
    "complexitychecks": [],
    "extensions": [
      "bitbucket-pipelines.yml"
    ],
    "line_comment": [
      "#"
    ],
    "multi_line": [],
    "quotes": []
  }
}
```

## Blade template

```json
{
  "Blade template": {
    "complexitychecks": [
      "@for ",
      "@for(",
      "@foreach ",
      "@foreach(",
      "@forelse ",
      "@forelse(",
      "@each ",
      "@each (",
      "@while ",
      "@while(",
      "@if ",
      "@if(",
      "@unless ",
      "@unless(",
      "@isset ",
      "@isset(",
      "@empty ",
      "@empty(",
      "@else ",
      "@elseif ",
      "@elseif(",
      "@while ",
      "@while(",
      "@switch ",
      "@switch (",
      "|| ",
      "&& ",
      "!= ",
      "== "
    ],
    "extensions": [
      "blade.php"
    ],
    "line_comment": [],
    "multi_line": [
      [
        "{{--",
        "--}}"
      ],
      [
        "<!--",
        "-->"
      ]
    ],
    "quotes": []
  }
}
```

## Blueprint

```json
{
  "Blueprint": {
    "complexitychecks": [],
    "extensions": [
      "blp"
    ],
    "line_comment": [
      "//"
    ],
    "multi_line": [
      [
        "/*",
        "*/"
      ]
    ],
    "quotes": [
      {
        "end": "\"",
        "start": "\""
      }
    ]
  }
}
```

## Boo

```json
{
  "Boo": {
    "complexitychecks": [
      "for ",
      "if ",
      "elif ",
      "unless ",
      " and ",
      "for ",
      "while ",
      "else ",
      "|| ",
      "&& ",
      "!= ",
      "== "
    ],
    "extensions": [
      "boo"
    ],
    "line_comment": [
      "//"
    ],
    "multi_line": [
      [
        "/*",
        "*/"
      ]
    ],
    "quotes": [
      {
        "end": "\"",
        "start": "\""
      },
      {
        "end": "'",
        "start": "'"
      },
      {
        "end": "\"\"\"",
        "start": "\"\"\""
      }
    ]
  }
}
```

## Bosque

```json
{
  "Bosque": {
    "complexitychecks": [
      "if ",
      "if(",
      "switch ",
      "match ",
      "case ",
      "| ",
      "|| ",
      "& ",
      "&& ",
      "!= ",
      "!== ",
      "== ",
      "=== "
    ],
    "extensions": [
      "bsq"
    ],
    "line_comment": [
      "//"
    ],
    "multi_line": [],
    "quotes": [
      {
        "end": "\"",
        "start": "\""
      },
      {
        "end": "'",
        "start": "'"
      }
    ]
  }
}
```

## Brainfuck

```json
{
  "Brainfuck": {
    "complexitychecks": [
      "[",
      "]",
      "<",
      ">",
      "+",
      "-",
      ".",
      ","
    ],
    "extensions": [
      "bf"
    ],
    "line_comment": [],
    "multi_line": [],
    "quotes": []
  }
}
```

## BuildStream

```json
{
  "BuildStream": {
    "complexitychecks": [],
    "extensions": [
      "bst"
    ],
    "line_comment": [
      "#"
    ],
    "multi_line": [],
    "quotes": []
  }
}
```

## C

```json
{
  "C": {
    "complexitychecks": [
      "for ",
      "for(",
      "if ",
      "if(",
      "switch ",
      "switch(",
      "while ",
      "while(",
      "else ",
      "|| ",
      "&& ",
      "!= ",
      "== "
    ],
    "extensions": [
      "c",
      "ec",
      "pgc"
    ],
    "line_comment": [
      "//"
    ],
    "multi_line": [
      [
        "/*",
        "*/"
      ]
    ],
    "quotes": [
      {
        "end": "\"",
        "start": "\""
      }
    ]
  }
}
```

## C Header

```json
{
  "C Header": {
    "complexitychecks": [
      "for ",
      "for(",
      "if ",
      "if(",
      "switch ",
      "switch(",
      "case ",
      "while ",
      "while(",
      "else ",
      "|| ",
      "&& ",
      "!= ",
      "== "
    ],
    "extensions": [
      "h"
    ],
    "line_comment": [
      "//"
    ],
    "multi_line": [
      [
        "/*",
        "*/"
      ]
    ],
    "quotes": [
      {
        "end": "\"",
        "start": "\""
      }
    ]
  }
}
```

## C Shell

```json
{
  "C Shell": {
    "complexitychecks": [
      "for ",
      "for(",
      "if ",
      "if(",
      "switch ",
      "while ",
      "else ",
      "|| ",
      "&& ",
      "!= ",
      "== "
    ],
    "extensions": [
      "csh"
    ],
    "filenames": [
      ".cshrc"
    ],
    "line_comment": [
      "#"
    ],
    "multi_line": [],
    "quotes": [],
    "shebangs": [
      "csh",
      "tcsh"
    ]
  }
}
```

## C#

```json
{
  "C#": {
    "complexitychecks": [
      "for ",
      "for(",
      "if ",
      "if(",
      "foreach ",
      "foreach(",
      "switch ",
      "while ",
      "else ",
      "|| ",
      "&& ",
      "!= ",
      "== "
    ],
    "extensions": [
      "cs",
      "csx"
    ],
    "line_comment": [
      "//"
    ],
    "multi_line": [
      [
        "/*",
        "*/"
      ]
    ],
    "quotes": [
      {
        "end": "\"",
        "ignoreEscape": true,
        "start": "@\""
      },
      {
        "end": "\"",
        "start": "\""
      }
    ],
    "shebangs": [
      "dotnet"
    ]
  }
}
```

## C++

```json
{
  "C++": {
    "complexitychecks": [
      "for ",
      "for(",
      "if ",
      "if(",
      "switch ",
      "switch(",
      "while ",
      "while(",
      "else ",
      "|| ",
      "&& ",
      "!= ",
      "== "
    ],
    "extensions": [
      "cc",
      "cpp",
      "cxx",
      "c++",
      "pcc",
      "ino",
      "ccm",
      "cppm",
      "cxxm",
      "c++m",
      "mxx"
    ],
    "line_comment": [
      "//"
    ],
    "multi_line": [
      [
        "/*",
        "*/"
      ]
    ],
    "quotes": [
      {
        "end": "\"",
        "start": "\""
      }
    ]
  }
}
```

## C++ Header

```json
{
  "C++ Header": {
    "complexitychecks": [
      "for ",
      "for(",
      "if ",
      "if(",
      "switch ",
      "switch(",
      "while ",
      "while(",
      "else ",
      "|| ",
      "&& ",
      "!= ",
      "== "
    ],
    "extensions": [
      "hh",
      "hpp",
      "hxx",
      "inl",
      "ipp",
      "ixx"
    ],
    "line_comment": [
      "//"
    ],
    "multi_line": [
      [
        "/*",
        "*/"
      ]
    ],
    "quotes": [
      {
        "end": "\"",
        "start": "\""
      }
    ]
  }
}
```

## C3

```json
{
  "C3": {
    "complexitychecks": [
      "for ",
      "for(",
      "foreach ",
      "foreach(",
      "if ",
      "if(",
      "switch ",
      "switch(",
      "case ",
      "while ",
      "while(",
      "else ",
      "|| ",
      "&& ",
      "!= ",
      "== ",
      "defer ",
      "macro "
    ],
    "extensions": [
      "c3"
    ],
    "line_comment": [
      "//"
    ],
    "multi_line": [
      [
        "/*",
        "*/"
      ],
      [
        "<*",
        "*>"
      ]
    ],
    "quotes": [
      {
        "end": "\"",
        "start": "\""
      },
      {
        "end": "`",
        "ignoreEscape": true,
        "start": "`"
      }
    ]
  }
}
```

## CMake

```json
{
  "CMake": {
    "complexitychecks": [
      "foreach ",
      "foreach(",
      "if ",
      "if(",
      "elseif ",
      "elseif(",
      "while ",
      "while(",
      "else ",
      "else(",
      "OR ",
      "AND ",
      "EQUAL ",
      "STREQUAL ",
      "VERSION_EQUAL ",
      "PATH_EQUAL "
    ],
    "extensions": [
      "cmake",
      "cmakelists.txt"
    ],
    "line_comment": [
      "#"
    ],
    "multi_line": [
      [
        "#[[",
        "]]"
      ]
    ],
    "quotes": [
      {
        "end": "\"",
        "start": "\""
      }
    ]
  }
}
```

## COBOL

```json
{
  "COBOL": {
    "complexitychecks": [
      "for ",
      "for(",
      "if ",
      "if(",
      "switch ",
      "while ",
      "else ",
      "|| ",
      "&& ",
      "!= ",
      "== "
    ],
    "extensions": [
      "cob",
      "cbl",
      "ccp",
      "cobol",
      "cpy"
    ],
    "line_comment": [
      "*"
    ],
    "multi_line": [],
    "quotes": []
  }
}
```

## CSS

```json
{
  "CSS": {
    "complexitychecks": [
      "for ",
      "for(",
      "if ",
      "if(",
      "switch ",
      "while ",
      "else ",
      "|| ",
      "&& ",
      "!= ",
      "== "
    ],
    "extensions": [
      "css"
    ],
    "line_comment": [
      "//"
    ],
    "multi_line": [
      [
        "/*",
        "*/"
      ]
    ],
    "quotes": [
      {
        "end": "\"",
        "start": "\""
      }
    ]
  }
}
```

## CSV

```json
{
  "CSV": {
    "complexitychecks": [],
    "extensions": [
      "csv"
    ],
    "line_comment": [],
    "multi_line": [],
    "quotes": []
  }
}
```

## Cabal

```json
{
  "Cabal": {
    "complexitychecks": [
      "for ",
      "for(",
      "if ",
      "if(",
      "switch ",
      "while ",
      "else ",
      "|| ",
      "&& ",
      "!= ",
      "== "
    ],
    "extensions": [
      "cabal"
    ],
    "line_comment": [
      "--"
    ],
    "multi_line": [
      [
        "{-",
        "-}"
      ]
    ],
    "quotes": []
  }
}
```

## Cairo

```json
{
  "Cairo": {
    "complexitychecks": [
      "loop ",
      "if ",
      "if(",
      "match ",
      "match(",
      "else ",
      "|| ",
      "&& ",
      "!= ",
      "== "
    ],
    "extensions": [
      "cairo"
    ],
    "line_comment": [
      "//"
    ],
    "multi_line": [],
    "quotes": [
      {
        "end": "'",
        "start": "'"
      }
    ]
  }
}
```

## Cangjie

```json
{
  "Cangjie": {
    "complexitychecks": [
      "for ",
      "for(",
      "if ",
      "if(",
      "while ",
      "else ",
      "|| ",
      "&& ",
      "!= ",
      "== "
    ],
    "extensions": [
      "cj"
    ],
    "line_comment": [
      "//"
    ],
    "multi_line": [
      [
        "/*",
        "*/"
      ]
    ],
    "quotes": [
      {
        "end": "'",
        "start": "'"
      },
      {
        "end": "\"",
        "start": "\""
      },
      {
        "end": "\"\"\"",
        "start": "\"\"\""
      },
      {
        "end": "'''",
        "start": "'''"
      }
    ]
  }
}
```

## Cap'n Proto

```json
{
  "Cap'n Proto": {
    "complexitychecks": [],
    "extensions": [
      "capnp"
    ],
    "line_comment": [
      "#"
    ],
    "multi_line": [],
    "quotes": []
  }
}
```

## Cassius

```json
{
  "Cassius": {
    "complexitychecks": [
      "for ",
      "for(",
      "if ",
      "if(",
      "switch ",
      "while ",
      "else ",
      "|| ",
      "&& ",
      "!= ",
      "== "
    ],
    "extensions": [
      "cassius"
    ],
    "line_comment": [
      "//"
    ],
    "multi_line": [
      [
        "/*",
        "*/"
      ]
    ],
    "quotes": [
      {
        "end": "\"",
        "start": "\""
      }
    ]
  }
}
```

## Ceylon

```json
{
  "Ceylon": {
    "complexitychecks": [
      "for ",
      "for(",
      "if ",
      "if(",
      "switch ",
      "while ",
      "else ",
      "|| ",
      "&& ",
      "!= ",
      "== "
    ],
    "extensions": [
      "ceylon"
    ],
    "line_comment": [
      "//"
    ],
    "multi_line": [
      [
        "/*",
        "*/"
      ]
    ],
    "quotes": [
      {
        "end": "\"",
        "start": "\""
      }
    ]
  }
}
```

## Chapel

```json
{
  "Chapel": {
    "complexitychecks": [
      "for ",
      "if ",
      "switch ",
      "while ",
      "else ",
      "do ",
      "|| ",
      "&& ",
      "!= ",
      "== "
    ],
    "extensions": [
      "chpl"
    ],
    "line_comment": [
      "//"
    ],
    "multi_line": [
      [
        "/*",
        "*/"
      ]
    ],
    "quotes": [
      {
        "end": "\"",
        "start": "\""
      },
      {
        "end": "'",
        "start": "'"
      }
    ]
  }
}
```

## Circom

```json
{
  "Circom": {
    "complexitychecks": [
      "for ",
      "for(",
      "if ",
      "if(",
      "switch ",
      "while ",
      "while(",
      "else ",
      "else(",
      "|| ",
      "&& ",
      "!= ",
      "== "
    ],
    "extensions": [
      "circom"
    ],
    "line_comment": [
      "//"
    ],
    "multi_line": [
      [
        "/*",
        "*/"
      ]
    ],
    "quotes": []
  }
}
```

## Clipper

```json
{
  "Clipper": {
    "complexitychecks": [
      "for ",
      "for(",
      "if ",
      "if(",
      "do while ",
      "while ",
      "else ",
      "elseif ",
      "else(",
      "switch ",
      "case ",
      "otherwise ",
      "begin sequence ",
      "end sequence ",
      "begin sequence(",
      "try ",
      "catch ",
      "finally ",
      "|| ",
      "&& ",
      "!= ",
      "== "
    ],
    "extensions": [
      "prg",
      "ch"
    ],
    "line_comment": [
      "//",
      "&&"
    ],
    "multi_line": [
      [
        "/*",
        "*/"
      ]
    ],
    "quotes": [
      {
        "end": "\"",
        "start": "\""
      },
      {
        "end": "'",
        "start": "'"
      }
    ]
  }
}
```

## Clojure

```json
{
  "Clojure": {
    "complexitychecks": [
      "(for ",
      "(when ",
      "(loop ",
      "(doseq ",
      "(cond ",
      "(if",
      "(if-not ",
      "(and ",
      "(or ",
      "(not ",
      "(= ",
      "(not= ",
      "(recur "
    ],
    "extensions": [
      "clj",
      "cljc"
    ],
    "line_comment": [
      ";"
    ],
    "multi_line": [],
    "quotes": []
  }
}
```

## ClojureScript

```json
{
  "ClojureScript": {
    "complexitychecks": [
      "for ",
      "for(",
      "if ",
      "if(",
      "switch ",
      "while ",
      "else ",
      "|| ",
      "&& ",
      "!= ",
      "== "
    ],
    "extensions": [
      "cljs"
    ],
    "line_comment": [
      ";"
    ],
    "multi_line": [],
    "quotes": []
  }
}
```

## Closure Template

```json
{
  "Closure Template": {
    "complexitychecks": [
      "for ",
      "for(",
      "if ",
      "if(",
      "switch ",
      "while ",
      "else ",
      "|| ",
      "&& ",
      "!= ",
      "== ",
      ">= ",
      "<= ",
      "?: ",
      "? : "
    ],
    "extensions": [
      "soy"
    ],
    "line_comment": [
      "//"
    ],
    "multi_line": [
      [
        "/**",
        "*/"
      ],
      [
        "/*",
        "*/"
      ]
    ],
    "quotes": [
      {
        "end": "\"",
        "start": "\""
      }
    ]
  }
}
```

## CloudFormation (JSON)

```json
{
  "CloudFormation (JSON)": {
    "complexitychecks": [
      "!GetAtt",
      "!Sub",
      "!Select",
      "!Equals",
      "!If",
      "DependsOn:",
      "!Select",
      "!Equals",
      "!If",
      "Fn::If",
      "Fn::And",
      "Fn::Equals",
      "Fn::Not",
      "Fn::Or",
      "Fn::Base64",
      "Fn::Cidr",
      "Fn::FindInMap",
      "Fn::GetAtt",
      "Fn::GetAZs",
      "Fn::ImportValue",
      "Fn::Join",
      "Fn::Select",
      "Fn::Split",
      "Fn::Sub",
      "Fn::Transform"
    ],
    "extensions": [
      "json"
    ],
    "keywords": [
      "\"AWSTemplateFormatVersion\"",
      "AWS::",
      "!GetAtt",
      "!Sub",
      "\"DependsOn\"",
      "!Select",
      "!Equals",
      "!If",
      "Fn::If",
      "Fn::And",
      "Fn::Equals",
      "Fn::Not",
      "Fn::Or",
      "Fn::Base64",
      "Fn::Cidr",
      "Fn::FindInMap",
      "Fn::GetAtt",
      "Fn::GetAZs",
      "Fn::ImportValue",
      "Fn::Join",
      "Fn::Select",
      "Fn::Split",
      "Fn::Sub",
      "Fn::Transform"
    ],
    "line_comment": [],
    "multi_line": [],
    "quotes": []
  }
}
```

## CloudFormation (YAML)

```json
{
  "CloudFormation (YAML)": {
    "complexitychecks": [
      "!GetAtt",
      "!Sub",
      "!Select",
      "!Equals",
      "!If",
      "DependsOn:",
      "!Select",
      "!Equals",
      "!If",
      "Fn::If",
      "Fn::And",
      "Fn::Equals",
      "Fn::Not",
      "Fn::Or",
      "Fn::Base64",
      "Fn::Cidr",
      "Fn::FindInMap",
      "Fn::GetAtt",
      "Fn::GetAZs",
      "Fn::ImportValue",
      "Fn::Join",
      "Fn::Select",
      "Fn::Split",
      "Fn::Sub",
      "Fn::Transform"
    ],
    "extensions": [
      "yaml",
      "yml"
    ],
    "keywords": [
      "Resources:",
      "AWSTemplateFormatVersion:",
      "Description:",
      "AWS::",
      "Properties:",
      "Name:",
      "Type:",
      "!GetAtt",
      "!Sub",
      "Statement:",
      "Ref:",
      "DependsOn:",
      "!Select",
      "!Equals",
      "!If",
      "Fn::If",
      "Fn::And",
      "Fn::Equals",
      "Fn::Not",
      "Fn::Or",
      "Fn::Base64",
      "Fn::Cidr",
      "Fn::FindInMap",
      "Fn::GetAtt",
      "Fn::GetAZs",
      "Fn::ImportValue",
      "Fn::Join",
      "Fn::Select",
      "Fn::Split",
      "Fn::Sub",
      "Fn::Transform"
    ],
    "line_comment": [
      "#"
    ],
    "multi_line": [],
    "quotes": []
  }
}
```

## CodeQL

```json
{
  "CodeQL": {
    "complexitychecks": [
      "and ",
      "or ",
      "implies ",
      "if ",
      "else ",
      "not ",
      "instanceof ",
      "in ",
      "exists(",
      "forall( ",
      "avg(",
      "concat(",
      "count(",
      "max(",
      "min(",
      "rank(",
      "strictconcat(",
      "strictcount(",
      "strictsum(",
      "sum("
    ],
    "extensions": [
      "ql",
      "qll"
    ],
    "line_comment": [
      "//"
    ],
    "multi_line": [
      [
        "/*",
        "*/"
      ]
    ],
    "quotes": [
      {
        "end": "\"",
        "start": "\""
      }
    ]
  }
}
```

## CoffeeScript

```json
{
  "CoffeeScript": {
    "complexitychecks": [
      "for ",
      "for(",
      "if ",
      "if(",
      "switch ",
      "while ",
      "else ",
      "|| ",
      "&& ",
      "!= ",
      "== "
    ],
    "extensions": [
      "coffee"
    ],
    "line_comment": [
      "#"
    ],
    "multi_line": [
      [
        "###",
        "###"
      ]
    ],
    "quotes": [
      {
        "end": "\\\"",
        "start": "\\\""
      },
      {
        "end": "'",
        "start": "'"
      }
    ]
  }
}
```

## Cogent

```json
{
  "Cogent": {
    "complexitychecks": [
      "for ",
      "for(",
      "if ",
      "if(",
      "switch ",
      "while ",
      "else ",
      "|| ",
      "&& ",
      "!= ",
      "== "
    ],
    "extensions": [
      "cogent"
    ],
    "line_comment": [
      "--"
    ],
    "multi_line": [],
    "quotes": []
  }
}
```

## ColdFusion

```json
{
  "ColdFusion": {
    "complexitychecks": [
      "for ",
      "for(",
      "if ",
      "if(",
      "switch ",
      "while ",
      "else ",
      "|| ",
      "&& ",
      "!= ",
      "== "
    ],
    "extensions": [
      "cfm"
    ],
    "line_comment": [],
    "multi_line": [
      [
        "<!---",
        "--->"
      ]
    ],
    "quotes": [
      {
        "end": "\\\"",
        "start": "\\\""
      },
      {
        "end": "'",
        "start": "'"
      }
    ]
  }
}
```

## ColdFusion CFScript

```json
{
  "ColdFusion CFScript": {
    "complexitychecks": [
      "for ",
      "for(",
      "if ",
      "if(",
      "switch ",
      "while ",
      "else ",
      "|| ",
      "&& ",
      "!= ",
      "== "
    ],
    "extensions": [
      "cfc"
    ],
    "line_comment": [
      "//"
    ],
    "multi_line": [
      [
        "/*",
        "*/"
      ]
    ],
    "quotes": [
      {
        "end": "\"",
        "start": "\""
      }
    ]
  }
}
```

## Coq

```json
{
  "Coq": {
    "complexitychecks": [
      "for ",
      "for(",
      "if ",
      "if(",
      "switch ",
      "while ",
      "else ",
      "|| ",
      "&& ",
      "!= ",
      "== "
    ],
    "extensions": [
      "v"
    ],
    "keywords": [
      "Require",
      "Hypothesis",
      "Inductive",
      "Remark",
      "Lemma",
      "Proof",
      "Definition",
      "Theorem",
      "Class",
      "Instance",
      "Module",
      "Context",
      "Section",
      "Notation",
      "End",
      "Fixpoint",
      "From Coq"
    ],
    "line_comment": [],
    "multi_line": [
      [
        "(*",
        "*)"
      ]
    ],
    "quotes": [
      {
        "end": "\"",
        "start": "\""
      }
    ]
  }
}
```

## Creole

```json
{
  "Creole": {
    "complexitychecks": [],
    "extensions": [
      "creole"
    ],
    "line_comment": [],
    "multi_line": [],
    "quotes": []
  }
}
```

## Crystal

```json
{
  "Crystal": {
    "complexitychecks": [
      "for ",
      "for(",
      "if ",
      "if(",
      "switch ",
      "while ",
      "else ",
      "|| ",
      "&& ",
      "!= ",
      "== "
    ],
    "extensions": [
      "cr"
    ],
    "line_comment": [
      "#"
    ],
    "multi_line": [],
    "quotes": [
      {
        "end": "\\\"",
        "start": "\\\""
      },
      {
        "end": "'",
        "start": "'"
      }
    ]
  }
}
```

## Cuda

```json
{
  "Cuda": {
    "complexitychecks": [
      "for ",
      "for(",
      "if ",
      "if(",
      "switch ",
      "while ",
      "else ",
      "|| ",
      "&& ",
      "!= ",
      "== "
    ],
    "extensions": [
      "cu"
    ],
    "line_comment": [
      "//"
    ],
    "multi_line": [
      [
        "/*",
        "*/"
      ]
    ],
    "quotes": [
      {
        "end": "\"",
        "start": "\""
      }
    ]
  }
}
```

## Cython

```json
{
  "Cython": {
    "complexitychecks": [
      "for ",
      "for(",
      "if ",
      "if(",
      "switch ",
      "while ",
      "else ",
      "and ",
      "or ",
      "not ",
      "in "
    ],
    "extensions": [
      "pyx",
      "pxi",
      "pxd"
    ],
    "line_comment": [
      "#"
    ],
    "multi_line": [],
    "quotes": [
      {
        "end": "\\\"",
        "start": "\\\""
      },
      {
        "end": "'",
        "start": "'"
      },
      {
        "end": "\\\"\\\"\\\"",
        "start": "\\\"\\\"\\\""
      },
      {
        "end": "'''",
        "start": "'''"
      }
    ]
  }
}
```

## D

```json
{
  "D": {
    "complexitychecks": [
      "for ",
      "for(",
      "if ",
      "if(",
      "switch ",
      "while ",
      "else ",
      "|| ",
      "&& ",
      "!= ",
      "== "
    ],
    "extensions": [
      "d"
    ],
    "line_comment": [
      "//"
    ],
    "multi_line": [
      [
        "/*",
        "*/"
      ],
      [
        "/+",
        "+/"
      ]
    ],
    "nestedmultiline": true,
    "quotes": [
      {
        "end": "\"",
        "start": "\""
      },
      {
        "end": "'",
        "start": "'"
      }
    ],
    "shebangs": [
      "rdmd"
    ]
  }
}
```

## DAML

```json
{
  "DAML": {
    "complexitychecks": [
      "if ",
      "then ",
      "else ",
      "|| ",
      "&& ",
      "/= ",
      "== ",
      "case ",
      "do {",
      "forall "
    ],
    "extensions": [
      "daml"
    ],
    "line_comment": [
      "--"
    ],
    "multi_line": [
      [
        "{-",
        "-}"
      ]
    ],
    "quotes": []
  }
}
```

## DM

```json
{
  "DM": {
    "complexitychecks": [
      "for ",
      "for(",
      "if ",
      "if(",
      "switch ",
      "switch(",
      "while ",
      "while(",
      "else ",
      "||",
      "&&",
      "!=",
      "<>",
      "==",
      "in "
    ],
    "extensions": [
      "dm"
    ],
    "line_comment": [
      "//"
    ],
    "multi_line": [
      [
        "/*",
        "*/"
      ]
    ],
    "nestedmultiline": true,
    "quotes": [
      {
        "end": "\"",
        "start": "\""
      },
      {
        "end": "'",
        "start": "'"
      }
    ]
  }
}
```

## DOT

```json
{
  "DOT": {
    "complexitychecks": [],
    "extensions": [
      "dot",
      "gv"
    ],
    "line_comment": [
      "//",
      "#"
    ],
    "multi_line": [
      [
        "/*",
        "*/"
      ]
    ],
    "quotes": []
  }
}
```

## Dart

```json
{
  "Dart": {
    "complexitychecks": [
      "for ",
      "for(",
      "if ",
      "if(",
      "switch ",
      "while ",
      "else ",
      "|| ",
      "&& ",
      "!= ",
      "== "
    ],
    "extensions": [
      "dart"
    ],
    "line_comment": [
      "//"
    ],
    "multi_line": [
      [
        "/*",
        "*/"
      ]
    ],
    "quotes": [
      {
        "end": "\"",
        "start": "\""
      }
    ]
  }
}
```

## Device Tree

```json
{
  "Device Tree": {
    "complexitychecks": [
      "for ",
      "for(",
      "if ",
      "if(",
      "switch ",
      "while ",
      "else ",
      "|| ",
      "&& ",
      "!= ",
      "== "
    ],
    "extensions": [
      "dts",
      "dtsi"
    ],
    "line_comment": [
      "//"
    ],
    "multi_line": [
      [
        "/*",
        "*/"
      ]
    ],
    "quotes": [
      {
        "end": "\"",
        "start": "\""
      }
    ]
  }
}
```

## Dhall

```json
{
  "Dhall": {
    "complexitychecks": [],
    "extensions": [
      "dhall"
    ],
    "line_comment": [
      "--"
    ],
    "multi_line": [
      [
        "{-",
        "-}"
      ]
    ],
    "quotes": [
      {
        "end": "\"",
        "start": "\""
      }
    ]
  }
}
```

## Docker ignore

```json
{
  "Docker ignore": {
    "complexitychecks": [],
    "extensions": [],
    "filenames": [
      ".dockerignore"
    ],
    "line_comment": [
      "#",
      "//"
    ],
    "multi_line": [],
    "quotes": []
  }
}
```

## Dockerfile

```json
{
  "Dockerfile": {
    "complexitychecks": [
      "for ",
      "for(",
      "if ",
      "if(",
      "switch ",
      "while ",
      "else ",
      "|| ",
      "&& ",
      "!= ",
      "== "
    ],
    "extensions": [
      "dockerfile"
    ],
    "filenames": [
      "dockerfile"
    ],
    "line_comment": [
      "#"
    ],
    "multi_line": [],
    "quotes": [
      {
        "end": "\\\"",
        "start": "\\\""
      },
      {
        "end": "'",
        "start": "'"
      }
    ]
  }
}
```

## Document Type Definition

```json
{
  "Document Type Definition": {
    "complexitychecks": [],
    "extensions": [
      "dtd"
    ],
    "line_comment": [],
    "multi_line": [],
    "quotes": []
  }
}
```

## Elixir

```json
{
  "Elixir": {
    "complexitychecks": [
      "case ",
      "cond ",
      "if ",
      "for ",
      "with ",
      "try ",
      "catch ",
      "rescue ",
      "else ",
      "and ",
      "or ",
      "not ",
      "|| ",
      "&& ",
      "!= ",
      "== ",
      "|> "
    ],
    "extensions": [
      "ex",
      "exs"
    ],
    "line_comment": [
      "#"
    ],
    "multi_line": [],
    "quotes": [
      {
        "end": "\"\"\"",
        "start": "\"\"\""
      },
      {
        "end": "\"",
        "start": "\""
      },
      {
        "end": "'''",
        "start": "'''"
      },
      {
        "end": "'",
        "start": "'"
      }
    ]
  }
}
```

## Elixir Template

```json
{
  "Elixir Template": {
    "complexitychecks": [
      "case ",
      "cond ",
      "if ",
      "for ",
      "with ",
      "try ",
      "catch ",
      "rescue ",
      "else ",
      "and ",
      "or ",
      "not ",
      "|| ",
      "&& ",
      "!= ",
      "== ",
      "|> ",
      "<% "
    ],
    "extensions": [
      "eex"
    ],
    "line_comment": [
      "#"
    ],
    "multi_line": [
      [
        "<!--",
        "-->"
      ]
    ],
    "quotes": [
      {
        "end": "\"\"\"",
        "start": "\"\"\""
      },
      {
        "end": "\"",
        "start": "\""
      },
      {
        "end": "'''",
        "start": "'''"
      },
      {
        "end": "'",
        "start": "'"
      }
    ]
  }
}
```

## Elm

```json
{
  "Elm": {
    "complexitychecks": [
      "for ",
      "for(",
      "if ",
      "if(",
      "case ",
      "while ",
      "else ",
      "|| ",
      "&& ",
      "!= ",
      "== "
    ],
    "extensions": [
      "elm"
    ],
    "line_comment": [
      "--"
    ],
    "multi_line": [
      [
        "{-",
        "-}"
      ]
    ],
    "quotes": [
      {
        "end": "\"",
        "start": "\""
      }
    ]
  }
}
```

## Emacs Dev Env

```json
{
  "Emacs Dev Env": {
    "complexitychecks": [
      "for ",
      "for(",
      "if ",
      "if(",
      "switch ",
      "while ",
      "else ",
      "|| ",
      "&& ",
      "!= ",
      "== "
    ],
    "extensions": [
      "ede"
    ],
    "line_comment": [
      ";"
    ],
    "multi_line": [],
    "quotes": []
  }
}
```

## Emacs Lisp

```json
{
  "Emacs Lisp": {
    "complexitychecks": [
      "for ",
      "for(",
      "if ",
      "if(",
      "switch ",
      "while ",
      "else ",
      "|| ",
      "&& ",
      "!= ",
      "== "
    ],
    "extensions": [
      "el"
    ],
    "line_comment": [
      ";"
    ],
    "multi_line": [],
    "quotes": []
  }
}
```

## EmiT

```json
{
  "EmiT": {
    "complexitychecks": [
      "if ",
      "if(",
      "warp ",
      "time ",
      "kills ",
      "collapse ",
      "|| ",
      "&& ",
      "!= ",
      "== "
    ],
    "extensions": [
      "emit"
    ],
    "line_comment": [
      "//"
    ],
    "multi_line": [],
    "quotes": [
      {
        "end": "\"",
        "start": "\""
      }
    ]
  }
}
```

## Erlang

```json
{
  "Erlang": {
    "complexitychecks": [
      "for ",
      "for(",
      "if ",
      "if(",
      "switch ",
      "while ",
      "else ",
      "|| ",
      "&& ",
      "!= ",
      "== "
    ],
    "extensions": [
      "erl",
      "hrl"
    ],
    "line_comment": [
      "%"
    ],
    "multi_line": [],
    "quotes": [],
    "shebangs": [
      "escript"
    ]
  }
}
```

## Expect

```json
{
  "Expect": {
    "complexitychecks": [
      "for ",
      "for(",
      "if ",
      "if(",
      "switch ",
      "while ",
      "else ",
      "|| ",
      "&& ",
      "!= ",
      "== "
    ],
    "extensions": [
      "exp"
    ],
    "line_comment": [
      "#"
    ],
    "multi_line": [],
    "quotes": [
      {
        "end": "\\\"",
        "start": "\\\""
      },
      {
        "end": "'",
        "start": "'"
      }
    ]
  }
}
```

## Extensible Stylesheet Language Transformations

```json
{
  "Extensible Stylesheet Language Transformations": {
    "complexitychecks": [],
    "extensions": [
      "xslt",
      "xsl"
    ],
    "line_comment": [],
    "multi_line": [],
    "quotes": []
  }
}
```

## F#

```json
{
  "F#": {
    "complexitychecks": [
      "for ",
      "for(",
      "if ",
      "if(",
      "match ",
      "while ",
      "else ",
      "|| ",
      "&& ",
      "!= ",
      "== "
    ],
    "extensions": [
      "fs",
      "fsi",
      "fsx",
      "fsscript"
    ],
    "line_comment": [
      "//"
    ],
    "multi_line": [
      [
        "(*",
        "*)"
      ]
    ],
    "quotes": []
  }
}
```

## F*

```json
{
  "F*": {
    "complexitychecks": [
      "for ",
      "for(",
      "if ",
      "if(",
      "switch ",
      "while ",
      "else ",
      "|| ",
      "&& ",
      "!= ",
      "== "
    ],
    "extensions": [
      "fst"
    ],
    "line_comment": [],
    "multi_line": [
      [
        "(*",
        "*)"
      ]
    ],
    "quotes": [
      {
        "end": "\"",
        "start": "\""
      }
    ]
  }
}
```

## FIDL

```json
{
  "FIDL": {
    "complexitychecks": [
      "for ",
      "for(",
      "if ",
      "if(",
      "switch ",
      "while ",
      "else ",
      "|| ",
      "&& ",
      "!= ",
      "== "
    ],
    "extensions": [
      "fidl"
    ],
    "line_comment": [
      "//"
    ],
    "multi_line": [
      [
        "/*",
        "*/"
      ]
    ],
    "quotes": [
      {
        "end": "\"",
        "start": "\""
      }
    ]
  }
}
```

## FORTRAN Legacy

```json
{
  "FORTRAN Legacy": {
    "complexitychecks": [
      "for ",
      "for(",
      "if ",
      "if(",
      "switch ",
      "while ",
      "else ",
      "|| ",
      "&& ",
      "!= ",
      "== "
    ],
    "extensions": [
      "f",
      "for",
      "ftn",
      "f77",
      "pfo"
    ],
    "line_comment": [
      "c",
      "C",
      "!",
      "*"
    ],
    "multi_line": [],
    "quotes": [
      {
        "end": "\\\"",
        "start": "\\\""
      },
      {
        "end": "'",
        "start": "'"
      }
    ]
  }
}
```

## FSL

```json
{
  "FSL": {
    "complexitychecks": [
      "->",
      "<-"
    ],
    "extensions": [
      "fsl"
    ],
    "line_comment": [
      "//"
    ],
    "multi_line": [],
    "quotes": []
  }
}
```

## FXML

```json
{
  "FXML": {
    "extensions": [
      "fxml"
    ],
    "line_comment": [],
    "multi_line": [
      [
        "<!--",
        "-->"
      ]
    ],
    "quotes": [
      {
        "end": "\"",
        "start": "\""
      }
    ]
  }
}
```

## Factor

```json
{
  "Factor": {
    "complexitychecks": [
      "if",
      "when",
      "unless",
      "if*",
      "when*",
      "unless*",
      "?if",
      "?",
      "cond",
      "case",
      "cond>quot",
      "case>quot",
      "alist>quot",
      "while",
      "until",
      "loop",
      "0&&",
      "1&&",
      "2&&",
      "3&&",
      "n&&",
      "&&",
      "0||",
      "1||",
      "2||",
      "3||",
      "n||",
      "||",
      "and",
      "or",
      "xor",
      "eq",
      "=",
      "smart-if",
      "smart-if*",
      "smart-when",
      "smart-when*",
      "smart-unless",
      "smart-unless*"
    ],
    "extensions": [
      "factor"
    ],
    "line_comment": [
      "!"
    ],
    "multi_line": [
      [
        "![[",
        "]]"
      ],
      [
        "![=[",
        "]=]"
      ],
      [
        "![==[",
        "]==]"
      ],
      [
        "![===[",
        "]===]"
      ],
      [
        "![====[",
        "]====]"
      ],
      [
        "![=====[",
        "]=====]"
      ],
      [
        "![======[",
        "]======]"
      ],
      [
        "/*",
        "*/"
      ],
      [
        "((",
        "))"
      ]
    ],
    "quotes": [
      {
        "end": "\"",
        "start": "\""
      },
      {
        "end": ";",
        "start": "STRING:"
      },
      {
        "end": "]======]",
        "start": "[======["
      },
      {
        "end": "]====]",
        "start": "[=====["
      },
      {
        "end": "]====]",
        "start": "[====["
      },
      {
        "end": "]===]",
        "start": "[===["
      },
      {
        "end": "]==]",
        "start": "[==["
      },
      {
        "end": "]=]",
        "start": "[=["
      },
      {
        "end": "]]",
        "start": "[["
      }
    ]
  }
}
```

## Fennel

```json
{
  "Fennel": {
    "complexitychecks": [
      "(for",
      "(each",
      "(if",
      "(when",
      "(while",
      "(switch",
      "(do",
      "(..",
      "(=",
      "(and",
      "(or"
    ],
    "extensions": [
      "fnl"
    ],
    "line_comment": [
      ";"
    ],
    "multi_line": [],
    "quotes": [
      {
        "end": "\"",
        "start": "\""
      },
      {
        "end": "'",
        "start": ","
      }
    ]
  }
}
```

## Fish

```json
{
  "Fish": {
    "complexitychecks": [
      "for ",
      "for(",
      "if ",
      "if(",
      "switch ",
      "while ",
      "else ",
      "|| ",
      "&& ",
      "!= ",
      "== "
    ],
    "extensions": [
      "fish"
    ],
    "line_comment": [
      "#"
    ],
    "multi_line": [],
    "quotes": [
      {
        "end": "\\\"",
        "start": "\\\""
      },
      {
        "end": "'",
        "start": "'"
      }
    ],
    "shebangs": [
      "fish"
    ]
  }
}
```

## Flow9

```json
{
  "Flow9": {
    "complexitychecks": [
      "if ",
      "if(",
      "else ",
      "else{",
      "fori ",
      "fori(",
      "switch ",
      "switch(",
      "fold ",
      "fold(",
      "|| ",
      "&& ",
      "!= ",
      "== ",
      "|> "
    ],
    "extensions": [
      "flow"
    ],
    "line_comment": [
      "//"
    ],
    "multi_line": [
      [
        "/*",
        "*/"
      ]
    ],
    "quotes": [
      {
        "end": "\"",
        "start": "\""
      }
    ]
  }
}
```

## Forth

```json
{
  "Forth": {
    "complexitychecks": [
      "for ",
      "for(",
      "if ",
      "if(",
      "switch ",
      "while ",
      "else ",
      "|| ",
      "&& ",
      "!= ",
      "== "
    ],
    "extensions": [
      "4th",
      "forth",
      "fr",
      "frt",
      "fth",
      "f83",
      "fb",
      "fpm",
      "e4",
      "rx",
      "ft"
    ],
    "line_comment": [
      "\\\\"
    ],
    "multi_line": [
      [
        "( ",
        ")"
      ]
    ],
    "quotes": []
  }
}
```

## Fortran Modern

```json
{
  "Fortran Modern": {
    "complexitychecks": [
      "for ",
      "for(",
      "if ",
      "if(",
      "switch ",
      "while ",
      "else ",
      "|| ",
      "&& ",
      "!= ",
      "== "
    ],
    "extensions": [
      "f03",
      "f08",
      "f90",
      "f95"
    ],
    "line_comment": [
      "!"
    ],
    "multi_line": [],
    "quotes": [
      {
        "end": "\\\"",
        "start": "\\\""
      }
    ]
  }
}
```

## Fragment Shader File

```json
{
  "Fragment Shader File": {
    "complexitychecks": [
      "for ",
      "for(",
      "if ",
      "if(",
      "switch ",
      "while ",
      "else ",
      "|| ",
      "&& ",
      "!= ",
      "== "
    ],
    "extensions": [
      "fsh"
    ],
    "line_comment": [
      "//"
    ],
    "multi_line": [
      [
        "/*",
        "*/"
      ]
    ],
    "quotes": [
      {
        "end": "\"",
        "start": "\""
      }
    ]
  }
}
```

## Freemarker Template

```json
{
  "Freemarker Template": {
    "complexitychecks": [
      "<#list ",
      "<#assign ",
      "<#if ",
      "<#elseif ",
      "<#else>",
      "<#else> ",
      "<#switch  ",
      "<#case ",
      "<#default>",
      "<#default> ",
      "!= ",
      "== "
    ],
    "extensions": [
      "ftl"
    ],
    "line_comment": [],
    "multi_line": [
      [
        "<#--",
        "-->"
      ]
    ],
    "quotes": []
  }
}
```

## Futhark

```json
{
  "Futhark": {
    "complexitychecks": [
      "if ",
      "else ",
      "then ",
      "for ",
      "loop ",
      "while ",
      "|| ",
      "&& ",
      "!= ",
      ">= ",
      "<= "
    ],
    "extensions": [
      "fut"
    ],
    "line_comment": [
      "--"
    ],
    "multi_line": [],
    "quotes": []
  }
}
```

## GDScript

```json
{
  "GDScript": {
    "complexitychecks": [
      "for ",
      "for(",
      "if ",
      "if(",
      "switch ",
      "while ",
      "else ",
      "|| ",
      "&& ",
      "!= ",
      "== "
    ],
    "extensions": [
      "gd"
    ],
    "line_comment": [
      "#"
    ],
    "multi_line": [],
    "quotes": [
      {
        "end": "\"",
        "start": "\""
      },
      {
        "end": "'",
        "start": "'"
      },
      {
        "end": "\"\"\"",
        "start": "\"\"\""
      }
    ]
  }
}
```

## GLSL

```json
{
  "GLSL": {
    "complexitychecks": [
      "for ",
      "for(",
      "if ",
      "if(",
      "switch ",
      "while ",
      "else ",
      "|| ",
      "&& ",
      "!= ",
      "== "
    ],
    "extensions": [
      "vert",
      "tesc",
      "tese",
      "geom",
      "frag",
      "comp",
      "glsl"
    ],
    "line_comment": [
      "//"
    ],
    "multi_line": [
      [
        "/*",
        "*/"
      ]
    ],
    "quotes": [
      {
        "end": "\"",
        "start": "\""
      }
    ]
  }
}
```

## GN

```json
{
  "GN": {
    "complexitychecks": [
      "if(",
      "if (",
      "else if(",
      "else if (",
      "else(",
      "else (",
      "|| ",
      "&& ",
      "!= ",
      "== "
    ],
    "extensions": [
      "gn",
      "gni"
    ],
    "line_comment": [
      "#"
    ],
    "multi_line": [],
    "quotes": [
      {
        "end": "\"",
        "start": "\""
      }
    ]
  }
}
```

## Game Maker Language

```json
{
  "Game Maker Language": {
    "complexitychecks": [
      "for ",
      "for(",
      "if ",
      "if(",
      "switch ",
      "while ",
      "else ",
      "repeat ",
      "repeat(",
      "|| ",
      "or ",
      "&& ",
      "and ",
      "!= ",
      "== "
    ],
    "extensions": [
      "gml"
    ],
    "line_comment": [
      "//",
      "///"
    ],
    "multi_line": [
      [
        "/*",
        "*/"
      ]
    ],
    "quotes": [
      {
        "end": "\"",
        "start": "\""
      }
    ]
  }
}
```

## Game Maker Project

```json
{
  "Game Maker Project": {
    "complexitychecks": [],
    "extensions": [
      "yyp"
    ],
    "line_comment": [],
    "multi_line": [],
    "quotes": []
  }
}
```

## Gemfile

```json
{
  "Gemfile": {
    "complexitychecks": [],
    "extensions": [],
    "filenames": [
      "gemfile"
    ],
    "line_comment": [
      "#"
    ],
    "multi_line": [],
    "quotes": [
      {
        "end": "\\\"",
        "start": "\\\""
      },
      {
        "end": "'",
        "start": "'"
      }
    ]
  }
}
```

## Gherkin Specification

```json
{
  "Gherkin Specification": {
    "complexitychecks": [
      "given",
      "when",
      "then",
      "and"
    ],
    "extensions": [
      "feature"
    ],
    "line_comment": [
      "#"
    ],
    "multi_line": [],
    "quotes": []
  }
}
```

## Gleam

```json
{
  "Gleam": {
    "complexitychecks": [
      "fn ",
      "case ",
      "-> ",
      "if "
    ],
    "extensions": [
      "gleam"
    ],
    "line_comment": [
      "//",
      "///",
      "////"
    ],
    "multi_line": [],
    "quotes": [
      {
        "end": "\"",
        "start": "\""
      }
    ]
  }
}
```

## Go

```json
{
  "Go": {
    "complexitychecks": [
      "go ",
      "for ",
      "for(",
      "if ",
      "if(",
      "switch ",
      "select ",
      "else ",
      "|| ",
      "&& ",
      "!= ",
      "== "
    ],
    "extensions": [
      "go"
    ],
    "line_comment": [
      "//"
    ],
    "multi_line": [
      [
        "/*",
        "*/"
      ]
    ],
    "quotes": [
      {
        "end": "\"",
        "start": "\""
      },
      {
        "end": "`",
        "ignoreEscape": true,
        "start": "`"
      }
    ]
  }
}
```

## Go Template

```json
{
  "Go Template": {
    "complexitychecks": [
      "{{if ",
      "{{ if ",
      "{{else",
      "{{ else",
      "{{range ",
      "{{ range ",
      "{{with",
      "{{ with"
    ],
    "extensions": [
      "tmpl",
      "gohtml",
      "gotxt"
    ],
    "line_comment": [],
    "multi_line": [
      [
        "{{/*",
        "*/}}"
      ]
    ],
    "quotes": []
  }
}
```

## Go+

```json
{
  "Go+": {
    "complexitychecks": [
      "go ",
      "for ",
      "for(",
      "if ",
      "if(",
      "switch ",
      "select ",
      "else ",
      "|| ",
      "&& ",
      "!= ",
      "== ",
      "?:"
    ],
    "extensions": [
      "gop"
    ],
    "line_comment": [
      "//",
      "#"
    ],
    "multi_line": [
      [
        "/*",
        "*/"
      ]
    ],
    "quotes": [
      {
        "end": "\"",
        "start": "\""
      },
      {
        "end": "`",
        "ignoreEscape": true,
        "start": "`"
      }
    ],
    "shebangs": [
      "gop"
    ]
  }
}
```

## Godot Scene

```json
{
  "Godot Scene": {
    "complexitychecks": [],
    "extensions": [
      "tscn"
    ],
    "line_comment": [],
    "multi_line": [],
    "quotes": []
  }
}
```

## Gradle

```json
{
  "Gradle": {
    "complexitychecks": [],
    "extensions": [
      "gradle"
    ],
    "line_comment": [
      "//"
    ],
    "multi_line": [],
    "quotes": [
      {
        "end": "'",
        "start": "'"
      },
      {
        "end": "\"",
        "start": "\""
      }
    ]
  }
}
```

## GraphQL

```json
{
  "GraphQL": {
    "complexitychecks": [
      "type ",
      "input ",
      "query ",
      "mutation ",
      "subscription ",
      "directive ",
      "scalar ",
      "enum ",
      "interface ",
      "union ",
      "fragment "
    ],
    "extensions": [
      "graphql"
    ],
    "line_comment": [
      "#"
    ],
    "multi_line": [
      [
        "\"\"\"",
        "\"\"\""
      ]
    ],
    "quotes": [
      {
        "end": "\"",
        "start": "\""
      },
      {
        "docString": true,
        "end": "\"\"\"",
        "start": "\"\"\""
      }
    ]
  }
}
```

## Groovy

```json
{
  "Groovy": {
    "complexitychecks": [
      "for ",
      "for(",
      "if ",
      "if(",
      "switch ",
      "while ",
      "else ",
      "|| ",
      "&& ",
      "!= ",
      "== "
    ],
    "extensions": [
      "groovy",
      "grt",
      "gtpl",
      "gvy"
    ],
    "line_comment": [
      "//"
    ],
    "multi_line": [
      [
        "/*",
        "*/"
      ]
    ],
    "quotes": [
      {
        "end": "\"",
        "start": "\""
      }
    ]
  }
}
```

## Gwion

```json
{
  "Gwion": {
    "complexitychecks": [
      "fun ",
      "while(",
      "while (",
      "repeat(",
      "repeat (",
      "if (",
      "if("
    ],
    "extensions": [
      "gw"
    ],
    "line_comment": [
      "#!"
    ],
    "multi_line": [],
    "quotes": [
      {
        "end": "\"",
        "start": "\""
      }
    ]
  }
}
```

## HAML

```json
{
  "HAML": {
    "extensions": [
      "haml"
    ],
    "line_comment": [
      "-#"
    ],
    "multi_line": [],
    "quotes": []
  }
}
```

## HCL

```json
{
  "HCL": {
    "complexitychecks": [
      "for_each ",
      "for ",
      "count ",
      "coalesce(",
      "== ",
      "!= ",
      "> ",
      "< ",
      "&& ",
      "|| "
    ],
    "extensions": [
      "hcl"
    ],
    "line_comment": [
      "#"
    ],
    "multi_line": [
      [
        "/*",
        "*/"
      ]
    ],
    "quotes": [
      {
        "end": "\"",
        "start": "\""
      }
    ]
  }
}
```

## HEEx

```json
{
  "HEEx": {
    "complexitychecks": [
      "case ",
      "cond ",
      "if ",
      "for ",
      "with ",
      "try ",
      "catch ",
      "rescue ",
      "else ",
      "and ",
      "or ",
      "not ",
      "!= ",
      "== ",
      "|| ",
      "&& ",
      "|> "
    ],
    "extensions": [
      "heex"
    ],
    "line_comment": [],
    "multi_line": [
      [
        "<%!--",
        "--%>"
      ]
    ],
    "quotes": [
      {
        "end": "\"",
        "start": "\""
      }
    ]
  }
}
```

## HEX

```json
{
  "HEX": {
    "complexitychecks": [],
    "extensions": [
      "hex"
    ],
    "line_comment": [],
    "multi_line": [],
    "quotes": []
  }
}
```

## HTML

```json
{
  "HTML": {
    "extensions": [
      "html",
      "htm"
    ],
    "line_comment": [],
    "multi_line": [
      [
        "<!--",
        "-->"
      ]
    ],
    "quotes": [
      {
        "end": "\"",
        "start": "\""
      }
    ]
  }
}
```

## Hamlet

```json
{
  "Hamlet": {
    "complexitychecks": [
      "for ",
      "for(",
      "if ",
      "if(",
      "switch ",
      "while ",
      "else ",
      "|| ",
      "&& ",
      "!= ",
      "== "
    ],
    "extensions": [
      "hamlet"
    ],
    "line_comment": [],
    "multi_line": [
      [
        "<!--",
        "-->"
      ]
    ],
    "quotes": [
      {
        "end": "\"",
        "start": "\""
      }
    ]
  }
}
```

## Handlebars

```json
{
  "Handlebars": {
    "complexitychecks": [
      "for ",
      "for(",
      "if ",
      "if(",
      "switch ",
      "while ",
      "else ",
      "|| ",
      "&& ",
      "!= ",
      "== "
    ],
    "extensions": [
      "hbs",
      "handlebars"
    ],
    "line_comment": [],
    "multi_line": [
      [
        "<!--",
        "-->"
      ],
      [
        "{{!",
        "}}"
      ]
    ],
    "quotes": [
      {
        "end": "\\\"",
        "start": "\\\""
      },
      {
        "end": "'",
        "start": "'"
      }
    ]
  }
}
```

## Happy

```json
{
  "Happy": {
    "complexitychecks": [],
    "extensions": [
      "y",
      "ly"
    ],
    "line_comment": [],
    "multi_line": [],
    "quotes": []
  }
}
```

## Hare

```json
{
  "Hare": {
    "complexitychecks": [
      "for ",
      "if ",
      "else ",
      "match ",
      "switch ",
      "|| ",
      "&& ",
      "!= ",
      "== "
    ],
    "extensions": [
      "ha"
    ],
    "line_comment": [
      "//"
    ],
    "quotes": [
      {
        "end": "\"",
        "start": "\""
      },
      {
        "end": "`",
        "start": "`"
      }
    ]
  }
}
```

## Haskell

```json
{
  "Haskell": {
    "complexitychecks": [
      "if ",
      "then ",
      "else ",
      "|| ",
      "&& ",
      "/= ",
      "== ",
      "case ",
      "do {",
      "forall "
    ],
    "extensions": [
      "hs"
    ],
    "line_comment": [
      "--"
    ],
    "multi_line": [
      [
        "{-",
        "-}"
      ]
    ],
    "quotes": []
  }
}
```

## Haxe

```json
{
  "Haxe": {
    "complexitychecks": [
      "for ",
      "for(",
      "if ",
      "if(",
      "switch ",
      "while ",
      "else ",
      "|| ",
      "&& ",
      "!= ",
      "== "
    ],
    "extensions": [
      "hx"
    ],
    "line_comment": [
      "//"
    ],
    "multi_line": [
      [
        "/*",
        "*/"
      ]
    ],
    "quotes": [
      {
        "end": "\"",
        "start": "\""
      }
    ]
  }
}
```

## IDL

```json
{
  "IDL": {
    "complexitychecks": [
      "for ",
      "for(",
      "if ",
      "if(",
      "switch ",
      "while ",
      "else ",
      "|| ",
      "&& ",
      "!= ",
      "== "
    ],
    "extensions": [
      "idl",
      "webidl",
      "widl"
    ],
    "line_comment": [
      "//"
    ],
    "multi_line": [
      [
        "/*",
        "*/"
      ]
    ],
    "quotes": [
      {
        "end": "\"",
        "start": "\""
      }
    ]
  }
}
```

## INI

```json
{
  "INI": {
    "extensions": [
      "ini"
    ],
    "line_comment": [
      "#",
      ";"
    ],
    "multi_line": [],
    "quotes": []
  }
}
```

## Idris

```json
{
  "Idris": {
    "complexitychecks": [
      "for ",
      "for(",
      "if ",
      "if(",
      "switch ",
      "while ",
      "else ",
      "|| ",
      "&& ",
      "!= ",
      "== "
    ],
    "extensions": [
      "idr",
      "lidr"
    ],
    "line_comment": [
      "--"
    ],
    "multi_line": [
      [
        "{-",
        "-}"
      ]
    ],
    "nestedmultiline": true,
    "quotes": [
      {
        "end": "\\\"",
        "start": "\\\""
      },
      {
        "end": "\\\"\\\"\\\"",
        "start": "\\\"\\\"\\\""
      }
    ]
  }
}
```

## Intel HEX

```json
{
  "Intel HEX": {
    "complexitychecks": [],
    "extensions": [
      "ihex"
    ],
    "line_comment": [],
    "multi_line": [],
    "quotes": []
  }
}
```

## Isabelle

```json
{
  "Isabelle": {
    "complexitychecks": [
      "for ",
      "for(",
      "if ",
      "if(",
      "switch ",
      "while ",
      "else ",
      "|| ",
      "&& ",
      "!= ",
      "== "
    ],
    "extensions": [
      "thy"
    ],
    "line_comment": [
      "--"
    ],
    "multi_line": [
      [
        "{*",
        "*}"
      ],
      [
        "(*",
        "*)"
      ],
      [
        "\u2039",
        "\u203a"
      ],
      [
        "\\\\<open>",
        "\\\\<close>"
      ]
    ],
    "quotes": [
      {
        "end": "''",
        "start": "''"
      }
    ]
  }
}
```

## JAI

```json
{
  "JAI": {
    "complexitychecks": [
      "for ",
      "for(",
      "if ",
      "if(",
      "switch ",
      "while ",
      "else ",
      "|| ",
      "&& ",
      "!= ",
      "== "
    ],
    "extensions": [
      "jai"
    ],
    "line_comment": [
      "//"
    ],
    "multi_line": [
      [
        "/*",
        "*/"
      ]
    ],
    "nestedmultiline": true,
    "quotes": [
      {
        "end": "\"",
        "start": "\""
      }
    ]
  }
}
```

## JCL

```json
{
  "JCL": {
    "complexitychecks": [
      " IF",
      " THEN",
      " ELSE",
      " PROC=",
      " PGM=",
      " DD ",
      " EXEC ",
      " JOB ",
      " COND=",
      " INCLUDE",
      " PEND"
    ],
    "extensions": [
      "jcl",
      "jcls"
    ],
    "line_comment": [
      "//*"
    ],
    "quotes": [
      {
        "start": "'",
        "end": "'"
      }
    ]
  }
}
```

## JSON

```json
{
  "JSON": {
    "complexitychecks": [],
    "extensions": [
      "json"
    ],
    "line_comment": [],
    "multi_line": [],
    "quotes": []
  }
}
```

## JSON5

```json
{
  "JSON5": {
    "complexitychecks": [],
    "extensions": [
      "json5"
    ],
    "line_comment": [
      "//"
    ],
    "multi_line": [],
    "quotes": []
  }
}
```

## JSONC

```json
{
  "JSONC": {
    "complexitychecks": [],
    "extensions": [
      "jsonc"
    ],
    "line_comment": [
      "//"
    ],
    "multi_line": [
      [
        "/*",
        "*/"
      ]
    ],
    "quotes": [
      {
        "end": "\"",
        "start": "\""
      }
    ]
  }
}
```

## JSONL

```json
{
  "JSONL": {
    "complexitychecks": [],
    "extensions": [
      "jsonl"
    ],
    "line_comment": [],
    "multi_line": [],
    "quotes": []
  }
}
```

## JSX

```json
{
  "JSX": {
    "complexitychecks": [
      "for ",
      "for(",
      "if ",
      "if(",
      "switch ",
      "while ",
      "else ",
      "|| ",
      "&& ",
      "!= ",
      "== "
    ],
    "extensions": [
      "jsx"
    ],
    "line_comment": [
      "//"
    ],
    "multi_line": [
      [
        "/*",
        "*/"
      ]
    ],
    "quotes": [
      {
        "end": "\"",
        "start": "\""
      }
    ]
  }
}
```

## Jade

```json
{
  "Jade": {
    "complexitychecks": [
      "if ",
      "else if ",
      "unless "
    ],
    "extensions": [
      "jade"
    ],
    "line_comment": [
      "//-"
    ],
    "multi_line": [],
    "quotes": []
  }
}
```

## Janet

```json
{
  "Janet": {
    "complexitychecks": [
      "(if ",
      "(for ",
      "(for ",
      "(cond ",
      "(switch ",
      "(when ",
      "(while ",
      "(loop ",
      "(case "
    ],
    "extensions": [
      "janet"
    ],
    "line_comment": [
      "#"
    ],
    "multi_line": [],
    "nestedmultiline": false,
    "quotes": [
      {
        "end": "\"",
        "start": "\""
      },
      {
        "end": "``",
        "start": "``"
      },
      {
        "end": "\"",
        "start": "@\""
      }
    ]
  }
}
```

## Java

```json
{
  "Java": {
    "complexitychecks": [
      "for ",
      "for(",
      "if ",
      "if(",
      "switch ",
      "while ",
      "else ",
      "|| ",
      "&& ",
      "!= ",
      "== "
    ],
    "extensions": [
      "java"
    ],
    "line_comment": [
      "//"
    ],
    "multi_line": [
      [
        "/*",
        "*/"
      ]
    ],
    "quotes": [
      {
        "end": "\"",
        "start": "\""
      }
    ]
  }
}
```

## JavaScript

```json
{
  "JavaScript": {
    "complexitychecks": [
      "for ",
      "for(",
      "if ",
      "if(",
      "switch ",
      "while ",
      "else ",
      "|| ",
      "&& ",
      "!= ",
      "== ",
      "?.",
      "?? ",
      "??= "
    ],
    "extensions": [
      "js",
      "cjs",
      "mjs"
    ],
    "line_comment": [
      "//"
    ],
    "multi_line": [
      [
        "/*",
        "*/"
      ]
    ],
    "quotes": [
      {
        "end": "\"",
        "start": "\""
      },
      {
        "end": "'",
        "start": "'"
      },
      {
        "end": "`",
        "start": "`"
      }
    ],
    "shebangs": [
      "node"
    ]
  }
}
```

## JavaServer Pages

```json
{
  "JavaServer Pages": {
    "complexitychecks": [
      "for ",
      "for(",
      "if ",
      "if(",
      "switch ",
      "while ",
      "else ",
      "|| ",
      "&& ",
      "!= ",
      "== "
    ],
    "extensions": [
      "jsp"
    ],
    "line_comment": [
      "//"
    ],
    "multi_line": [
      [
        "/*",
        "*/"
      ]
    ],
    "quotes": [
      {
        "end": "\"",
        "start": "\""
      },
      {
        "end": "'",
        "start": "'"
      }
    ]
  }
}
```

## Jenkins Buildfile

```json
{
  "Jenkins Buildfile": {
    "complexitychecks": [],
    "extensions": [
      "jenkinsfile"
    ],
    "line_comment": [],
    "multi_line": [],
    "quotes": []
  }
}
```

## Jinja

```json
{
  "Jinja": {
    "complexitychecks": [
      "{% for ",
      "{%- for ",
      "{% if ",
      "{%- if ",
      "{% else ",
      "{%- else ",
      "{% elif ",
      "{% macro ",
      "{%- macro ",
      "{% call ",
      "{%- call ",
      "{% filter ",
      "{%- filter ",
      "{% set ",
      "{% include ",
      "{% from ",
      "{% extends ",
      "{% with "
    ],
    "extensions": [
      "jinja",
      "j2",
      "jinja2"
    ],
    "line_comment": [],
    "multi_line": [
      [
        "{#",
        "#}"
      ]
    ],
    "quotes": []
  }
}
```

## Jsonnet

```json
{
  "Jsonnet": {
    "complexitychecks": [
      "for",
      "if",
      "else",
      "||",
      "&&",
      "!=",
      "=="
    ],
    "extensions": [
      "jsonnet",
      "libsonnet"
    ],
    "line_comment": [
      "#",
      "//"
    ],
    "multi_line": [
      [
        "/*",
        "*/"
      ]
    ],
    "quotes": [
      {
        "end": "\"",
        "start": "\""
      },
      {
        "end": "'",
        "start": "'"
      },
      {
        "end": "|||",
        "start": "|||"
      },
      {
        "end": "\"",
        "start": "@\""
      },
      {
        "end": "'",
        "start": "@'"
      }
    ],
    "shebangs": [
      "jsonnet"
    ]
  }
}
```

## Julia

```json
{
  "Julia": {
    "complexitychecks": [
      "for ",
      "for(",
      "if ",
      "if(",
      "while ",
      "else ",
      "elseif ",
      "elseif(",
      "try ",
      "catch ",
      "finally ",
      "|| ",
      "&& "
    ],
    "extensions": [
      "jl"
    ],
    "line_comment": [
      "#"
    ],
    "multi_line": [
      [
        "#=",
        "=#"
      ]
    ],
    "nestedmultiline": true,
    "quotes": [
      {
        "end": "\\\"",
        "start": "\\\""
      },
      {
        "end": "\\\"\\\"\\\"",
        "start": "\\\"\\\"\\\""
      }
    ]
  }
}
```

## Julius

```json
{
  "Julius": {
    "complexitychecks": [
      "for ",
      "for(",
      "if ",
      "if(",
      "switch ",
      "while ",
      "else ",
      "|| ",
      "&& ",
      "!= ",
      "== "
    ],
    "extensions": [
      "julius"
    ],
    "line_comment": [
      "//"
    ],
    "multi_line": [
      [
        "/*",
        "*/"
      ]
    ],
    "quotes": [
      {
        "end": "\"",
        "start": "\""
      }
    ]
  }
}
```

## Jupyter

```json
{
  "Jupyter": {
    "complexitychecks": [],
    "extensions": [
      "ipynb",
      "jpynb"
    ],
    "line_comment": [],
    "multi_line": [],
    "quotes": []
  }
}
```

## Just

```json
{
  "Just": {
    "complexitychecks": [
      "for ",
      "for(",
      "if ",
      "if(",
      "switch ",
      "while ",
      "else ",
      "|| ",
      "&& ",
      "!= ",
      "== "
    ],
    "extensions": [
      "justfile"
    ],
    "line_comment": [
      "#"
    ],
    "multi_line": [],
    "quotes": [
      {
        "end": "\\\"",
        "start": "\\\""
      }
    ]
  }
}
```

## K

```json
{
  "K": {
    "complexitychecks": [
      "'",
      "/",
      "\\",
      "':",
      "/:",
      "\\:",
      "|",
      "&",
      "!",
      "="
    ],
    "extensions": [
      "k"
    ],
    "line_comment": [
      "/"
    ],
    "quotes": [
      {
        "end": "\"",
        "start": "\""
      }
    ]
  }
}
```

## Korn Shell

```json
{
  "Korn Shell": {
    "complexitychecks": [
      "for ",
      "for(",
      "if ",
      "if(",
      "switch ",
      "while ",
      "else ",
      "|| ",
      "&& ",
      "!= ",
      "== "
    ],
    "extensions": [
      "ksh"
    ],
    "filenames": [
      ".kshrc"
    ],
    "line_comment": [
      "#"
    ],
    "multi_line": [],
    "quotes": [
      {
        "end": "\\\"",
        "start": "\\\""
      },
      {
        "end": "'",
        "start": "'"
      }
    ],
    "shebangs": [
      "ksh"
    ]
  }
}
```

## Kotlin

```json
{
  "Kotlin": {
    "complexitychecks": [
      "for ",
      "for(",
      "if ",
      "if(",
      "switch ",
      "while ",
      "else ",
      "|| ",
      "&& ",
      "!= ",
      "== "
    ],
    "extensions": [
      "kt",
      "kts"
    ],
    "line_comment": [
      "//"
    ],
    "multi_line": [
      [
        "/*",
        "*/"
      ]
    ],
    "nestedmultiline": true,
    "quotes": [
      {
        "end": "\"",
        "start": "\""
      }
    ]
  }
}
```

## Koto

```json
{
  "Koto": {
    "complexitychecks": [
      "for ",
      "while ",
      "until ",
      "continue ",
      "break ",
      "loop ",
      "if ",
      "switch ",
      "match ",
      "then",
      "else ",
      "|| ",
      "&& ",
      "!= ",
      "== ",
      "and ",
      "or ",
      "not "
    ],
    "extensions": [
      "koto"
    ],
    "line_comment": [
      "#"
    ],
    "multi_line": [
      [
        "#-",
        "-#"
      ]
    ],
    "nestedmultiline": true,
    "quotes": [
      {
        "end": "\"",
        "start": "\""
      },
      {
        "end": "'",
        "start": "'"
      }
    ]
  }
}
```

## LALRPOP

```json
{
  "LALRPOP": {
    "complexitychecks": [
      "for ",
      "for(",
      "if ",
      "if(",
      "switch ",
      "while ",
      "else ",
      "|| ",
      "&& ",
      "!= ",
      "== ",
      "match "
    ],
    "extensions": [
      "lalrpop"
    ],
    "line_comment": [
      "//"
    ],
    "multi_line": [
      [
        "/*",
        "*/"
      ]
    ],
    "nestedmultiline": true,
    "quotes": [
      {
        "end": "\"",
        "start": "\""
      },
      {
        "end": "\\\"",
        "start": "\\\""
      },
      {
        "end": "#\\\"",
        "start": "\\\"#"
      },
      {
        "end": "r##\\\"",
        "start": "\\\"##"
      },
      {
        "end": "r#\\\"",
        "start": "\\\"#"
      }
    ]
  }
}
```

## LD Script

```json
{
  "LD Script": {
    "complexitychecks": [
      "for ",
      "for(",
      "if ",
      "if(",
      "switch ",
      "while ",
      "else ",
      "|| ",
      "&& ",
      "!= ",
      "== "
    ],
    "extensions": [
      "lds"
    ],
    "line_comment": [
      "//"
    ],
    "multi_line": [
      [
        "/*",
        "*/"
      ]
    ],
    "quotes": [
      {
        "end": "\"",
        "start": "\""
      }
    ]
  }
}
```

## LESS

```json
{
  "LESS": {
    "complexitychecks": [],
    "extensions": [
      "less"
    ],
    "line_comment": [
      "//"
    ],
    "multi_line": [
      [
        "/*",
        "*/"
      ]
    ],
    "quotes": [
      {
        "end": "\"",
        "start": "\""
      }
    ]
  }
}
```

## LEX

```json
{
  "LEX": {
    "complexitychecks": [],
    "extensions": [
      "l"
    ],
    "line_comment": [],
    "multi_line": [
      [
        "/*",
        "*/"
      ]
    ],
    "quotes": []
  }
}
```

## LLVM IR

```json
{
  "LLVM IR": {
    "complexitychecks": [
      "llvm.loop",
      "br ",
      "switch ",
      "indirectbr ",
      "invoke ",
      "callbr ",
      "resume ",
      "catchswitch ",
      "catchret ",
      "cleanupret ",
      "shl ",
      "lshr ",
      "ashr ",
      "and ",
      "or ",
      "xor "
    ],
    "extensions": [
      "ll"
    ],
    "line_comment": [
      ";"
    ],
    "multi_line": [],
    "quotes": [
      {
        "end": "\"",
        "start": "\""
      }
    ],
    "shebangs": []
  }
}
```

## LOLCODE

```json
{
  "LOLCODE": {
    "complexitychecks": [
      "AWSUM THX ",
      "O NOES ",
      "PLZ OPEN FILE ",
      "IM IN YR ",
      "O RLY?",
      "O RLY? ",
      "WTF?",
      "WTF? "
    ],
    "extensions": [
      "lol",
      "lols"
    ],
    "line_comment": [
      "BTW"
    ],
    "multi_line": [
      [
        "OBTW",
        "TLDR"
      ]
    ],
    "quotes": [
      {
        "end": "\"",
        "start": "\""
      }
    ]
  }
}
```

## LaTeX

```json
{
  "LaTeX": {
    "complexitychecks": [],
    "extensions": [
      "tex"
    ],
    "line_comment": [
      "%"
    ],
    "multi_line": [],
    "quotes": []
  }
}
```

## Lean

```json
{
  "Lean": {
    "complexitychecks": [
      "for ",
      "for(",
      "if ",
      "if(",
      "switch ",
      "while ",
      "else ",
      "|| ",
      "&& ",
      "!= ",
      "== "
    ],
    "extensions": [
      "lean",
      "hlean"
    ],
    "line_comment": [
      "--"
    ],
    "multi_line": [
      [
        "/-",
        "-/"
      ]
    ],
    "nestedmultiline": true,
    "quotes": []
  }
}
```

## License

```json
{
  "License": {
    "complexitychecks": [],
    "extensions": [],
    "filenames": [
      "license",
      "licence",
      "copying",
      "copying3",
      "unlicense",
      "unlicence",
      "license-apache",
      "licence-apache",
      "license-mit",
      "licence-mit",
      "copyright"
    ],
    "line_comment": [],
    "multi_line": [],
    "quotes": []
  }
}
```

## Lisp

```json
{
  "Lisp": {
    "complexitychecks": [
      "for ",
      "for(",
      "if ",
      "if(",
      "switch ",
      "while ",
      "else ",
      "|| ",
      "&& ",
      "!= ",
      "== "
    ],
    "extensions": [
      "lisp",
      "lsp"
    ],
    "line_comment": [
      ";"
    ],
    "multi_line": [
      [
        "#|",
        "|#"
      ]
    ],
    "nestedmultiline": true,
    "quotes": [],
    "shebangs": [
      "sbcl"
    ]
  }
}
```

## LiveScript

```json
{
  "LiveScript": {
    "complexitychecks": [
      "for ",
      "for(",
      "if ",
      "if(",
      "switch ",
      "case ",
      "while ",
      "when ",
      "else ",
      "|| ",
      "&& ",
      "!= ",
      "!== ",
      "xor ",
      "and ",
      "or ",
      "|> ",
      "<< ",
      "<<< ",
      "<<<< ",
      ">> ",
      "== "
    ],
    "extensions": [
      "ls"
    ],
    "line_comment": [
      "#"
    ],
    "multi_line": [
      [
        "/*",
        "*/"
      ]
    ],
    "quotes": [
      {
        "end": "\"",
        "start": "\""
      },
      {
        "end": "'",
        "start": "'"
      }
    ]
  }
}
```

## Lua

```json
{
  "Lua": {
    "complexitychecks": [
      "for ",
      "for(",
      "if ",
      "if(",
      "while ",
      "while(",
      "else ",
      "else(",
      "elseif ",
      "elseif(",
      "until ",
      "until(",
      "or ",
      "and ",
      "~= ",
      "== "
    ],
    "extensions": [
      "lua"
    ],
    "line_comment": [
      "--"
    ],
    "multi_line": [
      [
        "--[[",
        "]]"
      ],
      [
        "--[=[",
        "]=]"
      ],
      [
        "--[==[",
        "]==]"
      ],
      [
        "--[===[",
        "]===]"
      ],
      [
        "--[====[",
        "]====]"
      ],
      [
        "--[=====[",
        "]=====]"
      ]
    ],
    "quotes": [
      {
        "end": "\"",
        "start": "\""
      },
      {
        "end": "'",
        "start": "'"
      },
      {
        "end": "[[",
        "start": "]]",
        "ignoreEscape": true
      }
    ],
    "shebangs": [
      "lua"
    ]
  }
}
```

## Luau

```json
{
  "Luau": {
    "complexitychecks": [
      "for ",
      "for(",
      "if ",
      "if(",
      "while ",
      "while(",
      "else ",
      "else(",
      "elseif ",
      "elseif(",
      "until ",
      "until(",
      "or ",
      "and ",
      "~= ",
      "== "
    ],
    "extensions": [
      "luau"
    ],
    "line_comment": [
      "--"
    ],
    "multi_line": [
      [
        "--[[",
        "]]"
      ],
      [
        "--[=[",
        "]=]"
      ],
      [
        "--[==[",
        "]==]"
      ],
      [
        "--[===[",
        "]===]"
      ],
      [
        "--[====[",
        "]====]"
      ],
      [
        "--[=====[",
        "]=====]"
      ]
    ],
    "quotes": [
      {
        "end": "\"",
        "start": "\""
      },
      {
        "end": "'",
        "start": "'"
      },
      {
        "end": "`",
        "start": "`"
      },
      {
        "end": "[[",
        "start": "]]",
        "ignoreEscape": true
      }
    ],
    "shebangs": [
      "luau"
    ]
  }
}
```

## Lucius

```json
{
  "Lucius": {
    "complexitychecks": [
      "for ",
      "for(",
      "if ",
      "if(",
      "switch ",
      "while ",
      "else ",
      "|| ",
      "&& ",
      "!= ",
      "== "
    ],
    "extensions": [
      "lucius"
    ],
    "line_comment": [
      "//"
    ],
    "multi_line": [
      [
        "/*",
        "*/"
      ]
    ],
    "quotes": [
      {
        "end": "\"",
        "start": "\""
      }
    ]
  }
}
```

## Luna

```json
{
  "Luna": {
    "complexitychecks": [],
    "extensions": [
      "luna"
    ],
    "line_comment": [
      "#"
    ],
    "multi_line": [],
    "quotes": [
      {
        "end": "\\\"",
        "start": "\\\""
      },
      {
        "end": "'",
        "start": "'"
      }
    ]
  }
}
```

## MATLAB

```json
{
  "MATLAB": {
    "complexitychecks": [
      "if ",
      "elseif ",
      "case ",
      "otherwise ",
      "try",
      "for ",
      "while "
    ],
    "extensions": [
      "m"
    ],
    "keywords": [
      "eye(",
      "zeros(",
      "ones(",
      "transpose(",
      "meshgrid(",
      "mod(",
      "classdef",
      "function",
      "disp(",
      "sin(",
      "tan(",
      "cos(",
      "plot",
      "sqrt(",
      "deblank(",
      "findstr(",
      "strrep(",
      "strcmp(",
      "display(",
      "strcat(",
      "iscellstr(",
      "strfind(",
      "%",
      "fprintf("
    ],
    "line_comment": [
      "%"
    ],
    "multi_line": [
      [
        "%{",
        "}%"
      ]
    ],
    "quotes": [
      {
        "end": "'",
        "start": "'"
      }
    ]
  }
}
```

## MDX

```json
{
  "MDX": {
    "complexitychecks": [],
    "extensions": [
      "mdx"
    ],
    "line_comment": [],
    "multi_line": [],
    "quotes": []
  }
}
```

## MQL Header

```json
{
  "MQL Header": {
    "complexitychecks": [
      "for ",
      "for(",
      "if ",
      "if(",
      "switch ",
      "while ",
      "else ",
      "|| ",
      "&& ",
      "!= ",
      "== "
    ],
    "extensions": [
      "mqh"
    ],
    "line_comment": [
      "//"
    ],
    "multi_line": [
      [
        "/*",
        "*/"
      ]
    ],
    "quotes": [
      {
        "end": "\"",
        "start": "\""
      }
    ]
  }
}
```

## MQL4

```json
{
  "MQL4": {
    "complexitychecks": [
      "for ",
      "for(",
      "if ",
      "if(",
      "switch ",
      "while ",
      "else ",
      "|| ",
      "&& ",
      "!= ",
      "== "
    ],
    "extensions": [
      "mq4"
    ],
    "line_comment": [
      "//"
    ],
    "multi_line": [
      [
        "/*",
        "*/"
      ]
    ],
    "quotes": [
      {
        "end": "\"",
        "start": "\""
      }
    ]
  }
}
```

## MQL5

```json
{
  "MQL5": {
    "complexitychecks": [
      "for ",
      "for(",
      "if ",
      "if(",
      "switch ",
      "while ",
      "else ",
      "|| ",
      "&& ",
      "!= ",
      "== "
    ],
    "extensions": [
      "mq5"
    ],
    "line_comment": [
      "//"
    ],
    "multi_line": [
      [
        "/*",
        "*/"
      ]
    ],
    "quotes": [
      {
        "end": "\"",
        "start": "\""
      }
    ]
  }
}
```

## MSBuild

```json
{
  "MSBuild": {
    "complexitychecks": [
      "Condition"
    ],
    "extensions": [
      "csproj",
      "vbproj",
      "fsproj",
      "vcproj",
      "vcxproj",
      "vcxproj.filters",
      "ilproj",
      "myapp",
      "props",
      "rdlc",
      "resx",
      "settings",
      "sln",
      "targets"
    ],
    "line_comment": [],
    "multi_line": [
      [
        "<!--",
        "-->"
      ]
    ],
    "quotes": [
      {
        "end": "\"",
        "start": "\""
      }
    ]
  }
}
```

## MUMPS

```json
{
  "MUMPS": {
    "complexitychecks": [
      "for ",
      "for(",
      "if ",
      "if(",
      "switch ",
      "while ",
      "else ",
      "|| ",
      "&& ",
      "!= ",
      "== "
    ],
    "extensions": [
      "mps"
    ],
    "line_comment": [
      ";"
    ],
    "multi_line": [],
    "quotes": [
      {
        "end": "\"",
        "start": "\""
      }
    ]
  }
}
```

## Macromedia eXtensible Markup Language

```json
{
  "Macromedia eXtensible Markup Language": {
    "complexitychecks": [],
    "extensions": [
      "mxml"
    ],
    "line_comment": [],
    "multi_line": [],
    "quotes": []
  }
}
```

## Madlang

```json
{
  "Madlang": {
    "complexitychecks": [
      "for ",
      "for(",
      "if ",
      "if(",
      "switch ",
      "while ",
      "else ",
      "|| ",
      "&& ",
      "!= ",
      "== "
    ],
    "extensions": [
      "mad"
    ],
    "line_comment": [
      "#"
    ],
    "multi_line": [
      [
        "{#",
        "#}"
      ]
    ],
    "quotes": []
  }
}
```

## Makefile

```json
{
  "Makefile": {
    "complexitychecks": [
      "for ",
      "for(",
      "if ",
      "if(",
      "switch ",
      "while ",
      "else ",
      "|| ",
      "&& ",
      "!= ",
      "== "
    ],
    "extensions": [
      "makefile",
      "mak",
      "mk",
      "bp"
    ],
    "filenames": [
      "makefile",
      "gnumakefile"
    ],
    "line_comment": [
      "#"
    ],
    "multi_line": [],
    "quotes": []
  }
}
```

## Mako

```json
{
  "Mako": {
    "complexitychecks": [
      "% for ",
      "% if ",
      "% else ",
      "% elif ",
      "<% include ",
      "<%def ",
      "<%page ",
      "<%def ",
      "<%block ",
      "<%namespace ",
      "<%inherit "
    ],
    "extensions": [
      "mako",
      "mao"
    ],
    "line_comment": [
      "##"
    ],
    "multi_line": [
      [
        "<%doc>",
        "</%doc>"
      ]
    ],
    "quotes": []
  }
}
```

## Markdown

```json
{
  "Markdown": {
    "complexitychecks": [],
    "extensions": [
      "md",
      "markdown"
    ],
    "line_comment": [],
    "multi_line": [],
    "quotes": []
  }
}
```

## Max

```json
{
  "Max": {
    "complexitychecks": [],
    "extensions": [
      "maxpat"
    ],
    "line_comment": [],
    "multi_line": [],
    "quotes": []
  }
}
```

## Meson

```json
{
  "Meson": {
    "complexitychecks": [
      "foreach ",
      "if ",
      "elif ",
      "unless ",
      "and ",
      "or ",
      "else "
    ],
    "extensions": [
      "meson.build",
      "meson_options.txt"
    ],
    "line_comment": [
      "#"
    ],
    "quotes": [
      {
        "end": "'",
        "start": "'"
      },
      {
        "end": "'''",
        "start": "'''"
      }
    ]
  }
}
```

## Metal

```json
{
  "Metal": {
    "complexitychecks": [
      "for ",
      "for(",
      "if ",
      "if(",
      "switch ",
      "switch(",
      "while ",
      "while(",
      "else ",
      "|| ",
      "&& ",
      "!= ",
      "== "
    ],
    "extensions": [
      "metal"
    ],
    "line_comment": [
      "//"
    ],
    "multi_line": [
      [
        "/*",
        "*/"
      ]
    ],
    "quotes": [
      {
        "end": "\"",
        "start": "\""
      }
    ]
  }
}
```

## Modula3

```json
{
  "Modula3": {
    "complexitychecks": [
      "for ",
      "for(",
      "if ",
      "if(",
      "switch ",
      "while ",
      "else ",
      "|| ",
      "&& ",
      "!= ",
      "== "
    ],
    "extensions": [
      "m3",
      "mg",
      "ig",
      "i3"
    ],
    "line_comment": [
      "#"
    ],
    "multi_line": [
      [
        "(*",
        "*)"
      ]
    ],
    "quotes": [
      {
        "end": "\"",
        "start": "\""
      }
    ]
  }
}
```

## Module-Definition

```json
{
  "Module-Definition": {
    "complexitychecks": [
      "for ",
      "for(",
      "if ",
      "if(",
      "switch ",
      "while ",
      "else ",
      "|| ",
      "&& ",
      "!= ",
      "== "
    ],
    "extensions": [
      "def"
    ],
    "line_comment": [
      ";"
    ],
    "multi_line": [],
    "quotes": []
  }
}
```

## Monkey C

```json
{
  "Monkey C": {
    "complexitychecks": [
      "for ",
      "for(",
      "if ",
      "if(",
      "switch ",
      "while ",
      "else ",
      "|| ",
      "&& ",
      "!= ",
      "== "
    ],
    "extensions": [
      "mc"
    ],
    "line_comment": [
      "//"
    ],
    "multi_line": [
      [
        "/*",
        "*/"
      ]
    ],
    "quotes": [
      {
        "end": "\"",
        "start": "\""
      }
    ]
  }
}
```

## Moonbit

```json
{
  "Moonbit": {
    "complexitychecks": [
      "for ",
      "if ",
      "switch ",
      "while ",
      "else ",
      "loop ",
      "guard ",
      "|| ",
      "&& ",
      "!= ",
      "== ",
      "match "
    ],
    "extensions": [
      "mbt"
    ],
    "line_comment": [
      "//"
    ],
    "multi_line": [],
    "quotes": [
      {
        "end": "\"",
        "start": "\""
      }
    ]
  }
}
```

## Mustache

```json
{
  "Mustache": {
    "complexitychecks": [
      "for ",
      "for(",
      "if ",
      "if(",
      "switch ",
      "while ",
      "else ",
      "|| ",
      "&& ",
      "!= ",
      "== "
    ],
    "extensions": [
      "mustache"
    ],
    "line_comment": [],
    "multi_line": [
      [
        "{{!",
        "}}"
      ]
    ],
    "quotes": [
      {
        "end": "\\\"",
        "start": "\\\""
      },
      {
        "end": "'",
        "start": "'"
      }
    ]
  }
}
```

## Nial

```json
{
  "Nial": {
    "complexitychecks": [
      "case ",
      "for ",
      "if ",
      "repeat ",
      "while ",
      "or ",
      "and ",
      "= ",
      "equal ",
      "~= ",
      "unequal "
    ],
    "extensions": [
      "ndf"
    ],
    "line_comment": [
      "%"
    ],
    "multi_line": [],
    "quotes": [
      {
        "end": "'",
        "start": "'"
      }
    ]
  }
}
```

## Nim

```json
{
  "Nim": {
    "complexitychecks": [
      "for ",
      "for(",
      "if ",
      "if(",
      "switch ",
      "while ",
      "else ",
      "|| ",
      "&& ",
      "!= ",
      "== "
    ],
    "extensions": [
      "nim"
    ],
    "line_comment": [
      "#"
    ],
    "multi_line": [],
    "quotes": [
      {
        "end": "\\\"",
        "start": "\\\""
      },
      {
        "end": "\\\"\\\"\\\"",
        "start": "\\\"\\\"\\\""
      }
    ]
  }
}
```

## Nix

```json
{
  "Nix": {
    "complexitychecks": [
      "for ",
      "for(",
      "if ",
      "if(",
      "switch ",
      "while ",
      "else ",
      "|| ",
      "&& ",
      "!= ",
      "== "
    ],
    "extensions": [
      "nix"
    ],
    "line_comment": [
      "#"
    ],
    "multi_line": [
      [
        "/*",
        "*/"
      ]
    ],
    "quotes": [
      {
        "end": "\"",
        "start": "\""
      }
    ]
  }
}
```

## Nushell

```json
{
  "Nushell": {
    "complexitychecks": [
      "for ",
      "do { ",
      "each {",
      "if ",
      "|| ",
      "&& ",
      "!= ",
      "== "
    ],
    "extensions": [
      "nu"
    ],
    "line_comment": [
      "#"
    ],
    "multi_line": [],
    "quotes": [
      {
        "end": "\"",
        "start": "\""
      },
      {
        "end": "'",
        "start": "'"
      }
    ],
    "shebangs": [
      "nu"
    ]
  }
}
```

## OCaml

```json
{
  "OCaml": {
    "complexitychecks": [
      "for ",
      "for(",
      "if ",
      "if(",
      "switch ",
      "while ",
      "else ",
      "|| ",
      "&& ",
      "!= ",
      "== "
    ],
    "extensions": [
      "ml",
      "mli"
    ],
    "line_comment": [],
    "multi_line": [
      [
        "(*",
        "*)"
      ]
    ],
    "quotes": [
      {
        "end": "\"",
        "start": "\""
      }
    ]
  }
}
```

## Objective C

```json
{
  "Objective C": {
    "complexitychecks": [
      "for ",
      "for(",
      "if ",
      "if(",
      "switch ",
      "while ",
      "else ",
      "|| ",
      "&& ",
      "!= ",
      "== "
    ],
    "extensions": [
      "m"
    ],
    "keywords": [
      "#include",
      "printf",
      "stdio.h",
      ".h",
      "@import",
      "@interface",
      "@property",
      "@implementation",
      "NSArray",
      "#pragma",
      "static",
      "const",
      "atomic",
      "@end",
      "//"
    ],
    "line_comment": [
      "//"
    ],
    "multi_line": [
      [
        "/*",
        "*/"
      ]
    ],
    "quotes": [
      {
        "end": "\"",
        "start": "\""
      }
    ]
  }
}
```

## Objective C++

```json
{
  "Objective C++": {
    "complexitychecks": [
      "for ",
      "for(",
      "if ",
      "if(",
      "switch ",
      "while ",
      "else ",
      "|| ",
      "&& ",
      "!= ",
      "== "
    ],
    "extensions": [
      "mm"
    ],
    "line_comment": [
      "//"
    ],
    "multi_line": [
      [
        "/*",
        "*/"
      ]
    ],
    "quotes": [
      {
        "end": "\"",
        "start": "\""
      }
    ]
  }
}
```

## Odin

```json
{
  "Odin": {
    "complexitychecks": [
      "for ",
      "for(",
      "if ",
      "if(",
      "when ",
      "switch ",
      "defer ",
      "else ",
      "|| ",
      "&& ",
      "!= ",
      "== "
    ],
    "extensions": [
      "odin"
    ],
    "line_comment": [
      "//"
    ],
    "multi_line": [
      [
        "/*",
        "*/"
      ]
    ],
    "quotes": [
      {
        "end": "\"",
        "start": "\""
      }
    ]
  }
}
```

## Opalang

```json
{
  "Opalang": {
    "complexitychecks": [
      "for ",
      "for(",
      "if ",
      "if(",
      "switch ",
      "while ",
      "else ",
      "|| ",
      "&& ",
      "!= ",
      "== "
    ],
    "extensions": [
      "opa"
    ],
    "line_comment": [
      "//"
    ],
    "multi_line": [
      [
        "/*",
        "*/"
      ]
    ],
    "quotes": [
      {
        "end": "\"",
        "start": "\""
      }
    ]
  }
}
```

## OpenQASM

```json
{
  "OpenQASM": {
    "complexitychecks": [
      "for ",
      "if ",
      "if(",
      "switch ",
      "switch(",
      "while ",
      "while(",
      "else ",
      "else(",
      "|| ",
      "&& ",
      "!= ",
      "== "
    ],
    "extensions": [
      "qasm"
    ],
    "line_comment": [
      "//"
    ],
    "multi_line": [
      [
        "/*",
        "*/"
      ]
    ],
    "quotes": [
      {
        "end": "\"",
        "start": "\""
      }
    ]
  }
}
```

## OpenTofu

```json
{
  "OpenTofu": {
    "complexitychecks": [
      "count",
      "for",
      "for_each",
      "if",
      ": ",
      "? ",
      "|| ",
      "&& ",
      "!= ",
      "> ",
      ">= ",
      "< ",
      "<= ",
      "== "
    ],
    "extensions": [
      "tofu"
    ],
    "line_comment": [
      "#",
      "//"
    ],
    "multi_line": [
      [
        "/*",
        "*/"
      ]
    ],
    "quotes": []
  }
}
```

## Org

```json
{
  "Org": {
    "complexitychecks": [
      "for ",
      "for(",
      "if ",
      "if(",
      "switch ",
      "while ",
      "else ",
      "|| ",
      "&& ",
      "!= ",
      "== "
    ],
    "extensions": [
      "org"
    ],
    "line_comment": [
      "# "
    ],
    "multi_line": [],
    "quotes": []
  }
}
```

## Oz

```json
{
  "Oz": {
    "complexitychecks": [
      "for ",
      "for(",
      "if ",
      "if(",
      "switch ",
      "while ",
      "else ",
      "|| ",
      "&& ",
      "!= ",
      "== "
    ],
    "extensions": [
      "oz"
    ],
    "line_comment": [
      "%"
    ],
    "multi_line": [
      [
        "/*",
        "*/"
      ]
    ],
    "quotes": [
      {
        "end": "\"",
        "start": "\""
      }
    ]
  }
}
```

## PHP

```json
{
  "PHP": {
    "complexitychecks": [
      "for ",
      "for(",
      "if ",
      "if(",
      "switch ",
      "while ",
      "else ",
      "|| ",
      "&& ",
      "!= ",
      "== "
    ],
    "extensions": [
      "php"
    ],
    "line_comment": [
      "#",
      "//"
    ],
    "multi_line": [
      [
        "/*",
        "*/"
      ]
    ],
    "quotes": [
      {
        "end": "\\\"",
        "start": "\\\""
      },
      {
        "end": "'",
        "start": "'"
      }
    ],
    "shebangs": [
      "php",
      "php5"
    ]
  }
}
```

## PKGBUILD

```json
{
  "PKGBUILD": {
    "complexitychecks": [],
    "extensions": [
      "pkgbuild"
    ],
    "line_comment": [],
    "multi_line": [],
    "quotes": []
  }
}
```

## PL/SQL

```json
{
  "PL/SQL": {
    "complexitychecks": [
      "and ",
      "and(",
      "else ",
      "else(",
      "elseif ",
      "elseif(",
      "if ",
      "if(",
      "loop ",
      "not ",
      "not(",
      "or ",
      "or(",
      "<> ",
      "<>(",
      "= ",
      "=("
    ],
    "extensions": [
      "fnc",
      "pkb",
      "pks",
      "prc",
      "trg",
      "vw"
    ],
    "line_comment": [
      "--"
    ],
    "multi_line": [
      [
        "/*",
        "*/"
      ]
    ],
    "quotes": [
      {
        "end": "'",
        "start": "'"
      }
    ]
  }
}
```

## PRQL

```json
{
  "PRQL": {
    "complexitychecks": [
      "case ",
      "&& ",
      "|| ",
      "!= ",
      "== ",
      "~= "
    ],
    "extensions": [
      "prql"
    ],
    "line_comment": [
      "#"
    ],
    "multi_line": [],
    "quotes": [
      {
        "end": "\"",
        "start": "\""
      },
      {
        "end": "'",
        "start": "'"
      },
      {
        "docString": true,
        "end": "\"\"\"",
        "start": "\"\"\""
      },
      {
        "docString": true,
        "end": "'''",
        "start": "'''"
      },
      {
        "docString": true,
        "end": "\"\"\"",
        "start": "r\"\"\""
      },
      {
        "docString": true,
        "end": "'''",
        "start": "r'''"
      }
    ]
  }
}
```

## PSL Assertion

```json
{
  "PSL Assertion": {
    "complexitychecks": [
      "for ",
      "for(",
      "if ",
      "if(",
      "switch ",
      "while ",
      "else ",
      "|| ",
      "&& ",
      "!= ",
      "== "
    ],
    "extensions": [
      "psl"
    ],
    "line_comment": [
      "//"
    ],
    "multi_line": [
      [
        "/*",
        "*/"
      ]
    ],
    "quotes": [
      {
        "end": "\"",
        "start": "\""
      }
    ]
  }
}
```

## Pascal

```json
{
  "Pascal": {
    "complexitychecks": [
      "for ",
      "for(",
      "if ",
      "if(",
      "switch ",
      "while ",
      "else ",
      "|| ",
      "&& ",
      "!= ",
      "== ",
      "AND ",
      "OR ",
      "IF ",
      "ELSE "
    ],
    "extensions": [
      "pas"
    ],
    "line_comment": [
      "//"
    ],
    "multi_line": [
      [
        "{",
        "}"
      ],
      [
        "(*",
        "*)"
      ]
    ],
    "quotes": [
      {
        "end": "'",
        "start": "'"
      }
    ]
  }
}
```

## Patch

```json
{
  "Patch": {
    "complexitychecks": [],
    "extensions": [
      "patch"
    ],
    "line_comment": [],
    "multi_line": [],
    "quotes": []
  }
}
```

## Perl

```json
{
  "Perl": {
    "complexitychecks": [
      "for ",
      "for(",
      "foreach ",
      "foreach(",
      "if ",
      "if(",
      "elsif ",
      "elsif(",
      "while ",
      "while(",
      "until ",
      "until(",
      "unless ",
      "unless(",
      "given ",
      "given(",
      "when ",
      "when(",
      "catch ",
      "catch(",
      "eq ",
      "ne ",
      "else ",
      "and ",
      "or ",
      "|| ",
      "&& ",
      "!= ",
      "== "
    ],
    "extensions": [
      "pl",
      "plx",
      "pm"
    ],
    "line_comment": [
      "#"
    ],
    "multi_line": [
      [
        "=pod",
        "=cut"
      ]
    ],
    "quotes": [
      {
        "end": "\"",
        "start": "\""
      },
      {
        "end": "'",
        "start": "'"
      }
    ],
    "shebangs": [
      "perl",
      "perl5"
    ]
  }
}
```

## Phoenix LiveView

```json
{
  "Phoenix LiveView": {
    "complexitychecks": [
      "case ",
      "cond ",
      "if ",
      "for ",
      "with ",
      "try ",
      "catch ",
      "rescue ",
      "else ",
      "and ",
      "or ",
      "not ",
      "|| ",
      "&& ",
      "!= ",
      "== ",
      "|> ",
      "<% ",
      "<. "
    ],
    "extensions": [
      "heex",
      "leex"
    ],
    "line_comment": [
      "#",
      "<!--"
    ],
    "multi_line": [
      [
        "<!--",
        "-->"
      ]
    ],
    "quotes": [
      {
        "end": "\\\"\\\"\\\"",
        "start": "\\\"\\\"\\\""
      },
      {
        "end": "\\\"",
        "start": "\\\""
      },
      {
        "end": "'''",
        "start": "'''"
      },
      {
        "end": "'",
        "start": "'"
      }
    ]
  }
}
```

## Picat

```json
{
  "Picat": {
    "complexitychecks": [
      "do ",
      "foreach ",
      "foreach(",
      "if ",
      "if(",
      "switch ",
      "while ",
      "while(",
      "else ",
      "|| ",
      "&& ",
      "!= ",
      "== "
    ],
    "extensions": [
      "pi"
    ],
    "line_comment": [
      "%"
    ],
    "multi_line": [
      [
        "/*",
        "*/"
      ]
    ],
    "quotes": [
      {
        "end": "\"",
        "start": "\""
      }
    ]
  }
}
```

## Pkl

```json
{
  "Pkl": {
    "complexitychecks": [
      "function ",
      "?? ",
      "?.",
      "ifNonNull(",
      "if ",
      " else ",
      ".map",
      "for ",
      "when ",
      "..."
    ],
    "extensions": [
      "pkl"
    ],
    "line_comment": [
      "//"
    ],
    "multi_line": [
      [
        "/*",
        "*/"
      ]
    ],
    "quotes": [
      {
        "end": "\"",
        "start": "\""
      },
      {
        "end": "#\"",
        "start": "\"#"
      },
      {
        "end": "##\"",
        "start": "\"##"
      },
      {
        "end": "\"\"\"",
        "ignoreEscape": true,
        "start": "\"\"\""
      }
    ]
  }
}
```

## Plain Text

```json
{
  "Plain Text": {
    "complexitychecks": [],
    "extensions": [
      "text",
      "txt"
    ],
    "line_comment": [],
    "multi_line": [],
    "quotes": []
  }
}
```

## Polly

```json
{
  "Polly": {
    "complexitychecks": [
      "for ",
      "for(",
      "if ",
      "if(",
      "switch ",
      "while ",
      "else ",
      "|| ",
      "&& ",
      "!= ",
      "== "
    ],
    "extensions": [
      "polly"
    ],
    "line_comment": [],
    "multi_line": [
      [
        "<!--",
        "-->"
      ]
    ],
    "quotes": [
      {
        "end": "\"",
        "start": "\""
      }
    ]
  }
}
```

## Pony

```json
{
  "Pony": {
    "complexitychecks": [
      "for ",
      "if ",
      "match ",
      "repeat",
      "while ",
      "else ",
      "elseif ",
      "| ",
      "|| ",
      "&& ",
      "!= ",
      "== "
    ],
    "extensions": [
      "pony"
    ],
    "line_comment": [
      "//"
    ],
    "multi_line": [
      [
        "/*",
        "*/"
      ]
    ],
    "quotes": [
      {
        "end": "\"",
        "start": "\""
      },
      {
        "end": "\\\"\\\"\\\"",
        "start": "\\\"\\\"\\\""
      }
    ]
  }
}
```

## PostScript

```json
{
  "PostScript": {
    "complexitychecks": [
      "if",
      "ifelse",
      "for",
      "repeat",
      "loop",
      "forall",
      "pathforall",
      "eq",
      "ne",
      "not",
      "and",
      "or"
    ],
    "extensions": [
      "ps"
    ],
    "line_comment": [
      "%"
    ],
    "quotes": [
      {
        "end": ")",
        "start": "("
      },
      {
        "end": ">",
        "start": "<"
      },
      {
        "end": "~>",
        "start": "<~"
      }
    ]
  }
}
```

## Powershell

```json
{
  "Powershell": {
    "complexitychecks": [
      "while ",
      "while(",
      "until ",
      "until(",
      "for ",
      "for(",
      "foreach ",
      "foreach(",
      "if ",
      "elseif ",
      "else ",
      "switch",
      "switch(",
      "-gt",
      "-lt",
      "-eq",
      "-ne",
      "-ge",
      "-le",
      "-in",
      "-notin",
      "-contains",
      "-notcontains"
    ],
    "extensions": [
      "ps1",
      "psm1"
    ],
    "line_comment": [
      "#"
    ],
    "multi_line": [
      [
        "<#",
        "#>"
      ]
    ],
    "quotes": [
      {
        "end": "\"",
        "start": "\""
      }
    ]
  }
}
```

## Processing

```json
{
  "Processing": {
    "complexitychecks": [
      "for ",
      "for(",
      "if ",
      "if(",
      "switch ",
      "while ",
      "else ",
      "|| ",
      "&& ",
      "!= ",
      "== "
    ],
    "extensions": [
      "pde"
    ],
    "line_comment": [
      "//"
    ],
    "multi_line": [
      [
        "/*",
        "*/"
      ]
    ],
    "quotes": [
      {
        "end": "\"",
        "start": "\""
      }
    ]
  }
}
```

## Prolog

```json
{
  "Prolog": {
    "complexitychecks": [
      "for ",
      "for(",
      "if ",
      "if(",
      "switch ",
      "while ",
      "else ",
      "|| ",
      "&& ",
      "!= ",
      "== "
    ],
    "extensions": [
      "p",
      "pro"
    ],
    "line_comment": [
      "%"
    ],
    "multi_line": [
      [
        "/*",
        "*/"
      ]
    ],
    "quotes": [
      {
        "end": "\"",
        "start": "\""
      }
    ]
  }
}
```

## Properties File

```json
{
  "Properties File": {
    "complexitychecks": [],
    "extensions": [
      "properties"
    ],
    "line_comment": [
      "#"
    ],
    "multi_line": [],
    "quotes": []
  }
}
```

## Protocol Buffers

```json
{
  "Protocol Buffers": {
    "complexitychecks": [
      "for ",
      "for(",
      "if ",
      "if(",
      "switch ",
      "while ",
      "else ",
      "|| ",
      "&& ",
      "!= ",
      "== "
    ],
    "extensions": [
      "proto"
    ],
    "line_comment": [
      "//"
    ],
    "multi_line": [
      [
        "/*",
        "*/"
      ]
    ],
    "quotes": []
  }
}
```

## Puppet

```json
{
  "Puppet": {
    "complexitychecks": [
      "for ",
      "for(",
      "if ",
      "if(",
      "switch ",
      "while ",
      "else ",
      "|| ",
      "&& ",
      "!= ",
      "== "
    ],
    "extensions": [
      "pp"
    ],
    "line_comment": [
      "#"
    ],
    "multi_line": [
      [
        "=begin",
        "=end"
      ]
    ],
    "quotes": [
      {
        "end": "\\\"",
        "start": "\\\""
      },
      {
        "end": "'",
        "start": "'"
      }
    ]
  }
}
```

## PureScript

```json
{
  "PureScript": {
    "complexitychecks": [
      "for ",
      "for(",
      "if ",
      "if(",
      "switch ",
      "while ",
      "else ",
      "|| ",
      "&& ",
      "!= ",
      "== "
    ],
    "extensions": [
      "purs"
    ],
    "line_comment": [
      "--"
    ],
    "multi_line": [
      [
        "{-",
        "-}"
      ]
    ],
    "quotes": []
  }
}
```

## Python

```json
{
  "Python": {
    "complexitychecks": [
      "for ",
      "for(",
      "while ",
      "while(",
      "if ",
      "if(",
      "elif ",
      "elif(",
      "else ",
      "else:",
      "match ",
      "match(",
      "try ",
      "try:",
      "except ",
      "except:",
      "finally ",
      "finally:",
      "with ",
      "with (",
      "and ",
      "and(",
      "or ",
      "or("
    ],
    "extensions": [
      "py",
      "pyw",
      "pyi"
    ],
    "line_comment": [
      "#"
    ],
    "multi_line": [],
    "quotes": [
      {
        "end": "\"",
        "start": "\""
      },
      {
        "end": "'",
        "start": "'"
      },
      {
        "ignoreEscape": true,
        "end": "'",
        "start": "r'"
      },
      {
        "ignoreEscape": true,
        "end": "\"",
        "start": "r\""
      },
      {
        "docString": true,
        "end": "\"\"\"",
        "start": "\"\"\""
      },
      {
        "docString": true,
        "end": "'''",
        "start": "'''"
      },
      {
        "docString": true,
        "ignoreEscape": true,
        "end": "\"\"\"",
        "start": "r\"\"\""
      },
      {
        "docString": true,
        "ignoreEscape": true,
        "end": "'''",
        "start": "r'''"
      },
      {
        "docString": true,
        "end": "\"\"\"",
        "start": "f\"\"\""
      },
      {
        "docString": true,
        "end": "'''",
        "start": "f'''"
      }
    ],
    "shebangs": [
      "python",
      "python2",
      "python3"
    ]
  }
}
```

## Q#

```json
{
  "Q#": {
    "complexitychecks": [
      "for ",
      "for(",
      "repeat ",
      "repeat{",
      "until (",
      "until(",
      "if ",
      "if(",
      "elif ",
      "elif{",
      "else ",
      "else{",
      "||| ",
      "&&& ",
      "<<<",
      ">>>",
      "^^^",
      "~~~",
      "!= ",
      "== "
    ],
    "extensions": [
      "qs"
    ],
    "line_comment": [
      "//"
    ],
    "multi_line": [],
    "quotes": [
      {
        "end": "\"",
        "start": "\""
      }
    ]
  }
}
```

## QCL

```json
{
  "QCL": {
    "complexitychecks": [
      "for ",
      "for(",
      "if ",
      "if(",
      "switch ",
      "while ",
      "else ",
      "|| ",
      "&& ",
      "!= ",
      "== "
    ],
    "extensions": [
      "qcl"
    ],
    "line_comment": [
      "//"
    ],
    "multi_line": [
      [
        "/*",
        "*/"
      ]
    ],
    "quotes": [
      {
        "end": "\"",
        "start": "\""
      }
    ]
  }
}
```

## QML

```json
{
  "QML": {
    "complexitychecks": [
      "for ",
      "for(",
      "if ",
      "if(",
      "switch ",
      "while ",
      "else ",
      "|| ",
      "&& ",
      "!= ",
      "== "
    ],
    "extensions": [
      "qml"
    ],
    "line_comment": [
      "//"
    ],
    "multi_line": [
      [
        "/*",
        "*/"
      ]
    ],
    "quotes": [
      {
        "end": "\"",
        "start": "\""
      }
    ]
  }
}
```

## R

```json
{
  "R": {
    "complexitychecks": [
      "for ",
      "for(",
      "if ",
      "if(",
      "switch ",
      "while ",
      "else ",
      "|| ",
      "&& ",
      "!= ",
      "== "
    ],
    "extensions": [
      "r"
    ],
    "line_comment": [
      "#"
    ],
    "multi_line": [],
    "quotes": [],
    "shebangs": [
      "Rscript"
    ]
  }
}
```

## RAML

```json
{
  "RAML": {
    "complexitychecks": [],
    "extensions": [
      "raml",
      "rml"
    ],
    "line_comment": [
      "#"
    ],
    "multi_line": [],
    "quotes": []
  }
}
```

## Racket

```json
{
  "Racket": {
    "complexitychecks": [
      "(if",
      "(cond",
      "[else",
      "(and",
      "(or",
      "(for",
      "#:when",
      "#:unless",
      "#:break",
      "#:final",
      "(do",
      "(when",
      "(unless",
      "(shared",
      "(case"
    ],
    "extensions": [
      "rkt"
    ],
    "line_comment": [
      ";"
    ],
    "multi_line": [
      [
        "|#",
        "#|"
      ]
    ],
    "nestedmultiline": true,
    "quotes": [
      {
        "end": "\"",
        "start": "\""
      }
    ],
    "shebangs": [
      "racket"
    ]
  }
}
```

## Rakefile

```json
{
  "Rakefile": {
    "complexitychecks": [
      "for ",
      "for(",
      "if ",
      "if(",
      "switch ",
      "while ",
      "else ",
      "|| ",
      "&& ",
      "!= ",
      "== "
    ],
    "extensions": [],
    "filenames": [
      "rake",
      "rakefile"
    ],
    "line_comment": [
      "#"
    ],
    "multi_line": [
      [
        "=begin",
        "=end"
      ]
    ],
    "quotes": [
      {
        "end": "\\\"",
        "start": "\\\""
      },
      {
        "end": "'",
        "start": "'"
      }
    ]
  }
}
```

## Raku

```json
{
  "Raku": {
    "complexitychecks": [
      "== ",
      "\u2261 ",
      "!= ",
      "\u2260 ",
      "!== ",
      "\u2262 ",
      "< ",
      "\u2282 ",
      "!< ",
      "\u2284 ",
      "<= ",
      "\u2264 ",
      "\u2286 ",
      "!<= ",
      "\u2288 ",
      "> ",
      "\u2283 ",
      "!> ",
      "\u2285 ",
      ">= ",
      "\u2265 ",
      "\u2287 ",
      "!>= ",
      "\u2289 ",
      "=~= ",
      "\u2245 ",
      "=== ",
      "eq ",
      "!eq ",
      "eqv ",
      "ne ",
      "gt ",
      "ge ",
      "lt ",
      "le ",
      "=:=",
      "CATCH ",
      "CONTROL ",
      "DOC ",
      "NEXT ",
      "and ",
      "default ",
      "do {",
      "else ",
      "elsif ",
      "emit ",
      "for ",
      "gather ",
      "given ",
      "if ",
      "last ",
      "loop (",
      "next ",
      "once ",
      "or ",
      "orwith ",
      "react {",
      "redo ",
      "repeat ",
      "start {",
      "supply ",
      "unless ",
      "until ",
      "when ",
      "whenever ",
      "while ",
      "with ",
      "without "
    ],
    "extensions": [
      "raku",
      "rakumod",
      "rakutest",
      "rakudoc",
      "t"
    ],
    "line_comment": [
      "#"
    ],
    "multi_line": [
      [
        "=begin",
        "=end"
      ],
      [
        "#`(",
        ")"
      ],
      [
        "#`[",
        "]"
      ],
      [
        "#`{",
        "}"
      ],
      [
        "#`\uff62",
        "\uff63"
      ]
    ],
    "quotes": [
      {
        "end": "\\\"",
        "start": "\\\""
      },
      {
        "end": "'",
        "start": "'"
      },
      {
        "end": "\u201c",
        "start": "\u201e"
      },
      {
        "end": "\u00bb",
        "start": "\u00ab"
      },
      {
        "end": ">>",
        "start": "<<"
      },
      {
        "end": "\u201d",
        "start": "\u201c"
      },
      {
        "end": "\u2018",
        "start": "\u2019"
      },
      {
        "end": "\uff63",
        "start": "\uff62"
      }
    ],
    "shebangs": [
      "raku"
    ]
  }
}
```

## Razor

```json
{
  "Razor": {
    "complexitychecks": [
      "for ",
      "for(",
      "if ",
      "if(",
      "switch ",
      "while ",
      "else ",
      "|| ",
      "&& ",
      "!= ",
      "== "
    ],
    "extensions": [
      "cshtml",
      "razor"
    ],
    "line_comment": [],
    "multi_line": [
      [
        "<!--",
        "-->"
      ],
      [
        "@*",
        "*@"
      ]
    ],
    "quotes": []
  }
}
```

## ReScript

```json
{
  "ReScript": {
    "complexitychecks": [
      "for ",
      "for(",
      "if ",
      "if(",
      "switch ",
      "while ",
      "else ",
      "|| ",
      "&& ",
      "!= ",
      "== ",
      "=== "
    ],
    "extensions": [
      "res",
      "resi"
    ],
    "line_comment": [
      "//"
    ],
    "multi_line": [
      [
        "/*",
        "*/"
      ]
    ],
    "quotes": [
      {
        "end": "\"",
        "start": "\""
      }
    ]
  }
}
```

## ReStructuredText

```json
{
  "ReStructuredText": {
    "complexitychecks": [],
    "extensions": [
      "rst"
    ],
    "line_comment": [],
    "multi_line": [],
    "quotes": []
  }
}
```

## ReasonML

```json
{
  "ReasonML": {
    "complexitychecks": [
      "for ",
      "for(",
      "if ",
      "if(",
      "switch ",
      "while ",
      "else ",
      "|| ",
      "&& ",
      "!= ",
      "== "
    ],
    "extensions": [
      "re",
      "rei"
    ],
    "line_comment": [
      "//"
    ],
    "multi_line": [
      [
        "/*",
        "*/"
      ]
    ],
    "quotes": [
      {
        "end": "\"",
        "start": "\""
      }
    ]
  }
}
```

## Redscript

```json
{
  "Redscript": {
    "complexitychecks": [
      "for ",
      "@if(",
      "switch ",
      "while ",
      "else ",
      "func ",
      "-> "
    ],
    "extensions": [
      "reds"
    ],
    "line_comment": [
      "//",
      "///"
    ],
    "multi_line": [
      [
        "/*",
        "*/"
      ]
    ],
    "nestedmultiline": true,
    "quotes": [
      {
        "end": "\"",
        "start": "\""
      }
    ]
  }
}
```

## Report Definition Language

```json
{
  "Report Definition Language": {
    "complexitychecks": [],
    "extensions": [
      "rdl"
    ],
    "line_comment": [],
    "multi_line": [
      [
        "<!--",
        "-->"
      ]
    ],
    "quotes": [
      {
        "end": "\"",
        "start": "\""
      }
    ]
  }
}
```

## Robot Framework

```json
{
  "Robot Framework": {
    "complexitychecks": [],
    "extensions": [
      "robot"
    ],
    "line_comment": [],
    "multi_line": [],
    "quotes": []
  }
}
```

## Ruby

```json
{
  "Ruby": {
    "complexitychecks": [
      "for ",
      "for(",
      "if ",
      "if(",
      "switch ",
      "while ",
      "else ",
      "|| ",
      "&& ",
      "!= ",
      "== "
    ],
    "extensions": [
      "rb"
    ],
    "line_comment": [
      "#"
    ],
    "multi_line": [
      [
        "=begin",
        "=end"
      ]
    ],
    "quotes": [
      {
        "end": "\\\"",
        "start": "\\\""
      },
      {
        "end": "'",
        "start": "'"
      }
    ],
    "shebangs": [
      "ruby"
    ]
  }
}
```

## Ruby HTML

```json
{
  "Ruby HTML": {
    "complexitychecks": [
      "for ",
      "for(",
      "if ",
      "if(",
      "switch ",
      "while ",
      "else ",
      "|| ",
      "&& ",
      "!= ",
      "== "
    ],
    "extensions": [
      "rhtml",
      "erb"
    ],
    "line_comment": [],
    "multi_line": [
      [
        "<!--",
        "-->"
      ]
    ],
    "quotes": [
      {
        "end": "\"",
        "start": "\""
      }
    ]
  }
}
```

## Rust

```json
{
  "Rust": {
    "complexitychecks": [
      "for ",
      "for(",
      "if ",
      "if(",
      "switch ",
      "while ",
      "else ",
      "|| ",
      "&& ",
      "!= ",
      "== ",
      "match "
    ],
    "extensions": [
      "rs"
    ],
    "line_comment": [
      "//"
    ],
    "multi_line": [
      [
        "/*",
        "*/"
      ]
    ],
    "nestedmultiline": true,
    "quotes": [
      {
        "end": "\"",
        "start": "\""
      }
    ]
  }
}
```

## SAS

```json
{
  "SAS": {
    "complexitychecks": [
      "do",
      "%do",
      "if",
      "%if",
      "else",
      "%else",
      "case",
      "or",
      "and",
      "^=",
      "\u00ac=",
      "~=",
      "ne",
      "eq"
    ],
    "extensions": [
      "sas"
    ],
    "line_comment": [
      "*"
    ],
    "multi_line": [
      [
        "/*",
        "*/"
      ]
    ],
    "quotes": [
      {
        "end": "\"",
        "start": "\""
      },
      {
        "end": "'",
        "start": "'"
      }
    ]
  }
}
```

## SKILL

```json
{
  "SKILL": {
    "complexitychecks": [
      "for ",
      "for(",
      "if ",
      "if(",
      "switch ",
      "while ",
      "else ",
      "|| ",
      "&& ",
      "!= ",
      "== "
    ],
    "extensions": [
      "il"
    ],
    "line_comment": [
      ";"
    ],
    "multi_line": [
      [
        "/*",
        "*/"
      ]
    ],
    "quotes": [
      {
        "end": "\"",
        "start": "\""
      }
    ]
  }
}
```

## SNOBOL

```json
{
  "SNOBOL": {
    "complexitychecks": [
      ":(",
      ":s(",
      ":f(",
      "eq ",
      "ne "
    ],
    "extensions": [
      "sno"
    ],
    "line_comment": [
      "*"
    ],
    "quotes": [
      {
        "end": "\"",
        "start": "\""
      },
      {
        "end": "'",
        "start": "'"
      }
    ]
  }
}
```

## SPDX

```json
{
  "SPDX": {
    "complexitychecks": [],
    "extensions": [
      "spdx"
    ],
    "line_comment": [],
    "multi_line": [],
    "quotes": []
  }
}
```

## SPL

```json
{
  "SPL": {
    "complexitychecks": [
      "construct",
      "foreach",
      "map",
      "while",
      "if",
      "include",
      "catch",
      "and",
      "or",
      "not",
      "call",
      "<|",
      "<{",
      "dup",
      "swap"
    ],
    "extensions": [
      "spl"
    ],
    "line_comment": [],
    "multi_line": [
      [
        "\"",
        "\";"
      ]
    ],
    "quotes": [
      {
        "end": "\"",
        "start": "\""
      },
      {
        "end": " ",
        "start": "^"
      },
      {
        "end": ">",
        "start": "^"
      },
      {
        "end": ":",
        "start": "^"
      }
    ],
    "shebangs": [
      "spl"
    ]
  }
}
```

## SQL

```json
{
  "SQL": {
    "complexitychecks": [
      "for ",
      "for(",
      "if ",
      "if(",
      "switch ",
      "while ",
      "else ",
      "|| ",
      "&& ",
      "!= ",
      "== "
    ],
    "extensions": [
      "sql",
      "dml",
      "ddl",
      "dql"
    ],
    "line_comment": [
      "--"
    ],
    "multi_line": [
      [
        "/*",
        "*/"
      ]
    ],
    "quotes": [
      {
        "end": "'",
        "start": "'"
      }
    ]
  }
}
```

## SRecode Template

```json
{
  "SRecode Template": {
    "complexitychecks": [
      "for ",
      "for(",
      "if ",
      "if(",
      "switch ",
      "while ",
      "else ",
      "|| ",
      "&& ",
      "!= ",
      "== "
    ],
    "extensions": [
      "srt"
    ],
    "line_comment": [
      ";;"
    ],
    "multi_line": [],
    "quotes": []
  }
}
```

## SVG

```json
{
  "SVG": {
    "complexitychecks": [
      "for ",
      "for(",
      "if ",
      "if(",
      "switch ",
      "while ",
      "else ",
      "|| ",
      "&& ",
      "!= ",
      "== "
    ],
    "extensions": [
      "svg"
    ],
    "line_comment": [],
    "multi_line": [
      [
        "<!--",
        "-->"
      ]
    ],
    "quotes": [
      {
        "end": "\"",
        "start": "\""
      }
    ]
  }
}
```

## Sass

```json
{
  "Sass": {
    "complexitychecks": [
      "for ",
      "for(",
      "if ",
      "if(",
      "switch ",
      "while ",
      "else ",
      "|| ",
      "&& ",
      "!= ",
      "== "
    ],
    "extensions": [
      "sass",
      "scss"
    ],
    "line_comment": [
      "//"
    ],
    "multi_line": [
      [
        "/*",
        "*/"
      ]
    ],
    "quotes": [
      {
        "end": "\"",
        "start": "\""
      }
    ]
  }
}
```

## Scala

```json
{
  "Scala": {
    "complexitychecks": [
      "for ",
      "for(",
      "if ",
      "if(",
      "switch ",
      "while ",
      "else ",
      "|| ",
      "&& ",
      "!= ",
      "== ",
      ">= ",
      "> ",
      "<= ",
      "< "
    ],
    "extensions": [
      "sc",
      "scala"
    ],
    "line_comment": [
      "//"
    ],
    "multi_line": [
      [
        "/*",
        "*/"
      ]
    ],
    "quotes": [
      {
        "end": "\"",
        "start": "\""
      }
    ]
  }
}
```

## Scallop

```json
{
  "Scallop": {
    "complexitychecks": [
      "rel ",
      "count(",
      "sum(",
      "prod(",
      "min(",
      "max(",
      "exists(",
      "forall(",
      "|| ",
      "&& ",
      "!= ",
      "== ",
      ">= ",
      "> ",
      "<= ",
      "< "
    ],
    "extensions": [
      "scl"
    ],
    "line_comment": [
      "//"
    ],
    "multi_line": [
      [
        "/*",
        "*/"
      ]
    ],
    "quotes": [
      {
        "end": "\"",
        "start": "\""
      }
    ]
  }
}
```

## Scheme

```json
{
  "Scheme": {
    "complexitychecks": [
      "for ",
      "for(",
      "if ",
      "if(",
      "switch ",
      "while ",
      "else ",
      "|| ",
      "&& ",
      "!= ",
      "== "
    ],
    "extensions": [
      "scm",
      "ss"
    ],
    "line_comment": [
      ";"
    ],
    "multi_line": [
      [
        "#|",
        "|#"
      ]
    ],
    "nestedmultiline": true,
    "quotes": [],
    "shebangs": []
  }
}
```

## Scons

```json
{
  "Scons": {
    "complexitychecks": [
      "for ",
      "for(",
      "if ",
      "if(",
      "switch ",
      "while ",
      "else ",
      "|| ",
      "&& ",
      "!= ",
      "== "
    ],
    "extensions": [
      "csig",
      "sconstruct",
      "sconscript"
    ],
    "line_comment": [
      "#"
    ],
    "multi_line": [],
    "quotes": [
      {
        "end": "\\\"",
        "start": "\\\""
      },
      {
        "end": "'",
        "start": "'"
      },
      {
        "end": "\\\"\\\"\\\"",
        "start": "\\\"\\\"\\\""
      },
      {
        "end": "'''",
        "start": "'''"
      }
    ]
  }
}
```

## Shell

```json
{
  "Shell": {
    "complexitychecks": [
      "for ",
      "for(",
      "if ",
      "if(",
      "switch ",
      "while ",
      "else ",
      "|| ",
      "&& ",
      "!= ",
      "== "
    ],
    "extensions": [
      "sh"
    ],
    "filenames": [
      ".tcshrc"
    ],
    "line_comment": [
      "#"
    ],
    "multi_line": [],
    "quotes": [
      {
        "end": "\\\"",
        "start": "\\\""
      },
      {
        "end": "'",
        "start": "'"
      }
    ],
    "shebangs": [
      "sh"
    ]
  }
}
```

## Sieve

```json
{
  "Sieve": {
    "complexitychecks": [
      "if",
      "if ",
      "elsif",
      "elsif ",
      "allof",
      "allof ",
      "anyof",
      "anyof ",
      "allof(",
      "anyof("
    ],
    "extensions": [
      "sieve"
    ],
    "line_comment": [
      "#"
    ],
    "multi_line": [
      [
        "/*",
        "*/"
      ]
    ],
    "quotes": [
      {
        "end": "\"",
        "start": "\""
      }
    ]
  }
}
```

## Slang

```json
{
  "Slang": {
    "complexitychecks": [
      "for ",
      "for(",
      "if ",
      "if(",
      "switch ",
      "while ",
      "else ",
      "|| ",
      "&& ",
      "!= ",
      "== "
    ],
    "extensions": [
      "slang"
    ],
    "line_comment": [
      "//"
    ],
    "multi_line": [
      [
        "/*",
        "*/"
      ]
    ],
    "quotes": [
      {
        "end": "\"",
        "start": "\""
      }
    ]
  }
}
```

## Slint

```json
{
  "Slint": {
    "complexitychecks": [
      "for ",
      "if ",
      "if(",
      "states ",
      "states[",
      "else ",
      "|| ",
      "&& ",
      "!= ",
      "== "
    ],
    "extensions": [
      "slint"
    ],
    "line_comment": [
      "//"
    ],
    "multi_line": [
      [
        "/*",
        "*/"
      ]
    ],
    "quotes": [
      {
        "end": "\"",
        "start": "\""
      }
    ]
  }
}
```

## Smalltalk

```json
{
  "Smalltalk": {
    "complexitychecks": [
      "bitAnd ",
      "bitOr ",
      "bitXor ",
      "bitInvert ",
      "bitShift ",
      "bitAt ",
      "highbit ",
      "allMask ",
      "anyMask ",
      "noMask ",
      "ifTrue ",
      "ifFalse ",
      "switch ",
      "whileTrue ",
      "whileFalse ",
      "to: "
    ],
    "extensions": [
      "cs.st",
      "pck.st"
    ],
    "line_comment": [],
    "multi_line": [
      [
        "\"",
        "\""
      ]
    ],
    "quotes": [
      {
        "end": "'",
        "start": "'"
      }
    ]
  }
}
```

## Smarty Template

```json
{
  "Smarty Template": {
    "complexitychecks": [
      "for ",
      "for(",
      "if ",
      "if(",
      "switch ",
      "while ",
      "else ",
      "|| ",
      "&& ",
      "!= ",
      "== ",
      "include "
    ],
    "extensions": [
      "tpl"
    ],
    "line_comment": [],
    "multi_line": [
      [
        "{*",
        "*}"
      ]
    ],
    "quotes": []
  }
}
```

## Snakemake

```json
{
  "Snakemake": {
    "complexitychecks": [
      "for ",
      "for(",
      "while ",
      "while(",
      "if ",
      "if(",
      "elif ",
      "elif(",
      "else ",
      "else:",
      "match ",
      "match(",
      "try ",
      "try:",
      "except ",
      "except(",
      "finally ",
      "finally:",
      "with ",
      "with (",
      "and ",
      "and(",
      "or ",
      "or("
    ],
    "extensions": [
      "smk",
      "rules"
    ],
    "filenames": [
      "snakefile"
    ],
    "line_comment": [
      "#"
    ],
    "multi_line": [],
    "quotes": [
      {
        "end": "\"",
        "start": "\""
      },
      {
        "end": "'",
        "start": "'"
      },
      {
        "docString": true,
        "end": "\"\"\"",
        "start": "\"\"\""
      },
      {
        "docString": true,
        "end": "'''",
        "start": "'''"
      },
      {
        "docString": true,
        "end": "\"\"\"",
        "start": "r\"\"\""
      },
      {
        "docString": true,
        "end": "'''",
        "start": "r'''"
      }
    ]
  }
}
```

## Softbridge Basic

```json
{
  "Softbridge Basic": {
    "complexitychecks": [
      "for ",
      "for(",
      "if ",
      "if(",
      "elseif ",
      "switch ",
      "while ",
      "else ",
      "|| ",
      "&& ",
      "!= ",
      "== "
    ],
    "extensions": [
      "sbl"
    ],
    "line_comment": [
      "'"
    ],
    "multi_line": [],
    "quotes": [
      {
        "end": "\\\"",
        "start": "\\\""
      }
    ]
  }
}
```

## Solidity

```json
{
  "Solidity": {
    "complexitychecks": [
      "for ",
      "for(",
      "if ",
      "if(",
      "switch ",
      "while ",
      "else ",
      "|| ",
      "&& ",
      "!= ",
      "== ",
      "assembly ",
      "assembly{",
      "unchecked ",
      "unchecked{"
    ],
    "extensions": [
      "sol"
    ],
    "line_comment": [
      "//"
    ],
    "multi_line": [
      [
        "/*",
        "*/"
      ]
    ],
    "quotes": [
      {
        "end": "\"",
        "start": "\""
      }
    ]
  }
}
```

## Specman e

```json
{
  "Specman e": {
    "complexitychecks": [
      "for ",
      "for(",
      "if ",
      "if(",
      "switch ",
      "while ",
      "else ",
      "|| ",
      "&& ",
      "!= ",
      "== "
    ],
    "extensions": [
      "e"
    ],
    "line_comment": [
      "--",
      "//"
    ],
    "multi_line": [
      [
        "'>",
        "<'"
      ]
    ],
    "quotes": []
  }
}
```

## Spice Netlist

```json
{
  "Spice Netlist": {
    "complexitychecks": [
      "for ",
      "for(",
      "if ",
      "if(",
      "switch ",
      "while ",
      "else ",
      "|| ",
      "&& ",
      "!= ",
      "== "
    ],
    "extensions": [
      "ckt"
    ],
    "line_comment": [
      "*"
    ],
    "multi_line": [],
    "quotes": []
  }
}
```

## Stan

```json
{
  "Stan": {
    "complexitychecks": [],
    "extensions": [
      "stan"
    ],
    "line_comment": [
      "#",
      "//"
    ],
    "multi_line": [
      [
        "/*",
        "*/"
      ]
    ],
    "quotes": [
      {
        "end": "\"",
        "start": "\""
      }
    ]
  }
}
```

## Standard ML (SML)

```json
{
  "Standard ML (SML)": {
    "complexitychecks": [
      "for ",
      "for(",
      "if ",
      "if(",
      "switch ",
      "while ",
      "else ",
      "|| ",
      "&& ",
      "!= ",
      "== "
    ],
    "extensions": [
      "sml"
    ],
    "line_comment": [],
    "multi_line": [
      [
        "(*",
        "*)"
      ]
    ],
    "quotes": [
      {
        "end": "\"",
        "start": "\""
      }
    ]
  }
}
```

## Stata

```json
{
  "Stata": {
    "complexitychecks": [
      "foreach",
      "forvalues",
      "if",
      "else",
      "while",
      "switch",
      "|",
      "&",
      "!=",
      "=="
    ],
    "extensions": [
      "do",
      "ado"
    ],
    "line_comment": [
      "//",
      "*"
    ],
    "multi_line": [
      [
        "/*",
        "*/"
      ]
    ],
    "quotes": [
      {
        "end": "\"",
        "start": "\""
      },
      {
        "end": "\"'",
        "start": "`\""
      }
    ]
  }
}
```

## Stylus

```json
{
  "Stylus": {
    "complexitychecks": [
      "for ",
      "if ",
      "unless ",
      "else ",
      "|| ",
      "&& ",
      "!= ",
      "== "
    ],
    "extensions": [
      "styl"
    ],
    "line_comment": [
      "//"
    ],
    "multi_line": [
      [
        "/*",
        "*/"
      ]
    ],
    "quotes": [
      {
        "end": "\"",
        "start": "\""
      }
    ]
  }
}
```

## Svelte

```json
{
  "Svelte": {
    "complexitychecks": [
      "for ",
      "for(",
      "if ",
      "if(",
      "switch ",
      "while ",
      "else ",
      "|| ",
      "&& ",
      "!= ",
      "== "
    ],
    "extensions": [
      "svelte"
    ],
    "line_comment": [
      "//"
    ],
    "multi_line": [
      [
        "<!--",
        "-->"
      ],
      [
        "/*",
        "*/"
      ]
    ],
    "quotes": [
      {
        "end": "\"",
        "start": "\""
      }
    ]
  }
}
```

## Swift

```json
{
  "Swift": {
    "complexitychecks": [
      "for ",
      "for(",
      "if ",
      "if(",
      "switch ",
      "while ",
      "else ",
      "catch ",
      "guard ",
      "?",
      "|| ",
      "&& ",
      "!= ",
      "== "
    ],
    "extensions": [
      "swift"
    ],
    "line_comment": [
      "//"
    ],
    "multi_line": [
      [
        "/*",
        "*/"
      ]
    ],
    "nestedmultiline": true,
    "quotes": [
      {
        "end": "\"",
        "start": "\""
      }
    ]
  }
}
```

## Swig

```json
{
  "Swig": {
    "complexitychecks": [],
    "extensions": [
      "i"
    ],
    "line_comment": [],
    "multi_line": [
      [
        "/*",
        "*/"
      ]
    ],
    "quotes": [
      {
        "end": "\"",
        "start": "\""
      }
    ]
  }
}
```

## SystemVerilog

```json
{
  "SystemVerilog": {
    "complexitychecks": [
      "for ",
      "for(",
      "if ",
      "if(",
      "switch ",
      "while ",
      "else ",
      "| ",
      "& ",
      "!= ",
      "!== ",
      "== ",
      "foreach ",
      "foreach(",
      "case ",
      "case(",
      "casex ",
      "casex(",
      "casez ",
      "casez(",
      "casexz ",
      "casexz(",
      "fork ",
      " ? ",
      "inside",
      "with",
      "event "
    ],
    "extensions": [
      "sv",
      "svh"
    ],
    "keywords": [
      "endmodule",
      "posedge",
      "edge",
      "always",
      "wire"
    ],
    "line_comment": [
      "//"
    ],
    "multi_line": [
      [
        "/*",
        "*/"
      ]
    ],
    "quotes": [
      {
        "end": "\"",
        "start": "\""
      }
    ]
  }
}
```

## Systemd

```json
{
  "Systemd": {
    "complexitychecks": [],
    "extensions": [
      "automount",
      "device",
      "link",
      "mount",
      "path",
      "scope",
      "service",
      "slice",
      "socket",
      "swap",
      "target",
      "timer"
    ],
    "line_comment": [
      "#"
    ],
    "multi_line": [],
    "quotes": []
  }
}
```

## TCL

```json
{
  "TCL": {
    "complexitychecks": [
      "for ",
      "for(",
      "if ",
      "if(",
      "switch ",
      "while ",
      "else ",
      "|| ",
      "&& ",
      "!= ",
      "== "
    ],
    "extensions": [
      "tcl"
    ],
    "line_comment": [
      "#"
    ],
    "multi_line": [],
    "quotes": [
      {
        "end": "\\\"",
        "start": "\\\""
      },
      {
        "end": "'",
        "start": "'"
      }
    ],
    "shebangs": [
      "tcl"
    ]
  }
}
```

## TL

```json
{
  "TL": {
    "complexitychecks": [],
    "extensions": [
      "tl"
    ],
    "line_comment": [
      "//",
      "///"
    ],
    "multi_line": [
      [
        "/*",
        "*/"
      ]
    ],
    "quotes": []
  }
}
```

## TOML

```json
{
  "TOML": {
    "complexitychecks": [
      "for ",
      "for(",
      "if ",
      "if(",
      "switch ",
      "while ",
      "else ",
      "|| ",
      "&& ",
      "!= ",
      "== "
    ],
    "extensions": [
      "toml"
    ],
    "line_comment": [
      "#"
    ],
    "multi_line": [],
    "quotes": [
      {
        "end": "\\\"",
        "start": "\\\""
      },
      {
        "end": "'",
        "start": "'"
      },
      {
        "end": "\\\"\\\"\\\"",
        "start": "\\\"\\\"\\\""
      },
      {
        "end": "'''",
        "start": "'''"
      }
    ]
  }
}
```

## TTCN-3

```json
{
  "TTCN-3": {
    "complexitychecks": [
      "for ",
      "for(",
      "from ",
      "if ",
      "if(",
      "select ",
      "case ",
      "while ",
      "do ",
      "goto ",
      "stop ",
      "break ",
      "else ",
      "|| ",
      "&& ",
      "!= ",
      "== "
    ],
    "extensions": [
      "ttcn",
      "ttcn3",
      "ttcnpp"
    ],
    "line_comment": [
      "//"
    ],
    "multi_line": [
      [
        "/*",
        "*/"
      ]
    ],
    "quotes": [
      {
        "end": "\"",
        "start": "\""
      }
    ]
  }
}
```

## Tact

```json
{
  "Tact": {
    "complexitychecks": [
      "if ",
      "if(",
      "else ",
      "try ",
      "catch ",
      "catch(",
      "repeat ",
      "repeat(",
      "while ",
      "while(",
      "do ",
      "until ",
      "until(",
      "foreach ",
      "foreach(",
      "|| ",
      "&& ",
      "!= ",
      "== "
    ],
    "extensions": [
      "tact"
    ],
    "line_comment": [
      "//",
      "///"
    ],
    "multi_line": [
      [
        "/*",
        "*/"
      ]
    ],
    "quotes": [
      {
        "end": "\"",
        "start": "\""
      }
    ]
  }
}
```

## TaskPaper

```json
{
  "TaskPaper": {
    "complexitychecks": [],
    "extensions": [
      "taskpaper"
    ],
    "line_comment": [],
    "multi_line": [],
    "quotes": []
  }
}
```

## TeX

```json
{
  "TeX": {
    "complexitychecks": [
      "for ",
      "for(",
      "if ",
      "if(",
      "switch ",
      "while ",
      "else ",
      "|| ",
      "&& ",
      "!= ",
      "== "
    ],
    "extensions": [
      "tex",
      "sty"
    ],
    "line_comment": [
      "%"
    ],
    "multi_line": [],
    "quotes": []
  }
}
```

## Teal

```json
{
  "Teal": {
    "complexitychecks": [
      "loop:",
      "retsub",
      "callsub ",
      "&&",
      "==",
      "||",
      "<=",
      ">="
    ],
    "extensions": [
      "teal"
    ],
    "line_comment": [
      "//"
    ],
    "multi_line": [],
    "quotes": []
  }
}
```

## Templ

```json
{
  "Templ": {
    "complexitychecks": [
      "if ",
      " else ",
      "switch ",
      "case ",
      "default:",
      "for ",
      "|| ",
      "&& ",
      "!= ",
      "== "
    ],
    "extensions": [
      "templ"
    ],
    "line_comment": [
      "//"
    ],
    "multi_line": [
      [
        "/*",
        "*/"
      ]
    ],
    "quotes": [
      {
        "end": "\"",
        "start": "\""
      },
      {
        "end": "`",
        "ignoreEscape": true,
        "start": "`"
      }
    ]
  }
}
```

## TemplateToolkit

```json
{
  "TemplateToolkit": {
    "complexitychecks": [
      "[% BLOCK",
      "[% FILTER",
      "[% FOR",
      "[% FOREACH",
      "[% IF",
      "[% INCLUDE",
      "[% MACRO",
      "[% PROCESS",
      "[% SWITCH",
      "[% UNLESS",
      "[% WRAPPER"
    ],
    "extensions": [
      "tt",
      "tt2"
    ],
    "line_comment": [],
    "multi_line": [
      [
        "[%#",
        "%]"
      ]
    ],
    "quotes": []
  }
}
```

## Tera

```json
{
  "Tera": {
    "complexitychecks": [
      "{% include ",
      "{% macro ",
      "{% block ",
      "{% extends ",
      "{% for ",
      "{% set ",
      "{% if ",
      "{% elif ",
      "{% else "
    ],
    "extensions": [
      "tera"
    ],
    "line_comment": [],
    "multi_line": [
      [
        "<!--",
        "-->"
      ],
      [
        "{#",
        "#}"
      ]
    ],
    "quotes": []
  }
}
```

## Terraform

```json
{
  "Terraform": {
    "complexitychecks": [
      "count",
      "for",
      "for_each",
      "if",
      ": ",
      "? ",
      "|| ",
      "&& ",
      "!= ",
      "> ",
      ">= ",
      "< ",
      "<= ",
      "== "
    ],
    "extensions": [
      "tf",
      "tfvars",
      "tf.json"
    ],
    "line_comment": [
      "#",
      "//"
    ],
    "multi_line": [
      [
        "/*",
        "*/"
      ]
    ],
    "quotes": []
  }
}
```

## Textile

```json
{
  "Textile": {
    "complexitychecks": [],
    "extensions": [
      "textile"
    ],
    "line_comment": [
      "###. "
    ],
    "multi_line": [
      [
        "###.. ",
        "p. "
      ]
    ],
    "quotes": []
  }
}
```

## Thrift

```json
{
  "Thrift": {
    "complexitychecks": [],
    "extensions": [
      "thrift"
    ],
    "line_comment": [
      "//",
      "#"
    ],
    "multi_line": [
      [
        "/*",
        "*/"
      ]
    ],
    "quotes": [
      {
        "end": "\"",
        "start": "\""
      },
      {
        "end": "'",
        "start": "'"
      }
    ]
  }
}
```

## Treetop

```json
{
  "Treetop": {
    "complexitychecks": [
      "for ",
      "for(",
      "if ",
      "if(",
      "switch ",
      "while ",
      "else ",
      "|| ",
      "&& ",
      "!= ",
      "== "
    ],
    "extensions": [
      "treetop",
      "tt"
    ],
    "line_comment": [
      "#"
    ],
    "quotes": [
      {
        "end": "\"",
        "start": "\""
      },
      {
        "end": "'",
        "start": "'"
      }
    ]
  }
}
```

## Twig Template

```json
{
  "Twig Template": {
    "complexitychecks": [
      "{% for ",
      "{% if ",
      "{% else ",
      "{% elseif "
    ],
    "extensions": [
      "twig"
    ],
    "line_comment": [],
    "multi_line": [],
    "quotes": []
  }
}
```

## TypeScript

```json
{
  "TypeScript": {
    "complexitychecks": [
      "for ",
      "for(",
      "if ",
      "if(",
      "switch ",
      "while ",
      "else ",
      "|| ",
      "&& ",
      "!= ",
      "!== ",
      "== ",
      "=== ",
      "case ",
      "case(",
      "?.",
      "?? ",
      "??= "
    ],
    "extensions": [
      "ts",
      "tsx"
    ],
    "line_comment": [
      "//"
    ],
    "multi_line": [
      [
        "/*",
        "*/"
      ]
    ],
    "quotes": [
      {
        "end": "\"",
        "start": "\""
      },
      {
        "end": "'",
        "start": "'"
      },
      {
        "end": "`",
        "start": "`"
      }
    ]
  }
}
```

## TypeScript Typings

```json
{
  "TypeScript Typings": {
    "complexitychecks": [
      "for ",
      "for(",
      "if ",
      "if(",
      "switch ",
      "while ",
      "else ",
      "|| ",
      "&& ",
      "!= ",
      "!== ",
      "== ",
      "=== ",
      "case ",
      "case(",
      "?.",
      "?? ",
      "??= "
    ],
    "extensions": [
      "d.ts"
    ],
    "line_comment": [
      "//"
    ],
    "multi_line": [
      [
        "/*",
        "*/"
      ]
    ],
    "quotes": [
      {
        "end": "\"",
        "start": "\""
      },
      {
        "end": "'",
        "start": "'"
      },
      {
        "end": "`",
        "start": "`"
      }
    ]
  }
}
```

## TypeSpec

```json
{
  "TypeSpec": {
    "complexitychecks": [],
    "extensions": [
      "tsp"
    ],
    "line_comment": [
      "//"
    ],
    "multi_line": [
      [
        "/*",
        "*/"
      ]
    ],
    "quotes": [
      {
        "end": "\"",
        "start": "\""
      },
      {
        "end": "\"\"\"",
        "ignoreEscape": true,
        "start": "\"\"\""
      }
    ]
  }
}
```

## Typst

```json
{
  "Typst": {
    "extensions": [
      "typ"
    ],
    "line_comment": [
      "//"
    ],
    "multi_line": [
      [
        "/*",
        "*/"
      ]
    ],
    "nestedmultiline": true,
    "quotes": [
      {
        "end": "\\\"",
        "start": "\\\""
      }
    ]
  }
}
```

## Unreal Script

```json
{
  "Unreal Script": {
    "complexitychecks": [
      "for ",
      "for(",
      "if ",
      "if(",
      "switch ",
      "while ",
      "else ",
      "|| ",
      "&& ",
      "!= ",
      "== "
    ],
    "extensions": [
      "uc",
      "uci",
      "upkg"
    ],
    "line_comment": [
      "//"
    ],
    "multi_line": [
      [
        "/*",
        "*/"
      ]
    ],
    "quotes": [
      {
        "end": "\"",
        "start": "\""
      }
    ]
  }
}
```

## Up

```json
{
  "Up": {
    "complexitychecks": [
      "for ",
      "if ",
      "switch ",
      "while ",
      "else ",
      "try ",
      "func ",
      "up ",
      "|| ",
      "&& ",
      "!= ",
      "== "
    ],
    "extensions": [
      "up"
    ],
    "line_comment": [
      "//"
    ],
    "multi_line": [],
    "quotes": [
      {
        "end": "\"",
        "start": "\""
      },
      {
        "end": "`",
        "start": "`"
      }
    ]
  }
}
```

## Ur/Web

```json
{
  "Ur/Web": {
    "complexitychecks": [
      "for ",
      "for(",
      "if ",
      "if(",
      "switch ",
      "while ",
      "else ",
      "|| ",
      "&& ",
      "!= ",
      "== "
    ],
    "extensions": [
      "ur",
      "urs"
    ],
    "line_comment": [],
    "multi_line": [
      [
        "(*",
        "*)"
      ]
    ],
    "quotes": [
      {
        "end": "\"",
        "start": "\""
      }
    ]
  }
}
```

## Ur/Web Project

```json
{
  "Ur/Web Project": {
    "complexitychecks": [
      "for ",
      "for(",
      "if ",
      "if(",
      "switch ",
      "while ",
      "else ",
      "|| ",
      "&& ",
      "!= ",
      "== "
    ],
    "extensions": [
      "urp"
    ],
    "line_comment": [
      "#"
    ],
    "multi_line": [],
    "quotes": []
  }
}
```

## V

```json
{
  "V": {
    "complexitychecks": [
      "for ",
      "for(",
      "if ",
      "if(",
      "switch ",
      "while ",
      "else ",
      "|| ",
      "&& ",
      "!= ",
      "== "
    ],
    "extensions": [
      "v"
    ],
    "keywords": [
      "break",
      "const ",
      "continue",
      "defer",
      "else ",
      "enum",
      "fn ",
      "goto",
      "import ",
      "in ",
      "interface",
      "match",
      "mut",
      "println",
      "pub",
      "return",
      "struct ",
      "type "
    ],
    "line_comment": [
      "//"
    ],
    "multi_line": [],
    "quotes": [
      {
        "end": "\"",
        "start": "\""
      },
      {
        "end": "`",
        "start": "`"
      }
    ]
  }
}
```

## VHDL

```json
{
  "VHDL": {
    "complexitychecks": [
      "for ",
      "for(",
      "if ",
      "if(",
      "switch ",
      "while ",
      "else ",
      "|| ",
      "&& ",
      "!= ",
      "== "
    ],
    "extensions": [
      "vhd",
      "vhdl"
    ],
    "keywords": [
      "abs",
      "access",
      "after",
      "alias",
      "all",
      "and",
      "architecture",
      "array",
      "assert",
      "attribute",
      "begin",
      "block",
      "body",
      "buffer",
      "bus",
      "case",
      "component",
      "configuration",
      "constant",
      "disconnect",
      "downto",
      "else",
      "elsif",
      "end",
      "entity",
      "exit",
      "file",
      "for",
      "function",
      "generate",
      "generic",
      "group",
      "guarded",
      "if",
      "impure",
      "in",
      "inertial",
      "inout",
      "is",
      "label",
      "library",
      "linkage",
      "literal",
      "loop",
      "map",
      "mod",
      "nand",
      "new",
      "next",
      "nor",
      "not",
      "null",
      "of",
      "on",
      "open",
      "or",
      "others",
      "out",
      "package",
      "port",
      "postponed",
      "procedure",
      "process",
      "pure",
      "range",
      "record",
      "register",
      "reject",
      "rem",
      "report",
      "return",
      "rol",
      "ror",
      "select",
      "severity",
      "shared",
      "signal",
      "sla",
      "sll",
      "sra",
      "srl",
      "subtype",
      "then",
      "to",
      "transport",
      "type",
      "unaffected",
      "units",
      "until",
      "use",
      "variable",
      "wait",
      "when",
      "while",
      "with",
      "xnor",
      "xor"
    ],
    "line_comment": [
      "--"
    ],
    "multi_line": [],
    "quotes": []
  }
}
```

## Vala

```json
{
  "Vala": {
    "complexitychecks": [
      "for ",
      "for(",
      "foreach ",
      "foreach(",
      "if ",
      "if(",
      "switch ",
      "switch(",
      "while ",
      "while(",
      "else ",
      "|| ",
      "&& ",
      "!= ",
      "== "
    ],
    "extensions": [
      "vala"
    ],
    "line_comment": [
      "//"
    ],
    "multi_line": [
      [
        "/*",
        "*/"
      ]
    ],
    "quotes": [
      {
        "end": "\"",
        "start": "\""
      },
      {
        "end": "\"",
        "start": "@\""
      },
      {
        "ignoreEscape": true,
        "end": "\"\"\"",
        "start": "\"\"\""
      }
    ]
  }
}
```

## Varnish Configuration

```json
{
  "Varnish Configuration": {
    "complexitychecks": [],
    "extensions": [
      "vcl"
    ],
    "line_comment": [
      "#",
      "//"
    ],
    "multi_line": [
      [
        "/*",
        "*/"
      ]
    ],
    "quotes": []
  }
}
```

## Verilog

```json
{
  "Verilog": {
    "complexitychecks": [
      "for ",
      "for(",
      "if ",
      "if(",
      "switch ",
      "while ",
      "else ",
      "|| ",
      "&& ",
      "!= ",
      "== "
    ],
    "extensions": [
      "vg",
      "vh",
      "v"
    ],
    "keywords": [
      "module",
      "endmodule",
      "timescale",
      "input",
      "output",
      "reg",
      "wire",
      "posedge",
      "negedge",
      "always",
      "begin",
      "switch",
      "case",
      "end",
      "endcase",
      "else",
      "localparam",
      "initial",
      "signed",
      "assign",
      "generate",
      "genvar"
    ],
    "line_comment": [
      "//"
    ],
    "multi_line": [
      [
        "/*",
        "*/"
      ]
    ],
    "quotes": [
      {
        "end": "\"",
        "start": "\""
      }
    ]
  }
}
```

## Verilog Args File

```json
{
  "Verilog Args File": {
    "complexitychecks": [],
    "extensions": [
      "irunargs",
      "xrunargs"
    ],
    "line_comment": [],
    "multi_line": [],
    "quotes": []
  }
}
```

## Vertex Shader File

```json
{
  "Vertex Shader File": {
    "complexitychecks": [
      "for ",
      "for(",
      "if ",
      "if(",
      "switch ",
      "while ",
      "else ",
      "|| ",
      "&& ",
      "!= ",
      "== "
    ],
    "extensions": [
      "vsh"
    ],
    "line_comment": [
      "//"
    ],
    "multi_line": [
      [
        "/*",
        "*/"
      ]
    ],
    "quotes": [
      {
        "end": "\"",
        "start": "\""
      }
    ]
  }
}
```

## Vim Script

```json
{
  "Vim Script": {
    "complexitychecks": [
      "for ",
      "for(",
      "if ",
      "if(",
      "switch ",
      "while ",
      "else ",
      "|| ",
      "&& ",
      "!= ",
      "== "
    ],
    "extensions": [
      "vim",
      "vimrc",
      "gvimrc"
    ],
    "filenames": [
      "_vimrc",
      ".vimrc",
      "_gvimrc",
      ".gvimrc",
      "vimrc",
      "gvimrc"
    ],
    "line_comment": [
      "\"",
      "#"
    ],
    "multi_line": [],
    "quotes": [
      {
        "end": "\\\"",
        "start": "\\\""
      },
      {
        "end": "'",
        "start": "'"
      }
    ]
  }
}
```

## Visual Basic

```json
{
  "Visual Basic": {
    "complexitychecks": [
      "for ",
      "for(",
      "if ",
      "if(",
      "elseif ",
      "switch ",
      "while ",
      "else ",
      "|| ",
      "&& ",
      "!= ",
      "== "
    ],
    "extensions": [
      "vb"
    ],
    "line_comment": [
      "'"
    ],
    "multi_line": [],
    "quotes": [
      {
        "end": "\\\"",
        "start": "\\\""
      }
    ]
  }
}
```

## Visual Basic for Applications

```json
{
  "Visual Basic for Applications": {
    "complexitychecks": [
      "for ",
      "for(",
      "if ",
      "if(",
      "elseif ",
      "switch ",
      "while ",
      "else ",
      "|| ",
      "&& ",
      "!= ",
      "== "
    ],
    "extensions": [
      "cls"
    ],
    "line_comment": [
      "'"
    ],
    "multi_line": [],
    "quotes": [
      {
        "end": "\\\"",
        "start": "\\\""
      }
    ]
  }
}
```

## Vue

```json
{
  "Vue": {
    "complexitychecks": [
      "for ",
      "for(",
      "if ",
      "if(",
      "switch ",
      "while ",
      "else ",
      "|| ",
      "&& ",
      "!= ",
      "== "
    ],
    "extensions": [
      "vue"
    ],
    "line_comment": [
      "//"
    ],
    "multi_line": [
      [
        "<!--",
        "-->"
      ],
      [
        "/*",
        "*/"
      ]
    ],
    "quotes": [
      {
        "end": "\"",
        "start": "\""
      },
      {
        "end": "'",
        "start": "'"
      }
    ]
  }
}
```

## W.I.S.E. Jobfile

```json
{
  "W.I.S.E. Jobfile": {
    "complexitychecks": [],
    "extensions": [
      "fgmj"
    ],
    "line_comment": [],
    "multi_line": [],
    "quotes": []
  }
}
```

## Web Services Description Language

```json
{
  "Web Services Description Language": {
    "extensions": [
      "wsdl"
    ],
    "line_comment": [],
    "multi_line": [
      [
        "<!--",
        "-->"
      ]
    ],
    "quotes": [
      {
        "end": "\"",
        "start": "\""
      }
    ]
  }
}
```

## WebGPU Shading Language

```json
{
  "WebGPU Shading Language": {
    "complexitychecks": [
      "for (",
      "for(",
      "if ",
      "if(",
      "switch ",
      "while ",
      "while(",
      "else ",
      "|| ",
      "&& ",
      "!= ",
      "== "
    ],
    "extensions": [
      "wgsl"
    ],
    "line_comment": [
      "//"
    ],
    "multi_line": [
      [
        "/*",
        "*/"
      ]
    ]
  }
}
```

## Windows Resource-Definition Script

```json
{
  "Windows Resource-Definition Script": {
    "extensions": [
      "rc"
    ],
    "keywords": [
      "#include",
      "#define",
      "RC_INVOKED",
      "VERSIONINFO",
      "FILEVERSION",
      "PRODUCTVERSION",
      "FILEOS",
      "FILETYPE",
      "BLOCK",
      "VALUE",
      "StringFileInfo",
      "VarFileInfo"
    ],
    "line_comment": [
      "//"
    ],
    "multi_line": [
      [
        "/*",
        "*/"
      ]
    ],
    "quotes": [
      {
        "end": "\"",
        "start": "\""
      }
    ]
  }
}
```

## Wolfram

```json
{
  "Wolfram": {
    "complexitychecks": [
      "for ",
      "for(",
      "if ",
      "if(",
      "switch ",
      "while ",
      "else ",
      "|| ",
      "&& ",
      "!= ",
      "== "
    ],
    "extensions": [
      "nb",
      "wl"
    ],
    "line_comment": [],
    "multi_line": [
      [
        "(*",
        "*)"
      ]
    ],
    "quotes": [
      {
        "end": "\"",
        "start": "\""
      }
    ]
  }
}
```

## Wren

```json
{
  "Wren": {
    "complexitychecks": [
      "for ",
      "for(",
      "if ",
      "if(",
      "switch ",
      "while ",
      "else ",
      "|| ",
      "&& ",
      "!= ",
      "== "
    ],
    "extensions": [
      "wren"
    ],
    "line_comment": [
      "//"
    ],
    "multi_line": [
      [
        "/*",
        "*/"
      ]
    ],
    "nestedmultiline": true,
    "quotes": [
      {
        "end": "\"",
        "start": "\""
      }
    ]
  }
}
```

## XAML

```json
{
  "XAML": {
    "complexitychecks": [
      "for ",
      "for(",
      "if ",
      "if(",
      "switch ",
      "while ",
      "else ",
      "|| ",
      "&& ",
      "!= ",
      "== "
    ],
    "extensions": [
      "xaml"
    ],
    "line_comment": [],
    "multi_line": [
      [
        "<!--",
        "-->"
      ]
    ],
    "quotes": [
      {
        "end": "\"",
        "start": "\""
      }
    ]
  }
}
```

## XML

```json
{
  "XML": {
    "extensions": [
      "xml"
    ],
    "line_comment": [],
    "multi_line": [
      [
        "<!--",
        "-->"
      ]
    ],
    "quotes": [
      {
        "end": "\"",
        "start": "\""
      }
    ]
  }
}
```

## XML Schema

```json
{
  "XML Schema": {
    "complexitychecks": [],
    "extensions": [
      "xsd"
    ],
    "line_comment": [],
    "multi_line": [],
    "quotes": []
  }
}
```

## XMake

```json
{
  "XMake": {
    "complexitychecks": [
      "for ",
      "for(",
      "if ",
      "if(",
      "while ",
      "while(",
      "else ",
      "else(",
      "elseif ",
      "elseif(",
      "until ",
      "until(",
      "or ",
      "and ",
      "~= ",
      "== "
    ],
    "extensions": [],
    "filenames": [
      "xmake.lua",
      "xpack.lua"
    ],
    "line_comment": [
      "--"
    ],
    "multi_line": [
      [
        "--[[",
        "]]"
      ],
      [
        "--[=[",
        "]=]"
      ],
      [
        "--[==[",
        "]==]"
      ],
      [
        "--[===[",
        "]===]"
      ],
      [
        "--[====[",
        "]====]"
      ],
      [
        "--[=====[",
        "]=====]"
      ]
    ],
    "quotes": [
      {
        "end": "\"",
        "start": "\""
      },
      {
        "end": "[[",
        "start": "]]",
        "ignoreEscape": true
      }
    ]
  }
}
```

## Xcode Config

```json
{
  "Xcode Config": {
    "complexitychecks": [],
    "extensions": [
      "xcconfig"
    ],
    "line_comment": [
      "//"
    ],
    "multi_line": [],
    "quotes": []
  }
}
```

## Xtend

```json
{
  "Xtend": {
    "complexitychecks": [
      "for ",
      "for(",
      "if ",
      "if(",
      "switch ",
      "while ",
      "else ",
      "|| ",
      "&& ",
      "!= ",
      "== "
    ],
    "extensions": [
      "xtend"
    ],
    "line_comment": [
      "//"
    ],
    "multi_line": [
      [
        "/*",
        "*/"
      ]
    ],
    "quotes": [
      {
        "end": "\"",
        "start": "\""
      }
    ]
  }
}
```

## YAML

```json
{
  "YAML": {
    "complexitychecks": [],
    "extensions": [
      "yaml",
      "yml"
    ],
    "line_comment": [
      "#"
    ],
    "multi_line": [],
    "quotes": []
  }
}
```

## Yarn

```json
{
  "Yarn": {
    "complexitychecks": [
      "<<if ",
      "<<elseif ",
      "<<else ",
      " eq ",
      " == ",
      " neq ",
      " ! ",
      " gt ",
      " > ",
      " lt ",
      " < ",
      " lte ",
      " <= ",
      " gte ",
      " >= ",
      " xor ",
      " ^ ",
      " and ",
      " && ",
      " || ",
      " or "
    ],
    "extensions": [
      "yarn"
    ],
    "line_comment": [],
    "quotes": []
  }
}
```

## Zig

```json
{
  "Zig": {
    "complexitychecks": [
      "catch ",
      "while ",
      "for ",
      "if ",
      "else ",
      "errdefer ",
      "try ",
      "switch ",
      "orelse ",
      "||",
      "&&",
      "!=",
      "=="
    ],
    "extensions": [
      "zig"
    ],
    "line_comment": [
      "//"
    ],
    "quotes": [
      {
        "end": "\\\"",
        "start": "\\\""
      },
      {
        "end": "\n",
        "start": "\\\\"
      }
    ]
  }
}
```

## ZoKrates

```json
{
  "ZoKrates": {
    "complexitychecks": [
      "for ",
      "if ",
      "switch ",
      "while ",
      "else ",
      "|| ",
      "&& ",
      "!= ",
      "== "
    ],
    "extensions": [
      "zok"
    ],
    "line_comment": [
      "//"
    ],
    "multi_line": [
      [
        "/*",
        "*/"
      ]
    ]
  }
}
```

## Zsh

```json
{
  "Zsh": {
    "complexitychecks": [
      "for ",
      "for(",
      "if ",
      "if(",
      "switch ",
      "while ",
      "else ",
      "|| ",
      "&& ",
      "!= ",
      "== "
    ],
    "extensions": [
      "zsh",
      "zshenv",
      "zlogin",
      "zlogout",
      "zprofile",
      "zshrc"
    ],
    "filenames": [
      ".zshenv",
      ".zlogin",
      ".zlogout",
      ".zprofile",
      ".zshrc"
    ],
    "line_comment": [
      "#"
    ],
    "multi_line": [],
    "quotes": [
      {
        "end": "\\\"",
        "start": "\\\""
      },
      {
        "end": "'",
        "start": "'"
      }
    ],
    "shebangs": [
      "zsh"
    ]
  }
}
```

## bait

```json
{
  "bait": {
    "complexitychecks": [
      "for ",
      "if ",
      "else ",
      " or ",
      " and ",
      "!= ",
      "== "
    ],
    "extensions": [
      "bt"
    ],
    "keywords": [
      "and",
      "break",
      "const ",
      "continue",
      "else ",
      "fun ",
      "import ",
      "not ",
      "or ",
      "package ",
      "return",
      "struct "
    ],
    "line_comment": [
      "//"
    ],
    "multi_line": [
      [
        "/*",
        "*/"
      ]
    ],
    "nestedmultiline": true,
    "quotes": [
      {
        "end": "'",
        "start": "'"
      },
      {
        "end": "\"",
        "start": "\""
      },
      {
        "end": "`",
        "start": "`"
      }
    ]
  }
}
```

## gitignore

```json
{
  "gitignore": {
    "complexitychecks": [],
    "extensions": [],
    "filenames": [
      ".gitignore"
    ],
    "line_comment": [
      "#"
    ],
    "multi_line": [],
    "quotes": []
  }
}
```

## hoon

```json
{
  "hoon": {
    "complexitychecks": [
      "%+  turn",
      "(turn ",
      "%+  roll",
      "(roll ",
      "%+  reel",
      "(reel ",
      "|.  ",
      "|.(",
      "|-  ",
      "|-(",
      "|?  ",
      "|?(",
      "?|  ",
      "?|(",
      "|(",
      "?-  ",
      "?-(",
      "?:  ",
      "?:(",
      "?.  ",
      "?.(",
      "?^  ",
      "?^(",
      "?<  ",
      "?<(",
      "?>  ",
      "?>(",
      "?+  ",
      "?+(",
      "?&  ",
      "?&(",
      "&(",
      "?@  ",
      "?@(",
      "?~  ",
      "?~(",
      "?=  ",
      "?=(",
      ".=  ",
      "=(",
      "!=("
    ],
    "extensions": [
      "hoon"
    ],
    "line_comment": [
      "::"
    ],
    "multi_line": [],
    "quotes": [
      {
        "end": "\"",
        "start": "\""
      },
      {
        "end": "'",
        "start": "'"
      },
      {
        "end": "```",
        "start": "```"
      }
    ]
  }
}
```

## ignore

```json
{
  "ignore": {
    "complexitychecks": [],
    "extensions": [],
    "filenames": [
      ".ignore"
    ],
    "line_comment": [
      "#"
    ],
    "multi_line": [],
    "quotes": []
  }
}
```

## jq

```json
{
  "jq": {
    "complexitychecks": [
      ".",
      "if ",
      "elif ",
      "else ",
      "!= ",
      "== ",
      ">= ",
      "<= ",
      "< ",
      "> ",
      "and ",
      "or ",
      "not ",
      "// ",
      "try ",
      "break "
    ],
    "extensions": [
      "jq"
    ],
    "line_comment": [
      "#"
    ],
    "multi_line": [],
    "quotes": [
      {
        "end": "\"",
        "start": "\""
      }
    ]
  }
}
```

## m4

```json
{
  "m4": {
    "complexitychecks": [],
    "extensions": [
      "m4"
    ],
    "line_comment": [
      "#"
    ],
    "multi_line": [],
    "quotes": []
  }
}
```

## nuspec

```json
{
  "nuspec": {
    "extensions": [
      "nuspec"
    ],
    "line_comment": [],
    "multi_line": [
      [
        "<!--",
        "-->"
      ]
    ],
    "quotes": [
      {
        "end": "\"",
        "start": "\""
      }
    ]
  }
}
```

## sed

```json
{
  "sed": {
    "complexitychecks": [
      "for ",
      "for(",
      "if ",
      "if(",
      "switch ",
      "while ",
      "else ",
      "and ",
      "or ",
      "not ",
      "in "
    ],
    "extensions": [
      "sed"
    ],
    "line_comment": [
      "#"
    ],
    "multi_line": [],
    "quotes": [],
    "shebangs": [
      "sed"
    ]
  }
}
```

## wenyan

```json
{
  "wenyan": {
    "complexitychecks": [
      "\u82e5",
      "\u82e5\u975e",
      "\u7b49\u65bc",
      "\u4e0d\u7b49\u65bc",
      "\u4e0d\u5927\u65bc",
      "\u4e0d\u5c0f\u65bc",
      "\u5927\u65bc",
      "\u5c0f\u65bc",
      "\u51e1",
      "\u70ba\u662f",
      "\u6046\u70ba\u662f",
      "\u4e2d\u4e4b",
      "\u904d"
    ],
    "extensions": [
      "wy"
    ],
    "line_comment": [
      "\u6279\u66f0",
      "\u6ce8\u66f0",
      "\u758f\u66f0"
    ],
    "multi_line": [],
    "quotes": [
      {
        "end": "\u300c\u300c",
        "start": "\u300d\u300d"
      }
    ]
  }
}
```

