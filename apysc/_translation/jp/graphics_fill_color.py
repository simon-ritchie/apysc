"""This module is for the translation mapping data of the
following document:

Document file: graphics_fill_color.md
Language: jp
"""

from typing import Dict

MAPPING: Dict[str, str] = {

    '# Graphics fill_color interface':
    '',

    'This page explains the `Graphics` class `fill_color` property interface.':  # noqa
    '',

    '## What interface is this?':
    '',

    'The `fill_color` property interface updates or get the instance\'s fill color.':  # noqa
    '',

    '## Basic usage':
    '',

    'The getter interface becomes the `String` hex color code value, and the setter one also requires the `String` hex color code value.\n\nThe following example changes the fill color (from cyan to magenta and magenta to cyan) when you click the rectangle:':  # noqa
    '',

    '```py\n# runnable\nimport apysc as ap\n\n\ndef on_click(e: ap.MouseEvent[ap.Rectangle], options: dict) -> None:\n    """\n    The handler that the rectangle calls when clicked.\n\n    Parameters\n    ----------\n    e : MouseEvent\n        Event instance.\n    options : dict\n        Optional arguments dictionary.\n    """\n    rectangle: ap.Rectangle = e.this\n    fill_color: ap.String = rectangle.fill_color\n    with ap.If(fill_color == \'#00aaff\'):\n        rectangle.fill_color = ap.String(\'#f0a\')\n    with ap.Else():\n        rectangle.fill_color = ap.String(\'#0af\')\n\n\nap.Stage(\n    stage_width=150, stage_height=150, background_color=\'#333\',\n    stage_elem_id=\'stage\')\nsprite: ap.Sprite = ap.Sprite()\nsprite.graphics.begin_fill(color=\'#0af\')\nrectangle: ap.Rectangle = sprite.graphics.draw_rect(\n    x=50, y=50, width=50, height=50)\nrectangle.click(on_click)\n\nap.save_overall_html(\n    dest_dir_path=\'./graphics_fill_color_basic_usage/\')\n```':  # noqa
    '',

    '<iframe src="static/graphics_fill_color_basic_usage/index.html" width="150" height="150"></iframe>':  # noqa
    '',

    '## fill_color property API':
    '',

    '<!-- Docstring: apysc._display.fill_color_interface.FillColorInterface.fill_color -->\n\n<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>\n\n**[Interface summary]** Get this instance\'s fill color.<hr>\n\n**[Returns]**\n\n- `fill_color`: String\n  - Current fill color (hexadecimal string, e.g., \'#00aaff\'). If not be set, this interface returns a blank string.\n\n<hr>\n\n**[Examples]**':  # noqa
    '',

    '```py\n>>> import apysc as ap\n>>> stage: ap.Stage = ap.Stage()\n>>> sprite: ap.Sprite = ap.Sprite()\n>>> sprite.graphics.begin_fill(color=\'#0af\')\n>>> rectangle: ap.Rectangle = sprite.graphics.draw_rect(\n...     x=50, y=50, width=50, height=50)\n>>> rectangle.fill_color = ap.String(\'#f0a\')\n>>> rectangle.fill_color\nString(\'#ff00aa\')\n```':  # noqa
    '',

}
