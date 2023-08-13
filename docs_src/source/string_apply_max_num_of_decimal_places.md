# String class apply_max_num_of_decimal_places interface

This page explains the `String` class `apply_max_num_of_decimal_places` method interface.

## What interface is this?

The `apply_max_num_of_decimal_places` method applies the maximum number of decimal places to a string.

For instance, if a string is `123.45678` and the maximum number of decimal places is `3`, this interface returns `123.456`.

If a string is not in float format, this interface returns the original string.

## Basic usage

The `apply_max_num_of_decimal_places` method requires the `max_num_of_decimal_places` (maximum number of decimal places, `int` or `Int` type) argument.

And this interface returns a new `String` instance.

```py
# runnable
import apysc as ap

ap.Stage(
    stage_width=0,
    stage_height=0,
    background_color=ap.Color("#333"),
    stage_elem_id="stage",
)

string = ap.String("123.456")
string = string.apply_max_num_of_decimal_places(max_num_of_decimal_places=1)
ap.assert_equal(string, "123.4")

# If a string is not a `float` value, this interface returns
# the original string.
string = ap.String("abc")
string = string.apply_max_num_of_decimal_places(max_num_of_decimal_places=1)
ap.assert_equal(string, "abc")

ap.save_overall_html(
    dest_dir_path="string_apply_max_num_of_decimal_places_basic_usage_1/"
)
```

<iframe src="static/string_apply_max_num_of_decimal_places_basic_usage_1/index.html" width="0" height="0"></iframe>

## apply_max_num_of_decimal_places API

<!-- Docstring: apysc._type.string_apply_max_num_of_decimal_places_mixin.StringApplyMaxNumOfDecimalPlacesMixIn.apply_max_num_of_decimal_places -->

<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>

**[Interface signature]** `apply_max_num_of_decimal_places(self, *, max_num_of_decimal_places: Union[int, ForwardRef('Int')], variable_name_suffix: str = '') -> 'String'`<hr>

**[Interface summary]**

Apply a maximum number of decimal places limit to this string.<hr>

**[Parameters]**

- `max_num_of_decimal_places`: Union[int, Int]
  - A maximum number of decimal places.
- `variable_name_suffix`: str, optional
  - A JavaScript variable name suffix string. This setting is sometimes useful for JavaScript debugging.

<hr>

**[Returns]**

- `string`: String
  - An applied string.

<hr>

**[Examples]**

```py
>>> import apysc as ap
>>> _ = ap.Stage()
>>> string = ap.String("123.456")
>>> string = string.apply_max_num_of_decimal_places(max_num_of_decimal_places=1)
>>> ap.assert_equal(string, "123.4")
```