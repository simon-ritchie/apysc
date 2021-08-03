# Point2D

This page will explain the `Point2D` class.

## What is the Point2D class?

The `Point2D` class is the basic 2D coordinates class interface. This handles the x-coordinate and y-coordinate. This is used, for example, the `Polygon` class drawing to specify each vertex point.

## Basic usage

The `Point2D` class constructor requires two parameters, the `x` and `y`. Both parameters type is the Python built-in `int` or `Int`.

```py
# runnable
import apysc as ap

point_1: ap.Point2D = ap.Point2D(x=10, y=20)

x: ap.Int = ap.Int(10)
y: ap.Int = ap.Int(20)
point_2: ap.Point2D = ap.Point2D(x=x, y=y)
```

## X and y getter interfaces

The `Point2D` class `x` and `y` property interfaces will return the `Int` type value, as follows:

```py
# runnable
import apysc as ap

point: ap.Point2D = ap.Point2D(x=10, y=20)
assert point.x == 10
assert point.y == 20
```

## X and y setter interfaces

The `x` and `y` property can be updated with a `Int` type value, as follows:

```py
# runnable
import apysc as ap

point: ap.Point2D = ap.Point2D(x=10, y=20)
point.x = ap.Int(30)
assert point.x == 30
```

## Usage example of the draw_polygon interface

The `draw_polygon` interface will requires `Point2D` list argument, so this section will show the example of the `Point2D` class with that drawing interface.

The following will draw the triangle vector graphics by specification of the three points:

```py
# runnable
import apysc as ap

stage: ap.Stage = ap.Stage(
    stage_width=150, stage_height=150, background_color='#333',
    stage_elem_id='stage')
sprite: ap.Sprite = ap.Sprite(stage=stage)
sprite.graphics.begin_fill(color='#0af')

sprite.graphics.draw_polygon(
    points=[
        ap.Point2D(x=75, y=50),
        ap.Point2D(x=50, y=100),
        ap.Point2D(x=100, y=100),
    ])

ap.save_overall_html(dest_dir_path='point2d_basic_usage/')
```

<iframe src="static/point2d_basic_usage/index.html" width="150" height="150"></iframe>
