# AnimationBase class start interface

This page explains the `AnimationBase` class `start` method interface.

## What interface is this?

The `start` method interface starts the target animation. This interface returns the `AnimationBase` subclass instance is when you call each animation interface, such as the `animation_move` or `animation_x`\, and it has the `start` method.

## Basic usage

Notes: you need to call the `start` method to start an animation after the calling of the animation method, such as the `animation_x`\, as follows:

```py
# runnable
import apysc as ap

ap.Stage(
    stage_width=200, stage_height=150, background_color='#333',
    stage_elem_id='stage')
sprite: ap.Sprite = ap.Sprite()
sprite.graphics.begin_fill(color='#0af')
rectangle: ap.Rectangle = sprite.graphics.draw_rect(
    x=50, y=50, width=50, height=50)

animation_x: ap.AnimationX = rectangle.animation_x(
    x=100, duration=3000, delay=3000)
animation_x.start()

ap.save_overall_html(
    dest_dir_path='./animation_base_start_basic_usage_1/')
```

<iframe src="static/animation_base_start_basic_usage_1/index.html" width="200" height="150"></iframe>

You can also use the method chain for code simplicity:

```py
# runnable
import apysc as ap

ap.Stage(
    stage_width=200, stage_height=150, background_color='#333',
    stage_elem_id='stage')
sprite: ap.Sprite = ap.Sprite()
sprite.graphics.begin_fill(color='#0af')
rectangle: ap.Rectangle = sprite.graphics.draw_rect(
    x=50, y=50, width=50, height=50)

rectangle.animation_x(x=100, duration=3000, delay=3000).start()

ap.save_overall_html(
    dest_dir_path='./animation_base_start_basic_usage_2/')
```

<iframe src="static/animation_base_start_basic_usage_2/index.html" width="200" height="150"></iframe>