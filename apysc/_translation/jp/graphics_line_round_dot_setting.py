"""This module is for the translation mapping data of the
following document:

Document file: graphics_line_round_dot_setting.md
Language: jp
"""

from typing import Dict

MAPPING: Dict[str, str] = {

    '# Graphics line_round_dot_setting interface':
    '',

    'This page explains the `Graphics` class `line_round_dot_setting` property interface.':  # noqa
    '',

    '## What interface is this?':
    '',

    'The `line_round_dot_setting` property interface updates or get the instance\'s current line round dot setting.':  # noqa
    '',

    '## Basic usage':
    '',

    'The getter or setter interface value becomes (or requires) the `LineRoundDotSetting` instance value.\n\nThe following example sets the 10-pixel round size to the line:':  # noqa
    '',

    '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    stage_width=250, stage_height=100, background_color=\'#333\',\n    stage_elem_id=\'stage\')\nsprite: ap.Sprite = ap.Sprite()\nsprite.graphics.line_style(color=\'#0af\', thickness=5)\n\nline: ap.Line = sprite.graphics.draw_line(\n    x_start=50, y_start=50, x_end=200, y_end=50)\nline.line_round_dot_setting = ap.LineRoundDotSetting(\n    round_size=10, space_size=5)\n\nap.save_overall_html(\n    dest_dir_path=\'./graphics_line_round_dot_setting_basic_usage/\')\n```':  # noqa
    '',

    '<iframe src="static/graphics_line_round_dot_setting_basic_usage/index.html" width="250" height="100"></iframe>':  # noqa
    '',

    '## line_round_dot_setting property API':
    '',

    '<!-- Docstring: apysc._display.line_round_dot_setting_interface.LineRoundDotSettingInterface.line_round_dot_setting -->\n\n<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>\n\n**[Interface summary]** Get this instance\'s line round dot setting.<hr>\n\n**[Returns]**\n\n- `line_round_dot_setting`: LineRoundDotSetting or None\n  - Line round dot setting.\n\n<hr>\n\n**[Examples]**':  # noqa
    '',

    '```py\n>>> import apysc as ap\n>>> stage: ap.Stage = ap.Stage()\n>>> sprite: ap.Sprite = ap.Sprite()\n>>> sprite.graphics.line_style(color=\'#fff\', thickness=10)\n>>> line: ap.Line = sprite.graphics.draw_line(\n...     x_start=50, y_start=50, x_end=150, y_end=50)\n>>> line.line_round_dot_setting = ap.LineRoundDotSetting(\n...     round_size=10, space_size=5)\n>>> line.line_round_dot_setting.round_size\nInt(10)\n\n>>> line.line_round_dot_setting.space_size\nInt(5)\n```':  # noqa
    '',

}
