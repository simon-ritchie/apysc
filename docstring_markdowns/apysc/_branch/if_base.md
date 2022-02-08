# apysc._branch.if_base docstrings

## Module summary

Abstract base class implementation for if, elif, and else.

## abstractmethod function docstring

A decorator indicating abstract methods. Requires that the metaclass is ABCMeta or derived from it. A class that has a metaclass derived from ABCMeta cannot be instantiated unless all of its abstract methods are overridden. The abstract methods can be called using any of the normal 'super' call mechanisms. Usage: class C(metaclass=ABCMeta): @abstractmethod def my_abstract_method(self, ...): ...

## ABC class docstring

Helper class that provides a standard way to create an ABC using inheritance.

Helper class that provides a standard way to create an ABC using inheritance.

### ABCMeta method docstring

Metaclass for defining Abstract Base Classes (ABCs). Use this metaclass to create an ABC. An ABC can be subclassed directly, and then acts as a mix-in class. You can also register unrelated concrete classes (even built-in classes) and unrelated ABCs as 'virtual subclasses' -- these and their descendants will be considered subclasses of the registering ABC by the built-in issubclass() function, but the registering ABC won't show up in their MRO (Method Resolution Order) nor will method implementations defined by the registering ABC be callable (not even via super()).

### __init__ method docstring

Initialize self. See help(type(self)) for accurate signature.

## Boolean class docstring

Boolean class for the apysc library.

Boolean class for the apysc library.<hr>

**[Notes]**

The Bool class is the alias of the Boolean, and it behaves the same as the Boolean class.<hr>

**[Examples]**

```py
>>> import apysc as ap
>>> bool_val_1: ap.Boolean = ap.Boolean(True)
>>> bool_val_1
Boolean(True)

>>> bool_val_2: ap.Bool = ap.Bool(True)
>>> bool_val_2
Boolean(True)

>>> bool_val_2.not_
Boolean(False)
```

<hr>

**[References]**

- [Boolean document](https://simon-ritchie.github.io/apysc/boolean.html)

### __bool__ method docstring

Get a boolean value directly.<hr>

**[Returns]**

- `result`: bool
  - Current boolean value.

### ABCMeta method docstring

Metaclass for defining Abstract Base Classes (ABCs). Use this metaclass to create an ABC. An ABC can be subclassed directly, and then acts as a mix-in class. You can also register unrelated concrete classes (even built-in classes) and unrelated ABCs as 'virtual subclasses' -- these and their descendants will be considered subclasses of the registering ABC by the built-in issubclass() function, but the registering ABC won't show up in their MRO (Method Resolution Order) nor will method implementations defined by the registering ABC be callable (not even via super()).

### __eq__ method docstring

Comparison method for equal condition.<hr>

**[Parameters]**

- `other`: *
  - Other value to compare (Boolean, bool, int, or Int).

<hr>

**[Returns]**

- `result`: Boolean
  - Comparison result.

### __init__ method docstring

Boolean class for apysc library.<hr>

**[Parameters]**

- `value`: bool or int or Boolean or Int
  - Initial boolean value. 0 or 1 are acceptable for an integer value.

<hr>

**[Notes]**

The Bool class is the alias of the Boolean, and it behaves the same as the Boolean class.<hr>

**[Examples]**

```py
>>> import apysc as ap
>>> bool_val_1: ap.Boolean = ap.Boolean(True)
>>> bool_val_1
Boolean(True)

>>> bool_val_2: ap.Bool = ap.Bool(True)
>>> bool_val_2
Boolean(True)
```

<hr>

**[References]**

- [Boolean document](https://simon-ritchie.github.io/apysc/boolean.html)

### __ne__ method docstring

Comparison method for not equal condition.<hr>

**[Parameters]**

- `other`: *
  - Other value to compare (Boolean, bool, int, or Int).

<hr>

**[Returns]**

- `result`: Boolean
  - Comparison result.

### __repr__ method docstring

Get a representation string of this instance.<hr>

**[Returns]**

- `repr_str`: str
  - Representation string of this instance.

### _append_constructor_expression method docstring

Append constructor expression.

### _append_copy_expression method docstring

Append copy expression.<hr>

**[Parameters]**

- `result_variable_name`: str
  - Copied value's variable name.

### _append_custom_event_binding_expression method docstring

Append a custom event binding expression.<hr>

**[Parameters]**

- `custom_event_type_str`: str
  - Target custom event type string.
- `name`: str
  - Handler's name.

### _append_custom_event_unbinding_expression method docstring

Add a custom event unbinding expression.<hr>

**[Parameters]**

- `custom_event_type_str`: str
  - Target custom event type string.
- `name`: str
  - Handler's name.

### _append_eq_expression method docstring

Append __eq__ method expression.<hr>

**[Parameters]**

- `result`: Boolean
  - Result boolean value.
- `other`: Boolean or Int
  - Other value to compare.

### _append_ne_expression method docstring

Append __ne__ method expression.<hr>

**[Parameters]**

- `result`: Boolean
  - Result boolean value.
- `other`: Boolean or Int
  - Other value to compare.

### _append_not_prop_expression method docstring

Append not_ property expression.<hr>

**[Parameters]**

- `result`: Boolean
  - Result Boolean value.

### _append_value_setter_expression method docstring

Append value's setter expression.<hr>

**[Parameters]**

- `value`: bool or VariableNameInterface
  - Any value to set.

### _append_value_updating_cpy_exp_to_handler_scope method docstring

Append a value updating copy expression if the current scope is an event handler's one.<hr>

**[Parameters]**

- `result_variable_name`: str
  - Copied value's variable name.

### _copy method docstring

Make a deep copy of this instance.<hr>

**[Returns]**

- `result`: *
  - Copied instance.

### _delete_snapshot_exists_val method docstring

Delete boolean value whether snapshot value exists or not.<hr>

**[Parameters]**

- `snapshot_name`: str
  - Target snapshot name.

### _get_bool_from_arg_value method docstring

Get bool value from specified argument value.<hr>

**[Parameters]**

- `value`: bool or int or Boolean or Int
  - Specified value. 0 or 1 are acceptable for integer value.

<hr>

**[Returns]**

- `result`: bool
  - Converted boolean value.

### _get_custom_event_type_str method docstring

Get a custom event type string from a type value.<hr>

**[Parameters]**

- `custom_event_type`: CustomEventType or str
  - Target custom event type or string.

<hr>

**[Returns]**

- `custom_event_type_str`: str
  - A custom event type string.

### _get_next_snapshot_name method docstring

Get a next snapshot name.<hr>

**[Returns]**

- `snapshot_name`: str
  - Next snapshot name.

### _get_previous_variable_name method docstring

Get a previous variable name.<hr>

**[Returns]**

- `previous_variable_name`: str
  - A previous variable name of this instance. If that value is not existing, then a blank string will be returned.

### _initialize_blank_object_if_not_initialized method docstring

Initialize a blank object value if it hasn't been initialized yet.

### _initialize_custom_event_handlers_if_not_initialized method docstring

Initialize the _custom_event_handlers data if it hasn't been initialized yet.<hr>

**[Parameters]**

- `custom_event_type_str`: str
  - Target custom event type string.

### _initialize_ss_exists_val_if_not_initialized method docstring

Initialize _snapshot_exists_ value it hasn't been initialized yet.

### _make_snapshot method docstring

Make value's snapshot.<hr>

**[Parameters]**

- `snapshot_name`: str
  - Target snapshot name.

### _revert method docstring

Revert value if snapshot exists.<hr>

**[Parameters]**

- `snapshot_name`: str
  - Target snapshot name.

### _run_all_make_snapshot_methods method docstring

Run all _make_snapshot methods. If instance is multiple inheritance one, and each has RevertInterface, then each _make_snapshot methods will be called.<hr>

**[Parameters]**

- `snapshot_name`: str
  - Target snapshot name.

### _run_all_revert_methods method docstring

Run all _revert methods. If instance is multiple inheritance one, and each has RevertInterface, then each _revert methods will be called.<hr>

**[Parameters]**

- `snapshot_name`: str
  - Target snapshot name.

### _run_base_cls_make_snapshot_methods_recursively method docstring

Run base classes make_snapshot methods recursively.<hr>

**[Parameters]**

- `class_`: type
  - Target type.
- `snapshot_name`: str
  - Target snapshot name.

### _run_base_cls_revert_methods_recursively method docstring

Run base classes revert methods recursively.<hr>

**[Parameters]**

- `class_`: type
  - Target type.
- `snapshot_name`: str
  - Target snapshot name.

### _set_custom_event_handler_data method docstring

Set a handler's data to the dictionary.<hr>

**[Parameters]**

- `handler`: _Handler
  - Callable will be called when an event is dispatched.
- `custom_event_type_str`: str
  - Target custom event type string.
- `options`: dict or None
  - Optional arguments dictionary to be passed to a handler.

### _set_single_snapshot_val_to_dict method docstring

Set a single snapshot value to the specified name dictionary.<hr>

**[Parameters]**

- `dict_name`: str
  - Target dictionary name.
- `value`: Any
  - Target value.
- `snapshot_name`: str
  - Target snapshot name.

<hr>

**[Notes]**

If a snapshot value of the same name already exists, the process will be stopped.

### _set_snapshot_exists_val method docstring

Set boolean value whether snapshot value exists or not.<hr>

**[Parameters]**

- `snapshot_name`: str
  - Target snapshot name.

### _set_value_and_skip_expression_appending method docstring

Update value attribute and skip expression appending.<hr>

**[Parameters]**

- `value`: bool or int or Boolean or Int
  - Any boolean value to set.

### _snapshot_exists method docstring

Get a boolean value whether snapshot value exists or not.<hr>

**[Parameters]**

- `snapshot_name`: str
  - Target snapshot name.

<hr>

**[Returns]**

- `snapshot_exists`: bool
  - Boolean value whether snapshot value exists or not.

### _unset_custom_event_handler_data method docstring

Unset a handler's data from the dictionary.<hr>

**[Parameters]**

- `handler`: _Handler
  - Callable will be called when an event is dispatched.
- `custom_event_type_str`: str
  - Target custom event type string.

### _validate_comparison_other_type method docstring

Validate comparison's other value type.<hr>

**[Parameters]**

- `other`: *
  - Other value to compare.

<hr>

**[Raises]**

- ValueError: If other value type is not Boolean, bool, Int, and int.

### bind_custom_event method docstring

Add a custom event listener setting.<hr>

**[Parameters]**

- `custom_event_type`: CustomEventType or str
  - Target custom event type.
- `handler`: _Handler
  - A handler will be called when the custom event is triggered.
- `e`: Event
  - Event instance.
- `options`: dict or None, default None
  - Optional arguments dictionary to be passed to a handler.
- `in_handler_head_expression`: str, default ''
  - Optional expression to be added at the handler function's head position.

<hr>

**[Returns]**

- `name`: str
  - Handler's name.

<hr>

**[Examples]**

```py
>>> import apysc as ap
>>> def on_custom_event(
...         e: ap.Event[ap.Rectangle], options: dict) -> None:
...     rectangle: ap.Rectangle = e.this
...     rectangle.fill_color = ap.String('#f0a')
>>> stage: ap.Stage = ap.Stage()
>>> sprite: ap.Sprite = ap.Sprite()
>>> sprite.graphics.begin_fill(color='#0af')
>>> rectangle: ap.Rectangle = sprite.graphics.draw_rect(
...     x=50, y=50, width=50, height=50)
>>> e: ap.Event = ap.Event(this=rectangle)
>>> _ = rectangle.bind_custom_event(
...     custom_event_type='my_custom_event',
...     handler=on_custom_event, e=e)
>>> # Do something here and then trigger the custom event
>>> rectangle.trigger_custom_event(
...     custom_event_type='my_custom_event')
```

<hr>

**[References]**

- [Bind and trigger the custom event document](https://simon-ritchie.github.io/apysc/bind_and_trigger_custom_event.html)
- [About the handler options' type document](https://simon-ritchie.github.io/apysc/about_handler_options_type.html)

### trigger_custom_event method docstring

Add a custom event trigger setting.<hr>

**[Parameters]**

- `custom_event_type`: CustomEventType or str
  - Target custom event type.

<hr>

**[Examples]**

```py
>>> import apysc as ap
>>> def on_custom_event(
...         e: ap.Event[ap.Rectangle], options: dict) -> None:
...     rectangle: ap.Rectangle = e.this
...     rectangle.fill_color = ap.String('#f0a')
>>> stage: ap.Stage = ap.Stage()
>>> sprite: ap.Sprite = ap.Sprite()
>>> sprite.graphics.begin_fill(color='#0af')
>>> rectangle: ap.Rectangle = sprite.graphics.draw_rect(
...     x=50, y=50, width=50, height=50)
>>> e: ap.Event = ap.Event(this=rectangle)
>>> _ = rectangle.bind_custom_event(
...     custom_event_type='my_custom_event',
...     handler=on_custom_event, e=e)
>>> # Do something here and then trigger the custom event
>>> rectangle.trigger_custom_event(
...     custom_event_type='my_custom_event')
```

<hr>

**[References]**

- [Bind and trigger the custom event document](https://simon-ritchie.github.io/apysc/bind_and_trigger_custom_event.html)

### unbind_custom_event method docstring

Unbind (remove) a custom event listener setting.<hr>

**[Parameters]**

- `custom_event_type`: CustomEventType or str
  - Target custom event type.
- `handler`: _Handler
  - A handler for when the custom event is triggered.

<hr>

**[Returns]**

- `name`: str
  - Handler's name.

<hr>

**[Examples]**

```py
>>> import apysc as ap
>>> def on_custom_event(
...         e: ap.Event[ap.Rectangle], options: dict) -> None:
...     rectangle: ap.Rectangle = e.this
...     rectangle.fill_color = ap.String('#f0a')
...     rectangle.unbind_custom_event(
...         custom_event_type='my_custom_event',
...         handler=on_custom_event)
>>> stage: ap.Stage = ap.Stage()
>>> sprite: ap.Sprite = ap.Sprite()
>>> sprite.graphics.begin_fill(color='#0af')
>>> rectangle: ap.Rectangle = sprite.graphics.draw_rect(
...     x=50, y=50, width=50, height=50)
>>> e: ap.Event = ap.Event(this=rectangle)
>>> _ = rectangle.bind_custom_event(
...     custom_event_type='my_custom_event',
...     handler=on_custom_event, e=e)
>>> # Do something here and then trigger the custom event
>>> rectangle.trigger_custom_event(
...     custom_event_type='my_custom_event')
```

### unbind_custom_event_all method docstring

Unbind (remove) custom event listener settings.<hr>

**[Parameters]**

- `custom_event_type`: CustomEventType or str
  - Target custom event type.

<hr>

**[Examples]**

```py
>>> import apysc as ap
>>> def on_custom_event(
...         e: ap.Event[ap.Rectangle], options: dict) -> None:
...     rectangle: ap.Rectangle = e.this
...     rectangle.fill_color = ap.String('#f0a')
...     rectangle.unbind_custom_event_all(
...         custom_event_type='my_custom_event')
>>> stage: ap.Stage = ap.Stage()
>>> sprite: ap.Sprite = ap.Sprite()
>>> sprite.graphics.begin_fill(color='#0af')
>>> rectangle: ap.Rectangle = sprite.graphics.draw_rect(
...     x=50, y=50, width=50, height=50)
>>> e: ap.Event = ap.Event(this=rectangle)
>>> _ = rectangle.bind_custom_event(
...     custom_event_type='my_custom_event',
...     handler=on_custom_event, e=e)
>>> # Do something here and then trigger the custom event
>>> rectangle.trigger_custom_event(
...     custom_event_type='my_custom_event')
```

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