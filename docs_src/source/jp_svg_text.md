<span class="inconspicuous-txt">※この翻訳ドキュメントはスクリプトによって出力・同期されています。内容が怪しそうな場合は<a href="https://github.com/simon-ritchie/apysc/issues" target="_blank">GitHubにissue</a>を追加したり[英語の原文](https://simon-ritchie.github.io/apysc/en/svg_text.html)の確認をお願いします。</span>

# SVGText クラス

このページでは`SVGText`クラスについて説明します。

## クラス概要

`SVGText`クラスはSVGテキストのオブジェクトを生成します。

## 基本的な使い方

`SVGText`クラスのコンストラクタは`text`引数の指定を必要とします。

コンストラクタでは`font_size`や`font_family`、`fill_color`、`bold`などのフォントやスタイルなどの引数を指定することもできます。

```py
# runnable
import apysc as ap

ap.Stage(
    background_color="#333", stage_width=200, stage_height=50, stage_elem_id="stage"
)
svg_text: ap.SVGText = ap.SVGText(
    text="Hello, world!",
    x=20,
    y=32,
    fill_color="#aaa",
)
ap.save_overall_html(dest_dir_path="svg_text_basic_usage/")
```

<iframe src="static/svg_text_basic_usage/index.html" width="200" height="50"></iframe>

## テキストのY座標の基準点に対する特記事項

テキストのY座標の基準点はテキストの下部付近の位置となります（これはSVGテキストの仕様となります）。

そのためもしもY座標に`y=0`を指定した場合、テキストのコンテンツがほとんど見えなくなります（以下の例では辛うじてコンマの一部が確認できます）。

```py
# runnable
import apysc as ap

ap.Stage(
    background_color="#333", stage_width=200, stage_height=50, stage_elem_id="stage"
)
svg_text: ap.SVGText = ap.SVGText(
    text="Hello, world!",
    x=20,
    y=0,
    fill_color="#aaa",
)
ap.save_overall_html(dest_dir_path="svg_text_note_on_the_y_baseline/")
```

<iframe src="static/svg_text_note_on_the_y_baseline/index.html" width="200" height="50"></iframe>

## text 属性のインターフェイス例

`text`属性ではインスタンスのテキストの更新もしくは取得を行えます。

```py
# runnable
import apysc as ap

ap.Stage(
    background_color="#333", stage_width=200, stage_height=50, stage_elem_id="stage"
)
svg_text: ap.SVGText = ap.SVGText(
    text="Hello, world!",
    x=20,
    y=32,
    fill_color="#aaa",
)
svg_text.text = ap.String("Lorem ipsum")
ap.save_overall_html(dest_dir_path="svg_text_text/")
```

<iframe src="static/svg_text_text/index.html" width="200" height="50"></iframe>

## font_size 属性のインターフェイス例

`font_size`属性ではインスタンスのフォントサイズの更新もしくは取得を行えます。

```py
# runnable
import apysc as ap

ap.Stage(
    background_color="#333", stage_width=200, stage_height=50, stage_elem_id="stage"
)
svg_text: ap.SVGText = ap.SVGText(
    text="Hello, world!",
    x=20,
    y=34,
    fill_color="#aaa",
)
svg_text.font_size = ap.Int(24)
ap.save_overall_html(dest_dir_path="svg_text_font_size/")
```

<iframe src="static/svg_text_font_size/index.html" width="200" height="50"></iframe>

## font_family 属性のインターフェイス例

`font_family`属性ではインスタンスのフォントファミリー（フォントの指定）の更新もしくは取得を行えます。

この属性は各フォント名の`String`型の文字列を格納した`Array`型の配列を必要とします。

```py
# runnable
import apysc as ap

ap.Stage(
    background_color="#333", stage_width=200, stage_height=50, stage_elem_id="stage"
)
svg_text: ap.SVGText = ap.SVGText(
    text="Hello, world!",
    x=20,
    y=32,
    fill_color="#aaa",
)
svg_text.font_family = ap.Array([ap.String("Impact"), ap.String("Times New Roman")])
ap.save_overall_html(dest_dir_path="svg_text_font_family/")
```

<iframe src="static/svg_text_font_family/index.html" width="200" height="50"></iframe>

## x属性のインターフェイス例

`x`属性ではX座標の値の更新もしくは取得を行えます:

```py
# runnable
import apysc as ap

ap.Stage(
    background_color="#333", stage_width=200, stage_height=50, stage_elem_id="stage"
)
svg_text: ap.SVGText = ap.SVGText(
    text="Hello, world!",
    y=32,
    fill_color="#aaa",
)
svg_text.x = ap.Number(50)
ap.save_overall_html(dest_dir_path="svg_text_x/")
```

<iframe src="static/svg_text_x/index.html" width="200" height="50"></iframe>

## y属性のインターフェイス例

`y`属性ではY座標の値の更新もしくは取得を行えます:

```py
# runnable
import apysc as ap

ap.Stage(
    background_color="#333", stage_width=200, stage_height=70, stage_elem_id="stage"
)
svg_text: ap.SVGText = ap.SVGText(
    text="Hello, world!",
    x=20,
    y=32,
    fill_color="#aaa",
)
svg_text.y = ap.Number(45)
ap.save_overall_html(dest_dir_path="svg_text_y/")
```

<iframe src="static/svg_text_y/index.html" width="200" height="70"></iframe>

## fill_color属性のインターフェイス例

`fill_color`属性は塗りの色の値の更新もしくは取得を行えます:

```py
# runnable
import apysc as ap

ap.Stage(
    background_color="#333", stage_width=200, stage_height=50, stage_elem_id="stage"
)
svg_text: ap.SVGText = ap.SVGText(
    text="Hello, world!",
    x=20,
    y=32,
)
svg_text.fill_color = ap.String("#0af")
ap.save_overall_html(dest_dir_path="svg_text_fill_color/")
```

<iframe src="static/svg_text_fill_color/index.html" width="200" height="50"></iframe>

## fill_alpha属性のインターフェイス例

`fill_alpha`属性は塗りの透明度の値の更新もしくは取得を行えます:

```py
# runnable
import apysc as ap

ap.Stage(
    background_color="#333", stage_width=200, stage_height=50, stage_elem_id="stage"
)
svg_text: ap.SVGText = ap.SVGText(
    text="Hello, world!",
    x=20,
    y=32,
    fill_color="#aaa",
)
svg_text.fill_alpha = ap.Number(0.3)
ap.save_overall_html(dest_dir_path="svg_text_fill_alpha/")
```

<iframe src="static/svg_text_fill_alpha/index.html" width="200" height="50"></iframe>

## line_color属性のインターフェイス例

`line_color`属性では線の色の値の更新もしくは取得を行えます:

```py
# runnable
import apysc as ap

ap.Stage(
    background_color="#333", stage_width=200, stage_height=50, stage_elem_id="stage"
)
svg_text: ap.SVGText = ap.SVGText(
    text="Hello, world!",
    x=20,
    y=34,
    font_size=24,
    bold=True,
    fill_color="",
    line_thickness=1,
)
svg_text.line_color = ap.String("#0af")
ap.save_overall_html(dest_dir_path="svg_text_line_color/")
```

<iframe src="static/svg_text_line_color/index.html" width="200" height="50"></iframe>

## line_alpha属性のインターフェイス例

`line_alpha`属性では線の透明度の値の更新もしくは取得を行えます:

```py
# runnable
import apysc as ap

ap.Stage(
    background_color="#333", stage_width=200, stage_height=50, stage_elem_id="stage"
)
svg_text: ap.SVGText = ap.SVGText(
    text="Hello, world!",
    x=20,
    y=34,
    font_size=24,
    bold=True,
    fill_color="",
    line_color="#0af",
    line_thickness=1,
)
svg_text.line_alpha = ap.Number(0.3)
ap.save_overall_html(dest_dir_path="svg_text_line_alpha/")
```

<iframe src="static/svg_text_line_alpha/index.html" width="200" height="50"></iframe>

## line_thickness属性のインターフェイス例

`line_thickness`属性では線の幅の更新もしくは取得を行えます:

```py
# runnable
import apysc as ap

ap.Stage(
    background_color="#333", stage_width=200, stage_height=50, stage_elem_id="stage"
)
svg_text: ap.SVGText = ap.SVGText(
    text="Hello, world!",
    x=20,
    y=34,
    font_size=24,
    bold=True,
    fill_color="",
    line_color="#0af",
)
svg_text.line_thickness = ap.Int(3)
ap.save_overall_html(dest_dir_path="svg_text_line_thickness/")
```

<iframe src="static/svg_text_line_thickness/index.html" width="200" height="50"></iframe>

## leading 属性のインターフェイス例

`leading`属性ではインスタンスの行間の更新もしくは取得を行えます。

```py
# runnable
import apysc as ap

ap.Stage(
    background_color="#333", stage_width=500, stage_height=120, stage_elem_id="stage"
)
svg_text: ap.SVGText = ap.SVGText(
    text="Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
"
    "sed do eiusmod tempor incididunt",
    x=20,
    y=32,
    fill_color="#aaa",
)
svg_text.leading = ap.Number(2.0)

ap.save_overall_html(dest_dir_path="svg_text_leading/")
```

<iframe src="static/svg_text_leading/index.html" width="500" height="120"></iframe>

## align 属性のインターフェイス例

`align`属性ではインスタンスの水平方向の行揃えの設定（左端、中央、右端）の更新もしくは取得を行えます。

この属性は`SVGTextAlign`のenumの値を必要とします。

```py
# runnable
import apysc as ap

ap.Stage(
    background_color="#333", stage_width=500, stage_height=100, stage_elem_id="stage"
)
svg_text: ap.SVGText = ap.SVGText(
    text="Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
"
    "sed do eiusmod tempor incididunt",
    x=250,
    y=32,
    fill_color="#aaa",
)
svg_text.align = ap.SVGTextAlign.CENTER

ap.save_overall_html(dest_dir_path="svg_text_align/")
```

<iframe src="static/svg_text_align/index.html" width="500" height="100"></iframe>

特記事項: この属性はX座標の基準位置（`x=0`の位置）を以下のように変更します:

- SVGTextAlign.CENTER: X座標の基準位置はテキストの中央位置になります。
- SVGTextAlign.RIGHT: X座標の基準位置はテキストの右端の位置になります。

```py
# runnable
import apysc as ap

STAGE_WIDTH: int = 500
STAGE_HEIGHT: int = 120
ap.Stage(
    background_color="#333",
    stage_width=STAGE_WIDTH,
    stage_height=STAGE_HEIGHT,
    stage_elem_id="stage",
)
container_sprite: ap.Sprite = ap.Sprite()
container_sprite.x = ap.Number(STAGE_WIDTH / 2)

vertical_x0_line: ap.Line = ap.Line(
    start_point=ap.Point2D(0, 0),
    end_point=ap.Point2D(0, STAGE_HEIGHT),
    line_color="#666",
    parent=container_sprite,
)
x0_text: ap.SVGText = ap.SVGText(
    text="Text's x=0 position",
    fill_color="#666",
    x=5,
    y=20,
    parent=container_sprite,
)

left_align_sample_text: ap.SVGText = ap.SVGText(
    text="Left align sample (default)",
    x=0,
    y=52,
    fill_color="#aaa",
    parent=container_sprite,
)

center_align_sample_text: ap.SVGText = ap.SVGText(
    text="Center align sample",
    x=0,
    y=72,
    fill_color="#aaa",
    parent=container_sprite,
)
center_align_sample_text.align = ap.SVGTextAlign.CENTER

right_align_sample_text: ap.SVGText = ap.SVGText(
    text="Right align sample",
    x=0,
    y=92,
    fill_color="#aaa",
    parent=container_sprite,
)
right_align_sample_text.align = ap.SVGTextAlign.RIGHT

ap.save_overall_html(dest_dir_path="svg_text_align_note/")
```

<iframe src="static/svg_text_align_note/index.html" width="500" height="120"></iframe>

## bold 属性のインターフェイス例

`bold`属性ではインスタンスの太字設定の更新もしくは取得を行えます。

```py
# runnable
import apysc as ap

ap.Stage(
    background_color="#333", stage_width=200, stage_height=50, stage_elem_id="stage"
)
svg_text: ap.SVGText = ap.SVGText(
    text="Bold style sample",
    x=20,
    y=32,
    fill_color="#aaa",
)
svg_text.bold = ap.Boolean(True)
ap.save_overall_html(dest_dir_path="svg_text_bold/")
```

<iframe src="static/svg_text_bold/index.html" width="200" height="50"></iframe>

## italic 属性のインターフェイス例

`italic`属性ではインスタンスの斜体の設定の更新もしくは取得を行えます。

```py
# runnable
import apysc as ap

ap.Stage(
    background_color="#333", stage_width=200, stage_height=50, stage_elem_id="stage"
)
svg_text: ap.SVGText = ap.SVGText(
    text="Italic style sample",
    x=20,
    y=32,
    fill_color="#aaa",
)
svg_text.italic = ap.Boolean(True)
ap.save_overall_html(dest_dir_path="svg_text_italic/")
```

<iframe src="static/svg_text_italic/index.html" width="200" height="50"></iframe>

## rotation_around_center属性のインターフェイス例

`rotation_around_center`属性ではインスタンスの中央座標での回転量（0～359）の更新もしくは取得を行えます:

```py
# runnable
import apysc as ap

stage: ap.Stage = ap.Stage(
    background_color="#333", stage_width=200, stage_height=50, stage_elem_id="stage"
)
svg_text: ap.SVGText = ap.SVGText(
    text="Hello, world!",
    x=100,
    y=32,
    fill_color="#aaa",
    align=ap.SVGTextAlign.CENTER,
)


def on_enter_frame(e: ap.EnterFrameEvent, optional: dict) -> None:
    """
    The handler to handle a timer event.

    Parameters
    ----------
    e : ap.EnterFrameEvent
        Event instance.
    optional : dict
        Optional argument dictionary.
    """
    svg_text.rotation_around_center += 1


stage.enter_frame(handler=on_enter_frame)
ap.save_overall_html(dest_dir_path="svg_txt_rotation_around_center/")
```

<iframe src="static/svg_txt_rotation_around_center/index.html" width="200" height="50"></iframe>

## set_rotation_around_pointとget_rotation_around_pointメソッドのインターフェイス例

`set_rotation_around_point`メソッドは指定された座標からのインスタンスの回転量（0～359）を更新します。

同様に、`get_rotation_around_point`メソッドでは指定された座標のインスタンスの回転量（0～359）を取得します:

```py
# runnable
import apysc as ap

stage: ap.Stage = ap.Stage(
    background_color="#333", stage_width=200, stage_height=120, stage_elem_id="stage"
)
X: ap.Number = ap.Number(20)
Y: ap.Number = ap.Number(32)
svg_text: ap.SVGText = ap.SVGText(
    text="Hello, world!",
    x=X,
    y=Y,
    fill_color="#aaa",
)


def on_enter_frame(e: ap.EnterFrameEvent, optional: dict) -> None:
    """
    The handler to handle a timer event.

    Parameters
    ----------
    e : ap.EnterFrameEvent
        Event instance.
    optional : dict
        Optional argument dictionary.
    """
    rotation: ap.Int = (
        svg_text.get_rotation_around_point(
            x=X,
            y=Y,
        )
        + 1
    )
    svg_text.set_rotation_around_point(
        rotation=rotation,
        x=X,
        y=Y,
    )


stage.enter_frame(handler=on_enter_frame)
ap.save_overall_html(dest_dir_path="svg_txt_rotation_around_point/")
```

<iframe src="static/svg_txt_rotation_around_point/index.html" width="200" height="120"></iframe>

## 拡縮関係のインターフェイスに対する特記事項

拡縮関係のインターフェイスは設定次第では表示が崩れたりするため利用は非推奨です。

## scale_x_from_center属性のインターフェイス例

`scale_x_from_center`属性ではインスタンスの中央座標でのX軸の拡縮値の更新もしくは取得を行えます:

```py
# runnable
import apysc as ap

stage: ap.Stage = ap.Stage(
    background_color="#333", stage_width=200, stage_height=50, stage_elem_id="stage"
)
direction: ap.Int = ap.Int(-1)
svg_text: ap.SVGText = ap.SVGText(
    text="Hello, world!",
    x=20,
    y=32,
    fill_color="#aaa",
)


def on_enter_frame(e: ap.EnterFrameEvent, optional: dict) -> None:
    """
    The handler to handle a timer event.

    Parameters
    ----------
    e : ap.EnterFrameEvent
        Event instance.
    optional : dict
        Optional argument dictionary.
    """
    scale: ap.Number = svg_text.scale_x_from_center
    with ap.If(scale > 1):
        direction.value = -1
    with ap.If(scale <= 0.3):
        direction.value = 1
    scale += direction * 0.005
    svg_text.scale_x_from_center = scale


stage.enter_frame(handler=on_enter_frame)
ap.save_overall_html(dest_dir_path="svg_txt_scale_x_from_center/")
```

<iframe src="static/svg_txt_scale_x_from_center/index.html" width="200" height="50"></iframe>

## set_scale_x_from_pointとget_scale_x_from_pointメソッドのインターフェイス例

`set_scale_x_from_point`メソッドは指定されたX座標を基準としてX軸の拡縮値を更新します。

同様に、`get_scale_x_from_point`メソッドでは指定されたX座標を基準としたX軸の拡縮値を取得します:

```py
# runnable
import apysc as ap

stage: ap.Stage = ap.Stage(
    background_color="#333", stage_width=200, stage_height=50, stage_elem_id="stage"
)
X: ap.Number = ap.Number(20)
direction: ap.Int = ap.Int(-1)
svg_text: ap.SVGText = ap.SVGText(
    text="Hello, world!",
    x=X,
    y=32,
    fill_color="#aaa",
)


def on_enter_frame(e: ap.EnterFrameEvent, optional: dict) -> None:
    """
    The handler to handle a timer event.

    Parameters
    ----------
    e : ap.EnterFrameEvent
        Event instance.
    optional : dict
        Optional argument dictionary.
    """
    scale: ap.Number = svg_text.get_scale_x_from_point(x=X)
    with ap.If(scale > 1):
        direction.value = -1
    with ap.If(scale <= 0.3):
        direction.value = 1
    scale += direction * 0.005
    svg_text.set_scale_x_from_point(scale_x=scale, x=X)


stage.enter_frame(handler=on_enter_frame)
ap.save_overall_html(dest_dir_path="svg_txt_scale_x_from_point/")
```

<iframe src="static/svg_txt_scale_x_from_point/index.html" width="200" height="50"></iframe>

## flip_x属性のインターフェイス例

`flip_x`属性ではインスタンスのX軸の反転状況の真偽値の更新もしくは取得を行えます:

```py
# runnable
import apysc as ap

stage: ap.Stage = ap.Stage(
    background_color="#333", stage_width=200, stage_height=50, stage_elem_id="stage"
)
svg_text: ap.SVGText = ap.SVGText(
    text="Hello, world!",
    x=20,
    y=32,
    fill_color="#aaa",
)


def on_timer(e: ap.TimerEvent, options: dict) -> None:
    """
    The handler to handle a timer event.

    Parameters
    ----------
    e : ap.TimerEvent
        Event instance.
    options : dict
        Optional argument dictionary.
    """
    svg_text.flip_x = svg_text.flip_x.not_


ap.Timer(handler=on_timer, delay=1000).start()
ap.save_overall_html(dest_dir_path="svg_txt_flip_x/")
```

<iframe src="static/svg_txt_flip_x/index.html" width="200" height="50"></iframe>

## flip_y属性のインターフェイス例

`flip_y`属性ではインスタンスのX軸の反転状況の真偽値の更新もしくは取得を行えます:

```py
# runnable
import apysc as ap

stage: ap.Stage = ap.Stage(
    background_color="#333", stage_width=200, stage_height=50, stage_elem_id="stage"
)
svg_text: ap.SVGText = ap.SVGText(
    text="Hello, world!",
    x=20,
    y=32,
    fill_color="#aaa",
)


def on_timer(e: ap.TimerEvent, options: dict) -> None:
    """
    The handler to handle a timer event.

    Parameters
    ----------
    e : ap.TimerEvent
        Event instance.
    options : dict
        Optional argument dictionary.
    """
    svg_text.flip_y = svg_text.flip_y.not_


ap.Timer(handler=on_timer, delay=1000).start()
ap.save_overall_html(dest_dir_path="svg_txt_flip_y/")
```

<iframe src="static/svg_txt_flip_y/index.html" width="200" height="50"></iframe>

## SVGText クラスのコンストラクタのAPI

<span class="inconspicuous-txt">特記事項: このAPIドキュメントはドキュメントビルド用のスクリプトによって自動で生成・同期されています。そのためもしかしたらこの節の内容は前節までの内容と重複している場合があります。</span>

**[インターフェイスの構造]** `__init__(self, *, text: Union[str, apysc._type.string.String], font_size: Union[int, apysc._type.int.Int] = 16, font_family: Union[apysc._type.array.Array[apysc._type.string.String], List[str], NoneType] = None, x: Union[float, apysc._type.number.Number] = 0.0, y: Union[float, apysc._type.number.Number] = 16.0, fill_color: Union[str, apysc._type.string.String] = '#666', fill_alpha: Union[float, apysc._type.number.Number] = 1.0, line_color: Union[str, apysc._type.string.String] = '', line_alpha: Union[float, apysc._type.number.Number] = 1.0, line_thickness: Union[int, apysc._type.int.Int] = 1, leading: Union[float, apysc._type.number.Number] = 1.5, align: apysc._display.svg_text_align_mixin.SVGTextAlign = <SVGTextAlign.LEFT: 'start'>, bold: Union[bool, apysc._type.boolean.Boolean] = False, italic: Union[bool, apysc._type.boolean.Boolean] = False, parent: Union[apysc._display.child_mixin.ChildMixIn, NoneType] = None, variable_name_suffix: str = '') -> None`<hr>

**[インターフェイス概要]**

SVGテキストのためのクラスです。<hr>

**[引数]**

- `text`: Union[str, String]
  - このクラスで使用するテキスト。

- `font_size`: Union[int, Int], optional
  - フォントサイズ設定。

- `font_family`: Optional[Union[Array[String], List[str]]], optional
  - フォントファミリー設定。配列内の各文字列には個別のフォント名を指定する必要があります（例: `Times New Roman`）。

- `x`: float or Number, optional
  - 描画を開始するX座標。

- `y`: float or Number, optional
  - 描画を開始するY座標（`特記事項`の節も確認をお願いします）。

- `fill_color`: str or String, optional
  - 塗りの色の設定。

- `fill_alpha`: float or Number, optional
  - 塗りの透明度の設定。

- `line_color`: str or String, default ''
  - 線の色の設定。

- `line_alpha`: float or Number, optional
  - 線の透明度の設定。

- `line_thickness`: int or Int, optional
  - 線幅の設定。

- `leading`: float or Number, optional
  - テキストの行間のサイズ。

- `align`: SVGTextAlign, default SVGTextAlign.LEFT
  - テキストの行揃えの設定。

- `bold`: Union[bool, Boolean], optional
  - テキストに太字のスタイル設定を行うかどうかの真偽値。

- `italic`: Union[bool, Boolean], optional
  - テキストを斜体表示のスタイル設定を行うかどうかの真偽値。

- `parent`: ChildMixIn or None, optional
  - このインスタンスを追加する親のインスタンス。もしもNoneが指定された場合、このインスタンスはステージのインスタンスへと追加されます。

- `variable_name_suffix`: str, optional
  - JavaScript上の変数のサフィックスの設定です。この設定はJavaScriptのデバッグ時に役立つことがあります。

<hr>

**[特記事項]**

 ・SVGTextの0の位置のY座標はテキストの下部からスタートします。そのため、もしy=0の座標を指定した場合テキストはほとんど見えなくなります。