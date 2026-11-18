---
layout: archive
title: "Software & Tools"
description: "Software by Ryoya Ando: LaTeX packages on CTAN (ltMermaid, ua-jecon), other LaTeX macros, and browser extensions."
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
- [overload / myoverload.sty](https://github.com/ryoya9826/overload), last modified : 2026/04/08 (README in Japanese)
  - This small LaTeX2e package lets one control sequence dispatch on how many arguments were given (0–9), using `\newoverload`, `\renewoverload`, `\addoverload`, and a trailing `\enddelim` terminator.
  
- [ltMermaid / `mermaid.sty` and `ltmermaid.sty`](https://github.com/ryoya9826/ltMermaid) ([CTAN](https://ctan.org/pkg/ltmermaid)), v1.1, last modified : 2026/10/22 (README in English; documentation in English and Japanese)
  - This repository provides two LaTeX packages to embed Mermaid diagrams: `mermaid` works with pdfLaTeX / XeLaTeX / upLaTeX / LuaLaTeX, while `ltmermaid` is a LuaLaTeX-native implementation. Both write diagram sources to disk, invoke the Mermaid CLI (`mmdc`) to render vector PDF files, and include the result with `\includegraphics`. `-shell-escape` and Mermaid CLI (`mmdc` or `npx -y @mermaid-js/mermaid-cli`) are required.
  - v1.1 supports Mermaid CLI 12 and the `-output-directory` option, and skips re-rendering diagrams that have not changed.

### BibTeX
- [ua-jecon / `ua-jecon.bst` and `ua-jecon.sty`](https://github.com/ryoya9826/ua-jecon) ([CTAN](https://ctan.org/pkg/ua-jecon)), v0.7.1, last modified : 2026/11/16 (README in English and Japanese; documentation in Japanese)
  - An extended version of [jecon.bst](https://github.com/ShiroTakeda/jecon-bst) (v6.2.1) by Shiro Takeda, a BibTeX style for economics that handles both Japanese and English references. upLaTeX or LuaLaTeX with upBibTeX is required for Japanese entries.
  - It adds the fields `arxiv`, `etranslator` and `label`, appends a, b, ... to entries with the same author(s) and year, and writes amsrefs-like compressed labels (e.g. `[And26]`). The wrapper package `ua-jecon.sty` loads `natbib`, selects the style and defines `\acite` to print these labels. The name stands for upBibTeX + amsrefs.
