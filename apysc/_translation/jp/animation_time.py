"""This module is for the translation mapping data of the
following document:

Document file: animation_time.md
Language: jp
"""

from typing import Dict

MAPPING: Dict[str, str] = {

    '# animation_time interface':
    '',

    'This page explains the `animation_time` method interface.':
    '',

    '## What interface is this?':
    '',

    'The `animation_time` interface returns the current animation elapsed time in milliseconds (`Number` type value).':  # noqa
    '',

    '## Basic usage':
    '',

    'The following example sets the x-coordinate animation of the rectangle and the 1-second interval timer to display an animation\'s current elapsed time to console (please press the F12 key).':  # noqa
    '',

    '```py\n# runnable\nfrom typing_extensions import TypedDict\n\nimport apysc as ap\n\n\nclass _RectOptions(TypedDict):\n    rectangle: ap.Rectangle\n\n\ndef on_timer(e: ap.TimerEvent, options: _RectOptions) -> None:\n    """\n    The handler that the animation calls.\n\n    Parameters\n    ----------\n    e : ap.TimerEvent\n        Event instance.\n    options : dict\n        Optional arguments dictionary.\n    """\n    rectangle: ap.Rectangle = options[\'rectangle\']\n    ap.trace(\'Animation elapsed time:\', rectangle.animation_time())\n\n\nap.Stage(\n    stage_width=500, stage_height=150, background_color=\'#333\',\n    stage_elem_id=\'stage\')\nsprite: ap.Sprite = ap.Sprite()\nsprite.graphics.begin_fill(color=\'#0af\')\n\nrectangle: ap.Rectangle = sprite.graphics.draw_rect(\n    x=50, y=50, width=50, height=50)\nrectangle.animation_x(x=400, duration=10000).start()\n\noptions: _RectOptions = {\'rectangle\': rectangle}\nap.Timer(on_timer, delay=1000, options=options).start()\n\nap.save_overall_html(\n    dest_dir_path=\'animation_time_basic_usage/\')\n```':  # noqa
    '',

    '<iframe src="static/animation_time_basic_usage/index.html" width="500" height="150"></iframe>':  # noqa
    '',

    '## animation_time property API':
    '',

    '<!-- Docstring: apysc._animation.animation_time_interface.AnimationTimeInterface.animation_time -->\n\n<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>\n\n**[Interface signature]** `animation_time(self) -> apysc._type.number.Number`<hr>\n\n**[Interface summary]** Get an animation elapsed millisecond.<hr>\n\n**[Returns]**\n\n- `elapsed_time`: Number\n  - An animation elapsed millisecond.\n\n<hr>\n\n**[Examples]**':  # noqa
    '',

    '```py\n>>> from typing_extensions import TypedDict\n>>> import apysc as ap\n>>> class RectOptions(TypedDict):\n...     rectangle: ap.Rectangle\n>>> def on_timer(\n...         e: ap.TimerEvent,\n...         options: RectOptions) -> None:\n...     rectangle: ap.Rectangle = options[\'rectangle\']\n...     animation_time: ap.Number = rectangle.animation_time()\n...     ap.trace(\'animation_time:\', animation_time)\n>>> stage: ap.Stage = ap.Stage()\n>>> sprite: ap.Sprite = ap.Sprite()\n>>> sprite.graphics.begin_fill(color=\'#0af\')\n>>> rectangle: ap.Rectangle = sprite.graphics.draw_rect(\n...     x=50, y=50, width=50, height=50)\n>>> _ = rectangle.animation_x(\n...     x=100,\n...     duration=1500,\n...     easing=ap.Easing.EASE_OUT_QUINT,\n... ).start()\n>>> options: RectOptions = {\'rectangle\': rectangle}\n>>> ap.Timer(\n...     on_timer, delay=ap.FPS.FPS_60,\n...     options=options).start()\n```':  # noqa
    '',

}
