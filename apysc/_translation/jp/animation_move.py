"""This module is for the translation mapping data of the
following document:

Document file: animation_move.md
Language: jp
"""

from typing import Dict

MAPPING: Dict[str, str] = {

    '# animation_move interface':
    '',

    'This page explains the `animation_move` method interface.':
    '',

    '## What interface is this?':
    '',

    'The `animation_move` method interface creates an `AnimationMove` instance. You can animate the x and y coordinates with it.\n\nThis interface exists on a `DisplayObject` subclass instance, such as the `Sprite` or `Rectangle`.':  # noqa
    '',

    '## Basic usage':
    '',

    'The following example sets the coordinates animation (from x=50, y=50 to x=100, y=100) with the `animation_move` method.':  # noqa
    '',

    '```py\n# runnable\nimport apysc as ap\n\n\ndef on_animation_complete_1(\n        e: ap.AnimationEvent[ap.Rectangle],\n        options: dict) -> None:\n    """\n    The handler that the animation calls when its end.\n\n    Parameters\n    ----------\n    e : ap.AnimationEvent\n        Event instance.\n    options : dict\n        Optional arguments dictionary.\n    """\n    animation_move: ap.AnimationMove = e.this.target.animation_move(\n        x=50, y=50, duration=1000)\n    animation_move.animation_complete(on_animation_complete_2)\n    animation_move.start()\n\n\ndef on_animation_complete_2(\n        e: ap.AnimationEvent[ap.Rectangle],\n        options: dict) -> None:\n    """\n    The handler that the animation calls when its end.\n\n    Parameters\n    ----------\n    e : ap.AnimationEvent\n        Event instance.\n    options : dict\n        Optional arguments dictionary.\n    """\n    animation_move: ap.AnimationMove = e.this.target.animation_move(\n        x=100, y=100, duration=1000)\n    animation_move.animation_complete(on_animation_complete_1)\n    animation_move.start()\n\n\nap.Stage(\n    stage_width=200, stage_height=200, background_color=\'#333\',\n    stage_elem_id=\'stage\')\nsprite: ap.Sprite = ap.Sprite()\nsprite.graphics.begin_fill(color=\'#0af\')\nrectangle: ap.Rectangle = sprite.graphics.draw_rect(\n    x=50, y=50, width=50, height=50)\n\nanimation_move: ap.AnimationMove = rectangle.animation_move(\n    x=100, y=100, duration=1000)\nanimation_move.animation_complete(on_animation_complete_1)\nanimation_move.start()\n\nap.save_overall_html(\n    dest_dir_path=\'./animation_move_basic_usage/\')\n```':  # noqa
    '',

    '<iframe src="static/animation_move_basic_usage/index.html" width="200" height="200"></iframe>':  # noqa
    '',

    '## animation_move API':
    '',

    '<!-- Docstring: apysc._animation.animation_move_interface.AnimationMoveInterface.animation_move -->\n\n<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>\n\n**[Interface signature]** `animation_move(self, x:Union[int, apysc._type.int.Int], y:Union[int, apysc._type.int.Int], *, duration:Union[int, apysc._type.int.Int]=3000, delay:Union[int, apysc._type.int.Int]=0, easing:apysc._animation.easing.Easing=<Easing.LINEAR: \'function(x) {return x;}\'>) -> apysc._animation.animation_move.AnimationMove`<hr>\n\n**[Interface summary]** Set the x and y coordinates animation settings.<hr>\n\n**[Parameters]**\n\n- `x`: Int or int\n  - Destination of the x-coordinate.\n- `y`: Int or int\n  - Destination of the y-coordinate.\n- `duration`: Int or int, default 3000\n  - Milliseconds before an animation ends.\n- `delay`: Int or int, default 0\n  - Milliseconds before an animation starts.\n- `easing`: Easing, default Easing.LINEAR\n  - Easing setting.\n\n<hr>\n\n**[Returns]**\n\n- `animation_move`: AnimationMove\n  - Created animation setting instance.\n\n<hr>\n\n**[Notes]**\n\nTo start this animation, you need to call the `start` method of the returned instance.<hr>\n\n**[Examples]**':  # noqa
    '',

    '```py\n>>> import apysc as ap\n>>> stage: ap.Stage = ap.Stage()\n>>> sprite: ap.Sprite = ap.Sprite()\n>>> sprite.graphics.begin_fill(color=\'#0af\')\n>>> sprite.graphics.line_style(\n...     color=\'#fff\', thickness=1)\n>>> rectangle: ap.Rectangle = sprite.graphics.draw_rect(\n...     x=50, y=50, width=50, height=50)\n>>> _ = rectangle.animation_move(\n...     x=100, y=150,\n...     duration=1500,\n...     easing=ap.Easing.EASE_OUT_QUINT,\n... ).start()\n```':  # noqa
    '',

    '<hr>\n\n**[References]**\n\n- [Animation interfaces duration setting document](https://simon-ritchie.github.io/apysc/animation_duration.html)\n- [Animation interfaces delay setting document](https://simon-ritchie.github.io/apysc/animation_delay.html)\n- [Each animation interface return value document](https://simon-ritchie.github.io/apysc/animation_return_value.html)\n- [Sequential animation setting document](https://simon-ritchie.github.io/apysc/sequential_animation.html)\n- [animation_parallel interface document](https://simon-ritchie.github.io/apysc/animation_parallel.html)\n- [Easing enum document](https://simon-ritchie.github.io/apysc/easing_enum.html)':  # noqa
    '',

}
