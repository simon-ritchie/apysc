"""This module is for the translation mapping data of the
following document:

Document file: display_object_parent.md
Language: jp
"""

from typing import Dict

MAPPING: Dict[str, str] = {

    '# Display object parent interfaces':
    '',

    'This page explains the `DisplayObject` class `parent` interfaces (the `parent` property and `remove_from_parent` method).':  # noqa
    '',

    '## What interfaces are these?':
    '',

    'The `parent` attribute is the getter property. This attribute becomes a `Stage` instance or a container instance like a `Sprite` instance.':  # noqa
    '',

    '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    background_color=\'#333\',\n    stage_width=150,\n    stage_height=200,\n    stage_elem_id=\'stage\')\n\nsprite: ap.Sprite = ap.Sprite()\nrectangle: ap.Rectangle = sprite.graphics.draw_rect(\n    x=50, y=50, width=50, height=50)\n\nassert isinstance(sprite.parent, ap.Stage)\nassert isinstance(sprite.graphics.parent, ap.Sprite)\nassert isinstance(rectangle.parent, ap.Graphics)\n```':  # noqa
    '',

    'Notes: This interface automatically adds the sprite to the stage at the constructor. Similarly, this interface adds the `Graphics` instance to the `Sprite` instance.\n\nThe `remove_from_parent` interface removes self-instance from the parent (and not be displayed on the stage).':  # noqa
    '',

    '## Basic usage of the remove_from_parent interface':
    '',

    'The `remove_from_parent` method interface (no argument options) removes the self-instance from the parent. A Removed instance is not displayed until any parent adds it again.':  # noqa
    '',

    '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    background_color=\'#333\',\n    stage_width=150,\n    stage_height=150,\n    stage_elem_id=\'stage\')\n\nsprite: ap.Sprite = ap.Sprite()\nrectangle: ap.Rectangle = sprite.graphics.draw_rect(\n    x=50, y=50, width=50, height=50)\n\n# Remove the rectangle from the parent, and nothing displays\n# on the stage.\nrectangle.remove_from_parent()\n\nap.save_overall_html(\n    dest_dir_path=\'display_object_remove_from_parent_basic_usage/\')\n```':  # noqa
    '',

    '<iframe src="static/display_object_remove_from_parent_basic_usage/index.html" width="150" height="150"></iframe>':  # noqa
    '',

    '## See also':
    '',

    '- [Add child and remove child interfaces](add_child_and_remove_child.md)':  # noqa
    '',

    '## parent API':
    '',

    '<!-- Docstring: apysc._display.parent_interface.ParentInterface.parent -->\n\n<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>\n\n**[Interface summary]** Get parent instance that has a add_child and remove_child interfaces.<hr>\n\n**[Returns]**\n\n- `parent`: any parent instance or None\n  - Parent instance with `add_child` and `remove_child` interfaces. If this instance does not have a parent instance (not added child), this interface returns None.\n\n<hr>\n\n**[Examples]**':  # noqa
    '',

    '```py\n>>> import apysc as ap\n>>> stage: ap.Stage = ap.Stage()\n>>> sprite_1: ap.Sprite = ap.Sprite()\n>>> sprite_1.graphics.begin_fill(color=\'#0af\')\n>>> rectangle: ap.Rectangle = sprite_1.graphics.draw_rect(\n...     x=50, y=50, width=50, height=50)\n>>> sprite_2: ap.Sprite = ap.Sprite()\n>>> sprite_2.add_child(rectangle)\n>>> rectangle.parent == sprite_2\nTrue\n```':  # noqa
    '',

}
