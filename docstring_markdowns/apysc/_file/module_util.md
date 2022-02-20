# `apysc._file.module_util` docstrings

## Module summary

Module related common utilities. Mainly following interfaces are defined: <br>・get_module_paths_recursively <br> ・Get all module paths under the specified directory. <br>・save_tmp_module <br> ・Save a temporary Python module. <br>・save_tmp_module_and_run_script <br> ・Save a temporary Python module and run that script. <br>・read_target_path_module <br> ・Read a module of the specified module path. <br>・read_module_or_class_from_package_path <br> ・Read a specified package path module or class.

## `get_module_paths_recursively` function docstring

Get all module paths under the specified directory.<hr>

**[Parameters]**

- `dir_path`: str
  - Directory path to search modules.
- `module_paths`: list of str or None
  - Current Python module paths (only used by recursive function calls).

<hr>

**[Returns]**

- `module_paths`: list of str
  - Python module paths. This interface does not include the `__init__.py` modules.

## `read_module_or_class_from_package_path` function docstring

Read a specified package path module or class.<hr>

**[Parameters]**

- `module_or_class_package_path`: str
  - Target package module or class path.

<hr>

**[Returns]**

- `module_or_class`: ModuleType or Type
  - Read module or class.

## `read_target_path_module` function docstring

Read a module of the specified module path.<hr>

**[Parameters]**

- `module_path`: str
  - Target module path.

<hr>

**[Returns]**

- `module`: ModuleType
  - Read module.

## `save_tmp_module` function docstring

Save a temporary Python module.<hr>

**[Parameters]**

- `script`: str
  - Python script string.

<hr>

**[Returns]**

- `saved_module_path`: str
  - Saved temporary module path.

## `save_tmp_module_and_run_script` function docstring

Save a temporary Python module and run that script.<hr>

**[Parameters]**

- `script`: str
  - Python script string.

<hr>

**[Returns]**

- `stdout`: str
  - Result stdout string.