"""This module is for the translation mapping data of the
following document:

Document file: mouse_event_abstract.md
Language: jp
"""

from typing import Dict

MAPPING: Dict[str, str] = {

    '# MouseEvent interfaces abstract':
    '',

    'This page explains the MouseEvent interfaces abstract.':
    '',

    '## What apysc can do in its interfaces':
    '',

    '- You can set the `MouseEvent` handlers, such as the click, mouse down, mouse over, and so on, to each graphic instance.\n- You can pass the optional arguments to the handler.':  # noqa
    '',

    '## Example of the click event':
    '',

    'To bind MouseEvent, defining the handler function (or method) would be necessary (e.g., `on_click`).\n\nThese handlers can bind with the click interface.':  # noqa
    '',

    '```py\n# runnable\nimport apysc as ap\n\n\ndef on_click(e: ap.MouseEvent[ap.Rectangle], options: dict) -> None:\n    """\n    The handler that the rectangle calls when clicked.\n\n    Parameters\n    ----------\n    e : ap.MouseEvent\n        Event instance.\n    options : dict\n        Optional arguments dictionary.\n    """\n    rectangle: ap.Rectangle = e.this\n    with ap.If(rectangle.fill_color == \'#00aaff\'):\n        rectangle.fill_color = ap.String(\'#f0a\')\n        ap.Return()\n\n    with ap.If(rectangle.fill_color == \'#ff00aa\'):\n        rectangle.fill_color = ap.String(\'#0af\')\n        ap.Return()\n\n\nap.Stage(\n    background_color=\'#333\',\n    stage_width=150,\n    stage_height=150,\n    stage_elem_id=\'stage\')\nsprite: ap.Sprite = ap.Sprite()\nsprite.graphics.begin_fill(color=\'#0af\')\nrectangle: ap.Rectangle = sprite.graphics.draw_rect(\n    x=50, y=50, width=50, height=50)\nrectangle.click(on_click)\n\nap.save_overall_html(\n    dest_dir_path=\'mouse_event_abstract_click/\')\n```':  # noqa
    '',

    '<iframe src="static/mouse_event_abstract_click/index.html" width="150" height="150"></iframe>':  # noqa
    '',

    '## See also':
    '',

    'There are a lot of other mouse event binding interfaces, such as the mouse down, mouse over, and mouse move. For more details, please see the following:\n\n- [Basic mouse event interfaces](mouse_event_basic.md)\n- [Click interface](click.md)\n- [Double click interface](dblclick.md)\n- [Mousedown and mouseup interfaces](mousedown_and_mouseup.md)\n- [Mouseover and mouseout interfaces](mouseover_and_mouseout.md)\n- [Mousemove interface](mousemove.md)':  # noqa
    '',

}
