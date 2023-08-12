# PathHorizontal class

This page explains the `PathHorizontal` class.

## What class is this?

The `PathHorizontal` class is the class to set a new horizontal line on a path.

It simplifies an implementation if you need to draw a horizontal line and not change a vertical coordinate.

Mainly, the `Path` class constructor or `draw_path` interfaces use this setting.

## Basic usage

The `PathHorizontal` class constructor requires only one argument, `x`.

The `Path` class constructor or `draw_path` interfaces' `path_data_list` argument requires its instance.

The following example sets the x=150 coordinate and draws the horizontal line from the x=50 coordinate:

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
        ap.PathHorizontal(x=150),
    ],
    line_color=ap.Color("#0af"),
    line_thickness=5,
)

ap.save_overall_html(dest_dir_path="path_horizontal_basic_usage/")
```

<iframe src="static/path_horizontal_basic_usage/index.html" width="200" height="100"></iframe>

## Relative position setting

The constructor's `relative` optional argument changes its behavior.

For example, if you set True to its argument, coordinates become relative.

The default setting is False, and it becomes absolute.

The following example sets the relative setting and moves to the 50px right position from the current position:

```py
# runnable
import apysc as ap

ap.Stage(
    background_color=ap.Color("#333"),
    stage_width=150,
    stage_height=100,
    stage_elem_id="stage",
)
path: ap.Path = ap.Path(
    path_data_list=[
        ap.PathMoveTo(x=50, y=50),
        ap.PathHorizontal(x=50, relative=True),
    ],
    line_color=ap.Color("#0af"),
    line_thickness=5,
)

ap.save_overall_html(dest_dir_path="path_horizontal_relative/")
```

<iframe src="static/path_horizontal_relative/index.html" width="150" height="100"></iframe>

## PathHorizontal class constructor API

<!-- Docstring: apysc._geom.path_horizontal.PathHorizontal.__init__ -->

<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>

**[Interface signature]** `__init__(self, x: Union[float, apysc._type.number.Number], *, relative: Union[bool, apysc._type.boolean.Boolean] = False, variable_name_suffix: str = '') -> None`<hr>

**[Interface summary]**

Path data class for the SVG's `horizontal line` (H).<hr>

**[Parameters]**

- `x`: float or Number
  - X-coordinate of the destination point.
- `relative`: bool or Boolean, default False
  - A boolean value indicates whether the path coordinates are relative or not (absolute).
- `variable_name_suffix`: str, default ''
  - A JavaScript variable name suffix string. This setting is sometimes useful for JavaScript debugging.

<hr>

**[Examples]**

```py
>>> import apysc as ap
>>> stage: ap.Stage = ap.Stage()
>>> sprite: ap.Sprite = ap.Sprite()
>>> sprite.graphics.line_style(color=ap.Color("#fff"), thickness=3)
>>> path: ap.Path = sprite.graphics.draw_path(
...     path_data_list=[
...         ap.PathMoveTo(x=0, y=50),
...         ap.PathHorizontal(x=50),
...     ]
... )
```

<hr>

**[References]**

- [Path class](https://simon-ritchie.github.io/apysc/en/path.html)
- [Graphics draw_path interface](https://simon-ritchie.github.io/apysc/en/graphics_draw_path.html)