# `apysc._type.disable_value_modification_mixin` docstrings

## Module summary

The mix-in class implementation to disable a value modification.

## `DisableValueModificationMixIn` class docstring

### `disable_value_modification` method docstring

Disable a value modification. This method is useful when you want to prevent the value modification (e.g., the value updating with the `value` property). This is recommended to call this method at the constructor or after the instantiation.

### `raise_if_value_modification_is_disabled` method docstring

Raise an error if the value modification is disabled.<hr>

**[Raises]**

- ValueError: If the value modification is disabled.