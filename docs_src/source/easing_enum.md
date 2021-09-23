# Easing enum

This page will explain the `Easing` enum class.

## What class is this?

The `Easing` enum class defines each easing function. These are used at the animation interfaces, for example, the `animation_move` interface.

## Basic usage

Each animation method interface, such as the `animation_move`, `animation_x`, has the `easing` argument and you can specify any of the `Easing.EASE_OUT_QUINT` enum, as follows:

```py
# runnable
import apysc as ap


def on_animation_complete_1(
        e: ap.AnimationEvent[ap.Rectangle],
        options: dict) -> None:
    """
    The handler will be called when the animation is complete.

    Parameters
    ----------
    e : ap.AnimationEvent
        Event instance.
    options : dict
        Optional arguments dictionary.
    """
    animation_move: ap.AnimationMove = e.this.target.animation_move(
        x=50, y=50, duration=1000, easing=ap.Easing.EASE_OUT_QUINT)
    animation_move.animation_complete(on_animation_complete_2)
    animation_move.start()


def on_animation_complete_2(
        e: ap.AnimationEvent[ap.Rectangle],
        options: dict) -> None:
    """
    The handler will be called when the animation is complete.

    Parameters
    ----------
    e : ap.AnimationEvent
        Event instance.
    options : dict
        Optional arguments dictionary.
    """
    animation_move: ap.AnimationMove = e.this.target.animation_move(
        x=100, y=100, duration=1000, easing=ap.Easing.EASE_OUT_QUINT)
    animation_move.animation_complete(on_animation_complete_1)
    animation_move.start()


stage: ap.Stage = ap.Stage(
    stage_width=200, stage_height=200, background_color='#333',
    stage_elem_id='stage')
sprite: ap.Sprite = ap.Sprite(stage=stage)
sprite.graphics.begin_fill(color='#0af')
rectangle: ap.Rectangle = sprite.graphics.draw_rect(
    x=50, y=50, width=50, height=50)

animation_move: ap.AnimationMove = rectangle.animation_move(
    x=100, y=100, duration=1000, easing=ap.Easing.EASE_OUT_QUINT)
animation_move.animation_complete(on_animation_complete_1)
animation_move.start()

ap.save_overall_html(
    dest_dir_path='./easing_enum_basic_usage/')
```

<iframe src="static/easing_enum_basic_usage/index.html" width="200" height="200"></iframe>

## What difference between the ease-in, ease-out, and ease-in-out

- Ease-in will start with slow speed, and stop with fast speed.
- Ease-out will start with fast speed, and stop with slow speed.
- Ease-in-out will start and stop with slow speed, and it gets faster on the way.

The following example will show the difference between the `EASE_IN_QUINT`, `EASE_OUT_QUINT`, and `EASE_IN_OUT_QUINT`.

<!--
# runnable
from typing_extensions import TypedDict

import apysc as ap


class _EasingOptions(TypedDict):
    easing: ap.Easing


DURATION: int = 1000
EASING_1: ap.Easing = ap.Easing.EASE_IN_QUINT
EASING_2: ap.Easing = ap.Easing.EASE_OUT_QUINT
EASING_3: ap.Easing = ap.Easing.EASE_IN_OUT_QUINT


def on_animation_complete_1(
        e: ap.AnimationEvent[ap.Rectangle],
        options: _EasingOptions) -> None:
    """
    The handler will be called when the animation is complete.

    Parameters
    ----------
    e : ap.AnimationEvent
        Event instance.
    options : dict
        Optional arguments dictionary.
    """
    animation_x: ap.AnimationX = e.this.target.animation_x(
        x=50, duration=DURATION, easing=options['easing'])
    animation_x.animation_complete(on_animation_complete_2, options=options)
    animation_x.start()


def on_animation_complete_2(
        e: ap.AnimationEvent[ap.Rectangle],
        options: _EasingOptions) -> None:
    """
    The handler will be called when the animation is complete.

    Parameters
    ----------
    e : ap.AnimationEvent
        Event instance.
    options : dict
        Optional arguments dictionary.
    """
    animation_x: ap.AnimationX = e.this.target.animation_x(
        x=100, duration=DURATION, easing=options['easing'])
    animation_x.animation_complete(
        on_animation_complete_1, options=options)
    animation_x.start()


stage: ap.Stage = ap.Stage(
    stage_width=200, stage_height=350, background_color='#333',
    stage_elem_id='stage')
sprite: ap.Sprite = ap.Sprite(stage=stage)
sprite.graphics.begin_fill(color='#0af')
rectangle_1: ap.Rectangle = sprite.graphics.draw_rect(
    x=50, y=50, width=50, height=50)
rectangle_2: ap.Rectangle = sprite.graphics.draw_rect(
    x=50, y=150, width=50, height=50)
rectangle_3: ap.Rectangle = sprite.graphics.draw_rect(
    x=50, y=250, width=50, height=50)

x: int = 100
animation_x: ap.AnimationX = rectangle_1.animation_x(
    x=x, duration=DURATION, easing=EASING_1)
options: _EasingOptions = {'easing': EASING_1}
animation_x.animation_complete(on_animation_complete_1, options=options)
animation_x.start()

animation_x = rectangle_2.animation_x(
    x=x, duration=DURATION, easing=EASING_2)
options = {'easing': EASING_2}
animation_x.animation_complete(on_animation_complete_1, options=options)
animation_x.start()

animation_x = rectangle_3.animation_x(
    x=x, duration=DURATION, easing=EASING_3)
options = {'easing': EASING_3}
animation_x.animation_complete(on_animation_complete_1, options=options)
animation_x.start()

ap.save_overall_html(
    dest_dir_path='./easing_enum_ease_difference/')
-->

<iframe src="static/easing_enum_ease_difference/index.html" width="200" height="350"></iframe>

## Ease-in examples

This section will show each ease-in setting result with the x-coordinate animation.

The following is the example of the `EASE_IN_SINE`, `EASE_IN_QUAD`, and `EASE_IN_CUBIC`:

<!--
```py
# runnable
from typing_extensions import TypedDict

import apysc as ap


class _EasingOptions(TypedDict):
    easing: ap.Easing


DURATION: int = 1000
EASING_1: ap.Easing = ap.Easing.EASE_IN_SINE
EASING_2: ap.Easing = ap.Easing.EASE_IN_QUAD
EASING_3: ap.Easing = ap.Easing.EASE_IN_CUBIC


def on_animation_complete_1(
        e: ap.AnimationEvent[ap.Rectangle],
        options: _EasingOptions) -> None:
    """
    The handler will be called when the animation is complete.

    Parameters
    ----------
    e : ap.AnimationEvent
        Event instance.
    options : dict
        Optional arguments dictionary.
    """
    animation_x: ap.AnimationX = e.this.target.animation_x(
        x=50, duration=DURATION, easing=options['easing'])
    animation_x.animation_complete(on_animation_complete_2, options=options)
    animation_x.start()


def on_animation_complete_2(
        e: ap.AnimationEvent[ap.Rectangle],
        options: _EasingOptions) -> None:
    """
    The handler will be called when the animation is complete.

    Parameters
    ----------
    e : ap.AnimationEvent
        Event instance.
    options : dict
        Optional arguments dictionary.
    """
    animation_x: ap.AnimationX = e.this.target.animation_x(
        x=100, duration=DURATION, easing=options['easing'])
    animation_x.animation_complete(
        on_animation_complete_1, options=options)
    animation_x.start()


stage: ap.Stage = ap.Stage(
    stage_width=200, stage_height=350, background_color='#333',
    stage_elem_id='stage')
sprite: ap.Sprite = ap.Sprite(stage=stage)
sprite.graphics.begin_fill(color='#0af')
rectangle_1: ap.Rectangle = sprite.graphics.draw_rect(
    x=50, y=50, width=50, height=50)
rectangle_2: ap.Rectangle = sprite.graphics.draw_rect(
    x=50, y=150, width=50, height=50)
rectangle_3: ap.Rectangle = sprite.graphics.draw_rect(
    x=50, y=250, width=50, height=50)

x: int = 100
animation_x: ap.AnimationX = rectangle_1.animation_x(
    x=x, duration=DURATION, easing=EASING_1)
options: _EasingOptions = {'easing': EASING_1}
animation_x.animation_complete(on_animation_complete_1, options=options)
animation_x.start()

animation_x = rectangle_2.animation_x(
    x=x, duration=DURATION, easing=EASING_2)
options = {'easing': EASING_2}
animation_x.animation_complete(on_animation_complete_1, options=options)
animation_x.start()

animation_x = rectangle_3.animation_x(
    x=x, duration=DURATION, easing=EASING_3)
options = {'easing': EASING_3}
animation_x.animation_complete(on_animation_complete_1, options=options)
animation_x.start()

ap.save_overall_html(
    dest_dir_path='./easing_enum_ease_in_1/')
```
-->

<iframe src="static/easing_enum_ease_in_1/index.html" width="200" height="350"></iframe>

The following is the example of the `EASE_IN_QUART`, `EASE_IN_QUINT`, and `EASE_IN_EXPO`:

<!--
```py
# runnable
from typing_extensions import TypedDict

import apysc as ap


class _EasingOptions(TypedDict):
    easing: ap.Easing


DURATION: int = 1000
EASING_1: ap.Easing = ap.Easing.EASE_IN_QUART
EASING_2: ap.Easing = ap.Easing.EASE_IN_QUINT
EASING_3: ap.Easing = ap.Easing.EASE_IN_EXPO


def on_animation_complete_1(
        e: ap.AnimationEvent[ap.Rectangle],
        options: _EasingOptions) -> None:
    """
    The handler will be called when the animation is complete.

    Parameters
    ----------
    e : ap.AnimationEvent
        Event instance.
    options : dict
        Optional arguments dictionary.
    """
    animation_x: ap.AnimationX = e.this.target.animation_x(
        x=50, duration=DURATION, easing=options['easing'])
    animation_x.animation_complete(on_animation_complete_2, options=options)
    animation_x.start()


def on_animation_complete_2(
        e: ap.AnimationEvent[ap.Rectangle],
        options: _EasingOptions) -> None:
    """
    The handler will be called when the animation is complete.

    Parameters
    ----------
    e : ap.AnimationEvent
        Event instance.
    options : dict
        Optional arguments dictionary.
    """
    animation_x: ap.AnimationX = e.this.target.animation_x(
        x=100, duration=DURATION, easing=options['easing'])
    animation_x.animation_complete(
        on_animation_complete_1, options=options)
    animation_x.start()


stage: ap.Stage = ap.Stage(
    stage_width=200, stage_height=350, background_color='#333',
    stage_elem_id='stage')
sprite: ap.Sprite = ap.Sprite(stage=stage)
sprite.graphics.begin_fill(color='#0af')
rectangle_1: ap.Rectangle = sprite.graphics.draw_rect(
    x=50, y=50, width=50, height=50)
rectangle_2: ap.Rectangle = sprite.graphics.draw_rect(
    x=50, y=150, width=50, height=50)
rectangle_3: ap.Rectangle = sprite.graphics.draw_rect(
    x=50, y=250, width=50, height=50)

x: int = 100
animation_x: ap.AnimationX = rectangle_1.animation_x(
    x=x, duration=DURATION, easing=EASING_1)
options: _EasingOptions = {'easing': EASING_1}
animation_x.animation_complete(on_animation_complete_1, options=options)
animation_x.start()

animation_x = rectangle_2.animation_x(
    x=x, duration=DURATION, easing=EASING_2)
options = {'easing': EASING_2}
animation_x.animation_complete(on_animation_complete_1, options=options)
animation_x.start()

animation_x = rectangle_3.animation_x(
    x=x, duration=DURATION, easing=EASING_3)
options = {'easing': EASING_3}
animation_x.animation_complete(on_animation_complete_1, options=options)
animation_x.start()

ap.save_overall_html(
    dest_dir_path='./easing_enum_ease_in_2/')
```
-->

<iframe src="static/easing_enum_ease_in_2/index.html" width="200" height="350"></iframe>

The following is the example of the `EASE_IN_CIRC` and `EASE_IN_BACK`:

<!--
```py
# runnable
from typing_extensions import TypedDict

import apysc as ap


class _EasingOptions(TypedDict):
    easing: ap.Easing


DURATION: int = 1000
EASING_1: ap.Easing = ap.Easing.EASE_IN_CIRC
EASING_2: ap.Easing = ap.Easing.EASE_IN_BACK


def on_animation_complete_1(
        e: ap.AnimationEvent[ap.Rectangle],
        options: _EasingOptions) -> None:
    """
    The handler will be called when the animation is complete.

    Parameters
    ----------
    e : ap.AnimationEvent
        Event instance.
    options : dict
        Optional arguments dictionary.
    """
    animation_x: ap.AnimationX = e.this.target.animation_x(
        x=50, duration=DURATION, easing=options['easing'])
    animation_x.animation_complete(on_animation_complete_2, options=options)
    animation_x.start()


def on_animation_complete_2(
        e: ap.AnimationEvent[ap.Rectangle],
        options: _EasingOptions) -> None:
    """
    The handler will be called when the animation is complete.

    Parameters
    ----------
    e : ap.AnimationEvent
        Event instance.
    options : dict
        Optional arguments dictionary.
    """
    animation_x: ap.AnimationX = e.this.target.animation_x(
        x=100, duration=DURATION, easing=options['easing'])
    animation_x.animation_complete(
        on_animation_complete_1, options=options)
    animation_x.start()


stage: ap.Stage = ap.Stage(
    stage_width=200, stage_height=250, background_color='#333',
    stage_elem_id='stage')
sprite: ap.Sprite = ap.Sprite(stage=stage)
sprite.graphics.begin_fill(color='#0af')
rectangle_1: ap.Rectangle = sprite.graphics.draw_rect(
    x=50, y=50, width=50, height=50)
rectangle_2: ap.Rectangle = sprite.graphics.draw_rect(
    x=50, y=150, width=50, height=50)
rectangle_3: ap.Rectangle = sprite.graphics.draw_rect(
    x=50, y=250, width=50, height=50)

x: int = 100
animation_x: ap.AnimationX = rectangle_1.animation_x(
    x=x, duration=DURATION, easing=EASING_1)
options: _EasingOptions = {'easing': EASING_1}
animation_x.animation_complete(on_animation_complete_1, options=options)
animation_x.start()

animation_x = rectangle_2.animation_x(
    x=x, duration=DURATION, easing=EASING_2)
options = {'easing': EASING_2}
animation_x.animation_complete(on_animation_complete_1, options=options)
animation_x.start()

ap.save_overall_html(
    dest_dir_path='./easing_enum_ease_in_3/')
```
-->

<iframe src="static/easing_enum_ease_in_3/index.html" width="200" height="250"></iframe>

The following is the example of the `EASE_IN_ELASTIC` and `EASE_IN_BOUNCE`:

<!--
```py
# runnable
from typing_extensions import TypedDict

import apysc as ap


class _EasingOptions(TypedDict):
    easing: ap.Easing


DURATION: int = 1000
EASING_1: ap.Easing = ap.Easing.EASE_IN_ELASTIC
EASING_2: ap.Easing = ap.Easing.EASE_IN_BOUNCE


def on_animation_complete_1(
        e: ap.AnimationEvent[ap.Rectangle],
        options: _EasingOptions) -> None:
    """
    The handler will be called when the animation is complete.

    Parameters
    ----------
    e : ap.AnimationEvent
        Event instance.
    options : dict
        Optional arguments dictionary.
    """
    animation_x: ap.AnimationX = e.this.target.animation_x(
        x=50, duration=DURATION, easing=options['easing'])
    animation_x.animation_complete(on_animation_complete_2, options=options)
    animation_x.start()


def on_animation_complete_2(
        e: ap.AnimationEvent[ap.Rectangle],
        options: _EasingOptions) -> None:
    """
    The handler will be called when the animation is complete.

    Parameters
    ----------
    e : ap.AnimationEvent
        Event instance.
    options : dict
        Optional arguments dictionary.
    """
    animation_x: ap.AnimationX = e.this.target.animation_x(
        x=100, duration=DURATION, easing=options['easing'])
    animation_x.animation_complete(
        on_animation_complete_1, options=options)
    animation_x.start()


stage: ap.Stage = ap.Stage(
    stage_width=200, stage_height=250, background_color='#333',
    stage_elem_id='stage')
sprite: ap.Sprite = ap.Sprite(stage=stage)
sprite.graphics.begin_fill(color='#0af')
rectangle_1: ap.Rectangle = sprite.graphics.draw_rect(
    x=50, y=50, width=50, height=50)
rectangle_2: ap.Rectangle = sprite.graphics.draw_rect(
    x=50, y=150, width=50, height=50)
rectangle_3: ap.Rectangle = sprite.graphics.draw_rect(
    x=50, y=250, width=50, height=50)

x: int = 100
animation_x: ap.AnimationX = rectangle_1.animation_x(
    x=x, duration=DURATION, easing=EASING_1)
options: _EasingOptions = {'easing': EASING_1}
animation_x.animation_complete(on_animation_complete_1, options=options)
animation_x.start()

animation_x = rectangle_2.animation_x(
    x=x, duration=DURATION, easing=EASING_2)
options = {'easing': EASING_2}
animation_x.animation_complete(on_animation_complete_1, options=options)
animation_x.start()

ap.save_overall_html(
    dest_dir_path='./easing_enum_ease_in_4/')
```
-->

<iframe src="static/easing_enum_ease_in_4/index.html" width="200" height="250"></iframe>

## Ease-out examples

This section will show each ease-out result with the x-coordinate animation.

The following is the example of the `EASE_OUT_SINE`, `EASE_OUT_QUAD`, and `EASE_OUT_CUBIC`:

<!--
```py
# runnable
from typing_extensions import TypedDict

import apysc as ap


class _EasingOptions(TypedDict):
    easing: ap.Easing


DURATION: int = 1000
EASING_1: ap.Easing = ap.Easing.EASE_OUT_SINE
EASING_2: ap.Easing = ap.Easing.EASE_OUT_QUAD
EASING_3: ap.Easing = ap.Easing.EASE_OUT_CUBIC


def on_animation_complete_1(
        e: ap.AnimationEvent[ap.Rectangle],
        options: _EasingOptions) -> None:
    """
    The handler will be called when the animation is complete.

    Parameters
    ----------
    e : ap.AnimationEvent
        Event instance.
    options : dict
        Optional arguments dictionary.
    """
    animation_x: ap.AnimationX = e.this.target.animation_x(
        x=50, duration=DURATION, easing=options['easing'])
    animation_x.animation_complete(on_animation_complete_2, options=options)
    animation_x.start()


def on_animation_complete_2(
        e: ap.AnimationEvent[ap.Rectangle],
        options: _EasingOptions) -> None:
    """
    The handler will be called when the animation is complete.

    Parameters
    ----------
    e : ap.AnimationEvent
        Event instance.
    options : dict
        Optional arguments dictionary.
    """
    animation_x: ap.AnimationX = e.this.target.animation_x(
        x=100, duration=DURATION, easing=options['easing'])
    animation_x.animation_complete(
        on_animation_complete_1, options=options)
    animation_x.start()


stage: ap.Stage = ap.Stage(
    stage_width=200, stage_height=350, background_color='#333',
    stage_elem_id='stage')
sprite: ap.Sprite = ap.Sprite(stage=stage)
sprite.graphics.begin_fill(color='#0af')
rectangle_1: ap.Rectangle = sprite.graphics.draw_rect(
    x=50, y=50, width=50, height=50)
rectangle_2: ap.Rectangle = sprite.graphics.draw_rect(
    x=50, y=150, width=50, height=50)
rectangle_3: ap.Rectangle = sprite.graphics.draw_rect(
    x=50, y=250, width=50, height=50)

x: int = 100
animation_x: ap.AnimationX = rectangle_1.animation_x(
    x=x, duration=DURATION, easing=EASING_1)
options: _EasingOptions = {'easing': EASING_1}
animation_x.animation_complete(on_animation_complete_1, options=options)
animation_x.start()

animation_x = rectangle_2.animation_x(
    x=x, duration=DURATION, easing=EASING_2)
options = {'easing': EASING_2}
animation_x.animation_complete(on_animation_complete_1, options=options)
animation_x.start()

animation_x = rectangle_3.animation_x(
    x=x, duration=DURATION, easing=EASING_3)
options = {'easing': EASING_3}
animation_x.animation_complete(on_animation_complete_1, options=options)
animation_x.start()

ap.save_overall_html(
    dest_dir_path='./easing_enum_ease_out_1/')
```
-->

<iframe src="static/easing_enum_ease_out_1/index.html" width="200" height="350"></iframe>

The following is the example of the `EASE_OUT_QUART`, `EASE_OUT_QUINT`, and `EASE_OUT_EXPO`:

<!--
```py
# runnable
from typing_extensions import TypedDict

import apysc as ap


class _EasingOptions(TypedDict):
    easing: ap.Easing


DURATION: int = 1000
EASING_1: ap.Easing = ap.Easing.EASE_OUT_QUART
EASING_2: ap.Easing = ap.Easing.EASE_OUT_QUINT
EASING_3: ap.Easing = ap.Easing.EASE_OUT_EXPO


def on_animation_complete_1(
        e: ap.AnimationEvent[ap.Rectangle],
        options: _EasingOptions) -> None:
    """
    The handler will be called when the animation is complete.

    Parameters
    ----------
    e : ap.AnimationEvent
        Event instance.
    options : dict
        Optional arguments dictionary.
    """
    animation_x: ap.AnimationX = e.this.target.animation_x(
        x=50, duration=DURATION, easing=options['easing'])
    animation_x.animation_complete(on_animation_complete_2, options=options)
    animation_x.start()


def on_animation_complete_2(
        e: ap.AnimationEvent[ap.Rectangle],
        options: _EasingOptions) -> None:
    """
    The handler will be called when the animation is complete.

    Parameters
    ----------
    e : ap.AnimationEvent
        Event instance.
    options : dict
        Optional arguments dictionary.
    """
    animation_x: ap.AnimationX = e.this.target.animation_x(
        x=100, duration=DURATION, easing=options['easing'])
    animation_x.animation_complete(
        on_animation_complete_1, options=options)
    animation_x.start()


stage: ap.Stage = ap.Stage(
    stage_width=200, stage_height=350, background_color='#333',
    stage_elem_id='stage')
sprite: ap.Sprite = ap.Sprite(stage=stage)
sprite.graphics.begin_fill(color='#0af')
rectangle_1: ap.Rectangle = sprite.graphics.draw_rect(
    x=50, y=50, width=50, height=50)
rectangle_2: ap.Rectangle = sprite.graphics.draw_rect(
    x=50, y=150, width=50, height=50)
rectangle_3: ap.Rectangle = sprite.graphics.draw_rect(
    x=50, y=250, width=50, height=50)

x: int = 100
animation_x: ap.AnimationX = rectangle_1.animation_x(
    x=x, duration=DURATION, easing=EASING_1)
options: _EasingOptions = {'easing': EASING_1}
animation_x.animation_complete(on_animation_complete_1, options=options)
animation_x.start()

animation_x = rectangle_2.animation_x(
    x=x, duration=DURATION, easing=EASING_2)
options = {'easing': EASING_2}
animation_x.animation_complete(on_animation_complete_1, options=options)
animation_x.start()

animation_x = rectangle_3.animation_x(
    x=x, duration=DURATION, easing=EASING_3)
options = {'easing': EASING_3}
animation_x.animation_complete(on_animation_complete_1, options=options)
animation_x.start()

ap.save_overall_html(
    dest_dir_path='./easing_enum_ease_out_2/')
```
-->

<iframe src="static/easing_enum_ease_out_2/index.html" width="200" height="350"></iframe>

The following is the example of the `EASE_OUT_CIRC` and `EASE_OUT_BACK`:

<!--
```py
# runnable
from typing_extensions import TypedDict

import apysc as ap


class _EasingOptions(TypedDict):
    easing: ap.Easing


DURATION: int = 1000
EASING_1: ap.Easing = ap.Easing.EASE_OUT_CIRC
EASING_2: ap.Easing = ap.Easing.EASE_OUT_BACK


def on_animation_complete_1(
        e: ap.AnimationEvent[ap.Rectangle],
        options: _EasingOptions) -> None:
    """
    The handler will be called when the animation is complete.

    Parameters
    ----------
    e : ap.AnimationEvent
        Event instance.
    options : dict
        Optional arguments dictionary.
    """
    animation_x: ap.AnimationX = e.this.target.animation_x(
        x=50, duration=DURATION, easing=options['easing'])
    animation_x.animation_complete(on_animation_complete_2, options=options)
    animation_x.start()


def on_animation_complete_2(
        e: ap.AnimationEvent[ap.Rectangle],
        options: _EasingOptions) -> None:
    """
    The handler will be called when the animation is complete.

    Parameters
    ----------
    e : ap.AnimationEvent
        Event instance.
    options : dict
        Optional arguments dictionary.
    """
    animation_x: ap.AnimationX = e.this.target.animation_x(
        x=100, duration=DURATION, easing=options['easing'])
    animation_x.animation_complete(
        on_animation_complete_1, options=options)
    animation_x.start()


stage: ap.Stage = ap.Stage(
    stage_width=200, stage_height=250, background_color='#333',
    stage_elem_id='stage')
sprite: ap.Sprite = ap.Sprite(stage=stage)
sprite.graphics.begin_fill(color='#0af')
rectangle_1: ap.Rectangle = sprite.graphics.draw_rect(
    x=50, y=50, width=50, height=50)
rectangle_2: ap.Rectangle = sprite.graphics.draw_rect(
    x=50, y=150, width=50, height=50)
rectangle_3: ap.Rectangle = sprite.graphics.draw_rect(
    x=50, y=250, width=50, height=50)

x: int = 100
animation_x: ap.AnimationX = rectangle_1.animation_x(
    x=x, duration=DURATION, easing=EASING_1)
options: _EasingOptions = {'easing': EASING_1}
animation_x.animation_complete(on_animation_complete_1, options=options)
animation_x.start()

animation_x = rectangle_2.animation_x(
    x=x, duration=DURATION, easing=EASING_2)
options = {'easing': EASING_2}
animation_x.animation_complete(on_animation_complete_1, options=options)
animation_x.start()

ap.save_overall_html(
    dest_dir_path='./easing_enum_ease_out_3/')
```
-->

<iframe src="static/easing_enum_ease_out_3/index.html" width="200" height="250"></iframe>

The following is the example of the `EASE_OUT_ELASTIC` and `EASE_OUT_BOUNCE`:

<!--
```py
# runnable
from typing_extensions import TypedDict

import apysc as ap


class _EasingOptions(TypedDict):
    easing: ap.Easing


DURATION: int = 1000
EASING_1: ap.Easing = ap.Easing.EASE_OUT_ELASTIC
EASING_2: ap.Easing = ap.Easing.EASE_OUT_BOUNCE


def on_animation_complete_1(
        e: ap.AnimationEvent[ap.Rectangle],
        options: _EasingOptions) -> None:
    """
    The handler will be called when the animation is complete.

    Parameters
    ----------
    e : ap.AnimationEvent
        Event instance.
    options : dict
        Optional arguments dictionary.
    """
    animation_x: ap.AnimationX = e.this.target.animation_x(
        x=50, duration=DURATION, easing=options['easing'])
    animation_x.animation_complete(on_animation_complete_2, options=options)
    animation_x.start()


def on_animation_complete_2(
        e: ap.AnimationEvent[ap.Rectangle],
        options: _EasingOptions) -> None:
    """
    The handler will be called when the animation is complete.

    Parameters
    ----------
    e : ap.AnimationEvent
        Event instance.
    options : dict
        Optional arguments dictionary.
    """
    animation_x: ap.AnimationX = e.this.target.animation_x(
        x=100, duration=DURATION, easing=options['easing'])
    animation_x.animation_complete(
        on_animation_complete_1, options=options)
    animation_x.start()


stage: ap.Stage = ap.Stage(
    stage_width=200, stage_height=250, background_color='#333',
    stage_elem_id='stage')
sprite: ap.Sprite = ap.Sprite(stage=stage)
sprite.graphics.begin_fill(color='#0af')
rectangle_1: ap.Rectangle = sprite.graphics.draw_rect(
    x=50, y=50, width=50, height=50)
rectangle_2: ap.Rectangle = sprite.graphics.draw_rect(
    x=50, y=150, width=50, height=50)
rectangle_3: ap.Rectangle = sprite.graphics.draw_rect(
    x=50, y=250, width=50, height=50)

x: int = 100
animation_x: ap.AnimationX = rectangle_1.animation_x(
    x=x, duration=DURATION, easing=EASING_1)
options: _EasingOptions = {'easing': EASING_1}
animation_x.animation_complete(on_animation_complete_1, options=options)
animation_x.start()

animation_x = rectangle_2.animation_x(
    x=x, duration=DURATION, easing=EASING_2)
options = {'easing': EASING_2}
animation_x.animation_complete(on_animation_complete_1, options=options)
animation_x.start()

ap.save_overall_html(
    dest_dir_path='./easing_enum_ease_out_4/')
```
-->

<iframe src="static/easing_enum_ease_out_4/index.html" width="200" height="250"></iframe>

## Ease-in-out examples
