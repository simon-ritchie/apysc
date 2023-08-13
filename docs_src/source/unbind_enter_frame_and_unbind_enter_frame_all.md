# unbind_enter_frame and unbind_enter_frame_all interfaces

This page explains the `unbind_enter_frame` and `unbind_enter_frame_all` methods interfaces.

## What interfaces are these?

The `unbind_enter_frame` and `unbind_enter_frame_all` methods disable an enter frame event's handler setting(s).

The `unbind_enter_frame` interface disables a specified single handler, and the `unbind_enter_frame_all` interface disables all handlers.

## Basic usage

The `unbind_enter_frame` interface requires the `handler` argument.

In addition, this interface raises an exception if a specified `handler` is not registered yet.

In the following example, if you click the rectangle, the handler disables an enter frame event.

```py
# runnable
import apysc as ap

stage: ap.Stage = ap.Stage(
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
    fill_color=ap.Color("#0af"),
)


def on_enter_frame(e: ap.EnterFrameEvent, options: dict) -> None:
    """
    The handler to handle an enter frame event.

    Parameters
    ----------
    e : ap.EnterFrameEvent
        Event instance.
    options : dict
        Optional argument dictionary.
    """
    rectangle.rotation_around_center += 1


def on_rectangle_click(
    e: ap.MouseEvent[ap.Rectangle],
    options: dict,
) -> None:
    """
    The handler to handle a rectangle click event.

    Parameters
    ----------
    e : ap.MouseEvent
        Event instance.
    options : dict
        Optional argument dictionary.
    """
    stage.unbind_enter_frame(handler=on_enter_frame)


stage.enter_frame(handler=on_enter_frame, fps=ap.FPS.FPS_30)
rectangle.click(handler=on_rectangle_click)
ap.save_overall_html(dest_dir_path="unbind_enter_frame_basic_usage/")
```

<iframe src="static/unbind_enter_frame_basic_usage/index.html" width="150" height="150"></iframe>

The `unbind_enter_frame_all` interface requires no argument.

In the following example, if you click any rectangle, the handler disables all enter frame events.

```py
# runnable
import apysc as ap

stage: ap.Stage = ap.Stage(
    stage_width=250,
    stage_height=150,
    background_color=ap.Color("#333"),
    stage_elem_id="stage",
)
left_rectangle: ap.Rectangle = ap.Rectangle(
    x=50,
    y=50,
    width=50,
    height=50,
    fill_color=ap.Color("#0af"),
)
right_rectangle: ap.Rectangle = ap.Rectangle(
    x=150,
    y=50,
    width=50,
    height=50,
    fill_color=ap.Color("#f0a"),
)


def on_enter_frame_1(e: ap.EnterFrameEvent, options: dict) -> None:
    """
    The handler to handle an enter frame event.

    Parameters
    ----------
    e : ap.EnterFrameEvent
        Event instance.
    options : dict
        Optional argument dictionary.
    """
    left_rectangle.rotation_around_center += 1


def on_enter_frame_2(e: ap.EnterFrameEvent, options: dict) -> None:
    """
    The handler to handle an enter frame event.

    Parameters
    ----------
    e : ap.EnterFrameEvent
        Event instance.
    options : dict
        Optional argument dictionary.
    """
    right_rectangle.rotation_around_center -= 1


def on_rectangle_click(e: ap.MouseEvent, options: dict) -> None:
    """
    The handler to handle a rectangle click event.

    Parameters
    ----------
    e : ap.MouseEvent
        Event instance.
    options : dict
        Optional argument dictionary.
    """
    stage.unbind_enter_frame_all()


stage.enter_frame(handler=on_enter_frame_1, fps=ap.FPS.FPS_30)
stage.enter_frame(handler=on_enter_frame_2, fps=ap.FPS.FPS_30)
left_rectangle.click(handler=on_rectangle_click)
right_rectangle.click(handler=on_rectangle_click)

ap.save_overall_html(dest_dir_path="unbind_enter_frame_all_basic_usage/")
```

<iframe src="static/unbind_enter_frame_all_basic_usage/index.html" width="250" height="150"></iframe>

## See also

- [enter_frame interface](enter_frame.md)

## unbind_enter_frame API

<!-- Docstring: apysc._event.enter_frame_mixin.EnterFrameMixIn.unbind_enter_frame -->

<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>

**[Interface signature]** `unbind_enter_frame(self, handler: Callable[[apysc._event.enter_frame_event.EnterFrameEvent, ~_Options], NoneType]) -> None`<hr>

**[Interface summary]**

Unbind a specified handler's enter-frame event.<hr>

**[Parameters]**

- `handler`: Callable[[EnterFrameEvent, _Options], None]
  - Unbinding target callable.

<hr>

**[Raises]**

- _EnterFrameEventNotRegistered: If there is no unbinding target of a specified handler.

<hr>

**[Examples]**

```py
>>> import apysc as ap
>>> stage: ap.Stage = ap.Stage()
>>> rectangle: ap.Rectangle = ap.Rectangle(
...     x=50, y=50, width=50, height=50, fill_color=ap.Color("#0af")
... )
>>> def on_enter_frame(e: ap.EnterFrameEvent, options: dict) -> None:
...     rectangle.x += 1
>>> stage.enter_frame(handler=on_enter_frame, fps=ap.FPS.FPS_30)
>>> # Any implementations here...
>>> stage.unbind_enter_frame(handler=on_enter_frame)
```

## unbind_enter_frame_all API

<!-- Docstring: apysc._event.enter_frame_mixin.EnterFrameMixIn.unbind_enter_frame_all -->

<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>

**[Interface signature]** `unbind_enter_frame_all(self) -> None`<hr>

**[Interface summary]**

Unbind all enter-frame events.<hr>

**[Examples]**

```py
>>> import apysc as ap
>>> stage: ap.Stage = ap.Stage()
>>> rectangle: ap.Rectangle = ap.Rectangle(
...     x=50, y=50, width=50, height=50, fill_color=ap.Color("#0af")
... )
>>> def on_enter_frame(e: ap.EnterFrameEvent, options: dict) -> None:
...     rectangle.x += 1
>>> stage.enter_frame(handler=on_enter_frame, fps=ap.FPS.FPS_30)
>>> # Any implementations here...
>>> stage.unbind_enter_frame_all()
```