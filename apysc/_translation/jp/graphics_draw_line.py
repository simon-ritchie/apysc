"""This module is for the translation mapping data of the
following document:

Document file: graphics_draw_line.md
Language: jp
"""

from typing import Dict

MAPPING: Dict[str, str] = {

    '# Graphics draw_line interface':
    '',

    'This page explains the `Graphics` class `draw_line` method interface.':
    '',

    '## What interface is this?':
    '',

    '`draw_line` interface will draw the simple straight line graphics. This interface will ignore `dot_setting`, `dash_setting`, `round_dot_setting`, and `dash_dot_setting`.':  # noqa
    '',

    '## Basic usage':
    '',

    '`draw_line` inteface has `x_start` (line x-start coordinate), `y_start` (line y-start coordinate), `x_end` (line x-end coordinate), and `y_end` (line y-end coordinate) arguments.':  # noqa
    '',

    '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    background_color=\'#333\',\n    stage_width=200,\n    stage_height=100,\n    stage_elem_id=\'stage\')\nsprite: ap.Sprite = ap.Sprite()\n\nsprite.graphics.line_style(color=\'#0af\', thickness=5)\nsprite.graphics.draw_line(x_start=50, y_start=50, x_end=150, y_end=50)\n\nap.save_overall_html(\n    dest_dir_path=\'graphics_draw_line_basic_usage/\')\n```':  # noqa
    '',

    '<iframe src="static/graphics_draw_line_basic_usage/index.html" width="200" height=100></iframe>':  # noqa
    '',

    '## Ignored line style settings':
    '',

    'This interface will ignore `dot_setting`, `dash_setting`, `round_dot_setting`, and `dash_dot_setting` for simplicity. If you need to draw these styled lines, then use `draw_dotted_line`, `draw_dashed_line`, `draw_round_dotted_line`, or `draw_dash_dotted_line` interfaces instead of the `draw_line` interface.':  # noqa
    '',

    '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    background_color=\'#333\',\n    stage_width=200,\n    stage_height=100,\n    stage_elem_id=\'stage\')\nsprite: ap.Sprite = ap.Sprite()\n\n# dot_setting will be ignored, and the result line will not be dotted.\nsprite.graphics.line_style(\n    color=\'#0af\', thickness=5,\n    dot_setting=ap.LineDotSetting(dot_size=5))\nsprite.graphics.draw_line(x_start=50, y_start=50, x_end=150, y_end=50)\n\nap.save_overall_html(\n    dest_dir_path=\'graphics_draw_line_ignored_dot_setting/\')\n```':  # noqa
    '',

    '<iframe src="static/graphics_draw_line_ignored_dot_setting/index.html" width="200" height=100></iframe>':  # noqa
    '',

    '## Line instance':
    '',

    '`draw_line` interface returns the `Line` instance. You can update each setting or bind events to that instance. `draw_dotted_line`, `draw_dashed_line`, `draw_round_dotted_line`\n, and `draw_dash_dotted_line` will also return the same type instance.':  # noqa
    '',

    '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    background_color=\'#333\',\n    stage_width=200,\n    stage_height=100,\n    stage_elem_id=\'stage\')\nsprite: ap.Sprite = ap.Sprite()\n\nsprite.graphics.line_style(\n    color=\'#0af\', thickness=5)\nline: ap.Line = sprite.graphics.draw_line(\n    x_start=50, y_start=50, x_end=150, y_end=50)\n\n# Update the line color from cyan to magenta.\nline.line_color = ap.String(\'#f0a\')\n\nap.save_overall_html(\n    dest_dir_path=\'graphics_draw_line_line_instance/\')\n```':  # noqa
    '',

    '<iframe src="static/graphics_draw_line_line_instance/index.html" width="200" height=100></iframe>':  # noqa
    '',

    '## draw_line API':
    '',

    '<!-- Docstring: apysc._display.graphics.Graphics.draw_line -->\n\n<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>\n\n**[Interface signature]** `draw_line(self, x_start:Union[int, apysc._type.int.Int], y_start:Union[int, apysc._type.int.Int], x_end:Union[int, apysc._type.int.Int], y_end:Union[int, apysc._type.int.Int]) -> \'_line.Line\'`<hr>\n\n**[Interface summary]** Draw a normal line vector graphic.<hr>\n\n**[Parameters]**\n\n- `x_start`: Int or int\n  - Line start x-coordinate.\n- `y_start`: Int or int\n  - Line start y-coordinate.\n- `x_end`: Int or int\n  - Line end x-coordinate.\n- `y_end`: Int or int\n  - Line end y-coordinate.\n\n<hr>\n\n**[Returns]**\n\n- `line`: Line\n  - Created line graphics instance.\n\n<hr>\n\n**[Notes]**\n\n ・This interface ignores line settings, like the `LineDotSetting`, `LineDashSetting`.<hr>\n\n**[Examples]**':  # noqa
    '',

    '```py\n>>> import apysc as ap\n>>> stage: ap.Stage = ap.Stage()\n>>> sprite: ap.Sprite = ap.Sprite()\n>>> sprite.graphics.line_style(color=\'#fff\', thickness=5)\n>>> line: ap.Line = sprite.graphics.draw_line(\n...     x_start=50, y_start=50, x_end=150, y_end=50)\n>>> line.line_color\nString(\'#ffffff\')\n\n>>> line.line_thickness\nInt(5)\n```':  # noqa
    '',

}
