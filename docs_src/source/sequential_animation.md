# Sequential animation setting

This page explains how to animate sequentially.

## Sequential animation interface calling on the same instance

If you call each animation interface sequentially, these animations start in order (e.g., when the first animation completion, the second one starts).

The following example sets the four animations of the coordinates. These animations do not start simultaneously:

```py
# runnable
import apysc as ap

ap.Stage(
    stage_width=200, stage_height=200, background_color='#333',
    stage_elem_id='stage')
sprite: ap.Sprite = ap.Sprite()
sprite.graphics.begin_fill(color='#0af')

rectangle: ap.Rectangle = sprite.graphics.draw_rect(
    x=50, y=50, width=50, height=50)
easing: ap.Easing = ap.Easing.EASE_OUT_QUINT
rectangle.animation_x(x=100, duration=1000, delay=1000, easing=easing).start()
rectangle.animation_y(y=100, duration=1000, delay=1000, easing=easing).start()
rectangle.animation_x(x=50, duration=1000, delay=1000, easing=easing).start()
rectangle.animation_y(y=50, duration=1000, delay=1000, easing=easing).start()

ap.save_overall_html(
    dest_dir_path='sequential_animation_example_1/')
```

<iframe src="static/sequential_animation_example_1/index.html" width="200" height="200"></iframe>

## animation_complete handler setting

Also, you can use the `animation_complete` interface to register a handler for the sequence animation. For the details, please see [animation_complete interface document](animation_complete.md).

## See also

If you want to animate multiple animations simultaneously, you can use the [`animation_parallel` interface](animation_parallel.md).
