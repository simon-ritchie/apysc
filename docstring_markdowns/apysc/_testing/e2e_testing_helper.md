# `apysc._testing.e2e_testing_helper` docstrings

## Module summary

This module is for the E2E testing common utilities and definitions.

## `_assert_local_file_error_log_not_exits` function docstring

Assert that local file assertion's an error log does not exist.<hr>

**[Parameters]**

- `file_path`: str
  - A target file path.

<hr>

**[Raises]**

- AssertionError: If there is an error log file.

## `_delete_local_file_assertion_error_logs` function docstring

Delete local files assertion error logs files if they exist.<hr>

**[Parameters]**

- `file_path`: str
  - A target local file path.

## `_get_local_file_assertion_err_file_path` function docstring

Get an assertion error log's file path of a local file.<hr>

**[Parameters]**

- `file_path`: str
  - A target local file path.

<hr>

**[Returns]**

- `log_file_path`: str
  - An assertion error log's file path of a local file.

## `_get_local_file_console_event_handler` function docstring

Get a console event's handler.<hr>

**[Parameters]**

- `file_path`: str
  - A target local file path.
- `expected_assert_f_msgs`: list of str or None, default None
  - Expected assertion failed messages.

<hr>

**[Returns]**

- `handler`: Callable
  - A target handler.

## `_get_local_file_page_err_file_path` function docstring

Get a page error log's file path of a local file.<hr>

**[Parameters]**

- `file_path`: str
  - A target local file path.

<hr>

**[Returns]**

- `log_file_path`: str
  - A page error's log file path of a local file.

## `_get_local_file_page_err_handler` function docstring

Get a page error's event handler.<hr>

**[Parameters]**

- `file_path`: str
  - A target local file path.

<hr>

**[Returns]**

- `handler`: Callable
  - A target handler.

## `_replace_paths_symbols_by_underscore` function docstring

Replace the path's symbols with the underscore symbol.<hr>

**[Parameters]**

- `file_path`: str
  - A target file path.

<hr>

**[Returns]**

- `file_path`: str
  - A result file path.

## `assert_local_files_not_raise_error` function docstring

Assert specified local files do not raise an error.<hr>

**[Parameters]**

- `local_file_data_list`: List[LocalFileData]
  - A target local file data list.

<hr>

**[Raises]**

- AssertionError: If specified files raise an exception.

## `get_docs_local_file_path` function docstring

Get a document's local file path for the E2E testing.<hr>

**[Parameters]**

- `lang`: Lang
  - A target language.
- `file_name`: str
  - A target file name (e.g., `index`).

<hr>

**[Returns]**

- `file_path`: str
  - A target document's local file path.

## `LocalFileData` class docstring