# apysc._validation.display_validation docstrings

## Module summary

Each display's validation implementations. Mainly following interfaces are defined: <br>・validate_stage Validate whether the specified instance is Stage type or not. <br>・validate_display_object Validate specified instance is DisplayObject type or it's subclass type (e.g., Sprite). <br>・validate_sprite Validate specified instance is Sprite type. <br>・validate_graphics Validate specified instance is Graphics type. <br>・validate_line_cap Validate specified line cap style setting. <br>・validate_line_joints Validate specified line joints style setting. <br>・validate_multiple_line_settings_isnt_set Validate multiple line settings (dotted, dashed, and so on) is not set.

## validate_display_object function docstring

Validate specified instance is DisplayObject type or it's subclass type (e.g., Sprite).<hr>

**[Parameters]**

- `display_object`: DisplayObject
  - DisplayObject instance to check.

<hr>

**[Raises]**

- ValueError: If specified instance is not DisplayObject type or it's subclass type.

## validate_graphics function docstring

Validate specified instance is Graphics type.<hr>

**[Parameters]**

- `graphics`: Graphics
  - Graphics instance to check.

<hr>

**[Raises]**

- ValueError: If specified instance is not Graphics type.

## validate_line_cap function docstring

Validate specified line cap style setting.<hr>

**[Parameters]**

- `cap`: LineCaps or String
  - Target line cap style setting to check.

<hr>

**[Raises]**

- ValueError: If specified cap setting type is not LineCaps or not defined string value.

## validate_line_joints function docstring

Validate specified line joints style setting.<hr>

**[Parameters]**

- `joints`: LineJoints or String
  - Target line joints style setting to check.

<hr>

**[Raises]**

- ValueError: If specified joints setting type is not LineJoints or not defined string value.

## validate_multiple_line_settings_isnt_set function docstring

Validate multiple line settings (dotted, dashed, and so on) is not set.<hr>

**[Parameters]**

- `any_instance`: Any
  - Any instance to check.

<hr>

**[Raises]**

- ValueError: If multiple line settings are set.

## validate_sprite function docstring

Validate specified instance is Sprite type.<hr>

**[Parameters]**

- `sprite`: Sprite
  - Sprite instance to check.

<hr>

**[Raises]**

- ValueError: If specified instance is not Sprite type.

## validate_stage function docstring

Validate whether the specified instance is Stage type or not.<hr>

**[Parameters]**

- `stage`: Stage
  - Stage instance to check.

<hr>

**[Raises]**

- ValueError: If specified instance is not stage type.

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