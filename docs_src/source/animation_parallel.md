# animation_parallel interface

This page explains the `animation_parallel` interface.

## What interface is this?

The `animation_parallel` method interface creates an `AnimationParallel` instance. You can set multiple simultaneous animations to the same instance with it.

This interface exists on a `DisplayObject` subclass instance, such as the `Sprite` or `Rectangle`.

## Basic usage

You can use this interface with the `animation_parallel` method. The `animations` list argument requires any animation settings.

The following example sets the simultaneous animations of the x, fill alpha, fill color, and line thickness.

```py
# runnable
import apysc as ap

ap.Stage(
    stage_width=400, stage_height=150, background_color='#333',
    stage_elem_id='stage')
sprite: ap.Sprite = ap.Sprite()
sprite.graphics.begin_fill(color='#0af')
sprite.graphics.line_style(color='#fff', thickness=3)

rectangle: ap.Rectangle = sprite.graphics.draw_rect(
    x=50, y=50, width=50, height=50)
rectangle.animation_parallel(
    animations=[
        rectangle.animation_x(x=300),
        rectangle.animation_fill_color(fill_color='#f0a'),
        rectangle.animation_fill_alpha(alpha=0.3),
        rectangle.animation_line_thickness(thickness=7),
    ],
    duration=3000, delay=3000, easing=ap.Easing.EASE_OUT_QUINT,
).start()

ap.save_overall_html(
    dest_dir_path='animation_parallel_basic_usage/')
```

<iframe src="static/animation_parallel_basic_usage/index.html" width="400" height="150"></iframe>

## Note for each animation's duration, delay, and easing setting

Animation settings of the `duration`\, `delay`\, and `easing` in the `animations` argument can't be changed since these animation settings are referring to the `animation_parallel` arguments. If you set these parameters in the `animations` arguments, setting raise an error:

```py
...
rectangle.animation_parallel(
    animations=[
        rectangle.animation_x(x=300, duration=1000),
    ],
    duration=3000, delay=2000, easing=ap.Easing.EASE_OUT_QUINT,
)
...
```

```
ValueError: There is an animation target that is changed duration setting: 1000
The duration setting of animation in the `animations` argument can not be changed.
Target animation type: <class 'apysc._animation.animation_x.AnimationX'>
```
