# `apysc._chart.vertical_bar_chart` docstrings

## Module summary

Class implementation for the vertical bar chart.

## `VerticalBarChart` class docstring

The class for the vertical bar chart.

### `__init__` method docstring

Create a vertical bar chart instance.<hr>

**[Parameters]**

- `data`: Union[Array[Dictionary[String, Union[Int, Number, String]]], List[Dict[str, Union[int, float, str]]]]  # noqa
  - A data array, which contains a 1-dimensional string key dictionary. A list of dictionaries or an `ap.Array` of `ap.Dictionary` values are acceptable. E.g., `[{"column_name_1": 10, "column_name_2"}]`
- `x_axis_settings`: XAxisSettings
  - An x-axis setting.
- `y_axis_settings`: YAxisSingleColumnSettings
  - A y-axis setting.
- `x`: Union[Number]
  - A chart's x-coordinate.
- `y`: Union[float, Number]
  - A chart's y-coordinate.
- `width`: Union[int, Int], default 640
  - A chart's width.
- `height`: Union[int, Int], default 395
  - A chart's height.
- `background_fill_color`: str or String, default "#ffffff"
  - A chart's background fill-color.
- `background_fill_alpha`: Union[float, Number], default 1.0
  - A chart's background fill-alpha.
- `border_color`: str or String, default ""
  - A chart's border color.
- `border_alpha`: Union[float, Number], default 1.0
  - A chart's border alpha.
- `border_thickness`: Union[int, Int], default 1
  - A chart's border thickness.
- `variable_name_suffix`: str, default ""
  - A JavaScript variable name suffix string. This setting is sometimes useful for JavaScript debugging.