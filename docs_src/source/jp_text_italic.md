<span class="inconspicuous-txt">※この翻訳ドキュメントはスクリプトによって出力・同期されています。内容が怪しそうな場合は<a href="https://github.com/simon-ritchie/apysc/issues" target="_blank">GitHubにissue</a>を追加したり[英語の原文](https://simon-ritchie.github.io/apysc/en/text_italic.html)の確認をお願いします。</span>

# テキストの italic 属性

このページではテキスト関係の`italic`属性について説明します。

## 属性の概要

`italic`属性はインスタンスの斜体のスタイル設定の更新もしくは取得を行うことができます。

## 基本的な使い方

getterもしくはsetterの各インターフェイスの値は`ap.Boolean`の型となります。

もし`ap.Boolean(True)`（もしくは`ap.True_`）の値を指定した場合、テキストインスタンスは斜体のスタイル設定になります。

```py
# runnable
import apysc as ap

stage: ap.Stage = ap.Stage(
    background_color=ap.Color("#333"),
    stage_width=350,
    stage_height=170,
    stage_elem_id="stage",
)
multi_line_text: ap.MultiLineText = ap.MultiLineText(
    text="Lorem ipsum dolor sit amet, consectetur adipiscing elit, "
    "sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. "
    "Ut enim ad minim veniam",
    width=300,
    font_size=16,
    fill_color=ap.Color("#00aaff"),
    x=25,
    y=25,
)
multi_line_text.italic = ap.True_

ap.save_overall_html(dest_dir_path="./text_italic_basic_usage/")
```

<iframe src="static/text_italic_basic_usage/index.html" width="350" height="170"></iframe>

## italic 属性のAPI

<span class="inconspicuous-txt">特記事項: このAPIドキュメントはドキュメントビルド用のスクリプトによって自動で生成・同期されています。そのためもしかしたらこの節の内容は前節までの内容と重複している場合があります。</span>

**[インターフェイス概要]**

斜体のスタイル（font-style）設定を取得します。<hr>

**[返却値]**

- `italic`: Boolean
  - 斜体のスタイル（font-style）の設定値。

<hr>

**[コードサンプル]**

```py
>>> import apysc as ap
>>> stage: ap.Stage = ap.Stage(
...     background_color=ap.Color("#333"),
...     stage_width=350,
...     stage_height=170,
...     stage_elem_id="stage",
... )
>>> multi_line_text: ap.MultiLineText = ap.MultiLineText(
...     text="Lorem ipsum dolor sit amet, consectetur adipiscing elit, "
...     "sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. "
...     "Ut enim ad minim veniam",
...     width=300,
...     font_size=16,
...     fill_color=ap.Color("#00aaff"),
...     x=25,
...     y=25,
... )
>>> multi_line_text.italic = ap.True_
>>> multi_line_text.italic
Boolean(True)
```