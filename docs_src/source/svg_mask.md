# SvgMask class and its related interfaces

This page explains the `SvgMask` class and related interfaces, such as the `add_svg_masking_object` method and `svg_mask` property.

## What class is this?

The `SvgMask` handles SVG graphics mask settings.

You can set another SVG `DisplayObject` as a mask for an SVG `DisplayObject` (e.g., `ap.Rectangle`) to display only the overlapping area.

## Basic usage

You can apply the mask setting in the following steps:

1. Create an `SvgMask` instance.

2. Add a `DisplayObject` to the created `SvgMask` instance with the `add_svg_masking_object` method.

3. Set a mask instance to the target `DisplayObject`'s `svg_mask` property.