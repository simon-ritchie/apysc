# `apysc._validation.parent_validation` docstrings

## Module summary

Parent-related validation interfaces.

## `validate_parent_contains_child` function docstring

Validate whether a parent contains a specified child.<hr>

**[Parameters]**

- `parent`: ChildInterface or None
  - Parent instance.
- `child`: DisplayObject
  - Child instance.

<hr>

**[Raises]**

- ValueError: If a parent does not contain a specified child. If a parent is None, this interface skips the checking.

## `validate_parent_instance` function docstring

Validate specified parent is `ChildInterface` instance.<hr>

**[Parameters]**

- `parent`: *
  - Any parent instance or None.

<hr>

**[Raises]**

- ValueError: If a specified parent isn't the `None` and `ChildInterface` instance.