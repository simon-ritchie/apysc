"""This module is for the translation mapping data of the
following document:

Document file: bind_and_trigger_custom_event.md
Language: jp
"""

from typing import Dict

MAPPING: Dict[str, str] = {

    '# Bind and trigger the custom event':
    '',

    'This page explains the `bind_custom_event` and `trigger_custom_event` interfaces.':  # noqa
    '',

    '## What interfaces are these?':
    '',

    'The `bind_custom_event` interface registers your custom event to the instance, and the `trigger_custom_event` one triggers the registered custom events at any time.':  # noqa
    '',

    '## Basic usage':
    '',

    'The `bind_custom_event` interface has the `custom_event_type`, `handler`, `e`, and `options` arguments (`options` is optional).\n\nThe `custom_event_type` argument is the custom event type name\'s string. This value needs to specify the same one at the calling of the `trigger_custom_event` interface.\n\nThe `e` argument is an event instance that may become the subclass of the `Event` class, such as the `MouseEvent` or `TimerEvent`\\.\n\nThe following example rotates the rectangle when you click it. If the rectangle rotated 90 degrees, then the custom event (`rotate_90_degrees`) is triggered, and the `on_rotate_90_degrees` handler (custom event) is called and display the second rectangle (toggle the `visible` property):':  # noqa
    '',

    '```py\n# runnable\nfrom typing_extensions import TypedDict\n\nimport apysc as ap\n\n# Custom event type name.\nROTATE_90_DEGREES: str = \'rotate_90_degrees\'\n\n\nclass _RectOptions(TypedDict):\n    rectangle: ap.Rectangle\n\n\ndef on_rectangle_click(\n        e: ap.MouseEvent[ap.Rectangle], options: dict) -> None:\n    """\n    The handler that the rectangle calls when clicked.\n\n    Parameters\n    ----------\n    e : ap.MouseEvent\n        Event instance.\n    options : dict\n        Optional arguments dictionary.\n    """\n    e.this.unbind_click(on_rectangle_click)\n    options_: _RectOptions = {\'rectangle\': e.this}\n    timer: ap.Timer = ap.Timer(\n        on_timer, delay=ap.FPS.FPS_60, repeat_count=90,\n        options=options_)\n    timer.timer_complete(\n        on_timer_complete,\n        options=options_)\n    timer.start()\n\n\ndef on_timer(e: ap.TimerEvent, options: _RectOptions) -> None:\n    """\n    The handler that the timer calls.\n\n    Parameters\n    ----------\n    e : ap.TimerEvent\n        Event instance.\n    options : dict\n        Optional arguments dictionary.\n    """\n    rectangle: ap.Rectangle = options[\'rectangle\']\n    rectangle.rotation_around_center += 1\n\n\ndef on_timer_complete(e: ap.TimerEvent, options: _RectOptions) -> None:\n    """\n    The handler that timer calls when its end.\n\n    Parameters\n    ----------\n    e : ap.TimerEvent\n        Event instance.\n    options : dict\n        Optional arguments dictionary.\n    """\n    rectangle: ap.Rectangle = options[\'rectangle\']\n    rectangle.trigger_custom_event(custom_event_type=ROTATE_90_DEGREES)\n\n\ndef on_rotate_90_degrees(e: ap.Event, options: _RectOptions) -> None:\n    """\n    The handler that the rectangle rates 90 degrees (custom event).\n\n    Parameters\n    ----------\n    e : ap.Event\n        Event instance.\n    options : dict\n        Optional arguments dictionary.\n    """\n    rectangle: ap.Rectangle = options[\'rectangle\']\n    rectangle.visible = ap.Boolean(True)\n\n\nap.Stage(\n    stage_width=250, stage_height=150, background_color=\'#333\',\n    stage_elem_id=\'stage\')\nsprite: ap.Sprite = ap.Sprite()\nsprite.graphics.begin_fill(color=\'#0af\')\n\nrectangle_1: ap.Rectangle = sprite.graphics.draw_rect(\n    x=50, y=50, width=50, height=50)\nrectangle_1.click(on_rectangle_click)\nrectangle_2: ap.Rectangle = sprite.graphics.draw_rect(\n    x=150, y=50, width=50, height=50)\nrectangle_2.visible = ap.Boolean(False)\n\ne: ap.Event = ap.Event(this=rectangle_1)\nrectangle_1.bind_custom_event(\n    custom_event_type=ROTATE_90_DEGREES, handler=on_rotate_90_degrees, e=e,\n    options={\'rectangle\': rectangle_2})\n\nap.save_overall_html(\n    dest_dir_path=\'bind_and_trigger_custom_event_basic_usage/\')\n```':  # noqa
    '',

    '<iframe src="static/bind_and_trigger_custom_event_basic_usage/index.html" width="250" height="150"></iframe>':  # noqa
    '',

    '## bind_custom_event API':
    '',

    '<!-- Docstring: apysc._event.custom_event_interface.CustomEventInterface.bind_custom_event -->\n\n<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>\n\n**[Interface signature]** `bind_custom_event(self, custom_event_type:Union[apysc._event.custom_event_type.CustomEventType, str], handler:Callable[[Any, Any], NoneType], e:apysc._event.event.Event, *, options:Union[Any, NoneType]=None, in_handler_head_expression:str=\'\') -> str`<hr>\n\n**[Interface summary]** Add a custom event listener setting.<hr>\n\n**[Parameters]**\n\n- `custom_event_type`: CustomEventType or str\n  - Target custom event type.\n- `handler`: _Handler\n  - Callable that this instance calls when its event\'s dispatching.\n- `e`: Event\n  - Event instance.\n- `options`: dict or None, default None\n  - Optional arguments dictionary to be passed to a handler.\n- `in_handler_head_expression`: str, default \'\'\n  - Optional expression to be added at the handler function\'s head position.\n\n<hr>\n\n**[Returns]**\n\n- `name`: str\n  - Handler\'s name.\n\n<hr>\n\n**[Examples]**':  # noqa
    '',

    '```py\n>>> import apysc as ap\n>>> def on_custom_event(\n...         e: ap.Event[ap.Rectangle], options: dict) -> None:\n...     rectangle: ap.Rectangle = e.this\n...     rectangle.fill_color = ap.String(\'#f0a\')\n>>> stage: ap.Stage = ap.Stage()\n>>> sprite: ap.Sprite = ap.Sprite()\n>>> sprite.graphics.begin_fill(color=\'#0af\')\n>>> rectangle: ap.Rectangle = sprite.graphics.draw_rect(\n...     x=50, y=50, width=50, height=50)\n>>> e: ap.Event = ap.Event(this=rectangle)\n>>> _ = rectangle.bind_custom_event(\n...     custom_event_type=\'my_custom_event\',\n...     handler=on_custom_event, e=e)\n>>> # Do something here and then trigger the custom event\n>>> rectangle.trigger_custom_event(\n...     custom_event_type=\'my_custom_event\')\n```':  # noqa
    '',

    '<hr>\n\n**[References]**\n\n- [About the handler options\' type document](https://simon-ritchie.github.io/apysc/about_handler_options_type.html)':  # noqa
    '',

    '## trigger_custom_event API':
    '',

    '<!-- Docstring: apysc._event.custom_event_interface.CustomEventInterface.trigger_custom_event -->\n\n<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>\n\n**[Interface signature]** `trigger_custom_event(self, custom_event_type:Union[apysc._event.custom_event_type.CustomEventType, str]) -> None`<hr>\n\n**[Interface summary]** Add a custom event trigger setting.<hr>\n\n**[Parameters]**\n\n- `custom_event_type`: CustomEventType or str\n  - Target custom event type.\n\n<hr>\n\n**[Examples]**':  # noqa
    '',

    '```py\n>>> import apysc as ap\n>>> def on_custom_event(\n...         e: ap.Event[ap.Rectangle], options: dict) -> None:\n...     rectangle: ap.Rectangle = e.this\n...     rectangle.fill_color = ap.String(\'#f0a\')\n>>> stage: ap.Stage = ap.Stage()\n>>> sprite: ap.Sprite = ap.Sprite()\n>>> sprite.graphics.begin_fill(color=\'#0af\')\n>>> rectangle: ap.Rectangle = sprite.graphics.draw_rect(\n...     x=50, y=50, width=50, height=50)\n>>> e: ap.Event = ap.Event(this=rectangle)\n>>> _ = rectangle.bind_custom_event(\n...     custom_event_type=\'my_custom_event\',\n...     handler=on_custom_event, e=e)\n>>> # Do something here and then trigger the custom event\n>>> rectangle.trigger_custom_event(\n...     custom_event_type=\'my_custom_event\')\n```':  # noqa
    '',

}
