# Array

This page will explain the `Array` class.

Before reading on, maybe it is useful to read the following page:

- [Why not using the Python built-in data type in the apysc library?](why_not_using_python_builtin_data_type.md)

## What is the Array?

The `Array` class is the apysc array class. It behaves like the Python built-in `list` value.

## Constructor method

The `Array` class constructor method requires iterable objects, like the `list`, `tuple`, `range`, or `Array` value.

```py
# runnable
import apysc as ap

arr_from_list: ap.Array = ap.Array([1, 2, 3])
assert arr_from_list == [1, 2, 3]

arr_from_tuple: ap.Array = ap.Array((4, 5, 6))
assert arr_from_tuple == [4, 5, 6]

other_arr: ap.Array = ap.Array([7, 8, 9])
arr_from_arr: ap.Array = ap.Array(other_arr)
assert arr_from_arr == [7, 8, 9]
```

## Generic type

If the `Array` values are unique types, then you can set the generic type to an `Array` value. This may be useful when you use it on the IDE (for type checkers).

```py
# runnable
from typing import Any, List
import apysc as ap

arr: ap.Array[int] = ap.Array([1, 2])
int_val: int = arr.pop()
assert isinstance(int_val, int)
```

## See also

- [apysc basic data classes common value interface](basic_data_classes_value_interface.md)
- [Array class append and push interfaces](array_append_and_push.md)
- [Array class extend and concat interfaces](array_extend_and_concat.md)
- [Array class insert and insert at interfaces](array_insert_and_insert_at.md)
- [Array class pop interface](array_pop.md)
- [Array class remove and remove at interfaces](array_remove_and_remove_at.md)
- [Array class sort interface](array_sort.md)
- [Array class reverse interface](array_reverse.md)
- [Array class slice interface](array_slice.md)
- [Array class length interface](array_length.md)
- [Array class join interface](array_join.md)
- [Array class index of interface](array_index_of.md)
- [Array class comparison interfaces](array_comparison.md)
