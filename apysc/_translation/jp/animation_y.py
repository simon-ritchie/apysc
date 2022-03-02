"""This module is for the translation mapping data of the
following document:

Document file: animation_y.md
Language: jp
"""

from typing import Dict

MAPPING: Dict[str, str] = {

    '# animation_y interface':
    '',

    'This page explains the `animation_y` method interface.':
    '',

    '## What interface is this?':
    '',

    'The `animation_y` method interface creates an `AnimationY` instance. You can animate y-coordinate with it.\n\nThis interface exists on a `DisplayObject` subclass instance, such as the `Sprite` or `Rectangle`.':  # noqa
    '',

    '## Basic usage':
    '',

    'The following example sets the y-coordinate animation (from 50 to 100) with the `animation_y` method.':  # noqa
    '',

    '```py\n# runnable\nimport apysc as ap\n\nEASING: ap.Easing = ap.Easing.EASE_OUT_QUINT\nDURATION: int = 1000\n\n\ndef on_animation_complete_1(\n        e: ap.AnimationEvent[ap.Rectangle], options: dict) -> None:\n    """\n    The handler that the animation calls when its end.\n\n    Parameters\n    ----------\n    e : ap.AnimationEvent\n        Event instance.\n    options : dict\n        Optional arguments dictionary.\n    """\n    rectangle: ap.Rectangle = e.this.target\n    animation_y: ap.AnimationY = rectangle.animation_y(\n        y=50, duration=DURATION, easing=EASING)\n    animation_y.animation_complete(on_animation_complete_2)\n    animation_y.start()\n\n\ndef on_animation_complete_2(\n        e: ap.AnimationEvent[ap.Rectangle], options: dict) -> None:\n    """\n    The handler that the animation calls when its end.\n\n    Parameters\n    ----------\n    e : ap.AnimationEvent\n        Event instance.\n    options : dict\n        Optional arguments dictionary.\n    """\n    rectangle: ap.Rectangle = e.this.target\n    animation_y: ap.AnimationY = rectangle.animation_y(\n        y=100, duration=DURATION, easing=EASING)\n    animation_y.animation_complete(on_animation_complete_1)\n    animation_y.start()\n\n\nap.Stage(\n    stage_width=150, stage_height=200,\n    background_color=\'#333\', stage_elem_id=\'stage\')\nsprite: ap.Sprite = ap.Sprite()\nsprite.graphics.begin_fill(color=\'#00aaff\')\nrectangle: ap.Rectangle = sprite.graphics.draw_rect(\n    x=50, y=50, width=50, height=50)\nanimation_y: ap.AnimationY = rectangle.animation_y(\n    y=100, duration=DURATION, easing=EASING)\nanimation_y.animation_complete(on_animation_complete_1)\nanimation_y.start()\n\nap.save_overall_html(\n    dest_dir_path=\'./animation_y_basic_usage/\')\n```':  # noqa
    '',

    '<iframe src="static/animation_y_basic_usage/index.html" width="150" height="200"></iframe>':  # noqa
    '',

    '## Notes for the Circle and Ellipse classes':
    '',

    'The `Circle` and `Ellipse` classes\' `animation_y` interface will return an `AnimationCy` (center-y) class instance, instead of a `AnimationY` instance, for internal implementation reason.':  # noqa
    '',

    '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    stage_width=200, stage_height=150,\n    background_color=\'#333\', stage_elem_id=\'stage\')\nsprite: ap.Sprite = ap.Sprite()\nsprite.graphics.begin_fill(color=\'#00aaff\')\ncircle: ap.Circle = sprite.graphics.draw_circle(x=100, y=100, radius=50)\nanimation_cy: ap.AnimationCy = circle.animation_y(\n    y=100, duration=1000, easing=ap.Easing.EASE_OUT_QUINT)\n```':  # noqa
    '',

    '':
    '',

    '## animation_y API':
    '',

    '<!-- Docstring: apysc._animation.animation_y_interface.AnimationYInterface.animation_y -->\n\n<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>\n\n**[Interface signature]** `animation_y(self, y:Union[int, apysc._type.int.Int], *, duration:Union[int, apysc._type.int.Int]=3000, delay:Union[int, apysc._type.int.Int]=0, easing:apysc._animation.easing.Easing=<Easing.LINEAR: \'function(x) {return x;}\'>) -> apysc._animation.animation_y.AnimationY`<hr>\n\n**[Interface summary]** Set the y-coordinate animation setting.<hr>\n\n**[Parameters]**\n\n- `y`: Int or int\n  - Destination of the y-coordinate.\n- `duration`: Int or int, default 3000\n  - Milliseconds before an animation ends.\n- `delay`: Int or int, default 0\n  - Milliseconds before an animation starts.\n- `easing`: Easing, default Easing.LINEAR\n  - Easing setting.\n\n<hr>\n\n**[Returns]**\n\n- `animation_y`: AnimationY\n  - Created animation setting instance.\n\n<hr>\n\n**[Notes]**\n\nTo start this animation, you need to call the `start` method of the returned instance.<hr>\n\n**[Examples]**':  # noqa
    '',

    '```py\n>>> import apysc as ap\n>>> stage: ap.Stage = ap.Stage()\n>>> sprite: ap.Sprite = ap.Sprite()\n>>> sprite.graphics.begin_fill(color=\'#0af\')\n>>> rectangle: ap.Rectangle = sprite.graphics.draw_rect(\n...     x=50, y=50, width=50, height=50)\n>>> _ = rectangle.animation_y(\n...     y=100,\n...     duration=1500,\n...     easing=ap.Easing.EASE_OUT_QUINT,\n... ).start()\n```':  # noqa
    '',

    '<hr>\n\n**[References]**\n\n- [Animation interfaces duration setting document](https://simon-ritchie.github.io/apysc/animation_duration.html)\n- [Animation interfaces delay setting document](https://simon-ritchie.github.io/apysc/animation_delay.html)\n- [Each animation interface return value document](https://simon-ritchie.github.io/apysc/animation_return_value.html)\n- [Sequential animation setting document](https://simon-ritchie.github.io/apysc/sequential_animation.html)\n- [animation_parallel interface document](https://simon-ritchie.github.io/apysc/animation_parallel.html)\n- [Easing enum document](https://simon-ritchie.github.io/apysc/easing_enum.html)':  # noqa
    '',

}
