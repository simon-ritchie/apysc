"""This module is for the translation mapping data of the
following document:

Document file: animation_complete.md
Language: jp
"""

from typing import Dict

MAPPING: Dict[str, str] = {

    '# AnimationBase class animation_complete interface':
    '',

    'This page explains the `AnimationBase` class `animation_complete` method interface.':  # noqa
    '',

    '## What interface is this?':
    '',

    'The `animation_complete` method binds a handler that the animation calls when its end.\n\nThe handler\'s arguments require the event instance (`ap.AnimationEvent`) at the first argument and the options dictionary at the second argument.':  # noqa
    '',

    '## Basic usage':
    '',

    'The `animation_complete` method requires a handler at the first argument and the optional options dictionary at the second argument.\n\nThe following example calls the `animation_complete` method at the x-coordinate animation end. It starts another animation to reset the x-coordinate:':  # noqa
    '',

    '```py\n# runnable\nimport apysc as ap\n\nDURATION: int = 1000\n\n\ndef on_animation_complete_1(\n        e: ap.AnimationEvent[ap.Rectangle],\n        options: dict) -> None:\n    """\n    The handler that animation calls when its end.\n\n    Parameters\n    ----------\n    e : ap.AnimationEvent\n        Event instance.\n    options : dict\n        Optional arguments dictionary.\n    """\n    rectangle: ap.Rectangle = e.this.target\n    animation_x: ap.AnimationX = rectangle.animation_x(\n        x=50, duration=DURATION)\n    animation_x.animation_complete(on_animation_complete_2)\n    animation_x.start()\n\n\ndef on_animation_complete_2(\n        e: ap.AnimationEvent[ap.Rectangle], options: dict) -> None:\n    """\n    The handler that animation calls when its end.\n\n    Parameters\n    ----------\n    e : ap.AnimationEvent\n        Event instance.\n    options : dict\n        Optional arguments dictionary.\n    """\n    rectangle: ap.Rectangle = e.this.target\n    animation_x: ap.AnimationX = rectangle.animation_x(\n        x=100, duration=DURATION)\n    animation_x.animation_complete(on_animation_complete_1)\n    animation_x.start()\n\n\nap.Stage(\n    stage_width=200, stage_height=150, background_color=\'#333\',\n    stage_elem_id=\'stage\')\nsprite: ap.Sprite = ap.Sprite()\nsprite.graphics.begin_fill(color=\'#0af\')\nrectangle: ap.Rectangle = sprite.graphics.draw_rect(\n    x=50, y=50, width=50, height=50)\n\nanimation_x: ap.AnimationX = rectangle.animation_x(\n    x=100, duration=1000)\nanimation_x.animation_complete(on_animation_complete_1)\nanimation_x.start()\n\nap.save_overall_html(\n    dest_dir_path=\'./animation_complete_basic_usage/\')\n```':  # noqa
    '',

    '<iframe src="static/animation_complete_basic_usage/index.html" width="200" height="150"></iframe>':  # noqa
    '',

    '## Notes about the other interface calling order':
    '',

    'You can only call the `animation_complete` before the animation start, so if you call the `animation_complete` method after the `start` method, it raises an exception:':  # noqa
    '',

    '```py\nimport apysc as ap\n\n\ndef on_animation_complete(\n        e: ap.AnimationEvent[ap.Rectangle],\n        options: dict) -> None:\n    """\n    The handler that animation calls when its end.\n\n    Parameters\n    ----------\n    e : ap.AnimationEvent\n        Event instance.\n    options : dict\n        Optional arguments dictionary.\n    """\n    ap.trace(\'Animation complete!\')\n\n\nap.Stage(\n    stage_width=200, stage_height=200, background_color=\'#333\',\n    stage_elem_id=\'stage\')\nsprite: ap.Sprite = ap.Sprite()\nsprite.graphics.begin_fill(color=\'#0af\')\nrectangle: ap.Rectangle = sprite.graphics.draw_rect(\n    x=50, y=50, width=50, height=50)\n\nanimation_move: ap.AnimationMove = rectangle.animation_move(\n    x=100, y=100, duration=1000)\nanimation_move.start()\nanimation_move.animation_complete(on_animation_complete)\n```':  # noqa
    '',

    '':
    '',

    '```\nException: This interface can not be called after the animation is started.\n```':  # noqa
    '',

    'The calling of the `animation_complete` method before the `start` method works correctly:':  # noqa
    '',

    '```py\n# runnable\nimport apysc as ap\n\n\ndef on_animation_complete(\n        e: ap.AnimationEvent[ap.Rectangle],\n        options: dict) -> None:\n    """\n    The handler that animation calls when its end.\n\n    Parameters\n    ----------\n    e : ap.AnimationEvent\n        Event instance.\n    options : dict\n        Optional arguments dictionary.\n    """\n    ap.trace(\'Animation complete!\')\n\n\nap.Stage(\n    stage_width=200, stage_height=200, background_color=\'#333\',\n    stage_elem_id=\'stage\')\nsprite: ap.Sprite = ap.Sprite()\nsprite.graphics.begin_fill(color=\'#0af\')\nrectangle: ap.Rectangle = sprite.graphics.draw_rect(\n    x=50, y=50, width=50, height=50)\n\nanimation_move: ap.AnimationMove = rectangle.animation_move(\n    x=100, y=100, duration=1000)\nanimation_move.animation_complete(on_animation_complete)\nanimation_move.start()\n```':  # noqa
    '',

    '':
    '',

    '## animation_complete API':
    '',

    '<!-- Docstring: apysc._animation.animation_base.AnimationBase.animation_complete -->\n\n<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>\n\n**[Interface signature]** `animation_complete(self, handler:Callable[[_ForwardRef(\'animation_event.AnimationEvent\'), ~_O], NoneType], *, options:Union[~_O, NoneType]=None) -> \'AnimationBase\'`<hr>\n\n**[Interface summary]** Add an animation complete event listener setting.<hr>\n\n**[Parameters]**\n\n- `handler`: _Handler\n  - A callable that an instance calls when an animation is complete.\n- `options`: dict or None, default None\n  - Optional arguments dictionary to be passed to a handler.\n\n<hr>\n\n**[Returns]**\n\n- `self`: AnimatonBase\n  - This instance.\n\n<hr>\n\n**[Raises]**\n\n- Exception: If calling this interface after an animation starts\n\n<hr>\n\n**[Notes]**\n\nThis interface can only use before an animation starts<hr>\n\n**[Examples]**':  # noqa
    '',

    '```py\n>>> import apysc as ap\n>>> def on_animation_complete(\n...         e: ap.AnimationEvent[ap.Rectangle],\n...         options: dict) -> None:\n...     ap.trace(\'Animation completed!\')\n>>> stage: ap.Stage = ap.Stage()\n>>> sprite: ap.Sprite = ap.Sprite()\n>>> sprite.graphics.begin_fill(color=\'#0af\')\n>>> rectangle: ap.Rectangle = sprite.graphics.draw_rect(\n...     x=50, y=50, width=50, height=50)\n>>> _ = rectangle.animation_x(\n...     x=100,\n... ).animation_complete(on_animation_complete).start()\n```':  # noqa
    '',

    '<hr>\n\n**[References]**\n\n- [About the handler options’ type document](https://simon-ritchie.github.io/apysc/about_handler_options_type.html)':  # noqa
    '',

}
