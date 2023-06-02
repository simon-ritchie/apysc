# String class strip interface

This page explains the `String` class `strip` method interface.

## What interface is this?

The `strip` method interface removes whitespaces or specified character(s) from a string's beginning and end edges.

## Basic usage

The `strip` method accepts the optional `string` argument.

If you skip this argument, this interface removes whitespaces (and line breaks) from a string's beginning and end edges.

```py
# runnable
import apysc as ap

ap.Stage(stage_width=0, stage_height=0, background_color="#333", stage_elem_id="stage")

string: ap.String = ap.String("  \n  aabbaa  ")
string = string.lstrip()
ap.assert_equal(string, "aabbaa")

ap.save_overall_html(dest_dir_path="string_strip_basic_usage_1/")
```

<iframe src="static/string_strip_basic_usage_1/index.html" width="0" height="0"></iframe>

Also, if you specify any value to the `string` argument, this interface removes its character(s) from a string's beginning and end edges.

```py
# runnable
import apysc as ap

ap.Stage(stage_width=0, stage_height=0, background_color="#333", stage_elem_id="stage")

string: ap.String = ap.String("aabbccaa")
string = string.strip(string="a")
ap.assert_equal(string, "bbcc")

ap.save_overall_html(dest_dir_path="string_strip_basic_usage_2/")
```

<iframe src="static/string_strip_basic_usage_2/index.html" width="0" height="0"></iframe>

## strip API

<!-- Docstring: apysc._type.string_strip_mixin.StringStripMixIn.strip -->

<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>

**[Interface signature]** `strip(self, *, string: Union[str, ForwardRef('String'), NoneType] = None, variable_name_suffix: str = '') -> 'String'`<hr>

**[Interface summary]**

Remove a specified character or string from left- and right-edges.<hr>

**[Parameters]**

- `string`: Optional[Union[str, "String"]], optional
  - A character or string to remove from the beginning and end of the this value. If this argument is `None` (default), this method removes spaces and line breaks.
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
>>> string: ap.String = ap.String("   aabbcc   ")
>>> string = string.strip()
>>> string
String("aabbcc")

>>> string = ap.String("aabbccaa")
>>> string = string.strip(string="a")
>>> string
String("bbcc")
```