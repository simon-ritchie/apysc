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

stage: Stage = Stage(background_color='#333')

save_expressions_overall_html(dest_dir_path='stage_background_color/')
```

This will create HTML with black background stage, as follows:

<iframe src="static/stage_background_color/index.html"
width="300" height="185"></iframe>

## Stage size setting

Stage class has options to set stage width and stage height.
