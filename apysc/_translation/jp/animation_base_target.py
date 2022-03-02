"""This module is for the translation mapping data of the
following document:

Document file: animation_base_target.md
Language: jp
"""

from typing import Dict

MAPPING: Dict[str, str] = {

    '# AnimationBase class target property interface':
    '',

    'This page explains the `AnimationBase` class `target` property interface.':  # noqa
    '',

    '## What property is this?':
    '',

    'The `target` property returns the animation target instance (e.g., `Sprite`\\, `Rectangle`).':  # noqa
    '',

    '## Basic usage':
    '',

    'Each subclass of the `AnimationBase` (e.g., `AnimationMove`\\, `AnimationX`) has the `target` getter property.':  # noqa
    '',

    '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    stage_width=200, stage_height=150,\n    background_color=\'#333\', stage_elem_id=\'stage\')\nsprite: ap.Sprite = ap.Sprite()\nsprite.graphics.begin_fill(color=\'#00aaff\')\nrectangle: ap.Rectangle = sprite.graphics.draw_rect(\n    x=50, y=50, width=50, height=50)\nanimation_x: ap.AnimationX = rectangle.animation_x(x=100)\nassert isinstance(animation_x.target, ap.Rectangle)\n```':  # noqa
    '',

    '':
    '',

    '## Generic type annotation setting':
    '',

    'The `AnimationBase` class and its subclasses can set a generic type annotation. For example, the `target` property type becomes its type if you set it.\n\nThe following code sets the `[ap.Rectangle]` generic type annotation:':  # noqa
    '',

    '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    stage_width=200, stage_height=150,\n    background_color=\'#333\', stage_elem_id=\'stage\')\nsprite: ap.Sprite = ap.Sprite()\nsprite.graphics.begin_fill(color=\'#00aaff\')\nrectangle: ap.Rectangle = sprite.graphics.draw_rect(\n    x=50, y=50, width=50, height=50)\nanimation_x: ap.AnimationX[ap.Rectangle] = rectangle.animation_x(x=100)\nassert isinstance(animation_x.target, ap.Rectangle)\n```':  # noqa
    '',

    'It is also sometimes useful to annotate generic type to the handler\'s `AnimationEvent`\\. This generic type annotation also affects the `target` type (`e.this.target`), as follows:':  # noqa
    '',

    '```py\n# runnable\nimport apysc as ap\n\n\ndef on_animation_complete(\n        e: ap.AnimationEvent[ap.Rectangle], options: dict) -> None:\n    """\n    The handler the animation calls when its end.\n\n    Parameters\n    ----------\n    e : ap.AnimationEvent\n        Event instance.\n    options : dict\n        Optional arguments dictionary.\n    """\n    rectangle: ap.Rectangle = e.this.target\n    rectangle.animation_x(x=50).start()\n\n\nap.Stage(\n    stage_width=200, stage_height=150,\n    background_color=\'#333\', stage_elem_id=\'stage\')\nsprite: ap.Sprite = ap.Sprite()\nsprite.graphics.begin_fill(color=\'#00aaff\')\nrectangle: ap.Rectangle = sprite.graphics.draw_rect(\n    x=50, y=50, width=50, height=50)\nanimation_x: ap.AnimationX = rectangle.animation_x(x=100)\nanimation_x.animation_complete(on_animation_complete)\n```':  # noqa
    '',

    '':
    '',

    '## target property API':
    '',

    '<!-- Docstring: apysc._animation.animation_base.AnimationBase.target -->\n\n<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>\n\n**[Interface summary]** Get an animation target instance.<hr>\n\n**[Returns]**\n\n- `target`: VariableNameInterface\n  - An animation target instance.\n\n<hr>\n\n**[Examples]**':  # noqa
    '',

    '```py\n>>> import apysc as ap\n>>> def on_animation_complete(\n...         e: ap.AnimationEvent[ap.Rectangle],\n...         options: dict) -> None:\n...     rectangle: ap.Rectangle = e.this.target\n>>> stage: ap.Stage = ap.Stage()\n>>> sprite: ap.Sprite = ap.Sprite()\n>>> sprite.graphics.begin_fill(color=\'#0af\')\n>>> rectangle: ap.Rectangle = sprite.graphics.draw_rect(\n...     x=50, y=50, width=50, height=50)\n>>> _ = rectangle.animation_x(\n...     x=100,\n... ).animation_complete(on_animation_complete).start()\n```':  # noqa
    '',

}
