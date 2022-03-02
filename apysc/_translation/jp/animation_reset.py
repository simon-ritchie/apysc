"""This module is for the translation mapping data of the
following document:

Document file: animation_reset.md
Language: jp
"""

from typing import Dict

MAPPING: Dict[str, str] = {

    '# animation_reset interface':
    '',

    'This page explains the `animation_reset` method interface.':
    '',

    '## What interface is this?':
    '',

    'The `animation_reset` interface resets all animations and stop.\n\nThis interface exists in the instances that have the animation interfaces (such as the `animation_x`\\, `animation_move`).':  # noqa
    '',

    '## Basic usage':
    '',

    'The following example sets the click event to the rectangle. If you click the rectangle, the x-coordinate animation starts. After 1 second has passed, the `animation_reset` interface resets the x-coordinate animation:':  # noqa
    '',

    '```py\n# runnable\nfrom typing_extensions import TypedDict\n\nimport apysc as ap\n\n\nclass _RectOptions(TypedDict):\n    rectangle: ap.Rectangle\n\n\ndef on_click(e: ap.MouseEvent[ap.Rectangle], options: dict) -> None:\n    """\n    The handler that the rectangle calls when clicked.\n\n    Parameters\n    ----------\n    e : ap.Rectangle\n        Event instance.\n    options : dict\n        Optional arguments dictionary.\n    """\n    e.this.animation_x(x=500, duration=3000).start()\n    options_: _RectOptions = {\'rectangle\': e.this}\n    timer: ap.Timer = ap.Timer(\n        on_timer, delay=1000, repeat_count=1, options=options_)\n    timer.start()\n\n\ndef on_timer(e: ap.TimerEvent, options: _RectOptions) -> None:\n    """\n    The handler that the timer calls.\n\n    Parameters\n    ----------\n    e : ap.TimerEvent\n        Event instance.\n    options : _RectOptions\n        Optional arguments dictionary.\n    """\n    options[\'rectangle\'].animation_reset()\n\n\nap.Stage(\n    stage_width=600, stage_height=150,\n    background_color=\'#333\', stage_elem_id=\'stage\')\nsprite: ap.Sprite = ap.Sprite()\nsprite.graphics.begin_fill(color=\'#00aaff\')\nrectangle: ap.Rectangle = sprite.graphics.draw_rect(\n    x=50, y=50, width=50, height=50)\nrectangle.click(on_click)\n\nap.save_overall_html(\n    dest_dir_path=\'./animation_reset_basic_usage/\')\n```':  # noqa
    '',

    '<iframe src="static/animation_reset_basic_usage/index.html" width="600" height=150></iframe>':  # noqa
    '',

    '## animation_reset API':
    '',

    '<!-- Docstring: apysc._animation.animation_reset_interface.AnimationResetInterface.animation_reset -->\n\n<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>\n\n**[Interface signature]** `animation_reset(self) -> None`<hr>\n\n**[Interface summary]** Stop all animations and reset.<hr>\n\n**[Examples]**':  # noqa
    '',

    '```py\n>>> from typing_extensions import TypedDict\n>>> import apysc as ap\n>>> class RectOptions(TypedDict):\n...     rectangle: ap.Rectangle\n>>> def on_timer(\n...         e: ap.TimerEvent,\n...         options: RectOptions) -> None:\n...     rectangle: ap.Rectangle = options[\'rectangle\']\n...     rectangle.animation_reset()\n>>> stage: ap.Stage = ap.Stage()\n>>> sprite: ap.Sprite = ap.Sprite()\n>>> sprite.graphics.begin_fill(color=\'#0af\')\n>>> rectangle: ap.Rectangle = sprite.graphics.draw_rect(\n...     x=50, y=50, width=50, height=50)\n>>> _ = rectangle.animation_x(\n...     x=100,\n...     duration=1500,\n...     easing=ap.Easing.EASE_OUT_QUINT,\n... ).start()\n>>> options: RectOptions = {\'rectangle\': rectangle}\n>>> ap.Timer(on_timer, delay=750, options=options).start()\n```':  # noqa
    '',

}
