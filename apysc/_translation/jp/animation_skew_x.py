"""This module is for the translation mapping data of the
following document:

Document file: animation_skew_x.md
Language: jp
"""

from typing import Dict

MAPPING: Dict[str, str] = {

    '# animation_skew_x interface':
    '',

    'This page explains the `animation_skew_x` method interface.':
    '',

    '## What interface is this?':
    '',

    'The `animation_skew_x` method interface creates an `ap.AnimationSkewX` instance. You can animate x-directional skewing with it.\n\nThis interface exists on a `GraphicsBase` subclass, such as the `Rectangle` class.':  # noqa
    '',

    '## Basic usage':
    '',

    'The following example sets the skew-x animation (from 0 to 50) with the `animation_skew_x` method:':  # noqa
    '',

    '```py\n# runnable\nimport apysc as ap\n\nDURATION: int = 1000\nEASING: ap.Easing = ap.Easing.EASE_OUT_QUINT\n\n\ndef on_animation_complete_1(\n        e: ap.AnimationEvent[ap.Rectangle], options: dict) -> None:\n    """\n    The handler that the animation calls when its end.\n\n    Parameters\n    ----------\n    e : AnimationEvent\n        Event instance.\n    options : dict\n        Optional arguments dictionary.\n    """\n    rectangle: ap.Rectangle = e.this.target\n    rectangle.animation_skew_x(\n        skew_x=0,\n        duration=DURATION,\n        easing=EASING,\n    ).animation_complete(on_animation_complete_2).start()\n\n\ndef on_animation_complete_2(\n        e: ap.AnimationEvent[ap.Rectangle], options: dict) -> None:\n    """\n    The handler that the animation calls when its end.\n\n    Parameters\n    ----------\n    e : AnimationEvent\n        Event instance.\n    options : dict\n        Optional arguments dictionary.\n    """\n    rectangle: ap.Rectangle = e.this.target\n    rectangle.animation_skew_x(\n        skew_x=50,\n        duration=DURATION,\n        easing=EASING,\n    ).animation_complete(on_animation_complete_1).start()\n\n\nap.Stage(\n    stage_width=150, stage_height=150,\n    background_color=\'#333\', stage_elem_id=\'stage\')\nsprite: ap.Sprite = ap.Sprite()\nsprite.graphics.begin_fill(color=\'#0af\')\nrectangle: ap.Rectangle = sprite.graphics.draw_rect(\n    x=50, y=50, width=50, height=50)\n\nrectangle.animation_skew_x(\n    skew_x=50,\n    duration=DURATION,\n    easing=EASING,\n).animation_complete(on_animation_complete_1).start()\n\nap.save_overall_html(\n    dest_dir_path=\'./animation_skew_x_basic_usage/\')\n```':  # noqa
    '',

    '<iframe src="static/animation_skew_x_basic_usage/index.html" width="150" height="150"></iframe>':  # noqa
    '',

    '## animation_skew_x API':
    '',

    '<!-- Docstring: apysc._animation.animation_skew_x_interface.AnimationSkewXInterface.animation_skew_x -->\n\n<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>\n\n**[Interface signature]** `animation_skew_x(self, skew_x:Union[int, apysc._type.int.Int], *, duration:Union[int, apysc._type.int.Int]=3000, delay:Union[int, apysc._type.int.Int]=0, easing:apysc._animation.easing.Easing=<Easing.LINEAR: \'function(x) {return x;}\'>) -> apysc._animation.animation_skew_x.AnimationSkewX`<hr>\n\n**[Interface summary]** Set the skew-x animation setting.<hr>\n\n**[Parameters]**\n\n- `skew_x`: Int or int\n  - The final skew-x of the animation.\n- `duration`: Int or int, default 3000\n  - Milliseconds before an animation ends.\n- `delay`: Int or int, default 0\n  - Milliseconds before an animation starts.\n- `easing`: Easing, default Easing.LINEAR\n  - Easing setting.\n\n<hr>\n\n**[Returns]**\n\n- `animation_skew_x`: AnimationSkewX\n  - Created animation setting instance.\n\n<hr>\n\n**[Notes]**\n\nTo start this animation, you need to call the `start` method of the returned instance.<hr>\n\n**[Examples]**':  # noqa
    '',

    '```py\n>>> import apysc as ap\n>>> stage: ap.Stage = ap.Stage()\n>>> sprite: ap.Sprite = ap.Sprite()\n>>> sprite.graphics.begin_fill(color=\'#0af\')\n>>> rectangle: ap.Rectangle = sprite.graphics.draw_rect(\n...     x=50, y=50, width=50, height=50)\n>>> _ = rectangle.animation_skew_x(\n...     skew_x=50,\n...     duration=1500,\n...     easing=ap.Easing.EASE_OUT_QUINT,\n... ).start()\n```':  # noqa
    '',

    '<hr>\n\n**[References]**\n\n- [Animation interfaces duration setting document](https://simon-ritchie.github.io/apysc/animation_duration.html)\n- [Animation interfaces delay setting document](https://simon-ritchie.github.io/apysc/animation_delay.html)\n- [Each animation interface return value document](https://simon-ritchie.github.io/apysc/animation_return_value.html)\n- [Sequential animation setting document](https://simon-ritchie.github.io/apysc/sequential_animation.html)\n- [animation_parallel interface document](https://simon-ritchie.github.io/apysc/animation_parallel.html)\n- [Easing enum document](https://simon-ritchie.github.io/apysc/easing_enum.html)':  # noqa
    '',

}
