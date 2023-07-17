# String class rstrip interface

This page explains the `String` class `rstrip` method interface.

## What interface is this?

The `rstrip` method interface removes whitespaces or a specified character(s) from a string's right edge.

## Basic usage

The `rstrip` accepts the optional `string` argument.

If you skip this argument, this interface removes whitespaces (and line breaks) from a string's right edge.

```py
# runnable
import apysc as ap

ap.Stage(stage_width=0, stage_height=0, background_color="#333", stage_elem_id="stage")

string: ap.String = ap.String("  aabbccaa  \n ")
string = string.rstrip()
ap.assert_equal(string, "  aabbccaa")

ap.save_overall_html(dest_dir_path="string_rstrip_basic_usage_1/")
```

<iframe src="static/string_rstrip_basic_usage_1/index.html" width="0" height="0"></iframe>

Also, if you specify any value to the `string` argument, this interface removes its character(s) from a string's right edge.

```py
# runnable
import apysc as ap

ap.Stage(stage_width=0, stage_height=0, background_color="#333", stage_elem_id="stage")

string: ap.String = ap.String("aabbccaa")
string = string.rstrip(string="a")
ap.assert_equal(string, "aabbcc")

ap.save_overall_html(dest_dir_path="string_rstrip_basic_usage_2/")
```

<iframe src="static/string_rstrip_basic_usage_2/index.html" width="0" height="0"></iframe>

## rstrip API

<!-- Docstring: apysc._type.string_rstrip_mixin.StringRStripMixIn.rstrip -->

<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>

**[Interface signature]** `rstrip(self, *, string: Union[str, ForwardRef('String'), NoneType] = None, variable_name_suffix: str = '') -> 'String'`<hr>

**[Interface summary]**

Remove a specified character or string from the end of this value.<hr>

**[Parameters]**

- `string`: Optional[Union[str, "String"]], optional
  - A character or string to remove from the end of this value. If this argument is `None` (default), this method removes spaces and line breaks.
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
>>> string: ap.String = ap.String("  aabbcc   ")
>>> string = string.rstrip()
>>> string
String("  aabbcc")

>>> string = ap.String("aabbccaa")
>>> string = string.rstrip(string="a")
>>> string
String("aabbcc")
```