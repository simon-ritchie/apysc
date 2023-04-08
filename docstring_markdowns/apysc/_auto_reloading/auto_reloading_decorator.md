# `apysc._auto_reloading.auto_reloading_decorator` docstrings

## Module summary

The decorator implementation for the auto-reloading.

## `_are_files_updated` function docstring

Get a boolean, whether files are updated or not.<hr>

**[Parameters]**

- `last_executed_time`: datetime
  - A last execution time.
- `checking_dir_paths`: List[str]
  - Directory paths to check for file changes.

<hr>

**[Returns]**

- `result`: bool
  - If any updated files exist, this interface returns True.

## `set_auto_reloading` function docstring

Set an auto-reloading setting as a decorator.<hr>

**[Parameters]**

- `checking_dir_paths`: List[str]
  - Directory paths to check for file changes.
- `max_checking_num`: Optional[int], optional
  - Maximum checking attempts number. Mainly this interface uses this setting for the testing.

<hr>

**[Returns]**

- `wrapped`: Callable
  - Wrapped callable object.

<hr>

**[Notes]**

Currently, this setting checks only `.py` files.