# apysc._html.debug_mode docstrings

## Module summary

Debugging mode setting interface implementations for the HTML and JavaScript.

## _get_callable_count function docstring

Get a specified callable count number.<hr>

**[Parameters]**

- `callable_`: Callable or str
  - Target function or method or property or dunder method name.
- `module_name`: str
  - Module name. This value will be set the `__name__` value.
- `class_`: Type or None, optional
  - Target class type. If the target callable_ variable is not a method, this argument will be ignored.

<hr>

**[Returns]**

- `callable_count`: int
  - Target count number.

## _get_callable_path_name function docstring

Get a specified callable count data path name.<hr>

**[Parameters]**

- `callable_`: Callable or str
  - Target function or method or property or dunder method name.
- `module_name`: str
  - Module name. This value will be set the `__name__` value.
- `class_`: Type or None, optional
  - Target class type. If the target callable_ variable is not a method, this argument will be ignored.

<hr>

**[Returns]**

- `path_name`: str
  - Target path name.

## _get_callable_str function docstring

Get a callable string (label).<hr>

**[Parameters]**

- `callable_`: Callable or str
  - Target function or method or property or dunder method name.

<hr>

**[Returns]**

- `callable_str`: str
  - A callable string (label).

## _increment_callable_count function docstring

Increment a specified callable count number.<hr>

**[Parameters]**

- `callable_`: Callable or str
  - Target function or method or property or dunder method name.
- `module_name`: str
  - Module name. This value will be set the `__name__` value.
- `class_`: Type or None, optional
  - Target class type. If the target callable_ variable is not a method, this argument will be ignored.

## is_debug_mode function docstring

Get a boolean value whether the current debug mode is enabled or not.<hr>

**[Returns]**

- `result`: bool
  - If the current debug mode is enabled, True will be returned.

<hr>

**[Examples]**

```py
>>> import apysc as ap
>>> stage: ap.Stage = ap.Stage()
>>> ap.set_debug_mode()
>>> ap.is_debug_mode()
True

>>> int_val: ap.Int = ap.Int(10)
>>> ap.unset_debug_mode()
>>> ap.is_debug_mode()
False
```

## set_debug_mode function docstring

Set the debug mode for the HTML and JavaScript debugging. This interface applies the following setting if calling this function: <br> ・Disabling HTML minify setting. <br> ・Changing to append per each interface JavaScript divider string.<hr>

**[Examples]**

```py
>>> import apysc as ap
>>> stage: ap.Stage = ap.Stage()
>>> ap.set_debug_mode()
>>> int_val: ap.Int = ap.Int(10)
```

<hr>

**[References]**

- [set_debug_mode interface document](https://simon-ritchie.github.io/apysc/set_debug_mode.html)

## unset_debug_mode function docstring

Unset the debug mode for the HTML and JavaScript debugging.<hr>

**[Examples]**

```py
>>> import apysc as ap
>>> stage: ap.Stage = ap.Stage()
>>> ap.set_debug_mode()
>>> int_val: ap.Int = ap.Int(10)
>>> ap.unset_debug_mode()
```

<hr>

**[References]**

- [unset_debug_mode interface document](https://simon-ritchie.github.io/apysc/unset_debug_mode.html)

## Callable class docstring

Callable type; Callable[[int], str] is a function of (int) -> str. The subscription syntax must always be used with exactly two values: the argument list and the return type. The argument list must be a list of types or ellipsis; the return type must be a single type. There is no syntax to indicate optional or keyword arguments, such function types are rarely used as callback types.

Callable type; Callable[[int], str] is a function of (int) -> str. The subscription syntax must always be used with exactly two values: the argument list and the return type. The argument list must be a list of types or ellipsis; the return type must be a single type. There is no syntax to indicate optional or keyword arguments, such function types are rarely used as callback types.

### CallableMeta method docstring

Metaclass for Callable (internal).

### __init__ method docstring

Initialize self. See help(type(self)) for accurate signature.

### object method docstring

The most base type

### Callable method docstring

Callable type; Callable[[int], str] is a function of (int) -> str. The subscription syntax must always be used with exactly two values: the argument list and the return type. The argument list must be a list of types or ellipsis; the return type must be a single type. There is no syntax to indicate optional or keyword arguments, such function types are rarely used as callback types.

## DebugInfo class docstring

Save a debug information (append callable interface name comment and arguments information) to the JavaScript expression file. This class is used at the `with` statement.

Save a debug information (append callable interface name comment and arguments information) to the JavaScript expression file. This class is used at the `with` statement.<hr>

**[Notes]**

If the debug mode setting is not enabled, saving will be skipped.<hr>

**[Examples]**

```py
>>> import apysc as ap
>>> stage: ap.Stage = ap.Stage()
>>> def any_func(a: int, b: str) -> None:
...     with ap.DebugInfo(
...             callable_=any_func, locals_=locals(),
...             module_name=__name__):
...         int_val: ap.Int = ap.Int(10)
```

<hr>

**[References]**

- [DebugInfo class document](https://simon-ritchie.github.io/apysc/debug_info.html)

### __enter__ method docstring

The method will be called at the start of the with block.

### __exit__ method docstring

The method will be called at the end of the with block.<hr>

**[Parameters]**

- `*args`: list
  - Positional arguments.

### __init__ method docstring

Save debug information (append callable interface name comment and arguments information) to the JavaScript expression file. This class needs to use the `with` statement when instantiating.<hr>

**[Parameters]**

- `callable_`: Callable or str
  - Target function or method or property or dunder method name.
- `locals_`: dict
  - Local variables. This value requires a `locals()` function's value.
- `module_name`: str
  - Module name. This value requires the `__name__` value.
- `class_`: Type or None, optional
  - Target class type. If the target callable_ variable is not a method, this interface ignores this argument.

<hr>

**[Notes]**

If the debug mode setting is not enabled, this interface skips the saving.<hr>

**[Examples]**

```py
>>> import apysc as ap
>>> stage: ap.Stage = ap.Stage()
>>> def any_func(a: int, b: str) -> None:
...     with ap.DebugInfo(
...             callable_=any_func, locals_=locals(),
...             module_name=__name__):
...         int_val: ap.Int = ap.Int(10)
```

<hr>

**[References]**

- [DebugInfo class document](https://simon-ritchie.github.io/apysc/debug_info.html)

### _get_class_info method docstring

Get a class information string.<hr>

**[Returns]**

- `class_info`: str
  - Target class information string.

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

### __init__ method docstring

Initialize self. See help(type(self)) for accurate signature.

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

## Indent class docstring

Class implementation for increment and decrement indentation number. Basically use this class at with statement.

Class implementation for increment and decrement indentation number. Basically use this class at with statement.

### __enter__ method docstring

Method to be used by with statement. This method will increment indentation number.

### __exit__ method docstring

Method to be used by with statement. This method will decrement indentation number.<hr>

**[Parameters]**

- `*args`: list
  - Any positional arguments.

### __init__ method docstring

Initialize self. See help(type(self)) for accurate signature.

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

## Type class docstring

A special construct usable to annotate class objects. For example, suppose we have the following classes:: class User: ... # Abstract base for User classes class BasicUser(User): ... class ProUser(User): ... class TeamUser(User): ... And a function that takes a class argument that's a subclass of User and returns an instance of the corresponding class:: U = TypeVar('U', bound=User) def new_user(user_class: Type[U]) -> U: user = user_class() # (Here we could write the user object to a database) return user joe = new_user(BasicUser) At this point the type checker knows that joe has type BasicUser.

A special construct usable to annotate class objects. For example, suppose we have the following classes:: class User: ... # Abstract base for User classes class BasicUser(User): ... class ProUser(User): ... class TeamUser(User): ... And a function that takes a class argument that's a subclass of User and returns an instance of the corresponding class:: U = TypeVar('U', bound=User) def new_user(user_class: Type[U]) -> U: user = user_class() # (Here we could write the user object to a database) return user joe = new_user(BasicUser) At this point the type checker knows that joe has type BasicUser.

### GenericMeta method docstring

Metaclass for generic types. This is a metaclass for typing.Generic and generic ABCs defined in typing module. User defined subclasses of GenericMeta can override __new__ and invoke super().__new__. Note that GenericMeta.__new__ has strict rules on what is allowed in its bases argument: * plain Generic is disallowed in bases; * Generic[...] should appear in bases at most once; * if Generic[...] is present, then it should list all type variables that appear in other bases. In addition, type of all generic bases is erased, e.g., C[int] is stripped to plain C.

### __init__ method docstring

Initialize self. See help(type(self)) for accurate signature.

### object method docstring

The most base type

### Type method docstring

A special construct usable to annotate class objects. For example, suppose we have the following classes:: class User: ... # Abstract base for User classes class BasicUser(User): ... class ProUser(User): ... class TeamUser(User): ... And a function that takes a class argument that's a subclass of User and returns an instance of the corresponding class:: U = TypeVar('U', bound=User) def new_user(user_class: Type[U]) -> U: user = user_class() # (Here we could write the user object to a database) return user joe = new_user(BasicUser) At this point the type checker knows that joe has type BasicUser.