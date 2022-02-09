# `apysc._type.revert_interface` docstrings

## Module summary

Class implementation for revert interface.

## `make_snapshots_of_each_scope_vars` function docstring

Make snapshots of each scope's variables.<hr>

**[Parameters]**

- `locals_`: dict
  - Local scope's variables.
- `globals_`: dict
  - Global scope's variables.

<hr>

**[Returns]**

- `snapshot_name`: str
  - Snapshot name to be used.

## `make_variables_snapshots` function docstring

Make snapshots of specified variables.<hr>

**[Parameters]**

- `variables`: list
  - Variables to make snapshots.

<hr>

**[Returns]**

- `snapshot_name`: str
  - Snapshot name to be used.

## `revert_each_scope_vars` function docstring

Revert each scope's variables.<hr>

**[Parameters]**

- `snapshot_name`: str
  - Snapshot name to use.
- `locals_`: dict
  - Local scope's variables.
- `globals_`: dict
  - Global scope's variables.

## `revert_variables` function docstring

Revert each variables.<hr>

**[Parameters]**

- `snapshot_name`: str
  - Snapshot name to use.
- `variables`: list
  - Each vairables to revert.

### `_delete_snapshot_exists_val` method docstring

Delete boolean value whether snapshot value exists or not.<hr>

**[Parameters]**

- `snapshot_name`: str
  - Target snapshot name.

### `_get_next_snapshot_name` method docstring

Get a next snapshot name.<hr>

**[Returns]**

- `snapshot_name`: str
  - Next snapshot name.

### `_initialize_ss_exists_val_if_not_initialized` method docstring

Initialize _snapshot_exists_ value it hasn't been initialized yet.

### `_make_snapshot` method docstring

Make value's snapshot.<hr>

**[Parameters]**

- `snapshot_name`: str
  - Target snapshot name.

### `_revert` method docstring

Revert values if snapshot exists.<hr>

**[Parameters]**

- `snapshot_name`: str
  - Target snapshot name.

### `_run_all_make_snapshot_methods` method docstring

Run all _make_snapshot methods. If instance is multiple inheritance one, and each has RevertInterface, then each _make_snapshot methods will be called.<hr>

**[Parameters]**

- `snapshot_name`: str
  - Target snapshot name.

### `_run_all_revert_methods` method docstring

Run all _revert methods. If instance is multiple inheritance one, and each has RevertInterface, then each _revert methods will be called.<hr>

**[Parameters]**

- `snapshot_name`: str
  - Target snapshot name.

### `_run_base_cls_make_snapshot_methods_recursively` method docstring

Run base classes make_snapshot methods recursively.<hr>

**[Parameters]**

- `class_`: type
  - Target type.
- `snapshot_name`: str
  - Target snapshot name.

### `_run_base_cls_revert_methods_recursively` method docstring

Run base classes revert methods recursively.<hr>

**[Parameters]**

- `class_`: type
  - Target type.
- `snapshot_name`: str
  - Target snapshot name.

### `_set_single_snapshot_val_to_dict` method docstring

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

### `_set_snapshot_exists_val` method docstring

Set boolean value whether snapshot value exists or not.<hr>

**[Parameters]**

- `snapshot_name`: str
  - Target snapshot name.

### `_snapshot_exists` method docstring

Get a boolean value whether snapshot value exists or not.<hr>

**[Parameters]**

- `snapshot_name`: str
  - Target snapshot name.

<hr>

**[Returns]**

- `snapshot_exists`: bool
  - Boolean value whether snapshot value exists or not.