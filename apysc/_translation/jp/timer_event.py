"""This module is for the translation mapping data of the
following document:

Document file: timer_event.md
Language: jp
"""

from typing import Dict

MAPPING: Dict[str, str] = {

    '# TimerEvent class':
    '',

    'This page explains the `TimerEvent` class.':
    '',

    '## What class is this?':
    '',

    'The `TimerEvent` class is the event class that a timer passes to a timer event handler function, such as the `Timer` class constructor or the `timer_complete` function\\.':  # noqa
    '',

    '## Basic usage':
    '',

    'Each timer event handler\'s `e` argument becomes the `TimerEvent` class instance.':  # noqa
    '',

    '```py\n# runnable\nfrom typing_extensions import TypedDict\n\nimport apysc as ap\n\n\nclass _RectOptions(TypedDict):\n    rectangle: ap.Rectangle\n\n\ndef on_timer(e: ap.TimerEvent, options: _RectOptions) -> None:\n    """\n    The handler that the timer calls.\n\n    Parameters\n    ----------\n    e : ap.TimerEvent\n        Event instance.\n    options : dict\n        Optional arguments dictionary.\n    """\n    rectangle: ap.Rectangle = options[\'rectangle\']\n    rectangle.rotation_around_center += 1\n\n\ndef on_timer_complete(e: ap.TimerEvent, options: dict) -> None:\n    """\n    The handler that the timer calls when completed.\n\n    Parameters\n    ----------\n    e : ap.TimerEvent\n        Event instance.\n    options : dict\n        Optional arguments dictionary.\n    """\n    ap.trace(\'Timer complete!\')\n\n\nap.Stage(\n    stage_width=150, stage_height=150, background_color=\'#333\',\n    stage_elem_id=\'stage\')\nsprite: ap.Sprite = ap.Sprite()\nsprite.graphics.begin_fill(color=\'#0af\')\nrectangle: ap.Rectangle = sprite.graphics.draw_rect(\n    x=50, y=50, width=50, height=50)\n\noptions: _RectOptions = {\'rectangle\': rectangle}\ntimer: ap.Timer = ap.Timer(\n    handler=on_timer, delay=33.3, options=options)\ntimer.start()\ntimer.timer_complete(handler=on_timer_complete)\n\nap.save_overall_html(\n    dest_dir_path=\'timer_event_basic_usage/\')\n```':  # noqa
    '',

    '<iframe src="static/timer_event_basic_usage/index.html" width="150" height="150"></iframe>':  # noqa
    '',

    '## This attribute':
    '',

    'The `TimerEvent` instance\'s `this` attribute becomes the target `Timer` instance, and you can use each timer instance interface from it.':  # noqa
    '',

    '```py\n# runnable\nfrom typing_extensions import TypedDict\n\nimport apysc as ap\n\n\nclass _RectOptions(TypedDict):\n    rectangle: ap.Rectangle\n\n\ndef on_timer(e: ap.TimerEvent, options: _RectOptions) -> None:\n    """\n    The handler that the timer calls.\n\n    Parameters\n    ----------\n    e : ap.TimerEvent\n        Event instance.\n    options : dict\n        Optional arguments dictionary.\n    """\n    rectangle: ap.Rectangle = options[\'rectangle\']\n    rectangle.rotation_around_center += 1\n    ap.trace(\'Current timer count: \', e.this.current_count)\n\n\nap.Stage(\n    stage_width=150, stage_height=150, background_color=\'#333\',\n    stage_elem_id=\'stage\')\nsprite: ap.Sprite = ap.Sprite()\nsprite.graphics.begin_fill(color=\'#0af\')\nrectangle: ap.Rectangle = sprite.graphics.draw_rect(\n    x=50, y=50, width=50, height=50)\n\noptions: _RectOptions = {\'rectangle\': rectangle}\ntimer: ap.Timer = ap.Timer(\n    handler=on_timer, delay=16.6, options=options)\ntimer.start()\n\nap.save_overall_html(\n    dest_dir_path=\'timer_event_this_attribute/\')\n```':  # noqa
    '',

    '<iframe src="static/timer_event_this_attribute/index.html" width="150" height="150"></iframe>':  # noqa
    '',

    '## TimerEvent constructor API':
    '',

    '<!-- Docstring: apysc._event.timer_event.TimerEvent.__init__ -->\n\n<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>\n\n**[Interface signature]** `__init__(self, this:\'timer.Timer\') -> None`<hr>\n\n**[Interface summary]** Timer event class.<hr>\n\n**[Parameters]**\n\n- `this`: Timer\n  - Target timer instance.\n\n<hr>\n\n**[Examples]**':  # noqa
    '',

    '```py\n>>> from typing_extensions import TypedDict\n>>> import apysc as ap\n>>> class RectOptions(TypedDict):\n...     rectangle: ap.Rectangle\n>>> def on_timer(e: ap.TimerEvent, options: RectOptions) -> None:\n...     rectangle: ap.Rectangle = options[\'rectangle\']\n...     rectangle.x += 1\n>>> stage: ap.Stage = ap.Stage()\n>>> sprite: ap.Sprite = ap.Sprite()\n>>> sprite.graphics.begin_fill(color=\'#0af\')\n>>> rectangle: ap.Rectangle = sprite.graphics.draw_rect(\n...     x=50, y=50, width=50, height=50)\n>>> options: RectOptions = {\'rectangle\': rectangle}\n>>> ap.Timer(\n...     on_timer, delay=ap.FPS.FPS_60, options=options,\n... ).start()\n```':  # noqa
    '',

    '':
    '',

    '## this attribute API':
    '',

    '<!-- Docstring: apysc._event.timer_event.TimerEvent.this -->\n\n<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>\n\n**[Interface summary]** Get a timer instance of listening to this event.<hr>\n\n**[Returns]**\n\n- `this`: TImer\n  - Instance of listening to this event.\n\n<hr>\n\n**[Examples]**':  # noqa
    '',

    '```py\n>>> from typing_extensions import TypedDict\n>>> import apysc as ap\n>>> class RectOptions(TypedDict):\n...     rectangle: ap.Rectangle\n>>> def on_timer(e: ap.TimerEvent, options: RectOptions) -> None:\n...     rectangle: ap.Rectangle = options[\'rectangle\']\n...     rectangle.x += 1\n...     with ap.If(rectangle.x >= 100):\n...         timer: ap.Timer = e.this\n...         timer.stop()\n>>> stage: ap.Stage = ap.Stage()\n>>> sprite: ap.Sprite = ap.Sprite()\n>>> sprite.graphics.begin_fill(color=\'#0af\')\n>>> rectangle: ap.Rectangle = sprite.graphics.draw_rect(\n...     x=50, y=50, width=50, height=50)\n>>> options: RectOptions = {\'rectangle\': rectangle}\n>>> ap.Timer(\n...     on_timer, delay=ap.FPS.FPS_60, options=options,\n... ).start()\n```':  # noqa
    '',

}
