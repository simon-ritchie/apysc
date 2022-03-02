"""This module is for the translation mapping data of the
following document:

Document file: graphics_line_dot_setting.md
Language: jp
"""

from typing import Dict

MAPPING: Dict[str, str] = {

    '# Graphics line_dot_setting interface':
    '',

    'This page explains the `Graphics` class `line_dot_setting` property interface.':  # noqa
    '',

    '## What interface is this?':
    '',

    'The `line_dot_setting` property interface updates or gets the instance\'s current line dot setting.':  # noqa
    '',

    '## Basic usage':
    '',

    'The getter or setter interface value becomes (or requires) the `LineDotSetting` instance value.\n\nThe following example sets the 5-pixel dot to the line:':  # noqa
    '',

    '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    stage_width=250, stage_height=100, background_color=\'#333\',\n    stage_elem_id=\'stage\')\nsprite: ap.Sprite = ap.Sprite()\nsprite.graphics.line_style(color=\'#0af\', thickness=5)\n\nline: ap.Line = sprite.graphics.draw_line(\n    x_start=50, y_start=50, x_end=200, y_end=50)\nline.line_dot_setting = ap.LineDotSetting(dot_size=5)\n\nap.save_overall_html(\n    dest_dir_path=\'./graphics_line_dot_setting_basic_usage/\')\n```':  # noqa
    '',

    '<iframe src="static/graphics_line_dot_setting_basic_usage/index.html" width="250" height="100"></iframe>':  # noqa
    '',

    '## See also':
    '',

    '- [Graphics class line style interface](graphics_line_style.md)':
    '',

    '## line_dot_setting property API':
    '',

    '<!-- Docstring: apysc._display.line_dot_setting_interface.LineDotSettingInterface.line_dot_setting -->\n\n<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>\n\n**[Interface summary]** Get this instance\'s line dot setting.<hr>\n\n**[Returns]**\n\n- `line_dot_setting`: LineDotSetting or None\n  - Lien dot setting.\n\n<hr>\n\n**[Examples]**':  # noqa
    '',

    '```py\n>>> import apysc as ap\n>>> stage: ap.Stage = ap.Stage()\n>>> sprite: ap.Sprite = ap.Sprite()\n>>> sprite.graphics.line_style(color=\'#fff\', thickness=10)\n>>> line: ap.Line = sprite.graphics.draw_line(\n...     x_start=50, y_start=50, x_end=150, y_end=50)\n>>> line.line_dot_setting = ap.LineDotSetting(dot_size=5)\n>>> line.line_dot_setting.dot_size\nInt(5)\n```':  # noqa
    '',

}
