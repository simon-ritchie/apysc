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

## module class docstring

module(name[, doc]) Create a module object. The name must be a string; the optional doc argument can have any type.

module(name[, doc]) Create a module object. The name must be a string; the optional doc argument can have any type.

### __dir__ method docstring

__dir__() -> list specialized dir() implementation