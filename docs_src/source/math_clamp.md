# Math clamp interface

This page explains the `Math` class's `clamp` class method interface.

## What interface is this?

The `clamp` method sets the value within a specified minimum and maximum range.

For example, if the value is `20` and the minimum is `25`, the result value becomes `25`.

Similarly, if the value is `20` and the maximum is `15`, the result value becomes `15`.

If the value is `20` and the minimum and maximum are `15` and `25`, this method returns the `20` value as is.

## Basic usage

The `clamp` method requires the `value`, `min_`, and `max_` arguments.

Each argument and return value becomes the `ap.Int` or `ap.Number` type.

```py
# runnable
import apysc as ap

ap.Stage(
    background_color=ap.Color("#333"),
    stage_width=1,
    stage_height=1,
    stage_elem_id="stage",
)
value: ap.Int = ap.Int(20)
result: ap.Int = ap.Math.clamp(value=value, min_=ap.Int(25), max_=ap.Int(50))
ap.assert_equal(result, ap.Int(25))

result = ap.Math.clamp(value=value, min_=ap.Int(10), max_=ap.Int(15))
ap.assert_equal(result, ap.Int(15))

result = ap.Math.clamp(value=value, min_=ap.Int(15), max_=ap.Int(25))
ap.assert_equal(result, ap.Int(20))

ap.save_overall_html(dest_dir_path="math_clamp_basic_usage/")
```

<iframe src="static/math_clamp_basic_usage/index.html" width="1" height="1"></iframe>

## clamp method API

<!-- Docstring: apysc._math.clamp_mixin.ClampMixIn.clamp -->

<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>

**[Interface signature]** `clamp(*, value: ~_ValueType, min_: ~_ValueType, max_: ~_ValueType) -> ~_ValueType`<hr>

**[Interface summary]**

Sets the value within a specified minimum and maximum range. If the value is less than the minumum, this method returns the minimum value. If the value is greater than the maximum, this method returns the maximum value.<hr>

**[Parameters]**

- `value`: _ValueType
  - Target `Int` or `Number` value.
- `min_`: _ValueType
  - Minimum value.
- `max_`: _ValueType
  - Maximum value.

<hr>

**[Returns]**

- `result`: _ValueType
  - Clamped value.

<hr>

**[Examples]**

```py
>>> import apysc as ap
>>> _ = ap.Stage()
>>> value: ap.Int = ap.Int(5)
>>> value = ap.Math.clamp(value=value, min_=ap.Int(10), max_=ap.Int(20))
>>> value
Int(10)

>>> value = ap.Int(25)
>>> value = ap.Math.clamp(value=value, min_=ap.Int(10), max_=ap.Int(20))
>>> value
Int(20)
```