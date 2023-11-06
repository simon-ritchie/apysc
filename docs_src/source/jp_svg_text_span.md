<span class="inconspicuous-txt">※この翻訳ドキュメントはスクリプトによって出力・同期されています。内容が怪しそうな場合は<a href="https://github.com/simon-ritchie/apysc/issues" target="_blank">GitHubにissue</a>を追加したり[英語の原文](https://simon-ritchie.github.io/apysc/en/svg_text_span.html)の確認をお願いします。</span>

# SVGTextSpan クラス

このページでは`SVGTextSpan`クラスについて説明します。

## インターフェイス概要

`SVGTextSpan`は`SvgText`の子となるテキスト要素を作成するためのクラスです。

複数の`SVGTextSpan`クラスのインスタンスを使ってそれぞれに異なるテキストのスタイルを設定した状態の`SvgText`のインスタンスを作成することができます。

## 基本的な使い方

`SVGTextSpan`クラスのコンストラクタには`text`引数を必要とします。

コンストラクタでは`font_size`や`font_family`、`fill_color`、`bold`などの各スタイル設定の引数を受け付けます。

もしもそれらのスタイル設定の引数指定を省略した場合、親のSVGTextのインスタンスのスタイルが反映されます。

また、複数の`SVGTextSpan`のインスタンスを使って`SvgText`のインスタンスの作成するには`create_with_svg_text_spans`のクラスメソッドを使うことで対応ができます。

```py
# runnable
import apysc as ap

stage: ap.Stage = ap.Stage(
    background_color=ap.Color("#333"),
    stage_width=200,
    stage_height=50,
    stage_elem_id="stage",
)
svg_text: ap.SvgText = ap.SvgText.create_with_svg_text_spans(
    text_spans=[
        ap.SVGTextSpan(text="Lorem "),
        ap.SVGTextSpan(text="ipsum ", font_size=20, fill_color=ap.Color("#0af")),
        ap.SVGTextSpan(text="dolor ", font_size=12),
    ],
    fill_color=ap.Color("#aaa"),
    font_size=16,
    x=20,
    y=32,
)

ap.save_overall_html(dest_dir_path="svg_txt_span_basic_usage/")
```

<iframe src="static/svg_txt_span_basic_usage/index.html" width="200" height="50"></iframe>

## 改行に対する特記事項

`SVGTextSpan`クラスは改行設定を無視します。

例えば、以下の例では改行用の文字列（`
`）を含んでいますがテキストの行は単一行になっています。

```py
# runnable
import apysc as ap

stage: ap.Stage = ap.Stage(
    background_color=ap.Color("#333"),
    stage_width=200,
    stage_height=50,
    stage_elem_id="stage",
)
svg_text: ap.SvgText = ap.SvgText.create_with_svg_text_spans(
    text_spans=[
        ap.SVGTextSpan(text="Lorem 
"),
        ap.SVGTextSpan(text="ipsum 
"),
        ap.SVGTextSpan(text="dolor"),
    ],
    x=20,
    y=32,
    fill_color=ap.Color("#aaa"),
)

ap.save_overall_html(dest_dir_path="svg_txt_span_notes_of_the_line_break/")
```

<iframe src="static/svg_txt_span_notes_of_the_line_break/index.html" width="200" height="50"></iframe>

もしも改行を加えたい場合には`SVGTextSpan`クラスではなく`SvgText`クラスを使用するか、もしくは複数のインスタンスを作成して対応をお願いします。

## text 属性のインターフェイス例

`text`属性ではインスタンスのテキストの更新もしくは取得を行えます。

```py
# runnable
import apysc as ap

stage: ap.Stage = ap.Stage(
    background_color=ap.Color("#333"),
    stage_width=200,
    stage_height=50,
    stage_elem_id="stage",
)
text_span_1: ap.SVGTextSpan = ap.SVGTextSpan(text="Lorem ")
text_span_2: ap.SVGTextSpan = ap.SVGTextSpan(text="ipsum")
text_span_2.text = ap.String("dolor")

svg_text: ap.SvgText = ap.SvgText.create_with_svg_text_spans(
    text_spans=[text_span_1, text_span_2],
    font_size=16,
    x=20,
    y=32,
    fill_color=ap.Color("#aaa"),
)

ap.save_overall_html(dest_dir_path="svg_txt_span_text/")
```

<iframe src="static/svg_txt_span_text/index.html" width="200" height="50"></iframe>

## font_size 属性のインターフェイス例

`font_size`属性ではインスタンスのフォントサイズの更新もしくは取得を行えます。

```py
# runnable
import apysc as ap

stage: ap.Stage = ap.Stage(
    background_color=ap.Color("#333"),
    stage_width=200,
    stage_height=50,
    stage_elem_id="stage",
)
text_span_1: ap.SVGTextSpan = ap.SVGTextSpan(text="Lorem ")
text_span_2: ap.SVGTextSpan = ap.SVGTextSpan(text="ipsum")
text_span_2.font_size = ap.Int(25)

svg_text: ap.SvgText = ap.SvgText.create_with_svg_text_spans(
    text_spans=[text_span_1, text_span_2],
    font_size=16,
    x=20,
    y=32,
    fill_color=ap.Color("#aaa"),
)

ap.save_overall_html(dest_dir_path="svg_txt_span_font_size/")
```

<iframe src="static/svg_txt_span_font_size/index.html" width="200" height="50"></iframe>

## font_family 属性のインターフェイス例

`font_family`属性ではインスタンスのフォントファミリー（フォントの指定）の更新もしくは取得を行えます。

この属性は各フォント名の`String`型の文字列を格納した`Array`型の配列を必要とします。

```py
# runnable
import apysc as ap

stage: ap.Stage = ap.Stage(
    background_color=ap.Color("#333"),
    stage_width=200,
    stage_height=50,
    stage_elem_id="stage",
)
text_span_1: ap.SVGTextSpan = ap.SVGTextSpan(text="Lorem ")
text_span_2: ap.SVGTextSpan = ap.SVGTextSpan(text="ipsum")
text_span_2.font_family = ap.Array([ap.String("Impact"), ap.String("Arial")])

svg_text: ap.SvgText = ap.SvgText.create_with_svg_text_spans(
    text_spans=[text_span_1, text_span_2],
    font_size=16,
    x=20,
    y=32,
    fill_color=ap.Color("#aaa"),
)

ap.save_overall_html(dest_dir_path="svg_txt_span_font_family/")
```

<iframe src="static/svg_txt_span_font_family/index.html" width="200" height="50"></iframe>

## fill_color属性のインターフェイス例

`fill_color`属性は塗りの色の値の更新もしくは取得を行えます:

```py
# runnable
import apysc as ap

stage: ap.Stage = ap.Stage(
    background_color=ap.Color("#333"),
    stage_width=200,
    stage_height=50,
    stage_elem_id="stage",
)
text_span_1: ap.SVGTextSpan = ap.SVGTextSpan(text="Lorem ")
text_span_2: ap.SVGTextSpan = ap.SVGTextSpan(text="ipsum")
text_span_2.fill_color = ap.Color("#0af")

svg_text: ap.SvgText = ap.SvgText.create_with_svg_text_spans(
    text_spans=[text_span_1, text_span_2],
    font_size=16,
    x=20,
    y=32,
    fill_color=ap.Color("#aaa"),
)

ap.save_overall_html(dest_dir_path="svg_txt_span_fill_color/")
```

<iframe src="static/svg_txt_span_fill_color/index.html" width="200" height="50"></iframe>

## fill_alpha属性のインターフェイス例

`fill_alpha`属性は塗りの透明度の値の更新もしくは取得を行えます:

```py
# runnable
import apysc as ap

stage: ap.Stage = ap.Stage(
    background_color=ap.Color("#333"),
    stage_width=200,
    stage_height=50,
    stage_elem_id="stage",
)
text_span_1: ap.SVGTextSpan = ap.SVGTextSpan(text="Lorem ")
text_span_2: ap.SVGTextSpan = ap.SVGTextSpan(text="ipsum")
text_span_2.fill_alpha = ap.Number(0.3)

svg_text: ap.SvgText = ap.SvgText.create_with_svg_text_spans(
    text_spans=[text_span_1, text_span_2],
    font_size=16,
    x=20,
    y=32,
    fill_color=ap.Color("#aaa"),
)

ap.save_overall_html(dest_dir_path="svg_txt_span_fill_alpha/")
```

<iframe src="static/svg_txt_span_fill_alpha/index.html" width="200" height="50"></iframe>

## line_color属性のインターフェイス例

`line_color`属性では線の色の値の更新もしくは取得を行えます:

```py
# runnable
import apysc as ap

stage: ap.Stage = ap.Stage(
    background_color=ap.Color("#333"),
    stage_width=200,
    stage_height=50,
    stage_elem_id="stage",
)
text_span_1: ap.SVGTextSpan = ap.SVGTextSpan(
    text="Lorem ", line_thickness=1, font_size=20, bold=True
)
text_span_1.line_color = ap.Color("#aaa")
text_span_2: ap.SVGTextSpan = ap.SVGTextSpan(
    text="ipsum", line_thickness=1, font_size=20, bold=True
)
text_span_2.line_color = ap.Color("#0af")

svg_text: ap.SvgText = ap.SvgText.create_with_svg_text_spans(
    text_spans=[text_span_1, text_span_2],
    font_size=16,
    x=20,
    y=32,
    fill_color=ap.COLORLESS,
)

ap.save_overall_html(dest_dir_path="svg_txt_span_line_color/")
```

<iframe src="static/svg_txt_span_line_color/index.html" width="200" height="50"></iframe>

## line_alpha属性のインターフェイス例

`line_alpha`属性では線の透明度の値の更新もしくは取得を行えます:

```py
# runnable
import apysc as ap

stage: ap.Stage = ap.Stage(
    background_color=ap.Color("#333"),
    stage_width=200,
    stage_height=50,
    stage_elem_id="stage",
)
text_span_1: ap.SVGTextSpan = ap.SVGTextSpan(
    text="Lorem ",
    line_color=ap.Color("#0af"),
    line_thickness=1,
    font_size=20,
    bold=True,
)
text_span_2: ap.SVGTextSpan = ap.SVGTextSpan(
    text="ipsum",
    line_color=ap.Color("#0af"),
    line_thickness=1,
    font_size=20,
    bold=True,
)
text_span_2.line_alpha = ap.Number(0.3)

svg_text: ap.SvgText = ap.SvgText.create_with_svg_text_spans(
    text_spans=[text_span_1, text_span_2],
    font_size=16,
    x=20,
    y=32,
    fill_color=ap.COLORLESS,
)

ap.save_overall_html(dest_dir_path="svg_txt_span_line_alpha/")
```

<iframe src="static/svg_txt_span_line_alpha/index.html" width="200" height="50"></iframe>

## line_thickness属性のインターフェイス例

`line_thickness`属性では線の幅の更新もしくは取得を行えます:

```py
# runnable
import apysc as ap

stage: ap.Stage = ap.Stage(
    background_color=ap.Color("#333"),
    stage_width=200,
    stage_height=50,
    stage_elem_id="stage",
)
text_span_1: ap.SVGTextSpan = ap.SVGTextSpan(
    text="Lorem ",
    line_color=ap.Color("#0af"),
    font_size=20,
    bold=True,
)
text_span_2: ap.SVGTextSpan = ap.SVGTextSpan(
    text="ipsum",
    line_color=ap.Color("#0af"),
    font_size=20,
    bold=True,
)
text_span_1.line_thickness = ap.Int(3)
text_span_2.line_thickness = ap.Int(3)

svg_text: ap.SvgText = ap.SvgText.create_with_svg_text_spans(
    text_spans=[text_span_1, text_span_2],
    font_size=16,
    x=20,
    y=32,
    fill_color=ap.COLORLESS,
)

ap.save_overall_html(dest_dir_path="svg_txt_span_line_thickness/")
```

<iframe src="static/svg_txt_span_line_thickness/index.html" width="200" height="50"></iframe>

## bold 属性のインターフェイス例

`bold`属性ではインスタンスの太字設定の更新もしくは取得を行えます。

```py
# runnable
import apysc as ap

stage: ap.Stage = ap.Stage(
    background_color=ap.Color("#333"),
    stage_width=200,
    stage_height=50,
    stage_elem_id="stage",
)
text_span_1: ap.SVGTextSpan = ap.SVGTextSpan(text="Lorem ")
text_span_2: ap.SVGTextSpan = ap.SVGTextSpan(text="ipsum")
text_span_2.bold = ap.Boolean(True)

svg_text: ap.SvgText = ap.SvgText.create_with_svg_text_spans(
    text_spans=[text_span_1, text_span_2],
    font_size=16,
    x=20,
    y=32,
    fill_color=ap.Color("#aaa"),
)

ap.save_overall_html(dest_dir_path="svg_txt_span_bold/")
```

<iframe src="static/svg_txt_span_bold/index.html" width="200" height="50"></iframe>

## italic 属性のインターフェイス例

`italic`属性ではインスタンスの斜体の設定の更新もしくは取得を行えます。

```py
# runnable
import apysc as ap

stage: ap.Stage = ap.Stage(
    background_color=ap.Color("#333"),
    stage_width=200,
    stage_height=50,
    stage_elem_id="stage",
)
text_span_1: ap.SVGTextSpan = ap.SVGTextSpan(text="Lorem ")
text_span_2: ap.SVGTextSpan = ap.SVGTextSpan(text="ipsum")
text_span_2.italic = ap.Boolean(True)

svg_text: ap.SvgText = ap.SvgText.create_with_svg_text_spans(
    text_spans=[text_span_1, text_span_2],
    font_size=16,
    x=20,
    y=32,
    fill_color=ap.Color("#aaa"),
)

ap.save_overall_html(dest_dir_path="svg_txt_span_italic/")
```

<iframe src="static/svg_txt_span_italic/index.html" width="200" height="50"></iframe>

## delta_x 属性のインターフェイス例

`delta_x`属性ではインスタンスのX座標の調整値の更新もしくは取得を行えます。

```py
# runnable
import apysc as ap

stage: ap.Stage = ap.Stage(
    background_color=ap.Color("#333"),
    stage_width=200,
    stage_height=50,
    stage_elem_id="stage",
)
text_span_1: ap.SVGTextSpan = ap.SVGTextSpan(text="Lorem ")
text_span_2: ap.SVGTextSpan = ap.SVGTextSpan(text="ipsum")
text_span_2.delta_x = ap.Number(-20)

svg_text: ap.SvgText = ap.SvgText.create_with_svg_text_spans(
    text_spans=[text_span_1, text_span_2],
    font_size=16,
    x=20,
    y=32,
    fill_color=ap.Color("#aaa"),
)

ap.save_overall_html(dest_dir_path="svg_txt_span_delta_x/")
```

<iframe src="static/svg_txt_span_delta_x/index.html" width="200" height="50"></iframe>

## delta_y 属性のインターフェイス例

`delta_y`属性ではインスタンスのY座標の調整値の更新もくしは取得を行えます。

特記事項: この設定は直前の`SVGTextSpan`インスタンスの設定を引き継ぎます。

```py
# runnable
import apysc as ap

stage: ap.Stage = ap.Stage(
    background_color=ap.Color("#333"),
    stage_width=200,
    stage_height=80,
    stage_elem_id="stage",
)
text_span_1: ap.SVGTextSpan = ap.SVGTextSpan(text="Lorem ")
text_span_2: ap.SVGTextSpan = ap.SVGTextSpan(text="ipsum ")
text_span_3: ap.SVGTextSpan = ap.SVGTextSpan(text="dolar")

text_span_2.delta_y = ap.Number(10)
text_span_3.delta_y = ap.Number(10)

svg_text: ap.SvgText = ap.SvgText.create_with_svg_text_spans(
    text_spans=[text_span_1, text_span_2],
    font_size=16,
    x=20,
    y=32,
    fill_color=ap.Color("#aaa"),
)

ap.save_overall_html(dest_dir_path="svg_txt_span_delta_y/")
```

<iframe src="static/svg_txt_span_delta_y/index.html" width="200" height="80"></iframe>

## SVGTextSpan クラスのコンストラクタのAPI

<span class="inconspicuous-txt">特記事項: このAPIドキュメントはドキュメントビルド用のスクリプトによって自動で生成・同期されています。そのためもしかしたらこの節の内容は前節までの内容と重複している場合があります。</span>

**[インターフェイスの構造]** `__init__(self, *, text: Union[str, apysc._type.string.String], font_size: Union[int, apysc._type.int.Int, NoneType] = None, font_family: Union[apysc._type.array.Array[apysc._type.string.String], List[str], NoneType] = None, fill_color: Union[apysc._color.color.Color, NoneType] = None, fill_alpha: Union[float, apysc._type.number.Number, NoneType] = None, line_color: Union[apysc._color.color.Color, NoneType] = None, line_alpha: Union[float, apysc._type.number.Number, NoneType] = None, line_thickness: Union[int, apysc._type.int.Int, NoneType] = None, bold: Union[bool, apysc._type.boolean.Boolean, NoneType] = None, italic: Union[bool, apysc._type.boolean.Boolean, NoneType] = None, delta_x: Union[float, apysc._type.number.Number] = 0.0, delta_y: Union[float, apysc._type.number.Number] = 0.0, variable_name_suffix: str = '') -> None`<hr>

**[インターフェイス概要]**

`SvgText`の子となるSVGのtext-span要素のためのクラスです。<hr>

**[引数]**

- `text`: Union[str, String]
  - このクラスで使用するテキスト。

- `font_size`: Optional[Union[int, Int]], optional
  - フォントサイズ設定。

- `font_family`: Optional[Union[Array[String], List[str]]], optional
  - フォントファミリー設定。配列内の各文字列には個別のフォント名を指定する必要があります（例: `Times New Roman`）。

- `fill_color`: Optional[Color], optional
  - 塗りの色の設定。

- `fill_alpha`: Optional[Union[float, Number]], optional
  - 塗りの透明度の設定。

- `line_color`: Optional[Color], optional
  - 線の色の設定。

- `line_alpha`: Optional[Union[float, Number]], optional
  - 線の透明度の設定。

- `line_thickness`: Optional[Union[int, Int]], optional
  - 設定の線幅。

- `bold`: Optional[Union[bool, Boolean]], optional
  - テキストに太字のスタイル設定を行うかどうかの真偽値。

- `italic`: Optional[Union[bool, Boolean]], optional
  - テキストを斜体表示のスタイル設定を行うかどうかの真偽値。

- `delta_x`: Union[float, Number], optional
  - X座標の調整値の設定。特記事項 : この設定は後に続く`SVGTextSpan`のインスタンスの座標も変更します。

- `delta_y`: Union[float, Number], optional
  - Y座標の調整値の設定。特記事項 : この設定は後に続く`SVGTextSpan`のインスタンスの座標も更新します。

- `variable_name_suffix`: str, optional
  - JavaScript上の変数のサフィックスの設定です。この設定はJavaScriptのデバッグ時に役立つことがあります。

<hr>

**[特記事項]**

 ・もしも各種スタイル設定に`None`が指定された場合、そのスタイルは親のスタイル設定を引き継ぎます。<hr>

**[コードサンプル]**

```py
>>> import apysc as ap
>>> stage: ap.Stage = ap.Stage(
...     background_color=ap.Color("#333"), stage_width=200, stage_height=50
... )
>>> svg_text: ap.SvgText = ap.SvgText.create_with_svg_text_spans(
...     text_spans=[
...         ap.SVGTextSpan(text="Hello, "),
...         ap.SVGTextSpan(text="Hello, ", font_size=14),
...     ],
...     font_size=20,
...     fill_color=ap.Color("#0af"),
... )
```

<hr>

**[関連資料]**

- [SvgText クラス](https://simon-ritchie.github.io/apysc/jp/jp_svg_text.html)

## SvgText クラスの create_with_svg_text_spans クラスメソッドのAPI

<span class="inconspicuous-txt">特記事項: このAPIドキュメントはドキュメントビルド用のスクリプトによって自動で生成・同期されています。そのためもしかしたらこの節の内容は前節までの内容と重複している場合があります。</span>

**[インターフェイスの構造]** `create_with_svg_text_spans(*, text_spans: Union[List[apysc._display.svg_text_span.SVGTextSpan], apysc._type.array.Array[apysc._display.svg_text_span.SVGTextSpan]], font_size: Union[int, apysc._type.int.Int] = 16, font_family: Union[apysc._type.array.Array[apysc._type.string.String], List[str], NoneType] = None, x: Union[float, apysc._type.number.Number] = 0.0, y: Union[float, apysc._type.number.Number] = 16.0, fill_color: apysc._color.color.Color = Color("#666666"), fill_alpha: Union[float, apysc._type.number.Number] = 1.0, line_color: apysc._color.color.Color = Color(""), line_alpha: Union[float, apysc._type.number.Number] = 1.0, line_thickness: Union[int, apysc._type.int.Int] = 1, leading: Union[float, apysc._type.number.Number] = 1.5, align: apysc._display.svg_text_align_mixin.SVGTextAlign = <SVGTextAlign.LEFT: 'start'>, bold: Union[bool, apysc._type.boolean.Boolean] = False, italic: Union[bool, apysc._type.boolean.Boolean] = False, parent: Union[apysc._display.child_mixin.ChildMixIn, NoneType] = None, variable_name_suffix: str = '') -> 'SvgText'`<hr>

**[インターフェイス概要]**

指定された各text spanのインスタンスを使用して`SvgText`のインスタンスを生成します。<hr>

**[引数]**

- `text_spans`: Union[List[SVGTextSpan], Array[SVGTextSpan]]
  - 各text span。

- `font_size`: Union[int, Int], optional
  - テキスト全体に設定するフォントサイズの設定。

- `font_family`: Optional[Union[Array[String], List[str]]], optional
  - テキスト全体に設定するフォント設定。配列内の各文字列はフォント名を指定する必要があります（例 : `Times New Roman`）。

- `x`: Union[float, Number], optional
  - 描画を開始するX座標。

- `y`: Union[float, Number], optional
  - 描画を開始するY座標（`特記事項`の節も確認をお願いします）。

- `fill_color`: Color, optional
  - テキスト全体に設定する塗りの色。

- `fill_alpha`: float or Number, optional
  - テキスト全体に設定する塗りの透明度。

- `line_color`: str or String, optional
  - テキスト全体に設定する線の色。

- `line_alpha`: float or Number, optional
  - テキスト全体に設定する線の透明度。

- `line_thickness`: int or Int, optional
  - テキスト全体に設定する線幅。

- `leading`: float or Number, optional
  - テキスト全体に設定する行間設定。

- `align`: SVGTextAlign, optional
  - テキスト全体に設定する行揃え設定。

- `bold`: Union[bool, Boolean], optional
  - テキストに太字のスタイル設定を行うかどうかの真偽値。

- `italic`: Union[bool, Boolean], optional
  - テキストを斜体表示のスタイル設定を行うかどうかの真偽値。

- `parent`: Optional[ChildMixIn], optional
  - このインスタンスを追加する親のインスタンス。もしもNoneが指定された場合、このインスタンスはステージのインスタンスへと追加されます。

- `variable_name_suffix`: str, optional
  - JavaScript上の変数のサフィックスの設定です。この設定はJavaScriptのデバッグ時に役立つことがあります。

<hr>

**[返却値]**

- `svg_text`: SvgText
  - 生成された`SvgText`のインスタンス。

<hr>

**[特記事項]**

 ・SVGTextクラスの座標の0の位置はテキストの下部からスタートします。そのためもしもy=0を指定した場合、テキストはほとんど見えない状態になります。<hr>

**[コードサンプル]**

```py
>>> import apysc as ap
>>> stage: ap.Stage = ap.Stage(
...     background_color=ap.Color("#333"),
...     stage_width=200,
...     stage_height=50,
... )
>>> svg_text: ap.SvgText = ap.SvgText.create_with_svg_text_spans(
...     text_spans=[
...         ap.SVGTextSpan(text="Hello, "),
...         ap.SVGTextSpan(text="Hello, ", font_size=14),
...     ],
...     font_size=20,
...     fill_color=ap.Color("#0af"),
... )
```

<hr>

**[関連資料]**

- [SvgText クラス](https://simon-ritchie.github.io/apysc/jp/jp_svg_text.html)