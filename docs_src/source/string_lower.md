# String class lower method

This page explains the `String` class `lower` method.

## What method is this?

The `lower` method returns a copied lowercase string.

## Basic usage

The `lower` method requires no arguments and it returns a `ap.String` type value.

```py
# runnable

import apysc as ap

ap.Stage(
    stage_width=0,
    stage_height=0,
    background_color=ap.Color("#333"),
    stage_elem_id="stage",
)
string: ap.String = ap.String("AbC1_")
ap.assert_equal(string, "abc1_")

ap.save_overall_html(dest_dir_path="string_lower_basic_usage/")
```

<iframe src="static/string_lower_basic_usage/index.html" width="0" height="0"></iframe>

## lower method API

<!-- Docstring: apysc._type.string_lower_mixin.StringLowerMixIn.lower -->

<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>

**[Interface signature]** `lower(self) -> 'String'`<hr>

**[Interface summary]**

Get a copied lower case string.<hr>

**[Returns]**

- `string`: String
  - A copied lower case string.

<hr>

**[Examples]**

```py
>>> import apysc as ap
>>> string: ap.String = ap.String("HELLO")
>>> string = string.lower()
>>> string
String("hello")
```