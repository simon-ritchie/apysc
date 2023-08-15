<span class="inconspicuous-txt">※この翻訳ドキュメントはスクリプトによって出力・同期されています。内容が怪しそうな場合は<a href="https://github.com/simon-ritchie/apysc/issues" target="_blank">GitHubにissue</a>を追加したり[英語の原文](https://simon-ritchie.github.io/apysc/en/ellipse.html)の確認をお願いします。</span>

# Ellipse クラス

このページでは`Ellipse`クラスについて説明します。

## クラス概要

`Ellipse`クラスは楕円のベクターグラフィックスのオブジェクトを生成します。

## 基本的な使い方

`Ellipse`クラスのコンストラクタでは`x`（楕円の中央のX座標）、`y`（楕円の中央のY座標）、`width`、`height`の各引数の指定が必要です。

コンストラクタでは他の`fill_color`などのスタイル設定の各引数も受け付けます。

```py
# runnable
import apysc as ap

ap.Stage(
    background_color=ap.Color("#333"),
    stage_width=150,
    stage_height=150,
    stage_elem_id="stage",
)
ellipse: ap.Ellipse = ap.Ellipse(
    x=75,
    y=75,
    width=100,
    height=75,
    fill_color=ap.Color("#0af"),
)

ap.save_overall_html(dest_dir_path="ellipse_basic_usage/")
```

<iframe src="static/ellipse_basic_usage/index.html" width="150" height="150"></iframe>

## draw_ellipse インターフェイスについての特記事項

`draw_ellipse`を使う形でも楕円のインスタンスを生成することができます。

関連資料:

- [Graphics クラスの draw_ellipse (楕円描画) のインターフェイス](jp_graphics_draw_ellipse.md)

## x属性のインターフェイス例

`x`属性ではX座標の値の更新もしくは取得を行えます:

```py
# runnable
import apysc as ap

ap.Stage(
    background_color=ap.Color("#333"),
    stage_width=150,
    stage_height=150,
    stage_elem_id="stage",
)
ellipse: ap.Ellipse = ap.Ellipse(
    x=0,
    y=75,
    width=100,
    height=75,
    fill_color=ap.Color("#0af"),
)
ellipse.x = ap.Number(100)

ap.save_overall_html(dest_dir_path="ellipse_x/")
```

<iframe src="static/ellipse_x/index.html" width="150" height="150"></iframe>

## y属性のインターフェイス例

`y`属性ではY座標の値の更新もしくは取得を行えます:

```py
# runnable
import apysc as ap

ap.Stage(
    background_color=ap.Color("#333"),
    stage_width=150,
    stage_height=150,
    stage_elem_id="stage",
)
ellipse: ap.Ellipse = ap.Ellipse(
    x=75,
    y=0,
    width=100,
    height=50,
    fill_color=ap.Color("#0af"),
)
ellipse.y = ap.Number(125)

ap.save_overall_html(dest_dir_path="ellipse_y/")
```

<iframe src="static/ellipse_y/index.html" width="150" height="150"></iframe>

## width属性のインターフェイス例

`width`属性では幅の値の更新もしくは取得を行えます:

```py
# runnable
import apysc as ap

ap.Stage(
    background_color=ap.Color("#333"),
    stage_width=150,
    stage_height=150,
    stage_elem_id="stage",
)
ellipse: ap.Ellipse = ap.Ellipse(
    x=75,
    y=75,
    width=0,
    height=75,
    fill_color=ap.Color("#0af"),
)
ellipse.width = ap.Int(125)

ap.save_overall_html(dest_dir_path="ellipse_width/")
```

<iframe src="static/ellipse_width/index.html" width="150" height="150"></iframe>

## height属性のインターフェイス例

`height`属性では高さの値の更新もしくは取得を行えます:

```py
# runnable
import apysc as ap

ap.Stage(
    background_color=ap.Color("#333"),
    stage_width=150,
    stage_height=150,
    stage_elem_id="stage",
)
ellipse: ap.Ellipse = ap.Ellipse(
    x=75,
    y=75,
    width=75,
    height=0,
    fill_color=ap.Color("#0af"),
)
ellipse.height = ap.Int(125)

ap.save_overall_html(dest_dir_path="ellipse_height/")
```

<iframe src="static/ellipse_height/index.html" width="150" height="150"></iframe>

## fill_color属性のインターフェイス例

`fill_color`属性は塗りの色の値の更新もしくは取得を行えます:

```py
# runnable
import apysc as ap

ap.Stage(
    background_color=ap.Color("#333"),
    stage_width=150,
    stage_height=150,
    stage_elem_id="stage",
)
ellipse: ap.Ellipse = ap.Ellipse(x=75, y=75, width=100, height=75)
ellipse.fill_color = ap.Color("#f0a")

ap.save_overall_html(dest_dir_path="ellipse_fill_color/")
```

<iframe src="static/ellipse_fill_color/index.html" width="150" height="150"></iframe>

## fill_alpha属性のインターフェイス例

`fill_alpha`属性は塗りの透明度の値の更新もしくは取得を行えます:

```py
# runnable
import apysc as ap

ap.Stage(
    background_color=ap.Color("#333"),
    stage_width=150,
    stage_height=150,
    stage_elem_id="stage",
)
ellipse: ap.Ellipse = ap.Ellipse(
    x=75,
    y=75,
    width=100,
    height=75,
    fill_color=ap.Color("#0af"),
)
ellipse.fill_alpha = ap.Number(0.3)

ap.save_overall_html(dest_dir_path="ellipse_fill_alpha/")
```

<iframe src="static/ellipse_fill_alpha/index.html" width="150" height="150"></iframe>

## line_color属性のインターフェイス例

`line_color`属性では線の色の値の更新もしくは取得を行えます:

```py
# runnable
import apysc as ap

ap.Stage(
    background_color=ap.Color("#333"),
    stage_width=150,
    stage_height=150,
    stage_elem_id="stage",
)
ellipse: ap.Ellipse = ap.Ellipse(x=75, y=75, width=100, height=75, line_thickness=5)
ellipse.line_color = ap.Color("#0af")

ap.save_overall_html(dest_dir_path="ellipse_line_color/")
```

<iframe src="static/ellipse_line_color/index.html" width="150" height="150"></iframe>

## line_alpha属性のインターフェイス例

`line_alpha`属性では線の透明度の値の更新もしくは取得を行えます:

```py
# runnable
import apysc as ap

ap.Stage(
    background_color=ap.Color("#333"),
    stage_width=150,
    stage_height=150,
    stage_elem_id="stage",
)
ellipse: ap.Ellipse = ap.Ellipse(
    x=75,
    y=75,
    width=100,
    height=75,
    line_color=ap.Color("0af"),
    line_thickness=5,
)
ellipse.line_alpha = ap.Number(0.3)

ap.save_overall_html(dest_dir_path="ellipse_line_alpha/")
```

<iframe src="static/ellipse_line_alpha/index.html" width="150" height="150"></iframe>

## line_thickness属性のインターフェイス例

`line_thickness`属性では線の幅の更新もしくは取得を行えます:

```py
# runnable
import apysc as ap

ap.Stage(
    background_color=ap.Color("#333"),
    stage_width=150,
    stage_height=150,
    stage_elem_id="stage",
)
ellipse: ap.Ellipse = ap.Ellipse(
    x=75,
    y=75,
    width=100,
    height=75,
    line_color=ap.Color("0af"),
)
ellipse.line_thickness = ap.Int(8)

ap.save_overall_html(dest_dir_path="ellipse_line_thickness/")
```

<iframe src="static/ellipse_line_thickness/index.html" width="150" height="150"></iframe>

## line_dot_setting属性のインターフェイス例

`line_dot_setting`属性では点線のスタイル設定の更新もしくは取得を行えます:

```py
# runnable
import apysc as ap

ap.Stage(
    background_color=ap.Color("#333"),
    stage_width=150,
    stage_height=150,
    stage_elem_id="stage",
)
ellipse: ap.Ellipse = ap.Ellipse(
    x=75,
    y=75,
    width=100,
    height=75,
    line_color=ap.Color("0af"),
    line_thickness=2,
)
ellipse.line_dot_setting = ap.LineDotSetting(dot_size=2)

ap.save_overall_html(dest_dir_path="ellipse_line_dot_setting/")
```

<iframe src="static/ellipse_line_dot_setting/index.html" width="150" height="150"></iframe>

## line_dash_setting属性のインターフェイス例

`line_dash_setting`属性では破線のスタイル設定の更新もしくは取得を行えます:

```py
# runnable
import apysc as ap

ap.Stage(
    background_color=ap.Color("#333"),
    stage_width=150,
    stage_height=150,
    stage_elem_id="stage",
)
ellipse: ap.Ellipse = ap.Ellipse(
    x=75, y=75, width=100, height=75, line_color=ap.Color("0af"), line_thickness=2
)
ellipse.line_dash_setting = ap.LineDashSetting(dash_size=6, space_size=2)

ap.save_overall_html(dest_dir_path="ellipse_line_dash_setting/")
```

<iframe src="static/ellipse_line_dash_setting/index.html" width="150" height="150"></iframe>

## line_round_dot_setting属性のインターフェイス例

`line_round_dot_setting`属性では丸ドット線のスタイル設定の更新もしくは取得を行えます:

```py
# runnable
import apysc as ap

ap.Stage(
    background_color=ap.Color("#333"),
    stage_width=150,
    stage_height=150,
    stage_elem_id="stage",
)
ellipse: ap.Ellipse = ap.Ellipse(
    x=75,
    y=75,
    width=100,
    height=75,
    line_color=ap.Color("0af"),
)
ellipse.line_round_dot_setting = ap.LineRoundDotSetting(round_size=5, space_size=2)

ap.save_overall_html(dest_dir_path="ellipse_line_round_dot_setting/")
```

<iframe src="static/ellipse_line_round_dot_setting/index.html" width="150" height="150"></iframe>

## line_dash_dot_setting属性のインターフェイス例

`line_dash_dot_setting`属性では一点鎖線のスタイル設定の更新もしくは取得を行えます:

```py
# runnable
import apysc as ap

ap.Stage(
    background_color=ap.Color("#333"),
    stage_width=150,
    stage_height=150,
    stage_elem_id="stage",
)
ellipse: ap.Ellipse = ap.Ellipse(
    x=75,
    y=75,
    width=100,
    height=75,
    line_color=ap.Color("0af"),
    line_thickness=2,
)
ellipse.line_dash_dot_setting = ap.LineDashDotSetting(
    dot_size=3, dash_size=6, space_size=3
)

ap.save_overall_html(dest_dir_path="ellipse_line_dash_dot_setting/")
```

<iframe src="static/ellipse_line_dash_dot_setting/index.html" width="150" height="150"></iframe>

## rotation_around_center属性のインターフェイス例

`rotation_around_center`属性ではインスタンスの中央座標での回転量（0～359）の更新もしくは取得を行えます:

```py
# runnable
import apysc as ap

ap.Stage(
    background_color=ap.Color("#333"),
    stage_width=150,
    stage_height=150,
    stage_elem_id="stage",
)
ellipse: ap.Ellipse = ap.Ellipse(
    x=75,
    y=75,
    width=150,
    height=100,
    fill_color=ap.Color("#0af"),
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
    ellipse.rotation_around_center += 1


ap.Timer(on_timer, delay=ap.FPS.FPS_60).start()
ap.save_overall_html(dest_dir_path="ellipse_rotation_around_center/")
```

<iframe src="static/ellipse_rotation_around_center/index.html" width="150" height="150"></iframe>

## set_rotation_around_pointとget_rotation_around_pointメソッドのインターフェイス例

`set_rotation_around_point`メソッドは指定された座標からのインスタンスの回転量（0～359）を更新します。

同様に、`get_rotation_around_point`メソッドでは指定された座標のインスタンスの回転量（0～359）を取得します:

```py
# runnable
import apysc as ap

ap.Stage(
    background_color=ap.Color("#333"),
    stage_width=150,
    stage_height=150,
    stage_elem_id="stage",
)
ellipse: ap.Ellipse = ap.Ellipse(
    x=75,
    y=75,
    width=150,
    height=100,
    fill_color=ap.Color("#0af"),
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
    rotation: ap.Int = ellipse.get_rotation_around_point(x=x, y=y)
    rotation += 1
    ellipse.set_rotation_around_point(rotation=rotation, x=x, y=y)


ap.Timer(on_timer, delay=ap.FPS.FPS_60).start()
ap.save_overall_html(dest_dir_path="ellipse_set_rotation_around_point/")
```

<iframe src="static/ellipse_set_rotation_around_point/index.html" width="150" height="150"></iframe>

## scale_x_from_center属性のインターフェイス例

`scale_x_from_center`属性ではインスタンスの中央座標でのX軸の拡縮値の更新もしくは取得を行えます:

```py
# runnable
import apysc as ap

ap.Stage(
    background_color=ap.Color("#333"),
    stage_width=150,
    stage_height=150,
    stage_elem_id="stage",
)
ellipse: ap.Ellipse = ap.Ellipse(
    x=75,
    y=75,
    width=150,
    height=100,
    fill_color=ap.Color("#0af"),
)
direction: ap.Int = ap.Int(-1)


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
    with ap.If(ellipse.scale_x_from_center <= 0.001):
        direction.value = 1
    with ap.If(ellipse.scale_x_from_center >= 2.0):
        direction.value = -1
    ellipse.scale_x_from_center += direction * 0.005


ap.Timer(on_timer, delay=ap.FPS.FPS_60).start()
ap.save_overall_html(dest_dir_path="ellipse_scale_x_from_center/")
```

<iframe src="static/ellipse_scale_x_from_center/index.html" width="150" height="150"></iframe>

## scale_y_from_center属性のインターフェイス例

`scale_y_from_center`属性ではインスタンスの中央座標でのX軸の拡縮値の更新もしくは取得を行えます:

```py
# runnable
import apysc as ap

ap.Stage(
    background_color=ap.Color("#333"),
    stage_width=150,
    stage_height=150,
    stage_elem_id="stage",
)
ellipse: ap.Ellipse = ap.Ellipse(
    x=75,
    y=75,
    width=150,
    height=100,
    fill_color=ap.Color("#0af"),
)
direction: ap.Int = ap.Int(-1)


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
    with ap.If(ellipse.scale_y_from_center <= 0.001):
        direction.value = 1
    with ap.If(ellipse.scale_y_from_center >= 2.0):
        direction.value = -1
    ellipse.scale_y_from_center += direction * 0.005


ap.Timer(on_timer, delay=ap.FPS.FPS_60).start()
ap.save_overall_html(dest_dir_path="ellipse_scale_y_from_center/")
```

<iframe src="static/ellipse_scale_y_from_center/index.html" width="150" height="150"></iframe>

## set_scale_x_from_pointとget_scale_x_from_pointメソッドのインターフェイス例

`set_scale_x_from_point`メソッドは指定されたX座標を基準としてX軸の拡縮値を更新します。

同様に、`get_scale_x_from_point`メソッドでは指定されたX座標を基準としたX軸の拡縮値を取得します:

```py
# runnable
import apysc as ap

ap.Stage(
    background_color=ap.Color("#333"),
    stage_width=150,
    stage_height=150,
    stage_elem_id="stage",
)
ellipse: ap.Ellipse = ap.Ellipse(
    x=75,
    y=75,
    width=150,
    height=100,
    fill_color=ap.Color("#0af"),
)
direction: ap.Int = ap.Int(-1)
x: ap.Int = ap.Int(150)


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
    scale: ap.Number = ellipse.get_scale_x_from_point(x=x)
    with ap.If(scale <= 0.001):
        direction.value = 1
    with ap.If(scale >= 2.0):
        direction.value = -1
    scale += direction * 0.005
    ellipse.set_scale_x_from_point(scale_x=scale, x=x)


ap.Timer(on_timer, delay=ap.FPS.FPS_60).start()
ap.save_overall_html(dest_dir_path="ellipse_scale_x_from_point/")
```

<iframe src="static/ellipse_scale_x_from_point/index.html" width="150" height="150"></iframe>

## set_scale_y_from_pointとget_scale_y_from_pointメソッドのインターフェイス例

`set_scale_y_from_point`メソッドは指定されたY座標を基準としてY軸の拡縮値を更新します。

同様に、`get_scale_y_from_point`メソッドでは指定されたY座標を基準としたY軸の拡縮値を取得します。

```py
# runnable
import apysc as ap

ap.Stage(
    background_color=ap.Color("#333"),
    stage_width=150,
    stage_height=150,
    stage_elem_id="stage",
)
ellipse: ap.Ellipse = ap.Ellipse(
    x=75,
    y=75,
    width=150,
    height=100,
    fill_color=ap.Color("#0af"),
)
direction: ap.Int = ap.Int(-1)
y: ap.Int = ap.Int(150)


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
    scale: ap.Number = ellipse.get_scale_y_from_point(y=y)
    with ap.If(scale <= 0.001):
        direction.value = 1
    with ap.If(scale >= 2.0):
        direction.value = -1
    scale += direction * 0.005
    ellipse.set_scale_y_from_point(scale_y=scale, y=y)


ap.Timer(on_timer, delay=ap.FPS.FPS_60).start()
ap.save_overall_html(dest_dir_path="ellipse_scale_y_from_point/")
```

<iframe src="static/ellipse_scale_y_from_point/index.html" width="150" height="150"></iframe>

## flip_x属性のインターフェイス例

`flip_x`属性ではインスタンスのX軸の反転状況の真偽値の更新もしくは取得を行えます:

```py
# runnable
import apysc as ap

ap.Stage(
    background_color=ap.Color("#333"),
    stage_width=150,
    stage_height=150,
    stage_elem_id="stage",
)
ellipse: ap.Ellipse = ap.Ellipse(
    x=75,
    y=75,
    width=150,
    height=100,
    fill_color=ap.Color("#0af"),
)
ellipse.rotation_around_center = ap.Int(30)


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
    ellipse.flip_x = ellipse.flip_x.not_


ap.Timer(on_timer, delay=1000).start()
ap.save_overall_html(dest_dir_path="ellipse_flip_x/")
```

<iframe src="static/ellipse_flip_x/index.html" width="150" height="150"></iframe>

特記事項: インスタンスの形状によってはこのインターフェイスはX軸とY軸の各インターフェイスで違いが分かりづらいケースが発生します。

## flip_y属性のインターフェイス例

`flip_y`属性ではインスタンスのX軸の反転状況の真偽値の更新もしくは取得を行えます:

```py
# runnable
import apysc as ap

ap.Stage(
    background_color=ap.Color("#333"),
    stage_width=150,
    stage_height=150,
    stage_elem_id="stage",
)
ellipse: ap.Ellipse = ap.Ellipse(
    x=75,
    y=75,
    width=150,
    height=100,
    fill_color=ap.Color("#0af"),
)
ellipse.rotation_around_center = ap.Int(30)


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
    ellipse.flip_y = ellipse.flip_y.not_


ap.Timer(on_timer, delay=1000).start()
ap.save_overall_html(dest_dir_path="ellipse_flip_y/")
```

<iframe src="static/ellipse_flip_y/index.html" width="150" height="150"></iframe>

特記事項: インスタンスの形状によってはこのインターフェイスはX軸とY軸の各インターフェイスで違いが分かりづらいケースが発生します。

## skew_x属性のインターフェイス例

`skew_x`属性ではインスタンスのX軸の歪みの値の更新もしくは取得を行えます:

```py
# runnable
import apysc as ap

ap.Stage(
    background_color=ap.Color("#333"),
    stage_width=150,
    stage_height=150,
    stage_elem_id="stage",
)
ellipse: ap.Ellipse = ap.Ellipse(
    x=75,
    y=75,
    width=150,
    height=100,
    fill_color=ap.Color("#0af"),
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
    ellipse.skew_x += 1


ap.Timer(on_timer, delay=ap.FPS.FPS_60).start()
ap.save_overall_html(dest_dir_path="ellipse_skew_x/")
```

<iframe src="static/ellipse_skew_x/index.html" width="150" height="150"></iframe>

特記事項: インスタンスの形状によってはこのインターフェイスはX軸とY軸の各インターフェイスで違いが分かりづらいケースが発生します。

## skew_y属性のインターフェイス例

`skew_y`属性ではインスタンスのY軸の歪みの値の更新もしくは取得を行えます:

```py
# runnable
import apysc as ap

ap.Stage(
    background_color=ap.Color("#333"),
    stage_width=150,
    stage_height=150,
    stage_elem_id="stage",
)
ellipse: ap.Ellipse = ap.Ellipse(
    x=75,
    y=75,
    width=150,
    height=100,
    fill_color=ap.Color("#0af"),
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
    ellipse.skew_y += 1


ap.Timer(on_timer, delay=ap.FPS.FPS_60).start()
ap.save_overall_html(dest_dir_path="ellipse_skew_y/")
```

<iframe src="static/ellipse_skew_y/index.html" width="150" height="150"></iframe>

特記事項: インスタンスの形状によってはこのインターフェイスはX軸とY軸の各インターフェイスで違いが分かりづらいケースが発生します。

## Ellipse クラスのコンストラクタのAPI

<span class="inconspicuous-txt">特記事項: このAPIドキュメントはドキュメントビルド用のスクリプトによって自動で生成・同期されています。そのためもしかしたらこの節の内容は前節までの内容と重複している場合があります。</span>

**[インターフェイスの構造]** `__init__(self, *, x: Union[float, apysc._type.number.Number], y: Union[float, apysc._type.number.Number], width: Union[int, apysc._type.int.Int], height: Union[int, apysc._type.int.Int], fill_color: apysc._color.color.Color = Color(""), fill_alpha: Union[float, apysc._type.number.Number] = 1.0, line_color: apysc._color.color.Color = Color(""), line_alpha: Union[float, apysc._type.number.Number] = 1.0, line_thickness: Union[int, apysc._type.int.Int] = 1, line_cap: Union[apysc._type.string.String, apysc._display.line_caps.LineCaps, NoneType] = None, line_dot_setting: Union[apysc._display.line_dot_setting.LineDotSetting, NoneType] = None, line_dash_setting: Union[apysc._display.line_dash_setting.LineDashSetting, NoneType] = None, line_round_dot_setting: Union[apysc._display.line_round_dot_setting.LineRoundDotSetting, NoneType] = None, line_dash_dot_setting: Union[apysc._display.line_dash_dot_setting.LineDashDotSetting, NoneType] = None, parent: Union[apysc._display.child_mixin.ChildMixIn, NoneType] = None, variable_name_suffix: str = '') -> None`<hr>

**[インターフェイス概要]**

楕円のベクターグラフィックスを生成します。<hr>

**[引数]**

- `x`: float or Number
  - 楕円の中央のX座標。

- `y`: float or Number
  - 楕円の中央のY座標。

- `width`: Int or int
  - 楕円の幅。

- `height`: Int or int
  - 楕円の高さ。

- `fill_color`: Color, default COLORLESS
  - 設定する塗りの色。

- `fill_alpha`: float or Number, default 1.0
  - 設定する塗りの透明度。

- `line_color`: Color, default COLORLESS
  - 設定する線の色。

- `line_alpha`: float or Number, default 1.0
  - 設定する線の透明度。

- `line_thickness`: int or Int, default 1
  - 設定の線幅。

- `line_cap`: String or LineCaps or None, default None
  - 設定する線の端のスタイル設定。

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
>>> stage: ap.Stage = ap.Stage()
>>> ellipse: ap.Ellipse = ap.Ellipse(
...     x=100, y=100, width=100, height=50, fill_color=ap.Color("#00aaff")
... )
>>> ellipse.x
Number(100.0)

>>> ellipse.y
Number(100.0)

>>> ellipse.width
Int(100)

>>> ellipse.height
Int(50)

>>> ellipse.fill_color
Color("#00aaff")
```