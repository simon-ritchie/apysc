"""This module is for the translation mapping data of the
following document:

Document file: display_object_and_graphics_base_prop_abstract.md
Language: jp
"""

from typing import Dict

MAPPING: Dict[str, str] = {
    ##################################################
    "# DisplayObject and GraphicsBase classes base properties abstract": "# DisplayObject と GraphicsBase クラスの基本的な属性の概要",  # noqa
    ##################################################
    "This page explains the `DisplayObject` and `GraphicsBase` classes' each property (such as the x, visible) abstract.": "このページでは`DisplayObject`や`GraphicsBase`の各サブクラスのxやvisibleなどの基本的な属性の概要について説明します。",  # noqa
    ##################################################
    "## What apysc can do in its properties": "## それらの属性でapyscができること",
    ##################################################
    "- You can get/set each property value, such as the x, y, visible.": "- xやy, visibleなどの属性の取得や更新を行うことができます。",  # noqa
    ##################################################
    "## x and y properties": "## x と y 属性",
    ##################################################
    "The x and y properties can get/set the x and y coordinates.": "xとy属性ではXとY座標を更新・取得することができます。",  # noqa
    ##################################################
    "<details>\n<summary>Display the code block:</summary>": "<details>\n<summary>コードブロックを表示:</summary>",  # noqa
    ##################################################
    '```py\n# runnable\nfrom typing_extensions import TypedDict\n\nimport apysc as ap\n\n\nclass RectOptions(TypedDict):\n    rectangle: ap.Rectangle\n    direction: ap.Int\n\n\ndef on_timer(e: ap.TimerEvent, options: RectOptions) -> None:\n    """\n    The handler that the timer calls.\n\n    Parameters\n    ----------\n    e : ap.TimerEvent\n        Event instance.\n    options : RectOptions\n        Optional arguments dictionary.\n    """\n    rectangle: ap.Rectangle = options["rectangle"]\n    direction: ap.Int = options["direction"]\n    rectangle.x += direction\n    rectangle.y += direction\n\n    with ap.If(rectangle.x >= 100):\n        direction.value = -1\n        ap.Return()\n\n    with ap.If(rectangle.x <= 50):\n        direction.value = 1\n        ap.Return()\n\n\nap.Stage(\n    background_color="#333", stage_width=200, stage_height=200, stage_elem_id="stage"\n)\nsprite: ap.Sprite = ap.Sprite()\nsprite.graphics.begin_fill(color="#0af")\nrectangle: ap.Rectangle = sprite.graphics.draw_rect(x=50, y=50, width=50, height=50)\n\ndirection: ap.Int = ap.Int(1)\noptions: RectOptions = {"rectangle": rectangle, "direction": direction}\nap.Timer(on_timer, delay=ap.FPS.FPS_60, options=options).start()\n\nap.save_overall_html(dest_dir_path="do_and_graphics_base_prop_abstract_x_and_y/")\n```': '```py\n# runnable\nfrom typing_extensions import TypedDict\n\nimport apysc as ap\n\n\nclass RectOptions(TypedDict):\n    rectangle: ap.Rectangle\n    direction: ap.Int\n\n\ndef on_timer(e: ap.TimerEvent, options: RectOptions) -> None:\n    """\n    The handler that the timer calls.\n\n    Parameters\n    ----------\n    e : ap.TimerEvent\n        Event instance.\n    options : RectOptions\n        Optional arguments dictionary.\n    """\n    rectangle: ap.Rectangle = options["rectangle"]\n    direction: ap.Int = options["direction"]\n    rectangle.x += direction\n    rectangle.y += direction\n\n    with ap.If(rectangle.x >= 100):\n        direction.value = -1\n        ap.Return()\n\n    with ap.If(rectangle.x <= 50):\n        direction.value = 1\n        ap.Return()\n\n\nap.Stage(\n    background_color="#333", stage_width=200, stage_height=200, stage_elem_id="stage"\n)\nsprite: ap.Sprite = ap.Sprite()\nsprite.graphics.begin_fill(color="#0af")\nrectangle: ap.Rectangle = sprite.graphics.draw_rect(x=50, y=50, width=50, height=50)\n\ndirection: ap.Int = ap.Int(1)\noptions: RectOptions = {"rectangle": rectangle, "direction": direction}\nap.Timer(on_timer, delay=ap.FPS.FPS_60, options=options).start()\n\nap.save_overall_html(dest_dir_path="do_and_graphics_base_prop_abstract_x_and_y/")\n```',  # noqa
    ##################################################
    "</details>": "</details>",
    ##################################################
    "For more details, please see the following:": "詳細については以下をご確認ください:",
    ##################################################
    "- [DisplayObject class x and y interfaces](display_object_x_and_y.md).": "- [DisplayObject クラスの x と y インターフェイス](jp_display_object_x_and_y.md)",  # noqa
    ##################################################
    "## visible property": "## visible 属性",
    ##################################################
    "The `visible` property can get/set the visibility of an object.": "`visible`属性ではオブジェクトの表示・非表示の属性値を取得・更新することができます。",  # noqa
    ##################################################
    "<details>\n<summary>Display the code block:</summary>": "<details>\n<summary>コードブロックを表示:</summary>",  # noqa
    ##################################################
    '```py\n# runnable\nfrom typing_extensions import TypedDict\n\nimport apysc as ap\n\n\nclass RectOptions(TypedDict):\n    rectangle: ap.Rectangle\n\n\ndef on_timer(e: ap.TimerEvent, options: RectOptions) -> None:\n    """\n    The handler that the timer calls.\n\n    Parameters\n    ----------\n    e : ap.TimerEvent\n        Event instance.\n    options : RectOptions\n        Optional arguments dictionary.\n    """\n    rectangle: ap.Rectangle = options["rectangle"]\n    rectangle.visible = rectangle.visible.not_\n\n\nap.Stage(\n    background_color="#333", stage_width=150, stage_height=150, stage_elem_id="stage"\n)\nsprite: ap.Sprite = ap.Sprite()\nsprite.graphics.begin_fill(color="#0af")\nrectangle: ap.Rectangle = sprite.graphics.draw_rect(x=50, y=50, width=50, height=50)\n\noptions: RectOptions = {"rectangle": rectangle}\nap.Timer(on_timer, delay=1000, options=options).start()\n\nap.save_overall_html(dest_dir_path="do_and_graphics_base_prop_abstract_visible/")\n```': '```py\n# runnable\nfrom typing_extensions import TypedDict\n\nimport apysc as ap\n\n\nclass RectOptions(TypedDict):\n    rectangle: ap.Rectangle\n\n\ndef on_timer(e: ap.TimerEvent, options: RectOptions) -> None:\n    """\n    The handler that the timer calls.\n\n    Parameters\n    ----------\n    e : ap.TimerEvent\n        Event instance.\n    options : RectOptions\n        Optional arguments dictionary.\n    """\n    rectangle: ap.Rectangle = options["rectangle"]\n    rectangle.visible = rectangle.visible.not_\n\n\nap.Stage(\n    background_color="#333", stage_width=150, stage_height=150, stage_elem_id="stage"\n)\nsprite: ap.Sprite = ap.Sprite()\nsprite.graphics.begin_fill(color="#0af")\nrectangle: ap.Rectangle = sprite.graphics.draw_rect(x=50, y=50, width=50, height=50)\n\noptions: RectOptions = {"rectangle": rectangle}\nap.Timer(on_timer, delay=1000, options=options).start()\n\nap.save_overall_html(dest_dir_path="do_and_graphics_base_prop_abstract_visible/")\n```',  # noqa
    ##################################################
    "</details>": "</details>",
    ##################################################
    "For more details, please see the following:": "詳細については以下をご確認ください:",
    ##################################################
    "- [DisplayObject class visible interface](display_object_visible.md).": "- [DisplayObject クラスの visible (表示・非表示) のインターフェイス](jp_display_object_visible.md)",  # noqa
    ##################################################
    "## rotation interfaces": "## 回転の各インターフェイス",
    ##################################################
    "The `rotation_around_center` property, `get_rotation_around_point` method, and `set_rotation_around_point` method can get/set the rotation angle.": "`rotation_around_center`属性、`get_rotation_around_point`メソッド、そして`set_rotation_around_point`メソッドでは回転の角度の値の取得と更新を行うことができます。",  # noqa
    ##################################################
    "<details>\n<summary>Display the code block:</summary>": "<details>\n<summary>コードブロックを表示:</summary>",  # noqa
    ##################################################
    '```py\n# runnable\nfrom typing_extensions import TypedDict\n\nimport apysc as ap\n\n\nclass RectOptions(TypedDict):\n    rectangle: ap.Rectangle\n\n\ndef on_timer(e: ap.TimerEvent, options: RectOptions) -> None:\n    """\n    The handler that the timer calls.\n\n    Parameters\n    ----------\n    e : ap.TimerEvent\n        Event instance.\n    options : RectOptions\n        Optional arguments dictionary.\n    """\n    rectangle: ap.Rectangle = options["rectangle"]\n    rectangle.rotation_around_center += 1\n\n\nap.Stage(\n    background_color="#333", stage_width=150, stage_height=150, stage_elem_id="stage"\n)\nsprite: ap.Sprite = ap.Sprite()\nsprite.graphics.begin_fill(color="#0af")\nrectangle: ap.Rectangle = sprite.graphics.draw_rect(x=50, y=50, width=50, height=50)\n\noptions: RectOptions = {"rectangle": rectangle}\nap.Timer(on_timer, delay=ap.FPS.FPS_60, options=options).start()\n\nap.save_overall_html(dest_dir_path="do_and_graphics_base_prop_abstract_rotation/")\n```': '```py\n# runnable\nfrom typing_extensions import TypedDict\n\nimport apysc as ap\n\n\nclass RectOptions(TypedDict):\n    rectangle: ap.Rectangle\n\n\ndef on_timer(e: ap.TimerEvent, options: RectOptions) -> None:\n    """\n    The handler that the timer calls.\n\n    Parameters\n    ----------\n    e : ap.TimerEvent\n        Event instance.\n    options : RectOptions\n        Optional arguments dictionary.\n    """\n    rectangle: ap.Rectangle = options["rectangle"]\n    rectangle.rotation_around_center += 1\n\n\nap.Stage(\n    background_color="#333", stage_width=150, stage_height=150, stage_elem_id="stage"\n)\nsprite: ap.Sprite = ap.Sprite()\nsprite.graphics.begin_fill(color="#0af")\nrectangle: ap.Rectangle = sprite.graphics.draw_rect(x=50, y=50, width=50, height=50)\n\noptions: RectOptions = {"rectangle": rectangle}\nap.Timer(on_timer, delay=ap.FPS.FPS_60, options=options).start()\n\nap.save_overall_html(dest_dir_path="do_and_graphics_base_prop_abstract_rotation/")\n```',  # noqa
    ##################################################
    "</details>": "</details>",
    ##################################################
    "For more details, please see the following:": "詳細については以下をご確認ください:",
    ##################################################
    "- [GraphicsBase class rotation_around_center interface](graphics_base_rotation_around_center.md)": "- [GraphicsBase クラスの rotation_around_center (中央座標基準の回転) インターフェイス](jp_graphics_base_rotation_around_center.md)",  # noqa
    ##################################################
    "- [GraphicsBase class rotation_around_point interfaces](graphics_base_rotation_around_point.md).": "- [GraphicsBase クラスの rotation_around_point (指定座標基準の回転) の各インターフェイス](jp_graphics_base_rotation_around_point.md)",  # noqa
    ##################################################
    "## scale interfaces": "## 拡縮の各インターフェイス",
    ##################################################
    "The `scale_x_from_center` property, `scale_y_from_center` property, `get_scale_x_from_point` method, `set_scale_x_from_point` method, `get_scale_y_from_point` method, and `set_scale_y_from_point` method can get/set the scale values.": "`scale_x_from_center`属性、`scale_y_from_center`属性、`get_scale_x_from_point`メソッド、`set_scale_x_from_point`メソッド、`get_scale_y_from_point`メソッド、そして`set_scale_y_from_point`メソッドの各インターフェイスでは拡縮の値の取得と更新を行うことができます。",  # noqa
    ##################################################
    "<details>\n<summary>Display the code block:</summary>": "<details>\n<summary>コードブロックを表示:</summary>",  # noqa
    ##################################################
    '```py\n# runnable\nfrom typing_extensions import TypedDict\n\nimport apysc as ap\n\n\nclass RectOptions(TypedDict):\n    rectangle: ap.Rectangle\n    scale_value: ap.Number\n\n\ndef on_timer(e: ap.TimerEvent, options: RectOptions) -> None:\n    """\n    The handler that the timer calls.\n\n    Parameters\n    ----------\n    e : ap.TimerEvent\n        Event instance.\n    options : RectOptions\n        Optional arguments dictionary.\n    """\n    rectangle: ap.Rectangle = options["rectangle"]\n    scale_value: ap.Number = options["scale_value"]\n    rectangle.scale_x_from_center += scale_value\n    rectangle.scale_y_from_center += scale_value\n\n    with ap.If(rectangle.scale_x_from_center >= 2.0):\n        scale_value.value = -0.01\n        ap.Return()\n\n    with ap.If(rectangle.scale_y_from_center <= 0.5):\n        scale_value.value = 0.01\n        ap.Return()\n\n\nap.Stage(\n    background_color="#333", stage_width=150, stage_height=150, stage_elem_id="stage"\n)\nsprite: ap.Sprite = ap.Sprite()\nsprite.graphics.begin_fill(color="#0af")\nrectangle: ap.Rectangle = sprite.graphics.draw_rect(x=50, y=50, width=50, height=50)\n\nscale_value: ap.Number = ap.Number(0.01)\noptions: RectOptions = {"rectangle": rectangle, "scale_value": scale_value}\nap.Timer(on_timer, delay=ap.FPS.FPS_60, options=options).start()\n\nap.save_overall_html(dest_dir_path="do_and_graphics_base_prop_abstract_scale/")\n```': '```py\n# runnable\nfrom typing_extensions import TypedDict\n\nimport apysc as ap\n\n\nclass RectOptions(TypedDict):\n    rectangle: ap.Rectangle\n    scale_value: ap.Number\n\n\ndef on_timer(e: ap.TimerEvent, options: RectOptions) -> None:\n    """\n    The handler that the timer calls.\n\n    Parameters\n    ----------\n    e : ap.TimerEvent\n        Event instance.\n    options : RectOptions\n        Optional arguments dictionary.\n    """\n    rectangle: ap.Rectangle = options["rectangle"]\n    scale_value: ap.Number = options["scale_value"]\n    rectangle.scale_x_from_center += scale_value\n    rectangle.scale_y_from_center += scale_value\n\n    with ap.If(rectangle.scale_x_from_center >= 2.0):\n        scale_value.value = -0.01\n        ap.Return()\n\n    with ap.If(rectangle.scale_y_from_center <= 0.5):\n        scale_value.value = 0.01\n        ap.Return()\n\n\nap.Stage(\n    background_color="#333", stage_width=150, stage_height=150, stage_elem_id="stage"\n)\nsprite: ap.Sprite = ap.Sprite()\nsprite.graphics.begin_fill(color="#0af")\nrectangle: ap.Rectangle = sprite.graphics.draw_rect(x=50, y=50, width=50, height=50)\n\nscale_value: ap.Number = ap.Number(0.01)\noptions: RectOptions = {"rectangle": rectangle, "scale_value": scale_value}\nap.Timer(on_timer, delay=ap.FPS.FPS_60, options=options).start()\n\nap.save_overall_html(dest_dir_path="do_and_graphics_base_prop_abstract_scale/")\n```',  # noqa
    ##################################################
    "</details>": "</details>",
    ##################################################
    "For more details, please see the following:": "詳細については以下をご確認ください:",
    ##################################################
    "- [GraphicsBase class scale_from_center interfaces](graphics_base_scale_from_center.md)": "- [GraphicsBase クラスの scale_from_center (中央座標基準の拡縮) の各インターフェイス](jp_graphics_base_scale_from_center.md)",  # noqa
    ##################################################
    "- [GraphicsBase class scale_from_point interfaces](graphics_base_scale_from_point.md).": "- [GraphicsBase クラスの scale_from_point (指定座標基準の拡縮) の各インターフェイス](jp_graphics_base_scale_from_point.md)",  # noqa
    ##################################################
    "## flip properties": "## 反転の各属性",
    ##################################################
    "The `flip_x` and `flip_y` properties can get/set the flip (reflection) setting.": "`flip_x`と`flip_y`の属性では反転の属性値の取得と更新を行うことができます。",  # noqa
    ##################################################
    "<details>\n<summary>Display the code block:</summary>": "<details>\n<summary>コードブロックを表示:</summary>",  # noqa
    ##################################################
    '```py\n# runnable\nfrom typing_extensions import TypedDict\n\nimport apysc as ap\n\n\nclass LineOptions(TypedDict):\n    line: ap.Line\n\n\ndef on_timer(e: ap.TimerEvent, options: LineOptions) -> None:\n    """\n    The handler that the timer calls.\n\n    Parameters\n    ----------\n    e : ap.TimerEvent\n        Event instance.\n    options : LineOptions\n        Optional arguments dictionary.\n    """\n    line: ap.Line = options["line"]\n    line.flip_x = line.flip_x.not_\n\n\nap.Stage(\n    background_color="#333", stage_width=150, stage_height=150, stage_elem_id="stage"\n)\nsprite: ap.Sprite = ap.Sprite()\nsprite.graphics.line_style(color="#fff", thickness=5)\nline: ap.Line = sprite.graphics.draw_line(x_start=50, y_start=50, x_end=100, y_end=100)\n\noptions: LineOptions = {"line": line}\nap.Timer(on_timer, delay=1000, options=options).start()\n\nap.save_overall_html(dest_dir_path="do_and_graphics_base_prop_abstract_flip/")\n```': '```py\n# runnable\nfrom typing_extensions import TypedDict\n\nimport apysc as ap\n\n\nclass LineOptions(TypedDict):\n    line: ap.Line\n\n\ndef on_timer(e: ap.TimerEvent, options: LineOptions) -> None:\n    """\n    The handler that the timer calls.\n\n    Parameters\n    ----------\n    e : ap.TimerEvent\n        Event instance.\n    options : LineOptions\n        Optional arguments dictionary.\n    """\n    line: ap.Line = options["line"]\n    line.flip_x = line.flip_x.not_\n\n\nap.Stage(\n    background_color="#333", stage_width=150, stage_height=150, stage_elem_id="stage"\n)\nsprite: ap.Sprite = ap.Sprite()\nsprite.graphics.line_style(color="#fff", thickness=5)\nline: ap.Line = sprite.graphics.draw_line(x_start=50, y_start=50, x_end=100, y_end=100)\n\noptions: LineOptions = {"line": line}\nap.Timer(on_timer, delay=1000, options=options).start()\n\nap.save_overall_html(dest_dir_path="do_and_graphics_base_prop_abstract_flip/")\n```',  # noqa
    ##################################################
    "</details>": "</details>",
    ##################################################
    "For more details, please see the following:": "詳細については以下をご確認ください:",
    ##################################################
    "- [GraphicsBase class flip_x and flip_y interfaces](graphics_base_flip_interfaces.md)": "- [GraphicsBase クラスの flip_x (横軸の反転) と flip_y (縦軸の反転) のインターフェイス](jp_graphics_base_flip_interfaces.md)",  # noqa
    ##################################################
    "## skew properties": "## 歪みの各属性",
    ##################################################
    "The `skew_x` and `skew_y` properties can get/set the skew-value.": "`skew_x`と`skew_y`の各属性では歪みの値を取得・更新することができます。",  # noqa
    ##################################################
    "<details>\n<summary>Display the code block:</summary>": "<details>\n<summary>コードブロックを表示:</summary>",  # noqa
    ##################################################
    '```py\n# runnable\nfrom typing_extensions import TypedDict\n\nimport apysc as ap\n\n\nclass RectOptions(TypedDict):\n    rectangle: ap.Rectangle\n\n\ndef on_timer(e: ap.TimerEvent, options: RectOptions) -> None:\n    """\n    The handler that the timer calls.\n\n    Parameters\n    ----------\n    e : ap.TimerEvent\n        Event instance.\n    options : RectOptions\n        Optional arguments dictionary.\n    """\n    rectangle: ap.Rectangle = options["rectangle"]\n    rectangle.skew_x += 1\n\n\nap.Stage(\n    background_color="#333", stage_width=150, stage_height=150, stage_elem_id="stage"\n)\nsprite: ap.Sprite = ap.Sprite()\nsprite.graphics.begin_fill(color="#0af")\nrectangle: ap.Rectangle = sprite.graphics.draw_rect(x=50, y=50, width=50, height=50)\n\noptions: RectOptions = {"rectangle": rectangle}\nap.Timer(on_timer, delay=ap.FPS.FPS_60, options=options).start()\n\nap.save_overall_html(dest_dir_path="do_and_graphics_base_prop_abstract_skew/")\n```': '```py\n# runnable\nfrom typing_extensions import TypedDict\n\nimport apysc as ap\n\n\nclass RectOptions(TypedDict):\n    rectangle: ap.Rectangle\n\n\ndef on_timer(e: ap.TimerEvent, options: RectOptions) -> None:\n    """\n    The handler that the timer calls.\n\n    Parameters\n    ----------\n    e : ap.TimerEvent\n        Event instance.\n    options : RectOptions\n        Optional arguments dictionary.\n    """\n    rectangle: ap.Rectangle = options["rectangle"]\n    rectangle.skew_x += 1\n\n\nap.Stage(\n    background_color="#333", stage_width=150, stage_height=150, stage_elem_id="stage"\n)\nsprite: ap.Sprite = ap.Sprite()\nsprite.graphics.begin_fill(color="#0af")\nrectangle: ap.Rectangle = sprite.graphics.draw_rect(x=50, y=50, width=50, height=50)\n\noptions: RectOptions = {"rectangle": rectangle}\nap.Timer(on_timer, delay=ap.FPS.FPS_60, options=options).start()\n\nap.save_overall_html(dest_dir_path="do_and_graphics_base_prop_abstract_skew/")\n```',  # noqa
    ##################################################
    "</details>": "</details>",
    ##################################################
    "For more details, please see the following:": "詳細については以下をご確認ください:",
    ##################################################
    "- [GraphicsBase class skew_x and skew_y interfaces](graphics_base_skew.md).": "- [GraphicsBase クラスの skew_x (X軸の歪み) と skew_y (Y軸の歪み) のインターフェイス](jp_graphics_base_skew.md)",  # noqa
    ##################################################
    "## See also": "## 関連資料",
    ##################################################
    "- [DisplayObject class](display_object.md)": "- [DisplayObject クラス](jp_display_object.md)",  # noqa
    ##################################################
    "- [DisplayObject class parent interfaces](display_object_parent.md)": "- [DisplayObjectクラス parent （親要素属性）のインターフェイス](jp_display_object_parent.md)",  # noqa
}
