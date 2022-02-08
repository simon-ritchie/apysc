# apysc._lint_and_doc.lint_and_doc_hash_util docstrings

## Module summary

The utilities module for each lint and doc's hash file (used to check whether the files are updated or not). Mainly following interfaces are defined: <br>・get_hash_dir_path <br> ・Get a specified type's hash directory path. <br>・get_target_module_hash_file_path <br> ・Get a specified module's hash file path. <br>・read_target_module_hash <br> ・Read a specified module's hashed string. <br>・read_saved_hash <br> ・Read an already-saved module's hashed string. <br>・save_target_module_hash <br> ・Save a target module's current hash. <br>・save_target_modules_hash <br> ・Save target modules' current hash. <br>・is_module_updated <br> ・Get a boolean value whether a specified module has been updated. <br>・remove_not_updated_module_paths <br> ・Remove not updated modules from specified module paths.

## _create_args_list_for_multiprocessing function docstring

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

## _is_module_updated_func_for_multiprocessing function docstring

Wrapper function of the `is_module_updated` function for the multiprocessing.<hr>

**[Parameters]**

- `args`: _IsModuleUpdatedArgs
  - Arguments dictionary to pass to the `is_module_updated` function.

<hr>

**[Returns]**

- `result`: bool
  - If a specified module has been updated then True will be returned.

## get_hash_dir_path function docstring

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

Returned directory path will create automatically if it does not exist.

## get_target_module_hash_file_path function docstring

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

Returned file's directory path will create automatically if it does not exist.

## is_module_updated function docstring

Get a boolean value whether a specified module has been updated.<hr>

**[Parameters]**

- `module_path`: str
  - Target module path.
- `hash_type`: HashType
  - Target hash type.

<hr>

**[Returns]**

- `result`: bool
  - If a specified module has been updated then True will be returned.

## read_saved_hash function docstring

Read an already-saved module's hashed string.<hr>

**[Parameters]**

- `module_path`: str
  - Target module path.
- `hash_type`: HashType
  - Target hash type.

<hr>

**[Returns]**

- `saved_hash`: str
  - An already-saved module's hash string. If there is no saved hash file then a blank string will be returned.

## read_target_module_hash function docstring

Read a specified module's hashed string.<hr>

**[Parameters]**

- `module_path`: str
  - Target module path.

<hr>

**[Returns]**

- `hashed_string`: str
  - Hashed module string. If there is no module at the specified path, then a blank string will be returned.

## remove_not_updated_module_paths function docstring

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

## save_target_module_hash function docstring

Save a target module's current hash.<hr>

**[Parameters]**

- `module_path`: str
  - Target module path.
- `hash_type`: HashType
  - Target hash type.

## save_target_modules_hash function docstring

Save target modules' current hash.<hr>

**[Parameters]**

- `module_paths`: list of str
  - Target module paths.
- `hash_type`: HashType
  - Target hash type.

## Enum class docstring

Generic enumeration. Derive from this class to define new enumerations.

Generic enumeration. Derive from this class to define new enumerations.

### EnumMeta method docstring

Metaclass for Enum

## HashType class docstring

An enumeration.

An enumeration.

### EnumMeta method docstring

Metaclass for Enum

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

## TypedDict class docstring

A simple typed name space. At runtime it is equivalent to a plain dict. TypedDict creates a dictionary type that expects all of its instances to have a certain set of keys, with each key associated with a value of a consistent type. This expectation is not checked at runtime but is only enforced by type checkers. Usage:: class Point2D(TypedDict): x: int y: int label: str a: Point2D = {'x': 1, 'y': 2, 'label': 'good'} # OK b: Point2D = {'z': 3, 'label': 'bad'} # Fails type check assert Point2D(x=1, y=2, label='first') == dict(x=1, y=2, label='first') The type info can be accessed via the Point2D.__annotations__ dict, and the Point2D.__required_keys__ and Point2D.__optional_keys__ frozensets. TypedDict supports two additional equivalent forms:: Point2D = TypedDict('Point2D', x=int, y=int, label=str) Point2D = TypedDict('Point2D', {'x': int, 'y': int, 'label': str}) The class syntax is only supported in Python 3.6+, while two other syntax forms work for Python 2.7 and 3.2+

A simple typed name space. At runtime it is equivalent to a plain dict. TypedDict creates a dictionary type that expects all of its instances to have a certain set of keys, with each key associated with a value of a consistent type. This expectation is not checked at runtime but is only enforced by type checkers. Usage:: class Point2D(TypedDict): x: int y: int label: str a: Point2D = {'x': 1, 'y': 2, 'label': 'good'} # OK b: Point2D = {'z': 3, 'label': 'bad'} # Fails type check assert Point2D(x=1, y=2, label='first') == dict(x=1, y=2, label='first') The type info can be accessed via the Point2D.__annotations__ dict, and the Point2D.__required_keys__ and Point2D.__optional_keys__ frozensets. TypedDict supports two additional equivalent forms:: Point2D = TypedDict('Point2D', x=int, y=int, label=str) Point2D = TypedDict('Point2D', {'x': int, 'y': int, 'label': str}) The class syntax is only supported in Python 3.6+, while two other syntax forms work for Python 2.7 and 3.2+

### __contains__ method docstring

True if D has a key k, else False.

### __delitem__ method docstring

Delete self[key].

### __getitem__ method docstring

x.__getitem__(y) <==> x[y]

### __iter__ method docstring

Implement iter(self).

### __len__ method docstring

Return len(self).

### __setitem__ method docstring

Set self[key] to value.

### __sizeof__ method docstring

D.__sizeof__() -> size of D in memory, in bytes

### clear method docstring

D.clear() -> None. Remove all items from D.

### copy method docstring

D.copy() -> a shallow copy of D

### fromkeys method docstring

Returns a new dict with keys from iterable and values equal to value.

### get method docstring

D.get(k[,d]) -> D[k] if k in D, else d. d defaults to None.

### items method docstring

D.items() -> a set-like object providing a view on D's items

### keys method docstring

D.keys() -> a set-like object providing a view on D's keys

### pop method docstring

D.pop(k[,d]) -> v, remove specified key and return the corresponding value. If key is not found, d is returned if given, otherwise KeyError is raised

### popitem method docstring

D.popitem() -> (k, v), remove and return some (key, value) pair as a 2-tuple; but raise KeyError if D is empty.

### setdefault method docstring

D.setdefault(k[,d]) -> D.get(k,d), also set D[k]=d if k not in D

### update method docstring

D.update([E, ]**F) -> None. Update D from dict/iterable E and F. If E is present and has a .keys() method, then does: for k in E: D[k] = E[k] If E is present and lacks a .keys() method, then does: for k, v in E: D[k] = v In either case, this is followed by: for k in F: D[k] = F[k]

### values method docstring

D.values() -> an object providing a view on D's values

## _IsModuleUpdatedArgs class docstring



### __contains__ method docstring

True if D has a key k, else False.

### __delitem__ method docstring

Delete self[key].

### __getitem__ method docstring

x.__getitem__(y) <==> x[y]

### __iter__ method docstring

Implement iter(self).

### __len__ method docstring

Return len(self).

### __setitem__ method docstring

Set self[key] to value.

### __sizeof__ method docstring

D.__sizeof__() -> size of D in memory, in bytes

### clear method docstring

D.clear() -> None. Remove all items from D.

### copy method docstring

D.copy() -> a shallow copy of D

### fromkeys method docstring

Returns a new dict with keys from iterable and values equal to value.

### get method docstring

D.get(k[,d]) -> D[k] if k in D, else d. d defaults to None.

### items method docstring

D.items() -> a set-like object providing a view on D's items

### keys method docstring

D.keys() -> a set-like object providing a view on D's keys

### pop method docstring

D.pop(k[,d]) -> v, remove specified key and return the corresponding value. If key is not found, d is returned if given, otherwise KeyError is raised

### popitem method docstring

D.popitem() -> (k, v), remove and return some (key, value) pair as a 2-tuple; but raise KeyError if D is empty.

### setdefault method docstring

D.setdefault(k[,d]) -> D.get(k,d), also set D[k]=d if k not in D

### update method docstring

D.update([E, ]**F) -> None. Update D from dict/iterable E and F. If E is present and has a .keys() method, then does: for k in E: D[k] = E[k] If E is present and lacks a .keys() method, then does: for k, v in E: D[k] = v In either case, this is followed by: for k in F: D[k] = F[k]

### values method docstring

D.values() -> an object providing a view on D's values