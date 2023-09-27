# Graphics draw_path interface

This page explains the `Graphics` class `draw_path` interface.

## What interface is this?

The `draw_path` interface draws vector graphics of a path.

## Basic usage

The `draw_path` interface requires the `path_data_list` argument.

The `path_data_list` argument is a list of path data, such as the `PathLineTo` or `PathBezier2D`.

```py
# runnable
import apysc as ap

ap.Stage(
    background_color=ap.Color("#333"),
    stage_width=300,
    stage_height=150,
    stage_elem_id="stage",
)
sprite: ap.Sprite = ap.Sprite()
sprite.graphics.line_style(color=ap.Color("#0af"), thickness=5)
path: ap.Path = sprite.graphics.draw_path(
    path_data_list=[
        ap.PathMoveTo(x=50, y=100),
        ap.PathLineTo(x=100, y=100),
        ap.PathLineTo(x=150, y=50),
        ap.PathBezier2D(
            control_x=200,
            control_y=100,
            dest_x=250,
            dest_y=50,
        ),
    ],
)

ap.save_overall_html(dest_dir_path="graphics_draw_path_basic_usage/")
```

<iframe src="static/graphics_draw_path_basic_usage/index.html" width="300" height="150"></iframe>

## See also

- [Path class](path.md)
- [PathMoveTo class](path_move_to.md)
- [PathLineTo class](path_line_to.md)
- [PathHorizontal class](path_horizontal.md)
- [PathVertical class](path_vertical.md)
- [PathClose class](path_close.md)
- [PathBezier2D class](path_bezier_2d.md)
- [PathBezier2DContinual class](path_bezier_3d.md)
- [PathBezier3DContinual class](path_bezier_3d_continual.md)

## draw_path API

<!-- Docstring: apysc._display.graphics.Graphics.draw_path -->

<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>

**[Interface signature]** `draw_path(self, *, path_data_list: List[apysc._geom.path_data_base.PathDataBase], variable_name_suffix: str = '') -> '_path.Path'`<hr>

**[Interface summary]**

Draw a path vector graphics.<hr>

**[Parameters]**

- `path_data_list`: list of PathDataBase
  - Target path data settings, such as the ap.PathData.MoveTo.
- `variable_name_suffix`: str, default ""
  - A JavaScript variable name suffix string. This setting is sometimes useful for JavaScript debugging.

<hr>

**[Returns]**

- `path`: Path
  - Created path graphics instance.

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
...         ap.PathBezier2D(control_x=50, control_y=0, dest_x=100, dest_y=50),
...     ]
... )
```

<hr>

**[References]**

- [Path class](https://simon-ritchie.github.io/apysc/en/path.html)
- [PathMoveTo class](https://simon-ritchie.github.io/apysc/en/path_move_to.html)
- [PathLineTo class](https://simon-ritchie.github.io/apysc/en/path_line_to.html)
- [PathHorizontal class](https://simon-ritchie.github.io/apysc/en/path_horizontal.html)
- [PathVertical class](https://simon-ritchie.github.io/apysc/en/path_vertical.html)
- [PathClose class](https://simon-ritchie.github.io/apysc/en/path_close.html)
- [PathBezier2D class](https://simon-ritchie.github.io/apysc/en/path_bezier_2d.html)
- [PathBezier2DContinual class](https://simon-ritchie.github.io/apysc/en/path_bezier_2d_continual.html)
- [PathBezier3D class](https://simon-ritchie.github.io/apysc/en/path_bezier_3d.html)
- [PathBezier3DContinual class](https://simon-ritchie.github.io/apysc/en/path_bezier_3d_continual.html)