# Quick start guide

This page will explain the first step of the apysc library journey.

## Installing

To use apysc library Python 3.6 or the later version is required.

You can use the pip command to install apysc.

```
$ pip install apysc
```

## Create stage and export HTML

`Stage` instance is apysc's space for displaying each graphics. You can set arguments of `stage_width` for width setting, `stage_height` for height setting, and `background_color` for background.

```py
# runnable
import apysc as ap

stage = ap.Stage(stage_width=300, stage_height=180, background_color='#333')
```

Then you can export each HTML and js files by the `save_overall_html` function (in this case, only the black background stage will be displayed).

```py
# runnable
import apysc as ap

stage: ap.Stage = ap.Stage(
    stage_width=300, stage_height=180, background_color='#333',
    stage_elem_id='stage')
ap.save_overall_html(
    dest_dir_path='quick_start_stage_creation/')
```

This code will create each HTML and js files to `dest_dir_path`. You can confirm an exported result by opening `index.html` (`quick_start_stage_creation/index.html`), as follows:

<iframe src="static/quick_start_stage_creation/index.html" width="300" height="180"></iframe>

## Add sprite container and vector graphics

`Sprite` class is the basic container object of each display object, and it can make vector graphics with the `graphics` property.

```py
# runnable
import apysc as ap

stage: ap.Stage = ap.Stage(
    stage_width=250, stage_height=150, background_color='#333',
    stage_elem_id='stage')
sprite: ap.Sprite = ap.Sprite(stage)

# Draw polyline vector graphics.
sprite.graphics.line_style(color='#fff', thickness=3)
sprite.graphics.move_to(x=50, y=50)
sprite.graphics.line_to(x=100, y=50)
sprite.graphics.line_to(x=50, y=100)
sprite.graphics.line_to(x=100, y=100)

# Draw rectangle vector graphic.
sprite.graphics.begin_fill(color='#0af')
sprite.graphics.draw_rect(x=150, y=50, width=50, height=50)

ap.save_overall_html(
    dest_dir_path='quick_start_sprite_graphics/')
```

<iframe src="static/quick_start_sprite_graphics/index.html" width="250" height="150"></iframe>

For more details of `Sprite` and `Graphics` and so on, please see each interface documentation page.
