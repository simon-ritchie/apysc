# apysc._callable.callable_util docstrings

## Module summary

Common callable utility implementations.

## get_arg_name_at function docstring

Get specified index argument name from function.<hr>

**[Parameters]**

- `func`: Callable
  - Target function (or method).
- `index`: int
  - Argument index (start from 0).

<hr>

**[Returns]**

- `arg_name`: str
  - Target index's argument name.

## get_func_default_vals function docstring

Get specified function's arguments default values.<hr>

**[Parameters]**

- `func`: Callable
  - Target function (or method).

<hr>

**[Returns]**

- `default_vals`: dict
  - Dictionary that has a argument name at key and default value at value. If argument has no default value, then `empty` object will be set.

## get_method_class_name function docstring

Get a specified method's class name.<hr>

**[Parameters]**

- `method`: Callable
  - Target method.

<hr>

**[Returns]**

- `class_name`: str
  - Target method's class name. If specified argument is not a method (e.g., function), then blank string will be returned.

## get_name_and_arg_value_dict_from_args function docstring

Get dictionary that has an argument name at key and specified argument values at value.<hr>

**[Parameters]**

- `func`: Callable
  - Target function (or method).
- `args`: list
  - Specified positional arguments.
- `kwargs`: dict
  - Specified keyword arguments.

<hr>

**[Returns]**

- `name_and_arg_value_dict`: dict
  - Dictionary that has an argument name at key and specified argument values at value.

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

## Parameter class docstring

Represents a parameter in a function signature. Has the following public attributes: * name : str The name of the parameter as a string. * default : object The default value for the parameter if specified. If the parameter has no default value, this attribute is set to `Parameter.empty`. * annotation The annotation for the parameter if specified. If the parameter has no annotation, this attribute is set to `Parameter.empty`. * kind : str Describes how argument values are bound to the parameter. Possible values: `Parameter.POSITIONAL_ONLY`, `Parameter.POSITIONAL_OR_KEYWORD`, `Parameter.VAR_POSITIONAL`, `Parameter.KEYWORD_ONLY`, `Parameter.VAR_KEYWORD`.

Represents a parameter in a function signature. Has the following public attributes: * name : str The name of the parameter as a string. * default : object The default value for the parameter if specified. If the parameter has no default value, this attribute is set to `Parameter.empty`. * annotation The annotation for the parameter if specified. If the parameter has no annotation, this attribute is set to `Parameter.empty`. * kind : str Describes how argument values are bound to the parameter. Possible values: `Parameter.POSITIONAL_ONLY`, `Parameter.POSITIONAL_OR_KEYWORD`, `Parameter.VAR_POSITIONAL`, `Parameter.KEYWORD_ONLY`, `Parameter.VAR_KEYWORD`.

### _empty method docstring

Marker object for Signature.empty and Parameter.empty.

### replace method docstring

Creates a customized copy of the Parameter.

## Signature class docstring

A Signature object represents the overall signature of a function. It stores a Parameter object for each parameter accepted by the function, as well as information specific to the function itself. A Signature object has the following public attributes and methods: * parameters : OrderedDict An ordered mapping of parameters' names to the corresponding Parameter objects (keyword-only arguments are in the same order as listed in `code.co_varnames`). * return_annotation : object The annotation for the return type of the function if specified. If the function has no annotation for its return type, this attribute is set to `Signature.empty`. * bind(*args, **kwargs) -> BoundArguments Creates a mapping from positional and keyword arguments to parameters. * bind_partial(*args, **kwargs) -> BoundArguments Creates a partial mapping from positional and keyword arguments to parameters (simulating 'functools.partial' behavior.)

A Signature object represents the overall signature of a function. It stores a Parameter object for each parameter accepted by the function, as well as information specific to the function itself. A Signature object has the following public attributes and methods: * parameters : OrderedDict An ordered mapping of parameters' names to the corresponding Parameter objects (keyword-only arguments are in the same order as listed in `code.co_varnames`). * return_annotation : object The annotation for the return type of the function if specified. If the function has no annotation for its return type, this attribute is set to `Signature.empty`. * bind(*args, **kwargs) -> BoundArguments Creates a mapping from positional and keyword arguments to parameters. * bind_partial(*args, **kwargs) -> BoundArguments Creates a partial mapping from positional and keyword arguments to parameters (simulating 'functools.partial' behavior.)

### __init__ method docstring

Constructs Signature from the given list of Parameter objects and 'return_annotation'. All arguments are optional.

### _bind method docstring

Private method. Don't use directly.

### BoundArguments method docstring

Result of `Signature.bind` call. Holds the mapping of arguments to the function's parameters. Has the following public attributes: * arguments : OrderedDict An ordered mutable mapping of parameters' names to arguments' values. Does not contain arguments' default values. * signature : Signature The Signature object that created this instance. * args : tuple Tuple of positional arguments values. * kwargs : dict Dict of keyword arguments values.

### Parameter method docstring

Represents a parameter in a function signature. Has the following public attributes: * name : str The name of the parameter as a string. * default : object The default value for the parameter if specified. If the parameter has no default value, this attribute is set to `Parameter.empty`. * annotation The annotation for the parameter if specified. If the parameter has no annotation, this attribute is set to `Parameter.empty`. * kind : str Describes how argument values are bound to the parameter. Possible values: `Parameter.POSITIONAL_ONLY`, `Parameter.POSITIONAL_OR_KEYWORD`, `Parameter.VAR_POSITIONAL`, `Parameter.KEYWORD_ONLY`, `Parameter.VAR_KEYWORD`.

### bind method docstring

Get a BoundArguments object, that maps the passed `args` and `kwargs` to the function's signature. Raises `TypeError` if the passed arguments can not be bound.

### bind_partial method docstring

Get a BoundArguments object, that partially maps the passed `args` and `kwargs` to the function's signature. Raises `TypeError` if the passed arguments can not be bound.

### _empty method docstring

Marker object for Signature.empty and Parameter.empty.

### from_builtin method docstring

Constructs Signature for the given builtin function. Deprecated since Python 3.5, use `Signature.from_callable()`.

### from_callable method docstring

Constructs Signature for the given callable object.

### from_function method docstring

Constructs Signature for the given python function. Deprecated since Python 3.5, use `Signature.from_callable()`.

### replace method docstring

Creates a customized copy of the Signature. Pass 'parameters' and/or 'return_annotation' arguments to override them in the new copy.

## _empty class docstring

Marker object for Signature.empty and Parameter.empty.

Marker object for Signature.empty and Parameter.empty.

### __init__ method docstring

Initialize self. See help(type(self)) for accurate signature.