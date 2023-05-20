# range function

This page explains the `range` function.

## What function is this?

The `range` function creates a range array of `ap.Int` (e.g., `[0, 1, 2, 3, 4, 5]`).

## Basic usage

If you specify only one argument, a range array becomes 0 to argument value -1.

```py
# runnable
import apysc as ap

ap.Stage(stage_width=0, stage_height=0, background_color="#333", stage_elem_id="stage")
range_arr: ap.Array[ap.Int] = ap.range(5)
ap.assert_equal(range_arr, [0, 1, 2, 3, 4])
ap.save_overall_html(dest_dir_path="range_basics_usage_1/")
```

<iframe src="static/range_basics_usage_1/index.html" width="0" height="0"></iframe>

Also, if you specify two arguments, a range array becomes a first argument value to a second argument value -1.

```py
# runnable
import apysc as ap

ap.Stage(stage_width=0, stage_height=0, background_color="#333", stage_elem_id="stage")
range_arr: ap.Array[ap.Int] = ap.range(2, 4)
ap.assert_equal(range_arr, [2, 3])
ap.save_overall_html(dest_dir_path="range_basics_usage_2/")
```

<iframe src="static/range_basics_usage_2/index.html" width="0" height="0"></iframe>

If three arguments, a range array becomes a first argument value to a second argument value, and a step between each value becomes a third argument value.

```py
# runnable
import apysc as ap

ap.Stage(stage_width=0, stage_height=0, background_color="#333", stage_elem_id="stage")
range_arr: ap.Array[ap.Int] = ap.range(2, 10, 2)
ap.assert_equal(range_arr, [2, 4, 6, 8])
ap.save_overall_html(dest_dir_path="range_basics_usage_3/")
```

<iframe src="static/range_basics_usage_3/index.html" width="0" height="0"></iframe>

## range function API

<!-- Docstring: apysc._loop._range.range -->

<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>

**[Interface signature]** `range(*args: Any) -> apysc._type.array.Array[apysc._type.int.Int]`<hr>

**[Interface summary]**

Create a range array of integers.<hr>

**[Returns]**

- `arr`: Array[Int]
  - A created array.

<hr>

**[Examples]**

```py
>>> import apysc as ap
>>> range_arr: ap.Array[ap.Int] = ap.range(5)
>>> ap.assert_equal(range_arr, [0, 1, 2, 3, 4])
>>> range_arr = ap.range(2, 4)
>>> ap.assert_equal(range_arr, [2, 3])
>>> range_arr = ap.range(2, 10, 2)
>>> ap.assert_equal(range_arr, [2, 4, 6, 8])
```