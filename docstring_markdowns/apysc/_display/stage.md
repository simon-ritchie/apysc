# `apysc._display.stage` docstrings

## Module summary

Stage-related implementations.

## `_read_stage_id_from_db` function docstring

Read a stage id from a database.<hr>

**[Returns]**

- ``: 
  - A stage id. If a created stage doesn't exist, this interface returns None.

## `_save_stage_id_to_db` function docstring

Save a stage's memory address (id) to the database.<hr>

**[Parameters]**

- `stage`: Stage
  - Target stage.

## `get_stage` function docstring

Get an already instantiated stage instance.<hr>

**[Returns]**

- `stage`: Stage
  - Target stage instance.

<hr>

**[Raises]**

- StageNotCreatedError: If there is no instantiated stage yet.

## `get_stage_elem_id` function docstring

Get a current stage's element id.<hr>

**[Returns]**

- `stage_elem_id`: str
  - Current stage's element id. If there is no instantiated stage yet, this interface returns a blank string.

## `get_stage_elem_str` function docstring

Get a current stage's jQuery element string.<hr>

**[Returns]**

- `stage_elem_str`: str
  - Stage's jQuery element string (e.g., '$("#<stage_elem_id>")').

## `is_stage_created` function docstring

Get a boolean whether a created stage exists or not.<hr>

**[Returns]**

- `result`: bool
  - If a created stage exists, this interface returns True.

## `Stage` class docstring

The Stage (overall view-area) class.<hr>

**[Examples]**

```py
>>> import apysc as ap
>>> stage: ap.Stage = ap.Stage(
...     stage_width=500,
...     stage_height=300,
...     background_color="#333",
...     stage_elem_id="sales_chart",
... )
```

<hr>

**[References]**

- [Stage](https://simon-ritchie.github.io/apysc/en/stage.html)

### `__init__` method docstring

Create Stage (overall viewport) instance.<hr>

**[Parameters]**

- `stage_width`: int, default 300
  - Stage width.
- `stage_height`: int, default 185
  - Stage height
- `background_color`: str, default '#ffffff'
  - Hexadecimal background color string.
- `add_to`: str, default 'body'
  - Specification of element to add stage. Unique tag (e.g., 'body') or ID selector (e.g., '#any-unique-elem') is acceptable.
- `stage_elem_id`: str or None, optional
  - ID attribute set to stage HTML element (e.g., 'line-graph'). If None is set, a random integer will be applied.
- `variable_name_suffix`: str, default ''
  - A JavaScript variable name suffix string. This setting is sometimes useful for JavaScript debugging.

<hr>

**[Examples]**

```py
>>> import apysc as ap
>>> stage: ap.Stage = ap.Stage(
...     stage_width=500,
...     stage_height=300,
...     background_color="#333",
...     stage_elem_id="sales_chart",
... )
```

<hr>

**[References]**

- [Stage](https://simon-ritchie.github.io/apysc/en/stage.html)

### `__repr__` method docstring

Get a string representation of this instance (for the sake of debugging).<hr>

**[Returns]**

- `repr_str`: str
  - Type name and elem id will be set (e.g., `Stage("<stage_elem_id>")`).

### `_append_constructor_expression` method docstring

Append stage constructor expression.

### `_create_stage_elem_id_if_none` method docstring

Create a random stage element id if a specified id is None.<hr>

**[Parameters]**

- `stage_elem_id`: str or None
  - Specified stage element id.

<hr>

**[Returns]**

- `result_id`: str
  - If a specified id isn't None, this interface returns an unchanged argument value. Otherwise, this interface returns a random integer string.

### `_make_constructor_expression` method docstring

Make a stage constructor expression string.<hr>

**[Returns]**

- `expression`: str
  - Result expression.

### `_make_style_str` method docstring

Make a stage's style string.<hr>

**[Returns]**

- `style`: str
  - Result style string (width, height, etc.).

### `_save_stage_elem_id` method docstring

Save the stage element id.

## `StageNotCreatedError` class docstring