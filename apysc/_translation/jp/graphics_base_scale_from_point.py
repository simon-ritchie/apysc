"""This module is for the translation mapping data of the
following document:

Document file: graphics_base_scale_from_point.md
Language: jp
"""

from typing import Dict

MAPPING: Dict[str, str] = {

    '# GraphicsBase get_scale_from_point and set_scale_from_point interfaces':  # noqa
    '',

    'This page explains the `GraphicsBase` class (base class of each graphics, such as the `Rectangle`) `get_scale_x_from_point`, `get_scale_y_from_point`, `set_scale_x_from_point`, and `set_scale_y_from_point` method interfaces.':  # noqa
    '',

    '## What interfaces are these?':
    '',

    'The `set_scale_x_from_point` method changes the object\'s horizontal scale from a given x-coordinate. Similarly, the `set_scale_y_from_point` method changes the object\'s vertical scale from a given y-coordinate.\n\nThe `scale_x_from_center` and `scale_y_from_center` interfaces are property, but the `set_scale_x_from_point` and `set_scale_y_from_point` interfaces are methods since these interfaces require a coodinate argument.\n\nSimilarly, the `get_scale_x_from_point` and `get_scale_y_from_point` methods will return the current scale from a given point. These interfaces also require a coordinate argument.\n\nReturn value is set for each coordinate. For example, if you set the scale-x value at the 50px x-coordinate, 100px x-coordinate scale will not be affected.':  # noqa
    '',

    '## Basic usage':
    '',

    'The `get_scale_x_from_point` method requires the `x` argument (`Int` value), and the `set_scale_x_from_point` requires the `scale_x` (`Number` value) and `x` arguments.\n\nThe following example creates three rectangles and increments (or decrements) for each rectangle scale-x value. The top rectangle scales from the left-x position. The middle one scales from the center-x. And the bottom one scales from the right-x.':  # noqa
    '',

    '```py\n# runnable\nfrom typing_extensions import TypedDict\n\nimport apysc as ap\n\n\nclass _Options(TypedDict):\n    rectangle: ap.Rectangle\n    x: ap.Int\n    direction: ap.Int\n\n\ndef on_timer(e: ap.TimerEvent, options: _Options) -> None:\n    """\n    The handler that the timer calls.\n\n    Parameters\n    ----------\n    e : ap.TimerEvent\n        Event instance.\n    options : dict\n        Optional arguments dictionary.\n    """\n    rectangle: ap.Rectangle = options[\'rectangle\']\n    x: ap.Int = options[\'x\']\n    direction: ap.Int = options[\'direction\']\n    current_scale_x: ap.Number = rectangle.get_scale_x_from_point(x=x)\n    current_scale_x += direction * 0.03\n    rectangle.set_scale_x_from_point(scale_x=current_scale_x, x=x)\n    with ap.If(current_scale_x >= 2.0):\n        direction *= -1\n    with ap.If(current_scale_x <= 0.0):\n        direction *= -1\n\n\nap.Stage(\n    stage_width=150, stage_height=350, background_color=\'#333\',\n    stage_elem_id=\'stage\')\nsprite: ap.Sprite = ap.Sprite()\nsprite.graphics.begin_fill(color=\'#0af\')\n\ntop_rect: ap.Rectangle = sprite.graphics.draw_rect(\n    x=50, y=50, width=50, height=50)\nmiddle_rect: ap.Rectangle = sprite.graphics.draw_rect(\n    x=50, y=150, width=50, height=50)\nbottom_rect: ap.Rectangle = sprite.graphics.draw_rect(\n    x=50, y=250, width=50, height=50)\n\ntop_rect_direction: ap.Int = ap.Int(1)\noptions: _Options = {\n    \'rectangle\': top_rect, \'x\': ap.Int(50),\n    \'direction\': top_rect_direction}\ntop_rect_timer: ap.Timer = ap.Timer(\n    on_timer, delay=ap.FPS.FPS_60,\n    options=options)\ntop_rect_timer.start()\n\nmiddle_rect_direction: ap.Int = ap.Int(1)\noptions = {\n    \'rectangle\': middle_rect, \'x\': ap.Int(75),\n    \'direction\': middle_rect_direction}\nmiddle_rect_timer: ap.Timer = ap.Timer(\n    on_timer, delay=ap.FPS.FPS_60,\n    options=options)\nmiddle_rect_timer.start()\n\nbottom_rect_direction: ap.Int = ap.Int(1)\noptions = {\n    \'rectangle\': bottom_rect, \'x\': ap.Int(100),\n    \'direction\': bottom_rect_direction}\nbottom_rect_timer: ap.Timer = ap.Timer(\n    on_timer, delay=ap.FPS.FPS_60,\n    options=options)\nbottom_rect_timer.start()\n\nap.save_overall_html(\n    dest_dir_path=\'graphics_base_scale_from_point_basic_usage_x/\')\n```':  # noqa
    '',

    '<iframe src="static/graphics_base_scale_from_point_basic_usage_x/index.html" width="150" height="350"></iframe>\n\nThe `get_scale_y_from_point` and `set_scale_y_from_point` methods have the similar arguments, `scale_y` and `y`. These interfaces work the same way as the x-axis interfaces, except that the axis directions are different.':  # noqa
    '',

    '```py\n# runnable\nfrom typing_extensions import TypedDict\n\nimport apysc as ap\n\n\nclass _Options(TypedDict):\n    rectangle: ap.Rectangle\n    y: ap.Int\n    direction: ap.Int\n\n\ndef on_timer(e: ap.TimerEvent, options: _Options) -> None:\n    """\n    The handler that the timer calls.\n\n    Parameters\n    ----------\n    e : ap.TimerEvent\n        Event instance.\n    options : dict\n        Optional arguments dictionary.\n    """\n    rectangle: ap.Rectangle = options[\'rectangle\']\n    y: ap.Int = options[\'y\']\n    direction: ap.Int = options[\'direction\']\n    current_scale_y: ap.Number = rectangle.get_scale_y_from_point(y=y)\n    current_scale_y += direction * 0.03\n    rectangle.set_scale_y_from_point(scale_y=current_scale_y, y=y)\n    with ap.If(current_scale_y >= 2.0):\n        direction *= -1\n    with ap.If(current_scale_y <= 0.0):\n        direction *= -1\n\n\nap.Stage(\n    stage_width=150, stage_height=150, background_color=\'#333\',\n    stage_elem_id=\'stage\')\nsprite: ap.Sprite = ap.Sprite()\nsprite.graphics.begin_fill(color=\'#0af\')\n\nrectangle: ap.Rectangle = sprite.graphics.draw_rect(\n    x=50, y=50, width=50, height=50)\ndirection: ap.Int = ap.Int(1)\noptions: _Options = {\n    \'rectangle\': rectangle, \'y\': ap.Int(50), \'direction\': direction}\ntimer: ap.Timer = ap.Timer(\n    on_timer, delay=ap.FPS.FPS_60,\n    options=options)\ntimer.start()\n\nap.save_overall_html(\n    dest_dir_path=\'graphics_base_scale_from_point_basic_usage_y/\')\n```':  # noqa
    '',

    '<iframe src="static/graphics_base_scale_from_point_basic_usage_y/index.html" width="150" height="150"></iframe>':  # noqa
    '',

    '## get_scale_x_from_point API':
    '',

    '<!-- Docstring: apysc._display.scale_x_from_point_interface.ScaleXFromPointInterface.get_scale_x_from_point -->\n\n<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>\n\n**[Interface signature]** `get_scale_x_from_point(self, x:apysc._type.int.Int) -> apysc._type.number.Number`<hr>\n\n**[Interface summary]** Get a scale-x value from the given x-coordinate.<hr>\n\n**[Parameters]**\n\n- `x`: Int\n  - X-coordinate.\n\n<hr>\n\n**[Returns]**\n\n- `scale_x`: Number\n  - Scale-x value from the given x-coordinate.\n\n<hr>\n\n**[Examples]**':  # noqa
    '',

    '```py\n>>> import apysc as ap\n>>> stage: ap.Stage = ap.Stage()\n>>> sprite: ap.Sprite = ap.Sprite()\n>>> sprite.graphics.begin_fill(color=\'#0af\')\n>>> rectangle: ap.Rectangle = sprite.graphics.draw_rect(\n...     x=50, y=50, width=50, height=50)\n>>> x: ap.Int = ap.Int(100)\n>>> rectangle.set_scale_x_from_point(scale_x=ap.Number(1.5), x=x)\n>>> rectangle.get_scale_x_from_point(x=x)\nNumber(1.5)\n```':  # noqa
    '',

    '':
    '',

    '## set_scale_x_from_point API':
    '',

    '<!-- Docstring: apysc._display.scale_x_from_point_interface.ScaleXFromPointInterface.set_scale_x_from_point -->\n\n<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>\n\n**[Interface signature]** `set_scale_x_from_point(self, scale_x:apysc._type.number.Number, x:apysc._type.int.Int) -> None`<hr>\n\n**[Interface summary]** Update a scale-x value from the given x-coordinate.<hr>\n\n**[Parameters]**\n\n- `scale_x`: Number\n  - Scale-x value to set.\n- `x`: Int\n  - X-coordinate.\n\n<hr>\n\n**[Examples]**':  # noqa
    '',

    '```py\n>>> import apysc as ap\n>>> stage: ap.Stage = ap.Stage()\n>>> sprite: ap.Sprite = ap.Sprite()\n>>> sprite.graphics.begin_fill(color=\'#0af\')\n>>> rectangle: ap.Rectangle = sprite.graphics.draw_rect(\n...     x=50, y=50, width=50, height=50)\n>>> x: ap.Int = ap.Int(100)\n>>> rectangle.set_scale_x_from_point(scale_x=ap.Number(1.5), x=x)\n>>> rectangle.get_scale_x_from_point(x=x)\nNumber(1.5)\n```':  # noqa
    '',

    '':
    '',

    '## get_scale_y_from_point API':
    '',

    '<!-- Docstring: apysc._display.scale_y_from_point_interface.ScaleYFromPointInterface.get_scale_y_from_point -->\n\n<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>\n\n**[Interface signature]** `get_scale_y_from_point(self, y:apysc._type.int.Int) -> apysc._type.number.Number`<hr>\n\n**[Interface summary]** Get a scale-y value from the given y-coordinate.<hr>\n\n**[Parameters]**\n\n- `y`: Int\n  - Y-coordinate.\n\n<hr>\n\n**[Returns]**\n\n- `scale_y`: ap.Number\n  - Scale-y value from the given y-coordinate.\n\n<hr>\n\n**[Examples]**':  # noqa
    '',

    '```py\n>>> import apysc as ap\n>>> stage: ap.Stage = ap.Stage()\n>>> sprite: ap.Sprite = ap.Sprite()\n>>> sprite.graphics.begin_fill(color=\'#0af\')\n>>> rectangle: ap.Rectangle = sprite.graphics.draw_rect(\n...     x=50, y=50, width=50, height=50)\n>>> y: ap.Int = ap.Int(100)\n>>> rectangle.set_scale_y_from_point(scale_y=ap.Number(1.5), y=y)\n>>> rectangle.get_scale_y_from_point(y=y)\nNumber(1.5)\n```':  # noqa
    '',

    '':
    '',

    '## set_scale_y_from_point API':
    '',

    '<!-- Docstring: apysc._display.scale_y_from_point_interface.ScaleYFromPointInterface.set_scale_y_from_point -->\n\n<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>\n\n**[Interface signature]** `set_scale_y_from_point(self, scale_y:apysc._type.number.Number, y:apysc._type.int.Int) -> None`<hr>\n\n**[Interface summary]** Update a scale-y value from the given y-coordinate.<hr>\n\n**[Parameters]**\n\n- `scale_y`: Number\n  - Scale-y value to set.\n- `y`: Int\n  - Y-coordinate.\n\n<hr>\n\n**[Examples]**':  # noqa
    '',

    '```py\n>>> import apysc as ap\n>>> stage: ap.Stage = ap.Stage()\n>>> sprite: ap.Sprite = ap.Sprite()\n>>> sprite.graphics.begin_fill(color=\'#0af\')\n>>> rectangle: ap.Rectangle = sprite.graphics.draw_rect(\n...     x=50, y=50, width=50, height=50)\n>>> y: ap.Int = ap.Int(100)\n>>> rectangle.set_scale_y_from_point(scale_y=ap.Number(1.5), y=y)\n>>> rectangle.get_scale_y_from_point(y=y)\nNumber(1.5)\n```':  # noqa
    '',

}
