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

## remove_children API

<!-- Docstring: apysc._display.child_mixin.ChildMixIn.remove_children -->

<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>

**[Interface signature]** `remove_children(self) -> None`<hr>

**[Interface summary]**

Remove all children from this instance.<hr>

**[Examples]**

```py
>>> import apysc as ap
>>> sprite: ap.Sprite = ap.Sprite()
>>> rectangle_1: ap.Rectangle = ap.Rectangle(
...     x=50, y=50, width=50, height=50, fill_color="#0af"
... )
>>> rectangle_2: ap.Rectangle = ap.Rectangle(
...     x=150, y=50, width=50, height=50, fill_color="#0af"
... )
>>> sprite.add_child(child=rectangle_1)
>>> sprite.add_child(child=rectangle_2)
>>> sprite.remove_children()
>>> sprite.num_children
Int(0)
```