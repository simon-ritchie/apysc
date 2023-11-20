<span class="inconspicuous-txt">※この翻訳ドキュメントはスクリプトによって出力・同期されています。内容が怪しそうな場合は<a href="https://github.com/simon-ritchie/apysc/issues" target="_blank">GitHubにissue</a>を追加したり[英語の原文](https://simon-ritchie.github.io/apysc/en/text_align.html)の確認をお願いします。</span>

# text_align 属性

このページではテキスト関係の`text_align`属性について説明します。

## 属性の概要

`text_align`属性ではインスタンスのテキストの行揃えの設定値の更新もしくは取得を行うことができます。

## 基本的な使い方

getterとsetterの各インターフェイスは`CssTextAlign`のenumの値を受け付けます。

設定できるenumの値は以下の通りです:

- `CssTextAlign.LEFT`
- `CssTextAlign.CENTER`

- `CssTextAlign.RIGHT`
- `CssTextAlign.JUSTIFY

## CssTextAlign.LEFTの例

特記事項 : この設定はデフォルトの設定です。

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
multi_line_text.text_align = ap.CssTextAlign.LEFT

ap.save_overall_html(dest_dir_path="./css_text_align_left/")
```

<iframe src="static/css_text_align_left/index.html" width="350" height="170"></iframe>

## CssTextAlign.CENTERの例

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
multi_line_text.text_align = ap.CssTextAlign.CENTER

ap.save_overall_html(dest_dir_path="./css_text_align_center/")
```

<iframe src="static/css_text_align_center/index.html" width="350" height="170"></iframe>

## CssTextAlign.RIGHTの例

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
multi_line_text.text_align = ap.CssTextAlign.RIGHT

ap.save_overall_html(dest_dir_path="./css_text_align_right/")
```

<iframe src="static/css_text_align_right/index.html" width="350" height="170"></iframe>

## CssTextAlign.JUSTIFYの例

特記じこを : このenumの設定はテキストを均等配置します。

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
multi_line_text.text_align = ap.CssTextAlign.JUSTIFY

ap.save_overall_html(dest_dir_path="./css_text_align_justify/")
```

<iframe src="static/css_text_align_justify/index.html" width="350" height="170"></iframe>

## text_align 属性のAPI

<span class="inconspicuous-txt">特記事項: このAPIドキュメントはドキュメントビルド用のスクリプトによって自動で生成・同期されています。そのためもしかしたらこの節の内容は前節までの内容と重複している場合があります。</span>

**[インターフェイス概要]**

テキストの行揃え設定の値を取得します。<hr>

**[返却値]**

- `text_align`: CssTextAlign
  - 行揃え設定。