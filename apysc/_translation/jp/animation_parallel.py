"""This module is for the translation mapping data of the
following document:

Document file: animation_parallel.md
Language: jp
"""

from typing import Dict

MAPPING: Dict[str, str] = {

    '# animation_parallel interface':
    '',

    'This page explains the `animation_parallel` interface.':
    '',

    '## What interface is this?':
    '',

    'The `animation_parallel` method interface creates an `AnimationParallel` instance. You can set multiple simultaneous animations to the same instance with it.\n\nThis interface exists on a `DisplayObject` subclass instance, such as the `Sprite` or `Rectangle` class.':  # noqa
    '',

    '## Basic usage':
    '',

    'You can use this interface with the `animation_parallel` method. The `animations` list argument requires any animation settings.\n\nThe following example sets the simultaneous animations of the x, fill alpha, fill color, and line thickness.':  # noqa
    '',

    '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    stage_width=400, stage_height=150, background_color=\'#333\',\n    stage_elem_id=\'stage\')\nsprite: ap.Sprite = ap.Sprite()\nsprite.graphics.begin_fill(color=\'#0af\')\nsprite.graphics.line_style(color=\'#fff\', thickness=3)\n\nrectangle: ap.Rectangle = sprite.graphics.draw_rect(\n    x=50, y=50, width=50, height=50)\nrectangle.animation_parallel(\n    animations=[\n        rectangle.animation_x(x=300),\n        rectangle.animation_fill_color(fill_color=\'#f0a\'),\n        rectangle.animation_fill_alpha(alpha=0.3),\n        rectangle.animation_line_thickness(thickness=7),\n    ],\n    duration=3000, delay=3000, easing=ap.Easing.EASE_OUT_QUINT,\n).start()\n\nap.save_overall_html(\n    dest_dir_path=\'animation_parallel_basic_usage/\')\n```':  # noqa
    '',

    '<iframe src="static/animation_parallel_basic_usage/index.html" width="400" height="150"></iframe>':  # noqa
    '',

    '## Note for each animation\'s duration, delay, and easing setting':
    '',

    'Animation settings of the `duration`\\, `delay`\\, and `easing` in the `animations` argument can\'t be changed since these animation settings are referring to the `animation_parallel` arguments. If you set these parameters in the `animations` arguments, setting raise an error:':  # noqa
    '',

    '```py\n...\nrectangle.animation_parallel(\n    animations=[\n        rectangle.animation_x(x=300, duration=1000),\n    ],\n    duration=3000, delay=2000, easing=ap.Easing.EASE_OUT_QUINT,\n)\n...\n```':  # noqa
    '',

    '':
    '',

    '```\nValueError: There is an animation target that is changed duration setting: 1000\nThe duration setting of animation in the `animations` argument can not be changed.\nTarget animation type: <class \'apysc._animation.animation_x.AnimationX\'>\n```':  # noqa
    '',

    '':
    '',

    '## animation_parallel API':
    '',

    '<!-- Docstring: apysc._animation.animation_parallel_interface.AnimationParallelInterface.animation_parallel -->\n\n<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>\n\n**[Interface signature]** `animation_parallel(self, animations:List[apysc._animation.animation_base.AnimationBase], *, duration:Union[int, apysc._type.int.Int]=3000, delay:Union[int, apysc._type.int.Int]=0, easing:apysc._animation.easing.Easing=<Easing.LINEAR: \'function(x) {return x;}\'>) -> apysc._animation.animation_parallel.AnimationParallel`<hr>\n\n**[Interface summary]** Set the parallel animation setting.<hr>\n\n**[Parameters]**\n\n- `animations`: list of AnimationBase\n  - Target animation settings.\n- `duration`: Int or int, default 3000\n  - Milliseconds before an animation ends.\n- `delay`: Int or int, default 0\n  - Milliseconds before an animation starts.\n- `easing`: Easing, default Easing.LINEAR\n  - Easing setting.\n\n<hr>\n\n**[Returns]**\n\n- `animation_parallel`: AnimationParallel\n  - Created animation setting instance.\n\n<hr>\n\n**[Raises]**\n\n- ValueError: <br> ・If the animations\' target is not this instance. <br> ・If there are changed duration, delay, or easing animation settings in the `animations` list.\n\n<hr>\n\n**[Notes]**\n\n ・To start this animation, you need to call the `start` method of the returned instance. <br> ・The `animations` argument can\'t contains the `AnimationParallel` instance. <br> ・This interface ignores the duration, delay, and easing arguments in the `animations` argument (this interface uses self-arguments instead).<hr>\n\n**[Examples]**':  # noqa
    '',

    '```py\n>>> import apysc as ap\n>>> stage: ap.Stage = ap.Stage()\n>>> sprite: ap.Sprite = ap.Sprite()\n>>> sprite.graphics.begin_fill(color=\'#0af\')\n>>> rectangle: ap.Rectangle = sprite.graphics.draw_rect(\n...     x=50, y=50, width=50, height=50)\n>>> _ = rectangle.animation_parallel(\n...     animations=[\n...         rectangle.animation_x(x=100),\n...         rectangle.animation_fill_color(fill_color=\'#f0a\'),\n...         rectangle.animation_fill_alpha(alpha=0.5),\n...     ],\n...     duration=1500,\n...     easing=ap.Easing.EASE_OUT_QUINT,\n... ).start()\n```':  # noqa
    '',

    '<hr>\n\n**[References]**\n\n- [Animation interfaces duration setting document](https://simon-ritchie.github.io/apysc/animation_duration.html)\n- [Animation interfaces delay setting document](https://simon-ritchie.github.io/apysc/animation_delay.html)\n- [Each animation interface return value document](https://simon-ritchie.github.io/apysc/animation_return_value.html)\n- [Sequential animation setting document](https://simon-ritchie.github.io/apysc/sequential_animation.html)\n- [Easing enum document](https://simon-ritchie.github.io/apysc/easing_enum.html)':  # noqa
    '',

}
