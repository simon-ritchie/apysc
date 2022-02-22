# `apysc._lint_and_doc.lint_and_doc_hash_util` docstrings

## Module summary

The utilities module for each lint and doc's hash file (used to check whether the files are updated or not). Mainly following interfaces are defined: <br>・get_hash_dir_path <br> ・Get a specified type's hash directory path. <br>・get_target_module_hash_file_path <br> ・Get a specified module's hash file path. <br>・read_target_module_hash <br> ・Read a specified module's hashed string. <br>・read_saved_hash <br> ・Read an already-saved module's hashed string. <br>・save_target_module_hash <br> ・Save a target module's current hash. <br>・save_target_modules_hash <br> ・Save target modules' current hash. <br>・is_module_updated <br> ・Get a boolean value whether a specified module has been updated. <br>・remove_not_updated_module_paths <br> ・Remove not updated modules from specified module paths.

## `_create_args_list_for_multiprocessing` function docstring

Create an arguments list for the multiprocessing.<hr>

**[Parameters]**

- `module_paths`: list of str
  - Target Python module paths.
- `hash_type`: HashType
  - Target hash type.

<hr>

**[Returns]**

- `args_list`: list of _IsModuleUpdatedArgs
  - Created arguments list for the multiprocessing.

## `_is_module_updated_func_for_multiprocessing` function docstring

Wrapper function of the `is_module_updated` function for the multiprocessing.<hr>

**[Parameters]**

- `args`: _IsModuleUpdatedArgs
  - Arguments dictionary to pass to the `is_module_updated` function.

<hr>

**[Returns]**

- `result`: bool
  - If there is an updated module, this interface returns True.

## `get_hash_dir_path` function docstring

Get a specified type's hash directory path.<hr>

**[Parameters]**

- `hash_type`: HashType
  - Target hash type.

<hr>

**[Returns]**

- `dir_path`: str
  - Target type's hash directory path.

<hr>

**[Notes]**

This interface creates a returned directory path if it does not exist.

## `get_target_module_hash_file_path` function docstring

Get a specified module's hash file path.<hr>

**[Parameters]**

- `module_path`: str
  - Target module path.
- `hash_type`: HashType
  - Target hash type.

<hr>

**[Returns]**

- `file_path`: str
  - Target hash file path.

<hr>

**[Notes]**

This interface automatically creates a returned file's directory path if it does not exist.

## `is_module_updated` function docstring

Get a boolean value whether a specified module is changing or not.<hr>

**[Parameters]**

- `module_path`: str
  - Target module path.
- `hash_type`: HashType
  - Target hash type.

<hr>

**[Returns]**

- `result`: bool
  - If a specified module is changing, this interface returns True.

## `read_saved_hash` function docstring

Read an already-saved module's hashed string.<hr>

**[Parameters]**

- `module_path`: str
  - Target module path.
- `hash_type`: HashType
  - Target hash type.

<hr>

**[Returns]**

- `saved_hash`: str
  - An already-saved module's hash string. If there is no saved hash file, this interface returns a blank string.

## `read_target_module_hash` function docstring

Read a specified module's hashed string.<hr>

**[Parameters]**

- `module_path`: str
  - Target module path.

<hr>

**[Returns]**

- `hashed_string`: str
  - Hashed module string. If there is no module at the specified path, this interface returns a blank string.

## `remove_not_updated_module_paths` function docstring

Remove not updated modules from specified module paths.<hr>

**[Parameters]**

- `module_paths`: list of str
  - Target Python module paths.
- `hash_type`: HashType
  - Target hash type.

<hr>

**[Returns]**

- `sliced_module_paths`: list of str
  - After the slicing module paths.

## `save_target_module_hash` function docstring

Save a target module's current hash.<hr>

**[Parameters]**

- `module_path`: str
  - Target module path.
- `hash_type`: HashType
  - Target hash type.

## `save_target_modules_hash` function docstring

Save target modules' current hash.<hr>

**[Parameters]**

- `module_paths`: list of str
  - Target module paths.
- `hash_type`: HashType
  - Target hash type.

## `HashType` class docstring

An enumeration.

## `_IsModuleUpdatedArgs` class docstring