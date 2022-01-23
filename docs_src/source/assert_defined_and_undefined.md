# assert_defined and assert_undefined interfaces

This page explains the `assert_defined` and `assert_undefined` function interfaces.

## What interfaces are these?

The `assert_defined` function interface asserts specified value is defined (initialized). Conversely, the `assert_undefined` function interface asserts specified value is undefined (not initialized or deleted).

## See also

- [JavaScript assertion interface basic behavior](assertion_basic_behavior.md)

## Basic usage

Both of the `assert_defined` and `assert_undefined` interfaces requires `value` argument and `msg` argument is optional.

The following assertion example (`assert_defined` and initialized value) passes:

```py
# runnable
import apysc as ap

stage: ap.Stage = ap.Stage(
    stage_width=0, stage_height=0, background_color='#333',
    stage_elem_id='stage')

int_val: ap.Int = ap.Int(10)
ap.assert_defined(
    value=int_val, msg='Value is not defined!')

ap.save_overall_html(
    dest_dir_path='assert_defined_basic_usage_1/')
```

```
[assert_defined]
Right-side variable name: i_11
Left value: other than undefined right value: 10
```

<iframe src="static/assert_defined_basic_usage_1/index.html" width="0" height="0"></iframe>

The following assertion example (`assert_defined` and the deleted value) fails:

```py
# runnable
import apysc as ap

stage: ap.Stage = ap.Stage(
    stage_width=0, stage_height=0, background_color='#333',
    stage_elem_id='stage')

int_val: ap.Int = ap.Int(10)
ap.append_js_expression(
    expression=f'{int_val.variable_name} = undefined;')
ap.assert_defined(
    value=int_val, msg='Value is not defined!')

ap.save_overall_html(
    dest_dir_path='assert_defined_basic_usage_2/')
```

```
[assert_defined]
Right-side variable name: i_11
Left value: other than undefined right value: undefined
...
Assertion failed: Value is not defined!
```

<iframe src="static/assert_defined_basic_usage_2/index.html" width="0" height="0"></iframe>

The following assertion example (`assert_undefined` and the deleted value) passes:

```py
# runnable
import apysc as ap

stage: ap.Stage = ap.Stage(
    stage_width=0, stage_height=0, background_color='#333',
    stage_elem_id='stage')

int_val: ap.Int = ap.Int(10)
ap.append_js_expression(
    expression=f'{int_val.variable_name} = undefined;')
ap.assert_undefined(
    value=int_val, msg='Value is defined!')

ap.save_overall_html(
    dest_dir_path='assert_undefined_basic_usage_1/')
```

```
[assert_undefined]
Right-side variable name: i_11
Left value: undefined right value: undefined
```

<iframe src="static/assert_undefined_basic_usage_1/index.html" width="0" height="0"></iframe>