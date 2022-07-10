<span class="inconspicuous-txt">※この翻訳ドキュメントはスクリプトによって出力・同期されています。内容が怪しそうな場合は<a href="https://github.com/simon-ritchie/apysc/issues" target="_blank">GitHubにissue</a>を追加したり[英語の原文](https://simon-ritchie.github.io/apysc/en/circle.html)の確認をお願いします。</span>

# Circle クラス

このページでは`Circle`クラスについて説明します。

## クラス概要

`Circle`クラスは円のベクターグラフィックスを生成します。

## 基本的な使い方

`Circle`クラスのコンストラクタでは`x`（円の中央のX座標）、`y`（円の中央のY座標）、そして半径としての`radius`引数が必要となります。

コンストラクタでは他の`fill_color`などのスタイル設定の各引数も受け付けます。

```py
# runnable
import apysc as ap

ap.Stage(
    background_color='#333',
    stage_width=150,
    stage_height=150,
    stage_elem_id='stage')
circle: ap.Circle = ap.Circle(
    x=75, y=75, radius=50, fill_color='#0af')

ap.save_overall_html(
    dest_dir_path='circle_basic_usage/')
```

<iframe src="static/circle_basic_usage/index.html" width="150" height="150"></iframe>

## draw_circle インターフェイスに対する特記事項

`draw_circle`インターフェイスを使って円を作成することもできます。

関連資料:

- [Graphics クラスの draw_circle (円の描画)のインターフェイス](jp_graphics_draw_circle.md)

## x属性のインターフェイス例

`x`属性ではX座標の値の更新もしくは取得を行えます:

```py
# runnable
import apysc as ap

ap.Stage(
    background_color='#333',
    stage_width=200,
    stage_height=150,
    stage_elem_id='stage')
circle: ap.Circle = ap.Circle(
    x=0, y=75, radius=50, fill_color='#0af')
circle.x = ap.Int(100)

ap.save_overall_html(
    dest_dir_path='circle_x/')
```

<iframe src="static/circle_x/index.html" width="200" height="150"></iframe>

## y属性のインターフェイス例

`y`属性ではY座標の値の更新もしくは取得を行えます:

```py
# runnable
import apysc as ap

ap.Stage(
    background_color='#333',
    stage_width=150,
    stage_height=200,
    stage_elem_id='stage')
circle: ap.Circle = ap.Circle(
    x=75, y=0, radius=50, fill_color='#0af')
circle.y = ap.Int(100)

ap.save_overall_html(
    dest_dir_path='circle_y/')
```

<iframe src="static/circle_y/index.html" width="150" height="200"></iframe>

## radius属性のインターフェイス例

`radius`属性では円の半径の値の更新もしくは取得を行えます:

```py
# runnable
import apysc as ap

ap.Stage(
    background_color='#333',
    stage_width=150,
    stage_height=150,
    stage_elem_id='stage')
circle: ap.Circle = ap.Circle(
    x=75, y=75, radius=0, fill_color='#0af')
circle.radius = ap.Int(30)

ap.save_overall_html(
    dest_dir_path='circle_radius/')
```

<iframe src="static/circle_radius/index.html" width="150" height="150"></iframe>

## fill_color属性のインターフェイス例

`fill_color`属性は塗りの色の値の更新もしくは取得を行えます:

```py
# runnable
import apysc as ap

ap.Stage(
    background_color='#333',
    stage_width=150,
    stage_height=150,
    stage_elem_id='stage')
circle: ap.Circle = ap.Circle(x=75, y=75, radius=50)
circle.fill_color = ap.String('#f0a')

ap.save_overall_html(
    dest_dir_path='circle_fill_color/')
```

<iframe src="static/circle_fill_color/index.html" width="150" height="150"></iframe>

## fill_alpha属性のインターフェイス例

`fill_alpha`属性は塗りの透明度の値の更新もしくは取得を行えます:

```py
# runnable
import apysc as ap

ap.Stage(
    background_color='#333',
    stage_width=150,
    stage_height=150,
    stage_elem_id='stage')
circle: ap.Circle = ap.Circle(
    x=75, y=75, radius=50, fill_color='#0af')
circle.fill_alpha = ap.Number(0.3)

ap.save_overall_html(
    dest_dir_path='circle_fill_alpha/')
```

<iframe src="static/circle_fill_alpha/index.html" width="150" height="150"></iframe>

## line_color属性のインターフェイス例

`line_color`属性では線の色の値の更新もしくは取得を行えます:

```py
# runnable
import apysc as ap

ap.Stage(
    background_color='#333',
    stage_width=150,
    stage_height=150,
    stage_elem_id='stage')
circle: ap.Circle = ap.Circle(
    x=75, y=75, radius=50, line_thickness=5)
circle.line_color = ap.String('#f0a')

ap.save_overall_html(
    dest_dir_path='circle_line_color/')
```

<iframe src="static/circle_line_color/index.html" width="150" height="150"></iframe>

## line_alpha属性のインターフェイス例

`line_alpha`属性では線の透明度の値の更新もしくは取得を行えます:

```py
# runnable
import apysc as ap

ap.Stage(
    background_color='#333',
    stage_width=150,
    stage_height=150,
    stage_elem_id='stage')
circle: ap.Circle = ap.Circle(
    x=75, y=75, radius=50, line_color='0af', line_thickness=5)
circle.line_alpha = ap.Number(0.3)

ap.save_overall_html(
    dest_dir_path='circle_line_alpha/')
```

<iframe src="static/circle_line_alpha/index.html" width="150" height="150"></iframe>

## line_thickness属性のインターフェイス例

`line_thickness`属性では線の幅の更新もしくは取得を行えます:

```py
# runnable
import apysc as ap

ap.Stage(
    background_color='#333',
    stage_width=150,
    stage_height=150,
    stage_elem_id='stage')
circle: ap.Circle = ap.Circle(
    x=75, y=75, radius=50, line_color='0af')
circle.line_thickness = ap.Int(8)

ap.save_overall_html(
    dest_dir_path='circle_line_thickness/')
```

<iframe src="static/circle_line_thickness/index.html" width="150" height="150"></iframe>

## line_dot_setting属性のインターフェイス例

`line_dot_setting`属性では点線のスタイル設定の更新もしくは取得を行えます:

```py
# runnable
import apysc as ap

ap.Stage(
    background_color='#333',
    stage_width=150,
    stage_height=150,
    stage_elem_id='stage')
circle: ap.Circle = ap.Circle(
    x=75, y=75, radius=50, line_color='0af', line_thickness=3)
circle.line_dot_setting = ap.LineDotSetting(dot_size=3)

ap.save_overall_html(
    dest_dir_path='circle_line_dot_setting/')
```

<iframe src="static/circle_line_dot_setting/index.html" width="150" height="150"></iframe>

## line_dash_setting属性のインターフェイス例

`line_dash_setting`属性では破線のスタイル設定の更新もしくは取得を行えます:

```py
# runnable
import apysc as ap

ap.Stage(
    background_color='#333',
    stage_width=150,
    stage_height=150,
    stage_elem_id='stage')
circle: ap.Circle = ap.Circle(
    x=75, y=75, radius=50, line_color='0af', line_thickness=3)
circle.line_dash_setting = ap.LineDashSetting(
    dash_size=5, space_size=2)

ap.save_overall_html(
    dest_dir_path='circle_line_dash_setting/')
```

<iframe src="static/circle_line_dash_setting/index.html" width="150" height="150"></iframe>

## line_round_dot_setting属性のインターフェイス例

`line_round_dot_setting`属性では丸ドット線のスタイル設定の更新もしくは取得を行えます:

```py
# runnable
import apysc as ap

ap.Stage(
    background_color='#333',
    stage_width=150,
    stage_height=150,
    stage_elem_id='stage')
circle: ap.Circle = ap.Circle(
    x=75, y=75, radius=50, line_color='0af')
circle.line_round_dot_setting = ap.LineRoundDotSetting(
    round_size=5, space_size=3)

ap.save_overall_html(
    dest_dir_path='circle_line_round_dot_setting/')
```

<iframe src="static/circle_line_round_dot_setting/index.html" width="150" height="150"></iframe>

## line_dash_dot_setting属性のインターフェイス例

`line_dash_dot_setting`属性では一点鎖線のスタイル設定の更新もしくは取得を行えます:

```py
# runnable
import apysc as ap

ap.Stage(
    background_color='#333',
    stage_width=150,
    stage_height=150,
    stage_elem_id='stage')
circle: ap.Circle = ap.Circle(
    x=75, y=75, radius=50, line_color='0af', line_thickness=3)
circle.line_dash_dot_setting = ap.LineDashDotSetting(
    dot_size=3, dash_size=6, space_size=3)

ap.save_overall_html(
    dest_dir_path='circle_line_dash_dot_setting/')
```

<iframe src="static/circle_line_dash_dot_setting/index.html" width="150" height="150"></iframe>

## rotation_around_center属性のインターフェイス例

`rotation_around_center`属性ではインスタンスの中央座標での回転量（0～359）の更新もしくは取得を行えます:

```py
# runnable
import apysc as ap

ap.Stage(
    background_color='#333',
    stage_width=150,
    stage_height=150,
    stage_elem_id='stage')
circle: ap.Circle = ap.Circle(
    x=75, y=75, radius=50, fill_color='#0af')
circle.scale_x_from_center = ap.Number(0.5)


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
    circle.rotation_around_center += 1


ap.Timer(on_timer, delay=ap.FPS.FPS_60).start()
ap.save_overall_html(
    dest_dir_path='circle_rotation_around_center/')
```

<iframe src="static/circle_rotation_around_center/index.html" width="150" height="150"></iframe>

## set_rotation_around_pointとget_rotation_around_pointメソッドのインターフェイス例

`set_rotation_around_point`メソッドは指定された座標からのインスタンスの回転量（0～359）を更新します。

同様に、`get_rotation_around_point`メソッドでは指定された座標のインスタンスの回転量（0～359）を取得します:

```py
# runnable
import apysc as ap

ap.Stage(
    background_color='#333',
    stage_width=150,
    stage_height=150,
    stage_elem_id='stage')
circle: ap.Circle = ap.Circle(
    x=75, y=75, radius=50, fill_color='#0af')
circle.scale_x_from_center = ap.Number(0.5)
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
    rotation: ap.Int = circle.get_rotation_around_point(
        x=x, y=y)
    rotation += 1
    circle.set_rotation_around_point(
        rotation=rotation, x=x, y=y)


ap.Timer(on_timer, delay=ap.FPS.FPS_60).start()
ap.save_overall_html(
    dest_dir_path='circle_set_rotation_around_point/')
```

<iframe src="static/circle_set_rotation_around_point/index.html" width="150" height="150"></iframe>

## flip_x属性のインターフェイス例

`flip_x`属性ではインスタンスのX軸の反転状況の真偽値の更新もしくは取得を行えます:

```py
# runnable
import apysc as ap

ap.Stage(
    background_color='#333',
    stage_width=150,
    stage_height=150,
    stage_elem_id='stage')
circle: ap.Circle = ap.Circle(
    x=75, y=75, radius=50, fill_color='#0af')
circle.scale_x_from_center = ap.Number(0.5)
circle.rotation_around_center = ap.Int(30)


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
    circle.flip_x = circle.flip_x.not_


ap.Timer(on_timer, delay=1000).start()
ap.save_overall_html(
    dest_dir_path='circle_flip_x/')
```

<iframe src="static/circle_flip_x/index.html" width="150" height="150"></iframe>

特記事項: インスタンスの形状によってはこのインターフェイスはX軸とY軸の各インターフェイスで違いが分かりづらいケースが発生します。

## flip_y属性のインターフェイス例

`flip_y`属性ではインスタンスのX軸の反転状況の真偽値の更新もしくは取得を行えます:

```py
# runnable
import apysc as ap

ap.Stage(
    background_color='#333',
    stage_width=150,
    stage_height=150,
    stage_elem_id='stage')
circle: ap.Circle = ap.Circle(
    x=75, y=75, radius=50, fill_color='#0af')
circle.scale_x_from_center = ap.Number(0.5)
circle.rotation_around_center = ap.Int(30)


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
    circle.flip_y = circle.flip_y.not_


ap.Timer(on_timer, delay=1000).start()
ap.save_overall_html(
    dest_dir_path='circle_flip_y/')
```

<iframe src="static/circle_flip_y/index.html" width="150" height="150"></iframe>

特記事項: インスタンスの形状によってはこのインターフェイスはX軸とY軸の各インターフェイスで違いが分かりづらいケースが発生します。

## skew_x属性のインターフェイス例

`skew_x`属性ではインスタンスのX軸の歪みの値の更新もしくは取得を行えます:

```py
# runnable
import apysc as ap

ap.Stage(
    background_color='#333',
    stage_width=150,
    stage_height=150,
    stage_elem_id='stage')
circle: ap.Circle = ap.Circle(
    x=75, y=75, radius=50, fill_color='#0af')


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
    circle.skew_x += 1


ap.Timer(on_timer, delay=ap.FPS.FPS_60).start()
ap.save_overall_html(
    dest_dir_path='circle_skew_x/')
```

<iframe src="static/circle_skew_x/index.html" width="150" height="150"></iframe>

特記事項: インスタンスの形状によってはこのインターフェイスはX軸とY軸の各インターフェイスで違いが分かりづらいケースが発生します。

## skew_y属性のインターフェイス例

`skew_y`属性ではインスタンスのY軸の歪みの値の更新もしくは取得を行えます:

```py
# runnable
import apysc as ap

ap.Stage(
    background_color='#333',
    stage_width=150,
    stage_height=150,
    stage_elem_id='stage')
circle: ap.Circle = ap.Circle(
    x=75, y=75, radius=50, fill_color='#0af')


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
    circle.skew_y += 1


ap.Timer(on_timer, delay=ap.FPS.FPS_60).start()
ap.save_overall_html(
    dest_dir_path='circle_skew_y/')
```

<iframe src="static/circle_skew_y/index.html" width="150" height="150"></iframe>

特記事項: インスタンスの形状によってはこのインターフェイスはX軸とY軸の各インターフェイスで違いが分かりづらいケースが発生します。

## Circle クラスのコンストラクタのAPI

<span class="inconspicuous-txt">特記事項: このAPIドキュメントはドキュメントビルド用のスクリプトによって自動で生成・同期されています。そのためもしかしたらこの節の内容は前節までの内容と重複している場合があります。</span>

**[インターフェイスの構造]** `__init__(self, *, x: Union[int, apysc._type.int.Int], y: Union[int, apysc._type.int.Int], radius: Union[int, apysc._type.int.Int], fill_color: Union[str, apysc._type.string.String] = '', fill_alpha: Union[float, apysc._type.number.Number] = 1.0, line_color: Union[str, apysc._type.string.String] = '', line_alpha: Union[float, apysc._type.number.Number] = 1.0, line_thickness: Union[int, apysc._type.int.Int] = 1, line_cap: Union[apysc._type.string.String, apysc._display.line_caps.LineCaps, NoneType] = None, line_joints: Union[apysc._type.string.String, apysc._display.line_joints.LineJoints, NoneType] = None, line_dot_setting: Union[apysc._display.line_dot_setting.LineDotSetting, NoneType] = None, line_dash_setting: Union[apysc._display.line_dash_setting.LineDashSetting, NoneType] = None, line_round_dot_setting: Union[apysc._display.line_round_dot_setting.LineRoundDotSetting, NoneType] = None, line_dash_dot_setting: Union[apysc._display.line_dash_dot_setting.LineDashDotSetting, NoneType] = None, parent: Union[apysc._display.child_interface.ChildInterface, NoneType] = None) -> None`<hr>

**[インターフェイス概要]** 円のベクターグラフィックスを生成します。<hr>

**[引数]**

- `x`: Int or int
  - 円の中心のX座標。

- `y`: Int or int
  - 円の中心のY座標。

- `radius`: Int or int
  - 円の半径。

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

<hr>

**[コードサンプル]**

```py
>>> import apysc as ap
>>> stage: ap.Stage = ap.Stage()
>>> circle: ap.Circle = ap.Circle(
...     x=100, y=100, radius=50, fill_color='#00aaff')
>>> circle.x
Int(100)

>>> circle.y
Int(100)

>>> circle.radius
Int(50)

>>> circle.fill_color
String('#00aaff')

>>> circle = ap.Circle(
...    x=100, y=100, radius=50,
...    line_color='#ffffff', line_thickness=3,
...    line_dot_setting=ap.LineDotSetting(dot_size=10))
>>> circle.line_color
String('#ffffff')

>>> circle.line_thickness
Int(3)
```