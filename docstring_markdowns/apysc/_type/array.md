# `apysc._type.array` docstrings

## Module summary

Class implementation for array.

## `Array` class docstring

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

### `__bool__` method docstring

Get a boolean value whether this array is empty or not.<hr>

**[Returns]**

- `result`: bool
  - If this array is empty, True will be returned.

### `__delitem__` method docstring

Delete specified index value from this array.<hr>

**[Parameters]**

- `index`: Int or int
  - Array's index to delete. Currently not supported tuple value (e.g., slicing).

<hr>

**[Raises]**

- ValueError: If specified index type is not int and Int.

### `__eq__` method docstring

Equal comparison method.<hr>

**[Parameters]**

- `other`: *
  - Other value to compare. list or Array types are acceptable.

<hr>

**[Returns]**

- `result`: Boolean
  - Comparison result.

### `__getitem__` method docstring

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

### `__init__` method docstring

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

### `__len__` method docstring

This method is disabled and can't use from Array instance.

### `__ne__` method docstring

Not equal comparison method.<hr>

**[Parameters]**

- `other`: *
  - Other value to compare. list or Array types are acceptable.

<hr>

**[Returns]**

- `result`: Boolean
  - Comparison result.

### `__repr__` method docstring

Get a representation string of this instance.<hr>

**[Returns]**

- `repr_str`: str
  - Representation string of this instance.

### `__setitem__` method docstring

Set value to a specified index.<hr>

**[Parameters]**

- `index`: Int or int
  - Array's index to set value. Currently not supported tuple value (e.g., slicing).
- `value`: *
  - Any value to set.

<hr>

**[Raises]**

- ValueError: If specified index type is not int and Int.

### `__str__` method docstring

String conversion method.<hr>

**[Returns]**

- `string`: str
  - Converted value string.

### `_append_concat_expression` method docstring

Append concat method expression.<hr>

**[Parameters]**

- `concatenated`: Array
  - Concatenated array value.
- `other_arr`: list or tuple or Array
  - Other array-like value to concatenate.

### `_append_constructor_expression` method docstring

Append constructor expression.

### `_append_eq_expression` method docstring

Append an __eq__ expression.<hr>

**[Parameters]**

- `result`: Boolean
  - Result boolean value.
- `other`: Array
  - Array other value to compare.

### `_append_extend_expression` method docstring

Append extend method expression.<hr>

**[Parameters]**

- `other_arr`: list or tuple or Array
  - Other array-like value to concatenate.

### `_append_getitem_expression` method docstring

Append __getitem__ expression.<hr>

**[Parameters]**

- `index`: Int or int
  - Array's index to get value.
- `value`: *
  - Specified index's value.

### `_append_index_of_expression` method docstring

Append index_of method expression.<hr>

**[Parameters]**

- `index`: Int
  - Found position of index. If value is not contains, -1 will be set.
- `value`: *
  - Any value to search.

### `_append_insert_expression` method docstring

Append insert method expression.<hr>

**[Parameters]**

- `index`: Int or int
  - Index to append value to.
- `value`: *
  - Any value to append.

### `_append_join_expression` method docstring

Append join method expression.<hr>

**[Parameters]**

- `joined`: String
  - Joined string.
- `sep`: String or str
  - Separator string.

### `_append_length_expression` method docstring

Append length method expression.<hr>

**[Parameters]**

- `length`: Int
  - Created length Int variable.

### `_append_ne_expression` method docstring

Append a __ne__ expression.<hr>

**[Parameters]**

- `result`: Boolean
  - Result boolean value.
- `other`: Array
  - Array other value to compare.

### `_append_pop_expression` method docstring

Append pop method expression.<hr>

**[Parameters]**

- `value`: *
  - Removed value.

### `_append_push_and_append_expression` method docstring

Append push and append method expression.<hr>

**[Parameters]**

- `value`: *
  - Any value to append.

### `_append_remove_at_expression` method docstring

Append remove_at method expression.<hr>

**[Parameters]**

- `index`: Int or int
  - Index to remove value.

### `_append_remove_expression` method docstring

Append remove method expression.<hr>

**[Parameters]**

- `value`: Any
  - Value to remove.

### `_append_reverse_expression` method docstring

Append reverse method expression.

### `_append_setitem_expression` method docstring

Append __setitem__ method expression.<hr>

**[Parameters]**

- `index`: Int or int
  - Array's index to set value. Currently not supported tuple value (e.g., slicing).
- `value`: *
  - Any value to set.

### `_append_slice_expression` method docstring

Append slice method expression.<hr>

**[Parameters]**

- `sliced_arr`: Array
  - Sliced array.
- `start`: Int or int or None
  - Slicing start index.
- `end`: Int or int or None
  - Slicing end index.

### `_append_sort_expression` method docstring

Append sort method expression.

### `_append_value_setter_expression` method docstring

Append value's setter expression.<hr>

**[Parameters]**

- `value`: list or tuple or Array
  - Iterable value (list, tuple, or Array) to set.

### `_convert_other_val_to_array` method docstring

If comparison's other value is list value, then convert it to Array instance.<hr>

**[Parameters]**

- `other`: *
  - Other value to compare.

<hr>

**[Returns]**

- `converted_val`: *
  - Converted value. If other value is list, then this will be Array type. Otherwise this will be returned directly (not to be converted).

### `_convert_range_to_list` method docstring

Convert argument value to list that if specified value is range type.<hr>

**[Parameters]**

- `value`: list or tuple or range or Array
  - Target value.

<hr>

**[Returns]**

- `value`: list or tuple or Array
  - Converted value.

### `_get_builtin_int_from_index` method docstring

Get Python builtin integer from index value.<hr>

**[Parameters]**

- `index`: Int or int
  - Specified array's index.

<hr>

**[Returns]**

- `builtin_int_index`: int
  - Python builtin integer index value.

### `_get_list_value` method docstring

Get a list value from specified list, tuple, or Array value.<hr>

**[Parameters]**

- `value`: list or tuple or Array
  - Specified list, tuple, or Array value.

<hr>

**[Returns]**

- `list_val`: list
  - Converted list value.

### `_make_snapshot` method docstring

Make values' snapshot.<hr>

**[Parameters]**

- `snapshot_name`: str
  - Target snapshot name.

### `_revert` method docstring

Revert values if snapshot exists.<hr>

**[Parameters]**

- `snapshot_name`: str
  - Target snapshot name.

### `_validate_acceptable_value_type` method docstring

Validate that specified value is acceptable type or not.<hr>

**[Parameters]**

- `value`: list or tuple or range or Array
  - Iterable value to check.

<hr>

**[Raises]**

- ValueError: If specified value's type is not list, tuple, or Array.

### `_validate_index_type_is_int` method docstring

Validate whether index value type is int (or Int) or not.<hr>

**[Parameters]**

- `index`: Int or int
  - Index value to check.

<hr>

**[Raises]**

- ValueError: If index type is not int or Int type.

### `append` method docstring

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

### `concat` method docstring

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

### `extend` method docstring

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

### `index_of` method docstring

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

### `insert` method docstring

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

### `insert_at` method docstring

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

### `join` method docstring

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

### `pop` method docstring

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

### `push` method docstring

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

### `remove` method docstring

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

### `remove_at` method docstring

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

### `reverse` method docstring

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

### `slice` method docstring

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

### `sort` method docstring

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