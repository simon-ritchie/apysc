# `apysc._lint_and_doc.docstring_util` docstrings

## Module summary

Utility implementations for docstrings.

## `_append_br_tag_and_replace_symbol_if_first_char_is_hyphen` function docstring

Append a break tag and replace the hypen symbol if the first character is the hypen symbol.<hr>

**[Parameters]**

- `line`: str
  - Target docstring line.

<hr>

**[Returns]**

- `line`: str
  - Replaced docstring line.

## `_convert_docstring_path_comment_to_markdown_format` function docstring

Convert a specified docstring path comment to a markdown format text.<hr>

**[Parameters]**

- `docstring_path_comment`: str
  - Target docstring path comment.
- `md_file_path`: str
  - Target markdown file path.

<hr>

**[Returns]**

- `markdown_format_docstring`: str
  - Converted text.

## `_convert_docstring_to_markdown` function docstring

Convert a specified docstring to a markdown format text.<hr>

**[Parameters]**

- `docstring`: str
  - Target docstring.
- `signature`: Signature or None
  - Target callable's signature. If a target interface is property, this argument becomes None.
- `callable_name`: str
  - Target callable name.
- `md_file_path`: str
  - Target markdown file path.

<hr>

**[Returns]**

- `markdown`: str
  - Converted markdown text.

## `_extract_docstring_path_specification_comment_from_line` function docstring

Extract a docstring path specification comment from a specified markdown line text.<hr>

**[Parameters]**

- `line`: str
  - Target markdown line text.
- `matches`: list of str
  - Matched docstring path specification comments.

<hr>

**[Returns]**

- `docstring_path_specification_comment`: str
  - Extracted comment string.

## `_extract_package_path_and_callable_name_from_path` function docstring

Extract a module or class package path and callable name from a specified path comment.<hr>

**[Parameters]**

- `docstring_path_comment`: str
  - Target docstring path comment.

<hr>

**[Returns]**

- `module_or_class_package_path`: str
  - Extracted module or class package path. e.g., 'apy.path' or 'any.path.AnyClass'.
- `callable_name`: str
  - Extracted callable name.

## `_extract_path_from_docstring_comment` function docstring

Extract a path string from a specified docstring path comment.<hr>

**[Parameters]**

- `docstring_path_comment`: str
  - Target docstring path comment.

<hr>

**[Returns]**

- `path`: str
  - Extracted path string.

## `_get_base_indent_num_if_not_set` function docstring

Get a base indent number from line if it is not set.<hr>

**[Parameters]**

- `line`: str
  - Target docstring line.
- `base_indent_num`: int
  - Current base indent number.

<hr>

**[Returns]**

- `base_indent_num`: int
  - If the base_indent_num argument is zero, this function returns the current line indent number. Otherwise, it returns the same value of the base_indent_num argument.

## `_get_callable_from_package_path_and_callable_name` function docstring

Get a callable object from a specified package path and callable name.<hr>

**[Parameters]**

- `module_or_class_package_path`: str
  - Target module or class package path.
- `callable_name`: str
  - Target callable name.

<hr>

**[Returns]**

- `callable_`: Callable
  - Target callable object.

<hr>

**[Raises]**

- _DocstringPathNotFoundError: If a specified package path's module or class does not exist.
- _DocstringCallableNotExistsError: If a target module or class does not have a specified name function or method.

## `_get_docstring_path_comment_matches` function docstring

Get matched docstring path specification comments.<hr>

**[Parameters]**

- `md_txt`: str
  - Target markdown text.

<hr>

**[Returns]**

- `matches`: list of str
  - Matched comments.

## `_get_indent_num_from_line` function docstring

Get an indent number from a specified docstring line.<hr>

**[Parameters]**

- `line`: str
  - Target docstring line.

<hr>

**[Returns]**

- `indent_num`: int
  - Indent number of a specified docstring line.

## `_get_params_or_rtns_section_pattern_by_type` function docstring

Get the parameters or returns section pattern of a specified type.<hr>

**[Parameters]**

- `target_type`: Parameter or Return
  - Target type.

<hr>

**[Returns]**

- `pattern`: _SectionPattern
  - Target section pattern.

<hr>

**[Raises]**

- ValueError: If an invalid target type is provided.

## `_get_value_name_and_type_from_line` function docstring

Get a parameter or return value and type from a specified line.<hr>

**[Parameters]**

- `line`: str
  - Target docstring line.

<hr>

**[Returns]**

- `value_name`: str
  - Target parameter or return value name.
- `type_name`: str
  - Target parameter or return value type name.

## `_is_example_output_line` function docstring

Get a boolean indicating whether a specified line is example section's output line or not.<hr>

**[Parameters]**

- `line`: str
  - Target docstring line.

<hr>

**[Returns]**

- `result`: bool
  - This function return True if a specified line is example section's output line.

## `_is_hyphens_line` function docstring

Get a boolean indicating whether a specified line is a hyphens line or not.<hr>

**[Parameters]**

- `line`: str
  - Target docstring line.

<hr>

**[Returns]**

- `result`: bool
  - If a specified line is a hyphens line, this function returns True.

## `_is_section_line` function docstring

Get a boolean indicating whether a specified docstring line is a section line or not.<hr>

**[Parameters]**

- `line`: str
  - Target docstring line text.

<hr>

**[Returns]**

- `result`: bool
  - If a specified docstring line is section line, this function returns True.

## `_is_skip_target_line` function docstring

Get a boolean indicating whether a specified line is skipping target or not.<hr>

**[Parameters]**

- `is_target_section_range`: bool
  - A boolean indicating whether a specified line is in a range of target section.
- `line`: str
  - Target docstring line.

<hr>

**[Returns]**

- `result`: bool
  - A boolean indicating whether a specified line is skipping target or not.

## `_is_target_section_pattern_line` function docstring

Get a boolean indicating whether a specified line is matching with a target section pattern or not.<hr>

**[Parameters]**

- `line`: str
  - Target docstring line.
- `section_pattern`: _SectionPattern
  - Target section pattern.

<hr>

**[Returns]**

- `result`: bool
  - If a specified line is the parameters section, this function returns True.

## `_make_example_and_append_to_list` function docstring

Make an example value and append it ot a specified list.<hr>

**[Parameters]**

- `example_values`: list of Example
  - A list to append an example value.
- `input_code_block_lines`: list of str
  - A list of input code block lines.
- `expected_output`: str
  - An expected output string.

<hr>

**[Notes]**

This function clears a list of input code block lines.

## `_make_prm_or_rtn_description_and_append_to_list` function docstring

Make a parameter or return value description from a list of lines and append parameter or return value to a specified list.<hr>

**[Parameters]**

- `target_type`: Type
  - Target type of the Parameter or Return.
- `param_or_rtn_values`: lisf of _ParamOrRtnBase
  - A list to append a parameter or return value.
- `value_name`: str
  - Parameter or return value name.
- `value_type_str`: str
  - Parameter or return type name.
- `description_lines`: list of str
  - A list of description lines.

<hr>

**[Notes]**

This function clears a list of description lines.

## `_make_raise_description_and_append_to_list` function docstring

Make a raise value description from a list of lines and append raise value to a specified list.<hr>

**[Parameters]**

- `raise_values`: list of Raise
  - A list to append a raise value.
- `err_class_name`: str
  - Target error class name.
- `description_lines`: list of str
  - A list of description lines.

<hr>

**[Notes]**

This function clears a list of description lines.

## `_make_reference_and_append_to_list` function docstring

Make a reference value and append it to a specified list.<hr>

**[Parameters]**

- `reference_values`: list of Reference
  - A list to append a reference value.
- `page_label`: str
  - Target reference page label.
- `url`: str
  - Target reference page URL.

## `_remove_blank_lines_from_list` function docstring

Remove blank lines from a list of lines.<hr>

**[Parameters]**

- `lines`: list of str
  - Target list of lines.

<hr>

**[Returns]**

- `result_lines`: list of str
  - A lines list which removed blank lines.

## `_remove_line_breaks_and_unnecessary_spaces` function docstring

Remove line breaks to a single space and unnecessary spaces (e.g., double spaces and leading and trailing spaces).<hr>

**[Parameters]**

- `text`: str
  - Target text.

<hr>

**[Returns]**

- `text`: str
  - Converted text.

## `_remove_noqa` function docstring

Remove a noqa comment from a specified string.<hr>

**[Parameters]**

- `string`: str
  - Target string.

<hr>

**[Returns]**

- `string`: str
  - Result string.

## `_remove_replaced_docstring_section_from_md_txt` function docstring

Remove replaced docstring from a specified markdown text.<hr>

**[Parameters]**

- `md_txt`: str
  - Target markdown text.
- `matches`: list of str
  - Matched docstring path specification comments.

<hr>

**[Returns]**

- `md_txt`: str
  - Result markdown text.

## `_remove_unnecessary_markdown_list_from_line` function docstring

Remove unnecessary markdown list string from a line.<hr>

**[Parameters]**

- `line`: str
  - Target docstring line.

<hr>

**[Returns]**

- `line`: str
  - Result docstring line.

## `_slice_references_by_md_file_path` function docstring

Slice a specified references list to exclude a same URL's document file.<hr>

**[Parameters]**

- `references`: list of Reference
  - Target references list to slice.
- `md_file_path`: str
  - Target markdown file path.

<hr>

**[Returns]**

- `sliced_references`: list of Reference
  - Sliced list.

## `append_examples_to_markdown` function docstring

Append examples to a specified markdown string.<hr>

**[Parameters]**

- `markdown`: str
  - Target markdown string.
- `examples`: list of Example
  - Examples list value to append to.

<hr>

**[Returns]**

- `markdown`: str
  - Result markdown string.

## `append_notes_to_markdown` function docstring

Append a notes string to a specified markdown string.<hr>

**[Parameters]**

- `markdown`: str
  - Target markdown string.
- `notes`: str
  - Target notes string.

<hr>

**[Returns]**

- `markdown`: str
  - Result markdown string.

## `append_params_or_rtns_to_markdown` function docstring

Append parameters or returns to a specified markdown string.<hr>

**[Parameters]**

- `markdown`: str
  - Target markdown string.
- `params_or_rtns`: list of _ParamOrRtn
  - Parameters or returns to append to.

<hr>

**[Returns]**

- `markdown`: str
  - Result markdown string.

## `append_raises_to_markdown` function docstring

Append raises to a specified markdown string.<hr>

**[Parameters]**

- `markdown`: str
  - Target markdown string.
- `raises`: list of Raise
  - Raises list value to append to.

<hr>

**[Returns]**

- `markdown`: str
  - Result markdown string.

## `append_references_to_markdown` function docstring

Append references to a specified markdown string.<hr>

**[Parameters]**

- `markdown`: str
  - Target markdown string.
- `references`: list of Reference
  - References list value to append to.

<hr>

**[Returns]**

- `markdown`: str
  - Result markdown string.

## `append_summary_to_markdown` function docstring

Append a interface summary string to a specified markdown string.<hr>

**[Parameters]**

- `markdown`: str
  - Target markdown string.
- `summary`: str
  - Target summary string.
- `heading_label`: str
  - A label to append at the beginning.

<hr>

**[Returns]**

- `markdown`: str
  - Result markdown string.

## `extract_example_values_from_docstring` function docstring

Extract example values from a docstring.<hr>

**[Parameters]**

- `docstring`: str
  - Target docstring.

<hr>

**[Returns]**

- `example_values`: list of Example
  - Extracted example values.

## `extract_notes_from_docstring` function docstring

Extract a notes value from a docstring.<hr>

**[Parameters]**

- `docstring`: str
  - Target docstring.

<hr>

**[Returns]**

- `notes`: str
  - Extract notes text value.

## `extract_param_or_rtn_values_from_docstring` function docstring

Extract parameter or return values from a docstring.<hr>

**[Parameters]**

- `target_type`: Type
  - Target type of the Parameter or Return.
- `docstring`: str
  - Target docstring.

<hr>

**[Returns]**

- `param_or_rtn_values`: list of Parameter or Return
  - Extracted parameter or return values.

## `extract_raise_values_from_docstring` function docstring

Extract raise values from a docstring.<hr>

**[Parameters]**

- `docstring`: str
  - Target docstring.

<hr>

**[Returns]**

- `raise_values`: list of Raise
  - Extracted raise values.

## `extract_reference_values_from_docstring` function docstring

Extract reference values from a docstring.<hr>

**[Parameters]**

- `docstring`: str
  - Target docstring.

<hr>

**[Returns]**

- `reference_values`: list of Reference
  - Extracted reference values.

## `extract_summary_from_docstring` function docstring

Extract a summary text from a docstring.<hr>

**[Parameters]**

- `docstring`: str
  - Target docstring.

<hr>

**[Returns]**

- `summary`: str
  - Extracted summary text.

<hr>

**[Notes]**

This function converts line break to a space.

## `get_docstring_src_module_paths` function docstring

Get docstring source module paths from a specified markdown file path.<hr>

**[Parameters]**

- `md_file_path`: str
  - Target markdown file path.

<hr>

**[Returns]**

- `module_paths`: list of str
  - Extracted docstring source module paths.

## `remove_trailing_hr_tag` function docstring

Remove a trailing `<hr>` tag from a specified markdown string.<hr>

**[Parameters]**

- `markdown`: str
  - Target markdown string.

<hr>

**[Returns]**

- `markdown`: str
  - Result markdown string.

## `replace_docstring_path_specification` function docstring

Replace a docstring path specification in a specified markdown document by a converted docstring text.<hr>

**[Parameters]**

- `md_file_path`: str
  - Target markdown file path.

## `reset_replaced_docstring_section` function docstring

Reset converted a markdown's docstring section.<hr>

**[Parameters]**

- `md_file_path`: str
  - Target markdown document file path.

<hr>

**[Returns]**

- `is_executed`: bool
  - Replacing is executed or not.

## `Example` class docstring

Example value type.

### `__eq__` method docstring

The method for equality comparison.<hr>

**[Parameters]**

- `other`: Any
  - Other value to compare with.

<hr>

**[Returns]**

- `result`: bool
  - If each attribute is equal to the other, this method returns True.

### `__init__` method docstring

Example value type.<hr>

**[Parameters]**

- `input_code_block`: str
  - Input code block string.
- `expected_output`: str, default ''
  - Expected output string.

## `Parameter` class docstring

Parameter value type.

### `__eq__` method docstring

The method for equality comparison.<hr>

**[Parameters]**

- `other`: Any
  - Other instance to compare with.

<hr>

**[Returns]**

- `result`: bool
  - If each attribute is equal to the other, this method returns True.

### `__init__` method docstring

Parameter or return value's base class.<hr>

**[Parameters]**

- `name`: str
  - Parameter or return value name.
- `type_str`: str
  - Parameter or return value type name.
- `description`: str
  - Parameter or return value description.

## `Raise` class docstring

Raise value type.

### `__eq__` method docstring

The method for equality comparison.<hr>

**[Parameters]**

- `other`: Any
  - Other value to compare with.

<hr>

**[Returns]**

- `result`: bool
  - If each attribute is equal to the other, this method returns True.

### `__init__` method docstring

Raise value type.<hr>

**[Parameters]**

- `err_class_name`: str
  - Target error class name.
- `description`: str
  - Error condition description.

## `Reference` class docstring

Reference value type.

### `__eq__` method docstring

The method for equality comparison.<hr>

**[Parameters]**

- `other`: Any
  - Other value to compare with.

<hr>

**[Returns]**

- `result`: bool
  - If each attribute is equal to the other, this method returns True.

### `__init__` method docstring

Reference value type.<hr>

**[Parameters]**

- `page_label`: str
  - Target reference page label.
- `url`: str
  - Target reference page URL.

## `Return` class docstring

Return value type.

### `__eq__` method docstring

The method for equality comparison.<hr>

**[Parameters]**

- `other`: Any
  - Other instance to compare with.

<hr>

**[Returns]**

- `result`: bool
  - If each attribute is equal to the other, this method returns True.

### `__init__` method docstring

Parameter or return value's base class.<hr>

**[Parameters]**

- `name`: str
  - Parameter or return value name.
- `type_str`: str
  - Parameter or return value type name.
- `description`: str
  - Parameter or return value description.

## `_DocstringCallableNotExistsError` class docstring

## `_DocstringPathNotFoundError` class docstring

## `_ParamOrRtnBase` class docstring

### `__eq__` method docstring

The method for equality comparison.<hr>

**[Parameters]**

- `other`: Any
  - Other instance to compare with.

<hr>

**[Returns]**

- `result`: bool
  - If each attribute is equal to the other, this method returns True.

### `__init__` method docstring

Parameter or return value's base class.<hr>

**[Parameters]**

- `name`: str
  - Parameter or return value name.
- `type_str`: str
  - Parameter or return value type name.
- `description`: str
  - Parameter or return value description.

## `_SectionPattern` class docstring

An enumeration.