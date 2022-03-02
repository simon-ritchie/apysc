"""This module is for the translation mapping data of the
following document:

Document file: graphics_line_alpha.md
Language: jp
"""

from typing import Dict

MAPPING: Dict[str, str] = {

    '# Graphics line_alpha interface':
    '',

    'This page explains the `Graphics` class `line_alpha` property interface.':  # noqa
    '',

    '## What interface is this?':
    '',

    'The `line_alpha` property interface updates or get the instance\'s line alpha (opacity).':  # noqa
    '',

    '## Basic usage':
    '',

    'The getter or setter interface value becomes (or requires) the `Number` value (0.0 to 1.0).\n\nThe following example sets the 0.5 line alpha to the second rectangle and 0.25 to the third rectangle:':  # noqa
    '',

    '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    stage_width=350, stage_height=150, background_color=\'#333\',\n    stage_elem_id=\'stage\')\nsprite: ap.Sprite = ap.Sprite()\nsprite.graphics.line_style(color=\'#0af\', thickness=5)\n\nrectangle_1: ap.Rectangle = sprite.graphics.draw_rect(\n    x=50, y=50, width=50, height=50)\n\nrectangle_2: ap.Rectangle = sprite.graphics.draw_rect(\n    x=150, y=50, width=50, height=50)\nrectangle_2.line_alpha = ap.Number(0.5)\n\nrectangle_3: ap.Rectangle = sprite.graphics.draw_rect(\n    x=250, y=50, width=50, height=50)\nrectangle_3.line_alpha = ap.Number(0.25)\n\nap.save_overall_html(\n    dest_dir_path=\'./graphics_line_alpha_basic_usage/\')\n```':  # noqa
    '',

    '<iframe src="static/graphics_line_alpha_basic_usage/index.html" width="350" height="150"></iframe>':  # noqa
    '',

    '## line_alpha property API':
    '',

    '<!-- Docstring: apysc._display.line_alpha_interface.LineAlphaInterface.line_alpha -->\n\n<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>\n\n**[Interface summary]** Get this instance\'s line alpha (opacity).<hr>\n\n**[Returns]**\n\n- `line_alpha`: Number\n  - Current line alpha (opacity. 0.0 to 1.0).\n\n<hr>\n\n**[Examples]**':  # noqa
    '',

    '```py\n>>> import apysc as ap\n>>> stage: ap.Stage = ap.Stage()\n>>> sprite: ap.Sprite = ap.Sprite()\n>>> sprite.graphics.line_style(color=\'#fff\', thickness=5, alpha=1.0)\n>>> rectangle: ap.Rectangle = sprite.graphics.draw_rect(\n...     x=50, y=50, width=50, height=50)\n>>> rectangle.line_alpha = ap.Number(0.5)\n>>> rectangle.line_alpha\nNumber(0.5)\n```':  # noqa
    '',

}
