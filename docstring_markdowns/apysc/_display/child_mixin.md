# `apysc._display.child_mixin` docstrings

## Module summary

Class implementation for the child-related mix-in.

## `append_expression_of_add_child` function docstring

Append expression of add_child (add).<hr>

**[Parameters]**

- `child`: DisplayObject
  - Child object to add.

## `append_expression_of_remove_child` function docstring

Append expression of remove_child interface.<hr>

**[Parameters]**

- `child`: DisplayObject
  - Child object to remove.

## `ChildMixIn` class docstring

### `_append_contains_expression` method docstring

Append contains method expression.<hr>

**[Parameters]**

- `result`: Boolean
  - Result boolean value.
- `child`: DisplayObject
  - Child instance to check.

### `_append_expression_of_remove_children` method docstring

Append an expression of the `remove_children` interface.

### `_append_get_child_at_expression` method docstring

Append a get_child_at method expression.<hr>

**[Parameters]**

- `child`: DisplayObject
  - Target index child instance.
- `index`: int or Int
  - Child's index (start from 0).

### `_append_num_children_expression` method docstring

Append num_children method expression.<hr>

**[Parameters]**

- `num_children`: Int
  - Current children number.

### `_initialize_children_if_not_initialized` method docstring

Initialize _children attribute if this interface does not initialize it yet.

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

### `add_child` method docstring

Add display object child to this instance.<hr>

**[Parameters]**

- `child`: DisplayObject
  - Child instance to add.

<hr>

**[Examples]**

```py
>>> import apysc as ap
>>> stage: ap.Stage = ap.Stage()
>>> sprite_1: ap.Sprite = ap.Sprite()
>>> sprite_1.graphics.begin_fill(color=ap.Color("#0af"))
>>> rectangle: ap.Rectangle = sprite_1.graphics.draw_rect(
...     x=50, y=50, width=50, height=50
... )
>>> sprite_2: ap.Sprite = ap.Sprite()
>>> sprite_2.add_child(rectangle)
```

<hr>

**[References]**

- [add_child and remove_child interfaces](https://simon-ritchie.github.io/apysc/en/add_child_and_remove_child.html)

### `contains` method docstring

Get a boolean whether this instance contains a specified child.<hr>

**[Parameters]**

- `child`: DisplayObject
  - Child instance to check.

<hr>

**[Returns]**

- `result`: Boolean
  - If this instance contains a specified child, this method returns True.

<hr>

**[Examples]**

```py
>>> import apysc as ap
>>> stage: ap.Stage = ap.Stage()
>>> sprite: ap.Sprite = ap.Sprite()
>>> sprite.graphics.begin_fill(color=ap.Color("#0af"), alpha=0.5)
>>> rectangle: ap.Rectangle = sprite.graphics.draw_rect(
...     x=50, y=50, width=50, height=50
... )
>>> sprite.graphics.contains(rectangle)
Boolean(True)

>>> rectangle.remove_from_parent()
>>> sprite.graphics.contains(rectangle)
Boolean(False)
```

<hr>

**[References]**

- [contains interface](https://simon-ritchie.github.io/apysc/en/contains.html)

### `get_child_at` method docstring

Get a child at a specified index.<hr>

**[Parameters]**

- `index`: int or Int
  - Child's index (start from 0).

<hr>

**[Returns]**

- `child`: DisplayObject
  - Target index child instance.

<hr>

**[Examples]**

```py
>>> import apysc as ap
>>> stage: ap.Stage = ap.Stage()
>>> sprite: ap.Sprite = ap.Sprite()
>>> sprite.graphics.begin_fill(color=ap.Color("#0af"), alpha=0.5)
>>> rectangle_1: ap.Rectangle = sprite.graphics.draw_rect(
...     x=50, y=50, width=50, height=50
... )
>>> rectangle_2: ap.Rectangle = sprite.graphics.draw_rect(
...     x=150, y=50, width=50, height=50
... )
>>> child_at_index_1: ap.DisplayObject = sprite.graphics.get_child_at(1)
>>> child_at_index_1 == rectangle_2
True
```

<hr>

**[References]**

- [get_child_at interface](https://simon-ritchie.github.io/apysc/en/get_child_at.html)

### `remove_child` method docstring

Remove display object child from this instance.<hr>

**[Parameters]**

- `child`: DisplayObject
  - Child instance to remove.

<hr>

**[Examples]**

```py
>>> import apysc as ap
>>> stage: ap.Stage = ap.Stage()
>>> sprite: ap.Sprite = ap.Sprite()
>>> sprite.graphics.begin_fill(color=ap.Color("#0af"), alpha=0.5)
>>> rectangle: ap.Rectangle = sprite.graphics.draw_rect(
...     x=50, y=50, width=50, height=50
... )
>>> sprite.graphics.remove_child(rectangle)
>>> print(rectangle.parent)
None
```

<hr>

**[References]**

- [add_child and remove_child interfaces](https://simon-ritchie.github.io/apysc/en/add_child_and_remove_child.html)

### `remove_children` method docstring

Remove all children from this instance.<hr>

**[Examples]**

```py
>>> import apysc as ap
>>> sprite: ap.Sprite = ap.Sprite()
>>> rectangle_1: ap.Rectangle = ap.Rectangle(
...     x=50, y=50, width=50, height=50, fill_color=ap.Color("#0af")
... )
>>> rectangle_2: ap.Rectangle = ap.Rectangle(
...     x=150, y=50, width=50, height=50, fill_color=ap.Color("#0af")
... )
>>> sprite.add_child(child=rectangle_1)
>>> sprite.add_child(child=rectangle_2)
>>> sprite.remove_children()
>>> sprite.num_children
Int(0)
```

<hr>

**[References]**

- [remove_children interface](https://simon-ritchie.github.io/apysc/en/remove_children.html)