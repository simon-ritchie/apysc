"""This module is for the translation mapping data of the
following document:

Document file: contains.md
Language: jp
"""

from typing import Dict

MAPPING: Dict[str, str] = {

    '# contains interface':
    '',

    'This page explains the container class, like the `Graphics`\\, `Sprite`\\, `Stage`) `contains` method interface.':  # noqa
    '',

    '## What interface is this?':
    '',

    'The `contains` interface returns the boolean (`Boolean`) value whether that `Sprite` instance has a given child or not.':  # noqa
    '',

    '## Basic usage':
    '',

    'The following example checks whether the first rectangle is a child of the `Sprite` container. If it is `true`\\, remove the rectangle from the sprite and display a log to the console (please press F12 to display that message).':  # noqa
    '',

    '```py\n# runnable\nfrom typing_extensions import TypedDict\n\nimport apysc as ap\n\n\nclass _RectOptions(TypedDict):\n    rectangle: ap.Rectangle\n\n\ndef on_sprite_click(\n        e: ap.MouseEvent[ap.Sprite], options: _RectOptions) -> None:\n    """\n    The handler that the sprite calls when clicked.\n\n    Parameters\n    ----------\n    e : MouseEvent\n        Event instance.\n    options : dict\n        Optional arguments dictionary.\n    """\n    sprite: ap.Sprite = e.this\n    rectangle_1: ap.Rectangle = options[\'rectangle\']\n    condition: ap.Boolean = sprite.graphics.contains(child=rectangle_1)\n    with ap.If(condition):\n        sprite.remove_child(child=rectangle_1)\n        ap.trace(\'Removed the rectangle!\')\n\n\nap.Stage(\n    background_color=\'#333\',\n    stage_width=250,\n    stage_height=150,\n    stage_elem_id=\'stage\')\n\nsprite: ap.Sprite = ap.Sprite()\nsprite.graphics.begin_fill(color=\'#0af\')\nrectangle_1: ap.Rectangle = sprite.graphics.draw_rect(\n    x=50, y=50, width=50, height=50)\nsprite.graphics.draw_rect(\n    x=150, y=50, width=50, height=50)\noptions: _RectOptions = {\'rectangle\': rectangle_1}\nsprite.click(on_sprite_click, options=options)\n\nap.save_overall_html(\n    dest_dir_path=\'sprite_contains_basic_usage/\')\n```':  # noqa
    '',

    '<iframe src="static/sprite_contains_basic_usage/index.html" width="250" height="150"></iframe>':  # noqa
    '',

    '## See also':
    '',

    '- [Add child and remove child interfaces](add_child_and_remove_child.md)':  # noqa
    '',

    '## contains API':
    '',

    '<!-- Docstring: apysc._display.child_interface.ChildInterface.contains -->\n\n<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>\n\n**[Interface signature]** `contains(self, child:apysc._display.display_object.DisplayObject) -> apysc._type.boolean.Boolean`<hr>\n\n**[Interface summary]** Get a boolean whether this instance contains a specified child.<hr>\n\n**[Parameters]**\n\n- `child`: DisplayObject\n  - Child instance to check.\n\n<hr>\n\n**[Returns]**\n\n- `result`: Boolean\n  - If this instance contains a specified child, this method returns True.\n\n<hr>\n\n**[Examples]**':  # noqa
    '',

    '```py\n>>> import apysc as ap\n>>> stage: ap.Stage = ap.Stage()\n>>> sprite: ap.Sprite = ap.Sprite()\n>>> sprite.graphics.begin_fill(color=\'#0af\', alpha=0.5)\n>>> rectangle: ap.Rectangle = sprite.graphics.draw_rect(\n...     x=50, y=50, width=50, height=50)\n>>> sprite.graphics.contains(rectangle)\nBoolean(True)\n\n>>> rectangle.remove_from_parent()\n>>> sprite.graphics.contains(rectangle)\nBoolean(False)\n```':  # noqa
    '',

}
