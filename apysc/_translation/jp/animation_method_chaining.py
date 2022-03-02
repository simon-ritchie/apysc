"""This module is for the translation mapping data of the
following document:

Document file: animation_method_chaining.md
Language: jp
"""

from typing import Dict

MAPPING: Dict[str, str] = {

    '# AnimationBase class interfaces method chaining':
    '',

    'This page describes the method chaining of the animation interfaces.':
    '',

    '## Each AnimationBase related interface returns its instance':
    '',

    'Each `AnimationBase` class-related interface (such as the `animation_x`\\, `start`\\, `animation_complete`) returns its instance. So that these interfaces can be used with the method chaining, as follows (method chaining of the `animation_x`\\, `animation_complete`\\, and `start` methods):':  # noqa
    '',

    '```py\n# runnable\nimport apysc as ap\n\n\ndef on_animation_complete(\n        e: ap.AnimationEvent[ap.Rectangle], options: dict) -> None:\n    """\n    The handler that the animation calls when its end.\n\n    Parameters\n    ----------\n    e : AnimationEvent\n        Event instance.\n    options : dict\n        Optional arguments dictionary.\n    """\n    ap.trace(\'Animation is completed!\')\n\n\nap.Stage(\n    stage_width=200, stage_height=150,\n    background_color=\'#333\', stage_elem_id=\'stage\')\nsprite: ap.Sprite = ap.Sprite()\nsprite.graphics.begin_fill(color=\'#00aaff\')\nrectangle: ap.Rectangle = sprite.graphics.draw_rect(\n    x=50, y=50, width=50, height=50)\nrectangle.animation_x(\n    x=100,\n    duration=1000,\n).animation_complete(on_animation_complete).start()\n\nap.save_overall_html(\n    dest_dir_path=\'./animation_method_chaining_basic_usage_1/\')\n```':  # noqa
    '',

    '<iframe src="static/animation_method_chaining_basic_usage_1/index.html" width="200" height=150></iframe>\n\nThese method chainings are sometimes useful for code simplicity.\n\nIf you want to chain the methods like JavaScript (e.g., `D3.js`), you can use backslashes at the line end, as follows:':  # noqa
    '',

    '```py\n# runnable\nimport apysc as ap\n\n\ndef on_animation_complete(\n        e: ap.AnimationEvent[ap.Rectangle], options: dict) -> None:\n    """\n    The handler that the animation calls when its end.\n\n    Parameters\n    ----------\n    e : AnimationEvent\n        Event instance.\n    options : dict\n        Optional arguments dictionary.\n    """\n    ap.trace(\'Animation is completed!\')\n\n\nap.Stage(\n    stage_width=200, stage_height=150,\n    background_color=\'#333\', stage_elem_id=\'stage\')\nsprite: ap.Sprite = ap.Sprite()\nsprite.graphics.begin_fill(color=\'#00aaff\')\nrectangle: ap.Rectangle = sprite.graphics.draw_rect(\n    x=50, y=50, width=50, height=50)\nrectangle\\\n    .animation_x(x=100, duration=1000)\\\n    .animation_complete(on_animation_complete)\\\n    .start()\n\nap.save_overall_html(\n    dest_dir_path=\'./animation_method_chaining_basic_usage_2/\')\n```':  # noqa
    '',

    '<iframe src="static/animation_method_chaining_basic_usage_2/index.html" width="200" height=150></iframe>':  # noqa
    '',

}
