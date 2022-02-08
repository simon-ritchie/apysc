# apysc._type.array docstrings

## Module summary

Class implementation for array.

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

## Boolean class docstring

Boolean class for the apysc library.

Boolean class for the apysc library.<hr>

**[Notes]**

The Bool class is the alias of the Boolean, and it behaves the same as the Boolean class.<hr>

**[Examples]**

```py
>>> import apysc as ap
>>> bool_val_1: ap.Boolean = ap.Boolean(True)
>>> bool_val_1
Boolean(True)

>>> bool_val_2: ap.Bool = ap.Bool(True)
>>> bool_val_2
Boolean(True)

>>> bool_val_2.not_
Boolean(False)
```

<hr>

**[References]**

- [Boolean document](https://simon-ritchie.github.io/apysc/boolean.html)

### __bool__ method docstring

Get a boolean value directly.<hr>

**[Returns]**

- `result`: bool
  - Current boolean value.

### ABCMeta method docstring

Metaclass for defining Abstract Base Classes (ABCs). Use this metaclass to create an ABC. An ABC can be subclassed directly, and then acts as a mix-in class. You can also register unrelated concrete classes (even built-in classes) and unrelated ABCs as 'virtual subclasses' -- these and their descendants will be considered subclasses of the registering ABC by the built-in issubclass() function, but the registering ABC won't show up in their MRO (Method Resolution Order) nor will method implementations defined by the registering ABC be callable (not even via super()).

### __eq__ method docstring

Comparison method for equal condition.<hr>

**[Parameters]**

- `other`: *
  - Other value to compare (Boolean, bool, int, or Int).

<hr>

**[Returns]**

- `result`: Boolean
  - Comparison result.

### __init__ method docstring

Boolean class for apysc library.<hr>

**[Parameters]**

- `value`: bool or int or Boolean or Int
  - Initial boolean value. 0 or 1 are acceptable for an integer value.

<hr>

**[Notes]**

The Bool class is the alias of the Boolean, and it behaves the same as the Boolean class.<hr>

**[Examples]**

```py
>>> import apysc as ap
>>> bool_val_1: ap.Boolean = ap.Boolean(True)
>>> bool_val_1
Boolean(True)

>>> bool_val_2: ap.Bool = ap.Bool(True)
>>> bool_val_2
Boolean(True)
```

<hr>

**[References]**

- [Boolean document](https://simon-ritchie.github.io/apysc/boolean.html)

### __ne__ method docstring

Comparison method for not equal condition.<hr>

**[Parameters]**

- `other`: *
  - Other value to compare (Boolean, bool, int, or Int).

<hr>

**[Returns]**

- `result`: Boolean
  - Comparison result.

### __repr__ method docstring

Get a representation string of this instance.<hr>

**[Returns]**

- `repr_str`: str
  - Representation string of this instance.

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
- `other`: Boolean or Int
  - Other value to compare.

### _append_ne_expression method docstring

Append __ne__ method expression.<hr>

**[Parameters]**

- `result`: Boolean
  - Result boolean value.
- `other`: Boolean or Int
  - Other value to compare.

### _append_not_prop_expression method docstring

Append not_ property expression.<hr>

**[Parameters]**

- `result`: Boolean
  - Result Boolean value.

### _append_value_setter_expression method docstring

Append value's setter expression.<hr>

**[Parameters]**

- `value`: bool or VariableNameInterface
  - Any value to set.

### _append_value_updating_cpy_exp_to_handler_scope method docstring

Append a value updating copy expression if the current scope is an event handler's one.<hr>

**[Parameters]**

- `result_variable_name`: str
  - Copied value's variable name.

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

### _get_bool_from_arg_value method docstring

Get bool value from specified argument value.<hr>

**[Parameters]**

- `value`: bool or int or Boolean or Int
  - Specified value. 0 or 1 are acceptable for integer value.

<hr>

**[Returns]**

- `result`: bool
  - Converted boolean value.

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

- `value`: bool or int or Boolean or Int
  - Any boolean value to set.

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

### _validate_comparison_other_type method docstring

Validate comparison's other value type.<hr>

**[Parameters]**

- `other`: *
  - Other value to compare.

<hr>

**[Raises]**

- ValueError: If other value type is not Boolean, bool, Int, and int.

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

## CopyInterface class docstring



### __init__ method docstring

Initialize self. See help(type(self)) for accurate signature.

### _append_copy_expression method docstring

Append copy expression.<hr>

**[Parameters]**

- `result_variable_name`: str
  - Copied value's variable name.

### _append_value_updating_cpy_exp_to_handler_scope method docstring

Append a value updating copy expression if the current scope is an event handler's one.<hr>

**[Parameters]**

- `result_variable_name`: str
  - Copied value's variable name.

### _copy method docstring

Make a deep copy of this instance.<hr>

**[Returns]**

- `result`: *
  - Copied instance.

### _get_previous_variable_name method docstring

Get a previous variable name.<hr>

**[Returns]**

- `previous_variable_name`: str
  - A previous variable name of this instance. If that value is not existing, then a blank string will be returned.

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

## Dict class docstring



### GenericMeta method docstring

Metaclass for generic types. This is a metaclass for typing.Generic and generic ABCs defined in typing module. User defined subclasses of GenericMeta can override __new__ and invoke super().__new__. Note that GenericMeta.__new__ has strict rules on what is allowed in its bases argument: * plain Generic is disallowed in bases; * Generic[...] should appear in bases at most once; * if Generic[...] is present, then it should list all type variables that appear in other bases. In addition, type of all generic bases is erased, e.g., C[int] is stripped to plain C.

### __contains__ method docstring

True if D has a key k, else False.

### __delitem__ method docstring

Delete self[key].

### dict method docstring

dict() -> new empty dictionary dict(mapping) -> new dictionary initialized from a mapping object's (key, value) pairs dict(iterable) -> new dictionary initialized as if via: d = {} for k, v in iterable: d[k] = v dict(**kwargs) -> new dictionary initialized with the name=value pairs in the keyword argument list. For example: dict(one=1, two=2)

### __getitem__ method docstring

x.__getitem__(y) <==> x[y]

### __init__ method docstring

Initialize self. See help(type(self)) for accurate signature.

### __iter__ method docstring

Implement iter(self).

### __len__ method docstring

Return len(self).

### object method docstring

The most base type

### __setitem__ method docstring

Set self[key] to value.

### __sizeof__ method docstring

D.__sizeof__() -> size of D in memory, in bytes

### clear method docstring

D.clear() -> None. Remove all items from D.

### copy method docstring

D.copy() -> a shallow copy of D

### fromkeys method docstring

Returns a new dict with keys from iterable and values equal to value.

### get method docstring

D.get(k[,d]) -> D[k] if k in D, else d. d defaults to None.

### items method docstring

D.items() -> a set-like object providing a view on D's items

### keys method docstring

D.keys() -> a set-like object providing a view on D's keys

### pop method docstring

D.pop(k[,d]) -> v, remove specified key and return the corresponding value. If key is not found, d is returned if given, otherwise KeyError is raised

### popitem method docstring

D.popitem() -> (k, v), remove and return some (key, value) pair as a 2-tuple; but raise KeyError if D is empty.

### setdefault method docstring

D.setdefault(k[,d]) -> D.get(k,d), also set D[k]=d if k not in D

### update method docstring

D.update([E, ]**F) -> None. Update D from dict/iterable E and F. If E is present and has a .keys() method, then does: for k in E: D[k] = E[k] If E is present and lacks a .keys() method, then does: for k, v in E: D[k] = v In either case, this is followed by: for k in F: D[k] = F[k]

### values method docstring

D.values() -> an object providing a view on D's values

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

## List class docstring



### __add__ method docstring

Return self+value.

### GenericMeta method docstring

Metaclass for generic types. This is a metaclass for typing.Generic and generic ABCs defined in typing module. User defined subclasses of GenericMeta can override __new__ and invoke super().__new__. Note that GenericMeta.__new__ has strict rules on what is allowed in its bases argument: * plain Generic is disallowed in bases; * Generic[...] should appear in bases at most once; * if Generic[...] is present, then it should list all type variables that appear in other bases. In addition, type of all generic bases is erased, e.g., C[int] is stripped to plain C.

### __contains__ method docstring

Return key in self.

### __delitem__ method docstring

Delete self[key].

### list method docstring

list() -> new empty list list(iterable) -> new list initialized from iterable's items

### __getitem__ method docstring

x.__getitem__(y) <==> x[y]

### __iadd__ method docstring

Implement self+=value.

### __imul__ method docstring

Implement self*=value.

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

### __reversed__ method docstring

L.__reversed__() -- return a reverse iterator over the list

### __rmul__ method docstring

Return value*self.

### __setitem__ method docstring

Set self[key] to value.

### __sizeof__ method docstring

L.__sizeof__() -- size of L in memory, in bytes

### append method docstring

L.append(object) -> None -- append object to end

### clear method docstring

L.clear() -> None -- remove all items from L

### copy method docstring

L.copy() -> list -- a shallow copy of L

### count method docstring

L.count(value) -> integer -- return number of occurrences of value

### extend method docstring

L.extend(iterable) -> None -- extend list by appending elements from the iterable

### index method docstring

L.index(value, [start, [stop]]) -> integer -- return first index of value. Raises ValueError if the value is not present.

### insert method docstring

L.insert(index, object) -- insert object before index

### pop method docstring

L.pop([index]) -> item -- remove and return item at index (default last). Raises IndexError if list is empty or index is out of range.

### remove method docstring

L.remove(value) -> None -- remove first occurrence of value. Raises ValueError if the value is not present.

### reverse method docstring

L.reverse() -- reverse *IN PLACE*

### sort method docstring

L.sort(key=None, reverse=False) -> None -- stable sort *IN PLACE*

## RevertInterface class docstring



### ABCMeta method docstring

Metaclass for defining Abstract Base Classes (ABCs). Use this metaclass to create an ABC. An ABC can be subclassed directly, and then acts as a mix-in class. You can also register unrelated concrete classes (even built-in classes) and unrelated ABCs as 'virtual subclasses' -- these and their descendants will be considered subclasses of the registering ABC by the built-in issubclass() function, but the registering ABC won't show up in their MRO (Method Resolution Order) nor will method implementations defined by the registering ABC be callable (not even via super()).

### __init__ method docstring

Initialize self. See help(type(self)) for accurate signature.

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

### _initialize_ss_exists_val_if_not_initialized method docstring

Initialize _snapshot_exists_ value it hasn't been initialized yet.

### _make_snapshot method docstring

Make value's snapshot.<hr>

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

## VariableNameInterface class docstring



### __init__ method docstring

Initialize self. See help(type(self)) for accurate signature.

### _get_previous_variable_name method docstring

Get a previous variable name.<hr>

**[Returns]**

- `previous_variable_name`: str
  - A previous variable name of this instance. If that value is not existing, then a blank string will be returned.