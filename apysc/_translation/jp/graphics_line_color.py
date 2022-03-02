"""This module is for the translation mapping data of the
following document:

Document file: graphics_line_color.md
Language: jp
"""

from typing import Dict

MAPPING: Dict[str, str] = {

    '# Graphics line_color interface':
    '',

    'This page explains the `Graphics` class `line_color` property interface.':  # noqa
    '',

    '## What interface is this?':
    '',

    'The `line_color` property interface updates or get the instance\'s line color.':  # noqa
    '',

    '## Basic usage':
    '',

    'The getter or setter interface value becomes (or requires) the `String` hex color code value.\n\nThe following example changes the line color (from cyan to magenta and magenta to cyan) when you click the rectangle:':  # noqa
    '',

    '```py\n# runnable\nimport apysc as ap\n\n\ndef on_click(e: ap.MouseEvent[ap.Rectangle], options: dict) -> None:\n    """\n    The handler that the rectangle calls when clicked.\n\n    Parameters\n    ----------\n    e : MouseEvent\n        Event instance.\n    options : dict\n        Optional arguments dictionary.\n    """\n    rectangle: ap.Rectangle = e.this\n    line_color: ap.String = rectangle.line_color\n    with ap.If(line_color == \'#00aaff\'):\n        rectangle.line_color = ap.String(\'#f0a\')\n    with ap.Else():\n        rectangle.line_color = ap.String(\'#0af\')\n\n\nap.Stage(\n    stage_width=150, stage_height=150, background_color=\'#333\',\n    stage_elem_id=\'stage\')\nsprite: ap.Sprite = ap.Sprite()\nsprite.graphics.begin_fill(color=\'#0\', alpha=0.0)\nsprite.graphics.line_style(color=\'#0af\', thickness=5)\n\nrectangle: ap.Rectangle = sprite.graphics.draw_rect(\n    x=50, y=50, width=50, height=50)\n\nap.save_overall_html(\n    dest_dir_path=\'./graphics_line_color_basic_usage/\')\n```':  # noqa
    '',

    '<iframe src="static/graphics_line_color_basic_usage/index.html" width="150" height="150"></iframe>':  # noqa
    '',

    '## line_color property API':
    '',

    '<!-- Docstring: apysc._display.line_color_interface.LineColorInterface.line_color -->\n\n<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>\n\n**[Interface summary]** Get this instance\'s line color.<hr>\n\n**[Returns]**\n\n- `line_color`: String\n  - Current line color (hexadecimal string, e.g., \'#00aaff\'). If not be set, this interface returns a blank string.\n\n<hr>\n\n**[Examples]**':  # noqa
    '',

    '```py\n>>> import apysc as ap\n>>> stage: ap.Stage = ap.Stage()\n>>> sprite: ap.Sprite = ap.Sprite()\n>>> sprite.graphics.line_style(color=\'#fff\', thickness=10)\n>>> line: ap.Line = sprite.graphics.draw_line(\n...     x_start=50, y_start=50, x_end=150, y_end=50)\n>>> line.line_color = ap.String(\'#0af\')\n>>> line.line_color\nString(\'#00aaff\')\n```':  # noqa
    '',

}
