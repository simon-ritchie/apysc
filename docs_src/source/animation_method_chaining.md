# AnimationBase class interfaces method chaining

This page describes the method chaining of the animation interfaces.

## Each AnimationBase related interface returns its instance

Each `AnimationBase` class-related interface (such as the `animation_x`\, `start`\, `animation_complete`) returns its instance. So that these interfaces can be used with the method chaining, as follows (method chaining of the `animation_x`\, `animation_complete`\, and `start` methods):

```py
# runnable
import apysc as ap


def on_animation_complete(
        e: ap.AnimationEvent[ap.Rectangle], options: dict) -> None:
    """
    The handler that the animation calls when its end.

    Parameters
    ----------
    e : AnimationEvent
        Event instance.
    options : dict
        Optional arguments dictionary.
    """
    ap.trace('Animation is completed!')


ap.Stage(
    stage_width=200, stage_height=150,
    background_color='#333', stage_elem_id='stage')
sprite: ap.Sprite = ap.Sprite()
sprite.graphics.begin_fill(color='#00aaff')
rectangle: ap.Rectangle = sprite.graphics.draw_rect(
    x=50, y=50, width=50, height=50)
rectangle.animation_x(
    x=100,
    duration=1000,
).animation_complete(on_animation_complete).start()

ap.save_overall_html(
    dest_dir_path='./animation_method_chaining_basic_usage_1/')
```

<iframe src="static/animation_method_chaining_basic_usage_1/index.html" width="200" height=150></iframe>

These method chainings are sometimes useful for code simplicity.

If you want to chain the methods like JavaScript (e.g., `D3.js`), you can use backslashes at the line end, as follows:

```py
# runnable
import apysc as ap


def on_animation_complete(
        e: ap.AnimationEvent[ap.Rectangle], options: dict) -> None:
    """
    The handler that the animation calls when its end.

    Parameters
    ----------
    e : AnimationEvent
        Event instance.
    options : dict
        Optional arguments dictionary.
    """
    ap.trace('Animation is completed!')


ap.Stage(
    stage_width=200, stage_height=150,
    background_color='#333', stage_elem_id='stage')
sprite: ap.Sprite = ap.Sprite()
sprite.graphics.begin_fill(color='#00aaff')
rectangle: ap.Rectangle = sprite.graphics.draw_rect(
    x=50, y=50, width=50, height=50)
rectangle\
    .animation_x(x=100, duration=1000)\
    .animation_complete(on_animation_complete)\
    .start()

ap.save_overall_html(
    dest_dir_path='./animation_method_chaining_basic_usage_2/')
```

<iframe src="static/animation_method_chaining_basic_usage_2/index.html" width="200" height=150></iframe>
