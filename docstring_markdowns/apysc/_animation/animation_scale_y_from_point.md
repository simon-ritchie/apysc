# apysc._animation.animation_scale_y_from_point docstrings

## Module summary

Class implementation for the scale-y from the given point animation value.

## AnimationBase class docstring



### GenericMeta method docstring

Metaclass for generic types. This is a metaclass for typing.Generic and generic ABCs defined in typing module. User defined subclasses of GenericMeta can override __new__ and invoke super().__new__. Note that GenericMeta.__new__ has strict rules on what is allowed in its bases argument: * plain Generic is disallowed in bases; * Generic[...] should appear in bases at most once; * if Generic[...] is present, then it should list all type variables that appear in other bases. In addition, type of all generic bases is erased, e.g., C[int] is stripped to plain C.

### __init__ method docstring

Base class for each animation setting.<hr>

**[Parameters]**

- `variable_name`: str
  - Variable name.

### ABC method docstring

Helper class that provides a standard way to create an ABC using inheritance.

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

### _get_animation_basic_expression method docstring

Get an animation basic expression string.<hr>

**[Returns]**

- `expression`: str
  - An animation basic expression string.

### _get_animation_complete_handler_expression method docstring

Get a expression of the animation complete handlers setting.<hr>

**[Returns]**

- `expression`: str
  - Target expression string. e.g., ' .after(handler_name)'

<hr>

**[Notes]**

If multiple handlers are registered, then multiple lines expression will be returned.

### _get_animation_func_expression method docstring

Get a animation function expression.

### _get_complete_event_in_handler_head_expression method docstring

Get an expression to be inserted into the complete event handler's head.

### _get_custom_event_type_str method docstring

Get a custom event type string from a type value.<hr>

**[Parameters]**

- `custom_event_type`: CustomEventType or str
  - Target custom event type or string.

<hr>

**[Returns]**

- `custom_event_type_str`: str
  - A custom event type string.

### _get_previous_variable_name method docstring

Get a previous variable name.<hr>

**[Returns]**

- `previous_variable_name`: str
  - A previous variable name of this instance. If that value is not existing, then a blank string will be returned.

### _initialize_blank_object_if_not_initialized method docstring

Initialize a blank object value if it hasn't been initialized yet.

### _initialize_custom_event_handlers_if_not_initialized method docstring

Initialize the _custom_event_handlers data if it hasn't been initialized yet.<hr>

**[Parameters]**

- `custom_event_type_str`: str
  - Target custom event type string.

### _set_basic_animation_settings method docstring

Set the basic animation settings.<hr>

**[Parameters]**

- `target`: VariableNameInterface
  - A target instance of the animation target (e.g., `DisplayObject` instance).
- `duration`: int or Int, default 3000
  - Milliseconds before an animation ends.
- `delay`: int or Int, default 0
  - Milliseconds before an animation starts.
- `easing`: Easing, default Easing.LINEAR
  - Easing setting. If None, Linear calculation is used.

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

### _validate_animation_not_started method docstring

Validate whether an animation hasn't already been started.<hr>

**[Raises]**

- Exception: If an animation has already been started.

### animation_complete method docstring

Add a animation complete event listener setting.<hr>

**[Parameters]**

- `handler`: _Handler
  - A callable that an instance calls when an animation is complete.
- `options`: dict or None, default None
  - Optional arguments dictionary to be passed to a handler.

<hr>

**[Returns]**

- `self`: AnimatonBase
  - This instance.

<hr>

**[Raises]**

- Exception: If calling this interface after an animation starts

<hr>

**[Notes]**

This interface can only use before an animation starts<hr>

**[Examples]**

```py
>>> import apysc as ap
>>> def on_animation_complete(
...         e: ap.AnimationEvent[ap.Rectangle],
...         options: dict) -> None:
...     ap.trace('Animation completed!')
>>> stage: ap.Stage = ap.Stage()
>>> sprite: ap.Sprite = ap.Sprite()
>>> sprite.graphics.begin_fill(color='#0af')
>>> rectangle: ap.Rectangle = sprite.graphics.draw_rect(
...     x=50, y=50, width=50, height=50)
>>> _ = rectangle.animation_x(
...     x=100,
... ).animation_complete(on_animation_complete).start()
```

<hr>

**[References]**

- [AnimationBase class animation_complete interface document](https://simon-ritchie.github.io/apysc/animation_complete.html)
- [About the handler options’ type document](https://simon-ritchie.github.io/apysc/about_handler_options_type.html)

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

### start method docstring

Start an animation with current settings.<hr>

**[Returns]**

- `self`: AnimatonBase
  - This instance.

<hr>

**[Examples]**

```py
>>> import apysc as ap
>>> stage: ap.Stage = ap.Stage()
>>> sprite: ap.Sprite = ap.Sprite()
>>> sprite.graphics.begin_fill(color='#0af')
>>> rectangle: ap.Rectangle = sprite.graphics.draw_rect(
...     x=50, y=50, width=50, height=50)
>>> _ = rectangle.animation_x(x=100).start()
```

<hr>

**[References]**

- [AnimationBase class start interface](https://simon-ritchie.github.io/apysc/animation_base_start.html)

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

## AnimationScaleYFromPoint class docstring

The animation class for a scale-y from the given point.

The animation class for a scale-y from the given point.<hr>

**[Examples]**

```py
>>> import apysc as ap
>>> stage: ap.Stage = ap.Stage()
>>> sprite: ap.Sprite = ap.Sprite()
>>> sprite.graphics.begin_fill(color='#0af')
>>> rectangle: ap.Rectangle = sprite.graphics.draw_rect(
...     x=50, y=50, width=50, height=50)
>>> animation: ap.AnimationScaleYFromPoint
>>> animation = rectangle.animation_scale_y_from_point(
...     scale_y_from_point=0.5,
...     y=ap.Int(100),
...     duration=1500,
...     easing=ap.Easing.EASE_OUT_QUINT,
... )
>>> _ = animation.start()
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

### GenericMeta method docstring

Metaclass for generic types. This is a metaclass for typing.Generic and generic ABCs defined in typing module. User defined subclasses of GenericMeta can override __new__ and invoke super().__new__. Note that GenericMeta.__new__ has strict rules on what is allowed in its bases argument: * plain Generic is disallowed in bases; * Generic[...] should appear in bases at most once; * if Generic[...] is present, then it should list all type variables that appear in other bases. In addition, type of all generic bases is erased, e.g., C[int] is stripped to plain C.

### __init__ method docstring

The animation class for a scale-y from the given point.<hr>

**[Parameters]**

- `target`: ScaleYFromPointInterface
  - A target instance of the animation target (e.g., `Rectangle` instance).
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

**[Raises]**

- TypeError: If a specified target is not a ScaleXFromPointInterface instance.

### ABC method docstring

Helper class that provides a standard way to create an ABC using inheritance.

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

### _get_animation_basic_expression method docstring

Get an animation basic expression string.<hr>

**[Returns]**

- `expression`: str
  - An animation basic expression string.

### _get_animation_complete_handler_expression method docstring

Get a expression of the animation complete handlers setting.<hr>

**[Returns]**

- `expression`: str
  - Target expression string. e.g., ' .after(handler_name)'

<hr>

**[Notes]**

If multiple handlers are registered, then multiple lines expression will be returned.

### _get_animation_func_expression method docstring

Get a animation function expression.<hr>

**[Returns]**

- `expression`: str
  - Animation function expression.

### _get_complete_event_in_handler_head_expression method docstring

Get an expression to be inserted into the complete event handler's head.<hr>

**[Returns]**

- `expression`: str
  - An expression to be inserted into the complete event handler's head.

### _get_custom_event_type_str method docstring

Get a custom event type string from a type value.<hr>

**[Parameters]**

- `custom_event_type`: CustomEventType or str
  - Target custom event type or string.

<hr>

**[Returns]**

- `custom_event_type_str`: str
  - A custom event type string.

### _get_previous_variable_name method docstring

Get a previous variable name.<hr>

**[Returns]**

- `previous_variable_name`: str
  - A previous variable name of this instance. If that value is not existing, then a blank string will be returned.

### AnimationScaleYFromPoint method docstring

The animation class for a scale-y from the given point.<hr>

**[Examples]**

```py
>>> import apysc as ap
>>> stage: ap.Stage = ap.Stage()
>>> sprite: ap.Sprite = ap.Sprite()
>>> sprite.graphics.begin_fill(color='#0af')
>>> rectangle: ap.Rectangle = sprite.graphics.draw_rect(
...     x=50, y=50, width=50, height=50)
>>> animation: ap.AnimationScaleYFromPoint
>>> animation = rectangle.animation_scale_y_from_point(
...     scale_y_from_point=0.5,
...     y=ap.Int(100),
...     duration=1500,
...     easing=ap.Easing.EASE_OUT_QUINT,
... )
>>> _ = animation.start()
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

### _initialize_blank_object_if_not_initialized method docstring

Initialize a blank object value if it hasn't been initialized yet.

### _initialize_custom_event_handlers_if_not_initialized method docstring

Initialize the _custom_event_handlers data if it hasn't been initialized yet.<hr>

**[Parameters]**

- `custom_event_type_str`: str
  - Target custom event type string.

### _set_basic_animation_settings method docstring

Set the basic animation settings.<hr>

**[Parameters]**

- `target`: VariableNameInterface
  - A target instance of the animation target (e.g., `DisplayObject` instance).
- `duration`: int or Int, default 3000
  - Milliseconds before an animation ends.
- `delay`: int or Int, default 0
  - Milliseconds before an animation starts.
- `easing`: Easing, default Easing.LINEAR
  - Easing setting. If None, Linear calculation is used.

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

### _validate_animation_not_started method docstring

Validate whether an animation hasn't already been started.<hr>

**[Raises]**

- Exception: If an animation has already been started.

### animation_complete method docstring

Add a animation complete event listener setting.<hr>

**[Parameters]**

- `handler`: _Handler
  - A callable that an instance calls when an animation is complete.
- `options`: dict or None, default None
  - Optional arguments dictionary to be passed to a handler.

<hr>

**[Returns]**

- `self`: AnimatonBase
  - This instance.

<hr>

**[Raises]**

- Exception: If calling this interface after an animation starts

<hr>

**[Notes]**

This interface can only use before an animation starts<hr>

**[Examples]**

```py
>>> import apysc as ap
>>> def on_animation_complete(
...         e: ap.AnimationEvent[ap.Rectangle],
...         options: dict) -> None:
...     ap.trace('Animation completed!')
>>> stage: ap.Stage = ap.Stage()
>>> sprite: ap.Sprite = ap.Sprite()
>>> sprite.graphics.begin_fill(color='#0af')
>>> rectangle: ap.Rectangle = sprite.graphics.draw_rect(
...     x=50, y=50, width=50, height=50)
>>> _ = rectangle.animation_x(
...     x=100,
... ).animation_complete(on_animation_complete).start()
```

<hr>

**[References]**

- [AnimationBase class animation_complete interface document](https://simon-ritchie.github.io/apysc/animation_complete.html)
- [About the handler options’ type document](https://simon-ritchie.github.io/apysc/about_handler_options_type.html)

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

### start method docstring

Start an animation with current settings.<hr>

**[Returns]**

- `self`: AnimatonBase
  - This instance.

<hr>

**[Examples]**

```py
>>> import apysc as ap
>>> stage: ap.Stage = ap.Stage()
>>> sprite: ap.Sprite = ap.Sprite()
>>> sprite.graphics.begin_fill(color='#0af')
>>> rectangle: ap.Rectangle = sprite.graphics.draw_rect(
...     x=50, y=50, width=50, height=50)
>>> _ = rectangle.animation_x(x=100).start()
```

<hr>

**[References]**

- [AnimationBase class start interface](https://simon-ritchie.github.io/apysc/animation_base_start.html)

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

## Easing class docstring

Enum class for the easing setting.

Enum class for the easing setting.<hr>

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

- [Easing enum document](https://simon-ritchie.github.io/apysc/easing_enum.html)

### EnumMeta method docstring

Metaclass for Enum

## Generic class docstring

Abstract base class for generic types. A generic type is typically declared by inheriting from this class parameterized with one or more type variables. For example, a generic mapping type might be defined as:: class Mapping(Generic[KT, VT]): def __getitem__(self, key: KT) -> VT: ... # Etc. This class can then be used as follows:: def lookup_name(mapping: Mapping[KT, VT], key: KT, default: VT) -> VT: try: return mapping[key] except KeyError: return default

Abstract base class for generic types. A generic type is typically declared by inheriting from this class parameterized with one or more type variables. For example, a generic mapping type might be defined as:: class Mapping(Generic[KT, VT]): def __getitem__(self, key: KT) -> VT: ... # Etc. This class can then be used as follows:: def lookup_name(mapping: Mapping[KT, VT], key: KT, default: VT) -> VT: try: return mapping[key] except KeyError: return default

### GenericMeta method docstring

Metaclass for generic types. This is a metaclass for typing.Generic and generic ABCs defined in typing module. User defined subclasses of GenericMeta can override __new__ and invoke super().__new__. Note that GenericMeta.__new__ has strict rules on what is allowed in its bases argument: * plain Generic is disallowed in bases; * Generic[...] should appear in bases at most once; * if Generic[...] is present, then it should list all type variables that appear in other bases. In addition, type of all generic bases is erased, e.g., C[int] is stripped to plain C.

### __init__ method docstring

Initialize self. See help(type(self)) for accurate signature.

### object method docstring

The most base type

### Generic method docstring

Abstract base class for generic types. A generic type is typically declared by inheriting from this class parameterized with one or more type variables. For example, a generic mapping type might be defined as:: class Mapping(Generic[KT, VT]): def __getitem__(self, key: KT) -> VT: ... # Etc. This class can then be used as follows:: def lookup_name(mapping: Mapping[KT, VT], key: KT, default: VT) -> VT: try: return mapping[key] except KeyError: return default

## Int class docstring

Integer class for the apysc library.

Integer class for the apysc library.<hr>

**[Examples]**

```py
>>> import apysc as ap
>>> int_val: ap.Int = ap.Int(10)
>>> int_val
Int(10)

>>> int_val == 10
Boolean(True)

>>> int_val == ap.Int(10)
Boolean(True)

>>> int_val >= 10
Boolean(True)

>>> int_val += 10
>>> int_val
Int(20)

>>> int_val = ap.Int(10.5)
>>> int_val
Int(10)
```

<hr>

**[References]**

- [Int and Number document](https://simon-ritchie.github.io/apysc/int_and_number.html)
- [Int and Number common arithmetic operations document](https://simon-ritchie.github.io/apysc/int_and_number_arithmetic_operations.html)
- [Int and Number common comparison operations document](https://simon-ritchie.github.io/apysc/int_and_number_comparison_operations.html)

### __add__ method docstring

Method for addition.<hr>

**[Parameters]**

- `other`: int or float or NumberValueInterface
  - Other value to add.

<hr>

**[Returns]**

- `result`: NumberValueInterface
  - Addition result value.

### GenericMeta method docstring

Metaclass for generic types. This is a metaclass for typing.Generic and generic ABCs defined in typing module. User defined subclasses of GenericMeta can override __new__ and invoke super().__new__. Note that GenericMeta.__new__ has strict rules on what is allowed in its bases argument: * plain Generic is disallowed in bases; * Generic[...] should appear in bases at most once; * if Generic[...] is present, then it should list all type variables that appear in other bases. In addition, type of all generic bases is erased, e.g., C[int] is stripped to plain C.

### __eq__ method docstring

Equal comparison method.<hr>

**[Parameters]**

- `other`: *
  - Other value to compare. Builtin types, Int, and Number class instances are acceptable.

<hr>

**[Returns]**

- `result`: Boolean
  - If specified value is same amount, True will be returned.

### __float__ method docstring

Float conversion method.<hr>

**[Returns]**

- `float_`: float
  - Converted float value.

### __floordiv__ method docstring

Method for floor division (return integer).<hr>

**[Parameters]**

- `other`: int or float or NumberValueInterface
  - Other value for floor division.

<hr>

**[Returns]**

- `result`: Int
  - Floor division result value.

### __ge__ method docstring

Greater than equal comparison method.<hr>

**[Parameters]**

- `other`: *
  - Other value to compare. Builtin types, Int, and Number class instances are acceptable.

<hr>

**[Returns]**

- `result`: Boolean
  - If this value is greater than or equal to a specified value, then True will be returned.

### __gt__ method docstring

Greater than comparison method.<hr>

**[Parameters]**

- `other`: *
  - Other value to compare. Builtin types, Int, and Number class instances are acceptable.

<hr>

**[Returns]**

- `result`: Boolean
  - If this value is greater than a specified value, then True will be returned.

### __iadd__ method docstring

Method for incremental addition.<hr>

**[Parameters]**

- `other`: int or float or NumberValueInterface
  - Other value for` incremental addition.

<hr>

**[Returns]**

- `result`: NumberValueInterface
  - Incremental addition result value.

### __imul__ method docstring

Method for incremental multiplication.<hr>

**[Parameters]**

- `other`: int or float or NumberValueInterface
  - Other value for incremental multiplication.

<hr>

**[Returns]**

- `result`: NumberValueInterface
  - Incremental multiplication result value.

### __init__ method docstring

Integer class for apysc library.<hr>

**[Parameters]**

- `value`: int or float or Int or Number
  - Initial integer value. If the `float` or `Number` value is specified, this class casts it to an integer.

<hr>

**[Examples]**

```py
>>> import apysc as ap
>>> int_val: ap.Int = ap.Int(10)
>>> int_val
Int(10)

>>> int_val == 10
Boolean(True)

>>> int_val == ap.Int(10)
Boolean(True)

>>> int_val >= 10
Boolean(True)

>>> int_val += 10
>>> int_val
Int(20)

>>> int_val = ap.Int(10.5)
>>> int_val
Int(10)
```

<hr>

**[References]**

- [Int and Number document](https://simon-ritchie.github.io/apysc/int_and_number.html)
- [Int and Number common arithmetic operations document](https://simon-ritchie.github.io/apysc/int_and_number_arithmetic_operations.html)
- [Int and Number common comparison operations document](https://simon-ritchie.github.io/apysc/int_and_number_comparison_operations.html)

### __int__ method docstring

Integer conversion method.<hr>

**[Returns]**

- `integer`: int
  - Converted integer value.

### __isub__ method docstring

Method for incremental subtraction.<hr>

**[Parameters]**

- `other`: int or float or NumberValueInterface
  - Other value for incremental subtraction.

<hr>

**[Returns]**

- `result`: NumberValueInterface
  - Incremental subtraction result value.

### __itruediv__ method docstring

Method for incremental true division.<hr>

**[Parameters]**

- `other`: int or float or NumberValueInterface
  - Other value for incremental true division.

<hr>

**[Returns]**

- `result`: NumberValueInterface
  - Incremental true division result value.

### __le__ method docstring

Less than equal comparison method.<hr>

**[Parameters]**

- `other`: *
  - Other value to compare. Builtin types, Int, and Number class instances are acceptable.

<hr>

**[Returns]**

- `result`: Boolean
  - If this value is less than or equal to a specified value, then True will be returned.

### __lt__ method docstring

Less than comparison method.<hr>

**[Parameters]**

- `other`: *
  - Other value to compare. Builtin types, Int, and Number class instances are acceptable.

<hr>

**[Returns]**

- `result`: Boolean
  - If this value is less than a specified value, then True will be returned.

### __mod__ method docstring

Method for the modulo operation.<hr>

**[Parameters]**

- `other`: int or float or NumberValueInterface
  - Other value to be used in the modulo operation.

<hr>

**[Returns]**

- `result`: NumberValueInterface
  - Modulo operation result value.

### __mul__ method docstring

Method for multiplication.<hr>

**[Parameters]**

- `other`: int or float or NumberValueInterface
  - Other value to multiply.

<hr>

**[Returns]**

- `result`: NumberValueInterface
  - Multiplication result value.

### __ne__ method docstring

Not equal comparison method.<hr>

**[Parameters]**

- `other`: *
  - Other value to compare. Builtin types, Int, and Number class instances are acceptable.

<hr>

**[Returns]**

- `result`: Boolean
  - If specified value is not same amount, True will be returned.

### object method docstring

The most base type

### __repr__ method docstring

Get a representation string of this instance.<hr>

**[Returns]**

- `repr_str`: str
  - Representation string of this instance.

### __str__ method docstring

String conversion method.<hr>

**[Returns]**

- `string`: str
  - Converted value string.

### __sub__ method docstring

Method for subtraction.<hr>

**[Parameters]**

- `other`: int or float or NumberValueInterface
  - Other value to subtract.

<hr>

**[Returns]**

- `result`: NumberValueInterface
  - Subtraction result value.

### __truediv__ method docstring

Method for true division (return floating point number).<hr>

**[Parameters]**

- `other`: int or float or NumberValueInterface
  - Other value for true division.

<hr>

**[Returns]**

- `result`: Number
  - True division result value.

### _append_addition_expression method docstring

Append addition expression.<hr>

**[Parameters]**

- `result`: NumberValueInterface
  - Addition result value.
- `other`: int or float or NumberValueInterface
  - Other value to add.

### _append_cast_expression method docstring

Append integer cast (parseInt) expression.<hr>

**[Parameters]**

- `is_number_specified`: bool
  - Boolean value whether a specified value is Number instance or not.

### _append_copy_expression method docstring

Append copy expression.<hr>

**[Parameters]**

- `result_variable_name`: str
  - Copied value's variable name.

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

### _append_eq_expression method docstring

Append __eq__ method expression.<hr>

**[Parameters]**

- `result`: Boolean
  - Result boolean value.
- `other`: VariableNameInterface
  - Other value to compare.

### _append_floor_division_expression method docstring

Append floor division expression.<hr>

**[Parameters]**

- `result`: NumberValueInterface
  - Floor division result value.
- `other`: int or float or NumberValueInterface
  - Other value for floor division.

### _append_ge_expression method docstring

Append __ge__ expression.<hr>

**[Parameters]**

- `result`: Boolean
  - Result boolean value.
- `other`: VariableNameInterface
  - Other value to compare.

### _append_gt_expression method docstring

Append __gt__ expression.<hr>

**[Parameters]**

- `result`: Boolean
  - Result boolean value.
- `other`: VariableNameInterface
  - Other value to compare.

### _append_incremental_calc_substitution_expression method docstring

Append a incremental calculation's substitution expression. This method will be called from the each interface.

### _append_le_expression method docstring

Append __le__ method expression.<hr>

**[Parameters]**

- `result`: Boolean
  - Result boolean value.
- `other`: VariableNameInterface
  - Other value to compare.

### _append_lt_expression method docstring

Append __lt__ method expression.<hr>

**[Parameters]**

- `result`: Boolean
  - Result boolean value.
- `other`: VariableNameInterface
  - Other value to compare.

### _append_modulo_expression method docstring

Append a module expression.<hr>

**[Parameters]**

- `result`: NumberValueInterface
  - Modulo operation result value.
- `other`: int or float or NumberValueInterface
  - Other value to be used in the modulo operation.

### _append_multiplication_expression method docstring

Append multiplication expression.<hr>

**[Parameters]**

- `result`: NumberValueInterface
  - Multiplication result value.
- `other`: int or float or NumberValueInterface
  - Other value to multiply.

### _append_ne_expression method docstring

Append __ne__ method expression.<hr>

**[Parameters]**

- `result`: Boolean
  - Result boolean value.
- `other`: VariableNameInterface
  - Other value to compare.

### _append_subtraction_expression method docstring

Append subtraction expression.<hr>

**[Parameters]**

- `result`: NumberValueInterface
  - Subtraction result value.
- `other`: int or float or NumberValueInterface
  - Other value to subtract.

### _append_true_division_expression method docstring

Append true division expression.<hr>

**[Parameters]**

- `result`: NumberValueInterface
  - True division result value.
- `other`: int or float or NumberValueInterface
  - Other value for true division.

### _append_value_setter_expression method docstring

Append value's setter expresion.<hr>

**[Parameters]**

- `value`: int or float or NumberValueInterface
  - Any number value to set.

### _append_value_updating_cpy_exp_to_handler_scope method docstring

Append a value updating copy expression if the current scope is an event handler's one.<hr>

**[Parameters]**

- `result_variable_name`: str
  - Copied value's variable name.

### _convert_other_val_to_int_or_number method docstring

If comparison other value is int or float, then convert it to Int or Number.<hr>

**[Parameters]**

- `other`: *
  - Other comparison value.

<hr>

**[Returns]**

- `converted_val`: *
  - Converted value. If int is specified, then this will be Int. float is specified, then Number. Other type will be returned directly (not to be converted).

### _copy method docstring

Make a deep copy of this instance.<hr>

**[Returns]**

- `result`: *
  - Copied instance.

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

### Int method docstring

Integer class for the apysc library.<hr>

**[Examples]**

```py
>>> import apysc as ap
>>> int_val: ap.Int = ap.Int(10)
>>> int_val
Int(10)

>>> int_val == 10
Boolean(True)

>>> int_val == ap.Int(10)
Boolean(True)

>>> int_val >= 10
Boolean(True)

>>> int_val += 10
>>> int_val
Int(20)

>>> int_val = ap.Int(10.5)
>>> int_val
Int(10)
```

<hr>

**[References]**

- [Int and Number document](https://simon-ritchie.github.io/apysc/int_and_number.html)
- [Int and Number common arithmetic operations document](https://simon-ritchie.github.io/apysc/int_and_number_arithmetic_operations.html)
- [Int and Number common comparison operations document](https://simon-ritchie.github.io/apysc/int_and_number_comparison_operations.html)

### _initialize_blank_object_if_not_initialized method docstring

Initialize a blank object value if it hasn't been initialized yet.

### _initialize_custom_event_handlers_if_not_initialized method docstring

Initialize the _custom_event_handlers data if it hasn't been initialized yet.<hr>

**[Parameters]**

- `custom_event_type_str`: str
  - Target custom event type string.

### _initialize_ss_exists_val_if_not_initialized method docstring

Initialize _snapshot_exists_ value it hasn't been initialized yet.

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

### _set_custom_event_handler_data method docstring

Set a handler's data to the dictionary.<hr>

**[Parameters]**

- `handler`: _Handler
  - Callable will be called when an event is dispatched.
- `custom_event_type_str`: str
  - Target custom event type string.
- `options`: dict or None
  - Optional arguments dictionary to be passed to a handler.

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

### _set_value_and_skip_expression_appending method docstring

Update value attribute and skip expression appending.<hr>

**[Parameters]**

- `value`: int or float or Int or Number
  - Any number value to set. If float or Number value is specified, that value will be cast to integer.

### _snapshot_exists method docstring

Get a boolean value whether snapshot value exists or not.<hr>

**[Parameters]**

- `snapshot_name`: str
  - Target snapshot name.

<hr>

**[Returns]**

- `snapshot_exists`: bool
  - Boolean value whether snapshot value exists or not.

### _unset_custom_event_handler_data method docstring

Unset a handler's data from the dictionary.<hr>

**[Parameters]**

- `handler`: _Handler
  - Callable will be called when an event is dispatched.
- `custom_event_type_str`: str
  - Target custom event type string.

### append_constructor_expression method docstring

Append current value's constructor expression.

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

## Number class docstring

Floating point number class for the apysc library.

Floating point number class for the apysc library.<hr>

**[Notes]**

Float class is the alias of the Number, and it behaves the same as the Number class.<hr>

**[Examples]**

```py
>>> import apysc as ap
>>> number: ap.Number = ap.Number(10.5)
>>> number
Number(10.5)

>>> number == 10.5
Boolean(True)

>>> number == ap.Number(10.5)
Boolean(True)

>>> number >= 10.5
Boolean(True)

>>> number += 10.3
>>> number
Number(20.8)
```

<hr>

**[References]**

- [Int and Number document](https://simon-ritchie.github.io/apysc/int_and_number.html)
- [Int and Number common arithmetic operations document](https://simon-ritchie.github.io/apysc/int_and_number_arithmetic_operations.html)
- [Int and Number common comparison operations document](https://simon-ritchie.github.io/apysc/int_and_number_comparison_operations.html)

### __add__ method docstring

Method for addition.<hr>

**[Parameters]**

- `other`: int or float or NumberValueInterface
  - Other value to add.

<hr>

**[Returns]**

- `result`: NumberValueInterface
  - Addition result value.

### GenericMeta method docstring

Metaclass for generic types. This is a metaclass for typing.Generic and generic ABCs defined in typing module. User defined subclasses of GenericMeta can override __new__ and invoke super().__new__. Note that GenericMeta.__new__ has strict rules on what is allowed in its bases argument: * plain Generic is disallowed in bases; * Generic[...] should appear in bases at most once; * if Generic[...] is present, then it should list all type variables that appear in other bases. In addition, type of all generic bases is erased, e.g., C[int] is stripped to plain C.

### __eq__ method docstring

Equal comparison method.<hr>

**[Parameters]**

- `other`: *
  - Other value to compare. Builtin types, Int, and Number class instances are acceptable.

<hr>

**[Returns]**

- `result`: Boolean
  - If specified value is same amount, True will be returned.

### __float__ method docstring

Float conversion method.<hr>

**[Returns]**

- `float_`: float
  - Converted float value.

### __floordiv__ method docstring

Method for floor division (return integer).<hr>

**[Parameters]**

- `other`: int or float or NumberValueInterface
  - Other value for floor division.

<hr>

**[Returns]**

- `result`: Int
  - Floor division result value.

### __ge__ method docstring

Greater than equal comparison method.<hr>

**[Parameters]**

- `other`: *
  - Other value to compare. Builtin types, Int, and Number class instances are acceptable.

<hr>

**[Returns]**

- `result`: Boolean
  - If this value is greater than or equal to a specified value, then True will be returned.

### __gt__ method docstring

Greater than comparison method.<hr>

**[Parameters]**

- `other`: *
  - Other value to compare. Builtin types, Int, and Number class instances are acceptable.

<hr>

**[Returns]**

- `result`: Boolean
  - If this value is greater than a specified value, then True will be returned.

### __iadd__ method docstring

Method for incremental addition.<hr>

**[Parameters]**

- `other`: int or float or NumberValueInterface
  - Other value for` incremental addition.

<hr>

**[Returns]**

- `result`: NumberValueInterface
  - Incremental addition result value.

### __imul__ method docstring

Method for incremental multiplication.<hr>

**[Parameters]**

- `other`: int or float or NumberValueInterface
  - Other value for incremental multiplication.

<hr>

**[Returns]**

- `result`: NumberValueInterface
  - Incremental multiplication result value.

### __init__ method docstring

Floating point number class for apysc library.<hr>

**[Parameters]**

- `value`: int or float or Int or Number
  - Initial floating point number value. This class casts it to float if you specify int or Int value.

<hr>

**[Notes]**

The `Float` class is the alias of the Number, and it behaves the same as the Number class.<hr>

**[Examples]**

```py
>>> import apysc as ap
>>> number: ap.Number = ap.Number(10.5)
>>> number
Number(10.5)

>>> number == 10.5
Boolean(True)

>>> number == ap.Number(10.5)
Boolean(True)

>>> number >= 10.5
Boolean(True)

>>> number += 10.3
>>> number
Number(20.8)
```

<hr>

**[References]**

- [Int and Number document](https://simon-ritchie.github.io/apysc/int_and_number.html)
- [Int and Number common arithmetic operations document](https://simon-ritchie.github.io/apysc/int_and_number_arithmetic_operations.html)
- [Int and Number common comparison operations document](https://simon-ritchie.github.io/apysc/int_and_number_comparison_operations.html)

### __int__ method docstring

Integer conversion method.<hr>

**[Returns]**

- `integer`: int
  - Converted integer value.

### __isub__ method docstring

Method for incremental subtraction.<hr>

**[Parameters]**

- `other`: int or float or NumberValueInterface
  - Other value for incremental subtraction.

<hr>

**[Returns]**

- `result`: NumberValueInterface
  - Incremental subtraction result value.

### __itruediv__ method docstring

Method for incremental true division.<hr>

**[Parameters]**

- `other`: int or float or NumberValueInterface
  - Other value for incremental true division.

<hr>

**[Returns]**

- `result`: NumberValueInterface
  - Incremental true division result value.

### __le__ method docstring

Less than equal comparison method.<hr>

**[Parameters]**

- `other`: *
  - Other value to compare. Builtin types, Int, and Number class instances are acceptable.

<hr>

**[Returns]**

- `result`: Boolean
  - If this value is less than or equal to a specified value, then True will be returned.

### __lt__ method docstring

Less than comparison method.<hr>

**[Parameters]**

- `other`: *
  - Other value to compare. Builtin types, Int, and Number class instances are acceptable.

<hr>

**[Returns]**

- `result`: Boolean
  - If this value is less than a specified value, then True will be returned.

### __mod__ method docstring

Method for the modulo operation.<hr>

**[Parameters]**

- `other`: int or float or NumberValueInterface
  - Other value to be used in the modulo operation.

<hr>

**[Returns]**

- `result`: NumberValueInterface
  - Modulo operation result value.

### __mul__ method docstring

Method for multiplication.<hr>

**[Parameters]**

- `other`: int or float or NumberValueInterface
  - Other value to multiply.

<hr>

**[Returns]**

- `result`: NumberValueInterface
  - Multiplication result value.

### __ne__ method docstring

Not equal comparison method.<hr>

**[Parameters]**

- `other`: *
  - Other value to compare. Builtin types, Int, and Number class instances are acceptable.

<hr>

**[Returns]**

- `result`: Boolean
  - If specified value is not same amount, True will be returned.

### object method docstring

The most base type

### __repr__ method docstring

Get a representation string of this instance.<hr>

**[Returns]**

- `repr_str`: str
  - Representation string of this instance.

### __str__ method docstring

String conversion method.<hr>

**[Returns]**

- `string`: str
  - Converted value string.

### __sub__ method docstring

Method for subtraction.<hr>

**[Parameters]**

- `other`: int or float or NumberValueInterface
  - Other value to subtract.

<hr>

**[Returns]**

- `result`: NumberValueInterface
  - Subtraction result value.

### __truediv__ method docstring

Method for true division (return floating point number).<hr>

**[Parameters]**

- `other`: int or float or NumberValueInterface
  - Other value for true division.

<hr>

**[Returns]**

- `result`: Number
  - True division result value.

### _append_addition_expression method docstring

Append addition expression.<hr>

**[Parameters]**

- `result`: NumberValueInterface
  - Addition result value.
- `other`: int or float or NumberValueInterface
  - Other value to add.

### _append_copy_expression method docstring

Append copy expression.<hr>

**[Parameters]**

- `result_variable_name`: str
  - Copied value's variable name.

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

### _append_eq_expression method docstring

Append __eq__ method expression.<hr>

**[Parameters]**

- `result`: Boolean
  - Result boolean value.
- `other`: VariableNameInterface
  - Other value to compare.

### _append_floor_division_expression method docstring

Append floor division expression.<hr>

**[Parameters]**

- `result`: NumberValueInterface
  - Floor division result value.
- `other`: int or float or NumberValueInterface
  - Other value for floor division.

### _append_ge_expression method docstring

Append __ge__ expression.<hr>

**[Parameters]**

- `result`: Boolean
  - Result boolean value.
- `other`: VariableNameInterface
  - Other value to compare.

### _append_gt_expression method docstring

Append __gt__ expression.<hr>

**[Parameters]**

- `result`: Boolean
  - Result boolean value.
- `other`: VariableNameInterface
  - Other value to compare.

### _append_incremental_calc_substitution_expression method docstring

Append a incremental calculation's substitution expression. This method will be called from the each interface.

### _append_le_expression method docstring

Append __le__ method expression.<hr>

**[Parameters]**

- `result`: Boolean
  - Result boolean value.
- `other`: VariableNameInterface
  - Other value to compare.

### _append_lt_expression method docstring

Append __lt__ method expression.<hr>

**[Parameters]**

- `result`: Boolean
  - Result boolean value.
- `other`: VariableNameInterface
  - Other value to compare.

### _append_modulo_expression method docstring

Append a module expression.<hr>

**[Parameters]**

- `result`: NumberValueInterface
  - Modulo operation result value.
- `other`: int or float or NumberValueInterface
  - Other value to be used in the modulo operation.

### _append_multiplication_expression method docstring

Append multiplication expression.<hr>

**[Parameters]**

- `result`: NumberValueInterface
  - Multiplication result value.
- `other`: int or float or NumberValueInterface
  - Other value to multiply.

### _append_ne_expression method docstring

Append __ne__ method expression.<hr>

**[Parameters]**

- `result`: Boolean
  - Result boolean value.
- `other`: VariableNameInterface
  - Other value to compare.

### _append_subtraction_expression method docstring

Append subtraction expression.<hr>

**[Parameters]**

- `result`: NumberValueInterface
  - Subtraction result value.
- `other`: int or float or NumberValueInterface
  - Other value to subtract.

### _append_true_division_expression method docstring

Append true division expression.<hr>

**[Parameters]**

- `result`: NumberValueInterface
  - True division result value.
- `other`: int or float or NumberValueInterface
  - Other value for true division.

### _append_value_setter_expression method docstring

Append value's setter expresion.<hr>

**[Parameters]**

- `value`: int or float or NumberValueInterface
  - Any number value to set.

### _append_value_updating_cpy_exp_to_handler_scope method docstring

Append a value updating copy expression if the current scope is an event handler's one.<hr>

**[Parameters]**

- `result_variable_name`: str
  - Copied value's variable name.

### _convert_other_val_to_int_or_number method docstring

If comparison other value is int or float, then convert it to Int or Number.<hr>

**[Parameters]**

- `other`: *
  - Other comparison value.

<hr>

**[Returns]**

- `converted_val`: *
  - Converted value. If int is specified, then this will be Int. float is specified, then Number. Other type will be returned directly (not to be converted).

### _copy method docstring

Make a deep copy of this instance.<hr>

**[Returns]**

- `result`: *
  - Copied instance.

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

### Number method docstring

Floating point number class for the apysc library.<hr>

**[Notes]**

Float class is the alias of the Number, and it behaves the same as the Number class.<hr>

**[Examples]**

```py
>>> import apysc as ap
>>> number: ap.Number = ap.Number(10.5)
>>> number
Number(10.5)

>>> number == 10.5
Boolean(True)

>>> number == ap.Number(10.5)
Boolean(True)

>>> number >= 10.5
Boolean(True)

>>> number += 10.3
>>> number
Number(20.8)
```

<hr>

**[References]**

- [Int and Number document](https://simon-ritchie.github.io/apysc/int_and_number.html)
- [Int and Number common arithmetic operations document](https://simon-ritchie.github.io/apysc/int_and_number_arithmetic_operations.html)
- [Int and Number common comparison operations document](https://simon-ritchie.github.io/apysc/int_and_number_comparison_operations.html)

### _initialize_blank_object_if_not_initialized method docstring

Initialize a blank object value if it hasn't been initialized yet.

### _initialize_custom_event_handlers_if_not_initialized method docstring

Initialize the _custom_event_handlers data if it hasn't been initialized yet.<hr>

**[Parameters]**

- `custom_event_type_str`: str
  - Target custom event type string.

### _initialize_ss_exists_val_if_not_initialized method docstring

Initialize _snapshot_exists_ value it hasn't been initialized yet.

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

### _set_custom_event_handler_data method docstring

Set a handler's data to the dictionary.<hr>

**[Parameters]**

- `handler`: _Handler
  - Callable will be called when an event is dispatched.
- `custom_event_type_str`: str
  - Target custom event type string.
- `options`: dict or None
  - Optional arguments dictionary to be passed to a handler.

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

### _set_value_and_skip_expression_appending method docstring

Update value attribute and skip expression appending.<hr>

**[Parameters]**

- `value`: int or float or Int or Number
  - Any number value to set. If float or Number value is specified, that value will be cast to integer.

### _snapshot_exists method docstring

Get a boolean value whether snapshot value exists or not.<hr>

**[Parameters]**

- `snapshot_name`: str
  - Target snapshot name.

<hr>

**[Returns]**

- `snapshot_exists`: bool
  - Boolean value whether snapshot value exists or not.

### _unset_custom_event_handler_data method docstring

Unset a handler's data from the dictionary.<hr>

**[Parameters]**

- `handler`: _Handler
  - Callable will be called when an event is dispatched.
- `custom_event_type_str`: str
  - Target custom event type string.

### append_constructor_expression method docstring

Append current value's constructor expression.

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

## TypeVar class docstring

Type variable. Usage:: T = TypeVar('T') # Can be anything A = TypeVar('A', str, bytes) # Must be str or bytes Type variables exist primarily for the benefit of static type checkers. They serve as the parameters for generic types as well as for generic function definitions. See class Generic for more information on generic types. Generic functions work as follows: def repeat(x: T, n: int) -> List[T]: '''Return a list containing n references to x.''' return [x]*n def longest(x: A, y: A) -> A: '''Return the longest of two strings.''' return x if len(x) >= len(y) else y The latter example's signature is essentially the overloading of (str, str) -> str and (bytes, bytes) -> bytes. Also note that if the arguments are instances of some subclass of str, the return type is still plain str. At runtime, isinstance(x, T) and issubclass(C, T) will raise TypeError. Type variables defined with covariant=True or contravariant=True can be used do declare covariant or contravariant generic types. See PEP 484 for more details. By default generic types are invariant in all type variables. Type variables can be introspected. e.g.: T.__name__ == 'T' T.__constraints__ == () T.__covariant__ == False T.__contravariant__ = False A.__constraints__ == (str, bytes)

Type variable. Usage:: T = TypeVar('T') # Can be anything A = TypeVar('A', str, bytes) # Must be str or bytes Type variables exist primarily for the benefit of static type checkers. They serve as the parameters for generic types as well as for generic function definitions. See class Generic for more information on generic types. Generic functions work as follows: def repeat(x: T, n: int) -> List[T]: '''Return a list containing n references to x.''' return [x]*n def longest(x: A, y: A) -> A: '''Return the longest of two strings.''' return x if len(x) >= len(y) else y The latter example's signature is essentially the overloading of (str, str) -> str and (bytes, bytes) -> bytes. Also note that if the arguments are instances of some subclass of str, the return type is still plain str. At runtime, isinstance(x, T) and issubclass(C, T) will raise TypeError. Type variables defined with covariant=True or contravariant=True can be used do declare covariant or contravariant generic types. See PEP 484 for more details. By default generic types are invariant in all type variables. Type variables can be introspected. e.g.: T.__name__ == 'T' T.__constraints__ == () T.__covariant__ == False T.__contravariant__ = False A.__constraints__ == (str, bytes)

### TypingMeta method docstring

Metaclass for most types defined in typing module (not a part of public API). This overrides __new__() to require an extra keyword parameter '_root', which serves as a guard against naive subclassing of the typing classes. Any legitimate class defined using a metaclass derived from TypingMeta must pass _root=True. This also defines a dummy constructor (all the work for most typing constructs is done in __new__) and a nicer repr().

### __new__ method docstring

Constructor. This only exists to give a better error message in case someone tries to subclass a special typing object (not a good idea).

## VariableNameInterface class docstring



### __init__ method docstring

Initialize self. See help(type(self)) for accurate signature.

### _get_previous_variable_name method docstring

Get a previous variable name.<hr>

**[Returns]**

- `previous_variable_name`: str
  - A previous variable name of this instance. If that value is not existing, then a blank string will be returned.