# `apysc._chart.create_single_column_y_axis_mixin` docstrings

## Module summary

The mix-in class implementation for the single column's `_create_y_axis` method.

## `_apply_x_coordinate_to_y_axis_ticks_texts` function docstring

Apply x-coordinate to y-axis ticks texts.<hr>

**[Parameters]**

- `horizontal_padding`: Int
  - A chart horizontal padding.
- `y_axis_ticks_texts`: Array[SVGText]
  - Y-axis ticks' texts.
- `variable_name_suffix`: str
  - A JavaScript variable name suffix string. This setting is sometimes useful for JavaScript debugging.

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
  - Calculate height.

## `_calculate_y_axis_max` function docstring

Calculate a y-axis max value.<hr>

**[Parameters]**

- `y_max`: Optional[Number]
  - A y-axis max setting (limitation).
- `in_value_y_max`: Number
  - A maximum y value in data.

<hr>

**[Returns]**

- `y_axis_max`: Number
  - A calculated y-axis max value.

## `_calculate_y_axis_min` function docstring

Calculate a y-axis min value.<hr>

**[Parameters]**

- `y_min`: Optional[Number]
  - A y-axis min setting.
- `in_value_y_min`: Number
  - A minimum y value in data.

<hr>

**[Returns]**

- `y_axis_min`: Number
  - A calculated y-axis min value.

## `_calculate_y_axis_ticks_num` function docstring

Calculate y-axis ticks number.<hr>

**[Parameters]**

- `y_axis_height`: Int
  - A y-axis height.
- `tick_max_num`: Optional[Int]
  - A maximum ticks number.
- `tick_text_font_size`: Int
  - A tick text font size.
- `variable_name_suffix`: str, optional
  - A JavaScript variable name suffix string. This setting is sometimes useful for JavaScript debugging.

<hr>

**[Returns]**

- `y_axis_ticks_num`: Int
  - Y-axis ticks number.

## `_calculate_y_axis_ticks_y_coordinates` function docstring

Calculate y-axis ticks coordinates.<hr>

**[Parameters]**

- `vertical_padding`: Int
  - A chart's vertical padding between borders and contents.
- `y_axis_height`: Int
  - An axis height.
- `y_axis_ticks_num`: Int
  - Axis tick number.
- `variable_name_suffix`: str
  - A JavaScript variable name suffix string. This setting is sometimes useful for JavaScript debugging.

<hr>

**[Returns]**

- `y_axis_ticks_y_coordinates`: Array[Number]
  - Y-axis ticks coordinates. The first index becomes the axis starting coordinate (bottom position of a y-axis).

## `_calculate_y_max_from_data` function docstring

Get a maximum y-axis value from specified data.<hr>

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
  - A maximum y-axis value.

## `_calculate_y_min_from_data` function docstring

Get a minimum y-axis value from specified data.<hr>

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
  - A minimum y-axis value.

## `_create_y_axis_ticks_texts` function docstring

Create y-axis ticks texts.<hr>

**[Parameters]**

- `y_axis_column_name`: str
  - A y-axis column name.
- `data`: Array[Dictionary[str, Union[Int, Number, String]]]
  - A data array, which contains a 1-dimensional string key dictionary.
- `y_axis_container`: Sprite
  - A y-axis container instance.
- `horizontal_padding`: Int
  - A chart horizontal padding.
- `y_axis_ticks_y_coordinates`: Array[Number]
  - Y-axis ticks y-coordinates.
- `tick_text_fill_color`: String
  - A tick text fill-color.
- `tick_text_fill_alpha`: Number
  - A tick text fill-alpha.
- `tick_text_font_size`: Int
  - A tick text font size.
- `tick_text_font_family`: Optional[String]
  - A tick text font family.
- `tick_text_bold`: Boolean
  - A boolean, whether to use bold tick text style or not.
- `tick_text_italic`: Boolean
  - A boolean, whether to use italic tick text style or not.
- `variable_name_suffix`: str
  - A JavaScript variable name suffix string. This setting is sometimes useful for JavaScript debugging.

<hr>

**[Returns]**

- `y_axis_ticks_texts`: Array[SVGText]
  - Created y-axis ticks texts.

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

## `_extract_text_value_from_data_dict` function docstring

Extract a text value from a specified data dictionary.<hr>

**[Parameters]**

- `data_dict`: Dictionary[str, Union[Int, Number, String]]
  - A single-row data dictionary.
- `y_axis_column_name`: str
  - A y-axis column name.

<hr>

**[Returns]**

- `text_value`: String
  - An extracted text value.

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