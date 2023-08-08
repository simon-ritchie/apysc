# DisplayObject class visible interface

This page explains the `DisplayObject` class `visible` property interface.

## What interface is this?

The `visible` property interface will change the `DisplayObject` visible / invisible state.

## Basic usage

The `visible` property accepts a `Boolean` value. If you set the True value, a `DisplayObject` instance becomes visible (default). Conversely, if you set the False value, a `DisplayObject` instance becomes invisible.

The following example switches the visible values when you click the rectangle. For example, suppose you click the left rectangle (the rectangle_1). In that case, the left rectangle becomes invisible, and the right rectangle (rectangle_2) becomes visible.

```py
# runnable
from typing_extensions import TypedDict

import apysc as ap


class _RectOptions(TypedDict):
    rectangle: ap.Rectangle


def on_rectangle_1_click(e: ap.MouseEvent[ap.Rectangle], options: _RectOptions) -> None:
    """
    The handler that the first rectangle calls when clicked.

    Parameters
    ----------
    e : MouseEvent
        Event instance.
    options : dict
        Optional arguments dictionary.
    """
    rectangle_1: ap.Rectangle = e.this
    rectangle_2: ap.Rectangle = options["rectangle"]
    rectangle_1.visible = ap.Boolean(False)
    rectangle_2.visible = ap.Boolean(True)


def on_rectangle_2_click(e: ap.MouseEvent[ap.Rectangle], options: _RectOptions) -> None:
    """
    The handler that the second rectangle calls when clicked.

    Parameters
    ----------
    e : MouseEvent
        Event instance.
    options : dict
        Optional arguments dictionary.
    """
    rectangle_1: ap.Rectangle = options["rectangle"]
    rectangle_2: ap.Rectangle = e.this
    rectangle_1.visible = ap.Boolean(True)
    rectangle_2.visible = ap.Boolean(False)


ap.Stage(
    background_color=ap.Color("#333"),
    stage_width=250,
    stage_height=150,
    stage_elem_id="stage",
)

sprite: ap.Sprite = ap.Sprite()

sprite.graphics.begin_fill(color=ap.Color("#0af"))
rectangle_1: ap.Rectangle = sprite.graphics.draw_rect(x=50, y=50, width=50, height=50)

sprite.graphics.begin_fill(color=ap.Color("#f0a"))
rectangle_2: ap.Rectangle = sprite.graphics.draw_rect(x=150, y=50, width=50, height=50)
rectangle_2.visible = ap.Boolean(False)

options: _RectOptions = {"rectangle": rectangle_2}
rectangle_1.click(on_rectangle_1_click, options=options)
options = {"rectangle": rectangle_1}
rectangle_2.click(on_rectangle_2_click, options=options)

ap.save_overall_html(dest_dir_path="display_object_visible_basic_usage/")
```

<iframe src="static/display_object_visible_basic_usage/index.html" width="250" height="150"></iframe>


## visible property API

<!-- Docstring: apysc._display.visible_mixin.VisibleMixIn.visible -->

<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>

**[Interface summary]**

Get a visibility value of this instance.<hr>

**[Returns]**

- `result`: Boolean
  - If this instance is visible, this interface returns True.

<hr>

**[Examples]**

```py
>>> import apysc as ap
>>> stage: ap.Stage = ap.Stage()
>>> sprite: ap.Sprite = ap.Sprite()
>>> sprite.graphics.begin_fill(color=ap.Color("#0af"))
>>> rectangle: ap.Rectangle = sprite.graphics.draw_rect(
...     x=50, y=50, width=50, height=50
... )
>>> rectangle.visible = ap.Boolean(False)
>>> rectangle.visible
Boolean(False)
```