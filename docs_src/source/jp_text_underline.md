<span class="inconspicuous-txt">※この翻訳ドキュメントはスクリプトによって出力・同期されています。内容が怪しそうな場合は<a href="https://github.com/simon-ritchie/apysc/issues" target="_blank">GitHubにissue</a>を追加したり[英語の原文](https://simon-ritchie.github.io/apysc/en/text_underline.html)の確認をお願いします。</span>

# テキストの underline 属性

このページではテキスト関係の`underline`属性について説明します。

## 属性の概要

`underline`属性はテキストの下線のスタイル設定の更新もしくは取得を行います。

## 基本的な使い方

getterもしくはsetterの各インターフェイスの値は`ap.Boolean`の型となります。

もし`ap.Boolean(True)`（もしくは`ap.True_`）の値を指定した場合、テキストは下線を表示します。

```py
# runnable
import apysc as ap

stage: ap.Stage = ap.Stage(
    background_color=ap.Color("#333"),
    stage_width=300,
    stage_height=195,
    stage_elem_id="stage",
)

multi_line_text: ap.MultiLineText = ap.MultiLineText(
    text="Lorem ipsum dolor sit amet, consectetur adipiscing elit, "
    "sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. "
    "Ut enim ad minim veniam",
    width=250,
    fill_color=ap.Colors.GRAY_AAAAAA,
    x=25,
    y=25,
)
multi_line_text.underline = ap.True_

ap.save_overall_html(dest_dir_path="./text_underline_basic_usage/")
```

<iframe src="static/text_underline_basic_usage/index.html" width="300" height="195"></iframe>

## underline 属性のAPI

<span class="inconspicuous-txt">特記事項: このAPIドキュメントはドキュメントビルド用のスクリプトによって自動で生成・同期されています。そのためもしかしたらこの節の内容は前節までの内容と重複している場合があります。</span>

**[インターフェイス概要]**

テキストの下線（`text-decoration: underline`）設定を取得します。<hr>

**[返却値]**

- `underline`: Boolean
  - テキストの下線の設定。

<hr>

**[コードサンプル]**

```py
>>> import apysc as ap
>>> stage: ap.Stage = ap.Stage(
...     background_color=ap.Color("#333"),
...     stage_width=300,
...     stage_height=195,
...     stage_elem_id="stage",
... )
>>> multi_line_text: ap.MultiLineText = ap.MultiLineText(
...     text="Lorem ipsum dolor sit amet, consectetur adipiscing elit, "
...     "sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. "
...     "Ut enim ad minim veniam",
...     width=250,
...     fill_color=ap.Colors.GRAY_AAAAAA,
...     x=25,
...     y=25,
... )
>>> multi_line_text.underline = ap.True_
>>> multi_line_text.underline
Boolean(True)
```