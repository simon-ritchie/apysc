# `apysc._html.exporter` docstrings

## Module summary

Expression exporting interface implementation.

## `_append_common_js_functions` function docstring

Append common JavaScript functions (e.g., helper function) to a expression string.<hr>

**[Parameters]**

- `expression`: str
  - Target expression string.

<hr>

**[Returns]**

- `expression`: str
  - Expression string which includes fundamental functions.

## `_append_entry_point_function_call` function docstring

Append entry-point function call's script to a HTML string.<hr>

**[Parameters]**

- `html_str`: str
  - Target HTML string.

<hr>

**[Returns]**

- `html_str`: str
  - After appended html string.

## `_append_event_handler_expressions` function docstring

Append event handler's expressions to a specified string.<hr>

**[Parameters]**

- `expression`: str
  - Expression string to append event handler's one.

<hr>

**[Returns]**

- `expression`: str
  - A result expression string.

## `_append_expression_to_html_str` function docstring

Append expression strings to a specified HTML string.<hr>

**[Parameters]**

- `html_str`: str
  - Target HTML string.
- `verbose`: int, default 1
  - The Logging setting.

<hr>

**[Returns]**

- `html_str`: str
  - HTML string after appended expressions.

## `_append_head_to_html_str` function docstring

Append a head tag section to a specified HTML string.<hr>

**[Parameters]**

- `html_str`: str
  - Target HTML string.
- `js_lib_dir_path`: str
  - JavaScript libraries directory path.
- `embed_js_libs`: bool, default False
  - Option to embed the JavaScript libraries script to the output HTML or not.

<hr>

**[Returns]**

- `html_str`: str
  - HTML string after appended.

## `_append_jslib_str_to_html` function docstring

Append JavaScript libraries script string to HTML.<hr>

**[Parameters]**

- `html_str`: str
  - A HTML string to be appended.
- `js_lib_dir_path`: str
  - Target libraries directory path. If the `embed_js_libs` option is True, then this setting will be ignored.
- `jslib_file_name`: str
  - Target JavaScript library file name.
- `embed_js_libs`: bool, default False
  - Option to embed the JavaScript libraries script to the output HTML or not.

<hr>

**[Returns]**

- `html_str`: str
  - Result HTML string.

## `_append_stage_global_variable_to_html` function docstring

Append a stage's global variable to an HTML string.<hr>

**[Parameters]**

- `html_str`: str
  - Target HTML string.

<hr>

**[Returns]**

- `html_str`: str
  - After appended HTML string.

## `_display_debug_mode_ignoring_minify_setting_info` function docstring

Display information of ignoring minify setting if the debug mode is enabled.<hr>

**[Parameters]**

- `minify`: bool
  - A Boolean value indicates whether minify HTML and js or not. The False setting is helpful when debugging.
- `verbose`: int
  - If 0 is specified, the apysc does not display a message. The apysc displays a message when this value is 1 or the other value.

<hr>

**[Returns]**

- `msg`: str
  - Displayed message.

## `_display_info` function docstring

Display an info log message.<hr>

**[Parameters]**

- `msg`: str
  - A message to display.
- `verbose`: int
  - If 0 is specified, the apysc does not display a message. 1 or the other value displays the message.

<hr>

**[Returns]**

- `msg`: str
  - Displayed message.

## `_export_js_libs` function docstring

Export JavaScript libraries to a specified directory.<hr>

**[Parameters]**

- `dest_dir_path`: str
  - Directory path to export JavaScript libraries.
- `skip_js_lib_exporting`: bool
  - If True is set, then JavaScript libraries will not be exported.

<hr>

**[Returns]**

- `saved_js_file_paths`: str
  - Saved JavaScript file paths.

## `_get_var_name_from_line` function docstring

Get a js variable name from a specified line string.<hr>

**[Parameters]**

- `line`: str
  - Target line string.

<hr>

**[Returns]**

- `var_name`: str
  - Result variable name. If line contains `var <any_name> = ...;` pattern, then `any_name` will be returned. Or if there is no var expression, blank string will be returned.

## `_minify_html` function docstring

Minify HTML and js string.<hr>

**[Parameters]**

- `html_str`: str
  - HTML string to minify.
- `minify`: bool
  - A boolean value indicates whether minify HTML and js or not. If False, the apysc skips minifying.

<hr>

**[Returns]**

- `html_str`: str
  - Result html string.

<hr>

**[Notes]**

If the debug mode setting is enabled, the apysc skips minifying.

## `_remove_blank_lines` function docstring

Remove blank (break or spaces only) lines from an expression string.<hr>

**[Parameters]**

- `expression`: str
  - Target expression string.

<hr>

**[Returns]**

- `expression`: str
  - Expression string that removed blank lines.

## `_remove_unused_js_vars` function docstring

Remove unused js variables from expression string.<hr>

**[Parameters]**

- `expression`: str
  - Target js expression string.

<hr>

**[Returns]**

- `expression`: str
  - An expression string after removing.

## `_save_html` function docstring

Save HTML string to file.<hr>

**[Parameters]**

- `html_str`: str
  - HTML String to save.
- `dir_path`: str
  - Destination directory path to save html.
- `file_name`: str
  - HTML file name. e.g., 'index.html'

## `_target_js_variable_is_used` function docstring

Get a boolean value whether an expression uses a target variable in JS expression or not.<hr>

**[Parameters]**

- `var_name`: str
  - Target variable name.
- `exp_lines`: list of str
  - js expression lines.

<hr>

**[Returns]**

- `result`: bool
  - If an expression uses a target variable in JS expression, this interface returns True.

## `get_entry_point_func_name` function docstring

Get an entry point function name.<hr>

**[Returns]**

- `entry_point_func_name`: str
  - An entry point function name.

## `save_overall_html` function docstring

Save the overall HTML and js files under the specified directory path.<hr>

**[Parameters]**

- `dest_dir_path`: str
  - Destination directory path to save each HTML and js file.
- `html_file_name`: str, default 'index.html'
  - The output HTML file name.
- `minify`: bool, default True
  - Boolean value indicates whether minify HTML and js or not. The False setting is helpful when debugging.
- `js_lib_dir_path`: str, default './'
  - JavaScript libraries directory path. This setting applies to a JavaScript source path in HTML. If not specified, then set the same directory with HTML. This setting is maybe helpful to set js lib directory, such as Django's static (static_collected) directory. This interface recommends setting True value to the `skip_js_lib_exporting` argument if this argument sets.
- `skip_js_lib_exporting`: bool, default False
  - If True, this interface does not export JavaScript libraries.
- `embed_js_libs`: bool, default False
  - Option to embed the JavaScript libraries script to the output HTML or not. If True, the output HTML becomes enormous, and be only one HTML file. Occasionally, this option is useful when sharing the exported file or using the output file with an iframe tag to avoid the CORS error.
- `verbose`: int, default 1
  - The Logging setting. If 0 is specified, this interface does not display a logging message. If 1 or the other value is specified, this interface displays a message usually.

<hr>

**[Notes]**

This interface empties a specified directory before saving.<hr>

**[Examples]**

```py
>>> import apysc as ap
>>> stage: ap.Stage = ap.Stage()
>>> # Do something here...
>>> ap.save_overall_html(dest_dir_path='tmp/output/')
```

<hr>

**[References]**

- [save_overall_html interface document](https://simon-ritchie.github.io/apysc/save_overall_html.html)