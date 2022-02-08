# apysc._display.graphics_expression docstrings

## Module summary

Graphics class related expression implementations.

## append_fill_expression function docstring

Append fill expression to specified expression's string.<hr>

**[Parameters]**

- `graphics`: Graphics
  - Target Graphics instance.
- `expression`: str
  - Expression string to be appended fill expression.
- `indent_num`: int
  - Indentation number.

<hr>

**[Returns]**

- `expression`: str
  - After appended expression string.

## append_fill_opacity_expression function docstring

Append fill opacity expression to specified expression's string.<hr>

**[Parameters]**

- `graphics`: Graphics
  - Target Graphics instance.
- `expression`: str
  - Expression string to be appended fill opacity expression.
- `indent_num`: int
  - Indentation number.

<hr>

**[Returns]**

- `expression`: str
  - After appended expression string.

## append_stroke_expression function docstring

Append stroke expression to specified expression's string.<hr>

**[Parameters]**

- `graphics`: Graphics
  - Target Graphics instance.
- `expression`: str
  - Expression string to be appended stroke expression.
- `indent_num`: int
  - Indentation number.

<hr>

**[Returns]**

- `expression`: str
  - After appended expression string.

## append_stroke_linecap_expression function docstring

Append stroke linecap expression to specified expression's string.<hr>

**[Parameters]**

- `graphics`: Graphics
  - Target Graphics instance.
- `expression`: str
  - Expression string to be appended stroke linecap expression.
- `indent_num`: int
  - Indentation number.

<hr>

**[Returns]**

- `expression`: str
  - After appended expression string.

## append_stroke_linejoin_expression function docstring

Append stroke linejoin expression to specified expression's string.<hr>

**[Parameters]**

- `graphics`: Graphics
  - Target Graphics instance.
- `expression`: str
  - Expression string to be appended stroke linejoin expression.
- `indent_num`: int
  - Indentation number.

<hr>

**[Returns]**

- `expression`: str
  - After appended expression string.

## append_stroke_opacity_expression function docstring

Append stroke opacity expression to specified expression's string.<hr>

**[Parameters]**

- `graphics`: Graphics
  - Target Graphics instance.
- `expression`: str
  - Expression string to be appended stroke opacity expression.
- `indent_num`: int
  - Indentation number.

<hr>

**[Returns]**

- `expression`: str
  - After appended expression string.

## append_stroke_width_expression function docstring

Append stroke width expression to specified expression's string.<hr>

**[Parameters]**

- `graphics`: Graphics
  - Target Graphics instance.
- `expression`: str
  - Expression string to be appended stroke width expression.
- `indent_num`: int
  - Indentation number.

<hr>

**[Returns]**

- `expression`: str
  - After appended expression string.

## append_x_expression function docstring

Append x position expression to specified expression's string.<hr>

**[Parameters]**

- `graphic`: GraphicsBase
  - Target graphic instance, for example, Rectangle.
- `expression`: str
  - Expression string to be appended x position expression.
- `indent_num`: int
  - Indentation number.

<hr>

**[Returns]**

- `expression`: str
  - After appended expression string.

## append_y_expression function docstring

Append y position expression to specified expression's string.<hr>

**[Parameters]**

- `graphic`: GraphicsBase
  - Target graphic instance, for example, Rectangle.
- `expression`: str
  - Expression string to be appended y position expression.
- `indent_num`: int
  - Indentation number.

<hr>

**[Returns]**

- `expression`: str
  - After appended expression string.

## Graphics class docstring

Create a object that has each vector graphics interface.

Create a object that has each vector graphics interface.<hr>

**[Examples]**

```py
>>> import apysc as ap
>>> stage: ap.Stage = ap.Stage()
>>> sprite: ap.Sprite = ap.Sprite()
>>> sprite.graphics.begin_fill(color='#0af')
>>> rectangle: ap.Rectangle = sprite.graphics.draw_rect(
...     x=50, y=50, width=50, height=50)
>>> rectangle.x
Int(50)

>>> circle: ap.Circle = sprite.graphics.draw_circle(
...     x=100, y=100, radius=50)
>>> circle.x
Int(100)
```

<hr>

**[References]**

- [Graphics document](https://simon-ritchie.github.io/apysc/graphics.html)

### ABCMeta method docstring

Metaclass for defining Abstract Base Classes (ABCs). Use this metaclass to create an ABC. An ABC can be subclassed directly, and then acts as a mix-in class. You can also register unrelated concrete classes (even built-in classes) and unrelated ABCs as 'virtual subclasses' -- these and their descendants will be considered subclasses of the registering ABC by the built-in issubclass() function, but the registering ABC won't show up in their MRO (Method Resolution Order) nor will method implementations defined by the registering ABC be callable (not even via super()).

### __init__ method docstring

Create a object that has each vector graphics interface.<hr>

**[Parameters]**

- `parent`: Sprite
  - This instance's parent instance.
- `variable_name`: str or None, default None
  - Variable name to set. Specified only when subclass instantiation.

<hr>

**[References]**

- [Graphics document](https://simon-ritchie.github.io/apysc/graphics.html)

### __repr__ method docstring

Get a string representation of this instance (for the sake of debugging).<hr>

**[Returns]**

- `repr_str`: str
  - Type name and variable name will be set (e.g., `Graphics('<variable_name>')`).

### _append_applying_new_attr_val_exp method docstring

Append the expression of applying new attribute value to each stacked value.<hr>

**[Parameters]**

- `new_attr`: Int or Number or String or Boolean
  - New attribute value.
- `attr_name`: str
  - Target attribute name.

### _append_attr_to_linking_stack method docstring

Append an attribute to the linking attribute stack.<hr>

**[Parameters]**

- `attr`: Int or Number or String or Boolean
  - Target attribute to be appended.
- `attr_name`: str
  - Target attribute name.

### _append_constructor_expression method docstring

Append constructor expression.

### _append_contains_expression method docstring

Append contains method expression.<hr>

**[Parameters]**

- `result`: Boolean
  - Result boolean value.
- `child`: DisplayObject
  - Child instance to check.

### _append_custom_event_binding_expression method docstring

Append a custom event binding expression.<hr>

**[Parameters]**

- `custom_event_type_str`: str
  - Target custom event type string.
- `name`: str
  - Handler's name.

### _append_custom_event_unbinding_expression method docstring

Add a custom event unbinding expression.<hr>

**[Parameters]**

- `custom_event_type_str`: str
  - Target custom event type string.
- `name`: str
  - Handler's name.

### _append_get_child_at_expression method docstring

Append get_child_at method expression.<hr>

**[Parameters]**

- `child`: DisplayObject
  - Target index child instance.
- `index`: int or Int
  - Child's index (start from 0).

### _append_get_css_expresion method docstring

Append a css getter expression string.<hr>

**[Parameters]**

- `name`: str or String
  - CSS name (e.g., 'display').
- `css`: String
  - CSS value.

### _append_mouse_event_binding_expression method docstring

Append a mouse event binding expression.<hr>

**[Parameters]**

- `name`: str
  - Handler's name.
- `mouse_event_type`: MouseEventType
  - Event type to bind.

### _append_num_children_expression method docstring

Append num_children method expression.<hr>

**[Parameters]**

- `num_children`: Int
  - Current children number.

### _append_set_css_expression method docstring

Append a css setter expression string.<hr>

**[Parameters]**

- `name`: str or String
  - CSS name (e.g., 'display').
- `value`: str or String
  - A CSS value string (e.g., 'none').

### _append_visible_attr_linking_setting method docstring

Append a visible attribute linking setting.

### _append_visible_update_expression method docstring

Append visible property updating expression.

### _append_x_attr_linking_setting method docstring

Append a x attribute linking setting.

### _append_x_update_expression method docstring

Append the x position updating expression.

### _append_y_attr_linking_setting method docstring

Append a y attribute linking setting.

### _append_y_update_expression method docstring

Append y position updating expression.

### _delete_snapshot_exists_val method docstring

Delete boolean value whether snapshot value exists or not.<hr>

**[Parameters]**

- `snapshot_name`: str
  - Target snapshot name.

### _get_custom_event_type_str method docstring

Get a custom event type string from a type value.<hr>

**[Parameters]**

- `custom_event_type`: CustomEventType or str
  - Target custom event type or string.

<hr>

**[Returns]**

- `custom_event_type_str`: str
  - A custom event type string.

### _get_next_snapshot_name method docstring

Get a next snapshot name.<hr>

**[Returns]**

- `snapshot_name`: str
  - Next snapshot name.

### _get_previous_variable_name method docstring

Get a previous variable name.<hr>

**[Returns]**

- `previous_variable_name`: str
  - A previous variable name of this instance. If that value is not existing, then a blank string will be returned.

### _initialize_attr_linking_stack method docstring

Initialize the _attr_linking_stack attribute if it hasn't been initialized yet.<hr>

**[Parameters]**

- `attr_name`: str
  - Target attribute name.

### _initialize_blank_object_if_not_initialized method docstring

Initialize a blank object value if it hasn't been initialized yet.

### _initialize_children_if_not_initialized method docstring

Initialize _children attribute if it hasn't been initialized yet.

### _initialize_click_handlers_if_not_initialized method docstring

Initialize _click_handlers attribute if it hasn't been initialized yet.

### _initialize_css_if_not_initialized method docstring

Initialize the _css attribute if it hasn't been initialized yet.

### _initialize_custom_event_handlers_if_not_initialized method docstring

Initialize the _custom_event_handlers data if it hasn't been initialized yet.<hr>

**[Parameters]**

- `custom_event_type_str`: str
  - Target custom event type string.

### _initialize_dblclick_handlers_if_not_initialized method docstring

Initialize _dblclick_handlers attribute if it is not initialized yet.

### _initialize_fill_alpha_if_not_initialized method docstring

Initialize fill_alpha attribute if it hasn't been initialized yet.

### _initialize_fill_color_if_not_initialized method docstring

Initialize fill_color attribute if it hasn't been initialized yet.

### _initialize_line_alpha_if_not_initialized method docstring

Initialize _line_alpha attribute if it is not initialized yet.

### _initialize_line_cap_if_not_initialized method docstring

Initialize _line_cap attribute if it hasn't been initialized yet.

### _initialize_line_color_if_not_initialized method docstring

Initialize _line_color attribute it it is not initialized yet.

### _initialize_line_dash_dot_setting_if_not_initialized method docstring

Initialize _line_dash_dot_setting attribute if it is not initialized yet.

### _initialize_line_dash_setting_if_not_initialized method docstring

Initialize _line_dash_setting attribute if it is not initialized yet.

### _initialize_line_dot_setting_if_not_initialized method docstring

Initialize _line_dot_setting attribute if it is not initialized yet.

### _initialize_line_joints_if_not_initialized method docstring

Initialize _line_joints attribute if it hasn't been initialized yet.

### _initialize_line_round_dot_setting_if_not_initialized method docstring

Initialize _line_round_dot_setting attribute if it is not initialized yet.

### _initialize_line_thickness_if_not_initialized method docstring

Initialize _line_thickness attribute if it is not initialized yet.

### _initialize_mouse_down_handlers_if_not_initialized method docstring

Initialize _mouse_down_handlers attribute if it is not initialized yet.

### _initialize_mouse_move_handlers_if_not_initialized method docstring

Initialize _mouse_move_handlers attribute if it is not initialized yet.

### _initialize_mouse_out_handlers_if_not_initialized method docstring

Initialize _mouse_out_handlers attribute if it is not initialized yet.

### _initialize_mouse_over_handlers_if_not_initialized method docstring

Initialize _mouse_over_handlers attribute if it is not initialized yet.

### _initialize_mouse_up_handlers_if_not_initialized method docstring

Initialize _mouse_up_handlers attribute if it is not initialized yet.

### _initialize_ss_exists_val_if_not_initialized method docstring

Initialize _snapshot_exists_ value it hasn't been initialized yet.

### _initialize_visible_if_not_initialized method docstring

Initialize _visible attribute if it hasn't been initialized yet.

### _initialize_x_if_not_initialized method docstring

Initialize the _x attribute if it hasn't been initialized yet.

### _initialize_y_if_not_initialized method docstring

Initialize the _y attribute if it hasn't been initialized yet.

### _is_target_attr_already_linked method docstring

Get a boolean value whether a specified attribute has already been appended to the linking attribute stack.<hr>

**[Parameters]**

- `attr`: Int or Number or String or Boolean
  - Target attribute to be appended.
- `attr_name`: str
  - Target attribute name.

<hr>

**[Returns]**

- `result`: bool
  - If a specified attribute has already been appended to the linking stack, this value will be True.

### _make_snapshot method docstring

Make a value's snapshot.<hr>

**[Parameters]**

- `snapshot_name`: str
  - Target snapshot name.

### _reset_each_line_settings method docstring

Reset each line settings (e.g., LineDotSetting, LineDashSetting, and so on).<hr>

**[Notes]**

expression will not be appended.

### _revert method docstring

Revert a value if snapshot exists.<hr>

**[Parameters]**

- `snapshot_name`: str
  - Target snapshot name.

### _run_all_make_snapshot_methods method docstring

Run all _make_snapshot methods. If instance is multiple inheritance one, and each has RevertInterface, then each _make_snapshot methods will be called.<hr>

**[Parameters]**

- `snapshot_name`: str
  - Target snapshot name.

### _run_all_revert_methods method docstring

Run all _revert methods. If instance is multiple inheritance one, and each has RevertInterface, then each _revert methods will be called.<hr>

**[Parameters]**

- `snapshot_name`: str
  - Target snapshot name.

### _run_base_cls_make_snapshot_methods_recursively method docstring

Run base classes make_snapshot methods recursively.<hr>

**[Parameters]**

- `class_`: type
  - Target type.
- `snapshot_name`: str
  - Target snapshot name.

### _run_base_cls_revert_methods_recursively method docstring

Run base classes revert methods recursively.<hr>

**[Parameters]**

- `class_`: type
  - Target type.
- `snapshot_name`: str
  - Target snapshot name.

### _set_custom_event_handler_data method docstring

Set a handler's data to the dictionary.<hr>

**[Parameters]**

- `handler`: _Handler
  - Callable will be called when an event is dispatched.
- `custom_event_type_str`: str
  - Target custom event type string.
- `options`: dict or None
  - Optional arguments dictionary to be passed to a handler.

### _set_line_cap method docstring

Set line cap setting to attribute.<hr>

**[Parameters]**

- `cap`: LineCaps or None, default None
  - Line cap (edge style) setting.

### _set_line_joints method docstring

Set line joints setting to attribute.<hr>

**[Parameters]**

- `joints`: LineJoints or None, default None
  - Line vertices (joints) style setting.

### _set_mouse_event_handler_data method docstring

Set a handler's data to the given dictionary.<hr>

**[Parameters]**

- `handler`: _Handler
  - Callable would be called when event is dispatched.
- `handlers_dict`: dict
  - Dictionary to be set handler's data.
- `options`: dict or None
  - Optional arguments dictionary to be passed to handler.

### _set_overflow_visible_setting method docstring

Set the `visible` value to the `overflow` CSS property.

### _set_single_snapshot_val_to_dict method docstring

Set a single snapshot value to the specified name dictionary.<hr>

**[Parameters]**

- `dict_name`: str
  - Target dictionary name.
- `value`: Any
  - Target value.
- `snapshot_name`: str
  - Target snapshot name.

<hr>

**[Notes]**

If a snapshot value of the same name already exists, the process will be stopped.

### _set_snapshot_exists_val method docstring

Set boolean value whether snapshot value exists or not.<hr>

**[Parameters]**

- `snapshot_name`: str
  - Target snapshot name.

### _snapshot_exists method docstring

Get a boolean value whether snapshot value exists or not.<hr>

**[Parameters]**

- `snapshot_name`: str
  - Target snapshot name.

<hr>

**[Returns]**

- `snapshot_exists`: bool
  - Boolean value whether snapshot value exists or not.

### _unbind_all_mouse_events method docstring

Unbind specified all mouse event type's event.<hr>

**[Parameters]**

- `mouse_event_type`: MouseEventType
  - Event type to unbind.
- `handlers_dict`: dict
  - Dictionary that has handler's data.

### _unbind_mouse_event method docstring

Unbind specified handler's mouse event.<hr>

**[Parameters]**

- `handler`: _Handler
  - Unbinding target Callable.
- `mouse_event_type`: MouseEventType
  - Event type to unbind.
- `handlers_dict`: dict
  - Dictionary that has handler's data.

### _unset_custom_event_handler_data method docstring

Unset a handler's data from the dictionary.<hr>

**[Parameters]**

- `handler`: _Handler
  - Callable will be called when an event is dispatched.
- `custom_event_type_str`: str
  - Target custom event type string.

### add_child method docstring

Add display object child to this instance.<hr>

**[Parameters]**

- `child`: DisplayObject
  - Child instance to add.

<hr>

**[Examples]**

```py
>>> import apysc as ap
>>> stage: ap.Stage = ap.Stage()
>>> sprite_1: ap.Sprite = ap.Sprite()
>>> sprite_1.graphics.begin_fill(color='#0af')
>>> rectangle: ap.Rectangle = sprite_1.graphics.draw_rect(
...     x=50, y=50, width=50, height=50)
>>> sprite_2: ap.Sprite = ap.Sprite()
>>> sprite_2.add_child(rectangle)
```

<hr>

**[References]**

- [add_child and remove_child interfaces document](https://simon-ritchie.github.io/apysc/add_child_and_remove_child.html)

### animation_finish method docstring

Finish all animations (set the animation last value to each attribute).<hr>

**[Examples]**

```py
>>> from typing_extensions import TypedDict
>>> import apysc as ap
>>> class RectOptions(TypedDict):
...     rectangle: ap.Rectangle
>>> def on_timer(
...         e: ap.TimerEvent,
...         options: RectOptions) -> None:
...     rectangle: ap.Rectangle = options['rectangle']
...     rectangle.animation_finish()
>>> stage: ap.Stage = ap.Stage()
>>> sprite: ap.Sprite = ap.Sprite()
>>> sprite.graphics.begin_fill(color='#0af')
>>> rectangle: ap.Rectangle = sprite.graphics.draw_rect(
...     x=50, y=50, width=50, height=50)
>>> _ = rectangle.animation_x(
...     x=100,
...     duration=1500,
...     easing=ap.Easing.EASE_OUT_QUINT,
... ).start()
>>> options: RectOptions = {'rectangle': rectangle}
>>> ap.Timer(on_timer, delay=750, options=options).start()
```

<hr>

**[References]**

- [animation_finish interface document](https://simon-ritchie.github.io/apysc/animation_finish.html)

### animation_move method docstring

Set the x and y coordinates animation settings.<hr>

**[Parameters]**

- `x`: Int or int
  - Destination of the x-coordinate.
- `y`: Int or int
  - Destination of the y-coordinate.
- `duration`: Int or int, default 3000
  - Milliseconds before an animation ends.
- `delay`: Int or int, default 0
  - Milliseconds before an animation starts.
- `easing`: Easing, default Easing.LINEAR
  - Easing setting.

<hr>

**[Returns]**

- `animation_move`: AnimationMove
  - Created animation setting instance.

<hr>

**[Notes]**

To start this animation, you need to call the `start` method of the returned instance.<hr>

**[Examples]**

```py
>>> import apysc as ap
>>> stage: ap.Stage = ap.Stage()
>>> sprite: ap.Sprite = ap.Sprite()
>>> sprite.graphics.begin_fill(color='#0af')
>>> sprite.graphics.line_style(
...     color='#fff', thickness=1)
>>> rectangle: ap.Rectangle = sprite.graphics.draw_rect(
...     x=50, y=50, width=50, height=50)
>>> _ = rectangle.animation_move(
...     x=100, y=150,
...     duration=1500,
...     easing=ap.Easing.EASE_OUT_QUINT,
... ).start()
```

<hr>

**[References]**

- [animation_move interface document](https://simon-ritchie.github.io/apysc/animation_move.html)
- [Animation interfaces duration setting document](https://simon-ritchie.github.io/apysc/animation_duration.html)
- [Animation interfaces delay setting document](https://simon-ritchie.github.io/apysc/animation_delay.html)
- [Each animation interface return value document](https://simon-ritchie.github.io/apysc/animation_return_value.html)
- [Sequential animation setting document](https://simon-ritchie.github.io/apysc/sequential_animation.html)
- [animation_parallel interface document](https://simon-ritchie.github.io/apysc/animation_parallel.html)
- [Easing enum document](https://simon-ritchie.github.io/apysc/easing_enum.html)

### animation_parallel method docstring

Set the parallel animation setting.<hr>

**[Parameters]**

- `animations`: list of AnimationBase
  - Target animation settings.
- `duration`: Int or int, default 3000
  - Milliseconds before an animation ends.
- `delay`: Int or int, default 0
  - Milliseconds before an animation starts.
- `easing`: Easing, default Easing.LINEAR
  - Easing setting.

<hr>

**[Returns]**

- `animation_parallel`: AnimationParallel
  - Created animation setting instance.

<hr>

**[Raises]**

- ValueError: <br> ・If the animations' target is not this instance. <br> ・If there are changed duration, delay, or easing animation settings in the `animations` list.

<hr>

**[Notes]**

 ・To start this animation, you need to call the `start` method of the returned instance. <br> ・The `animations` argument can't contains the `AnimationParallel` instance. <br> ・This interface ignores the duration, delay, and easing arguments in the `animations` argument (this interface uses self-arguments instead).<hr>

**[Examples]**

```py
>>> import apysc as ap
>>> stage: ap.Stage = ap.Stage()
>>> sprite: ap.Sprite = ap.Sprite()
>>> sprite.graphics.begin_fill(color='#0af')
>>> rectangle: ap.Rectangle = sprite.graphics.draw_rect(
...     x=50, y=50, width=50, height=50)
>>> _ = rectangle.animation_parallel(
...     animations=[
...         rectangle.animation_x(x=100),
...         rectangle.animation_fill_color(fill_color='#f0a'),
...         rectangle.animation_fill_alpha(alpha=0.5),
...     ],
...     duration=1500,
...     easing=ap.Easing.EASE_OUT_QUINT,
... ).start()
```

<hr>

**[References]**

- [Animation interfaces duration setting document](https://simon-ritchie.github.io/apysc/animation_duration.html)
- [Animation interfaces delay setting document](https://simon-ritchie.github.io/apysc/animation_delay.html)
- [Each animation interface return value document](https://simon-ritchie.github.io/apysc/animation_return_value.html)
- [Sequential animation setting document](https://simon-ritchie.github.io/apysc/sequential_animation.html)
- [animation_parallel interface document](https://simon-ritchie.github.io/apysc/animation_parallel.html)
- [Easing enum document](https://simon-ritchie.github.io/apysc/easing_enum.html)

### animation_pause method docstring

Stop the all animations.<hr>

**[Examples]**

```py
>>> from typing_extensions import TypedDict
>>> import apysc as ap
>>> class RectOptions(TypedDict):
...     rectangle: ap.Rectangle
>>> def on_timer(
...         e: ap.TimerEvent,
...         options: RectOptions) -> None:
...     rectangle: ap.Rectangle = options['rectangle']
...     rectangle.animation_pause()
>>> stage: ap.Stage = ap.Stage()
>>> sprite: ap.Sprite = ap.Sprite()
>>> sprite.graphics.begin_fill(color='#0af')
>>> rectangle: ap.Rectangle = sprite.graphics.draw_rect(
...     x=50, y=50, width=50, height=50)
>>> _ = rectangle.animation_x(
...     x=100,
...     duration=1500,
...     easing=ap.Easing.EASE_OUT_QUINT,
... ).start()
>>> options: RectOptions = {'rectangle': rectangle}
>>> ap.Timer(on_timer, delay=750, options=options).start()
```

<hr>

**[References]**

- [animation_pause and animation_play interfaces document](https://simon-ritchie.github.io/apysc/animation_pause_and_play.html)

### animation_play method docstring

Restart the all paused animations.<hr>

**[Examples]**

```py
>>> from typing_extensions import TypedDict
>>> import apysc as ap
>>> class RectOptions(TypedDict):
...     rectangle: ap.Rectangle
>>> def on_timer_1(
...         e: ap.TimerEvent,
...         options: RectOptions) -> None:
...     rectangle: ap.Rectangle = options['rectangle']
...     rectangle.animation_pause()
>>> def on_timer_2(
...         e: ap.TimerEvent,
...         options: RectOptions) -> None:
...     rectangle: ap.Rectangle = options['rectangle']
...     rectangle.animation_play()
>>> stage: ap.Stage = ap.Stage()
>>> sprite: ap.Sprite = ap.Sprite()
>>> sprite.graphics.begin_fill(color='#0af')
>>> rectangle: ap.Rectangle = sprite.graphics.draw_rect(
...     x=50, y=50, width=50, height=50)
>>> _ = rectangle.animation_x(
...     x=100,
...     duration=1500,
...     easing=ap.Easing.EASE_OUT_QUINT,
... ).start()
>>> options: RectOptions = {'rectangle': rectangle}
>>> ap.Timer(on_timer_1, delay=500, options=options).start()
>>> ap.Timer(on_timer_2, delay=1000, options=options).start()
```

<hr>

**[References]**

- [animation_pause and animation_play interfaces document](https://simon-ritchie.github.io/apysc/animation_pause_and_play.html)

### animation_reset method docstring

Stop the all animations and reset.<hr>

**[Examples]**

```py
>>> from typing_extensions import TypedDict
>>> import apysc as ap
>>> class RectOptions(TypedDict):
...     rectangle: ap.Rectangle
>>> def on_timer(
...         e: ap.TimerEvent,
...         options: RectOptions) -> None:
...     rectangle: ap.Rectangle = options['rectangle']
...     rectangle.animation_reset()
>>> stage: ap.Stage = ap.Stage()
>>> sprite: ap.Sprite = ap.Sprite()
>>> sprite.graphics.begin_fill(color='#0af')
>>> rectangle: ap.Rectangle = sprite.graphics.draw_rect(
...     x=50, y=50, width=50, height=50)
>>> _ = rectangle.animation_x(
...     x=100,
...     duration=1500,
...     easing=ap.Easing.EASE_OUT_QUINT,
... ).start()
>>> options: RectOptions = {'rectangle': rectangle}
>>> ap.Timer(on_timer, delay=750, options=options).start()
```

<hr>

**[References]**

- [animation_reset interface document](https://simon-ritchie.github.io/apysc/animation_reset.html)

### animation_reverse method docstring

Reverse the all running animations.<hr>

**[Notes]**

Suppose you call this interface multiple times and animations reach the beginning or end of the animation. In that case, this interface ignores the reverse instruction. This behavior means that the same interval's timer tick reverse setting does not work correctly (since the same interval setting reaches the animation start).<hr>

**[Examples]**

```py
>>> from typing_extensions import TypedDict
>>> import apysc as ap
>>> class RectOptions(TypedDict):
...     rectangle: ap.Rectangle
>>> def on_timer(
...         e: ap.TimerEvent,
...         options: RectOptions) -> None:
...     rectangle: ap.Rectangle = options['rectangle']
...     rectangle.animation_reverse()
>>> stage: ap.Stage = ap.Stage()
>>> sprite: ap.Sprite = ap.Sprite()
>>> sprite.graphics.begin_fill(color='#0af')
>>> rectangle: ap.Rectangle = sprite.graphics.draw_rect(
...     x=50, y=50, width=50, height=50)
>>> _ = rectangle.animation_x(
...     x=100,
...     duration=1500,
...     easing=ap.Easing.EASE_OUT_QUINT,
... ).start()
>>> options: RectOptions = {'rectangle': rectangle}
>>> ap.Timer(on_timer, delay=750, options=options).start()
```

<hr>

**[References]**

- [animation_reverse interface document](https://simon-ritchie.github.io/apysc/animation_reverse.html)

### animation_time method docstring

Get an animation elapsed milisecond.<hr>

**[Returns]**

- `elapsed_time`: Number
  - An animation elapsed millisecond.

<hr>

**[Examples]**

```py
>>> from typing_extensions import TypedDict
>>> import apysc as ap
>>> class RectOptions(TypedDict):
...     rectangle: ap.Rectangle
>>> def on_timer(
...         e: ap.TimerEvent,
...         options: RectOptions) -> None:
...     rectangle: ap.Rectangle = options['rectangle']
...     animation_time: ap.Number = rectangle.animation_time()
...     ap.trace('animation_time:', animation_time)
>>> stage: ap.Stage = ap.Stage()
>>> sprite: ap.Sprite = ap.Sprite()
>>> sprite.graphics.begin_fill(color='#0af')
>>> rectangle: ap.Rectangle = sprite.graphics.draw_rect(
...     x=50, y=50, width=50, height=50)
>>> _ = rectangle.animation_x(
...     x=100,
...     duration=1500,
...     easing=ap.Easing.EASE_OUT_QUINT,
... ).start()
>>> options: RectOptions = {'rectangle': rectangle}
>>> ap.Timer(
...     on_timer, delay=ap.FPS.FPS_60,
...     options=options).start()
```

<hr>

**[References]**

- [animation_time interface document](https://simon-ritchie.github.io/apysc/animation_time.html)

### animation_x method docstring

Set the x-coordinate animation setting.<hr>

**[Parameters]**

- `x`: Int or int
  - Destination of the x-coordinate.
- `duration`: Int or int, default 3000
  - Milliseconds before an animation ends.
- `delay`: Int or int, default 0
  - Milliseconds before an animation starts.
- `easing`: Easing, default Easing.LINEAR
  - Easing setting.

<hr>

**[Returns]**

- `animation_x`: AnimationX
  - Created animation setting instance.

<hr>

**[Notes]**

To start this animation, you need to call the `start` method of the returned instance.<hr>

**[Examples]**

```py
>>> import apysc as ap
>>> stage: ap.Stage = ap.Stage()
>>> sprite: ap.Sprite = ap.Sprite()
>>> sprite.graphics.begin_fill(color='#0af')
>>> rectangle: ap.Rectangle = sprite.graphics.draw_rect(
...     x=50, y=50, width=50, height=50)
>>> _ = rectangle.animation_x(
...     x=100,
...     duration=1500,
...     easing=ap.Easing.EASE_OUT_QUINT,
... ).start()
```

<hr>

**[References]**

- [animation_x interface document](https://simon-ritchie.github.io/apysc/animation_x.html)
- [Animation interfaces duration setting document](https://simon-ritchie.github.io/apysc/animation_duration.html)
- [Animation interfaces delay setting document](https://simon-ritchie.github.io/apysc/animation_delay.html)
- [Each animation interface return value document](https://simon-ritchie.github.io/apysc/animation_return_value.html)
- [Sequential animation setting document](https://simon-ritchie.github.io/apysc/sequential_animation.html)
- [animation_parallel interface document](https://simon-ritchie.github.io/apysc/animation_parallel.html)
- [Easing enum document](https://simon-ritchie.github.io/apysc/easing_enum.html)

### animation_y method docstring

Set the y-coordinate animation setting.<hr>

**[Parameters]**

- `y`: Int or int
  - Destination of the y-coordinate.
- `duration`: Int or int, default 3000
  - Milliseconds before an animation ends.
- `delay`: Int or int, default 0
  - Milliseconds before an animation starts.
- `easing`: Easing, default Easing.LINEAR
  - Easing setting.

<hr>

**[Returns]**

- `animation_y`: AnimationY
  - Created animation setting instance.

<hr>

**[Notes]**

To start this animation, you need to call the `start` method of the returned instance.<hr>

**[Examples]**

```py
>>> import apysc as ap
>>> stage: ap.Stage = ap.Stage()
>>> sprite: ap.Sprite = ap.Sprite()
>>> sprite.graphics.begin_fill(color='#0af')
>>> rectangle: ap.Rectangle = sprite.graphics.draw_rect(
...     x=50, y=50, width=50, height=50)
>>> _ = rectangle.animation_y(
...     y=100,
...     duration=1500,
...     easing=ap.Easing.EASE_OUT_QUINT,
... ).start()
```

<hr>

**[References]**

- [animation_y interface document](https://simon-ritchie.github.io/apysc/animation_y.html)
- [Animation interfaces duration setting document](https://simon-ritchie.github.io/apysc/animation_duration.html)
- [Animation interfaces delay setting document](https://simon-ritchie.github.io/apysc/animation_delay.html)
- [Each animation interface return value document](https://simon-ritchie.github.io/apysc/animation_return_value.html)
- [Sequential animation setting document](https://simon-ritchie.github.io/apysc/sequential_animation.html)
- [animation_parallel interface document](https://simon-ritchie.github.io/apysc/animation_parallel.html)
- [Easing enum document](https://simon-ritchie.github.io/apysc/easing_enum.html)

### begin_fill method docstring

Set single color value for fill.<hr>

**[Parameters]**

- `color`: str or String
  - Hexadecimal color string. e.g., '#00aaff'
- `alpha`: float or Number, default 1.0
  - Color opacity (0.0 to 1.0).

<hr>

**[Examples]**

```py
>>> import apysc as ap
>>> stage: ap.Stage = ap.Stage()
>>> sprite: ap.Sprite = ap.Sprite()
>>> sprite.graphics.begin_fill(color='#0af')
>>> rectangle: ap.Rectangle = sprite.graphics.draw_rect(
...     x=50, y=50, width=50, height=50)
>>> rectangle.fill_color
String('#00aaff')
```

<hr>

**[References]**

- [Graphics begin_fill interface document](https://simon-ritchie.github.io/apysc/graphics_begin_fill.html)

### bind_custom_event method docstring

Add a custom event listener setting.<hr>

**[Parameters]**

- `custom_event_type`: CustomEventType or str
  - Target custom event type.
- `handler`: _Handler
  - A handler will be called when the custom event is triggered.
- `e`: Event
  - Event instance.
- `options`: dict or None, default None
  - Optional arguments dictionary to be passed to a handler.
- `in_handler_head_expression`: str, default ''
  - Optional expression to be added at the handler function's head position.

<hr>

**[Returns]**

- `name`: str
  - Handler's name.

<hr>

**[Examples]**

```py
>>> import apysc as ap
>>> def on_custom_event(
...         e: ap.Event[ap.Rectangle], options: dict) -> None:
...     rectangle: ap.Rectangle = e.this
...     rectangle.fill_color = ap.String('#f0a')
>>> stage: ap.Stage = ap.Stage()
>>> sprite: ap.Sprite = ap.Sprite()
>>> sprite.graphics.begin_fill(color='#0af')
>>> rectangle: ap.Rectangle = sprite.graphics.draw_rect(
...     x=50, y=50, width=50, height=50)
>>> e: ap.Event = ap.Event(this=rectangle)
>>> _ = rectangle.bind_custom_event(
...     custom_event_type='my_custom_event',
...     handler=on_custom_event, e=e)
>>> # Do something here and then trigger the custom event
>>> rectangle.trigger_custom_event(
...     custom_event_type='my_custom_event')
```

<hr>

**[References]**

- [Bind and trigger the custom event document](https://simon-ritchie.github.io/apysc/bind_and_trigger_custom_event.html)
- [About the handler options' type document](https://simon-ritchie.github.io/apysc/about_handler_options_type.html)

### clear method docstring

Clear all graphics and reset fill and line settings.<hr>

**[Examples]**

```py
>>> import apysc as ap
>>> stage: ap.Stage = ap.Stage()
>>> sprite: ap.Sprite = ap.Sprite()
>>> sprite.graphics.begin_fill(color='#0af')
>>> _ = sprite.graphics.draw_rect(
...     x=50, y=50, width=50, height=50)
>>> _ = sprite.graphics.draw_rect(
...     x=150, y=50, width=50, height=50)
>>> sprite.graphics.num_children
Int(2)

>>> sprite.graphics.fill_color
String('#00aaff')

>>> sprite.graphics.clear()
>>> sprite.graphics.num_children
Int(0)

>>> sprite.graphics.fill_color
String('')
```

### click method docstring

Add a click event listener setting.<hr>

**[Parameters]**

- `handler`: _Handler
  - A callable would be called when clicking this instance.
- `options`: dict or None, default None
  - Optional arguments dictionary to be passed to a handler.

<hr>

**[Returns]**

- `name`: str
  - Handler's name.

<hr>

**[Examples]**

```py
>>> import apysc as ap
>>> def on_click(
...         e: ap.MouseEvent[ap.Rectangle], options: dict) -> None:
...     rectangle: ap.Rectangle = e.this
...     rectangle.x += 10
>>> stage: ap.Stage = ap.Stage()
>>> sprite: ap.Sprite = ap.Sprite()
>>> sprite.graphics.begin_fill(color='#0af')
>>> rectangle: ap.Rectangle = sprite.graphics.draw_rect(
...     x=50, y=50, width=50, height=50)
>>> _ = rectangle.click(on_click)
```

<hr>

**[References]**

- [Click interface document](https://simon-ritchie.github.io/apysc/click.html)
- [About the handler options’ type document](https://simon-ritchie.github.io/apysc/about_handler_options_type.html)

### contains method docstring

Get a boolean whether this instance contains a specified child.<hr>

**[Parameters]**

- `child`: DisplayObject
  - Child instance to check.

<hr>

**[Returns]**

- `result`: Boolean
  - If this instance contains a specified child, this method returns True.

<hr>

**[Examples]**

```py
>>> import apysc as ap
>>> stage: ap.Stage = ap.Stage()
>>> sprite: ap.Sprite = ap.Sprite()
>>> sprite.graphics.begin_fill(color='#0af', alpha=0.5)
>>> rectangle: ap.Rectangle = sprite.graphics.draw_rect(
...     x=50, y=50, width=50, height=50)
>>> sprite.graphics.contains(rectangle)
Boolean(True)

>>> rectangle.remove_from_parent()
>>> sprite.graphics.contains(rectangle)
Boolean(False)
```

<hr>

**[References]**

- [contains interface document](https://simon-ritchie.github.io/apysc/contains.html)

### dblclick method docstring

Add double click event listener setting.<hr>

**[Parameters]**

- `handler`: _Handler
  - Callable that would be called when double-clicking this instance.
- `options`: dict or None, default None
  - Optional arguments dictionary to be passed to a handler.

<hr>

**[Returns]**

- `name`: str
  - Handler's name.

<hr>

**[Examples]**

```py
>>> import apysc as ap
>>> def on_double_click(
...         e: ap.MouseEvent[ap.Rectangle], options: dict) -> None:
...     rectangle: ap.Rectangle = e.this
...     rectangle.fill_color = ap.String('#f0a')
>>> stage: ap.Stage = ap.Stage()
>>> sprite: ap.Sprite = ap.Sprite()
>>> sprite.graphics.begin_fill(color='#0af')
>>> rectangle: ap.Rectangle = sprite.graphics.draw_rect(
...     x=50, y=50, width=50, height=50)
>>> _ = rectangle.dblclick(on_double_click)
```

<hr>

**[References]**

- [Double click interface document](https://simon-ritchie.github.io/apysc/dblclick.html)
- [About the handler options’ type document](https://simon-ritchie.github.io/apysc/about_handler_options_type.html)

### draw_circle method docstring

Draw a circle vector graphics.<hr>

**[Parameters]**

- `x`: Int or int
  - X-coordinate of the circle center.
- `y`: Int or int
  - Y-coordinate of the circle center.
- `radius`: Int or int
  - Circle radius.

<hr>

**[Returns]**

- `circle`: Circle
  - Created circle graphics instance.

<hr>

**[Examples]**

```py
>>> import apysc as ap
>>> stage: ap.Stage = ap.Stage()
>>> sprite: ap.Sprite = ap.Sprite()
>>> sprite.graphics.begin_fill(color='#0af')
>>> circle: ap.Circle = sprite.graphics.draw_circle(
...     x=100, y=100, radius=50)
>>> circle.x
Int(100)

>>> circle.y
Int(100)

>>> circle.radius
Int(50)

>>> circle.fill_color
String('#00aaff')
```

<hr>

**[References]**

- [Graphics draw_circle interface document](https://simon-ritchie.github.io/apysc/graphics_draw_circle.html)

### draw_dash_dotted_line method docstring

Draw a dash dotted (1-dot chain) line vector graphics.<hr>

**[Parameters]**

- `x_start`: Int or int
  - Line start x-coordinate.
- `y_start`: Int or int
  - Line start y-coordinate.
- `x_end`: Int or int
  - Line end x-coordinate.
- `y_end`: Int or int
  - Line end y-coordinate.
- `dot_size`: Int or int
  - Dot size.
- `dash_size`: Int or int
  - Dash size.
- `space_size`: Int or int
  - Blank space size between dots and dashes.

<hr>

**[Returns]**

- `line`: Line
  - Created line graphics instance.

<hr>

**[Examples]**

```py
>>> import apysc as ap
>>> stage: ap.Stage = ap.Stage()
>>> sprite: ap.Sprite = ap.Sprite()
>>> sprite.graphics.line_style(color='#fff', thickness=5)
>>> line: ap.Line = sprite.graphics.draw_dash_dotted_line(
...    x_start=50, y_start=50, x_end=150, y_end=50,
...    dot_size=2, dash_size=5, space_size=3)
>>> line.line_color
String('#ffffff')

>>> line.line_dash_dot_setting.dot_size
Int(2)

>>> line.line_dash_dot_setting.dash_size
Int(5)

>>> line.line_dash_dot_setting.space_size
Int(3)
```

<hr>

**[References]**

- [Graphics draw_dash_dotted_line interface document](https://simon-ritchie.github.io/apysc/graphics_draw_dash_dotted_line.html)

### draw_dashed_line method docstring

Draw a dashed line vector graphics.<hr>

**[Parameters]**

- `x_start`: Int or int
  - Line start x-coordinate.
- `y_start`: Int or int
  - Line start y-coordinate.
- `x_end`: Int or int
  - Line end x-coordinate.
- `y_end`: Int or int
  - Line end y-coordinate.
- `dash_size`: Int or int
  - Dash size.
- `space_size`: Int or int
  - Blank space size between dashes.

<hr>

**[Returns]**

- `line`: Line
  - Created line graphics instance.

<hr>

**[Notes]**

 ・This interface ignores line settings, like the `LineDotSetting`, except `LineDashSetting`.<hr>

**[Examples]**

```py
>>> import apysc as ap
>>> stage: ap.Stage = ap.Stage()
>>> sprite: ap.Sprite = ap.Sprite()
>>> sprite.graphics.line_style(color='#fff', thickness=5)
>>> line: ap.Line = sprite.graphics.draw_dashed_line(
...     x_start=50, y_start=50, x_end=150, y_end=50,
...     dash_size=5, space_size=2)
>>> line.line_color
String('#ffffff')

>>> line.line_dash_setting.dash_size
Int(5)

>>> line.line_dash_setting.space_size
Int(2)
```

<hr>

**[References]**

- [Graphics draw_dashed_line interface document](https://simon-ritchie.github.io/apysc/graphics_draw_dashed_line.html)

### draw_dotted_line method docstring

Draw a dotted line vector graphics.<hr>

**[Parameters]**

- `x_start`: Int or int
  - Line start x-coordinate.
- `y_start`: Int or int
  - Line start y-coordinate.
- `x_end`: Int or int
  - Line end x-coordinate.
- `y_end`: Int or int
  - Line end y-coordinate.
- `dot_size`: Int or int
  - Dot size.

<hr>

**[Returns]**

- `line`: Line
  - Created line graphics instance.

<hr>

**[Notes]**

 ・This interface ignores line settings, like the `LineDashSetting`, except `LineDotSetting`.<hr>

**[Examples]**

```py
>>> import apysc as ap
>>> stage: ap.Stage = ap.Stage()
>>> sprite: ap.Sprite = ap.Sprite()
>>> sprite.graphics.line_style(color='#fff', thickness=5)
>>> line: ap.Line = sprite.graphics.draw_dotted_line(
...     x_start=50, y_start=50, x_end=150, y_end=50, dot_size=5)
>>> line.line_color
String('#ffffff')

>>> line.line_thickness
Int(5)

>>> line.line_dot_setting.dot_size
Int(5)
```

<hr>

**[References]**

- [Graphics draw_dotted_line interface document](https://simon-ritchie.github.io/apysc/graphics_draw_dotted_line.html)

### draw_ellipse method docstring

Draw a ellipse vector graphics.<hr>

**[Parameters]**

- `x`: Int or int
  - X-coordinate of the ellipse center.
- `y`: Int or int
  - Y-coordinate of the ellipse center.
- `width`: Int or int
  - Ellipse width.
- `height`: Int or int
  - Ellipse height.

<hr>

**[Returns]**

- `ellipse`: Ellipse
  - Created ellipse graphics instance.

<hr>

**[Examples]**

```py
>>> import apysc as ap
>>> stage: ap.Stage = ap.Stage()
>>> sprite: ap.Sprite = ap.Sprite()
>>> sprite.graphics.begin_fill(color='#0af')
>>> ellipse: ap.Ellipse = sprite.graphics.draw_ellipse(
...     x=100, y=100, width=100, height=50)
>>> ellipse.x
Int(100)

>>> ellipse.y
Int(100)

>>> ellipse.width
Int(100)

>>> ellipse.height
Int(50)

>>> ellipse.fill_color
String('#00aaff')
```

<hr>

**[References]**

- [Graphics draw_ellipse interface](https://simon-ritchie.github.io/apysc/graphics_draw_ellipse.html)

### draw_line method docstring

Draw a normal line vector graphics.<hr>

**[Parameters]**

- `x_start`: Int or int
  - Line start x-coordinate.
- `y_start`: Int or int
  - Line start y-coordinate.
- `x_end`: Int or int
  - Line end x-coordinate.
- `y_end`: Int or int
  - Line end y-coordinate.

<hr>

**[Returns]**

- `line`: Line
  - Created line graphics instance.

<hr>

**[Notes]**

 ・This interface ignores line settings, like the `LineDotSetting`, `LineDashSetting`.<hr>

**[Examples]**

```py
>>> import apysc as ap
>>> stage: ap.Stage = ap.Stage()
>>> sprite: ap.Sprite = ap.Sprite()
>>> sprite.graphics.line_style(color='#fff', thickness=5)
>>> line: ap.Line = sprite.graphics.draw_line(
...     x_start=50, y_start=50, x_end=150, y_end=50)
>>> line.line_color
String('#ffffff')

>>> line.line_thickness
Int(5)
```

<hr>

**[References]**

- [Graphics draw_line interface document](https://simon-ritchie.github.io/apysc/graphics_draw_line.html)

### draw_path method docstring

Draw a path vector graphics.<hr>

**[Parameters]**

- `path_data_list`: list of PathDataBase
  - Target path data settings, such as the ap.PathData.MoveTo.

<hr>

**[Returns]**

- `path`: Path
  - Created path graphics instance.

<hr>

**[Examples]**

```py
>>> import apysc as ap
>>> stage: ap.Stage = ap.Stage()
>>> sprite: ap.Sprite = ap.Sprite()
>>> sprite.graphics.line_style(color='#fff', thickness=3)
>>> path: ap.Path = sprite.graphics.draw_path(
...     path_data_list=[
...         ap.PathMoveTo(x=0, y=50),
...         ap.PathBezier2D(
...             control_x=50, control_y=0,
...             dest_x=100, dest_y=50),
...     ])
```

### draw_polygon method docstring

Draw a polygon vector graphic. This interface is similar to the Polyline class (created by `move_to` or `line_to`). But unlike that, this interface connects the last point and the start point.<hr>

**[Parameters]**

- `points`: list of Point2D or Array.
  - Polygon vertex points.

<hr>

**[Returns]**

- `polygon`: Polygon
  - Created polygon graphics instance.

<hr>

**[Examples]**

```py
>>> import apysc as ap
>>> stage: ap.Stage = ap.Stage()
>>> sprite: ap.Sprite = ap.Sprite()
>>> sprite.graphics.begin_fill(color='#0af')
>>> polygon: ap.Polygon = sprite.graphics.draw_polygon(
...     points=[
...         ap.Point2D(x=25, y=0),
...         ap.Point2D(x=0, y=50),
...         ap.Point2D(x=50, y=50),
...     ])
>>> polygon.fill_color
String('#00aaff')
```

<hr>

**[References]**

- [Graphics draw_polygon interface document](https://simon-ritchie.github.io/apysc/graphics_draw_polygon.html)

### draw_rect method docstring

Draw a rectangle vector graphics.<hr>

**[Parameters]**

- `x`: Int or int
  - X position to start drawing.
- `y`: Int or int
  - Y position to start drawing.
- `width`: Int or int
  - Rectangle width.
- `height`: Int or int
  - Rectangle height.

<hr>

**[Returns]**

- `rectangle`: Rectangle
  - Created rectangle.

<hr>

**[Examples]**

```py
>>> import apysc as ap
>>> stage: ap.Stage = ap.Stage()
>>> sprite: ap.Sprite = ap.Sprite()
>>> sprite.graphics.begin_fill(color='#0af')
>>> rectangle: ap.Rectangle = sprite.graphics.draw_rect(
...     x=50, y=50, width=50, height=50)
>>> rectangle.x
Int(50)

>>> rectangle.width
Int(50)

>>> rectangle.fill_color
String('#00aaff')
```

<hr>

**[References]**

- [Graphics draw_rect interface document](https://simon-ritchie.github.io/apysc/graphics_draw_rect.html)

### draw_round_dotted_line method docstring

Draw a round dotted line vector graphics.<hr>

**[Parameters]**

- `x_start`: Int or int
  - Line start x-coordinate.
- `y_start`: Int or int
  - Line start y-coordinate.
- `x_end`: Int or int
  - Line end x-coordinate.
- `y_end`: Int or int
  - Line end y-coordinate.
- `round_size`: Int or int
  - Dot round size.
- `space_size`: Int or int
  - Blank space size between dots.

<hr>

**[Returns]**

- `line`: Line
  - Created line graphics instance.

<hr>

**[Notes]**

This interface ignores line settings, like the `LineDotSetting`, except `LineRoundDotSetting`.<hr>

**[Examples]**

```py
>>> import apysc as ap
>>> stage: ap.Stage = ap.Stage()
>>> sprite: ap.Sprite = ap.Sprite()
>>> sprite.graphics.line_style(color='#fff', thickness=5)
>>> line: ap.Line = sprite.graphics.draw_round_dotted_line(
...    x_start=50, y_start=50, x_end=150, y_end=50,
...    round_size=6, space_size=3)
>>> line.line_color
String('#ffffff')

>>> line.line_round_dot_setting.round_size
Int(6)

>>> line.line_round_dot_setting.space_size
Int(3)
```

<hr>

**[References]**

- [Graphics draw_round_dotted_line interface document](https://simon-ritchie.github.io/apysc/graphics_draw_round_dotted_line.html)

### draw_round_rect method docstring

Draw a rounded rectangle vector graphics.<hr>

**[Parameters]**

- `x`: Int or int
  - X-coordinate to start drawing.
- `y`: Int or int
  - Y-coordinate to start drawing.
- `width`: Int or int
  - Rectangle width.
- `height`: Int or int
  - Rectangle height.
- `ellipse_width`: Int or int
  - Ellipse width of the rectangle corner.
- `ellipse_height`: Int or int
  - Ellipse height of the rectangle corner.

<hr>

**[Returns]**

- `rectangle`: Rectangle
  - Created rectangle.

<hr>

**[Examples]**

```py
>>> import apysc as ap
>>> stage: ap.Stage = ap.Stage()
>>> sprite: ap.Sprite = ap.Sprite()
>>> sprite.graphics.begin_fill(color='#0af')
>>> round_rect: ap.Rectangle = sprite.graphics.draw_round_rect(
...     x=50, y=50, width=50, height=50,
...     ellipse_width=10, ellipse_height=15)
>>> round_rect.ellipse_width
Int(10)

>>> round_rect.ellipse_height
Int(15)
```

<hr>

**[References]**

- [Graphics draw_round_rect interface document](https://simon-ritchie.github.io/apysc/graphics_draw_round_rect.html)

### get_child_at method docstring

Get child at a specified index.<hr>

**[Parameters]**

- `index`: int or Int
  - Child's index (start from 0).

<hr>

**[Returns]**

- `child`: DisplayObject
  - Target index child instance.

<hr>

**[Examples]**

```py
>>> import apysc as ap
>>> stage: ap.Stage = ap.Stage()
>>> sprite: ap.Sprite = ap.Sprite()
>>> sprite.graphics.begin_fill(color='#0af', alpha=0.5)
>>> rectangle_1: ap.Rectangle = sprite.graphics.draw_rect(
...     x=50, y=50, width=50, height=50)
>>> rectangle_2: ap.Rectangle = sprite.graphics.draw_rect(
...     x=150, y=50, width=50, height=50)
>>> child_at_index_1: ap.DisplayObject = (
...     sprite.graphics.get_child_at(1))
>>> child_at_index_1 == rectangle_2
True
```

<hr>

**[References]**

- [get_child_at interface document](https://simon-ritchie.github.io/apysc/get_child_at.html)

### get_css method docstring

Get a CSS value string.<hr>

**[Parameters]**

- `name`: str or String
  - CSS name (e.g., 'display').

<hr>

**[Returns]**

- `css`: ap.String
  - CSS value.

<hr>

**[Examples]**

```py
>>> import apysc as ap
>>> stage: ap.Stage = ap.Stage()
>>> sprite: ap.Sprite = ap.Sprite()
>>> sprite.graphics.begin_fill(color='#0af', alpha=0.5)
>>> sprite.set_css(name='display', value='none')
>>> sprite.get_css(name='display')
String('none')
```

<hr>

**[References]**

- [Display object get_css and set_css interfaces document](https://simon-ritchie.github.io/apysc/display_object_get_and_set_css.html)

### line_style method docstring

Set line style values.<hr>

**[Parameters]**

- `color`: String or str
  - Hexadecimal color string. e.g., '#00aaff'
- `thickness`: Int or int, default 1
  - Line thickness (minimum value is 1).
- `alpha`: float or Number, default 1.0
  - Line color opacity (0.0 to 1.0).
- `cap`: LineCaps or None, default None
  - Line cap (edge style) setting. The not line-related graphics (e.g., Rectangle ignores this, conversely used by Polyline) ignore this setting.
- `joints`: LineJoints or None, default None
  - Line vertices (joints) style setting. The not polyline-related graphics (e.g., Rectangle ignores this, conversely used by Polyline) ignore this setting.
- `dot_setting`: LineDotSetting or None, default None
  - Dash setting. If this is specified, it makes a line dashed.
- `dash_setting`: LineDashSetting or None, default None
  - Dash setting. If this is specified, it makes a line dashed.
- `round_dot_setting`: LineRoundDotSetting or None, default None
  - Round dot setting. If this is specified, it makes a line round dotted. Notes: since this style uses a cap setting, it overrides cap and line thickness settings. And it increases the amount of line size. If you want to adjust to the same width of a normal line when using move_to and line_to interfaces, add half-round size to start x-coordinate and subtract from end e-coordinate. e.g., `this.move_to(x + round_size / 2, y)`, `this.line_to(x - round_size / 2, y)`
- `dash_dot_setting`: LineDashDotSetting or None, default None
  - Dash dot (1-dot chain) setting. If this is specified, it makes a line 1-dot chained.

<hr>

**[Examples]**

```py
>>> import apysc as ap
>>> stage: ap.Stage = ap.Stage()
>>> sprite: ap.Sprite = ap.Sprite()
>>> sprite.graphics.line_style(
...     color='#fff', thickness=5, alpha=0.5,
...     cap=ap.LineCaps.ROUND)
>>> line: ap.Line = sprite.graphics.draw_line(
...     x_start=50, y_start=50, x_end=150, y_end=50)
>>> line.line_color
String('#ffffff')

>>> line.line_thickness
Int(5)

>>> line.line_alpha
Number(0.5)

>>> line.line_cap
String('round')
```

<hr>

**[References]**

- [Graphics line_style interface document](https://simon-ritchie.github.io/apysc/graphics_line_style.html)

### line_to method docstring

Draw a line from previous point to specified point (initial point is x = 0, y = 0).<hr>

**[Parameters]**

- `x`: Int or int
  - X destination point to draw a line.
- `y`: Int or int
  - Y destination point to draw a line.

<hr>

**[Returns]**

- `line`: Polyline
  - Line graphics instance.

<hr>

**[Examples]**

```py
>>> import apysc as ap
>>> stage: ap.Stage = ap.Stage()
>>> sprite: ap.Sprite = ap.Sprite()
>>> sprite.graphics.line_style(color='#fff', thickness=5)
>>> line_1: ap.Polyline = sprite.graphics.move_to(x=50, y=50)
>>> line_2: ap.Polyline = sprite.graphics.line_to(x=150, y=50)
>>> line_3: ap.Polyline = sprite.graphics.line_to(x=50, y=150)
>>> line_1 == line_2 == line_3
True

>>> line_1.line_color
String('#ffffff')

>>> line_1.line_thickness
Int(5)
```

<hr>

**[References]**

- [Graphics move_to and line_to interfaces document](https://simon-ritchie.github.io/apysc/graphics_move_to_and_line_to.html)

### mousedown method docstring

Add mouse down event listener setting.<hr>

**[Parameters]**

- `handler`: _Handler
  - Callable that would be called when mouse down on this instance.
- `options`: dict or None, default None
  - Optional arguments dictionary to be passed to a handler.

<hr>

**[Returns]**

- `name`: str
  - Handler's name.

<hr>

**[Examples]**

```py
>>> import apysc as ap
>>> def on_mousedown(
...         e: ap.MouseEvent[ap.Rectangle], options: dict) -> None:
...     rectangle: ap.Rectangle = e.this
...     rectangle.fill_color = ap.String('#f0a')
>>> stage: ap.Stage = ap.Stage()
>>> sprite: ap.Sprite = ap.Sprite()
>>> sprite.graphics.begin_fill(color='#0af')
>>> rectangle: ap.Rectangle = sprite.graphics.draw_rect(
...     x=50, y=50, width=50, height=50)
>>> _ = rectangle.mousedown(on_mousedown)
```

<hr>

**[References]**

- [Mousedown and mouseup interfaces document](https://simon-ritchie.github.io/apysc/mousedown_and_mouseup.html)
- [About the handler options’ type document](https://simon-ritchie.github.io/apysc/about_handler_options_type.html)

### mousemove method docstring

Add mouse move event listener setting.<hr>

**[Parameters]**

- `handler`: _Handler
  - Callable that would be called when mousemove on this instance.
- `options`: dict or None, default None
  - Optional arguments dictionary to be passed to a handler.

<hr>

**[Returns]**

- `name`: str
  - Handler's name.

<hr>

**[Examples]**

```py
>>> import apysc as ap
>>> def on_mousemove(
...         e: ap.MouseEvent[ap.Rectangle], options: dict) -> None:
...     stage_x: ap.Int = e.stage_x
...     ap.trace('stage_x:', stage_x)
>>> stage: ap.Stage = ap.Stage()
>>> sprite: ap.Sprite = ap.Sprite()
>>> sprite.graphics.begin_fill(color='#0af')
>>> rectangle: ap.Rectangle = sprite.graphics.draw_rect(
...     x=50, y=50, width=50, height=50)
>>> _ = rectangle.mousemove(on_mousemove)
```

<hr>

**[References]**

- [Mousemove interface document](https://simon-ritchie.github.io/apysc/mousemove.html)
- [About the handler options’ type document](https://simon-ritchie.github.io/apysc/about_handler_options_type.html)

### mouseout method docstring

Add mouse out event listener setting.<hr>

**[Parameters]**

- `handler`: _Handler
  - Callable that would be called when mouse out on this instance.
- `options`: dict or None, default None
  - Optional arguments dictionary to be passed to a handler.

<hr>

**[Returns]**

- `name`: str
  - Handler's name.

<hr>

**[Examples]**

```py
>>> import apysc as ap
>>> def on_mouseout(
...         e: ap.MouseEvent[ap.Rectangle], options: dict) -> None:
...     rectangle: ap.Rectangle = e.this
...     rectangle.fill_color = ap.String('#f0a')
>>> stage: ap.Stage = ap.Stage()
>>> sprite: ap.Sprite = ap.Sprite()
>>> sprite.graphics.begin_fill(color='#0af')
>>> rectangle: ap.Rectangle = sprite.graphics.draw_rect(
...     x=50, y=50, width=50, height=50)
>>> _ = rectangle.mouseout(on_mouseout)
```

<hr>

**[References]**

- [Mouseover and mouseout interfaces](https://simon-ritchie.github.io/apysc/mouseover_and_mouseout.html)
- [About the handler options’ type document](https://simon-ritchie.github.io/apysc/about_handler_options_type.html)

### mouseover method docstring

Add mouse over event listener setting.<hr>

**[Parameters]**

- `handler`: _Handler
  - Callable that would be called when mouse over on this instance.
- `options`: dict or None, default None
  - Optional arguments dictionary to be passed to a handler.

<hr>

**[Returns]**

- `name`: str
  - Handler's name.

<hr>

**[Examples]**

```py
>>> import apysc as ap
>>> def on_mouseover(
...         e: ap.MouseEvent[ap.Rectangle], options: dict) -> None:
...     rectangle: ap.Rectangle = e.this
...     rectangle.fill_color = ap.String('#f0a')
>>> stage: ap.Stage = ap.Stage()
>>> sprite: ap.Sprite = ap.Sprite()
>>> sprite.graphics.begin_fill(color='#0af')
>>> rectangle: ap.Rectangle = sprite.graphics.draw_rect(
...     x=50, y=50, width=50, height=50)
>>> _ = rectangle.mouseout(on_mouseover)
```

<hr>

**[References]**

- [Mouseover and mouseout interfaces](https://simon-ritchie.github.io/apysc/mouseover_and_mouseout.html)
- [About the handler options' type document](https://simon-ritchie.github.io/apysc/about_handler_options_type.html)

### mouseup method docstring

Add mouse up event listener setting.<hr>

**[Parameters]**

- `handler`: _Handler
  - Callable that would be called when mouse-up on this instance.
- `options`: dict or None, default None
  - Optional arguments dictionary to be passed to a handler

<hr>

**[Returns]**

- `name`: str
  - Handler's name.

<hr>

**[Examples]**

```py
>>> import apysc as ap
>>> def on_mouseup(
...         e: ap.MouseEvent[ap.Rectangle], options: dict) -> None:
...     rectangle: ap.Rectangle = e.this
...     rectangle.fill_color = ap.String('#f0a')
>>> stage: ap.Stage = ap.Stage()
>>> sprite: ap.Sprite = ap.Sprite()
>>> sprite.graphics.begin_fill(color='#0af')
>>> rectangle: ap.Rectangle = sprite.graphics.draw_rect(
...     x=50, y=50, width=50, height=50)
>>> _ = rectangle.mouseup(on_mouseup)
```

<hr>

**[References]**

- [Mousedown and mouseup interfaces document](https://simon-ritchie.github.io/apysc/mousedown_and_mouseup.html)
- [About the handler options’ type document](https://simon-ritchie.github.io/apysc/about_handler_options_type.html)

### move_to method docstring

Move a line position to a specified point.<hr>

**[Parameters]**

- `x`: Int or int
  - X destination point to move.
- `y`: Int or int
  - Y destination point to move.

<hr>

**[Returns]**

- `line`: Polyline
  - Line graphics instance.

<hr>

**[Examples]**

```py
>>> import apysc as ap
>>> stage: ap.Stage = ap.Stage()
>>> sprite: ap.Sprite = ap.Sprite()
>>> sprite.graphics.line_style(color='#fff', thickness=5)
>>> line_1: ap.Polyline = sprite.graphics.move_to(x=50, y=50)
>>> line_2: ap.Polyline = sprite.graphics.line_to(x=150, y=50)
>>> line_1 == line_2
True

>>> line_1.line_color
String('#ffffff')

>>> line_1.line_thickness
Int(5)
```

<hr>

**[References]**

- [Graphics move_to and line_to interfaces document](https://simon-ritchie.github.io/apysc/graphics_move_to_and_line_to.html)

### remove_child method docstring

Remove display object child from this instance.<hr>

**[Parameters]**

- `child`: DisplayObject
  - Child instance to remove.

<hr>

**[Examples]**

```py
>>> import apysc as ap
>>> stage: ap.Stage = ap.Stage()
>>> sprite: ap.Sprite = ap.Sprite()
>>> sprite.graphics.begin_fill(color='#0af', alpha=0.5)
>>> rectangle: ap.Rectangle = sprite.graphics.draw_rect(
...     x=50, y=50, width=50, height=50)
>>> sprite.graphics.remove_child(rectangle)
>>> print(rectangle.parent)
None
```

<hr>

**[References]**

- [add_child and remove_child interfaces document](https://simon-ritchie.github.io/apysc/add_child_and_remove_child.html)

### remove_from_parent method docstring

Remove this instance from parent.<hr>

**[Raises]**

- ValueError: If this instance is not added to any parent.

### set_css method docstring

Set a specified value string to the CSS.<hr>

**[Parameters]**

- `name`: str or String
  - CSS name (e.g., 'display').
- `value`: str or String
  - A CSS value string (e.g., 'none').

<hr>

**[Examples]**

```py
>>> import apysc as ap
>>> stage: ap.Stage = ap.Stage()
>>> sprite: ap.Sprite = ap.Sprite()
>>> sprite.graphics.begin_fill(color='#0af', alpha=0.5)
>>> sprite.set_css(name='display', value='none')
>>> sprite.get_css(name='display')
String('none')
```

<hr>

**[References]**

- [Display object get_css and set_css interfaces document](https://simon-ritchie.github.io/apysc/display_object_get_and_set_css.html)

### trigger_custom_event method docstring

Add a custom event trigger setting.<hr>

**[Parameters]**

- `custom_event_type`: CustomEventType or str
  - Target custom event type.

<hr>

**[Examples]**

```py
>>> import apysc as ap
>>> def on_custom_event(
...         e: ap.Event[ap.Rectangle], options: dict) -> None:
...     rectangle: ap.Rectangle = e.this
...     rectangle.fill_color = ap.String('#f0a')
>>> stage: ap.Stage = ap.Stage()
>>> sprite: ap.Sprite = ap.Sprite()
>>> sprite.graphics.begin_fill(color='#0af')
>>> rectangle: ap.Rectangle = sprite.graphics.draw_rect(
...     x=50, y=50, width=50, height=50)
>>> e: ap.Event = ap.Event(this=rectangle)
>>> _ = rectangle.bind_custom_event(
...     custom_event_type='my_custom_event',
...     handler=on_custom_event, e=e)
>>> # Do something here and then trigger the custom event
>>> rectangle.trigger_custom_event(
...     custom_event_type='my_custom_event')
```

<hr>

**[References]**

- [Bind and trigger the custom event document](https://simon-ritchie.github.io/apysc/bind_and_trigger_custom_event.html)

### unbind_click method docstring

Unbind specified handler's click event.<hr>

**[Parameters]**

- `handler`: _Handler
  - Unbinding target Callable.

<hr>

**[Examples]**

```py
>>> import apysc as ap
>>> def on_click(
...         e: ap.MouseEvent[ap.Rectangle], options: dict) -> None:
...     rectangle: ap.Rectangle = e.this
...     rectangle.fill_color = ap.String('#f0a')
...     rectangle.unbind_click(on_click)
>>> stage: ap.Stage = ap.Stage()
>>> sprite: ap.Sprite = ap.Sprite()
>>> sprite.graphics.begin_fill(color='#0af')
>>> rectangle: ap.Rectangle = sprite.graphics.draw_rect(
...     x=50, y=50, width=50, height=50)
>>> _ = rectangle.click(on_click)
```

<hr>

**[References]**

- [Click interface document](https://simon-ritchie.github.io/apysc/click.html)

### unbind_click_all method docstring

Unbind all click events.<hr>

**[Examples]**

```py
>>> import apysc as ap
>>> def on_click(
...         e: ap.MouseEvent[ap.Rectangle], options: dict) -> None:
...     rectangle: ap.Rectangle = e.this
...     rectangle.fill_color = ap.String('#f0a')
...     rectangle.unbind_click_all()
>>> stage: ap.Stage = ap.Stage()
>>> sprite: ap.Sprite = ap.Sprite()
>>> sprite.graphics.begin_fill(color='#0af')
>>> rectangle: ap.Rectangle = sprite.graphics.draw_rect(
...     x=50, y=50, width=50, height=50)
>>> _ = rectangle.click(on_click)
```

<hr>

**[References]**

- [Click interface document](https://simon-ritchie.github.io/apysc/click.html)

### unbind_custom_event method docstring

Unbind (remove) a custom event listener setting.<hr>

**[Parameters]**

- `custom_event_type`: CustomEventType or str
  - Target custom event type.
- `handler`: _Handler
  - A handler for when the custom event is triggered.

<hr>

**[Returns]**

- `name`: str
  - Handler's name.

<hr>

**[Examples]**

```py
>>> import apysc as ap
>>> def on_custom_event(
...         e: ap.Event[ap.Rectangle], options: dict) -> None:
...     rectangle: ap.Rectangle = e.this
...     rectangle.fill_color = ap.String('#f0a')
...     rectangle.unbind_custom_event(
...         custom_event_type='my_custom_event',
...         handler=on_custom_event)
>>> stage: ap.Stage = ap.Stage()
>>> sprite: ap.Sprite = ap.Sprite()
>>> sprite.graphics.begin_fill(color='#0af')
>>> rectangle: ap.Rectangle = sprite.graphics.draw_rect(
...     x=50, y=50, width=50, height=50)
>>> e: ap.Event = ap.Event(this=rectangle)
>>> _ = rectangle.bind_custom_event(
...     custom_event_type='my_custom_event',
...     handler=on_custom_event, e=e)
>>> # Do something here and then trigger the custom event
>>> rectangle.trigger_custom_event(
...     custom_event_type='my_custom_event')
```

### unbind_custom_event_all method docstring

Unbind (remove) custom event listener settings.<hr>

**[Parameters]**

- `custom_event_type`: CustomEventType or str
  - Target custom event type.

<hr>

**[Examples]**

```py
>>> import apysc as ap
>>> def on_custom_event(
...         e: ap.Event[ap.Rectangle], options: dict) -> None:
...     rectangle: ap.Rectangle = e.this
...     rectangle.fill_color = ap.String('#f0a')
...     rectangle.unbind_custom_event_all(
...         custom_event_type='my_custom_event')
>>> stage: ap.Stage = ap.Stage()
>>> sprite: ap.Sprite = ap.Sprite()
>>> sprite.graphics.begin_fill(color='#0af')
>>> rectangle: ap.Rectangle = sprite.graphics.draw_rect(
...     x=50, y=50, width=50, height=50)
>>> e: ap.Event = ap.Event(this=rectangle)
>>> _ = rectangle.bind_custom_event(
...     custom_event_type='my_custom_event',
...     handler=on_custom_event, e=e)
>>> # Do something here and then trigger the custom event
>>> rectangle.trigger_custom_event(
...     custom_event_type='my_custom_event')
```

### unbind_dblclick method docstring

Unbind a specified handler's double click event.<hr>

**[Parameters]**

- `handler`: _Handler
  - Unbinding target Callable.

<hr>

**[Examples]**

```py
>>> import apysc as ap
>>> def on_double_click(
...         e: ap.MouseEvent[ap.Rectangle], options: dict) -> None:
...     rectangle: ap.Rectangle = e.this
...     rectangle.fill_color = ap.String('#f0a')
...     rectangle.unbind_dblclick(on_double_click)
>>> stage: ap.Stage = ap.Stage()
>>> sprite: ap.Sprite = ap.Sprite()
>>> sprite.graphics.begin_fill(color='#0af')
>>> rectangle: ap.Rectangle = sprite.graphics.draw_rect(
...     x=50, y=50, width=50, height=50)
>>> _ = rectangle.dblclick(on_double_click)
```

### unbind_dblclick_all method docstring

Unbind all double click events.<hr>

**[Examples]**

```py
>>> import apysc as ap
>>> def on_double_click(
...         e: ap.MouseEvent[ap.Rectangle], options: dict) -> None:
...     rectangle: ap.Rectangle = e.this
...     rectangle.fill_color = ap.String('#f0a')
...     rectangle.unbind_dblclick_all()
>>> stage: ap.Stage = ap.Stage()
>>> sprite: ap.Sprite = ap.Sprite()
>>> sprite.graphics.begin_fill(color='#0af')
>>> rectangle: ap.Rectangle = sprite.graphics.draw_rect(
...     x=50, y=50, width=50, height=50)
>>> _ = rectangle.dblclick(on_double_click)
```

### unbind_mousedown method docstring

Unbind a specified handler's mouse down event.<hr>

**[Parameters]**

- `handler`: _Handler
  - Unbinding target Callable.

<hr>

**[Examples]**

```py
>>> import apysc as ap
>>> def on_mousedown(
...         e: ap.MouseEvent[ap.Rectangle], options: dict) -> None:
...     rectangle: ap.Rectangle = e.this
...     rectangle.fill_color = ap.String('#f0a')
...     rectangle.unbind_mousedown(on_mousedown)
>>> stage: ap.Stage = ap.Stage()
>>> sprite: ap.Sprite = ap.Sprite()
>>> sprite.graphics.begin_fill(color='#0af')
>>> rectangle: ap.Rectangle = sprite.graphics.draw_rect(
...     x=50, y=50, width=50, height=50)
>>> _ = rectangle.mousedown(on_mousedown)
```

<hr>

**[References]**

- [Mousedown and mouseup interfaces document](https://simon-ritchie.github.io/apysc/mousedown_and_mouseup.html)

### unbind_mousedown_all method docstring

Unbind all mouse down events.<hr>

**[Examples]**

```py
>>> import apysc as ap
>>> def on_mousedown(
...         e: ap.MouseEvent[ap.Rectangle], options: dict) -> None:
...     rectangle: ap.Rectangle = e.this
...     rectangle.fill_color = ap.String('#f0a')
...     rectangle.unbind_mousedown_all()
>>> stage: ap.Stage = ap.Stage()
>>> sprite: ap.Sprite = ap.Sprite()
>>> sprite.graphics.begin_fill(color='#0af')
>>> rectangle: ap.Rectangle = sprite.graphics.draw_rect(
...     x=50, y=50, width=50, height=50)
>>> _ = rectangle.mousedown(on_mousedown)
```

<hr>

**[References]**

- [Mousedown and mouseup interfaces document](https://simon-ritchie.github.io/apysc/mousedown_and_mouseup.html)

### unbind_mousemove method docstring

Unbind a specified handler's mouse move event.<hr>

**[Parameters]**

- `handler`: _Handler
  - Unbinding target Callable.

<hr>

**[Examples]**

```py
>>> import apysc as ap
>>> def on_mousemove(
...         e: ap.MouseEvent[ap.Rectangle], options: dict) -> None:
...     stage_x: ap.Int = e.stage_x
...     ap.trace('stage_x:', stage_x)
>>> def on_click(
...         e: ap.MouseEvent[ap.Rectangle], options: dict) -> None:
...     rectangle: ap.Rectangle = e.this
...     rectangle.unbind_mousemove(on_mousemove)
>>> stage: ap.Stage = ap.Stage()
>>> sprite: ap.Sprite = ap.Sprite()
>>> sprite.graphics.begin_fill(color='#0af')
>>> rectangle: ap.Rectangle = sprite.graphics.draw_rect(
...     x=50, y=50, width=50, height=50)
>>> _ = rectangle.mousemove(on_mousemove)
>>> _ = rectangle.click(on_click)
```

<hr>

**[References]**

- [Mousemove interface document](https://simon-ritchie.github.io/apysc/mousemove.html)

### unbind_mousemove_all method docstring

Unbind all mouse move events.<hr>

**[Examples]**

```py
>>> import apysc as ap
>>> def on_mousemove(
...         e: ap.MouseEvent[ap.Rectangle], options: dict) -> None:
...     stage_x: ap.Int = e.stage_x
...     ap.trace('stage_x:', stage_x)
>>> def on_click(
...         e: ap.MouseEvent[ap.Rectangle], options: dict) -> None:
...     rectangle: ap.Rectangle = e.this
...     rectangle.unbind_mousemove_all()
>>> stage: ap.Stage = ap.Stage()
>>> sprite: ap.Sprite = ap.Sprite()
>>> sprite.graphics.begin_fill(color='#0af')
>>> rectangle: ap.Rectangle = sprite.graphics.draw_rect(
...     x=50, y=50, width=50, height=50)
>>> _ = rectangle.mousemove(on_mousemove)
>>> _ = rectangle.click(on_click)
```

<hr>

**[References]**

- [Mousemove interface document](https://simon-ritchie.github.io/apysc/mousemove.html)

### unbind_mouseout method docstring

Unbind a specified handler's mouse out event.<hr>

**[Parameters]**

- `handler`: _Handler
  - Unbinding target Callable.

<hr>

**[Examples]**

```py
>>> import apysc as ap
>>> def on_mouseout(
...         e: ap.MouseEvent[ap.Rectangle], options: dict) -> None:
...     rectangle: ap.Rectangle = e.this
...     rectangle.fill_color = ap.String('#f0a')
...     rectangle.unbind_mouseout(on_mouseout)
>>> stage: ap.Stage = ap.Stage()
>>> sprite: ap.Sprite = ap.Sprite()
>>> sprite.graphics.begin_fill(color='#0af')
>>> rectangle: ap.Rectangle = sprite.graphics.draw_rect(
...     x=50, y=50, width=50, height=50)
>>> _ = rectangle.mouseout(on_mouseout)
```

<hr>

**[References]**

- [Mouseover and mouseout interfaces](https://simon-ritchie.github.io/apysc/mouseover_and_mouseout.html)

### unbind_mouseout_all method docstring

Unbind all mouse out events.<hr>

**[Examples]**

```py
>>> import apysc as ap
>>> def on_mouseout(
...         e: ap.MouseEvent[ap.Rectangle], options: dict) -> None:
...     rectangle: ap.Rectangle = e.this
...     rectangle.fill_color = ap.String('#f0a')
...     rectangle.unbind_mouseout_all()
>>> stage: ap.Stage = ap.Stage()
>>> sprite: ap.Sprite = ap.Sprite()
>>> sprite.graphics.begin_fill(color='#0af')
>>> rectangle: ap.Rectangle = sprite.graphics.draw_rect(
...     x=50, y=50, width=50, height=50)
>>> _ = rectangle.mouseout(on_mouseout)
```

<hr>

**[References]**

- [Mouseover and mouseout interfaces](https://simon-ritchie.github.io/apysc/mouseover_and_mouseout.html)

### unbind_mouseover method docstring

Unbind a specified handler's mouseover event.<hr>

**[Parameters]**

- `handler`: _Handler
  - Unbinding target Callable.

<hr>

**[Examples]**

```py
>>> import apysc as ap
>>> def on_mouseover(
...         e: ap.MouseEvent[ap.Rectangle], options: dict) -> None:
...     rectangle: ap.Rectangle = e.this
...     rectangle.fill_color = ap.String('#f0a')
...     rectangle.unbind_mouseover(on_mouseover)
>>> stage: ap.Stage = ap.Stage()
>>> sprite: ap.Sprite = ap.Sprite()
>>> sprite.graphics.begin_fill(color='#0af')
>>> rectangle: ap.Rectangle = sprite.graphics.draw_rect(
...     x=50, y=50, width=50, height=50)
>>> _ = rectangle.mouseout(on_mouseover)
```

<hr>

**[References]**

- [Mouseover and mouseout interfaces](https://simon-ritchie.github.io/apysc/mouseover_and_mouseout.html)

### unbind_mouseover_all method docstring

Unbind all mouseover events.<hr>

**[Examples]**

```py
>>> import apysc as ap
>>> def on_mouseover(
...         e: ap.MouseEvent[ap.Rectangle], options: dict) -> None:
...     rectangle: ap.Rectangle = e.this
...     rectangle.fill_color = ap.String('#f0a')
...     rectangle.unbind_mouseover_all()
>>> stage: ap.Stage = ap.Stage()
>>> sprite: ap.Sprite = ap.Sprite()
>>> sprite.graphics.begin_fill(color='#0af')
>>> rectangle: ap.Rectangle = sprite.graphics.draw_rect(
...     x=50, y=50, width=50, height=50)
>>> _ = rectangle.mouseout(on_mouseover)
```

<hr>

**[References]**

- [Mouseover and mouseout interfaces](https://simon-ritchie.github.io/apysc/mouseover_and_mouseout.html)

### unbind_mouseup method docstring

Unbind a specified handler's mouse-up event.<hr>

**[Parameters]**

- `handler`: _Handler
  - Unbinding target Callable.

<hr>

**[Examples]**

```py
>>> import apysc as ap
>>> def on_mouseup(
...         e: ap.MouseEvent[ap.Rectangle], options: dict) -> None:
...     rectangle: ap.Rectangle = e.this
...     rectangle.fill_color = ap.String('#f0a')
...     rectangle.unbind_mouseup(on_mouseup)
>>> stage: ap.Stage = ap.Stage()
>>> sprite: ap.Sprite = ap.Sprite()
>>> sprite.graphics.begin_fill(color='#0af')
>>> rectangle: ap.Rectangle = sprite.graphics.draw_rect(
...     x=50, y=50, width=50, height=50)
>>> _ = rectangle.mouseup(on_mouseup)
```

<hr>

**[References]**

- [Mousedown and mouseup interfaces document](https://simon-ritchie.github.io/apysc/mousedown_and_mouseup.html)

### unbind_mouseup_all method docstring

Unbind all mouse up events.<hr>

**[Examples]**

```py
>>> import apysc as ap
>>> def on_mouseup(
...         e: ap.MouseEvent[ap.Rectangle], options: dict) -> None:
...     rectangle: ap.Rectangle = e.this
...     rectangle.fill_color = ap.String('#f0a')
...     rectangle.unbind_mouseup_all()
>>> stage: ap.Stage = ap.Stage()
>>> sprite: ap.Sprite = ap.Sprite()
>>> sprite.graphics.begin_fill(color='#0af')
>>> rectangle: ap.Rectangle = sprite.graphics.draw_rect(
...     x=50, y=50, width=50, height=50)
>>> _ = rectangle.mouseup(on_mouseup)
```

<hr>

**[References]**

- [Mousedown and mouseup interfaces document](https://simon-ritchie.github.io/apysc/mousedown_and_mouseup.html)

## GraphicsBase class docstring



### ABCMeta method docstring

Metaclass for defining Abstract Base Classes (ABCs). Use this metaclass to create an ABC. An ABC can be subclassed directly, and then acts as a mix-in class. You can also register unrelated concrete classes (even built-in classes) and unrelated ABCs as 'virtual subclasses' -- these and their descendants will be considered subclasses of the registering ABC by the built-in issubclass() function, but the registering ABC won't show up in their MRO (Method Resolution Order) nor will method implementations defined by the registering ABC be callable (not even via super()).

### __init__ method docstring

Vector graphic base class.<hr>

**[Parameters]**

- `parent`: Graphics
  - Parent `Graphics` instance.
- `x`: int or Int
  - X position.
- `y`: int or Int
  - Y position.
- `variable_name`: str
  - Variable name of this instance. This will be used to js expression.

### _animation_skew_y method docstring

**Important notes** Currently this interface does not work correctly. For more details please see: https://github.com/svgdotjs/svg.js/issues/1222 Set the skew-y animation animation.<hr>

**[Parameters]**

- `skew_y`: int or Int
  - The final skew-y of the animation.
- `duration`: int or Int, default 3000
  - Milliseconds before an animation ends.
- `delay`: int or Int, default 0
  - Milliseconds before an animation starts.
- `easing`: Easing, default Easing.LINEAR
  - Easing setting.

<hr>

**[Returns]**

- `animation_skew_y`: AnimationSkewY
  - Created animation setting instance.

<hr>

**[Notes]**

To start this animation, you need to call the `start` method of the returned instance.<hr>

**[Examples]**

```py
>>> import apysc as ap
>>> stage: ap.Stage = ap.Stage()
>>> sprite: ap.Sprite = ap.Sprite()
>>> sprite.graphics.begin_fill(color='#0af')
>>> rectangle: ap.Rectangle = sprite.graphics.draw_rect(
...     x=50, y=50, width=50, height=50)
>>> _ = rectangle._animation_skew_y(
...     skew_y=50,
...     duration=1500,
...     easing=ap.Easing.EASE_OUT_QUINT,
... ).start()
```

<hr>

**[References]**

- [Animation interfaces duration setting document](https://simon-ritchie.github.io/apysc/animation_duration.html)
- [Animation interfaces delay setting document](https://simon-ritchie.github.io/apysc/animation_delay.html)
- [Each animation interface return value document](https://simon-ritchie.github.io/apysc/animation_return_value.html)
- [Sequential animation setting document](https://simon-ritchie.github.io/apysc/sequential_animation.html)
- [animation_parallel interface document](https://simon-ritchie.github.io/apysc/animation_parallel.html)
- [Easing enum document](https://simon-ritchie.github.io/apysc/easing_enum.html)

### _append_applying_new_attr_val_exp method docstring

Append the expression of applying new attribute value to each stacked value.<hr>

**[Parameters]**

- `new_attr`: Int or Number or String or Boolean
  - New attribute value.
- `attr_name`: str
  - Target attribute name.

### _append_attr_to_linking_stack method docstring

Append an attribute to the linking attribute stack.<hr>

**[Parameters]**

- `attr`: Int or Number or String or Boolean
  - Target attribute to be appended.
- `attr_name`: str
  - Target attribute name.

### _append_custom_event_binding_expression method docstring

Append a custom event binding expression.<hr>

**[Parameters]**

- `custom_event_type_str`: str
  - Target custom event type string.
- `name`: str
  - Handler's name.

### _append_custom_event_unbinding_expression method docstring

Add a custom event unbinding expression.<hr>

**[Parameters]**

- `custom_event_type_str`: str
  - Target custom event type string.
- `name`: str
  - Handler's name.

### _append_flip_x_attr_linking_setting method docstring

Append a flip-x attribute linking setting.

### _append_flip_x_update_expression method docstring

Append a x-axis flipping value updating expression.<hr>

**[Parameters]**

- `before_value`: Boolean
  - Before updating flipping value.

### _append_flip_y_attr_linking_setting method docstring

Append a flip-y attribute linking setting.

### _append_flip_y_update_expression method docstring

Append a y-axis flipping value updating expression.<hr>

**[Parameters]**

- `before_value`: Boolean
  - Before updating flipping value.

### _append_get_css_expresion method docstring

Append a css getter expression string.<hr>

**[Parameters]**

- `name`: str or String
  - CSS name (e.g., 'display').
- `css`: String
  - CSS value.

### _append_mouse_event_binding_expression method docstring

Append a mouse event binding expression.<hr>

**[Parameters]**

- `name`: str
  - Handler's name.
- `mouse_event_type`: MouseEventType
  - Event type to bind.

### _append_rotation_around_center_attr_linking_setting method docstring

Append a rotation around center attribute linking setting.

### _append_rotation_around_center_update_expression method docstring

Append the rotation around the center of this instance updating expression.<hr>

**[Parameters]**

- `before_value`: ap.Int
  - Before updating value.

### _append_rotation_around_point_update_expression method docstring

Append a rotation value around the given coordinates updating expression.<hr>

**[Parameters]**

- `rotation`: Int
  - Rotation value to set.
- `x`: Int
  - X-coordinate.
- `y`: Int
  - Y-coordinate.

### _append_scale_x_from_center_attr_linking_setting method docstring

Append a scale-x attribute linking setting.

### _append_scale_x_from_center_update_expression method docstring

Append the scale-x from the center of this instance updating expression.<hr>

**[Parameters]**

- `before_value`: ap.Number
  - Before updating value.

### _append_scale_x_from_point_update_expression method docstring

Append the scale-x from the specified x-coordinate updating expression.<hr>

**[Parameters]**

- `x`: Int
  - X-coordinate.

### _append_scale_y_from_center_attr_linking_setting method docstring

Append a scale-y attribute linking setting.

### _append_scale_y_from_center_update_expression method docstring

Append the scale-y from the center of this instance updating expression.<hr>

**[Parameters]**

- `before_value`: ap.Number
  - Before updating value.

### _append_scale_y_from_point_update_expression method docstring

Append the scale-y from the specified y-coordinate updating expression.<hr>

**[Parameters]**

- `y`: Int
  - Y-coordinate.

### _append_set_css_expression method docstring

Append a css setter expression string.<hr>

**[Parameters]**

- `name`: str or String
  - CSS name (e.g., 'display').
- `value`: str or String
  - A CSS value string (e.g., 'none').

### _append_skew_x_attr_linking_setting method docstring

Append a skew-x attribute linking setting.

### _append_skew_x_update_expression method docstring

Append the skew x updating expression.<hr>

**[Parameters]**

- `before_value`: ap.Int
  - Before updating value.

### _append_skew_y_attr_linking_setting method docstring

Append a skew-y attribute linking setting.

### _append_skew_y_update_expression method docstring

Append the skew y updating expression.<hr>

**[Parameters]**

- `before_value`: ap.Int
  - Before updating value.

### _append_visible_attr_linking_setting method docstring

Append a visible attribute linking setting.

### _append_visible_update_expression method docstring

Append visible property updating expression.

### _append_x_attr_linking_setting method docstring

Append a x attribute linking setting.

### _append_x_update_expression method docstring

Append the x position updating expression.

### _append_y_attr_linking_setting method docstring

Append a y attribute linking setting.

### _append_y_update_expression method docstring

Append y position updating expression.

### _delete_snapshot_exists_val method docstring

Delete boolean value whether snapshot value exists or not.<hr>

**[Parameters]**

- `snapshot_name`: str
  - Target snapshot name.

### _get_custom_event_type_str method docstring

Get a custom event type string from a type value.<hr>

**[Parameters]**

- `custom_event_type`: CustomEventType or str
  - Target custom event type or string.

<hr>

**[Returns]**

- `custom_event_type_str`: str
  - A custom event type string.

### _get_next_snapshot_name method docstring

Get a next snapshot name.<hr>

**[Returns]**

- `snapshot_name`: str
  - Next snapshot name.

### _get_previous_variable_name method docstring

Get a previous variable name.<hr>

**[Returns]**

- `previous_variable_name`: str
  - A previous variable name of this instance. If that value is not existing, then a blank string will be returned.

### _get_rotation_around_point_updating_expression method docstring

Get a rotation value around the given coordinates updating expression string.<hr>

**[Parameters]**

- `rotation`: Int
  - Rotation value to set.
- `x`: Int
  - X-coordinate.
- `y`: Int
  - Y-coordinate.

<hr>

**[Returns]**

- `expression`: str
  - A rotation value around the given coordinates updating expression string.

### _initialize_attr_linking_stack method docstring

Initialize the _attr_linking_stack attribute if it hasn't been initialized yet.<hr>

**[Parameters]**

- `attr_name`: str
  - Target attribute name.

### _initialize_blank_object_if_not_initialized method docstring

Initialize a blank object value if it hasn't been initialized yet.

### _initialize_click_handlers_if_not_initialized method docstring

Initialize _click_handlers attribute if it hasn't been initialized yet.

### _initialize_css_if_not_initialized method docstring

Initialize the _css attribute if it hasn't been initialized yet.

### _initialize_custom_event_handlers_if_not_initialized method docstring

Initialize the _custom_event_handlers data if it hasn't been initialized yet.<hr>

**[Parameters]**

- `custom_event_type_str`: str
  - Target custom event type string.

### _initialize_dblclick_handlers_if_not_initialized method docstring

Initialize _dblclick_handlers attribute if it is not initialized yet.

### _initialize_flip_x_if_not_initialized method docstring

Initialize the _flip_x attribute if it hasn't been initialized yet.

### _initialize_flip_y_if_not_initialized method docstring

Initialize the _flip_y attribute if it hasn't been initialized yet.

### _initialize_mouse_down_handlers_if_not_initialized method docstring

Initialize _mouse_down_handlers attribute if it is not initialized yet.

### _initialize_mouse_move_handlers_if_not_initialized method docstring

Initialize _mouse_move_handlers attribute if it is not initialized yet.

### _initialize_mouse_out_handlers_if_not_initialized method docstring

Initialize _mouse_out_handlers attribute if it is not initialized yet.

### _initialize_mouse_over_handlers_if_not_initialized method docstring

Initialize _mouse_over_handlers attribute if it is not initialized yet.

### _initialize_mouse_up_handlers_if_not_initialized method docstring

Initialize _mouse_up_handlers attribute if it is not initialized yet.

### _initialize_rotation_around_center_if_not_initialized method docstring

Initialize the `_rotation_around_center` attribute if if hasn't been initialized yet.

### _initialize_rotation_around_point_if_not_initialized method docstring

Initialize the `_rotation_around_point` attribute if it hasn't been initialized yet.

### _initialize_scale_x_from_center_if_not_initialized method docstring

Initialize the `_scale_x_from_center` attribute if it hasn't been initialized yet.

### _initialize_scale_x_from_point_if_not_initialized method docstring

Initialize the `_scale_x_from_point` attribute if it hasn't been initialized yet.

### _initialize_scale_y_from_center_if_not_initialized method docstring

Initialize the `_scale_y_from_center` attribute if it hasn't been initialized yet.'

### _initialize_scale_y_from_point_if_not_initialized method docstring

Initialize the `_scale_y_from_point` attribute if it hasn't been initialized yet.

### _initialize_skew_x_if_not_initialized method docstring

Initialize the _skew_x attribute if it hasn't been initialized yet.

### _initialize_skew_y_if_not_initialized method docstring

Initialize the _skew_y attribute if it hasn't been initialized yet.

### _initialize_ss_exists_val_if_not_initialized method docstring

Initialize _snapshot_exists_ value it hasn't been initialized yet.

### _initialize_visible_if_not_initialized method docstring

Initialize _visible attribute if it hasn't been initialized yet.

### _initialize_x_if_not_initialized method docstring

Initialize the _x attribute if it hasn't been initialized yet.

### _initialize_y_if_not_initialized method docstring

Initialize the _y attribute if it hasn't been initialized yet.

### _is_target_attr_already_linked method docstring

Get a boolean value whether a specified attribute has already been appended to the linking attribute stack.<hr>

**[Parameters]**

- `attr`: Int or Number or String or Boolean
  - Target attribute to be appended.
- `attr_name`: str
  - Target attribute name.

<hr>

**[Returns]**

- `result`: bool
  - If a specified attribute has already been appended to the linking stack, this value will be True.

### _make_snapshot method docstring

Make a value's snapshot.<hr>

**[Parameters]**

- `snapshot_name`: str
  - Target snapshot name.

### _revert method docstring

Revert a value if snapshot exists.<hr>

**[Parameters]**

- `snapshot_name`: str
  - Target snapshot name.

### _run_all_make_snapshot_methods method docstring

Run all _make_snapshot methods. If instance is multiple inheritance one, and each has RevertInterface, then each _make_snapshot methods will be called.<hr>

**[Parameters]**

- `snapshot_name`: str
  - Target snapshot name.

### _run_all_revert_methods method docstring

Run all _revert methods. If instance is multiple inheritance one, and each has RevertInterface, then each _revert methods will be called.<hr>

**[Parameters]**

- `snapshot_name`: str
  - Target snapshot name.

### _run_base_cls_make_snapshot_methods_recursively method docstring

Run base classes make_snapshot methods recursively.<hr>

**[Parameters]**

- `class_`: type
  - Target type.
- `snapshot_name`: str
  - Target snapshot name.

### _run_base_cls_revert_methods_recursively method docstring

Run base classes revert methods recursively.<hr>

**[Parameters]**

- `class_`: type
  - Target type.
- `snapshot_name`: str
  - Target snapshot name.

### _set_custom_event_handler_data method docstring

Set a handler's data to the dictionary.<hr>

**[Parameters]**

- `handler`: _Handler
  - Callable will be called when an event is dispatched.
- `custom_event_type_str`: str
  - Target custom event type string.
- `options`: dict or None
  - Optional arguments dictionary to be passed to a handler.

### _set_mouse_event_handler_data method docstring

Set a handler's data to the given dictionary.<hr>

**[Parameters]**

- `handler`: _Handler
  - Callable would be called when event is dispatched.
- `handlers_dict`: dict
  - Dictionary to be set handler's data.
- `options`: dict or None
  - Optional arguments dictionary to be passed to handler.

### _set_overflow_visible_setting method docstring

Set the `visible` value to the `overflow` CSS property.

### _set_single_snapshot_val_to_dict method docstring

Set a single snapshot value to the specified name dictionary.<hr>

**[Parameters]**

- `dict_name`: str
  - Target dictionary name.
- `value`: Any
  - Target value.
- `snapshot_name`: str
  - Target snapshot name.

<hr>

**[Notes]**

If a snapshot value of the same name already exists, the process will be stopped.

### _set_snapshot_exists_val method docstring

Set boolean value whether snapshot value exists or not.<hr>

**[Parameters]**

- `snapshot_name`: str
  - Target snapshot name.

### _snapshot_exists method docstring

Get a boolean value whether snapshot value exists or not.<hr>

**[Parameters]**

- `snapshot_name`: str
  - Target snapshot name.

<hr>

**[Returns]**

- `snapshot_exists`: bool
  - Boolean value whether snapshot value exists or not.

### _unbind_all_mouse_events method docstring

Unbind specified all mouse event type's event.<hr>

**[Parameters]**

- `mouse_event_type`: MouseEventType
  - Event type to unbind.
- `handlers_dict`: dict
  - Dictionary that has handler's data.

### _unbind_mouse_event method docstring

Unbind specified handler's mouse event.<hr>

**[Parameters]**

- `handler`: _Handler
  - Unbinding target Callable.
- `mouse_event_type`: MouseEventType
  - Event type to unbind.
- `handlers_dict`: dict
  - Dictionary that has handler's data.

### _unset_custom_event_handler_data method docstring

Unset a handler's data from the dictionary.<hr>

**[Parameters]**

- `handler`: _Handler
  - Callable will be called when an event is dispatched.
- `custom_event_type_str`: str
  - Target custom event type string.

### animation_finish method docstring

Finish all animations (set the animation last value to each attribute).<hr>

**[Examples]**

```py
>>> from typing_extensions import TypedDict
>>> import apysc as ap
>>> class RectOptions(TypedDict):
...     rectangle: ap.Rectangle
>>> def on_timer(
...         e: ap.TimerEvent,
...         options: RectOptions) -> None:
...     rectangle: ap.Rectangle = options['rectangle']
...     rectangle.animation_finish()
>>> stage: ap.Stage = ap.Stage()
>>> sprite: ap.Sprite = ap.Sprite()
>>> sprite.graphics.begin_fill(color='#0af')
>>> rectangle: ap.Rectangle = sprite.graphics.draw_rect(
...     x=50, y=50, width=50, height=50)
>>> _ = rectangle.animation_x(
...     x=100,
...     duration=1500,
...     easing=ap.Easing.EASE_OUT_QUINT,
... ).start()
>>> options: RectOptions = {'rectangle': rectangle}
>>> ap.Timer(on_timer, delay=750, options=options).start()
```

<hr>

**[References]**

- [animation_finish interface document](https://simon-ritchie.github.io/apysc/animation_finish.html)

### animation_move method docstring

Set the x and y coordinates animation settings.<hr>

**[Parameters]**

- `x`: Int or int
  - Destination of the x-coordinate.
- `y`: Int or int
  - Destination of the y-coordinate.
- `duration`: Int or int, default 3000
  - Milliseconds before an animation ends.
- `delay`: Int or int, default 0
  - Milliseconds before an animation starts.
- `easing`: Easing, default Easing.LINEAR
  - Easing setting.

<hr>

**[Returns]**

- `animation_move`: AnimationMove
  - Created animation setting instance.

<hr>

**[Notes]**

To start this animation, you need to call the `start` method of the returned instance.<hr>

**[Examples]**

```py
>>> import apysc as ap
>>> stage: ap.Stage = ap.Stage()
>>> sprite: ap.Sprite = ap.Sprite()
>>> sprite.graphics.begin_fill(color='#0af')
>>> sprite.graphics.line_style(
...     color='#fff', thickness=1)
>>> rectangle: ap.Rectangle = sprite.graphics.draw_rect(
...     x=50, y=50, width=50, height=50)
>>> _ = rectangle.animation_move(
...     x=100, y=150,
...     duration=1500,
...     easing=ap.Easing.EASE_OUT_QUINT,
... ).start()
```

<hr>

**[References]**

- [animation_move interface document](https://simon-ritchie.github.io/apysc/animation_move.html)
- [Animation interfaces duration setting document](https://simon-ritchie.github.io/apysc/animation_duration.html)
- [Animation interfaces delay setting document](https://simon-ritchie.github.io/apysc/animation_delay.html)
- [Each animation interface return value document](https://simon-ritchie.github.io/apysc/animation_return_value.html)
- [Sequential animation setting document](https://simon-ritchie.github.io/apysc/sequential_animation.html)
- [animation_parallel interface document](https://simon-ritchie.github.io/apysc/animation_parallel.html)
- [Easing enum document](https://simon-ritchie.github.io/apysc/easing_enum.html)

### animation_parallel method docstring

Set the parallel animation setting.<hr>

**[Parameters]**

- `animations`: list of AnimationBase
  - Target animation settings.
- `duration`: Int or int, default 3000
  - Milliseconds before an animation ends.
- `delay`: Int or int, default 0
  - Milliseconds before an animation starts.
- `easing`: Easing, default Easing.LINEAR
  - Easing setting.

<hr>

**[Returns]**

- `animation_parallel`: AnimationParallel
  - Created animation setting instance.

<hr>

**[Raises]**

- ValueError: <br> ・If the animations' target is not this instance. <br> ・If there are changed duration, delay, or easing animation settings in the `animations` list.

<hr>

**[Notes]**

 ・To start this animation, you need to call the `start` method of the returned instance. <br> ・The `animations` argument can't contains the `AnimationParallel` instance. <br> ・This interface ignores the duration, delay, and easing arguments in the `animations` argument (this interface uses self-arguments instead).<hr>

**[Examples]**

```py
>>> import apysc as ap
>>> stage: ap.Stage = ap.Stage()
>>> sprite: ap.Sprite = ap.Sprite()
>>> sprite.graphics.begin_fill(color='#0af')
>>> rectangle: ap.Rectangle = sprite.graphics.draw_rect(
...     x=50, y=50, width=50, height=50)
>>> _ = rectangle.animation_parallel(
...     animations=[
...         rectangle.animation_x(x=100),
...         rectangle.animation_fill_color(fill_color='#f0a'),
...         rectangle.animation_fill_alpha(alpha=0.5),
...     ],
...     duration=1500,
...     easing=ap.Easing.EASE_OUT_QUINT,
... ).start()
```

<hr>

**[References]**

- [Animation interfaces duration setting document](https://simon-ritchie.github.io/apysc/animation_duration.html)
- [Animation interfaces delay setting document](https://simon-ritchie.github.io/apysc/animation_delay.html)
- [Each animation interface return value document](https://simon-ritchie.github.io/apysc/animation_return_value.html)
- [Sequential animation setting document](https://simon-ritchie.github.io/apysc/sequential_animation.html)
- [animation_parallel interface document](https://simon-ritchie.github.io/apysc/animation_parallel.html)
- [Easing enum document](https://simon-ritchie.github.io/apysc/easing_enum.html)

### animation_pause method docstring

Stop the all animations.<hr>

**[Examples]**

```py
>>> from typing_extensions import TypedDict
>>> import apysc as ap
>>> class RectOptions(TypedDict):
...     rectangle: ap.Rectangle
>>> def on_timer(
...         e: ap.TimerEvent,
...         options: RectOptions) -> None:
...     rectangle: ap.Rectangle = options['rectangle']
...     rectangle.animation_pause()
>>> stage: ap.Stage = ap.Stage()
>>> sprite: ap.Sprite = ap.Sprite()
>>> sprite.graphics.begin_fill(color='#0af')
>>> rectangle: ap.Rectangle = sprite.graphics.draw_rect(
...     x=50, y=50, width=50, height=50)
>>> _ = rectangle.animation_x(
...     x=100,
...     duration=1500,
...     easing=ap.Easing.EASE_OUT_QUINT,
... ).start()
>>> options: RectOptions = {'rectangle': rectangle}
>>> ap.Timer(on_timer, delay=750, options=options).start()
```

<hr>

**[References]**

- [animation_pause and animation_play interfaces document](https://simon-ritchie.github.io/apysc/animation_pause_and_play.html)

### animation_play method docstring

Restart the all paused animations.<hr>

**[Examples]**

```py
>>> from typing_extensions import TypedDict
>>> import apysc as ap
>>> class RectOptions(TypedDict):
...     rectangle: ap.Rectangle
>>> def on_timer_1(
...         e: ap.TimerEvent,
...         options: RectOptions) -> None:
...     rectangle: ap.Rectangle = options['rectangle']
...     rectangle.animation_pause()
>>> def on_timer_2(
...         e: ap.TimerEvent,
...         options: RectOptions) -> None:
...     rectangle: ap.Rectangle = options['rectangle']
...     rectangle.animation_play()
>>> stage: ap.Stage = ap.Stage()
>>> sprite: ap.Sprite = ap.Sprite()
>>> sprite.graphics.begin_fill(color='#0af')
>>> rectangle: ap.Rectangle = sprite.graphics.draw_rect(
...     x=50, y=50, width=50, height=50)
>>> _ = rectangle.animation_x(
...     x=100,
...     duration=1500,
...     easing=ap.Easing.EASE_OUT_QUINT,
... ).start()
>>> options: RectOptions = {'rectangle': rectangle}
>>> ap.Timer(on_timer_1, delay=500, options=options).start()
>>> ap.Timer(on_timer_2, delay=1000, options=options).start()
```

<hr>

**[References]**

- [animation_pause and animation_play interfaces document](https://simon-ritchie.github.io/apysc/animation_pause_and_play.html)

### animation_reset method docstring

Stop the all animations and reset.<hr>

**[Examples]**

```py
>>> from typing_extensions import TypedDict
>>> import apysc as ap
>>> class RectOptions(TypedDict):
...     rectangle: ap.Rectangle
>>> def on_timer(
...         e: ap.TimerEvent,
...         options: RectOptions) -> None:
...     rectangle: ap.Rectangle = options['rectangle']
...     rectangle.animation_reset()
>>> stage: ap.Stage = ap.Stage()
>>> sprite: ap.Sprite = ap.Sprite()
>>> sprite.graphics.begin_fill(color='#0af')
>>> rectangle: ap.Rectangle = sprite.graphics.draw_rect(
...     x=50, y=50, width=50, height=50)
>>> _ = rectangle.animation_x(
...     x=100,
...     duration=1500,
...     easing=ap.Easing.EASE_OUT_QUINT,
... ).start()
>>> options: RectOptions = {'rectangle': rectangle}
>>> ap.Timer(on_timer, delay=750, options=options).start()
```

<hr>

**[References]**

- [animation_reset interface document](https://simon-ritchie.github.io/apysc/animation_reset.html)

### animation_reverse method docstring

Reverse the all running animations.<hr>

**[Notes]**

Suppose you call this interface multiple times and animations reach the beginning or end of the animation. In that case, this interface ignores the reverse instruction. This behavior means that the same interval's timer tick reverse setting does not work correctly (since the same interval setting reaches the animation start).<hr>

**[Examples]**

```py
>>> from typing_extensions import TypedDict
>>> import apysc as ap
>>> class RectOptions(TypedDict):
...     rectangle: ap.Rectangle
>>> def on_timer(
...         e: ap.TimerEvent,
...         options: RectOptions) -> None:
...     rectangle: ap.Rectangle = options['rectangle']
...     rectangle.animation_reverse()
>>> stage: ap.Stage = ap.Stage()
>>> sprite: ap.Sprite = ap.Sprite()
>>> sprite.graphics.begin_fill(color='#0af')
>>> rectangle: ap.Rectangle = sprite.graphics.draw_rect(
...     x=50, y=50, width=50, height=50)
>>> _ = rectangle.animation_x(
...     x=100,
...     duration=1500,
...     easing=ap.Easing.EASE_OUT_QUINT,
... ).start()
>>> options: RectOptions = {'rectangle': rectangle}
>>> ap.Timer(on_timer, delay=750, options=options).start()
```

<hr>

**[References]**

- [animation_reverse interface document](https://simon-ritchie.github.io/apysc/animation_reverse.html)

### animation_rotation_around_center method docstring

Set the rotation around the center animation setting.<hr>

**[Parameters]**

- `rotation_around_center`: Int or int
  - The final rotation of the animation.
- `duration`: Int or int, default 3000
  - Milliseconds before an animation ends.
- `delay`: Int or int, default 0
  - Milliseconds before an animation starts.
- `easing`: Easing, default Easing.LINEAR
  - Easing setting.

<hr>

**[Returns]**

- `animation_rotation_around_center`: AnimationRotationAroundCenter
  - Created animation setting instance.

<hr>

**[Notes]**

To start this animation, you need to call the `start` method of the returned instance.<hr>

**[Examples]**

```py
>>> import apysc as ap
>>> stage: ap.Stage = ap.Stage()
>>> sprite: ap.Sprite = ap.Sprite()
>>> sprite.graphics.begin_fill(color='#0af')
>>> rectangle: ap.Rectangle = sprite.graphics.draw_rect(
...     x=50, y=50, width=50, height=50)
>>> _ = rectangle.animation_rotation_around_center(
...     rotation_around_center=90,
...     duration=1500,
...     easing=ap.Easing.EASE_OUT_QUINT,
... ).start()
```

<hr>

**[References]**

- [animation_rotation_around_center interface document](https://simon-ritchie.github.io/apysc/animation_rotation_around_center.html)
- [Animation interfaces duration setting document](https://simon-ritchie.github.io/apysc/animation_duration.html)
- [Animation interfaces delay setting document](https://simon-ritchie.github.io/apysc/animation_delay.html)
- [Each animation interface return value document](https://simon-ritchie.github.io/apysc/animation_return_value.html)
- [Sequential animation setting document](https://simon-ritchie.github.io/apysc/sequential_animation.html)
- [animation_parallel interface document](https://simon-ritchie.github.io/apysc/animation_parallel.html)
- [Easing enum document](https://simon-ritchie.github.io/apysc/easing_enum.html)

### animation_rotation_around_point method docstring

Set the rotation around the given point animation setting.<hr>

**[Parameters]**

- `rotation_around_point`: Int or int
  - The final rotation of the animation.
- `x`: Int or int
  - X-coordinate.
- `y`: Int or int
  - Y-coordinate.
- `duration`: Int or int, default 3000
  - Milliseconds before an animation ends.
- `delay`: Int or int, default 0
  - Milliseconds before an animation starts.
- `easing`: Easing, default Easing.LINEAR
  - Easing setting.

<hr>

**[Returns]**

- `animation_rotation_around_point`: AnimationRotationAroundPoint
  - Created animation setting instance.

<hr>

**[Notes]**

To start this animation, you need to call the `start` method of the returned instance.<hr>

**[Examples]**

```py
>>> import apysc as ap
>>> stage: ap.Stage = ap.Stage()
>>> sprite: ap.Sprite = ap.Sprite()
>>> sprite.graphics.begin_fill(color='#0af')
>>> rectangle: ap.Rectangle = sprite.graphics.draw_rect(
...     x=50, y=50, width=50, height=50)
>>> _ = rectangle.animation_rotation_around_point(
...     rotation_around_point=90,
...     x=ap.Int(100),
...     y=ap.Int(100),
...     duration=1500,
...     easing=ap.Easing.EASE_OUT_QUINT,
... ).start()
```

<hr>

**[References]**

- [animation_rotation_around_point interface document](https://simon-ritchie.github.io/apysc/animation_rotation_around_point.html)
- [Animation interfaces duration setting document](https://simon-ritchie.github.io/apysc/animation_duration.html)
- [Animation interfaces delay setting document](https://simon-ritchie.github.io/apysc/animation_delay.html)
- [Each animation interface return value document](https://simon-ritchie.github.io/apysc/animation_return_value.html)
- [Sequential animation setting document](https://simon-ritchie.github.io/apysc/sequential_animation.html)
- [animation_parallel interface document](https://simon-ritchie.github.io/apysc/animation_parallel.html)
- [Easing enum document](https://simon-ritchie.github.io/apysc/easing_enum.html)

### animation_scale_x_from_center method docstring

Set the scale-x from the center point animation setting.<hr>

**[Parameters]**

- `scale_x_from_center`: Number or float
  - The final scale-x of the animation.
- `duration`: Int or int, default 3000
  - Milliseconds before an animation ends.
- `delay`: Int or int, default 0
  - Milliseconds before an animation starts.
- `easing`: Easing, default Easing.LINEAR
  - Easing setting.

<hr>

**[Returns]**

- `animation_scale_x_from_center`: AnimationScaleXFromCenter
  - Created animation setting instance.

<hr>

**[Notes]**

To start this animation, you need to call the `start` method of the returned instance.<hr>

**[Examples]**

```py
>>> import apysc as ap
>>> stage: ap.Stage = ap.Stage()
>>> sprite: ap.Sprite = ap.Sprite()
>>> sprite.graphics.begin_fill(color='#0af')
>>> rectangle: ap.Rectangle = sprite.graphics.draw_rect(
...     x=50, y=50, width=50, height=50)
>>> _ = rectangle.animation_scale_x_from_center(
...     scale_x_from_center=0.5,
...     duration=1500,
...     easing=ap.Easing.EASE_OUT_QUINT,
... ).start()
```

<hr>

**[References]**

- [animation_scale_x_from_center interface document](https://simon-ritchie.github.io/apysc/animation_scale_x_and_y_from_center.html)
- [Animation interfaces duration setting document](https://simon-ritchie.github.io/apysc/animation_duration.html)
- [Animation interfaces delay setting document](https://simon-ritchie.github.io/apysc/animation_delay.html)
- [Each animation interface return value document](https://simon-ritchie.github.io/apysc/animation_return_value.html)
- [Sequential animation setting document](https://simon-ritchie.github.io/apysc/sequential_animation.html)
- [animation_parallel interface document](https://simon-ritchie.github.io/apysc/animation_parallel.html)
- [Easing enum document](https://simon-ritchie.github.io/apysc/easing_enum.html)

### animation_scale_x_from_point method docstring

Set the scale-x from the given point animation setting.<hr>

**[Parameters]**

- `scale_x_from_point`: float or Number
  - The final scale-x from the given point of the animation.
- `x`: int or Int
  - X-coordinate.
- `duration`: int or Int, default 3000
  - Milliseconds before an animation ends.
- `delay`: int or Int, default 0
  - Milliseconds before an animation starts.
- `easing`: Easing, default Easing.LINEAR
  - Easing setting.

<hr>

**[Returns]**

- `animation_scale_x_from_point`: AnimationScaleXFromPoint
  - Created animation setting instance.

<hr>

**[Notes]**

To start this animation, you need to call the `start` method of the returned instance.<hr>

**[Examples]**

```py
>>> import apysc as ap
>>> stage: ap.Stage = ap.Stage()
>>> sprite: ap.Sprite = ap.Sprite()
>>> sprite.graphics.begin_fill(color='#0af')
>>> rectangle: ap.Rectangle = sprite.graphics.draw_rect(
...     x=50, y=50, width=50, height=50)
>>> _ = rectangle.animation_scale_x_from_point(
...     scale_x_from_point=0.5,
...     x=ap.Int(100),
...     duration=1500,
...     easing=ap.Easing.EASE_OUT_QUINT,
... ).start()
```

<hr>

**[References]**

- [animation_scale_x_from_point interface document](https://simon-ritchie.github.io/apysc/animation_scale_x_and_y_from_point.html)
- [Animation interfaces duration setting document](https://simon-ritchie.github.io/apysc/animation_duration.html)
- [Animation interfaces delay setting document](https://simon-ritchie.github.io/apysc/animation_delay.html)
- [Each animation interface return value document](https://simon-ritchie.github.io/apysc/animation_return_value.html)
- [Sequential animation setting document](https://simon-ritchie.github.io/apysc/sequential_animation.html)
- [animation_parallel interface document](https://simon-ritchie.github.io/apysc/animation_parallel.html)
- [Easing enum document](https://simon-ritchie.github.io/apysc/easing_enum.html)

### animation_scale_y_from_center method docstring

Set the scale-y from the center point animation setting.<hr>

**[Parameters]**

- `scale_y_from_center`: Number or float
  - The final scale-y of the animation.
- `duration`: Int or int, default 3000
  - Milliseconds before an animation ends.
- `delay`: Int or int, default 0
  - Milliseconds before an animation starts.
- `easing`: Easing, default Easing.LINEAR
  - Easing setting.

<hr>

**[Returns]**

- `animation_scale_y_from_center`: AnimationScaleYFromCenter
  - Created animation setting instance.

<hr>

**[Notes]**

To start this animation, you need to call the `start` method of the returned instance.<hr>

**[Examples]**

```py
>>> import apysc as ap
>>> stage: ap.Stage = ap.Stage()
>>> sprite: ap.Sprite = ap.Sprite()
>>> sprite.graphics.begin_fill(color='#0af')
>>> rectangle: ap.Rectangle = sprite.graphics.draw_rect(
...     x=50, y=50, width=50, height=50)
>>> _ = rectangle.animation_scale_y_from_center(
...     scale_y_from_center=0.5,
...     duration=1500,
...     easing=ap.Easing.EASE_OUT_QUINT,
... ).start()
```

<hr>

**[References]**

- [animation_scale_y_from_center interface document](https://simon-ritchie.github.io/apysc/animation_scale_x_and_y_from_center.html)
- [Animation interfaces duration setting document](https://simon-ritchie.github.io/apysc/animation_duration.html)
- [Animation interfaces delay setting document](https://simon-ritchie.github.io/apysc/animation_delay.html)
- [Each animation interface return value document](https://simon-ritchie.github.io/apysc/animation_return_value.html)
- [Sequential animation setting document](https://simon-ritchie.github.io/apysc/sequential_animation.html)
- [animation_parallel interface document](https://simon-ritchie.github.io/apysc/animation_parallel.html)
- [Easing enum document](https://simon-ritchie.github.io/apysc/easing_enum.html)

### animation_scale_y_from_point method docstring

Set the scale-y from the given point animation setting.<hr>

**[Parameters]**

- `scale_y_from_point`: float or Number
  - The final scale-y from the given point of the animation.
- `y`: int or Int
  - Y-coordinate.
- `duration`: int or Int, default 3000
  - Milliseconds before an animation ends.
- `delay`: int or Int, default 0
  - Milliseconds before an animation starts.
- `easing`: Easing, default Easing.LINEAR
  - Easing setting.

<hr>

**[Returns]**

- `animation_scale_y_from_point`: AnimationScaleYFromPoint
  - Created animation setting instance.

<hr>

**[Notes]**

To start this animation, you need to call the `start` method of the returned instance.<hr>

**[Examples]**

```py
>>> import apysc as ap
>>> stage: ap.Stage = ap.Stage()
>>> sprite: ap.Sprite = ap.Sprite()
>>> sprite.graphics.begin_fill(color='#0af')
>>> rectangle: ap.Rectangle = sprite.graphics.draw_rect(
...     x=50, y=50, width=50, height=50)
>>> _ = rectangle.animation_scale_y_from_point(
...     scale_y_from_point=0.5,
...     y=ap.Int(100),
...     duration=1500,
...     easing=ap.Easing.EASE_OUT_QUINT,
... ).start()
```

<hr>

**[References]**

- [animation_scale_from_point interfaces document](https://simon-ritchie.github.io/apysc/animation_scale_x_and_y_from_point.html)
- [Animation interfaces duration setting document](https://simon-ritchie.github.io/apysc/animation_duration.html)
- [Animation interfaces delay setting document](https://simon-ritchie.github.io/apysc/animation_delay.html)
- [Each animation interface return value document](https://simon-ritchie.github.io/apysc/animation_return_value.html)
- [Sequential animation setting document](https://simon-ritchie.github.io/apysc/sequential_animation.html)
- [animation_parallel interface document](https://simon-ritchie.github.io/apysc/animation_parallel.html)
- [Easing enum document](https://simon-ritchie.github.io/apysc/easing_enum.html)

### animation_skew_x method docstring

Set the skew-x animation setting.<hr>

**[Parameters]**

- `skew_x`: Int or int
  - The final skew-x of the animation.
- `duration`: Int or int, default 3000
  - Milliseconds before an animation ends.
- `delay`: Int or int, default 0
  - Milliseconds before an animation starts.
- `easing`: Easing, default Easing.LINEAR
  - Easing setting.

<hr>

**[Returns]**

- `animation_skew_x`: AnimationSkewX
  - Created animation setting instance.

<hr>

**[Notes]**

To start this animation, you need to call the `start` method of the returned instance.<hr>

**[Examples]**

```py
>>> import apysc as ap
>>> stage: ap.Stage = ap.Stage()
>>> sprite: ap.Sprite = ap.Sprite()
>>> sprite.graphics.begin_fill(color='#0af')
>>> rectangle: ap.Rectangle = sprite.graphics.draw_rect(
...     x=50, y=50, width=50, height=50)
>>> _ = rectangle.animation_skew_x(
...     skew_x=50,
...     duration=1500,
...     easing=ap.Easing.EASE_OUT_QUINT,
... ).start()
```

<hr>

**[References]**

- [animation_skew_x interface document](https://simon-ritchie.github.io/apysc/animation_skew_x.html)
- [Animation interfaces duration setting document](https://simon-ritchie.github.io/apysc/animation_duration.html)
- [Animation interfaces delay setting document](https://simon-ritchie.github.io/apysc/animation_delay.html)
- [Each animation interface return value document](https://simon-ritchie.github.io/apysc/animation_return_value.html)
- [Sequential animation setting document](https://simon-ritchie.github.io/apysc/sequential_animation.html)
- [animation_parallel interface document](https://simon-ritchie.github.io/apysc/animation_parallel.html)
- [Easing enum document](https://simon-ritchie.github.io/apysc/easing_enum.html)

### animation_time method docstring

Get an animation elapsed milisecond.<hr>

**[Returns]**

- `elapsed_time`: Number
  - An animation elapsed millisecond.

<hr>

**[Examples]**

```py
>>> from typing_extensions import TypedDict
>>> import apysc as ap
>>> class RectOptions(TypedDict):
...     rectangle: ap.Rectangle
>>> def on_timer(
...         e: ap.TimerEvent,
...         options: RectOptions) -> None:
...     rectangle: ap.Rectangle = options['rectangle']
...     animation_time: ap.Number = rectangle.animation_time()
...     ap.trace('animation_time:', animation_time)
>>> stage: ap.Stage = ap.Stage()
>>> sprite: ap.Sprite = ap.Sprite()
>>> sprite.graphics.begin_fill(color='#0af')
>>> rectangle: ap.Rectangle = sprite.graphics.draw_rect(
...     x=50, y=50, width=50, height=50)
>>> _ = rectangle.animation_x(
...     x=100,
...     duration=1500,
...     easing=ap.Easing.EASE_OUT_QUINT,
... ).start()
>>> options: RectOptions = {'rectangle': rectangle}
>>> ap.Timer(
...     on_timer, delay=ap.FPS.FPS_60,
...     options=options).start()
```

<hr>

**[References]**

- [animation_time interface document](https://simon-ritchie.github.io/apysc/animation_time.html)

### animation_x method docstring

Set the x-coordinate animation setting.<hr>

**[Parameters]**

- `x`: Int or int
  - Destination of the x-coordinate.
- `duration`: Int or int, default 3000
  - Milliseconds before an animation ends.
- `delay`: Int or int, default 0
  - Milliseconds before an animation starts.
- `easing`: Easing, default Easing.LINEAR
  - Easing setting.

<hr>

**[Returns]**

- `animation_x`: AnimationX
  - Created animation setting instance.

<hr>

**[Notes]**

To start this animation, you need to call the `start` method of the returned instance.<hr>

**[Examples]**

```py
>>> import apysc as ap
>>> stage: ap.Stage = ap.Stage()
>>> sprite: ap.Sprite = ap.Sprite()
>>> sprite.graphics.begin_fill(color='#0af')
>>> rectangle: ap.Rectangle = sprite.graphics.draw_rect(
...     x=50, y=50, width=50, height=50)
>>> _ = rectangle.animation_x(
...     x=100,
...     duration=1500,
...     easing=ap.Easing.EASE_OUT_QUINT,
... ).start()
```

<hr>

**[References]**

- [animation_x interface document](https://simon-ritchie.github.io/apysc/animation_x.html)
- [Animation interfaces duration setting document](https://simon-ritchie.github.io/apysc/animation_duration.html)
- [Animation interfaces delay setting document](https://simon-ritchie.github.io/apysc/animation_delay.html)
- [Each animation interface return value document](https://simon-ritchie.github.io/apysc/animation_return_value.html)
- [Sequential animation setting document](https://simon-ritchie.github.io/apysc/sequential_animation.html)
- [animation_parallel interface document](https://simon-ritchie.github.io/apysc/animation_parallel.html)
- [Easing enum document](https://simon-ritchie.github.io/apysc/easing_enum.html)

### animation_y method docstring

Set the y-coordinate animation setting.<hr>

**[Parameters]**

- `y`: Int or int
  - Destination of the y-coordinate.
- `duration`: Int or int, default 3000
  - Milliseconds before an animation ends.
- `delay`: Int or int, default 0
  - Milliseconds before an animation starts.
- `easing`: Easing, default Easing.LINEAR
  - Easing setting.

<hr>

**[Returns]**

- `animation_y`: AnimationY
  - Created animation setting instance.

<hr>

**[Notes]**

To start this animation, you need to call the `start` method of the returned instance.<hr>

**[Examples]**

```py
>>> import apysc as ap
>>> stage: ap.Stage = ap.Stage()
>>> sprite: ap.Sprite = ap.Sprite()
>>> sprite.graphics.begin_fill(color='#0af')
>>> rectangle: ap.Rectangle = sprite.graphics.draw_rect(
...     x=50, y=50, width=50, height=50)
>>> _ = rectangle.animation_y(
...     y=100,
...     duration=1500,
...     easing=ap.Easing.EASE_OUT_QUINT,
... ).start()
```

<hr>

**[References]**

- [animation_y interface document](https://simon-ritchie.github.io/apysc/animation_y.html)
- [Animation interfaces duration setting document](https://simon-ritchie.github.io/apysc/animation_duration.html)
- [Animation interfaces delay setting document](https://simon-ritchie.github.io/apysc/animation_delay.html)
- [Each animation interface return value document](https://simon-ritchie.github.io/apysc/animation_return_value.html)
- [Sequential animation setting document](https://simon-ritchie.github.io/apysc/sequential_animation.html)
- [animation_parallel interface document](https://simon-ritchie.github.io/apysc/animation_parallel.html)
- [Easing enum document](https://simon-ritchie.github.io/apysc/easing_enum.html)

### bind_custom_event method docstring

Add a custom event listener setting.<hr>

**[Parameters]**

- `custom_event_type`: CustomEventType or str
  - Target custom event type.
- `handler`: _Handler
  - A handler will be called when the custom event is triggered.
- `e`: Event
  - Event instance.
- `options`: dict or None, default None
  - Optional arguments dictionary to be passed to a handler.
- `in_handler_head_expression`: str, default ''
  - Optional expression to be added at the handler function's head position.

<hr>

**[Returns]**

- `name`: str
  - Handler's name.

<hr>

**[Examples]**

```py
>>> import apysc as ap
>>> def on_custom_event(
...         e: ap.Event[ap.Rectangle], options: dict) -> None:
...     rectangle: ap.Rectangle = e.this
...     rectangle.fill_color = ap.String('#f0a')
>>> stage: ap.Stage = ap.Stage()
>>> sprite: ap.Sprite = ap.Sprite()
>>> sprite.graphics.begin_fill(color='#0af')
>>> rectangle: ap.Rectangle = sprite.graphics.draw_rect(
...     x=50, y=50, width=50, height=50)
>>> e: ap.Event = ap.Event(this=rectangle)
>>> _ = rectangle.bind_custom_event(
...     custom_event_type='my_custom_event',
...     handler=on_custom_event, e=e)
>>> # Do something here and then trigger the custom event
>>> rectangle.trigger_custom_event(
...     custom_event_type='my_custom_event')
```

<hr>

**[References]**

- [Bind and trigger the custom event document](https://simon-ritchie.github.io/apysc/bind_and_trigger_custom_event.html)
- [About the handler options' type document](https://simon-ritchie.github.io/apysc/about_handler_options_type.html)

### click method docstring

Add a click event listener setting.<hr>

**[Parameters]**

- `handler`: _Handler
  - A callable would be called when clicking this instance.
- `options`: dict or None, default None
  - Optional arguments dictionary to be passed to a handler.

<hr>

**[Returns]**

- `name`: str
  - Handler's name.

<hr>

**[Examples]**

```py
>>> import apysc as ap
>>> def on_click(
...         e: ap.MouseEvent[ap.Rectangle], options: dict) -> None:
...     rectangle: ap.Rectangle = e.this
...     rectangle.x += 10
>>> stage: ap.Stage = ap.Stage()
>>> sprite: ap.Sprite = ap.Sprite()
>>> sprite.graphics.begin_fill(color='#0af')
>>> rectangle: ap.Rectangle = sprite.graphics.draw_rect(
...     x=50, y=50, width=50, height=50)
>>> _ = rectangle.click(on_click)
```

<hr>

**[References]**

- [Click interface document](https://simon-ritchie.github.io/apysc/click.html)
- [About the handler options’ type document](https://simon-ritchie.github.io/apysc/about_handler_options_type.html)

### dblclick method docstring

Add double click event listener setting.<hr>

**[Parameters]**

- `handler`: _Handler
  - Callable that would be called when double-clicking this instance.
- `options`: dict or None, default None
  - Optional arguments dictionary to be passed to a handler.

<hr>

**[Returns]**

- `name`: str
  - Handler's name.

<hr>

**[Examples]**

```py
>>> import apysc as ap
>>> def on_double_click(
...         e: ap.MouseEvent[ap.Rectangle], options: dict) -> None:
...     rectangle: ap.Rectangle = e.this
...     rectangle.fill_color = ap.String('#f0a')
>>> stage: ap.Stage = ap.Stage()
>>> sprite: ap.Sprite = ap.Sprite()
>>> sprite.graphics.begin_fill(color='#0af')
>>> rectangle: ap.Rectangle = sprite.graphics.draw_rect(
...     x=50, y=50, width=50, height=50)
>>> _ = rectangle.dblclick(on_double_click)
```

<hr>

**[References]**

- [Double click interface document](https://simon-ritchie.github.io/apysc/dblclick.html)
- [About the handler options’ type document](https://simon-ritchie.github.io/apysc/about_handler_options_type.html)

### get_css method docstring

Get a CSS value string.<hr>

**[Parameters]**

- `name`: str or String
  - CSS name (e.g., 'display').

<hr>

**[Returns]**

- `css`: ap.String
  - CSS value.

<hr>

**[Examples]**

```py
>>> import apysc as ap
>>> stage: ap.Stage = ap.Stage()
>>> sprite: ap.Sprite = ap.Sprite()
>>> sprite.graphics.begin_fill(color='#0af', alpha=0.5)
>>> sprite.set_css(name='display', value='none')
>>> sprite.get_css(name='display')
String('none')
```

<hr>

**[References]**

- [Display object get_css and set_css interfaces document](https://simon-ritchie.github.io/apysc/display_object_get_and_set_css.html)

### get_rotation_around_point method docstring

Get a rotation value around the given coordinates.<hr>

**[Parameters]**

- `x`: Int
  - X-coordinate.
- `y`: Int
  - Y-coordinate.

<hr>

**[Returns]**

- `rotation`: Int
  - Rotation value around the given coordinates.

<hr>

**[Examples]**

```py
>>> import apysc as ap
>>> stage: ap.Stage = ap.Stage()
>>> sprite: ap.Sprite = ap.Sprite()
>>> sprite.graphics.begin_fill(color='#0af')
>>> rectangle: ap.Rectangle = sprite.graphics.draw_rect(
...     x=50, y=50, width=50, height=50)
>>> x: ap.Int = ap.Int(100)
>>> y: ap.Int = ap.Int(100)
>>> rectangle.set_rotation_around_point(
...     rotation=ap.Int(45), x=x, y=y)
>>> rectangle.get_rotation_around_point(x=x, y=y)
Int(45)
```

<hr>

**[References]**

- [GraphicsBase rotate_around_point interfaces document](https://simon-ritchie.github.io/apysc/graphics_base_rotation_around_point.html)

### get_scale_x_from_point method docstring

Get a scale-x value from the given x-coordinate.<hr>

**[Parameters]**

- `x`: Int
  - X-coordinate.

<hr>

**[Returns]**

- `scale_x`: Number
  - Scale-x value from the given x-coordinate.

<hr>

**[Examples]**

```py
>>> import apysc as ap
>>> stage: ap.Stage = ap.Stage()
>>> sprite: ap.Sprite = ap.Sprite()
>>> sprite.graphics.begin_fill(color='#0af')
>>> rectangle: ap.Rectangle = sprite.graphics.draw_rect(
...     x=50, y=50, width=50, height=50)
>>> x: ap.Int = ap.Int(100)
>>> rectangle.set_scale_x_from_point(scale_x=ap.Number(1.5), x=x)
>>> rectangle.get_scale_x_from_point(x=x)
Number(1.5)
```

<hr>

**[References]**

- [GraphicsBase scale_from_point interfaces document](https://simon-ritchie.github.io/apysc/graphics_base_scale_from_point.html)

### get_scale_y_from_point method docstring

Get a scale-y value from the given y-coordinate.<hr>

**[Parameters]**

- `y`: Int
  - Y-coordinate.

<hr>

**[Returns]**

- `scale_y`: ap.Number
  - Scale-y value from the given y-coordinate.

<hr>

**[Examples]**

```py
>>> import apysc as ap
>>> stage: ap.Stage = ap.Stage()
>>> sprite: ap.Sprite = ap.Sprite()
>>> sprite.graphics.begin_fill(color='#0af')
>>> rectangle: ap.Rectangle = sprite.graphics.draw_rect(
...     x=50, y=50, width=50, height=50)
>>> y: ap.Int = ap.Int(100)
>>> rectangle.set_scale_y_from_point(scale_y=ap.Number(1.5), y=y)
>>> rectangle.get_scale_y_from_point(y=y)
Number(1.5)
```

<hr>

**[References]**

- [GraphicsBase scale_from_point interfaces document](https://simon-ritchie.github.io/apysc/graphics_base_scale_from_point.html)

### mousedown method docstring

Add mouse down event listener setting.<hr>

**[Parameters]**

- `handler`: _Handler
  - Callable that would be called when mouse down on this instance.
- `options`: dict or None, default None
  - Optional arguments dictionary to be passed to a handler.

<hr>

**[Returns]**

- `name`: str
  - Handler's name.

<hr>

**[Examples]**

```py
>>> import apysc as ap
>>> def on_mousedown(
...         e: ap.MouseEvent[ap.Rectangle], options: dict) -> None:
...     rectangle: ap.Rectangle = e.this
...     rectangle.fill_color = ap.String('#f0a')
>>> stage: ap.Stage = ap.Stage()
>>> sprite: ap.Sprite = ap.Sprite()
>>> sprite.graphics.begin_fill(color='#0af')
>>> rectangle: ap.Rectangle = sprite.graphics.draw_rect(
...     x=50, y=50, width=50, height=50)
>>> _ = rectangle.mousedown(on_mousedown)
```

<hr>

**[References]**

- [Mousedown and mouseup interfaces document](https://simon-ritchie.github.io/apysc/mousedown_and_mouseup.html)
- [About the handler options’ type document](https://simon-ritchie.github.io/apysc/about_handler_options_type.html)

### mousemove method docstring

Add mouse move event listener setting.<hr>

**[Parameters]**

- `handler`: _Handler
  - Callable that would be called when mousemove on this instance.
- `options`: dict or None, default None
  - Optional arguments dictionary to be passed to a handler.

<hr>

**[Returns]**

- `name`: str
  - Handler's name.

<hr>

**[Examples]**

```py
>>> import apysc as ap
>>> def on_mousemove(
...         e: ap.MouseEvent[ap.Rectangle], options: dict) -> None:
...     stage_x: ap.Int = e.stage_x
...     ap.trace('stage_x:', stage_x)
>>> stage: ap.Stage = ap.Stage()
>>> sprite: ap.Sprite = ap.Sprite()
>>> sprite.graphics.begin_fill(color='#0af')
>>> rectangle: ap.Rectangle = sprite.graphics.draw_rect(
...     x=50, y=50, width=50, height=50)
>>> _ = rectangle.mousemove(on_mousemove)
```

<hr>

**[References]**

- [Mousemove interface document](https://simon-ritchie.github.io/apysc/mousemove.html)
- [About the handler options’ type document](https://simon-ritchie.github.io/apysc/about_handler_options_type.html)

### mouseout method docstring

Add mouse out event listener setting.<hr>

**[Parameters]**

- `handler`: _Handler
  - Callable that would be called when mouse out on this instance.
- `options`: dict or None, default None
  - Optional arguments dictionary to be passed to a handler.

<hr>

**[Returns]**

- `name`: str
  - Handler's name.

<hr>

**[Examples]**

```py
>>> import apysc as ap
>>> def on_mouseout(
...         e: ap.MouseEvent[ap.Rectangle], options: dict) -> None:
...     rectangle: ap.Rectangle = e.this
...     rectangle.fill_color = ap.String('#f0a')
>>> stage: ap.Stage = ap.Stage()
>>> sprite: ap.Sprite = ap.Sprite()
>>> sprite.graphics.begin_fill(color='#0af')
>>> rectangle: ap.Rectangle = sprite.graphics.draw_rect(
...     x=50, y=50, width=50, height=50)
>>> _ = rectangle.mouseout(on_mouseout)
```

<hr>

**[References]**

- [Mouseover and mouseout interfaces](https://simon-ritchie.github.io/apysc/mouseover_and_mouseout.html)
- [About the handler options’ type document](https://simon-ritchie.github.io/apysc/about_handler_options_type.html)

### mouseover method docstring

Add mouse over event listener setting.<hr>

**[Parameters]**

- `handler`: _Handler
  - Callable that would be called when mouse over on this instance.
- `options`: dict or None, default None
  - Optional arguments dictionary to be passed to a handler.

<hr>

**[Returns]**

- `name`: str
  - Handler's name.

<hr>

**[Examples]**

```py
>>> import apysc as ap
>>> def on_mouseover(
...         e: ap.MouseEvent[ap.Rectangle], options: dict) -> None:
...     rectangle: ap.Rectangle = e.this
...     rectangle.fill_color = ap.String('#f0a')
>>> stage: ap.Stage = ap.Stage()
>>> sprite: ap.Sprite = ap.Sprite()
>>> sprite.graphics.begin_fill(color='#0af')
>>> rectangle: ap.Rectangle = sprite.graphics.draw_rect(
...     x=50, y=50, width=50, height=50)
>>> _ = rectangle.mouseout(on_mouseover)
```

<hr>

**[References]**

- [Mouseover and mouseout interfaces](https://simon-ritchie.github.io/apysc/mouseover_and_mouseout.html)
- [About the handler options' type document](https://simon-ritchie.github.io/apysc/about_handler_options_type.html)

### mouseup method docstring

Add mouse up event listener setting.<hr>

**[Parameters]**

- `handler`: _Handler
  - Callable that would be called when mouse-up on this instance.
- `options`: dict or None, default None
  - Optional arguments dictionary to be passed to a handler

<hr>

**[Returns]**

- `name`: str
  - Handler's name.

<hr>

**[Examples]**

```py
>>> import apysc as ap
>>> def on_mouseup(
...         e: ap.MouseEvent[ap.Rectangle], options: dict) -> None:
...     rectangle: ap.Rectangle = e.this
...     rectangle.fill_color = ap.String('#f0a')
>>> stage: ap.Stage = ap.Stage()
>>> sprite: ap.Sprite = ap.Sprite()
>>> sprite.graphics.begin_fill(color='#0af')
>>> rectangle: ap.Rectangle = sprite.graphics.draw_rect(
...     x=50, y=50, width=50, height=50)
>>> _ = rectangle.mouseup(on_mouseup)
```

<hr>

**[References]**

- [Mousedown and mouseup interfaces document](https://simon-ritchie.github.io/apysc/mousedown_and_mouseup.html)
- [About the handler options’ type document](https://simon-ritchie.github.io/apysc/about_handler_options_type.html)

### remove_from_parent method docstring

Remove this instance from parent.<hr>

**[Raises]**

- ValueError: If this instance is not added to any parent.

### set_css method docstring

Set a specified value string to the CSS.<hr>

**[Parameters]**

- `name`: str or String
  - CSS name (e.g., 'display').
- `value`: str or String
  - A CSS value string (e.g., 'none').

<hr>

**[Examples]**

```py
>>> import apysc as ap
>>> stage: ap.Stage = ap.Stage()
>>> sprite: ap.Sprite = ap.Sprite()
>>> sprite.graphics.begin_fill(color='#0af', alpha=0.5)
>>> sprite.set_css(name='display', value='none')
>>> sprite.get_css(name='display')
String('none')
```

<hr>

**[References]**

- [Display object get_css and set_css interfaces document](https://simon-ritchie.github.io/apysc/display_object_get_and_set_css.html)

### set_rotation_around_point method docstring

Update a rotation value around the given coordinates.<hr>

**[Parameters]**

- `rotation`: Int
  - Rotation value to set.
- `x`: Int
  - X-coordinate.
- `y`: Int
  - Y-coordinate.

<hr>

**[References]**

- [GraphicsBase rotate_around_point interfaces document](https://simon-ritchie.github.io/apysc/graphics_base_rotation_around_point.html)

### set_scale_x_from_point method docstring

Update a scale-x value from the given x-coordinate.<hr>

**[Parameters]**

- `scale_x`: Number
  - Scale-x value to set.
- `x`: Int
  - X-coordinate.

<hr>

**[Examples]**

```py
>>> import apysc as ap
>>> stage: ap.Stage = ap.Stage()
>>> sprite: ap.Sprite = ap.Sprite()
>>> sprite.graphics.begin_fill(color='#0af')
>>> rectangle: ap.Rectangle = sprite.graphics.draw_rect(
...     x=50, y=50, width=50, height=50)
>>> x: ap.Int = ap.Int(100)
>>> rectangle.set_scale_x_from_point(scale_x=ap.Number(1.5), x=x)
>>> rectangle.get_scale_x_from_point(x=x)
Number(1.5)
```

<hr>

**[References]**

- [GraphicsBase scale_from_point interfaces document](https://simon-ritchie.github.io/apysc/graphics_base_scale_from_point.html)

### set_scale_y_from_point method docstring

Update a scale-y value from the given y-coordinate.<hr>

**[Parameters]**

- `scale_y`: Number
  - Scale-y value to set.
- `y`: Int
  - Y-coordinate.

<hr>

**[Examples]**

```py
>>> import apysc as ap
>>> stage: ap.Stage = ap.Stage()
>>> sprite: ap.Sprite = ap.Sprite()
>>> sprite.graphics.begin_fill(color='#0af')
>>> rectangle: ap.Rectangle = sprite.graphics.draw_rect(
...     x=50, y=50, width=50, height=50)
>>> y: ap.Int = ap.Int(100)
>>> rectangle.set_scale_y_from_point(scale_y=ap.Number(1.5), y=y)
>>> rectangle.get_scale_y_from_point(y=y)
Number(1.5)
```

<hr>

**[References]**

- [GraphicsBase scale_from_point interfaces document](https://simon-ritchie.github.io/apysc/graphics_base_scale_from_point.html)

### trigger_custom_event method docstring

Add a custom event trigger setting.<hr>

**[Parameters]**

- `custom_event_type`: CustomEventType or str
  - Target custom event type.

<hr>

**[Examples]**

```py
>>> import apysc as ap
>>> def on_custom_event(
...         e: ap.Event[ap.Rectangle], options: dict) -> None:
...     rectangle: ap.Rectangle = e.this
...     rectangle.fill_color = ap.String('#f0a')
>>> stage: ap.Stage = ap.Stage()
>>> sprite: ap.Sprite = ap.Sprite()
>>> sprite.graphics.begin_fill(color='#0af')
>>> rectangle: ap.Rectangle = sprite.graphics.draw_rect(
...     x=50, y=50, width=50, height=50)
>>> e: ap.Event = ap.Event(this=rectangle)
>>> _ = rectangle.bind_custom_event(
...     custom_event_type='my_custom_event',
...     handler=on_custom_event, e=e)
>>> # Do something here and then trigger the custom event
>>> rectangle.trigger_custom_event(
...     custom_event_type='my_custom_event')
```

<hr>

**[References]**

- [Bind and trigger the custom event document](https://simon-ritchie.github.io/apysc/bind_and_trigger_custom_event.html)

### unbind_click method docstring

Unbind specified handler's click event.<hr>

**[Parameters]**

- `handler`: _Handler
  - Unbinding target Callable.

<hr>

**[Examples]**

```py
>>> import apysc as ap
>>> def on_click(
...         e: ap.MouseEvent[ap.Rectangle], options: dict) -> None:
...     rectangle: ap.Rectangle = e.this
...     rectangle.fill_color = ap.String('#f0a')
...     rectangle.unbind_click(on_click)
>>> stage: ap.Stage = ap.Stage()
>>> sprite: ap.Sprite = ap.Sprite()
>>> sprite.graphics.begin_fill(color='#0af')
>>> rectangle: ap.Rectangle = sprite.graphics.draw_rect(
...     x=50, y=50, width=50, height=50)
>>> _ = rectangle.click(on_click)
```

<hr>

**[References]**

- [Click interface document](https://simon-ritchie.github.io/apysc/click.html)

### unbind_click_all method docstring

Unbind all click events.<hr>

**[Examples]**

```py
>>> import apysc as ap
>>> def on_click(
...         e: ap.MouseEvent[ap.Rectangle], options: dict) -> None:
...     rectangle: ap.Rectangle = e.this
...     rectangle.fill_color = ap.String('#f0a')
...     rectangle.unbind_click_all()
>>> stage: ap.Stage = ap.Stage()
>>> sprite: ap.Sprite = ap.Sprite()
>>> sprite.graphics.begin_fill(color='#0af')
>>> rectangle: ap.Rectangle = sprite.graphics.draw_rect(
...     x=50, y=50, width=50, height=50)
>>> _ = rectangle.click(on_click)
```

<hr>

**[References]**

- [Click interface document](https://simon-ritchie.github.io/apysc/click.html)

### unbind_custom_event method docstring

Unbind (remove) a custom event listener setting.<hr>

**[Parameters]**

- `custom_event_type`: CustomEventType or str
  - Target custom event type.
- `handler`: _Handler
  - A handler for when the custom event is triggered.

<hr>

**[Returns]**

- `name`: str
  - Handler's name.

<hr>

**[Examples]**

```py
>>> import apysc as ap
>>> def on_custom_event(
...         e: ap.Event[ap.Rectangle], options: dict) -> None:
...     rectangle: ap.Rectangle = e.this
...     rectangle.fill_color = ap.String('#f0a')
...     rectangle.unbind_custom_event(
...         custom_event_type='my_custom_event',
...         handler=on_custom_event)
>>> stage: ap.Stage = ap.Stage()
>>> sprite: ap.Sprite = ap.Sprite()
>>> sprite.graphics.begin_fill(color='#0af')
>>> rectangle: ap.Rectangle = sprite.graphics.draw_rect(
...     x=50, y=50, width=50, height=50)
>>> e: ap.Event = ap.Event(this=rectangle)
>>> _ = rectangle.bind_custom_event(
...     custom_event_type='my_custom_event',
...     handler=on_custom_event, e=e)
>>> # Do something here and then trigger the custom event
>>> rectangle.trigger_custom_event(
...     custom_event_type='my_custom_event')
```

### unbind_custom_event_all method docstring

Unbind (remove) custom event listener settings.<hr>

**[Parameters]**

- `custom_event_type`: CustomEventType or str
  - Target custom event type.

<hr>

**[Examples]**

```py
>>> import apysc as ap
>>> def on_custom_event(
...         e: ap.Event[ap.Rectangle], options: dict) -> None:
...     rectangle: ap.Rectangle = e.this
...     rectangle.fill_color = ap.String('#f0a')
...     rectangle.unbind_custom_event_all(
...         custom_event_type='my_custom_event')
>>> stage: ap.Stage = ap.Stage()
>>> sprite: ap.Sprite = ap.Sprite()
>>> sprite.graphics.begin_fill(color='#0af')
>>> rectangle: ap.Rectangle = sprite.graphics.draw_rect(
...     x=50, y=50, width=50, height=50)
>>> e: ap.Event = ap.Event(this=rectangle)
>>> _ = rectangle.bind_custom_event(
...     custom_event_type='my_custom_event',
...     handler=on_custom_event, e=e)
>>> # Do something here and then trigger the custom event
>>> rectangle.trigger_custom_event(
...     custom_event_type='my_custom_event')
```

### unbind_dblclick method docstring

Unbind a specified handler's double click event.<hr>

**[Parameters]**

- `handler`: _Handler
  - Unbinding target Callable.

<hr>

**[Examples]**

```py
>>> import apysc as ap
>>> def on_double_click(
...         e: ap.MouseEvent[ap.Rectangle], options: dict) -> None:
...     rectangle: ap.Rectangle = e.this
...     rectangle.fill_color = ap.String('#f0a')
...     rectangle.unbind_dblclick(on_double_click)
>>> stage: ap.Stage = ap.Stage()
>>> sprite: ap.Sprite = ap.Sprite()
>>> sprite.graphics.begin_fill(color='#0af')
>>> rectangle: ap.Rectangle = sprite.graphics.draw_rect(
...     x=50, y=50, width=50, height=50)
>>> _ = rectangle.dblclick(on_double_click)
```

### unbind_dblclick_all method docstring

Unbind all double click events.<hr>

**[Examples]**

```py
>>> import apysc as ap
>>> def on_double_click(
...         e: ap.MouseEvent[ap.Rectangle], options: dict) -> None:
...     rectangle: ap.Rectangle = e.this
...     rectangle.fill_color = ap.String('#f0a')
...     rectangle.unbind_dblclick_all()
>>> stage: ap.Stage = ap.Stage()
>>> sprite: ap.Sprite = ap.Sprite()
>>> sprite.graphics.begin_fill(color='#0af')
>>> rectangle: ap.Rectangle = sprite.graphics.draw_rect(
...     x=50, y=50, width=50, height=50)
>>> _ = rectangle.dblclick(on_double_click)
```

### unbind_mousedown method docstring

Unbind a specified handler's mouse down event.<hr>

**[Parameters]**

- `handler`: _Handler
  - Unbinding target Callable.

<hr>

**[Examples]**

```py
>>> import apysc as ap
>>> def on_mousedown(
...         e: ap.MouseEvent[ap.Rectangle], options: dict) -> None:
...     rectangle: ap.Rectangle = e.this
...     rectangle.fill_color = ap.String('#f0a')
...     rectangle.unbind_mousedown(on_mousedown)
>>> stage: ap.Stage = ap.Stage()
>>> sprite: ap.Sprite = ap.Sprite()
>>> sprite.graphics.begin_fill(color='#0af')
>>> rectangle: ap.Rectangle = sprite.graphics.draw_rect(
...     x=50, y=50, width=50, height=50)
>>> _ = rectangle.mousedown(on_mousedown)
```

<hr>

**[References]**

- [Mousedown and mouseup interfaces document](https://simon-ritchie.github.io/apysc/mousedown_and_mouseup.html)

### unbind_mousedown_all method docstring

Unbind all mouse down events.<hr>

**[Examples]**

```py
>>> import apysc as ap
>>> def on_mousedown(
...         e: ap.MouseEvent[ap.Rectangle], options: dict) -> None:
...     rectangle: ap.Rectangle = e.this
...     rectangle.fill_color = ap.String('#f0a')
...     rectangle.unbind_mousedown_all()
>>> stage: ap.Stage = ap.Stage()
>>> sprite: ap.Sprite = ap.Sprite()
>>> sprite.graphics.begin_fill(color='#0af')
>>> rectangle: ap.Rectangle = sprite.graphics.draw_rect(
...     x=50, y=50, width=50, height=50)
>>> _ = rectangle.mousedown(on_mousedown)
```

<hr>

**[References]**

- [Mousedown and mouseup interfaces document](https://simon-ritchie.github.io/apysc/mousedown_and_mouseup.html)

### unbind_mousemove method docstring

Unbind a specified handler's mouse move event.<hr>

**[Parameters]**

- `handler`: _Handler
  - Unbinding target Callable.

<hr>

**[Examples]**

```py
>>> import apysc as ap
>>> def on_mousemove(
...         e: ap.MouseEvent[ap.Rectangle], options: dict) -> None:
...     stage_x: ap.Int = e.stage_x
...     ap.trace('stage_x:', stage_x)
>>> def on_click(
...         e: ap.MouseEvent[ap.Rectangle], options: dict) -> None:
...     rectangle: ap.Rectangle = e.this
...     rectangle.unbind_mousemove(on_mousemove)
>>> stage: ap.Stage = ap.Stage()
>>> sprite: ap.Sprite = ap.Sprite()
>>> sprite.graphics.begin_fill(color='#0af')
>>> rectangle: ap.Rectangle = sprite.graphics.draw_rect(
...     x=50, y=50, width=50, height=50)
>>> _ = rectangle.mousemove(on_mousemove)
>>> _ = rectangle.click(on_click)
```

<hr>

**[References]**

- [Mousemove interface document](https://simon-ritchie.github.io/apysc/mousemove.html)

### unbind_mousemove_all method docstring

Unbind all mouse move events.<hr>

**[Examples]**

```py
>>> import apysc as ap
>>> def on_mousemove(
...         e: ap.MouseEvent[ap.Rectangle], options: dict) -> None:
...     stage_x: ap.Int = e.stage_x
...     ap.trace('stage_x:', stage_x)
>>> def on_click(
...         e: ap.MouseEvent[ap.Rectangle], options: dict) -> None:
...     rectangle: ap.Rectangle = e.this
...     rectangle.unbind_mousemove_all()
>>> stage: ap.Stage = ap.Stage()
>>> sprite: ap.Sprite = ap.Sprite()
>>> sprite.graphics.begin_fill(color='#0af')
>>> rectangle: ap.Rectangle = sprite.graphics.draw_rect(
...     x=50, y=50, width=50, height=50)
>>> _ = rectangle.mousemove(on_mousemove)
>>> _ = rectangle.click(on_click)
```

<hr>

**[References]**

- [Mousemove interface document](https://simon-ritchie.github.io/apysc/mousemove.html)

### unbind_mouseout method docstring

Unbind a specified handler's mouse out event.<hr>

**[Parameters]**

- `handler`: _Handler
  - Unbinding target Callable.

<hr>

**[Examples]**

```py
>>> import apysc as ap
>>> def on_mouseout(
...         e: ap.MouseEvent[ap.Rectangle], options: dict) -> None:
...     rectangle: ap.Rectangle = e.this
...     rectangle.fill_color = ap.String('#f0a')
...     rectangle.unbind_mouseout(on_mouseout)
>>> stage: ap.Stage = ap.Stage()
>>> sprite: ap.Sprite = ap.Sprite()
>>> sprite.graphics.begin_fill(color='#0af')
>>> rectangle: ap.Rectangle = sprite.graphics.draw_rect(
...     x=50, y=50, width=50, height=50)
>>> _ = rectangle.mouseout(on_mouseout)
```

<hr>

**[References]**

- [Mouseover and mouseout interfaces](https://simon-ritchie.github.io/apysc/mouseover_and_mouseout.html)

### unbind_mouseout_all method docstring

Unbind all mouse out events.<hr>

**[Examples]**

```py
>>> import apysc as ap
>>> def on_mouseout(
...         e: ap.MouseEvent[ap.Rectangle], options: dict) -> None:
...     rectangle: ap.Rectangle = e.this
...     rectangle.fill_color = ap.String('#f0a')
...     rectangle.unbind_mouseout_all()
>>> stage: ap.Stage = ap.Stage()
>>> sprite: ap.Sprite = ap.Sprite()
>>> sprite.graphics.begin_fill(color='#0af')
>>> rectangle: ap.Rectangle = sprite.graphics.draw_rect(
...     x=50, y=50, width=50, height=50)
>>> _ = rectangle.mouseout(on_mouseout)
```

<hr>

**[References]**

- [Mouseover and mouseout interfaces](https://simon-ritchie.github.io/apysc/mouseover_and_mouseout.html)

### unbind_mouseover method docstring

Unbind a specified handler's mouseover event.<hr>

**[Parameters]**

- `handler`: _Handler
  - Unbinding target Callable.

<hr>

**[Examples]**

```py
>>> import apysc as ap
>>> def on_mouseover(
...         e: ap.MouseEvent[ap.Rectangle], options: dict) -> None:
...     rectangle: ap.Rectangle = e.this
...     rectangle.fill_color = ap.String('#f0a')
...     rectangle.unbind_mouseover(on_mouseover)
>>> stage: ap.Stage = ap.Stage()
>>> sprite: ap.Sprite = ap.Sprite()
>>> sprite.graphics.begin_fill(color='#0af')
>>> rectangle: ap.Rectangle = sprite.graphics.draw_rect(
...     x=50, y=50, width=50, height=50)
>>> _ = rectangle.mouseout(on_mouseover)
```

<hr>

**[References]**

- [Mouseover and mouseout interfaces](https://simon-ritchie.github.io/apysc/mouseover_and_mouseout.html)

### unbind_mouseover_all method docstring

Unbind all mouseover events.<hr>

**[Examples]**

```py
>>> import apysc as ap
>>> def on_mouseover(
...         e: ap.MouseEvent[ap.Rectangle], options: dict) -> None:
...     rectangle: ap.Rectangle = e.this
...     rectangle.fill_color = ap.String('#f0a')
...     rectangle.unbind_mouseover_all()
>>> stage: ap.Stage = ap.Stage()
>>> sprite: ap.Sprite = ap.Sprite()
>>> sprite.graphics.begin_fill(color='#0af')
>>> rectangle: ap.Rectangle = sprite.graphics.draw_rect(
...     x=50, y=50, width=50, height=50)
>>> _ = rectangle.mouseout(on_mouseover)
```

<hr>

**[References]**

- [Mouseover and mouseout interfaces](https://simon-ritchie.github.io/apysc/mouseover_and_mouseout.html)

### unbind_mouseup method docstring

Unbind a specified handler's mouse-up event.<hr>

**[Parameters]**

- `handler`: _Handler
  - Unbinding target Callable.

<hr>

**[Examples]**

```py
>>> import apysc as ap
>>> def on_mouseup(
...         e: ap.MouseEvent[ap.Rectangle], options: dict) -> None:
...     rectangle: ap.Rectangle = e.this
...     rectangle.fill_color = ap.String('#f0a')
...     rectangle.unbind_mouseup(on_mouseup)
>>> stage: ap.Stage = ap.Stage()
>>> sprite: ap.Sprite = ap.Sprite()
>>> sprite.graphics.begin_fill(color='#0af')
>>> rectangle: ap.Rectangle = sprite.graphics.draw_rect(
...     x=50, y=50, width=50, height=50)
>>> _ = rectangle.mouseup(on_mouseup)
```

<hr>

**[References]**

- [Mousedown and mouseup interfaces document](https://simon-ritchie.github.io/apysc/mousedown_and_mouseup.html)

### unbind_mouseup_all method docstring

Unbind all mouse up events.<hr>

**[Examples]**

```py
>>> import apysc as ap
>>> def on_mouseup(
...         e: ap.MouseEvent[ap.Rectangle], options: dict) -> None:
...     rectangle: ap.Rectangle = e.this
...     rectangle.fill_color = ap.String('#f0a')
...     rectangle.unbind_mouseup_all()
>>> stage: ap.Stage = ap.Stage()
>>> sprite: ap.Sprite = ap.Sprite()
>>> sprite.graphics.begin_fill(color='#0af')
>>> rectangle: ap.Rectangle = sprite.graphics.draw_rect(
...     x=50, y=50, width=50, height=50)
>>> _ = rectangle.mouseup(on_mouseup)
```

<hr>

**[References]**

- [Mousedown and mouseup interfaces document](https://simon-ritchie.github.io/apysc/mousedown_and_mouseup.html)