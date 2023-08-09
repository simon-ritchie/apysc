# GraphicsBase line_dash_setting interface

This page explains the `GraphicsBase` class `line_dash_setting` property interface.

## What interface is this?

The `line_dash_setting` property interface updates or gets the instance's current line dash setting.

## Basic usage

The getter or setter interface value becomes (or requires) the `LineDashSetting` instance value.

The following example sets the 10-pixel dash size and 3-pixel space size to the line:

```py
# runnable
import apysc as ap

ap.Stage(
    stage_width=250,
    stage_height=100,
    background_color=ap.Color("#333"),
    stage_elem_id="stage",
)
sprite: ap.Sprite = ap.Sprite()
sprite.graphics.line_style(color=ap.Color("#0af"), thickness=5)

line: ap.Line = sprite.graphics.draw_line(x_start=50, y_start=50, x_end=200, y_end=50)
line.line_dash_setting = ap.LineDashSetting(dash_size=10, space_size=3)

ap.save_overall_html(dest_dir_path="./graphics_base_line_dash_setting_basic_usage/")
```

<iframe src="static/graphics_base_line_dash_setting_basic_usage/index.html" width="250" height="100"></iframe>

## Delete setting

The `delete_line_dash_setting` interface deletes this line setting.

In the following example, if you click the rectangle, the handler deletes the line setting:

```py
# runnable
import apysc as ap


def on_click(e: ap.MouseEvent[ap.Rectangle], options: dict) -> None:
    """
    The handler for the click event.

    Parameters
    ----------
    e : ap.MouseEvent[ap.Rectangle]
        Event instance.
    options : dict
        Optional argument dictionary.
    """
    rectangle: ap.Rectangle = e.this
    rectangle.delete_line_dash_setting()


ap.Stage(
    stage_width=150,
    stage_height=150,
    background_color=ap.Color("#333"),
    stage_elem_id="stage",
)
rectangle: ap.Rectangle = ap.Rectangle(
    x=50,
    y=50,
    width=50,
    height=50,
    fill_color=ap.Color("#666"),
    line_color=ap.Color("#fff"),
    line_thickness=2,
    line_dash_setting=ap.LineDashSetting(dash_size=4, space_size=2),
)
rectangle.click(handler=on_click)

ap.save_overall_html(dest_dir_path="./graphics_base_line_dash_setting_delete_setting/")
```

<iframe src="static/graphics_base_line_dash_setting_delete_setting/index.html" width="150" height="150"></iframe>

## line_dash_setting property API

<!-- Docstring: apysc._display.line_dash_setting_mixin.LineDashSettingMixIn.line_dash_setting -->

<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>

**[Interface summary]**

Get a current line dash setting.<hr>

**[Returns]**

- `line_dash_setting`: LineDashSetting or None
  - Line dash setting.

<hr>

**[Examples]**

```py
>>> import apysc as ap
>>> stage: ap.Stage = ap.Stage()
>>> sprite: ap.Sprite = ap.Sprite()
>>> sprite.graphics.line_style(color=ap.Color("#fff"), thickness=10)
>>> line: ap.Line = sprite.graphics.draw_line(
...     x_start=50, y_start=50, x_end=150, y_end=50
... )
>>> line.line_dash_setting = ap.LineDashSetting(dash_size=5, space_size=2)
>>> line.line_dash_setting.dash_size
Int(5)

>>> line.line_dash_setting.space_size
Int(2)
```

## delete_line_dash_setting API

<!-- Docstring: apysc._display.line_dash_setting_mixin.LineDashSettingMixIn.delete_line_dash_setting -->

<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>

**[Interface signature]** `delete_line_dash_setting(self) -> None`<hr>

**[Interface summary]**

Delete a current line dash setting.