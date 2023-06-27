# `apysc._validation.matrix_data_validation` docstrings

## Module summary

The validation utilities for matrix data.

## `validate_matrix_array_data` function docstring

Validate whether a specified matrix array data is a valid type or not.<hr>

**[Parameters]**

- `matrix_array_data`: Array[Dictionary[String, Union[Int, Number, String]]]
  - A matrix array data.
- `additional_err_msg`: str
  - An additional error message to display.

<hr>

**[Raises]**

- TypeError: <br> ・If a specified data type is not `ap.Array`. <br> ・If values are not the type of the `ap.Dictionary`. <br> ・If a dictionary key's type is not `ap.String`. <br> ・If a dictionary value's type is not `ap.Int`, `ap.Number`, or `ap.String`.

## `validate_matrix_list_data` function docstring

Validate whether a specified matrix list data is a valid type or not.<hr>

**[Parameters]**

- `matrix_list_data`: List[Dict[str, Union[int, float, str]]]
  - A matrix list data.
- `additional_err_msg`: str, optional
  - An additional error message to display.

<hr>

**[Raises]**

- TypeError: <br> ・If a specified data type is not a list. <br> ・If values are not type of dict. <br> ・If a dictionary key's type is not str. <br> ・If a dictionary value's type is not int, float, or str.