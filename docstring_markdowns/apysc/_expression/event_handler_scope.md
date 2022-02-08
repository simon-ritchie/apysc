# apysc._expression.event_handler_scope docstrings

## Module summary

Implementations for the event handler's expression scope interfaces.

## _decrement_scope_count function docstring

Decrement current scope count.

## _delete_handler_calling_stack function docstring

Delete the handler calling stack data from the SQLite.<hr>

**[Parameters]**

- `handler_name`: str
  - Target handler's name.

## _increment_scope_count function docstring

Increment current scope count.

## _save_current_scope_count function docstring

Save current scope count.<hr>

**[Parameters]**

- `count`: int
  - Scope count ot save.

## _save_handler_calling_stack function docstring

Save the handler calling stack data to the SQLite.<hr>

**[Parameters]**

- `handler_name`: str
  - Target handler's name.
- `instance`: VariableNameInterface
  - Instance will be binded the target handler.

## get_current_event_handler_scope_count function docstring

Get a current event handler's scope count.<hr>

**[Returns]**

- `scope_count`: int
  - Current event handler's scope count. If normal handler's call, then 1 will be returned, or call other handler in handler's function, then 2 or more count will be returned.

## remove_suffix_num_from_handler_name function docstring

Remove the suffix number from a specified handler name.<hr>

**[Parameters]**

- `handler_name`: str
  - Target handler's name.

<hr>

**[Returns]**

- `handler_name`: str
  - Result handler's name.

## HandlerScope class docstring

Class for a handler scope. This is used at a with statement.

Class for a handler scope. This is used at a with statement.

### __enter__ method docstring

Enter and set an event handler scope setting.

### __exit__ method docstring

Exit and remove an event handler scope setting.<hr>

**[Parameters]**

- `*args`: list
  - Positional arguments.

### __init__ method docstring

Class for a handler scope. This is used at a with statement.<hr>

**[Parameters]**

- `handler_name`: str
  - Target handler's name.
- `instance`: VariableNameInterface
  - Instance will be binded the target handler.

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

## TemporaryNotHandlerScope class docstring

Class temporarily sets up a scope that is not a handler. This is used at a with statement.

Class temporarily sets up a scope that is not a handler. This is used at a with statement.

### __enter__ method docstring

Enter and set the scope count to zero.

### __exit__ method docstring

Exit and revert the scope count.<hr>

**[Parameters]**

- `*args`: list
  - Positional arguments.

### __init__ method docstring

Class temporarily sets up a scope that is not a handler. This is used at a with statement.

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

## VariableNameInterface class docstring



### _get_previous_variable_name method docstring

Get a previous variable name.<hr>

**[Returns]**

- `previous_variable_name`: str
  - A previous variable name of this instance. If that value is not existing, then a blank string will be returned.