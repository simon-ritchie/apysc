"""This module is for the translation mapping data of the
following document:

Document file: display_object.md
Language: jp
"""

from typing import Dict

MAPPING: Dict[str, str] = {

    '# DisplayObject':
    '',

    'This page explains the `DisplayObject` class.':
    '',

    '## What is the DisplayObject?':
    '',

    'The `DisplayObject` is the apysc base class for each display class, such as  `Sprite`\\, `Rectangle`\\, `Circle`\\, or something else.\n\nYou can verify the `DisplayObject` inheritance with each instance by the `isinstance` function.':  # noqa
    '',

    '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    background_color=\'#333\',\n    stage_width=200,\n    stage_height=200,\n    stage_elem_id=\'stage\')\n\nsprite: ap.Sprite = ap.Sprite()\nsprite.graphics.begin_fill(color=\'#0af\')\ncircle: ap.Circle = sprite.graphics.draw_circle(x=100, y=100, radius=100)\n\n# Verify each instance type.\nassert isinstance(sprite, ap.DisplayObject)\nassert isinstance(circle, ap.DisplayObject)\n```':  # noqa
    '',

    'The apysc uses this class for the basic interfaces or the creating the new display object with the `DisplayObject` inheritance.\n\nThe `DisplayObject` class has the basic interfaces, like `x`\\, `y`\\, `visible`\\, each mouse event binding, or others. The following page explains these interfaces one by one.':  # noqa
    '',

    '## See also':
    '',

    '- [DisplayObject class x and y interfaces](display_object_x_and_y.md)\n- [DisplayObject class parent interfaces](display_object_parent.md)\n- [DisplayObject class visible interface](display_object_visible.md)\n- [DisplayObject class mouse event binding interfaces](display_object_mouse_event.md)':  # noqa
    '',

}
