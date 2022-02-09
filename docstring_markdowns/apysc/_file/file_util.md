# apysc._file.file_util docstrings

## Module summary

Files' common utilities implementation. Mainly following interfaces are defined: <br>・empty_directory <br> ・Empty specified directory. <br>・read_txt <br> ・Read specified file's text. <br>・save_plain_txt <br> ・Save plain text string to file. <br>・append_plain_txt <br> ・Append plain text string to file. <br>・remove_file_if_exists <br> ・Remove specified file if exists. <br>・get_abs_directory_path_from_file_path <br> ・Get an absolute directory path of specified file. <br>・get_abs_module_dir_path <br> ・Get a specified module's abosulute directory path. <br>・get_specified_ext_file_paths_recursively <br> ・Get specified extension file paths recursively. <br>・count_files_recursively <br> ・Count the existing files number in a specified directory.

## append_plain_txt function docstring

Append plain text string to file.<hr>

**[Parameters]**

- `txt`: str
  - Plain text string to append.
- `file_path`: str
  - Destination file path.

## count_files_recursively function docstring

Count the existing files number in a specified directory recursively.<hr>

**[Parameters]**

- `dir_path`: str
  - Target directory path.

<hr>

**[Returns]**

- `count`: int
  - Existing files count.

## empty_directory function docstring

Empty specified directory.<hr>

**[Parameters]**

- `directory_path`: str
  - Directory path to empty. This folder itself will not be removed.

## get_abs_directory_path_from_file_path function docstring

Get an absolute directory path of specified file.<hr>

**[Parameters]**

- `file_path`: str
  - Target file path.

<hr>

**[Returns]**

- `dir_path`: str
  - An absolute directory path.

## get_abs_module_dir_path function docstring

Get a specified module's abosulute directory path.<hr>

**[Parameters]**

- `module`: ModuleType
  - Target module.

<hr>

**[Returns]**

- `abs_module_dir_path`: str
  - Specified module's abosulute directory path.

## get_specified_ext_file_paths_recursively function docstring

Get specified extension file paths recursively.<hr>

**[Parameters]**

- `extension`: str
  - Target file extension (e.g., '.md', 'md', and so on).
- `dir_path`: str
  - Directory path to search files recursively.
- `file_paths`: list of str or None
  - Current file paths (only used for recursive function calls).

<hr>

**[Returns]**

- `file_paths`: list of str
  - File paths that end with target extension.

## read_txt function docstring

Read specified file's text.<hr>

**[Parameters]**

- `file_path`: str
  - File path to read.

<hr>

**[Returns]**

- `txt`: str
  - Target file's text.

## remove_file_if_exists function docstring

Remove specified file if exists.<hr>

**[Parameters]**

- `file_path`: str
  - File path to remove.

## save_plain_txt function docstring

Save plain text string to file.<hr>

**[Parameters]**

- `txt`: str
  - Plain text string to save.
- `file_path`: str
  - Destination file path.