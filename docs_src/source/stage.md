# Stage

This page explains the `Stage` class.

## What is the Stage?

The `Stage` is the apysc overall drawing area (like a viewport, canvas, or something else) and contains all elements.

You must create the `Stage` at the first of the apysc project (this runs cleaning up internal data and files).

## Create stage

Creating stage is simple, like this:

```py
# runnable
import apysc as ap

stage: ap.Stage = ap.Stage()
```

## Stage background color setting

`Stage` class has a `background_color` option, which changes the stage's background color.

```py
# runnable
import apysc as ap

stage: ap.Stage = ap.Stage(
    background_color='#333',
    stage_elem_id='stage')

ap.save_overall_html(
    dest_dir_path='stage_background_color/')
```

This will create HTML with black background stage, as follows:

<iframe src="static/stage_background_color/index.html" width="300" height="185"></iframe>

## Stage size setting

Stage class has options to set stage width and stage height (arguments of `stage_width` and `stage_height`). These settings change stage sizes.

```py
# runnable
import apysc as ap

stage: ap.Stage = ap.Stage(
    stage_width=500, stage_height=50,
    background_color='#333',
    stage_elem_id='stage')

ap.save_overall_html(
    dest_dir_path='stage_size/')
```

The Previous script will create a horizontal stage, as follows:

<iframe src="static/stage_size/index.html" width="500", height="50"></iframe>

## Stage element id setting

Stage element id (HTML id) can be set by `stage_elem_id` argument. If you don't specify this, the apysc sets any unique id (based on created timestamp, like `stage_12345...`).

```py
# runnable
import apysc as ap

stage: ap.Stage = ap.Stage(
    background_color='#333',
    stage_elem_id='line_chart_1')
```

This option is useful when using the apysc project multiple times (for an easily identifiable ID) or version control.

## Stage class constructor API

<!-- Docstring: apysc._display.stage.Stage.__init__ -->

<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>

**[Interface signature]** `__init__(self, *, stage_width:int=300, stage_height:int=185, background_color:str='#ffffff', add_to:str='body', stage_elem_id:Union[str, NoneType]=None) -> None`<hr>

**[Interface summary]** Create Stage (overall viewport) instance.<hr>

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

## stage_elem_id property API

<!-- Docstring: apysc._display.stage.Stage.stage_elem_id -->

<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>

**[Interface summary]** Get stage's html element id.<hr>

**[Returns]**

- `stage_elem_id`: str
  - Stage's html element id (not including class or id symbol). e.g., 'line-graph'

<hr>

**[Examples]**

```py
>>> import apysc as ap
>>> stage: ap.Stage = ap.Stage(
...     stage_width=500, stage_height=300,
...     background_color='#333', stage_elem_id='sales_chart')
>>> stage.stage_elem_id
'sales_chart'
```

## add_child API

<!-- Docstring: apysc._display.child_interface.ChildInterface.add_child -->

<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>

**[Interface signature]** `add_child(self, child:apysc._display.display_object.DisplayObject) -> None`<hr>

**[Interface summary]** Add display object child to this instance.<hr>

**[Parameters]**

- `child`: DisplayObject
  - Child instance to add.

<hr>

**[Examples]**

```py
>>> import apysc as ap
>>> stage: ap.Stage = ap.Stage()
>>> sprite_1: ap.Sprite = ap.Sprite()
>>> sprite_1.graphics.begin_fill(color='#0af')
>>> rectangle: ap.Rectangle = sprite_1.graphics.draw_rect(
...     x=50, y=50, width=50, height=50)
>>> sprite_2: ap.Sprite = ap.Sprite()
>>> sprite_2.add_child(rectangle)
```

<hr>

**[References]**

- [add_child and remove_child interfaces document](https://bit.ly/3g7TMf0)

## remove_child API

<!-- Docstring: apysc._display.child_interface.ChildInterface.remove_child -->

<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>

**[Interface signature]** `remove_child(self, child:apysc._display.display_object.DisplayObject) -> None`<hr>

**[Interface summary]** Remove display object child from this instance.<hr>

**[Parameters]**

- `child`: DisplayObject
  - Child instance to remove.

<hr>

**[Examples]**

```py
>>> import apysc as ap
>>> stage: ap.Stage = ap.Stage()
>>> sprite: ap.Sprite = ap.Sprite()
>>> sprite.graphics.begin_fill(color='#0af', alpha=0.5)
>>> rectangle: ap.Rectangle = sprite.graphics.draw_rect(
...     x=50, y=50, width=50, height=50)
>>> sprite.graphics.remove_child(rectangle)
>>> print(rectangle.parent)
None
```

<hr>

**[References]**

- [add_child and remove_child interfaces document](https://bit.ly/3g7TMf0)

## contains API

<!-- Docstring: apysc._display.child_interface.ChildInterface.contains -->

<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>

**[Interface signature]** `contains(self, child:apysc._display.display_object.DisplayObject) -> apysc._type.boolean.Boolean`<hr>

**[Interface summary]** Get a boolean whether this instance contains a specified child.<hr>

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
>>> sprite.graphics.begin_fill(color='#0af', alpha=0.5)
>>> rectangle: ap.Rectangle = sprite.graphics.draw_rect(
...     x=50, y=50, width=50, height=50)
>>> sprite.graphics.contains(rectangle)
Boolean(True)

>>> rectangle.remove_from_parent()
>>> sprite.graphics.contains(rectangle)
Boolean(False)
```

<hr>

**[References]**

- [contains interface document](https://simon-ritchie.github.io/apysc/contains.html)

## num_children property API

<!-- Docstring: apysc._display.child_interface.ChildInterface.num_children -->

<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>

**[Interface summary]** Get a current children's number.<hr>

**[Returns]**

- `num_children`: int
  - Current children number.

<hr>

**[Examples]**

```py
>>> import apysc as ap
>>> stage: ap.Stage = ap.Stage()
>>> sprite: ap.Sprite = ap.Sprite()
>>> sprite.graphics.begin_fill(color='#0af', alpha=0.5)
>>> rectangle_1: ap.Rectangle = sprite.graphics.draw_rect(
...     x=50, y=50, width=50, height=50)
>>> rectangle_2: ap.Rectangle = sprite.graphics.draw_rect(
...     x=150, y=50, width=50, height=50)
>>> sprite.graphics.num_children
Int(2)
```

<hr>

**[References]**

- [num_children interface document](https://simon-ritchie.github.io/apysc/num_children.html)

## get_child_at API

<!-- Docstring: apysc._display.child_interface.ChildInterface.get_child_at -->

<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>

**[Interface signature]** `get_child_at(self, index:Union[int, apysc._type.int.Int]) -> apysc._display.display_object.DisplayObject`<hr>

**[Interface summary]** Get child at a specified index.<hr>

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
>>> sprite.graphics.begin_fill(color='#0af', alpha=0.5)
>>> rectangle_1: ap.Rectangle = sprite.graphics.draw_rect(
...     x=50, y=50, width=50, height=50)
>>> rectangle_2: ap.Rectangle = sprite.graphics.draw_rect(
...     x=150, y=50, width=50, height=50)
>>> child_at_index_1: ap.DisplayObject = (
...     sprite.graphics.get_child_at(1))
>>> child_at_index_1 == rectangle_2
True
```

<hr>

**[References]**

- [get_child_at interface document](https://simon-ritchie.github.io/apysc/get_child_at.html)