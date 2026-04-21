---
layout: archive
title: "LaTeX Packages"
permalink: /latex/
last_modified_at: 2026-04-21
---

{% include base_path %}

These are the LaTeX packages I developed.
## Macros
- [overload / myoverload.sty](https://github.com/ryoya9826/overload), last modified : 2026/04/08 (README in Japanese)
  - This small LaTeX2e package lets one control sequence dispatch on how many arguments were given (0–9), using `\newoverload`, `\renewoverload`, `\addoverload`, and a trailing `\enddelim` terminator.
  
- [ltMermaid / `mermaid.sty` and `ltmermaid.sty`](https://github.com/ryoya9826/ltMermaid) ([CTAN](https://ctan.org/pkg/ltmermaid)), last modified : 2026/04/16 (README in English)
  - This repository provides two LaTeX packages to embed Mermaid diagrams: `mermaid` works with pdfLaTeX / XeLaTeX / upLaTeX / LuaLaTeX, while `ltmermaid` is a LuaLaTeX-native implementation. Both write diagram sources to disk, invoke the Mermaid CLI (`mmdc`) to render vector PDF files, and include the result with `\includegraphics`. `-shell-escape` and Mermaid CLI (`mmdc` or `npx -y @mermaid-js/mermaid-cli`) are required.

## BibTeX
- [ua-jecon / `ua-jecon.bst` and `ua-jecon.sty`](https://github.com/ryoya9826/ua-jecon), last modified : 2026/04/21 (README in Japanese)
  - A derivative of [jecon.bst](https://github.com/ShiroTakeda/jecon-bst) by Shiro Takeda, with several extensions for economics bibliography in Japanese. It also supports amsrefs-style compressed citations via the `\acite` command.
