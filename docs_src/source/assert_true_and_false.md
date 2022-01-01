# assert_true and assert_false interfaces

This page explains the `assert_true` and `assert_false` function interfaces.

## What interfaces are these?

The `assert_true` function interface asserts a specified `Boolean` value is true. Conversely, the `assert_false` function interface asserts a specified `Boolean` value is false.

## See also

- [JavaScript assertion interface common behavior](assertion_common_behavior.md)

## Basic usage

The `assert_true` and `assert_false` interfaces requires `value` argument. The `type_strict` and `msg` arguments are optional (default value of the `type_strict` argument is `True`).

If the `type_strict` argument is `True`, the assertion will use the JavaScript strict comparison operator (`===`). For instance, if the `value` is `Int(1)` and the `type_strict` is `True`, an assertion will fail (because of the comparison between the `Boolean` and `Int`). Conversely, if the `type_strict` is `False`, `Int(1)` will pass the `assert_true` assertion.

These interfaces display an assertion result on the browser console.

The following assertion example (`assert_true` and value is the `Boolean(True)`) passes:

```py
# runnable
import apysc as ap

stage: ap.Stage = ap.Stage(
    stage_width=0, stage_height=0, background_color='#333',
    stage_elem_id='stage')

bool_1: ap.Boolean = ap.Boolean(True)
ap.assert_true(bool_1, msg='Boolean value is not True!')

ap.save_overall_html(
    dest_dir_path='assert_true_basic_usage_1/')
```

```
[assert_true]
Right-side variable name: b_3
Left value: true right value: true
```

<iframe src="static/assert_true_basic_usage_1/index.html" width="0" height="0"></iframe>

The following assertion example (`assert_true` and value is the `Boolean(False)`) fails:

```py
# runnable
import apysc as ap

stage: ap.Stage = ap.Stage(
    stage_width=0, stage_height=0, background_color='#333',
    stage_elem_id='stage')

bool_1: ap.Boolean = ap.Boolean(False)
ap.assert_true(bool_1, msg='Boolean value is not True!')

ap.save_overall_html(
    dest_dir_path='assert_true_basic_usage_2/')
```

```
[assert_true]
Right-side variable name: b_3
Left value: true right value: false
...
Assertion failed: Boolean value is not True!
```

<iframe src="static/assert_true_basic_usage_2/index.html" width="0" height="0"></iframe>

The following assertion example (`assert_true` and value is the `Int(1)` and `type_strict` is `True`) will fail:

```py
# runnable
import apysc as ap

stage: ap.Stage = ap.Stage(
    stage_width=0, stage_height=0, background_color='#333',
    stage_elem_id='stage')

int_1: ap.Int = ap.Int(1)
ap.assert_true(int_1, type_strict=True, msg='Value is not Boolean(True)!')

ap.save_overall_html(
    dest_dir_path='assert_true_basic_usage_3/')
```

```
[assert_true]
Right-side variable name: i_11
Left value: true right value: 1
...
Assertion failed: Value is not Boolean(True)!
```

<iframe src="static/assert_true_basic_usage_3/index.html" width="0" height="0"></iframe>

The following assertion example (`assert_true` and value is the `Int(1)` and `type_strict` is `False`) will pass:

```py
# runnable
import apysc as ap

stage: ap.Stage = ap.Stage(
    stage_width=0, stage_height=0, background_color='#333',
    stage_elem_id='stage')

int_1: ap.Int = ap.Int(1)
ap.assert_true(int_1, type_strict=False, msg='Value is not True!')

ap.save_overall_html(
    dest_dir_path='assert_true_basic_usage_4/')
```

```
[assert_true]
Right-side variable name: i_11
Left value: true right value: 1
```

<iframe src="static/assert_true_basic_usage_4/index.html" width="0" height="0"></iframe>

The following assertion example (`assert_false` and value is the `Boolean(False)`) passes:

```py
# runnable
import apysc as ap

stage: ap.Stage = ap.Stage(
    stage_width=0, stage_height=0, background_color='#333',
    stage_elem_id='stage')

bool_1: ap.Boolean = ap.Boolean(False)
ap.assert_false(bool_1, msg='Value is not False!')

ap.save_overall_html(
    dest_dir_path='assert_false_basic_usage_1/')
```

```
[assert_false]
Right-side variable name: b_3
Left value: false right value: false
```

<iframe src="static/assert_false_basic_usage_1/index.html" width="0" height="0"></iframe>
