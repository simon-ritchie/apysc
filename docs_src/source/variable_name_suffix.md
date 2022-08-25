# variable_name_suffix argument setting

This page explains the `variable_name_suffix` argument setting.

## What argument is this?

The `variable_name_suffix` argument changes an exported JavaScript's variable name suffix.

This setting sometimes becomes useful when you want to debug an exported JavaScript code.

## Basic usage

Each class has a `variable_name_suffix`, and you can set a suffix with its argument.

The following example sets the `my_int` suffix to the `ap.Int` instance:

```py
import apysc as ap

ap.Stage(stage_width=150, stage_height=150, stage_elem_id="stage")
int_val: ap.Int = ap.Int(10, variable_name_suffix="my_int")
ap.trace(int_val)

ap.save_overall_html(
    dest_dir_path="./variable_name_suffix_basic_usage_1/", minify=False
)
```

In the exported JavaScript code, you can verify its `ap.Int` variable has the specified suffix, `_my_int`, as follows:

```js
  // ...
  var i_9__my_int = 10;
  console.log(i_9__my_int, "Called from: tmp.py, line number: 5");
  // ...
```

Class attributes inherit a suffix value of its class argument's value.

For example, if you set the `my_rectangle` value to the `variable_name_suffix` argument, its attributes (e.g., `x`, `fill_color`) also inherit the `my_rectangle` suffix:

```py
import apysc as ap

ap.Stage(stage_width=150, stage_height=150, stage_elem_id="stage")
rectangle: ap.Rectangle = ap.Rectangle(
    x=50,
    y=50,
    width=50,
    height=50,
    fill_color="#0af",
    variable_name_suffix="my_rectangle",
)

ap.save_overall_html(
    dest_dir_path="./variable_name_suffix_basic_usage_2/", minify=False
)
```

In that case, each attribute also has an attribute identifier suffix, such as the `x`, `width`:

```js
  var i_9__my_rectangle__x = 50;
  var i_10__my_rectangle__y = 50;
  var i_12__my_rectangle__width = 50;
  // ...
  var rect_1__my_rectangle = stage
    .rect(i_16__my_rectangle__width, i_17__my_rectangle__height)
    .attr({
      fill: s_1__my_rectangle__fill_color,
      "fill-opacity": n_2__my_rectangle__fill_alpha,
      "stroke-width": i_15__my_rectangle__line_thickness,
      "stroke-opacity": n_3__my_rectangle__line_alpha,
      x: i_9__my_rectangle__x,
      y: i_10__my_rectangle__y,
    });
  // ...
```