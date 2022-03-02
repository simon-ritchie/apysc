"""This module is for the translation mapping data of the
following document:

Document file: graphics_draw_polygon.md
Language: jp
"""

from typing import Dict

MAPPING: Dict[str, str] = {

    '# Graphics draw_polygon interface':
    '',

    'This page explains the `Graphics` class `draw_polygon` method interface.':  # noqa
    '',

    '## What interface is this?':
    '',

    'The `draw_polygon` interface draws vector polygon graphics. This interface works slightly similar to the `line_to` and `move_to` interfaces, but the paths do not need to be closed.':  # noqa
    '',

    '## Basic usage':
    '',

    'The `draw_polygon` interface has the `points` argument, which determines the polygon vertices coordinates.':  # noqa
    '',

    '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    background_color=\'#333\',\n    stage_width=250,\n    stage_height=150,\n    stage_elem_id=\'stage\')\n\nsprite: ap.Sprite = ap.Sprite()\n\n# Draw the triangle with the draw_polygon interface.\nsprite.graphics.begin_fill(color=\'#0af\')\nsprite.graphics.draw_polygon(\n    points=ap.Array([\n        ap.Point2D(x=75, y=50),\n        ap.Point2D(x=50, y=100),\n        ap.Point2D(x=100, y=100),\n    ]))\n\n# Draw the diamond shape with the draw_polygon interface.\nsprite.graphics.draw_polygon(\n    points=ap.Array([\n        ap.Point2D(x=175, y=50),\n        ap.Point2D(x=150, y=75),\n        ap.Point2D(x=175, y=100),\n        ap.Point2D(x=200, y=75),\n    ]))\n\nap.save_overall_html(\n    dest_dir_path=\'graphics_draw_polygon_basic_usage/\')\n```':  # noqa
    '',

    '<iframe src="static/graphics_draw_polygon_basic_usage/index.html" width="250" height="150"></iframe>':  # noqa
    '',

    '## Difference between the line_to and draw_polygon interfaces':
    '',

    'If you set the fill color, the `draw_polygon` interface becomes slightly similar to the `line_to` (and `move_to`) interfaces. So, for example, the following codes both draw the triangle.\n\nThe `draw_polygon` interface draws the left rectangle. Similarly, the `move_to` and `line_to` interfaces draw the right one.':  # noqa
    '',

    '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    background_color=\'#333\',\n    stage_width=250,\n    stage_height=150,\n    stage_elem_id=\'stage\')\n\nsprite: ap.Sprite = ap.Sprite()\nsprite.graphics.begin_fill(color=\'#0af\')\n\n# Draw the triangle with the draw_polygon interface.\nsprite.graphics.draw_polygon(\n    points=ap.Array([\n        ap.Point2D(x=75, y=50),\n        ap.Point2D(x=50, y=100),\n        ap.Point2D(x=100, y=100),\n    ]))\n\n# Draw the triangle with the move_to and line_to interfaces.\nsprite.graphics.move_to(x=175, y=50)\nsprite.graphics.line_to(x=150, y=100)\nsprite.graphics.line_to(x=200, y=100)\n\nap.save_overall_html(\n    dest_dir_path=\'graphics_draw_polygon_line_to_difference_1/\')\n```':  # noqa
    '',

    '<iframe src="static/graphics_draw_polygon_line_to_difference_1/index.html" width="250" height="150"></iframe>\n\nBut there is a difference in whether closing the paths is necessary or not. This difference becomes significant when you set the line style setting. The `line_to` interface does not close the paths from end coordinates to start coordinates.':  # noqa
    '',

    '```py\n# runnable\nimport apysc as ap\n\nstage: ap.Stage = ap.Stage(\n    background_color=\'#333\',\n    stage_width=250,\n    stage_height=150,\n    stage_elem_id=\'stage\')\n\nsprite: ap.Sprite = ap.Sprite()\nsprite.graphics.begin_fill(color=\'#0af\')\n\n# Set the line style to see the difference.\nsprite.graphics.line_style(color=\'#fff\', thickness=3)\n\n# Draw the triangle with the draw_polygon interface.\nsprite.graphics.draw_polygon(\n    points=ap.Array([\n        ap.Point2D(x=75, y=50),\n        ap.Point2D(x=50, y=100),\n        ap.Point2D(x=100, y=100),\n    ]))\n\n# Draw the triangle with the move_to and line_to interfaces.\nsprite.graphics.move_to(x=175, y=50)\nsprite.graphics.line_to(x=150, y=100)\nsprite.graphics.line_to(x=200, y=100)\n\nap.save_overall_html(\n    dest_dir_path=\'graphics_draw_polygon_line_to_difference_2/\')\n```':  # noqa
    '',

    '<iframe src="static/graphics_draw_polygon_line_to_difference_2/index.html" width="250" height="150"></iframe>':  # noqa
    '',

    '## Return value':
    '',

    'The `draw_polygon` interface returns the `Polygon` instance. And that has the basic interface as same as the other type graphics instances. The `Polygon` instance also has the `append_line_point` method interface to append points dynamically.\n\nFor instance, the following code appends the point and changes from the triangle to the rectangle.':  # noqa
    '',

    '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    background_color=\'#333\',\n    stage_width=150,\n    stage_height=150,\n    stage_elem_id=\'stage\')\n\nsprite: ap.Sprite = ap.Sprite()\nsprite.graphics.begin_fill(color=\'#0af\')\n\n# Draw the triangle.\npolygon: ap.Polygon = sprite.graphics.draw_polygon(\n    points=ap.Array([\n        ap.Point2D(x=75, y=50),\n        ap.Point2D(x=50, y=75),\n        ap.Point2D(x=75, y=100),\n    ]))\n\n# Append the point and change to the rectangle dynamically.\npolygon.append_line_point(x=100, y=75)\n\nap.save_overall_html(\n    dest_dir_path=\'graphics_draw_polygon_append_line_point/\')\n```':  # noqa
    '',

    '<iframe src="static/graphics_draw_polygon_append_line_point/index.html" width="150" height="150"></iframe>':  # noqa
    '',

    '## draw_polygon API':
    '',

    '<!-- Docstring: apysc._display.graphics.Graphics.draw_polygon -->\n\n<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>\n\n**[Interface signature]** `draw_polygon(self, points:Union[List[apysc._geom.point2d.Point2D], apysc._type.array.Array[apysc._geom.point2d.Point2D]]) -> \'_polyg.Polygon\'`<hr>\n\n**[Interface summary]** Draw a polygon vector graphic. This interface is similar to the Polyline class (created by `move_to` or `line_to`). But unlike that, this interface connects the last point and the start point.<hr>\n\n**[Parameters]**\n\n- `points`: list of Point2D or Array.\n  - Polygon vertex points.\n\n<hr>\n\n**[Returns]**\n\n- `polygon`: Polygon\n  - Created polygon graphics instance.\n\n<hr>\n\n**[Examples]**':  # noqa
    '',

    '```py\n>>> import apysc as ap\n>>> stage: ap.Stage = ap.Stage()\n>>> sprite: ap.Sprite = ap.Sprite()\n>>> sprite.graphics.begin_fill(color=\'#0af\')\n>>> polygon: ap.Polygon = sprite.graphics.draw_polygon(\n...     points=[\n...         ap.Point2D(x=25, y=0),\n...         ap.Point2D(x=0, y=50),\n...         ap.Point2D(x=50, y=50),\n...     ])\n>>> polygon.fill_color\nString(\'#00aaff\')\n```':  # noqa
    '',

}
