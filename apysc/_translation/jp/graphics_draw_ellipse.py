"""This module is for the translation mapping data of the
following document:

Document file: graphics_draw_ellipse.md
Language: jp
"""

from typing import Dict

MAPPING: Dict[str, str] = {

    '# Graphics draw_ellipse interface':
    '',

    'This page explains the `Graphics` class `draw_ellipse` method interface.':  # noqa
    '',

    '## What interface is this?':
    '',

    'The `draw_ellipse` interface draws the vector ellipse graphics.':
    '',

    '## Basic usage':
    '',

    'The `draw_ellipse` interface has the `x`\\, `y`\\, `width`\\, and `height` arguments. The `x` and `y` arguments are the ellipse center coordinates. The `width` and `height` arguments are the ellipse size. These sizes are twice the size of the radius.':  # noqa
    '',

    '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    background_color=\'#333\',\n    stage_width=325,\n    stage_height=200,\n    stage_elem_id=\'stage\')\n\nsprite: ap.Sprite = ap.Sprite()\n\n# Set the cyan fill color and draw the ellipse.\nsprite.graphics.begin_fill(color=\'#0af\')\nsprite.graphics.draw_ellipse(x=125, y=100, width=150, height=100)\n\n# Set the only dotted-line style and draw the ellipse.\nsprite.graphics.begin_fill(color=\'\')\nsprite.graphics.line_style(\n    color=\'#fff\', thickness=3, dot_setting=ap.LineDotSetting(dot_size=3))\nsprite.graphics.draw_ellipse(x=200, y=100, width=150, height=100)\n\nap.save_overall_html(\n    dest_dir_path=\'graphics_draw_ellipse_basic_usage/\')\n```':  # noqa
    '',

    '<iframe src="static/graphics_draw_ellipse_basic_usage/index.html" width="325" height="200"></iframe>':  # noqa
    '',

    '## Return value':
    '',

    'The return value of the `draw_ellipse` interface is the instance of the `Ellipse` class.\n\nIt has the basic interfaces (like the `x` or the `width` attributes) similar to the other graphics classes.\n\nThe following code example binds the click event handler. If you click the ellipse, the width and height become wider.':  # noqa
    '',

    '```py\n# runnable\nimport apysc as ap\n\n\ndef on_ellipse_click(\n        e: ap.MouseEvent[ap.Ellipse], options: dict) -> None:\n    """\n    The handler that the ellipse calls when clicked.\n\n    Parameters\n    ----------\n    e : MouseEvent\n        Event instance.\n    options : dict\n        Optional arguments dictionary.\n    """\n    ellipse: ap.Ellipse = e.this\n    ellipse.width += 15\n    ellipse.height += 10\n\n\nap.Stage(\n    background_color=\'#333\',\n    stage_width=250,\n    stage_height=200,\n    stage_elem_id=\'stage\')\n\nsprite: ap.Sprite = ap.Sprite()\n\nsprite.graphics.begin_fill(color=\'#0af\')\nellipse: ap.Ellipse = sprite.graphics.draw_ellipse(\n    x=125, y=100, width=150, height=100)\nellipse.click(on_ellipse_click)\n\nap.save_overall_html(\n    dest_dir_path=\'graphics_draw_ellipse_return_value/\')\n```':  # noqa
    '',

    '<iframe src="static/graphics_draw_ellipse_return_value/index.html" width="250" height="200"></iframe>':  # noqa
    '',

    '## draw_ellipse API':
    '',

    '<!-- Docstring: apysc._display.graphics.Graphics.draw_ellipse -->\n\n<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>\n\n**[Interface signature]** `draw_ellipse(self, x:Union[int, apysc._type.int.Int], y:Union[int, apysc._type.int.Int], width:Union[int, apysc._type.int.Int], height:Union[int, apysc._type.int.Int]) -> \'_ellipse.Ellipse\'`<hr>\n\n**[Interface summary]** Draw an ellipse vector graphic.<hr>\n\n**[Parameters]**\n\n- `x`: Int or int\n  - X-coordinate of the ellipse center.\n- `y`: Int or int\n  - Y-coordinate of the ellipse center.\n- `width`: Int or int\n  - Ellipse width.\n- `height`: Int or int\n  - Ellipse height.\n\n<hr>\n\n**[Returns]**\n\n- `ellipse`: Ellipse\n  - Created ellipse graphics instance.\n\n<hr>\n\n**[Examples]**':  # noqa
    '',

    '```py\n>>> import apysc as ap\n>>> stage: ap.Stage = ap.Stage()\n>>> sprite: ap.Sprite = ap.Sprite()\n>>> sprite.graphics.begin_fill(color=\'#0af\')\n>>> ellipse: ap.Ellipse = sprite.graphics.draw_ellipse(\n...     x=100, y=100, width=100, height=50)\n>>> ellipse.x\nInt(100)\n\n>>> ellipse.y\nInt(100)\n\n>>> ellipse.width\nInt(100)\n\n>>> ellipse.height\nInt(50)\n\n>>> ellipse.fill_color\nString(\'#00aaff\')\n```':  # noqa
    '',

}
