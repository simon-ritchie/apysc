<span class="inconspicuous-txt">※この翻訳ドキュメントはスクリプトによって出力・同期されています。内容が怪しそうな場合は<a href="https://github.com/simon-ritchie/apysc/issues" target="_blank">GitHubにissue</a>を追加したり[英語の原文](https://simon-ritchie.github.io/apysc/en/display_object_and_graphics_base_prop_abstract.html)の確認をお願いします。</span>

# DisplayObject と GraphicsBase クラスの基本的な属性の概要

このページでは`DisplayObject`や`GraphicsBase`の各サブクラスのxやvisibleなどの基本的な属性の概要について説明します。

## それらの属性でapyscができること

- xやy, visibleなどの属性の取得や更新を行うことができます。

## x と y 属性

xとy属性ではXとY座標を更新・取得することができます。

<details>
<summary>コードブロックを表示:</summary>

```py
# runnable
from typing_extensions import TypedDict

import apysc as ap


class RectOptions(TypedDict):
    rectangle: ap.Rectangle
    direction: ap.Int


def on_timer(e: ap.TimerEvent, options: RectOptions) -> None:
    """
    The handler that the timer calls.

    Parameters
    ----------
    e : ap.TimerEvent
        Event instance.
    options : RectOptions
        Optional arguments dictionary.
    """
    rectangle: ap.Rectangle = options['rectangle']
    direction: ap.Int = options['direction']
    rectangle.x += direction
    rectangle.y += direction

    with ap.If(rectangle.x >= 100):
        direction.value = -1
        ap.Return()

    with ap.If(rectangle.x <= 50):
        direction.value = 1
        ap.Return()


ap.Stage(
    background_color='#333',
    stage_width=200,
    stage_height=200,
    stage_elem_id='stage')
sprite: ap.Sprite = ap.Sprite()
sprite.graphics.begin_fill(color='#0af')
rectangle: ap.Rectangle = sprite.graphics.draw_rect(
    x=50, y=50, width=50, height=50)

direction: ap.Int = ap.Int(1)
options: RectOptions = {'rectangle': rectangle, 'direction': direction}
ap.Timer(on_timer, delay=ap.FPS.FPS_60, options=options).start()

ap.save_overall_html(
    dest_dir_path='do_and_graphics_base_prop_abstract_x_and_y/')
```

</details>

<iframe src="static/do_and_graphics_base_prop_abstract_x_and_y/index.html" width="200" height="200"></iframe>

詳細については以下をご確認ください:

- [DisplayObject クラスの x と y インターフェイス](jp_display_object_x_and_y.md)

## visible 属性

`visible`属性ではオブジェクトの表示・非表示の属性値を取得・更新することができます。

<details>
<summary>コードブロックを表示:</summary>

```py
# runnable
from typing_extensions import TypedDict

import apysc as ap


class RectOptions(TypedDict):
    rectangle: ap.Rectangle


def on_timer(e: ap.TimerEvent, options: RectOptions) -> None:
    """
    The handler that the timer calls.

    Parameters
    ----------
    e : ap.TimerEvent
        Event instance.
    options : RectOptions
        Optional arguments dictionary.
    """
    rectangle: ap.Rectangle = options['rectangle']
    rectangle.visible = rectangle.visible.not_


ap.Stage(
    background_color='#333',
    stage_width=150,
    stage_height=150,
    stage_elem_id='stage')
sprite: ap.Sprite = ap.Sprite()
sprite.graphics.begin_fill(color='#0af')
rectangle: ap.Rectangle = sprite.graphics.draw_rect(
    x=50, y=50, width=50, height=50)

options: RectOptions = {'rectangle': rectangle}
ap.Timer(on_timer, delay=1000, options=options).start()

ap.save_overall_html(
    dest_dir_path='do_and_graphics_base_prop_abstract_visible/')
```

</details>

<iframe src="static/do_and_graphics_base_prop_abstract_visible/index.html" width="150" height="150"></iframe>

詳細については以下をご確認ください:

- [DisplayObject クラスの visible (表示・非表示) のインターフェイス](jp_display_object_visible.md)

## 回転の各インターフェイス

`rotation_around_center`属性、`get_rotation_around_point`メソッド、そして`set_rotation_around_point`メソッドでは回転の角度の値の取得と更新を行うことができます。

<details>
<summary>コードブロックを表示:</summary>

```py
# runnable
from typing_extensions import TypedDict

import apysc as ap


class RectOptions(TypedDict):
    rectangle: ap.Rectangle


def on_timer(e: ap.TimerEvent, options: RectOptions) -> None:
    """
    The handler that the timer calls.

    Parameters
    ----------
    e : ap.TimerEvent
        Event instance.
    options : RectOptions
        Optional arguments dictionary.
    """
    rectangle: ap.Rectangle = options['rectangle']
    rectangle.rotation_around_center += 1


ap.Stage(
    background_color='#333',
    stage_width=150,
    stage_height=150,
    stage_elem_id='stage')
sprite: ap.Sprite = ap.Sprite()
sprite.graphics.begin_fill(color='#0af')
rectangle: ap.Rectangle = sprite.graphics.draw_rect(
    x=50, y=50, width=50, height=50)

options: RectOptions = {'rectangle': rectangle}
ap.Timer(on_timer, delay=ap.FPS.FPS_60, options=options).start()

ap.save_overall_html(
    dest_dir_path='do_and_graphics_base_prop_abstract_rotation/')
```

</details>

<iframe src="static/do_and_graphics_base_prop_abstract_rotation/index.html" width="150" height="150"></iframe>

詳細については以下をご確認ください:

- [GraphicsBase クラスの rotation_around_center (中央座標基準の回転) インターフェイス](jp_graphics_base_rotation_around_center.md)
- [GraphicsBase クラスの rotation_around_point (指定座標基準の回転) の各インターフェイス](jp_graphics_base_rotation_around_point.md)

## 拡縮の各インターフェイス

`scale_x_from_center`属性、`scale_y_from_center`属性、`get_scale_x_from_point`メソッド、`set_scale_x_from_point`メソッド、`get_scale_y_from_point`メソッド、そして`set_scale_y_from_point`メソッドの各インターフェイスでは拡縮の値の取得と更新を行うことができます。

<details>
<summary>コードブロックを表示:</summary>

```py
# runnable
from typing_extensions import TypedDict

import apysc as ap


class RectOptions(TypedDict):
    rectangle: ap.Rectangle
    scale_value: ap.Number


def on_timer(e: ap.TimerEvent, options: RectOptions) -> None:
    """
    The handler that the timer calls.

    Parameters
    ----------
    e : ap.TimerEvent
        Event instance.
    options : RectOptions
        Optional arguments dictionary.
    """
    rectangle: ap.Rectangle = options['rectangle']
    scale_value: ap.Number = options['scale_value']
    rectangle.scale_x_from_center += scale_value
    rectangle.scale_y_from_center += scale_value

    with ap.If(rectangle.scale_x_from_center >= 2.0):
        scale_value.value = -0.01
        ap.Return()

    with ap.If(rectangle.scale_y_from_center <= 0.5):
        scale_value.value = 0.01
        ap.Return()


ap.Stage(
    background_color='#333',
    stage_width=150,
    stage_height=150,
    stage_elem_id='stage')
sprite: ap.Sprite = ap.Sprite()
sprite.graphics.begin_fill(color='#0af')
rectangle: ap.Rectangle = sprite.graphics.draw_rect(
    x=50, y=50, width=50, height=50)

scale_value: ap.Number = ap.Number(0.01)
options: RectOptions = {'rectangle': rectangle, 'scale_value': scale_value}
ap.Timer(on_timer, delay=ap.FPS.FPS_60, options=options).start()

ap.save_overall_html(
    dest_dir_path='do_and_graphics_base_prop_abstract_scale/')
```

</details>

<iframe src="static/do_and_graphics_base_prop_abstract_scale/index.html" width="150" height="150"></iframe>

詳細については以下をご確認ください:

- [GraphicsBase クラスの scale_from_center (中央座標基準の拡縮) の各インターフェイス](jp_graphics_base_scale_from_center.md)
- [GraphicsBase クラスの scale_from_point (指定座標基準の拡縮) の各インターフェイス](jp_graphics_base_scale_from_point.md)

## 反転の各属性

`flip_x`と`flip_y`の属性では反転の属性値の取得と更新を行うことができます。

<details>
<summary>コードブロックを表示:</summary>

```py
# runnable
from typing_extensions import TypedDict

import apysc as ap


class LineOptions(TypedDict):
    line: ap.Line


def on_timer(e: ap.TimerEvent, options: LineOptions) -> None:
    """
    The handler that the timer calls.

    Parameters
    ----------
    e : ap.TimerEvent
        Event instance.
    options : LineOptions
        Optional arguments dictionary.
    """
    line: ap.Line = options['line']
    line.flip_x = line.flip_x.not_


ap.Stage(
    background_color='#333',
    stage_width=150,
    stage_height=150,
    stage_elem_id='stage')
sprite: ap.Sprite = ap.Sprite()
sprite.graphics.line_style(color='#fff', thickness=5)
line: ap.Line = sprite.graphics.draw_line(
    x_start=50, y_start=50, x_end=100, y_end=100)

options: LineOptions = {'line': line}
ap.Timer(on_timer, delay=1000, options=options).start()

ap.save_overall_html(
    dest_dir_path='do_and_graphics_base_prop_abstract_flip/')
```

</details>

<iframe src="static/do_and_graphics_base_prop_abstract_flip/index.html" width="150" height="150"></iframe>

詳細については以下をご確認ください:

- [GraphicsBase クラスの flip_x (横軸の反転) と flip_y (縦軸の反転) のインターフェイス](jp_graphics_base_flip_interfaces.md)

## 歪みの各属性

`skew_x`と`skew_y`の各属性では歪みの値を取得・更新することができます。

<details>
<summary>コードブロックを表示:</summary>

```py
# runnable
from typing_extensions import TypedDict

import apysc as ap


class RectOptions(TypedDict):
    rectangle: ap.Rectangle


def on_timer(e: ap.TimerEvent, options: RectOptions) -> None:
    """
    The handler that the timer calls.

    Parameters
    ----------
    e : ap.TimerEvent
        Event instance.
    options : RectOptions
        Optional arguments dictionary.
    """
    rectangle: ap.Rectangle = options['rectangle']
    rectangle.skew_x += 1


ap.Stage(
    background_color='#333',
    stage_width=150,
    stage_height=150,
    stage_elem_id='stage')
sprite: ap.Sprite = ap.Sprite()
sprite.graphics.begin_fill(color='#0af')
rectangle: ap.Rectangle = sprite.graphics.draw_rect(
    x=50, y=50, width=50, height=50)

options: RectOptions = {'rectangle': rectangle}
ap.Timer(on_timer, delay=ap.FPS.FPS_60, options=options).start()

ap.save_overall_html(
    dest_dir_path='do_and_graphics_base_prop_abstract_skew/')
```

</details>

<iframe src="static/do_and_graphics_base_prop_abstract_skew/index.html" width="150" height="150"></iframe>

詳細については以下をご確認ください:

- [GraphicsBase クラスの skew_x (X軸の歪み) と skew_y (Y軸の歪み) のインターフェイス](jp_graphics_base_skew.md)

## 関連資料

- [DisplayObject クラス](jp_display_object.md)
- [DisplayObjectクラス parent （親要素属性）のインターフェイス](jp_display_object_parent.md)