# assert_equal and assert_not_equal interfaces

This page explains the `assert_equal` and `assert_not_equal` function interfaces.

## What interfaces are these?

The `assert_equal` function interface asserts that two JavaScript values are equal. The `assert_not_equal` function interface asserts that the two JavaScript values are not equal.

## See also

- [JavaScript assertion interface basic behavior](assertion_basic_behavior.md)

## Basic usage

The `assert_equal` and `assert_not_equal` interfaces requires the `left` and `right` arguments. The `msg` argument is optional.

If the `left` value and `right` values are not the same, the `assert_equal` assertion fails and display an error message on the browser console:

```py
# runnable
import apysc as ap

stage: ap.Stage = ap.Stage(
    stage_width=0, stage_height=0, background_color='#333',
    stage_elem_id='stage')

int_1: ap.Int = ap.Int(10)
ap.assert_equal(left=11, right=int_1, msg='Values are not equal!')

ap.save_overall_html(
    dest_dir_path='assert_equal_basic_usage/')
```

```
[assert_equal]
Left-side variable name: i_11
Left value: 11 right value: 10
...
Assertion failed: Values are not equal!
```

<iframe src="static/assert_equal_basic_usage/index.html" width="0" height="0"></iframe>

The `assert_not_equal` interface has the same arguments, and if the `left` value and `right` value are the same values, an assertion fails:

```py
# runnable
import apysc as ap

stage: ap.Stage = ap.Stage(
    stage_width=0, stage_height=0, background_color='#333',
    stage_elem_id='stage')

int_1: ap.Int = ap.Int(10)
ap.assert_not_equal(left=10, right=int_1, msg='Values are equal!')

ap.save_overall_html(
    dest_dir_path='assert_not_equal_basic_usage/')
```

```
[assert_not_equal]
Right-side variable name: i_11
Left value: 10 right value: 10
...
Assertion failed: Values are equal!
```

<iframe src="static/assert_not_equal_basic_usage/index.html" width="0" height="0"></iframe>


## assert_equal API

<!-- Docstring: apysc._console.assertion.assert_equal -->

<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>

**[Interface signature]** `assert_equal(left:Any, right:Any, *, msg:str='') -> None`<hr>

**[Interface summary]** JavaScript assertion interface for equal condition.<hr>

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

## assert_not_equal API

<!-- Docstring: apysc._console.assertion.assert_not_equal -->

<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>

**[Interface signature]** `assert_not_equal(left:Any, right:Any, *, msg:str='') -> None`<hr>

**[Interface summary]** JavaScript assertion interface for not equal condition.<hr>

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