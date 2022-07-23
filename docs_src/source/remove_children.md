# remove_children interface

This page explains the `remove_children` method interface of container classes.

## What interface is this?

The `remove_children` method removes all children from a container instance.

## Basic usage

The `remove_children` method takes no arguments to use.

In the following example, if you click any rectangle, the handler calls the `remove_children` method and removes all children:

```py
# runnable
import apysc as ap


def on_click(e: ap.MouseEvent[ap.Sprite], options: dict) -> None:
    """
    The click event handler.

    Parameters
    ----------
    e : ap.MouseEvent[ap.Sprite]
        Event instance.
    options : dict
        Optional arguments dictionary.
    """
    sprite: ap.Sprite = e.this
    sprite.remove_children()


ap.Stage(
    stage_width=250, stage_height=150, background_color="#333", stage_elem_id="stage"
)
sprite: ap.Sprite = ap.Sprite()
sprite.graphics.begin_fill(color="#0af")
sprite.graphics.draw_rect(x=50, y=50, width=50, height=50)
sprite.graphics.draw_rect(x=150, y=50, width=50, height=50)
sprite.click(on_click)

ap.save_overall_html(dest_dir_path="remove_children_basic_usage/")
```

<iframe src="static/remove_children_basic_usage/index.html" width="250" height="150"></iframe>