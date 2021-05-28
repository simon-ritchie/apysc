# Stage

This page will explain `Stage` class.

## What is Stage

Stage is apysc's overall drawing area (it's like a view port or canvas, or something else) and a container of all elements.

Stage must be created at the first of apysc project (this will run cleaning up processes).

## Create stage

Creating stage is simple, like this:

```py
# runnable
from apysc import Stage

stage: Stage = Stage()
```

## Stage background color setting

Stage class has a `background_color` option, and this will change stage's background color.

```py
# runnable
from apysc import Stage
from apysc import save_expressions_overall_html

stage: Stage = Stage(
    background_color='#333',
    stage_elem_id='stage')

save_expressions_overall_html(dest_dir_path='stage_background_color/')
```

This will create HTML with black background stage, as follows:

<iframe src="static/stage_background_color/index.html" width="300" height="185"></iframe>

## Stage size setting

Stage class has options to set stage width and stage height (arguments of `stage_width` and `stage_height`). These settings will change stage sizes.

```py
# runnable
from apysc import Stage
from apysc import save_expressions_overall_html

stage: Stage = Stage(
    stage_width=500, stage_height=50,
    background_color='#333',
    stage_elem_id='stage')

save_expressions_overall_html(dest_dir_path='stage_size/')
```

The Previous script will create a horizontal stage, as follows:

<iframe src="static/stage_size/index.html" width="500", height="50"></iframe>

## Stage element id setting

Stage element id (HTML id) can be set by `stage_elem_id` argument. If this will not be specified, then any unique id will be set (based on created timestamp, like `stage_12345...`).

```py
# runnable
from apysc import Stage

stage: Stage = Stage(
    background_color='#333',
    stage_elem_id='line_chart_1')
```

This option is useful when apysc project is used multiple times (for an easily identifiable ID) or for version control.
