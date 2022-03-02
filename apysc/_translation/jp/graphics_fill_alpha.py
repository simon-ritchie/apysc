"""This module is for the translation mapping data of the
following document:

Document file: graphics_fill_alpha.md
Language: jp
"""

from typing import Dict

MAPPING: Dict[str, str] = {

    '# Graphics fill_alpha interface':
    '',

    'This page explains the `Graphics` class `fill_alpha` property interface.':  # noqa
    '',

    '## What interface is this?':
    '',

    'The `fill_alpha` property interface updates or get the instance\'s fill alpha (opacity).':  # noqa
    '',

    '## Basic usage':
    '',

    'The getter or setter interface value becomes (or require) the `Number` value (0.0 to 1.0).\n\nThe following example sets the 0.5 fill alpha to the second rectangle and 0.25 to the third rectangle:':  # noqa
    '',

    '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    stage_width=350, stage_height=150, background_color=\'#333\',\n    stage_elem_id=\'stage\')\nsprite: ap.Sprite = ap.Sprite()\nsprite.graphics.begin_fill(color=\'#0af\')\n\nrectangle_1: ap.Rectangle = sprite.graphics.draw_rect(\n    x=50, y=50, width=50, height=50)\n\nrectangle_2: ap.Rectangle = sprite.graphics.draw_rect(\n    x=150, y=50, width=50, height=50)\nrectangle_2.fill_alpha = ap.Number(0.5)\n\nrectangle_3: ap.Rectangle = sprite.graphics.draw_rect(\n    x=250, y=50, width=50, height=50)\nrectangle_3.fill_alpha = ap.Number(0.25)\n\nap.save_overall_html(\n    dest_dir_path=\'./graphics_fill_alpha_basic_usage/\')\n```':  # noqa
    '',

    '<iframe src="static/graphics_fill_alpha_basic_usage/index.html" width="350" height="150"></iframe>':  # noqa
    '',

    '## fill_alpha property API':
    '',

    '<!-- Docstring: apysc._display.fill_alpha_interface.FillAlphaInterface.fill_alpha -->\n\n<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>\n\n**[Interface summary]** Get this instance\'s fill opacity.<hr>\n\n**[Returns]**\n\n- `fill_alpha`: Number\n  - Current fill opacity (0.0 to 1.0).\n\n<hr>\n\n**[Examples]**':  # noqa
    '',

    '```py\n>>> import apysc as ap\n>>> stage: ap.Stage = ap.Stage()\n>>> sprite: ap.Sprite = ap.Sprite()\n>>> sprite.graphics.begin_fill(color=\'#0af\')\n>>> rectangle: ap.Rectangle = sprite.graphics.draw_rect(\n...     x=50, y=50, width=50, height=50)\n>>> rectangle.fill_alpha = ap.Number(0.5)\n>>> rectangle.fill_alpha\nNumber(0.5)\n```':  # noqa
    '',

}
