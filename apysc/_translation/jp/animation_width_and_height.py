"""This module is for the translation mapping data of the
following document:

Document file: animation_width_and_height.md
Language: jp
"""

from typing import Dict

MAPPING: Dict[str, str] = {

    '# animation_width and animation_height interfaces':
    '',

    'This page explains the `animation_width` and `animation_height` interfaces.':  # noqa
    '',

    '## What interfaces are these?':
    '',

    'The `animation_width` method interface creates an `AnimationWidth` instance. You can animate object width with it.\n\nSimilarly, the `animation_height` method interface creates an `AnimationHeight` instance. You can animate object height with it.\n\nThese interfaces exist on some `DisplayObject` instances, such as the `Rectangle` class.':  # noqa
    '',

    '## Basic usage':
    '',

    'The following example sets the width animation (from 50 to 100) with the `animation_width` method:':  # noqa
    '',

    '```py\n# runnable\nimport apysc as ap\n\nDURATION: int = 1000\nEASING: ap.Easing = ap.Easing.EASE_OUT_QUINT\n\n\ndef on_animation_complete_1(\n        e: ap.AnimationEvent[ap.Rectangle], options: dict) -> None:\n    """\n    The handler that the animation calls when its end.\n\n    Parameters\n    ----------\n    e : ap.AnimationEvent\n        Event instance.\n    options : dict\n        Optional arguments dictionary.\n    """\n    rectangle: ap.Rectangle = e.this.target\n    animation_width: ap.AnimationWidth = rectangle.animation_width(\n        width=50, duration=DURATION, easing=EASING)\n    animation_width.animation_complete(on_animation_complete_2)\n    animation_width.start()\n\n\ndef on_animation_complete_2(\n        e: ap.AnimationEvent[ap.Rectangle], options: dict) -> None:\n    """\n    The handler that the animation calls when its end.\n\n    Parameters\n    ----------\n    e : ap.AnimationEvent\n        Event instance.\n    options : dict\n        Optional arguments dictionary.\n    """\n    rectangle: ap.Rectangle = e.this.target\n    animation_width: ap.AnimationWidth = rectangle.animation_width(\n        width=100, duration=DURATION, easing=EASING)\n    animation_width.animation_complete(on_animation_complete_1)\n    animation_width.start()\n\n\nap.Stage(\n    stage_width=200, stage_height=150,\n    background_color=\'#333\', stage_elem_id=\'stage\')\nsprite: ap.Sprite = ap.Sprite()\nsprite.graphics.begin_fill(color=\'#00aaff\')\nrectangle: ap.Rectangle = sprite.graphics.draw_rect(\n    x=50, y=50, width=50, height=50)\nanimation_width: ap.AnimationWidth = rectangle.animation_width(\n    width=100, duration=DURATION, easing=EASING)\nanimation_width.animation_complete(on_animation_complete_1)\nanimation_width.start()\n\nap.save_overall_html(\n    dest_dir_path=\'./animation_width_basic_usage/\')\n```':  # noqa
    '',

    '<iframe src="static/animation_width_basic_usage/index.html" width="200" height="150"></iframe>\n\nSimilarly, the following example animates the height with the `animation_height` method:':  # noqa
    '',

    '```py\n# runnable\nimport apysc as ap\n\nDURATION: int = 1000\nEASING: ap.Easing = ap.Easing.EASE_OUT_QUINT\n\n\ndef on_animation_complete_1(\n        e: ap.AnimationEvent[ap.Rectangle], options: dict) -> None:\n    """\n    The handler that the animation calls when its end.\n\n    Parameters\n    ----------\n    e : ap.AnimationEvent\n        Event instance.\n    options : dict\n        Optional arguments dictionary.\n    """\n    rectangle: ap.Rectangle = e.this.target\n    animation_height: ap.AnimationHeight = rectangle.animation_height(\n        height=50, duration=DURATION, easing=EASING)\n    animation_height.animation_complete(on_animation_complete_2)\n    animation_height.start()\n\n\ndef on_animation_complete_2(\n        e: ap.AnimationEvent[ap.Rectangle], options: dict) -> None:\n    """\n    The handler that the animation calls when its end.\n\n    Parameters\n    ----------\n    e : ap.AnimationEvent\n        Event instance.\n    options : dict\n        Optional arguments dictionary.\n    """\n    rectangle: ap.Rectangle = e.this.target\n    animation_height: ap.AnimationHeight = rectangle.animation_height(\n        height=100, duration=DURATION, easing=EASING)\n    animation_height.animation_complete(on_animation_complete_1)\n    animation_height.start()\n\n\nap.Stage(\n    stage_width=150, stage_height=200,\n    background_color=\'#333\', stage_elem_id=\'stage\')\nsprite: ap.Sprite = ap.Sprite()\nsprite.graphics.begin_fill(color=\'#00aaff\')\nrectangle: ap.Rectangle = sprite.graphics.draw_rect(\n    x=50, y=50, width=50, height=50)\nanimation_height: ap.AnimationHeight = rectangle.animation_height(\n    height=100, duration=DURATION, easing=EASING)\nanimation_height.animation_complete(on_animation_complete_1)\nanimation_height.start()\n\nap.save_overall_html(\n    dest_dir_path=\'./animation_height_basic_usage/\')\n```':  # noqa
    '',

    '<iframe src="static/animation_height_basic_usage/index.html" width="150" height="200"></iframe>':  # noqa
    '',

    '## Notes for the Ellipse instance':
    '',

    'The ellipse instance\'s `animation_width` and `animation_height` interfaces will return an `AnimationWidthForEllipse` and `AnimationHeightForEllipse` instance instead of an `AnimationWidth` instance, for the reason of the internal implementation, as follows:':  # noqa
    '',

    '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    stage_width=150, stage_height=200,\n    background_color=\'#333\', stage_elem_id=\'stage\')\nsprite: ap.Sprite = ap.Sprite()\nsprite.graphics.begin_fill(color=\'#00aaff\')\nellipse: ap.Ellipse = sprite.graphics.draw_ellipse(\n    x=100, y=100, width=100, height=100)\nanimation_width: ap.AnimationWidthForEllipse = ellipse.animation_width(\n    width=200, duration=1000)\nanimation_width.start()\n```':  # noqa
    '',

    '':
    '',

    '## animation_width API':
    '',

    '<!-- Docstring: apysc._animation.animation_width_interface.AnimationWidthInterface.animation_width -->\n\n<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>\n\n**[Interface signature]** `animation_width(self, width:Union[int, apysc._type.int.Int], *, duration:Union[int, apysc._type.int.Int]=3000, delay:Union[int, apysc._type.int.Int]=0, easing:apysc._animation.easing.Easing=<Easing.LINEAR: \'function(x) {return x;}\'>) -> apysc._animation.animation_width.AnimationWidth`<hr>\n\n**[Interface summary]** Set the width animation setting.<hr>\n\n**[Parameters]**\n\n- `width`: Int or int\n  - The final width of the animation.\n- `duration`: Int or int, default 3000\n  - Milliseconds before an animation ends.\n- `delay`: Int or int, default 0\n  - Milliseconds before an animation starts.\n- `easing`: Easing, default Easing.LINEAR\n  - Easing setting.\n\n<hr>\n\n**[Returns]**\n\n- `animation_width`: AnimationWidth\n  - Created animation setting instance.\n\n<hr>\n\n**[Notes]**\n\nTo start this animation, you need to call the `start` method of the returned instance.<hr>\n\n**[Examples]**':  # noqa
    '',

    '```py\n>>> import apysc as ap\n>>> stage: ap.Stage = ap.Stage()\n>>> sprite: ap.Sprite = ap.Sprite()\n>>> sprite.graphics.begin_fill(color=\'#0af\')\n>>> rectangle: ap.Rectangle = sprite.graphics.draw_rect(\n...     x=50, y=50, width=50, height=50)\n>>> _ = rectangle.animation_width(\n...     width=100,\n...     duration=1500,\n...     easing=ap.Easing.EASE_OUT_QUINT,\n... ).start()\n```':  # noqa
    '',

    '<hr>\n\n**[References]**\n\n- [Animation interfaces duration setting document](https://simon-ritchie.github.io/apysc/animation_duration.html)\n- [Animation interfaces delay setting document](https://simon-ritchie.github.io/apysc/animation_delay.html)\n- [Each animation interface return value document](https://simon-ritchie.github.io/apysc/animation_return_value.html)\n- [Sequential animation setting document](https://simon-ritchie.github.io/apysc/sequential_animation.html)\n- [animation_parallel interface document](https://simon-ritchie.github.io/apysc/animation_parallel.html)\n- [Easing enum document](https://simon-ritchie.github.io/apysc/easing_enum.html)':  # noqa
    '',

    '## animation_height API':
    '',

    '<!-- Docstring: apysc._animation.animation_height_interface.AnimationHeightInterface.animation_height -->\n\n<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>\n\n**[Interface signature]** `animation_height(self, height:Union[int, apysc._type.int.Int], *, duration:Union[int, apysc._type.int.Int]=3000, delay:Union[int, apysc._type.int.Int]=0, easing:apysc._animation.easing.Easing=<Easing.LINEAR: \'function(x) {return x;}\'>) -> apysc._animation.animation_height.AnimationHeight`<hr>\n\n**[Interface summary]** Set the height animation setting.<hr>\n\n**[Parameters]**\n\n- `height`: Int or int\n  - The final height of the animation.\n- `duration`: Int or int, default 3000\n  - Milliseconds before an animation ends.\n- `delay`: Int or int, default 0\n  - Milliseconds before an animation starts.\n- `easing`: Easing, default Easing.LINEAR\n  - Easing setting.\n\n<hr>\n\n**[Returns]**\n\n- `animation_height`: AnimationHeight\n  - Created animation setting instance.\n\n<hr>\n\n**[Notes]**\n\nTo start this animation, you need to call the `start` method of the returned instance.<hr>\n\n**[Examples]**':  # noqa
    '',

    '```py\n>>> import apysc as ap\n>>> stage: ap.Stage = ap.Stage()\n>>> sprite: ap.Sprite = ap.Sprite()\n>>> sprite.graphics.begin_fill(color=\'#0af\')\n>>> rectangle: ap.Rectangle = sprite.graphics.draw_rect(\n...     x=50, y=50, width=50, height=50)\n>>> _ = rectangle.animation_height(\n...     height=100,\n...     duration=1500,\n...     easing=ap.Easing.EASE_OUT_QUINT,\n... ).start()\n```':  # noqa
    '',

    '<hr>\n\n**[References]**\n\n- [Animation interfaces duration setting document](https://simon-ritchie.github.io/apysc/animation_duration.html)\n- [Animation interfaces delay setting document](https://simon-ritchie.github.io/apysc/animation_delay.html)\n- [Each animation interface return value document](https://simon-ritchie.github.io/apysc/animation_return_value.html)\n- [Sequential animation setting document](https://simon-ritchie.github.io/apysc/sequential_animation.html)\n- [animation_parallel interface document](https://simon-ritchie.github.io/apysc/animation_parallel.html)\n- [Easing enum document](https://simon-ritchie.github.io/apysc/easing_enum.html)':  # noqa
    '',

}
