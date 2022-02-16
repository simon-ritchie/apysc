# `apysc._display.parent_interface` docstrings

## Module summary

Class implementation for the parent-related interfaces.

## `ParentInterface` class docstring

### `_make_snapshot` method docstring

Make value's snapshot.<hr>

**[Parameters]**

- `snapshot_name`: str
  - Target snapshot name.

### `_revert` method docstring

Revert value if snapshot exists.<hr>

**[Parameters]**

- `snapshot_name`: str
  - Target snapshot name.

### `remove_from_parent` method docstring

Remove this instance from a parent.<hr>

**[Raises]**

- ValueError: If a parent is None (there is no parent).