<span class="inconspicuous-txt">※この翻訳ドキュメントはスクリプトによって出力・同期されています。内容が怪しそうな場合は<a href="https://github.com/simon-ritchie/apysc/issues" target="_blank">GitHubにissue</a>を追加したり[英語の原文](https://simon-ritchie.github.io/apysc/en/text_align_last.html)の確認をお願いします。</span>

# text_align_last 属性

このページではテキスト関係の`text_align_last`属性について説明します。

## 属性の概要

`text_align_last`属性では最終行の行揃えの設定の更新もしくは取得を行えます。

## 基本的な使い方

getterとsetterの各インターフェイスの型は`ap.CssTextAlignLast`のenumの値となります。

指定できるenumの値は以下の通りです:

- `CssTextAlignLast.AUTO` （デフォルト）
- `CssTextAlignLast.LEFT`

- `CssTextAlignLast.CENTER`
- `CssTextAlignLast.RIGHT`

- `CssTextAlignLast.JUSTIFY`

## CssTextAlignLast.AUTOの例

特記事項: この設定はデフォルトの設定です。

`CssTextAlignLast.AUTO`設定（挙動）は`text_align`の設定を継承します。

例えば、もし`text_align`設定が`CssTextAlign.CENTER`の場合には`text_align_last`属性も中央寄せとして振る舞います。

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
multi_line_text.text_align_last = ap.CssTextAlignLast.AUTO

ap.save_overall_html(dest_dir_path="./css_text_align_last_auto/")
```

<iframe src="static/css_text_align_last_auto/index.html" width="350" height="170"></iframe>

## CssTextAlignLast.LEFTの例

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
multi_line_text.text_align_last = ap.CssTextAlignLast.LEFT

ap.save_overall_html(dest_dir_path="./css_text_align_last_left/")
```

<iframe src="static/css_text_align_last_left/index.html" width="350" height="170"></iframe>

## CssTextAlignLast.CENTERの例

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
multi_line_text.text_align_last = ap.CssTextAlignLast.CENTER

ap.save_overall_html(dest_dir_path="./css_text_align_last_center/")
```

<iframe src="static/css_text_align_last_center/index.html" width="350" height="170"></iframe>

## CssTextAlignLast.RIGHTの例

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
multi_line_text.text_align_last = ap.CssTextAlignLast.RIGHT

ap.save_overall_html(dest_dir_path="./css_text_align_last_right/")
```

<iframe src="static/css_text_align_last_right/index.html" width="350" height="170"></iframe>

## CssTextAlignLast.JUSTIFYの例

特記事項: このenumの設定は最終行のテキストを均等に行揃えします。

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
multi_line_text.text_align_last = ap.CssTextAlignLast.JUSTIFY

ap.save_overall_html(dest_dir_path="./css_text_align_last_justify/")
```

<iframe src="static/css_text_align_last_justify/index.html" width="350" height="170"></iframe>

## text_align_last 属性のAPI

<span class="inconspicuous-txt">特記事項: このAPIドキュメントはドキュメントビルド用のスクリプトによって自動で生成・同期されています。そのためもしかしたらこの節の内容は前節までの内容と重複している場合があります。</span>

**[インターフェイス概要]**

text-align-last属性の値を取得します。<hr>

**[返却値]**

- `text_align_last`: CssTextAlignLast
  - text-align-last属性の値。

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
>>> multi_line_text.text_align = ap.CssTextAlign.JUSTIFY
>>> multi_line_text.text_align_last = ap.CssTextAlignLast.RIGHT
>>> assert multi_line_text.text_align_last == ap.CssTextAlignLast.RIGHT
```