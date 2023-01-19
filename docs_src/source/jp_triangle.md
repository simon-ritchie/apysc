<span class="inconspicuous-txt">※この翻訳ドキュメントはスクリプトによって出力・同期されています。内容が怪しそうな場合は<a href="https://github.com/simon-ritchie/apysc/issues" target="_blank">GitHubにissue</a>を追加したり[英語の原文](https://simon-ritchie.github.io/apysc/en/triangle.html)の確認をお願いします。</span>

# Triangle クラス

このページでは`Triangle`クラスについて説明します。

## クラス概要

`Triangle`クラスは三角形のベクターグラフィックスのオブジェクトを生成します。

## 基本的な使い方

`Triangle`クラスのコンストラクタでは`x1`、`y1`、`x2`、`y2`、`x3`、`y3`の各引数の指定を必要とします。

`x1`と`y1`引数は1つ目の頂点の座標となります。

同様に、`x2`と`y2`引数は2つ目の頂点の座標となり、`x3`と`y3`は3つ目の頂点の座標となります。

コンストラクタでは他の`fill_color`などのスタイル設定の各引数も受け付けます。

```py
# runnable
import apysc as ap

ap.Stage(
    background_color="#333", stage_width=150, stage_height=150, stage_elem_id="stage"
)
triangle: ap.Triangle = ap.Triangle(
    x1=75,
    y1=50,
    x2=50,
    y2=100,
    x3=100,
    y3=100,
    fill_color="#0af",
)

ap.save_overall_html(dest_dir_path="triangle_basic_usage/")
```

<iframe src="static/triangle_basic_usage/index.html" width="150" height="150"></iframe>

## x属性のインターフェイス例

`x`属性ではX座標の値の更新もしくは取得を行えます:

```py
# runnable
import apysc as ap

ap.Stage(
    background_color="#333", stage_width=150, stage_height=150, stage_elem_id="stage"
)
triangle: ap.Triangle = ap.Triangle(
    x1=75,
    y1=50,
    x2=50,
    y2=100,
    x3=100,
    y3=100,
    fill_color="#0af",
)
triangle.x = ap.Int(100)

ap.save_overall_html(dest_dir_path="triangle_x/")
```

<iframe src="static/triangle_x/index.html" width="150" height="150"></iframe>

## y属性のインターフェイス例

`y`属性ではY座標の値の更新もしくは取得を行えます:

```py
# runnable
import apysc as ap

ap.Stage(
    background_color="#333", stage_width=150, stage_height=150, stage_elem_id="stage"
)
triangle: ap.Triangle = ap.Triangle(
    x1=75,
    y1=50,
    x2=50,
    y2=100,
    x3=100,
    y3=100,
    fill_color="#0af",
)
triangle.y = ap.Int(100)

ap.save_overall_html(dest_dir_path="triangle_y/")
```

<iframe src="static/triangle_y/index.html" width="150" height="150"></iframe>

## x1属性のインターフェイス例

`x1`属性では1つ目の頂点のX座標の更新もしくは取得を行えます:

```py
# runnable
import apysc as ap

ap.Stage(
    background_color="#333", stage_width=150, stage_height=150, stage_elem_id="stage"
)
triangle: ap.Triangle = ap.Triangle(
    x1=75,
    y1=50,
    x2=50,
    y2=100,
    x3=100,
    y3=100,
    fill_color="#0af",
)
triangle.x1 = ap.Int(100)

ap.save_overall_html(dest_dir_path="triangle_x1/")
```

<iframe src="static/triangle_x1/index.html" width="150" height="150"></iframe>

## y1属性のインターフェイス例

`y1`属性では1つ目の頂点のY座標の更新もしくは取得を行えます:

```py
# runnable
import apysc as ap

ap.Stage(
    background_color="#333", stage_width=150, stage_height=150, stage_elem_id="stage"
)
triangle: ap.Triangle = ap.Triangle(
    x1=75,
    y1=50,
    x2=50,
    y2=100,
    x3=100,
    y3=100,
    fill_color="#0af",
)
triangle.y1 = ap.Int(0)

ap.save_overall_html(dest_dir_path="triangle_y1/")
```

<iframe src="static/triangle_y1/index.html" width="150" height="150"></iframe>

## x2属性のインターフェイス例

`x2`属性では2つ目の頂点のX座標の更新もしくは取得を行えます:

```py
# runnable
import apysc as ap

ap.Stage(
    background_color="#333", stage_width=150, stage_height=150, stage_elem_id="stage"
)
triangle: ap.Triangle = ap.Triangle(
    x1=75,
    y1=50,
    x2=50,
    y2=100,
    x3=100,
    y3=100,
    fill_color="#0af",
)
triangle.x2 = ap.Int(75)

ap.save_overall_html(dest_dir_path="triangle_x2/")
```

<iframe src="static/triangle_x2/index.html" width="150" height="150"></iframe>

## y2属性のインターフェイス例

`y2`属性では2つ目の頂点のY座標の更新もしくは取得を行えます:

```py
# runnable
import apysc as ap

ap.Stage(
    background_color="#333", stage_width=150, stage_height=150, stage_elem_id="stage"
)
triangle: ap.Triangle = ap.Triangle(
    x1=75,
    y1=50,
    x2=50,
    y2=100,
    x3=100,
    y3=100,
    fill_color="#0af",
)
triangle.y2 = ap.Int(75)

ap.save_overall_html(dest_dir_path="triangle_y2/")
```

<iframe src="static/triangle_y2/index.html" width="150" height="150"></iframe>

## x3属性のインターフェイス例

`x3`属性では3つ目のX座標の更新もしくは取得を行えます:

```py
# runnable
import apysc as ap

ap.Stage(
    background_color="#333", stage_width=150, stage_height=150, stage_elem_id="stage"
)
triangle: ap.Triangle = ap.Triangle(
    x1=75,
    y1=50,
    x2=50,
    y2=100,
    x3=100,
    y3=100,
    fill_color="#0af",
)
triangle.x3 = ap.Int(75)

ap.save_overall_html(dest_dir_path="triangle_x3/")
```

<iframe src="static/triangle_x3/index.html" width="150" height="150"></iframe>

## y3属性のインターフェイス例

`y3`属性では3つ目のY座標の更新もしくは取得を行えます:

```py
# runnable
import apysc as ap

ap.Stage(
    background_color="#333", stage_width=150, stage_height=150, stage_elem_id="stage"
)
triangle: ap.Triangle = ap.Triangle(
    x1=75,
    y1=50,
    x2=50,
    y2=100,
    x3=100,
    y3=100,
    fill_color="#0af",
)
triangle.y3 = ap.Int(75)

ap.save_overall_html(dest_dir_path="triangle_y3/")
```

<iframe src="static/triangle_y3/index.html" width="150" height="150"></iframe>

## fill_color属性のインターフェイス例

`fill_color`属性は塗りの色の値の更新もしくは取得を行えます:

```py
# runnable
import apysc as ap

ap.Stage(
    background_color="#333", stage_width=150, stage_height=150, stage_elem_id="stage"
)
triangle: ap.Triangle = ap.Triangle(
    x1=75,
    y1=50,
    x2=50,
    y2=100,
    x3=100,
    y3=100,
    fill_color="#0af",
)
triangle.fill_color = ap.String("#f0a")

ap.save_overall_html(dest_dir_path="triangle_fill_color/")
```

<iframe src="static/triangle_fill_color/index.html" width="150" height="150"></iframe>

## fill_alpha属性のインターフェイス例

`fill_alpha`属性は塗りの透明度の値の更新もしくは取得を行えます:

```py
# runnable
import apysc as ap

ap.Stage(
    background_color="#333", stage_width=150, stage_height=150, stage_elem_id="stage"
)
triangle: ap.Triangle = ap.Triangle(
    x1=75,
    y1=50,
    x2=50,
    y2=100,
    x3=100,
    y3=100,
    fill_color="#0af",
)
triangle.fill_alpha = ap.Number(0.3)

ap.save_overall_html(dest_dir_path="triangle_fill_alpha/")
```

<iframe src="static/triangle_fill_alpha/index.html" width="150" height="150"></iframe>

## line_color属性のインターフェイス例

`line_color`属性では線の色の値の更新もしくは取得を行えます:

```py
# runnable
import apysc as ap

ap.Stage(
    background_color="#333", stage_width=150, stage_height=150, stage_elem_id="stage"
)
triangle: ap.Triangle = ap.Triangle(
    x1=75,
    y1=50,
    x2=50,
    y2=100,
    x3=100,
    y3=100,
    fill_color="#0af",
    line_thickness=3,
)
triangle.line_color = ap.String("#fff")

ap.save_overall_html(dest_dir_path="triangle_line_color/")
```

<iframe src="static/triangle_line_color/index.html" width="150" height="150"></iframe>

## line_alpha属性のインターフェイス例

`line_alpha`属性では線の透明度の値の更新もしくは取得を行えます:

```py
# runnable
import apysc as ap

ap.Stage(
    background_color="#333", stage_width=150, stage_height=150, stage_elem_id="stage"
)
triangle: ap.Triangle = ap.Triangle(
    x1=75,
    y1=50,
    x2=50,
    y2=100,
    x3=100,
    y3=100,
    line_color="#0af",
    line_thickness=3,
)
triangle.line_alpha = ap.Number(0.3)

ap.save_overall_html(dest_dir_path="triangle_line_alpha/")
```

<iframe src="static/triangle_line_alpha/index.html" width="150" height="150"></iframe>

## line_thickness属性のインターフェイス例

`line_thickness`属性では線の幅の更新もしくは取得を行えます:

```py
# runnable
import apysc as ap

ap.Stage(
    background_color="#333", stage_width=150, stage_height=150, stage_elem_id="stage"
)
triangle: ap.Triangle = ap.Triangle(
    x1=75,
    y1=50,
    x2=50,
    y2=100,
    x3=100,
    y3=100,
    line_color="#0af",
    line_thickness=1,
)
triangle.line_thickness = ap.Int(5)

ap.save_overall_html(dest_dir_path="triangle_line_thickness/")
```

<iframe src="static/triangle_line_thickness/index.html" width="150" height="150"></iframe>

## line_dot_setting属性のインターフェイス例

`line_dot_setting`属性では点線のスタイル設定の更新もしくは取得を行えます:

```py
# runnable
import apysc as ap

ap.Stage(
    background_color="#333", stage_width=150, stage_height=150, stage_elem_id="stage"
)
triangle: ap.Triangle = ap.Triangle(
    x1=75,
    y1=50,
    x2=50,
    y2=100,
    x3=100,
    y3=100,
    line_color="#0af",
    line_thickness=5,
)
triangle.line_dot_setting = ap.LineDotSetting(dot_size=3)

ap.save_overall_html(dest_dir_path="triangle_line_dot_setting/")
```

<iframe src="static/triangle_line_dot_setting/index.html" width="150" height="150"></iframe>

## line_dash_setting属性のインターフェイス例

`line_dash_setting`属性では破線のスタイル設定の更新もしくは取得を行えます:

```py
# runnable
import apysc as ap

ap.Stage(
    background_color="#333", stage_width=150, stage_height=150, stage_elem_id="stage"
)
triangle: ap.Triangle = ap.Triangle(
    x1=75,
    y1=50,
    x2=50,
    y2=100,
    x3=100,
    y3=100,
    line_color="#0af",
    line_thickness=5,
)
triangle.line_dash_setting = ap.LineDashSetting(dash_size=7, space_size=2)

ap.save_overall_html(dest_dir_path="triangle_line_dash_setting/")
```

<iframe src="static/triangle_line_dash_setting/index.html" width="150" height="150"></iframe>

## line_round_dot_setting属性のインターフェイス例

`line_round_dot_setting`属性では丸ドット線のスタイル設定の更新もしくは取得を行えます:

```py
# runnable
import apysc as ap

ap.Stage(
    background_color="#333", stage_width=150, stage_height=150, stage_elem_id="stage"
)
triangle: ap.Triangle = ap.Triangle(
    x1=75,
    y1=50,
    x2=50,
    y2=100,
    x3=100,
    y3=100,
    line_color="#0af",
)
triangle.line_round_dot_setting = ap.LineRoundDotSetting(round_size=6, space_size=3)

ap.save_overall_html(dest_dir_path="triangle_line_round_dot_setting/")
```

<iframe src="static/triangle_line_round_dot_setting/index.html" width="150" height="150"></iframe>

## line_dash_dot_setting属性のインターフェイス例

`line_dash_dot_setting`属性では一点鎖線のスタイル設定の更新もしくは取得を行えます:

```py
# runnable
import apysc as ap

ap.Stage(
    background_color="#333", stage_width=150, stage_height=150, stage_elem_id="stage"
)
triangle: ap.Triangle = ap.Triangle(
    x1=75,
    y1=50,
    x2=50,
    y2=100,
    x3=100,
    y3=100,
    line_color="#0af",
    line_thickness=3,
)
triangle.line_dash_dot_setting = ap.LineDashDotSetting(
    dot_size=3, dash_size=6, space_size=3
)

ap.save_overall_html(dest_dir_path="triangle_line_dash_dot_setting/")
```

<iframe src="static/triangle_line_dash_dot_setting/index.html" width="150" height="150"></iframe>

## rotation_around_center属性のインターフェイス例

`rotation_around_center`属性ではインスタンスの中央座標での回転量（0～359）の更新もしくは取得を行えます:

```py
# runnable
import apysc as ap

stage: ap.Stage = ap.Stage(
    background_color="#333", stage_width=150, stage_height=150, stage_elem_id="stage"
)
triangle: ap.Triangle = ap.Triangle(
    x1=75,
    y1=50,
    x2=50,
    y2=100,
    x3=100,
    y3=100,
    fill_color="#0af",
)


def on_enter_frame(e: ap.EnterFrameEvent[ap.Triangle], options: dict) -> None:
    """
    The enter-frame event handler.

    Parameters
    ----------
    e : ap.EnterFrameEvent[ap.Triangle]
        Event instance.
    options : dict
        Optional arguments dictionary.
    """
    triangle.rotation_around_center += 1


stage.enter_frame(handler=on_enter_frame)
ap.save_overall_html(dest_dir_path="triangle_rotation_around_center/")
```

<iframe src="static/triangle_rotation_around_center/index.html" width="150" height="150"></iframe>

## set_rotation_around_pointとget_rotation_around_pointメソッドのインターフェイス例

`set_rotation_around_point`メソッドは指定された座標からのインスタンスの回転量（0～359）を更新します。

同様に、`get_rotation_around_point`メソッドでは指定された座標のインスタンスの回転量（0～359）を取得します:

```py
# runnable
import apysc as ap

stage: ap.Stage = ap.Stage(
    background_color="#333", stage_width=150, stage_height=150, stage_elem_id="stage"
)
ROTATION_X: ap.Int = ap.Int(100)
ROTATION_Y: ap.Int = ap.Int(100)
triangle: ap.Triangle = ap.Triangle(
    x1=75,
    y1=50,
    x2=50,
    y2=100,
    x3=ROTATION_X,
    y3=ROTATION_Y,
    fill_color="#0af",
)


def on_enter_frame(e: ap.EnterFrameEvent[ap.Triangle], options: dict) -> None:
    """
    The enter-frame event handler.

    Parameters
    ----------
    e : ap.EnterFrameEvent[ap.Triangle]
        Event instance.
    options : dict
        Optional arguments dictionary.
    """
    rotation: ap.Int = triangle.get_rotation_around_point(x=ROTATION_X, y=ROTATION_Y)
    triangle.set_rotation_around_point(
        rotation=rotation + 1, x=ROTATION_X, y=ROTATION_Y
    )


stage.enter_frame(handler=on_enter_frame)
ap.save_overall_html(dest_dir_path="triangle_set_rotation_around_point/")
```

<iframe src="static/triangle_set_rotation_around_point/index.html" width="150" height="150"></iframe>

## scale_x_from_center属性のインターフェイス例

`scale_x_from_center`属性ではインスタンスの中央座標でのX軸の拡縮値の更新もしくは取得を行えます:

```py
# runnable
import apysc as ap

stage: ap.Stage = ap.Stage(
    background_color="#333", stage_width=150, stage_height=150, stage_elem_id="stage"
)
triangle: ap.Triangle = ap.Triangle(
    x1=75,
    y1=50,
    x2=50,
    y2=100,
    x3=100,
    y3=100,
    fill_color="#0af",
)
direction: ap.Int = ap.Int(1)


def on_enter_frame(e: ap.EnterFrameEvent[ap.Triangle], options: dict) -> None:
    """
    The enter-frame event handler.

    Parameters
    ----------
    e : ap.EnterFrameEvent[ap.Triangle]
        Event instance.
    options : dict
        Optional arguments dictionary.
    """
    with ap.If(triangle.scale_x_from_center <= 0.001):
        direction.value = 1
    with ap.If(triangle.scale_x_from_center >= 2.0):
        direction.value = -1
    triangle.scale_x_from_center += direction * 0.005


stage.enter_frame(handler=on_enter_frame)
ap.save_overall_html(dest_dir_path="triangle_scale_x_from_center/")
```

<iframe src="static/triangle_scale_x_from_center/index.html" width="150" height="150"></iframe>

## scale_y_from_center属性のインターフェイス例

`scale_y_from_center`属性ではインスタンスの中央座標でのX軸の拡縮値の更新もしくは取得を行えます:

```py
# runnable
import apysc as ap

stage: ap.Stage = ap.Stage(
    background_color="#333", stage_width=150, stage_height=150, stage_elem_id="stage"
)
triangle: ap.Triangle = ap.Triangle(
    x1=75,
    y1=50,
    x2=50,
    y2=100,
    x3=100,
    y3=100,
    fill_color="#0af",
)
direction: ap.Int = ap.Int(1)


def on_enter_frame(e: ap.EnterFrameEvent[ap.Triangle], options: dict) -> None:
    """
    The enter-frame event handler.

    Parameters
    ----------
    e : ap.EnterFrameEvent[ap.Triangle]
        Event instance.
    options : dict
        Optional arguments dictionary.
    """
    with ap.If(triangle.scale_y_from_center <= 0.001):
        direction.value = 1
    with ap.If(triangle.scale_y_from_center >= 2.0):
        direction.value = -1
    triangle.scale_y_from_center += direction * 0.005


stage.enter_frame(handler=on_enter_frame)
ap.save_overall_html(dest_dir_path="triangle_scale_y_from_center/")
```

<iframe src="static/triangle_scale_y_from_center/index.html" width="150" height="150"></iframe>

## set_scale_x_from_pointとget_scale_x_from_pointメソッドのインターフェイス例

```py
# runnable
import apysc as ap

stage: ap.Stage = ap.Stage(
    background_color="#333", stage_width=150, stage_height=150, stage_elem_id="stage"
)
SCALE_COORDINATE_X: ap.Int = ap.Int(100)
triangle: ap.Triangle = ap.Triangle(
    x1=75,
    y1=50,
    x2=50,
    y2=100,
    x3=SCALE_COORDINATE_X,
    y3=100,
    fill_color="#0af",
)
direction: ap.Int = ap.Int(1)


def on_enter_frame(e: ap.EnterFrameEvent[ap.Triangle], options: dict) -> None:
    """
    The enter-frame event handler.

    Parameters
    ----------
    e : ap.EnterFrameEvent[ap.Triangle]
        Event instance.
    options : dict
        Optional arguments dictionary.
    """
    scale: ap.Number = triangle.get_scale_x_from_point(x=SCALE_COORDINATE_X)
    scale += direction * 0.005
    with ap.If(scale <= 0.001):
        direction.value = 1
    with ap.If(scale >= 2.0):
        direction.value = -1
    triangle.set_scale_x_from_point(scale_x=scale, x=SCALE_COORDINATE_X)


stage.enter_frame(handler=on_enter_frame)
ap.save_overall_html(dest_dir_path="triangle_set_scale_x_from_point/")
```

<iframe src="static/triangle_set_scale_x_from_point/index.html" width="150" height="150"></iframe>

## set_scale_y_from_pointとget_scale_y_from_pointメソッドのインターフェイス例

`set_scale_y_from_point`メソッドは指定されたY座標を基準としてY軸の拡縮値を更新します。

同様に、`get_scale_y_from_point`メソッドでは指定されたY座標を基準としたY軸の拡縮値を取得します。

```py
# runnable
import apysc as ap

stage: ap.Stage = ap.Stage(
    background_color="#333", stage_width=150, stage_height=150, stage_elem_id="stage"
)
SCALE_COORDINATE_Y: ap.Int = ap.Int(100)
triangle: ap.Triangle = ap.Triangle(
    x1=75,
    y1=50,
    x2=50,
    y2=100,
    x3=100,
    y3=SCALE_COORDINATE_Y,
    fill_color="#0af",
)
direction: ap.Int = ap.Int(1)


def on_enter_frame(e: ap.EnterFrameEvent[ap.Triangle], options: dict) -> None:
    """
    The enter-frame event handler.

    Parameters
    ----------
    e : ap.EnterFrameEvent[ap.Triangle]
        Event instance.
    options : dict
        Optional arguments dictionary.
    """
    scale: ap.Number = triangle.get_scale_y_from_point(y=SCALE_COORDINATE_Y)
    scale += direction * 0.005
    with ap.If(scale <= 0.001):
        direction.value = 1
    with ap.If(scale >= 2.0):
        direction.value = -1
    triangle.set_scale_y_from_point(scale_y=scale, y=SCALE_COORDINATE_Y)


stage.enter_frame(handler=on_enter_frame)
ap.save_overall_html(dest_dir_path="triangle_set_scale_y_from_point/")
```

<iframe src="static/triangle_set_scale_y_from_point/index.html" width="150" height="150"></iframe>

## flip_x属性のインターフェイス例

`flip_x`属性ではインスタンスのX軸の反転状況の真偽値の更新もしくは取得を行えます:

```py
# runnable
import apysc as ap

ap.Stage(
    background_color="#333", stage_width=150, stage_height=150, stage_elem_id="stage"
)
triangle: ap.Triangle = ap.Triangle(
    x1=50,
    y1=50,
    x2=50,
    y2=100,
    x3=100,
    y3=100,
    fill_color="#0af",
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
    triangle.flip_x = triangle.flip_x.not_


ap.Timer(handler=on_timer, delay=1000).start()
ap.save_overall_html(dest_dir_path="triangle_flip_x/")
```

<iframe src="static/triangle_flip_x/index.html" width="150" height="150"></iframe>

## flip_y属性のインターフェイス例

`flip_y`属性ではインスタンスのX軸の反転状況の真偽値の更新もしくは取得を行えます:

```py
# runnable
import apysc as ap

ap.Stage(
    background_color="#333", stage_width=150, stage_height=150, stage_elem_id="stage"
)
triangle: ap.Triangle = ap.Triangle(
    x1=75,
    y1=50,
    x2=50,
    y2=100,
    x3=100,
    y3=100,
    fill_color="#0af",
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
    triangle.flip_y = triangle.flip_y.not_


ap.Timer(handler=on_timer, delay=1000).start()
ap.save_overall_html(dest_dir_path="triangle_flip_y/")
```

<iframe src="static/triangle_flip_y/index.html" width="150" height="150"></iframe>

## skew_x属性のインターフェイス例

`skew_x`属性ではインスタンスのX軸の歪みの値の更新もしくは取得を行えます:

```py
# runnable
import apysc as ap

stage: ap.Stage = ap.Stage(
    background_color="#333", stage_width=150, stage_height=150, stage_elem_id="stage"
)
triangle: ap.Triangle = ap.Triangle(
    x1=75,
    y1=50,
    x2=50,
    y2=100,
    x3=100,
    y3=100,
    fill_color="#0af",
)


def on_enter_frame(e: ap.EnterFrameEvent[ap.Triangle], options: dict) -> None:
    """
    The enter-frame event handler.

    Parameters
    ----------
    e : ap.EnterFrameEvent[ap.Triangle]
        Event instance.
    options : dict
        Optional arguments dictionary.
    """
    triangle.skew_x += 1


stage.enter_frame(handler=on_enter_frame)
ap.save_overall_html(dest_dir_path="triangle_skew_x/")
```

<iframe src="static/triangle_skew_x/index.html" width="150" height="150"></iframe>

## skew_y属性のインターフェイス例

`skew_y`属性ではインスタンスのY軸の歪みの値の更新もしくは取得を行えます:

```py
# runnable
import apysc as ap

stage: ap.Stage = ap.Stage(
    background_color="#333", stage_width=150, stage_height=150, stage_elem_id="stage"
)
triangle: ap.Triangle = ap.Triangle(
    x1=75,
    y1=50,
    x2=50,
    y2=100,
    x3=100,
    y3=100,
    fill_color="#0af",
)


def on_enter_frame(e: ap.EnterFrameEvent[ap.Triangle], options: dict) -> None:
    """
    The enter-frame event handler.

    Parameters
    ----------
    e : ap.EnterFrameEvent[ap.Triangle]
        Event instance.
    options : dict
        Optional arguments dictionary.
    """
    triangle.skew_y += 1


stage.enter_frame(handler=on_enter_frame)
ap.save_overall_html(dest_dir_path="triangle_skew_y/")
```

<iframe src="static/triangle_skew_y/index.html" width="150" height="150"></iframe>

## Triangle クラスのコンストラクタのAPI

<span class="inconspicuous-txt">特記事項: このAPIドキュメントはドキュメントビルド用のスクリプトによって自動で生成・同期されています。そのためもしかしたらこの節の内容は前節までの内容と重複している場合があります。</span>

**[インターフェイスの構造]** `__init__(self, *, x1: Union[int, apysc._type.int.Int], y1: Union[int, apysc._type.int.Int], x2: Union[int, apysc._type.int.Int], y2: Union[int, apysc._type.int.Int], x3: Union[int, apysc._type.int.Int], y3: Union[int, apysc._type.int.Int], fill_color: Union[str, apysc._type.string.String] = '', fill_alpha: Union[float, apysc._type.number.Number] = 1.0, line_color: Union[str, apysc._type.string.String] = '', line_alpha: Union[float, apysc._type.number.Number] = 1.0, line_thickness: Union[int, apysc._type.int.Int] = 1, line_cap: Union[apysc._type.string.String, apysc._display.line_caps.LineCaps, NoneType] = None, line_joints: Union[apysc._type.string.String, apysc._display.line_joints.LineJoints, NoneType] = None, line_dot_setting: Union[apysc._display.line_dot_setting.LineDotSetting, NoneType] = None, line_dash_setting: Union[apysc._display.line_dash_setting.LineDashSetting, NoneType] = None, line_round_dot_setting: Union[apysc._display.line_round_dot_setting.LineRoundDotSetting, NoneType] = None, line_dash_dot_setting: Union[apysc._display.line_dash_dot_setting.LineDashDotSetting, NoneType] = None, parent: Union[apysc._display.child_mixin.ChildMixIn, NoneType] = None, variable_name_suffix: str = '') -> None`<hr>

**[インターフェイス概要]**

三角形のベクターグラフィックスのインスタンスを生成します。<hr>

**[引数]**

- `x1`: Union[int, Int]
  - 1つ目の頂点のX座標。

- `y1`: Union[int, Int]
  - 1つ目の頂点のY座標。

- `x2`: Union[int, Int]
  - 2つ目の頂点のX座標。

- `y2`: Union[int, Int]
  - 2つ目の頂点のY座標。

- `x3`: Union[int, Int]
  - 3つ目の頂点のX座標。

- `y3`: Union[int, Int]
  - 3つ目の頂点のY座標。

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

- `parent`: ChildMixIn or None, default None
  - このインスタンスを追加する親のインスタンス。もしもNoneが指定された場合、このインスタンスはステージのインスタンスへと追加されます。

- `variable_name_suffix`: str, default ''
  - JavaScript上の変数のサフィックスの設定です。この設定はJavaScriptのデバッグ時に役立つことがあります。

<hr>

**[コードサンプル]**

```py
>>> import apysc as ap
>>> _ = ap.Stage()
>>> triangle: ap.Triangle = ap.Triangle(
...     x1=75,
...     y1=50,
...     x2=50,
...     y2=100,
...     x3=100,
...     y3=100,
...     fill_color="#0af",
...     line_color="#fff",
...     line_thickness=3,
... )
>>> triangle.x2
Int(50)

>>> triangle.y1 = ap.Int(30)
>>> triangle.y1
Int(30)
```

## x1 属性のAPI

<span class="inconspicuous-txt">特記事項: このAPIドキュメントはドキュメントビルド用のスクリプトによって自動で生成・同期されています。そのためもしかしたらこの節の内容は前節までの内容と重複している場合があります。</span>

**[インターフェイス概要]**

1つ目のX座標を取得します。<hr>

**[返却値]**

- `x1`: Int
  - 1つ目のX座標。

## y1 属性のAPI

<span class="inconspicuous-txt">特記事項: このAPIドキュメントはドキュメントビルド用のスクリプトによって自動で生成・同期されています。そのためもしかしたらこの節の内容は前節までの内容と重複している場合があります。</span>

**[インターフェイス概要]**

1つ目のY座標を取得します。<hr>

**[返却値]**

- `y1`: Int
  - 1つ目のY座標。

## x2 属性のAPI

<span class="inconspicuous-txt">特記事項: このAPIドキュメントはドキュメントビルド用のスクリプトによって自動で生成・同期されています。そのためもしかしたらこの節の内容は前節までの内容と重複している場合があります。</span>

**[インターフェイス概要]**

Get a second x-coordinate.<hr>

**[返却値]**

- `x2`: Int
  - 2つ目のX座標。

## y2 属性のAPI

<span class="inconspicuous-txt">特記事項: このAPIドキュメントはドキュメントビルド用のスクリプトによって自動で生成・同期されています。そのためもしかしたらこの節の内容は前節までの内容と重複している場合があります。</span>

**[インターフェイス概要]**

2つ目のY座標を取得します。<hr>

**[返却値]**

- `y2`: Int
  - 2つ目のY座標。

## x3 属性のAPI

<span class="inconspicuous-txt">特記事項: このAPIドキュメントはドキュメントビルド用のスクリプトによって自動で生成・同期されています。そのためもしかしたらこの節の内容は前節までの内容と重複している場合があります。</span>

**[インターフェイス概要]**

3つ目のX座標を取得します。<hr>

**[返却値]**

- `x3`: Int
  - 3つ目のX座標。

## y3 属性のAPI

<span class="inconspicuous-txt">特記事項: このAPIドキュメントはドキュメントビルド用のスクリプトによって自動で生成・同期されています。そのためもしかしたらこの節の内容は前節までの内容と重複している場合があります。</span>

**[インターフェイス概要]**

3つ目のY座標を取得します。<hr>

**[返却値]**

- `y3`: Int
  - 3つ目のY座標。