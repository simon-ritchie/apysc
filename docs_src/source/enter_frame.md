# enter_frame interface

This page explains the `enter_frame` method interface.

## What interface is this?

The `enter_frame` interface sets a handler for an animation.

This interface calls a specified handler at each frame.

## Which should we use, the Timer class or the enter_frame interface?

The `Timer` class also can handle animation.

So, Which should we use, the `Timer` class or the `enter_frame` interface for an animation?

The answer is, basically, the `enter_frame`.

The `enter_frame` interface is less likely to shift the pace of handler calling.

On the other hand, the `Timer` class's calling timing can be off if a CPU is busy.

## Basic usage

The `enter_frame` interface exists in classes, such as the `Stage` or `Sprite`.

The `enter_frame` interface requires the `handler` argument (callable object, such as the function or method).

The `fps` argument is optional and determines an animation's frame rate (it accepts the `FPS` enum).

Also, the `options` argument is an optional dictionary and passes optional parameters to a handler.

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


stage.enter_frame(handler=on_enter_frame, fps=ap.FPS.FPS_30)
ap.save_overall_html(dest_dir_path="enter_frame_basic_usage/")
```

<iframe src="static/enter_frame_basic_usage/index.html" width="150" height="150"></iframe>

## See also

- [Timer class](timer.md)
- [FPS enum](fps.md)

## enter_frame API

<!-- Docstring: apysc._event.enter_frame_mixin.EnterFrameMixIn.enter_frame -->

<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>

**[Interface signature]** `enter_frame(self, handler: Callable[[apysc._event.enter_frame_event.EnterFrameEvent, ~_Options], NoneType], *, fps: apysc._time.fps.FPS = <FPS.FPS_60: <apysc._time.fps.FPSDefinition object at 0x7fc849f025b0>>, options: Union[~_Options, NoneType] = None) -> None`<hr>

**[Interface summary]**

Add an enter frame event listener setting.<hr>

**[Parameters]**

- `handler`: Callable[[EnterFrameEvent, _Options], None]
  - A handler function to handle the enter frame event.
- `fps`: FPS, default FPS.FPS_60
  - Frame per second to set.
- `options`: Optional[_Options], optional
  - Optional arguments to pass to a handler function.

<hr>

**[Notes]**

If this is the second call of this interface and an argument is the same function, this interface ignores `options` argument (it changes only the running status and `fps` setting).<hr>

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
```