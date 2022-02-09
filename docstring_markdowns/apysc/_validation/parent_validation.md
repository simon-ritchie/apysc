# `apysc._validation.parent_validation` docstrings

## Module summary

Parent related validation interfaces.

## `validate_parent_contains_child` function docstring

Validate parent contains specified child.<hr>

**[Parameters]**

- `parent`: ChildInterface or None
  - Parent instance.
- `child`: DisplayObject
  - Child instance.

<hr>

**[Raises]**

- ValueError: If parent not contains specified child. If parent is None, check will be skipped.

## `validate_parent_instance` function docstring

Validate specified parent is `ChildInterface` instance.<hr>

**[Parameters]**

- `parent`: *
  - Any parent instance or None.

<hr>

**[Raises]**

- ValueError: If specified parent is not None and not `ChildInterface` instance.