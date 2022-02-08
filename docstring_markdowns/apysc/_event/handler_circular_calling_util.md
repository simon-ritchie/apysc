# apysc._event.handler_circular_calling_util docstrings

## Module summary

Handler circular calling related utilities.

## _append_handler_name_to_last_of_list function docstring

Append a specified handler's name to the last of the list if the last one is an other handler's name. This function is used to unify last value regardless of `HandlerScope` setting.<hr>

**[Parameters]**

- `handler_name`: str
  - Targer handler name.
- `handler_names`: list of str
  - List to be appended.

<hr>

**[Returns]**

- `handler_names`: list of str
  - Result list value.

## _get_same_name_prev_data function docstring

Get previous handler name and variable name values of the previous same name (but the suffix number is different) handler from the current stack.<hr>

**[Parameters]**

- `handler_name`: str
  - Target handler's name.

<hr>

**[Returns]**

- `prev_hadler_name`: str
  - A previous same name (but the suffix number is different) handler's name value.
- `prev_variable_name`: str
  - A previous variable name value.

<hr>

**[Raises]**

- ValueError: If there is no previous same name handler's name in the SQLite.

## _get_same_name_prev_hadler_name function docstring

Get a previous same name (but the suffix number is different) handler's name from the current stack.<hr>

**[Parameters]**

- `handler_name`: str
  - Target handler's name.

<hr>

**[Returns]**

- `same_name_prev_hadler_name`: str
  - A previous same name (but the suffix number is different) handler's name.

## _get_same_name_prev_variable_name function docstring

Get a previous same name (but the suffix number is different) handler binded variable name from the current stack.<hr>

**[Parameters]**

- `handler_name`: str
  - Target handler's name.

<hr>

**[Returns]**

- `prev_variable_name`: str
  - A previous handler binded instance's variable name.

## _is_already_saved_circular_calling function docstring

Get a boolean indicating whether a specified handler name has been already saved as the circular calling handler or not.<hr>

**[Parameters]**

- `handler_name`: str
  - Target handler's name.

<hr>

**[Returns]**

- `result`: bool
  - If a specified handler name has already been saved as the circular calling handler then True will be returned

## _read_handler_names function docstring

Read the current handler names from the calling stack.<hr>

**[Returns]**

- `handler_names`: list of str
  - Target handler names.

## _save_circular_calling_handler_name function docstring

Save a circular calling handler name to the SQLite.<hr>

**[Parameters]**

- `handler_name`: str
  - Target handler's name.

## get_prev_handler_name function docstring

Get a previous handler's name of a specified handler's one if it is a circular calling handler.<hr>

**[Parameters]**

- `handler_name`: str
  - Target handler's name.

<hr>

**[Returns]**

- `prev_handler_name`: str
  - A previous handler's name. If there is no previous one, then blank string will be returned.

## get_prev_variable_name function docstring

Get a previous handler binded instance's variable name if a specified handler is a circular calling handler.<hr>

**[Parameters]**

- `handler_name`: str
  - Target handler's name.

<hr>

**[Returns]**

- `prev_variable_name`: str
  - A previous handler binded instance's variable name. If there is no previous (same handler's name prefix) one then blank string will be returned.

## is_handler_circular_calling function docstring

Get a boolean value whether a specified handler is a circular call or not.<hr>

**[Parameters]**

- `handler_name`: str
  - Targer handler name.

<hr>

**[Returns]**

- `result`: bool
  - If a specified handler is a circular call, True will be returned.

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

### __init__ method docstring

Initialize self. See help(type(self)) for accurate signature.

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

### __init__ method docstring

Initialize self. See help(type(self)) for accurate signature.

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