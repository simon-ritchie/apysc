# `apysc._lint_and_doc.lint_and_doc_hash_util` docstrings

## Module summary

The utilities module for each lint and doc's hash file (used to check whether the files are updated or not). Mainly following interfaces are defined: <br>・get_hash_dir_path <br> ・Get a specified type's hash directory path. <br>・get_target_file_hash_file_path <br> ・Get a specified file's hash file path. <br>・read_target_file_hash <br> ・Read a specified file's hashed string. <br>・read_saved_hash <br> ・Read an already-saved file's hashed string. <br>・save_target_file_hash <br> ・Save a target file's current hash. <br>・save_target_files_hash <br> ・Save target files' current hash. <br>・is_file_updated <br> ・Get a boolean value whether a specified file has been updated. <br>・remove_not_updated_file_paths <br> ・Remove not updated files from specified file paths.

## `_create_args_list_for_multiprocessing` function docstring

Create an arguments list for the multiprocessing.<hr>

**[Parameters]**

- `file_paths`: list of str
  - Target file paths.
- `hash_type`: HashType
  - Target hash type.

<hr>

**[Returns]**

- `args_list`: list of _IsFileUpdatedArgs
  - Created arguments list for the multiprocessing.

## `_is_file_updated_func_for_multiprocessing` function docstring

Wrapper function of the `is_file_updated` function for the multiprocessing.<hr>

**[Parameters]**

- `args`: _IsFileUpdatedArgs
  - Arguments dictionary to pass to the `is_file_updated` function.

<hr>

**[Returns]**

- `result`: bool
  - If there is an updated file, this interface returns True.

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

## `get_target_file_hash_file_path` function docstring

Get a specified file's hash file path.<hr>

**[Parameters]**

- `file_path`: str
  - Target file path.
- `hash_type`: HashType
  - Target hash type.

<hr>

**[Returns]**

- `file_path`: str
  - Target hash file path.

<hr>

**[Notes]**

This interface automatically creates a returned file's directory path if it does not exist.

## `is_file_updated` function docstring

Get a boolean value whether a specified file is changing or not.<hr>

**[Parameters]**

- `file_path`: str
  - Target file path.
- `hash_type`: HashType
  - Target hash type.

<hr>

**[Returns]**

- `result`: bool
  - If a specified file is changing, this interface returns True.

## `read_saved_hash` function docstring

Read an already-saved file's hashed string.<hr>

**[Parameters]**

- `file_path`: str
  - Target file path.
- `hash_type`: HashType
  - Target hash type.

<hr>

**[Returns]**

- `saved_hash`: str
  - An already-saved file's hash string. If there is no saved hash file, this interface returns a blank string.

## `read_target_file_hash` function docstring

Read a specified file's hashed string.<hr>

**[Parameters]**

- `file_path`: str
  - Target file path.

<hr>

**[Returns]**

- `hashed_string`: str
  - Hashed file string. If there is no file at the specified path, this interface returns a blank string.

## `remove_not_updated_file_paths` function docstring

Remove not updated files from specified file paths.<hr>

**[Parameters]**

- `file_paths`: list of str
  - Target file paths.
- `hash_type`: HashType
  - Target hash type.

<hr>

**[Returns]**

- `sliced_file_paths`: list of str
  - After the slicing file paths.

## `save_target_file_hash` function docstring

Save a target file's current hash.<hr>

**[Parameters]**

- `file_path`: str
  - Target file path.
- `hash_type`: HashType
  - Target hash type.

## `save_target_files_hash` function docstring

Save target files' current hash.<hr>

**[Parameters]**

- `file_paths`: list of str
  - Target file paths.
- `hash_type`: HashType
  - Target hash type.

## `HashType` class docstring

An enumeration.

## `_IsFileUpdatedArgs` class docstring