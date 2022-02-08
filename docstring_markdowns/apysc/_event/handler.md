# apysc._event.handler docstrings

## Module summary

Class implementation for handler.

## _append_in_handler_head_expression function docstring

Append an in-handler head expression if it is not blank.<hr>

**[Parameters]**

- `in_handler_head_expression`: str
  - Optional expression to be added at the handler function's head position if it is not blank.

## append_handler_expression function docstring

Append a handler's expression.<hr>

**[Parameters]**

- `handler_data`: HandlerData
  - Target handler's data to append.
- `handler_name`: str
  - Target handler's name.
- `e`: Event
  - Created event instance.
- `in_handler_head_expression`: str, default ''
  - Optional expression to be added at the handler function's head position.

## append_unbinding_all_expression function docstring

Append all events unbinding expression.<hr>

**[Parameters]**

- `this`: VariableNameInterface
  - Instance that events are binded.
- `mouse_event_type`: MouseEventType
  - Event type to unbind.

## append_unbinding_expression function docstring

Append event unbinding expression.<hr>

**[Parameters]**

- `this`: VariableNameInterface
  - Instance that event is binded.
- `handler_name`: str
  - Target handler's name.
- `mouse_event_type`: MouseEventType
  - Event type to unbind.

## get_handler_name function docstring

Get a handler name.<hr>

**[Parameters]**

- `handler`: _Handler
  - Target handler.
- `instance`: VariableNameInterface
  - Instance to bind target handler.

<hr>

**[Returns]**

- `handler_name`: str
  - Handler name (method path + class name (if handler is method) + function or method name) + instance's variable name.

## Callable class docstring

Callable type; Callable[[int], str] is a function of (int) -> str. The subscription syntax must always be used with exactly two values: the argument list and the return type. The argument list must be a list of types or ellipsis; the return type must be a single type. There is no syntax to indicate optional or keyword arguments, such function types are rarely used as callback types.

Callable type; Callable[[int], str] is a function of (int) -> str. The subscription syntax must always be used with exactly two values: the argument list and the return type. The argument list must be a list of types or ellipsis; the return type must be a single type. There is no syntax to indicate optional or keyword arguments, such function types are rarely used as callback types.

### CallableMeta method docstring

Metaclass for Callable (internal).

### object method docstring

The most base type

### Callable method docstring

Callable type; Callable[[int], str] is a function of (int) -> str. The subscription syntax must always be used with exactly two values: the argument list and the return type. The argument list must be a list of types or ellipsis; the return type must be a single type. There is no syntax to indicate optional or keyword arguments, such function types are rarely used as callback types.

## Event class docstring

Basic event class.

Basic event class.<hr>

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

### GenericMeta method docstring

Metaclass for generic types. This is a metaclass for typing.Generic and generic ABCs defined in typing module. User defined subclasses of GenericMeta can override __new__ and invoke super().__new__. Note that GenericMeta.__new__ has strict rules on what is allowed in its bases argument: * plain Generic is disallowed in bases; * Generic[...] should appear in bases at most once; * if Generic[...] is present, then it should list all type variables that appear in other bases. In addition, type of all generic bases is erased, e.g., C[int] is stripped to plain C.

### __init__ method docstring

Basic event class.<hr>

**[Parameters]**

- `this`: VariableNameInterface
  - Instance that listening event (e.g., Sprite).
- `type_name`: str or None, default None
  - Type name to set. Only specify when inherit this class.

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

### _get_previous_variable_name method docstring

Get a previous variable name.<hr>

**[Returns]**

- `previous_variable_name`: str
  - A previous variable name of this instance. If that value is not existing, then a blank string will be returned.

### Event method docstring

Basic event class.<hr>

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

### _validate_type_name_and_self_type method docstring

Validate type_name argument is None when self instance is not Event subclass, and the opposite pattern is true as well.<hr>

**[Parameters]**

- `type_name`: str or None
  - Type name to set.

<hr>

**[Raises]**

- ValueError: <br> ・If type_name is not None and self instance is Event type. <br> ・If type_name is None and self instance is not Event type.

## HandlerData class docstring



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

## MouseEventType class docstring

Mouse event type definitions.

Mouse event type definitions.

### EnumMeta method docstring

Metaclass for Enum

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

## VariableNameInterface class docstring



### _get_previous_variable_name method docstring

Get a previous variable name.<hr>

**[Returns]**

- `previous_variable_name`: str
  - A previous variable name of this instance. If that value is not existing, then a blank string will be returned.

## Callable class docstring

Callable type; Callable[[int], str] is a function of (int) -> str. The subscription syntax must always be used with exactly two values: the argument list and the return type. The argument list must be a list of types or ellipsis; the return type must be a single type. There is no syntax to indicate optional or keyword arguments, such function types are rarely used as callback types.

Callable type; Callable[[int], str] is a function of (int) -> str. The subscription syntax must always be used with exactly two values: the argument list and the return type. The argument list must be a list of types or ellipsis; the return type must be a single type. There is no syntax to indicate optional or keyword arguments, such function types are rarely used as callback types.

### CallableMeta method docstring

Metaclass for Callable (internal).

### object method docstring

The most base type

### Callable method docstring

Callable type; Callable[[int], str] is a function of (int) -> str. The subscription syntax must always be used with exactly two values: the argument list and the return type. The argument list must be a list of types or ellipsis; the return type must be a single type. There is no syntax to indicate optional or keyword arguments, such function types are rarely used as callback types.

### Callable method docstring

Callable type; Callable[[int], str] is a function of (int) -> str. The subscription syntax must always be used with exactly two values: the argument list and the return type. The argument list must be a list of types or ellipsis; the return type must be a single type. There is no syntax to indicate optional or keyword arguments, such function types are rarely used as callback types.