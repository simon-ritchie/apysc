"""This module is for the translation mapping data of the
following document:

Document file: sprite.md
Language: jp
"""

from typing import Dict

MAPPING: Dict[str, str] = {

    '# Sprite':
    '',

    'This page explains the `Sprite` class.':
    '',

    '## What is the Sprite?':
    '',

    'The `Sprite` class is the container of each `DisplayObject` instance. It also has the `Graphics` class interfaces and can draw each vector graphic.':  # noqa
    '',

    '## Note for the automated addition':
    '',

    'The `Sprite` instance is automated added to the stage (no need to call `add_child` or other related interfaces). However, suppose you want to add to the other instance. In that case, you need to call the `add_child` method manually.':  # noqa
    '',

    '## graphics attribute interfaces':
    '',

    'The `Sprite` instance has the `graphics` attribute, and you can draw each vector graphic with it. For example, the following code draws the cyan color rectangle.':  # noqa
    '',

    '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    background_color=\'#333\',\n    stage_width=150,\n    stage_height=150,\n    stage_elem_id=\'stage\')\n\nsprite: ap.Sprite = ap.Sprite()\nsprite.graphics.begin_fill(color=\'#0af\')\nsprite.graphics.draw_rect(x=50, y=50, width=50, height=50)\n\nap.save_overall_html(\n    dest_dir_path=\'sprite_graphics_attribute/\')\n```':  # noqa
    '',

    '<iframe src="static/sprite_graphics_attribute/index.html" width="150" height="150"></iframe>\n\nFor more details, please see the `Graphics` related documents, for example:\n\n- [Graphics class](graphics.md)\n- [Graphics class begin fill interface](graphics_begin_fill.md)\n- [Graphics class line style interface](graphics_line_style.md)\n- [Graphics class draw rect interface](graphics_draw_rect.md)\n- [Graphics class draw circle interface](graphics_draw_circle.md)':  # noqa
    '',

    '## Move DisplayObject instances simultaneously':
    '',

    'The `Sprite` class is a container, and if you move that coordinates, it changes children\'s coordinates simultaneously. For example, the following code changes the sprite y-coordinate when clicking the rectangle.':  # noqa
    '',

    '```py\n# runnable\nimport apysc as ap\n\n\ndef on_sprite_click(\n        e: ap.MouseEvent[ap.Sprite], options: dict) -> None:\n    """\n    The handler that the sprite calls when clicked.\n\n    Parameters\n    ----------\n    e : MouseEvent\n        Event instance.\n    options : dict\n        Optional arguments dictionary.\n    """\n    sprite: ap.Sprite = e.this\n    sprite.y += 50\n\n\nap.Stage(\n    background_color=\'#333\',\n    stage_width=250,\n    stage_height=250,\n    stage_elem_id=\'stage\')\n\nsprite: ap.Sprite = ap.Sprite()\nsprite.graphics.begin_fill(color=\'#0af\')\nsprite.graphics.draw_rect(x=50, y=50, width=50, height=50)\nsprite.graphics.draw_rect(x=150, y=50, width=50, height=50)\nsprite.click(on_sprite_click)\n\nap.save_overall_html(\n    dest_dir_path=\'sprite_move_instances_simultaneously/\')\n```':  # noqa
    '',

    '<iframe src="static/sprite_move_instances_simultaneously/index.html" width="250" height="250"></iframe>\n\nThe subsequent pages explain the other interfaces, such as the `add_child` interface.':  # noqa
    '',

    '## See also':
    '',

    '- [Add child and remove child interfaces](add_child_and_remove_child.md)\n- [Contains interface](contains.md)\n- [Num children interface](num_children.md)\n- [Get child at interface](get_child_at.md)':  # noqa
    '',

    '## Sprite class constructor API':
    '',

    '<!-- Docstring: apysc._display.sprite.Sprite.__init__ -->\n\n<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>\n\n**[Interface signature]** `__init__(self, *, variable_name:Union[str, NoneType]=None) -> None`<hr>\n\n**[Interface summary]** Create a basic display object that can be a parent.<hr>\n\n**[Parameters]**\n\n- `variable_name`: str or None, default None\n  - Variable name of this instance. A js expression uses this setting. It is unnecessary to specify any string except when instantiating the `Sprite` subclass.\n\n<hr>\n\n**[Examples]**':  # noqa
    '',

    '```py\n>>> import apysc as ap\n>>> stage: ap.Stage = ap.Stage()\n>>> sprite_1: ap.Sprite = ap.Sprite()\n>>> # Create the sprite child rectangle\n>>> sprite_1.graphics.begin_fill(color=\'#0af\')\n>>> rect: ap.Rectangle = sprite_1.graphics.draw_rect(\n...     x=50, y=50, width=50, height=50)\n>>> sprite_1.graphics.contains(rect)\nBoolean(True)\n\n>>> # Move the created rectangle to the other sprite\n>>> sprite_2: ap.Sprite = ap.Sprite()\n>>> sprite_2.add_child(rect)\n>>> sprite_1.graphics.contains(rect)\nBoolean(False)\n\n>>> sprite_2.contains(rect)\nBoolean(True)\n\n>>> # Move the sprite container\n>>> sprite_2.x = ap.Int(50)\n>>> sprite_2.x\nInt(50)\n```':  # noqa
    '',

}