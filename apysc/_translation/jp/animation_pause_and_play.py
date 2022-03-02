"""This module is for the translation mapping data of the
following document:

Document file: animation_pause_and_play.md
Language: jp
"""

from typing import Dict

MAPPING: Dict[str, str] = {

    '# animation_pause and animation_play interfaces':
    '',

    'This page explains the `animation_pause` and `animation_play` method interfaces.':  # noqa
    '',

    '## What interface are these?':
    '',

    'The `animation_pause` interface pauses all the running animations of the target instance. The `animation_play` interface restarts the paused animation.\n\nThese interfaces exist in the instances that have the animation interfaces (such as the `animation_x`\\, `animation_move`).':  # noqa
    '',

    '## Basic usage':
    '',

    'The following example starts the x-coordinate animation and stops after 1 second. After stopping the animation and additionally 500 milliseconds passed, restarting the animation:':  # noqa
    '',

    '```py\n# runnable\nfrom typing_extensions import TypedDict\n\nimport apysc as ap\n\n\nclass _RectOptions(TypedDict):\n    rectangle: ap.Rectangle\n\n\ndef on_timer_1(e: ap.TimerEvent, options: _RectOptions) -> None:\n    """\n    The handler that the timer calls.\n\n    Parameters\n    ----------\n    e : ap.TimerEvent\n        Event instance.\n    options : _RectOptions\n        Optional arguments dictionary.\n    """\n    options[\'rectangle\'].animation_pause()\n    timer: ap.Timer = ap.Timer(\n        on_timer_2, delay=500, options=options, repeat_count=1)\n    timer.start()\n\n\ndef on_timer_2(e: ap.TimerEvent, options: _RectOptions) -> None:\n    """\n    The handler that the timer calls.\n\n    Parameters\n    ----------\n    e : ap.TimerEvent\n        Event instance.\n    options : _RectOptions\n        Optional arguments dictionary.\n    """\n    options[\'rectangle\'].animation_play()\n\n\nap.Stage(\n    stage_width=600, stage_height=150,\n    background_color=\'#333\', stage_elem_id=\'stage\')\nsprite: ap.Sprite = ap.Sprite()\nsprite.graphics.begin_fill(color=\'#00aaff\')\nrectangle: ap.Rectangle = sprite.graphics.draw_rect(\n    x=50, y=50, width=50, height=50)\nrectangle.animation_x(x=500, duration=15_000).start()\n\noptions: _RectOptions = {\'rectangle\': rectangle}\ntimer: ap.Timer = ap.Timer(\n    on_timer_1, delay=1000, options=options)\ntimer.start()\n\nap.save_overall_html(\n    dest_dir_path=\'./animation_pause_basic_usage/\')\n```':  # noqa
    '',

    '<iframe src="static/animation_pause_basic_usage/index.html" width="600" height="150"></iframe>':  # noqa
    '',

    '## animation_pause API':
    '',

    '<!-- Docstring: apysc._animation.animation_pause_interface.AnimationPauseInterface.animation_pause -->\n\n<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>\n\n**[Interface signature]** `animation_pause(self) -> None`<hr>\n\n**[Interface summary]** Stop all animations.<hr>\n\n**[Examples]**':  # noqa
    '',

    '```py\n>>> from typing_extensions import TypedDict\n>>> import apysc as ap\n>>> class RectOptions(TypedDict):\n...     rectangle: ap.Rectangle\n>>> def on_timer(\n...         e: ap.TimerEvent,\n...         options: RectOptions) -> None:\n...     rectangle: ap.Rectangle = options[\'rectangle\']\n...     rectangle.animation_pause()\n>>> stage: ap.Stage = ap.Stage()\n>>> sprite: ap.Sprite = ap.Sprite()\n>>> sprite.graphics.begin_fill(color=\'#0af\')\n>>> rectangle: ap.Rectangle = sprite.graphics.draw_rect(\n...     x=50, y=50, width=50, height=50)\n>>> _ = rectangle.animation_x(\n...     x=100,\n...     duration=1500,\n...     easing=ap.Easing.EASE_OUT_QUINT,\n... ).start()\n>>> options: RectOptions = {\'rectangle\': rectangle}\n>>> ap.Timer(on_timer, delay=750, options=options).start()\n```':  # noqa
    '',

    '':
    '',

    '## animation_play API':
    '',

    '<!-- Docstring: apysc._animation.animation_play_interface.AnimationPlayInterface.animation_play -->\n\n<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>\n\n**[Interface signature]** `animation_play(self) -> None`<hr>\n\n**[Interface summary]** Restart all paused animations.<hr>\n\n**[Examples]**':  # noqa
    '',

    '```py\n>>> from typing_extensions import TypedDict\n>>> import apysc as ap\n>>> class RectOptions(TypedDict):\n...     rectangle: ap.Rectangle\n>>> def on_timer_1(\n...         e: ap.TimerEvent,\n...         options: RectOptions) -> None:\n...     rectangle: ap.Rectangle = options[\'rectangle\']\n...     rectangle.animation_pause()\n>>> def on_timer_2(\n...         e: ap.TimerEvent,\n...         options: RectOptions) -> None:\n...     rectangle: ap.Rectangle = options[\'rectangle\']\n...     rectangle.animation_play()\n>>> stage: ap.Stage = ap.Stage()\n>>> sprite: ap.Sprite = ap.Sprite()\n>>> sprite.graphics.begin_fill(color=\'#0af\')\n>>> rectangle: ap.Rectangle = sprite.graphics.draw_rect(\n...     x=50, y=50, width=50, height=50)\n>>> _ = rectangle.animation_x(\n...     x=100,\n...     duration=1500,\n...     easing=ap.Easing.EASE_OUT_QUINT,\n... ).start()\n>>> options: RectOptions = {\'rectangle\': rectangle}\n>>> ap.Timer(on_timer_1, delay=500, options=options).start()\n>>> ap.Timer(on_timer_2, delay=1000, options=options).start()\n```':  # noqa
    '',

}
