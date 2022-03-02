"""This module is for the translation mapping data of the
following document:

Document file: graphics_draw_rect.md
Language: jp
"""

from typing import Dict

MAPPING: Dict[str, str] = {

    '# Graphics draw_rect interface':
    '',

    'This page explains the `Graphics` class `draw_rect` method interface.':
    '',

    '## What interface is this?':
    '',

    '`draw_rect` interface draws vector rectangle graphics.':
    '',

    '## Basic usage':
    '',

    '`draw_rect` interface has `x`, `y`, `width`, and `height` arguments. `x` and `y` are rectangle coordinates setting, and `width` and `height` will determine rectangle size.':  # noqa
    '',

    '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    background_color=\'#333\',\n    stage_width=200,\n    stage_height=150,\n    stage_elem_id=\'stage\')\nsprite: ap.Sprite = ap.Sprite()\nsprite.graphics.begin_fill(color=\'#0af\')\nsprite.graphics.draw_rect(x=50, y=50, width=100, height=50)\n\nap.save_overall_html(\n    dest_dir_path=\'graphics_draw_rect_basic_usage/\')\n```':  # noqa
    '',

    'The previous script draws horizontal rectangle graphics.\n\n<iframe src="static/graphics_draw_rect_basic_usage/index.html" width="200" height="150"></iframe>\n\nNotes: `begin_fill` call (fill color setting) is necessary before `draw_rect` interface call. If you skip it, it displays nothing on stage.':  # noqa
    '',

    '```py\n# runnable\nimport apysc as ap\n\nstage: ap.Stage = ap.Stage(\n    background_color=\'#333\',\n    stage_width=200,\n    stage_height=150,\n    stage_elem_id=\'stage\')\nsprite: ap.Sprite = ap.Sprite()\nsprite.graphics.draw_rect(x=50, y=50, width=100, height=50)\n\nap.save_overall_html(\n    dest_dir_path=\'graphics_draw_rect_basic_usage_skipped_begin_fill/\')\n```':  # noqa
    '',

    '<iframe src="static/graphics_draw_rect_basic_usage_skipped_begin_fill/index.html" width="200" height="150"></iframe>':  # noqa
    '',

    '## Rectangle instance':
    '',

    '`draw_rect` interface will return `Rectangle` instance. You can update each setting or bind events.\n\nFor instance, the following script sets the mouse event to `Rectangle` and updates x position in the handler (`on_click`).':  # noqa
    '',

    '```py\n# runnable\nimport apysc as ap\n\n\ndef on_click(e: ap.MouseEvent[ap.Rectangle], options: dict) -> None:\n    """\n    The handler that the rectangle calls when clicked.\n\n    Parameters\n    ----------\n    e : MouseEvent\n        Created event instance.\n    options : dict\n        Optional arguments.\n    """\n    rectangle: ap.Rectangle = e.this\n    rectangle.x = ap.Int(100)\n\n\nap.Stage(\n    background_color=\'#333\',\n    stage_width=200,\n    stage_height=150,\n    stage_elem_id=\'stage\')\nsprite: ap.Sprite = ap.Sprite()\n\nsprite.graphics.begin_fill(color=\'#0af\')\nrectangle: ap.Rectangle = sprite.graphics.draw_rect(\n    x=50, y=50, width=50, height=50)\nrectangle.click(on_click)\n\nap.save_overall_html(\n    dest_dir_path=\'graphics_draw_rect_rectangle/\')\n```':  # noqa
    '',

    'If you click rectangle, the handler changes the x position to 100.\n\n<iframe src="static/graphics_draw_rect_rectangle/index.html" width="200" height="150"></iframe>':  # noqa
    '',

    '## draw_rect API':
    '',

    '<!-- Docstring: apysc._display.graphics.Graphics.draw_rect -->\n\n<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>\n\n**[Interface signature]** `draw_rect(self, x:Union[int, apysc._type.int.Int], y:Union[int, apysc._type.int.Int], width:Union[int, apysc._type.int.Int], height:Union[int, apysc._type.int.Int]) -> apysc._display.rectangle.Rectangle`<hr>\n\n**[Interface summary]** Draw a rectangle vector graphics.<hr>\n\n**[Parameters]**\n\n- `x`: Int or int\n  - X position to start drawing.\n- `y`: Int or int\n  - Y position to start drawing.\n- `width`: Int or int\n  - Rectangle width.\n- `height`: Int or int\n  - Rectangle height.\n\n<hr>\n\n**[Returns]**\n\n- `rectangle`: Rectangle\n  - Created rectangle.\n\n<hr>\n\n**[Examples]**':  # noqa
    '',

    '```py\n>>> import apysc as ap\n>>> stage: ap.Stage = ap.Stage()\n>>> sprite: ap.Sprite = ap.Sprite()\n>>> sprite.graphics.begin_fill(color=\'#0af\')\n>>> rectangle: ap.Rectangle = sprite.graphics.draw_rect(\n...     x=50, y=50, width=50, height=50)\n>>> rectangle.x\nInt(50)\n\n>>> rectangle.width\nInt(50)\n\n>>> rectangle.fill_color\nString(\'#00aaff\')\n```':  # noqa
    '',

}
