# apysc._branch._else docstrings

## Module summary

Else branch instruction implementation.

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

## Else class docstring

A class to append else branch instruction expression.

A class to append else branch instruction expression.<hr>

**[Notes]**

 ・You can only use this class immediately after the `If` or `Elif` statement.<hr>

**[Examples]**

```py
>>> import apysc as ap
>>> int_val: ap.Int = ap.Int(10)
>>> with ap.If(int_val >= 11):
...     ap.trace('Value is greater than equal 11.')
>>> with ap.Else():
...     ap.trace('Value is less than 11.')
```

<hr>

**[References]**

- [Else document](https://simon-ritchie.github.io/apysc/else.html)
- [Each branch instruction class's scope variables reverting setting](https://simon-ritchie.github.io/apysc/branch_instruction_variables_reverting_setting.html)

### ABCMeta method docstring

Metaclass for defining Abstract Base Classes (ABCs). Use this metaclass to create an ABC. An ABC can be subclassed directly, and then acts as a mix-in class. You can also register unrelated concrete classes (even built-in classes) and unrelated ABCs as 'virtual subclasses' -- these and their descendants will be considered subclasses of the registering ABC by the built-in issubclass() function, but the registering ABC won't show up in their MRO (Method Resolution Order) nor will method implementations defined by the registering ABC be callable (not even via super()).

### __enter__ method docstring

Method to be called when begining of with statement.<hr>

**[Returns]**

- `self`: IfBase
  - This instance.

### __exit__ method docstring

Method to be called when end of with statement.<hr>

**[Parameters]**

- `exc_type`: Type
  - Exception type.
- `exc_value`: *
  - Exception value.
- `traceback`: *
  - Traceback value.

### __init__ method docstring

A class to append else branch instruction expression.<hr>

**[Parameters]**

- `locals_`: dict or None, default None
  - Current scope's local variables. Set locals() value to this argument. If specified, this interface reverts all local scope VariableNameInterface variables (like Int, Sprite) at the end of an `Else` scope. This setting is useful when you don't want to update each variable by implementing the `Else` scope.
- `globals_`: dict or None, default None
  - Current scope's global variables. Set globals() value to this argument. This setting works the same way as the locals_ argument.

<hr>

**[Notes]**

 ・You can only use this class immediately after the `If` or `Elif` statement.<hr>

**[Examples]**

```py
>>> import apysc as ap
>>> int_val: ap.Int = ap.Int(10)
>>> with ap.If(int_val >= 11):
...     ap.trace('Value is greater than equal 11.')
>>> with ap.Else():
...     ap.trace('Value is less than 11.')
```

<hr>

**[References]**

- [Else document](https://simon-ritchie.github.io/apysc/else.html)
- [Each branch instruction class's scope variables reverting setting](https://simon-ritchie.github.io/apysc/branch_instruction_variables_reverting_setting.html)

### _append_enter_expression method docstring

Append else branch instruction start expression.<hr>

**[Raises]**

- ValueError: If the last scope is not If or Elif.

### _append_exit_expression method docstring

Append if branch instruction end expression.

### _last_scope_is_if_or_elif method docstring

Get a boolean value whether the last scope is If or Elif.<hr>

**[Returns]**

- `result`: bool
  - If last scope is If or Else, then True will be returned.

### _set_last_scope method docstring

Set expression last scope value.

## IfBase class docstring



### ABCMeta method docstring

Metaclass for defining Abstract Base Classes (ABCs). Use this metaclass to create an ABC. An ABC can be subclassed directly, and then acts as a mix-in class. You can also register unrelated concrete classes (even built-in classes) and unrelated ABCs as 'virtual subclasses' -- these and their descendants will be considered subclasses of the registering ABC by the built-in issubclass() function, but the registering ABC won't show up in their MRO (Method Resolution Order) nor will method implementations defined by the registering ABC be callable (not even via super()).

### __enter__ method docstring

Method to be called when begining of with statement.<hr>

**[Returns]**

- `self`: IfBase
  - This instance.

### __exit__ method docstring

Method to be called when end of with statement.<hr>

**[Parameters]**

- `exc_type`: Type
  - Exception type.
- `exc_value`: *
  - Exception value.
- `traceback`: *
  - Traceback value.

### __init__ method docstring

A class to append if (else if and else) branch instruction expression.<hr>

**[Parameters]**

- `condition`: Boolean or None
  - Boolean value to be used for judgment.
- `locals_`: dict or None, default None
  - Current scope's local variables. Set locals() value to this argument. If specified, all local scope VariableNameInterface variables (like Int, Sprite) will be reverted ad the end of If scope. This setting is useful when you don't want to update each variable by the implementation of the If scope.
- `globals_`: dict or None, default None
  - Current scope's global variables. Set golobals() value to this argument. This works the same way as the locals_ argument.

<hr>

**[References]**

- [If document](https://simon-ritchie.github.io/apysc/if.html)
- [Elif document](https://simon-ritchie.github.io/apysc/elif.html)
- [Else document](https://simon-ritchie.github.io/apysc/else.html)
- [Each branch instruction class's scope variables reverting setting](https://simon-ritchie.github.io/apysc/branch_instruction_variables_reverting_setting.html)

### _append_enter_expression method docstring

Append branch instruction start expression.

### _append_exit_expression method docstring

Append if branch instruction end expression.

### _last_scope_is_if_or_elif method docstring

Get a boolean value whether the last scope is If or Elif.<hr>

**[Returns]**

- `result`: bool
  - If last scope is If or Else, then True will be returned.

### _set_last_scope method docstring

Set expression last scope value.