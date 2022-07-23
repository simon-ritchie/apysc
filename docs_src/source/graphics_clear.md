# Graphics clear interface

This page explains the `Graphics` class `clear` method interface.

## What interface is this?

The `clear` method removes all graphics and clears (resets) fill and line settings.

## Basic usage

The `clear` method takes no arguments.

The handler calls the `clear` method in the following example if you click any rectangle.

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
    ap.assert_equal(sprite.graphics.fill_color, "#00aaff")
    sprite.graphics.clear()
    ap.assert_equal(sprite.graphics.fill_color, "")


ap.Stage(
    stage_width=250, stage_height=150, background_color="#333", stage_elem_id="stage"
)
sprite: ap.Sprite = ap.Sprite()
sprite.graphics.begin_fill(color="#0af")
sprite.graphics.draw_rect(x=50, y=50, width=50, height=50)
sprite.graphics.draw_rect(x=150, y=50, width=50, height=50)
sprite.click(on_click)

ap.save_overall_html(dest_dir_path="graphics_clear_basic_usage/")
```

<iframe src="static/graphics_clear_basic_usage/index.html" width="250" height="150"></iframe>