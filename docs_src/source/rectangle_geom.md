# RectangleGeom class

This page explains the `RectangleGeom` class.

## What class is this?

The `RectangleGeom` class has the rectangle's geometry interfaces, such as the `left_x`, `center_x`, `right_x`, `top_y`, `center_y`, `bottom_y`, `width`, and `height`.

## Basic usage

Mainly, the apysc initializes the `RectangleGeom` class.

For instance, the `get_bounds` method returns a `RectangleGeom` instance; and sets its instance's rectangle geometry data (bounding box).

```py
# runnable
import apysc as ap
stage: ap.Stage = ap.Stage(
    background_color="#333", stage_width=200, stage_height=200
)
rectangle: ap.Rectangle = ap.Rectangle(
    x=50,
    y=50,
    width=100,
    height=75,
)
bounding_box: ap.RectangleGeom = rectangle.get_bounds()
# text: ap.SVGText = ap.SVGText(text=)
```
