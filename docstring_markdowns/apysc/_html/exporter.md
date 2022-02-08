# apysc._html.exporter docstrings

## Module summary

Expression exporting interface implementation.

## _append_common_js_functions function docstring

Append common JavaScript functions (e.g., helper function) to a expression string.<hr>

**[Parameters]**

- `expression`: str
  - Target expression string.

<hr>

**[Returns]**

- `expression`: str
  - Expression string that common functions are appended.

## _append_entry_point_function_call function docstring

Append entry point function call script to html string.<hr>

**[Parameters]**

- `html_str`: str
  - Target HTML string.

<hr>

**[Returns]**

- `html_str`: str
  - After appended html string.

## _append_event_handler_expressions function docstring

Append event handler's expressions to a specified string.<hr>

**[Parameters]**

- `expression`: str
  - Expression string to append event handler's one.

<hr>

**[Returns]**

- `expression`: str
  - Result expression string.

## _append_expression_to_html_str function docstring

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

## _append_head_to_html_str function docstring

Append head tag section to specified html string.<hr>

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

## _append_jslib_str_to_html function docstring

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

## _append_stage_global_variable_to_html function docstring

Append stage's global variable to html string.<hr>

**[Parameters]**

- `html_str`: str
  - Target HTML string.

<hr>

**[Returns]**

- `html_str`: str
  - After appended HTML string.

## _display_debug_mode_ignoring_minify_setting_info function docstring

Display an information of ignoring minify setting if the debug mode is enabled.<hr>

**[Parameters]**

- `minify`: bool
  - Boolean value whether minify HTML and js or not. False setting is useful when debugging.
- `verbose`: int
  - If 0 is specified, message will not be displayed. 1 or the other value will display the message.

<hr>

**[Returns]**

- `msg`: str
  - Displayed message.

## _display_info function docstring

Display an info log message.<hr>

**[Parameters]**

- `msg`: str
  - A message to display.
- `verbose`: int
  - If 0 is specified, message will not be displayed. 1 or the other value will display the message.

<hr>

**[Returns]**

- `msg`: str
  - Displayed message.

## _export_js_libs function docstring

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

## _get_var_name_from_line function docstring

Get a js variable name from specified line string.<hr>

**[Parameters]**

- `line`: str
  - Target line string.

<hr>

**[Returns]**

- `var_name`: str
  - Result variable name. If line contains `var <any_name> = ...;` pattern, then `any_name` will be returned. Or if there is no var expression, blank string will be returned.

## _minify_html function docstring

Minify HTML and js string.<hr>

**[Parameters]**

- `html_str`: str
  - HTML string to minify.
- `minify`: bool
  - Boolean value whether minify HTML and js or not. If False, then minifying will be skipped.

<hr>

**[Returns]**

- `html_str`: str
  - Result html string.

<hr>

**[Notes]**

If the debug mode setting is enabled, minifying will be skipped.

## _remove_blank_lines function docstring

Remove blank (break or spaces only) lines from expression string.<hr>

**[Parameters]**

- `expression`: str
  - Target expression string.

<hr>

**[Returns]**

- `expression`: str
  - Expression string that removed blank lines.

## _remove_unused_js_vars function docstring

Remove unused js variables from expression string.<hr>

**[Parameters]**

- `expression`: str
  - Target js expression string.

<hr>

**[Returns]**

- `expression`: str
  - After removing expression string.

## _save_html function docstring

Save HTML string to file.<hr>

**[Parameters]**

- `html_str`: str
  - HTML String to save.
- `dir_path`: str
  - Destination directory path to save html.
- `file_name`: str
  - HTML file name. e.g., 'index.html'

## _target_js_variable_is_used function docstring

Get a boolean value whether target variable is used in js expression or not.<hr>

**[Parameters]**

- `var_name`: str
  - Target variable name.
- `exp_lines`: list of str
  - js expression lines.

<hr>

**[Returns]**

- `result`: bool
  - If target variable is used in js expression, True will be returned.

## get_entry_point_func_name function docstring

Get an entry point function name.<hr>

**[Returns]**

- `entry_point_func_name`: str
  - An entry point function name.

## save_overall_html function docstring

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

## List class docstring



### __add__ method docstring

Return self+value.

### GenericMeta method docstring

Metaclass for generic types. This is a metaclass for typing.Generic and generic ABCs defined in typing module. User defined subclasses of GenericMeta can override __new__ and invoke super().__new__. Note that GenericMeta.__new__ has strict rules on what is allowed in its bases argument: * plain Generic is disallowed in bases; * Generic[...] should appear in bases at most once; * if Generic[...] is present, then it should list all type variables that appear in other bases. In addition, type of all generic bases is erased, e.g., C[int] is stripped to plain C.

### __contains__ method docstring

Return key in self.

### __delitem__ method docstring

Delete self[key].

### list method docstring

list() -> new empty list list(iterable) -> new list initialized from iterable's items

### __getitem__ method docstring

x.__getitem__(y) <==> x[y]

### __iadd__ method docstring

Implement self+=value.

### __imul__ method docstring

Implement self*=value.

### __init__ method docstring

Initialize self. See help(type(self)) for accurate signature.

### __iter__ method docstring

Implement iter(self).

### __len__ method docstring

Return len(self).

### __mul__ method docstring

Return self*value.

### object method docstring

The most base type

### __reversed__ method docstring

L.__reversed__() -- return a reverse iterator over the list

### __rmul__ method docstring

Return value*self.

### __setitem__ method docstring

Set self[key] to value.

### __sizeof__ method docstring

L.__sizeof__() -- size of L in memory, in bytes

### append method docstring

L.append(object) -> None -- append object to end

### clear method docstring

L.clear() -> None -- remove all items from L

### copy method docstring

L.copy() -> list -- a shallow copy of L

### count method docstring

L.count(value) -> integer -- return number of occurrences of value

### extend method docstring

L.extend(iterable) -> None -- extend list by appending elements from the iterable

### index method docstring

L.index(value, [start, [stop]]) -> integer -- return first index of value. Raises ValueError if the value is not present.

### insert method docstring

L.insert(index, object) -- insert object before index

### pop method docstring

L.pop([index]) -> item -- remove and return item at index (default last). Raises IndexError if list is empty or index is out of range.

### remove method docstring

L.remove(value) -> None -- remove first occurrence of value. Raises ValueError if the value is not present.

### reverse method docstring

L.reverse() -- reverse *IN PLACE*

### sort method docstring

L.sort(key=None, reverse=False) -> None -- stable sort *IN PLACE*

## Logger class docstring

Instances of the Logger class represent a single logging channel. A "logging channel" indicates an area of an application. Exactly how an "area" is defined is up to the application developer. Since an application can have any number of areas, logging channels are identified by a unique string. Application areas can be nested (e.g. an area of "input processing" might include sub-areas "read CSV files", "read XLS files" and "read Gnumeric files"). To cater for this natural nesting, channel names are organized into a namespace hierarchy where levels are separated by periods, much like the Java or Python package namespace. So in the instance given above, channel names might be "input" for the upper level, and "input.csv", "input.xls" and "input.gnu" for the sub-levels. There is no arbitrary limit to the depth of nesting.

Instances of the Logger class represent a single logging channel. A "logging channel" indicates an area of an application. Exactly how an "area" is defined is up to the application developer. Since an application can have any number of areas, logging channels are identified by a unique string. Application areas can be nested (e.g. an area of "input processing" might include sub-areas "read CSV files", "read XLS files" and "read Gnumeric files"). To cater for this natural nesting, channel names are organized into a namespace hierarchy where levels are separated by periods, much like the Java or Python package namespace. So in the instance given above, channel names might be "input" for the upper level, and "input.csv", "input.xls" and "input.gnu" for the sub-levels. There is no arbitrary limit to the depth of nesting.

### __init__ method docstring

Initialize the logger with a name and an optional level.

### _log method docstring

Low-level logging routine which creates a LogRecord and then calls all the handlers of this logger to handle the record.

### addFilter method docstring

Add the specified filter to this handler.

### addHandler method docstring

Add the specified handler to this logger.

### callHandlers method docstring

Pass a record to all relevant handlers. Loop through all handlers for this logger and its parents in the logger hierarchy. If no handler was found, output a one-off error message to sys.stderr. Stop searching up the hierarchy whenever a logger with the "propagate" attribute set to zero is found - that will be the last logger whose handlers are called.

### critical method docstring

Log 'msg % args' with severity 'CRITICAL'. To pass exception information, use the keyword argument exc_info with a true value, e.g. logger.critical("Houston, we have a %s", "major disaster", exc_info=1)

### debug method docstring

Log 'msg % args' with severity 'DEBUG'. To pass exception information, use the keyword argument exc_info with a true value, e.g. logger.debug("Houston, we have a %s", "thorny problem", exc_info=1)

### error method docstring

Log 'msg % args' with severity 'ERROR'. To pass exception information, use the keyword argument exc_info with a true value, e.g. logger.error("Houston, we have a %s", "major problem", exc_info=1)

### exception method docstring

Convenience method for logging an ERROR with exception information.

### critical method docstring

Log 'msg % args' with severity 'CRITICAL'. To pass exception information, use the keyword argument exc_info with a true value, e.g. logger.critical("Houston, we have a %s", "major disaster", exc_info=1)

### filter method docstring

Determine if a record is loggable by consulting all the filters. The default is to allow the record to be logged; any filter can veto this and the record is then dropped. Returns a zero value if a record is to be dropped, else non-zero. .. versionchanged:: 3.2 Allow filters to be just callables.

### findCaller method docstring

Find the stack frame of the caller so that we can note the source file name, line number and function name.

### getChild method docstring

Get a logger which is a descendant to this one. This is a convenience method, such that logging.getLogger('abc').getChild('def.ghi') is the same as logging.getLogger('abc.def.ghi') It's useful, for example, when the parent logger is named using __name__ rather than a literal string.

### getEffectiveLevel method docstring

Get the effective level for this logger. Loop through this logger and its parents in the logger hierarchy, looking for a non-zero logging level. Return the first one found.

### handle method docstring

Call the handlers for the specified record. This method is used for unpickled records received from a socket, as well as those created locally. Logger-level filtering is applied.

### hasHandlers method docstring

See if this logger has any handlers configured. Loop through all handlers for this logger and its parents in the logger hierarchy. Return True if a handler was found, else False. Stop searching up the hierarchy whenever a logger with the "propagate" attribute set to zero is found - that will be the last logger which is checked for the existence of handlers.

### info method docstring

Log 'msg % args' with severity 'INFO'. To pass exception information, use the keyword argument exc_info with a true value, e.g. logger.info("Houston, we have a %s", "interesting problem", exc_info=1)

### isEnabledFor method docstring

Is this logger enabled for level 'level'?

### log method docstring

Log 'msg % args' with the integer severity 'level'. To pass exception information, use the keyword argument exc_info with a true value, e.g. logger.log(level, "We have a %s", "mysterious problem", exc_info=1)

### makeRecord method docstring

A factory method which can be overridden in subclasses to create specialized LogRecords.

### removeFilter method docstring

Remove the specified filter from this handler.

### removeHandler method docstring

Remove the specified handler from this logger.

### setLevel method docstring

Set the logging level of this logger. level must be an int or a str.

### warning method docstring

Log 'msg % args' with severity 'WARNING'. To pass exception information, use the keyword argument exc_info with a true value, e.g. logger.warning("Houston, we have a %s", "bit of a problem", exc_info=1)

## Minifier class docstring

