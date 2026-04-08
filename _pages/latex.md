---
layout: archive
title: "LaTeX Packages"
permalink: /latex/
redirect_from:
  - /resume
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
  
- [Mermaidenv / mermaid.sty](https://github.com/ryoya9826/ltMermaid), last modified : 2026/04/08 (README in English and Japanese)<br>
  - This package defines the `mermaid` environment: diagram sources are written to disk, the Mermaid CLI (`mmdc`) renders **PDF** (vector), and the result is included with `\includegraphics`. **LuaLaTeX**, **`-shell-escape`**, and **Node.js** with **`mmdc`** or **`npx`** (plus Mermaid CLI’s headless Chromium) are required.<br>
  - Mermaidの図をLaTeXに埋め込みます。ソースをディスクに書き出し、Mermaid CLI（`mmdc`）でPDFを生成して`\includegraphics`で取り込みます。LuaLaTeX を `-shell-escape` で実行する必要があり、また Node.js／`mmdc`（または`npx`）が必要です。詳細はREADMEを参照してください．
