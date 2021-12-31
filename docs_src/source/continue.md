# Continue

This page will explain the `Continue` class.

Before reading on, maybe it is useful to read the following page (the `Continue` class will be used for the same reason of each apysc data type):

- [Why not using the Python built-in data type in the apysc library?](why_not_using_python_builtin_data_type.md)

## What is the Continue class?

The `Continue` class will be used in the `with For` block to skip a current loop iteration (in JavaScript). It will behave like the Python built-in `continue` keyword.

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

If you use the `Continue` class in the out of the `with For` block then an exception will be raised:

```py
import apysc as ap

ap.Continue()
```

```
Exception: The `Continue` class can be instantiated in the with loop statement, for example, after the `with ap.For(...):` statement.
```
