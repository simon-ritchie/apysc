<span class="inconspicuous-txt">※この翻訳ドキュメントはスクリプトによって出力・同期されています。内容が怪しそうな場合は<a href="https://github.com/simon-ritchie/apysc/issues" target="_blank">GitHubにissue</a>を追加したり[英語の原文](https://simon-ritchie.github.io/apysc/en/rectangle.html)の確認をお願いします。</span>

# Rectangle クラス

このページでは`Rectangle`クラスについて説明します。

## クラス概要

`Rectangle`クラスは四角のベクターグラフィックスを生成します。

## 基本的な使い方

`Rectangle`クラスのコンストラクタでは`x`、`y`、`width`、`height`の引数指定が必要になります。

コンストラクタでは他の`fill_color`などのスタイル設定の各引数も受け付けます。

```py
# runnable
import apysc as ap

ap.Stage(
    background_color="#333", stage_width=200, stage_height=150, stage_elem_id="stage"
)
rectangle: ap.Rectangle = ap.Rectangle(
    x=50, y=50, width=100, height=50, fill_color="#0af"
)

ap.save_overall_html(dest_dir_path="rectangle_basic_usage/")
```

<iframe src="static/rectangle_basic_usage/index.html" width="200" height="150"></iframe>

## draw_rect インターフェイスに対する特記事項

`draw_rect`インターフェイスを使っても四角のインスタンスを生成することができます。

関連資料:

- [Graphics クラスの draw_rect (四角の描画)のインターフェイス](jp_graphics_draw_rect.md)

## x属性のインターフェイス例

`x`属性ではX座標の値の更新もしくは取得を行えます:

```py
# runnable
import apysc as ap

ap.Stage(
    background_color="#333", stage_width=200, stage_height=150, stage_elem_id="stage"
)
rectangle: ap.Rectangle = ap.Rectangle(
    x=0, y=50, width=50, height=50, fill_color="#0af"
)
rectangle.x = ap.Int(100)

ap.save_overall_html(dest_dir_path="rectangle_x/")
```

<iframe src="static/rectangle_x/index.html" width="200" height="150"></iframe>

## y属性のインターフェイス例

`y`属性ではY座標の値の更新もしくは取得を行えます:

```py
# runnable
import apysc as ap

ap.Stage(
    background_color="#333", stage_width=150, stage_height=200, stage_elem_id="stage"
)
rectangle: ap.Rectangle = ap.Rectangle(
    x=50, y=0, width=50, height=50, fill_color="#0af"
)
rectangle.y = ap.Int(100)

ap.save_overall_html(dest_dir_path="rectangle_y/")
```

<iframe src="static/rectangle_y/index.html" width="150" height="200"></iframe>

## width属性のインターフェイス例

`width`属性では幅の値の更新もしくは取得を行えます:

```py
# runnable
import apysc as ap

ap.Stage(
    background_color="#333", stage_width=200, stage_height=150, stage_elem_id="stage"
)
rectangle: ap.Rectangle = ap.Rectangle(
    x=50, y=50, width=50, height=50, fill_color="#0af"
)
rectangle.width = ap.Int(100)

ap.save_overall_html(dest_dir_path="rectangle_width/")
```

<iframe src="static/rectangle_width/index.html" width="200" height="150"></iframe>

## height属性のインターフェイス例

`height`属性では高さの値の更新もしくは取得を行えます:

```py
# runnable
import apysc as ap

ap.Stage(
    background_color="#333", stage_width=150, stage_height=200, stage_elem_id="stage"
)
rectangle: ap.Rectangle = ap.Rectangle(
    x=50, y=50, width=50, height=50, fill_color="#0af"
)
rectangle.height = ap.Int(100)

ap.save_overall_html(dest_dir_path="rectangle_height/")
```

<iframe src="static/rectangle_height/index.html" width="150" height="200"></iframe>

## ellipse_width属性のインターフェイス例

`ellipse_width`属性では四角の角丸の幅の値の更新もしくは取得を行えます:

```py
# runnable
import apysc as ap

ap.Stage(
    background_color="#333", stage_width=150, stage_height=150, stage_elem_id="stage"
)
rectangle: ap.Rectangle = ap.Rectangle(
    x=50, y=50, width=50, height=50, fill_color="#0af"
)
rectangle.ellipse_width = ap.Int(30)
rectangle.ellipse_height = ap.Int(15)

ap.save_overall_html(dest_dir_path="rectangle_ellipse_width/")
```

<iframe src="static/rectangle_ellipse_width/index.html" width="150" height="150"></iframe>

## ellipse_height属性のインターフェイス例

`ellipse_height`属性では四角の角丸の高さの値の更新もしくは取得を行えます:

```py
# runnable
import apysc as ap

ap.Stage(
    background_color="#333", stage_width=150, stage_height=150, stage_elem_id="stage"
)
rectangle: ap.Rectangle = ap.Rectangle(
    x=50, y=50, width=50, height=50, fill_color="#0af"
)
rectangle.ellipse_width = ap.Int(15)
rectangle.ellipse_height = ap.Int(30)

ap.save_overall_html(dest_dir_path="rectangle_ellipse_height/")
```

<iframe src="static/rectangle_ellipse_height/index.html" width="150" height="150"></iframe>

## fill_color属性のインターフェイス例

`fill_color`属性は塗りの色の値の更新もしくは取得を行えます:

```py
# runnable
import apysc as ap

ap.Stage(
    background_color="#333", stage_width=150, stage_height=150, stage_elem_id="stage"
)
rectangle: ap.Rectangle = ap.Rectangle(
    x=50, y=50, width=50, height=50, fill_color="#0af"
)
rectangle.fill_color = ap.String("#f0a")

ap.save_overall_html(dest_dir_path="rectangle_fill_color/")
```

<iframe src="static/rectangle_fill_color/index.html" width="150" height="150"></iframe>

## fill_alpha属性のインターフェイス例

`fill_alpha`属性は塗りの透明度の値の更新もしくは取得を行えます:

```py
# runnable
import apysc as ap

ap.Stage(
    background_color="#333", stage_width=150, stage_height=150, stage_elem_id="stage"
)
rectangle: ap.Rectangle = ap.Rectangle(
    x=50, y=50, width=50, height=50, fill_color="#0af"
)
rectangle.fill_alpha = ap.Number(0.3)

ap.save_overall_html(dest_dir_path="rectangle_fill_alpha/")
```

<iframe src="static/rectangle_fill_alpha/index.html" width="150" height="150"></iframe>

## line_color属性のインターフェイス例

`line_color`属性では線の色の値の更新もしくは取得を行えます:

```py
# runnable
import apysc as ap

ap.Stage(
    background_color="#333", stage_width=150, stage_height=150, stage_elem_id="stage"
)
rectangle: ap.Rectangle = ap.Rectangle(
    x=50, y=50, width=50, height=50, line_thickness=5
)
rectangle.line_color = ap.String("#0af")

ap.save_overall_html(dest_dir_path="rectangle_line_color/")
```

<iframe src="static/rectangle_line_color/index.html" width="150" height="150"></iframe>

## line_alpha属性のインターフェイス例

`line_alpha`属性では線の透明度の値の更新もしくは取得を行えます:

```py
# runnable
import apysc as ap

ap.Stage(
    background_color="#333", stage_width=150, stage_height=150, stage_elem_id="stage"
)
rectangle: ap.Rectangle = ap.Rectangle(
    x=50, y=50, width=50, height=50, line_color="#0af", line_thickness=5
)
rectangle.line_alpha = ap.Number(0.3)

ap.save_overall_html(dest_dir_path="rectangle_line_alpha/")
```

<iframe src="static/rectangle_line_alpha/index.html" width="150" height="150"></iframe>

## line_thickness属性のインターフェイス例

`line_thickness`属性では線の幅の更新もしくは取得を行えます:

```py
# runnable
import apysc as ap

ap.Stage(
    background_color="#333", stage_width=150, stage_height=150, stage_elem_id="stage"
)
rectangle: ap.Rectangle = ap.Rectangle(
    x=50, y=50, width=50, height=50, line_color="#0af"
)
rectangle.line_thickness = ap.Int(10)

ap.save_overall_html(dest_dir_path="rectangle_line_thickness/")
```

<iframe src="static/rectangle_line_thickness/index.html" width="150" height="150"></iframe>

## line_dot_setting属性のインターフェイス例

`line_dot_setting`属性では点線のスタイル設定の更新もしくは取得を行えます:

```py
# runnable
import apysc as ap

ap.Stage(
    background_color="#333", stage_width=150, stage_height=150, stage_elem_id="stage"
)
rectangle: ap.Rectangle = ap.Rectangle(
    x=50, y=50, width=50, height=50, line_color="#0af", line_thickness=5
)
rectangle.line_dot_setting = ap.LineDotSetting(dot_size=3)

ap.save_overall_html(dest_dir_path="rectangle_line_dot_setting/")
```

<iframe src="static/rectangle_line_dot_setting/index.html" width="150" height="150"></iframe>

## line_dash_setting属性のインターフェイス例

`line_dash_setting`属性では破線のスタイル設定の更新もしくは取得を行えます:

```py
# runnable
import apysc as ap

ap.Stage(
    background_color="#333", stage_width=150, stage_height=150, stage_elem_id="stage"
)
rectangle: ap.Rectangle = ap.Rectangle(
    x=50, y=50, width=50, height=50, line_color="#0af", line_thickness=2
)
rectangle.line_dash_setting = ap.LineDashSetting(dash_size=7, space_size=2)

ap.save_overall_html(dest_dir_path="rectangle_line_dash_setting/")
```

<iframe src="static/rectangle_line_dash_setting/index.html" width="150" height="150"></iframe>

## line_round_dot_setting属性のインターフェイス例

`line_round_dot_setting`属性では丸ドット線のスタイル設定の更新もしくは取得を行えます:

```py
# runnable
import apysc as ap

ap.Stage(
    background_color="#333", stage_width=150, stage_height=150, stage_elem_id="stage"
)
rectangle: ap.Rectangle = ap.Rectangle(
    x=50, y=50, width=50, height=50, line_color="#0af"
)
rectangle.line_round_dot_setting = ap.LineRoundDotSetting(round_size=6, space_size=3)

ap.save_overall_html(dest_dir_path="rectangle_line_round_dot_setting/")
```

<iframe src="static/rectangle_line_round_dot_setting/index.html" width="150" height="150"></iframe>

## line_dash_dot_setting属性のインターフェイス例

`line_dash_dot_setting`属性では一点鎖線のスタイル設定の更新もしくは取得を行えます:

```py
# runnable
import apysc as ap

ap.Stage(
    background_color="#333", stage_width=150, stage_height=150, stage_elem_id="stage"
)
rectangle: ap.Rectangle = ap.Rectangle(
    x=50, y=50, width=50, height=50, line_color="#0af", line_thickness=3
)
rectangle.line_dash_dot_setting = ap.LineDashDotSetting(
    dot_size=3, dash_size=7, space_size=3
)

ap.save_overall_html(dest_dir_path="rectangle_line_dash_dot_setting/")
```

<iframe src="static/rectangle_line_dash_dot_setting/index.html" width="150" height="150"></iframe>

## rotation_around_center属性のインターフェイス例

`rotation_around_center`属性ではインスタンスの中央座標での回転量（0～359）の更新もしくは取得を行えます:

```py
# runnable
import apysc as ap

ap.Stage(
    background_color="#333", stage_width=150, stage_height=150, stage_elem_id="stage"
)
rectangle: ap.Rectangle = ap.Rectangle(
    x=50, y=50, width=50, height=50, fill_color="#0af"
)


def on_timer(e: ap.TimerEvent, options: dict) -> None:
    """
    The timer event handler.

    Parameters
    ----------
    e : ap.TimerEvent
        Event instance.
    options : dict
        Optional arguments dictionary.
    """
    rectangle.rotation_around_center += 1


ap.Timer(on_timer, delay=ap.FPS.FPS_60).start()
ap.save_overall_html(dest_dir_path="rectangle_rotation_around_center/")
```

<iframe src="static/rectangle_rotation_around_center/index.html" width="150" height="150"></iframe>

## set_rotation_around_pointとget_rotation_around_pointメソッドのインターフェイス例

`set_rotation_around_point`メソッドは指定された座標からのインスタンスの回転量（0～359）を更新します。

同様に、`get_rotation_around_point`メソッドでは指定された座標のインスタンスの回転量（0～359）を取得します:

```py
# runnable
import apysc as ap

ap.Stage(
    background_color="#333", stage_width=150, stage_height=150, stage_elem_id="stage"
)
rectangle: ap.Rectangle = ap.Rectangle(
    x=50, y=50, width=50, height=50, fill_color="#0af"
)
x: ap.Int = ap.Int(100)
y: ap.Int = ap.Int(100)


def on_timer(e: ap.TimerEvent, options: dict) -> None:
    """
    The timer event handler.

    Parameters
    ----------
    e : ap.TimerEvent
        Event instance.
    options : dict
        Optional arguments dictionary.
    """
    rotation: ap.Int = rectangle.get_rotation_around_point(x=x, y=y)
    rotation += 1
    rectangle.set_rotation_around_point(rotation=rotation, x=x, y=y)


ap.Timer(on_timer, delay=ap.FPS.FPS_60).start()
ap.save_overall_html(dest_dir_path="rectangle_set_rotation_around_point/")
```

<iframe src="static/rectangle_set_rotation_around_point/index.html" width="150" height="150"></iframe>

## flip_x属性のインターフェイス例

`flip_x`属性ではインスタンスのX軸の反転状況の真偽値の更新もしくは取得を行えます:

```py
# runnable
import apysc as ap

ap.Stage(
    background_color="#333", stage_width=150, stage_height=150, stage_elem_id="stage"
)
rectangle: ap.Rectangle = ap.Rectangle(
    x=50, y=50, width=50, height=50, fill_color="#0af"
)
rectangle.rotation_around_center = ap.Int(30)


def on_timer(e: ap.TimerEvent, options: dict) -> None:
    """
    The timer event handler.

    Parameters
    ----------
    e : ap.TimerEvent
        Event instance.
    options : dict
        Optional arguments dictionary.
    """
    rectangle.flip_x = rectangle.flip_x.not_


ap.Timer(on_timer, delay=1000).start()
ap.save_overall_html(dest_dir_path="rectangle_flip_x/")
```

<iframe src="static/rectangle_flip_x/index.html" width="150" height="150"></iframe>

特記事項: インスタンスの形状によってはこのインターフェイスはX軸とY軸の各インターフェイスで違いが分かりづらいケースが発生します。

## flip_y属性のインターフェイス例

`flip_y`属性ではインスタンスのX軸の反転状況の真偽値の更新もしくは取得を行えます:

```py
# runnable
import apysc as ap

ap.Stage(
    background_color="#333", stage_width=150, stage_height=150, stage_elem_id="stage"
)
rectangle: ap.Rectangle = ap.Rectangle(
    x=50, y=50, width=50, height=50, fill_color="#0af"
)
rectangle.rotation_around_center = ap.Int(30)


def on_timer(e: ap.TimerEvent, options: dict) -> None:
    """
    The timer event handler.

    Parameters
    ----------
    e : ap.TimerEvent
        Event instance.
    options : dict
        Optional arguments dictionary.
    """
    rectangle.flip_y = rectangle.flip_y.not_


ap.Timer(on_timer, delay=1000).start()
ap.save_overall_html(dest_dir_path="rectangle_flip_y/")
```

<iframe src="static/rectangle_flip_y/index.html" width="150" height="150"></iframe>

特記事項: インスタンスの形状によってはこのインターフェイスはX軸とY軸の各インターフェイスで違いが分かりづらいケースが発生します。

## skew_x属性のインターフェイス例

`skew_x`属性ではインスタンスのX軸の歪みの値の更新もしくは取得を行えます:

```py
# runnable
import apysc as ap

ap.Stage(
    background_color="#333", stage_width=150, stage_height=150, stage_elem_id="stage"
)
rectangle: ap.Rectangle = ap.Rectangle(
    x=50, y=50, width=50, height=50, fill_color="#0af"
)


def on_timer(e: ap.TimerEvent, options: dict) -> None:
    """
    The timer event handler.

    Parameters
    ----------
    e : ap.TimerEvent
        Event instance.
    options : dict
        Optional arguments dictionary.
    """
    rectangle.skew_x += 1


ap.Timer(on_timer, delay=ap.FPS.FPS_60).start()
ap.save_overall_html(dest_dir_path="rectangle_skew_x/")
```

<iframe src="static/rectangle_skew_x/index.html" width="150" height="150"></iframe>

## skew_y属性のインターフェイス例

`skew_y`属性ではインスタンスのY軸の歪みの値の更新もしくは取得を行えます:

```py
# runnable
import apysc as ap

ap.Stage(
    background_color="#333", stage_width=150, stage_height=150, stage_elem_id="stage"
)
rectangle: ap.Rectangle = ap.Rectangle(
    x=50, y=50, width=50, height=50, fill_color="#0af"
)


def on_timer(e: ap.TimerEvent, options: dict) -> None:
    """
    The timer event handler.

    Parameters
    ----------
    e : ap.TimerEvent
        Event instance.
    options : dict
        Optional arguments dictionary.
    """
    rectangle.skew_y += 1


ap.Timer(on_timer, delay=ap.FPS.FPS_60).start()
ap.save_overall_html(dest_dir_path="rectangle_skew_y/")
```

<iframe src="static/rectangle_skew_y/index.html" width="150" height="150"></iframe>

## Rectangle クラスのコンストラクタのAPI

<span class="inconspicuous-txt">特記事項: このAPIドキュメントはドキュメントビルド用のスクリプトによって自動で生成・同期されています。そのためもしかしたらこの節の内容は前節までの内容と重複している場合があります。</span>

**[インターフェイスの構造]** `__init__(self, *, x: Union[int, apysc._type.int.Int], y: Union[int, apysc._type.int.Int], width: Union[int, apysc._type.int.Int], height: Union[int, apysc._type.int.Int], ellipse_width: Union[int, apysc._type.int.Int] = 0, ellipse_height: Union[int, apysc._type.int.Int] = 0, fill_color: Union[str, apysc._type.string.String] = '', fill_alpha: Union[float, apysc._type.number.Number] = 1.0, line_color: Union[str, apysc._type.string.String] = '', line_alpha: Union[float, apysc._type.number.Number] = 1.0, line_thickness: Union[int, apysc._type.int.Int] = 1, line_cap: Union[apysc._type.string.String, apysc._display.line_caps.LineCaps, NoneType] = None, line_joints: Union[apysc._type.string.String, apysc._display.line_joints.LineJoints, NoneType] = None, line_dot_setting: Union[apysc._display.line_dot_setting.LineDotSetting, NoneType] = None, line_dash_setting: Union[apysc._display.line_dash_setting.LineDashSetting, NoneType] = None, line_round_dot_setting: Union[apysc._display.line_round_dot_setting.LineRoundDotSetting, NoneType] = None, line_dash_dot_setting: Union[apysc._display.line_dash_dot_setting.LineDashDotSetting, NoneType] = None, parent: Union[apysc._display.child_interface.ChildInterface, NoneType] = None, variable_name_suffix: str = '') -> None`<hr>

**[インターフェイス概要]** 四角のベクターグラフィックスを作成します。<hr>

**[引数]**

- `x`: Int or int
  - 描画を開始するX座標。

- `y`: Int or int
  - 描画を開始するY座標。

- `width`: Int or int
  - 四角の幅。

- `height`: Int or int
  - 四角の高さ。

- `ellipse_width`: int or Int
  - 楕円の幅。

- `ellipse_height`: int or Int
  - 楕円の高さ。

- `fill_color`: str or String, default ''
  - 設定する塗りの色。

- `fill_alpha`: float or Number, default 1.0
  - 設定する塗りの透明度。

- `line_color`: str or String, default ''
  - 設定する線の色。

- `line_alpha`: float or Number, default 1.0
  - 設定する線の透明度。

- `line_thickness`: int or Int, default 1
  - 設定の線幅。

- `line_cap`: String or LineCaps or None, default None
  - 設定する線の端のスタイル設定。

- `line_joints`: String or LineJoints or None, default None
  - 設定する線の連結部分のスタイル設定。

- `line_dot_setting`: LineDotSetting or None, default None
  - 設定する点線のスタイル設定。

- `line_dash_setting`: LineDashSetting or None, default None
  - 設定する破線のスタイル設定。

- `line_round_dot_setting`: LineRoundDotSetting or None, default None
  - 設定する丸ドットのスタイル設定。

- `line_dash_dot_setting`: LineDashDotSetting or None, default None
  - 設定する一点鎖線のスタイル設定。

- `parent`: ChildInterface or None, default None
  - このインスタンスを追加する親のインスタンス。もしもNoneが指定された場合、このインスタンスはステージのインスタンスへと追加されます。

- `variable_name_suffix`: str, default ''
  - JavaScript上の変数のサフィックスの設定です。この設定はJavaScriptのデバッグ時に役立つことがあります。

<hr>

**[コードサンプル]**

```py
>>> import apysc as ap
>>> stage: ap.Stage = ap.Stage()
>>> rectangle: ap.Rectangle = ap.Rectangle(
...     x=50, y=50, width=100, height=100, fill_color='#00aaff')
>>> rectangle.x
Int(50)

>>> rectangle.y
Int(50)

>>> rectangle.width
Int(100)

>>> rectangle.height
Int(100)

>>> rectangle.fill_color
String('#00aaff')
```