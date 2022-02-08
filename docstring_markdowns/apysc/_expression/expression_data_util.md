# apysc._expression.expression_data_util docstrings

## Module summary

The implementation of manipulating HTL and js expression files. Mainly following interfaces are defined: <br>・empty_expression : Empty the current js expression data. <br>・append_js_expression : Append js expression. <br>・get_current_expression : Get current expression string. <br>・get_current_event_handler_scope_expression : Get a current event handler scope's expression string. <br>・exec_query : Execute a SQLite sql query.

## _check_connection function docstring

The decorator function to check a SQLite connection when a specified function calling, and if failed, create a new connection and recall a function.<hr>

**[Parameters]**

- `func`: Callable
  - Target function to decorate.

<hr>

**[Returns]**

- `new_func`: Callable
  - Decorated function.

## new_func function docstring

Function for the decoration.<hr>

**[Parameters]**

- `*args`: list
  - Any positional arguments.
- `**kwargs`: dict
  - Any keyword arguments.

<hr>

**[Returns]**

- `result`: Any
  - Any returned value.

## new_func function docstring

Function for the decoration.<hr>

**[Parameters]**

- `*args`: list
  - Any positional arguments.
- `**kwargs`: dict
  - Any keyword arguments.

<hr>

**[Returns]**

- `result`: Any
  - Any returned value.

## new_func function docstring

Function for the decoration.<hr>

**[Parameters]**

- `*args`: list
  - Any positional arguments.
- `**kwargs`: dict
  - Any keyword arguments.

<hr>

**[Returns]**

- `result`: Any
  - Any returned value.

## new_func function docstring

Function for the decoration.<hr>

**[Parameters]**

- `*args`: list
  - Any positional arguments.
- `**kwargs`: dict
  - Any keyword arguments.

<hr>

**[Returns]**

- `result`: Any
  - Any returned value.

## new_func function docstring

Function for the decoration.<hr>

**[Parameters]**

- `*args`: list
  - Any positional arguments.
- `**kwargs`: dict
  - Any keyword arguments.

<hr>

**[Returns]**

- `result`: Any
  - Any returned value.

## new_func function docstring

Function for the decoration.<hr>

**[Parameters]**

- `*args`: list
  - Any positional arguments.
- `**kwargs`: dict
  - Any keyword arguments.

<hr>

**[Returns]**

- `result`: Any
  - Any returned value.

## new_func function docstring

Function for the decoration.<hr>

**[Parameters]**

- `*args`: list
  - Any positional arguments.
- `**kwargs`: dict
  - Any keyword arguments.

<hr>

**[Returns]**

- `result`: Any
  - Any returned value.

## new_func function docstring

Function for the decoration.<hr>

**[Parameters]**

- `*args`: list
  - Any positional arguments.
- `**kwargs`: dict
  - Any keyword arguments.

<hr>

**[Returns]**

- `result`: Any
  - Any returned value.

## new_func function docstring

Function for the decoration.<hr>

**[Parameters]**

- `*args`: list
  - Any positional arguments.
- `**kwargs`: dict
  - Any keyword arguments.

<hr>

**[Returns]**

- `result`: Any
  - Any returned value.

## new_func function docstring

Function for the decoration.<hr>

**[Parameters]**

- `*args`: list
  - Any positional arguments.
- `**kwargs`: dict
  - Any keyword arguments.

<hr>

**[Returns]**

- `result`: Any
  - Any returned value.

## new_func function docstring

Function for the decoration.<hr>

**[Parameters]**

- `*args`: list
  - Any positional arguments.
- `**kwargs`: dict
  - Any keyword arguments.

<hr>

**[Returns]**

- `result`: Any
  - Any returned value.

## new_func function docstring

Function for the decoration.<hr>

**[Parameters]**

- `*args`: list
  - Any positional arguments.
- `**kwargs`: dict
  - Any keyword arguments.

<hr>

**[Returns]**

- `result`: Any
  - Any returned value.

## new_func function docstring

Function for the decoration.<hr>

**[Parameters]**

- `*args`: list
  - Any positional arguments.
- `**kwargs`: dict
  - Any keyword arguments.

<hr>

**[Returns]**

- `result`: Any
  - Any returned value.

## new_func function docstring

Function for the decoration.<hr>

**[Parameters]**

- `*args`: list
  - Any positional arguments.
- `**kwargs`: dict
  - Any keyword arguments.

<hr>

**[Returns]**

- `result`: Any
  - Any returned value.

## _get_current_expression function docstring

Get a current expression string from a specified table.<hr>

**[Parameters]**

- `table_name`: TableName
  - Target table name.

<hr>

**[Returns]**

- `current_expression`: str
  - Current expression string.

## _get_expression_table_name function docstring

Get a expression table name. This value will be switched whether current scope is event handler's one or not.<hr>

**[Returns]**

- `table_name`: str
  - Target expression table name.

## _make_create_table_query function docstring

Make a create table sql query.<hr>

**[Parameters]**

- `table_name`: str
  - Target table name.
- `column_ddl`: str
  - Target table columns DDL string. e.g., ' id INTEGER, ...'

<hr>

**[Returns]**

- `query`: str
  - A create table sql query.

## new_func function docstring

Function for the decoration.<hr>

**[Parameters]**

- `*args`: list
  - Any positional arguments.
- `**kwargs`: dict
  - Any keyword arguments.

<hr>

**[Returns]**

- `result`: Any
  - Any returned value.

## _validate_limit_clause function docstring

Validate whether a LIMIT clause is used in a UPDATE or DELETE sql.<hr>

**[Parameters]**

- `sql`: str
  - Target sql.

<hr>

**[Raises]**

- _LimitClauseCantUseError: If the LIMIT clause used in a DELETE or UPDATE sql.

## append_js_expression function docstring

Append js expression.<hr>

**[Parameters]**

- `expression`: str
  - JavaScript Expression string.

<hr>

**[Examples]**

```py
>>> import apysc as ap
>>> ap.append_js_expression(expression='console.log("Hello!")')
```

<hr>

**[References]**

- [append_js_expression interface document](https://simon-ritchie.github.io/apysc/append_js_expression.html)

## empty_expression function docstring

Empty the current js expression data.

## exec_query function docstring

Execute a SQLite sql query.<hr>

**[Parameters]**

- `sql`: str
  - Target sql.
- `commit`: bool, default True
  - A boolean value whether commit the transaction after the sql query or not.

<hr>

**[Raises]**

- _LimitClauseCantUseError: If the LIMIT clause used in a DELETE or UPDATE sql.

## get_current_event_handler_scope_expression function docstring

Get a current event handler scope's expression string.<hr>

**[Returns]**

- `current_expression`: str
  - Current expression's string.

<hr>

**[Notes]**

If it is necessary to get normal scope's expression, then use get_current_expression function instead.

## get_current_expression function docstring

Get a current expression's string.<hr>

**[Returns]**

- `current_expression`: str
  - Current expression's string.

<hr>

**[Notes]**

If it is necessary to get event handler scope's expression, then use get_current_event_handler_scope_expression function instead.

## initialize_sqlite_tables_if_not_initialized function docstring

Initialize the sqlite tables if they have not been initialized yet.<hr>

**[Returns]**

- `initialized`: bool
  - If initialized, returns True.

## Callable class docstring

Callable type; Callable[[int], str] is a function of (int) -> str. The subscription syntax must always be used with exactly two values: the argument list and the return type. The argument list must be a list of types or ellipsis; the return type must be a single type. There is no syntax to indicate optional or keyword arguments, such function types are rarely used as callback types.

Callable type; Callable[[int], str] is a function of (int) -> str. The subscription syntax must always be used with exactly two values: the argument list and the return type. The argument list must be a list of types or ellipsis; the return type must be a single type. There is no syntax to indicate optional or keyword arguments, such function types are rarely used as callback types.

### CallableMeta method docstring

Metaclass for Callable (internal).

### object method docstring

The most base type

### Callable method docstring

Callable type; Callable[[int], str] is a function of (int) -> str. The subscription syntax must always be used with exactly two values: the argument list and the return type. The argument list must be a list of types or ellipsis; the return type must be a single type. There is no syntax to indicate optional or keyword arguments, such function types are rarely used as callback types.

## Enum class docstring

Generic enumeration. Derive from this class to define new enumerations.

Generic enumeration. Derive from this class to define new enumerations.

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

## TableName class docstring

An enumeration.

An enumeration.

### EnumMeta method docstring

Metaclass for Enum

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

## TypeVar class docstring

Type variable. Usage:: T = TypeVar('T') # Can be anything A = TypeVar('A', str, bytes) # Must be str or bytes Type variables exist primarily for the benefit of static type checkers. They serve as the parameters for generic types as well as for generic function definitions. See class Generic for more information on generic types. Generic functions work as follows: def repeat(x: T, n: int) -> List[T]: '''Return a list containing n references to x.''' return [x]*n def longest(x: A, y: A) -> A: '''Return the longest of two strings.''' return x if len(x) >= len(y) else y The latter example's signature is essentially the overloading of (str, str) -> str and (bytes, bytes) -> bytes. Also note that if the arguments are instances of some subclass of str, the return type is still plain str. At runtime, isinstance(x, T) and issubclass(C, T) will raise TypeError. Type variables defined with covariant=True or contravariant=True can be used do declare covariant or contravariant generic types. See PEP 484 for more details. By default generic types are invariant in all type variables. Type variables can be introspected. e.g.: T.__name__ == 'T' T.__constraints__ == () T.__covariant__ == False T.__contravariant__ = False A.__constraints__ == (str, bytes)

Type variable. Usage:: T = TypeVar('T') # Can be anything A = TypeVar('A', str, bytes) # Must be str or bytes Type variables exist primarily for the benefit of static type checkers. They serve as the parameters for generic types as well as for generic function definitions. See class Generic for more information on generic types. Generic functions work as follows: def repeat(x: T, n: int) -> List[T]: '''Return a list containing n references to x.''' return [x]*n def longest(x: A, y: A) -> A: '''Return the longest of two strings.''' return x if len(x) >= len(y) else y The latter example's signature is essentially the overloading of (str, str) -> str and (bytes, bytes) -> bytes. Also note that if the arguments are instances of some subclass of str, the return type is still plain str. At runtime, isinstance(x, T) and issubclass(C, T) will raise TypeError. Type variables defined with covariant=True or contravariant=True can be used do declare covariant or contravariant generic types. See PEP 484 for more details. By default generic types are invariant in all type variables. Type variables can be introspected. e.g.: T.__name__ == 'T' T.__constraints__ == () T.__covariant__ == False T.__contravariant__ = False A.__constraints__ == (str, bytes)

### TypingMeta method docstring

Metaclass for most types defined in typing module (not a part of public API). This overrides __new__() to require an extra keyword parameter '_root', which serves as a guard against naive subclassing of the typing classes. Any legitimate class defined using a metaclass derived from TypingMeta must pass _root=True. This also defines a dummy constructor (all the work for most typing constructs is done in __new__) and a nicer repr().

### __new__ method docstring

Constructor. This only exists to give a better error message in case someone tries to subclass a special typing object (not a good idea).

## _LimitClauseCantUseError class docstring



### with_traceback method docstring

Exception.with_traceback(tb) -- set self.__traceback__ to tb and return self.