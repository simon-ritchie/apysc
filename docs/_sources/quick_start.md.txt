# Quick start

This page will explain the first step of apysc's journey.

## Installing

To use apysc library, Python 3.6 or later version is required.

You can use pip command to install apysc.

```
$ pip install apysc
```

## Create stage and export HTML

`Stage` instance is apysc's space for displaying each graphics. You can set arguments of `stage_width` for width setting, `stage_height` for height setting, and `background_color` for background.

```py
# runnable
from apysc import Stage

stage = Stage(stage_width=300, stage_height=180, background_color='#333')
```

Then you can export each HTML and js filed by `save_expressions_overall_html` function (in this case, only the black background stage will be displayed).

```py
# runnable
from apysc import Stage
from apysc import save_expressions_overall_html

stage: Stage = Stage(
    stage_width=300, stage_height=180, background_color='#333',
    stage_elem_id='stage')
save_expressions_overall_html(
    dest_dir_path='quick_start_stage_creation/')
```

This code will create each HTML and js files to `dest_dir_path`. You can confirm an exported result by opening `index.html` (`quick_start_stage_creation/index.html`), as follows:

<iframe src="static/quick_start_stage_creation/index.html" width="300" height="180"></iframe>

## Add sprite container and vector graphics

`Sprite` class is basic container object of each display objects, and it can make vector graphics with graphics property.

```py
# runnable
from apysc import Stage
from apysc import Sprite
from apysc import save_expressions_overall_html

stage: Stage = Stage(
    stage_width=250, stage_height=150, background_color='#333',
    stage_elem_id='stage')
sprite: Sprite = Sprite(stage)

# Draw polyline vector graphics.
sprite.graphics.line_style(color='#fff', thickness=3)
sprite.graphics.move_to(x=50, y=50)
sprite.graphics.line_to(x=100, y=50)
sprite.graphics.line_to(x=50, y=100)
sprite.graphics.line_to(x=100, y=100)

# Draw rectangle vector graphic.
sprite.graphics.begin_fill(color='#0af')
sprite.graphics.draw_rect(x=150, y=50, width=50, height=50)

save_expressions_overall_html(
    dest_dir_path='quick_start_sprite_graphics/')
```

<iframe src="static/quick_start_sprite_graphics/index.html" width="250" height="150"></iframe>

For more details of `Sprite`, `Graphics`, and so on, please see each interfaces documentation pages.
