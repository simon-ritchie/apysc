# `apysc._converter.list_of_strs_to_array` docstrings

## Module summary

The conversion utility to convert a built-in list of str to an apysc's Array of String.

## `list_of_strs_to_array_of_string` function docstring

Convert a built-in list of str to an apysc's `Array` of `String`.<hr>

**[Parameters]**

- `optional_list_or_arr`: Optional[Union[List[str], Array[String]]]
  - An optional list of str or array of `String` to convert.
- `variable_name_suffix`: str, optional
  - A JavaScript variable name suffix string. This setting is sometimes useful for JavaScript debugging.

<hr>

**[Returns]**

- `converted_value`: Optional[Array[String]]
  - A converted array of `String` value. If the `optional_list_or_arr` is None, this function returns None.