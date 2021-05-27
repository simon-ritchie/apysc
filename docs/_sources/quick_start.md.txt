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
from apysc import Stage

stage = Stage(stage_width=300, stage_height=180, background_color='#333')
```

Then you can export each HTML and js filed by `save_expressions_overall_html` function (in this case, only the black background stage will be displayed).

```py
# runnable
from apysc import Stage
from apysc import save_expressions_overall_html

stage = Stage(
    stage_width=300, stage_height=180, background_color='#333',
    stage_elem_id='stage')
save_expressions_overall_html(
    dest_dir_path='quick_start_stage_creation/')
```

This code will create each HTML and js files to `dest_dir_path`. You can confirm an exported result by opening `index.html` (`quick_start_stage_creation/index.html`).

<iframe src="static/quick_start_stage_creation/index.html"></iframe>

