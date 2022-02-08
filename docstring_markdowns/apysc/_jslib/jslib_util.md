# apysc._jslib.jslib_util docstrings

## Module summary

Common JavaScript library utility implementations. Mainly the following interfaces are defined: <br>・get_jslib_file_names Get the JavaScript libraries file names. <br>・get_jslib_abs_dir_path Get the Javascript library's absolute directory path. <br>・export_jslib_to_specified_dir Export a JavaScript library to specified directory. <br>・read_jslib_str Read a JavaScript library file str.

## export_jslib_to_specified_dir function docstring

Export a JavaScript library to specified directory.<hr>

**[Parameters]**

- `dest_dir_path`: str
  - Directory path to export JavaScript library file.
- `jslib_name`: str
  - JavaScript file name to export.

<hr>

**[Returns]**

- `dest_file_path`: str
  - Exported Javascript library's file path.

<hr>

**[Raises]**

- FileNotFoundError: If specified JavaScript file is not found.

## get_jslib_abs_dir_path function docstring

Get the Javascript library's absolute directory path.<hr>

**[Returns]**

- `jslib_abs_dir_path`: str
  - Javascript library's absolute directory path. This module's directory will be set.

## get_jslib_file_names function docstring

Get the JavaScript libraries file names.<hr>

**[Returns]**

- `jslib_file_names`: list of str
  - JavaScript libraries file names existing in this module's directory. e.g., ['jquery.min.js', 'svg.min.js']

## read_jslib_str function docstring

Read a JavaScript library file str.<hr>

**[Parameters]**

- `jslib_name`: str
  - JavaScript file name to read.

<hr>

**[Returns]**

- `jslib_str`: str
  - Read JavaScript library string.

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