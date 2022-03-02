"""This module is for the translation mapping data of the
following document:

Document file: sequential_animation.md
Language: jp
"""

from typing import Dict

MAPPING: Dict[str, str] = {

    '# Sequential animation setting':
    '',

    'This page explains how to animate sequentially.':
    '',

    '## Sequential animation interface calling on the same instance':
    '',

    'If you call each animation interface sequentially, these animations start in order (e.g., when the first animation completion, the second one starts).\n\nThe following example sets the four animations of the coordinates. These animations do not start simultaneously:':  # noqa
    '',

    '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    stage_width=200, stage_height=200, background_color=\'#333\',\n    stage_elem_id=\'stage\')\nsprite: ap.Sprite = ap.Sprite()\nsprite.graphics.begin_fill(color=\'#0af\')\n\nrectangle: ap.Rectangle = sprite.graphics.draw_rect(\n    x=50, y=50, width=50, height=50)\neasing: ap.Easing = ap.Easing.EASE_OUT_QUINT\nrectangle.animation_x(x=100, duration=1000, delay=1000, easing=easing).start()\nrectangle.animation_y(y=100, duration=1000, delay=1000, easing=easing).start()\nrectangle.animation_x(x=50, duration=1000, delay=1000, easing=easing).start()\nrectangle.animation_y(y=50, duration=1000, delay=1000, easing=easing).start()\n\nap.save_overall_html(\n    dest_dir_path=\'sequential_animation_example_1/\')\n```':  # noqa
    '',

    '<iframe src="static/sequential_animation_example_1/index.html" width="200" height="200"></iframe>':  # noqa
    '',

    '## animation_complete handler setting':
    '',

    'Also, you can use the `animation_complete` interface to register a handler for the sequence animation. For the details, please see [animation_complete interface document](animation_complete.md).':  # noqa
    '',

    '## See also':
    '',

    'If you want to animate multiple animations simultaneously, you can use the [`animation_parallel` interface](animation_parallel.md).':  # noqa
    '',

}
