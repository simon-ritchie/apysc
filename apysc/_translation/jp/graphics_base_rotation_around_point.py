"""This module is for the translation mapping data of the
following document:

Document file: graphics_base_rotation_around_point.md
Language: jp
"""

from typing import Dict

MAPPING: Dict[str, str] = {

    '# GraphicsBase rotation_around_point interfaces':
    '',

    'This page explains the `GraphicsBase` class (base class of each graphics, such as the `Rectangle`) `get_rotation_around_point` and `set_rotation_around_point` method interfaces.':  # noqa
    '',

    '## What interfaces are these?':
    '',

    'The `get_rotation_around_point` method will return a rotation value around the given coordinates, and the `set_rotation_around_point` method will update a rotation value around the given coordinates.\n\nThese rotation values are relative, and each point has the rotation value. For example, the coordinates of the `(x=50, y=50)` and the other coordinates of the `(x=100, y=100)` have different rotation values.':  # noqa
    '',

    '## Basic usage':
    '',

    'The `get_rotation_around_point` method requires the `x` and `y` arguments and return a rotation value around the given coordinates. The `set_rotation_around_point` requires `x`, `y` and `rotation` arguments. All the arguments and return value are `Int` type.\n\nThe following example creates the two rectangles and rotates each rectangle in the timer handler. The first rectangle rotates around the top-left coordinates (`x=50, y=50`). Also, the second one rotates around the bottom-right coordinates (`x=100, y=100`).':  # noqa
    '',

    '```py\n# runnable\nfrom typing_extensions import TypedDict\n\nimport apysc as ap\n\n\nclass _RectanglesOptions(TypedDict):\n    rectangle_1: ap.Rectangle\n    rectangle_2: ap.Rectangle\n\n\ndef on_timer(e: ap.TimerEvent, options: _RectanglesOptions) -> None:\n    """\n    The handler that the timer calls.\n\n    Parameters\n    ----------\n    e : ap.TimerEvent\n        Event instance.\n    options : dict\n        Optional arguments dictionary.\n    """\n    x: ap.Int = ap.Int(50)\n    y: ap.Int = ap.Int(50)\n    rectangle_1: ap.Rectangle = options[\'rectangle_1\']\n    rotation: ap.Int = rectangle_1.get_rotation_around_point(x=x, y=y)\n    rotation += 1\n    rectangle_1.set_rotation_around_point(rotation=rotation, x=x, y=y)\n\n    rectangle_2: ap.Rectangle = options[\'rectangle_2\']\n    x = ap.Int(100)\n    y = ap.Int(100)\n    rotation = rectangle_2.get_rotation_around_point(x=x, y=y)\n    rotation += 1\n    rectangle_2.set_rotation_around_point(rotation=rotation, x=x, y=y)\n\n\nap.Stage(\n    stage_width=150, stage_height=150, background_color=\'#333\',\n    stage_elem_id=\'stage\')\nsprite: ap.Sprite = ap.Sprite()\nsprite.graphics.begin_fill(color=\'#0af\', alpha=0.5)\n\nrectangle_1: ap.Rectangle = sprite.graphics.draw_rect(\n    x=50, y=50, width=50, height=50)\nrectangle_2: ap.Rectangle = sprite.graphics.draw_rect(\n    x=50, y=50, width=50, height=50)\n\noptions: _RectanglesOptions = {\n    \'rectangle_1\': rectangle_1, \'rectangle_2\': rectangle_2}\ntimer: ap.Timer = ap.Timer(\n    on_timer, delay=ap.FPS.FPS_60, options=options)\ntimer.start()\n\nap.save_overall_html(\n    dest_dir_path=\'graphics_base_rotation_around_point_basic_usage/\')\n```':  # noqa
    '',

    '<iframe src="static/graphics_base_rotation_around_point_basic_usage/index.html" width="150" height="150"></iframe>':  # noqa
    '',

    '## get_rotation_around_point API':
    '',

    '<!-- Docstring: apysc._display.rotation_around_point_interface.RotationAroundPointInterface.get_rotation_around_point -->\n\n<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>\n\n**[Interface signature]** `get_rotation_around_point(self, x:apysc._type.int.Int, y:apysc._type.int.Int) -> apysc._type.int.Int`<hr>\n\n**[Interface summary]** Get a rotation value around the given coordinates.<hr>\n\n**[Parameters]**\n\n- `x`: Int\n  - X-coordinate.\n- `y`: Int\n  - Y-coordinate.\n\n<hr>\n\n**[Returns]**\n\n- `rotation`: Int\n  - Rotation value around the given coordinates.\n\n<hr>\n\n**[Examples]**':  # noqa
    '',

    '```py\n>>> import apysc as ap\n>>> stage: ap.Stage = ap.Stage()\n>>> sprite: ap.Sprite = ap.Sprite()\n>>> sprite.graphics.begin_fill(color=\'#0af\')\n>>> rectangle: ap.Rectangle = sprite.graphics.draw_rect(\n...     x=50, y=50, width=50, height=50)\n>>> x: ap.Int = ap.Int(100)\n>>> y: ap.Int = ap.Int(100)\n>>> rectangle.set_rotation_around_point(\n...     rotation=ap.Int(45), x=x, y=y)\n>>> rectangle.get_rotation_around_point(x=x, y=y)\nInt(45)\n```':  # noqa
    '',

    '':
    '',

    '## set_rotation_around_point API':
    '',

    '<!-- Docstring: apysc._display.rotation_around_point_interface.RotationAroundPointInterface.set_rotation_around_point -->\n\n<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>\n\n**[Interface signature]** `set_rotation_around_point(self, rotation:apysc._type.int.Int, x:apysc._type.int.Int, y:apysc._type.int.Int) -> None`<hr>\n\n**[Interface summary]** Update a rotation value around the given coordinates.<hr>\n\n**[Parameters]**\n\n- `rotation`: Int\n  - Rotation value to set.\n- `x`: Int\n  - X-coordinate.\n- `y`: Int\n  - Y-coordinate.':  # noqa
    '',

}
