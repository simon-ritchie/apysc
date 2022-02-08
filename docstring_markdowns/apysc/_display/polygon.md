# apysc._display.polygon docstrings

## Module summary

Implementations of Polygon class.

## AppendLinePointInterface class docstring



### ABCMeta method docstring

Metaclass for defining Abstract Base Classes (ABCs). Use this metaclass to create an ABC. An ABC can be subclassed directly, and then acts as a mix-in class. You can also register unrelated concrete classes (even built-in classes) and unrelated ABCs as 'virtual subclasses' -- these and their descendants will be considered subclasses of the registering ABC by the built-in issubclass() function, but the registering ABC won't show up in their MRO (Method Resolution Order) nor will method implementations defined by the registering ABC be callable (not even via super()).

### _append_points_update_expression method docstring

Append points updating expression.<hr>

**[Parameters]**

- `value`: Array
  - Points value to set.

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

### _initialize_points_if_not_initialized method docstring

Initialize _points attribute if it hasn't been initialized yet.

### _initialize_ss_exists_val_if_not_initialized method docstring

Initialize _snapshot_exists_ value it hasn't been initialized yet.

### _make_2dim_points_expression method docstring

Make JavaScript expression string.<hr>

**[Returns]**

- `variable_name`: str
  - Created JavaScript points variable (2-dimensional array) name.
- `expression`: str
  - JavaScript expression string. This expression make 2-dimensional JavaScript array variable, like '[[x_1, y_1], [x_2, y_2], ...]'.

### _make_snapshot method docstring

Make values' snapshots.<hr>

**[Parameters]**

- `snapshot_name`: str
  - Target snapshot name.

### _revert method docstring

Revert values if snapshots exist.<hr>

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

### append_line_point method docstring

Append line point at the end.<hr>

**[Parameters]**

- `x`: int or Int
  - X-coordinate.
- `y`: int or Int
  - Y-coordinate.

<hr>

**[Examples]**

```py
>>> import apysc as ap
>>> stage: ap.Stage = ap.Stage()
>>> sprite: ap.Sprite = ap.Sprite()
>>> sprite.graphics.begin_fill('#0af')
>>> polygon: ap.Polygon = sprite.graphics.draw_polygon(
...     points=[
...         ap.Point2D(x=0, y=0),
...         ap.Point2D(x=0, y=50),
...         ap.Point2D(x=50, y=50),
...     ])
>>> polygon.append_line_point(x=50, y=0)
```

## Array class docstring

Array class for the apysc library.

Array class for the apysc library.<hr>

**[Examples]**

```py
>>> import apysc as ap
>>> arr: ap.Array = ap.Array([1, 2, 3])
>>> arr
Array([1, 2, 3])

>>> arr[0]
1

>>> arr[1]
2

>>> arr = ap.Array((4, 5, 6))
>>> arr
Array([4, 5, 6])

>>> arr = ap.Array(range(3))
>>> arr
Array([0, 1, 2])

>>> arr = ap.Array([1, 2, 3])
>>> arr.append(4)
>>> arr
Array([1, 2, 3, 4])

>>> arr = ap.Array([1, 2, 3])
>>> arr = arr.concat([4, 5, 6])
>>> arr
Array([1, 2, 3, 4, 5, 6])
```

<hr>

**[References]**

- [Array document](https://simon-ritchie.github.io/apysc/array.html)
- [Array class comparison interfaces document](https://simon-ritchie.github.io/apysc/array_comparison.html)

### __bool__ method docstring

Get a boolean value whether this array is empty or not.<hr>

**[Returns]**

- `result`: bool
  - If this array is empty, True will be returned.

### GenericMeta method docstring

Metaclass for generic types. This is a metaclass for typing.Generic and generic ABCs defined in typing module. User defined subclasses of GenericMeta can override __new__ and invoke super().__new__. Note that GenericMeta.__new__ has strict rules on what is allowed in its bases argument: * plain Generic is disallowed in bases; * Generic[...] should appear in bases at most once; * if Generic[...] is present, then it should list all type variables that appear in other bases. In addition, type of all generic bases is erased, e.g., C[int] is stripped to plain C.

### __delitem__ method docstring

Delete specified index value from this array.<hr>

**[Parameters]**

- `index`: Int or int
  - Array's index to delete. Currently not supported tuple value (e.g., slicing).

<hr>

**[Raises]**

- ValueError: If specified index type is not int and Int.

### __eq__ method docstring

Equal comparison method.<hr>

**[Parameters]**

- `other`: *
  - Other value to compare. list or Array types are acceptable.

<hr>

**[Returns]**

- `result`: Boolean
  - Comparison result.

### __getitem__ method docstring

Get a specified index single value.<hr>

**[Parameters]**

- `index`: Int or int
  - Array's index to get value. Currently not supported tuple value (e.g., slicing).

<hr>

**[Returns]**

- `value`: *
  - Specified index's value.

<hr>

**[Raises]**

- ValueError: If specified index type is not int and Int.

### __init__ method docstring

Array class for the apysc library.<hr>

**[Parameters]**

- `value`: list or tuple or range or Array
  - Initial array value.

<hr>

**[Examples]**

```py
>>> import apysc as ap
>>> arr: ap.Array = ap.Array([1, 2, 3])
>>> arr
Array([1, 2, 3])

>>> arr[0]
1

>>> arr[1]
2

>>> arr = ap.Array((4, 5, 6))
>>> arr
Array([4, 5, 6])

>>> arr = ap.Array(range(3))
>>> arr
Array([0, 1, 2])
```

<hr>

**[References]**

- [Array document](https://simon-ritchie.github.io/apysc/array.html)
- [Array class comparison interfaces document](https://simon-ritchie.github.io/apysc/array_comparison.html)

### __len__ method docstring

This method is disabled and can't use from Array instance.

### __ne__ method docstring

Not equal comparison method.<hr>

**[Parameters]**

- `other`: *
  - Other value to compare. list or Array types are acceptable.

<hr>

**[Returns]**

- `result`: Boolean
  - Comparison result.

### object method docstring

The most base type

### __repr__ method docstring

Get a representation string of this instance.<hr>

**[Returns]**

- `repr_str`: str
  - Representation string of this instance.

### __setitem__ method docstring

Set value to a specified index.<hr>

**[Parameters]**

- `index`: Int or int
  - Array's index to set value. Currently not supported tuple value (e.g., slicing).
- `value`: *
  - Any value to set.

<hr>

**[Raises]**

- ValueError: If specified index type is not int and Int.

### __str__ method docstring

String conversion method.<hr>

**[Returns]**

- `string`: str
  - Converted value string.

### _append_concat_expression method docstring

Append concat method expression.<hr>

**[Parameters]**

- `concatenated`: Array
  - Concatenated array value.
- `other_arr`: list or tuple or Array
  - Other array-like value to concatenate.

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

Append an __eq__ expression.<hr>

**[Parameters]**

- `result`: Boolean
  - Result boolean value.
- `other`: Array
  - Array other value to compare.

### _append_extend_expression method docstring

Append extend method expression.<hr>

**[Parameters]**

- `other_arr`: list or tuple or Array
  - Other array-like value to concatenate.

### _append_getitem_expression method docstring

Append __getitem__ expression.<hr>

**[Parameters]**

- `index`: Int or int
  - Array's index to get value.
- `value`: *
  - Specified index's value.

### _append_index_of_expression method docstring

Append index_of method expression.<hr>

**[Parameters]**

- `index`: Int
  - Found position of index. If value is not contains, -1 will be set.
- `value`: *
  - Any value to search.

### _append_insert_expression method docstring

Append insert method expression.<hr>

**[Parameters]**

- `index`: Int or int
  - Index to append value to.
- `value`: *
  - Any value to append.

### _append_join_expression method docstring

Append join method expression.<hr>

**[Parameters]**

- `joined`: String
  - Joined string.
- `sep`: String or str
  - Separator string.

### _append_length_expression method docstring

Append length method expression.<hr>

**[Parameters]**

- `length`: Int
  - Created length Int variable.

### _append_ne_expression method docstring

Append a __ne__ expression.<hr>

**[Parameters]**

- `result`: Boolean
  - Result boolean value.
- `other`: Array
  - Array other value to compare.

### _append_pop_expression method docstring

Append pop method expression.<hr>

**[Parameters]**

- `value`: *
  - Removed value.

### _append_push_and_append_expression method docstring

Append push and append method expression.<hr>

**[Parameters]**

- `value`: *
  - Any value to append.

### _append_remove_at_expression method docstring

Append remove_at method expression.<hr>

**[Parameters]**

- `index`: Int or int
  - Index to remove value.

### _append_remove_expression method docstring

Append remove method expression.<hr>

**[Parameters]**

- `value`: Any
  - Value to remove.

### _append_reverse_expression method docstring

Append reverse method expression.

### _append_setitem_expression method docstring

Append __setitem__ method expression.<hr>

**[Parameters]**

- `index`: Int or int
  - Array's index to set value. Currently not supported tuple value (e.g., slicing).
- `value`: *
  - Any value to set.

### _append_slice_expression method docstring

Append slice method expression.<hr>

**[Parameters]**

- `sliced_arr`: Array
  - Sliced array.
- `start`: Int or int or None
  - Slicing start index.
- `end`: Int or int or None
  - Slicing end index.

### _append_sort_expression method docstring

Append sort method expression.

### _append_value_setter_expression method docstring

Append value's setter expression.<hr>

**[Parameters]**

- `value`: list or tuple or Array
  - Iterable value (list, tuple, or Array) to set.

### _append_value_updating_cpy_exp_to_handler_scope method docstring

Append a value updating copy expression if the current scope is an event handler's one.<hr>

**[Parameters]**

- `result_variable_name`: str
  - Copied value's variable name.

### _convert_other_val_to_array method docstring

If comparison's other value is list value, then convert it to Array instance.<hr>

**[Parameters]**

- `other`: *
  - Other value to compare.

<hr>

**[Returns]**

- `converted_val`: *
  - Converted value. If other value is list, then this will be Array type. Otherwise this will be returned directly (not to be converted).

### _convert_range_to_list method docstring

Convert argument value to list that if specified value is range type.<hr>

**[Parameters]**

- `value`: list or tuple or range or Array
  - Target value.

<hr>

**[Returns]**

- `value`: list or tuple or Array
  - Converted value.

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

### _get_builtin_int_from_index method docstring

Get Python builtin integer from index value.<hr>

**[Parameters]**

- `index`: Int or int
  - Specified array's index.

<hr>

**[Returns]**

- `builtin_int_index`: int
  - Python builtin integer index value.

### _get_custom_event_type_str method docstring

Get a custom event type string from a type value.<hr>

**[Parameters]**

- `custom_event_type`: CustomEventType or str
  - Target custom event type or string.

<hr>

**[Returns]**

- `custom_event_type_str`: str
  - A custom event type string.

### _get_list_value method docstring

Get a list value from specified list, tuple, or Array value.<hr>

**[Parameters]**

- `value`: list or tuple or Array
  - Specified list, tuple, or Array value.

<hr>

**[Returns]**

- `list_val`: list
  - Converted list value.

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

### Array method docstring

Array class for the apysc library.<hr>

**[Examples]**

```py
>>> import apysc as ap
>>> arr: ap.Array = ap.Array([1, 2, 3])
>>> arr
Array([1, 2, 3])

>>> arr[0]
1

>>> arr[1]
2

>>> arr = ap.Array((4, 5, 6))
>>> arr
Array([4, 5, 6])

>>> arr = ap.Array(range(3))
>>> arr
Array([0, 1, 2])

>>> arr = ap.Array([1, 2, 3])
>>> arr.append(4)
>>> arr
Array([1, 2, 3, 4])

>>> arr = ap.Array([1, 2, 3])
>>> arr = arr.concat([4, 5, 6])
>>> arr
Array([1, 2, 3, 4, 5, 6])
```

<hr>

**[References]**

- [Array document](https://simon-ritchie.github.io/apysc/array.html)
- [Array class comparison interfaces document](https://simon-ritchie.github.io/apysc/array_comparison.html)

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

### _validate_acceptable_value_type method docstring

Validate that specified value is acceptable type or not.<hr>

**[Parameters]**

- `value`: list or tuple or range or Array
  - Iterable value to check.

<hr>

**[Raises]**

- ValueError: If specified value's type is not list, tuple, or Array.

### _validate_index_type_is_int method docstring

Validate whether index value type is int (or Int) or not.<hr>

**[Parameters]**

- `index`: Int or int
  - Index value to check.

<hr>

**[Raises]**

- ValueError: If index type is not int or Int type.

### append method docstring

Add any value to the end of this array. This method behaves the same `push` method.<hr>

**[Parameters]**

- `value`: *
  - Any value to append.

<hr>

**[Examples]**

```py
>>> import apysc as ap
>>> arr: ap.Array = ap.Array([1, 2, 3])
>>> arr.append(4)
>>> arr
Array([1, 2, 3, 4])
```

<hr>

**[References]**

- [Array class append and push interfaces document](https://simon-ritchie.github.io/apysc/array_append_and_push.html)

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

### concat method docstring

Concatenate argument array to this one. This interface positions the argument array's values after this array values. This method is similar to extend method, but there is a difference in whether updating the same variable (extend) or returned as a different variable (concat).<hr>

**[Parameters]**

- `other_arr`: list or tuple or Array
  - Other array-like values to concatenate.

<hr>

**[Returns]**

- `concatenated`: Array
  - Concatenated array value.

<hr>

**[Examples]**

```py
>>> import apysc as ap
>>> arr: ap.Array = ap.Array([1, 2, 3])
>>> arr = arr.concat([4, 5, 6])
>>> arr
Array([1, 2, 3, 4, 5, 6])
```

<hr>

**[References]**

- [Array class extend and concat interfaces document](https://simon-ritchie.github.io/apysc/array_extend_and_concat.html)

### extend method docstring

Concatenate argument array to this one. This interface positions the argument array's values after this array values. This method is similar to the concat method. Still, there is a difference in whether updating the same variable (extend) or returned as a different variable (concat).<hr>

**[Parameters]**

- `other_arr`: list or tuple or Array
  - Other array-like values to concatenate.

<hr>

**[Examples]**

```py
>>> import apysc as ap
>>> arr: ap.Array = ap.Array([1, 2, 3])
>>> arr.extend([4, 5, 6])
>>> arr
Array([1, 2, 3, 4, 5, 6])
```

<hr>

**[References]**

- [Array class extend and concat interfaces document](https://simon-ritchie.github.io/apysc/array_extend_and_concat.html)

### index_of method docstring

Search specified value's index and return it.<hr>

**[Parameters]**

- `value`: *
  - Any value to search.

<hr>

**[Returns]**

- `index`: Int
  - Found position of index. If this array does not contain a value, this interface returns -1.

<hr>

**[Examples]**

```py
>>> import apysc as ap
>>> arr: ap.Array = ap.Array([1, 3, 5])
>>> arr.index_of(3)
Int(1)
```

<hr>

**[References]**

- [Array class index_of interface document](https://simon-ritchie.github.io/apysc/array_index_of.html)

### insert method docstring

Insert value to this array at a specified index. This interface behaves the same `insert_at` method.<hr>

**[Parameters]**

- `index`: Int or int
  - Index to append value.
- `value`: *
  - Any value to append.

<hr>

**[Examples]**

```py
>>> import apysc as ap
>>> arr: ap.Array = ap.Array([1, 3])
>>> arr.insert(index=1, value=2)
>>> arr
Array([1, 2, 3])
```

<hr>

**[References]**

- [Array class insert and insert_at interfaces document](https://simon-ritchie.github.io/apysc/array_insert_and_insert_at.html)

### insert_at method docstring

Insert value to this array at a specified index. This interface behaves the same `insert` method.<hr>

**[Parameters]**

- `index`: Int or int
  - Index to append value.
- `value`: *
  - Any value to append.

<hr>

**[Examples]**

```py
>>> import apysc as ap
>>> arr: ap.Array = ap.Array([1, 3])
>>> arr.insert_at(index=1, value=2)
>>> arr
Array([1, 2, 3])
```

<hr>

**[References]**

- [Array class insert and insert_at interfaces document](https://simon-ritchie.github.io/apysc/array_insert_and_insert_at.html)

### join method docstring

Join this array value with a specified separator string.<hr>

**[Parameters]**

- `sep`: String or str
  - Separator string.

<hr>

**[Returns]**

- `joined`: String
  - Joined string.

<hr>

**[Examples]**

```py
>>> import apysc as ap
>>> arr: ap.Array = ap.Array([1, 2, 3])
>>> arr.join(sep=', ')
String('1, 2, 3')
```

<hr>

**[References]**

- [Array class join interface document](https://simon-ritchie.github.io/apysc/array_join.html)

### pop method docstring

Remove this array's last value and return it.<hr>

**[Returns]**

- `value`: *
  - Removed value.

<hr>

**[Examples]**

```py
>>> import apysc as ap
>>> arr: ap.Array = ap.Array([1, 2, 3])
>>> popped_val: int = arr.pop()
>>> popped_val
3

>>> arr
Array([1, 2])
```

<hr>

**[References]**

- [Array class pop interface document](https://simon-ritchie.github.io/apysc/array_pop.html)

### push method docstring

Add any value to the end of this array. This behaves same as append method.<hr>

**[Parameters]**

- `value`: *
  - Any value to append.

<hr>

**[Examples]**

```py
>>> import apysc as ap
>>> arr: ap.Array = ap.Array([1, 2, 3])
>>> arr.push(4)
>>> arr
Array([1, 2, 3, 4])
```

<hr>

**[References]**

- [Array class append and push interfaces document](https://simon-ritchie.github.io/apysc/array_append_and_push.html)

### remove method docstring

Remove specified value from this array.<hr>

**[Parameters]**

- `value`: Any
  - Value to remove.

<hr>

**[Examples]**

```py
>>> import apysc as ap
>>> arr: ap.Array = ap.Array([1, 3, 5])
>>> arr.remove(3)
>>> arr
Array([1, 5])
```

<hr>

**[References]**

- [Array class remove and remove_at interfaces document](https://simon-ritchie.github.io/apysc/array_remove_and_remove_at.html)

### remove_at method docstring

Remove specified index value from this array.<hr>

**[Parameters]**

- `index`: Int or int
  - Index to remove value.

<hr>

**[Examples]**

```py
>>> import apysc as ap
>>> arr: ap.Array = ap.Array([1, 2, 3])
>>> arr.remove_at(1)
>>> arr
Array([1, 3])
```

<hr>

**[References]**

- [Array class remove and remove_at interfaces document](https://simon-ritchie.github.io/apysc/array_remove_and_remove_at.html)

### reverse method docstring

Reverse this array in place.<hr>

**[Examples]**

```py
>>> import apysc as ap
>>> arr: ap.Array = ap.Array([1, 2, 3])
>>> arr.reverse()
>>> arr
Array([3, 2, 1])
```

<hr>

**[References]**

- [Array class reverse interface document](https://simon-ritchie.github.io/apysc/array_reverse.html)

### slice method docstring

Slice this array by specified start and end indexes.<hr>

**[Parameters]**

- `start`: Int or int or None, default None
  - Slicing start index.
- `end`: Int or int or None, default None
  - Slicing end index (a result array does not contain this index).

<hr>

**[Returns]**

- `sliced_arr`: Array
  - Sliced array.

<hr>

**[Examples]**

```py
>>> import apysc as ap
>>> arr: ap.Array = ap.Array([1, 2, 3, 4])
>>> arr.slice(start=1, end=3)
Array([2, 3])

>>> arr.slice(start=1)
Array([2, 3, 4])

>>> arr.slice(end=2)
Array([1, 2])
```

<hr>

**[References]**

- [Array class slice interface document](https://simon-ritchie.github.io/apysc/array_slice.html)

### sort method docstring

Sort this array in place.<hr>

**[Parameters]**

- `ascending`: bool, default True
  - Sort by ascending or not. If False is specified, this interface sorts values descending.

<hr>

**[Examples]**

```py
>>> import apysc as ap
>>> arr: ap.Array = ap.Array([3, 5, 1, 4, 2])
>>> arr.sort()
>>> arr
Array([1, 2, 3, 4, 5])

>>> arr.sort(ascending=False)
>>> arr
Array([5, 4, 3, 2, 1])
```

<hr>

**[References]**

- [Array class sort interface document](https://simon-ritchie.github.io/apysc/array_sort.html)

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

## LineBase class docstring



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

### __repr__ method docstring

Get a string representation of this instance (for the sake of debugging).

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

### _append_basic_vals_expression method docstring

Append basic values expression to specified one.<hr>

**[Parameters]**

- `expression`: str
  - Target expression.
- `indent_num`: int
  - Indentation number.

<hr>

**[Returns]**

- `expression`: str
  - After appending expression.

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

### _append_fill_alpha_attr_linking_setting method docstring

Append a scale-y attribute linking setting.

### _append_fill_alpha_update_expression method docstring

Append fill alpha updating expression.

### _append_fill_color_update_expression method docstring

Append fill color updating expression.

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

### _append_line_alpha_attr_linking_setting method docstring

Append a line alpha attribute linking setting.

### _append_line_alpha_update_expression method docstring

Append line alpha updating expression.

### _append_line_cap_update_expression method docstring

Append line cap updating expression.

### _append_line_color_update_expression method docstring

Append line color updating expression.

### _append_line_dash_dot_setting_update_expression method docstring

Append line dash dot setting updating expression.

### _append_line_dash_setting_update_expression method docstring

Append line dash setting updating expression.

### _append_line_dot_setting_update_expression method docstring

Append line dot setting updating expression.

### _append_line_joints_update_expression method docstring

Append line cap updating expression.

### _append_line_round_dot_setting_update_expression method docstring

Append line round dot setting updating expression.

### _append_line_thickness_attr_linking_setting method docstring

Append a line thickness attribute linking setting.

### _append_line_thickness_update_expression method docstring

Append line thickness update expression.

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

### _initialize_fill_alpha_if_not_initialized method docstring

Initialize _fill_alpha attribute if it hasn't been initialized yet.

### _initialize_fill_color_if_not_initialized method docstring

Initialize fill_color attribute if that value is not instantiated yet.

### _initialize_flip_x_if_not_initialized method docstring

Initialize the _flip_x attribute if it hasn't been initialized yet.

### _initialize_flip_y_if_not_initialized method docstring

Initialize the _flip_y attribute if it hasn't been initialized yet.

### _initialize_line_alpha_if_not_initialized method docstring

Initialize _line_alpha attribute if it hasn't been initialized yet.

### _initialize_line_cap_if_not_initialized method docstring

Inilialize _line_cap attribute if it is not initialized yet.

### _initialize_line_color_if_not_initialized method docstring

Initialize line_color attribute if that value is not initialized yet.

### _initialize_line_dash_dot_setting_if_not_initialized method docstring

Initialize _line_dash_dot_setting attribute if it is not initialized yet.

### _initialize_line_dash_setting_if_not_initialized method docstring

Initialize _line_dash_setting attribute if it is not initialized yet.

### _initialize_line_dot_setting_if_not_initialized method docstring

Initialize _line_dot_setting attribute if it is not initialized yet.

### _initialize_line_joints_if_not_initialized method docstring

Initialize _line_joints attribute if that it is not initialized yet.

### _initialize_line_round_dot_setting_if_not_initialized method docstring

Initialize _line_round_dot_setting if it is not initialized yet.

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

### _set_initial_basic_values method docstring

Set initial basic values (fill color, line thickness, and so on).<hr>

**[Parameters]**

- `parent`: Graphics
  - Graphics instance to link this graphic.

### _set_initial_fill_color_if_not_blank method docstring

Set initial fill color value if specified value is not blank string.<hr>

**[Parameters]**

- `fill_color`: str or String
  - Fill color (hexadecimal string, e.g., '#00aaff').

### _set_initial_line_color_if_not_blank method docstring

Set initial line color value if specified value is not blank string.<hr>

**[Parameters]**

- `line_color`: str or String
  - Line color (hexadecimal string, e.g., '#00aaff').

### _set_line_setting_if_not_none_value_exists method docstring

If a line setting (dot, dash, or something else) with a value other than None exists, set that value to the attribute.<hr>

**[Parameters]**

- `parent_graphics`: Graphics
  - Parent Graphics instance.

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

### _update_fill_alpha_and_skip_appending_exp method docstring

Update fill opacity and skip appending expression.<hr>

**[Parameters]**

- `value`: Number
  - Fill opacity to set.

### _update_fill_color_and_skip_appending_exp method docstring

Update fill color and skip appending expression.<hr>

**[Parameters]**

- `value`: String
  - Fill color to set.

### _update_line_alpha_and_skip_appending_exp method docstring

Update line alpha and skip appending expression.<hr>

**[Parameters]**

- `value`: float or Number
  - Line alpha (opacity) to set.

### _update_line_cap_and_skip_appending_exp method docstring

Update line cap and skip appending expression.<hr>

**[Parameters]**

- `value`: String or LineCaps
  - Line cap style setting to set.

### _update_line_color_and_skip_appending_exp method docstring

Update line color and skip appending expression.<hr>

**[Parameters]**

- `value`: String
  - Line color to set.

### _update_line_dash_dot_setting_and_skip_appending_exp method docstring

Update line dash dot (1-dot chain) setting and skip appending expression.<hr>

**[Parameters]**

- `value`: LineDashDotSetting or None
  - Line dash dot (1-dot chain) setting to set.

### _update_line_dash_setting_and_skip_appending_exp method docstring

Update line dash setting and skip appending expression.<hr>

**[Parameters]**

- `value`: LineDashSetting or None
  - Line dash setting to set.

### _update_line_dot_setting_and_skip_appending_exp method docstring

Update line dot setting and skip appending expression.<hr>

**[Parameters]**

- `value`: LineDotSetting or None
  - Line dot setting to set.

### _update_line_joints_and_skip_appending_exp method docstring

Update line joints and skip appending expression.<hr>

**[Parameters]**

- `value`: STring or LineJoints
  - Line joints style setting to set.

### _update_line_round_dot_setting_and_skip_appending_exp method docstring

Update line round setting and skip appending expression.<hr>

**[Parameters]**

- `value`: LineRoundSetting or None
  - Line round dot setting to set.

### _update_line_thickness_and_skip_appending_exp method docstring

Update line thickness and skip appending expression.<hr>

**[Parameters]**

- `value`: int or Int
  - Line thickness to set.

### animation_fill_alpha method docstring

Set the fill alpha (opacity) animation setting.<hr>

**[Parameters]**

- `alpha`: Number or float
  - The final alpha (opacity) of the animation.
- `duration`: Int or int, default 3000
  - Milliseconds before an animation ends.
- `delay`: Int or int, default 0
  - Milliseconds before an animation starts.
- `easing`: Easing, default Easing.LINEAR
  - Easing setting.

<hr>

**[Returns]**

- `animation_fill_alpha`: AnimationFillAlpha
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
>>> circle: ap.Circle = sprite.graphics.draw_circle(
...     x=100, y=100, radius=50)
>>> _ = circle.animation_y(
...     y=100,
...     duration=1500,
...     easing=ap.Easing.EASE_OUT_QUINT,
... ).start()
```

<hr>

**[References]**

- [animation_fill_alpha interface document](https://simon-ritchie.github.io/apysc/animation_fill_alpha.html)
- [Animation interfaces duration setting document](https://simon-ritchie.github.io/apysc/animation_duration.html)
- [Each animation interface return value document](https://simon-ritchie.github.io/apysc/animation_return_value.html)
- [Sequential animation setting document](https://simon-ritchie.github.io/apysc/sequential_animation.html)
- [animation_parallel interface document](https://simon-ritchie.github.io/apysc/animation_parallel.html)
- [Easing enum document](https://simon-ritchie.github.io/apysc/easing_enum.html)

### animation_fill_color method docstring

Set the fill color animation setting.<hr>

**[Parameters]**

- `fill_color`: str or String
  - The final fill color (hex color code) of the animation.
- `duration`: Int or int, default 3000
  - Milliseconds before an animation ends.
- `delay`: Int or int, default 0
  - Milliseconds before an animation starts.
- `easing`: Easing, default Easing.LINEAR
  - Easing setting.

<hr>

**[Returns]**

- `animation_fill_color`: AnimationFillColor
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
>>> _ = rectangle.animation_fill_color(
...     fill_color='#f0a',
...     duration=1500,
...     easing=ap.Easing.EASE_OUT_QUINT,
... ).start()
```

<hr>

**[References]**

- [animation_fill_color interface document](https://simon-ritchie.github.io/apysc/animation_fill_color.html)
- [Animation interfaces duration setting document](https://simon-ritchie.github.io/apysc/animation_duration.html)
- [Animation interfaces delay setting document](https://simon-ritchie.github.io/apysc/animation_delay.html)
- [Each animation interface return value document](https://simon-ritchie.github.io/apysc/animation_return_value.html)
- [Sequential animation setting document](https://simon-ritchie.github.io/apysc/sequential_animation.html)
- [animation_parallel interface document](https://simon-ritchie.github.io/apysc/animation_parallel.html)
- [Easing enum document](https://simon-ritchie.github.io/apysc/easing_enum.html)

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

### animation_line_alpha method docstring

Set the line alpha animation setting.<hr>

**[Parameters]**

- `alpha`: Number or float
  - The final line alpha of the animation.
- `duration`: Int or int, default 3000
  - Milliseconds before an animation ends.
- `delay`: Int or int, default 0
  - Milliseconds before an animation starts.
- `easing`: Easing, default Easing.LINEAR
  - Easing setting.

<hr>

**[Returns]**

- `animation_line_alpha`: AnimationLineAlpha
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
...     color='#fff', thickness=5, alpha=1.0)
>>> rectangle: ap.Rectangle = sprite.graphics.draw_rect(
...     x=50, y=50, width=50, height=50)
>>> _ = rectangle.animation_line_alpha(
...     alpha=0.0,
...     duration=1500,
...     easing=ap.Easing.EASE_OUT_QUINT,
... ).start()
```

<hr>

**[References]**

- [animation_line_alpha interface document](https://simon-ritchie.github.io/apysc/animation_line_alpha.html)
- [Animation interfaces duration setting document](https://simon-ritchie.github.io/apysc/animation_duration.html)
- [Animation interfaces delay setting document](https://simon-ritchie.github.io/apysc/animation_delay.html)
- [Each animation interface return value document](https://simon-ritchie.github.io/apysc/animation_return_value.html)
- [Sequential animation setting document](https://simon-ritchie.github.io/apysc/sequential_animation.html)
- [animation_parallel interface document](https://simon-ritchie.github.io/apysc/animation_parallel.html)
- [Easing enum document](https://simon-ritchie.github.io/apysc/easing_enum.html)

### animation_line_color method docstring

Set the line color animation setting.<hr>

**[Parameters]**

- `line_color`: str or String
  - The final line color (hex color code) of the animation.
- `duration`: Int or int, default 3000
  - Milliseconds before an animation ends.
- `delay`: Int or int, default 0
  - Milliseconds before an animation starts.
- `easing`: Easing, default Easing.LINEAR
  - Easing setting.

<hr>

**[Returns]**

- `animation_line_color`: AnimationLineColor
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
...     color='#fff', thickness=5)
>>> rectangle: ap.Rectangle = sprite.graphics.draw_rect(
...     x=50, y=50, width=50, height=50)
>>> _ = rectangle.animation_line_color(
...     line_color='#0af',
...     duration=1500,
...     easing=ap.Easing.EASE_OUT_QUINT,
... ).start()
```

<hr>

**[References]**

- [animation_line_color interface document](https://simon-ritchie.github.io/apysc/animation_line_color.html)
- [Animation interfaces duration setting document](https://simon-ritchie.github.io/apysc/animation_duration.html)
- [Animation interfaces delay setting document](https://simon-ritchie.github.io/apysc/animation_delay.html)
- [Each animation interface return value document](https://simon-ritchie.github.io/apysc/animation_return_value.html)
- [Sequential animation setting document](https://simon-ritchie.github.io/apysc/sequential_animation.html)
- [animation_parallel interface document](https://simon-ritchie.github.io/apysc/animation_parallel.html)
- [Easing enum document](https://simon-ritchie.github.io/apysc/easing_enum.html)

### animation_line_thickness method docstring

Set the line thickness animation setting.<hr>

**[Parameters]**

- `thickness`: Int or int
  - The final line thickness of the animation.
- `duration`: Int or int, default 3000
  - Milliseconds before an animation ends.
- `delay`: Int or int, default 0
  - Milliseconds before an animation starts.
- `easing`: Easing, default Easing.LINEAR
  - Easing setting.

<hr>

**[Returns]**

- `animation_line_thickness`: AnimationLineThickness
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
>>> _ = rectangle.animation_line_thickness(
...     thickness=6,
...     duration=1500,
...     easing=ap.Easing.EASE_OUT_QUINT,
... ).start()
```

<hr>

**[References]**

- [animation_line_thickness interface document](https://simon-ritchie.github.io/apysc/animation_line_thickness.html)
- [Animation interfaces duration setting document](https://simon-ritchie.github.io/apysc/animation_duration.html)
- [Animation interfaces delay setting document](https://simon-ritchie.github.io/apysc/animation_delay.html)
- [Each animation interface return value document](https://simon-ritchie.github.io/apysc/animation_return_value.html)
- [Sequential animation setting document](https://simon-ritchie.github.io/apysc/sequential_animation.html)
- [animation_parallel interface document](https://simon-ritchie.github.io/apysc/animation_parallel.html)
- [Easing enum document](https://simon-ritchie.github.io/apysc/easing_enum.html)

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

## Point2D class docstring

2-dimensional geometry point class.

2-dimensional geometry point class.<hr>

**[Examples]**

```py
>>> import apysc as ap
>>> stage: ap.Stage = ap.Stage()
>>> sprite: ap.Sprite = ap.Sprite()
>>> sprite.graphics.begin_fill(color='#0af')
>>> point_1: ap.Point2D = ap.Point2D(x=0, y=0)
>>> polygon: ap.Polygon = sprite.graphics.draw_polygon(
...     points=[
...         point_1,
...         ap.Point2D(x=0, y=50),
...         ap.Point2D(x=50, y=25),
...     ])
>>> point_1.x
Int(0)

>>> point_1.y
Int(0)
```

### ABCMeta method docstring

Metaclass for defining Abstract Base Classes (ABCs). Use this metaclass to create an ABC. An ABC can be subclassed directly, and then acts as a mix-in class. You can also register unrelated concrete classes (even built-in classes) and unrelated ABCs as 'virtual subclasses' -- these and their descendants will be considered subclasses of the registering ABC by the built-in issubclass() function, but the registering ABC won't show up in their MRO (Method Resolution Order) nor will method implementations defined by the registering ABC be callable (not even via super()).

### __eq__ method docstring

Equal comparison method.<hr>

**[Parameters]**

- `other`: Any
  - Other value to compare.

<hr>

**[Returns]**

- `result`: Boolean
  - Comparison result.

### __init__ method docstring

2-dimensional geometry point.<hr>

**[Parameters]**

- `x`: int or Int
  - X-coordinate.
- `y`: int or Int
  - Y-coordinate.

<hr>

**[Examples]**

```py
>>> import apysc as ap
>>> stage: ap.Stage = ap.Stage()
>>> sprite: ap.Sprite = ap.Sprite()
>>> sprite.graphics.begin_fill(color='#0af')
>>> polygon: ap.Polygon = sprite.graphics.draw_polygon(
...     points=[
...         ap.Point2D(x=0, y=0),
...         ap.Point2D(x=0, y=50),
...         ap.Point2D(x=50, y=25),
...     ])
```

### __ne__ method docstring

Not equal comparison method.<hr>

**[Parameters]**

- `other`: Any
  - Other value to compare.

<hr>

**[Returns]**

- `result`: Boolean
  - Comparison result.

### __repr__ method docstring

Get a string representation of this instance (for the sake of debugging).<hr>

**[Returns]**

- `repr_str`: str
  - Type name and coordinates values are set (e.g., `Point2D(Int(50), Int(100))`).

### _append_constructor_expression method docstring

Append constructor expression.

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

### _append_x_getter_expression method docstring

Append x property getter expression.<hr>

**[Parameters]**

- `x`: Int
  - Target x value.

### _append_x_setter_expression method docstring

Append x property setter expression.<hr>

**[Parameters]**

- `value`: Int
  - X-coordinate to set.

### _append_y_getter_expression method docstring

Append y property getter expression.<hr>

**[Parameters]**

- `y`: Int
  - Target y value.

### _append_y_setter_expression method docstring

Append y property setter expression.<hr>

**[Parameters]**

- `value`: Int
  - Y-coordinate to set.

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

Make values' snapshots.<hr>

**[Parameters]**

- `snapshot_name`: str
  - Target snapshot name.

### _revert method docstring

Revert values if snapshots exist.<hr>

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

## Polygon class docstring

The polygon vector graphics class.

The polygon vector graphics class.<hr>

**[Examples]**

```py
>>> import apysc as ap
>>> stage: ap.Stage = ap.Stage()
>>> sprite: ap.Sprite = ap.Sprite()
>>> sprite.graphics.begin_fill(color='#0af')
>>> polygon: ap.Polygon = sprite.graphics.draw_polygon(
...     points=[
...         ap.Point2D(x=50, y=50),
...         ap.Point2D(x=50, y=100),
...         ap.Point2D(x=100, y=75),
...     ])
>>> polygon.fill_color
String('#00aaff')
```

<hr>

**[References]**

- [Graphics draw_polygon interface document](https://simon-ritchie.github.io/apysc/graphics_draw_polygon.html)

### ABCMeta method docstring

Metaclass for defining Abstract Base Classes (ABCs). Use this metaclass to create an ABC. An ABC can be subclassed directly, and then acts as a mix-in class. You can also register unrelated concrete classes (even built-in classes) and unrelated ABCs as 'virtual subclasses' -- these and their descendants will be considered subclasses of the registering ABC by the built-in issubclass() function, but the registering ABC won't show up in their MRO (Method Resolution Order) nor will method implementations defined by the registering ABC be callable (not even via super()).

### __init__ method docstring

Create a polygon vector graphic. This is similar to Polyline class, but unlike that, end point and start point will be connected.<hr>

**[Parameters]**

- `parent`: Graphics
  - Graphics instance to link this graphic.
- `points`: Array of Point2D
  - List of polygon vertex points.

<hr>

**[Examples]**

```py
>>> import apysc as ap
>>> stage: ap.Stage = ap.Stage()
>>> sprite: ap.Sprite = ap.Sprite()
>>> sprite.graphics.begin_fill(color='#0af')
>>> polygon: ap.Polygon = sprite.graphics.draw_polygon(
...     points=[
...         ap.Point2D(x=50, y=50),
...         ap.Point2D(x=50, y=100),
...         ap.Point2D(x=100, y=75),
...     ])
>>> polygon.fill_color
String('#00aaff')
```

<hr>

**[References]**

- [Graphics draw_polygon interface document](https://simon-ritchie.github.io/apysc/graphics_draw_polygon.html)

### __repr__ method docstring

Get a string representation of this instance (for the sake of debugging).<hr>

**[Returns]**

- `repr_str`: str
  - Type name and variable name will be set (e.g., `Polygon('<variable_name>')`).

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

### _append_basic_vals_expression method docstring

Append basic values expression to specified one.<hr>

**[Parameters]**

- `expression`: str
  - Target expression.
- `indent_num`: int
  - Indentation number.

<hr>

**[Returns]**

- `expression`: str
  - After appending expression.

### _append_constructor_expression method docstring

Append constructor expression.

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

### _append_fill_alpha_attr_linking_setting method docstring

Append a scale-y attribute linking setting.

### _append_fill_alpha_update_expression method docstring

Append fill alpha updating expression.

### _append_fill_color_update_expression method docstring

Append fill color updating expression.

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

### _append_line_alpha_attr_linking_setting method docstring

Append a line alpha attribute linking setting.

### _append_line_alpha_update_expression method docstring

Append line alpha updating expression.

### _append_line_cap_update_expression method docstring

Append line cap updating expression.

### _append_line_color_update_expression method docstring

Append line color updating expression.

### _append_line_dash_dot_setting_update_expression method docstring

Append line dash dot setting updating expression.

### _append_line_dash_setting_update_expression method docstring

Append line dash setting updating expression.

### _append_line_dot_setting_update_expression method docstring

Append line dot setting updating expression.

### _append_line_joints_update_expression method docstring

Append line cap updating expression.

### _append_line_round_dot_setting_update_expression method docstring

Append line round dot setting updating expression.

### _append_line_thickness_attr_linking_setting method docstring

Append a line thickness attribute linking setting.

### _append_line_thickness_update_expression method docstring

Append line thickness update expression.

### _append_mouse_event_binding_expression method docstring

Append a mouse event binding expression.<hr>

**[Parameters]**

- `name`: str
  - Handler's name.
- `mouse_event_type`: MouseEventType
  - Event type to bind.

### _append_points_update_expression method docstring

Append points updating expression.<hr>

**[Parameters]**

- `value`: Array
  - Points value to set.

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

### _initialize_fill_alpha_if_not_initialized method docstring

Initialize _fill_alpha attribute if it hasn't been initialized yet.

### _initialize_fill_color_if_not_initialized method docstring

Initialize fill_color attribute if that value is not instantiated yet.

### _initialize_flip_x_if_not_initialized method docstring

Initialize the _flip_x attribute if it hasn't been initialized yet.

### _initialize_flip_y_if_not_initialized method docstring

Initialize the _flip_y attribute if it hasn't been initialized yet.

### _initialize_line_alpha_if_not_initialized method docstring

Initialize _line_alpha attribute if it hasn't been initialized yet.

### _initialize_line_cap_if_not_initialized method docstring

Inilialize _line_cap attribute if it is not initialized yet.

### _initialize_line_color_if_not_initialized method docstring

Initialize line_color attribute if that value is not initialized yet.

### _initialize_line_dash_dot_setting_if_not_initialized method docstring

Initialize _line_dash_dot_setting attribute if it is not initialized yet.

### _initialize_line_dash_setting_if_not_initialized method docstring

Initialize _line_dash_setting attribute if it is not initialized yet.

### _initialize_line_dot_setting_if_not_initialized method docstring

Initialize _line_dot_setting attribute if it is not initialized yet.

### _initialize_line_joints_if_not_initialized method docstring

Initialize _line_joints attribute if that it is not initialized yet.

### _initialize_line_round_dot_setting_if_not_initialized method docstring

Initialize _line_round_dot_setting if it is not initialized yet.

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

### _initialize_points_if_not_initialized method docstring

Initialize _points attribute if it hasn't been initialized yet.

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

### _make_2dim_points_expression method docstring

Make JavaScript expression string.<hr>

**[Returns]**

- `variable_name`: str
  - Created JavaScript points variable (2-dimensional array) name.
- `expression`: str
  - JavaScript expression string. This expression make 2-dimensional JavaScript array variable, like '[[x_1, y_1], [x_2, y_2], ...]'.

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

### _set_initial_basic_values method docstring

Set initial basic values (fill color, line thickness, and so on).<hr>

**[Parameters]**

- `parent`: Graphics
  - Graphics instance to link this graphic.

### _set_initial_fill_color_if_not_blank method docstring

Set initial fill color value if specified value is not blank string.<hr>

**[Parameters]**

- `fill_color`: str or String
  - Fill color (hexadecimal string, e.g., '#00aaff').

### _set_initial_line_color_if_not_blank method docstring

Set initial line color value if specified value is not blank string.<hr>

**[Parameters]**

- `line_color`: str or String
  - Line color (hexadecimal string, e.g., '#00aaff').

### _set_line_setting_if_not_none_value_exists method docstring

If a line setting (dot, dash, or something else) with a value other than None exists, set that value to the attribute.<hr>

**[Parameters]**

- `parent_graphics`: Graphics
  - Parent Graphics instance.

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

### _update_fill_alpha_and_skip_appending_exp method docstring

Update fill opacity and skip appending expression.<hr>

**[Parameters]**

- `value`: Number
  - Fill opacity to set.

### _update_fill_color_and_skip_appending_exp method docstring

Update fill color and skip appending expression.<hr>

**[Parameters]**

- `value`: String
  - Fill color to set.

### _update_line_alpha_and_skip_appending_exp method docstring

Update line alpha and skip appending expression.<hr>

**[Parameters]**

- `value`: float or Number
  - Line alpha (opacity) to set.

### _update_line_cap_and_skip_appending_exp method docstring

Update line cap and skip appending expression.<hr>

**[Parameters]**

- `value`: String or LineCaps
  - Line cap style setting to set.

### _update_line_color_and_skip_appending_exp method docstring

Update line color and skip appending expression.<hr>

**[Parameters]**

- `value`: String
  - Line color to set.

### _update_line_dash_dot_setting_and_skip_appending_exp method docstring

Update line dash dot (1-dot chain) setting and skip appending expression.<hr>

**[Parameters]**

- `value`: LineDashDotSetting or None
  - Line dash dot (1-dot chain) setting to set.

### _update_line_dash_setting_and_skip_appending_exp method docstring

Update line dash setting and skip appending expression.<hr>

**[Parameters]**

- `value`: LineDashSetting or None
  - Line dash setting to set.

### _update_line_dot_setting_and_skip_appending_exp method docstring

Update line dot setting and skip appending expression.<hr>

**[Parameters]**

- `value`: LineDotSetting or None
  - Line dot setting to set.

### _update_line_joints_and_skip_appending_exp method docstring

Update line joints and skip appending expression.<hr>

**[Parameters]**

- `value`: STring or LineJoints
  - Line joints style setting to set.

### _update_line_round_dot_setting_and_skip_appending_exp method docstring

Update line round setting and skip appending expression.<hr>

**[Parameters]**

- `value`: LineRoundSetting or None
  - Line round dot setting to set.

### _update_line_thickness_and_skip_appending_exp method docstring

Update line thickness and skip appending expression.<hr>

**[Parameters]**

- `value`: int or Int
  - Line thickness to set.

### animation_fill_alpha method docstring

Set the fill alpha (opacity) animation setting.<hr>

**[Parameters]**

- `alpha`: Number or float
  - The final alpha (opacity) of the animation.
- `duration`: Int or int, default 3000
  - Milliseconds before an animation ends.
- `delay`: Int or int, default 0
  - Milliseconds before an animation starts.
- `easing`: Easing, default Easing.LINEAR
  - Easing setting.

<hr>

**[Returns]**

- `animation_fill_alpha`: AnimationFillAlpha
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
>>> circle: ap.Circle = sprite.graphics.draw_circle(
...     x=100, y=100, radius=50)
>>> _ = circle.animation_y(
...     y=100,
...     duration=1500,
...     easing=ap.Easing.EASE_OUT_QUINT,
... ).start()
```

<hr>

**[References]**

- [animation_fill_alpha interface document](https://simon-ritchie.github.io/apysc/animation_fill_alpha.html)
- [Animation interfaces duration setting document](https://simon-ritchie.github.io/apysc/animation_duration.html)
- [Each animation interface return value document](https://simon-ritchie.github.io/apysc/animation_return_value.html)
- [Sequential animation setting document](https://simon-ritchie.github.io/apysc/sequential_animation.html)
- [animation_parallel interface document](https://simon-ritchie.github.io/apysc/animation_parallel.html)
- [Easing enum document](https://simon-ritchie.github.io/apysc/easing_enum.html)

### animation_fill_color method docstring

Set the fill color animation setting.<hr>

**[Parameters]**

- `fill_color`: str or String
  - The final fill color (hex color code) of the animation.
- `duration`: Int or int, default 3000
  - Milliseconds before an animation ends.
- `delay`: Int or int, default 0
  - Milliseconds before an animation starts.
- `easing`: Easing, default Easing.LINEAR
  - Easing setting.

<hr>

**[Returns]**

- `animation_fill_color`: AnimationFillColor
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
>>> _ = rectangle.animation_fill_color(
...     fill_color='#f0a',
...     duration=1500,
...     easing=ap.Easing.EASE_OUT_QUINT,
... ).start()
```

<hr>

**[References]**

- [animation_fill_color interface document](https://simon-ritchie.github.io/apysc/animation_fill_color.html)
- [Animation interfaces duration setting document](https://simon-ritchie.github.io/apysc/animation_duration.html)
- [Animation interfaces delay setting document](https://simon-ritchie.github.io/apysc/animation_delay.html)
- [Each animation interface return value document](https://simon-ritchie.github.io/apysc/animation_return_value.html)
- [Sequential animation setting document](https://simon-ritchie.github.io/apysc/sequential_animation.html)
- [animation_parallel interface document](https://simon-ritchie.github.io/apysc/animation_parallel.html)
- [Easing enum document](https://simon-ritchie.github.io/apysc/easing_enum.html)

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

### animation_line_alpha method docstring

Set the line alpha animation setting.<hr>

**[Parameters]**

- `alpha`: Number or float
  - The final line alpha of the animation.
- `duration`: Int or int, default 3000
  - Milliseconds before an animation ends.
- `delay`: Int or int, default 0
  - Milliseconds before an animation starts.
- `easing`: Easing, default Easing.LINEAR
  - Easing setting.

<hr>

**[Returns]**

- `animation_line_alpha`: AnimationLineAlpha
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
...     color='#fff', thickness=5, alpha=1.0)
>>> rectangle: ap.Rectangle = sprite.graphics.draw_rect(
...     x=50, y=50, width=50, height=50)
>>> _ = rectangle.animation_line_alpha(
...     alpha=0.0,
...     duration=1500,
...     easing=ap.Easing.EASE_OUT_QUINT,
... ).start()
```

<hr>

**[References]**

- [animation_line_alpha interface document](https://simon-ritchie.github.io/apysc/animation_line_alpha.html)
- [Animation interfaces duration setting document](https://simon-ritchie.github.io/apysc/animation_duration.html)
- [Animation interfaces delay setting document](https://simon-ritchie.github.io/apysc/animation_delay.html)
- [Each animation interface return value document](https://simon-ritchie.github.io/apysc/animation_return_value.html)
- [Sequential animation setting document](https://simon-ritchie.github.io/apysc/sequential_animation.html)
- [animation_parallel interface document](https://simon-ritchie.github.io/apysc/animation_parallel.html)
- [Easing enum document](https://simon-ritchie.github.io/apysc/easing_enum.html)

### animation_line_color method docstring

Set the line color animation setting.<hr>

**[Parameters]**

- `line_color`: str or String
  - The final line color (hex color code) of the animation.
- `duration`: Int or int, default 3000
  - Milliseconds before an animation ends.
- `delay`: Int or int, default 0
  - Milliseconds before an animation starts.
- `easing`: Easing, default Easing.LINEAR
  - Easing setting.

<hr>

**[Returns]**

- `animation_line_color`: AnimationLineColor
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
...     color='#fff', thickness=5)
>>> rectangle: ap.Rectangle = sprite.graphics.draw_rect(
...     x=50, y=50, width=50, height=50)
>>> _ = rectangle.animation_line_color(
...     line_color='#0af',
...     duration=1500,
...     easing=ap.Easing.EASE_OUT_QUINT,
... ).start()
```

<hr>

**[References]**

- [animation_line_color interface document](https://simon-ritchie.github.io/apysc/animation_line_color.html)
- [Animation interfaces duration setting document](https://simon-ritchie.github.io/apysc/animation_duration.html)
- [Animation interfaces delay setting document](https://simon-ritchie.github.io/apysc/animation_delay.html)
- [Each animation interface return value document](https://simon-ritchie.github.io/apysc/animation_return_value.html)
- [Sequential animation setting document](https://simon-ritchie.github.io/apysc/sequential_animation.html)
- [animation_parallel interface document](https://simon-ritchie.github.io/apysc/animation_parallel.html)
- [Easing enum document](https://simon-ritchie.github.io/apysc/easing_enum.html)

### animation_line_thickness method docstring

Set the line thickness animation setting.<hr>

**[Parameters]**

- `thickness`: Int or int
  - The final line thickness of the animation.
- `duration`: Int or int, default 3000
  - Milliseconds before an animation ends.
- `delay`: Int or int, default 0
  - Milliseconds before an animation starts.
- `easing`: Easing, default Easing.LINEAR
  - Easing setting.

<hr>

**[Returns]**

- `animation_line_thickness`: AnimationLineThickness
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
>>> _ = rectangle.animation_line_thickness(
...     thickness=6,
...     duration=1500,
...     easing=ap.Easing.EASE_OUT_QUINT,
... ).start()
```

<hr>

**[References]**

- [animation_line_thickness interface document](https://simon-ritchie.github.io/apysc/animation_line_thickness.html)
- [Animation interfaces duration setting document](https://simon-ritchie.github.io/apysc/animation_duration.html)
- [Animation interfaces delay setting document](https://simon-ritchie.github.io/apysc/animation_delay.html)
- [Each animation interface return value document](https://simon-ritchie.github.io/apysc/animation_return_value.html)
- [Sequential animation setting document](https://simon-ritchie.github.io/apysc/sequential_animation.html)
- [animation_parallel interface document](https://simon-ritchie.github.io/apysc/animation_parallel.html)
- [Easing enum document](https://simon-ritchie.github.io/apysc/easing_enum.html)

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

### append_line_point method docstring

Append line point at the end.<hr>

**[Parameters]**

- `x`: int or Int
  - X-coordinate.
- `y`: int or Int
  - Y-coordinate.

<hr>

**[Examples]**

```py
>>> import apysc as ap
>>> stage: ap.Stage = ap.Stage()
>>> sprite: ap.Sprite = ap.Sprite()
>>> sprite.graphics.begin_fill('#0af')
>>> polygon: ap.Polygon = sprite.graphics.draw_polygon(
...     points=[
...         ap.Point2D(x=0, y=0),
...         ap.Point2D(x=0, y=50),
...         ap.Point2D(x=50, y=50),
...     ])
>>> polygon.append_line_point(x=50, y=0)
```

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