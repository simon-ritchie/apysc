# delete interface

This page explains the `delete` function interface.

## What interface is this?

The `delete` function deletes any instance, and it becomes an `undefined` object.

If an instance is a `DisplayObject` instance, this interface removes an instance from the stage.

For example, this interface removes a `Sprite` or `Rectangle` instance.

## Basic usage

You can specify any apysc instance to the `delete` argument.

```py
# runnable
import apysc as ap

ap.Stage()
int_val: ap.Int = ap.Int(10)
ap.delete(int_val)
```

If a specified instance is a `DisplayObject` instance, this function removes it from a stage.

Also, it becomes an undefined object.

```py
# runnable
import apysc as ap


def on_click(e: ap.MouseEvent[ap.Sprite], options: dict) -> None:
    """
    The click event handler that a sprite calls.

    Parameters
    ----------
    e : ap.MouseEvent[ap.Sprite]
        Event instance.
    options : dict
        Optional arguments dictionary.
    """
    sprite: ap.Sprite = e.this
    ap.delete(sprite)
    ap.assert_undefined(sprite)


ap.Stage(
    stage_width=150,
    stage_height=150,
    background_color=ap.Color("#333"),
    stage_elem_id="stage",
)
sprite: ap.Sprite = ap.Sprite()
sprite.graphics.begin_fill(color=ap.Color("#0af"))
sprite.graphics.draw_rect(x=50, y=50, width=50, height=50)
sprite.click(on_click)

ap.save_overall_html(dest_dir_path="delete_basic_usage/")
```

If you click the following rectangle, the `delete` function removes it from the stage.

<iframe src="static/delete_basic_usage/index.html" width="150" height="150"></iframe>