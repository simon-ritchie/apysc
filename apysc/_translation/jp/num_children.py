"""This module is for the translation mapping data of the
following document:

Document file: num_children.md
Language: jp
"""

from typing import Dict

MAPPING: Dict[str, str] = {

    '# num_children interface':
    '',

    'This page explains the container class, like the `Graphics`\\, `Sprite`\\, `Stage`) `num_children` property interface.':  # noqa
    '',

    '## What interface is this?':
    '',

    'The `num_children` property interface returns the integer (`Int`) value of the number of children.':  # noqa
    '',

    '## Notes':
    '',

    'The `Sprite` instance\'s initial children number is 1, not 0 since a sprite instance has a `graphics` child.':  # noqa
    '',

    '## Basic usage':
    '',

    'The `num_children` property returns the number of children (`Int` value). You can use it for the calculation, for instance, coordinates calculation.\n\nThe following example appends a new rectangle when you click the sprite (rectangle) instance. The `num_children` property determines a new rectangle x-coordinate. When clicking a rectangle, this code also displays the current `num_children` property value to the browser console (please press the F12 key).':  # noqa
    '',

    '```py\n# runnable\nimport apysc as ap\n\n\ndef on_sprite_click(\n        e: ap.MouseEvent[ap.Sprite], options: dict) -> None:\n    """\n    The handler that the sprite calls when clicked.\n\n    Parameters\n    ----------\n    e : MouseEvent\n        Event instance.\n    options : dict\n        Optional arguments dictionary.\n    """\n    sprite: ap.Sprite = e.this\n    rectangle_x: ap.Int = (sprite.num_children - 1) * 100 + 50\n    new_rect: ap.Rectangle = sprite.graphics.draw_rect(\n        x=rectangle_x,\n        y=50, width=50, height=50)\n    sprite.add_child(new_rect)\n    ap.trace(\n        \'Current sprite children number:\', sprite.num_children,\n        \'rectangle x:\', rectangle_x)\n\n\nap.Stage(\n    background_color=\'#333\',\n    stage_width=450,\n    stage_height=150,\n    stage_elem_id=\'stage\')\n\nsprite: ap.Sprite = ap.Sprite()\nsprite.graphics.begin_fill(color=\'#0af\')\nrectangle_1: ap.Rectangle = sprite.graphics.draw_rect(\n    x=50, y=50, width=50, height=50)\nsprite.add_child(rectangle_1)\nsprite.click(on_sprite_click)\n\nap.save_overall_html(\n    dest_dir_path=\'num_children_basic_usage/\')\n```':  # noqa
    '',

    '<iframe src="static/num_children_basic_usage/index.html" width="450" height="150"></iframe>':  # noqa
    '',

    '## num_children API':
    '',

    '<!-- Docstring: apysc._display.child_interface.ChildInterface.num_children -->\n\n<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>\n\n**[Interface summary]** Get a current children\'s number.<hr>\n\n**[Returns]**\n\n- `num_children`: int\n  - Current children number.\n\n<hr>\n\n**[Examples]**':  # noqa
    '',

    '```py\n>>> import apysc as ap\n>>> stage: ap.Stage = ap.Stage()\n>>> sprite: ap.Sprite = ap.Sprite()\n>>> sprite.graphics.begin_fill(color=\'#0af\', alpha=0.5)\n>>> rectangle_1: ap.Rectangle = sprite.graphics.draw_rect(\n...     x=50, y=50, width=50, height=50)\n>>> rectangle_2: ap.Rectangle = sprite.graphics.draw_rect(\n...     x=150, y=50, width=50, height=50)\n>>> sprite.graphics.num_children\nInt(2)\n```':  # noqa
    '',

}
