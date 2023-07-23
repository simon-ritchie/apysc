# Array class last_value property

This page explains the `Array` class `last_value` property.

## What property is this?

The `last_value` property returns the last value of an array.

## Basic usage

The following example shows that the `last_value` property becomes 30 (the array values are `[10, 20, 30]`).

```py
# runnable
import apysc as ap

ap.Stage(stage_width=0, stage_height=0, background_color="#333", stage_elem_id="stage")
arr: ap.Array[int] = ap.Array([10, 20, 30])
last_value: int = arr.last_value
ap.assert_equal(last_value, 30)

ap.save_overall_html(dest_dir_path="array_last_value_basic_usage_1/")
```

<iframe src="static/array_last_value_basic_usage_1/index.html" width="0" height="0"></iframe>

If an array's value is empty, this property becomes the `undefined` value on the JavaScript runtime:

```py
# runnable
import apysc as ap

ap.Stage(stage_width=0, stage_height=0, background_color="#333", stage_elem_id="stage")
arr: ap.Array[ap.Int] = ap.Array([], fixed_value_type=ap.Int)
last_value: ap.Int = arr.last_value
ap.assert_undefined(last_value)

ap.save_overall_html(dest_dir_path="array_last_value_basic_usage_2/")
```

<iframe src="static/array_last_value_basic_usage_2/index.html" width="0" height="0"></iframe>

## last_value property API

<!-- Docstring: apysc._type.array.Array.last_value -->

<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>

**[Interface summary]**

Get an array's last index value.<hr>

**[Returns]**

- `last_value`: _ArrValue
  - An array's last index value.

<hr>

**[Notes]**

 ・The constructor's `fixed_value_type` setting affects this property's value type. <br> ・If an array is empty, this value becomes `undefined` on the JavaScript runtime.<hr>

**[Examples]**

```py
>>> import apysc as ap
>>> _ = ap.Stage(
...     stage_width=100,
...     stage_height=50,
...     background_color="#333",
...     stage_elem_id="stage",
... )
>>> arr: ap.Array[ap.Int] = ap.Array([], fixed_value_type=ap.Int)
>>> last_value: ap.Int = arr.last_value
>>> ap.assert_undefined(last_value)
>>> arr.append(ap.Int(10))
>>> last_value = arr.last_value
>>> ap.assert_equal(last_value, 10)
>>> arr.append(ap.Int(20))
>>> last_value = arr.last_value
>>> ap.assert_equal(last_value, 20)
```