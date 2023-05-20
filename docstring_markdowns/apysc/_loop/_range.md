# `apysc._loop._range` docstrings

## Module summary

The implementation for the `range` function.

## `_create_double_args_case_arr` function docstring

Create a double arguments case array.<hr>

**[Parameters]**

- `start`: Int
  - A start position argument.
- `end`: Int
  - An end position argument.

<hr>

**[Returns]**

- `arr`: Array[Int]
  - A created array of integers.

## `_create_single_arg_case_arr` function docstring

Create a single argument case array.<hr>

**[Parameters]**

- `end`: Int
  - An end position argument.

<hr>

**[Returns]**

- `arr`: Array[Int]
  - A created array of integers.

## `_create_triple_args_case_arr` function docstring

Create a triple arguments case array.<hr>

**[Parameters]**

- `start`: Int
  - A start position argument.
- `end`: Int
  - An end position argument.
- `step`: Int
  - A step number argument.

<hr>

**[Returns]**

- `arr`: Array[Int]
  - A created array of integers.

## `range` function docstring

Create a range array of integers.<hr>

**[Returns]**

- `arr`: Array[Int]
  - A created array.

<hr>

**[Examples]**

```py
>>> import apysc as ap
>>> range_arr: ap.Array[ap.Int] = ap.range(5)
>>> ap.assert_equal(range_arr, [0, 1, 2, 3, 4])
>>> range_arr = ap.range(2, 4)
>>> ap.assert_equal(range_arr, [2, 3])
>>> range_arr = ap.range(2, 10, 2)
>>> ap.assert_equal(range_arr, [2, 4, 6, 8])
```

<hr>

**[References]**

- [range function](https://simon-ritchie.github.io/apysc/en/range.html)