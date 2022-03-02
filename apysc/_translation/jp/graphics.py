"""This module is for the translation mapping data of the
following document:

Document file: graphics.md
Language: jp
"""

from typing import Dict

MAPPING: Dict[str, str] = {

    '# Graphics':
    '',

    'This page explains the `Graphics` class.':
    '',

    '## What is Graphics?':
    '',

    'The `Graphics` is the class to handle each vector graphics interface. This interface has the draw rectangle interface, draw line interface, or something else.\n\nThe `Sprite` or other `DisplayObject` instances instantiate this class instance.':  # noqa
    '',

    '## Call interfaces from sprite instance':
    '',

    'Sprite (object container) instance has the `graphics` attribute to call each drawing interface with this attribute.':  # noqa
    '',

    '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    background_color=\'#333\',\n    stage_width=250,\n    stage_height=180,\n    stage_elem_id=\'stage\')\n\nsprite: ap.Sprite = ap.Sprite()\n\n# Draw the white border and cyan color rectangle.\nsprite.graphics.line_style(color=\'#fff\', thickness=5)\nsprite.graphics.begin_fill(color=\'#0af\')\nsprite.graphics.draw_rect(\n    x=50, y=50, width=50, height=50)\n\n# Draw the magenta color polyline.\nsprite.graphics.begin_fill(color=\'\')\nsprite.graphics.line_style(color=\'#f0a\', thickness=5)\nsprite.graphics.move_to(x=150, y=50)\nsprite.graphics.line_to(x=200, y=50)\nsprite.graphics.line_to(x=150, y=100)\nsprite.graphics.line_to(x=200, y=100)\n\n# Draw the dashed line.\nsprite.graphics.draw_dashed_line(\n    x_start=50, y_start=130, x_end=200, y_end=130,\n    dash_size=10, space_size=5)\n\nap.save_overall_html(\n    dest_dir_path=\'graphics_call_interfaces_from_sprite_instance/\')\n```':  # noqa
    '',

    '<iframe src="static/graphics_call_interfaces_from_sprite_instance/index.html" width="250" height="180"></iframe>':  # noqa
    '',

    '## Return values':
    '',

    'Each interface returns created graphic instances (e.g., `Rectangle`\\, `Polyline`\\, and so on). These instances have the basic `DisplayObject` attributes and methods, like x, y, fill_alpha, visible, or something else.\n\nFor example, you can set an event and coordinate\'s updating to these instances, as follows:':  # noqa
    '',

    '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    background_color=\'#333\',\n    stage_width=200,\n    stage_height=200,\n    stage_elem_id=\'stage\')\n\nsprite: ap.Sprite = ap.Sprite()\n\n\ndef on_rectangle_click(\n        e: ap.MouseEvent[ap.Rectangle], options: dict) -> None:\n    """\n    The handler that the rectangle calls when clicked.\n\n    Parameters\n    ----------\n    e : MouseEvent\n        Event instance.\n    options : dict\n        Optional arguments dictionary.\n    """\n    rectangle: ap.Rectangle = e.this\n\n    # Update the coordinates, fill alpha, and fill color.\n    rectangle.x = ap.Int(100)\n    rectangle.y = ap.Int(100)\n    rectangle.fill_alpha = ap.Number(0.5)\n    rectangle.fill_color = ap.String(\'#f0a\')\n\n\n# drew_rect interface will return Rectangle instance.\nsprite.graphics.begin_fill(color=\'#0af\')\nrectangle: ap.Rectangle = sprite.graphics.draw_rect(\n    x=50, y=50, width=50, height=50)\n\n# Bind click event to the rectangle.\nrectangle.click(on_rectangle_click)\n\nap.save_overall_html(\n    dest_dir_path=\'graphics_return_values/\')\n```':  # noqa
    '',

    'If you click the following rectangle, that rectangle changes x and y coordinates, fill color, and alpha (opacity) values.\n\n<iframe src="static/graphics_return_values/index.html" width="200" height="200"></iframe>':  # noqa
    '',

    '## See also':
    '',

    '- [Graphics class begin fill interface](graphics_begin_fill.md)\n- [Graphics class line style interface](graphics_line_style.md)\n- [Graphics class draw rect interface](graphics_draw_rect.md)\n- [Graphics class draw round rect interface](graphics_draw_round_rect.md)\n- [Graphics class draw circle interface](graphics_draw_circle.md)\n- [Graphics class draw ellipse interface](graphics_draw_ellipse.md)\n- [Graphics class move to and line to interfaces](graphics_move_to_and_line_to.md)\n- [Graphics class draw line interface](graphics_draw_line.md)\n- [Graphics class draw dotted line interface](graphics_draw_dotted_line.md)\n- [Graphics class draw dashed line interface](graphics_draw_dashed_line.md)\n- [Graphics class draw round dotted line interface](graphics_draw_round_dotted_line.md)\n- [Graphics class draw dash dotted line interface](graphics_draw_dash_dotted_line.md)\n- [Graphics class draw polygon interface](graphics_draw_polygon.md)':  # noqa
    '',

}
