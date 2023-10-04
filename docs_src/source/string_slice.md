# String class slice method

This page explains the `String` class `slice` method.

## What method is this?

The `slice` method slices a string with the specified start and end indices.

## Basic usage

The `slice` method requires the `start` and `end` arguments.

The `start` argument is the starting index of slicing.

Similarly, the `end` argument is the end index of slicing, with the range being up to (but not including) this index.

```py
# runnable
import apysc as ap

stage: ap.Stage = ap.Stage(
    stage_width=0,
    stage_height=0,
    background_color=ap.Color("#333"),
    stage_elem_id="stage",
)

string: ap.String = ap.String("012345")
result_string: ap.String = string.slice(start=0)
ap.assert_equal(result_string, "012345")

result_string = string.slice(start=1)
ap.assert_equal(result_string, "12345")

result_string = string.slice(start=0, end=2)
ap.assert_equal(result_string, "01")

result_string = string.slice(start=2, end=4)
ap.assert_equal(result_string, "23")

result_string = string.slice(start=-2)
ap.assert_equal(result_string, "45")

result_string = string.slice(start=-3, end=-1)
ap.assert_equal(result_string, "34")

ap.save_overall_html(dest_dir_path="string_slice_basic_usage/")
```

<iframe src="static/string_slice_basic_usage/index.html" width="0" height="0"></iframe>

## slice method API

<!-- Docstring: apysc._type.string_slice_mixin.StringSliceMixIn.slice -->

<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>

**[Interface signature]** `slice(self, *, start: Union[int, ForwardRef('Int')], end: Union[int, ForwardRef('Int'), NoneType] = None, variable_name_suffix: str = '') -> 'String'`<hr>

**[Interface summary]**

Get a sliced string based on the specified arguments range.<hr>

**[Parameters]**

- `start`: Union[int, "Int"]
  - A start index of the slice range.
- `end`: Optional[Union[int, "Int"]], optional
  - An end index of the slice range. If this argument is not specified, this method skips the end position's slicing.
- `variable_name_suffix`: str, default ""
  - A JavaScript variable name suffix string. This setting is sometimes useful for JavaScript debugging.

<hr>

**[Returns]**

- `result`: String
  - A sliced result string.

<hr>

**[Examples]**

```py
>>> import apysc as ap
>>> stage: ap.Stage = ap.Stage(
...     stage_width=0,
...     stage_height=0,
...     background_color=ap.Color("#333"),
...     stage_elem_id="stage",
... )
>>> string: ap.String = ap.String("012345")
>>> result_string: ap.String = string.slice(start=0)
>>> result_string
String("012345")

>>> result_string = string.slice(start=1)
>>> result_string
String("12345")

>>> result_string = string.slice(start=0, end=2)
>>> result_string
String("01")

>>> result_string = string.slice(start=2, end=4)
>>> result_string
String("23")

>>> result_string = string.slice(start=-2)
>>> result_string
String("45")

>>> result_string = string.slice(start=-3, end=-1)
>>> result_string
String("34")
```