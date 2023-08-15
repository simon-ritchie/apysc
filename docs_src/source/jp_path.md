<span class="inconspicuous-txt">※この翻訳ドキュメントはスクリプトによって出力・同期されています。内容が怪しそうな場合は<a href="https://github.com/simon-ritchie/apysc/issues" target="_blank">GitHubにissue</a>を追加したり[英語の原文](https://simon-ritchie.github.io/apysc/en/path.html)の確認をお願いします。</span>

# Path クラス

このページでは`Path`クラスについて説明します。

## クラス概要

`Path`クラスはパスのベクターグラフィックスのオブジェクトを生成します。

## 基本的な使い方

`Path`クラスのコンストラクタは`path_data_list`引数を必要とします。

`path_data_list`引数は`PathLineTo`や`PathBezier2D`などの各パス設定を格納したリストです。

コンストラクタは`fill_color`や`line_color`などのスタイル設定用の引数も受け付けます。

```py
# runnable
import apysc as ap

ap.Stage(
    background_color=ap.Color("#333"),
    stage_width=200,
    stage_height=100,
    stage_elem_id="stage",
)
path: ap.Path = ap.Path(
    path_data_list=[
        ap.PathMoveTo(x=50, y=50),
        ap.PathLineTo(x=150, y=50),
    ],
    line_color=ap.Color("0af"),
    line_thickness=5,
)

ap.save_overall_html(dest_dir_path="path_basic_usage/")
```

<iframe src="static/path_basic_usage/index.html" width="200" height="100"></iframe>

## PathMoveTo クラス設定

`PathMoveTo`クラスはパスに新しい座標設定を追加するためのクラスです。

<iframe src="static/path_move_to_basic_usage/index.html" width="200" height="100"></iframe>

詳細は以下をご確認ください:

- [PathMoveTo クラス](jp_path_move_to.md)

## PathLineTo クラス設定

`PathLineTo`クラスは現在設定されている座標位置から新たな線のパスを描画します。

<iframe src="static/path_line_to_basic_usage/index.html" width="200" height="100"></iframe>

詳細は以下をご確認ください:

- [PathLineTo クラス](jp_path_line_to.md)

## PathHorizontal クラス設定

`PathHorizontal`クラスはパス上に水平方向の直線の描画設定を追加するためのクラスです。

<iframe src="static/path_horizontal_basic_usage/index.html" width="200" height="100"></iframe>

詳細は以下をご確認ください:

- [PathHorizontal クラス](jp_path_horizontal.md)

## PathVertical クラス設定

`PathVertical`クラスはパス上に新しい垂直の直線の設定を追加するためのクラスです。

<iframe src="static/path_vertical_basic_usage/index.html" width="100" height="200"></iframe>

詳細は以下をご確認ください:

- [PathVertical クラス](jp_path_vertical.md)

## PathClose クラス設定

`PathVertical`クラスはパス上に新しい垂直の直線の設定を追加するためのクラスです。

<iframe src="static/path_close_basic_usage/index.html" width="250" height="150"></iframe>

詳細は以下をご確認ください:

- [PathClose クラス](jp_path_close.md)

## PathBezier2D クラス設定

`PathBezier2D`クラスはパスへ2次のベジェ曲線を設定するためのクラスです。

<iframe src="static/path_bezier_2d_basic_usage_1/index.html" width="200" height="150"></iframe>

詳細は以下をご確認ください:

- [PathBezier2D クラス](jp_path_bezier_2d.md)

## PathBezier2DContinual クラス設定

PathBezier2DContinual`クラスはパスに連続した2次元のベジェ曲線を設定するためのクラスです。

<iframe src="static/path_bezier_2d_continual_basic_usage/index.html" width="400" height="200"></iframe>

詳細は以下をご確認ください:

- [PathBezier2DContinual クラス](jp_path_bezier_2d_continual.md)

## PathBezier3D クラス設定

`PathBezier3D`クラスはパス上に3次のベジェ曲線を設定するためのクラスです。

<iframe src="static/path_bezier_3d_basic_usage_1/index.html" width="250" height="270"></iframe>

詳細は以下をご確認ください:

- [PathBezier3D クラス](jp_path_bezier_3d.md)

## PathBezier3DContinual クラス設定

`PathBezier3DContinual`クラスはパス上に連続した3次ベジェ曲線を設定するためのクラスです。

<iframe src="static/path_bezier_3d_continual_basic_usage_1/index.html" width="400" height="420"></iframe>

詳細は以下をご確認ください:

- [PathBezier3DContinual クラス](jp_path_bezier_3d_continual.md)

## x属性のインターフェイス例

`x`属性ではX座標の値の更新もしくは取得を行えます:

```py
# runnable
import apysc as ap

ap.Stage(
    background_color=ap.Color("#333"),
    stage_width=150,
    stage_height=100,
    stage_elem_id="stage",
)
sprite: ap.Sprite = ap.Sprite()
path: ap.Path = ap.Path(
    path_data_list=[
        ap.PathMoveTo(x=0, y=0),
        ap.PathLineTo(x=0, y=50),
        ap.PathLineTo(x=50, y=50),
        ap.PathClose(),
    ],
    line_color=ap.Color("#0af"),
    line_thickness=5,
)
path.x = ap.Number(50)

ap.save_overall_html(dest_dir_path="path_x/")
```

<iframe src="static/path_x/index.html" width="150" height="100"></iframe>

## y属性のインターフェイス例

`y`属性ではY座標の値の更新もしくは取得を行えます:

```py
# runnable
import apysc as ap

ap.Stage(
    background_color=ap.Color("#333"),
    stage_width=100,
    stage_height=150,
    stage_elem_id="stage",
)
sprite: ap.Sprite = ap.Sprite()
path: ap.Path = ap.Path(
    path_data_list=[
        ap.PathMoveTo(x=0, y=0),
        ap.PathLineTo(x=0, y=50),
        ap.PathLineTo(x=50, y=50),
        ap.PathClose(),
    ],
    line_color=ap.Color("#0af"),
    line_thickness=5,
)
path.y = ap.Number(50)

ap.save_overall_html(dest_dir_path="path_y/")
```

<iframe src="static/path_y/index.html" width="100" height="150"></iframe>

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
sprite: ap.Sprite = ap.Sprite()
path: ap.Path = ap.Path(
    path_data_list=[
        ap.PathMoveTo(x=50, y=50),
        ap.PathLineTo(x=50, y=100),
        ap.PathLineTo(x=100, y=100),
        ap.PathClose(),
    ],
)
path.fill_color = ap.Color("#0af")

ap.save_overall_html(dest_dir_path="path_fill_color/")
```

<iframe src="static/path_fill_color/index.html" width="150" height="150"></iframe>

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
sprite: ap.Sprite = ap.Sprite()

path: ap.Path = ap.Path(
    path_data_list=[
        ap.PathMoveTo(x=50, y=50),
        ap.PathLineTo(x=50, y=100),
        ap.PathLineTo(x=100, y=100),
        ap.PathClose(),
    ],
    fill_color=ap.Color("#0af"),
)
path.fill_alpha = ap.Number(0.5)

ap.save_overall_html(dest_dir_path="path_fill_alpha/")
```

<iframe src="static/path_fill_alpha/index.html" width="150" height="150"></iframe>

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
sprite: ap.Sprite = ap.Sprite()

path: ap.Path = ap.Path(
    path_data_list=[
        ap.PathMoveTo(x=50, y=50),
        ap.PathLineTo(x=50, y=100),
        ap.PathLineTo(x=100, y=100),
        ap.PathClose(),
    ],
    line_thickness=5,
)
path.line_color = ap.Color("#0af")

ap.save_overall_html(dest_dir_path="path_line_color/")
```

<iframe src="static/path_line_color/index.html" width="150" height="150"></iframe>

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
sprite: ap.Sprite = ap.Sprite()

path: ap.Path = ap.Path(
    path_data_list=[
        ap.PathMoveTo(x=50, y=50),
        ap.PathLineTo(x=50, y=100),
        ap.PathLineTo(x=100, y=100),
        ap.PathClose(),
    ],
    line_color=ap.Color("#0af"),
    line_thickness=5,
)
path.line_alpha = ap.Number(0.5)

ap.save_overall_html(dest_dir_path="path_line_alpha/")
```

<iframe src="static/path_line_alpha/index.html" width="150" height="150"></iframe>

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
sprite: ap.Sprite = ap.Sprite()

path: ap.Path = ap.Path(
    path_data_list=[
        ap.PathMoveTo(x=50, y=50),
        ap.PathLineTo(x=50, y=100),
        ap.PathLineTo(x=100, y=100),
        ap.PathClose(),
    ],
    line_color=ap.Color("#0af"),
)
path.line_thickness = ap.Int(10)

ap.save_overall_html(dest_dir_path="path_line_thickness/")
```

<iframe src="static/path_line_thickness/index.html" width="150" height="150"></iframe>

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
sprite: ap.Sprite = ap.Sprite()

path: ap.Path = ap.Path(
    path_data_list=[
        ap.PathMoveTo(x=50, y=50),
        ap.PathLineTo(x=50, y=100),
        ap.PathLineTo(x=100, y=100),
        ap.PathClose(),
    ],
    line_color=ap.Color("#0af"),
    line_thickness=3,
)
path.line_dot_setting = ap.LineDotSetting(dot_size=3)

ap.save_overall_html(dest_dir_path="path_line_dot_setting/")
```

<iframe src="static/path_line_dot_setting/index.html" width="150" height="150"></iframe>

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
sprite: ap.Sprite = ap.Sprite()

path: ap.Path = ap.Path(
    path_data_list=[
        ap.PathMoveTo(x=50, y=50),
        ap.PathLineTo(x=50, y=100),
        ap.PathLineTo(x=100, y=100),
        ap.PathClose(),
    ],
    line_color=ap.Color("#0af"),
    line_thickness=3,
)
path.line_dash_setting = ap.LineDashSetting(dash_size=7, space_size=2)

ap.save_overall_html(dest_dir_path="path_line_dash_setting/")
```

<iframe src="static/path_line_dash_setting/index.html" width="150" height="150"></iframe>

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
sprite: ap.Sprite = ap.Sprite()

path: ap.Path = ap.Path(
    path_data_list=[
        ap.PathMoveTo(x=50, y=50),
        ap.PathLineTo(x=50, y=100),
        ap.PathLineTo(x=100, y=100),
        ap.PathClose(),
    ],
    line_color=ap.Color("#0af"),
)
path.line_round_dot_setting = ap.LineRoundDotSetting(round_size=5, space_size=4)

ap.save_overall_html(dest_dir_path="path_line_round_dot_setting/")
```

<iframe src="static/path_line_round_dot_setting/index.html" width="150" height="150"></iframe>

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
sprite: ap.Sprite = ap.Sprite()

path: ap.Path = ap.Path(
    path_data_list=[
        ap.PathMoveTo(x=50, y=50),
        ap.PathLineTo(x=50, y=100),
        ap.PathLineTo(x=100, y=100),
        ap.PathClose(),
    ],
    line_color=ap.Color("#0af"),
    line_thickness=3,
)
path.line_dash_dot_setting = ap.LineDashDotSetting(
    dot_size=3,
    dash_size=6,
    space_size=3,
)

ap.save_overall_html(dest_dir_path="path_line_dash_dot_setting/")
```

<iframe src="static/path_line_dash_dot_setting/index.html" width="150" height="150"></iframe>

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
sprite: ap.Sprite = ap.Sprite()

path: ap.Path = ap.Path(
    path_data_list=[
        ap.PathMoveTo(x=50, y=50),
        ap.PathLineTo(x=50, y=100),
        ap.PathLineTo(x=100, y=100),
        ap.PathClose(),
    ],
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
    path.rotation_around_center += 1


ap.Timer(handler=on_timer, delay=ap.FPS.FPS_60).start()
ap.save_overall_html(dest_dir_path="path_rotation_around_center/")
```

<iframe src="static/path_rotation_around_center/index.html" width="150" height="150"></iframe>

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
sprite: ap.Sprite = ap.Sprite()

path: ap.Path = ap.Path(
    path_data_list=[
        ap.PathMoveTo(x=50, y=50),
        ap.PathLineTo(x=50, y=100),
        ap.PathLineTo(x=100, y=100),
        ap.PathClose(),
    ],
    line_color=ap.Color("#0af"),
    line_thickness=3,
)
X: ap.Int = ap.Int(100)
Y: ap.Int = ap.Int(100)


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
    rotation: ap.Int = path.get_rotation_around_point(x=X, y=Y) + 1
    path.set_rotation_around_point(rotation=rotation, x=X, y=Y)


ap.Timer(handler=on_timer, delay=ap.FPS.FPS_60).start()
ap.save_overall_html(dest_dir_path="path_rotation_around_point/")
```

<iframe src="static/path_rotation_around_point/index.html" width="150" height="150"></iframe>

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
sprite: ap.Sprite = ap.Sprite()

path: ap.Path = ap.Path(
    path_data_list=[
        ap.PathMoveTo(x=50, y=50),
        ap.PathLineTo(x=50, y=100),
        ap.PathLineTo(x=100, y=100),
        ap.PathClose(),
    ],
    line_color=ap.Color("#0af"),
    line_thickness=3,
)
direction: ap.Int = ap.Int(1)


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
    scale: ap.Number = path.scale_x_from_center
    with ap.If(scale <= 0.001):
        direction.value = 1
    with ap.If(scale >= 2):
        direction.value = -1
    path.scale_x_from_center += direction * 0.01


ap.Timer(handler=on_timer, delay=ap.FPS.FPS_60).start()
ap.save_overall_html(dest_dir_path="path_scale_x_from_center/")
```

<iframe src="static/path_scale_x_from_center/index.html" width="150" height="150"></iframe>

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
sprite: ap.Sprite = ap.Sprite()

path: ap.Path = ap.Path(
    path_data_list=[
        ap.PathMoveTo(x=50, y=50),
        ap.PathLineTo(x=50, y=100),
        ap.PathLineTo(x=100, y=100),
        ap.PathClose(),
    ],
    line_color=ap.Color("#0af"),
    line_thickness=3,
)
direction: ap.Int = ap.Int(1)


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
    scale: ap.Number = path.scale_y_from_center
    with ap.If(scale <= 0.001):
        direction.value = 1
    with ap.If(scale >= 2):
        direction.value = -1
    path.scale_y_from_center += direction * 0.01


ap.Timer(handler=on_timer, delay=ap.FPS.FPS_60).start()
ap.save_overall_html(dest_dir_path="path_scale_y_from_center/")
```

<iframe src="static/path_scale_y_from_center/index.html" width="150" height="150"></iframe>

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
sprite: ap.Sprite = ap.Sprite()

path: ap.Path = ap.Path(
    path_data_list=[
        ap.PathMoveTo(x=50, y=50),
        ap.PathLineTo(x=50, y=100),
        ap.PathLineTo(x=100, y=100),
        ap.PathClose(),
    ],
    line_color=ap.Color("#0af"),
    line_thickness=3,
)
direction: ap.Int = ap.Int(1)
X: ap.Int = ap.Int(100)


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
    scale: ap.Number = path.get_scale_x_from_point(x=X)
    with ap.If(scale <= 0.001):
        direction.value = 1
    with ap.If(scale >= 2):
        direction.value = -1
    scale += direction * 0.005
    path.set_scale_x_from_point(scale_x=scale, x=X)


ap.Timer(handler=on_timer, delay=ap.FPS.FPS_60).start()
ap.save_overall_html(dest_dir_path="path_scale_x_from_point/")
```

<iframe src="static/path_scale_x_from_point/index.html" width="150" height="150"></iframe>

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
sprite: ap.Sprite = ap.Sprite()

path: ap.Path = ap.Path(
    path_data_list=[
        ap.PathMoveTo(x=50, y=50),
        ap.PathLineTo(x=50, y=100),
        ap.PathLineTo(x=100, y=100),
        ap.PathClose(),
    ],
    line_color=ap.Color("#0af"),
    line_thickness=3,
)
direction: ap.Int = ap.Int(1)
Y: ap.Int = ap.Int(100)


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
    scale: ap.Number = path.get_scale_y_from_point(y=Y)
    with ap.If(scale <= 0.001):
        direction.value = 1
    with ap.If(scale >= 2):
        direction.value = -1
    scale += direction * 0.005
    path.set_scale_y_from_point(scale_y=scale, y=Y)


ap.Timer(handler=on_timer, delay=ap.FPS.FPS_60).start()
ap.save_overall_html(dest_dir_path="path_scale_y_from_point/")
```

<iframe src="static/path_scale_y_from_point/index.html" width="150" height="150"></iframe>

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
sprite: ap.Sprite = ap.Sprite()

path: ap.Path = ap.Path(
    path_data_list=[
        ap.PathMoveTo(x=50, y=50),
        ap.PathLineTo(x=50, y=100),
        ap.PathLineTo(x=100, y=100),
        ap.PathClose(),
    ],
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
    path.flip_x = path.flip_x.not_


ap.Timer(handler=on_timer, delay=1000).start()
ap.save_overall_html(dest_dir_path="path_flip_x/")
```

<iframe src="static/path_flip_x/index.html" width="150" height="150"></iframe>

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
sprite: ap.Sprite = ap.Sprite()

path: ap.Path = ap.Path(
    path_data_list=[
        ap.PathMoveTo(x=50, y=50),
        ap.PathLineTo(x=50, y=100),
        ap.PathLineTo(x=100, y=100),
        ap.PathClose(),
    ],
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
    path.flip_y = path.flip_y.not_


ap.Timer(handler=on_timer, delay=1000).start()
ap.save_overall_html(dest_dir_path="path_flip_y/")
```

<iframe src="static/path_flip_y/index.html" width="150" height="150"></iframe>

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
sprite: ap.Sprite = ap.Sprite()

path: ap.Path = ap.Path(
    path_data_list=[
        ap.PathMoveTo(x=50, y=50),
        ap.PathLineTo(x=50, y=100),
        ap.PathLineTo(x=100, y=100),
        ap.PathClose(),
    ],
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
    path.skew_x += 1


ap.Timer(handler=on_timer, delay=ap.FPS.FPS_60).start()
ap.save_overall_html(dest_dir_path="path_skew_x/")
```

<iframe src="static/path_skew_x/index.html" width="150" height="150"></iframe>

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
sprite: ap.Sprite = ap.Sprite()

path: ap.Path = ap.Path(
    path_data_list=[
        ap.PathMoveTo(x=50, y=50),
        ap.PathLineTo(x=50, y=100),
        ap.PathLineTo(x=100, y=100),
        ap.PathClose(),
    ],
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
    path.skew_y += 1


ap.Timer(handler=on_timer, delay=ap.FPS.FPS_60).start()
ap.save_overall_html(dest_dir_path="path_skew_y/")
```

<iframe src="static/path_skew_y/index.html" width="150" height="150"></iframe>

## Path クラスのコンストラクタのAPI

<span class="inconspicuous-txt">特記事項: このAPIドキュメントはドキュメントビルド用のスクリプトによって自動で生成・同期されています。そのためもしかしたらこの節の内容は前節までの内容と重複している場合があります。</span>

**[インターフェイスの構造]** `__init__(self, *, path_data_list: List[apysc._geom.path_data_base.PathDataBase], fill_color: apysc._color.color.Color = Color(""), fill_alpha: Union[float, apysc._type.number.Number] = 1.0, line_color: apysc._color.color.Color = Color(""), line_alpha: Union[float, apysc._type.number.Number] = 1.0, line_thickness: Union[int, apysc._type.int.Int] = 1, line_cap: Union[apysc._type.string.String, apysc._display.line_caps.LineCaps, NoneType] = None, line_joints: Union[apysc._type.string.String, apysc._display.line_joints.LineJoints, NoneType] = None, line_dot_setting: Union[apysc._display.line_dot_setting.LineDotSetting, NoneType] = None, line_dash_setting: Union[apysc._display.line_dash_setting.LineDashSetting, NoneType] = None, line_round_dot_setting: Union[apysc._display.line_round_dot_setting.LineRoundDotSetting, NoneType] = None, line_dash_dot_setting: Union[apysc._display.line_dash_dot_setting.LineDashDotSetting, NoneType] = None, parent: Union[apysc._display.child_mixin.ChildMixIn, NoneType] = None, variable_name_suffix: str = '') -> None`<hr>

**[インターフェイス概要]**

パスのベクターグラフィックスを生成します。<hr>

**[引数]**

- `path_data_list`: list of PathDataBase
  - ap.PathData.MoveToなどの対象のパスデータの設定のリスト。

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
>>> stage: ap.Stage = ap.Stage()
>>> path: ap.Path = ap.Path(
...     path_data_list=[
...         ap.PathMoveTo(x=0, y=50),
...         ap.PathBezier2D(control_x=50, control_y=0, dest_x=100, dest_y=50),
...     ],
...     line_color=ap.Color("#ffffff"),
...     line_thickness=3,
... )
>>> path.line_color
Color("#ffffff")

>>> path.line_thickness
Int(3)
```

<hr>

**[関連資料]**

- [Graphics クラスの draw_path インターフェイス](https://simon-ritchie.github.io/apysc/jp/jp_graphics_draw_path.html)
- [PathMoveTo クラス](https://simon-ritchie.github.io/apysc/jp/jp_path_move_to.html)

- [PathLineTo クラス](https://simon-ritchie.github.io/apysc/jp/jp_path_line_to.html)
- [PathHorizontal クラス](https://simon-ritchie.github.io/apysc/jp/jp_path_horizontal.html)

- [PathVertical クラス](https://simon-ritchie.github.io/apysc/jp/jp_path_vertical.html)
- [PathClose クラス](https://simon-ritchie.github.io/apysc/jp/jp_path_close.html)

- [PathBezier2D クラス](https://simon-ritchie.github.io/apysc/jp/jp_path_bezier_2d.html)
- [PathBezier2DContinual クラス](https://simon-ritchie.github.io/apysc/jp/jp_path_bezier_2d_continual.html)

- [PathBezier3D クラス](https://simon-ritchie.github.io/apysc/jp/jp_path_bezier_3d.html)
- [PathBezier3DContinual クラス](https://simon-ritchie.github.io/apysc/jp/jp_path_bezier_3d_continual.html)