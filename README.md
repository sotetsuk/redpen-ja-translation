[![Build Status](https://travis-ci.org/sotetsuk/redpen-ja-translation.svg?branch=master)](https://travis-ci.org/sotetsuk/redpen-ja-translation)

# LaTeX文書の邦訳用RedPenテンプレート

## 趣旨
英文のLaTeXで書かれた技術書を翻訳する際には、様々な点に注意を払わねばならない。たとえば

- 句読点が揃っているか（```、。``` or ```，．```）
- 専門語訳は揃っているか（```グリーディ``` or ```貪欲```）
- ```（）```の使い方は統一されているか（半角 or 全角、スペースを入れるか入れないか）
- 数式の記号が原著のものときちんと揃っているか

など、統一すべき点、機械的にチェックすべき点を上げればキリがない。
また、これらを複数人で翻訳する際に統一するのはなお難しい。


そこで、このリポジトリでは、ドキュメントチェックツールである[RedPen](http://redpen.cc/)を（主に）使い、
そうしたLaTeX技術文書の翻訳に特化した設定をテンプレートとして用意する。

## 使い方
## 規約

### 01 記号に関する規約

- 句読点は全角のカンマとピリオド: ```，```, ```．```（RedPen: InvalidSymbol）
- コロンは半角＋後ろにスペース: ```:_```（RedPen: InvalidSymbol, SymbolWithSpace）
- セミコロンは半角＋後ろにスペース: ```;_```（RedPen: InvalidSymbol, SymbolWithSpace）
- クエスチョンマークは全角: ```？```（RedPen: InvalidSymbol）
- エクステンションマークは全角: ```！```（RedPen: InvalidSymbol）
- スペースは半角のみ（RedPen: InvalidSymbol）
- [TODO] LaTeX本文中でダブルコーテーション記号は使わない（代わりに``` `` ```と```''```で囲む）
- [TODO] 括弧に関する規約
  - [TODO] 括弧の中が半角英数だけなら半角＋前後スペース
  - [TODO] 括弧の中に全角文字があれば全角の（）

### 02 文長に関する規約

- 一文の文長は _**150**_ 文字まで（RedPen: SentenceLength）
- 一文のコンマ数は _**5**_ 個まで（RedPen: CommaNumber）

### 03 日本語表現に関する規約

- 日本語の数値表現を半角英数字に統一する（RedPen: JapaneseNumberExpression）
  - e.g., ```1つ```, ```2つ```
- カタカナ単語のゆらぎを減らす（RedPen: KatakanaSpellCheck）
  - e.g., ```オペレーションズ・リサーチ``` vs ```オペレーションズリサーチ```
- 同じ文頭表現を過度に利用しない（RedPen: FrequentSentenceStart）
- 「の」を過度に繰り返えさない（RedPen: JapaneseAmbiguousNounConjunction）
- カタカナ単語の語尾を適切にする（例外リスト）（RedPen: KatakanaEndHyphen）
- [TODO] 過度に連続した漢字を使わない（RedPen: LongKanjiChain）
- [TODO] 二重否定を使わない（RedPen: DoubleNegative）
- [TODO] 送り仮名を統一する（リスト）（漢字かひらがなか）
  - e.g., 行なう、満たす、時、例えば
- [TODO] 不適切な語の出現を弾く（リスト）（RedPen: SuggestExpression）
  - e.g., ```TODO```、本の中での```本稿```

### 04 翻訳特有の規約

- [TODO] 訳文は原文を一文（あるいはより細かい）単位でコメントアウトし、その次の行に訳語を書く（区切りは```.```, ```:```, ```;```, inline以外の数式）
- [TODO] 訳語をリストに沿って訳語を統一する（訳語リスト）
  - [TODO] コメントアウトされた原文に対し、次の行で適切な訳語を使う
  - [TODO] 不適切な訳語を使わない（RedPen: SuggestExpression）
- [TODO] 文字修飾を原文に統一する（コメントアウトされた原文に対し、次の行で同じ修飾（```\bf```など）が（同じ回数）出現している）
- [TODO] 略語に関する規約
  - [TODO] 略語が併記されている場合、略語をセミコロンで区切って併記する（e.g., ```Reinforcement Learning (RL) is ...``` は ```強化学習 (Reinforcement Learning; RL) とは... ```）
  - [TDOO] 略語に対しフルスペルが併記されている場合、訳語をセミコロンで区切って括弧内に併記する（e.g., ```LS (least-squares)``` は ```LS（least-squares; 最小二乗）```）
- [TODO] 初めて出現した見出し語句に対し、訳の後に括弧で原文の語句を掲載する（見出し語リスト）
- [TODO] 文中のLaTeXの数式が、コメントアウトされた原文と同じになっている
- [TODO] 原著と同じセクション構成になっている
- [TODO] 原著と同じ段落構成になっている

### 05 ケアレスミスを検出するための規約

- 同一の単語が連続して使用されていないかをチェックする（RedPen: SuccessiveWord）
- [TODO] 英単語が出現した場合、その表現が原文中のものと同じになっているか
  - e.g., 原文中: RL-GLUE, 訳文中: RL-Glue

<!--
### その他使えそうなValidator

- [TODO] JapaneseStyle （ですます。である）
-->

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
