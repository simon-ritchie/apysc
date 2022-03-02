"""This module is for the translation mapping data of the
following document:

Document file: animation_event.md
Language: jp
"""

from typing import Dict

MAPPING: Dict[str, str] = {

    '# AnimationEvent':
    '',

    'This page explains the `AnimationEvent` class.':
    '',

    '## What class is this?':
    '',

    'An animation-related event handler uses the `AnimationEvent` class, such as the complete animation event. Each animation interface passes this event instance to the handler.':  # noqa
    '',

    '## Basic usage':
    '',

    'The following example sets the animation complete event handler. The animation interface passes the `AnimationEvent` instance argument as the `e: ap.AnimationEvent`:':  # noqa
    '',

    '```py\n# runnable\nimport apysc as ap\n\n\ndef on_animation_complete(e: ap.AnimationEvent, options: dict) -> None:\n    """\n    The handler that animation calls when its end.\n\n    Parameters\n    ----------\n    e : ap.AnimationEvent\n        Event instance.\n    options : dict\n        Optional arguments dictionary.\n    """\n    ap.trace(\'Animation is completed!\')\n\n\nap.Stage(\n    stage_width=200, stage_height=150,\n    background_color=\'#333\', stage_elem_id=\'stage\')\nsprite: ap.Sprite = ap.Sprite()\nsprite.graphics.begin_fill(color=\'#00aaff\')\nrectangle: ap.Rectangle = sprite.graphics.draw_rect(\n    x=50, y=50, width=50, height=50)\nanimation_x: ap.AnimationX = rectangle.animation_x(x=100)\nanimation_x.animation_complete(on_animation_complete)\nanimation_x.start()\n```':  # noqa
    '',

    '':
    '',

    '## this property':
    '',

    'The `AnimationEvent` instance\'s `this` property is a subclass instance of the `AnimationBase` class, such as the `AnimationMove`\\, `AnimationX`\\, or other class.\n\nThis type depends on the called interface, e.g., if you use the `animation_x` interface, `this` property type becomes an `AnimationX` instance.':  # noqa
    '',

    '```py\n# runnable\nimport apysc as ap\n\n\ndef on_animation_complete(e: ap.AnimationEvent, options: dict) -> None:\n    """\n    The handler that animation calls when its end.\n\n    Parameters\n    ----------\n    e : ap.AnimationEvent\n        Event instance.\n    options : dict\n        Optional arguments dictionary.\n    """\n    assert isinstance(e.this, ap.AnimationX)\n\n\nap.Stage(\n    stage_width=200, stage_height=150,\n    background_color=\'#333\', stage_elem_id=\'stage\')\nsprite: ap.Sprite = ap.Sprite()\nsprite.graphics.begin_fill(color=\'#00aaff\')\nrectangle: ap.Rectangle = sprite.graphics.draw_rect(\n    x=50, y=50, width=50, height=50)\nanimation_x: ap.AnimationX = rectangle.animation_x(x=100)\nanimation_x.animation_complete(on_animation_complete)\nanimation_x.start()\n```':  # noqa
    '',

    '':
    '',

    '## Generic type annotation':
    '',

    'The `AnimationEvent` class can set a generic type annotation. If you set a generic type annotation, then the animation target property type (e.g., `DisplayObject`) changes.\n\nThe following example sets a `Rectangle` generic type annotation to the `AnimationEvent` and benefits from type checking libraries (such as the `mypy` or `Pylance`).':  # noqa
    '',

    '```py\n# runnable\nimport apysc as ap\n\n\ndef on_animation_complete(\n        e: ap.AnimationEvent[ap.Rectangle], options: dict) -> None:\n    """\n    The handler that animation calls when its end.\n\n    Parameters\n    ----------\n    e : ap.AnimationEvent\n        Event instance.\n    options : dict\n        Optional arguments dictionary.\n    """\n    rectangle: ap.Rectangle = e.this.target\n    rectangle.animation_x(x=50).start()\n\n\nap.Stage(\n    stage_width=200, stage_height=150,\n    background_color=\'#333\', stage_elem_id=\'stage\')\nsprite: ap.Sprite = ap.Sprite()\nsprite.graphics.begin_fill(color=\'#00aaff\')\nrectangle: ap.Rectangle = sprite.graphics.draw_rect(\n    x=50, y=50, width=50, height=50)\nanimation_x: ap.AnimationX = rectangle.animation_x(x=100)\nanimation_x.animation_complete(on_animation_complete)\nanimation_x.start()\n```':  # noqa
    '',

    '':
    '',

    '## AnimationEvent constructor API':
    '',

    '<!-- Docstring: apysc._event.animation_event.AnimationEvent.__init__ -->\n\n<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>\n\n**[Interface signature]** `__init__(self, *, this:\'animation_base.AnimationBase[_T]\') -> None`<hr>\n\n**[Interface summary]** Animation event class.<hr>\n\n**[Parameters]**\n\n- `this`: AnimationBase\n  - Animation setting instance.\n\n<hr>\n\n**[Examples]**':  # noqa
    '',

    '```py\n>>> import apysc as ap\n>>> def on_animation_complete(\n...         e: ap.AnimationEvent[ap.Rectangle],\n...         options: dict) -> None:\n...     rectangle: ap.Rectangle = e.this.target\n>>> stage: ap.Stage = ap.Stage()\n>>> sprite: ap.Sprite = ap.Sprite()\n>>> sprite.graphics.begin_fill(color=\'#0af\')\n>>> rectangle: ap.Rectangle = sprite.graphics.draw_rect(\n...     x=50, y=50, width=50, height=50)\n>>> _ = rectangle.animation_x(\n...     x=100).animation_complete(on_animation_complete)\n```':  # noqa
    '',

    '':
    '',

    '## this property API':
    '',

    '<!-- Docstring: apysc._event.animation_event.AnimationEvent.this -->\n\n<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>\n\n**[Interface summary]** Get an animation setting instance of listening to this event.<hr>\n\n**[Returns]**\n\n- `this`: AnimationBase\n  - Instance of listening to this event.\n\n<hr>\n\n**[Examples]**':  # noqa
    '',

    '```py\n>>> import apysc as ap\n>>> def on_animation_complete(\n...         e: ap.AnimationEvent[ap.Rectangle],\n...         options: dict) -> None:\n...     rectangle: ap.Rectangle = e.this.target\n>>> stage: ap.Stage = ap.Stage()\n>>> sprite: ap.Sprite = ap.Sprite()\n>>> sprite.graphics.begin_fill(color=\'#0af\')\n>>> rectangle: ap.Rectangle = sprite.graphics.draw_rect(\n...     x=50, y=50, width=50, height=50)\n>>> _ = rectangle.animation_x(\n...     x=100).animation_complete(on_animation_complete)\n```':  # noqa
    '',

}
