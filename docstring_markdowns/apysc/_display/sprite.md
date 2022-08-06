# `apysc._display.sprite` docstrings

## Module summary

Implementations for Sprite class.

## `Sprite` class docstring

This class is for the basic display object that can be a parent.<hr>

**[Examples]**

```py
>>> import apysc as ap
>>> stage: ap.Stage = ap.Stage()
>>> sprite_1: ap.Sprite = ap.Sprite()
>>> # Create the sprite child rectangle
>>> sprite_1.graphics.begin_fill(color="#0af")
>>> rect: ap.Rectangle = sprite_1.graphics.draw_rect(
...     x=50, y=50, width=50, height=50
... )
>>> sprite_1.graphics.contains(rect)
Boolean(True)

>>> # Move the created rectangle to the other sprite
>>> sprite_2: ap.Sprite = ap.Sprite()
>>> sprite_2.add_child(rect)
>>> sprite_1.graphics.contains(rect)
Boolean(False)

>>> sprite_2.contains(rect)
Boolean(True)

>>> # Move the sprite container
>>> sprite_2.x = ap.Int(50)
>>> sprite_2.x
Int(50)
```

<hr>

**[References]**

- [Sprite document](https://simon-ritchie.github.io/apysc/en/sprite.html)

### `__init__` method docstring

Create a basic display object that can be a parent.<hr>

**[Parameters]**

- `variable_name`: str, default '
  - Variable name of this instance. A js expression uses this setting. It is unnecessary to specify any string except when instantiating the `Sprite` subclass.
- `variable_name_suffix`: str, default ''
  - A JavaScript variable name suffix string. This setting is sometimes useful for JavaScript's debugging.

<hr>

**[Examples]**

```py
>>> import apysc as ap
>>> stage: ap.Stage = ap.Stage()
>>> sprite_1: ap.Sprite = ap.Sprite()
>>> # Create the sprite child rectangle
>>> sprite_1.graphics.begin_fill(color="#0af")
>>> rect: ap.Rectangle = sprite_1.graphics.draw_rect(
...     x=50, y=50, width=50, height=50
... )
>>> sprite_1.graphics.contains(rect)
Boolean(True)

>>> # Move the created rectangle to the other sprite
>>> sprite_2: ap.Sprite = ap.Sprite()
>>> sprite_2.add_child(rect)
>>> sprite_1.graphics.contains(rect)
Boolean(False)

>>> sprite_2.contains(rect)
Boolean(True)

>>> # Move the sprite container
>>> sprite_2.x = ap.Int(50)
>>> sprite_2.x
Int(50)
```

<hr>

**[References]**

- [Sprite document](https://simon-ritchie.github.io/apysc/en/sprite.html)

### `__repr__` method docstring

Get a string representation of this instance (for the sake of debugging).<hr>

**[Returns]**

- `repr_str`: str
  - Type name and variable name will be set (e.g., `Sprite('<variable_name>')`).

### `_append_constructor_expression` method docstring

Append Sprite constructor expression.

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