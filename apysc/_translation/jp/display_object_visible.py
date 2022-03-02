"""This module is for the translation mapping data of the
following document:

Document file: display_object_visible.md
Language: jp
"""

from typing import Dict

MAPPING: Dict[str, str] = {

    '# Display object visible interface':
    '',

    'This page explains the `DisplayObject` class `visible` property interface.':  # noqa
    '',

    '## What interface is this?':
    '',

    'The `visible` property interface will change the `DisplayObject` visible / invisible state.':  # noqa
    '',

    '## Basic usage':
    '',

    'The `visible` property accepts a `Boolean` value. If you set the True value, a `DisplayObject` instance becomes visible (default). Conversely, if you set the False value, a `DisplayObject` instance becomes invisible.\n\nThe following example switches the visible values when you click the rectangle. For example, suppose you click the left rectangle (the rectangle_1). In that case, the left rectangle becomes invisible, and the right rectangle (rectangle_2) becomes visible.':  # noqa
    '',

    '```py\n# runnable\nfrom typing_extensions import TypedDict\n\nimport apysc as ap\n\n\nclass _RectOptions(TypedDict):\n    rectangle: ap.Rectangle\n\n\ndef on_rectangle_1_click(\n        e: ap.MouseEvent[ap.Rectangle], options: _RectOptions) -> None:\n    """\n    The handler that the first rectangle calls when clicked.\n\n    Parameters\n    ----------\n    e : MouseEvent\n        Event instance.\n    options : dict\n        Optional arguments dictionary.\n    """\n    rectangle_1: ap.Rectangle = e.this\n    rectangle_2: ap.Rectangle = options[\'rectangle\']\n    rectangle_1.visible = ap.Boolean(False)\n    rectangle_2.visible = ap.Boolean(True)\n\n\ndef on_rectangle_2_click(\n        e: ap.MouseEvent[ap.Rectangle], options: _RectOptions) -> None:\n    """\n    The handler that the second rectangle calls when clicked.\n\n    Parameters\n    ----------\n    e : MouseEvent\n        Event instance.\n    options : dict\n        Optional arguments dictionary.\n    """\n    rectangle_1: ap.Rectangle = options[\'rectangle\']\n    rectangle_2: ap.Rectangle = e.this\n    rectangle_1.visible = ap.Boolean(True)\n    rectangle_2.visible = ap.Boolean(False)\n\n\nap.Stage(\n    background_color=\'#333\',\n    stage_width=250,\n    stage_height=150,\n    stage_elem_id=\'stage\')\n\nsprite: ap.Sprite = ap.Sprite()\n\nsprite.graphics.begin_fill(color=\'#0af\')\nrectangle_1: ap.Rectangle = sprite.graphics.draw_rect(\n    x=50, y=50, width=50, height=50)\n\nsprite.graphics.begin_fill(color=\'#f0a\')\nrectangle_2: ap.Rectangle = sprite.graphics.draw_rect(\n    x=150, y=50, width=50, height=50)\nrectangle_2.visible = ap.Boolean(False)\n\noptions: _RectOptions = {\'rectangle\': rectangle_2}\nrectangle_1.click(\n    on_rectangle_1_click, options=options)\noptions = {\'rectangle\': rectangle_1}\nrectangle_2.click(\n    on_rectangle_2_click, options=options)\n\nap.save_overall_html(\n    dest_dir_path=\'display_object_visible_basic_usage/\')\n```':  # noqa
    '',

    '<iframe src="static/display_object_visible_basic_usage/index.html" width="250" height="150"></iframe>':  # noqa
    '',

    '## visible property API':
    '',

    '<!-- Docstring: apysc._display.visible_interface.VisibleInterface.visible -->\n\n<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>\n\n**[Interface summary]** Get a visibility value of this instance.<hr>\n\n**[Returns]**\n\n- `result`: Boolean\n  - If this instance is visible, this interface returns True.\n\n<hr>\n\n**[Examples]**':  # noqa
    '',

    '```py\n>>> import apysc as ap\n>>> stage: ap.Stage = ap.Stage()\n>>> sprite: ap.Sprite = ap.Sprite()\n>>> sprite.graphics.begin_fill(color=\'#0af\')\n>>> rectangle: ap.Rectangle = sprite.graphics.draw_rect(\n...     x=50, y=50, width=50, height=50)\n>>> rectangle.visible = ap.Boolean(False)\n>>> rectangle.visible\nBoolean(False)\n```':  # noqa
    '',

}
