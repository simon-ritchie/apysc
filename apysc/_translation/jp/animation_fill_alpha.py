"""This module is for the translation mapping data of the
following document:

Document file: animation_fill_alpha.md
Language: jp
"""

from typing import Dict

MAPPING: Dict[str, str] = {

    '# animation_fill_alpha interface':
    '',

    'This page explains the `animation_fill_alpha` method interface.':
    '',

    '## What interface is this?':
    '',

    'The `animation_fill_alpha` method interface creates an `ap.AnimationFillAlpha` instance (animation setting instance and the  `AnimationBase` subclass). You can animate fill alpha (opacity) with it.\n\nThis interface exists on a `GraphicsBase` subclass, such as the `Rectangle` or `Circle` class.':  # noqa
    '',

    '## Basic usage':
    '',

    'The following example sets the fill alpha animation (from 1.0 to 0.0) with the `animation_fill_alpha` method:':  # noqa
    '',

    '```py\n# runnable\nimport apysc as ap\n\nDURATION: int = 1000\n\n\ndef on_animation_complete_1(\n        e: ap.AnimationEvent[ap.Rectangle], options: dict) -> None:\n    """\n    The handler that animation calls when its end.\n\n    Parameters\n    ----------\n    e : AnimationEvent\n        Event instance.\n    options : dict\n        Optional arguments dictionary.\n    """\n    rectangle: ap.Rectangle = e.this.target\n    rectangle.animation_fill_alpha(\n        alpha=1.0, duration=DURATION,\n    ).animation_complete(on_animation_complete_2).start()\n\n\ndef on_animation_complete_2(\n        e: ap.AnimationEvent[ap.Rectangle], options: dict) -> None:\n    """\n    The handler that animation calls when its end.\n\n    Parameters\n    ----------\n    e : AnimationEvent\n        Event instance.\n    options : dict\n        Optional arguments dictionary.\n    """\n    rectangle: ap.Rectangle = e.this.target\n    rectangle.animation_fill_alpha(\n        alpha=0.0, duration=DURATION,\n    ).animation_complete(on_animation_complete_1).start()\n\n\nap.Stage(\n    stage_width=150, stage_height=150,\n    background_color=\'#333\', stage_elem_id=\'stage\')\nsprite: ap.Sprite = ap.Sprite()\nsprite.graphics.begin_fill(color=\'#00aaff\')\nrectangle: ap.Rectangle = sprite.graphics.draw_rect(\n    x=50, y=50, width=50, height=50)\nrectangle.animation_fill_alpha(\n    alpha=0.0, duration=DURATION,\n).animation_complete(on_animation_complete_1).start()\n\nap.save_overall_html(\n    dest_dir_path=\'./animation_fill_alpha_basic_usage/\')\n```':  # noqa
    '',

    '<iframe src="static/animation_fill_alpha_basic_usage/index.html" width="150" height="150"></iframe>':  # noqa
    '',

    '## animation_fill_alpha API':
    '',

    '<!-- Docstring: apysc._animation.animation_fill_alpha_interface.AnimationFillAlphaInterface.animation_fill_alpha -->\n\n<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>\n\n**[Interface signature]** `animation_fill_alpha(self, alpha:Union[float, apysc._type.number.Number], *, duration:Union[int, apysc._type.int.Int]=3000, delay:Union[int, apysc._type.int.Int]=0, easing:apysc._animation.easing.Easing=<Easing.LINEAR: \'function(x) {return x;}\'>) -> apysc._animation.animation_fill_alpha.AnimationFillAlpha`<hr>\n\n**[Interface summary]** Set the fill alpha (opacity) animation setting.<hr>\n\n**[Parameters]**\n\n- `alpha`: Number or float\n  - The final alpha (opacity) of the animation.\n- `duration`: Int or int, default 3000\n  - Milliseconds before an animation ends.\n- `delay`: Int or int, default 0\n  - Milliseconds before an animation starts.\n- `easing`: Easing, default Easing.LINEAR\n  - Easing setting.\n\n<hr>\n\n**[Returns]**\n\n- `animation_fill_alpha`: AnimationFillAlpha\n  - Created animation setting instance.\n\n<hr>\n\n**[Notes]**\n\nTo start this animation, you need to call the `start` method of the returned instance.<hr>\n\n**[Examples]**':  # noqa
    '',

    '```py\n>>> import apysc as ap\n>>> stage: ap.Stage = ap.Stage()\n>>> sprite: ap.Sprite = ap.Sprite()\n>>> sprite.graphics.begin_fill(color=\'#0af\')\n>>> circle: ap.Circle = sprite.graphics.draw_circle(\n...     x=100, y=100, radius=50)\n>>> _ = circle.animation_y(\n...     y=100,\n...     duration=1500,\n...     easing=ap.Easing.EASE_OUT_QUINT,\n... ).start()\n```':  # noqa
    '',

    '<hr>\n\n**[References]**\n\n- [Animation interfaces duration setting document](https://simon-ritchie.github.io/apysc/animation_duration.html)\n- [Each animation interface return value document](https://simon-ritchie.github.io/apysc/animation_return_value.html)\n- [Sequential animation setting document](https://simon-ritchie.github.io/apysc/sequential_animation.html)\n- [animation_parallel interface document](https://simon-ritchie.github.io/apysc/animation_parallel.html)\n- [Easing enum document](https://simon-ritchie.github.io/apysc/easing_enum.html)':  # noqa
    '',

}
