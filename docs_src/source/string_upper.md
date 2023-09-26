# String class upper method

This page explains the `String` class `upper` method.

## What method is this?

The `upper` method returns a copied uppercase string.

## Basic usage

The `upper` method requires no arguments and it returns a `ap.String` type value.

```py
# runnable

import apysc as ap

ap.Stage(
    stage_width=0,
    stage_height=0,
    background_color=ap.Color("#333"),
    stage_elem_id="stage",
)
string: ap.String = ap.String("aBc1_")
string = string.upper()
ap.assert_equal(string, "ABC1_")

ap.save_overall_html(dest_dir_path="string_upper_basic_usage/")
```

<iframe src="static/string_upper_basic_usage/index.html" width="0" height="0"></iframe>

## upper method API

<!-- Docstring: apysc._type.string_upper_mixin.StringUpperMixIn.upper -->

<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>

**[Interface signature]** `upper(self) -> 'String'`<hr>

**[Interface summary]**

Get a copied upper case string.<hr>

**[Returns]**

- `string`: String
  - A copied upper case string.

<hr>

**[Examples]**

```py
>>> import apysc as ap
>>> string: ap.String = ap.String("Hello")
>>> string = string.upper()
>>> string
String("HELLO")
```