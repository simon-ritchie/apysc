# String class length property

This page explains the `String` class `length` property.

## What property is this?

The `length` property returns the number of characters.

For example, the `ABCDEF` string returns 6, and the `あいうえお` string returns 5.

## Basic usage

The `length` property returns an `Int` value as follows:

```py
# runnable
import apysc as ap

ap.Stage(stage_width=0, stage_height=0, background_color="#333", stage_elem_id="stage")

string: ap.String = ap.String("ABCDEF")
length: ap.Int = string.length
ap.assert_equal(length, 6)

ap.save_overall_html(dest_dir_path="string_length_basic_usage_1/")
```

<iframe src="static/string_length_basic_usage_1/index.html" width="0" height="0"></iframe>

## Notes of the emoji

This property returns an unexpected characters length when the string is an emoji character: since this property counts Unicode code points.

Most of the emoji characters behave as expected length, as follows:

```py
# runnable
import apysc as ap

ap.Stage(stage_width=0, stage_height=0, background_color="#333", stage_elem_id="stage")
string: ap.String = ap.String("🎉")
ap.assert_equal(string.length, 1)

string = ap.String("🥳🌟🍻")
ap.assert_equal(string.length, 3)

ap.save_overall_html(dest_dir_path="string_length_notes_1/")
```

<iframe src="static/string_length_notes_1/index.html" width="0" height="0"></iframe>

However, in some emojis that have multiple code points, this property returns an unexpected length of characters (this behavior is the same as the Python):

```py
# runnable
import apysc as ap

ap.Stage(stage_width=0, stage_height=0, background_color="#333", stage_elem_id="stage")

assert len("👨‍👩‍👦") == 5

string: ap.String = ap.String("👨‍👩‍👦")
ap.assert_equal(string.length, 5)

ap.save_overall_html(dest_dir_path="string_length_notes_2/")
```

<iframe src="static/string_length_notes_2/index.html" width="0" height="0"></iframe>

## length property API

<!-- Docstring: apysc._type.string_length_mixin.StringLengthMixIn.length -->

<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>

**[Interface summary]**

Get a character length (number).<hr>

**[Returns]**

- `characters_length`: Int
  - A character length (number).

<hr>

**[Examples]**

```py
>>> import apysc as ap
>>> string: ap.String = ap.String("Hello")
>>> string.length
Int(5)
```