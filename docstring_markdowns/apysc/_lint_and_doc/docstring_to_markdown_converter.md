# apysc._lint_and_doc.docstring_to_markdown_converter docstrings

## Module summary

The script to convert and sync each docstring to markdown files.

## _append_each_section_to_markdown function docstring

Append each docstring section to a specified markdown string.<hr>

**[Parameters]**

- `markdown`: str
  - Target markdown string.
- `docstring`: str
  - Target docstring.

<hr>

**[Returns]**

- `markdown`: str
  - Result markdown string.

## _append_module_docstring_to_markdown function docstring

Append a module description docstring to a specified markdown string.<hr>

**[Parameters]**

- `markdown`: str
  - Target markdown string.
- `docstring`: str or None
  - Target module description docstring.

<hr>

**[Returns]**

- `markdown`: str
  - Result markdown string.

## _append_toplevel_class_docstring_to_markdown function docstring

Append a top-level class docstring to a specified markdown string.<hr>

**[Parameters]**

- `markdown`: str
  - Target markdown string.
- `toplevel_class`: Type
  - Target top-level class.

<hr>

**[Returns]**

- `markdown`: str
  - Result markdown string.

## _append_toplevel_function_docstring_to_markdown function docstring

Append a top-level function docstring to a specified markdown string.<hr>

**[Parameters]**

- `markdown`: str
  - Target markdown string.
- `toplevel_function`: Callable
  - Target top-level functions.

<hr>

**[Returns]**

- `markdown`: str
  - Result markdown string.

## _convert_module_docstring_to_markdown function docstring

Convert a specified module's docstring to a markdown string.<hr>

**[Parameters]**

- `module`: ModuleType
  - Target module.

<hr>

**[Returns]**

- `markdown`: str
  - Converted markdown string.

## _get_excluding_target_builtin_methods function docstring

Get a excluding target builtin methods' docstring values dict.<hr>

**[Returns]**

- `excluding_target_builtin_methods_dict`: dict
  - A dictionary which has builtin method name's keys and docstring values.

## _get_methods_from_class function docstring

Get methods from a specified class.<hr>

**[Parameters]**

- `class_`: Type
  - Target class.

<hr>

**[Returns]**

- `methods`: list of Callable
  - Extracted methods.

## _get_module_toplevel_functions function docstring

Get top-level functions from a specified module.<hr>

**[Parameters]**

- `module`: ModuleType
  - Target module.

<hr>

**[Returns]**

- `toplevel_functions`: list of Callable
  - Top-level functions.

## _get_toplevel_classes function docstring

Get top-level classes from a specified module.<hr>

**[Parameters]**

- `module`: ModuleType
  - Target module.

<hr>

**[Returns]**

- `toplevel_classes`: list of Type
  - Top-level classes.

## _save_markdown function docstring

Save a specified module's markdown file.<hr>

**[Parameters]**

- `module_path`: str
  - Target Python module path.

<hr>

**[Returns]**

- `markdown_file_path`: str
  - Saved markdown file path.

## convert_recursively function docstring

Convert each docstring in the specified directory to markdown files recursively.<hr>

**[Parameters]**

- `dir_path`: str
  - Target directory path.

<hr>

**[Returns]**

- `saved_markdown_file_paths`: list of str
  - list of saved markdown file paths.

## Callable class docstring

Callable type; Callable[[int], str] is a function of (int) -> str. The subscription syntax must always be used with exactly two values: the argument list and the return type. The argument list must be a list of types or ellipsis; the return type must be a single type. There is no syntax to indicate optional or keyword arguments, such function types are rarely used as callback types.

Callable type; Callable[[int], str] is a function of (int) -> str. The subscription syntax must always be used with exactly two values: the argument list and the return type. The argument list must be a list of types or ellipsis; the return type must be a single type. There is no syntax to indicate optional or keyword arguments, such function types are rarely used as callback types.

### CallableMeta method docstring

Metaclass for Callable (internal).

### object method docstring

The most base type

### Callable method docstring

Callable type; Callable[[int], str] is a function of (int) -> str. The subscription syntax must always be used with exactly two values: the argument list and the return type. The argument list must be a list of types or ellipsis; the return type must be a single type. There is no syntax to indicate optional or keyword arguments, such function types are rarely used as callback types.

## Dict class docstring



### GenericMeta method docstring

Metaclass for generic types. This is a metaclass for typing.Generic and generic ABCs defined in typing module. User defined subclasses of GenericMeta can override __new__ and invoke super().__new__. Note that GenericMeta.__new__ has strict rules on what is allowed in its bases argument: * plain Generic is disallowed in bases; * Generic[...] should appear in bases at most once; * if Generic[...] is present, then it should list all type variables that appear in other bases. In addition, type of all generic bases is erased, e.g., C[int] is stripped to plain C.

### __contains__ method docstring

True if D has a key k, else False.

### __delitem__ method docstring

Delete self[key].

### dict method docstring

dict() -> new empty dictionary dict(mapping) -> new dictionary initialized from a mapping object's (key, value) pairs dict(iterable) -> new dictionary initialized as if via: d = {} for k, v in iterable: d[k] = v dict(**kwargs) -> new dictionary initialized with the name=value pairs in the keyword argument list. For example: dict(one=1, two=2)

### __getitem__ method docstring

x.__getitem__(y) <==> x[y]

### __iter__ method docstring

Implement iter(self).

### __len__ method docstring

Return len(self).

### object method docstring

The most base type

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

## Tuple class docstring

Tuple type; Tuple[X, Y] is the cross-product type of X and Y. Example: Tuple[T1, T2] is a tuple of two elements corresponding to type variables T1 and T2. Tuple[int, float, str] is a tuple of an int, a float and a string. To specify a variable-length tuple of homogeneous type, use Tuple[T, ...].

Tuple type; Tuple[X, Y] is the cross-product type of X and Y. Example: Tuple[T1, T2] is a tuple of two elements corresponding to type variables T1 and T2. Tuple[int, float, str] is a tuple of an int, a float and a string. To specify a variable-length tuple of homogeneous type, use Tuple[T, ...].

### __add__ method docstring

Return self+value.

### TupleMeta method docstring

Metaclass for Tuple (internal).

### __contains__ method docstring

Return key in self.

### tuple method docstring

tuple() -> empty tuple tuple(iterable) -> tuple initialized from iterable's items If the argument is a tuple, the return value is the same object.

### __getitem__ method docstring

Return self[key].

### __iter__ method docstring

Implement iter(self).

### __len__ method docstring

Return len(self).

### __mul__ method docstring

Return self*value.

### object method docstring

The most base type

### __rmul__ method docstring

Return value*self.

### Tuple method docstring

Tuple type; Tuple[X, Y] is the cross-product type of X and Y. Example: Tuple[T1, T2] is a tuple of two elements corresponding to type variables T1 and T2. Tuple[int, float, str] is a tuple of an int, a float and a string. To specify a variable-length tuple of homogeneous type, use Tuple[T, ...].

### count method docstring

T.count(value) -> integer -- return number of occurrences of value

### index method docstring

T.index(value, [start, [stop]]) -> integer -- return first index of value. Raises ValueError if the value is not present.

## Type class docstring

A special construct usable to annotate class objects. For example, suppose we have the following classes:: class User: ... # Abstract base for User classes class BasicUser(User): ... class ProUser(User): ... class TeamUser(User): ... And a function that takes a class argument that's a subclass of User and returns an instance of the corresponding class:: U = TypeVar('U', bound=User) def new_user(user_class: Type[U]) -> U: user = user_class() # (Here we could write the user object to a database) return user joe = new_user(BasicUser) At this point the type checker knows that joe has type BasicUser.

A special construct usable to annotate class objects. For example, suppose we have the following classes:: class User: ... # Abstract base for User classes class BasicUser(User): ... class ProUser(User): ... class TeamUser(User): ... And a function that takes a class argument that's a subclass of User and returns an instance of the corresponding class:: U = TypeVar('U', bound=User) def new_user(user_class: Type[U]) -> U: user = user_class() # (Here we could write the user object to a database) return user joe = new_user(BasicUser) At this point the type checker knows that joe has type BasicUser.

### GenericMeta method docstring

Metaclass for generic types. This is a metaclass for typing.Generic and generic ABCs defined in typing module. User defined subclasses of GenericMeta can override __new__ and invoke super().__new__. Note that GenericMeta.__new__ has strict rules on what is allowed in its bases argument: * plain Generic is disallowed in bases; * Generic[...] should appear in bases at most once; * if Generic[...] is present, then it should list all type variables that appear in other bases. In addition, type of all generic bases is erased, e.g., C[int] is stripped to plain C.

### object method docstring

The most base type

### Type method docstring

A special construct usable to annotate class objects. For example, suppose we have the following classes:: class User: ... # Abstract base for User classes class BasicUser(User): ... class ProUser(User): ... class TeamUser(User): ... And a function that takes a class argument that's a subclass of User and returns an instance of the corresponding class:: U = TypeVar('U', bound=User) def new_user(user_class: Type[U]) -> U: user = user_class() # (Here we could write the user object to a database) return user joe = new_user(BasicUser) At this point the type checker knows that joe has type BasicUser.