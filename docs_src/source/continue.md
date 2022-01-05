# Continue

This page explains the `Continue` class.

Before reading on, maybe it is helpful to read the following page (apysc uses the `Continue` class for the same reason):

- [Why the apysc library doesn't use the Python built-in data type](why_apysc_doesnt_use_python_builtin_data_type.md)

## What is the Continue class?

The `with For` block uses the `Continue` class to skip a current loop iteration (in JavaScript). It behaves like the Python built-in `continue` keyword.

## Basic usage

The `Continue` class can only be used in the `with For` (or other loop class) block, as follows:

```py
# runnable
import apysc as ap

ap.Stage(
    stage_width=250, stage_height=150,
    background_color='#333', stage_elem_id='stage')
sprite: ap.Sprite = ap.Sprite()

arr: ap.Array = ap.Array(range(2))
i: ap.Int
with ap.For(arr) as i:
    condition: ap.Boolean = i == 0
    with ap.If(condition):
        sprite.graphics.begin_fill(color='#0af')
        sprite.graphics.draw_rect(x=50, y=50, width=50, height=50)
        ap.Continue()

    sprite.graphics.begin_fill(color='#f0a')
    sprite.graphics.draw_rect(x=150, y=50, width=50, height=50)

ap.save_overall_html(
    dest_dir_path='continue_basic_usage/')
```

<iframe src="static/continue_basic_usage/index.html" width="250" height="150"></iframe>

If you use the `Continue` class in the out of the `with For` block, then an exception is raised:

```py
import apysc as ap

ap.Continue()
```

```
Exception: The `Continue` class can be instantiated in the with loop statement, for example, after the `with ap.For(...):` statement.
```
