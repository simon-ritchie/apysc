"""This module is for the translation mapping data of the
following document:

Document file: graphics_line_thickness.md
Language: jp
"""

from typing import Dict

MAPPING: Dict[str, str] = {

    '# Graphics line_thickness interface':
    '',

    'This page explains the `Graphics` class `line_thickness` property interface.':  # noqa
    '',

    '## What interface is this?':
    '',

    'The `line_thickness` property interface updates or get the instance\'s line thickness (line width).':  # noqa
    '',

    '## Basic usage':
    '',

    'The getter or setter interface value becomes (or requires) the `Int` value.\n\nThe following example sets the 5-pixel line thickness to the first rectangle and the 10-pixel line thickness to the second one:':  # noqa
    '',

    '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    stage_width=250, stage_height=150, background_color=\'#333\',\n    stage_elem_id=\'stage\')\nsprite: ap.Sprite = ap.Sprite()\nsprite.graphics.line_style(color=\'#0af\', thickness=1)\n\nrectangle_1: ap.Rectangle = sprite.graphics.draw_rect(\n    x=50, y=50, width=50, height=50)\nrectangle_1.line_thickness = ap.Int(5)\n\nrectangle_2: ap.Rectangle = sprite.graphics.draw_rect(\n    x=150, y=50, width=50, height=50)\nrectangle_2.line_thickness = ap.Int(10)\n\nap.save_overall_html(\n    dest_dir_path=\'./graphics_line_thickness_basic_usage/\')\n```':  # noqa
    '',

    '<iframe src="static/graphics_line_thickness_basic_usage/index.html" width="250" height="150"></iframe>':  # noqa
    '',

    '## line_thickness property API':
    '',

    '<!-- Docstring: apysc._display.line_thickness_interface.LineThicknessInterface.line_thickness -->\n\n<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>\n\n**[Interface summary]** Get this instance\'s line thickness.<hr>\n\n**[Returns]**\n\n- `line_thickness`: Int\n  - Current line thickness.\n\n<hr>\n\n**[Examples]**':  # noqa
    '',

    '```py\n>>> import apysc as ap\n>>> stage: ap.Stage = ap.Stage()\n>>> sprite: ap.Sprite = ap.Sprite()\n>>> sprite.graphics.line_style(\n...     color=\'#fff\', thickness=5)\n>>> line: ap.Line = sprite.graphics.draw_line(\n...     x_start=50, y_start=50, x_end=150, y_end=50)\n>>> line.line_thickness\nInt(5)\n```':  # noqa
    '',

}
