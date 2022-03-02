"""This module is for the translation mapping data of the
following document:

Document file: graphics_begin_fill.md
Language: jp
"""

from typing import Dict

MAPPING: Dict[str, str] = {

    '# Graphics begin_fill interface':
    '',

    'This page explains the `Graphics` class `begin_fill` method interface.':  # noqa
    '',

    '## What interface is this?':
    '',

    '`begin_fill` interface would set the fill color and fill alpha settings. This setting would be maintained until it is called again or called the `clear` method.':  # noqa
    '',

    '## Basic usage':
    '',

    'Draw vector graphics interfaces (e.g., `draw_rect`) would use these fill settings when creating, so the `begin_fill` method needs to be called before calling each drawing interface.':  # noqa
    '',

    '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    background_color=\'#333\',\n    stage_width=350,\n    stage_height=150,\n    stage_elem_id=\'stage\')\nsprite: ap.Sprite = ap.Sprite()\n\n# Set blue fill color and draw the first rectangle.\nsprite.graphics.begin_fill(color=\'#0af\')\nsprite.graphics.draw_rect(\n    x=50, y=50, width=50, height=50)\n\n# Draw the second rectangle (fill color setting will be maintained).\nsprite.graphics.draw_rect(\n    x=150, y=50, width=50, height=50)\n\n# Set the other fill color and draw the third rectangle.\nsprite.graphics.begin_fill(color=\'#f0a\')\nsprite.graphics.draw_rect(\n    x=250, y=50, width=50, height=50)\n\nap.save_overall_html(\n    dest_dir_path=\'graphics_begin_fill_basic_usage/\')\n```':  # noqa
    '',

    '<iframe src="static/graphics_begin_fill_basic_usage/index.html" width="350" height="150"></iframe>':  # noqa
    '',

    '## Fill color setting':
    '',

    'The `color` argument sets the fill color, and the `begin_fill` interface requires this argument.':  # noqa
    '',

    '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    background_color=\'#333\',\n    stage_width=150,\n    stage_height=150,\n    stage_elem_id=\'stage\')\nsprite: ap.Sprite = ap.Sprite()\n\n# Set a cyan fill color and draw the rectangle.\nsprite.graphics.begin_fill(color=\'#0af\')\nsprite.graphics.draw_rect(x=50, y=50, width=50, height=50)\n\nap.save_overall_html(\n    dest_dir_path=\'graphics_begin_fill_fill_color/\')\n```':  # noqa
    '',

    '<iframe src="static/graphics_begin_fill_fill_color/index.html" width="150" height="150"></iframe>\n\nIf you want to clear fill color, specify a blank string to this argument.\n\nFor example, since the following code clears fill color settings, a rectangle graphic becomes invisible.':  # noqa
    '',

    '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    background_color=\'#333\',\n    stage_width=150,\n    stage_height=150,\n    stage_elem_id=\'stage\')\nsprite: ap.Sprite = ap.Sprite()\n\nsprite.graphics.begin_fill(color=\'#0af\')\n\n# Clear fill color by specifying blank string.\nsprite.graphics.begin_fill(color=\'\')\n\n# Since fill color is not set, the rectangle is invisible.\nsprite.graphics.draw_rect(\n    x=50, y=50, width=50, height=50)\n\nap.save_overall_html(\n    dest_dir_path=\'graphics_begin_fill_color_setting_clear/\')\n```':  # noqa
    '',

    '<iframe src="static/graphics_begin_fill_color_setting_clear/index.html" width="150" height="150"></iframe>\n\nColor code is acceptable like the following list:\n\n- Six characters, e.g., `#00aaff`.\n- Three characters, e.g., `#0af` (this becomes `#00aaff`).\n- Single character, e.g., `#5` (this becomes `#000005`).\n- Skipped `#` symbol, e.g., `0af` (this becomes `#00aaff`).\n- Blank string, e.g., `\'\'` (this setting clears the fill color setting).':  # noqa
    '',

    '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    background_color=\'#333\',\n    stage_width=450,\n    stage_height=150,\n    stage_elem_id=\'stage\')\nsprite: ap.Sprite = ap.Sprite()\n\n# Six characters fill color setting (a cyan color).\nsprite.graphics.begin_fill(color=\'#00aaff\')\nsprite.graphics.draw_rect(\n    x=50, y=50, width=50, height=50)\n\n# Three characters fill color setting (a magenta color).\nsprite.graphics.begin_fill(color=\'#f0a\')\nsprite.graphics.draw_rect(\n    x=150, y=50, width=50, height=50)\n\n# Single characters fill color setting (a black color).\nsprite.graphics.begin_fill(color=\'#0\')\nsprite.graphics.draw_rect(\n    x=250, y=50, width=50, height=50)\n\n# Fill color that Skipped `#` symbol is also acceptable.\nsprite.graphics.begin_fill(color=\'999\')\nsprite.graphics.draw_rect(\n    x=350, y=50, width=50, height=50)\n\nap.save_overall_html(\n    dest_dir_path=\'graphics_begin_fill_acceptable_color_settings/\')\n```':  # noqa
    '',

    '<iframe src="static/graphics_begin_fill_acceptable_color_settings/index.html" width="450" height="150"></iframe>':  # noqa
    '',

    '## Fill color alpha (opacity) setting':
    '',

    'Fill color alpha (opacity) can be set by the `alpha` argument. It can accept 0.0 (transparent) to 1.0 (opaque).':  # noqa
    '',

    '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    background_color=\'#333\',\n    stage_width=200,\n    stage_height=200,\n    stage_elem_id=\'stage\')\nsprite: ap.Sprite = ap.Sprite()\n\nsprite.graphics.begin_fill(color=\'#00aaff\', alpha=0.2)\nsprite.graphics.draw_rect(\n    x=50, y=75, width=50, height=50)\nsprite.graphics.draw_rect(\n    x=75, y=50, width=50, height=50)\nsprite.graphics.draw_rect(\n    x=75, y=75, width=50, height=50)\nsprite.graphics.draw_rect(\n    x=75, y=100, width=50, height=50)\nsprite.graphics.draw_rect(\n    x=100, y=75, width=50, height=50)\n\nap.save_overall_html(\n    dest_dir_path=\'graphics_begin_fill_alpha_setting/\')\n```':  # noqa
    '',

    '<iframe src="static/graphics_begin_fill_alpha_setting/index.html" width="200" height="200"></iframe>':  # noqa
    '',

    '## begin_fill API':
    '',

    '<!-- Docstring: apysc._display.begin_fill_interface.BeginFillInterface.begin_fill -->\n\n<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>\n\n**[Interface signature]** `begin_fill(self, color:~StrOrString, *, alpha:Union[float, apysc._type.number.Number]=1.0) -> None`<hr>\n\n**[Interface summary]** Set single color value for fill.<hr>\n\n**[Parameters]**\n\n- `color`: str or String\n  - Hexadecimal color string. e.g., \'#00aaff\'\n- `alpha`: float or Number, default 1.0\n  - Color opacity (0.0 to 1.0).\n\n<hr>\n\n**[Examples]**':  # noqa
    '',

    '```py\n>>> import apysc as ap\n>>> stage: ap.Stage = ap.Stage()\n>>> sprite: ap.Sprite = ap.Sprite()\n>>> sprite.graphics.begin_fill(color=\'#0af\')\n>>> rectangle: ap.Rectangle = sprite.graphics.draw_rect(\n...     x=50, y=50, width=50, height=50)\n>>> rectangle.fill_color\nString(\'#00aaff\')\n```':  # noqa
    '',

    '':
    '',

    '## fill_color property API':
    '',

    '<!-- Docstring: apysc._display.begin_fill_interface.BeginFillInterface.fill_color -->\n\n<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>\n\n**[Interface summary]** Get current fill color.<hr>\n\n**[Returns]**\n\n- `fill_color`: String\n  - Current fill color (hexadecimal string, e.g., \'#00aaff\'). If not be set, this interface returns a blank string.\n\n<hr>\n\n**[Examples]**':  # noqa
    '',

    '```py\n>>> import apysc as ap\n>>> stage: ap.Stage = ap.Stage()\n>>> sprite: ap.Sprite = ap.Sprite()\n>>> sprite.graphics.begin_fill(color=\'#0af\')\n>>> rectangle: ap.Rectangle = sprite.graphics.draw_rect(\n...     x=50, y=50, width=50, height=50)\n>>> rectangle.fill_color\nString(\'#00aaff\')\n```':  # noqa
    '',

    '':
    '',

    '## fill_alpha property API':
    '',

    '<!-- Docstring: apysc._display.begin_fill_interface.BeginFillInterface.fill_alpha -->\n\n<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>\n\n**[Interface summary]** Get current fill color opacity.<hr>\n\n**[Returns]**\n\n- `fill_alpha`: Number\n  - Current fill color opacity (0.0 to 1.0). If not be set, 1.0 will be returned.\n\n<hr>\n\n**[Examples]**':  # noqa
    '',

    '```py\n>>> import apysc as ap\n>>> stage: ap.Stage = ap.Stage()\n>>> sprite: ap.Sprite = ap.Sprite()\n>>> sprite.graphics.begin_fill(color=\'#0af\', alpha=0.5)\n>>> rectangle: ap.Rectangle = sprite.graphics.draw_rect(\n...     x=50, y=50, width=50, height=50)\n>>> rectangle.fill_alpha\nNumber(0.5)\n```':  # noqa
    '',

}
