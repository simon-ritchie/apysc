# `apysc._console.assertion` docstrings

## Module summary

Each js assertion (console.assert) interface implementations. Mainly following interfaces are defined: <br>・assert_equal JavaScript assertion interface for the equal condition. <br>・assert_not_equal JavaScript assertion interface for the not equal condition. <br>・assert_true JavaScript assertion interface for the true condition. <br>・assert_false JavaScript assertion interface for the false condition. <br>・assert_greater JavaScript assertion interface for the greater than condition. <br>・assert_greater_equal JavaScript assertion interface for the greater than or equal to condition. <br>・assert_less JavaScript assertion interface for the less than condition. <br>・assert_less_equal JavaScript assertion interface for the less than or equal to condition. <br>・assert_arrays_equal JavaScript assertion interface for the Array values equal condition. <br>・assert_arrays_not_equal JavaScript assertion interface for the Array values not equal condition. <br>・assert_dicts_equal JavaScript assertion interface for the Dictionary values equal condition. <br>・assert_dicts_not_equal JavaScript assertion interface for the Dictionary values not equal condition. <br>・assert_defined JavaScript assertion interface for the defined (not undefined) value condition. <br>・assert_undefined JavaScript assertion interface for the undefined value condition.

## `_add_equal_if_type_strict_setting_is_true` function docstring

Add single equal character to expression if type_string setting is True.<hr>

**[Parameters]**

- `expression`: str
  - Expression to be added.
- `type_strict`: bool
  - Type strict setting value.

<hr>

**[Returns]**

- `expression`: str
  - If the type_strict setting is True value, this interface appends a single equal character to tail.

## `_get_left_and_right_strs` function docstring

Get left and right value strings from specified values.<hr>

**[Parameters]**

- `left`: *
  - Left-side value to compare.
- `right`: *
  - Right-side value to compare.

<hr>

**[Returns]**

- `left_str`: str
  - Left-side value's string. If a value is a string, this interface wraps this left-side value by double quotation.
- `right_str`: str
  - Right-side value's string. If a value is a string, this interface wraps this right-side value by double quotation.

## `_make_arrays_or_dicts_comparison_expression` function docstring

Make arrays or dicts comparison (assert_arrays_equal, assert_arrays_not_equal, assert_dicts_equal, or assert_dicts_not_equal) expression string.<hr>

**[Parameters]**

- `left`: *
  - Left-side value to compare.
- `right`: *
  - Right-side value to compare.
- `msg`: str, optional
  - Message to display when assertion failed.
- `not_condition`: bool
  - Boolean value whether this expression is not condition (assert_arrays_not_equal) or not.

<hr>

**[Returns]**

- `expression`: str
  - A result expression string.

## `_trace_arrays_or_dicts_assertion_info` function docstring

Append arrays or dictionaries values' information trace expression.<hr>

**[Parameters]**

- `interface_label`: str
  - Target assertion interface label, e.g., 'assert_arrays_equal'.
- `left`: *
  - Left-side value to compare.
- `right`: *
  - Right-side value to compare.
- `outer_frames_index_adjustment`: int
  - The trace's outer frames index adjustment setting. This function uses this argument to adjust the caller's information.

## `_trace_info` function docstring

Append trace expression of specified values.<hr>

**[Parameters]**

- `interface_label`: str
  - Target assertion interface label, e.g., 'assert_equal'.
- `left`: *
  - Left-side value to compare.
- `right`: *
  - Right-side value to compare.
- `outer_frames_index_adjustment`: int
  - The trace's outer frames index adjustment setting. This function uses this argument to adjust the caller's information.

## `_value_type_is_array` function docstring

Get a boolean value whether the specified value is Array type or not.<hr>

**[Parameters]**

- `value`: *
  - Target value to check.

<hr>

**[Returns]**

- `result`: bool
  - If the value type is Array, this interface returns True.

## `_value_type_is_dict` function docstring

Get a boolean value whether the specified value is Dictionary type or not.<hr>

**[Parameters]**

- `value`: *
  - Target value to check.

<hr>

**[Returns]**

- `result`: bool
  - If the value type is Dictionary, this interface returns True.

## `assert_arrays_equal` function docstring

JavaScript assertion interface for the Array values equal condition.<hr>

**[Parameters]**

- `left`: *
  - Left-side value to compare.
- `right`: *
  - Right-side value to compare.
- `msg`: str, optional
  - Message to display when assertion failed.
- `outer_frames_index_adjustment`: int, optional
  - The trace's outer frames index adjustment setting. This function uses this argument to adjust the caller's information. Also, this function only uses this argument in internal logic.

<hr>

**[Notes]**

This interface is used instead of assert_equal for Array class comparison (JavaScript can not compare arrays directly, like a Python, for example, `[1, 2] === [1, 2]` becomes false).<hr>

**[Examples]**

```py
>>> import apysc as ap
>>> _ = ap.Stage()
>>> arr_1: ap.Array = ap.Array([1, 2, 3])
>>> arr_2: ap.Array = ap.Array([1, 2, 3])
>>> ap.assert_arrays_equal(arr_1, arr_2)
```

<hr>

**[References]**

- [assert_arrays_equal and assert_arrays_not_equal interfaces](https://simon-ritchie.github.io/apysc/en/assert_arrays_equal_and_arrays_not_equal.html)

## `assert_arrays_not_equal` function docstring

JavaScript assertion interface for the Array values not equal condition.<hr>

**[Parameters]**

- `left`: *
  - Left-side value to compare.
- `right`: *
  - Right-side value to compare.
- `msg`: str, optional
  - Message to display when assertion failed.
- `outer_frames_index_adjustment`: int, optional
  - The trace's outer frames index adjustment setting. This function uses this argument to adjust the caller's information. Also, this function only uses this argument in internal logic.

<hr>

**[Notes]**

This interface is used instead of assert_not_equal for Array class comparison (JavaScript can not compare arrays directly, like a Python, for example, `[1, 2] === [1, 2]` becomes false).<hr>

**[Examples]**

```py
>>> import apysc as ap
>>> _ = ap.Stage()
>>> arr_1: ap.Array = ap.Array([1, 2, 3])
>>> arr_2: ap.Array = ap.Array([4, 5, 6])
>>> ap.assert_arrays_not_equal(arr_1, arr_2)
```

<hr>

**[References]**

- [assert_arrays_equal and assert_arrays_not_equal interfaces](https://simon-ritchie.github.io/apysc/en/assert_arrays_equal_and_arrays_not_equal.html)

## `assert_defined` function docstring

JavaScript assertion interface for the defined (not undefined) value condition.<hr>

**[Parameters]**

- `value`: *
  - Target value to check.
- `msg`: str, optional
  - Message to display when assertion failed.

<hr>

**[Examples]**

```py
>>> import apysc as ap
>>> int_val: ap.Int = ap.Int(10)
>>> ap.assert_defined(int_val)
```

<hr>

**[References]**

- [assert_defined and assert_undefined interfaces](https://simon-ritchie.github.io/apysc/en/assert_defined_and_undefined.html)

## `assert_dicts_equal` function docstring

JavaScript assertion interface for the Dictionary values equal condition.<hr>

**[Parameters]**

- `left`: *
  - Left-side value to compare.
- `right`: *
  - Right-side value to compare.
- `msg`: str, optional
  - Message to display when assertion failed.
- `outer_frames_index_adjustment`: int, optional
  - The trace's outer frames index adjustment setting. This function uses this argument to adjust the caller's information. Also, this function only uses this argument in internal logic.

<hr>

**[Notes]**

This interface is used instead of assert_equal for Dictionary class comparison (JavaScript can not compare dictionary (Object) directly, like a Python, for example, `{"a": 10} === {"a": 10}` becomes false).<hr>

**[Examples]**

```py
>>> import apysc as ap
>>> dict_1: ap.Dictionary = ap.Dictionary({"a": 10})
>>> dict_2: ap.Dictionary = ap.Dictionary({"a": 10})
>>> ap.assert_dicts_equal(dict_1, dict_2)
```

<hr>

**[References]**

- [assert_dicts_equal and assert_dicts_not_equal interfaces](https://simon-ritchie.github.io/apysc/en/assert_dicts_equal_and_dicts_not_equal.html)

## `assert_dicts_not_equal` function docstring

JavaScript assertion interface for the Dictionary values not equal condition.<hr>

**[Parameters]**

- `left`: *
  - Left-side value to compare.
- `right`: *
  - Right-side value to compare.
- `msg`: str, optional
  - Message to display when assertion failed.
- `outer_frames_index_adjustment`: int, optional
  - The trace's outer frames index adjustment setting. This function uses this argument to adjust the caller's information. Also, this function only uses this argument in internal logic.

<hr>

**[Notes]**

This interface is used instead of assert_not_equal for Dictionary class comparison (JavaScript can not compare dictionary (Object) directly, like a Python, for example, `{"a": 10} !== {"a": 10}` becomes true).<hr>

**[Examples]**

```py
>>> import apysc as ap
>>> dict_1: ap.Dictionary = ap.Dictionary({"a": 10})
>>> dict_2: ap.Dictionary = ap.Dictionary({"a": 20})
>>> ap.assert_dicts_not_equal(dict_1, dict_2)
```

<hr>

**[References]**

- [assert_dicts_equal and assert_dicts_not_equal interfaces](https://simon-ritchie.github.io/apysc/en/assert_dicts_equal_and_dicts_not_equal.html)

## `assert_equal` function docstring

JavaScript assertion interface for the equal condition.<hr>

**[Parameters]**

- `left`: *
  - Left-side value to compare.
- `right`: *
  - Right-side value to compare.
- `msg`: str, optional
  - Message to display when assertion failed.

<hr>

**[Notes]**

 ・If specified values are types of Array (or list), then this interface calls the assert_arrays_equal function instead. <br> ・If specified values are types of Dictionary (or dict), then this interface calls the assert_dicts_equal instead.<hr>

**[Examples]**

```py
>>> import apysc as ap
>>> int_1: ap.Int = ap.Int(10)
>>> int_2: ap.Int = ap.Int(10)
>>> ap.assert_equal(int_1, int_2)
```

<hr>

**[References]**

- [assert_equal and assert_not_equal interfaces](https://simon-ritchie.github.io/apysc/en/assert_equal_and_not_equal.html)

## `assert_false` function docstring

JavaScript assertion interface for the false condition.<hr>

**[Parameters]**

- `value`: *
  - Target value to check.
- `type_strict`: bool, default True
  - Whether strictly check actual value or not. For example, if type_strict is True, an integer of 0 fails tests. On the contrary (if type_strict is False), an integer of 0 passes tests.
- `msg`: str, optional
  - Message to display when assertion failed.

<hr>

**[Examples]**

```py
>>> import apysc as ap
>>> int_val: ap.Int = ap.Int(10)
>>> boolean: ap.Boolean = int_val == 11
>>> ap.assert_false(boolean)
```

<hr>

**[References]**

- [assert_true and assert_false interfaces](https://simon-ritchie.github.io/apysc/en/assert_true_and_false.html)

## `assert_greater` function docstring

JavaScript assertion interface for the greater than condition.<hr>

**[Parameters]**

- `left`: Union[int, float, Int, Number]
  - Left-side (greater) value to compare.
- `right`: Union[int, float, Int, Number]
  - Right-side (less) value to compare.
- `msg`: str, optional
  - Message to display when assertion failed.

<hr>

**[Examples]**

```py
>>> import apysc as ap
>>> int_val_1: ap.Int = ap.Int(10)
>>> int_val_2: ap.Int = ap.Int(9)
>>> ap.assert_greater(left=int_val_1, right=int_val_2)
```

## `assert_greater_equal` function docstring

JavaScript assertion interface for the greater than or equal to condition.<hr>

**[Parameters]**

- `left`: Union[int, float, Int, Number]
  - Left-side (greater) value to compare.
- `right`: Union[int, float, Int, Number]
  - Right-side (less) value to compare.
- `msg`: str, optional
  - Message to display when assertion failed.

<hr>

**[Examples]**

```py
>>> import apysc as ap
>>> int_val_1: ap.Int = ap.Int(10)
>>> int_val_2: ap.Int = ap.Int(9)
>>> ap.assert_greater_equal(left=int_val_1, right=int_val_2)
>>> int_val_3: ap.Int = ap.Int(10)
>>> ap.assert_greater_equal(left=int_val_1, right=int_val_3)
```

## `assert_less` function docstring

JavaScript assertion interface for the less than condition.<hr>

**[Parameters]**

- `left`: Union[int, float, Int, Number]
  - Left-side (less) value to compare.
- `right`: Union[int, float, Int, Number]
  - Right-side (greater) value to compare.
- `msg`: str, optional
  - Message to display when assertion failed.

<hr>

**[Examples]**

```py
>>> import apysc as ap
>>> int_val_1: ap.Int = ap.Int(9)
>>> int_val_2: ap.Int = ap.Int(10)
>>> ap.assert_greater_equal(left=int_val_1, right=int_val_2)
```

## `assert_less_equal` function docstring

JavaScript assertion interface for the less than or equal to condition.<hr>

**[Parameters]**

- `left`: Union[int, float, Int, Number]
  - Left-side (less) value to compare.
- `right`: Union[int, float, Int, Number]
  - Right-side (greater) value to compare.
- `msg`: str, optional
  - Message to display when assertion failed.

<hr>

**[Examples]**

```py
>>> import apysc as ap
>>> int_val_1: ap.Int = ap.Int(9)
>>> int_val_2: ap.Int = ap.Int(10)
>>> ap.assert_greater_equal(left=int_val_1, right=int_val_2)
>>> int_val_3: ap.Int = ap.Int(9)
>>> ap.assert_greater_equal(left=int_val_1, right=int_val_3)
```

## `assert_not_equal` function docstring

JavaScript assertion interface for the not equal condition.<hr>

**[Parameters]**

- `left`: *
  - Left-side value to compare.
- `right`: *
  - Right-side value to compare.
- `msg`: str, optional
  - Message to display when assertion failed.

<hr>

**[Notes]**

 ・If specified values are types of Array (or list), then this interface calls the assert_arrays_not_equal function instead. <br> ・If specified values are types of Dictionary (or dict), this interface calls the assert_dicts_not_equal function instead.<hr>

**[Examples]**

```py
>>> import apysc as ap
>>> int_1: ap.Int = ap.Int(10)
>>> int_2: ap.Int = ap.Int(11)
>>> ap.assert_not_equal(int_1, int_2)
```

<hr>

**[References]**

- [assert_equal and assert_not_equal interfaces](https://simon-ritchie.github.io/apysc/en/assert_equal_and_not_equal.html)

## `assert_true` function docstring

JavaScript assertion interface for the true condition.<hr>

**[Parameters]**

- `value`: *
  - Target value to check.
- `type_strict`: bool, default True
  - Whether strictly check actual value or not. For example, if type_strict is True, an integer of 1 fails tests. On the contrary (if type_strict is False), an integer of 1 passes tests.
- `msg`: str, optional
  - Message to display when assertion failed.

<hr>

**[Examples]**

```py
>>> import apysc as ap
>>> int_val: ap.Int = ap.Int(10)
>>> boolean: ap.Boolean = int_val == 10
>>> ap.assert_true(boolean)
```

<hr>

**[References]**

- [assert_true and assert_false interfaces](https://simon-ritchie.github.io/apysc/en/assert_true_and_false.html)

## `assert_undefined` function docstring

JavaScript assertion interface for the undefined value condition.<hr>

**[Parameters]**

- `value`: *
  - Target value to check.
- `msg`: str, optional
  - Message to display when assertion failed.

<hr>

**[Examples]**

```py
>>> import apysc as ap
>>> int_val: ap.Int = ap.Int(10)
>>> ap.append_js_expression(expression=f"{int_val.variable_name} = undefined;")
>>> ap.assert_undefined(int_val)
```

<hr>

**[References]**

- [assert_defined and assert_undefined interfaces](https://simon-ritchie.github.io/apysc/en/assert_defined_and_undefined.html)