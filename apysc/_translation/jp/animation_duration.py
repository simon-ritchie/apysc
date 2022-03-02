"""This module is for the translation mapping data of the
following document:

Document file: animation_duration.md
Language: jp
"""

from typing import Dict

MAPPING: Dict[str, str] = {

    '# Animation interfaces duration setting':
    '',

    'This page explains the animation interfaces `duration` setting.':
    '',

    '## What setting is this?':
    '',

    'The `duration` setting determines the animation time from start to end in milliseconds. For instance, if you specify 3000 to the `duration` argument, the animation takes 3 seconds to complete.\n\nEach animation method interface (such as the `animation_move`\\, `animation_x`\\, and so on) has the `duration` argument.':  # noqa
    '',

    '## Basic usage':
    '',

    'The following example sets 3 seconds to the `duration` option and animates x-coordinate.':  # noqa
    '',

    '```py\n# runnable\nimport apysc as ap\n\nDURATION: int = 3000\nEASING: ap.Easing = ap.Easing.EASE_OUT_QUINT\n\n\ndef on_animation_complete_1(\n        e: ap.AnimationEvent[ap.Rectangle],\n        options: dict) -> None:\n    """\n    The handler that animation calls when its end.\n\n    Parameters\n    ----------\n    e : ap.AnimationEvent\n        Event instance.\n    options : dict\n        Optional arguments dictionary.\n    """\n    rectangle: ap.Rectangle = e.this.target\n    animation_x: ap.AnimationX = rectangle.animation_x(\n        x=50, duration=DURATION, easing=EASING)\n    animation_x.animation_complete(on_animation_complete_2)\n    animation_x.start()\n\n\ndef on_animation_complete_2(\n        e: ap.AnimationEvent[ap.Rectangle], options: dict) -> None:\n    """\n    The handler that animation calls when its end.\n\n    Parameters\n    ----------\n    e : ap.AnimationEvent\n        Event instance.\n    options : dict\n        Optional arguments dictionary.\n    """\n    rectangle: ap.Rectangle = e.this.target\n    animation_x: ap.AnimationX = rectangle.animation_x(\n        x=400, duration=DURATION, easing=EASING)\n    animation_x.animation_complete(on_animation_complete_1)\n    animation_x.start()\n\n\nap.Stage(\n    stage_width=500, stage_height=150, background_color=\'#333\',\n    stage_elem_id=\'stage\')\nsprite: ap.Sprite = ap.Sprite()\nsprite.graphics.begin_fill(color=\'#0af\')\nrectangle: ap.Rectangle = sprite.graphics.draw_rect(\n    x=50, y=50, width=50, height=50)\n\nanimation_x: ap.AnimationX = rectangle.animation_x(\n    x=400, duration=DURATION, easing=EASING)\nanimation_x.animation_complete(on_animation_complete_1)\nanimation_x.start()\n\nap.save_overall_html(\n    dest_dir_path=\'./animation_duration_basic_usage/\')\n```':  # noqa
    '',

    '<iframe src="static/animation_duration_basic_usage/index.html" width="500" height="150"></iframe>':  # noqa
    '',

}
