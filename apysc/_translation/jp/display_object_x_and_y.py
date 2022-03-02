"""This module is for the translation mapping data of the
following document:

Document file: display_object_x_and_y.md
Language: jp
"""

from typing import Dict

MAPPING: Dict[str, str] = {

    '# Display object x and y interfaces':
    '',

    'This page explains the `DisplayObject` class x and y property interfaces.':  # noqa
    '',

    '## What interfaces are these?':
    '',

    'The x and y properties change the `DisplayObject` instance 2-dimensional coordinates.':  # noqa
    '',

    '## Basic usage':
    '',

    'Each `DisplayObject` instance has the x and y properties and can get/set the value with it.':  # noqa
    '',

    '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    background_color=\'#333\',\n    stage_width=150,\n    stage_height=150,\n    stage_elem_id=\'stage\')\n\nsprite: ap.Sprite = ap.Sprite()\nsprite.graphics.begin_fill(color=\'#0af\')\nrectangle: ap.Rectangle = sprite.graphics.draw_rect(\n    x=0, y=0, width=50, height=50)\n\n# Update the x and y coordinates from 0 to 50.\nrectangle.x = ap.Int(50)\nrectangle.y = ap.Int(50)\n\nap.save_overall_html(\n    dest_dir_path=\'display_object_x_and_y_basic_usage/\')\n```':  # noqa
    '',

    '<iframe src="static/display_object_x_and_y_basic_usage/index.html" width="150" height="150"></iframe>':  # noqa
    '',

    '## Augmented assignment':
    '',

    'The x and y properties support the Augmented assignments, like the `+=`\\, `-=`\\, `/=`\\, and `*=` operators.\n\nThe following example appends 10-pixel to the y-coordinate when you click the rectangle.':  # noqa
    '',

    '```py\n# runnable\nimport apysc as ap\n\n\ndef on_click(e: ap.MouseEvent[ap.Rectangle], options: dict) -> None:\n    """\n    The handler that the rectangle calls when clicked.\n\n    Parameters\n    ----------\n    e : MouseEvent\n        Event instance.\n    options : dict\n        Optional arguments dictionary.\n    """\n    rectangle: ap.Rectangle = e.this\n    rectangle.y += 10\n\n\nap.Stage(\n    background_color=\'#333\',\n    stage_width=150,\n    stage_height=150,\n    stage_elem_id=\'stage\')\n\nsprite: ap.Sprite = ap.Sprite()\nsprite.graphics.begin_fill(color=\'#0af\')\nrectangle: ap.Rectangle = sprite.graphics.draw_rect(\n    x=50, y=50, width=50, height=50)\nrectangle.click(on_click)\n\nap.save_overall_html(\n    dest_dir_path=\'display_object_x_and_y_augmented_assignment/\')\n```':  # noqa
    '',

    '<iframe src="static/display_object_x_and_y_augmented_assignment/index.html" width="150" height="150"></iframe>':  # noqa
    '',

    '## x property API':
    '',

    '<!-- Docstring: apysc._display.x_interface.XInterface.x -->\n\n<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>\n\n**[Interface summary]** Get a x-coordinate.<hr>\n\n**[Returns]**\n\n- `x`: Int\n  - X-coordinate.\n\n<hr>\n\n**[Examples]**':  # noqa
    '',

    '```py\n>>> import apysc as ap\n>>> stage: ap.Stage = ap.Stage()\n>>> sprite: ap.Sprite = ap.Sprite()\n>>> sprite.graphics.begin_fill(color=\'#0af\')\n>>> rectangle: ap.Rectangle = sprite.graphics.draw_rect(\n...     x=50, y=50, width=50, height=50)\n>>> rectangle.x = ap.Int(100)\n>>> rectangle.x\nInt(100)\n```':  # noqa
    '',

    '':
    '',

    '## y property API':
    '',

    '<!-- Docstring: apysc._display.y_interface.YInterface.y -->\n\n<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>\n\n**[Interface summary]** Get a y-coordinate.<hr>\n\n**[Returns]**\n\n- `y`: Int\n  - Y-coordinate.\n\n<hr>\n\n**[Examples]**':  # noqa
    '',

    '```py\n>>> import apysc as ap\n>>> stage: ap.Stage = ap.Stage()\n>>> sprite: ap.Sprite = ap.Sprite()\n>>> sprite.graphics.begin_fill(color=\'#0af\')\n>>> rectangle: ap.Rectangle = sprite.graphics.draw_rect(\n...     x=50, y=50, width=50, height=50)\n>>> rectangle.y = ap.Int(100)\n>>> rectangle.y\nInt(100)\n```':  # noqa
    '',

}
