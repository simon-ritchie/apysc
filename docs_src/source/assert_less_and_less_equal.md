# assert_less and assert_less_equal interfaces

This page explains the `assert_less` and `assert_less_equal` function interfaces.

## What interfaces are these?

The `assert_less` function interface asserts a specified first value is less than a specified second value.

Similarly, the `assert_less_equal` function interface asserts a specified first value is less than or equal to a specified second value.

## See also

- [JavaScript assertion interface basic behavior](assertion_basic_behavior.md)

## Basic usage

The `assert_less` and `assert_less_equal` interfaces require the `left` and `right` arguments.

These arguments only accept numeric values, such as the Python built-in `int`, `float`, apysc `Int`, or `Number` value.

The `msg` argument is optional.

This interface displays a specified `msg` (message) argument to the browser console when an assertion fails.

```py
# runnable
import apysc as ap

stage: ap.Stage = ap.Stage(
    stage_width=0, stage_height=0, background_color="#333", stage_elem_id="stage"
)
int_val_1: ap.Int = ap.Int(10)
int_val_2: ap.Int = ap.Int(9)
ap.assert_less(left=int_val_1, right=int_val_2, msg="Assertion failed")

ap.assert_less_equal(left=int_val_1, right=10, msg="Assertion failed")

ap.save_overall_html(dest_dir_path="assert_less_and_less_equal_basic_usage_1/")
```

<iframe src="static/assert_less_and_less_equal_basic_usage_1/index.html" width="0" height="0"></iframe>

The following example fails an assertion and displays the `Assertion failed` message on the browser console:

```py
# runnable
import apysc as ap

stage: ap.Stage = ap.Stage(
    stage_width=0, stage_height=0, background_color="#333", stage_elem_id="stage"
)
int_val_1: ap.Int = ap.Int(9)
int_val_2: ap.Int = ap.Int(9)
ap.assert_less(left=int_val_1, right=int_val_2, msg="Assertion failed")

ap.save_overall_html(dest_dir_path="assert_less_and_less_equal_basic_usage_2/")
```

<iframe src="static/assert_less_and_less_equal_basic_usage_2/index.html" width="0" height="0"></iframe>

## assert_less API

<!-- Docstring: apysc._console.assertion.assert_less -->

<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>

**[Interface signature]** `assert_less(left: Union[int, float, apysc._type.int.Int, apysc._type.number.Number], right: Union[int, float, apysc._type.int.Int, apysc._type.number.Number], *, msg: str = '') -> None`<hr>

**[Interface summary]**

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

## assert_less_equal API

<!-- Docstring: apysc._console.assertion.assert_less_equal -->

<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>

**[Interface signature]** `assert_less_equal(left: Union[int, float, apysc._type.int.Int, apysc._type.number.Number], right: Union[int, float, apysc._type.int.Int, apysc._type.number.Number], *, msg: str = '') -> None`<hr>

**[Interface summary]**

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