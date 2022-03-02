"""This module is for the translation mapping data of the
following document:

Document file: add_child_and_remove_child.md
Language: jp
"""

from typing import Dict

MAPPING: Dict[str, str] = {

    '# add_child and remove_child interfaces':
    '',

    'This page explains the container class, like the `Graphics`\\, `Sprite`\\, `Stage`) `add_child` and `remove_child` method interfaces.':  # noqa
    '',

    '## What interfaces are these?':
    '',

    'The `add_child` and `remove_child` add or remove a `DisplayObject` child instance from a container instance. The apysc does not display a removed `DisplayObject` instance.':  # noqa
    '',

    '## Automatic addition of the children':
    '',

    'The apysc appends each `DisplayObject` instance to a parent at the constructor. So, for example, it appends a `Sprite` instance to a parent stage. Similarly, it appends a `graphics` instance to a parent `Sprite` instance.\n\nIf you need to adjust a parent, it is necessary to call the `add_child` or `remove_child` interfaces manually (for instance, set a `Sprite` parent to the other `Sprite`).':  # noqa
    '',

    '## Basic usage of the remove_child interface':
    '',

    'The `remove_child` interface removes a child from a parent container instance. The apysc does not display a removed `DisplayObject` instance.\n\nFor example, the following code calls the `remove_child` interface in the click handler, so if you click the rectangle, it removes that rectangle.':  # noqa
    '',

    '```py\n# runnable\nfrom typing_extensions import TypedDict\n\nimport apysc as ap\n\n\nclass _RectOptions(TypedDict):\n    rectangle: ap.Rectangle\n\n\ndef on_sprite_click(\n        e: ap.MouseEvent[ap.Sprite], options: _RectOptions) -> None:\n    """\n    The handler that the sprite calls when clicked.\n\n    Parameters\n    ----------\n    e : MouseEvent\n        Event instance.\n    options : dict\n        Optional arguments dictionary.\n    """\n    sprite: ap.Sprite = e.this\n    rectangle: ap.Rectangle = options[\'rectangle\']\n    sprite.remove_child(child=rectangle)\n\n\nap.Stage(\n    background_color=\'#333\',\n    stage_width=150,\n    stage_height=150,\n    stage_elem_id=\'stage\')\n\nsprite: ap.Sprite = ap.Sprite()\nsprite.graphics.begin_fill(color=\'#0af\')\nrectangle: ap.Rectangle = sprite.graphics.draw_rect(\n    x=50, y=50, width=50, height=50)\noptions: _RectOptions = {\'rectangle\': rectangle}\nsprite.click(on_sprite_click, options=options)\n\nap.save_overall_html(\n    dest_dir_path=\'sprite_basic_usage_of_remove_child/\')\n```':  # noqa
    '',

    '<iframe src="static/sprite_basic_usage_of_remove_child/index.html" width="150" height="150"></iframe>':  # noqa
    '',

    '## The basic usage of the add_child interface':
    '',

    'The `add_child` interface adds a removed child again or adds a child to the other container instance.\n\nThe following code example removes the rectangle from the first `Sprite` container (be positioned to the left) when you click the rectangle. Also, that click event adds the rectangle to the second `Sprite` container (be positioned to the right).':  # noqa
    '',

    '```py\n# runnable\nfrom typing_extensions import TypedDict\n\nimport apysc as ap\n\n\nclass _SpriteAndRectOptions(TypedDict):\n    rectangle: ap.Rectangle\n    sprite: ap.Sprite\n\n\ndef on_sprite_click(\n        e: ap.MouseEvent[ap.Sprite],\n        options: _SpriteAndRectOptions) -> None:\n    """\n    The handler that the sprite calls when clicked.\n\n    Parameters\n    ----------\n    e : MouseEvent\n        Event instance.\n    options : dict\n        Optional arguments dictionary.\n    """\n    first_sprite: ap.Sprite = e.this\n    rectangle: ap.Rectangle = options[\'rectangle\']\n    second_sprite: ap.Sprite = options[\'sprite\']\n    first_sprite.remove_child(child=rectangle)\n    second_sprite.add_child(child=rectangle)\n\n\nap.Stage(\n    background_color=\'#333\',\n    stage_width=250,\n    stage_height=150,\n    stage_elem_id=\'stage\')\n\nfirst_sprite: ap.Sprite = ap.Sprite()\nfirst_sprite.graphics.begin_fill(color=\'#0af\')\nfirst_sprite.x = ap.Int(50)\nfirst_sprite.y = ap.Int(50)\nrectangle: ap.Rectangle = first_sprite.graphics.draw_rect(\n    x=0, y=0, width=50, height=50)\n\nsecond_sprite: ap.Sprite = ap.Sprite()\nsecond_sprite.x = ap.Int(150)\nsecond_sprite.y = ap.Int(50)\n\noptions: _SpriteAndRectOptions = {\n    \'rectangle\': rectangle, \'sprite\': second_sprite}\nfirst_sprite.click(on_sprite_click, options=options)\n\nap.save_overall_html(\n    dest_dir_path=\'sprite_basic_usage_of_add_child/\')\n```':  # noqa
    '',

    '<iframe src="static/sprite_basic_usage_of_add_child/index.html" width="250" height="150"></iframe>':  # noqa
    '',

    '## See also':
    '',

    '- [DisplayObject class parent interfaces](display_object_parent.md)\n- [Contains interface](contains.md)':  # noqa
    '',

    '## add_child API':
    '',

    '<!-- Docstring: apysc._display.child_interface.ChildInterface.add_child -->\n\n<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>\n\n**[Interface signature]** `add_child(self, child:apysc._display.display_object.DisplayObject) -> None`<hr>\n\n**[Interface summary]** Add display object child to this instance.<hr>\n\n**[Parameters]**\n\n- `child`: DisplayObject\n  - Child instance to add.\n\n<hr>\n\n**[Examples]**':  # noqa
    '',

    '```py\n>>> import apysc as ap\n>>> stage: ap.Stage = ap.Stage()\n>>> sprite_1: ap.Sprite = ap.Sprite()\n>>> sprite_1.graphics.begin_fill(color=\'#0af\')\n>>> rectangle: ap.Rectangle = sprite_1.graphics.draw_rect(\n...     x=50, y=50, width=50, height=50)\n>>> sprite_2: ap.Sprite = ap.Sprite()\n>>> sprite_2.add_child(rectangle)\n```':  # noqa
    '',

    '':
    '',

    '## remove_child API':
    '',

    '<!-- Docstring: apysc._display.child_interface.ChildInterface.remove_child -->\n\n<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>\n\n**[Interface signature]** `remove_child(self, child:apysc._display.display_object.DisplayObject) -> None`<hr>\n\n**[Interface summary]** Remove display object child from this instance.<hr>\n\n**[Parameters]**\n\n- `child`: DisplayObject\n  - Child instance to remove.\n\n<hr>\n\n**[Examples]**':  # noqa
    '',

    '```py\n>>> import apysc as ap\n>>> stage: ap.Stage = ap.Stage()\n>>> sprite: ap.Sprite = ap.Sprite()\n>>> sprite.graphics.begin_fill(color=\'#0af\', alpha=0.5)\n>>> rectangle: ap.Rectangle = sprite.graphics.draw_rect(\n...     x=50, y=50, width=50, height=50)\n>>> sprite.graphics.remove_child(rectangle)\n>>> print(rectangle.parent)\nNone\n```':  # noqa
    '',

}
