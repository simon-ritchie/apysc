# `apysc._chart.create_single_column_y_axis_mixin` docstrings

## Module summary

The mix-in class implementation for the single column's `_create_y_axis` method.

## `_calculate_y_axis_height` function docstring

Calculate a y-axis height.<hr>

**[Parameters]**

- `chart_height`: Int
  - A chart height.
- `vertical_padding`: Int
  - A chart's vertical padding between borders and contents.
- `tick_text_font_size`: Int
  - A tick text font size.
- `axis_label_font_size`: Int
  - An axis label font size.
- `is_display_axis_label`: Boolean
  - A boolean, whether an axis label is visible or not.
- `variable_name_suffix`: str, optional
  - A JavaScript variable name suffix string. This setting is sometimes useful for JavaScript debugging.

<hr>

**[Returns]**

- `y_axis_height`: Int
  - A calculate height.

## `_calculate_y_axis_ticks_num` function docstring

Calculate a y-axis ticks number.<hr>

**[Parameters]**

- `y_axis_height`: Int
  - A y-axis height.
- `tick_max_num`: Optional[Int]
  - A ticks maximum number.
- `tick_text_font_size`: Int
  - A tick text font size.
- `variable_name_suffix`: str, optional
  - A JavaScript variable name suffix string. This setting is sometimes useful for JavaScript debugging.

<hr>

**[Returns]**

- `y_axis_ticks_num`: Int
  - A y-axis ticks number.

## `_calculate_y_max_from_data` function docstring

Get a y-axis maximum value from a specified data.<hr>

**[Parameters]**

- `data`: Array[Dictionary[str, Union[Int, Number, String]]]
  - A data array, which contains a 1-dimensional string key dictionary.
- `y_axis_column_name`: str
  - A y-axis column name.
- `variable_name_suffix`: str
  - A JavaScript variable name suffix string. This setting is sometimes useful for JavaScript debugging.

<hr>

**[Returns]**

- `y_max`: Number
  - A y-axis maximum value.

## `_calculate_y_min_from_data` function docstring

Get a y-axis minimum value from specified data.<hr>

**[Parameters]**

- `data`: Array[Dictionary[str, Union[Int, Number, String]]]
  - A data array, which contains a 1-dimensional string key dictionary.
- `y_axis_column_name`: str
  - A y-axis column name.
- `variable_name_suffix`: str, optional
  - A JavaScript variable name suffix string. This setting is sometimes useful for JavaScript debugging.

<hr>

**[Returns]**

- `y_min`: Number
  - A y-axis minimum value.

## `_extract_column_values_from_data` function docstring

Get a specified column values array from a specified data.<hr>

**[Parameters]**

- `data`: Array[Dictionary[str, Union[Int, Number, String]]]
  - A data array, which contains a 1-dimensional string key dictionary.
- `column_name`: str
  - A y-axis column name.
- `variable_name_suffix`: str, optional
  - A JavaScript variable name suffix string. This setting is sometimes useful for JavaScript debugging.

<hr>

**[Returns]**

- `values`: Array[Union[Int, Number]]
  - A values array.

## `CreateSingleColumnYAxisMixIn` class docstring

### `_create_y_axis` method docstring

Create a y-axis instance.<hr>

**[Parameters]**

- `data`: Array[Dictionary[str, Union[Int, Number, String]]],
  - A data array, which contains a 1-dimensional string key dictionary.
- `y_axis_container`: Sprite
  - A y-axis container instance.
- `chart_height`: Int
  - A chart height.
- `x_axis_settings`: XAxisSettings
  - An x-axis settings instance.
- `y_axis_settings`: YAxisSingleColumnSettings
  - A y-axis settings instance.
- `vertical_padding`: Int
  - A chart's vertical padding between borders and contents.
- `horizontal_padding`: Int
  - A chart's horizontal padding between borders and contents.
- `variable_name_suffix`: str, optional
  - A JavaScript variable name suffix string. This setting is sometimes useful for JavaScript debugging.