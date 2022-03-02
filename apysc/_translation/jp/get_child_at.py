"""This module is for the translation mapping data of the
following document:

Document file: get_child_at.md
Language: jp
"""

from typing import Dict

MAPPING: Dict[str, str] = {

    '# get_child_at interface':
    '',

    'This page explains the container class, like the `Graphics`\\, `Sprite`\\, `Stage`) `get_child_at` method interface.':  # noqa
    '',

    '## What interface is this?':
    '',

    'The `get_child_at` interface returns a child (`DisplayObject`) instance at the specified index.':  # noqa
    '',

    '## Basic usage':
    '',

    'The following code example is adding the rectangle to the sprite container. The `Sprite` class adds the `Graphics` instance at the constructor so that the first child becomes the `Graphics` instance. The second child becomes the `Rectangle` instance, which the sprite added with the `add_child` method.':  # noqa
    '',

    '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    background_color=\'#333\',\n    stage_width=450,\n    stage_height=150,\n    stage_elem_id=\'stage\')\n\nsprite: ap.Sprite = ap.Sprite()\nsprite.graphics.begin_fill(color=\'#0af\')\nrectangle_1: ap.Rectangle = sprite.graphics.draw_rect(\n    x=50, y=50, width=50, height=50)\nsprite.add_child(rectangle_1)\n\nfirst_child: ap.DisplayObject = sprite.get_child_at(index=0)\nassert isinstance(first_child, ap.Graphics)\n\nsecond_child: ap.DisplayObject = sprite.get_child_at(index=1)\nassert isinstance(second_child, ap.Rectangle)\n```':  # noqa
    '',

    '':
    '',

    '## get_child_at API':
    '',

    '<!-- Docstring: apysc._display.child_interface.ChildInterface.get_child_at -->\n\n<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>\n\n**[Interface signature]** `get_child_at(self, index:Union[int, apysc._type.int.Int]) -> apysc._display.display_object.DisplayObject`<hr>\n\n**[Interface summary]** Get child at a specified index.<hr>\n\n**[Parameters]**\n\n- `index`: int or Int\n  - Child\'s index (start from 0).\n\n<hr>\n\n**[Returns]**\n\n- `child`: DisplayObject\n  - Target index child instance.\n\n<hr>\n\n**[Examples]**':  # noqa
    '',

    '```py\n>>> import apysc as ap\n>>> stage: ap.Stage = ap.Stage()\n>>> sprite: ap.Sprite = ap.Sprite()\n>>> sprite.graphics.begin_fill(color=\'#0af\', alpha=0.5)\n>>> rectangle_1: ap.Rectangle = sprite.graphics.draw_rect(\n...     x=50, y=50, width=50, height=50)\n>>> rectangle_2: ap.Rectangle = sprite.graphics.draw_rect(\n...     x=150, y=50, width=50, height=50)\n>>> child_at_index_1: ap.DisplayObject = (\n...     sprite.graphics.get_child_at(1))\n>>> child_at_index_1 == rectangle_2\nTrue\n```':  # noqa
    '',

}
