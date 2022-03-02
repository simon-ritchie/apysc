"""This module is for the translation mapping data of the
following document:

Document file: graphics_base_skew.md
Language: jp
"""

from typing import Dict

MAPPING: Dict[str, str] = {

    '# GraphicsBase skew_x and skew_y interfaces':
    '',

    'This page explains the `GraphicsBase` class (base class of each graphic, such as the `Rectangle`) `skew_x` and `skew_y` property interfaces.\n\nEach interface value type is the `Int` value.':  # noqa
    '',

    '## What interfaces are these?':
    '',

    'The `skew_x` property skews an object\'s x-axis. Conversely, the `skew_y` property skew a y-axis. These interfaces have getter and setter interfaces.\n\nThe following example shows you the default rectangle (left) and the skewed 50px in the x-direction rectangle (right).':  # noqa
    '',

    '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    stage_width=250, stage_height=150, background_color=\'#333\',\n    stage_elem_id=\'stage\')\nsprite: ap.Sprite = ap.Sprite()\nsprite.graphics.begin_fill(color=\'#0af\')\n\nleft_rectangle: ap.Rectangle = sprite.graphics.draw_rect(\n    x=50, y=50, width=50, height=50)\nright_rectangle: ap.Rectangle = sprite.graphics.draw_rect(\n    x=150, y=50, width=50, height=50)\nright_rectangle.skew_x = ap.Int(50)\n\nap.save_overall_html(\n    dest_dir_path=\'graphics_base_skew_x_basic_usage/\')\n```':  # noqa
    '',

    '<iframe src="static/graphics_base_skew_x_basic_usage/index.html" width="250" height="150"></iframe>\n\nThe following example skews the rectangle in the y-direction incrementally.':  # noqa
    '',

    '```py\n# runnable\nfrom typing_extensions import TypedDict\n\nimport apysc as ap\n\n\nclass _RectOptions(TypedDict):\n    rectangle: ap.Rectangle\n\n\ndef on_timer(e: ap.TimerEvent, options: _RectOptions) -> None:\n    """\n    The handler that the timer calls.\n\n    Parameters\n    ----------\n    e : TimerEvent\n        Event instance.\n    options : dict\n        Optional arguments dictionary.\n    """\n    rectangle: ap.Rectangle = options[\'rectangle\']\n    rectangle.skew_y += 1\n\n\nap.Stage(\n    stage_width=150, stage_height=150, background_color=\'#333\',\n    stage_elem_id=\'stage\')\nsprite: ap.Sprite = ap.Sprite()\nsprite.graphics.begin_fill(color=\'#0af\')\n\nrectangle: ap.Rectangle = sprite.graphics.draw_rect(\n    x=50, y=50, width=50, height=50)\noptions: _RectOptions = {\'rectangle\': rectangle}\ntimer: ap.Timer = ap.Timer(\n    handler=on_timer, delay=ap.FPS.FPS_60, options=options)\ntimer.start()\n\nap.save_overall_html(\n    dest_dir_path=\'graphics_base_skew_y_incremental_basic_usage/\')\n```':  # noqa
    '',

    '<iframe src="static/graphics_base_skew_y_incremental_basic_usage/index.html" width="150" height="150"></iframe>':  # noqa
    '',

    '## skew_x property API':
    '',

    '<!-- Docstring: apysc._display.skew_x_interface.SkewXInterface.skew_x -->\n\n<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>\n\n**[Interface summary]** Get a current skew x value of the instance.<hr>\n\n**[Returns]**\n\n- `skew_x`: Int\n  - Current skew x value of this instance.\n\n<hr>\n\n**[Examples]**':  # noqa
    '',

    '```py\n>>> import apysc as ap\n>>> stage: ap.Stage = ap.Stage()\n>>> sprite: ap.Sprite = ap.Sprite()\n>>> sprite.graphics.begin_fill(color=\'#0af\')\n>>> rectangle: ap.Rectangle = sprite.graphics.draw_rect(\n...     x=50, y=50, width=50, height=50)\n>>> rectangle.skew_x = ap.Int(50)\n>>> rectangle.skew_x\nInt(50)\n```':  # noqa
    '',

    '':
    '',

    '## skew_y property API':
    '',

    '<!-- Docstring: apysc._display.skew_y_interface.SkewYInterface.skew_y -->\n\n<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>\n\n**[Interface summary]** Get a current skew y value of the instance.<hr>\n\n**[Returns]**\n\n- `skew_y`: Int\n  - Current skew y value of the instance.\n\n<hr>\n\n**[Examples]**':  # noqa
    '',

    '```py\n>>> import apysc as ap\n>>> stage: ap.Stage = ap.Stage()\n>>> sprite: ap.Sprite = ap.Sprite()\n>>> sprite.graphics.begin_fill(color=\'#0af\')\n>>> rectangle: ap.Rectangle = sprite.graphics.draw_rect(\n...     x=50, y=50, width=50, height=50)\n>>> rectangle.skew_y = ap.Int(50)\n>>> rectangle.skew_y\nInt(50)\n```':  # noqa
    '',

}
