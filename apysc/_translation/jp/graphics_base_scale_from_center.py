"""This module is for the translation mapping data of the
following document:

Document file: graphics_base_scale_from_center.md
Language: jp
"""

from typing import Dict

MAPPING: Dict[str, str] = {

    '# GraphicsBase scale_x_from_center and scale_y_from_center interfaces':
    '',

    'This page explains the `GraphicsBase` class (base class of each graphics, such as the `Rectangle`) `scale_x_from_center` and `scale_y_from_center` property interfaces.':  # noqa
    '',

    '## What interfaces are these?':
    '',

    'The `scale_x_from_center` property changes the object\'s horizontal scale, and the `scale_y_from_center` property changes the object\'s vertical scale. These scaling interfaces change the scale from the center coordinates of each object.':  # noqa
    '',

    '## Basic usage':
    '',

    'Each property getter interface returns a `Number` value. The setter interfaces also require a `Number` to update scales (If 0.0 is specified, the object becomes invisible. 1.0 becomes the default scale, and 2.0 becomes the twice-scale value).\n\nThe following example shows the default scale rectangle (left), horizontally half-scaled rectangle (center), vertically half-scaled rectangle (right).':  # noqa
    '',

    '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    stage_width=350, stage_height=150, background_color=\'#333\',\n    stage_elem_id=\'stage\')\nsprite: ap.Sprite = ap.Sprite()\nsprite.graphics.begin_fill(color=\'#0af\')\n\nleft_rectangle: ap.Rectangle = sprite.graphics.draw_rect(\n    x=50, y=50, width=50, height=50)\ncenter_rectangle: ap.Rectangle = sprite.graphics.draw_rect(\n    x=150, y=50, width=50, height=50)\ncenter_rectangle.scale_x_from_center = ap.Number(0.5)\nright_rectangle: ap.Rectangle = sprite.graphics.draw_rect(\n    x=250, y=50, width=50, height=50)\nright_rectangle.scale_y_from_center = ap.Number(0.5)\n\nap.save_overall_html(\n    dest_dir_path=\'graphics_base_scale_from_center_basic_usage_1/\')\n```':  # noqa
    '',

    '<iframe src="static/graphics_base_scale_from_center_basic_usage_1/index.html" width="350" height="150"></iframe>\n\nThese interfaces apply the scaling from the center coordinates, as follows:':  # noqa
    '',

    '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    stage_width=150, stage_height=150, background_color=\'#333\',\n    stage_elem_id=\'stage\')\nsprite: ap.Sprite = ap.Sprite()\nsprite.graphics.begin_fill(color=\'#0af\', alpha=0.3)\n\nrectangle_1: ap.Rectangle = sprite.graphics.draw_rect(\n    x=50, y=50, width=50, height=50)\n\nrectangle_2: ap.Rectangle = sprite.graphics.draw_rect(\n    x=50, y=50, width=50, height=50)\nrectangle_2.scale_x_from_center = ap.Number(0.5)\nrectangle_2.scale_y_from_center = ap.Number(0.5)\n\nrectangle_3: ap.Rectangle = sprite.graphics.draw_rect(\n    x=50, y=50, width=50, height=50)\nrectangle_3.scale_x_from_center = ap.Number(0.25)\nrectangle_3.scale_y_from_center = ap.Number(0.25)\n\nap.save_overall_html(\n    dest_dir_path=\'graphics_base_scale_from_center_basic_usage_2/\')\n```':  # noqa
    '',

    '<iframe src="static/graphics_base_scale_from_center_basic_usage_2/index.html" width="150" height="150"></iframe>\n\nThe `+=` and `-=` operators are also supported:':  # noqa
    '',

    '```py\n# runnable\nfrom typing_extensions import TypedDict\n\nimport apysc as ap\n\n\nclass _RectanglesOptions(TypedDict):\n    rectangle_1: ap.Rectangle\n    rectangle_2: ap.Rectangle\n    direction: ap.Int\n\n\ndef on_timer(e: ap.TimerEvent, options: _RectanglesOptions) -> None:\n    """\n    The handler that the timer calls.\n\n    Parameters\n    ----------\n    e : ap.TimerEvent\n        Event instance.\n    options : dict\n        Optional arguments dictionary.\n    """\n    rectangle_1: ap.Rectangle = options[\'rectangle_1\']\n    rectangle_2: ap.Rectangle = options[\'rectangle_2\']\n    direction: ap.Int = options[\'direction\']\n\n    current_scale: ap.Number = rectangle_1.scale_x_from_center\n    condition_1: ap.Boolean = current_scale >= 2.0\n    condition_2: ap.Boolean = current_scale <= 0.05\n    with ap.If(condition_1):\n        direction.value = -1\n    with ap.Elif(condition_2):\n        direction.value = 1\n\n    rectangle_1.scale_x_from_center += direction * 0.03\n    rectangle_2.scale_y_from_center += direction * 0.03\n\n\nap.Stage(\n    stage_width=150, stage_height=150, background_color=\'#333\',\n    stage_elem_id=\'stage\')\nsprite: ap.Sprite = ap.Sprite()\n\nsprite.graphics.begin_fill(color=\'#0af\', alpha=0.5)\nrectangle_1: ap.Rectangle = sprite.graphics.draw_rect(\n    x=50, y=50, width=50, height=50)\n\nsprite.graphics.begin_fill(color=\'#f0a\', alpha=0.5)\nrectangle_2: ap.Rectangle = sprite.graphics.draw_rect(\n    x=50, y=50, width=50, height=50)\n\n\ndirection: ap.Int = ap.Int(1.0)\noptions: _RectanglesOptions = {\n    \'rectangle_1\': rectangle_1, \'rectangle_2\': rectangle_2,\n    \'direction\': direction}\ntimer: ap.Timer = ap.Timer(\n    on_timer, delay=ap.FPS.FPS_60,\n    options=options)\ntimer.start()\n\nap.save_overall_html(\n    dest_dir_path=\'graphics_base_scale_from_center_basic_usage_3/\')\n```':  # noqa
    '',

    '<iframe src="static/graphics_base_scale_from_center_basic_usage_3/index.html" width="150" height="150"></iframe>':  # noqa
    '',

    '## scale_x_from_center property API':
    '',

    '<!-- Docstring: apysc._display.scale_x_from_center_interface.ScaleXFromCenterInterface.scale_x_from_center -->\n\n<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>\n\n**[Interface summary]** Get a scale-x value from the center of this instance.<hr>\n\n**[Returns]**\n\n- `scale_x_from_center`: ap.Number\n  - Scale-x value from the center of this instance.\n\n<hr>\n\n**[Examples]**':  # noqa
    '',

    '```py\n>>> import apysc as ap\n>>> stage: ap.Stage = ap.Stage()\n>>> sprite: ap.Sprite = ap.Sprite()\n>>> sprite.graphics.begin_fill(color=\'#0af\')\n>>> rectangle: ap.Rectangle = sprite.graphics.draw_rect(\n...     x=50, y=50, width=50, height=50)\n>>> rectangle.scale_x_from_center = ap.Number(1.5)\n>>> rectangle.scale_x_from_center\nNumber(1.5)\n```':  # noqa
    '',

    '':
    '',

    '## scale_y_from_center property API':
    '',

    '<!-- Docstring: apysc._display.scale_y_from_center_interface.ScaleYFromCenterInterface.scale_y_from_center -->\n\n<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>\n\n**[Interface summary]** Get a scale-y value from the center of this instance.<hr>\n\n**[Returns]**\n\n- `scale_y_from_center`: ap.Number\n  - Scale-y value from the center of this instance.\n\n<hr>\n\n**[Examples]**':  # noqa
    '',

    '```py\n>>> import apysc as ap\n>>> stage: ap.Stage = ap.Stage()\n>>> sprite: ap.Sprite = ap.Sprite()\n>>> sprite.graphics.begin_fill(color=\'#0af\')\n>>> rectangle: ap.Rectangle = sprite.graphics.draw_rect(\n...     x=50, y=50, width=50, height=50)\n>>> rectangle.scale_y_from_center = ap.Number(1.5)\n>>> rectangle.scale_y_from_center\nNumber(1.5)\n```':  # noqa
    '',

}
