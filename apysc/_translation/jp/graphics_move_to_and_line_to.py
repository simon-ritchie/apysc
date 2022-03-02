"""This module is for the translation mapping data of the
following document:

Document file: graphics_move_to_and_line_to.md
Language: jp
"""

from typing import Dict

MAPPING: Dict[str, str] = {

    '# Graphics move_to and line_to interfaces':
    '',

    'This page explains the `Graphics` class `move_to` and `line_to` method interfaces.':  # noqa
    '',

    '## What interfaces are they?':
    '',

    'The `move_to` interface sets the line start point. The `line_to` draws the line from a current point to a destination point. Sequentially, if you call the `line_to` interface, the line becomes polyline.\n\nIf you call the `move_to` interface after the calling of `line_to`\\, it creates a new line instance.':  # noqa
    '',

    '## Basic usage':
    '',

    'The `move_to` and `line_to` interfaces have x and y arguments.':
    '',

    '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    background_color=\'#333\',\n    stage_width=300,\n    stage_height=100,\n    stage_elem_id=\'stage\')\nsprite: ap.Sprite = ap.Sprite()\n\nsprite.graphics.line_style(color=\'#0af\', thickness=5)\n\n# Move to x=50, y=50 point (no drawing).\nsprite.graphics.move_to(x=50, y=50)\n\n# Draw the line from the current point (50, 50) to the\n# destination point (250, 50).\nsprite.graphics.line_to(x=250, y=50)\n\nap.save_overall_html(\n    dest_dir_path=\'graphics_move_to_and_line_to_basic_usage/\')\n```':  # noqa
    '',

    '<iframe src="static/graphics_move_to_and_line_to_basic_usage/index.html" width="300" height="100"></iframe>':  # noqa
    '',

    '## Sequential calling of the line_to interface':
    '',

    'Sequentially, if you call the `line_to` interface, the result line becomes the polyline.':  # noqa
    '',

    '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    background_color=\'#333\',\n    stage_width=200,\n    stage_height=200,\n    stage_elem_id=\'stage\')\nsprite: ap.Sprite = ap.Sprite()\n\nsprite.graphics.line_style(color=\'#0af\', thickness=5)\n\n# Move to x=50, y=50 point (no drawing).\nsprite.graphics.move_to(x=50, y=50)\n\n# Draw the line from the current point (50, 50) to the\n# destination point (150, 50).\nsprite.graphics.line_to(x=150, y=50)\n\n# Draw the line from the current point (250, 50) to the\n# destination point (50, 150). This calling changes the line\n# to the polyline.\nsprite.graphics.line_to(x=50, y=150)\n\n# Finally the polyline becomes Z shape by drawing to\n# destination point (150, 150).\nsprite.graphics.line_to(x=150, y=150)\n\nap.save_overall_html(\n    dest_dir_path=\'graphics_move_to_and_line_to_sequential_calling/\')\n```':  # noqa
    '',

    '<iframe src="static/graphics_move_to_and_line_to_sequential_calling/index.html" width="200" height="200"></iframe>':  # noqa
    '',

    '## move_to interface calling after line_to interface calling':
    '',

    'If you call the `move_to` interface after calling the `line_to` interface, it creates a new line instance.':  # noqa
    '',

    '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    background_color=\'#333\',\n    stage_width=250,\n    stage_height=150,\n    stage_elem_id=\'stage\')\nsprite: ap.Sprite = ap.Sprite()\n\nsprite.graphics.line_style(color=\'#0af\', thickness=5)\n\n# First move_to interface calling.\nsprite.graphics.move_to(x=50, y=50)\nsprite.graphics.line_to(x=100, y=50)\nsprite.graphics.line_to(x=50, y=100)\nsprite.graphics.line_to(x=100, y=100)\n\n# Second move_to interface calling. This will create a new\n# polyline instance.\nsprite.graphics.move_to(x=150, y=50)\nsprite.graphics.line_to(x=200, y=50)\nsprite.graphics.line_to(x=150, y=100)\nsprite.graphics.line_to(x=200, y=100)\n\nap.save_overall_html(\n    dest_dir_path=\'graphics_move_to_and_line_to_multi_move_to_calling/\')\n```':  # noqa
    '',

    '<iframe src="static/graphics_move_to_and_line_to_multi_move_to_calling/index.html" width="250" height="150"></iframe>':  # noqa
    '',

    '## Polyline instance':
    '',

    '`move_to` and `line_to` interfaces will return `Polyline` instance. You can update each setting or bind events to that instance.\n\nFor instance, the following script sets the mouse event to `Polyline`\\, updates the line color, and sets dot style in the handler (`on_line_click`).':  # noqa
    '',

    '```py\n# runnable\nimport apysc as ap\n\n\ndef on_line_click(\n        e: ap.MouseEvent[ap.Polyline], options: dict) -> None:\n    """\n    The handler that the line instance calls when clicked.\n\n    Parameters\n    ----------\n    e : MouseEvent\n        The event instance.\n    options : dict\n        Optional arguments.\n    """\n    polyline: ap.Polyline = e.this\n    polyline.line_color = ap.String(\'#f0a\')\n    polyline.line_dot_setting = ap.LineDotSetting(dot_size=5)\n\n\nap.Stage(\n    background_color=\'#333\',\n    stage_width=200,\n    stage_height=100,\n    stage_elem_id=\'stage\')\nsprite: ap.Sprite = ap.Sprite()\n\nsprite.graphics.line_style(color=\'#0af\', thickness=30)\npolyline: ap.Polyline = sprite.graphics.move_to(x=50, y=50)\nsprite.graphics.line_to(x=150, y=50)\npolyline.click(on_line_click)\n\nap.save_overall_html(\n    dest_dir_path=\'graphics_move_to_and_line_to_polyline/\')\n```':  # noqa
    '',

    'If you click the following line, line style will be updated:\n\n<iframe src="static/graphics_move_to_and_line_to_polyline/index.html" width="200" height="100"></iframe>':  # noqa
    '',

    '## move_to API':
    '',

    '<!-- Docstring: apysc._display.graphics.Graphics.move_to -->\n\n<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>\n\n**[Interface signature]** `move_to(self, x:Union[int, apysc._type.int.Int], y:Union[int, apysc._type.int.Int]) -> \'_polyline.Polyline\'`<hr>\n\n**[Interface summary]** Move a line position to a specified point.<hr>\n\n**[Parameters]**\n\n- `x`: Int or int\n  - X destination point to move.\n- `y`: Int or int\n  - Y destination point to move.\n\n<hr>\n\n**[Returns]**\n\n- `line`: Polyline\n  - Line graphics instance.\n\n<hr>\n\n**[Examples]**':  # noqa
    '',

    '```py\n>>> import apysc as ap\n>>> stage: ap.Stage = ap.Stage()\n>>> sprite: ap.Sprite = ap.Sprite()\n>>> sprite.graphics.line_style(color=\'#fff\', thickness=5)\n>>> line_1: ap.Polyline = sprite.graphics.move_to(x=50, y=50)\n>>> line_2: ap.Polyline = sprite.graphics.line_to(x=150, y=50)\n>>> line_1 == line_2\nTrue\n\n>>> line_1.line_color\nString(\'#ffffff\')\n\n>>> line_1.line_thickness\nInt(5)\n```':  # noqa
    '',

    '':
    '',

    '## line_to API':
    '',

    '<!-- Docstring: apysc._display.graphics.Graphics.line_to -->\n\n<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>\n\n**[Interface signature]** `line_to(self, x:Union[int, apysc._type.int.Int], y:Union[int, apysc._type.int.Int]) -> \'_polyline.Polyline\'`<hr>\n\n**[Interface summary]** Draw a line from previous point to specified point (initial point is x = 0, y = 0).<hr>\n\n**[Parameters]**\n\n- `x`: Int or int\n  - X destination point to draw a line.\n- `y`: Int or int\n  - Y destination point to draw a line.\n\n<hr>\n\n**[Returns]**\n\n- `line`: Polyline\n  - Line graphics instance.\n\n<hr>\n\n**[Examples]**':  # noqa
    '',

    '```py\n>>> import apysc as ap\n>>> stage: ap.Stage = ap.Stage()\n>>> sprite: ap.Sprite = ap.Sprite()\n>>> sprite.graphics.line_style(color=\'#fff\', thickness=5)\n>>> line_1: ap.Polyline = sprite.graphics.move_to(x=50, y=50)\n>>> line_2: ap.Polyline = sprite.graphics.line_to(x=150, y=50)\n>>> line_3: ap.Polyline = sprite.graphics.line_to(x=50, y=150)\n>>> line_1 == line_2 == line_3\nTrue\n\n>>> line_1.line_color\nString(\'#ffffff\')\n\n>>> line_1.line_thickness\nInt(5)\n```':  # noqa
    '',

}
