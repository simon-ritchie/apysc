"""This module is for the translation mapping data of the
following document:

Document file: graphics_draw_round_rect.md
Language: jp
"""

from typing import Dict

MAPPING: Dict[str, str] = {

    '# Graphics draw_round_rect interface':
    '',

    'This page explains the `Graphics` class `draw_round_rect` method interface.':  # noqa
    '',

    '## What interface is this?':
    '',

    '`draw_round_rect` interface draws vector rounded rectangle graphics.':
    '',

    '## Basic usage':
    '',

    '`draw_rect` interface has `x`, `y`, `width`, and `height` arguments. `x` and `y` are rectangle coordinates setting, and `width` and `height` will determine rectangle size.\n\nThis interface also has `ellipse_width` and `ellipse_height` arguments to set the round size to the rectangle corners.':  # noqa
    '',

    '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    background_color=\'#333\',\n    stage_width=350,\n    stage_height=150,\n    stage_elem_id=\'stage\')\n\nsprite: ap.Sprite = ap.Sprite()\nsprite.graphics.begin_fill(color=\'#0af\')\n\n# Set 10-pixel ellipse size and draw the rectangle.\nsprite.graphics.draw_round_rect(\n    x=50, y=50, width=50, height=50, ellipse_width=10, ellipse_height=10)\n\n# Set 20-pixel ellipse size and draw the rectangle.\nsprite.graphics.draw_round_rect(\n    x=150, y=50, width=50, height=50, ellipse_width=20, ellipse_height=20)\n\n# Set 5-pixel ellipse width and 20-pixel ellipse height and\n# draw the rectangle.\nsprite.graphics.draw_round_rect(\n    x=250, y=50, width=50, height=50, ellipse_width=5, ellipse_height=20)\n\nap.save_overall_html(\n    dest_dir_path=\'graphics_draw_round_rect_basic_usage/\')\n```':  # noqa
    '',

    '<iframe src="static/graphics_draw_round_rect_basic_usage/index.html" width="350" height="150"></iframe>':  # noqa
    '',

    '## Return value':
    '',

    '`draw_round_rect` interface will return the `Rectangle` instance, same as the `draw_rect` interface.\n\nThe `Rectangle` instance has the `ellipse_width` attribute and `ellipse_height` to change the rectangle round size.':  # noqa
    '',

    '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    background_color=\'#333\',\n    stage_width=150,\n    stage_height=150,\n    stage_elem_id=\'stage\')\n\nsprite: ap.Sprite = ap.Sprite()\nsprite.graphics.begin_fill(color=\'#0af\')\n\nrectangle: ap.Rectangle = sprite.graphics.draw_round_rect(\n    x=50, y=50, width=50, height=50, ellipse_width=10, ellipse_height=10)\n\n# You can update the ellipse_width and ellipse_height\n# attributes dynamically.\nrectangle.ellipse_width = ap.Int(20)\n\nap.save_overall_html(\n    dest_dir_path=\'graphics_draw_round_rect_return_value/\')\n```':  # noqa
    '',

    '<iframe src="static/graphics_draw_round_rect_return_value/index.html" width="150" height="150"></iframe>':  # noqa
    '',

    '## draw_round_rect API':
    '',

    '<!-- Docstring: apysc._display.graphics.Graphics.draw_round_rect -->\n\n<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>\n\n**[Interface signature]** `draw_round_rect(self, x:Union[int, apysc._type.int.Int], y:Union[int, apysc._type.int.Int], width:Union[int, apysc._type.int.Int], height:Union[int, apysc._type.int.Int], ellipse_width:Union[int, apysc._type.int.Int], ellipse_height:Union[int, apysc._type.int.Int]) -> apysc._display.rectangle.Rectangle`<hr>\n\n**[Interface summary]** Draw a rounded rectangle vector graphics.<hr>\n\n**[Parameters]**\n\n- `x`: Int or int\n  - X-coordinate to start drawing.\n- `y`: Int or int\n  - Y-coordinate to start drawing.\n- `width`: Int or int\n  - Rectangle width.\n- `height`: Int or int\n  - Rectangle height.\n- `ellipse_width`: Int or int\n  - Ellipse width of the rectangle corner.\n- `ellipse_height`: Int or int\n  - Ellipse height of the rectangle corner.\n\n<hr>\n\n**[Returns]**\n\n- `rectangle`: Rectangle\n  - Created rectangle.\n\n<hr>\n\n**[Examples]**':  # noqa
    '',

    '```py\n>>> import apysc as ap\n>>> stage: ap.Stage = ap.Stage()\n>>> sprite: ap.Sprite = ap.Sprite()\n>>> sprite.graphics.begin_fill(color=\'#0af\')\n>>> round_rect: ap.Rectangle = sprite.graphics.draw_round_rect(\n...     x=50, y=50, width=50, height=50,\n...     ellipse_width=10, ellipse_height=15)\n>>> round_rect.ellipse_width\nInt(10)\n\n>>> round_rect.ellipse_height\nInt(15)\n```':  # noqa
    '',

}
