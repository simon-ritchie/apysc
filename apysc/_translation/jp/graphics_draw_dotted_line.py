"""This module is for the translation mapping data of the
following document:

Document file: graphics_draw_dotted_line.md
Language: jp
"""

from typing import Dict

MAPPING: Dict[str, str] = {

    '# Graphics draw_dotted_line interface':
    '',

    'This page explains the `Graphics` class `draw_dotted_line` method interface.':  # noqa
    '',

    '## What interface is this?':
    '',

    '`draw_dotted_line` interface will draw the simple straight dotted-line graphics. This interface will ignore `dot_setting`, `dash_setting`, `round_dot_setting`, and `dash_dot_setting`.':  # noqa
    '',

    '## Basic usage':
    '',

    '`draw_dotted_line` interface has basic coordinates arguments of `x_start`, `y_start`, `x_end` and `y_end`. That also has `dot_size` argument and it will set line dot size.':  # noqa
    '',

    '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    background_color=\'#333\',\n    stage_width=250,\n    stage_height=130,\n    stage_elem_id=\'stage\')\nsprite: ap.Sprite = ap.Sprite()\n\n# Set 2-pixel dot size and draw line.\nsprite.graphics.line_style(\n    color=\'#0af\', thickness=2)\nsprite.graphics.draw_dotted_line(\n    x_start=50, y_start=50, x_end=200, y_end=50, dot_size=2)\n\n# Set 5-pixel dot size and draw line.\nsprite.graphics.line_style(\n    color=\'#0af\', thickness=2)\nsprite.graphics.draw_dotted_line(\n    x_start=50, y_start=80, x_end=200, y_end=80, dot_size=5)\n\nap.save_overall_html(\n    dest_dir_path=\'graphics_draw_dotted_line_basic_usage/\')\n```':  # noqa
    '',

    '<iframe src="static/graphics_draw_dotted_line_basic_usage/index.html" width="250" height="130"></iframe>':  # noqa
    '',

    '## draw_dotted_line API':
    '',

    '<!-- Docstring: apysc._display.graphics.Graphics.draw_dotted_line -->\n\n<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>\n\n**[Interface signature]** `draw_dotted_line(self, x_start:Union[int, apysc._type.int.Int], y_start:Union[int, apysc._type.int.Int], x_end:Union[int, apysc._type.int.Int], y_end:Union[int, apysc._type.int.Int], dot_size:Union[int, apysc._type.int.Int]) -> \'_line.Line\'`<hr>\n\n**[Interface summary]** Draw a dotted line vector graphics.<hr>\n\n**[Parameters]**\n\n- `x_start`: Int or int\n  - Line start x-coordinate.\n- `y_start`: Int or int\n  - Line start y-coordinate.\n- `x_end`: Int or int\n  - Line end x-coordinate.\n- `y_end`: Int or int\n  - Line end y-coordinate.\n- `dot_size`: Int or int\n  - Dot size.\n\n<hr>\n\n**[Returns]**\n\n- `line`: Line\n  - Created line graphics instance.\n\n<hr>\n\n**[Notes]**\n\n ・This interface ignores line settings, like the `LineDashSetting`, except `LineDotSetting`.<hr>\n\n**[Examples]**':  # noqa
    '',

    '```py\n>>> import apysc as ap\n>>> stage: ap.Stage = ap.Stage()\n>>> sprite: ap.Sprite = ap.Sprite()\n>>> sprite.graphics.line_style(color=\'#fff\', thickness=5)\n>>> line: ap.Line = sprite.graphics.draw_dotted_line(\n...     x_start=50, y_start=50, x_end=150, y_end=50, dot_size=5)\n>>> line.line_color\nString(\'#ffffff\')\n\n>>> line.line_thickness\nInt(5)\n\n>>> line.line_dot_setting.dot_size\nInt(5)\n```':  # noqa
    '',

}
