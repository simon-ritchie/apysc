"""This module is for the translation mapping data of the
following document:

Document file: point2d.md
Language: jp
"""

from typing import Dict

MAPPING: Dict[str, str] = {

    '# Point2D':
    '',

    'This page explains the `Point2D` class.':
    '',

    '## What is the Point2D class?':
    '',

    'The `Point2D` class is the 2D coordinates class interface. This interface handles the x-coordinate and y-coordinate. This interface is used, for example, the `Polygon` class drawing to specify each vertex point.':  # noqa
    '',

    '## Basic usage':
    '',

    'The `Point2D` class constructor requires the `x` and `y` arguments. Both parameters type is the Python built-in `int` or `Int`\\.':  # noqa
    '',

    '```py\n# runnable\nimport apysc as ap\n\npoint_1: ap.Point2D = ap.Point2D(x=10, y=20)\n\nx: ap.Int = ap.Int(10)\ny: ap.Int = ap.Int(20)\npoint_2: ap.Point2D = ap.Point2D(x=x, y=y)\n```':  # noqa
    '',

    '':
    '',

    '## X and y getter interfaces':
    '',

    'The `Point2D` class `x` and `y` property interfaces returns the `Int` type value, as follows:':  # noqa
    '',

    '```py\n# runnable\nimport apysc as ap\n\npoint: ap.Point2D = ap.Point2D(x=10, y=20)\nassert point.x == 10\nassert point.y == 20\n```':  # noqa
    '',

    '':
    '',

    '## X and y setter interfaces':
    '',

    'The `x` and `y` property can be updated with an `Int` type value, as follows:':  # noqa
    '',

    '```py\n# runnable\nimport apysc as ap\n\npoint: ap.Point2D = ap.Point2D(x=10, y=20)\npoint.x = ap.Int(30)\nassert point.x == 30\n```':  # noqa
    '',

    '':
    '',

    '## Usage example of the draw_polygon interface':
    '',

    'The `draw_polygon` interface requires the `Point2D` list argument so that this section shows the example of the `Point2D` class with that drawing interface.\n\nThe following draws the triangle vector graphics by specifying the three points:':  # noqa
    '',

    '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    stage_width=150, stage_height=150, background_color=\'#333\',\n    stage_elem_id=\'stage\')\nsprite: ap.Sprite = ap.Sprite()\nsprite.graphics.begin_fill(color=\'#0af\')\n\nsprite.graphics.draw_polygon(\n    points=[\n        ap.Point2D(x=75, y=50),\n        ap.Point2D(x=50, y=100),\n        ap.Point2D(x=100, y=100),\n    ])\n\nap.save_overall_html(\n    dest_dir_path=\'point2d_basic_usage/\')\n```':  # noqa
    '',

    '<iframe src="static/point2d_basic_usage/index.html" width="150" height="150"></iframe>':  # noqa
    '',

    '## Point2D class constructor API':
    '',

    '<!-- Docstring: apysc._geom.point2d.Point2D.__init__ -->\n\n<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>\n\n**[Interface signature]** `__init__(self, x:Union[int, apysc._type.int.Int], y:Union[int, apysc._type.int.Int]) -> None`<hr>\n\n**[Interface summary]** 2-dimensional geometry point.<hr>\n\n**[Parameters]**\n\n- `x`: int or Int\n  - X-coordinate.\n- `y`: int or Int\n  - Y-coordinate.\n\n<hr>\n\n**[Examples]**':  # noqa
    '',

    '```py\n>>> import apysc as ap\n>>> stage: ap.Stage = ap.Stage()\n>>> sprite: ap.Sprite = ap.Sprite()\n>>> sprite.graphics.begin_fill(color=\'#0af\')\n>>> polygon: ap.Polygon = sprite.graphics.draw_polygon(\n...     points=[\n...         ap.Point2D(x=0, y=0),\n...         ap.Point2D(x=0, y=50),\n...         ap.Point2D(x=50, y=25),\n...     ])\n```':  # noqa
    '',

    '':
    '',

    '## x property API':
    '',

    '<!-- Docstring: apysc._geom.point2d.Point2D.x -->\n\n<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>\n\n**[Interface summary]** X-coordinate property.<hr>\n\n**[Returns]**\n\n- `x`: Int\n  - X-coordinate.\n\n<hr>\n\n**[Examples]**':  # noqa
    '',

    '```py\n>>> import apysc as ap\n>>> point: ap.Point2D = ap.Point2D(x=50, y=100)\n>>> point.x = ap.Int(150)\n>>> point.x\nInt(150)\n```':  # noqa
    '',

    '':
    '',

    '## y property API':
    '',

    '<!-- Docstring: apysc._geom.point2d.Point2D.y -->\n\n<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>\n\n**[Interface summary]** Y-coordinate property.<hr>\n\n**[Returns]**\n\n- `y`: Int\n  - Y-coordinate.\n\n<hr>\n\n**[Examples]**':  # noqa
    '',

    '```py\n>>> import apysc as ap\n>>> point: ap.Point2D = ap.Point2D(x=50, y=100)\n>>> point.y = ap.Int(150)\n>>> point.y\nInt(150)\n```':  # noqa
    '',

}
