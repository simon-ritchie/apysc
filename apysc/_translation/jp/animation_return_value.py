"""This module is for the translation mapping data of the
following document:

Document file: animation_return_value.md
Language: jp
"""

from typing import Dict

MAPPING: Dict[str, str] = {

    '# Each animation interface return value':
    '',

    'This page explains each animation interface, such as the `animation_move`\\, return value (`AnimationBase` instance).':  # noqa
    '',

    '## Each interface returns the subclass instance of the AnimationBase':
    '',

    'Each animation interface returns the subclass instance of the `AnimationBase`\\. So, for example, the `animation_move` interface returns the `AnimationMove` instance, and the `animation_x` interface  returns the `AnimationX` instance.\n\nThe `AnimationBase` class has the standard animation interfaces, such as the `start` (method to start animation), `animation_complete` (method to bind the animation completion event), `target` (property of the animation target).':  # noqa
    '',

    '## Basic usage':
    '',

    'Each return value class is in the apysc package (e.g., `ap.AnimationMove`). Therefore, you can set the type annotation with it.\n\nThe following code example uses the `animation_x` method interface. And You get an `AnimationX` instance to start and bind the animation completion event with it.':  # noqa
    '',

    '```py\n# runnable\nimport apysc as ap\n\nDURATION: int = 1000\n\n\ndef on_animation_complete_1(\n        e: ap.AnimationEvent[ap.Rectangle],\n        options: dict) -> None:\n    """\n    The handler that the animation calls when its end.\n\n    Parameters\n    ----------\n    e : ap.AnimationEvent\n        Event instance.\n    options : dict\n        Optional arguments dictionary.\n    """\n    rectangle: ap.Rectangle = e.this.target\n    animation_x: ap.AnimationX = rectangle.animation_x(\n        x=50, duration=DURATION)\n    animation_x.animation_complete(on_animation_complete_2)\n    animation_x.start()\n\n\ndef on_animation_complete_2(\n        e: ap.AnimationEvent[ap.Rectangle],\n        options: dict) -> None:\n    """\n    The handler that the animation calls when its end.\n\n    Parameters\n    ----------\n    e : ap.AnimationEvent\n        Event instance.\n    options : dict\n        Optional arguments dictionary.\n    """\n    rectangle: ap.Rectangle = e.this.target\n    animation_x: ap.AnimationX = rectangle.animation_x(\n        x=100, duration=DURATION)\n    animation_x.animation_complete(on_animation_complete_1)\n    animation_x.start()\n\n\nap.Stage(\n    stage_width=200, stage_height=150, background_color=\'#333\',\n    stage_elem_id=\'stage\')\nsprite: ap.Sprite = ap.Sprite()\nsprite.graphics.begin_fill(color=\'#0af\')\nrectangle: ap.Rectangle = sprite.graphics.draw_rect(\n    x=50, y=50, width=50, height=50)\nanimation_x: ap.AnimationX = rectangle.animation_x(\n    x=100, duration=DURATION)\nanimation_x.animation_complete(on_animation_complete_1)\nanimation_x.start()\n\nap.save_overall_html(\n    dest_dir_path=\'./animation_return_value_basic_usage/\')\n```':  # noqa
    '',

    '<iframe src="static/animation_return_value_basic_usage/index.html" width="200" height="150"></iframe>':  # noqa
    '',

}
