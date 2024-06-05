# SvgMask class and its related interfaces

This page explains the `SvgMask` class and related interfaces, such as the `add_svg_masking_object` method and `svg_mask` property.

## What class is this?

The `SvgMask` handles SVG graphics mask settings.

You can set another SVG `DisplayObject` as a mask for an SVG `DisplayObject` (e.g., `Rectangle`) to display only the overlapping area.

## Basic usage

You can apply the mask setting in the following steps:

1. Create an `SvgMask` instance.

2. Add a `DisplayObject` to the created `SvgMask` instance with the `add_svg_masking_object` method.

3. Set a mask instance to the target `DisplayObject`'s `svg_mask` property.

```py
# runnable
import apysc as ap

ap.Stage(
    background_color=ap.Color("#333"),
    stage_width=150,
    stage_height=150,
    stage_elem_id="stage",
)

# 1. Create an `SvgMask` instance.
mask: ap.SvgMask = ap.SvgMask()
circle: ap.Circle = ap.Circle(x=100, y=100, radius=50, fill_color=ap.Colors.CYAN_00AAFF)

# 2. Add a `DisplayObject` to the created `SvgMask` instance.
mask.add_svg_masking_object(masking_object=circle)
rectangle: ap.Rectangle = ap.Rectangle(
    x=0, y=0, width=100, height=100, fill_color=ap.Colors.CYAN_00AAFF
)

# 3. Set a mask instance to the target `DisplayObject`'s `svg_mask` property.
rectangle.svg_mask = mask

ap.save_overall_html(dest_dir_path="svg_mask_basic_usage/")
```

<iframe src="static/svg_mask_basic_usage/index.html" width="150" height="150"></iframe>

## SvgMask constructor API

<!-- Docstring: apysc._mask.svg_mask.SvgMask.__init__ -->

<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>

**[Interface signature]** `__init__(self, *, variable_name_suffix: str = '') -> None`<hr>

**[Interface summary]**

The class for the SVG masking.<hr>

**[Parameters]**

- `variable_name_suffix`: str, default ""
  - A JavaScript variable name suffix string. This setting is sometimes useful for JavaScript debugging.

<hr>

**[Examples]**

```py
>>> import apysc as ap
>>> _ = ap.Stage()
>>> mask: ap.SvgMask = ap.SvgMask()
>>> circle: ap.Circle = ap.Circle(
...     x=50, y=50, radius=50, fill_color=ap.Colors.CYAN_00AAFF
... )
>>> mask.add_svg_masking_object(masking_object=circle)
>>> rectangle: ap.Rectangle = ap.Rectangle(
...     x=0, y=0, width=100, height=100, fill_color=ap.Colors.CYAN_00AAFF
... )
>>> rectangle.svg_mask = mask
```

## SvgMask add_svg_masking_object method API

<!-- Docstring: apysc._mask.svg_mask.SvgMask.add_svg_masking_object -->

<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>

**[Interface signature]** `add_svg_masking_object(self, *, masking_object: apysc._display.fill_color_mixin.FillColorMixIn) -> None`<hr>

**[Interface summary]**

Add an SVG masking object to this mask. This instance uses its masking object to mask other SVG graphics objects. It is possible to add multiple masking objects to a mask.<hr>

**[Parameters]**

- `masking_object`: FillColorMixIn
  - The masking object to add.

<hr>

**[Examples]**

```py
>>> import apysc as ap
>>> _ = ap.Stage()
>>> mask: ap.SvgMask = ap.SvgMask()
>>> circle: ap.Circle = ap.Circle(
...     x=50, y=50, radius=50, fill_color=ap.Colors.CYAN_00AAFF
... )
>>> mask.add_svg_masking_object(masking_object=circle)
>>> rectangle: ap.Rectangle = ap.Rectangle(
...     x=0, y=0, width=100, height=100, fill_color=ap.Colors.CYAN_00AAFF
... )
>>> rectangle.svg_mask = mask
```

## svg_mask property API

<!-- Docstring: apysc._mask.svg_mask_mixin.SvgMaskMixIn.svg_mask -->

<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>

**[Interface summary]**

Get an SVG mask setting. If the mask is not set, this property becomes `None`.<hr>

**[Returns]**

- `mask`: Optional[SvgMask]
  - A mask setting.

<hr>

**[Examples]**

```py
>>> import apysc as ap
>>> _ = ap.Stage()
>>> mask: ap.SvgMask = ap.SvgMask()
>>> circle: ap.Circle = ap.Circle(
...     x=50, y=50, radius=50, fill_color=ap.Colors.CYAN_00AAFF
... )
>>> mask.add_svg_masking_object(masking_object=circle)
>>> rectangle: ap.Rectangle = ap.Rectangle(
...     x=0, y=0, width=100, height=100, fill_color=ap.Colors.CYAN_00AAFF
... )
>>> rectangle.svg_mask = mask
>>> assert rectangle.svg_mask == mask
```