"""This module is for the translation mapping data of the
following document:

Document file: graphics_line_style.md
Language: jp
"""

from typing import Dict

MAPPING: Dict[str, str] = {

    '# Graphics line_style interface':
    '',

    'This page explains the `Graphics` class `line_style` method interface.':  # noqa
    '',

    '## What interface is this?':
    '',

    'The `line_style` interface sets each line style, such as the line color, line alpha, line thickness, line dot setting. This interface maintains these settings until it is called again or called the `clear` method (similar to the `begin_fill` interface).':  # noqa
    '',

    '## Basic usage':
    '',

    'Draw vector graphics interfaces (e.g., the `draw_rect` or `line_to`) use these line settings when creating. Therefore, calling the `line_style` method is necessary before calling each drawing interface.':  # noqa
    '',

    '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    background_color=\'#333\',\n    stage_width=200,\n    stage_height=162,\n    stage_elem_id=\'stage\')\nsprite: ap.Sprite = ap.Sprite()\n\n# Draw a white line with 3px line thickness.\nsprite.graphics.line_style(color=\'#ccc\', thickness=8)\nsprite.graphics.move_to(x=50, y=50)\nsprite.graphics.line_to(x=150, y=50)\n\n# Line style setting will be maintained.\nsprite.graphics.move_to(x=50, y=80)\nsprite.graphics.line_to(x=150, y=80)\n\n# Change line color and thickness.\nsprite.graphics.line_style(color=\'#0af\', thickness=3)\nsprite.graphics.move_to(x=50, y=110)\nsprite.graphics.line_to(x=150, y=110)\n\nap.save_overall_html(\n    dest_dir_path=\'graphics_line_style_basics/\')\n```':  # noqa
    '',

    '<iframe src="static/graphics_line_style_basics/index.html" width="200" height="162"></iframe>':  # noqa
    '',

    '## Line-color setting':
    '',

    'The required `color` argument sets the line color.':
    '',

    '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    background_color=\'#333\',\n    stage_width=200,\n    stage_height=102,\n    stage_elem_id=\'stage\')\nsprite: ap.Sprite = ap.Sprite()\n\n# Set a cyan line color and draw the line.\nsprite.graphics.line_style(color=\'#0af\', thickness=4)\nsprite.graphics.draw_line(x_start=50, x_end=150, y_start=50, y_end=50)\n\nap.save_overall_html(\n    dest_dir_path=\'graphics_line_style_line_color/\')\n```':  # noqa
    '',

    '<iframe src="static/graphics_line_style_line_color/index.html" width="200" height="102"></iframe>\n\nIf you want to clear line color, specify a blank string to this argument.\n\nFor example, the result line graphic becomes invisible since the following code clears the line color setting.':  # noqa
    '',

    '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    background_color=\'#333\',\n    stage_width=200,\n    stage_height=102,\n    stage_elem_id=\'stage\')\nsprite: ap.Sprite = ap.Sprite()\n\n# Set a cyan line color.\nsprite.graphics.line_style(color=\'#0af\', thickness=4)\n\n# Clear the line color by specifying a blank string.\nsprite.graphics.line_style(color=\'\', thickness=4)\nsprite.graphics.draw_line(x_start=50, x_end=150, y_start=50, y_end=50)\n\nap.save_overall_html(\n    dest_dir_path=\'graphics_line_style_clear_line_color/\')\n```':  # noqa
    '',

    '<iframe src="static/graphics_line_style_clear_line_color/index.html" width="200" height="102"></iframe>\n\nColor code is acceptable like the following list (same as `begin_fill` interface `color` argument):\n\n- Six characters, e.g., `#00aaff`.\n- Three characters, e.g., `#0af` (this becomes `#00aaff`).\n- Single character, e.g., `#5` (this becomes `#000005`).\n- Skipped `#` symbol, e.g., `0af` (this becomes `#00aaff`).\n- Blank string, e.g., `\'\'` (this clears line color setting).':  # noqa
    '',

    '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    background_color=\'#333\',\n    stage_width=200,\n    stage_height=162,\n    stage_elem_id=\'stage\')\nsprite: ap.Sprite = ap.Sprite()\n\n# The six characters line color setting (a cyan color).\nsprite.graphics.line_style(color=\'#00aaff\', thickness=4)\nsprite.graphics.draw_line(x_start=50, x_end=150, y_start=50, y_end=50)\n\n# The three characters line color setting (a magenta color).\nsprite.graphics.line_style(color=\'#f0a\', thickness=4)\nsprite.graphics.draw_line(x_start=50, x_end=150, y_start=80, y_end=80)\n\n# The one character line color setting (a black color).\nsprite.graphics.line_style(color=\'#5\', thickness=4)\nsprite.graphics.draw_line(x_start=50, x_end=150, y_start=110, y_end=110)\n\nap.save_overall_html(\n    dest_dir_path=\'graphics_line_style_line_color_color_code/\')\n```':  # noqa
    '',

    '<iframe src="static/graphics_line_style_line_color_color_code/index.html" width="200" height="162"></iframe>':  # noqa
    '',

    '## Line thickness setting':
    '',

    'The `thickness` argument sets the line thickness. It can accept greater than or equal to 1.':  # noqa
    '',

    '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    background_color=\'#333\',\n    stage_width=200,\n    stage_height=165,\n    stage_elem_id=\'stage\')\nsprite: ap.Sprite = ap.Sprite()\n\n# Set 1-pixel line thickness.\nsprite.graphics.line_style(color=\'#0af\', thickness=1)\nsprite.graphics.draw_line(x_start=50, x_end=150, y_start=50, y_end=50)\n\n# Set 4-pixel line thickness.\nsprite.graphics.line_style(color=\'#0af\', thickness=4)\nsprite.graphics.draw_line(x_start=50, x_end=150, y_start=80, y_end=80)\n\n# Set 10-pixel line thickness.\nsprite.graphics.line_style(color=\'#0af\', thickness=10)\nsprite.graphics.draw_line(x_start=50, x_end=150, y_start=110, y_end=110)\n\nap.save_overall_html(\n    dest_dir_path=\'graphics_line_style_thickness/\')\n```':  # noqa
    '',

    '<iframe src="static/graphics_line_style_thickness/index.html" width="200" height="165"></iframe>':  # noqa
    '',

    '## Line alpha (opacity) setting':
    '',

    'A line alpha (opacity) can be set by the `alpha` argument. It can accept 0.0 (transparent) to 1.0 (opaque).':  # noqa
    '',

    '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    background_color=\'#333\',\n    stage_width=150,\n    stage_height=150,\n    stage_elem_id=\'stage\')\nsprite: ap.Sprite = ap.Sprite()\n\n# Draw the cyan line from upper-left to lower-right.\nsprite.graphics.line_style(color=\'#0af\', thickness=15, alpha=0.3)\nsprite.graphics.draw_line(x_start=50, x_end=100, y_start=50, y_end=100)\n\n# Draw the magenta line from upper-right to lower-left.\nsprite.graphics.line_style(color=\'#f0a\', thickness=15, alpha=0.3)\nsprite.graphics.draw_line(x_start=100, x_end=50, y_start=50, y_end=100)\n\nap.save_overall_html(\n    dest_dir_path=\'graphics_line_style_alpha/\')\n```':  # noqa
    '',

    '<iframe src="static/graphics_line_style_alpha/index.html" width="150" height="150"></iframe>':  # noqa
    '',

    '## Line cap setting':
    '',

    'Line cap setting changes line edge style. The `cap` argument sets this style setting, and `LineCaps` enum values are acceptable.\n\nThere are three `LineCaps` options, as follows:\n\n- BUTT: This is the default value, and it sets no cap.\n- ROUND: This changes the line edge to the rounded one.\n- SQUARE: This is similar to BUTT, but it increases the line length by the squared edge.':  # noqa
    '',

    '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    background_color=\'#333\',\n    stage_width=200,\n    stage_height=180,\n    stage_elem_id=\'stage\')\nsprite: ap.Sprite = ap.Sprite()\n\n# BUTT caps setting (default).\nsprite.graphics.line_style(color=\'#0af\', thickness=20, cap=ap.LineCaps.BUTT)\nsprite.graphics.draw_line(x_start=50, x_end=150, y_start=50, y_end=50)\n\n# ROUND caps setting.\nsprite.graphics.line_style(color=\'#0af\', thickness=20, cap=ap.LineCaps.ROUND)\nsprite.graphics.draw_line(x_start=50, x_end=150, y_start=90, y_end=90)\n\n# SQUARE caps setting (same line length setting as BUTT line,\n# but this will be longer for the caps).\nsprite.graphics.line_style(color=\'#0af\', thickness=20, cap=ap.LineCaps.SQUARE)\nsprite.graphics.draw_line(x_start=50, x_end=150, y_start=130, y_end=130)\n\nap.save_overall_html(\n    dest_dir_path=\'graphics_line_style_caps/\')\n```':  # noqa
    '',

    '<iframe src="static/graphics_line_style_caps/index.html" width="200" height="180"></iframe>':  # noqa
    '',

    '## Line joints setting':
    '',

    'Line joints setting changes the line vertices style. The `joints` argument sets this style, and `LineJoints` enum values are acceptable. The `Polyline` class (`move_to` and `line_to` interfaces) mainly uses this argument.\n\nThere are three LineJoints enum values, as follows:\n\n- MITER: This setting sets the style like a picture frame vertices. This setting is the default style setting.\n- ROUND: This setting sets the rounded vertices style.\n- BEVEL: This setting sets a sloping vertices style.':  # noqa
    '',

    '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    background_color=\'#333\',\n    stage_width=350,\n    stage_height=150,\n    stage_elem_id=\'stage\')\nsprite: ap.Sprite = ap.Sprite()\n\n# Set MITER joints setting and draw the polyline.\nsprite.graphics.line_style(\n    color=\'#0af\', thickness=10, joints=ap.LineJoints.MITER)\nsprite.graphics.move_to(x=50, y=100)\nsprite.graphics.line_to(x=75, y=50)\nsprite.graphics.line_to(x=100, y=100)\n\n# Set ROUND joints setting and draw the polyline.\nsprite.graphics.line_style(\n    color=\'#0af\', thickness=10, joints=ap.LineJoints.ROUND)\nsprite.graphics.move_to(x=150, y=100)\nsprite.graphics.line_to(x=175, y=50)\nsprite.graphics.line_to(x=200, y=100)\n\n# Set BEVEL joints setting and draw the polyline.\nsprite.graphics.line_style(\n    color=\'#0af\', thickness=10, joints=ap.LineJoints.BEVEL)\nsprite.graphics.move_to(x=250, y=100)\nsprite.graphics.line_to(x=275, y=50)\nsprite.graphics.line_to(x=300, y=100)\n\nap.save_overall_html(\n    dest_dir_path=\'graphics_line_style_joints/\')\n```':  # noqa
    '',

    '<iframe src="static/graphics_line_style_joints/index.html" width="350" height="150"></iframe>':  # noqa
    '',

    '## Line dot setting':
    '',

    'Line dot setting changes the line to dotted line. The `dot_setting` argument (`LineDotSetting` value) sets this setting. It can change dot size by the `dot_size` argument (greater than or equal to 1 value is acceptable).':  # noqa
    '',

    '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    background_color=\'#333\',\n    stage_width=300,\n    stage_height=160,\n    stage_elem_id=\'stage\')\nsprite: ap.Sprite = ap.Sprite()\n\n# Set the line dot settings with 2-pixel dot size and draw the dotted line.\nsprite.graphics.line_style(\n    color=\'#0af\', thickness=5, dot_setting=ap.LineDotSetting(dot_size=2))\nsprite.graphics.move_to(x=50, y=50)\nsprite.graphics.line_to(x=250, y=50)\n\n# Set the line dot settings with 5-pixel dot size and draw the dotted line.\nsprite.graphics.line_style(\n    color=\'#0af\', thickness=5, dot_setting=ap.LineDotSetting(dot_size=5))\nsprite.graphics.move_to(x=50, y=80)\nsprite.graphics.line_to(x=250, y=80)\n\n# Set the line dot settings with 10-pixel dot size and draw the dotted line.\nsprite.graphics.line_style(\n    color=\'#0af\', thickness=5, dot_setting=ap.LineDotSetting(dot_size=10))\nsprite.graphics.move_to(x=50, y=110)\nsprite.graphics.line_to(x=250, y=110)\n\nap.save_overall_html(\n    dest_dir_path=\'graphics_line_style_line_dot_setting/\')\n```':  # noqa
    '',

    '<iframe src="static/graphics_line_style_line_dot_setting/index.html" width="300" height="160"></iframe>\n\nThis setting (or the other similar settings) also changes the `Rectangle` or other graphics classes.':  # noqa
    '',

    '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    background_color=\'#333\',\n    stage_width=250,\n    stage_height=150,\n    stage_elem_id=\'stage\')\nsprite: ap.Sprite = ap.Sprite()\n\n# Set the line dot setting with 2-pixel dot size and draw the rectangle.\n# Fill color setting is skipped.\nsprite.graphics.line_style(\n    color=\'#0af\', thickness=5, dot_setting=ap.LineDotSetting(dot_size=2))\nsprite.graphics.draw_rect(x=50, y=50, width=50, height=50)\n\n# Draw the rectangle with the dotted line setting and the fill color.\nsprite.graphics.begin_fill(color=\'#038\')\nsprite.graphics.draw_rect(x=150, y=50, width=50, height=50)\n\nap.save_overall_html(\n    dest_dir_path=\'graphics_line_style_line_dot_setting_rectangle/\')\n```':  # noqa
    '',

    '<iframe src="static/graphics_line_style_line_dot_setting_rectangle/index.html" width="250" height="150"></iframe>\n\nNotes: This setting will be ignored by `draw_line`, `draw_dotted_line`, `draw_dashed_line`, `draw_round_dotted_line`, and `draw_dash_dotted_line` interfaces.':  # noqa
    '',

    '## Line dash setting':
    '',

    'Line dash setting changes the line to the dashed line. The `dash_setting` argument (`LineDashSetting` value) sets this setting. It can change dash size and space size by the `dash_size` and `space_size` arguments.':  # noqa
    '',

    '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    background_color=\'#333\',\n    stage_width=300,\n    stage_height=130,\n    stage_elem_id=\'stage\')\nsprite: ap.Sprite = ap.Sprite()\n\n# Set 10-pixel dash size and 3-pixel space size and draw the line.\nsprite.graphics.line_style(\n    color=\'#0af\', thickness=3,\n    dash_setting=ap.LineDashSetting(dash_size=10, space_size=3))\nsprite.graphics.move_to(x=50, y=50)\nsprite.graphics.line_to(x=250, y=50)\n\n# Set 15-pixel dash size and 5-pixel space size and draw the line.\nsprite.graphics.line_style(\n    color=\'#0af\', thickness=3,\n    dash_setting=ap.LineDashSetting(dash_size=15, space_size=5))\nsprite.graphics.move_to(x=50, y=80)\nsprite.graphics.line_to(x=250, y=80)\n\nap.save_overall_html(\n    dest_dir_path=\'graphics_line_style_line_dash_setting/\')\n```':  # noqa
    '',

    '<iframe src="static/graphics_line_style_line_dash_setting/index.html" width="300" height="130"></iframe>\n\nNotes: This setting will be ignored by `draw_line`, `draw_dotted_line`, `draw_dashed_line`, `draw_round_dotted_line`, and `draw_dash_dotted_line` interfaces.':  # noqa
    '',

    '## Line round dot setting':
    '',

    'Line round dot setting changes the line to the round dotted line. The `round_dot_setting` argument (`LineRoundDotSetting` value) sets this setting. It can change round size and space size by the `round_size` and `space_size` arguments.':  # noqa
    '',

    '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    background_color=\'#333\',\n    stage_width=300,\n    stage_height=130,\n    stage_elem_id=\'stage\')\nsprite: ap.Sprite = ap.Sprite()\n\n# Set 5-pixel round size and draw the line.\nsprite.graphics.line_style(\n    color=\'#0af\', thickness=5,\n    round_dot_setting=ap.LineRoundDotSetting(round_size=5, space_size=5))\nsprite.graphics.move_to(x=50, y=50)\nsprite.graphics.line_to(x=250, y=50)\n\n# Set 10-pixel round size and draw the line.\nsprite.graphics.line_style(\n    color=\'#0af\', thickness=5,\n    round_dot_setting=ap.LineRoundDotSetting(round_size=10, space_size=5))\nsprite.graphics.move_to(x=50, y=80)\nsprite.graphics.line_to(x=250, y=80)\n\nap.save_overall_html(\n    dest_dir_path=\'graphics_line_style_line_round_dot_setting/\')\n```':  # noqa
    '',

    '<iframe src="static/graphics_line_style_line_round_dot_setting/index.html" width="300" height="130"></iframe>\n\nNotes: Since this setting uses the `cap` setting internally, this setting ignores the `cap` setting, increasing the line length by the capsize.\n\nNotes: This setting will be ignored by `draw_line`, `draw_dotted_line`, `draw_dashed_line`, `draw_round_dotted_line`, and `draw_dash_dotted_line` interfaces.':  # noqa
    '',

    '## Line dash-dot setting':
    '',

    'Line dash-dot setting changes the line to the dash-dotted line (also called long dashed short dashed line or one-dot chain line). The `dash_dot_setting` arguments set this setting. This argument accepts the `dot_size` (short dashed size), `dash_size` (long dashed size), and `space_size` arguments.':  # noqa
    '',

    '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    background_color=\'#333\',\n    stage_width=300,\n    stage_height=130,\n    stage_elem_id=\'stage\')\nsprite: ap.Sprite = ap.Sprite()\n\n# Set 3-pixel dot size and 10-pixel dash size and draw the line.\nsprite.graphics.line_style(\n    color=\'#0af\', thickness=3,\n    dash_dot_setting=ap.LineDashDotSetting(\n        dot_size=3, dash_size=10, space_size=3))\nsprite.graphics.move_to(x=50, y=50)\nsprite.graphics.line_to(x=250, y=50)\n\n# Set 5-pixel dot size and 15-pixel dash size and draw the line.\nsprite.graphics.line_style(\n    color=\'#0af\', thickness=3,\n    dash_dot_setting=ap.LineDashDotSetting(\n        dot_size=5, dash_size=15, space_size=3))\nsprite.graphics.move_to(x=50, y=80)\nsprite.graphics.line_to(x=250, y=80)\n\nap.save_overall_html(\n    dest_dir_path=\'graphics_line_style_line_dash_dot_setting/\')\n```':  # noqa
    '',

    '<iframe src="static/graphics_line_style_line_dash_dot_setting/index.html" width="300" height="130"></iframe>\n\nNotes: This setting will be ignored by `draw_line`, `draw_dotted_line`, `draw_dashed_line`, `draw_round_dotted_line`, and `draw_dash_dotted_line` interfaces.':  # noqa
    '',

    '## line_style API':
    '',

    '<!-- Docstring: apysc._display.line_style_interface.LineStyleInterface.line_style -->\n\n<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>\n\n**[Interface signature]** `line_style(self, color:~StrOrString, *, thickness:Union[int, apysc._type.int.Int]=1, alpha:Union[float, apysc._type.number.Number]=1.0, cap:Union[apysc._display.line_caps.LineCaps, NoneType]=None, joints:Union[apysc._display.line_joints.LineJoints, NoneType]=None, dot_setting:Union[apysc._display.line_dot_setting.LineDotSetting, NoneType]=None, dash_setting:Union[apysc._display.line_dash_setting.LineDashSetting, NoneType]=None, round_dot_setting:Union[apysc._display.line_round_dot_setting.LineRoundDotSetting, NoneType]=None, dash_dot_setting:Union[apysc._display.line_dash_dot_setting.LineDashDotSetting, NoneType]=None) -> None`<hr>\n\n**[Interface summary]** Set line style values.<hr>\n\n**[Parameters]**\n\n- `color`: String or str\n  - Hexadecimal color string. e.g., \'#00aaff\'\n- `thickness`: Int or int, default 1\n  - Line thickness (minimum value is 1).\n- `alpha`: float or Number, default 1.0\n  - Line color opacity (0.0 to 1.0).\n- `cap`: LineCaps or None, default None\n  - Line cap (edge style) setting. The not line-related graphics (e.g., Rectangle ignores this, conversely used by Polyline) ignore this setting.\n- `joints`: LineJoints or None, default None\n  - Line vertices (joints) style setting. The not polyline-related graphics (e.g., Rectangle ignores this, conversely used by Polyline) ignore this setting.\n- `dot_setting`: LineDotSetting or None, default None\n  - Dash setting. If this is specified, it makes a line dashed.\n- `dash_setting`: LineDashSetting or None, default None\n  - Dash setting. If this is specified, it makes a line dashed.\n- `round_dot_setting`: LineRoundDotSetting or None, default None\n  - Round dot setting. If this is specified, it makes a line round dotted. Notes: since this style uses a cap setting, it overrides cap and line thickness settings. And it increases the amount of line size. If you want to adjust to the same width of a normal line when using move_to and line_to interfaces, add half-round size to start x-coordinate and subtract from end e-coordinate. e.g., `this.move_to(x + round_size / 2, y)`, `this.line_to(x - round_size / 2, y)`\n- `dash_dot_setting`: LineDashDotSetting or None, default None\n  - Dash dot (1-dot chain) setting. If this is specified, it makes a line 1-dot chained.\n\n<hr>\n\n**[Examples]**':  # noqa
    '',

    '```py\n>>> import apysc as ap\n>>> stage: ap.Stage = ap.Stage()\n>>> sprite: ap.Sprite = ap.Sprite()\n>>> sprite.graphics.line_style(\n...     color=\'#fff\', thickness=5, alpha=0.5,\n...     cap=ap.LineCaps.ROUND)\n>>> line: ap.Line = sprite.graphics.draw_line(\n...     x_start=50, y_start=50, x_end=150, y_end=50)\n>>> line.line_color\nString(\'#ffffff\')\n\n>>> line.line_thickness\nInt(5)\n\n>>> line.line_alpha\nNumber(0.5)\n\n>>> line.line_cap\nString(\'round\')\n```':  # noqa
    '',

    '':
    '',

    '## line_color property API':
    '',

    '<!-- Docstring: apysc._display.line_style_interface.LineStyleInterface.line_color -->\n\n<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>\n\n**[Interface summary]** Get current line color.<hr>\n\n**[Returns]**\n\n- `line_color`: String\n  - Current line color (hexadecimal string, e.g., \'#00aaff\'). If not be set, this interface returns a blank string.\n\n<hr>\n\n**[Examples]**':  # noqa
    '',

    '```py\n>>> import apysc as ap\n>>> stage: ap.Stage = ap.Stage()\n>>> sprite: ap.Sprite = ap.Sprite()\n>>> sprite.graphics.line_style(\n...     color=\'#fff\', thickness=5, alpha=0.5,\n...     cap=ap.LineCaps.ROUND)\n>>> sprite.graphics.line_color\nString(\'#ffffff\')\n```':  # noqa
    '',

    '':
    '',

    '## line_thickness property API':
    '',

    '<!-- Docstring: apysc._display.line_style_interface.LineStyleInterface.line_thickness -->\n\n<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>\n\n**[Interface summary]** Get current line thickness.<hr>\n\n**[Returns]**\n\n- `line_thickness`: Int\n  - Current line thickness.\n\n<hr>\n\n**[Examples]**':  # noqa
    '',

    '```py\n>>> import apysc as ap\n>>> stage: ap.Stage = ap.Stage()\n>>> sprite: ap.Sprite = ap.Sprite()\n>>> sprite.graphics.line_style(\n...     color=\'#fff\', thickness=5, alpha=0.5)\n>>> sprite.graphics.line_thickness\nInt(5)\n```':  # noqa
    '',

    '':
    '',

    '## line_alpha property API':
    '',

    '<!-- Docstring: apysc._display.line_style_interface.LineStyleInterface.line_alpha -->\n\n<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>\n\n**[Interface summary]** Get current line color opacity.<hr>\n\n**[Returns]**\n\n- `line_alpha`: Number\n  - Current line opacity (0.0 to 1.0).\n\n<hr>\n\n**[Examples]**':  # noqa
    '',

    '```py\n>>> import apysc as ap\n>>> stage: ap.Stage = ap.Stage()\n>>> sprite: ap.Sprite = ap.Sprite()\n>>> sprite.graphics.line_style(\n...     color=\'#fff\', thickness=5, alpha=0.5,\n...     cap=ap.LineCaps.ROUND)\n>>> sprite.graphics.line_alpha\nNumber(0.5)\n```':  # noqa
    '',

    '':
    '',

    '## line_cap property API':
    '',

    '<!-- Docstring: apysc._display.line_style_interface.LineStyleInterface.line_cap -->\n\n<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>\n\n**[Interface summary]** Get current line cap (edge) style setting.<hr>\n\n**[Returns]**\n\n- `line_cap`: String\n  - Current line cap (edge) style setting.\n\n<hr>\n\n**[Examples]**':  # noqa
    '',

    '```py\n>>> import apysc as ap\n>>> stage: ap.Stage = ap.Stage()\n>>> sprite: ap.Sprite = ap.Sprite()\n>>> sprite.graphics.line_style(\n...     color=\'#fff\', thickness=5, alpha=0.5,\n...     cap=ap.LineCaps.ROUND)\n>>> sprite.graphics.line_cap\nString(\'round\')\n```':  # noqa
    '',

    '':
    '',

    '## line_joints property API':
    '',

    '<!-- Docstring: apysc._display.line_style_interface.LineStyleInterface.line_joints -->\n\n<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>\n\n**[Interface summary]** Get current line joints (vertices) style setting.<hr>\n\n**[Returns]**\n\n- `line_joints`: String\n  - Current line joints (vertices) style setting.\n\n<hr>\n\n**[Examples]**':  # noqa
    '',

    '```py\n>>> import apysc as ap\n>>> stage: ap.Stage = ap.Stage()\n>>> sprite: ap.Sprite = ap.Sprite()\n>>> sprite.graphics.line_style(\n...     color=\'#fff\', thickness=5,\n...     joints=ap.LineJoints.ROUND)\n>>> sprite.graphics.line_joints\nString(\'round\')\n```':  # noqa
    '',

    '':
    '',

    '## line_dot_setting property API':
    '',

    '<!-- Docstring: apysc._display.line_style_interface.LineStyleInterface.line_dot_setting -->\n\n<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>\n\n**[Interface summary]** Get current line dot setting.<hr>\n\n**[Returns]**\n\n- `line_dot_setting`: LineDotSetting or None\n  - Current line dot setting.\n\n<hr>\n\n**[Examples]**':  # noqa
    '',

    '```py\n>>> import apysc as ap\n>>> stage: ap.Stage = ap.Stage()\n>>> sprite: ap.Sprite = ap.Sprite()\n>>> sprite.graphics.line_style(\n...     color=\'#fff\', thickness=5,\n...     dot_setting=ap.LineDotSetting(dot_size=5))\n>>> sprite.graphics.line_dot_setting.dot_size\nInt(5)\n```':  # noqa
    '',

    '':
    '',

    '## line_dash_setting property API':
    '',

    '<!-- Docstring: apysc._display.line_style_interface.LineStyleInterface.line_dash_setting -->\n\n<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>\n\n**[Interface summary]** Get current line dash setting.<hr>\n\n**[Returns]**\n\n- `line_dash_setting`: LineDashSetting or None\n  - Current line dash setting.\n\n<hr>\n\n**[Examples]**':  # noqa
    '',

    '```py\n>>> import apysc as ap\n>>> stage: ap.Stage = ap.Stage()\n>>> sprite: ap.Sprite = ap.Sprite()\n>>> sprite.graphics.line_style(\n...     color=\'#fff\', thickness=5,\n...     dash_setting=ap.LineDashSetting(\n...         dash_size=10, space_size=5))\n>>> sprite.graphics.line_dash_setting.dash_size\nInt(10)\n\n>>> sprite.graphics.line_dash_setting.space_size\nInt(5)\n```':  # noqa
    '',

    '':
    '',

    '## line_round_dot_setting property API':
    '',

    '<!-- Docstring: apysc._display.line_style_interface.LineStyleInterface.line_round_dot_setting -->\n\n<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>\n\n**[Interface summary]** Get current line round dot setting.<hr>\n\n**[Returns]**\n\n- `line_round_dot_setting`: LineRoundDotSetting or None\n  - Current line round dot setting.\n\n<hr>\n\n**[Examples]**':  # noqa
    '',

    '```py\n>>> import apysc as ap\n>>> stage: ap.Stage = ap.Stage()\n>>> sprite: ap.Sprite = ap.Sprite()\n>>> sprite.graphics.line_style(\n...     color=\'#fff\', thickness=5,\n...     round_dot_setting=ap.LineRoundDotSetting(\n...         round_size=6, space_size=3))\n>>> sprite.graphics.line_round_dot_setting.round_size\nInt(6)\n\n>>> sprite.graphics.line_round_dot_setting.space_size\nInt(3)\n```':  # noqa
    '',

    '':
    '',

    '## line_dash_dot_setting property API':
    '',

    '<!-- Docstring: apysc._display.line_style_interface.LineStyleInterface.line_dash_dot_setting -->\n\n<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>\n\n**[Interface summary]** Get current line dash dot setting.<hr>\n\n**[Returns]**\n\n- `line_dash_dot_setting`: LineDashDotSetting or None\n  - Current line dash dot setting.\n\n<hr>\n\n**[Examples]**':  # noqa
    '',

    '```py\n>>> import apysc as ap\n>>> stage: ap.Stage = ap.Stage()\n>>> sprite: ap.Sprite = ap.Sprite()\n>>> sprite.graphics.line_style(\n...     color=\'#fff\', thickness=5,\n...     dash_dot_setting=ap.LineDashDotSetting(\n...         dot_size=2, dash_size=5, space_size=3))\n>>> sprite.graphics.line_dash_dot_setting.dot_size\nInt(2)\n\n>>> sprite.graphics.line_dash_dot_setting.dash_size\nInt(5)\n\n>>> sprite.graphics.line_dash_dot_setting.space_size\nInt(3)\n```':  # noqa
    '',

}
