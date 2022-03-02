"""This module is for the translation mapping data of the
following document:

Document file: animation_reverse.md
Language: jp
"""

from typing import Dict

MAPPING: Dict[str, str] = {

    '# animation_reverse interface':
    '',

    'This page explains the `animation_reverse` method interface.':
    '',

    '## What interface is this?':
    '',

    'The `animation_reverse` interface reverses the running animations.\n\nThis interface exists in the instances that have the animation interfaces (such as the `animation_x`\\, `animation_move`).':  # noqa
    '',

    '## Basic usage':
    '',

    'The following example sets the x-coordinate animation and starts the 1-second interval timer to reverse animation with the `animation_reverse` interface.':  # noqa
    '',

    '```py\n# runnable\nfrom typing_extensions import TypedDict\n\nimport apysc as ap\n\n\nclass _RectOptions(TypedDict):\n    rectangle: ap.Rectangle\n\n\ndef on_timer_1(e: ap.TimerEvent, options: _RectOptions) -> None:\n    """\n    The event handler that timer calls after the 3 seconds.\n\n    Parameters\n    ----------\n    e : ap.TimerEvent\n        Event instance.\n    options : dict\n        Optional arguments dictionary.\n    """\n    ap.Timer(on_timer_2, delay=1000, options=options).start()\n\n\ndef on_timer_2(e: ap.TimerEvent, options: _RectOptions) -> None:\n    """\n    The event handler that timer calls every second.\n\n    Parameters\n    ----------\n    e : ap.TimerEvent\n        Event instance.\n    options : dict\n        Optional arguments dictionary.\n    """\n    rectangle: ap.Rectangle = options[\'rectangle\']\n    rectangle.animation_reverse()\n\n\nap.Stage(\n    stage_width=500, stage_height=150, background_color=\'#333\',\n    stage_elem_id=\'stage\')\nsprite: ap.Sprite = ap.Sprite()\nsprite.graphics.begin_fill(color=\'#0af\')\n\nrectangle: ap.Rectangle = sprite.graphics.draw_rect(\n    x=50, y=50, width=50, height=50)\nrectangle.animation_x(x=400, duration=5000).start()\noptions: _RectOptions = {\'rectangle\': rectangle}\nap.Timer(\n    on_timer_1, delay=3000, repeat_count=1,\n    options=options).start()\n\nap.save_overall_html(\n    dest_dir_path=\'animation_reverse_basic_usage/\')\n```':  # noqa
    '',

    '<iframe src="static/animation_reverse_basic_usage/index.html" width="500" height="150"></iframe>':  # noqa
    '',

    '## Interface Notes':
    '',

    'This interface can only use during animation. If you use this at the end of the animation, nothing happens, as follows:':  # noqa
    '',

    '```py\n# runnable\nfrom typing_extensions import TypedDict\n\nimport apysc as ap\n\n\nclass _RectOptions(TypedDict):\n    rectangle: ap.Rectangle\n\n\ndef on_timer(e: ap.TimerEvent, options: _RectOptions) -> None:\n    """\n    The handler that the timer calls.\n\n    Parameters\n    ----------\n    e : ap.TimerEvent\n        Event instance.\n    options : dict\n        Optional arguments dictionary.\n    """\n    rectangle: ap.Rectangle = options[\'rectangle\']\n\n    # Nothing happens since the animation has already been completed.\n    rectangle.animation_reverse()\n\n\nap.Stage(\n    stage_width=500, stage_height=150, background_color=\'#333\',\n    stage_elem_id=\'stage\')\nsprite: ap.Sprite = ap.Sprite()\nsprite.graphics.begin_fill(color=\'#0af\')\n\nrectangle: ap.Rectangle = sprite.graphics.draw_rect(\n    x=50, y=50, width=50, height=50)\nrectangle.animation_x(x=400, duration=1000).start()\n\noptions: _RectOptions = {\'rectangle\': rectangle}\nap.Timer(on_timer, delay=1500, repeat_count=1, options=options).start()\n\nap.save_overall_html(\n    dest_dir_path=\'animation_reverse_notes/\')\n```':  # noqa
    '',

    '<iframe src="static/animation_reverse_notes/index.html" width="500" height="150"></iframe>':  # noqa
    '',

    '## animation_reverse API':
    '',

    '<!-- Docstring: apysc._animation.animation_reverse_interface.AnimationReverseInterface.animation_reverse -->\n\n<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>\n\n**[Interface signature]** `animation_reverse(self) -> None`<hr>\n\n**[Interface summary]** Reverse all running animations.<hr>\n\n**[Notes]**\n\nSuppose you call this interface multiple times and animations reach the beginning or end of the animation. In that case, this interface ignores the reverse instruction. This behavior means that the same interval\'s timer tick reverse setting does not work correctly (since the same interval setting reaches the animation start).<hr>\n\n**[Examples]**':  # noqa
    '',

    '```py\n>>> from typing_extensions import TypedDict\n>>> import apysc as ap\n>>> class RectOptions(TypedDict):\n...     rectangle: ap.Rectangle\n>>> def on_timer(\n...         e: ap.TimerEvent,\n...         options: RectOptions) -> None:\n...     rectangle: ap.Rectangle = options[\'rectangle\']\n...     rectangle.animation_reverse()\n>>> stage: ap.Stage = ap.Stage()\n>>> sprite: ap.Sprite = ap.Sprite()\n>>> sprite.graphics.begin_fill(color=\'#0af\')\n>>> rectangle: ap.Rectangle = sprite.graphics.draw_rect(\n...     x=50, y=50, width=50, height=50)\n>>> _ = rectangle.animation_x(\n...     x=100,\n...     duration=1500,\n...     easing=ap.Easing.EASE_OUT_QUINT,\n... ).start()\n>>> options: RectOptions = {\'rectangle\': rectangle}\n>>> ap.Timer(on_timer, delay=750, options=options).start()\n```':  # noqa
    '',

}
