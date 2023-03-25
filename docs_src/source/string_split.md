# String class split interface

This page explains the `String` class `split` method interface.

## What interface is this?

The `split` method interface splits a string into an `Array` instance of `String`s.

## Basic usage

The `split` method requires the `sep` `String` argument as a separator.

```py
# runnable
import apysc as ap

ap.Stage(stage_width=0, stage_height=0, background_color="#333", stage_elem_id="stage")

str_value: ap.String = ap.String("Lorem ipsum dolor sit")
splitted_strs: ap.Array[ap.String] = str_value.split(sep=ap.String(" "))
ap.assert_arrays_equal(splitted_strs, ["Lorem", "ipsum", "dolor", "sit"])

ap.save_overall_html(dest_dir_path="string_split_basic_usage/")
```

<iframe src="static/string_split_basic_usage/index.html" width="0" height="0"></iframe>

## split API

<!-- Docstring: apysc._type.string_split_mixin.StringSplitMixIn.split -->

<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>

**[Interface signature]** `split(self, *, sep: 'String') -> 'Array[String]'`<hr>

**[Interface summary]**

Split a current string with a separator string.<hr>

**[Parameters]**

- `sep`: String
  - A separator string.

<hr>

**[Returns]**

- `splitted_strs`: Array[String]
  - A splitted strings' array.

<hr>

**[Examples]**

```py
>>> import apysc as ap
>>> str_value: ap.String = ap.String("Lorem ipsum dolor sit")
>>> splitted_strs: ap.Array[ap.String] = str_value.split(sep=ap.String(" "))
>>> ap.assert_arrays_equal(splitted_strs, ["Lorem", "ipsum", "dolor", "sit"])
```