"""This module is for the translation mapping data of the
following document:

Document file: fps.md
Language: jp
"""

from typing import Dict

MAPPING: Dict[str, str] = {

    '# FPS enum':
    '',

    'This page explains the `FPS` enum class.':
    '',

    '## What class is this?':
    '',

    'The `FPS` enum class is the definition of each FPS (frames per second). The timer uses this enum to determine the timer tick interval.':  # noqa
    '',

    '## Basic usage':
    '',

    'There is an enum definition of FPS in 5 intervals. The `Timer` class `delay` argument is acceptable `FPS` enum value. For example, specify the `FPS.FPS_60` value to that argument. A timer interval becomes approximately `16.6666667` milliseconds. Similarly, it becomes the `33.3333333` milliseconds when you specify the `FPS.FPS_30` value.':  # noqa
    '',

    '```py\n# runnable\nfrom typing_extensions import TypedDict\n\nimport apysc as ap\n\n\nclass _RectOptions(TypedDict):\n    rectangle: ap.Rectangle\n\n\ndef on_timer(e: ap.TimerEvent, options: _RectOptions) -> None:\n    """\n    The handler that the timer calls.\n\n    Parameters\n    ----------\n    e : ap.TimerEvent\n        Event instance.\n    options : dict\n        Optional arguments dictionary.\n    """\n    rectangle: ap.Rectangle = options[\'rectangle\']\n    rectangle.rotation_around_center += 1\n\n\nap.Stage(\n    stage_width=350, stage_height=150, background_color=\'#333\',\n    stage_elem_id=\'stage\')\nsprite: ap.Sprite = ap.Sprite()\nsprite.graphics.begin_fill(color=\'#0af\')\n\nrectangle_1: ap.Rectangle = sprite.graphics.draw_rect(\n    x=50, y=50, width=50, height=50)\noptions: _RectOptions = {\'rectangle\': rectangle_1}\ntimer_1: ap.Timer = ap.Timer(\n    handler=on_timer, delay=ap.FPS.FPS_10, options=options)\ntimer_1.start()\n\nrectangle_2: ap.Rectangle = sprite.graphics.draw_rect(\n    x=150, y=50, width=50, height=50)\noptions = {\'rectangle\': rectangle_2}\ntimer_2: ap.Timer = ap.Timer(\n    handler=on_timer, delay=ap.FPS.FPS_30, options=options)\ntimer_2.start()\n\nrectangle_3: ap.Rectangle = sprite.graphics.draw_rect(\n    x=250, y=50, width=50, height=50)\noptions = {\'rectangle\': rectangle_3}\ntimer_3: ap.Timer = ap.Timer(\n    handler=on_timer, delay=ap.FPS.FPS_60, options=options)\ntimer_3.start()\n\nap.save_overall_html(\n    dest_dir_path=\'fps_basic_usage/\')\n```':  # noqa
    '',

    '<iframe src="static/fps_basic_usage/index.html" width="350" height="150"></iframe>':  # noqa
    '',

    '## See also':
    '',

    '- [Timer class delay setting](timer_delay.md)':
    '',

}
