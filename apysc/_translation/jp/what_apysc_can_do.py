"""This module is for the translation mapping data of the
following document:

Document file: what_apysc_can_do.md
Language: jp
"""

from typing import Dict

MAPPING: Dict[str, str] = {

    '# What apysc can do in its current implementation':
    '',

    'This page explains the current apysc implementation and functionality summary.':  # noqa
    '',

    '## Write with the Python and export HTML or use it on the Jupyter':
    '',

    'The apysc library can write the front-end with the Python language and export the HTML or use it on the Jupyter notebook, JupyterLab, and the Google Colaboratory!\n\nSee also:\n\n- [Save overall html interface](save_overall_html.md)\n- [Display on the jupyter interface](display_on_jupyter.md)\n- [Display on the Google Colaboratory interface](display_on_colaboratory.md)':  # noqa
    '',

    '## Draw the many types of the vector graphics':
    '',

    'The apysc library can draw many vector graphics types, like the rectangle, circle, line.\n\n<details>\n<summary>Display the code block:</summary>':  # noqa
    '',

    '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    stage_width=650, stage_height=210, background_color=\'#333\',\n    stage_elem_id=\'stage\')\nsprite: ap.Sprite = ap.Sprite()\n\nsprite.graphics.begin_fill(color=\'#0af\')\nsprite.graphics.draw_rect(x=50, y=50, width=50, height=50)\n\nsprite.graphics.draw_round_rect(\n    x=150, y=50, width=50, height=50, ellipse_width=12, ellipse_height=12)\n\nsprite.graphics.draw_circle(x=275, y=75, radius=25)\n\nsprite.graphics.draw_ellipse(x=375, y=75, width=50, height=30)\n\nsprite.graphics.draw_polygon(\n    points=[\n        ap.Point2D(x=475, y=50),\n        ap.Point2D(x=450, y=100),\n        ap.Point2D(x=500, y=100),\n    ])\n\nsprite.graphics.begin_fill(color=\'\')\nsprite.graphics.line_style(color=\'#eee\', thickness=3)\nsprite.graphics.move_to(x=550, y=50)\nsprite.graphics.line_to(x=600, y=50)\nsprite.graphics.line_to(x=550, y=100)\nsprite.graphics.line_to(x=600, y=100)\n\nsprite.graphics.draw_line(x_start=50, y_start=130, x_end=600, y_end=130)\nsprite.graphics.draw_dotted_line(\n    x_start=50, y_start=130, x_end=600, y_end=130, dot_size=5)\nsprite.graphics.draw_round_dotted_line(\n    x_start=53, y_start=160, x_end=600, y_end=160, round_size=6, space_size=6)\n\nap.save_overall_html(\n    dest_dir_path=\'what_apysc_can_do_draw_vector_graphics/\')\n```':  # noqa
    '',

    '</details>\n\n<iframe src="static/what_apysc_can_do_draw_vector_graphics/index.html" width="650" height="210"></iframe>\n\nSee also:\n\n- [Graphics class](graphics.md)\n- [Graphics class begin fill interface](graphics_begin_fill.md)\n- [Graphics class line style interface](graphics_line_style.md)\n- [Graphics class draw rect interface](graphics_draw_rect.md)\n- [Graphics class draw round rect interface](graphics_draw_round_rect.md)\n- [Graphics class draw circle interface](graphics_draw_circle.md)\n- [Graphics class draw ellipse interface](graphics_draw_ellipse.md)\n- [Graphics class move to and line to interfaces](graphics_move_to_and_line_to.md)\n- [Graphics class draw line interface](graphics_draw_line.md)\n- [Graphics class draw dotted line interface](graphics_draw_dotted_line.md)\n- [Graphics class draw dashed line interface](graphics_draw_dashed_line.md)\n- [Graphics class draw round dotted line interface](graphics_draw_round_dotted_line.md)\n- [Graphics class draw dash dotted line interface](graphics_draw_dash_dotted_line.md)\n- [Graphics class draw polygon interface](graphics_draw_polygon.md)':  # noqa
    '',

    '## Set each mouse event':
    '',

    'The apysc library supports each mouse event, like the click, mouse down, mouse over, mouse move.\n\nThe click event example (please click the following rectangle):\n\n<details>\n<summary>Display the code block:</summary>':  # noqa
    '',

    '```py\n# runnable\nimport apysc as ap\n\n\ndef on_click(\n        e: ap.MouseEvent[ap.Rectangle], options: dict) -> None:\n    """\n    The handler that the rectangle calls when clicked.\n\n    Parameters\n    ----------\n    e : ap.MouseEvent\n        Event instance.\n    options : dict\n        Optional arguments dictionary.\n    """\n    color: ap.String = e.this.fill_color\n    condition: ap.Boolean = color == \'#00aaff\'\n    with ap.If(condition):\n        e.this.fill_color = ap.String(\'#f0a\')\n    with ap.Else():\n        e.this.fill_color = ap.String(\'#0af\')\n\n\nap.Stage(\n    stage_width=150, stage_height=150, background_color=\'#333\',\n    stage_elem_id=\'stage\')\nsprite: ap.Sprite = ap.Sprite()\n\nsprite.graphics.begin_fill(color=\'#0af\')\nrectangle: ap.Rectangle = sprite.graphics.draw_rect(\n    x=50, y=50, width=50, height=50)\nrectangle.click(on_click)\n\nap.save_overall_html(\n    dest_dir_path=\'what_apysc_can_do_mouse_event_click/\')\n```':  # noqa
    '',

    '</details>\n\n<iframe src="static/what_apysc_can_do_mouse_event_click/index.html" width="150" height="150"></iframe>\n\nSee also:\n\n- [Basic mouse event interfaces](mouse_event_basic.md)\n- [Click interface](click.md)\n- [Mousedown and mouseup interfaces](mousedown_and_mouseup.md)\n- [Mouseover and mouseout interfaces](mouseover_and_mouseout.md)\n- [Mousemove interface](mousemove.md)':  # noqa
    '',

    '## The timer interface and animation':
    '',

    'You can use the timer-related interfaces and animate with those.\n\n<details>\n<summary>Display the code block:</summary>':  # noqa
    '',

    '```py\n# runnable\nfrom typing_extensions import TypedDict\n\nimport apysc as ap\n\n\nclass _Options(TypedDict):\n    rectangle: ap.Rectangle\n    alpha_direction: ap.Int\n\n\ndef on_timer(e: ap.TimerEvent, options: _Options) -> None:\n    """\n    The handler that the timer calls.\n\n    Parameters\n    ----------\n    e : ap.TimerEvent\n        Event instance.\n    options : dict\n        Optional arguments dictionary.\n    """\n    rectangle: ap.Rectangle = options[\'rectangle\']\n    alpha_direction: ap.Int = options[\'alpha_direction\']\n    current_alpha: ap.Number = rectangle.fill_alpha\n    condition_1: ap.Boolean = current_alpha < 0.0\n    condition_2: ap.Boolean = current_alpha > 1.0\n    with ap.If(condition_1):\n        alpha_direction.value = 1\n    with ap.Elif(condition_2):\n        alpha_direction.value = -1\n    rectangle.fill_alpha += alpha_direction * 0.03\n    rectangle.rotation_around_center += 1\n\n\nap.Stage(\n    stage_width=150, stage_height=150, background_color=\'#333\',\n    stage_elem_id=\'stage\')\nsprite: ap.Sprite = ap.Sprite()\n\nsprite.graphics.begin_fill(color=\'#0af\')\nalpha_direction: ap.Int = ap.Int(1)\nrectangle: ap.Rectangle = sprite.graphics.draw_rect(\n    x=50, y=50, width=50, height=50)\noptions: _Options = {\n    \'rectangle\': rectangle, \'alpha_direction\': alpha_direction}\ntimer: ap.Timer = ap.Timer(\n    on_timer, delay=ap.FPS.FPS_60, options=options)\ntimer.start()\n\nap.save_overall_html(\n    dest_dir_path=\'what_apysc_can_do_timer_animation/\')\n```':  # noqa
    '',

    '</details>\n\n<iframe src="static/what_apysc_can_do_timer_animation/index.html" width="150" height="150"></iframe>\n\nSee also:\n\n- [Timer class](timer.md)\n- [TimerEvent class](timer_event.md)\n- [Timer class delay setting](timer_delay.md)\n- [FPS enum](fps.md)\n- [Timer class repeat count setting](timer_repeat_count.md)\n- [Timer class start and stop interfaces](timer_start_and_stop.md)\n- [Timer class timer complete interface](timer_complete.md)\n- [Timer class reset interface](timer_reset.md)':  # noqa
    '',

}
