"""This module is for the translation mapping data of the
following document:

Document file: graphics_draw_circle.md
Language: jp
"""

from typing import Dict

MAPPING: Dict[str, str] = {

    '# Graphics draw_circle interface':
    '',

    'This page explains the `Graphics` class `draw_circle` method interface.':  # noqa
    '',

    '## What interface is this?':
    '',

    '`draw_circle` interface draws the vector circle graphics.':
    '',

    '## Basic usage':
    '',

    'The `draw_circle` interface has the `x`\\, `y`\\, and `radius` arguments.\n\nThe `x` and `y` arguments are the circle center coordinates, and the radius argument determines the circle size. The width and height become twice the `radius` value.':  # noqa
    '',

    '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    background_color=\'#333\',\n    stage_width=350,\n    stage_height=200,\n    stage_elem_id=\'stage\')\n\nsprite: ap.Sprite = ap.Sprite()\n\n# Set the cyan color and draw the circle.\nsprite.graphics.begin_fill(color=\'#0af\')\nsprite.graphics.draw_circle(x=100, y=100, radius=50)\n\n# Set the dotted-line style and draw the circle.\nsprite.graphics.begin_fill(color=\'\')\nsprite.graphics.line_style(\n    color=\'#fff\', thickness=3, dot_setting=ap.LineDotSetting(dot_size=3))\nsprite.graphics.draw_circle(x=250, y=100, radius=50)\n\n# Draw the inner circle.\nsprite.graphics.draw_circle(x=250, y=100, radius=25)\n\nap.save_overall_html(\n    dest_dir_path=\'graphics_draw_circle_basic_usage/\')\n```':  # noqa
    '',

    '<iframe src="static/graphics_draw_circle_basic_usage/index.html" width="350" height="200"></iframe>':  # noqa
    '',

    '## Return value':
    '',

    'The return value of the `draw_circle` interface is the instance of the `Circle` class.\n\nIt has the `radius` attribute or other basic interfaces and you can change these settings.':  # noqa
    '',

    '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    background_color=\'#333\',\n    stage_width=400,\n    stage_height=400,\n    stage_elem_id=\'stage\')\n\nsprite: ap.Sprite = ap.Sprite()\n\n# Draw the small radius circle.\nsprite.graphics.begin_fill(color=\'#0af\')\ncircle: ap.Circle = sprite.graphics.draw_circle(x=200, y=200, radius=25)\n\n# Update circle radius to become the bigger one.\ncircle.radius = ap.Int(100)\n\nap.save_overall_html(\n    dest_dir_path=\'graphics_draw_circle_return_value/\')\n```':  # noqa
    '',

    '<iframe src="static/graphics_draw_circle_return_value/index.html" width="400" height="400"></iframe>':  # noqa
    '',

    '## draw_circle API':
    '',

    '<!-- Docstring: apysc._display.graphics.Graphics.draw_circle -->\n\n<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>\n\n**[Interface signature]** `draw_circle(self, x:Union[int, apysc._type.int.Int], y:Union[int, apysc._type.int.Int], radius:Union[int, apysc._type.int.Int]) -> \'_circle.Circle\'`<hr>\n\n**[Interface summary]** Draw a circle vector graphics.<hr>\n\n**[Parameters]**\n\n- `x`: Int or int\n  - X-coordinate of the circle center.\n- `y`: Int or int\n  - Y-coordinate of the circle center.\n- `radius`: Int or int\n  - Circle radius.\n\n<hr>\n\n**[Returns]**\n\n- `circle`: Circle\n  - Created circle graphics instance.\n\n<hr>\n\n**[Examples]**':  # noqa
    '',

    '```py\n>>> import apysc as ap\n>>> stage: ap.Stage = ap.Stage()\n>>> sprite: ap.Sprite = ap.Sprite()\n>>> sprite.graphics.begin_fill(color=\'#0af\')\n>>> circle: ap.Circle = sprite.graphics.draw_circle(\n...     x=100, y=100, radius=50)\n>>> circle.x\nInt(100)\n\n>>> circle.y\nInt(100)\n\n>>> circle.radius\nInt(50)\n\n>>> circle.fill_color\nString(\'#00aaff\')\n```':  # noqa
    '',

}
