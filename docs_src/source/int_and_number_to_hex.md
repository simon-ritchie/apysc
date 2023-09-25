# Int and Number classes to_hex method

This page explains the `Int` and `Number` classes `to_hex` method.

## What method is this?

The `to_hex` method returns a hexadecimal string (e.g., "1f") from an `ap.Int` or `ap.Number` value.

## Note for `ap.Number` value

If you use this method with an `ap.Number` value, this method ignores floating-point number.

## Basic usage

The `to_hex` method requires no arguments.

This method returns a hexadecimal string (`ap.String` type value).

```py
# runnable

import apysc as ap

ap.Stage(
    stage_width=0,
    stage_height=0,
    background_color=ap.Color("#333"),
    stage_elem_id="stage",
)
int_value: ap.Int = ap.Int(28)
hex_str: ap.String = int_value.to_hex()
ap.assert_equal(hex_str, "1c")

number: ap.Number = ap.Number(28.5)
hex_str = int_value.to_hex()
ap.assert_equal(hex_str, "1c")

ap.save_overall_html(dest_dir_path="int_and_number_to_hex_basic_usage/")
```

<iframe src="static/to_fixed_basics_usage/index.html" width="0" height="0"></iframe>

## to_hex method API

<!-- Docstring: apysc._type.to_hex_mixin.ToHexMixIn.to_hex -->

<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>

**[Interface signature]** `to_hex(self, *, variable_name_suffix: str = '') -> apysc._type.string.String`<hr>

**[Interface summary]**

Get a hexadecimal string (e.g., "1f").<hr>

**[Parameters]**

- `variable_name_suffix`: str, default ''
  - A JavaScript variable name suffix string. This setting is sometimes useful for JavaScript debugging.

<hr>

**[Returns]**

- `hex_str`: String
  - A hexadecimal string (e.g., "1f").

<hr>

**[Notes]**

This method ignores floating point numbers.<hr>

**[Examples]**

```py
>>> import apysc as ap
>>> int_value: ap.Int = ap.Int(28)
>>> hex_str: ap.String = int_value.to_hex()
>>> hex_str
String("1c")

>>> number: ap.Number = ap.Number(28.5)
>>> hex_str = int_value.to_hex()
>>> hex_str
String("1c")
```