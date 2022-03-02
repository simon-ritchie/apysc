"""This module is for the translation mapping data of the
following document:

Document file: graphics_draw_round_dotted_line.md
Language: jp
"""

from typing import Dict

MAPPING: Dict[str, str] = {

    '# Graphics draw_round_dotted_line interface':
    '',

    'This page explains the `Graphics` class `draw_round_dotted_line` method interface.':  # noqa
    '',

    '## What interface is this?':
    '',

    '`draw_round_dotted_line` interface draws the simple straight round dotted-line graphics. This interface ignores `dot_setting`\\, `dash_setting`\\, `round_dot_setting`\\, `dash_dot_setting`\\, and `cap` settings (this interface is using round cap setting so cap setting will also be ignored).':  # noqa
    '',

    '## Basic usage':
    '',

    '`draw_round_dotted_line` interface has basic coordinates arguments of `x_start`, `y_start`, `x_end` and `y_end`. That also has `round_size` and `space_size` arguments to determine the round style (line round size and the space size between each round).':  # noqa
    '',

    '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    background_color=\'#333\',\n    stage_width=250,\n    stage_height=130,\n    stage_elem_id=\'stage\')\nsprite: ap.Sprite = ap.Sprite()\n\n# Set 5-pixel round size and draw the line.\nsprite.graphics.line_style(color=\'#0af\')\nsprite.graphics.draw_round_dotted_line(\n    x_start=50, y_start=50, x_end=200, y_end=50,\n    round_size=5, space_size=5)\n\n# Set 10-pixel round size and draw the line.\nsprite.graphics.draw_round_dotted_line(\n    x_start=50, y_start=80, x_end=200, y_end=80,\n    round_size=10, space_size=5)\n\nap.save_overall_html(\n    dest_dir_path=\'graphics_draw_round_dotted_line_basic_usage/\')\n```':  # noqa
    '',

    '<iframe src="static/graphics_draw_round_dotted_line_basic_usage/index.html" width="250" height="130"></iframe>':  # noqa
    '',

    '## Notes':
    '',

    'Since this interface uses the round cap setting, the line length becomes longer by the size of the cap.\n\nIf you want to align the left line position with other lines, subtract half-round size from the `x_start` argument.':  # noqa
    '',

    '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    background_color=\'#333\',\n    stage_width=270,\n    stage_height=130,\n    stage_elem_id=\'stage\')\nsprite: ap.Sprite = ap.Sprite()\n\n# Set 5-pixel round size and draw the line.\nsprite.graphics.line_style(color=\'#0af\')\nsprite.graphics.draw_round_dotted_line(\n    x_start=50, y_start=50, x_end=220, y_end=50,\n    round_size=10, space_size=5)\n\n# Set 45-pixel (50 - half-round size) to x_start argument\n# and draw the normal line.\nsprite.graphics.draw_line(\n    x_start=45, y_start=80, x_end=225, y_end=80)\n\nap.save_overall_html(\n    dest_dir_path=\'graphics_draw_round_dotted_line_notes/\')\n```':  # noqa
    '',

    '<iframe src="static/graphics_draw_round_dotted_line_notes/index.html" width="270" height="130"></iframe>':  # noqa
    '',

    '## draw_round_dotted_line API':
    '',

    '<!-- Docstring: apysc._display.graphics.Graphics.draw_round_dotted_line -->\n\n<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>\n\n**[Interface signature]** `draw_round_dotted_line(self, x_start:Union[int, apysc._type.int.Int], y_start:Union[int, apysc._type.int.Int], x_end:Union[int, apysc._type.int.Int], y_end:Union[int, apysc._type.int.Int], round_size:Union[int, apysc._type.int.Int], space_size:Union[int, apysc._type.int.Int]) -> \'_line.Line\'`<hr>\n\n**[Interface summary]** Draw a round-dotted line vector graphics.<hr>\n\n**[Parameters]**\n\n- `x_start`: Int or int\n  - Line start x-coordinate.\n- `y_start`: Int or int\n  - Line start y-coordinate.\n- `x_end`: Int or int\n  - Line end x-coordinate.\n- `y_end`: Int or int\n  - Line end y-coordinate.\n- `round_size`: Int or int\n  - Dot round size.\n- `space_size`: Int or int\n  - Blank space size between dots.\n\n<hr>\n\n**[Returns]**\n\n- `line`: Line\n  - Created line graphics instance.\n\n<hr>\n\n**[Notes]**\n\nThis interface ignores line settings, like the `LineDotSetting`, except `LineRoundDotSetting`.<hr>\n\n**[Examples]**':  # noqa
    '',

    '```py\n>>> import apysc as ap\n>>> stage: ap.Stage = ap.Stage()\n>>> sprite: ap.Sprite = ap.Sprite()\n>>> sprite.graphics.line_style(color=\'#fff\', thickness=5)\n>>> line: ap.Line = sprite.graphics.draw_round_dotted_line(\n...    x_start=50, y_start=50, x_end=150, y_end=50,\n...    round_size=6, space_size=3)\n>>> line.line_color\nString(\'#ffffff\')\n\n>>> line.line_round_dot_setting.round_size\nInt(6)\n\n>>> line.line_round_dot_setting.space_size\nInt(3)\n```':  # noqa
    '',

}
