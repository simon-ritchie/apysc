# apysc._event.custom_event_interface docstrings

## Module summary

Class implementation for the custom event interface.

## BlankObjectInterface class docstring



### _initialize_blank_object_if_not_initialized method docstring

Initialize a blank object value if it hasn't been initialized yet.

## Callable class docstring

Callable type; Callable[[int], str] is a function of (int) -> str. The subscription syntax must always be used with exactly two values: the argument list and the return type. The argument list must be a list of types or ellipsis; the return type must be a single type. There is no syntax to indicate optional or keyword arguments, such function types are rarely used as callback types.

Callable type; Callable[[int], str] is a function of (int) -> str. The subscription syntax must always be used with exactly two values: the argument list and the return type. The argument list must be a list of types or ellipsis; the return type must be a single type. There is no syntax to indicate optional or keyword arguments, such function types are rarely used as callback types.

### CallableMeta method docstring

Metaclass for Callable (internal).

### object method docstring

The most base type

### Callable method docstring

Callable type; Callable[[int], str] is a function of (int) -> str. The subscription syntax must always be used with exactly two values: the argument list and the return type. The argument list must be a list of types or ellipsis; the return type must be a single type. There is no syntax to indicate optional or keyword arguments, such function types are rarely used as callback types.

## CustomEventInterface class docstring



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

### _get_custom_event_type_str method docstring

Get a custom event type string from a type value.<hr>

**[Parameters]**

- `custom_event_type`: CustomEventType or str
  - Target custom event type or string.

<hr>

**[Returns]**

- `custom_event_type_str`: str
  - A custom event type string.

### _initialize_blank_object_if_not_initialized method docstring

Initialize a blank object value if it hasn't been initialized yet.

### _initialize_custom_event_handlers_if_not_initialized method docstring

Initialize the _custom_event_handlers data if it hasn't been initialized yet.<hr>

**[Parameters]**

- `custom_event_type_str`: str
  - Target custom event type string.

### _set_custom_event_handler_data method docstring

Set a handler's data to the dictionary.<hr>

**[Parameters]**

- `handler`: _Handler
  - Callable will be called when an event is dispatched.
- `custom_event_type_str`: str
  - Target custom event type string.
- `options`: dict or None
  - Optional arguments dictionary to be passed to a handler.

### _unset_custom_event_handler_data method docstring

Unset a handler's data from the dictionary.<hr>

**[Parameters]**

- `handler`: _Handler
  - Callable will be called when an event is dispatched.
- `custom_event_type_str`: str
  - Target custom event type string.

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

## CustomEventType class docstring

An enumeration.

An enumeration.

### EnumMeta method docstring

Metaclass for Enum

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

## str class docstring

str(object='') -> str str(bytes_or_buffer[, encoding[, errors]]) -> str Create a new string object from the given object. If encoding or errors is specified, then the object must expose a data buffer that will be decoded using the given encoding and error handler. Otherwise, returns the result of object.__str__() (if defined) or repr(object). encoding defaults to sys.getdefaultencoding(). errors defaults to 'strict'.

str(object='') -> str str(bytes_or_buffer[, encoding[, errors]]) -> str Create a new string object from the given object. If encoding or errors is specified, then the object must expose a data buffer that will be decoded using the given encoding and error handler. Otherwise, returns the result of object.__str__() (if defined) or repr(object). encoding defaults to sys.getdefaultencoding(). errors defaults to 'strict'.

### __add__ method docstring

Return self+value.

### __contains__ method docstring

Return key in self.

### __format__ method docstring

S.__format__(format_spec) -> str Return a formatted version of S as described by format_spec.

### __getitem__ method docstring

Return self[key].

### __iter__ method docstring

Implement iter(self).

### __len__ method docstring

Return len(self).

### __mod__ method docstring

Return self%value.

### __mul__ method docstring

Return self*value.

### __rmod__ method docstring

Return value%self.

### __rmul__ method docstring

Return value*self.

### __sizeof__ method docstring

S.__sizeof__() -> size of S in memory, in bytes

### capitalize method docstring

S.capitalize() -> str Return a capitalized version of S, i.e. make the first character have upper case and the rest lower case.

### casefold method docstring

S.casefold() -> str Return a version of S suitable for caseless comparisons.

### center method docstring

S.center(width[, fillchar]) -> str Return S centered in a string of length width. Padding is done using the specified fill character (default is a space)

### count method docstring

S.count(sub[, start[, end]]) -> int Return the number of non-overlapping occurrences of substring sub in string S[start:end]. Optional arguments start and end are interpreted as in slice notation.

### encode method docstring

S.encode(encoding='utf-8', errors='strict') -> bytes Encode S using the codec registered for encoding. Default encoding is 'utf-8'. errors may be given to set a different error handling scheme. Default is 'strict' meaning that encoding errors raise a UnicodeEncodeError. Other possible values are 'ignore', 'replace' and 'xmlcharrefreplace' as well as any other name registered with codecs.register_error that can handle UnicodeEncodeErrors.

### endswith method docstring

S.endswith(suffix[, start[, end]]) -> bool Return True if S ends with the specified suffix, False otherwise. With optional start, test S beginning at that position. With optional end, stop comparing S at that position. suffix can also be a tuple of strings to try.

### expandtabs method docstring

S.expandtabs(tabsize=8) -> str Return a copy of S where all tab characters are expanded using spaces. If tabsize is not given, a tab size of 8 characters is assumed.

### find method docstring

S.find(sub[, start[, end]]) -> int Return the lowest index in S where substring sub is found, such that sub is contained within S[start:end]. Optional arguments start and end are interpreted as in slice notation. Return -1 on failure.

### format method docstring

S.format(*args, **kwargs) -> str Return a formatted version of S, using substitutions from args and kwargs. The substitutions are identified by braces ('{' and '}').

### format_map method docstring

S.format_map(mapping) -> str Return a formatted version of S, using substitutions from mapping. The substitutions are identified by braces ('{' and '}').

### index method docstring

S.index(sub[, start[, end]]) -> int Return the lowest index in S where substring sub is found, such that sub is contained within S[start:end]. Optional arguments start and end are interpreted as in slice notation. Raises ValueError when the substring is not found.

### isalnum method docstring

S.isalnum() -> bool Return True if all characters in S are alphanumeric and there is at least one character in S, False otherwise.

### isalpha method docstring

S.isalpha() -> bool Return True if all characters in S are alphabetic and there is at least one character in S, False otherwise.

### isdecimal method docstring

S.isdecimal() -> bool Return True if there are only decimal characters in S, False otherwise.

### isdigit method docstring

S.isdigit() -> bool Return True if all characters in S are digits and there is at least one character in S, False otherwise.

### isidentifier method docstring

S.isidentifier() -> bool Return True if S is a valid identifier according to the language definition. Use keyword.iskeyword() to test for reserved identifiers such as "def" and "class".

### islower method docstring

S.islower() -> bool Return True if all cased characters in S are lowercase and there is at least one cased character in S, False otherwise.

### isnumeric method docstring

S.isnumeric() -> bool Return True if there are only numeric characters in S, False otherwise.

### isprintable method docstring

S.isprintable() -> bool Return True if all characters in S are considered printable in repr() or S is empty, False otherwise.

### isspace method docstring

S.isspace() -> bool Return True if all characters in S are whitespace and there is at least one character in S, False otherwise.

### istitle method docstring

S.istitle() -> bool Return True if S is a titlecased string and there is at least one character in S, i.e. upper- and titlecase characters may only follow uncased characters and lowercase characters only cased ones. Return False otherwise.

### isupper method docstring

S.isupper() -> bool Return True if all cased characters in S are uppercase and there is at least one cased character in S, False otherwise.

### join method docstring

S.join(iterable) -> str Return a string which is the concatenation of the strings in the iterable. The separator between elements is S.

### ljust method docstring

S.ljust(width[, fillchar]) -> str Return S left-justified in a Unicode string of length width. Padding is done using the specified fill character (default is a space).

### lower method docstring

S.lower() -> str Return a copy of the string S converted to lowercase.

### lstrip method docstring

S.lstrip([chars]) -> str Return a copy of the string S with leading whitespace removed. If chars is given and not None, remove characters in chars instead.

### maketrans method docstring

Return a translation table usable for str.translate(). If there is only one argument, it must be a dictionary mapping Unicode ordinals (integers) or characters to Unicode ordinals, strings or None. Character keys will be then converted to ordinals. If there are two arguments, they must be strings of equal length, and in the resulting dictionary, each character in x will be mapped to the character at the same position in y. If there is a third argument, it must be a string, whose characters will be mapped to None in the result.

### partition method docstring

S.partition(sep) -> (head, sep, tail) Search for the separator sep in S, and return the part before it, the separator itself, and the part after it. If the separator is not found, return S and two empty strings.

### replace method docstring

S.replace(old, new[, count]) -> str Return a copy of S with all occurrences of substring old replaced by new. If the optional argument count is given, only the first count occurrences are replaced.

### rfind method docstring

S.rfind(sub[, start[, end]]) -> int Return the highest index in S where substring sub is found, such that sub is contained within S[start:end]. Optional arguments start and end are interpreted as in slice notation. Return -1 on failure.

### rindex method docstring

S.rindex(sub[, start[, end]]) -> int Return the highest index in S where substring sub is found, such that sub is contained within S[start:end]. Optional arguments start and end are interpreted as in slice notation. Raises ValueError when the substring is not found.

### rjust method docstring

S.rjust(width[, fillchar]) -> str Return S right-justified in a string of length width. Padding is done using the specified fill character (default is a space).

### rpartition method docstring

S.rpartition(sep) -> (head, sep, tail) Search for the separator sep in S, starting at the end of S, and return the part before it, the separator itself, and the part after it. If the separator is not found, return two empty strings and S.

### rsplit method docstring

S.rsplit(sep=None, maxsplit=-1) -> list of strings Return a list of the words in S, using sep as the delimiter string, starting at the end of the string and working to the front. If maxsplit is given, at most maxsplit splits are done. If sep is not specified, any whitespace string is a separator.

### rstrip method docstring

S.rstrip([chars]) -> str Return a copy of the string S with trailing whitespace removed. If chars is given and not None, remove characters in chars instead.

### split method docstring

S.split(sep=None, maxsplit=-1) -> list of strings Return a list of the words in S, using sep as the delimiter string. If maxsplit is given, at most maxsplit splits are done. If sep is not specified or is None, any whitespace string is a separator and empty strings are removed from the result.

### splitlines method docstring

S.splitlines([keepends]) -> list of strings Return a list of the lines in S, breaking at line boundaries. Line breaks are not included in the resulting list unless keepends is given and true.

### startswith method docstring

S.startswith(prefix[, start[, end]]) -> bool Return True if S starts with the specified prefix, False otherwise. With optional start, test S beginning at that position. With optional end, stop comparing S at that position. prefix can also be a tuple of strings to try.

### strip method docstring

S.strip([chars]) -> str Return a copy of the string S with leading and trailing whitespace removed. If chars is given and not None, remove characters in chars instead.

### swapcase method docstring

S.swapcase() -> str Return a copy of S with uppercase characters converted to lowercase and vice versa.

### title method docstring

S.title() -> str Return a titlecased version of S, i.e. words start with title case characters, all remaining cased characters have lower case.

### translate method docstring

S.translate(table) -> str Return a copy of the string S in which each character has been mapped through the given translation table. The table must implement lookup/indexing via __getitem__, for instance a dictionary or list, mapping Unicode ordinals to Unicode ordinals, strings, or None. If this operation raises LookupError, the character is left untouched. Characters mapped to None are deleted.

### upper method docstring

S.upper() -> str Return a copy of S converted to uppercase.

### zfill method docstring

S.zfill(width) -> str Pad a numeric string S with zeros on the left, to fill a field of the specified width. The string S is never truncated.

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

## str class docstring

str(object='') -> str str(bytes_or_buffer[, encoding[, errors]]) -> str Create a new string object from the given object. If encoding or errors is specified, then the object must expose a data buffer that will be decoded using the given encoding and error handler. Otherwise, returns the result of object.__str__() (if defined) or repr(object). encoding defaults to sys.getdefaultencoding(). errors defaults to 'strict'.

str(object='') -> str str(bytes_or_buffer[, encoding[, errors]]) -> str Create a new string object from the given object. If encoding or errors is specified, then the object must expose a data buffer that will be decoded using the given encoding and error handler. Otherwise, returns the result of object.__str__() (if defined) or repr(object). encoding defaults to sys.getdefaultencoding(). errors defaults to 'strict'.

### __add__ method docstring

Return self+value.

### __contains__ method docstring

Return key in self.

### __format__ method docstring

S.__format__(format_spec) -> str Return a formatted version of S as described by format_spec.

### __getitem__ method docstring

Return self[key].

### __iter__ method docstring

Implement iter(self).

### __len__ method docstring

Return len(self).

### __mod__ method docstring

Return self%value.

### __mul__ method docstring

Return self*value.

### __rmod__ method docstring

Return value%self.

### __rmul__ method docstring

Return value*self.

### __sizeof__ method docstring

S.__sizeof__() -> size of S in memory, in bytes

### capitalize method docstring

S.capitalize() -> str Return a capitalized version of S, i.e. make the first character have upper case and the rest lower case.

### casefold method docstring

S.casefold() -> str Return a version of S suitable for caseless comparisons.

### center method docstring

S.center(width[, fillchar]) -> str Return S centered in a string of length width. Padding is done using the specified fill character (default is a space)

### count method docstring

S.count(sub[, start[, end]]) -> int Return the number of non-overlapping occurrences of substring sub in string S[start:end]. Optional arguments start and end are interpreted as in slice notation.

### encode method docstring

S.encode(encoding='utf-8', errors='strict') -> bytes Encode S using the codec registered for encoding. Default encoding is 'utf-8'. errors may be given to set a different error handling scheme. Default is 'strict' meaning that encoding errors raise a UnicodeEncodeError. Other possible values are 'ignore', 'replace' and 'xmlcharrefreplace' as well as any other name registered with codecs.register_error that can handle UnicodeEncodeErrors.

### endswith method docstring

S.endswith(suffix[, start[, end]]) -> bool Return True if S ends with the specified suffix, False otherwise. With optional start, test S beginning at that position. With optional end, stop comparing S at that position. suffix can also be a tuple of strings to try.

### expandtabs method docstring

S.expandtabs(tabsize=8) -> str Return a copy of S where all tab characters are expanded using spaces. If tabsize is not given, a tab size of 8 characters is assumed.

### find method docstring

S.find(sub[, start[, end]]) -> int Return the lowest index in S where substring sub is found, such that sub is contained within S[start:end]. Optional arguments start and end are interpreted as in slice notation. Return -1 on failure.

### format method docstring

S.format(*args, **kwargs) -> str Return a formatted version of S, using substitutions from args and kwargs. The substitutions are identified by braces ('{' and '}').

### format_map method docstring

S.format_map(mapping) -> str Return a formatted version of S, using substitutions from mapping. The substitutions are identified by braces ('{' and '}').

### index method docstring

S.index(sub[, start[, end]]) -> int Return the lowest index in S where substring sub is found, such that sub is contained within S[start:end]. Optional arguments start and end are interpreted as in slice notation. Raises ValueError when the substring is not found.

### isalnum method docstring

S.isalnum() -> bool Return True if all characters in S are alphanumeric and there is at least one character in S, False otherwise.

### isalpha method docstring

S.isalpha() -> bool Return True if all characters in S are alphabetic and there is at least one character in S, False otherwise.

### isdecimal method docstring

S.isdecimal() -> bool Return True if there are only decimal characters in S, False otherwise.

### isdigit method docstring

S.isdigit() -> bool Return True if all characters in S are digits and there is at least one character in S, False otherwise.

### isidentifier method docstring

S.isidentifier() -> bool Return True if S is a valid identifier according to the language definition. Use keyword.iskeyword() to test for reserved identifiers such as "def" and "class".

### islower method docstring

S.islower() -> bool Return True if all cased characters in S are lowercase and there is at least one cased character in S, False otherwise.

### isnumeric method docstring

S.isnumeric() -> bool Return True if there are only numeric characters in S, False otherwise.

### isprintable method docstring

S.isprintable() -> bool Return True if all characters in S are considered printable in repr() or S is empty, False otherwise.

### isspace method docstring

S.isspace() -> bool Return True if all characters in S are whitespace and there is at least one character in S, False otherwise.

### istitle method docstring

S.istitle() -> bool Return True if S is a titlecased string and there is at least one character in S, i.e. upper- and titlecase characters may only follow uncased characters and lowercase characters only cased ones. Return False otherwise.

### isupper method docstring

S.isupper() -> bool Return True if all cased characters in S are uppercase and there is at least one cased character in S, False otherwise.

### join method docstring

S.join(iterable) -> str Return a string which is the concatenation of the strings in the iterable. The separator between elements is S.

### ljust method docstring

S.ljust(width[, fillchar]) -> str Return S left-justified in a Unicode string of length width. Padding is done using the specified fill character (default is a space).

### lower method docstring

S.lower() -> str Return a copy of the string S converted to lowercase.

### lstrip method docstring

S.lstrip([chars]) -> str Return a copy of the string S with leading whitespace removed. If chars is given and not None, remove characters in chars instead.

### maketrans method docstring

Return a translation table usable for str.translate(). If there is only one argument, it must be a dictionary mapping Unicode ordinals (integers) or characters to Unicode ordinals, strings or None. Character keys will be then converted to ordinals. If there are two arguments, they must be strings of equal length, and in the resulting dictionary, each character in x will be mapped to the character at the same position in y. If there is a third argument, it must be a string, whose characters will be mapped to None in the result.

### partition method docstring

S.partition(sep) -> (head, sep, tail) Search for the separator sep in S, and return the part before it, the separator itself, and the part after it. If the separator is not found, return S and two empty strings.

### replace method docstring

S.replace(old, new[, count]) -> str Return a copy of S with all occurrences of substring old replaced by new. If the optional argument count is given, only the first count occurrences are replaced.

### rfind method docstring

S.rfind(sub[, start[, end]]) -> int Return the highest index in S where substring sub is found, such that sub is contained within S[start:end]. Optional arguments start and end are interpreted as in slice notation. Return -1 on failure.

### rindex method docstring

S.rindex(sub[, start[, end]]) -> int Return the highest index in S where substring sub is found, such that sub is contained within S[start:end]. Optional arguments start and end are interpreted as in slice notation. Raises ValueError when the substring is not found.

### rjust method docstring

S.rjust(width[, fillchar]) -> str Return S right-justified in a string of length width. Padding is done using the specified fill character (default is a space).

### rpartition method docstring

S.rpartition(sep) -> (head, sep, tail) Search for the separator sep in S, starting at the end of S, and return the part before it, the separator itself, and the part after it. If the separator is not found, return two empty strings and S.

### rsplit method docstring

S.rsplit(sep=None, maxsplit=-1) -> list of strings Return a list of the words in S, using sep as the delimiter string, starting at the end of the string and working to the front. If maxsplit is given, at most maxsplit splits are done. If sep is not specified, any whitespace string is a separator.

### rstrip method docstring

S.rstrip([chars]) -> str Return a copy of the string S with trailing whitespace removed. If chars is given and not None, remove characters in chars instead.

### split method docstring

S.split(sep=None, maxsplit=-1) -> list of strings Return a list of the words in S, using sep as the delimiter string. If maxsplit is given, at most maxsplit splits are done. If sep is not specified or is None, any whitespace string is a separator and empty strings are removed from the result.

### splitlines method docstring

S.splitlines([keepends]) -> list of strings Return a list of the lines in S, breaking at line boundaries. Line breaks are not included in the resulting list unless keepends is given and true.

### startswith method docstring

S.startswith(prefix[, start[, end]]) -> bool Return True if S starts with the specified prefix, False otherwise. With optional start, test S beginning at that position. With optional end, stop comparing S at that position. prefix can also be a tuple of strings to try.

### strip method docstring

S.strip([chars]) -> str Return a copy of the string S with leading and trailing whitespace removed. If chars is given and not None, remove characters in chars instead.

### swapcase method docstring

S.swapcase() -> str Return a copy of S with uppercase characters converted to lowercase and vice versa.

### title method docstring

S.title() -> str Return a titlecased version of S, i.e. words start with title case characters, all remaining cased characters have lower case.

### translate method docstring

S.translate(table) -> str Return a copy of the string S in which each character has been mapped through the given translation table. The table must implement lookup/indexing via __getitem__, for instance a dictionary or list, mapping Unicode ordinals to Unicode ordinals, strings, or None. If this operation raises LookupError, the character is left untouched. Characters mapped to None are deleted.

### upper method docstring

S.upper() -> str Return a copy of S converted to uppercase.

### zfill method docstring

S.zfill(width) -> str Pad a numeric string S with zeros on the left, to fill a field of the specified width. The string S is never truncated.