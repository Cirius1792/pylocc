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
    "extensions": [
      "abap"
    ],
    "line_comment": [
      "*",
      "\\\""
    ],
    "multi_line": []
  }
}
```

## ABNF

```json
{
  "ABNF": {
    "extensions": [
      "abnf"
    ],
    "line_comment": [
      ";"
    ],
    "multi_line": []
  }
}
```

## APL

```json
{
  "APL": {
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
    "multi_line": []
  }
}
```

## ASP

```json
{
  "ASP": {
    "extensions": [
      "asa",
      "asp"
    ],
    "line_comment": [
      "'",
      "REM"
    ],
    "multi_line": []
  }
}
```

## ASP.NET

```json
{
  "ASP.NET": {
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
    ]
  }
}
```

## ATS

```json
{
  "ATS": {
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
    ]
  }
}
```

## AWK

```json
{
  "AWK": {
    "extensions": [
      "awk"
    ],
    "line_comment": [
      "#"
    ],
    "multi_line": []
  }
}
```

## ActionScript

```json
{
  "ActionScript": {
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
    ]
  }
}
```

## Ada

```json
{
  "Ada": {
    "extensions": [
      "ada",
      "adb",
      "ads",
      "pad"
    ],
    "line_comment": [
      "--"
    ],
    "multi_line": []
  }
}
```

## Agda

```json
{
  "Agda": {
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
    ]
  }
}
```

## Alchemist

```json
{
  "Alchemist": {
    "extensions": [
      "crn"
    ],
    "line_comment": [
      "#"
    ],
    "multi_line": []
  }
}
```

## Alex

```json
{
  "Alex": {
    "extensions": [
      "x"
    ],
    "line_comment": [],
    "multi_line": []
  }
}
```

## Alloy

```json
{
  "Alloy": {
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
    ]
  }
}
```

## Android Interface Definition Language

```json
{
  "Android Interface Definition Language": {
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
    ]
  }
}
```

## AppleScript

```json
{
  "AppleScript": {
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
    ]
  }
}
```

## Arturo

```json
{
  "Arturo": {
    "extensions": [
      "art"
    ],
    "line_comment": [
      ";"
    ],
    "multi_line": []
  }
}
```

## AsciiDoc

```json
{
  "AsciiDoc": {
    "extensions": [
      "adoc"
    ],
    "line_comment": [],
    "multi_line": []
  }
}
```

## Assembly

```json
{
  "Assembly": {
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
    ]
  }
}
```

## Astro

```json
{
  "Astro": {
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
    ]
  }
}
```

## AutoHotKey

```json
{
  "AutoHotKey": {
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
    ]
  }
}
```

## Autoconf

```json
{
  "Autoconf": {
    "extensions": [
      "in"
    ],
    "line_comment": [
      "#",
      "dnl"
    ],
    "multi_line": []
  }
}
```

## Avro

```json
{
  "Avro": {
    "extensions": [
      "avdl",
      "avpr",
      "avsc"
    ],
    "line_comment": [],
    "multi_line": []
  }
}
```

## BASH

```json
{
  "BASH": {
    "extensions": [
      "bash",
      "bash_login",
      "bash_logout",
      "bash_profile",
      "bashrc"
    ],
    "line_comment": [
      "#"
    ],
    "multi_line": []
  }
}
```

## Basic

```json
{
  "Basic": {
    "extensions": [
      "bas"
    ],
    "line_comment": [
      "'"
    ],
    "multi_line": []
  }
}
```

## Batch

```json
{
  "Batch": {
    "extensions": [
      "bat",
      "btm",
      "cmd"
    ],
    "line_comment": [
      "REM",
      "::"
    ],
    "multi_line": []
  }
}
```

## Bazel

```json
{
  "Bazel": {
    "extensions": [
      "bzl",
      "build.bazel",
      "build",
      "workspace"
    ],
    "line_comment": [
      "#"
    ],
    "multi_line": []
  }
}
```

## Bean

```json
{
  "Bean": {
    "extensions": [
      "bean",
      "beancount"
    ],
    "line_comment": [
      ";"
    ],
    "multi_line": []
  }
}
```

## Bicep

```json
{
  "Bicep": {
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
    ]
  }
}
```

## Bitbake

```json
{
  "Bitbake": {
    "extensions": [
      "bb",
      "bbappend",
      "bbclass"
    ],
    "line_comment": [
      "#"
    ],
    "multi_line": []
  }
}
```

## Bitbucket Pipeline

```json
{
  "Bitbucket Pipeline": {
    "extensions": [
      "bitbucket-pipelines.yml"
    ],
    "line_comment": [
      "#"
    ],
    "multi_line": []
  }
}
```

## Blade template

```json
{
  "Blade template": {
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
    ]
  }
}
```

## Blueprint

```json
{
  "Blueprint": {
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
    ]
  }
}
```

## Boo

```json
{
  "Boo": {
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
    ]
  }
}
```

## Bosque

```json
{
  "Bosque": {
    "extensions": [
      "bsq"
    ],
    "line_comment": [
      "//"
    ],
    "multi_line": []
  }
}
```

## Brainfuck

```json
{
  "Brainfuck": {
    "extensions": [
      "bf"
    ],
    "line_comment": [],
    "multi_line": []
  }
}
```

## BuildStream

```json
{
  "BuildStream": {
    "extensions": [
      "bst"
    ],
    "line_comment": [
      "#"
    ],
    "multi_line": []
  }
}
```

## C

```json
{
  "C": {
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
    ]
  }
}
```

## C Header

```json
{
  "C Header": {
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
    ]
  }
}
```

## C Shell

```json
{
  "C Shell": {
    "extensions": [
      "csh"
    ],
    "line_comment": [
      "#"
    ],
    "multi_line": []
  }
}
```

## C#

```json
{
  "C#": {
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
    ]
  }
}
```

## C++

```json
{
  "C++": {
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
    ]
  }
}
```

## C++ Header

```json
{
  "C++ Header": {
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
    ]
  }
}
```

## C3

```json
{
  "C3": {
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
    ]
  }
}
```

## CMake

```json
{
  "CMake": {
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
    ]
  }
}
```

## COBOL

```json
{
  "COBOL": {
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
    "multi_line": []
  }
}
```

## CSS

```json
{
  "CSS": {
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
    ]
  }
}
```

## CSV

```json
{
  "CSV": {
    "extensions": [
      "csv"
    ],
    "line_comment": [],
    "multi_line": []
  }
}
```

## Cabal

```json
{
  "Cabal": {
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
    ]
  }
}
```

## Cairo

```json
{
  "Cairo": {
    "extensions": [
      "cairo"
    ],
    "line_comment": [
      "//"
    ],
    "multi_line": []
  }
}
```

## Cangjie

```json
{
  "Cangjie": {
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
    ]
  }
}
```

## Cap'n Proto

```json
{
  "Cap'n Proto": {
    "extensions": [
      "capnp"
    ],
    "line_comment": [
      "#"
    ],
    "multi_line": []
  }
}
```

## Cassius

```json
{
  "Cassius": {
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
    ]
  }
}
```

## Ceylon

```json
{
  "Ceylon": {
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
    ]
  }
}
```

## Chapel

```json
{
  "Chapel": {
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
    ]
  }
}
```

## Circom

```json
{
  "Circom": {
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
    ]
  }
}
```

## Clipper

```json
{
  "Clipper": {
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
    ]
  }
}
```

## Clojure

```json
{
  "Clojure": {
    "extensions": [
      "clj",
      "cljc"
    ],
    "line_comment": [
      ";"
    ],
    "multi_line": []
  }
}
```

## ClojureScript

```json
{
  "ClojureScript": {
    "extensions": [
      "cljs"
    ],
    "line_comment": [
      ";"
    ],
    "multi_line": []
  }
}
```

## Closure Template

```json
{
  "Closure Template": {
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
    ]
  }
}
```

## CloudFormation (JSON)

```json
{
  "CloudFormation (JSON)": {
    "extensions": [
      "json"
    ],
    "line_comment": [],
    "multi_line": []
  }
}
```

## CloudFormation (YAML)

```json
{
  "CloudFormation (YAML)": {
    "extensions": [
      "yaml",
      "yml"
    ],
    "line_comment": [
      "#"
    ],
    "multi_line": []
  }
}
```

## CodeQL

```json
{
  "CodeQL": {
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
    ]
  }
}
```

## CoffeeScript

```json
{
  "CoffeeScript": {
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
    ]
  }
}
```

## Cogent

```json
{
  "Cogent": {
    "extensions": [
      "cogent"
    ],
    "line_comment": [
      "--"
    ],
    "multi_line": []
  }
}
```

## ColdFusion

```json
{
  "ColdFusion": {
    "extensions": [
      "cfm"
    ],
    "line_comment": [],
    "multi_line": [
      [
        "<!---",
        "--->"
      ]
    ]
  }
}
```

## ColdFusion CFScript

```json
{
  "ColdFusion CFScript": {
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
    ]
  }
}
```

## Coq

```json
{
  "Coq": {
    "extensions": [
      "v"
    ],
    "line_comment": [],
    "multi_line": [
      [
        "(*",
        "*)"
      ]
    ]
  }
}
```

## Creole

```json
{
  "Creole": {
    "extensions": [
      "creole"
    ],
    "line_comment": [],
    "multi_line": []
  }
}
```

## Crystal

```json
{
  "Crystal": {
    "extensions": [
      "cr"
    ],
    "line_comment": [
      "#"
    ],
    "multi_line": []
  }
}
```

## Cuda

```json
{
  "Cuda": {
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
    ]
  }
}
```

## Cython

```json
{
  "Cython": {
    "extensions": [
      "pyx",
      "pxi",
      "pxd"
    ],
    "line_comment": [
      "#"
    ],
    "multi_line": []
  }
}
```

## D

```json
{
  "D": {
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
    ]
  }
}
```

## DAML

```json
{
  "DAML": {
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
    ]
  }
}
```

## DM

```json
{
  "DM": {
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
    ]
  }
}
```

## DOT

```json
{
  "DOT": {
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
    ]
  }
}
```

## Dart

```json
{
  "Dart": {
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
    ]
  }
}
```

## Device Tree

```json
{
  "Device Tree": {
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
    ]
  }
}
```

## Dhall

```json
{
  "Dhall": {
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
    ]
  }
}
```

## Docker ignore

```json
{
  "Docker ignore": {
    "extensions": [],
    "line_comment": [
      "#",
      "//"
    ],
    "multi_line": []
  }
}
```

## Dockerfile

```json
{
  "Dockerfile": {
    "extensions": [
      "dockerfile"
    ],
    "line_comment": [
      "#"
    ],
    "multi_line": []
  }
}
```

## Document Type Definition

```json
{
  "Document Type Definition": {
    "extensions": [
      "dtd"
    ],
    "line_comment": [],
    "multi_line": []
  }
}
```

## Elixir

```json
{
  "Elixir": {
    "extensions": [
      "ex",
      "exs"
    ],
    "line_comment": [
      "#"
    ],
    "multi_line": []
  }
}
```

## Elixir Template

```json
{
  "Elixir Template": {
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
    ]
  }
}
```

## Elm

```json
{
  "Elm": {
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
    ]
  }
}
```

## Emacs Dev Env

```json
{
  "Emacs Dev Env": {
    "extensions": [
      "ede"
    ],
    "line_comment": [
      ";"
    ],
    "multi_line": []
  }
}
```

## Emacs Lisp

```json
{
  "Emacs Lisp": {
    "extensions": [
      "el"
    ],
    "line_comment": [
      ";"
    ],
    "multi_line": []
  }
}
```

## EmiT

```json
{
  "EmiT": {
    "extensions": [
      "emit"
    ],
    "line_comment": [
      "//"
    ],
    "multi_line": []
  }
}
```

## Erlang

```json
{
  "Erlang": {
    "extensions": [
      "erl",
      "hrl"
    ],
    "line_comment": [
      "%"
    ],
    "multi_line": []
  }
}
```

## Expect

```json
{
  "Expect": {
    "extensions": [
      "exp"
    ],
    "line_comment": [
      "#"
    ],
    "multi_line": []
  }
}
```

## Extensible Stylesheet Language Transformations

```json
{
  "Extensible Stylesheet Language Transformations": {
    "extensions": [
      "xslt",
      "xsl"
    ],
    "line_comment": [],
    "multi_line": []
  }
}
```

## F#

```json
{
  "F#": {
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
    ]
  }
}
```

## F*

```json
{
  "F*": {
    "extensions": [
      "fst"
    ],
    "line_comment": [],
    "multi_line": [
      [
        "(*",
        "*)"
      ]
    ]
  }
}
```

## FIDL

```json
{
  "FIDL": {
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
    ]
  }
}
```

## FORTRAN Legacy

```json
{
  "FORTRAN Legacy": {
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
    "multi_line": []
  }
}
```

## FSL

```json
{
  "FSL": {
    "extensions": [
      "fsl"
    ],
    "line_comment": [
      "//"
    ],
    "multi_line": []
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
    ]
  }
}
```

## Factor

```json
{
  "Factor": {
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
    ]
  }
}
```

## Fennel

```json
{
  "Fennel": {
    "extensions": [
      "fnl"
    ],
    "line_comment": [
      ";"
    ],
    "multi_line": []
  }
}
```

## Fish

```json
{
  "Fish": {
    "extensions": [
      "fish"
    ],
    "line_comment": [
      "#"
    ],
    "multi_line": []
  }
}
```

## Flow9

```json
{
  "Flow9": {
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
    ]
  }
}
```

## Forth

```json
{
  "Forth": {
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
    ]
  }
}
```

## Fortran Modern

```json
{
  "Fortran Modern": {
    "extensions": [
      "f03",
      "f08",
      "f90",
      "f95"
    ],
    "line_comment": [
      "!"
    ],
    "multi_line": []
  }
}
```

## Fragment Shader File

```json
{
  "Fragment Shader File": {
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
    ]
  }
}
```

## Freemarker Template

```json
{
  "Freemarker Template": {
    "extensions": [
      "ftl"
    ],
    "line_comment": [],
    "multi_line": [
      [
        "<#--",
        "-->"
      ]
    ]
  }
}
```

## Futhark

```json
{
  "Futhark": {
    "extensions": [
      "fut"
    ],
    "line_comment": [
      "--"
    ],
    "multi_line": []
  }
}
```

## GDScript

```json
{
  "GDScript": {
    "extensions": [
      "gd"
    ],
    "line_comment": [
      "#"
    ],
    "multi_line": []
  }
}
```

## GLSL

```json
{
  "GLSL": {
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
    ]
  }
}
```

## GN

```json
{
  "GN": {
    "extensions": [
      "gn",
      "gni"
    ],
    "line_comment": [
      "#"
    ],
    "multi_line": []
  }
}
```

## Game Maker Language

```json
{
  "Game Maker Language": {
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
    ]
  }
}
```

## Game Maker Project

```json
{
  "Game Maker Project": {
    "extensions": [
      "yyp"
    ],
    "line_comment": [],
    "multi_line": []
  }
}
```

## Gemfile

```json
{
  "Gemfile": {
    "extensions": [],
    "line_comment": [
      "#"
    ],
    "multi_line": []
  }
}
```

## Gherkin Specification

```json
{
  "Gherkin Specification": {
    "extensions": [
      "feature"
    ],
    "line_comment": [
      "#"
    ],
    "multi_line": []
  }
}
```

## Gleam

```json
{
  "Gleam": {
    "extensions": [
      "gleam"
    ],
    "line_comment": [
      "//",
      "///",
      "////"
    ],
    "multi_line": []
  }
}
```

## Go

```json
{
  "Go": {
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
    ]
  }
}
```

## Go Template

```json
{
  "Go Template": {
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
    ]
  }
}
```

## Go+

```json
{
  "Go+": {
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
    ]
  }
}
```

## Godot Scene

```json
{
  "Godot Scene": {
    "extensions": [
      "tscn"
    ],
    "line_comment": [],
    "multi_line": []
  }
}
```

## Gradle

```json
{
  "Gradle": {
    "extensions": [
      "gradle"
    ],
    "line_comment": [
      "//"
    ],
    "multi_line": []
  }
}
```

## GraphQL

```json
{
  "GraphQL": {
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
    ]
  }
}
```

## Groovy

```json
{
  "Groovy": {
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
    ]
  }
}
```

## Gwion

```json
{
  "Gwion": {
    "extensions": [
      "gw"
    ],
    "line_comment": [
      "#!"
    ],
    "multi_line": []
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
    "multi_line": []
  }
}
```

## HCL

```json
{
  "HCL": {
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
    ]
  }
}
```

## HEEx

```json
{
  "HEEx": {
    "extensions": [
      "heex"
    ],
    "line_comment": [],
    "multi_line": [
      [
        "<%!--",
        "--%>"
      ]
    ]
  }
}
```

## HEX

```json
{
  "HEX": {
    "extensions": [
      "hex"
    ],
    "line_comment": [],
    "multi_line": []
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
    ]
  }
}
```

## Hamlet

```json
{
  "Hamlet": {
    "extensions": [
      "hamlet"
    ],
    "line_comment": [],
    "multi_line": [
      [
        "<!--",
        "-->"
      ]
    ]
  }
}
```

## Handlebars

```json
{
  "Handlebars": {
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
    ]
  }
}
```

## Happy

```json
{
  "Happy": {
    "extensions": [
      "y",
      "ly"
    ],
    "line_comment": [],
    "multi_line": []
  }
}
```

## Hare

```json
{
  "Hare": {
    "extensions": [
      "ha"
    ],
    "line_comment": [
      "//"
    ]
  }
}
```

## Haskell

```json
{
  "Haskell": {
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
    ]
  }
}
```

## Haxe

```json
{
  "Haxe": {
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
    ]
  }
}
```

## IDL

```json
{
  "IDL": {
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
    "multi_line": []
  }
}
```

## Idris

```json
{
  "Idris": {
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
    ]
  }
}
```

## Intel HEX

```json
{
  "Intel HEX": {
    "extensions": [
      "ihex"
    ],
    "line_comment": [],
    "multi_line": []
  }
}
```

## Isabelle

```json
{
  "Isabelle": {
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
    ]
  }
}
```

## JAI

```json
{
  "JAI": {
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
    ]
  }
}
```

## JCL

```json
{
  "JCL": {
    "extensions": [
      "jcl",
      "jcls"
    ],
    "line_comment": [
      "//*"
    ]
  }
}
```

## JSON

```json
{
  "JSON": {
    "extensions": [
      "json"
    ],
    "line_comment": [],
    "multi_line": []
  }
}
```

## JSON5

```json
{
  "JSON5": {
    "extensions": [
      "json5"
    ],
    "line_comment": [
      "//"
    ],
    "multi_line": []
  }
}
```

## JSONC

```json
{
  "JSONC": {
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
    ]
  }
}
```

## JSONL

```json
{
  "JSONL": {
    "extensions": [
      "jsonl"
    ],
    "line_comment": [],
    "multi_line": []
  }
}
```

## JSX

```json
{
  "JSX": {
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
    ]
  }
}
```

## Jade

```json
{
  "Jade": {
    "extensions": [
      "jade"
    ],
    "line_comment": [
      "//-"
    ],
    "multi_line": []
  }
}
```

## Janet

```json
{
  "Janet": {
    "extensions": [
      "janet"
    ],
    "line_comment": [
      "#"
    ],
    "multi_line": []
  }
}
```

## Java

```json
{
  "Java": {
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
    ]
  }
}
```

## JavaScript

```json
{
  "JavaScript": {
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
    ]
  }
}
```

## JavaServer Pages

```json
{
  "JavaServer Pages": {
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
    ]
  }
}
```

## Jenkins Buildfile

```json
{
  "Jenkins Buildfile": {
    "extensions": [
      "jenkinsfile"
    ],
    "line_comment": [],
    "multi_line": []
  }
}
```

## Jinja

```json
{
  "Jinja": {
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
    ]
  }
}
```

## Jsonnet

```json
{
  "Jsonnet": {
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
    ]
  }
}
```

## Julia

```json
{
  "Julia": {
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
    ]
  }
}
```

## Julius

```json
{
  "Julius": {
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
    ]
  }
}
```

## Jupyter

```json
{
  "Jupyter": {
    "extensions": [
      "ipynb",
      "jpynb"
    ],
    "line_comment": [],
    "multi_line": []
  }
}
```

## Just

```json
{
  "Just": {
    "extensions": [
      "justfile"
    ],
    "line_comment": [
      "#"
    ],
    "multi_line": []
  }
}
```

## K

```json
{
  "K": {
    "extensions": [
      "k"
    ],
    "line_comment": [
      "/"
    ]
  }
}
```

## Korn Shell

```json
{
  "Korn Shell": {
    "extensions": [
      "ksh"
    ],
    "line_comment": [
      "#"
    ],
    "multi_line": []
  }
}
```

## Kotlin

```json
{
  "Kotlin": {
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
    ]
  }
}
```

## Koto

```json
{
  "Koto": {
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
    ]
  }
}
```

## LALRPOP

```json
{
  "LALRPOP": {
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
    ]
  }
}
```

## LD Script

```json
{
  "LD Script": {
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
    ]
  }
}
```

## LESS

```json
{
  "LESS": {
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
    ]
  }
}
```

## LEX

```json
{
  "LEX": {
    "extensions": [
      "l"
    ],
    "line_comment": [],
    "multi_line": [
      [
        "/*",
        "*/"
      ]
    ]
  }
}
```

## LLVM IR

```json
{
  "LLVM IR": {
    "extensions": [
      "ll"
    ],
    "line_comment": [
      ";"
    ],
    "multi_line": []
  }
}
```

## LOLCODE

```json
{
  "LOLCODE": {
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
    ]
  }
}
```

## LaTeX

```json
{
  "LaTeX": {
    "extensions": [
      "tex"
    ],
    "line_comment": [
      "%"
    ],
    "multi_line": []
  }
}
```

## Lean

```json
{
  "Lean": {
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
    ]
  }
}
```

## License

```json
{
  "License": {
    "extensions": [],
    "line_comment": [],
    "multi_line": []
  }
}
```

## Lisp

```json
{
  "Lisp": {
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
    ]
  }
}
```

## LiveScript

```json
{
  "LiveScript": {
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
    ]
  }
}
```

## Lua

```json
{
  "Lua": {
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
    ]
  }
}
```

## Luau

```json
{
  "Luau": {
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
    ]
  }
}
```

## Lucius

```json
{
  "Lucius": {
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
    ]
  }
}
```

## Luna

```json
{
  "Luna": {
    "extensions": [
      "luna"
    ],
    "line_comment": [
      "#"
    ],
    "multi_line": []
  }
}
```

## MATLAB

```json
{
  "MATLAB": {
    "extensions": [
      "m"
    ],
    "line_comment": [
      "%"
    ],
    "multi_line": [
      [
        "%{",
        "}%"
      ]
    ]
  }
}
```

## MDX

```json
{
  "MDX": {
    "extensions": [
      "mdx"
    ],
    "line_comment": [],
    "multi_line": []
  }
}
```

## MQL Header

```json
{
  "MQL Header": {
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
    ]
  }
}
```

## MQL4

```json
{
  "MQL4": {
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
    ]
  }
}
```

## MQL5

```json
{
  "MQL5": {
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
    ]
  }
}
```

## MSBuild

```json
{
  "MSBuild": {
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
    ]
  }
}
```

## MUMPS

```json
{
  "MUMPS": {
    "extensions": [
      "mps"
    ],
    "line_comment": [
      ";"
    ],
    "multi_line": []
  }
}
```

## Macromedia eXtensible Markup Language

```json
{
  "Macromedia eXtensible Markup Language": {
    "extensions": [
      "mxml"
    ],
    "line_comment": [],
    "multi_line": []
  }
}
```

## Madlang

```json
{
  "Madlang": {
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
    ]
  }
}
```

## Makefile

```json
{
  "Makefile": {
    "extensions": [
      "makefile",
      "mak",
      "mk",
      "bp"
    ],
    "line_comment": [
      "#"
    ],
    "multi_line": []
  }
}
```

## Mako

```json
{
  "Mako": {
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
    ]
  }
}
```

## Markdown

```json
{
  "Markdown": {
    "extensions": [
      "md",
      "markdown"
    ],
    "line_comment": [],
    "multi_line": []
  }
}
```

## Max

```json
{
  "Max": {
    "extensions": [
      "maxpat"
    ],
    "line_comment": [],
    "multi_line": []
  }
}
```

## Meson

```json
{
  "Meson": {
    "extensions": [
      "meson.build",
      "meson_options.txt"
    ],
    "line_comment": [
      "#"
    ]
  }
}
```

## Metal

```json
{
  "Metal": {
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
    ]
  }
}
```

## Modula3

```json
{
  "Modula3": {
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
    ]
  }
}
```

## Module-Definition

```json
{
  "Module-Definition": {
    "extensions": [
      "def"
    ],
    "line_comment": [
      ";"
    ],
    "multi_line": []
  }
}
```

## Monkey C

```json
{
  "Monkey C": {
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
    ]
  }
}
```

## Moonbit

```json
{
  "Moonbit": {
    "extensions": [
      "mbt"
    ],
    "line_comment": [
      "//"
    ],
    "multi_line": []
  }
}
```

## Mustache

```json
{
  "Mustache": {
    "extensions": [
      "mustache"
    ],
    "line_comment": [],
    "multi_line": [
      [
        "{{!",
        "}}"
      ]
    ]
  }
}
```

## Nial

```json
{
  "Nial": {
    "extensions": [
      "ndf"
    ],
    "line_comment": [
      "%"
    ],
    "multi_line": []
  }
}
```

## Nim

```json
{
  "Nim": {
    "extensions": [
      "nim"
    ],
    "line_comment": [
      "#"
    ],
    "multi_line": []
  }
}
```

## Nix

```json
{
  "Nix": {
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
    ]
  }
}
```

## Nushell

```json
{
  "Nushell": {
    "extensions": [
      "nu"
    ],
    "line_comment": [
      "#"
    ],
    "multi_line": []
  }
}
```

## OCaml

```json
{
  "OCaml": {
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
    ]
  }
}
```

## Objective C

```json
{
  "Objective C": {
    "extensions": [
      "m"
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

## Objective C++

```json
{
  "Objective C++": {
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
    ]
  }
}
```

## Odin

```json
{
  "Odin": {
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
    ]
  }
}
```

## Opalang

```json
{
  "Opalang": {
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
    ]
  }
}
```

## OpenQASM

```json
{
  "OpenQASM": {
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
    ]
  }
}
```

## OpenTofu

```json
{
  "OpenTofu": {
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
    ]
  }
}
```

## Org

```json
{
  "Org": {
    "extensions": [
      "org"
    ],
    "line_comment": [
      "# "
    ],
    "multi_line": []
  }
}
```

## Oz

```json
{
  "Oz": {
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
    ]
  }
}
```

## PHP

```json
{
  "PHP": {
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
    ]
  }
}
```

## PKGBUILD

```json
{
  "PKGBUILD": {
    "extensions": [
      "pkgbuild"
    ],
    "line_comment": [],
    "multi_line": []
  }
}
```

## PL/SQL

```json
{
  "PL/SQL": {
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
    ]
  }
}
```

## PRQL

```json
{
  "PRQL": {
    "extensions": [
      "prql"
    ],
    "line_comment": [
      "#"
    ],
    "multi_line": []
  }
}
```

## PSL Assertion

```json
{
  "PSL Assertion": {
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
    ]
  }
}
```

## Pascal

```json
{
  "Pascal": {
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
    ]
  }
}
```

## Patch

```json
{
  "Patch": {
    "extensions": [
      "patch"
    ],
    "line_comment": [],
    "multi_line": []
  }
}
```

## Perl

```json
{
  "Perl": {
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
    ]
  }
}
```

## Phoenix LiveView

```json
{
  "Phoenix LiveView": {
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
    ]
  }
}
```

## Picat

```json
{
  "Picat": {
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
    ]
  }
}
```

## Pkl

```json
{
  "Pkl": {
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
    ]
  }
}
```

## Plain Text

```json
{
  "Plain Text": {
    "extensions": [
      "text",
      "txt"
    ],
    "line_comment": [],
    "multi_line": []
  }
}
```

## Polly

```json
{
  "Polly": {
    "extensions": [
      "polly"
    ],
    "line_comment": [],
    "multi_line": [
      [
        "<!--",
        "-->"
      ]
    ]
  }
}
```

## Pony

```json
{
  "Pony": {
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
    ]
  }
}
```

## PostScript

```json
{
  "PostScript": {
    "extensions": [
      "ps"
    ],
    "line_comment": [
      "%"
    ]
  }
}
```

## Powershell

```json
{
  "Powershell": {
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
    ]
  }
}
```

## Processing

```json
{
  "Processing": {
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
    ]
  }
}
```

## Prolog

```json
{
  "Prolog": {
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
    ]
  }
}
```

## Properties File

```json
{
  "Properties File": {
    "extensions": [
      "properties"
    ],
    "line_comment": [
      "#"
    ],
    "multi_line": []
  }
}
```

## Protocol Buffers

```json
{
  "Protocol Buffers": {
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
    ]
  }
}
```

## Puppet

```json
{
  "Puppet": {
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
    ]
  }
}
```

## PureScript

```json
{
  "PureScript": {
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
    ]
  }
}
```

## Python

```json
{
  "Python": {
    "extensions": [
      "py",
      "pyw",
      "pyi"
    ],
    "line_comment": [
      "#"
    ],
    "multi_line": []
  }
}
```

## Q#

```json
{
  "Q#": {
    "extensions": [
      "qs"
    ],
    "line_comment": [
      "//"
    ],
    "multi_line": []
  }
}
```

## QCL

```json
{
  "QCL": {
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
    ]
  }
}
```

## QML

```json
{
  "QML": {
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
    ]
  }
}
```

## R

```json
{
  "R": {
    "extensions": [
      "r"
    ],
    "line_comment": [
      "#"
    ],
    "multi_line": []
  }
}
```

## RAML

```json
{
  "RAML": {
    "extensions": [
      "raml",
      "rml"
    ],
    "line_comment": [
      "#"
    ],
    "multi_line": []
  }
}
```

## Racket

```json
{
  "Racket": {
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
    ]
  }
}
```

## Rakefile

```json
{
  "Rakefile": {
    "extensions": [],
    "line_comment": [
      "#"
    ],
    "multi_line": [
      [
        "=begin",
        "=end"
      ]
    ]
  }
}
```

## Raku

```json
{
  "Raku": {
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
    ]
  }
}
```

## Razor

```json
{
  "Razor": {
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
    ]
  }
}
```

## ReScript

```json
{
  "ReScript": {
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
    ]
  }
}
```

## ReStructuredText

```json
{
  "ReStructuredText": {
    "extensions": [
      "rst"
    ],
    "line_comment": [],
    "multi_line": []
  }
}
```

## ReasonML

```json
{
  "ReasonML": {
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
    ]
  }
}
```

## Redscript

```json
{
  "Redscript": {
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
    ]
  }
}
```

## Report Definition Language

```json
{
  "Report Definition Language": {
    "extensions": [
      "rdl"
    ],
    "line_comment": [],
    "multi_line": [
      [
        "<!--",
        "-->"
      ]
    ]
  }
}
```

## Robot Framework

```json
{
  "Robot Framework": {
    "extensions": [
      "robot"
    ],
    "line_comment": [],
    "multi_line": []
  }
}
```

## Ruby

```json
{
  "Ruby": {
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
    ]
  }
}
```

## Ruby HTML

```json
{
  "Ruby HTML": {
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
    ]
  }
}
```

## Rust

```json
{
  "Rust": {
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
    ]
  }
}
```

## SAS

```json
{
  "SAS": {
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
    ]
  }
}
```

## SKILL

```json
{
  "SKILL": {
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
    ]
  }
}
```

## SNOBOL

```json
{
  "SNOBOL": {
    "extensions": [
      "sno"
    ],
    "line_comment": [
      "*"
    ]
  }
}
```

## SPDX

```json
{
  "SPDX": {
    "extensions": [
      "spdx"
    ],
    "line_comment": [],
    "multi_line": []
  }
}
```

## SPL

```json
{
  "SPL": {
    "extensions": [
      "spl"
    ],
    "line_comment": [],
    "multi_line": [
      [
        "\"",
        "\";"
      ]
    ]
  }
}
```

## SQL

```json
{
  "SQL": {
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
    ]
  }
}
```

## SRecode Template

```json
{
  "SRecode Template": {
    "extensions": [
      "srt"
    ],
    "line_comment": [
      ";;"
    ],
    "multi_line": []
  }
}
```

## SVG

```json
{
  "SVG": {
    "extensions": [
      "svg"
    ],
    "line_comment": [],
    "multi_line": [
      [
        "<!--",
        "-->"
      ]
    ]
  }
}
```

## Sass

```json
{
  "Sass": {
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
    ]
  }
}
```

## Scala

```json
{
  "Scala": {
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
    ]
  }
}
```

## Scallop

```json
{
  "Scallop": {
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
    ]
  }
}
```

## Scheme

```json
{
  "Scheme": {
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
    ]
  }
}
```

## Scons

```json
{
  "Scons": {
    "extensions": [
      "csig",
      "sconstruct",
      "sconscript"
    ],
    "line_comment": [
      "#"
    ],
    "multi_line": []
  }
}
```

## Shell

```json
{
  "Shell": {
    "extensions": [
      "sh"
    ],
    "line_comment": [
      "#"
    ],
    "multi_line": []
  }
}
```

## Sieve

```json
{
  "Sieve": {
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
    ]
  }
}
```

## Slang

```json
{
  "Slang": {
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
    ]
  }
}
```

## Slint

```json
{
  "Slint": {
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
    ]
  }
}
```

## Smalltalk

```json
{
  "Smalltalk": {
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
    ]
  }
}
```

## Smarty Template

```json
{
  "Smarty Template": {
    "extensions": [
      "tpl"
    ],
    "line_comment": [],
    "multi_line": [
      [
        "{*",
        "*}"
      ]
    ]
  }
}
```

## Snakemake

```json
{
  "Snakemake": {
    "extensions": [
      "smk",
      "rules"
    ],
    "line_comment": [
      "#"
    ],
    "multi_line": []
  }
}
```

## Softbridge Basic

```json
{
  "Softbridge Basic": {
    "extensions": [
      "sbl"
    ],
    "line_comment": [
      "'"
    ],
    "multi_line": []
  }
}
```

## Solidity

```json
{
  "Solidity": {
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
    ]
  }
}
```

## Specman e

```json
{
  "Specman e": {
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
    ]
  }
}
```

## Spice Netlist

```json
{
  "Spice Netlist": {
    "extensions": [
      "ckt"
    ],
    "line_comment": [
      "*"
    ],
    "multi_line": []
  }
}
```

## Stan

```json
{
  "Stan": {
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
    ]
  }
}
```

## Standard ML (SML)

```json
{
  "Standard ML (SML)": {
    "extensions": [
      "sml"
    ],
    "line_comment": [],
    "multi_line": [
      [
        "(*",
        "*)"
      ]
    ]
  }
}
```

## Stata

```json
{
  "Stata": {
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
    ]
  }
}
```

## Stylus

```json
{
  "Stylus": {
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
    ]
  }
}
```

## Svelte

```json
{
  "Svelte": {
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
    ]
  }
}
```

## Swift

```json
{
  "Swift": {
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
    ]
  }
}
```

## Swig

```json
{
  "Swig": {
    "extensions": [
      "i"
    ],
    "line_comment": [],
    "multi_line": [
      [
        "/*",
        "*/"
      ]
    ]
  }
}
```

## SystemVerilog

```json
{
  "SystemVerilog": {
    "extensions": [
      "sv",
      "svh"
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

## Systemd

```json
{
  "Systemd": {
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
    "multi_line": []
  }
}
```

## TCL

```json
{
  "TCL": {
    "extensions": [
      "tcl"
    ],
    "line_comment": [
      "#"
    ],
    "multi_line": []
  }
}
```

## TL

```json
{
  "TL": {
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
    ]
  }
}
```

## TOML

```json
{
  "TOML": {
    "extensions": [
      "toml"
    ],
    "line_comment": [
      "#"
    ],
    "multi_line": []
  }
}
```

## TTCN-3

```json
{
  "TTCN-3": {
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
    ]
  }
}
```

## Tact

```json
{
  "Tact": {
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
    ]
  }
}
```

## TaskPaper

```json
{
  "TaskPaper": {
    "extensions": [
      "taskpaper"
    ],
    "line_comment": [],
    "multi_line": []
  }
}
```

## TeX

```json
{
  "TeX": {
    "extensions": [
      "tex",
      "sty"
    ],
    "line_comment": [
      "%"
    ],
    "multi_line": []
  }
}
```

## Teal

```json
{
  "Teal": {
    "extensions": [
      "teal"
    ],
    "line_comment": [
      "//"
    ],
    "multi_line": []
  }
}
```

## Templ

```json
{
  "Templ": {
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
    ]
  }
}
```

## TemplateToolkit

```json
{
  "TemplateToolkit": {
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
    ]
  }
}
```

## Tera

```json
{
  "Tera": {
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
    ]
  }
}
```

## Terraform

```json
{
  "Terraform": {
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
    ]
  }
}
```

## Textile

```json
{
  "Textile": {
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
    ]
  }
}
```

## Thrift

```json
{
  "Thrift": {
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
    ]
  }
}
```

## Treetop

```json
{
  "Treetop": {
    "extensions": [
      "treetop",
      "tt"
    ],
    "line_comment": [
      "#"
    ]
  }
}
```

## Twig Template

```json
{
  "Twig Template": {
    "extensions": [
      "twig"
    ],
    "line_comment": [],
    "multi_line": []
  }
}
```

## TypeScript

```json
{
  "TypeScript": {
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
    ]
  }
}
```

## TypeScript Typings

```json
{
  "TypeScript Typings": {
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
    ]
  }
}
```

## TypeSpec

```json
{
  "TypeSpec": {
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
    ]
  }
}
```

## Unreal Script

```json
{
  "Unreal Script": {
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
    ]
  }
}
```

## Up

```json
{
  "Up": {
    "extensions": [
      "up"
    ],
    "line_comment": [
      "//"
    ],
    "multi_line": []
  }
}
```

## Ur/Web

```json
{
  "Ur/Web": {
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
    ]
  }
}
```

## Ur/Web Project

```json
{
  "Ur/Web Project": {
    "extensions": [
      "urp"
    ],
    "line_comment": [
      "#"
    ],
    "multi_line": []
  }
}
```

## V

```json
{
  "V": {
    "extensions": [
      "v"
    ],
    "line_comment": [
      "//"
    ],
    "multi_line": []
  }
}
```

## VHDL

```json
{
  "VHDL": {
    "extensions": [
      "vhd",
      "vhdl"
    ],
    "line_comment": [
      "--"
    ],
    "multi_line": []
  }
}
```

## Vala

```json
{
  "Vala": {
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
    ]
  }
}
```

## Varnish Configuration

```json
{
  "Varnish Configuration": {
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
    ]
  }
}
```

## Verilog

```json
{
  "Verilog": {
    "extensions": [
      "vg",
      "vh",
      "v"
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

## Verilog Args File

```json
{
  "Verilog Args File": {
    "extensions": [
      "irunargs",
      "xrunargs"
    ],
    "line_comment": [],
    "multi_line": []
  }
}
```

## Vertex Shader File

```json
{
  "Vertex Shader File": {
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
    ]
  }
}
```

## Vim Script

```json
{
  "Vim Script": {
    "extensions": [
      "vim",
      "vimrc",
      "gvimrc"
    ],
    "line_comment": [
      "\"",
      "#"
    ],
    "multi_line": []
  }
}
```

## Visual Basic

```json
{
  "Visual Basic": {
    "extensions": [
      "vb"
    ],
    "line_comment": [
      "'"
    ],
    "multi_line": []
  }
}
```

## Visual Basic for Applications

```json
{
  "Visual Basic for Applications": {
    "extensions": [
      "cls"
    ],
    "line_comment": [
      "'"
    ],
    "multi_line": []
  }
}
```

## Vue

```json
{
  "Vue": {
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
    ]
  }
}
```

## W.I.S.E. Jobfile

```json
{
  "W.I.S.E. Jobfile": {
    "extensions": [
      "fgmj"
    ],
    "line_comment": [],
    "multi_line": []
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
    ]
  }
}
```

## WebGPU Shading Language

```json
{
  "WebGPU Shading Language": {
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

## Wolfram

```json
{
  "Wolfram": {
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
    ]
  }
}
```

## Wren

```json
{
  "Wren": {
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
    ]
  }
}
```

## XAML

```json
{
  "XAML": {
    "extensions": [
      "xaml"
    ],
    "line_comment": [],
    "multi_line": [
      [
        "<!--",
        "-->"
      ]
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
    ]
  }
}
```

## XML Schema

```json
{
  "XML Schema": {
    "extensions": [
      "xsd"
    ],
    "line_comment": [],
    "multi_line": []
  }
}
```

## XMake

```json
{
  "XMake": {
    "extensions": [],
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
    ]
  }
}
```

## Xcode Config

```json
{
  "Xcode Config": {
    "extensions": [
      "xcconfig"
    ],
    "line_comment": [
      "//"
    ],
    "multi_line": []
  }
}
```

## Xtend

```json
{
  "Xtend": {
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
    ]
  }
}
```

## YAML

```json
{
  "YAML": {
    "extensions": [
      "yaml",
      "yml"
    ],
    "line_comment": [
      "#"
    ],
    "multi_line": []
  }
}
```

## Yarn

```json
{
  "Yarn": {
    "extensions": [
      "yarn"
    ],
    "line_comment": []
  }
}
```

## Zig

```json
{
  "Zig": {
    "extensions": [
      "zig"
    ],
    "line_comment": [
      "//"
    ]
  }
}
```

## ZoKrates

```json
{
  "ZoKrates": {
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
    "extensions": [
      "zsh",
      "zshenv",
      "zlogin",
      "zlogout",
      "zprofile",
      "zshrc"
    ],
    "line_comment": [
      "#"
    ],
    "multi_line": []
  }
}
```

## bait

```json
{
  "bait": {
    "extensions": [
      "bt"
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

## gitignore

```json
{
  "gitignore": {
    "extensions": [],
    "line_comment": [
      "#"
    ],
    "multi_line": []
  }
}
```

## hoon

```json
{
  "hoon": {
    "extensions": [
      "hoon"
    ],
    "line_comment": [
      "::"
    ],
    "multi_line": []
  }
}
```

## ignore

```json
{
  "ignore": {
    "extensions": [],
    "line_comment": [
      "#"
    ],
    "multi_line": []
  }
}
```

## jq

```json
{
  "jq": {
    "extensions": [
      "jq"
    ],
    "line_comment": [
      "#"
    ],
    "multi_line": []
  }
}
```

## m4

```json
{
  "m4": {
    "extensions": [
      "m4"
    ],
    "line_comment": [
      "#"
    ],
    "multi_line": []
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
    ]
  }
}
```

## sed

```json
{
  "sed": {
    "extensions": [
      "sed"
    ],
    "line_comment": [
      "#"
    ],
    "multi_line": []
  }
}
```

## wenyan

```json
{
  "wenyan": {
    "extensions": [
      "wy"
    ],
    "line_comment": [
      "\u6279\u66f0",
      "\u6ce8\u66f0",
      "\u758f\u66f0"
    ],
    "multi_line": []
  }
}
```

