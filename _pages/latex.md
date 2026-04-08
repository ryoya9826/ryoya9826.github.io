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
- [overload package](https://github.com/ryoya9826/overload), last modified : 2021/08/02 <br>
  - This package provides macros to overload the arguments of LaTeX macros. 
- [Mermaidenv / mermaid.sty](https://github.com/ryoya9826/Mermaidenv), last modified : 2026/04/08 (README in English and Japanese)<br>
  - This package defines the `mermaid` environment: diagram sources are written to disk, the Mermaid CLI (`mmdc`) renders **PDF** (vector), and the result is included with `\includegraphics`. **LuaLaTeX**, **`-shell-escape`**, and **Node.js** with **`mmdc`** or **`npx`** (plus Mermaid CLI’s headless Chromium) are required.<br>
  - Mermaidの図をLaTeXに埋め込みます。ソースをディスクに書き出し、Mermaid CLI（`mmdc`）でPDFを生成して`\includegraphics`で取り込みます。LuaLaTeXと`-shell-escape`、およびNode.js／`mmdc`（または`npx`）とヘッドレスChromiumが必要です。詳細はリポジトリのREADME（英日）を参照してください．
