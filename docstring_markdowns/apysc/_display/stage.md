# apysc._display.stage docstrings

## Module summary

Stage (canvas) implementation.

## _save_stage_id_to_db function docstring

Save a stage's memory address (id) to the database.<hr>

**[Parameters]**

- `stage`: Stage
  - Target stage.

## get_stage function docstring

Get a already instantiated stage instance.<hr>

**[Returns]**

- `stage`: Stage
  - Target stage instance.

<hr>

**[Raises]**

- _StageNotCreatedError: If a stage is not instantiated yet.

## get_stage_elem_id function docstring

Get current stage's element id.<hr>

**[Returns]**

- `stage_elem_id`: str
  - Current stage's element id. If stage is not instantiated yet, blank string will be set.

## get_stage_elem_str function docstring

Get current stage's jQuery element string.<hr>

**[Returns]**

- `stage_elem_str`: str
  - Stage's jQuery element string (e.g., '$("#<stage_elem_id>")').

## get_stage_variable_name function docstring

Get current stage's global variable name.<hr>

**[Returns]**

- `stage_variable_name`: str
  - Current stage's js global variable name. If stage is not instantiated yet, blank string will be set.

## Stage class docstring

The Stage (overall viewport) class.

The Stage (overall viewport) class.<hr>

**[Examples]**

```py
>>> import apysc as ap
>>> stage: ap.Stage = ap.Stage(
...     stage_width=500, stage_height=300,
...     background_color='#333', stage_elem_id='sales_chart')
```

<hr>

**[References]**

- [Stage document](https://simon-ritchie.github.io/apysc/stage.html)

### __init__ method docstring

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
  - ID attribute set to stage html element (e.g., 'line-graph'). If None is set, random integer will be applied.

<hr>

**[Examples]**

```py
>>> import apysc as ap
>>> stage: ap.Stage = ap.Stage(
...     stage_width=500, stage_height=300,
...     background_color='#333', stage_elem_id='sales_chart')
```

<hr>

**[References]**

- [Stage document](https://simon-ritchie.github.io/apysc/stage.html)

### __repr__ method docstring

Get a string representation of this instance (for the sake of debugging).<hr>

**[Returns]**

- `repr_str`: str
  - Type name and elem id will be set (e.g., `Stage('<stage_elem_id>')`).

### _append_constructor_expression method docstring

Append stage constructor expression.

### _create_stage_elem_id_if_none method docstring

Create random stage element id if specified id is None.<hr>

**[Parameters]**

- `stage_elem_id`: str or None
  - Specified stage element id.

<hr>

**[Returns]**

- `result_id`: str
  - If specified id is not None, then unchanged argument value will be returned. Otherwise, random integer string will be returned.

### _make_constructor_expression method docstring

Make a stage constructor expression string.<hr>

**[Returns]**

- `expression`: str
  - Result expression.

### _make_style_str method docstring

Make a stage's style string.<hr>

**[Returns]**

- `style`: str
  - Result style string (width, height, etc).

### _save_stage_elem_id method docstring

Save the stage element id.

## _StageNotCreatedError class docstring

