# DateTime class now interface

This page explains the `DateTime` class `now` method interface.

## What interface is this?

The `DateTime`'s `now` class method returns a current time `DateTime` instance.

## Basic usage

The `DateTime` class has the `now` method defined as a class method.

It returns a `DateTime` instance, and its values become a current time.

In the following example, if you click the rectangle, the click handler displays a current year, month, and day on the browser console.

```py
# runnable
import apysc as ap


def on_click(e: ap.MouseEvent, options: dict) -> None:
    """
    The handler to handle a rectangle's click event.

    Parameters
    ----------
    e : ap.MouseEvent
        An event instance.
    options : dict
        Optional arguments dictionary.
    """
    now_datetime: ap.DateTime = ap.DateTime.now()
    ap.trace("Current year:", now_datetime.year)
    ap.trace("Current month:", now_datetime.month)
    ap.trace("Current day:", now_datetime.day)


ap.Stage(
    background_color=ap.Color("#333"),
    stage_width=150,
    stage_height=150,
    stage_elem_id="stage",
)
rectangle: ap.Rectangle = ap.Rectangle(
    x=50,
    y=50,
    width=50,
    height=50,
    fill_color=ap.Color("#0af"),
)
rectangle.click(on_click)

ap.save_overall_html(dest_dir_path="datetime_now_basic_usage/")
```

<iframe src="static/datetime_now_basic_usage/index.html" width="150" height="150"></iframe>

## now class method API

<!-- Docstring: apysc._time.datetime_.DateTime.now -->

<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>

**[Interface signature]** `now(*, variable_name_suffix: str = '') -> 'DateTime'`<hr>

**[Interface summary]**

Get a `DateTime` instance of the current time.<hr>

**[Parameters]**

- `variable_name_suffix`: str, default ''
  - A JavaScript variable name suffix string. This setting is sometimes useful for JavaScript debugging.

<hr>

**[Returns]**

- `dt`: DateTime
  - A created `DateTime` instance.

<hr>

**[Examples]**

```py
>>> from datetime import datetime
>>> import apysc as ap
>>> _ = ap.Stage()
>>> py_now: datetime = datetime.now()
>>> ap_now: ap.DateTime = ap.DateTime.now()
>>> ap_now.year == py_now.year
Boolean(True)

>>> ap_now.month == py_now.month
Boolean(True)

>>> ap_now.day == py_now.day
Boolean(True)
```