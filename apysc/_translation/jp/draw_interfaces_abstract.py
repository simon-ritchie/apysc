"""This module is for the translation mapping data of the
following document:

Document file: draw_interfaces_abstract.md
Language: jp
"""

from typing import Dict

MAPPING: Dict[str, str] = {

    '# Draw interfaces abstract':
    '',

    'This page would explain the drawing interfaces abstract.':
    '',

    '## What apysc can do in its drawing interfaces':
    '',

    '- You can set the fill-color, fill-alpha (opacity), line-color, line-alpha, line-thickness values and draw each SVG graphic with these.\n- Supported graphics: The rectangle, circle, ellipse, polygon, line, polyline, and path.':  # noqa
    '',

    '## Fill settings':
    '',

    'The `begin_fill` interface sets the fill-color and fill-alpha (opacity).':  # noqa
    '',

    '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    background_color=\'#333\',\n    stage_width=150,\n    stage_height=150,\n    stage_elem_id=\'stage\')\nsprite: ap.Sprite = ap.Sprite()\nsprite.graphics.begin_fill(color=\'#0af\', alpha=0.5)\nsprite.graphics.draw_rect(x=50, y=50, width=50, height=50)\n\nap.save_overall_html(\n    dest_dir_path=\'draw_interfaces_abstract_begin_fill/\')\n```':  # noqa
    '',

    '<iframe src="static/draw_interfaces_abstract_begin_fill/index.html" width="150" height="150"></iframe>\n\nFor more details, please see the [Graphics class begin fill interface](graphics_begin_fill.md).':  # noqa
    '',

    '## Line style settings':
    '',

    'The `line_style` interface sets the line-color, line-alpha (opacity), line-thickness.':  # noqa
    '',

    '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    background_color=\'#333\',\n    stage_width=200,\n    stage_height=100,\n    stage_elem_id=\'stage\')\nsprite: ap.Sprite = ap.Sprite()\nsprite.graphics.line_style(color=\'#fff\', thickness=5, alpha=0.5)\nsprite.graphics.draw_line(x_start=50, y_start=50, x_end=150, y_end=50)\n\nap.save_overall_html(\n    dest_dir_path=\'draw_interfaces_abstract_line_style/\')\n```':  # noqa
    '',

    '<iframe src="static/draw_interfaces_abstract_line_style/index.html" width="200" height="100"></iframe>\n\nFor more details, please see the [Graphics class line style interface](graphics_line_style.md).':  # noqa
    '',

    '## Each drawing interface':
    '',

    'Each drawing interface has the `draw_` prefix draw SVG graphics (e.g., draw_rect, draw_circle).':  # noqa
    '',

    '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    background_color=\'#333\',\n    stage_width=250,\n    stage_height=150,\n    stage_elem_id=\'stage\')\nsprite: ap.Sprite = ap.Sprite()\nsprite.graphics.begin_fill(color=\'#0af\')\nsprite.graphics.draw_rect(x=50, y=50, width=50, height=50)\nsprite.graphics.draw_circle(x=175, y=75, radius=25)\n\nap.save_overall_html(\n    dest_dir_path=\'draw_interfaces_abstract_each_drawing_interface/\')\n```':  # noqa
    '',

    '<iframe src="static/draw_interfaces_abstract_each_drawing_interface/index.html" width="250" height="150"></iframe>\n\nFor more details, please see the following:\n\n- [Graphics class draw rect interface](graphics_draw_rect.md)\n- [Graphics class draw round rect interface](graphics_draw_round_rect.md)\n- [Graphics class draw circle interface](graphics_draw_circle.md)\n- [Graphics class draw ellipse interface](graphics_draw_ellipse.md)\n- [Graphics class move to and line to interfaces](graphics_move_to_and_line_to.md)\n- [Graphics class draw line interface](graphics_draw_line.md)\n- [Graphics class draw dotted line interface](graphics_draw_dotted_line.md)\n- [Graphics class draw dashed line interface](graphics_draw_dashed_line.md)\n- [Graphics class draw round dotted line interface](graphics_draw_round_dotted_line.md)\n- [Graphics class draw dash dotted line interface](graphics_draw_dash_dotted_line.md)\n- [Graphics class draw polygon interface](graphics_draw_polygon.md)':  # noqa
    '',

    '## See also':
    '',

    '- [Graphics class](graphics.md)\n- [Graphics class fill color interface](graphics_fill_color.md)\n- [Graphics class fill alpha interface](graphics_fill_alpha.md)\n- [Graphics class line color interface](graphics_line_color.md)\n- [Graphics class line alpha interface](graphics_line_alpha.md)\n- [Graphics class line thickness interface](graphics_line_thickness.md)\n- [Graphics class line dot setting interface](graphics_line_dot_setting.md)\n- [Graphics class line dash setting interface](graphics_line_dash_setting.md)\n- [Graphics class line round dot setting interface](graphics_line_round_dot_setting.md)\n- [Graphics class line dash dot setting interface](graphics_line_dash_dot_setting.md)':  # noqa
    '',

}
