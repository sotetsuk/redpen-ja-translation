[![Build Status](https://travis-ci.org/sotetsuk/redpen-ja-translation.svg?branch=master)](https://travis-ci.org/sotetsuk/redpen-ja-translation)

# 技術書日本語訳用RedPenテンプレート

## 趣旨
英文のLaTeXで書かれた技術書を翻訳する際には、様々な点に注意を払わねばならない。
特に複数人で行う場合、

- 句読点が揃っているか（```、。``` or ```，．```）
- 専門語訳は揃っているか（```オペレーションズ・リサーチ``` or ```オペレーションズリサーチ```）
- ```（）```の使い方は統一されているか（半角 or 全角、スペースを入れるか入れないか）
- 数式の記号が原著のものときちんと揃っているか

など、統一すべき点、機械的にチェックすべき点を上げればキリがない。


そこで、このリポジトリでは、ドキュメントチェックツールである[RedPen](http://redpen.cc/)を（主に）使い、
そうしたLaTeX技術文書の翻訳に特化した設定をテンプレートとして用意する。

## 使い方
## 規約
## ライセンス

```
The MIT License (MIT)

Copyright (c) 2016 Sotetsu KOYAMADA

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```
