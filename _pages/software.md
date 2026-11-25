---
layout: archive
title: "Software & Tools"
description: "Software by Ryoya Ando: LaTeX packages on CTAN (ltMermaid, ua-jecon), the overload macro package, and browser extensions."
permalink: /software/
redirect_from:
  - /latex/
---

{% include base_path %}

## Browser Extensions
- [Blur Focus / `chrome-extension-blur`](https://github.com/ryoya9826/chrome-extension-blur)
  - A Chrome extension that applies a blur effect to specified elements on a webpage, which can be temporarily revealed on hover. Useful for hiding personal information during screen sharing or taking screenshots.

## LaTeX Packages
These are the LaTeX packages I developed.

### Macros
- [overload / `overload.sty`](https://github.com/ryoya9826/overload), v2.0, last modified : 2026/11/25 (README in English and Japanese; documentation in Japanese)
  - A LaTeX2e package that lets one command name dispatch on the number of arguments (0–9). Bodies are registered with `\newoverload`, `\renewoverload` and `\addoverload`. It works with pdfLaTeX, LuaLaTeX, XeLaTeX, pLaTeX and upLaTeX, and needs no other packages.
  - v2.0 renames the package from `myoverload` and counts the following brace groups by lookahead, so the `\enddelim` terminator is now optional. Nested calls such as `\hoge{\hoge{a}{b}}{c}` work, and the commands are `\protected`, so they can be used in section titles and captions.

- [ltMermaid / `mermaid.sty` and `ltmermaid.sty`](https://github.com/ryoya9826/ltMermaid) ([CTAN](https://ctan.org/pkg/ltmermaid)), v1.1, last modified : 2026/10/22 (README in English; documentation in English and Japanese)
  - This repository provides two LaTeX packages to embed Mermaid diagrams: `mermaid` works with pdfLaTeX / XeLaTeX / upLaTeX / LuaLaTeX, while `ltmermaid` is a LuaLaTeX-native implementation. Both write diagram sources to disk, invoke the Mermaid CLI (`mmdc`) to render vector PDF files, and include the result with `\includegraphics`. `-shell-escape` and Mermaid CLI (`mmdc` or `npx -y @mermaid-js/mermaid-cli`) are required.
  - v1.1 supports Mermaid CLI 12 and the `-output-directory` option, and skips re-rendering diagrams that have not changed.

### BibTeX
- [ua-jecon / `ua-jecon.bst` and `ua-jecon.sty`](https://github.com/ryoya9826/ua-jecon) ([CTAN](https://ctan.org/pkg/ua-jecon)), v0.7.2, last modified : 2026/11/25 (README in English and Japanese; documentation in Japanese)
  - An extended version of [jecon.bst](https://github.com/ShiroTakeda/jecon-bst) (v6.2.1) by Shiro Takeda, a BibTeX style for economics that handles both Japanese and English references. upLaTeX or LuaLaTeX with upBibTeX is required for Japanese entries.
  - It adds the fields `arxiv`, `etranslator` and `label`, appends a, b, ... to entries with the same author(s) and year, and writes amsrefs-like compressed labels (e.g. `[And26]`). The wrapper package `ua-jecon.sty` loads `natbib`, selects the style and defines `\acite` to print these labels. The name stands for upBibTeX + amsrefs.
  - v0.7.2 builds the compressed labels character by character, so author names with accented letters such as `Ł` or `ś`, or with TeX accents such as `{\"o}`, give the correct first three letters. The comment at the top of the `.bbl` file now points to the latest `ua-jecon` on CTAN and GitHub.
