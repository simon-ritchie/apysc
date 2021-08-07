# assert_dicts_equal and assert_dicts_not_equal interfaces

This page will explain the `assert_dicts_equal` and `assert_dicts_not_equal` function interfaces.

## What interfaces are these?

The `assert_dicts_equal` function interface will assert specified two dictionaries (`Dictionary` type value) are equal. Conversely, the `assert_dicts_not_equal` function interface will assert specified two dictionaries are not equal.

## See also

- [JavaScript assertion interface common behavior](assertion_common_behavior.md)

## Basic usage

Both of the `assert_dicts_equal` and `assert_dicts_not_equal` interfaces require the `expected` and `actual` arguments. The `msg` argument is optional.

The `expected` argument can specify a Python built-in `dict` value and `Dictionary` value.

The following example (`assert_dicts_equal` and values are equal) will pass:

```py
# runnable
import apysc as ap

stage: ap.Stage = ap.Stage(
    stage_width=0, stage_height=0, background_color='#333',
    stage_elem_id='stage')

dict_val: ap.Dictionary = ap.Dictionary({'a': 10, 'b': 20})
ap.assert_dicts_equal(
    expected={'a': 10, 'b': 20}, actual=dict_val,
    msg='Values are not equal!')

ap.save_overall_html(
    dest_dir_path='assert_dicts_equal_basic_usage_1/')
```

```
[assert_dicts_equal]
Expected: {a: 10, b: 20} actual: dct_1
```

<iframe src="static/assert_dicts_equal_basic_usage_1/index.html" width="0" height="0"></iframe>

The following example (`assert_dicts_equal` and values are not equal) will fail:

```py
# runnable
import apysc as ap

stage: ap.Stage = ap.Stage(
    stage_width=0, stage_height=0, background_color='#333',
    stage_elem_id='stage')

dict_val: ap.Dictionary = ap.Dictionary({'a': 10, 'b': 20})
ap.assert_dicts_equal(
    expected={'a': 30}, actual=dict_val, msg='Values are not equal!')

ap.save_overall_html(
    dest_dir_path='assert_dicts_equal_basic_usage_2/')
```

```
[assert_dicts_equal]
Expected: {a: 30} actual: dct_1
...
Assertion failed: Values are not equal!
```

<iframe src="static/assert_dicts_equal_basic_usage_2/index.html" width="0" height="0"></iframe>

The following example (`assert_dicts_not_equal` and values are not equal) will pass:

```py
# runnable
import apysc as ap

stage: ap.Stage = ap.Stage(
    stage_width=0, stage_height=0, background_color='#333',
    stage_elem_id='stage')

dict_val: ap.Dictionary = ap.Dictionary({'a': 10, 'b': 20})
ap.assert_dicts_not_equal(
    expected={'a': 30}, actual=dict_val, msg='Values are equal!')

ap.save_overall_html(
    dest_dir_path='assert_dicts_not_equal_basic_usage_1/')
```

```
[assert_dicts_not_equal]
Expected: {a: 30} actual: dct_1
```

<iframe src="static/assert_dicts_not_equal_basic_usage_1/index.html" width="0" height="0"></iframe>

## Notes for the assert_equal and assert_not_equal interfaces

If a `Dictionary` value is specified to the `assert_equal` or `assert_not_equal` interface's `actual` value, then the `assert_dicts_equal` or `assert_dicts_not_equal` interfaces will be called instead of the `assert_equal` or `assert_not_equal` interfaces automatically.

```py
# runnable
import apysc as ap

stage: ap.Stage = ap.Stage(
    stage_width=0, stage_height=0, background_color='#333',
    stage_elem_id='stage')

dict_val: ap.Dictionary = ap.Dictionary({'a': 30})
ap.assert_equal(
    expected={'a': 30}, actual=dict_val,
    msg='Values are not equal!')

ap.save_overall_html(
    dest_dir_path='assert_dicts_equal_notes_for_assert_equal/')
```

```
[assert_dicts_equal]
Expected: {a: 30} actual: dct_1
```

<iframe src="static/assert_dicts_equal_notes_for_assert_equal/index.html" width="0" height="0"></iframe>
