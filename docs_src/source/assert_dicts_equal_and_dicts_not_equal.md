# assert_dicts_equal and assert_dicts_not_equal interfaces

This page explains the `assert_dicts_equal` and `assert_dicts_not_equal` function interfaces.

## What interfaces are these?

The `assert_dicts_equal` function interface asserts specified two dictionaries (`Dictionary` type value) are equal. Conversely, the `assert_dicts_not_equal` function interface asserts specified two dictionaries are not equal.

## See also

- [JavaScript assertion interface basic behavior](assertion_basic_behavior.md)

## Basic usage

Both of the `assert_dicts_equal` and `assert_dicts_not_equal` interfaces require the `left` and `right` arguments. The `msg` argument is optional.

You can specify a Python built-in `dict` and `Dictionary` values to these arguments.

The following example (`assert_dicts_equal` and values are equal) passes:

```py
# runnable
import apysc as ap

stage: ap.Stage = ap.Stage(
    stage_width=0, stage_height=0, background_color='#333',
    stage_elem_id='stage')

dict_val: ap.Dictionary = ap.Dictionary({'a': 10, 'b': 20})
ap.assert_dicts_equal(
    left={'a': 10, 'b': 20}, right=dict_val,
    msg='Values are not equal!')

ap.save_overall_html(
    dest_dir_path='assert_dicts_equal_basic_usage_1/')
```

```
[assert_dicts_equal]
Left value: {a: 10, b: 20} right value: dct_1
```

<iframe src="static/assert_dicts_equal_basic_usage_1/index.html" width="0" height="0"></iframe>

The following example (`assert_dicts_equal` and values are not equal)  fails:

```py
# runnable
import apysc as ap

stage: ap.Stage = ap.Stage(
    stage_width=0, stage_height=0, background_color='#333',
    stage_elem_id='stage')

dict_val: ap.Dictionary = ap.Dictionary({'a': 10, 'b': 20})
ap.assert_dicts_equal(
    left={'a': 30}, right=dict_val, msg='Values are not equal!')

ap.save_overall_html(
    dest_dir_path='assert_dicts_equal_basic_usage_2/')
```

```
[assert_dicts_equal]
Left value: {a: 30} right value: dct_1
...
Assertion failed: Values are not equal!
```

<iframe src="static/assert_dicts_equal_basic_usage_2/index.html" width="0" height="0"></iframe>

The following example (`assert_dicts_not_equal` and values are not equal) passes:

```py
# runnable
import apysc as ap

stage: ap.Stage = ap.Stage(
    stage_width=0, stage_height=0, background_color='#333',
    stage_elem_id='stage')

dict_val: ap.Dictionary = ap.Dictionary({'a': 10, 'b': 20})
ap.assert_dicts_not_equal(
    left={'a': 30}, right=dict_val, msg='Values are equal!')

ap.save_overall_html(
    dest_dir_path='assert_dicts_not_equal_basic_usage_1/')
```

```
[assert_dicts_not_equal]
Left value: {a: 30} right value: dct_1
```

<iframe src="static/assert_dicts_not_equal_basic_usage_1/index.html" width="0" height="0"></iframe>

## Notes for the assert_equal and assert_not_equal interfaces

If a `Dictionary` value is specified to the `assert_equal` or `assert_not_equal` interface's argument value, then the `assert_dicts_equal` or `assert_dicts_not_equal` interfaces will be called instead of the `assert_equal` or `assert_not_equal` interfaces automatically.

```py
# runnable
import apysc as ap

stage: ap.Stage = ap.Stage(
    stage_width=0, stage_height=0, background_color='#333',
    stage_elem_id='stage')

dict_val: ap.Dictionary = ap.Dictionary({'a': 30})
ap.assert_equal(
    left={'a': 30}, right=dict_val,
    msg='Values are not equal!')

ap.save_overall_html(
    dest_dir_path='assert_dicts_equal_notes_for_assert_equal/')
```

```
[assert_dicts_equal]
Left value: {a: 30} right value: dct_1
```

<iframe src="static/assert_dicts_equal_notes_for_assert_equal/index.html" width="0" height="0"></iframe>
