# `apysc._chart.set_initial_matrix_data_mixin` docstrings

## Module summary

The mix-in class implementation for the `_set_initial_matrix_data` method.

## `_convert_list_to_array` function docstring

Convert a specified matrix list to an array.<hr>

**[Parameters]**

- `data`: List[Dict[str, Union[int, float, str]]]
  - A matrix list.
- `variable_name_suffix`: str, optional
  - A JavaScript variable name suffix string. This setting is sometimes useful for JavaScript debugging.

<hr>

**[Returns]**

- `data__`: Array[Dictionary[String, Union[Int, Number, String]]]:
  - A converted array.

## `SetInitialMatrixDataMixIn` class docstring

### `_set_initial_matrix_data` method docstring

Set an initial matrix data.<hr>

**[Parameters]**

- `data`: _DataType
  - A data array, which contains a 1-dimensional string key dictionary. A list of dictionaries or an `ap.Array` of `ap.Dictionary` values are acceptable. E.g., `[{"column_name_1": 10, "column_name_2"}]`
- `variable_name_suffix`: str, optional
  - A JavaScript variable name suffix string. This setting is sometimes useful for JavaScript debugging.