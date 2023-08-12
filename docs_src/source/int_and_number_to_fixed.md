# Int and Number classes to_fixed interface

This page explains the `Int` and `Number` classes `to_fixed` method interface.

## What interface is this?

The `to_fixed` method converts a number to a fixed floating-point string notation.

## Basic usage

The `to_fixed` method requires a `digits` argument.

Its argument accepts between 0 to 100 range value.

If you specify 0 to the `digits` argument, a result string becomes an integer string.

Also, if you set 2 to the `digits` argument, a result string becomes a number with two decimal places string (e.g., 10.34).

This interface reflects even rounding to a truncated floating-point number.

For example, if a number is 10.678, and a `digits` argument is 2, a result string becomes 10.68.

```py
# runnable
import apysc as ap

ap.Stage(
    stage_width=0,
    stage_height=0,
    background_color=ap.Color("#333"),
    stage_elem_id="stage",
)
num: ap.Number = ap.Number(10.789)
fixed_float_str: ap.String = num.to_fixed(digits=2)
ap.assert_equal(fixed_float_str, "10.79")

fixed_float_str = num.to_fixed(digits=5)
ap.assert_equal(fixed_float_str, "10.78900")

fixed_float_str = num.to_fixed(digits=0)
ap.assert_equal(fixed_float_str, "11")

ap.save_overall_html(dest_dir_path="to_fixed_basics_usage/")
```

<iframe src="static/to_fixed_basics_usage/index.html" width="0" height="0"></iframe>

## to_fixed API

<!-- Docstring: apysc._type.to_fixed_mixin.ToFixedMixIn.to_fixed -->

<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>

**[Interface signature]** `to_fixed(self, *, digits: Union[int, ForwardRef('Int')], variable_name_suffix: str = '') -> apysc._type.string.String`<hr>

**[Interface summary]**

Convert value to fixed floating point string notation.<hr>

**[Parameters]**

- `digits`: int or Int
  - A floating point digit number (0 to 100 value is acceptable).
- `variable_name_suffix`: str, optional
  - A JavaScript variable name suffix string. This setting is sometimes useful for JavaScript debugging.

<hr>

**[Returns]**

- `result_str`: String
  - A converted string.

<hr>

**[Examples]**

```py
>>> import apysc as ap
>>> _ = ap.Stage()
>>> num: ap.Number = ap.Number(10.789)
>>> fixed_float_str: ap.String = num.to_fixed(digits=2)
>>> fixed_float_str
String("10.79")

>>> fixed_float_str = num.to_fixed(digits=5)
>>> fixed_float_str
String("10.78900")

>>> fixed_float_str = num.to_fixed(digits=0)
>>> fixed_float_str
String("11")
```