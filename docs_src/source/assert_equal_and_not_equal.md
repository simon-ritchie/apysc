# assert_equal and assert_not_equal interfaces

This page will explain the `assert_equal` and `assert_not_equal` function interfaces.

## What interfaces are these?

The `assert_equal` function interface will assert two JavaScript values are equal. The `assert_not_equal` function interface will assert two JavaScript values are not equal.

## See also

- [JavaScript assertion interface common behavior](assertion_common_behavior.md)

## Basic usage

The `assert_equal` and `assert_not_equal` interfaces requires the `expected` and `actual` arguments. The `msg` argument is optional.

If an `expected` value and `actual` values are not the same, the `assert_equal` assertion will fail and display an error message on the browser console:

```py
# runnable
import apysc as ap

stage: ap.Stage = ap.Stage(
    stage_width=0, stage_height=0, background_color='#333',
    stage_elem_id='stage')

int_1: ap.Int = ap.Int(10)
ap.assert_equal(expected=11, actual=int_1, msg='Values are not equal!')

ap.save_overall_html(
    dest_dir_path='assert_equal_basic_usage/')
```

```
[assert_equal]
Actual variable name: i_11
Expected: 11 actual: 10
...
Assertion failed: Values are not equal!
```

<iframe src="static/assert_equal_basic_usage/index.html" width="0" height="0"></iframe>

The `assert_not_equal` interface has the same arguments and if an `expected` value and `actual` value are the same values, an assertion will fail:

```py
# runnable
import apysc as ap

stage: ap.Stage = ap.Stage(
    stage_width=0, stage_height=0, background_color='#333',
    stage_elem_id='stage')

int_1: ap.Int = ap.Int(10)
ap.assert_not_equal(expected=10, actual=int_1, msg='Values are equal!')

ap.save_overall_html(
    dest_dir_path='assert_not_equal_basic_usage/')
```

```
[assert_not_equal]
Actual variable name: i_11
Expected: 10 actual: 10
...
Assertion failed: Values are equal!
```

<iframe src="static/assert_not_equal_basic_usage/index.html" width="0" height="0"></iframe>
