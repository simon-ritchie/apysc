# PathClose class

This page explains the `PathClose` class.

## What class is this?

The `PathClose` class is the class to close a path.

If a path's start and end points are not connecting, this setting connects these points.

Mainly, the `Path` class constructor or `draw_path` interfaces use this setting.

## Basic usage

The `PathClose` class constructor takes no arguments.

The `Path` class constructor or `draw_path` interfaces' `path_data_list` argument requires its instance.

In the following example, the left path graphics do not use this `Close` class setting.

Conversely, the right path graphics use the `Close` class setting, and it connects the start and end points:

```py
# runnable
import apysc as ap

ap.Stage(
    background_color=ap.Color("#333"),
    stage_width=250,
    stage_height=150,
    stage_elem_id="stage",
)
left_path: ap.Path = ap.Path(
    path_data_list=[
        ap.PathMoveTo(x=75, y=50),
        ap.PathLineTo(x=50, y=100),
        ap.PathLineTo(x=100, y=100),
    ],
    line_color=ap.Color("#0af"),
    line_thickness=5,
)

right_path: ap.Path = ap.Path(
    path_data_list=[
        ap.PathMoveTo(x=175, y=50),
        ap.PathLineTo(x=150, y=100),
        ap.PathLineTo(x=200, y=100),
        ap.PathClose(),
    ],
    line_color=ap.Color("#0af"),
    line_thickness=5,
)

ap.save_overall_html(dest_dir_path="path_close_basic_usage/")
```

<iframe src="static/path_close_basic_usage/index.html" width="250" height="150"></iframe>

## PathClose class constructor API

<!-- Docstring: apysc._geom.path_close.PathClose.__init__ -->

<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>

**[Interface signature]** `__init__(self) -> None`<hr>

**[Interface summary]**

Path data class for the SVG's `close path` (Z).<hr>

**[Examples]**

```py
>>> import apysc as ap
>>> stage: ap.Stage = ap.Stage()
>>> sprite: ap.Sprite = ap.Sprite()
>>> sprite.graphics.line_style(color=ap.Color("#fff"), thickness=3)
>>> path: ap.Path = sprite.graphics.draw_path(
...     path_data_list=[
...         ap.PathMoveTo(x=0, y=00),
...         ap.PathLineTo(x=50, y=0),
...         ap.PathLineTo(x=50, y=50),
...         ap.PathClose(),
...     ]
... )
```

<hr>

**[References]**

- [Path class](https://simon-ritchie.github.io/apysc/en/path.html)
- [Graphics draw_path interface](https://simon-ritchie.github.io/apysc/en/graphics_draw_path.html)