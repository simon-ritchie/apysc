<span class="inconspicuous-txt">※この翻訳ドキュメントはスクリプトによって出力・同期されています。内容が怪しそうな場合は<a href="https://github.com/simon-ritchie/apysc/issues" target="_blank">GitHubにissue</a>を追加したり[英語の原文](https://simon-ritchie.github.io/apysc/en/line.html)の確認をお願いします。</span>

# Line クラス

このページでは`Line`クラスについて説明します。

## クラス概要

`Line`クラスは直線のベクターグラフィックスを生成します。

## 基本的な使い方

`Line`クラスのコンストラクタでは`start_point`や`end_point`の引数指定を必要とします。

コンストラクタは`line_color`などのスタイル設定の引数も受け付けます。

```py
# runnable
import apysc as ap

ap.Stage(
    background_color=ap.Color("#333"),
    stage_width=200,
    stage_height=100,
    stage_elem_id="stage",
)
line: ap.Line = ap.Line(
    start_point=ap.Point2D(x=50, y=50),
    end_point=ap.Point2D(x=150, y=50),
    line_color=ap.Color("#0af"),
    line_thickness=5,
)

ap.save_overall_html(dest_dir_path="line_basic_usage/")
```

<iframe src="static/line_basic_usage/index.html" width="200" height="100"></iframe>

## draw_line や他の各インターフェイスの特記事項

`draw_line`や`draw_dotted_line`などの他のインターフェイスを使う形でも直線のインスタンスを生成することができます。

関連資料:

- [Graphics クラスの draw_line (線の描画)のインターフェイス](jp_graphics_draw_line.md)
- [Graphics クラスの draw_dotted_line (点線の描画)のインターフェイス](jp_graphics_draw_dotted_line.md)

- [Graphics クラスの draw_dashed_line (破線の描画)のインターフェイス](jp_graphics_draw_dashed_line.md)
- [Graphics クラスの draw_round_dotted_line (点線(丸)の描画)のインターフェイス](jp_graphics_draw_round_dotted_line.md)

- [Graphics クラスの draw_dash_dotted_line (一点鎖線の描画)のインターフェイス](jp_graphics_draw_dash_dotted_line.md)

## x属性のインターフェイス例

`x`属性ではX座標の値の更新もしくは取得を行えます:

```py
# runnable
import apysc as ap

ap.Stage(
    background_color=ap.Color("#333"),
    stage_width=200,
    stage_height=100,
    stage_elem_id="stage",
)
line: ap.Line = ap.Line(
    start_point=ap.Point2D(x=50, y=50),
    end_point=ap.Point2D(x=150, y=50),
    line_color=ap.Color("#0af"),
    line_thickness=5,
)
line.x = ap.Number(100)

ap.save_overall_html(dest_dir_path="line_x/")
```

<iframe src="static/line_x/index.html" width="200" height="100"></iframe>

特記事項: この属性の値は引数の座標の最小値と同値になります。

## y属性のインターフェイス例

`y`属性ではY座標の値の更新もしくは取得を行えます:

```py
# runnable
import apysc as ap

ap.Stage(
    background_color=ap.Color("#333"),
    stage_width=200,
    stage_height=100,
    stage_elem_id="stage",
)
line: ap.Line = ap.Line(
    start_point=ap.Point2D(x=50, y=50),
    end_point=ap.Point2D(x=150, y=50),
    line_color=ap.Color("#0af"),
    line_thickness=5,
)
line.y = ap.Number(80)

ap.save_overall_html(dest_dir_path="line_y/")
```

<iframe src="static/line_y/index.html" width="200" height="100"></iframe>

特記事項: この属性の値は引数の座標の最小値と同値になります。

## line_color属性のインターフェイス例

`line_color`属性では線の色の値の更新もしくは取得を行えます:

```py
# runnable
import apysc as ap

ap.Stage(
    background_color=ap.Color("#333"),
    stage_width=200,
    stage_height=100,
    stage_elem_id="stage",
)
line: ap.Line = ap.Line(
    start_point=ap.Point2D(x=50, y=50),
    end_point=ap.Point2D(x=150, y=50),
    line_thickness=5,
)
line.line_color = ap.Color("#f0a")

ap.save_overall_html(dest_dir_path="line_line_color/")
```

<iframe src="static/line_line_color/index.html" width="200" height="100"></iframe>

## line_alpha属性のインターフェイス例

`line_alpha`属性では線の透明度の値の更新もしくは取得を行えます:

```py
# runnable
import apysc as ap

ap.Stage(
    background_color=ap.Color("#333"),
    stage_width=200,
    stage_height=100,
    stage_elem_id="stage",
)
line: ap.Line = ap.Line(
    start_point=ap.Point2D(x=50, y=50),
    end_point=ap.Point2D(x=150, y=50),
    line_color=ap.Color("#0af"),
    line_thickness=5,
)
line.line_alpha = ap.Number(0.3)

ap.save_overall_html(dest_dir_path="line_line_alpha/")
```

<iframe src="static/line_line_alpha/index.html" width="200" height="100"></iframe>

## line_thickness属性のインターフェイス例

`line_thickness`属性では線の幅の更新もしくは取得を行えます:

```py
# runnable
import apysc as ap

ap.Stage(
    background_color=ap.Color("#333"),
    stage_width=200,
    stage_height=100,
    stage_elem_id="stage",
)
line: ap.Line = ap.Line(
    start_point=ap.Point2D(x=50, y=50),
    end_point=ap.Point2D(x=150, y=50),
    line_color=ap.Color("#0af"),
)
line.line_thickness = ap.Int(10)

ap.save_overall_html(dest_dir_path="line_line_thickness/")
```

<iframe src="static/line_line_thickness/index.html" width="200" height="100"></iframe>

## line_dot_setting属性のインターフェイス例

`line_dot_setting`属性では点線のスタイル設定の更新もしくは取得を行えます:

```py
# runnable
import apysc as ap

ap.Stage(
    background_color=ap.Color("#333"),
    stage_width=200,
    stage_height=100,
    stage_elem_id="stage",
)
line: ap.Line = ap.Line(
    start_point=ap.Point2D(x=50, y=50),
    end_point=ap.Point2D(x=150, y=50),
    line_color=ap.Color("#0af"),
    line_thickness=3,
)
line.line_dot_setting = ap.LineDotSetting(dot_size=3)

ap.save_overall_html(dest_dir_path="line_line_dot_setting/")
```

<iframe src="static/line_line_dot_setting/index.html" width="200" height="100"></iframe>

## line_dash_setting属性のインターフェイス例

`line_dash_setting`属性では破線のスタイル設定の更新もしくは取得を行えます:

```py
# runnable
import apysc as ap

ap.Stage(
    background_color=ap.Color("#333"),
    stage_width=200,
    stage_height=100,
    stage_elem_id="stage",
)
line: ap.Line = ap.Line(
    start_point=ap.Point2D(x=50, y=50),
    end_point=ap.Point2D(x=150, y=50),
    line_color=ap.Color("#0af"),
    line_thickness=3,
)
line.line_dash_setting = ap.LineDashSetting(dash_size=6, space_size=2)

ap.save_overall_html(dest_dir_path="line_line_dash_setting/")
```

<iframe src="static/line_line_dash_setting/index.html" width="200" height="100"></iframe>

## line_round_dot_setting属性のインターフェイス例

`line_round_dot_setting`属性では丸ドット線のスタイル設定の更新もしくは取得を行えます:

```py
# runnable
import apysc as ap

ap.Stage(
    background_color=ap.Color("#333"),
    stage_width=200,
    stage_height=100,
    stage_elem_id="stage",
)
line: ap.Line = ap.Line(
    start_point=ap.Point2D(x=50, y=50),
    end_point=ap.Point2D(x=150, y=50),
    line_color=ap.Color("#0af"),
)
line.line_round_dot_setting = ap.LineRoundDotSetting(round_size=5, space_size=3)

ap.save_overall_html(dest_dir_path="line_line_round_dot_setting/")
```

<iframe src="static/line_line_round_dot_setting/index.html" width="200" height="100"></iframe>

## line_dash_dot_setting属性のインターフェイス例

`line_dash_dot_setting`属性では一点鎖線のスタイル設定の更新もしくは取得を行えます:

```py
# runnable
import apysc as ap

ap.Stage(
    background_color=ap.Color("#333"),
    stage_width=200,
    stage_height=100,
    stage_elem_id="stage",
)
line: ap.Line = ap.Line(
    start_point=ap.Point2D(x=50, y=50),
    end_point=ap.Point2D(x=150, y=50),
    line_color=ap.Color("#0af"),
    line_thickness=3,
)
line.line_dash_dot_setting = ap.LineDashDotSetting(
    dot_size=2, dash_size=5, space_size=2
)

ap.save_overall_html(dest_dir_path="line_line_dash_dot_setting/")
```

<iframe src="static/line_line_dash_dot_setting/index.html" width="200" height="100"></iframe>

## rotation_around_center属性のインターフェイス例

`rotation_around_center`属性ではインスタンスの中央座標での回転量（0～359）の更新もしくは取得を行えます:

```py
# runnable
import apysc as ap

ap.Stage(
    background_color=ap.Color("#333"),
    stage_width=200,
    stage_height=100,
    stage_elem_id="stage",
)
line: ap.Line = ap.Line(
    start_point=ap.Point2D(x=50, y=40),
    end_point=ap.Point2D(x=150, y=60),
    line_color=ap.Color("#0af"),
    line_thickness=3,
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
    line.rotation_around_center += 1


ap.Timer(on_timer, delay=ap.FPS.FPS_60).start()
ap.save_overall_html(dest_dir_path="line_rotation_around_center/")
```

<iframe src="static/line_rotation_around_center/index.html" width="200" height="100"></iframe>

## set_rotation_around_pointとget_rotation_around_pointメソッドのインターフェイス例

`set_rotation_around_point`メソッドは指定された座標からのインスタンスの回転量（0～359）を更新します。

同様に、`get_rotation_around_point`メソッドでは指定された座標のインスタンスの回転量（0～359）を取得します:

```py
# runnable
import apysc as ap

ap.Stage(
    background_color=ap.Color("#333"),
    stage_width=200,
    stage_height=100,
    stage_elem_id="stage",
)
line: ap.Line = ap.Line(
    start_point=ap.Point2D(x=50, y=40),
    end_point=ap.Point2D(x=150, y=60),
    line_color=ap.Color("#0af"),
    line_thickness=3,
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
    rotation: ap.Int = line.get_rotation_around_point(x=x, y=y)
    rotation += 1
    line.set_rotation_around_point(rotation=rotation, x=x, y=y)


ap.Timer(on_timer, delay=ap.FPS.FPS_60).start()
ap.save_overall_html(dest_dir_path="line_set_rotation_around_point/")
```

<iframe src="static/line_set_rotation_around_point/index.html" width="200" height="100"></iframe>

## scale_x_from_center属性のインターフェイス例

`scale_x_from_center`属性ではインスタンスの中央座標でのX軸の拡縮値の更新もしくは取得を行えます:

```py
# runnable
import apysc as ap

ap.Stage(
    background_color=ap.Color("#333"),
    stage_width=200,
    stage_height=100,
    stage_elem_id="stage",
)
line: ap.Line = ap.Line(
    start_point=ap.Point2D(x=50, y=40),
    end_point=ap.Point2D(x=150, y=60),
    line_color=ap.Color("#0af"),
    line_thickness=30,
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
    with ap.If(line.scale_x_from_center <= 0.001):
        direction.value = 1
    with ap.If(line.scale_x_from_center >= 2.0):
        direction.value = -1
    line.scale_x_from_center += direction * 0.005


ap.Timer(on_timer, delay=ap.FPS.FPS_60).start()
ap.save_overall_html(dest_dir_path="line_scale_x_from_center/")
```

<iframe src="static/line_scale_x_from_center/index.html" width="200" height="100"></iframe>

## scale_y_from_center属性のインターフェイス例

`scale_y_from_center`属性ではインスタンスの中央座標でのX軸の拡縮値の更新もしくは取得を行えます:

```py
# runnable
import apysc as ap

ap.Stage(
    background_color=ap.Color("#333"),
    stage_width=200,
    stage_height=100,
    stage_elem_id="stage",
)
line: ap.Line = ap.Line(
    start_point=ap.Point2D(x=50, y=40),
    end_point=ap.Point2D(x=150, y=60),
    line_color=ap.Color("#0af"),
    line_thickness=30,
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
    with ap.If(line.scale_y_from_center <= 0.001):
        direction.value = 1
    with ap.If(line.scale_y_from_center >= 2.0):
        direction.value = -1
    line.scale_y_from_center += direction * 0.005


ap.Timer(on_timer, delay=ap.FPS.FPS_60).start()
ap.save_overall_html(dest_dir_path="line_scale_y_from_center/")
```

<iframe src="static/line_scale_y_from_center/index.html" width="200" height="100"></iframe>

## set_scale_x_from_pointとget_scale_x_from_pointメソッドのインターフェイス例

`set_scale_x_from_point`メソッドは指定されたX座標を基準としてX軸の拡縮値を更新します。

同様に、`get_scale_x_from_point`メソッドでは指定されたX座標を基準としたX軸の拡縮値を取得します:

```py
# runnable
import apysc as ap

ap.Stage(
    background_color=ap.Color("#333"),
    stage_width=200,
    stage_height=100,
    stage_elem_id="stage",
)
line: ap.Line = ap.Line(
    start_point=ap.Point2D(x=50, y=40),
    end_point=ap.Point2D(x=150, y=60),
    line_color=ap.Color("#0af"),
    line_thickness=30,
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
    scale: ap.Number = line.get_scale_x_from_point(x=x)
    with ap.If(scale <= 0.001):
        direction.value = 1
    with ap.If(scale >= 2.0):
        direction.value = -1
    scale += direction * 0.005
    line.set_scale_x_from_point(scale_x=scale, x=x)


ap.Timer(on_timer, delay=ap.FPS.FPS_60).start()
ap.save_overall_html(dest_dir_path="line_scale_x_from_point/")
```

<iframe src="static/line_scale_x_from_point/index.html" width="200" height="100"></iframe>

## set_scale_y_from_pointとget_scale_y_from_pointメソッドのインターフェイス例

`set_scale_y_from_point`メソッドは指定されたY座標を基準としてY軸の拡縮値を更新します。

同様に、`get_scale_y_from_point`メソッドでは指定されたY座標を基準としたY軸の拡縮値を取得します。

```py
# runnable
import apysc as ap

ap.Stage(
    background_color=ap.Color("#333"),
    stage_width=200,
    stage_height=100,
    stage_elem_id="stage",
)
line: ap.Line = ap.Line(
    start_point=ap.Point2D(x=50, y=40),
    end_point=ap.Point2D(x=150, y=60),
    line_color=ap.Color("#0af"),
    line_thickness=30,
)
direction: ap.Int = ap.Int(-1)
y: ap.Int = ap.Int(60)


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
    scale: ap.Number = line.get_scale_y_from_point(y=y)
    with ap.If(scale <= 0.001):
        direction.value = 1
    with ap.If(scale >= 2.0):
        direction.value = -1
    scale += direction * 0.005
    line.set_scale_y_from_point(scale_y=scale, y=y)


ap.Timer(on_timer, delay=ap.FPS.FPS_60).start()
ap.save_overall_html(dest_dir_path="line_scale_y_from_point/")
```

<iframe src="static/line_scale_y_from_point/index.html" width="200" height="100"></iframe>

## flip_x属性のインターフェイス例

`flip_x`属性ではインスタンスのX軸の反転状況の真偽値の更新もしくは取得を行えます:

```py
# runnable
import apysc as ap

ap.Stage(
    background_color=ap.Color("#333"),
    stage_width=200,
    stage_height=100,
    stage_elem_id="stage",
)
line: ap.Line = ap.Line(
    start_point=ap.Point2D(x=50, y=40),
    end_point=ap.Point2D(x=150, y=60),
    line_color=ap.Color("#0af"),
    line_thickness=3,
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
    line.flip_x = line.flip_x.not_


ap.Timer(on_timer, delay=1000).start()
ap.save_overall_html(dest_dir_path="line_flip_x/")
```

<iframe src="static/line_flip_x/index.html" width="200" height="100"></iframe>

特記事項: インスタンスの形状によってはこのインターフェイスはX軸とY軸の各インターフェイスで違いが分かりづらいケースが発生します。

## flip_y属性のインターフェイス例

`flip_y`属性ではインスタンスのX軸の反転状況の真偽値の更新もしくは取得を行えます:

```py
# runnable
import apysc as ap

ap.Stage(
    background_color=ap.Color("#333"),
    stage_width=200,
    stage_height=100,
    stage_elem_id="stage",
)
line: ap.Line = ap.Line(
    start_point=ap.Point2D(x=50, y=40),
    end_point=ap.Point2D(x=150, y=60),
    line_color=ap.Color("#0af"),
    line_thickness=3,
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
    line.flip_y = line.flip_y.not_


ap.Timer(on_timer, delay=1000).start()
ap.save_overall_html(dest_dir_path="line_flip_y/")
```

<iframe src="static/line_flip_y/index.html" width="200" height="100"></iframe>

特記事項: インスタンスの形状によってはこのインターフェイスはX軸とY軸の各インターフェイスで違いが分かりづらいケースが発生します。

## skew_x属性のインターフェイス例

`skew_x`属性ではインスタンスのX軸の歪みの値の更新もしくは取得を行えます:

```py
# runnable
import apysc as ap

ap.Stage(
    background_color=ap.Color("#333"),
    stage_width=200,
    stage_height=100,
    stage_elem_id="stage",
)
line: ap.Line = ap.Line(
    start_point=ap.Point2D(x=50, y=40),
    end_point=ap.Point2D(x=150, y=60),
    line_color=ap.Color("#0af"),
    line_thickness=3,
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
    line.skew_x += 1


ap.Timer(on_timer, delay=ap.FPS.FPS_60).start()
ap.save_overall_html(dest_dir_path="line_skew_x/")
```

<iframe src="static/line_skew_x/index.html" width="200" height="100"></iframe>

特記事項: インスタンスの形状によってはこのインターフェイスはX軸とY軸の各インターフェイスで違いが分かりづらいケースが発生します。

## skew_y属性のインターフェイス例

`skew_y`属性ではインスタンスのY軸の歪みの値の更新もしくは取得を行えます:

```py
# runnable
import apysc as ap

ap.Stage(
    background_color=ap.Color("#333"),
    stage_width=200,
    stage_height=100,
    stage_elem_id="stage",
)
line: ap.Line = ap.Line(
    start_point=ap.Point2D(x=50, y=40),
    end_point=ap.Point2D(x=150, y=60),
    line_color=ap.Color("#0af"),
    line_thickness=3,
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
    line.skew_y += 1


ap.Timer(on_timer, delay=ap.FPS.FPS_60).start()
ap.save_overall_html(dest_dir_path="line_skew_y/")
```

<iframe src="static/line_skew_y/index.html" width="200" height="100"></iframe>

特記事項: インスタンスの形状によってはこのインターフェイスはX軸とY軸の各インターフェイスで違いが分かりづらいケースが発生します。

## Line クラスのコンストラクタのAPI

<span class="inconspicuous-txt">特記事項: このAPIドキュメントはドキュメントビルド用のスクリプトによって自動で生成・同期されています。そのためもしかしたらこの節の内容は前節までの内容と重複している場合があります。</span>

**[インターフェイスの構造]** `__init__(self, *, start_point: 'point2d.Point2D', end_point: 'point2d.Point2D', line_color: apysc._color.color.Color = Color(""), line_alpha: Union[float, apysc._type.number.Number] = 1.0, line_thickness: Union[int, apysc._type.int.Int] = 1, line_cap: Union[apysc._type.string.String, apysc._display.line_caps.LineCaps, NoneType] = None, line_dot_setting: Union[apysc._display.line_dot_setting.LineDotSetting, NoneType] = None, line_dash_setting: Union[apysc._display.line_dash_setting.LineDashSetting, NoneType] = None, line_round_dot_setting: Union[apysc._display.line_round_dot_setting.LineRoundDotSetting, NoneType] = None, line_dash_dot_setting: Union[apysc._display.line_dash_dot_setting.LineDashDotSetting, NoneType] = None, parent: Union[apysc._display.child_mixin.ChildMixIn, NoneType] = None, variable_name_suffix: str = '') -> None`<hr>

**[インターフェイス概要]**

線のベクターグラフィックスを生成します。<hr>

**[引数]**

- `start_point`: Points2D
  - 線の開始座標。

- `end_point`: Points2D
  - 線の終了座標。

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

- `variable_name_suffix`: str, default ""
  - JavaScript上の変数のサフィックスの設定です。この設定はJavaScriptのデバッグ時に役立つことがあります。

<hr>

**[コードサンプル]**

```py
>>> import apysc as ap
>>> stage: ap.Stage = ap.Stage()
>>> line: ap.Line = ap.Line(
...     start_point=ap.Point2D(x=50, y=50),
...     end_point=ap.Point2D(x=150, y=50),
...     line_color=ap.Color("#ffffff"),
...     line_thickness=3,
... )
>>> line.line_color
Color("#ffffff")

>>> line.line_thickness
Int(3)
```