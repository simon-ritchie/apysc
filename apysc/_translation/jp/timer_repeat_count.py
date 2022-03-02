"""This module is for the translation mapping data of the
following document:

Document file: timer_repeat_count.md
Language: jp
"""

from typing import Dict

MAPPING: Dict[str, str] = {

    '# Timer class repeat_count setting':
    '',

    'This page explains the `Timer` class `repeat_count` argument setting.':
    '',

    '## What argument is this?':
    '',

    'The `repeat_count` argument setting determines the max handler calling number. For example, if you specify the 10 value, a timer calls the handler 10 times and stops.':  # noqa
    '',

    '## Basic usage':
    '',

    'You can set the `repeat_count` parameter at the `Timer` constructor. The following example sets the timer with the 100 times `repeat_count` value when clicking the rectangle.\n\nIf the timer moves the rectangle 100 times (100-pixels to the right), the timer stops.':  # noqa
    '',

    '```py\n# runnable\nfrom typing_extensions import TypedDict\n\nimport apysc as ap\n\n\nclass _RectOptions(TypedDict):\n    rectangle: ap.Rectangle\n\n\ndef on_rectangle_click(\n        e: ap.MouseEvent[ap.Rectangle], options: dict) -> None:\n    """\n    The handler that a rectangle calls when clicked.\n\n    Parameters\n    ----------\n    e : ap.MouseEvent\n        Event instance.\n    options : dict\n        Optional arguments dictionary.\n    """\n    options_: _RectOptions = {\'rectangle\': e.this}\n    timer: ap.Timer = ap.Timer(\n        handler=on_timer, delay=16, repeat_count=100,\n        options=options_)\n    timer.start()\n    e.this.unbind_click(handler=on_rectangle_click)\n\n\ndef on_timer(e: ap.TimerEvent, options: _RectOptions) -> None:\n    """\n    The handler that a timer calls.\n\n    Parameters\n    ----------\n    e : ap.TimerEvent\n        Event instance.\n    options : dict\n        Optional arguments dictionary.\n    """\n    rectangle: ap.Rectangle = options[\'rectangle\']\n    rectangle.x += 1\n\n\nap.Stage(\n    stage_width=250, stage_height=150, background_color=\'#333\',\n    stage_elem_id=\'stage\')\nsprite: ap.Sprite = ap.Sprite()\nsprite.graphics.begin_fill(color=\'#0af\')\nrectangle: ap.Rectangle = sprite.graphics.draw_rect(\n    x=50, y=50, width=50, height=50)\nrectangle.click(on_rectangle_click)\n\nap.save_overall_html(\n    dest_dir_path=\'timer_repeat_count_basic_usage/\')\n```':  # noqa
    '',

    '<iframe src="static/timer_repeat_count_basic_usage/index.html" width="250" height="150"></iframe>':  # noqa
    '',

    '## Timer constructor API':
    '',

    '<!-- Docstring: apysc._time.timer.Timer.__init__ -->\n\n<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>\n\n**[Interface signature]** `__init__(self, handler:Callable[[_ForwardRef(\'timer_event.TimerEvent\'), ~_O1], NoneType], delay:Union[int, float, apysc._type.number_value_interface.NumberValueInterface, apysc._time.fps.FPS], *, repeat_count:Union[int, apysc._type.int.Int]=0, options:Union[~_O1, NoneType]=None) -> None`<hr>\n\n**[Interface summary]** Timer class to handle function calling at regular intervals.<hr>\n\n**[Parameters]**\n\n- `handler`: _Handler\n  - A handler would be called at regular intervals.\n- `delay`: Int or int or Number or float or FPS\n  - A delay between each `Handler` calling in a millisecond or FPS value. If an `FPS` value is specified, this value becomes a millisecond calculated with that FPS value (e.g., if the `FPS_60` value is specified, then `delay` becomes 16.6666667).\n- `repeat_count`: Int or int\n  - Max count of a `Handler`\'s calling. A timer stops if the `Handler`\'s calling count has reached this value. If 0 is specified, then a timer loops forever.\n- `options`: dict or None, default None\n  - Optional arguments dictionary to pass a `Handler` callable.\n\n<hr>\n\n**[Examples]**':  # noqa
    '',

    '```py\n>>> from typing_extensions import TypedDict\n>>> import apysc as ap\n>>> class RectOptions(TypedDict):\n...     rectangle: ap.Rectangle\n>>> def on_timer(e: ap.TimerEvent, options: RectOptions) -> None:\n...     rectangle: ap.Rectangle = options[\'rectangle\']\n...     rectangle.x += 1\n>>> stage: ap.Stage = ap.Stage()\n>>> sprite: ap.Sprite = ap.Sprite()\n>>> sprite.graphics.begin_fill(color=\'#0af\')\n>>> rectangle: ap.Rectangle = sprite.graphics.draw_rect(\n...     x=50, y=50, width=50, height=50)\n>>> options: RectOptions = {\'rectangle\': rectangle}\n>>> _ = ap.Timer(\n...     on_timer, delay=ap.FPS.FPS_60, options=options).start()\n```':  # noqa
    '',

    '<hr>\n\n**[References]**\n\n- [Timer document](https://simon-ritchie.github.io/apysc/timer.html)\n- [TimerEvent class document](https://simon-ritchie.github.io/apysc/timer_event.html)\n- [Timer class delay setting document](https://simon-ritchie.github.io/apysc/timer_delay.html)\n- [FPS enum document](https://simon-ritchie.github.io/apysc/fps.html)\n- [About the handler options\' type document](https://simon-ritchie.github.io/apysc/about_handler_options_type.html)':  # noqa
    '',

    '## repeat_count property API':
    '',

    '<!-- Docstring: apysc._time.timer.Timer.repeat_count -->\n\n<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>\n\n**[Interface summary]** Get a max count value of a handler\'s calling.<hr>\n\n**[Returns]**\n\n- `repeat_count`: Int\n  - Max count of a handler\'s calling. If this value is 0, then a timer loop forever.\n\n<hr>\n\n**[Examples]**':  # noqa
    '',

    '```py\n>>> import apysc as ap\n>>> def on_timer(e: ap.TimerEvent, options: dict) -> None:\n...     pass\n>>> timer: ap.Timer = ap.Timer(\n...     on_timer, delay=33.3, repeat_count=50)\n>>> timer.repeat_count\nInt(50)\n```':  # noqa
    '',

}
