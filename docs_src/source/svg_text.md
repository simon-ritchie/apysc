# SVGText class

This page explains the `SVGText` class.

## What class is this?

The `SVGText` class creates an SVG text object.

## Basic usage

The `SVGText` class constructor requires the `text` argument.

The constructor also accepts each font's and style's argument, such as the `font_size`, `font_family`, `fill_color`, and `bold`.

```py
# runnable
import apysc as ap

ap.Stage(
    background_color=ap.Color("#333"),
    stage_width=200,
    stage_height=50,
    stage_elem_id="stage",
)
svg_text: ap.SVGText = ap.SVGText(
    text="Hello, world!",
    x=20,
    y=32,
    fill_color=ap.Color("#aaa"),
)
ap.save_overall_html(dest_dir_path="svg_text_basic_usage/")
```

<iframe src="static/svg_text_basic_usage/index.html" width="200" height="50"></iframe>

## Note on the baseline of a text's y-coordinate

The baseline of a text's y-coordinate is the text's bottom position (this is the specification of the SVG text).

So if you specify `y=0` as the coordinate, you can see almost nothing of a text's content (barely see the bottom of the comma in the following example).

```py
# runnable
import apysc as ap

ap.Stage(
    background_color=ap.Color("#333"),
    stage_width=200,
    stage_height=50,
    stage_elem_id="stage",
)
svg_text: ap.SVGText = ap.SVGText(
    text="Hello, world!",
    x=20,
    y=0,
    fill_color=ap.Color("#aaa"),
)
ap.save_overall_html(dest_dir_path="svg_text_note_on_the_y_baseline/")
```

<iframe src="static/svg_text_note_on_the_y_baseline/index.html" width="200" height="50"></iframe>

## text property interface example

The `text` property updates or gets the instance's text.

```py
# runnable
import apysc as ap

ap.Stage(
    background_color=ap.Color("#333"),
    stage_width=200,
    stage_height=50,
    stage_elem_id="stage",
)
svg_text: ap.SVGText = ap.SVGText(
    text="Hello, world!",
    x=20,
    y=32,
    fill_color=ap.Color("#aaa"),
)
svg_text.text = ap.String("Lorem ipsum")
ap.save_overall_html(dest_dir_path="svg_text_text/")
```

<iframe src="static/svg_text_text/index.html" width="200" height="50"></iframe>

## font_size property interface example

The `font_size` property updates or gets the instance's font size.

```py
# runnable
import apysc as ap

ap.Stage(
    background_color=ap.Color("#333"),
    stage_width=200,
    stage_height=50,
    stage_elem_id="stage",
)
svg_text: ap.SVGText = ap.SVGText(
    text="Hello, world!",
    x=20,
    y=34,
    fill_color=ap.Color("#aaa"),
)
svg_text.font_size = ap.Int(24)
ap.save_overall_html(dest_dir_path="svg_text_font_size/")
```

<iframe src="static/svg_text_font_size/index.html" width="200" height="50"></iframe>

## font_family property interface example

The `font_family` property updates or gets the instance's font family.

This property requires an `Array` of each font name `String`.

```py
# runnable
import apysc as ap

ap.Stage(
    background_color=ap.Color("#333"),
    stage_width=200,
    stage_height=50,
    stage_elem_id="stage",
)
svg_text: ap.SVGText = ap.SVGText(
    text="Hello, world!",
    x=20,
    y=32,
    fill_color=ap.Color("#aaa"),
)
svg_text.font_family = ap.Array([ap.String("Impact"), ap.String("Times New Roman")])
ap.save_overall_html(dest_dir_path="svg_text_font_family/")
```

<iframe src="static/svg_text_font_family/index.html" width="200" height="50"></iframe>

## x property interface example

The `x` property updates or gets the instance's x-coordinate:

```py
# runnable
import apysc as ap

ap.Stage(
    background_color=ap.Color("#333"),
    stage_width=200,
    stage_height=50,
    stage_elem_id="stage",
)
svg_text: ap.SVGText = ap.SVGText(
    text="Hello, world!",
    y=32,
    fill_color=ap.Color("#aaa"),
)
svg_text.x = ap.Number(50)
ap.save_overall_html(dest_dir_path="svg_text_x/")
```

<iframe src="static/svg_text_x/index.html" width="200" height="50"></iframe>

## y property interface example

The `y` property updates or gets the instance's y-coordinate:

```py
# runnable
import apysc as ap

ap.Stage(
    background_color=ap.Color("#333"),
    stage_width=200,
    stage_height=70,
    stage_elem_id="stage",
)
svg_text: ap.SVGText = ap.SVGText(
    text="Hello, world!",
    x=20,
    y=32,
    fill_color=ap.Color("#aaa"),
)
svg_text.y = ap.Number(45)
ap.save_overall_html(dest_dir_path="svg_text_y/")
```

<iframe src="static/svg_text_y/index.html" width="200" height="70"></iframe>

## fill_color property interface example

The `fill_color` property updates or gets the instance's fill color:

```py
# runnable
import apysc as ap

ap.Stage(
    background_color=ap.Color("#333"),
    stage_width=200,
    stage_height=50,
    stage_elem_id="stage",
)
svg_text: ap.SVGText = ap.SVGText(
    text="Hello, world!",
    x=20,
    y=32,
)
svg_text.fill_color = ap.String("#0af")
ap.save_overall_html(dest_dir_path="svg_text_fill_color/")
```

<iframe src="static/svg_text_fill_color/index.html" width="200" height="50"></iframe>

## fill_alpha property interface example

The `fill_alpha` property updates or gets the instance's fill alpha (opacity):

```py
# runnable
import apysc as ap

ap.Stage(
    background_color=ap.Color("#333"),
    stage_width=200,
    stage_height=50,
    stage_elem_id="stage",
)
svg_text: ap.SVGText = ap.SVGText(
    text="Hello, world!",
    x=20,
    y=32,
    fill_color=ap.Color("#aaa"),
)
svg_text.fill_alpha = ap.Number(0.3)
ap.save_overall_html(dest_dir_path="svg_text_fill_alpha/")
```

<iframe src="static/svg_text_fill_alpha/index.html" width="200" height="50"></iframe>

## line_color property interface example

The `line_color` property updates or gets the instance's line color:

```py
# runnable
import apysc as ap

ap.Stage(
    background_color=ap.Color("#333"),
    stage_width=200,
    stage_height=50,
    stage_elem_id="stage",
)
svg_text: ap.SVGText = ap.SVGText(
    text="Hello, world!",
    x=20,
    y=34,
    font_size=24,
    bold=True,
    fill_color=ap.COLORLESS,
    line_thickness=1,
)
svg_text.line_color = ap.String("#0af")
ap.save_overall_html(dest_dir_path="svg_text_line_color/")
```

<iframe src="static/svg_text_line_color/index.html" width="200" height="50"></iframe>

## line_alpha property interface example

The `line_alpha` property updates or gets the instance's line alpha (opacity):

```py
# runnable
import apysc as ap

ap.Stage(
    background_color=ap.Color("#333"),
    stage_width=200,
    stage_height=50,
    stage_elem_id="stage",
)
svg_text: ap.SVGText = ap.SVGText(
    text="Hello, world!",
    x=20,
    y=34,
    font_size=24,
    bold=True,
    fill_color=ap.COLORLESS,
    line_color=ap.Color("#0af"),
    line_thickness=1,
)
svg_text.line_alpha = ap.Number(0.3)
ap.save_overall_html(dest_dir_path="svg_text_line_alpha/")
```

<iframe src="static/svg_text_line_alpha/index.html" width="200" height="50"></iframe>

## line_thickness property interface example

The `line_thickness` property updates or gets the instance's line thickness (line width):

```py
# runnable
import apysc as ap

ap.Stage(
    background_color=ap.Color("#333"),
    stage_width=200,
    stage_height=50,
    stage_elem_id="stage",
)
svg_text: ap.SVGText = ap.SVGText(
    text="Hello, world!",
    x=20,
    y=34,
    font_size=24,
    bold=True,
    fill_color=ap.COLORLESS,
    line_color=ap.Color("#0af"),
)
svg_text.line_thickness = ap.Int(3)
ap.save_overall_html(dest_dir_path="svg_text_line_thickness/")
```

<iframe src="static/svg_text_line_thickness/index.html" width="200" height="50"></iframe>

## leading property interface example

The `leading` property updates or gets the instance's text leading (line height).

```py
# runnable
import apysc as ap

ap.Stage(
    background_color=ap.Color("#333"),
    stage_width=500,
    stage_height=120,
    stage_elem_id="stage",
)
svg_text: ap.SVGText = ap.SVGText(
    text="Lorem ipsum dolor sit amet,\nconsectetur adipiscing elit,\n"
    "sed do eiusmod tempor incididunt",
    x=20,
    y=32,
    fill_color=ap.Color("#aaa"),
)
svg_text.leading = ap.Number(2.0)

ap.save_overall_html(dest_dir_path="svg_text_leading/")
```

<iframe src="static/svg_text_leading/index.html" width="500" height="120"></iframe>

## align property interface example

The `align` property updates or gets the instance's horizontal text alignment (left, center, or right).

This property requires the `SVGTextAlign` enum.

```py
# runnable
import apysc as ap

ap.Stage(
    background_color=ap.Color("#333"),
    stage_width=500,
    stage_height=100,
    stage_elem_id="stage",
)
svg_text: ap.SVGText = ap.SVGText(
    text="Lorem ipsum dolor sit amet,\nconsectetur adipiscing elit,\n"
    "sed do eiusmod tempor incididunt",
    x=250,
    y=32,
    fill_color=ap.Color("#aaa"),
)
svg_text.align = ap.SVGTextAlign.CENTER

ap.save_overall_html(dest_dir_path="svg_text_align/")
```

<iframe src="static/svg_text_align/index.html" width="500" height="100"></iframe>

Note: This property setting changes x coordinate baseline (position of `x=0`), as follows:

- SVGTextAlign.CENTER: X coordinate baseline becomes the text's center position.
- SVGTextAlign.RIGHT: X coordinate baseline becomes the text's right position.

```py
# runnable
import apysc as ap

STAGE_WIDTH: int = 500
STAGE_HEIGHT: int = 120
ap.Stage(
    background_color=ap.Color("#333"),
    stage_width=STAGE_WIDTH,
    stage_height=STAGE_HEIGHT,
    stage_elem_id="stage",
)
container_sprite: ap.Sprite = ap.Sprite()
container_sprite.x = ap.Number(STAGE_WIDTH / 2)

vertical_x0_line: ap.Line = ap.Line(
    start_point=ap.Point2D(0, 0),
    end_point=ap.Point2D(0, STAGE_HEIGHT),
    line_color=ap.Color("#666"),
    parent=container_sprite,
)
x0_text: ap.SVGText = ap.SVGText(
    text="Text's x=0 position",
    fill_color=ap.Color("#666"),
    x=5,
    y=20,
    parent=container_sprite,
)

left_align_sample_text: ap.SVGText = ap.SVGText(
    text="Left align sample (default)",
    x=0,
    y=52,
    fill_color=ap.Color("#aaa"),
    parent=container_sprite,
)

center_align_sample_text: ap.SVGText = ap.SVGText(
    text="Center align sample",
    x=0,
    y=72,
    fill_color=ap.Color("#aaa"),
    parent=container_sprite,
)
center_align_sample_text.align = ap.SVGTextAlign.CENTER

right_align_sample_text: ap.SVGText = ap.SVGText(
    text="Right align sample",
    x=0,
    y=92,
    fill_color=ap.Color("#aaa"),
    parent=container_sprite,
)
right_align_sample_text.align = ap.SVGTextAlign.RIGHT

ap.save_overall_html(dest_dir_path="svg_text_align_note/")
```

<iframe src="static/svg_text_align_note/index.html" width="500" height="120"></iframe>

## bold property interface example

The `bold` property updates or gets the instance's `bold` text setting.

```py
# runnable
import apysc as ap

ap.Stage(
    background_color=ap.Color("#333"),
    stage_width=200,
    stage_height=50,
    stage_elem_id="stage",
)
svg_text: ap.SVGText = ap.SVGText(
    text="Bold style sample",
    x=20,
    y=32,
    fill_color=ap.Color("#aaa"),
)
svg_text.bold = ap.Boolean(True)
ap.save_overall_html(dest_dir_path="svg_text_bold/")
```

<iframe src="static/svg_text_bold/index.html" width="200" height="50"></iframe>

## italic property interface example

The `italic` property updates or gets the instance's `italic` style setting.

```py
# runnable
import apysc as ap

ap.Stage(
    background_color=ap.Color("#333"),
    stage_width=200,
    stage_height=50,
    stage_elem_id="stage",
)
svg_text: ap.SVGText = ap.SVGText(
    text="Italic style sample",
    x=20,
    y=32,
    fill_color=ap.Color("#aaa"),
)
svg_text.italic = ap.Boolean(True)
ap.save_overall_html(dest_dir_path="svg_text_italic/")
```

<iframe src="static/svg_text_italic/index.html" width="200" height="50"></iframe>

## rotation_around_center property interface example

The `rotation_around_center` property updates or gets the instance's rotation value (0 to 359) from the center point:

```py
# runnable
import apysc as ap

stage: ap.Stage = ap.Stage(
    background_color=ap.Color("#333"),
    stage_width=200,
    stage_height=50,
    stage_elem_id="stage",
)
svg_text: ap.SVGText = ap.SVGText(
    text="Hello, world!",
    x=100,
    y=32,
    fill_color=ap.Color("#aaa"),
    align=ap.SVGTextAlign.CENTER,
)


def on_enter_frame(e: ap.EnterFrameEvent, optional: dict) -> None:
    """
    The handler to handle a timer event.

    Parameters
    ----------
    e : ap.EnterFrameEvent
        Event instance.
    optional : dict
        Optional argument dictionary.
    """
    svg_text.rotation_around_center += 1


stage.enter_frame(handler=on_enter_frame)
ap.save_overall_html(dest_dir_path="svg_txt_rotation_around_center/")
```

<iframe src="static/svg_txt_rotation_around_center/index.html" width="200" height="50"></iframe>

## set_rotation_around_point and get_rotation_around_point methods interface example

The `set_rotation_around_point` method updates the instance's rotation value (0 to 359) from a specified point.

Similarly, the `get_rotation_around_point` method gets the instance's rotation value (0 to 359) from a specified point:

```py
# runnable
import apysc as ap

stage: ap.Stage = ap.Stage(
    background_color=ap.Color("#333"),
    stage_width=200,
    stage_height=120,
    stage_elem_id="stage",
)
X: ap.Number = ap.Number(20)
Y: ap.Number = ap.Number(32)
svg_text: ap.SVGText = ap.SVGText(
    text="Hello, world!",
    x=X,
    y=Y,
    fill_color=ap.Color("#aaa"),
)


def on_enter_frame(e: ap.EnterFrameEvent, optional: dict) -> None:
    """
    The handler to handle a timer event.

    Parameters
    ----------
    e : ap.EnterFrameEvent
        Event instance.
    optional : dict
        Optional argument dictionary.
    """
    rotation: ap.Int = (
        svg_text.get_rotation_around_point(
            x=X,
            y=Y,
        )
        + 1
    )
    svg_text.set_rotation_around_point(
        rotation=rotation,
        x=X,
        y=Y,
    )


stage.enter_frame(handler=on_enter_frame)
ap.save_overall_html(dest_dir_path="svg_txt_rotation_around_point/")
```

<iframe src="static/svg_txt_rotation_around_point/index.html" width="200" height="120"></iframe>

## Scale-related interfaces note

The scale-related interfaces are not recommended as the display may become distorted depending on the settings.

## scale_x_from_center property interface example

The `scale_x_from_center` property updates or gets the instance's scale-x from the center point:

```py
# runnable
import apysc as ap

stage: ap.Stage = ap.Stage(
    background_color=ap.Color("#333"),
    stage_width=200,
    stage_height=50,
    stage_elem_id="stage",
)
direction: ap.Int = ap.Int(-1)
svg_text: ap.SVGText = ap.SVGText(
    text="Hello, world!",
    x=20,
    y=32,
    fill_color=ap.Color("#aaa"),
)


def on_enter_frame(e: ap.EnterFrameEvent, optional: dict) -> None:
    """
    The handler to handle a timer event.

    Parameters
    ----------
    e : ap.EnterFrameEvent
        Event instance.
    optional : dict
        Optional argument dictionary.
    """
    scale: ap.Number = svg_text.scale_x_from_center
    with ap.If(scale > 1):
        direction.value = -1
    with ap.If(scale <= 0.3):
        direction.value = 1
    scale += direction * 0.005
    svg_text.scale_x_from_center = scale


stage.enter_frame(handler=on_enter_frame)
ap.save_overall_html(dest_dir_path="svg_txt_scale_x_from_center/")
```

<iframe src="static/svg_txt_scale_x_from_center/index.html" width="200" height="50"></iframe>

## set_scale_x_from_point and get_scale_x_from_point methods interface example

The `set_scale_x_from_point` method updates the instance's scale-x from a specified point.

Similarly, the `get_scale_x_from_point` method gets the instance's scale-x from a specified point:

```py
# runnable
import apysc as ap

stage: ap.Stage = ap.Stage(
    background_color=ap.Color("#333"),
    stage_width=200,
    stage_height=50,
    stage_elem_id="stage",
)
X: ap.Number = ap.Number(20)
direction: ap.Int = ap.Int(-1)
svg_text: ap.SVGText = ap.SVGText(
    text="Hello, world!",
    x=X,
    y=32,
    fill_color=ap.Color("#aaa"),
)


def on_enter_frame(e: ap.EnterFrameEvent, optional: dict) -> None:
    """
    The handler to handle a timer event.

    Parameters
    ----------
    e : ap.EnterFrameEvent
        Event instance.
    optional : dict
        Optional argument dictionary.
    """
    scale: ap.Number = svg_text.get_scale_x_from_point(x=X)
    with ap.If(scale > 1):
        direction.value = -1
    with ap.If(scale <= 0.3):
        direction.value = 1
    scale += direction * 0.005
    svg_text.set_scale_x_from_point(scale_x=scale, x=X)


stage.enter_frame(handler=on_enter_frame)
ap.save_overall_html(dest_dir_path="svg_txt_scale_x_from_point/")
```

<iframe src="static/svg_txt_scale_x_from_point/index.html" width="200" height="50"></iframe>

## flip_x property interface example

The `flip_x` property updates or gets the instance's flip-x (reflecting state) boolean value:

```py
# runnable
import apysc as ap

stage: ap.Stage = ap.Stage(
    background_color=ap.Color("#333"),
    stage_width=200,
    stage_height=50,
    stage_elem_id="stage",
)
svg_text: ap.SVGText = ap.SVGText(
    text="Hello, world!",
    x=20,
    y=32,
    fill_color=ap.Color("#aaa"),
)


def on_timer(e: ap.TimerEvent, options: dict) -> None:
    """
    The handler to handle a timer event.

    Parameters
    ----------
    e : ap.TimerEvent
        Event instance.
    options : dict
        Optional argument dictionary.
    """
    svg_text.flip_x = svg_text.flip_x.not_


ap.Timer(handler=on_timer, delay=1000).start()
ap.save_overall_html(dest_dir_path="svg_txt_flip_x/")
```

<iframe src="static/svg_txt_flip_x/index.html" width="200" height="50"></iframe>

## flip_y property interface example

The `flip_y` property updates or gets the instance's flip-y (reflecting state) boolean value:

```py
# runnable
import apysc as ap

stage: ap.Stage = ap.Stage(
    background_color=ap.Color("#333"),
    stage_width=200,
    stage_height=50,
    stage_elem_id="stage",
)
svg_text: ap.SVGText = ap.SVGText(
    text="Hello, world!",
    x=20,
    y=32,
    fill_color=ap.Color("#aaa"),
)


def on_timer(e: ap.TimerEvent, options: dict) -> None:
    """
    The handler to handle a timer event.

    Parameters
    ----------
    e : ap.TimerEvent
        Event instance.
    options : dict
        Optional argument dictionary.
    """
    svg_text.flip_y = svg_text.flip_y.not_


ap.Timer(handler=on_timer, delay=1000).start()
ap.save_overall_html(dest_dir_path="svg_txt_flip_y/")
```

<iframe src="static/svg_txt_flip_y/index.html" width="200" height="50"></iframe>

## SVGText constructor API

<!-- Docstring: apysc._display.svg_text.SVGText.__init__ -->

<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>

**[Interface signature]** `__init__(self, *, text: Union[str, apysc._type.string.String], font_size: Union[int, apysc._type.int.Int] = 16, font_family: Union[apysc._type.array.Array[apysc._type.string.String], List[str], NoneType] = None, x: Union[float, apysc._type.number.Number] = 0.0, y: Union[float, apysc._type.number.Number] = 16.0, fill_color: Union[str, apysc._type.string.String] = '#666', fill_alpha: Union[float, apysc._type.number.Number] = 1.0, line_color: Union[str, apysc._type.string.String] = '', line_alpha: Union[float, apysc._type.number.Number] = 1.0, line_thickness: Union[int, apysc._type.int.Int] = 1, leading: Union[float, apysc._type.number.Number] = 1.5, align: apysc._display.svg_text_align_mixin.SVGTextAlign = <SVGTextAlign.LEFT: 'start'>, bold: Union[bool, apysc._type.boolean.Boolean] = False, italic: Union[bool, apysc._type.boolean.Boolean] = False, parent: Union[apysc._display.child_mixin.ChildMixIn, NoneType] = None, variable_name_suffix: str = '') -> None`<hr>

**[Interface summary]**

The class for an SVG text.<hr>

**[Parameters]**

- `text`: Union[str, String]
  - A text to use in this class.
- `font_size`: Union[int, Int], optional
  - A font-size setting.
- `font_family`: Optional[Union[Array[String], List[str]]], optional
  - A font-family setting. Each string in an array needs to be a font name (e.g., `Times New Roman`).
- `x`: float or Number, optional
  - X-coordinate to start drawing.
- `y`: float or Number, optional
  - Y-coordinate to start drawing (please see also the `Notes` section).
- `fill_color`: str or String, optional
  - A fill-color setting.
- `fill_alpha`: float or Number, optional
  - A fill-alpha setting.
- `line_color`: str or String, default ''
  - A line-color setting.
- `line_alpha`: float or Number, optional
  - A line-alpha setting.
- `line_thickness`: int or Int, optional
  - A line-thickness (line-width) setting.
- `leading`: float or Number, optional
  - A text-leading size.
- `align`: SVGTextAlign, default SVGTextAlign.LEFT
  - A text-align setting.
- `bold`: Union[bool, Boolean], optional
  - A boolean, whether this text is a bold style or not.
- `italic`: Union[bool, Boolean], optional
  - A boolean, whether a text is an italic style or not (normal).
- `parent`: ChildMixIn or None, optional
  - A parent instance to add this instance. If a specified value is None, this interface uses a stage instance.
- `variable_name_suffix`: str, optional
  - A JavaScript variable name suffix string. This setting is sometimes useful for JavaScript debugging.

<hr>

**[Notes]**

 ・SVGText's y-coordinate zero-position starts at the bottom of a text. So if you set y=0, a text becomes almost invisible.<hr>

**[Examples]**

```py
>>> import apysc as ap
>>> stage: ap.Stage = ap.Stage(
...     background_color=ap.Color("#333"),
...     stage_width=200,
...     stage_height=50,
...     stage_elem_id="stage",
... )
>>> svg_text: ap.SVGText = ap.SVGText(
...     text="Hello, world!",
...     font_size=20,
...     fill_color=ap.Color("#0af"),
... )
>>> svg_text.text
String("Hello, world!")

>>> svg_text.font_size
Int(20)

>>> svg_text.fill_color
String("#00aaff")
```