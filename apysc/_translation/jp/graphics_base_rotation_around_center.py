"""This module is for the translation mapping data of the
following document:

Document file: graphics_base_rotation_around_center.md
Language: jp
"""

from typing import Dict

MAPPING: Dict[str, str] = {

    '# GraphicsBase rotation_around_center interface':
    '',

    'This page explains the `GraphicsBase` class (base class of each graphic, such as the `Rectangle`) `rotation_around_center` property interface.':  # noqa
    '',

    '## What interface is this?':
    '',

    'The `rotation_around_center` property interface can set the rotation angle to its instance (rotation value around its center point).':  # noqa
    '',

    '## Basic usage':
    '',

    'The `rotation_around_center` interface accepts the `int` or `Int` value.':  # noqa
    '',

    '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    background_color=\'#333\',\n    stage_width=150,\n    stage_height=150,\n    stage_elem_id=\'stage\')\nsprite: ap.Sprite = ap.Sprite()\n\n# Set the cyan fill color and draw the rectangle.\nsprite.graphics.begin_fill(color=\'#0af\', alpha=0.5)\ncyan_rect: ap.Rectangle = sprite.graphics.draw_rect(\n    x=50, y=50, width=50, height=50)\ncyan_rect.rotation_around_center = ap.Int(30)\n\n# Set the magenta fill color and draw the rectangle.\nsprite.graphics.begin_fill(color=\'#f0a\', alpha=0.5)\nmagenta_rect: ap.Rectangle = sprite.graphics.draw_rect(\n    x=50, y=50, width=50, height=50)\n# Append the rotation angle with the incremental addition (the result\n# rotation will be 60 degrees).\nmagenta_rect.rotation_around_center += ap.Int(30)\nmagenta_rect.rotation_around_center += ap.Int(30)\n\nap.save_overall_html(\n    dest_dir_path=\'graphics_base_rotation_around_center_basic_usage/\')\n```':  # noqa
    '',

    '<iframe src="static/graphics_base_rotation_around_center_basic_usage/index.html" width="150" height="150"></iframe>':  # noqa
    '',

    '## Notes':
    '',

    'This interface supports only the graphics instances currently. The container instances, such as the `Sprite` instance, are not supported (due to the HTML (SVG) specification).':  # noqa
    '',

    '## rotation_around_center property API':
    '',

    '<!-- Docstring: apysc._display.rotation_around_center_interface.RotationAroundCenterInterface.rotation_around_center -->\n\n<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>\n\n**[Interface summary]** Get a rotation value around the center of this instance.<hr>\n\n**[Returns]**\n\n- `rotation_around_center`: Int\n  - Rotation value around the center of this instance.\n\n<hr>\n\n**[Examples]**':  # noqa
    '',

    '```py\n>>> import apysc as ap\n>>> stage: ap.Stage = ap.Stage()\n>>> sprite: ap.Sprite = ap.Sprite()\n>>> sprite.graphics.begin_fill(color=\'#0af\')\n>>> rectangle: ap.Rectangle = sprite.graphics.draw_rect(\n...     x=50, y=50, width=50, height=50)\n>>> rectangle.rotation_around_center = ap.Int(45)\n>>> rectangle.rotation_around_center\nInt(45)\n```':  # noqa
    '',

}
