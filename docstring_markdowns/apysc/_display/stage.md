# apysc._display.stage docstrings

## Module summary

Stage (canvas) implementation.

## _save_stage_id_to_db function docstring

Save a stage's memory address (id) to the database.<hr>

**[Parameters]**

- `stage`: Stage
  - Target stage.

## get_stage function docstring

Get a already instantiated stage instance.<hr>

**[Returns]**

- `stage`: Stage
  - Target stage instance.

<hr>

**[Raises]**

- _StageNotCreatedError: If a stage is not instantiated yet.

## get_stage_elem_id function docstring

Get current stage's element id.<hr>

**[Returns]**

- `stage_elem_id`: str
  - Current stage's element id. If stage is not instantiated yet, blank string will be set.

## get_stage_elem_str function docstring

Get current stage's jQuery element string.<hr>

**[Returns]**

- `stage_elem_str`: str
  - Stage's jQuery element string (e.g., '$("#<stage_elem_id>")').

## get_stage_variable_name function docstring

Get current stage's global variable name.<hr>

**[Returns]**

- `stage_variable_name`: str
  - Current stage's js global variable name. If stage is not instantiated yet, blank string will be set.

## ChildInterface class docstring



### ABCMeta method docstring

Metaclass for defining Abstract Base Classes (ABCs). Use this metaclass to create an ABC. An ABC can be subclassed directly, and then acts as a mix-in class. You can also register unrelated concrete classes (even built-in classes) and unrelated ABCs as 'virtual subclasses' -- these and their descendants will be considered subclasses of the registering ABC by the built-in issubclass() function, but the registering ABC won't show up in their MRO (Method Resolution Order) nor will method implementations defined by the registering ABC be callable (not even via super()).

### __init__ method docstring

Initialize self. See help(type(self)) for accurate signature.

### _append_contains_expression method docstring

Append contains method expression.<hr>

**[Parameters]**

- `result`: Boolean
  - Result boolean value.
- `child`: DisplayObject
  - Child instance to check.

### _append_get_child_at_expression method docstring

Append get_child_at method expression.<hr>

**[Parameters]**

- `child`: DisplayObject
  - Target index child instance.
- `index`: int or Int
  - Child's index (start from 0).

### _append_num_children_expression method docstring

Append num_children method expression.<hr>

**[Parameters]**

- `num_children`: Int
  - Current children number.

### _delete_snapshot_exists_val method docstring

Delete boolean value whether snapshot value exists or not.<hr>

**[Parameters]**

- `snapshot_name`: str
  - Target snapshot name.

### _get_next_snapshot_name method docstring

Get a next snapshot name.<hr>

**[Returns]**

- `snapshot_name`: str
  - Next snapshot name.

### _initialize_children_if_not_initialized method docstring

Initialize _children attribute if it hasn't been initialized yet.

### _initialize_ss_exists_val_if_not_initialized method docstring

Initialize _snapshot_exists_ value it hasn't been initialized yet.

### _make_snapshot method docstring

Make values' snapshot.<hr>

**[Parameters]**

- `snapshot_name`: str
  - Target snapshot name.

### _revert method docstring

Revert values if snapshot exists.<hr>

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

## CustomEventInterface class docstring



### __init__ method docstring

Initialize self. See help(type(self)) for accurate signature.

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

### _get_custom_event_type_str method docstring

Get a custom event type string from a type value.<hr>

**[Parameters]**

- `custom_event_type`: CustomEventType or str
  - Target custom event type or string.

<hr>

**[Returns]**

- `custom_event_type_str`: str
  - A custom event type string.

### _initialize_blank_object_if_not_initialized method docstring

Initialize a blank object value if it hasn't been initialized yet.

### _initialize_custom_event_handlers_if_not_initialized method docstring

Initialize the _custom_event_handlers data if it hasn't been initialized yet.<hr>

**[Parameters]**

- `custom_event_type_str`: str
  - Target custom event type string.

### _set_custom_event_handler_data method docstring

Set a handler's data to the dictionary.<hr>

**[Parameters]**

- `handler`: _Handler
  - Callable will be called when an event is dispatched.
- `custom_event_type_str`: str
  - Target custom event type string.
- `options`: dict or None
  - Optional arguments dictionary to be passed to a handler.

### _unset_custom_event_handler_data method docstring

Unset a handler's data from the dictionary.<hr>

**[Parameters]**

- `handler`: _Handler
  - Callable will be called when an event is dispatched.
- `custom_event_type_str`: str
  - Target custom event type string.

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

## HeightInterface class docstring



### ABCMeta method docstring

Metaclass for defining Abstract Base Classes (ABCs). Use this metaclass to create an ABC. An ABC can be subclassed directly, and then acts as a mix-in class. You can also register unrelated concrete classes (even built-in classes) and unrelated ABCs as 'virtual subclasses' -- these and their descendants will be considered subclasses of the registering ABC by the built-in issubclass() function, but the registering ABC won't show up in their MRO (Method Resolution Order) nor will method implementations defined by the registering ABC be callable (not even via super()).

### __init__ method docstring

Initialize self. See help(type(self)) for accurate signature.

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

### _append_height_attr_linking_setting method docstring

Append a height attribute linking setting.

### _append_height_update_expression method docstring

Append height updating expression.

### _delete_snapshot_exists_val method docstring

Delete boolean value whether snapshot value exists or not.<hr>

**[Parameters]**

- `snapshot_name`: str
  - Target snapshot name.

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

### _initialize_height_if_not_initialized method docstring

Initialize _height attribute if it hasn't been initialized yet.

### _initialize_ss_exists_val_if_not_initialized method docstring

Initialize _snapshot_exists_ value it hasn't been initialized yet.

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

Make value's snapshot.<hr>

**[Parameters]**

- `snapshot_name`: str
  - Target snapshot name.

### _revert method docstring

Revert value if snapshot exists.<hr>

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

### _update_height_and_skip_appending_exp method docstring

Update height value and skip appending expression.<hr>

**[Parameters]**

- `value`: int or Int
  - Height value to set.

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

### animation_height method docstring

Set the height animation setting.<hr>

**[Parameters]**

- `height`: Int or int
  - The final height of the animation.
- `duration`: Int or int, default 3000
  - Milliseconds before an animation ends.
- `delay`: Int or int, default 0
  - Milliseconds before an animation starts.
- `easing`: Easing, default Easing.LINEAR
  - Easing setting.

<hr>

**[Returns]**

- `animation_height`: AnimationHeight
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
>>> _ = rectangle.animation_height(
...     height=100,
...     duration=1500,
...     easing=ap.Easing.EASE_OUT_QUINT,
... ).start()
```

<hr>

**[References]**

- [animation_width and animation_height interfaces document](https://simon-ritchie.github.io/apysc/animation_width_and_height.html)
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

## MouseEventInterfaces class docstring

Class implementation for inheritance of each mouse event interfaces.

Class implementation for inheritance of each mouse event interfaces.

### __init__ method docstring

Initialize self. See help(type(self)) for accurate signature.

### _append_mouse_event_binding_expression method docstring

Append a mouse event binding expression.<hr>

**[Parameters]**

- `name`: str
  - Handler's name.
- `mouse_event_type`: MouseEventType
  - Event type to bind.

### _initialize_click_handlers_if_not_initialized method docstring

Initialize _click_handlers attribute if it hasn't been initialized yet.

### _initialize_dblclick_handlers_if_not_initialized method docstring

Initialize _dblclick_handlers attribute if it is not initialized yet.

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

### _set_mouse_event_handler_data method docstring

Set a handler's data to the given dictionary.<hr>

**[Parameters]**

- `handler`: _Handler
  - Callable would be called when event is dispatched.
- `handlers_dict`: dict
  - Dictionary to be set handler's data.
- `options`: dict or None
  - Optional arguments dictionary to be passed to handler.

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

## Stage class docstring

The Stage (overall viewport) class.

The Stage (overall viewport) class.<hr>

**[Examples]**

```py
>>> import apysc as ap
>>> stage: ap.Stage = ap.Stage(
...     stage_width=500, stage_height=300,
...     background_color='#333', stage_elem_id='sales_chart')
```

<hr>

**[References]**

- [Stage document](https://simon-ritchie.github.io/apysc/stage.html)

### ABCMeta method docstring

Metaclass for defining Abstract Base Classes (ABCs). Use this metaclass to create an ABC. An ABC can be subclassed directly, and then acts as a mix-in class. You can also register unrelated concrete classes (even built-in classes) and unrelated ABCs as 'virtual subclasses' -- these and their descendants will be considered subclasses of the registering ABC by the built-in issubclass() function, but the registering ABC won't show up in their MRO (Method Resolution Order) nor will method implementations defined by the registering ABC be callable (not even via super()).

### __init__ method docstring

Create Stage (overall viewport) instance.<hr>

**[Parameters]**

- `stage_width`: int, default 300
  - Stage width.
- `stage_height`: int, default 185
  - Stage height
- `background_color`: str, default '#ffffff'
  - Hexadecimal background color string.
- `add_to`: str, default 'body'
  - Specification of element to add stage. Unique tag (e.g., 'body') or ID selector (e.g., '#any-unique-elem') is acceptable.
- `stage_elem_id`: str or None, optional
  - ID attribute set to stage html element (e.g., 'line-graph'). If None is set, random integer will be applied.

<hr>

**[Examples]**

```py
>>> import apysc as ap
>>> stage: ap.Stage = ap.Stage(
...     stage_width=500, stage_height=300,
...     background_color='#333', stage_elem_id='sales_chart')
```

<hr>

**[References]**

- [Stage document](https://simon-ritchie.github.io/apysc/stage.html)

### __repr__ method docstring

Get a string representation of this instance (for the sake of debugging).<hr>

**[Returns]**

- `repr_str`: str
  - Type name and elem id will be set (e.g., `Stage('<stage_elem_id>')`).

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

Append stage constructor expression.

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

### _append_height_attr_linking_setting method docstring

Append a height attribute linking setting.

### _append_height_update_expression method docstring

Append height updating expression.

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

### _append_width_attr_linking_setting method docstring

Append a width attribute linking setting.

### _append_width_update_expression method docstring

Append width updating expression.

### _create_stage_elem_id_if_none method docstring

Create random stage element id if specified id is None.<hr>

**[Parameters]**

- `stage_elem_id`: str or None
  - Specified stage element id.

<hr>

**[Returns]**

- `result_id`: str
  - If specified id is not None, then unchanged argument value will be returned. Otherwise, random integer string will be returned.

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

### _initialize_custom_event_handlers_if_not_initialized method docstring

Initialize the _custom_event_handlers data if it hasn't been initialized yet.<hr>

**[Parameters]**

- `custom_event_type_str`: str
  - Target custom event type string.

### _initialize_dblclick_handlers_if_not_initialized method docstring

Initialize _dblclick_handlers attribute if it is not initialized yet.

### _initialize_height_if_not_initialized method docstring

Initialize _height attribute if it hasn't been initialized yet.

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

### _initialize_width_if_not_initialized method docstring

Initialize _width attribute if it hasn't been initialized yet.

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

### _make_constructor_expression method docstring

Make a stage constructor expression string.<hr>

**[Returns]**

- `expression`: str
  - Result expression.

### _make_snapshot method docstring

Make values' snapshot.<hr>

**[Parameters]**

- `snapshot_name`: str
  - Target snapshot name.

### _make_style_str method docstring

Make a stage's style string.<hr>

**[Returns]**

- `style`: str
  - Result style string (width, height, etc).

### _revert method docstring

Revert values if snapshot exists.<hr>

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

### _save_stage_elem_id method docstring

Save the stage element id.

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

### _update_height_and_skip_appending_exp method docstring

Update height value and skip appending expression.<hr>

**[Parameters]**

- `value`: int or Int
  - Height value to set.

### _update_width_and_skip_appending_exp method docstring

Update width value and skip appending expression.<hr>

**[Parameters]**

- `value`: int or Int
  - Width value to set.

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

### animation_height method docstring

Set the height animation setting.<hr>

**[Parameters]**

- `height`: Int or int
  - The final height of the animation.
- `duration`: Int or int, default 3000
  - Milliseconds before an animation ends.
- `delay`: Int or int, default 0
  - Milliseconds before an animation starts.
- `easing`: Easing, default Easing.LINEAR
  - Easing setting.

<hr>

**[Returns]**

- `animation_height`: AnimationHeight
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
>>> _ = rectangle.animation_height(
...     height=100,
...     duration=1500,
...     easing=ap.Easing.EASE_OUT_QUINT,
... ).start()
```

<hr>

**[References]**

- [animation_width and animation_height interfaces document](https://simon-ritchie.github.io/apysc/animation_width_and_height.html)
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

### animation_width method docstring

Set the width animation setting.<hr>

**[Parameters]**

- `width`: Int or int
  - The final width of the animation.
- `duration`: Int or int, default 3000
  - Milliseconds before an animation ends.
- `delay`: Int or int, default 0
  - Milliseconds before an animation starts.
- `easing`: Easing, default Easing.LINEAR
  - Easing setting.

<hr>

**[Returns]**

- `animation_width`: AnimationWidth
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
>>> _ = rectangle.animation_width(
...     width=100,
...     duration=1500,
...     easing=ap.Easing.EASE_OUT_QUINT,
... ).start()
```

<hr>

**[References]**

- [animation_width and animation_height interfaces document](https://simon-ritchie.github.io/apysc/animation_width_and_height.html)
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

## Tuple class docstring

Tuple type; Tuple[X, Y] is the cross-product type of X and Y. Example: Tuple[T1, T2] is a tuple of two elements corresponding to type variables T1 and T2. Tuple[int, float, str] is a tuple of an int, a float and a string. To specify a variable-length tuple of homogeneous type, use Tuple[T, ...].

Tuple type; Tuple[X, Y] is the cross-product type of X and Y. Example: Tuple[T1, T2] is a tuple of two elements corresponding to type variables T1 and T2. Tuple[int, float, str] is a tuple of an int, a float and a string. To specify a variable-length tuple of homogeneous type, use Tuple[T, ...].

### __add__ method docstring

Return self+value.

### TupleMeta method docstring

Metaclass for Tuple (internal).

### __contains__ method docstring

Return key in self.

### tuple method docstring

tuple() -> empty tuple tuple(iterable) -> tuple initialized from iterable's items If the argument is a tuple, the return value is the same object.

### __getitem__ method docstring

Return self[key].

### __init__ method docstring

Initialize self. See help(type(self)) for accurate signature.

### __iter__ method docstring

Implement iter(self).

### __len__ method docstring

Return len(self).

### __mul__ method docstring

Return self*value.

### object method docstring

The most base type

### __rmul__ method docstring

Return value*self.

### Tuple method docstring

Tuple type; Tuple[X, Y] is the cross-product type of X and Y. Example: Tuple[T1, T2] is a tuple of two elements corresponding to type variables T1 and T2. Tuple[int, float, str] is a tuple of an int, a float and a string. To specify a variable-length tuple of homogeneous type, use Tuple[T, ...].

### count method docstring

T.count(value) -> integer -- return number of occurrences of value

### index method docstring

T.index(value, [start, [stop]]) -> integer -- return first index of value. Raises ValueError if the value is not present.

## VariableNameInterface class docstring



### __init__ method docstring

Initialize self. See help(type(self)) for accurate signature.

### _get_previous_variable_name method docstring

Get a previous variable name.<hr>

**[Returns]**

- `previous_variable_name`: str
  - A previous variable name of this instance. If that value is not existing, then a blank string will be returned.

## WidthInterface class docstring



### ABCMeta method docstring

Metaclass for defining Abstract Base Classes (ABCs). Use this metaclass to create an ABC. An ABC can be subclassed directly, and then acts as a mix-in class. You can also register unrelated concrete classes (even built-in classes) and unrelated ABCs as 'virtual subclasses' -- these and their descendants will be considered subclasses of the registering ABC by the built-in issubclass() function, but the registering ABC won't show up in their MRO (Method Resolution Order) nor will method implementations defined by the registering ABC be callable (not even via super()).

### __init__ method docstring

Initialize self. See help(type(self)) for accurate signature.

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

### _append_width_attr_linking_setting method docstring

Append a width attribute linking setting.

### _append_width_update_expression method docstring

Append width updating expression.

### _delete_snapshot_exists_val method docstring

Delete boolean value whether snapshot value exists or not.<hr>

**[Parameters]**

- `snapshot_name`: str
  - Target snapshot name.

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

### _initialize_ss_exists_val_if_not_initialized method docstring

Initialize _snapshot_exists_ value it hasn't been initialized yet.

### _initialize_width_if_not_initialized method docstring

Initialize _width attribute if it hasn't been initialized yet.

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

Make value's snapshot.<hr>

**[Parameters]**

- `snapshot_name`: str
  - Target snapshot name.

### _revert method docstring

Revert value if snapshot exists.<hr>

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

### _update_width_and_skip_appending_exp method docstring

Update width value and skip appending expression.<hr>

**[Parameters]**

- `value`: int or Int
  - Width value to set.

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

### animation_width method docstring

Set the width animation setting.<hr>

**[Parameters]**

- `width`: Int or int
  - The final width of the animation.
- `duration`: Int or int, default 3000
  - Milliseconds before an animation ends.
- `delay`: Int or int, default 0
  - Milliseconds before an animation starts.
- `easing`: Easing, default Easing.LINEAR
  - Easing setting.

<hr>

**[Returns]**

- `animation_width`: AnimationWidth
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
>>> _ = rectangle.animation_width(
...     width=100,
...     duration=1500,
...     easing=ap.Easing.EASE_OUT_QUINT,
... ).start()
```

<hr>

**[References]**

- [animation_width and animation_height interfaces document](https://simon-ritchie.github.io/apysc/animation_width_and_height.html)
- [Animation interfaces duration setting document](https://simon-ritchie.github.io/apysc/animation_duration.html)
- [Animation interfaces delay setting document](https://simon-ritchie.github.io/apysc/animation_delay.html)
- [Each animation interface return value document](https://simon-ritchie.github.io/apysc/animation_return_value.html)
- [Sequential animation setting document](https://simon-ritchie.github.io/apysc/sequential_animation.html)
- [animation_parallel interface document](https://simon-ritchie.github.io/apysc/animation_parallel.html)
- [Easing enum document](https://simon-ritchie.github.io/apysc/easing_enum.html)

## _StageNotCreatedError class docstring



### __init__ method docstring

Initialize self. See help(type(self)) for accurate signature.

### with_traceback method docstring

Exception.with_traceback(tb) -- set self.__traceback__ to tb and return self.

## datetime class docstring

datetime(year, month, day[, hour[, minute[, second[, microsecond[,tzinfo]]]]]) The year, month and day arguments are required. tzinfo may be None, or an instance of a tzinfo subclass. The remaining arguments may be ints.

datetime(year, month, day[, hour[, minute[, second[, microsecond[,tzinfo]]]]]) The year, month and day arguments are required. tzinfo may be None, or an instance of a tzinfo subclass. The remaining arguments may be ints.

### __add__ method docstring

Return self+value.

### __format__ method docstring

Formats self with strftime.

### __init__ method docstring

Initialize self. See help(type(self)) for accurate signature.

### __radd__ method docstring

Return value+self.

### __reduce__ method docstring

__reduce__() -> (cls, state)

### __reduce_ex__ method docstring

__reduce_ex__(proto) -> (cls, state)

### __rsub__ method docstring

Return value-self.

### __sub__ method docstring

Return self-value.

### astimezone method docstring

tz -> convert to local time in new timezone tz

### combine method docstring

date, time -> datetime with same date and time fields

### ctime method docstring

Return ctime() style string.

### date method docstring

Return date object with same year, month and day.

### dst method docstring

Return self.tzinfo.dst(self).

### fromordinal method docstring

int -> date corresponding to a proleptic Gregorian ordinal.

### fromtimestamp method docstring

timestamp[, tz] -> tz's local time from POSIX timestamp.

### isocalendar method docstring

Return a 3-tuple containing ISO year, week number, and weekday.

### isoformat method docstring

[sep] -> string in ISO 8601 format, YYYY-MM-DDT[HH[:MM[:SS[.mmm[uuu]]]]][+HH:MM]. sep is used to separate the year from the time, and defaults to 'T'. timespec specifies what components of the time to include (allowed values are 'auto', 'hours', 'minutes', 'seconds', 'milliseconds', and 'microseconds').

### isoweekday method docstring

Return the day of the week represented by the date. Monday == 1 ... Sunday == 7

### now method docstring

Returns new datetime object representing current time local to tz. tz Timezone object. If no tz is specified, uses local timezone.

### replace method docstring

Return datetime with new specified fields.

### strftime method docstring

format -> strftime() style string.

### strptime method docstring

string, format -> new datetime parsed from a string (like time.strptime()).

### time method docstring

Return time object with same time but with tzinfo=None.

### timestamp method docstring

Return POSIX timestamp as float.

### timetuple method docstring

Return time tuple, compatible with time.localtime().

### timetz method docstring

Return time object with same time and tzinfo.

### today method docstring

Current date or datetime: same as self.__class__.fromtimestamp(time.time()).

### toordinal method docstring

Return proleptic Gregorian ordinal. January 1 of year 1 is day 1.

### tzname method docstring

Return self.tzinfo.tzname(self).

### utcfromtimestamp method docstring

Construct a naive UTC datetime from a POSIX timestamp.

### utcnow method docstring

Return a new datetime representing UTC day and time.

### utcoffset method docstring

Return self.tzinfo.utcoffset(self).

### utctimetuple method docstring

Return UTC time tuple, compatible with time.localtime().

### weekday method docstring

Return the day of the week represented by the date. Monday == 0 ... Sunday == 6