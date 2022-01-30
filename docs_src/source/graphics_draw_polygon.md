# Graphics draw_polygon interface

This page explains the `Graphics` class `draw_polygon` method interface.

## What interface is this?

The `draw_polygon` interface draws vector polygon graphics. This interface works slightly similar to the `line_to` and `move_to` interfaces, but the paths do not need to be closed.

## Basic usage

The `draw_polygon` interface has the `points` argument, which determines the polygon vertices coordinates.

```py
# runnable
import apysc as ap

ap.Stage(
    background_color='#333',
    stage_width=250,
    stage_height=150,
    stage_elem_id='stage')

sprite: ap.Sprite = ap.Sprite()

# Draw the triangle with the draw_polygon interface.
sprite.graphics.begin_fill(color='#0af')
sprite.graphics.draw_polygon(
    points=ap.Array([
        ap.Point2D(x=75, y=50),
        ap.Point2D(x=50, y=100),
        ap.Point2D(x=100, y=100),
    ]))

# Draw the diamond shape with the draw_polygon interface.
sprite.graphics.draw_polygon(
    points=ap.Array([
        ap.Point2D(x=175, y=50),
        ap.Point2D(x=150, y=75),
        ap.Point2D(x=175, y=100),
        ap.Point2D(x=200, y=75),
    ]))

ap.save_overall_html(
    dest_dir_path='graphics_draw_polygon_basic_usage/')
```

<iframe src="static/graphics_draw_polygon_basic_usage/index.html" width="250" height="150"></iframe>

## Difference between the line_to and draw_polygon interfaces

If you set the fill color, the `draw_polygon` interface becomes slightly similar to the `line_to` (and `move_to`) interfaces. So, for example, the following codes both draw the triangle.

The `draw_polygon` interface draws the left rectangle. Similarly, the `move_to` and `line_to` interfaces draw the right one.

```py
# runnable
import apysc as ap

ap.Stage(
    background_color='#333',
    stage_width=250,
    stage_height=150,
    stage_elem_id='stage')

sprite: ap.Sprite = ap.Sprite()
sprite.graphics.begin_fill(color='#0af')

# Draw the triangle with the draw_polygon interface.
sprite.graphics.draw_polygon(
    points=ap.Array([
        ap.Point2D(x=75, y=50),
        ap.Point2D(x=50, y=100),
        ap.Point2D(x=100, y=100),
    ]))

# Draw the triangle with the move_to and line_to interfaces.
sprite.graphics.move_to(x=175, y=50)
sprite.graphics.line_to(x=150, y=100)
sprite.graphics.line_to(x=200, y=100)

ap.save_overall_html(
    dest_dir_path='graphics_draw_polygon_line_to_difference_1/')
```

<iframe src="static/graphics_draw_polygon_line_to_difference_1/index.html" width="250" height="150"></iframe>

But there is a difference in whether closing the paths is necessary or not. This difference becomes significant when you set the line style setting. The `line_to` interface does not close the paths from end coordinates to start coordinates.

```py
# runnable
import apysc as ap

stage: ap.Stage = ap.Stage(
    background_color='#333',
    stage_width=250,
    stage_height=150,
    stage_elem_id='stage')

sprite: ap.Sprite = ap.Sprite()
sprite.graphics.begin_fill(color='#0af')

# Set the line style to see the difference.
sprite.graphics.line_style(color='#fff', thickness=3)

# Draw the triangle with the draw_polygon interface.
sprite.graphics.draw_polygon(
    points=ap.Array([
        ap.Point2D(x=75, y=50),
        ap.Point2D(x=50, y=100),
        ap.Point2D(x=100, y=100),
    ]))

# Draw the triangle with the move_to and line_to interfaces.
sprite.graphics.move_to(x=175, y=50)
sprite.graphics.line_to(x=150, y=100)
sprite.graphics.line_to(x=200, y=100)

ap.save_overall_html(
    dest_dir_path='graphics_draw_polygon_line_to_difference_2/')
```

<iframe src="static/graphics_draw_polygon_line_to_difference_2/index.html" width="250" height="150"></iframe>

## Return value

The `draw_polygon` interface returns the `Polygon` instance. And that has the basic interface as same as the other type graphics instances. The `Polygon` instance also has the `append_line_point` method interface to append points dynamically.

For instance, the following code appends the point and changes from the triangle to the rectangle.

```py
# runnable
import apysc as ap

ap.Stage(
    background_color='#333',
    stage_width=150,
    stage_height=150,
    stage_elem_id='stage')

sprite: ap.Sprite = ap.Sprite()
sprite.graphics.begin_fill(color='#0af')

# Draw the triangle.
polygon: ap.Polygon = sprite.graphics.draw_polygon(
    points=ap.Array([
        ap.Point2D(x=75, y=50),
        ap.Point2D(x=50, y=75),
        ap.Point2D(x=75, y=100),
    ]))

# Append the point and change to the rectangle dynamically.
polygon.append_line_point(x=100, y=75)

ap.save_overall_html(
    dest_dir_path='graphics_draw_polygon_append_line_point/')
```

<iframe src="static/graphics_draw_polygon_append_line_point/index.html" width="150" height="150"></iframe>


## draw_polygon API

<!-- Docstring: apysc._display.graphics.Graphics.draw_polygon -->

<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>

**[Interface signature]** `draw_polygon(self, points:Union[List[apysc._geom.point2d.Point2D], apysc._type.array.Array[apysc._geom.point2d.Point2D]]) -> '_polyg.Polygon'`<hr>

**[Interface summary]** Draw a polygon vector graphic. This interface is similar to the Polyline class (created by `move_to` or `line_to`). But unlike that, this interface connects the last point and the start point.<hr>

**[Parameters]**

- `points`: list of Point2D or Array.
  - Polygon vertex points.

<hr>

**[Returns]**

- `polygon`: Polygon
  - Created polygon graphics instance.

<hr>

**[Examples]**

```py
>>> import apysc as ap
>>> stage: ap.Stage = ap.Stage()
>>> sprite: ap.Sprite = ap.Sprite()
>>> sprite.graphics.begin_fill(color='#0af')
>>> polygon: ap.Polygon = sprite.graphics.draw_polygon(
...     points=[
...         ap.Point2D(x=25, y=0),
...         ap.Point2D(x=0, y=50),
...         ap.Point2D(x=50, y=50),
...     ])
>>> polygon.fill_color
String('#00aaff')
```