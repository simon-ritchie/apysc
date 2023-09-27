# `apysc._chart.x_axis_settings` docstrings

## Module summary

Class implementation for the x-axis settings.

## `XAxisSettings` class docstring

### `__init__` method docstring

X-axis settings class.<hr>

**[Parameters]**

- `x_axis_column_name`: str
  - X-axis column name.
- `tick_max_num`: Optional[Union[int, Int]], optional
  - A tick max display number. Often tick display number becomes under this value.
- `tick_text_font_size`: Union[int, Int], optional
  - A tick text font-size setting.
- `tick_text_font_family`: Optional[Union[Array[String], List[str]]], optional
  - A tick text font family setting. Each string in an array needs to be a font name (e.g., `Times New Roman`).
- `tick_text_fill_color`: str or String, optional
  - A tick text fill-color setting.
- `tick_text_fill_alpha`: Union[float, Number], optional
  - A tick text fill-alpha setting.
- `tick_text_bold`: Union[bool, Boolean], optional
  - A boolean, whether a tick text is a bold style or not.
- `tick_text_italic`: Union[bool, Boolean], optional
  - A boolean, whether a tick text is an italic style or not (normal).
- `line_color`: str or String, optional
  - An axis line color setting.
- `line_thickness`: Union[int, Int], optional
  - An axis line thickness (line width) setting.
- `line_alpha`: Union[float, Number], optional
  - An axis line alpha setting.
- `is_display_axis_label`: Union[bool, Boolean], optional
  - A boolean, whether an axis label is visible or not.
- `axis_label_position`: XAxisLabelPosition, optional
  - An axis label position setting.
- `axis_label_font_size`: Union[int, Int], optional
  - An axis label font size setting.
- `axis_label_font_family`: Optional[Union[Array[String], List[str]]], optional
  - An axis label font family setting.
- `axis_label_fill_color`: str or String, optional
  - An axis label fill-color setting.
- `axis_label_fill_alpha`: Union[float, Number], optional
  - An axis label fill-alpha setting.
- `axis_label_bold`: Union[bool, Boolean], optional
  - A boolean, whether an axis label is a bold style or not.
- `axis_label_italic`: Union[bool, Boolean], optional
  - A boolean, whether an axis label is an italic style or not (normal).
- `variable_name_suffix`: str, default ""
  - A JavaScript variable name suffix string. This setting is sometimes useful for JavaScript debugging.