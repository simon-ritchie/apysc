# Point2D

This page explains the `Point2D` class.

## What is the Point2D class?

The `Point2D` class is the 2D coordinates class interface. This interface handles the x-coordinate and y-coordinate. This interface is used, for example, the `Polygon` class drawing to specify each vertex point.

## Basic usage

The `Point2D` class constructor requires the `x` and `y` arguments. Both parameters type is the Python built-in `int` or `Int`\.

```py
# runnable
import apysc as ap

point_1: ap.Point2D = ap.Point2D(x=10, y=20)

x: ap.Int = ap.Int(10)
y: ap.Int = ap.Int(20)
point_2: ap.Point2D = ap.Point2D(x=x, y=y)
```

## X and y getter interfaces

The `Point2D` class `x` and `y` property interfaces returns the `Int` type value, as follows:

```py
# runnable
import apysc as ap

point: ap.Point2D = ap.Point2D(x=10, y=20)
assert point.x == 10
assert point.y == 20
```

## X and y setter interfaces

The `x` and `y` property can be updated with an `Int` type value, as follows:

```py
# runnable
import apysc as ap

point: ap.Point2D = ap.Point2D(x=10, y=20)
point.x = ap.Int(30)
assert point.x == 30
```

## Usage example of the draw_polygon interface

The `draw_polygon` interface requires the `Point2D` list argument so that this section shows the example of the `Point2D` class with that drawing interface.

The following draws the triangle vector graphics by specifying the three points:

```py
# runnable
import apysc as ap

ap.Stage(
    stage_width=150, stage_height=150, background_color='#333',
    stage_elem_id='stage')
sprite: ap.Sprite = ap.Sprite()
sprite.graphics.begin_fill(color='#0af')

sprite.graphics.draw_polygon(
    points=[
        ap.Point2D(x=75, y=50),
        ap.Point2D(x=50, y=100),
        ap.Point2D(x=100, y=100),
    ])

ap.save_overall_html(
    dest_dir_path='point2d_basic_usage/')
```

<iframe src="static/point2d_basic_usage/index.html" width="150" height="150"></iframe>


## Point2D class constructor API

<!-- Docstring: apysc._geom.point2d.Point2D.__init__ -->

<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>

**[Interface signature]** `__init__(self, x:Union[int, apysc._type.int.Int], y:Union[int, apysc._type.int.Int]) -> None`<hr>

**[Interface summary]** 2-dimensional geometry point.<hr>

**[Parameters]**

- `x`: int or Int
  - X-coordinate.
- `y`: int or Int
  - Y-coordinate.

<hr>

**[Examples]**

```py
>>> import apysc as ap
>>> stage: ap.Stage = ap.Stage()
>>> sprite: ap.Sprite = ap.Sprite()
>>> sprite.graphics.begin_fill(color='#0af')
>>> polygon: ap.Polygon = sprite.graphics.draw_polygon(
...     points=[
...         ap.Point2D(x=0, y=0),
...         ap.Point2D(x=0, y=50),
...         ap.Point2D(x=50, y=25),
...     ])
```

## x property API

<!-- Docstring: apysc._geom.point2d.Point2D.x -->

<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>

**[Interface summary]** X-coordinate property.<hr>

**[Returns]**

- `x`: Int
  - X-coordinate.

<hr>

**[Examples]**

```py
>>> import apysc as ap
>>> point: ap.Point2D = ap.Point2D(x=50, y=100)
>>> point.x = ap.Int(150)
>>> point.x
Int(150)
```

## y property API

<!-- Docstring: apysc._geom.point2d.Point2D.y -->

<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>

**[Interface summary]** Y-coordinate property.<hr>

**[Returns]**

- `y`: Int
  - Y-coordinate.

<hr>

**[Examples]**

```py
>>> import apysc as ap
>>> point: ap.Point2D = ap.Point2D(x=50, y=100)
>>> point.y = ap.Int(150)
>>> point.y
Int(150)
```