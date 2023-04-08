# to_string interface

This page explains the `to_string` method interface.

## What interface is this?

The `to_string` method returns a `String` representation of itself.

This interface exists on each basic data class, such as the `Int`, `Number`,  `Boolean`, or `Array`.

## Basic usage

The `to_string` method requires no arguments.

A result value becomes a JavaScript-based value.

For instance, a `Boolean` value becomes `true` or `false`, not `True` or `False`.

```py
# runnable
import apysc as ap

stage: ap.Stage = ap.Stage(
    background_color="#333", stage_width=0, stage_height=0, stage_elem_id="stage"
)
int_value: ap.Int = ap.Int(100)
string: ap.String = int_value.to_string()
ap.assert_equal(string, "100")

number_value: ap.Number = ap.Number(10.5)
string = number_value.to_string()
ap.assert_equal(string, "10.5")

bool_value: ap.Boolean = ap.Boolean(True)
string = bool_value.to_string()
ap.assert_equal(string, "true")

array_value: ap.Array = ap.Array([10, 20, 30])
string = array_value.to_string()
ap.assert_equal(string, "10,20,30")

ap.save_overall_html(dest_dir_path="to_string_basic_usage_1/")
```

<iframe src="static/to_string_basic_usage_1/index.html" width="0" height="0"></iframe>

Sometimes this method becomes useful when using text-related interfaces with its string.

```py
# runnable
import apysc as ap

stage: ap.Stage = ap.Stage(
    background_color="#333", stage_width=300, stage_height=50, stage_elem_id="stage"
)
width: ap.Int = ap.Int(50)
text: ap.SVGText = ap.SVGText(
    text=ap.String("width is: ") + width.to_string(),
    fill_color="#aaa",
    x=20,
    y=30,
)
ap.save_overall_html(dest_dir_path="to_string_basic_usage_2/")
```

<iframe src="static/to_string_basic_usage_2/index.html" width="300" height="50"></iframe>

## to_string method API

<!-- Docstring: apysc._type.to_string_mixin.ToStringMixIn.to_string -->

<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>

**[Interface signature]** `to_string(self) -> apysc._type.string.String`<hr>

**[Interface summary]**

Convert this instance to a string.<hr>

**[Returns]**

- `string`: String
  - A converted string.

<hr>

**[Examples]**

```py
>>> import apysc as ap
>>> stage: ap.Stage = ap.Stage(
...     background_color="#333", stage_width=200, stage_height=200
... )
>>> int_value: ap.Int = ap.Int(value=100)
>>> string: ap.String = int_value.to_string()
>>> ap.assert_equal(string, "100")
```