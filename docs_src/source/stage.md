# Stage

This page explains the `Stage` class.

## What is the Stage?

The `Stage` is the apysc overall drawing area (like a viewport or canvas, or something else) and a container of all elements.

You must create the `Stage` at the first of the apysc project (this runs cleaning up internal data and files).

## Create stage

Creating stage is simple, like this:

```py
# runnable
import apysc as ap

stage: ap.Stage = ap.Stage()
```

## Stage background color setting

`Stage` class has a `background_color` option, which changes the stage's background color.

```py
# runnable
import apysc as ap

stage: ap.Stage = ap.Stage(
    background_color='#333',
    stage_elem_id='stage')

ap.save_overall_html(
    dest_dir_path='stage_background_color/')
```

This will create HTML with black background stage, as follows:

<iframe src="static/stage_background_color/index.html" width="300" height="185"></iframe>

## Stage size setting

Stage class has options to set stage width and stage height (arguments of `stage_width` and `stage_height`). These settings change stage sizes.

```py
# runnable
import apysc as ap

stage: ap.Stage = ap.Stage(
    stage_width=500, stage_height=50,
    background_color='#333',
    stage_elem_id='stage')

ap.save_overall_html(
    dest_dir_path='stage_size/')
```

The Previous script will create a horizontal stage, as follows:

<iframe src="static/stage_size/index.html" width="500", height="50"></iframe>

## Stage element id setting

Stage element id (HTML id) can be set by `stage_elem_id` argument. If you don't specify this, the apysc sets any unique id (based on created timestamp, like `stage_12345...`).

```py
# runnable
import apysc as ap

stage: ap.Stage = ap.Stage(
    background_color='#333',
    stage_elem_id='line_chart_1')
```

This option is useful when using the apysc project multiple times (for an easily identifiable ID) or version control.