"""This module is for the translation mapping data of the
following document:

Document file: timer.md
Language: jp
"""

from typing import Dict

MAPPING: Dict[str, str] = {

    '# Timer':
    '',

    'This page explains the `Timer` class.':
    '',

    '## What is the Timer?':
    '',

    'The `Timer` class handles the timer\'s tick. You can call a handler at any intervals by it.':  # noqa
    '',

    '## Basic usage':
    '',

    'The `Timer` class requires arguments for the `handler` and `delay` (timer interval in milliseconds). And the `start` method starts that timer. A timer passes the `TimerEvent` instance and options arguments to a specified handler.\n\nThe following code sets the `Timer` when clicking the rectangle (`Sprite`):':  # noqa
    '',

    '```py\n# runnable\nfrom typing_extensions import TypedDict\n\nimport apysc as ap\n\n\nclass _RectOptions(TypedDict):\n    rectangle: ap.Rectangle\n\n\ndef on_sprite_click(\n        e: ap.MouseEvent[ap.Sprite], options: _RectOptions) -> None:\n    """\n    The Handler that the rectangle calls when clicked.\n\n    Parameters\n    ----------\n    e : MouseEvent\n        Event instance.\n    options : dict\n        Optional arguments dictionary.\n    """\n    e.this.unbind_click_all()\n    timer: ap.Timer = ap.Timer(on_timer, delay=16.6, options=options)\n    timer.start()\n\n\ndef on_timer(e: ap.TimerEvent, options: _RectOptions) -> None:\n    """\n    The Handler a timer calls.\n\n    Parameters\n    ----------\n    e : TimerEvent\n        Event instance.\n    options : dict\n        Optional arguments dictionary.\n    """\n    rectangle: ap.Rectangle = options[\'rectangle\']\n    rectangle.x += 1\n\n\nap.Stage(\n    stage_width=350, stage_height=150, background_color=\'#333\',\n    stage_elem_id=\'stage\')\nsprite: ap.Sprite = ap.Sprite()\nsprite.graphics.begin_fill(color=\'#0af\')\nrectangle: ap.Rectangle = sprite.graphics.draw_rect(\n    x=50, y=50, width=50, height=50)\noptions: _RectOptions = {\'rectangle\': rectangle}\nsprite.click(on_sprite_click, options=options)\n\nap.save_overall_html(\n    dest_dir_path=\'timer_basic_usage/\')\n```':  # noqa
    '',

    'If you click the rectangle, the timer starts, and the Handler increases the rectangle x value.\n\n<iframe src="static/timer_basic_usage/index.html" width="350" height="150"></iframe>':  # noqa
    '',

    '## See also':
    '',

    '- [TimerEvent class](timer_event.md)\n- [Timer class delay setting](timer_delay.md)\n- [FPS enum](fps.md)\n- [Timer class repeat count setting](timer_repeat_count.md)\n- [Timer class start and stop interfaces](timer_start_and_stop.md)\n- [Timer class timer complete interface](timer_complete.md)\n- [Timer class reset interface](timer_reset.md)':  # noqa
    '',

    '## Timer constructor API':
    '',

    '<!-- Docstring: apysc._time.timer.Timer.__init__ -->\n\n<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>\n\n**[Interface signature]** `__init__(self, handler:Callable[[_ForwardRef(\'timer_event.TimerEvent\'), ~_O1], NoneType], delay:Union[int, float, apysc._type.number_value_interface.NumberValueInterface, apysc._time.fps.FPS], *, repeat_count:Union[int, apysc._type.int.Int]=0, options:Union[~_O1, NoneType]=None) -> None`<hr>\n\n**[Interface summary]** Timer class to handle function calling at regular intervals.<hr>\n\n**[Parameters]**\n\n- `handler`: _Handler\n  - A handler would be called at regular intervals.\n- `delay`: Int or int or Number or float or FPS\n  - A delay between each `Handler` calling in a millisecond or FPS value. If an `FPS` value is specified, this value becomes a millisecond calculated with that FPS value (e.g., if the `FPS_60` value is specified, then `delay` becomes 16.6666667).\n- `repeat_count`: Int or int\n  - Max count of a `Handler`\'s calling. A timer stops if the `Handler`\'s calling count has reached this value. If 0 is specified, then a timer loops forever.\n- `options`: dict or None, default None\n  - Optional arguments dictionary to pass a `Handler` callable.\n\n<hr>\n\n**[Examples]**':  # noqa
    '',

    '```py\n>>> from typing_extensions import TypedDict\n>>> import apysc as ap\n>>> class RectOptions(TypedDict):\n...     rectangle: ap.Rectangle\n>>> def on_timer(e: ap.TimerEvent, options: RectOptions) -> None:\n...     rectangle: ap.Rectangle = options[\'rectangle\']\n...     rectangle.x += 1\n>>> stage: ap.Stage = ap.Stage()\n>>> sprite: ap.Sprite = ap.Sprite()\n>>> sprite.graphics.begin_fill(color=\'#0af\')\n>>> rectangle: ap.Rectangle = sprite.graphics.draw_rect(\n...     x=50, y=50, width=50, height=50)\n>>> options: RectOptions = {\'rectangle\': rectangle}\n>>> _ = ap.Timer(\n...     on_timer, delay=ap.FPS.FPS_60, options=options).start()\n```':  # noqa
    '',

    '<hr>\n\n**[References]**\n\n- [TimerEvent class document](https://simon-ritchie.github.io/apysc/timer_event.html)\n- [Timer class delay setting document](https://simon-ritchie.github.io/apysc/timer_delay.html)\n- [FPS enum document](https://simon-ritchie.github.io/apysc/fps.html)\n- [Timer class repeat_count setting](https://simon-ritchie.github.io/apysc/timer_repeat_count.html)\n- [About the handler options\' type document](https://simon-ritchie.github.io/apysc/about_handler_options_type.html)':  # noqa
    '',

}
