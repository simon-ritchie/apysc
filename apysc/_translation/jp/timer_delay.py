"""This module is for the translation mapping data of the
following document:

Document file: timer_delay.md
Language: jp
"""

from typing import Dict

MAPPING: Dict[str, str] = {

    '# Timer class delay setting':
    '',

    'This page explains the `Timer` class `delay` argument setting.':
    '',

    '## What argument is this?':
    '',

    'The `delay` argument setting determines the timer tick interval. This setting is a milliseconds unit, so a value of 1000 ticks every 1 second.\n\nThe `int`\\, `float`\\, `Int`\\, `Number`\\, and `FPS` enum can be acceptable.':  # noqa
    '',

    '## Basic usage':
    '',

    'You can set the `delay` parameter at the `Timer` class constructor. The following example sets each timer (`timer_1`, `timer_2`, `timer_3`) and passes the delay values of `100`, `333.3333333`, `16.6666667`.\n\nThe first-timer (`delay` is 100) is called 10 times in a second, and the second one (`delay` is 33.3333333) is 30 times in a second, and the third one (`delay` is 16.6666667) is 60 times.':  # noqa
    '',

    '```py\n# runnable\nfrom typing_extensions import TypedDict\n\nimport apysc as ap\n\nap.Stage(\n    stage_width=350, stage_height=150, background_color=\'#333\',\n    stage_elem_id=\'stage\')\nsprite: ap.Sprite = ap.Sprite()\n\nsprite.graphics.begin_fill(color=\'#0af\')\nrectangle_1: ap.Rectangle = sprite.graphics.draw_rect(\n    x=50, y=50, width=50, height=50)\nrectangle_2: ap.Rectangle = sprite.graphics.draw_rect(\n    x=150, y=50, width=50, height=50)\nrectangle_3: ap.Rectangle = sprite.graphics.draw_rect(\n    x=250, y=50, width=50, height=50)\n\n\nclass _RectOptions(TypedDict):\n    rectangle: ap.Rectangle\n\n\ndef on_timer(e: ap.TimerEvent, options: _RectOptions) -> None:\n    """\n    The Handler would be called every timer tick.\n\n    Parameters\n    ----------\n    e : ap.TimerEvent\n        Event instance.\n    options : dict\n        Optional arguments dictionary.\n    """\n    rectangle: ap.Rectangle = options[\'rectangle\']\n    rectangle.rotation_around_center += 1\n\n\noptions: _RectOptions = {\'rectangle\': rectangle_1}\ntimer_1: ap.Timer = ap.Timer(\n    handler=on_timer, delay=100, options=options)\ntimer_1.start()\n\noptions = {\'rectangle\': rectangle_2}\ntimer_2: ap.Timer = ap.Timer(\n    handler=on_timer, delay=33.3333333, options=options)\ntimer_2.start()\n\noptions = {\'rectangle\': rectangle_3}\ntimer_3: ap.Timer = ap.Timer(\n    handler=on_timer, delay=16.6666667, options=options)\ntimer_3.start()\n\nap.save_overall_html(\n    dest_dir_path=\'timer_delay_basic_usage/\')\n```':  # noqa
    '',

    '<iframe src="static/timer_delay_basic_usage/index.html" width="350" height="150"></iframe>':  # noqa
    '',

    '## Set the FPS enum value to the delay argument':
    '',

    'You can also pass the `FPS` (frames per second) enum value to the `delay` argument. For example, if the `FPS.FPS_60` is specified, a timer delay becomes 60 frames per second (16.6666667 milliseconds). Likely, the `FPS.FPS_30` is specified, a timer delay becomes 30 frames per second (33.3333333 milliseconds).':  # noqa
    '',

    '```py\n# runnable\nfrom typing_extensions import TypedDict\n\nimport apysc as ap\n\nap.Stage(\n    stage_width=150, stage_height=150, background_color=\'#333\',\n    stage_elem_id=\'stage\')\nsprite: ap.Sprite = ap.Sprite()\nsprite.graphics.begin_fill(color=\'#0af\')\nrectangle: ap.Rectangle = sprite.graphics.draw_rect(\n    x=50, y=50, width=50, height=50)\n\n\nclass _RectOptions(TypedDict):\n    rectangle: ap.Rectangle\n\n\ndef on_timer(e: ap.TimerEvent, options: _RectOptions) -> None:\n    """\n    The Handler would be called every timer tick.\n\n    Parameters\n    ----------\n    e : ap.TimerEvent\n        Event instance.\n    options : dict\n        Optional arguments dictionary.\n    """\n    rectangle: ap.Rectangle = options[\'rectangle\']\n    rectangle.rotation_around_center += 1\n\n\noptions: _RectOptions = {\'rectangle\': rectangle}\ntimer: ap.Timer = ap.Timer(\n    handler=on_timer, delay=ap.FPS.FPS_60,\n    options=options)\ntimer.start()\n\nap.save_overall_html(\n    dest_dir_path=\'timer_delay_fps_enum/\')\n```':  # noqa
    '',

    '<iframe src="static/timer_delay_fps_enum/index.html" width="150" height="150"></iframe>':  # noqa
    '',

    '## See also':
    '',

    '- [FPS enum](fps.md)':
    '',

    '## Timer constructor API':
    '',

    '<!-- Docstring: apysc._time.timer.Timer.__init__ -->\n\n<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>\n\n**[Interface signature]** `__init__(self, handler:Callable[[_ForwardRef(\'timer_event.TimerEvent\'), ~_O1], NoneType], delay:Union[int, float, apysc._type.number_value_interface.NumberValueInterface, apysc._time.fps.FPS], *, repeat_count:Union[int, apysc._type.int.Int]=0, options:Union[~_O1, NoneType]=None) -> None`<hr>\n\n**[Interface summary]** Timer class to handle function calling at regular intervals.<hr>\n\n**[Parameters]**\n\n- `handler`: _Handler\n  - A handler would be called at regular intervals.\n- `delay`: Int or int or Number or float or FPS\n  - A delay between each `Handler` calling in a millisecond or FPS value. If an `FPS` value is specified, this value becomes a millisecond calculated with that FPS value (e.g., if the `FPS_60` value is specified, then `delay` becomes 16.6666667).\n- `repeat_count`: Int or int\n  - Max count of a `Handler`\'s calling. A timer stops if the `Handler`\'s calling count has reached this value. If 0 is specified, then a timer loops forever.\n- `options`: dict or None, default None\n  - Optional arguments dictionary to pass a `Handler` callable.\n\n<hr>\n\n**[Examples]**':  # noqa
    '',

    '```py\n>>> from typing_extensions import TypedDict\n>>> import apysc as ap\n>>> class RectOptions(TypedDict):\n...     rectangle: ap.Rectangle\n>>> def on_timer(e: ap.TimerEvent, options: RectOptions) -> None:\n...     rectangle: ap.Rectangle = options[\'rectangle\']\n...     rectangle.x += 1\n>>> stage: ap.Stage = ap.Stage()\n>>> sprite: ap.Sprite = ap.Sprite()\n>>> sprite.graphics.begin_fill(color=\'#0af\')\n>>> rectangle: ap.Rectangle = sprite.graphics.draw_rect(\n...     x=50, y=50, width=50, height=50)\n>>> options: RectOptions = {\'rectangle\': rectangle}\n>>> _ = ap.Timer(\n...     on_timer, delay=ap.FPS.FPS_60, options=options).start()\n```':  # noqa
    '',

    '<hr>\n\n**[References]**\n\n- [Timer document](https://simon-ritchie.github.io/apysc/timer.html)\n- [TimerEvent class document](https://simon-ritchie.github.io/apysc/timer_event.html)\n- [FPS enum document](https://simon-ritchie.github.io/apysc/fps.html)\n- [Timer class repeat_count setting](https://simon-ritchie.github.io/apysc/timer_repeat_count.html)\n- [About the handler options\' type document](https://simon-ritchie.github.io/apysc/about_handler_options_type.html)':  # noqa
    '',

    '## delay property API':
    '',

    '<!-- Docstring: apysc._time.timer.Timer.delay -->\n\n<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>\n\n**[Interface summary]** Get a delay value.<hr>\n\n**[Returns]**\n\n- `delay`: Number\n  - A delay value of each `Handler` calling in milliseconds.\n\n<hr>\n\n**[Examples]**':  # noqa
    '',

    '```py\n>>> import apysc as ap\n>>> def on_timer(e: ap.TimerEvent, options: dict) -> None:\n...     pass\n>>> timer: ap.Timer = ap.Timer(\n...     on_timer, delay=33.3, repeat_count=50)\n>>> timer.delay\nNumber(33.3)\n```':  # noqa
    '',

}
