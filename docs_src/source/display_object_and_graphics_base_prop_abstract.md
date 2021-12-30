# DisplayObject and GraphicsBase classes base properties abstract

This page would explain the `DisplayObject` and `GraphicsBase` classes' each property (such as the x, visible) abstract.

## What apysc can do in its properties

- You can get/set each property value, such as the x, y, visible, scale, etc.

## x and y properties

The `x` and `y` properties can get/set the x and y coordinates.

<details>
<summary>Display the code block:</summary>

```py
# runnable
from typing_extensions import TypedDict

import apysc as ap


class RectOptions(TypedDict):
    rectangle: ap.Rectangle
    direction: ap.Int


def on_timer(e: ap.TimerEvent, options: RectOptions) -> None:
    """
    The handler would be called from a timer.

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


stage: ap.Stage = ap.Stage(
    background_color='#333',
    stage_width=200,
    stage_height=200,
    stage_elem_id='stage')
sprite: ap.Sprite = ap.Sprite(stage=stage)
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

For more details, please see [DisplayObject class x and y interfaces](display_object_x_and_y.md).

## visible property

The `visible` property can get/set the visibility of an object.

<details>
<summary>Display the code block:</summary>

```py
# runnable
from typing_extensions import TypedDict

import apysc as ap


class RectOptions(TypedDict):
    rectangle: ap.Rectangle


def on_timer(e: ap.TimerEvent, options: RectOptions) -> None:
    """
    The handler would be called from a timer.

    Parameters
    ----------
    e : ap.TimerEvent
        Event instance.
    options : RectOptions
        Optional arguments dictionary.
    """
    rectangle: ap.Rectangle = options['rectangle']
    rectangle.visible = rectangle.visible.not_


stage: ap.Stage = ap.Stage(
    background_color='#333',
    stage_width=150,
    stage_height=150,
    stage_elem_id='stage')
sprite: ap.Sprite = ap.Sprite(stage=stage)
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

For more details, please see [DisplayObject class visible interface](display_object_visible.md).

## rotation interfaces

The `rotation_around_center` property, `get_rotation_around_point` method, and `set_rotation_around_point` method can get/set the rotation angle.

<details>
<summary>Display the code block:</summary>

```py
# runnable
from typing_extensions import TypedDict

import apysc as ap


class RectOptions(TypedDict):
    rectangle: ap.Rectangle


def on_timer(e: ap.TimerEvent, options: RectOptions) -> None:
    """
    The handler would be called from a timer.

    Parameters
    ----------
    e : ap.TimerEvent
        Event instance.
    options : RectOptions
        Optional arguments dictionary.
    """
    rectangle: ap.Rectangle = options['rectangle']
    rectangle.rotation_around_center += 1


stage: ap.Stage = ap.Stage(
    background_color='#333',
    stage_width=150,
    stage_height=150,
    stage_elem_id='stage')
sprite: ap.Sprite = ap.Sprite(stage=stage)
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

For more details, please see [GraphicsBase class rotation around center interface](graphics_base_rotation_around_center.md) and [GraphicsBase class rotation around point interfaces](graphics_base_rotation_around_point.md).

## scale properties

## flip properties

## skew properties

## See also

- [DisplayObject class](display_object.md)
- [DisplayObject class parent interfaces](display_object_parent.md)
