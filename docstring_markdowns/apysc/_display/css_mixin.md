# `apysc._display.css_mixin` docstrings

## Module summary

Class implementation for the CSS mix-in.

## `CssMixIn` class docstring

### `_append_get_css_expresion` method docstring

Append a CSS getter expression string.<hr>

**[Parameters]**

- `name`: str or String
  - CSS name (e.g., 'display').
- `css`: String
  - CSS value.

### `_append_set_css_expression` method docstring

Append a CSS setter expression string.<hr>

**[Parameters]**

- `name`: str or String
  - CSS name (e.g., 'display').
- `value`: str or String
  - A CSS value string (e.g., 'none').

### `_initialize_css_if_not_initialized` method docstring

Initialize the _css attribute if this interface does not initialize it yet.

### `_make_snapshot` method docstring

Make values' snapshot.<hr>

**[Parameters]**

- `snapshot_name`: str
  - Target snapshot name.

### `_revert` method docstring

Revert values if a snapshot exists.<hr>

**[Parameters]**

- `snapshot_name`: str
  - Target snapshot name.

### `get_css` method docstring

Get a CSS value string.<hr>

**[Parameters]**

- `name`: str or String
  - CSS name (e.g., 'display').

<hr>

**[Returns]**

- `css`: ap.String
  - CSS value.

<hr>

**[Examples]**

```py
>>> import apysc as ap
>>> stage: ap.Stage = ap.Stage()
>>> sprite: ap.Sprite = ap.Sprite()
>>> sprite.graphics.begin_fill(color=ap.Color("#0af"), alpha=0.5)
>>> sprite.set_css(name="display", value="none")
>>> sprite.get_css(name="display")
String("none")
```

<hr>

**[References]**

- [Display object get_css and set_css interfaces](https://simon-ritchie.github.io/apysc/en/display_object_get_and_set_css.html)

### `set_css` method docstring

Set a specified value string to the CSS.<hr>

**[Parameters]**

- `name`: str or String
  - CSS name (e.g., 'display').
- `value`: str or String
  - A CSS value string (e.g., 'none').

<hr>

**[Examples]**

```py
>>> import apysc as ap
>>> stage: ap.Stage = ap.Stage()
>>> sprite: ap.Sprite = ap.Sprite()
>>> sprite.graphics.begin_fill(color=ap.Color("#0af"), alpha=0.5)
>>> sprite.set_css(name="display", value="none")
>>> sprite.get_css(name="display")
String("none")
```

<hr>

**[References]**

- [Display object get_css and set_css interfaces](https://simon-ritchie.github.io/apysc/en/display_object_get_and_set_css.html)