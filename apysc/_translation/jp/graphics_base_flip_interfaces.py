"""This module is for the translation mapping data of the
following document:

Document file: graphics_base_flip_interfaces.md
Language: jp
"""

from typing import Dict

MAPPING: Dict[str, str] = {

    '# GraphicsBase flip_x and flip_y interfaces':
    '',

    'This page explains the `GraphicsBase` class (base class of each graphics, such as the `Rectangle`) `flip_x` and `flip_y` property interfaces.':  # noqa
    '',

    '## What interfaces are these?':
    '',

    'The `flip_x` property flips an object in the x-axis direction, and the `flip_y` property flips in the y-axis direction.':  # noqa
    '',

    '## Basic usage':
    '',

    'The `flip_x` and `flip_y` can be set a `Boolean` value. If you set the `True`\\, an object becomes flipped. Conversely, if you set the `False`\\, an object resets flipping.\n\nThe getter interface returns a `Boolean` value of a current flipping value.\n\nThe following example flips the triangle polygon in the x-axis direction and resets per second:':  # noqa
    '',

    '```py\n# runnable\nfrom typing_extensions import TypedDict\n\nimport apysc as ap\n\n\nclass _PolygonOptions(TypedDict):\n    polygon: ap.Polygon\n\n\ndef on_timer(e: ap.TimerEvent, options: _PolygonOptions) -> None:\n    """\n    The handler that the timer calls.\n\n    Parameters\n    ----------\n    e : ap.TimerEvent\n        Event instance.\n    options : dict\n        Optional arguments dictionary.\n    """\n    polygon: ap.Polygon = options[\'polygon\']\n    flip_x: ap.Boolean = polygon.flip_x\n    flip_x = flip_x.not_\n    polygon.flip_x = flip_x\n\n\nap.Stage(\n    stage_width=150, stage_height=150, background_color=\'#333\',\n    stage_elem_id=\'stage\')\nsprite: ap.Sprite = ap.Sprite()\nsprite.graphics.begin_fill(color=\'#0af\')\n\npolygon: ap.Polygon = sprite.graphics.draw_polygon(\n    points=[\n        ap.Point2D(x=50, y=50),\n        ap.Point2D(x=50, y=100),\n        ap.Point2D(x=100, y=75),\n    ])\noptions: _PolygonOptions = {\'polygon\': polygon}\ntimer: ap.Timer = ap.Timer(\n    on_timer, delay=1000, options=options)\ntimer.start()\n\nap.save_overall_html(\n    dest_dir_path=\'graphics_base_flip_x_basic_usage/\')\n```':  # noqa
    '',

    '<iframe src="static/graphics_base_flip_x_basic_usage/index.html" width="150" height="150"></iframe>\n\nThe `flip_y` interface behaves the same as the `flip_x` interface, except the axis direction.':  # noqa
    '',

    '## flip_x property API':
    '',

    '<!-- Docstring: apysc._display.flip_x_interface.FlipXInterface.flip_x -->\n\n<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>\n\n**[Interface summary]** Get a boolean value whether the x-axis is flipping or not.<hr>\n\n**[Returns]**\n\n- `flip_x`: Boolean\n  - A boolean value whether the x-axis is flipping or not.\n\n<hr>\n\n**[Examples]**':  # noqa
    '',

    '```py\n>>> import apysc as ap\n>>> stage: ap.Stage = ap.Stage()\n>>> sprite: ap.Sprite = ap.Sprite()\n>>> sprite.graphics.begin_fill(color=\'#0af\')\n>>> polygon: ap.Polygon = sprite.graphics.draw_polygon(\n...     points=[\n...         ap.Point2D(x=0, y=0),\n...         ap.Point2D(x=0, y=50),\n...         ap.Point2D(x=50, y=25),\n...     ])\n>>> polygon.flip_x = ap.Boolean(True)\n>>> polygon.flip_x\nBoolean(True)\n```':  # noqa
    '',

    '':
    '',

    '## flip_y property API':
    '',

    '<!-- Docstring: apysc._display.flip_y_interface.FlipYInterface.flip_y -->\n\n<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>\n\n**[Interface summary]** Get a boolean value whether the y-axis is flipping or not.<hr>\n\n**[Returns]**\n\n- `flip_y`: Boolean\n  - A boolean value whether the y-axis is flipping or not.\n\n<hr>\n\n**[Examples]**':  # noqa
    '',

    '```py\n>>> import apysc as ap\n>>> stage: ap.Stage = ap.Stage()\n>>> sprite: ap.Sprite = ap.Sprite()\n>>> sprite.graphics.begin_fill(color=\'#0af\')\n>>> polygon: ap.Polygon = sprite.graphics.draw_polygon(\n...     points=[\n...         ap.Point2D(x=0, y=0),\n...         ap.Point2D(x=50, y=0),\n...         ap.Point2D(x=25, y=50),\n...     ])\n>>> polygon.flip_y = ap.Boolean(True)\n>>> polygon.flip_y\nBoolean(True)\n```':  # noqa
    '',

}
