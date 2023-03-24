# `apysc._type.deleted_object_mixin` docstrings

## Module summary

This module is for the class implementation of the `DeletedObjectMixIn`.

## `DeletedObjectMixIn` class docstring

### `_disable_each_method` method docstring

Disable each method of this instance.<hr>

**[Notes]**

This method disables only public methods (this method skips methods which starts with the single underscore character).

### `_disabled_method` method docstring

The method to replace each method when this object becomes deleted object.<hr>

**[Raises]**

- _DisabledObjectError: This interface always raises an exception.

### `_make_snapshot` method docstring

Make a value snapshot.<hr>

**[Parameters]**

- `snapshot_name`: str
  - Target snapshot name.

### `_revert` method docstring

Revert a value if a snapshot exists.<hr>

**[Parameters]**

- `snapshot_name`: str
  - Target snapshot name.

## `_DisabledObjectError` class docstring