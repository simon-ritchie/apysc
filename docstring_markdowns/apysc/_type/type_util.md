# apysc._type.type_util docstrings

## Module summary

Type related common implementations. Mainly following interface is defined: <br>・is_number <br> ・Get a boolean value whether specified value is Number value. <br>・is_float_or_number <br> ・Get a boolean value whether specified value is float or Nuber value. <br>・is_bool <br> ・Get a boolean value whether specified value is bool or Boolean value. <br>・is_same_class_instance <br> ・Get a boolean value whether specified class and instance's class are same or not. <br>・is_immutable_type <br> ・Get a boolean value whether specified value is immutable type or not.

## is_bool function docstring

Get a boolean value whether specified value is bool or Boolean value.<hr>

**[Parameters]**

- `value`: *
  - Any value to check.

<hr>

**[Returns]**

- `result`: bool
  - If bool or Boolean value is specified, True will be returned.

## is_float_or_number function docstring

Get a boolean value whether specified value is float or Nuber value.<hr>

**[Parameters]**

- `value`: *
  - Any value to check.

<hr>

**[Returns]**

- `result`: bool
  - If float or Number value is specified, True will be returned.

## is_immutable_type function docstring

Get a boolean value whether specified value is immutable type or not.<hr>

**[Parameters]**

- `value`: Any
  - Target value to check.

<hr>

**[Returns]**

- `result`: bool
  - If a specified value is immutable, then True will be set.

<hr>

**[Notes]**

apysc's value types, such as the `Int`, are checked as immutable since these js types are immutable.

## is_number function docstring

Get a boolean value whether specified value is Number value.<hr>

**[Parameters]**

- `value`: *
  - Any value to check.

<hr>

**[Returns]**

- `result`: bool
  - If Number value is specified, True will be returned.

## is_same_class_instance function docstring

Get a boolean value whether specified class and instance's class are same or not.<hr>

**[Parameters]**

- `class_`: Type
  - Expected class.
- `instance`: *
  - Intance to check it's class.

<hr>

**[Returns]**

- `result`: bool
  - If a specified class and instance's class are same, then True will be set.

<hr>

**[Notes]**

If instance is subclass of `cls` argument, differ from `isinstace`, then False will be returned.

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