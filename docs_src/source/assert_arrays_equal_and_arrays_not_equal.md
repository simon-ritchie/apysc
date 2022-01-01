# assert_arrays_equal and assert_arrays_not_equal interfaces

This page explains the `assert_arrays_equal` and `assert_arrays_not_equal` function interfaces.

## What interfaces are these?

The `assert_arrays_equal` function interface asserts that the two arrays are equal. Conversely, the `assert_arrays_not_equal` function interface asserts that the two arrays are not equal.

## See also

- [JavaScript assertion interface common behavior](assertion_common_behavior.md)

## Basic usage

Both of the `assert_arrays_equal` and `assert_arrays_not_equal` interfaces require the `left` and `right` arguments. The `msg` argument is optional.

The arguments accept a Python built-in `list` value and `Array` value.

The following example (`assert_arrays_equal` and values are equal) passes:

```py
# runnable
import apysc as ap

stage: ap.Stage = ap.Stage(
    stage_width=0, stage_height=0, background_color='#333',
    stage_elem_id='stage')

arr_1: ap.Array = ap.Array([1, 2, 3])
ap.assert_arrays_equal(
    left=[1, 2, 3], right=arr_1, msg='Values are not equal!')

ap.save_overall_html(
    dest_dir_path='assert_arrays_equal_basic_usage_1/')
```

```
[assert_arrays_equal]
Left value: [1, 2, 3] right value: arr_2
```

<iframe src="static/assert_arrays_equal_basic_usage_1/index.html" width="0" height="0"></iframe>

The following example (`assert_arrays_equal` and values are not equal) fails:

```py
# runnable
import apysc as ap

stage: ap.Stage = ap.Stage(
    stage_width=0, stage_height=0, background_color='#333',
    stage_elem_id='stage')

arr_1: ap.Array = ap.Array([1, 2, 3])
ap.assert_arrays_equal(
    left=[1, 2], right=arr_1, msg='Values are not equal!')

ap.save_overall_html(
    dest_dir_path='assert_arrays_equal_basic_usage_2/')
```

```
[assert_arrays_equal]
Left value: [1, 2] right value: arr_2
...
Assertion failed: Values are not equal!
```

<iframe src="static/assert_arrays_equal_basic_usage_2/index.html" width="0" height="0"></iframe>

The following example (`assert_arrays_not_equal` and values are not equal) passes:

```py
# runnable
import apysc as ap

stage: ap.Stage = ap.Stage(
    stage_width=0, stage_height=0, background_color='#333',
    stage_elem_id='stage')

arr_1: ap.Array = ap.Array([1, 2, 3])
ap.assert_arrays_not_equal(
    left=[1, 2], right=arr_1, msg='Values are equal!')

ap.save_overall_html(
    dest_dir_path='assert_arrays_not_equal_basic_usage_1/')
```

<iframe src="static/assert_arrays_not_equal_basic_usage_1/index.html" width="0" height="0"></iframe>

## Notes for the assert_equal and assert_not_equal interfaces

If an `Array` value is specified to the `assert_equal` or `assert_not_equal` interface's values, then the `assert_arrays_equal` or `assert_arrays_not_equal` interfaces will be called instead of the `assert_equal` or `assert_not_equal` interfaces automatically.

```py
# runnable
import apysc as ap

stage: ap.Stage = ap.Stage(
    stage_width=0, stage_height=0, background_color='#333',
    stage_elem_id='stage')

arr_1: ap.Array = ap.Array([1, 2, 3, 4, 5])
ap.assert_equal(
    left=[1, 2, 3, 4, 5], right=arr_1, msg='Values are equal!')

ap.save_overall_html(
    dest_dir_path='assert_arrays_equal_notes_for_the_assert_equal/')
```

```
[assert_arrays_equal]
Left value: [1, 2, 3, 4, 5] right value: arr_2
```

<iframe src="static/assert_arrays_equal_notes_for_the_assert_equal/index.html" width="0" height="0"></iframe>
