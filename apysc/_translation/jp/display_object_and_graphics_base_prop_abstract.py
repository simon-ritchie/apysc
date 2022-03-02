"""This module is for the translation mapping data of the
following document:

Document file: display_object_and_graphics_base_prop_abstract.md
Language: jp
"""

from typing import Dict

MAPPING: Dict[str, str] = {

    '# DisplayObject and GraphicsBase classes base properties abstract':
    '',

    'This page explains the `DisplayObject` and `GraphicsBase` classes\' each property (such as the x, visible) abstract.':  # noqa
    '',

    '## What apysc can do in its properties':
    '',

    '- You can get/set each property value, such as the x, y, visible.':
    '',

    '## x and y properties':
    '',

    'The x and y properties can get/set the x and y coordinates.\n\n<details>\n<summary>Display the code block:</summary>':  # noqa
    '',

    '```py\n# runnable\nfrom typing_extensions import TypedDict\n\nimport apysc as ap\n\n\nclass RectOptions(TypedDict):\n    rectangle: ap.Rectangle\n    direction: ap.Int\n\n\ndef on_timer(e: ap.TimerEvent, options: RectOptions) -> None:\n    """\n    The handler that the timer calls.\n\n    Parameters\n    ----------\n    e : ap.TimerEvent\n        Event instance.\n    options : RectOptions\n        Optional arguments dictionary.\n    """\n    rectangle: ap.Rectangle = options[\'rectangle\']\n    direction: ap.Int = options[\'direction\']\n    rectangle.x += direction\n    rectangle.y += direction\n\n    with ap.If(rectangle.x >= 100):\n        direction.value = -1\n        ap.Return()\n\n    with ap.If(rectangle.x <= 50):\n        direction.value = 1\n        ap.Return()\n\n\nap.Stage(\n    background_color=\'#333\',\n    stage_width=200,\n    stage_height=200,\n    stage_elem_id=\'stage\')\nsprite: ap.Sprite = ap.Sprite()\nsprite.graphics.begin_fill(color=\'#0af\')\nrectangle: ap.Rectangle = sprite.graphics.draw_rect(\n    x=50, y=50, width=50, height=50)\n\ndirection: ap.Int = ap.Int(1)\noptions: RectOptions = {\'rectangle\': rectangle, \'direction\': direction}\nap.Timer(on_timer, delay=ap.FPS.FPS_60, options=options).start()\n\nap.save_overall_html(\n    dest_dir_path=\'do_and_graphics_base_prop_abstract_x_and_y/\')\n```':  # noqa
    '',

    '</details>\n\n<iframe src="static/do_and_graphics_base_prop_abstract_x_and_y/index.html" width="200" height="200"></iframe>\n\nFor more details, please see [DisplayObject class x and y interfaces](display_object_x_and_y.md).':  # noqa
    '',

    '## visible property':
    '',

    'The `visible` property can get/set the visibility of an object.\n\n<details>\n<summary>Display the code block:</summary>':  # noqa
    '',

    '```py\n# runnable\nfrom typing_extensions import TypedDict\n\nimport apysc as ap\n\n\nclass RectOptions(TypedDict):\n    rectangle: ap.Rectangle\n\n\ndef on_timer(e: ap.TimerEvent, options: RectOptions) -> None:\n    """\n    The handler that the timer calls.\n\n    Parameters\n    ----------\n    e : ap.TimerEvent\n        Event instance.\n    options : RectOptions\n        Optional arguments dictionary.\n    """\n    rectangle: ap.Rectangle = options[\'rectangle\']\n    rectangle.visible = rectangle.visible.not_\n\n\nap.Stage(\n    background_color=\'#333\',\n    stage_width=150,\n    stage_height=150,\n    stage_elem_id=\'stage\')\nsprite: ap.Sprite = ap.Sprite()\nsprite.graphics.begin_fill(color=\'#0af\')\nrectangle: ap.Rectangle = sprite.graphics.draw_rect(\n    x=50, y=50, width=50, height=50)\n\noptions: RectOptions = {\'rectangle\': rectangle}\nap.Timer(on_timer, delay=1000, options=options).start()\n\nap.save_overall_html(\n    dest_dir_path=\'do_and_graphics_base_prop_abstract_visible/\')\n```':  # noqa
    '',

    '</details>\n\n<iframe src="static/do_and_graphics_base_prop_abstract_visible/index.html" width="150" height="150"></iframe>\n\nFor more details, please see [DisplayObject class visible interface](display_object_visible.md).':  # noqa
    '',

    '## rotation interfaces':
    '',

    'The `rotation_around_center` property, `get_rotation_around_point` method, and `set_rotation_around_point` method can get/set the rotation angle.\n\n<details>\n<summary>Display the code block:</summary>':  # noqa
    '',

    '```py\n# runnable\nfrom typing_extensions import TypedDict\n\nimport apysc as ap\n\n\nclass RectOptions(TypedDict):\n    rectangle: ap.Rectangle\n\n\ndef on_timer(e: ap.TimerEvent, options: RectOptions) -> None:\n    """\n    The handler that the timer calls.\n\n    Parameters\n    ----------\n    e : ap.TimerEvent\n        Event instance.\n    options : RectOptions\n        Optional arguments dictionary.\n    """\n    rectangle: ap.Rectangle = options[\'rectangle\']\n    rectangle.rotation_around_center += 1\n\n\nap.Stage(\n    background_color=\'#333\',\n    stage_width=150,\n    stage_height=150,\n    stage_elem_id=\'stage\')\nsprite: ap.Sprite = ap.Sprite()\nsprite.graphics.begin_fill(color=\'#0af\')\nrectangle: ap.Rectangle = sprite.graphics.draw_rect(\n    x=50, y=50, width=50, height=50)\n\noptions: RectOptions = {\'rectangle\': rectangle}\nap.Timer(on_timer, delay=ap.FPS.FPS_60, options=options).start()\n\nap.save_overall_html(\n    dest_dir_path=\'do_and_graphics_base_prop_abstract_rotation/\')\n```':  # noqa
    '',

    '</details>\n\n<iframe src="static/do_and_graphics_base_prop_abstract_rotation/index.html" width="150" height="150"></iframe>\n\nFor more details, please see [GraphicsBase class rotation around center interface](graphics_base_rotation_around_center.md) and [GraphicsBase class rotation around point interfaces](graphics_base_rotation_around_point.md).':  # noqa
    '',

    '## scale interfaces':
    '',

    'The `scale_x_from_center` property, `scale_y_from_center` property, `get_scale_x_from_point` method, `set_scale_x_from_point` method, `get_scale_y_from_point` method, and `set_scale_y_from_point` method can get/set the scale values.\n\n<details>\n<summary>Display the code block:</summary>':  # noqa
    '',

    '```py\n# runnable\nfrom typing_extensions import TypedDict\n\nimport apysc as ap\n\n\nclass RectOptions(TypedDict):\n    rectangle: ap.Rectangle\n    scale_value: ap.Number\n\n\ndef on_timer(e: ap.TimerEvent, options: RectOptions) -> None:\n    """\n    The handler that the timer calls.\n\n    Parameters\n    ----------\n    e : ap.TimerEvent\n        Event instance.\n    options : RectOptions\n        Optional arguments dictionary.\n    """\n    rectangle: ap.Rectangle = options[\'rectangle\']\n    scale_value: ap.Number = options[\'scale_value\']\n    rectangle.scale_x_from_center += scale_value\n    rectangle.scale_y_from_center += scale_value\n\n    with ap.If(rectangle.scale_x_from_center >= 2.0):\n        scale_value.value = -0.01\n        ap.Return()\n\n    with ap.If(rectangle.scale_y_from_center <= 0.5):\n        scale_value.value = 0.01\n        ap.Return()\n\n\nap.Stage(\n    background_color=\'#333\',\n    stage_width=150,\n    stage_height=150,\n    stage_elem_id=\'stage\')\nsprite: ap.Sprite = ap.Sprite()\nsprite.graphics.begin_fill(color=\'#0af\')\nrectangle: ap.Rectangle = sprite.graphics.draw_rect(\n    x=50, y=50, width=50, height=50)\n\nscale_value: ap.Number = ap.Number(0.01)\noptions: RectOptions = {\'rectangle\': rectangle, \'scale_value\': scale_value}\nap.Timer(on_timer, delay=ap.FPS.FPS_60, options=options).start()\n\nap.save_overall_html(\n    dest_dir_path=\'do_and_graphics_base_prop_abstract_scale/\')\n```':  # noqa
    '',

    '</details>\n\n<iframe src="static/do_and_graphics_base_prop_abstract_scale/index.html" width="150" height="150"></iframe>\n\nFor more details, please see [GraphicsBase class scale from center interfaces](graphics_base_scale_from_center.md) and [GraphicsBase class scale from point interfaces](graphics_base_scale_from_point.md).':  # noqa
    '',

    '## flip properties':
    '',

    'The `flip_x` and `flip_y` properties can get/set the flip (reflection) setting.\n\n<details>\n<summary>Display the code block:</summary>':  # noqa
    '',

    '```py\n# runnable\nfrom typing_extensions import TypedDict\n\nimport apysc as ap\n\n\nclass LineOptions(TypedDict):\n    line: ap.Line\n\n\ndef on_timer(e: ap.TimerEvent, options: LineOptions) -> None:\n    """\n    The handler that the timer calls.\n\n    Parameters\n    ----------\n    e : ap.TimerEvent\n        Event instance.\n    options : LineOptions\n        Optional arguments dictionary.\n    """\n    line: ap.Line = options[\'line\']\n    line.flip_x = line.flip_x.not_\n\n\nap.Stage(\n    background_color=\'#333\',\n    stage_width=150,\n    stage_height=150,\n    stage_elem_id=\'stage\')\nsprite: ap.Sprite = ap.Sprite()\nsprite.graphics.line_style(color=\'#fff\', thickness=5)\nline: ap.Line = sprite.graphics.draw_line(\n    x_start=50, y_start=50, x_end=100, y_end=100)\n\noptions: LineOptions = {\'line\': line}\nap.Timer(on_timer, delay=1000, options=options).start()\n\nap.save_overall_html(\n    dest_dir_path=\'do_and_graphics_base_prop_abstract_flip/\')\n```':  # noqa
    '',

    '</details>\n\n<iframe src="static/do_and_graphics_base_prop_abstract_flip/index.html" width="150" height="150"></iframe>\n\nFor more details, please see [GraphicsBase class flip x and flip y interfaces](graphics_base_flip_interfaces.md).':  # noqa
    '',

    '## skew properties':
    '',

    'The `skew_x` and `skew_y` properties can get/set the skew-value.\n\n<details>\n<summary>Display the code block:</summary>':  # noqa
    '',

    '```py\n# runnable\nfrom typing_extensions import TypedDict\n\nimport apysc as ap\n\n\nclass RectOptions(TypedDict):\n    rectangle: ap.Rectangle\n\n\ndef on_timer(e: ap.TimerEvent, options: RectOptions) -> None:\n    """\n    The handler that the timer calls.\n\n    Parameters\n    ----------\n    e : ap.TimerEvent\n        Event instance.\n    options : RectOptions\n        Optional arguments dictionary.\n    """\n    rectangle: ap.Rectangle = options[\'rectangle\']\n    rectangle.skew_x += 1\n\n\nap.Stage(\n    background_color=\'#333\',\n    stage_width=150,\n    stage_height=150,\n    stage_elem_id=\'stage\')\nsprite: ap.Sprite = ap.Sprite()\nsprite.graphics.begin_fill(color=\'#0af\')\nrectangle: ap.Rectangle = sprite.graphics.draw_rect(\n    x=50, y=50, width=50, height=50)\n\noptions: RectOptions = {\'rectangle\': rectangle}\nap.Timer(on_timer, delay=ap.FPS.FPS_60, options=options).start()\n\nap.save_overall_html(\n    dest_dir_path=\'do_and_graphics_base_prop_abstract_skew/\')\n```':  # noqa
    '',

    '</details>\n\n<iframe src="static/do_and_graphics_base_prop_abstract_skew/index.html" width="150" height="150"></iframe>\n\nFor more details, please see [GraphicsBase class skew x and skew y interfaces](graphics_base_skew.md).':  # noqa
    '',

    '## See also':
    '',

    '- [DisplayObject class](display_object.md)\n- [DisplayObject class parent interfaces](display_object_parent.md)':  # noqa
    '',

}
