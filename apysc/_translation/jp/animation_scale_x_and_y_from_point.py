"""This module is for the translation mapping data of the
following document:

Document file: animation_scale_x_and_y_from_point.md
Language: jp
"""

from typing import Dict

MAPPING: Dict[str, str] = {

    '# animation_scale_x_from_point and animation_scale_y_from_point interfaces':  # noqa
    '',

    'This page explains the `animation_scale_x_from_point` and `animation_scale_y_from_point` method interfaces.':  # noqa
    '',

    '## What interfaces are these?':
    '',

    'The `animation_scale_x_from_point` method interface will create an `ap.AnimationScaleXFromPoint` instance. You can animate the x-directional scale with it from a specified x-coordinate.\n\nSimilarly, the `animation_scale_y_from_point` method interface creates an `ap.AnimationScaleYFromPoint` instance. You can animate the y-directional scale with it from a specified y-coordinate.\n\nThese interfaces exist on a `GraphicsBase` subclass (that has the `scale_x_from_center` and `scale_y_from_center` interfaces), such as the `Rectangle` or `Circle`.':  # noqa
    '',

    '## Basic usage':
    '',

    'The following example sets the x-directional scale (left-side rectangle) and y-directional scale (right-side rectangle) animation (from 1.0 to 2.0) with the `animation_scale_x_from_point` and `animation_scale_y_from_point` methods.\n\nThese settings set the left-side rectangle scales from the left end (x=50) and the right-side rectangle scales from the bottom end (y=100).':  # noqa
    '',

    '```py\n# runnable\nfrom enum import Enum\n\nfrom typing_extensions import TypedDict\n\nimport apysc as ap\n\nDURATION: int = 1000\nEASING: ap.Easing = ap.Easing.EASE_OUT_QUINT\nLEFT_RECTANGLE_X: int = 50\nRIGHT_RECTANGLE_Y: int = 100\nSCALE_1: float = 1.0\nSCALE_2: float = 2.0\n\n\nclass Direction(Enum):\n    X = 1\n    Y = 2\n\n\nclass Options(TypedDict):\n    direction: Direction\n\n\ndef on_animation_complete_1(\n        e: ap.AnimationEvent[ap.Rectangle], options: Options) -> None:\n    """\n    The handler that the animation calls when its end.\n\n    Parameters\n    ----------\n    e : AnimationEvent\n        Event instance.\n    options : dict\n        Optional arguments dictionary.\n    """\n    rectangle: ap.Rectangle = e.this.target\n    if options[\'direction\'] == Direction.X:\n        rectangle.animation_scale_x_from_point(\n            scale_x_from_point=SCALE_1,\n            x=LEFT_RECTANGLE_X,\n            duration=DURATION,\n            easing=EASING,\n        ).animation_complete(\n            on_animation_complete_2,\n            options=options,\n        ).start()\n    elif options[\'direction\'] == Direction.Y:\n        rectangle.animation_scale_y_from_point(\n            scale_y_from_point=SCALE_1,\n            y=RIGHT_RECTANGLE_Y,\n            duration=DURATION,\n            easing=EASING,\n        ).animation_complete(\n            on_animation_complete_2,\n            options=options,\n        ).start()\n\n\ndef on_animation_complete_2(\n        e: ap.AnimationEvent[ap.Rectangle], options: Options) -> None:\n    """\n    The handler that the animation calls when its end.\n\n    Parameters\n    ----------\n    e : AnimationEvent\n        Event instance.\n    options : dict\n        Optional arguments dictionary.\n    """\n    rectangle: ap.Rectangle = e.this.target\n    if options[\'direction\'] == Direction.X:\n        rectangle.animation_scale_x_from_point(\n            scale_x_from_point=SCALE_2,\n            x=LEFT_RECTANGLE_X,\n            duration=DURATION,\n            easing=EASING,\n        ).animation_complete(\n            on_animation_complete_1,\n            options=options,\n        ).start()\n    elif options[\'direction\'] == Direction.Y:\n        rectangle.animation_scale_y_from_point(\n            scale_y_from_point=SCALE_2,\n            y=RIGHT_RECTANGLE_Y,\n            duration=DURATION,\n            easing=EASING,\n        ).animation_complete(\n            on_animation_complete_1,\n            options=options,\n        ).start()\n\n\nap.Stage(\n    stage_width=250, stage_height=150,\n    background_color=\'#333\', stage_elem_id=\'stage\')\nsprite: ap.Sprite = ap.Sprite()\nsprite.graphics.begin_fill(color=\'#0af\')\nleft_rectangle: ap.Rectangle = sprite.graphics.draw_rect(\n    x=50, y=50, width=50, height=50)\nright_rectangle: ap.Rectangle = sprite.graphics.draw_rect(\n    x=150, y=50, width=50, height=50)\n\noptions: Options = {\'direction\': Direction.X}\nleft_rectangle.animation_scale_x_from_point(\n    scale_x_from_point=SCALE_2,\n    x=LEFT_RECTANGLE_X,\n    duration=DURATION,\n    easing=EASING,\n).animation_complete(\n    on_animation_complete_1,\n    options=options,\n).start()\n\noptions = {\'direction\': Direction.Y}\nright_rectangle.animation_scale_y_from_point(\n    scale_y_from_point=SCALE_2,\n    y=RIGHT_RECTANGLE_Y,\n    duration=DURATION,\n    easing=EASING,\n).animation_complete(\n    on_animation_complete_1,\n    options=options,\n).start()\n\nap.save_overall_html(\n    dest_dir_path=\'./animation_scale_x_and_y_from_point_basic_usage/\')\n```':  # noqa
    '',

    '<iframe src="static/animation_scale_x_and_y_from_point_basic_usage/index.html" width="250" height="150"></iframe>':  # noqa
    '',

}
