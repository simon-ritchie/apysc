# String class lstrip interface

This page explains the `String` class `lstrip` method interface.

## What interface is this?

The `lstrip` method interface removes whitespaces or a specified character(s) from a string's left edge.

## Basic usage

The `lstrip` accepts the optional `string` argument.

If you skip this argument, this interface removes whitespaces (and line breaks) from a string's left edge.

```py
# runnable
import apysc as ap

ap.Stage(
    stage_width=0,
    stage_height=0,
    background_color=ap.Color("#333"),
    stage_elem_id="stage",
)

string: ap.String = ap.String("  \n　 aabbaa  ")
string = string.lstrip()
ap.assert_equal(string, "aabbaa  ")

ap.save_overall_html(dest_dir_path="string_lstrip_basic_usage_1/")
```

<iframe src="static/string_lstrip_basic_usage_1/index.html" width="0" height="0"></iframe>

Also, if you specify any value to the `string` argument, this interface removes its character(s) from a string's left edge.

```py
# runnable
import apysc as ap

ap.Stage(
    stage_width=0,
    stage_height=0,
    background_color=ap.Color("#333"),
    stage_elem_id="stage",
)

string: ap.String = ap.String("aabbaa")
string = string.lstrip(string="a")
ap.assert_equal(string, "bbaa")

ap.save_overall_html(dest_dir_path="string_lstrip_basic_usage_2/")
```

<iframe src="static/string_lstrip_basic_usage_2/index.html" width="0" height="0"></iframe>

## lstrip API

<!-- Docstring: apysc._type.string_lstrip_mixin.StringLStripMixIn.lstrip -->

<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>

**[Interface signature]** `lstrip(self, *, string: Union[str, ForwardRef('String'), NoneType] = None, variable_name_suffix: str = '') -> 'String'`<hr>

**[Interface summary]**

Remove a specified character or string from the beginning of this value.<hr>

**[Parameters]**

- `string`: Optional[Union[str, "String"]], optional
  - A character or string to remove from the beginning of this value. If this argument is `None` (default), this method removes spaces and line breaks.
- `variable_name_suffix`: str, optional
  - A JavaScript variable name suffix string. This setting is sometimes useful for JavaScript debugging.

<hr>

**[Returns]**

- `result`: String
  - A stripped result string.

<hr>

**[Examples]**

```py
>>> import apysc as ap
>>> _ = ap.Stage()
>>> string: ap.String = ap.String("   aabbcc  ")
>>> string = string.lstrip()
>>> string
String("aabbcc  ")

>>> string = ap.String("aabbccaa")
>>> string = string.lstrip(string="a")
>>> string
String("bbccaa")
```