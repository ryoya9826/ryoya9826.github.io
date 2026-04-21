---
layout: archive
title: "LaTeX Packages"
permalink: /latex/
last_modified_at: 2026-04-21
---

{% include base_path %}

These are the LaTeX packages I developed.
## Macros
- [askw3 package](https://github.com/ryoya9826/askw3-dtx), last modified : 2021/05/14 (Document is Japanese)<br>
   - This package combines the amsthm and ascmac packages to provide a framed theorem environment.
 There are also some other macros that I have created personally. See the documentation for details. <br>
   - amsthmパッケージとascmacパッケージを組み合わせることにより，枠で囲われた定理環境を提供します．
他にもいくつか個人的に作成したマクロを収録しています．詳細はドキュメントを見てください．
- [overload / myoverload.sty](https://github.com/ryoya9826/overload), last modified : 2026/04/08 (README in Japanese)<br>
  - This small LaTeX2e package lets one control sequence dispatch on **how many arguments** were given (0–9), using `\newoverload`, `\renewoverload`, `\addoverload`, and a trailing `\enddelim` terminator.<br>
  
- [ltMermaid / `mermaid.sty` and `ltmermaid.sty`](https://github.com/ryoya9826/ltMermaid) ([CTAN](https://ctan.org/pkg/ltmermaid)), last modified : 2026/04/16 (README in English)<br>
  - This repository provides two LaTeX packages to embed Mermaid diagrams: `mermaid` works with pdfLaTeX / XeLaTeX / upLaTeX / LuaLaTeX, while `ltmermaid` is a LuaLaTeX-native implementation. Both write diagram sources to disk, invoke the Mermaid CLI (`mmdc`) to render vector PDF files, and include the result with `\includegraphics`. **`-shell-escape`** and Mermaid CLI (`mmdc` or `npx -y @mermaid-js/mermaid-cli`) are required.<br>
  - Mermaid図をLaTeXに埋め込むための2つのパッケージ `mermaid.sty` / `ltmermaid.sty` を提供します．`mermaid` は pdfLaTeX / XeLaTeX / upLaTeX / LuaLaTeX などで利用でき，`ltmermaid` は LuaLaTeX 専用の実装です．いずれもソースをディスクに書き出し，Mermaid CLI（`mmdc`）でベクタPDFを生成して `\includegraphics` で取り込みます．利用時には `-shell-escape` と Mermaid CLI（`mmdc` または `npx -y @mermaid-js/mermaid-cli`）が必要です．
