# Array class

This page explains the `Array` class.

Before reading on, maybe it is helpful to read the following page:

- [Why the apysc library doesn't use the Python built-in data type](why_apysc_doesnt_use_python_builtin_data_type.md)

## What is the Array?

The `Array` class is the apysc array class. It behaves like the Python built-in `list` value.

## Constructor method

The `Array` class constructor method requires iterable objects, like the `list`\, `tuple`\, `range`\, or `Array` value.

```py
# runnable
import apysc as ap

ap.Stage()
arr_from_list: ap.Array = ap.Array([1, 2, 3])
assert arr_from_list == [1, 2, 3]

arr_from_tuple: ap.Array = ap.Array((4, 5, 6))
assert arr_from_tuple == [4, 5, 6]

other_arr: ap.Array = ap.Array([7, 8, 9])
arr_from_arr: ap.Array = ap.Array(other_arr)
assert arr_from_arr == [7, 8, 9]
```

## Generic type annotation

If the `Array` values types are unique, you can set the generic type to an `Array` value. This annotation may be helpful when you use it on the IDE (for type checkers).

```py
# runnable
import apysc as ap

ap.Stage()
arr: ap.Array[int] = ap.Array([1, 2])
int_val: int = arr.pop()
assert isinstance(int_val, int)
```

## fixed_value_type argument

The constructor's `fixed_value_type` argument is optional.

If specified, the array value-related interfaces, such as the `__getitem__` method (array subscript interface, for example, `arr[5]`), becomes possibly returning a specified type instance.

It returns an instance of the specified type, especially when an array index exceeds the length of an array on the Python runtime.

```py
# runnable
import apysc as ap

ap.Stage(
    stage_width=100, stage_height=50, background_color="#333", stage_elem_id="stage"
)
arr: ap.Array[ap.Int] = ap.Array([ap.Int(10)], fixed_value_type=ap.Int)

# Index 5 is out of bounds on the Python runtime,
# but since the `fixed_value_type` is the `ap.Int`,
# this interface returns an `ap.Int` value.
int_value: ap.Int = arr[5]
assert isinstance(int_value, ap.Int)
```

## See also

- [Funcdamental data classes common value interface](fundamental_data_classes_value_interface.md)
- [Array class append and push interfaces](array_append_and_push.md)
- [Array class extend and concat interfaces](array_extend_and_concat.md)
- [Array class insert and insert_at interfaces](array_insert_and_insert_at.md)
- [Array class pop interface](array_pop.md)
- [Array class remove and remove_at interfaces](array_remove_and_remove_at.md)
- [Array class sort interface](array_sort.md)
- [Array class reverse interface](array_reverse.md)
- [Array class slice interface](array_slice.md)
- [Array class length interface](array_length.md)
- [Array class join interface](array_join.md)
- [Array class index_of interface](array_index_of.md)
- [Array class comparison interfaces](array_comparison.md)


## Array class constructor API

<!-- Docstring: apysc._type.array.Array.__init__ -->

<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>

**[Interface signature]** `__init__(self, value: Union[List[~_ArrValue], tuple, range, ForwardRef('Array')], *, fixed_value_type: Union[Type[apysc._loop.initialize_with_base_value_interface.InitializeWithBaseValueInterface], NoneType] = None, variable_name_suffix: str = '', skip_init_substitution_expression_appending: bool = False) -> None`<hr>

**[Interface summary]**

Array class for the apysc library.<hr>

**[Parameters]**

- `value`: Array or list or tuple or range
  - Initial array value.
- `fixed_value_type`: Optional[Type[InitializeWithBaseValueInterface]], optional
  - A fixed value type of array. This argument only becomes an apysc type, such as the `ap.Int`, `ap.String`, or `ap.Rectangle`. If specified, the array value-related interfaces, such as the `__getitem__` method (array subscript interface, for example, `arr[5]`), becomes possibly returning a specified value type instance.
- `variable_name_suffix`: str, default ''
  - A JavaScript variable name suffix string. This setting is sometimes useful for JavaScript debugging.
- `skip_init_substitution_expression_appending`: bool, default False
  - A boolean indicates whether to skip an initial substitution expression or not. This class uses this option internally.

<hr>

**[Examples]**

```py
>>> import apysc as ap
>>> _ = ap.Stage()
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

- [Array class comparison interfaces](https://simon-ritchie.github.io/apysc/en/array_comparison.html)

## value property API

<!-- Docstring: apysc._type.array.Array.value -->

<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>

**[Interface summary]**

Get a current array value.<hr>

**[Returns]**

- `value`: list
  - Current array value.

<hr>

**[Examples]**

```py
>>> import apysc as ap
>>> _ = ap.Stage()
>>> arr: ap.Array = ap.Array([1, 2, 3])
>>> arr.value = [4, 5, 6]
>>> arr.value
[4, 5, 6]
```

<hr>

**[References]**

- [apysc fundamental data classes value interface](https://simon-ritchie.github.io/apysc/en/fundamental_data_classes_value_interface.html)