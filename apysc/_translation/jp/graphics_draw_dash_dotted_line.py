"""This module is for the translation mapping data of the
following document:

Document file: graphics_draw_dash_dotted_line.md
Language: jp
"""

from typing import Dict

MAPPING: Dict[str, str] = {

    '# Graphics draw_dash_dotted_line interface':
    '',

    'This page explains the `Graphics` class `draw_dash_dotted_line` method interface.':  # noqa
    '',

    '## What interface is this?':
    '',

    '`draw_dash_dotted_line` interface draws the simple straight dash dotted-line (also called 1-dot chain line or long dashed short dashed line) graphics.\n\n This interface will ignore `dot_setting`, `dash_setting`, `round_dot_setting`, and `dash_dot_setting`.':  # noqa
    '',

    '## Basic usage':
    '',

    '`draw_dash_dotted_line` interface has basic coordinates arguments of `x_start`, `y_start`, `x_end` and `y_end`. That also has `dot_size` (the short dash size), `dash_size` (the long dash size) and `space_size` (the space size between the each dashes) arguments to determine line style.':  # noqa
    '',

    '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    background_color=\'#333\',\n    stage_width=250,\n    stage_height=130,\n    stage_elem_id=\'stage\')\nsprite: ap.Sprite = ap.Sprite()\n\n# Set 2-pixel dot size and 6-pixel dash size and draw the line.\nsprite.graphics.line_style(color=\'#0af\', thickness=5)\nsprite.graphics.draw_dash_dotted_line(\n    x_start=50, y_start=50, x_end=200, y_end=50,\n    dot_size=2, dash_size=6, space_size=5)\n\n# Set 5-pixel dot size and 10-pixel dash size and draw the line.\nsprite.graphics.draw_dash_dotted_line(\n    x_start=50, y_start=80, x_end=200, y_end=80,\n    dot_size=5, dash_size=10, space_size=5)\n\nap.save_overall_html(\n    dest_dir_path=\'graphics_draw_dash_dotted_line_basic_usage/\')\n```':  # noqa
    '',

    '<iframe src="static/graphics_draw_dash_dotted_line_basic_usage/index.html" width="250" height="130"></iframe>':  # noqa
    '',

    '## draw_dash_dotted_line API':
    '',

    '<!-- Docstring: apysc._display.graphics.Graphics.draw_dash_dotted_line -->\n\n<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>\n\n**[Interface signature]** `draw_dash_dotted_line(self, x_start:Union[int, apysc._type.int.Int], y_start:Union[int, apysc._type.int.Int], x_end:Union[int, apysc._type.int.Int], y_end:Union[int, apysc._type.int.Int], dot_size:Union[int, apysc._type.int.Int], dash_size:Union[int, apysc._type.int.Int], space_size:Union[int, apysc._type.int.Int]) -> \'_line.Line\'`<hr>\n\n**[Interface summary]** Draw a dash-dotted (1-dot chain) line vector graphics.<hr>\n\n**[Parameters]**\n\n- `x_start`: Int or int\n  - Line start x-coordinate.\n- `y_start`: Int or int\n  - Line start y-coordinate.\n- `x_end`: Int or int\n  - Line end x-coordinate.\n- `y_end`: Int or int\n  - Line end y-coordinate.\n- `dot_size`: Int or int\n  - Dot size.\n- `dash_size`: Int or int\n  - Dash size.\n- `space_size`: Int or int\n  - Blank space size between dots and dashes.\n\n<hr>\n\n**[Returns]**\n\n- `line`: Line\n  - Created line graphics instance.\n\n<hr>\n\n**[Examples]**':  # noqa
    '',

    '```py\n>>> import apysc as ap\n>>> stage: ap.Stage = ap.Stage()\n>>> sprite: ap.Sprite = ap.Sprite()\n>>> sprite.graphics.line_style(color=\'#fff\', thickness=5)\n>>> line: ap.Line = sprite.graphics.draw_dash_dotted_line(\n...    x_start=50, y_start=50, x_end=150, y_end=50,\n...    dot_size=2, dash_size=5, space_size=3)\n>>> line.line_color\nString(\'#ffffff\')\n\n>>> line.line_dash_dot_setting.dot_size\nInt(2)\n\n>>> line.line_dash_dot_setting.dash_size\nInt(5)\n\n>>> line.line_dash_dot_setting.space_size\nInt(3)\n```':  # noqa
    '',

}
