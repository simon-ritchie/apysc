# String class zfill method

This page explains the `String` class `zfill` method.

## What method is this?

The `zfill` method returns a zero-filled string with the specified widgth (number of total characters).

## Basic usage

The `zfill` method required the `width` argument (`int` or `ap.Int` type).

It determines the number of total characters.

A return value becomes copied `ap.String` value.

```py
# runnable

import apysc as ap

ap.Stage(
    stage_width=0,
    stage_height=0,
    background_color=ap.Color("#333"),
    stage_elem_id="stage",
)

string: ap.String = ap.String(value="1")
string = string.zfill(width=1)
ap.assert_equal(string, "1")

string = string.zfill(width=3)
ap.assert_equal(string, "001")

string = string.zfill(width=5)
ap.assert_equal(string, "00001")

ap.save_overall_html(dest_dir_path="string_zfill_basic_usage/")
```

<iframe src="static/string_zfill_basic_usage/index.html" width="0" height="0"></iframe>

## zfill method API

<!-- Docstring: apysc._type.string_zfill_mixin.StringZfillMixIn.zfill -->

<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>

**[Interface signature]** `zfill(self, *, width: Union[int, ForwardRef('Int')]) -> 'String'`<hr>

**[Interface summary]**

Return a copy of the string left filled with 0.<hr>

**[Parameters]**

- `width`: Union[int, "Int"]
  - A width (length) of the string.

<hr>

**[Returns]**

- `result`: String
  - A result string.

<hr>

**[Examples]**

```py
>>> import apysc as ap
>>> _: ap.Stage = ap.Stage()
>>> string: ap.String = ap.String("1")
>>> string = string.zfill(width=1)
>>> string
String("1")

>>> string = string.zfill(width=3)
>>> string
String("001")

>>> string = string.zfill(width=5)
>>> string
String("00001")
```