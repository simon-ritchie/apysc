"""This module is for the translation mapping data of the
following document:

Document file: animation_scale_x_and_y_from_center.md
Language: jp
"""

from typing import Dict

MAPPING: Dict[str, str] = {

    '# animation_scale_x_from_center and animation_scale_y_from_center interfaces':  # noqa
    '',

    'This page explains the `animation_scale_x_from_center` and `animation_scale_y_from_center` method interfaces.':  # noqa
    '',

    '## What interfaces are these?':
    '',

    'The `animation_scale_x_from_center` method interface creates an `ap.AnimationScaleXFromCenter` instance. You can animate x-direction\'s scale with it.\n\nSimilarly, the `animation_scale_y_from_center` method interface creates an `ap.AnimationScaleYFromCenter` instance. You can animate y-direction\'s scale with it.\n\nThese interfaces exist on a `GraphicsBase` subclass (that has the `scale_x_from_center` and `scale_y_from_center` interfaces), such as the `Rectangle` or `Circle`.':  # noqa
    '',

    '## Basic usage':
    '',

    'The following example sets the scale-x (left-side rectangle) and scale-y (right-side rectangle) animation (from 1.0 to 2.0) with the `animation_scale_x_from_center` and `animation_scale_y_from_center` methods:':  # noqa
    '',

    '```py\n# runnable\nfrom enum import Enum\n\nfrom typing_extensions import TypedDict\n\nimport apysc as ap\n\nDURATION: int = 1000\nEASING: ap.Easing = ap.Easing.EASE_OUT_QUINT\n\n\nclass Direction(Enum):\n    X = 1\n    Y = 2\n\n\nclass Options(TypedDict):\n    direction: Direction\n\n\ndef on_animation_complete_1(\n        e: ap.AnimationEvent[ap.Rectangle], options: Options) -> None:\n    """\n    The handler that the animation calls when its end.\n\n    Parameters\n    ----------\n    e : AnimationEvent\n        Event instance.\n    options : dict\n        Optional arguments dictionary.\n    """\n    rectangle: ap.Rectangle = e.this.target\n    SCALE: float = 1.0\n    if options[\'direction\'] == Direction.X:\n        rectangle.animation_scale_x_from_center(\n            scale_x_from_center=SCALE,\n            duration=DURATION,\n            easing=EASING,\n        ).animation_complete(\n            on_animation_complete_2,\n            options=options,\n        ).start()\n    elif options[\'direction\'] == Direction.Y:\n        rectangle.animation_scale_y_from_center(\n            scale_y_from_center=SCALE,\n            duration=DURATION,\n            easing=EASING,\n        ).animation_complete(\n            on_animation_complete_2,\n            options=options,\n        ).start()\n\n\ndef on_animation_complete_2(\n        e: ap.AnimationEvent[ap.Rectangle], options: Options) -> None:\n    """\n    The handler that the animation calls when its end.\n\n    Parameters\n    ----------\n    e : AnimationEvent\n        Event instance.\n    options : dict\n        Optional arguments dictionary.\n    """\n    rectangle: ap.Rectangle = e.this.target\n    SCALE: float = 2.0\n    if options[\'direction\'] == Direction.X:\n        rectangle.animation_scale_x_from_center(\n            scale_x_from_center=SCALE,\n            duration=DURATION,\n            easing=EASING,\n        ).animation_complete(\n            on_animation_complete_1,\n            options=options,\n        ).start()\n    elif options[\'direction\'] == Direction.Y:\n        rectangle.animation_scale_y_from_center(\n            scale_y_from_center=SCALE,\n            duration=DURATION,\n            easing=EASING,\n        ).animation_complete(\n            on_animation_complete_1,\n            options=options,\n        ).start()\n\n\nap.Stage(\n    stage_width=250, stage_height=150,\n    background_color=\'#333\', stage_elem_id=\'stage\')\nsprite: ap.Sprite = ap.Sprite()\nsprite.graphics.begin_fill(color=\'#0af\')\nleft_rectangle: ap.Rectangle = sprite.graphics.draw_rect(\n    x=50, y=50, width=50, height=50)\nright_rectangle: ap.Rectangle = sprite.graphics.draw_rect(\n    x=150, y=50, width=50, height=50)\n\noptions: Options = {\'direction\': Direction.X}\nleft_rectangle.animation_scale_x_from_center(\n    scale_x_from_center=2.0,\n    duration=DURATION,\n    easing=EASING,\n).animation_complete(\n    on_animation_complete_1,\n    options=options,\n).start()\n\noptions = {\'direction\': Direction.Y}\nright_rectangle.animation_scale_y_from_center(\n    scale_y_from_center=2.0,\n    duration=DURATION,\n    easing=EASING,\n).animation_complete(\n    on_animation_complete_1,\n    options=options,\n).start()\n\nap.save_overall_html(\n    dest_dir_path=\'./animation_scale_x_and_y_from_center_basic_usage/\')\n```':  # noqa
    '',

    '<iframe src="static/animation_scale_x_and_y_from_center_basic_usage/index.html" width="250" height="150"></iframe>':  # noqa
    '',

    '## animation_scale_x_from_center API':
    '',

    '<!-- Docstring: apysc._animation.animation_scale_x_from_center_interface.AnimationScaleXFromCenterInterface.animation_scale_x_from_center -->\n\n<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>\n\n**[Interface signature]** `animation_scale_x_from_center(self, scale_x_from_center:Union[float, apysc._type.number.Number], *, duration:Union[int, apysc._type.int.Int]=3000, delay:Union[int, apysc._type.int.Int]=0, easing:apysc._animation.easing.Easing=<Easing.LINEAR: \'function(x) {return x;}\'>) -> apysc._animation.animation_scale_x_from_center.AnimationScaleXFromCenter`<hr>\n\n**[Interface summary]** Set the scale-x from the center point animation setting.<hr>\n\n**[Parameters]**\n\n- `scale_x_from_center`: Number or float\n  - The final scale-x of the animation.\n- `duration`: Int or int, default 3000\n  - Milliseconds before an animation ends.\n- `delay`: Int or int, default 0\n  - Milliseconds before an animation starts.\n- `easing`: Easing, default Easing.LINEAR\n  - Easing setting.\n\n<hr>\n\n**[Returns]**\n\n- `animation_scale_x_from_center`: AnimationScaleXFromCenter\n  - Created animation setting instance.\n\n<hr>\n\n**[Notes]**\n\nTo start this animation, you need to call the `start` method of the returned instance.<hr>\n\n**[Examples]**':  # noqa
    '',

    '```py\n>>> import apysc as ap\n>>> stage: ap.Stage = ap.Stage()\n>>> sprite: ap.Sprite = ap.Sprite()\n>>> sprite.graphics.begin_fill(color=\'#0af\')\n>>> rectangle: ap.Rectangle = sprite.graphics.draw_rect(\n...     x=50, y=50, width=50, height=50)\n>>> _ = rectangle.animation_scale_x_from_center(\n...     scale_x_from_center=0.5,\n...     duration=1500,\n...     easing=ap.Easing.EASE_OUT_QUINT,\n... ).start()\n```':  # noqa
    '',

    '<hr>\n\n**[References]**\n\n- [Animation interfaces duration setting document](https://simon-ritchie.github.io/apysc/animation_duration.html)\n- [Animation interfaces delay setting document](https://simon-ritchie.github.io/apysc/animation_delay.html)\n- [Each animation interface return value document](https://simon-ritchie.github.io/apysc/animation_return_value.html)\n- [Sequential animation setting document](https://simon-ritchie.github.io/apysc/sequential_animation.html)\n- [animation_parallel interface document](https://simon-ritchie.github.io/apysc/animation_parallel.html)\n- [Easing enum document](https://simon-ritchie.github.io/apysc/easing_enum.html)':  # noqa
    '',

    '## animation_scale_y_from_center API':
    '',

    '<!-- Docstring: apysc._animation.animation_scale_y_from_center_interface.AnimationScaleYFromCenterInterface.animation_scale_y_from_center -->\n\n<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>\n\n**[Interface signature]** `animation_scale_y_from_center(self, scale_y_from_center:Union[float, apysc._type.number.Number], *, duration:Union[int, apysc._type.int.Int]=3000, delay:Union[int, apysc._type.int.Int]=0, easing:apysc._animation.easing.Easing=<Easing.LINEAR: \'function(x) {return x;}\'>) -> apysc._animation.animation_scale_y_from_center.AnimationScaleYFromCenter`<hr>\n\n**[Interface summary]** Set the scale-y from the center point animation setting.<hr>\n\n**[Parameters]**\n\n- `scale_y_from_center`: Number or float\n  - The final scale-y of the animation.\n- `duration`: Int or int, default 3000\n  - Milliseconds before an animation ends.\n- `delay`: Int or int, default 0\n  - Milliseconds before an animation starts.\n- `easing`: Easing, default Easing.LINEAR\n  - Easing setting.\n\n<hr>\n\n**[Returns]**\n\n- `animation_scale_y_from_center`: AnimationScaleYFromCenter\n  - Created animation setting instance.\n\n<hr>\n\n**[Notes]**\n\nTo start this animation, you need to call the `start` method of the returned instance.<hr>\n\n**[Examples]**':  # noqa
    '',

    '```py\n>>> import apysc as ap\n>>> stage: ap.Stage = ap.Stage()\n>>> sprite: ap.Sprite = ap.Sprite()\n>>> sprite.graphics.begin_fill(color=\'#0af\')\n>>> rectangle: ap.Rectangle = sprite.graphics.draw_rect(\n...     x=50, y=50, width=50, height=50)\n>>> _ = rectangle.animation_scale_y_from_center(\n...     scale_y_from_center=0.5,\n...     duration=1500,\n...     easing=ap.Easing.EASE_OUT_QUINT,\n... ).start()\n```':  # noqa
    '',

    '<hr>\n\n**[References]**\n\n- [Animation interfaces duration setting document](https://simon-ritchie.github.io/apysc/animation_duration.html)\n- [Animation interfaces delay setting document](https://simon-ritchie.github.io/apysc/animation_delay.html)\n- [Each animation interface return value document](https://simon-ritchie.github.io/apysc/animation_return_value.html)\n- [Sequential animation setting document](https://simon-ritchie.github.io/apysc/sequential_animation.html)\n- [animation_parallel interface document](https://simon-ritchie.github.io/apysc/animation_parallel.html)\n- [Easing enum document](https://simon-ritchie.github.io/apysc/easing_enum.html)':  # noqa
    '',

}
