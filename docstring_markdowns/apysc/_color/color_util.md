# apysc._color.color_util docstrings

## Module summary

Color related implementations.

## _append_complement_hex_color_expression function docstring

Append complement_hex_color function's expression.<hr>

**[Parameters]**

- `hex_color_code`: String
  - Complemented hex color code string.

## _fill_one_digit_hex_color_code function docstring

Fill 1 digit hexadecimal color code until it becomes 6 digits.<hr>

**[Parameters]**

- `hex_color_code`: str
  - One digit hexadecimal color code (not including '#'). e.g., 'a', '0'

<hr>

**[Returns]**

- `filled_color_code`: str
  - Result color code. e.g., '00000a', '000000'

## _fill_three_digit_hex_color_code function docstring

Fill 3 digits hexadecimal color code until it becomes 6 digits.<hr>

**[Parameters]**

- `hex_color_code`: str
  - One digit hexadecimal color code (not including '#'). e.g., 'aaa', 'fff'

<hr>

**[Returns]**

- `filled_color_code`: str
  - Result color code. e.g., 'aaaaaa', 'ffffff'

## complement_hex_color function docstring

Complement hex color for convenience, for instance, add # prefix or three digits to six digits, upper case to lower case etc.<hr>

**[Parameters]**

- `hex_color_code`: str or String
  - Hexadecimal color code. e.g., 'ff0000', '#666', '#0'

<hr>

**[Returns]**

- `complemented_hex_color_code`: str or String
  - Result hex color code. e.g., '#ff0000', '#666666, '#000000'

## String class docstring

String class for apysc library.

String class for apysc library.<hr>

**[Examples]**

```py
>>> import apysc as ap
>>> string: ap.String = ap.String('Hello')
>>> string
String('Hello')

>>> string += ' World!'
>>> string
String('Hello World!')

>>> string.value = 'World!'
>>> string
String('World!')

>>> string.value = 'Hello!'
>>> string *= 3
>>> string
String('Hello!Hello!Hello!')
```

<hr>

**[References]**

- [String document](https://simon-ritchie.github.io/apysc/string.html)
- [String class comparison operations document](https://simon-ritchie.github.io/apysc/string_comparison_operations.html)
- [String class addition and multiplication operations document](https://simon-ritchie.github.io/apysc/string_addition_and_multiplication.html)

### __add__ method docstring

Method for addition (string concatenation).<hr>

**[Parameters]**

- `other`: str or String
  - Other string value to concatenate.

<hr>

**[Returns]**

- `result`: String
  - Concatenated result string.

### ABCMeta method docstring

Metaclass for defining Abstract Base Classes (ABCs). Use this metaclass to create an ABC. An ABC can be subclassed directly, and then acts as a mix-in class. You can also register unrelated concrete classes (even built-in classes) and unrelated ABCs as 'virtual subclasses' -- these and their descendants will be considered subclasses of the registering ABC by the built-in issubclass() function, but the registering ABC won't show up in their MRO (Method Resolution Order) nor will method implementations defined by the registering ABC be callable (not even via super()).

### __eq__ method docstring

Method for equal comparison.<hr>

**[Parameters]**

- `other`: *
  - Any value to compare.

<hr>

**[Returns]**

- `result`: Boolean
  - Comparison result. If same value of str or String is specified, True will be returned.

### __float__ method docstring

Method for float conversion.<hr>

**[Returns]**

- `result`: float
  - Converted float value.

### __ge__ method docstring

Method for greater than or equal comparison.<hr>

**[Parameters]**

- `other`: str or String
  - String value to compare.

<hr>

**[Returns]**

- `result`: Boolean
  - Comparison result.

### __gt__ method docstring

Method for greater than comparison.<hr>

**[Parameters]**

- `other`: str or String
  - String value to compare.

<hr>

**[Returns]**

- `result`: Boolean
  - Comparison result.

### __iadd__ method docstring

Method for incremental addition (string concatenation).<hr>

**[Parameters]**

- `other`: str or String
  - Other string value to concatenate.

<hr>

**[Returns]**

- `result`: String
  - Concatenated result string.

### __imul__ method docstring

Method for incremental multiplication (string repetition).<hr>

**[Parameters]**

- `other`: int or Int
  - String repetition number.

<hr>

**[Returns]**

- `result`: String
  - Repetition result string.

### __init__ method docstring

String class for apysc library.<hr>

**[Parameters]**

- `value`: str or String
  - Initial string value.

<hr>

**[Examples]**

```py
>>> import apysc as ap
>>> string: ap.String = ap.String('Hello')
>>> string
String('Hello')

>>> string += ' World!'
>>> string
String('Hello World!')
```

<hr>

**[References]**

- [String document](https://simon-ritchie.github.io/apysc/string.html)
- [String class comparison operations document](https://simon-ritchie.github.io/apysc/string_comparison_operations.html)
- [String class addition and multiplication operations document](https://simon-ritchie.github.io/apysc/string_addition_and_multiplication.html)

### __int__ method docstring

Method for integer conversion.<hr>

**[Returns]**

- `result`: int
  - Converted integer value.

### __le__ method docstring

Method for less than or equal comparison.<hr>

**[Parameters]**

- `other`: str or String
  - String value to compare.

<hr>

**[Returns]**

- `result`: Boolean
  - Comparison result.

### __lt__ method docstring

Method for less than comparison.<hr>

**[Parameters]**

- `other`: str or String
  - String value to compare.

<hr>

**[Returns]**

- `result`: Boolean
  - Comparison result.

### __mul__ method docstring

Method for multiplication (string repetition).<hr>

**[Parameters]**

- `other`: int or Int
  - String repetition number.

<hr>

**[Returns]**

- `result`: String
  - Repeated result string.

### __ne__ method docstring

Method for not equal comparison.<hr>

**[Parameters]**

- `other`: *
  - Any value to compare.

<hr>

**[Returns]**

- `result`: Boolean
  - Comparison result. If not same value of str or String is specified, True will be returned.

### __repr__ method docstring

Get a representation string of this instance.<hr>

**[Returns]**

- `repr_str`: str
  - Representation string of this instance.

### __str__ method docstring

Method for str conversion.<hr>

**[Returns]**

- `result`: str
  - Python builtins str value.

### _append_addition_expression method docstring

Append addition (string concatenation) expression.<hr>

**[Parameters]**

- `result`: String
  - Addition result value.
- `other`: str or String
  - Other string value to concatenate.

### _append_constructor_expression method docstring

Append constructor expression.

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

### _append_ge_expression method docstring

Append __ge__ method expression.<hr>

**[Parameters]**

- `result`: Boolean
  - Result boolean value.
- `other`: VariableNameInterface
  - Other value to compare.

### _append_gt_expression method docstring

Append __gt__ method expression.<hr>

**[Parameters]**

- `result`: Boolean
  - Result boolean value.
- `other`: VariableNameInterface
  - Other value to compare.

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

### _append_multiplication_expression method docstring

Append multiplication (string repetition) expression.<hr>

**[Parameters]**

- `result`: String
  - Multiplication result value.
- `other`: int or Int
  - String repetition number.

### _append_ne_expression method docstring

Append __ne__ method expression.<hr>

**[Parameters]**

- `result`: Boolean
  - Result boolean value.
- `other`: VariableNameInterface
  - Other value to compare.

### _append_value_setter_expression method docstring

Append value's setter expression.<hr>

**[Parameters]**

- `value`: str or String
  - Any string value to set.

### _append_value_updating_cpy_exp_to_handler_scope method docstring

Append a value updating copy expression if the current scope is an event handler's one.<hr>

**[Parameters]**

- `result_variable_name`: str
  - Copied value's variable name.

### _convert_other_val_to_string method docstring

If comparison other value is string, then convert it to String.<hr>

**[Parameters]**

- `other`: *
  - Other comparison value.

<hr>

**[Returns]**

- `converted_val`: *
  - Converted value. If other value is string, then this will be String instance. Other type will be returned directly (not to be converted).

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

### _get_str_value method docstring

Get a (Python's) str value from specified value.<hr>

**[Parameters]**

- `value`: str or String
  - Target string value.

<hr>

**[Returns]**

- `value`: str
  - Python's builtin str value.

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

## TypeVar class docstring

Type variable. Usage:: T = TypeVar('T') # Can be anything A = TypeVar('A', str, bytes) # Must be str or bytes Type variables exist primarily for the benefit of static type checkers. They serve as the parameters for generic types as well as for generic function definitions. See class Generic for more information on generic types. Generic functions work as follows: def repeat(x: T, n: int) -> List[T]: '''Return a list containing n references to x.''' return [x]*n def longest(x: A, y: A) -> A: '''Return the longest of two strings.''' return x if len(x) >= len(y) else y The latter example's signature is essentially the overloading of (str, str) -> str and (bytes, bytes) -> bytes. Also note that if the arguments are instances of some subclass of str, the return type is still plain str. At runtime, isinstance(x, T) and issubclass(C, T) will raise TypeError. Type variables defined with covariant=True or contravariant=True can be used do declare covariant or contravariant generic types. See PEP 484 for more details. By default generic types are invariant in all type variables. Type variables can be introspected. e.g.: T.__name__ == 'T' T.__constraints__ == () T.__covariant__ == False T.__contravariant__ = False A.__constraints__ == (str, bytes)

Type variable. Usage:: T = TypeVar('T') # Can be anything A = TypeVar('A', str, bytes) # Must be str or bytes Type variables exist primarily for the benefit of static type checkers. They serve as the parameters for generic types as well as for generic function definitions. See class Generic for more information on generic types. Generic functions work as follows: def repeat(x: T, n: int) -> List[T]: '''Return a list containing n references to x.''' return [x]*n def longest(x: A, y: A) -> A: '''Return the longest of two strings.''' return x if len(x) >= len(y) else y The latter example's signature is essentially the overloading of (str, str) -> str and (bytes, bytes) -> bytes. Also note that if the arguments are instances of some subclass of str, the return type is still plain str. At runtime, isinstance(x, T) and issubclass(C, T) will raise TypeError. Type variables defined with covariant=True or contravariant=True can be used do declare covariant or contravariant generic types. See PEP 484 for more details. By default generic types are invariant in all type variables. Type variables can be introspected. e.g.: T.__name__ == 'T' T.__constraints__ == () T.__covariant__ == False T.__contravariant__ = False A.__constraints__ == (str, bytes)

### TypingMeta method docstring

Metaclass for most types defined in typing module (not a part of public API). This overrides __new__() to require an extra keyword parameter '_root', which serves as a guard against naive subclassing of the typing classes. Any legitimate class defined using a metaclass derived from TypingMeta must pass _root=True. This also defines a dummy constructor (all the work for most typing constructs is done in __new__) and a nicer repr().

### __new__ method docstring

Constructor. This only exists to give a better error message in case someone tries to subclass a special typing object (not a good idea).