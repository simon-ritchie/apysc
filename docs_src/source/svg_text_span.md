# SvgTextSpan class

This page explains the `SvgTextSpan` class.

## What interface is this?

The `SvgTextSpan` is the class for an SVG text-span (the child class of `SvgText`).

You can create an `SvgText` instance with multiple `SvgTextSpan` class instances and set different text styles.

## Basic usage

The `SvgTextSpan` class constructor requires the `text` argument.

The constructor also accepts each font's and style's argument, such as the `font_size`, `font_family`, `fill_color`, and `bold`.

If you skip the style settings' arguments, these settings become the parent SvgText's styles.

You can use `SvgTextSpan` instances to create an `SvgText` instance with the `create_with_svg_text_spans` class method.

```py
# runnable
import apysc as ap

stage: ap.Stage = ap.Stage(
    background_color=ap.Color("#333"),
    stage_width=200,
    stage_height=50,
    stage_elem_id="stage",
)
svg_text: ap.SvgText = ap.SvgText.create_with_svg_text_spans(
    text_spans=[
        ap.SvgTextSpan(text="Lorem "),
        ap.SvgTextSpan(text="ipsum ", font_size=20, fill_color=ap.Color("#0af")),
        ap.SvgTextSpan(text="dolor ", font_size=12),
    ],
    fill_color=ap.Color("#aaa"),
    font_size=16,
    x=20,
    y=32,
)

ap.save_overall_html(dest_dir_path="svg_txt_span_basic_usage/")
```

<iframe src="static/svg_txt_span_basic_usage/index.html" width="200" height="50"></iframe>

## Notes of the line breaking

The `SvgTextSpan` class ignores line breaks.

For instance, the following example's text contains a line break (`\n`), but the text line becomes a single line.

```py
# runnable
import apysc as ap

stage: ap.Stage = ap.Stage(
    background_color=ap.Color("#333"),
    stage_width=200,
    stage_height=50,
    stage_elem_id="stage",
)
svg_text: ap.SvgText = ap.SvgText.create_with_svg_text_spans(
    text_spans=[
        ap.SvgTextSpan(text="Lorem \n"),
        ap.SvgTextSpan(text="ipsum \n"),
        ap.SvgTextSpan(text="dolor"),
    ],
    x=20,
    y=32,
    fill_color=ap.Color("#aaa"),
)

ap.save_overall_html(dest_dir_path="svg_txt_span_notes_of_the_line_break/")
```

<iframe src="static/svg_txt_span_notes_of_the_line_break/index.html" width="200" height="50"></iframe>

If you want to add a line break, please use the `SvgText` class (not the `SvgTextSpan`) or create multiple `SvgText` instances.

## text property interface example

The `text` property updates or gets the instance's text.

```py
# runnable
import apysc as ap

stage: ap.Stage = ap.Stage(
    background_color=ap.Color("#333"),
    stage_width=200,
    stage_height=50,
    stage_elem_id="stage",
)
text_span_1: ap.SvgTextSpan = ap.SvgTextSpan(text="Lorem ")
text_span_2: ap.SvgTextSpan = ap.SvgTextSpan(text="ipsum")
text_span_2.text = ap.String("dolor")

svg_text: ap.SvgText = ap.SvgText.create_with_svg_text_spans(
    text_spans=[text_span_1, text_span_2],
    font_size=16,
    x=20,
    y=32,
    fill_color=ap.Color("#aaa"),
)

ap.save_overall_html(dest_dir_path="svg_txt_span_text/")
```

<iframe src="static/svg_txt_span_text/index.html" width="200" height="50"></iframe>

## font_size property interface example

The `font_size` property updates or gets the instance's font size.

```py
# runnable
import apysc as ap

stage: ap.Stage = ap.Stage(
    background_color=ap.Color("#333"),
    stage_width=200,
    stage_height=50,
    stage_elem_id="stage",
)
text_span_1: ap.SvgTextSpan = ap.SvgTextSpan(text="Lorem ")
text_span_2: ap.SvgTextSpan = ap.SvgTextSpan(text="ipsum")
text_span_2.font_size = ap.Int(25)

svg_text: ap.SvgText = ap.SvgText.create_with_svg_text_spans(
    text_spans=[text_span_1, text_span_2],
    font_size=16,
    x=20,
    y=32,
    fill_color=ap.Color("#aaa"),
)

ap.save_overall_html(dest_dir_path="svg_txt_span_font_size/")
```

<iframe src="static/svg_txt_span_font_size/index.html" width="200" height="50"></iframe>

## font_family property interface example

The `font_family` property updates or gets the instance's font family.

This property requires an `Array` of each font name `String`.

```py
# runnable
import apysc as ap

stage: ap.Stage = ap.Stage(
    background_color=ap.Color("#333"),
    stage_width=200,
    stage_height=50,
    stage_elem_id="stage",
)
text_span_1: ap.SvgTextSpan = ap.SvgTextSpan(text="Lorem ")
text_span_2: ap.SvgTextSpan = ap.SvgTextSpan(text="ipsum")
text_span_2.font_family = ap.Array([ap.String("Impact"), ap.String("Arial")])

svg_text: ap.SvgText = ap.SvgText.create_with_svg_text_spans(
    text_spans=[text_span_1, text_span_2],
    font_size=16,
    x=20,
    y=32,
    fill_color=ap.Color("#aaa"),
)

ap.save_overall_html(dest_dir_path="svg_txt_span_font_family/")
```

<iframe src="static/svg_txt_span_font_family/index.html" width="200" height="50"></iframe>

## fill_color property interface example

The `fill_color` property updates or gets the instance's fill color:

```py
# runnable
import apysc as ap

stage: ap.Stage = ap.Stage(
    background_color=ap.Color("#333"),
    stage_width=200,
    stage_height=50,
    stage_elem_id="stage",
)
text_span_1: ap.SvgTextSpan = ap.SvgTextSpan(text="Lorem ")
text_span_2: ap.SvgTextSpan = ap.SvgTextSpan(text="ipsum")
text_span_2.fill_color = ap.Color("#0af")

svg_text: ap.SvgText = ap.SvgText.create_with_svg_text_spans(
    text_spans=[text_span_1, text_span_2],
    font_size=16,
    x=20,
    y=32,
    fill_color=ap.Color("#aaa"),
)

ap.save_overall_html(dest_dir_path="svg_txt_span_fill_color/")
```

<iframe src="static/svg_txt_span_fill_color/index.html" width="200" height="50"></iframe>

## fill_alpha property interface example

The `fill_alpha` property updates or gets the instance's fill alpha (opacity):

```py
# runnable
import apysc as ap

stage: ap.Stage = ap.Stage(
    background_color=ap.Color("#333"),
    stage_width=200,
    stage_height=50,
    stage_elem_id="stage",
)
text_span_1: ap.SvgTextSpan = ap.SvgTextSpan(text="Lorem ")
text_span_2: ap.SvgTextSpan = ap.SvgTextSpan(text="ipsum")
text_span_2.fill_alpha = ap.Number(0.3)

svg_text: ap.SvgText = ap.SvgText.create_with_svg_text_spans(
    text_spans=[text_span_1, text_span_2],
    font_size=16,
    x=20,
    y=32,
    fill_color=ap.Color("#aaa"),
)

ap.save_overall_html(dest_dir_path="svg_txt_span_fill_alpha/")
```

<iframe src="static/svg_txt_span_fill_alpha/index.html" width="200" height="50"></iframe>

## line_color property interface example

The `line_color` property updates or gets the instance's line color:

```py
# runnable
import apysc as ap

stage: ap.Stage = ap.Stage(
    background_color=ap.Color("#333"),
    stage_width=200,
    stage_height=50,
    stage_elem_id="stage",
)
text_span_1: ap.SvgTextSpan = ap.SvgTextSpan(
    text="Lorem ", line_thickness=1, font_size=20, bold=True
)
text_span_1.line_color = ap.Color("#aaa")
text_span_2: ap.SvgTextSpan = ap.SvgTextSpan(
    text="ipsum", line_thickness=1, font_size=20, bold=True
)
text_span_2.line_color = ap.Color("#0af")

svg_text: ap.SvgText = ap.SvgText.create_with_svg_text_spans(
    text_spans=[text_span_1, text_span_2],
    font_size=16,
    x=20,
    y=32,
    fill_color=ap.COLORLESS,
)

ap.save_overall_html(dest_dir_path="svg_txt_span_line_color/")
```

<iframe src="static/svg_txt_span_line_color/index.html" width="200" height="50"></iframe>

## line_alpha property interface example

The `line_alpha` property updates or gets the instance's line alpha (opacity):

```py
# runnable
import apysc as ap

stage: ap.Stage = ap.Stage(
    background_color=ap.Color("#333"),
    stage_width=200,
    stage_height=50,
    stage_elem_id="stage",
)
text_span_1: ap.SvgTextSpan = ap.SvgTextSpan(
    text="Lorem ",
    line_color=ap.Color("#0af"),
    line_thickness=1,
    font_size=20,
    bold=True,
)
text_span_2: ap.SvgTextSpan = ap.SvgTextSpan(
    text="ipsum",
    line_color=ap.Color("#0af"),
    line_thickness=1,
    font_size=20,
    bold=True,
)
text_span_2.line_alpha = ap.Number(0.3)

svg_text: ap.SvgText = ap.SvgText.create_with_svg_text_spans(
    text_spans=[text_span_1, text_span_2],
    font_size=16,
    x=20,
    y=32,
    fill_color=ap.COLORLESS,
)

ap.save_overall_html(dest_dir_path="svg_txt_span_line_alpha/")
```

<iframe src="static/svg_txt_span_line_alpha/index.html" width="200" height="50"></iframe>

## line_thickness property interface example

The `line_thickness` property updates or gets the instance's line thickness (line width):

```py
# runnable
import apysc as ap

stage: ap.Stage = ap.Stage(
    background_color=ap.Color("#333"),
    stage_width=200,
    stage_height=50,
    stage_elem_id="stage",
)
text_span_1: ap.SvgTextSpan = ap.SvgTextSpan(
    text="Lorem ",
    line_color=ap.Color("#0af"),
    font_size=20,
    bold=True,
)
text_span_2: ap.SvgTextSpan = ap.SvgTextSpan(
    text="ipsum",
    line_color=ap.Color("#0af"),
    font_size=20,
    bold=True,
)
text_span_1.line_thickness = ap.Int(3)
text_span_2.line_thickness = ap.Int(3)

svg_text: ap.SvgText = ap.SvgText.create_with_svg_text_spans(
    text_spans=[text_span_1, text_span_2],
    font_size=16,
    x=20,
    y=32,
    fill_color=ap.COLORLESS,
)

ap.save_overall_html(dest_dir_path="svg_txt_span_line_thickness/")
```

<iframe src="static/svg_txt_span_line_thickness/index.html" width="200" height="50"></iframe>

## bold property interface example

The `bold` property updates or gets the instance's `bold` text setting.

```py
# runnable
import apysc as ap

stage: ap.Stage = ap.Stage(
    background_color=ap.Color("#333"),
    stage_width=200,
    stage_height=50,
    stage_elem_id="stage",
)
text_span_1: ap.SvgTextSpan = ap.SvgTextSpan(text="Lorem ")
text_span_2: ap.SvgTextSpan = ap.SvgTextSpan(text="ipsum")
text_span_2.bold = ap.Boolean(True)

svg_text: ap.SvgText = ap.SvgText.create_with_svg_text_spans(
    text_spans=[text_span_1, text_span_2],
    font_size=16,
    x=20,
    y=32,
    fill_color=ap.Color("#aaa"),
)

ap.save_overall_html(dest_dir_path="svg_txt_span_bold/")
```

<iframe src="static/svg_txt_span_bold/index.html" width="200" height="50"></iframe>

## italic property interface example

The `italic` property updates or gets the instance's `italic` style setting.

```py
# runnable
import apysc as ap

stage: ap.Stage = ap.Stage(
    background_color=ap.Color("#333"),
    stage_width=200,
    stage_height=50,
    stage_elem_id="stage",
)
text_span_1: ap.SvgTextSpan = ap.SvgTextSpan(text="Lorem ")
text_span_2: ap.SvgTextSpan = ap.SvgTextSpan(text="ipsum")
text_span_2.italic = ap.Boolean(True)

svg_text: ap.SvgText = ap.SvgText.create_with_svg_text_spans(
    text_spans=[text_span_1, text_span_2],
    font_size=16,
    x=20,
    y=32,
    fill_color=ap.Color("#aaa"),
)

ap.save_overall_html(dest_dir_path="svg_txt_span_italic/")
```

<iframe src="static/svg_txt_span_italic/index.html" width="200" height="50"></iframe>

## delta_x property interface example

The `delta_x` property updates or gets the instance's delta-x (x-coordinate adjustment).

```py
# runnable
import apysc as ap

stage: ap.Stage = ap.Stage(
    background_color=ap.Color("#333"),
    stage_width=200,
    stage_height=50,
    stage_elem_id="stage",
)
text_span_1: ap.SvgTextSpan = ap.SvgTextSpan(text="Lorem ")
text_span_2: ap.SvgTextSpan = ap.SvgTextSpan(text="ipsum")
text_span_2.delta_x = ap.Number(-20)

svg_text: ap.SvgText = ap.SvgText.create_with_svg_text_spans(
    text_spans=[text_span_1, text_span_2],
    font_size=16,
    x=20,
    y=32,
    fill_color=ap.Color("#aaa"),
)

ap.save_overall_html(dest_dir_path="svg_txt_span_delta_x/")
```

<iframe src="static/svg_txt_span_delta_x/index.html" width="200" height="50"></iframe>

## delta_y property interface example

The `delta_y` property updates or gets the instance's delta-y (y-coordinate adjustment).

Note: This setting inherits a y-coordinate from the previous `SvgTextSpan` instance.

```py
# runnable
import apysc as ap

stage: ap.Stage = ap.Stage(
    background_color=ap.Color("#333"),
    stage_width=200,
    stage_height=80,
    stage_elem_id="stage",
)
text_span_1: ap.SvgTextSpan = ap.SvgTextSpan(text="Lorem ")
text_span_2: ap.SvgTextSpan = ap.SvgTextSpan(text="ipsum ")
text_span_3: ap.SvgTextSpan = ap.SvgTextSpan(text="dolar")

text_span_2.delta_y = ap.Number(10)
text_span_3.delta_y = ap.Number(10)

svg_text: ap.SvgText = ap.SvgText.create_with_svg_text_spans(
    text_spans=[text_span_1, text_span_2],
    font_size=16,
    x=20,
    y=32,
    fill_color=ap.Color("#aaa"),
)

ap.save_overall_html(dest_dir_path="svg_txt_span_delta_y/")
```

<iframe src="static/svg_txt_span_delta_y/index.html" width="200" height="80"></iframe>

## SvgTextSpan constructor API

<!-- Docstring: apysc._display.svg_text_span.SvgTextSpan.__init__ -->

<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>

**[Interface signature]** `__init__(self, *, text: Union[str, apysc._type.string.String], font_size: Union[int, apysc._type.int.Int, NoneType] = None, font_family: Union[apysc._type.array.Array[apysc._type.string.String], List[str], NoneType] = None, fill_color: Union[apysc._color.color.Color, NoneType] = None, fill_alpha: Union[float, apysc._type.number.Number, NoneType] = None, line_color: Union[apysc._color.color.Color, NoneType] = None, line_alpha: Union[float, apysc._type.number.Number, NoneType] = None, line_thickness: Union[int, apysc._type.int.Int, NoneType] = None, bold: Union[bool, apysc._type.boolean.Boolean, NoneType] = None, italic: Union[bool, apysc._type.boolean.Boolean, NoneType] = None, delta_x: Union[float, apysc._type.number.Number] = 0.0, delta_y: Union[float, apysc._type.number.Number] = 0.0, variable_name_suffix: str = '') -> None`<hr>

**[Interface summary]**

The class for an SVG text-span (the child class of `SvgText`).<hr>

**[Parameters]**

- `text`: Union[str, String]
  - A text to use in this class.
- `font_size`: Optional[Union[int, Int]], optional
  - A font-size setting.
- `font_family`: Optional[Union[Array[String], List[str]]], optional
  - A font-family setting. Each string in an array needs to be a font name (e.g., `Times New Roman`).
- `fill_color`: Optional[Color], optional
  - A fill-color setting.
- `fill_alpha`: Optional[Union[float, Number]], optional
  - A fill-alpha setting.
- `line_color`: Optional[Color], optional
  - A line-color setting.
- `line_alpha`: Optional[Union[float, Number]], optional
  - A line-alpha setting.
- `line_thickness`: Optional[Union[int, Int]], optional
  - A line-thickness (line-width) to set.
- `bold`: Optional[Union[bool, Boolean]], optional
  - A boolean, whether this text is a bold style or not.
- `italic`: Optional[Union[bool, Boolean]], optional
  - A boolean, whether a text is an italic style or not (normal).
- `delta_x`: Union[float, Number], optional
  - A coordinate delta-x setting. Notes: This setting also changes a coordinate of subsequent `SvgTextSpan`'s instance.
- `delta_y`: Union[float, Number], optional
  - A coordinate delta-y setting. Notes: This setting also changes a coordinate of subsequent `SvgTextSpan`'s instance.
- `variable_name_suffix`: str, optional
  - A JavaScript variable name suffix string. This setting is sometimes useful for JavaScript debugging.

<hr>

**[Notes]**

 ・If style settings are `None`, its styles inherit parent style settings.<hr>

**[Examples]**

```py
>>> import apysc as ap
>>> stage: ap.Stage = ap.Stage(
...     background_color=ap.Color("#333"), stage_width=200, stage_height=50
... )
>>> svg_text: ap.SvgText = ap.SvgText.create_with_svg_text_spans(
...     text_spans=[
...         ap.SvgTextSpan(text="Hello, "),
...         ap.SvgTextSpan(text="Hello, ", font_size=14),
...     ],
...     font_size=20,
...     fill_color=ap.Color("#0af"),
... )
```

<hr>

**[References]**

- [SvgText class](https://simon-ritchie.github.io/apysc/en/svg_text.html)

## SvgText create_with_svg_text_spans class method API

<!-- Docstring: apysc._display.svg_text.SvgText.create_with_svg_text_spans -->

<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>

**[Interface signature]** `create_with_svg_text_spans(*, text_spans: Union[List[apysc._display.svg_text_span.SvgTextSpan], apysc._type.array.Array[apysc._display.svg_text_span.SvgTextSpan]], font_size: Union[int, apysc._type.int.Int] = 16, font_family: Union[apysc._type.array.Array[apysc._type.string.String], List[str], NoneType] = None, x: Union[float, apysc._type.number.Number] = 0.0, y: Union[float, apysc._type.number.Number] = 16.0, fill_color: apysc._color.color.Color = Color("#666666"), fill_alpha: Union[float, apysc._type.number.Number] = 1.0, line_color: apysc._color.color.Color = Color(""), line_alpha: Union[float, apysc._type.number.Number] = 1.0, line_thickness: Union[int, apysc._type.int.Int] = 1, leading: Union[float, apysc._type.number.Number] = 1.5, align: apysc._display.svg_text_align_mixin.SvgTextAlign = <SvgTextAlign.LEFT: 'start'>, bold: Union[bool, apysc._type.boolean.Boolean] = False, italic: Union[bool, apysc._type.boolean.Boolean] = False, parent: Union[apysc._display.child_mixin.ChildMixIn, NoneType] = None, variable_name_suffix: str = '') -> 'SvgText'`<hr>

**[Interface summary]**

Create an `SvgText` instance with specified text spans.<hr>

**[Parameters]**

- `text_spans`: Union[List[SvgTextSpan], Array[SvgTextSpan]]
  - Text spans.
- `font_size`: Union[int, Int], optional
  - A font-size setting for an overall text.
- `font_family`: Optional[Union[Array[String], List[str]]], optional
  - A font-family setting for an overall text. Each string in an array needs to be a font name (e.g., `Times New Roman`).
- `x`: Union[float, Number], optional
  - X-coordinate to start drawing.
- `y`: Union[float, Number], optional
  - Y-coordinate to start drawing (please see also the `Notes` section).
- `fill_color`: Color, optional
  - A fill-color setting for an overall text.
- `fill_alpha`: float or Number, optional
  - A fill-alpha setting for an overall text.
- `line_color`: Color, optional
  - A line-color setting for an overall text.
- `line_alpha`: float or Number, optional
  - A line-alpha setting for an overall text.
- `line_thickness`: int or Int, optional
  - A line-thickness (line-width) setting for an overall text.
- `leading`: float or Number, optional
  - A text-leading size for an overall text.
- `align`: SvgTextAlign, optional
  - A text-align setting for an overall text.
- `bold`: Union[bool, Boolean], optional
  - A boolean, whether this text is a bold style or not.
- `italic`: Union[bool, Boolean], optional
  - A boolean, whether a text is an italic style or not (normal).
- `parent`: Optional[ChildMixIn], optional
  - A parent instance to add this instance. If the specified value is None, this interface uses a stage instance.
- `variable_name_suffix`: str, optional
  - A JavaScript variable name suffix string. This setting is sometimes useful for JavaScript debugging.

<hr>

**[Returns]**

- `svg_text`: SvgText
  - A created `SvgText` instance.

<hr>

**[Notes]**

 ・SvgText's y-coordinate zero-position starts at the bottom of a text. So if you set y=0, a text becomes almost invisible.<hr>

**[Examples]**

```py
>>> import apysc as ap
>>> stage: ap.Stage = ap.Stage(
...     background_color=ap.Color("#333"),
...     stage_width=200,
...     stage_height=50,
... )
>>> svg_text: ap.SvgText = ap.SvgText.create_with_svg_text_spans(
...     text_spans=[
...         ap.SvgTextSpan(text="Hello, "),
...         ap.SvgTextSpan(text="Hello, ", font_size=14),
...     ],
...     font_size=20,
...     fill_color=ap.Color("#0af"),
... )
```

<hr>

**[References]**

- [SvgText class](https://simon-ritchie.github.io/apysc/en/svg_text.html)