"""This module is for the translation mapping data of the
following document:

Document file: display_object_mouse_event.md
Language: jp
"""

from typing import Dict

MAPPING: Dict[str, str] = {

    '# Display object mouse event binding interfaces':
    '',

    'This page explains the `DisplayObject` class mouse event binding interfaces.':  # noqa
    '',

    '## What interfaces are these?':
    '',

    'Each `DisplayObject` instance has the mouse event binding interfaces, like the click, mouse over, mouse move.\n\nThese interfaces can bind the mouse event to a `DisplayObject` instance. So, for instance, you can assign any function to handle when a `DisplayObject` instance click.':  # noqa
    '',

    '## Basic usage':
    '',

    'You can bind event handler (callable) with each interface, like the `click`\\, `mouseover`\\.\n\nThe following example binds the click event handler, and if you click the rectangle, the fill color is changed.':  # noqa
    '',

    '```py\n# runnable\nimport apysc as ap\n\n\ndef on_click(\n        e: ap.MouseEvent[ap.Rectangle], options: dict) -> None:\n    """\n    The handler that the rectangle calls when clicked.\n\n    Parameters\n    ----------\n    e : MouseEvent\n        Event instance.\n    options : dict\n        Optional arguments dictionary.\n    """\n    rectangle: ap.Rectangle = e.this\n    rectangle.fill_color = ap.String(\'#f0a\')\n\n\nap.Stage(\n    background_color=\'#333\',\n    stage_width=150,\n    stage_height=150,\n    stage_elem_id=\'stage\')\n\nsprite: ap.Sprite = ap.Sprite()\nsprite.graphics.begin_fill(color=\'#0af\')\nrectangle: ap.Rectangle = sprite.graphics.draw_rect(\n    x=50, y=50, width=50, height=50)\nrectangle.click(on_click)\n\nap.save_overall_html(\n    dest_dir_path=\'display_object_mouse_event_basic_usage/\')\n```':  # noqa
    '',

    '<iframe src="static/display_object_mouse_event_basic_usage/index.html" width="150" height="150"></iframe>':  # noqa
    '',

    '## See also':
    '',

    'For more details, please see the following pages:\n\n- [Basic mouse event interfaces](mouse_event_basic.md)\n- [Click interface](click.md)\n- [Mousedown and mouseup interfaces](mousedown_and_mouseup.md)\n- [Mouseover and mouseout interfaces](mouseover_and_mouseout.md)\n- [Mousemove interface](mousemove.md)':  # noqa
    '',

}
