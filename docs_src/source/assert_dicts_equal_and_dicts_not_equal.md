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


## assert_dicts_equal API

<!-- Docstring: apysc._console.assertion.assert_dicts_equal -->

<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>

**[Interface signature]** `assert_dicts_equal(left:Any, right:Any, *, msg:str='') -> None`<hr>

**[Interface summary]** JavaScript assertion interface for Dictionary values equal condition.<hr>

**[Parameters]**

- `left`: *
  - Left-side value to compare.
- `right`: *
  - Right-side value to compare.
- `msg`: str, optional
  - Message to display when assertion failed.

<hr>

**[Notes]**

This interface is used instead of assert_equal for Dictionary class comparison (JavaScript can not compare dictionary (Object) directly, like a Python, for example, `{"a": 10} === {"a": 10}` becomes false).<hr>

**[Examples]**

```py
>>> import apysc as ap
>>> dict_1: ap.Dictionary = ap.Dictionary({'a': 10})
>>> dict_2: ap.Dictionary = ap.Dictionary({'a': 10})
>>> ap.assert_dicts_equal(dict_1, dict_2)
```

## assert_dicts_not_equal API

<!-- Docstring: apysc._console.assertion.assert_dicts_not_equal -->

<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>

**[Interface signature]** `assert_dicts_not_equal(left:Any, right:Any, *, msg:str='') -> None`<hr>

**[Interface summary]** JavaScript assertion interface for Dictionary values not equal condition.<hr>

**[Parameters]**

- `left`: *
  - Left-side value to compare.
- `right`: *
  - Right-side value to compare.
- `msg`: str, optional
  - Message to display when assertion failed.

<hr>

**[Notes]**

This interface is used instead of assert_not_equal for Dictionary class comparison (JavaScript can not compare dictionary (Object) directly, like a Python, for example, `{"a": 10} !== {"a": 10}` becomes true).<hr>

**[Examples]**

```py
>>> import apysc as ap
>>> dict_1: ap.Dictionary = ap.Dictionary({'a': 10})
>>> dict_2: ap.Dictionary = ap.Dictionary({'a': 20})
>>> ap.assert_dicts_not_equal(dict_1, dict_2)
```