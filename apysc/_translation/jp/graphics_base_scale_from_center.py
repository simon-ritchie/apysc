"""This module is for the translation mapping data of the
following document:

Document file: graphics_base_scale_from_center.md
Language: jp
"""

from typing import Dict

MAPPING: Dict[str, str] = {
    ##################################################
    "# GraphicsBase scale_x_from_center and scale_y_from_center interfaces": "# GraphicsBase クラスの scale_x_from_center と scale_y_from_center インターフェイス",  # noqa
    ##################################################
    "This page explains the `GraphicsBase` class (base class of each graphic, such as the `Rectangle`) `scale_x_from_center` and `scale_y_from_center` property interfaces.": "このページでは`GraphicsBase`クラス（`Rectangle`などの各グラフィッククラスの基底クラス）の`scale_x_from_center`と`scale_y_from_center`属性のインターフェイスについて説明します。",  # noqa
    ##################################################
    "## What interfaces are these?": "## 各インターフェイスの概要",
    ##################################################
    "The `scale_x_from_center` property changes the object's horizontal scale, and the `scale_y_from_center` property changes the object's vertical scale. These scaling interfaces change the scale from the center coordinates of each object.": "`scale_x_from_center`属性はオブジェクトの水平方向の拡縮を変更し、`scale_y_from_center`属性は垂直方向の拡縮を変更します。これらの拡縮のインターフェイスはオブジェクトの中央座標を基準に実行されます。",  # noqa
    ##################################################
    "## Basic usage": "## 基本的な使い方",
    ##################################################
    "Each property getter interface returns a `Number` value. The setter interfaces also require a `Number` to update scales (If 0.0 is specified, the object becomes invisible. 1.0 becomes the default scale, and 2.0 becomes the twice-scale value).": "各属性のgetterのインターフェイスは`Number`型の値を返却します。setterのインターフェイスでは拡縮の更新値として`Number`型の値の指定が必要になります（もしも0.0が指定されればオブジェクトは見えなくなり、1.0でデフォルトの拡縮、2.0で2倍のサイズになります）。",  # noqa
    ##################################################
    "The following example shows the default scale rectangle (left), horizontally half-scaled rectangle (center), vertically half-scaled rectangle (right).": "以下のコード例では左の四角ではデフォルトの拡縮値、真ん中の四角では水平方向に半分のサイズ、→の四角では垂直方向に半分のサイズを設定しています。",  # noqa
    ##################################################
    '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    stage_width=350,\n    stage_height=150,\n    background_color=ap.Color("#333"),\n    stage_elem_id="stage",\n)\nsprite: ap.Sprite = ap.Sprite()\nsprite.graphics.begin_fill(color=ap.Color("#0af"))\n\nleft_rectangle: ap.Rectangle = sprite.graphics.draw_rect(\n    x=50, y=50, width=50, height=50\n)\ncenter_rectangle: ap.Rectangle = sprite.graphics.draw_rect(\n    x=150, y=50, width=50, height=50\n)\ncenter_rectangle.scale_x_from_center = ap.Number(0.5)\nright_rectangle: ap.Rectangle = sprite.graphics.draw_rect(\n    x=250, y=50, width=50, height=50\n)\nright_rectangle.scale_y_from_center = ap.Number(0.5)\n\nap.save_overall_html(dest_dir_path="graphics_base_scale_from_center_basic_usage_1/")\n```': '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    stage_width=350,\n    stage_height=150,\n    background_color=ap.Color("#333"),\n    stage_elem_id="stage",\n)\nsprite: ap.Sprite = ap.Sprite()\nsprite.graphics.begin_fill(color=ap.Color("#0af"))\n\nleft_rectangle: ap.Rectangle = sprite.graphics.draw_rect(\n    x=50, y=50, width=50, height=50\n)\ncenter_rectangle: ap.Rectangle = sprite.graphics.draw_rect(\n    x=150, y=50, width=50, height=50\n)\ncenter_rectangle.scale_x_from_center = ap.Number(0.5)\nright_rectangle: ap.Rectangle = sprite.graphics.draw_rect(\n    x=250, y=50, width=50, height=50\n)\nright_rectangle.scale_y_from_center = ap.Number(0.5)\n\nap.save_overall_html(dest_dir_path="graphics_base_scale_from_center_basic_usage_1/")\n```',  # noqa
    ##################################################
    "These interfaces apply the scaling from the center coordinates as follows:": "これらのインターフェイスでは以下の例のように中央座標を基準に拡縮が実行されます:",  # noqa
    ##################################################
    '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    stage_width=150,\n    stage_height=150,\n    background_color=ap.Color("#333"),\n    stage_elem_id="stage",\n)\nsprite: ap.Sprite = ap.Sprite()\nsprite.graphics.begin_fill(color=ap.Color("#0af"), alpha=0.3)\n\nrectangle_1: ap.Rectangle = sprite.graphics.draw_rect(x=50, y=50, width=50, height=50)\n\nrectangle_2: ap.Rectangle = sprite.graphics.draw_rect(x=50, y=50, width=50, height=50)\nrectangle_2.scale_x_from_center = ap.Number(0.5)\nrectangle_2.scale_y_from_center = ap.Number(0.5)\n\nrectangle_3: ap.Rectangle = sprite.graphics.draw_rect(x=50, y=50, width=50, height=50)\nrectangle_3.scale_x_from_center = ap.Number(0.25)\nrectangle_3.scale_y_from_center = ap.Number(0.25)\n\nap.save_overall_html(dest_dir_path="graphics_base_scale_from_center_basic_usage_2/")\n```': '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    stage_width=150,\n    stage_height=150,\n    background_color=ap.Color("#333"),\n    stage_elem_id="stage",\n)\nsprite: ap.Sprite = ap.Sprite()\nsprite.graphics.begin_fill(color=ap.Color("#0af"), alpha=0.3)\n\nrectangle_1: ap.Rectangle = sprite.graphics.draw_rect(x=50, y=50, width=50, height=50)\n\nrectangle_2: ap.Rectangle = sprite.graphics.draw_rect(x=50, y=50, width=50, height=50)\nrectangle_2.scale_x_from_center = ap.Number(0.5)\nrectangle_2.scale_y_from_center = ap.Number(0.5)\n\nrectangle_3: ap.Rectangle = sprite.graphics.draw_rect(x=50, y=50, width=50, height=50)\nrectangle_3.scale_x_from_center = ap.Number(0.25)\nrectangle_3.scale_y_from_center = ap.Number(0.25)\n\nap.save_overall_html(dest_dir_path="graphics_base_scale_from_center_basic_usage_2/")\n```',  # noqa
    ##################################################
    "The `+=` and `-=` operators are also supported:": "`+=`や`-=`記号のオペレーターによる操作もサポートしています:",  # noqa
    ##################################################
    '```py\n# runnable\nfrom typing_extensions import TypedDict\n\nimport apysc as ap\n\n\nclass _RectanglesOptions(TypedDict):\n    rectangle_1: ap.Rectangle\n    rectangle_2: ap.Rectangle\n    direction: ap.Int\n\n\ndef on_timer(e: ap.TimerEvent, options: _RectanglesOptions) -> None:\n    """\n    The handler that the timer calls.\n\n    Parameters\n    ----------\n    e : ap.TimerEvent\n        Event instance.\n    options : dict\n        Optional arguments dictionary.\n    """\n    rectangle_1: ap.Rectangle = options["rectangle_1"]\n    rectangle_2: ap.Rectangle = options["rectangle_2"]\n    direction: ap.Int = options["direction"]\n\n    current_scale: ap.Number = rectangle_1.scale_x_from_center\n    condition_1: ap.Boolean = current_scale >= 2.0\n    condition_2: ap.Boolean = current_scale <= 0.05\n    with ap.If(condition_1):\n        direction.value = -1\n    with ap.Elif(condition_2):\n        direction.value = 1\n\n    rectangle_1.scale_x_from_center += direction * 0.03\n    rectangle_2.scale_y_from_center += direction * 0.03\n\n\nap.Stage(\n    stage_width=150,\n    stage_height=150,\n    background_color=ap.Color("#333"),\n    stage_elem_id="stage",\n)\nsprite: ap.Sprite = ap.Sprite()\n\nsprite.graphics.begin_fill(color=ap.Color("#0af"), alpha=0.5)\nrectangle_1: ap.Rectangle = sprite.graphics.draw_rect(x=50, y=50, width=50, height=50)\n\nsprite.graphics.begin_fill(color=ap.Color("#f0a"), alpha=0.5)\nrectangle_2: ap.Rectangle = sprite.graphics.draw_rect(x=50, y=50, width=50, height=50)\n\n\ndirection: ap.Int = ap.Int(1.0)\noptions: _RectanglesOptions = {\n    "rectangle_1": rectangle_1,\n    "rectangle_2": rectangle_2,\n    "direction": direction,\n}\ntimer: ap.Timer = ap.Timer(on_timer, delay=ap.FPS.FPS_60, options=options)\ntimer.start()\n\nap.save_overall_html(dest_dir_path="graphics_base_scale_from_center_basic_usage_3/")\n```': '```py\n# runnable\nfrom typing_extensions import TypedDict\n\nimport apysc as ap\n\n\nclass _RectanglesOptions(TypedDict):\n    rectangle_1: ap.Rectangle\n    rectangle_2: ap.Rectangle\n    direction: ap.Int\n\n\ndef on_timer(e: ap.TimerEvent, options: _RectanglesOptions) -> None:\n    """\n    The handler that the timer calls.\n\n    Parameters\n    ----------\n    e : ap.TimerEvent\n        Event instance.\n    options : dict\n        Optional arguments dictionary.\n    """\n    rectangle_1: ap.Rectangle = options["rectangle_1"]\n    rectangle_2: ap.Rectangle = options["rectangle_2"]\n    direction: ap.Int = options["direction"]\n\n    current_scale: ap.Number = rectangle_1.scale_x_from_center\n    condition_1: ap.Boolean = current_scale >= 2.0\n    condition_2: ap.Boolean = current_scale <= 0.05\n    with ap.If(condition_1):\n        direction.value = -1\n    with ap.Elif(condition_2):\n        direction.value = 1\n\n    rectangle_1.scale_x_from_center += direction * 0.03\n    rectangle_2.scale_y_from_center += direction * 0.03\n\n\nap.Stage(\n    stage_width=150,\n    stage_height=150,\n    background_color=ap.Color("#333"),\n    stage_elem_id="stage",\n)\nsprite: ap.Sprite = ap.Sprite()\n\nsprite.graphics.begin_fill(color=ap.Color("#0af"), alpha=0.5)\nrectangle_1: ap.Rectangle = sprite.graphics.draw_rect(x=50, y=50, width=50, height=50)\n\nsprite.graphics.begin_fill(color=ap.Color("#f0a"), alpha=0.5)\nrectangle_2: ap.Rectangle = sprite.graphics.draw_rect(x=50, y=50, width=50, height=50)\n\n\ndirection: ap.Int = ap.Int(1.0)\noptions: _RectanglesOptions = {\n    "rectangle_1": rectangle_1,\n    "rectangle_2": rectangle_2,\n    "direction": direction,\n}\ntimer: ap.Timer = ap.Timer(on_timer, delay=ap.FPS.FPS_60, options=options)\ntimer.start()\n\nap.save_overall_html(dest_dir_path="graphics_base_scale_from_center_basic_usage_3/")\n```',  # noqa
    ##################################################
    "## scale_x_from_center property API": "## scale_x_from_center 属性のAPI",
    ##################################################
    '<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>': '<span class="inconspicuous-txt">特記事項: このAPIドキュメントはドキュメントビルド用のスクリプトによって自動で生成・同期されています。そのためもしかしたらこの節の内容は前節までの内容と重複している場合があります。</span>',  # noqa
    ##################################################
    "**[Interface summary]**": "**[インターフェイス概要]**",
    ##################################################
    "Get a scale-x value from the center of this instance.<hr>": "インスタンスの中央座標を基準とした水平方向の拡縮の値を取得します。<hr>",  # noqa
    ##################################################
    "**[Returns]**": "**[返却値]**",
    ##################################################
    "- `scale_x_from_center`: ap.Number": "- `scale_x_from_center`: ap.Number",
    ##################################################
    "  - Scale-x value from the center of this instance.": "  - インスタンスの中央座標を基準とした水平方向の拡縮の値。",  # noqa
    ##################################################
    "<hr>": "<hr>",
    ##################################################
    "**[Notes]**": "**[特記事項]**",
    ##################################################
    "The scale's minimum value is almost zero, and it does not become negative.<hr>": "拡縮の最小値はほぼ0となり、その値は負の値にはなりません。<hr>",  # noqa
    ##################################################
    "**[Examples]**": "**[コードサンプル]**",
    ##################################################
    '```py\n>>> import apysc as ap\n>>> stage: ap.Stage = ap.Stage()\n>>> sprite: ap.Sprite = ap.Sprite()\n>>> sprite.graphics.begin_fill(color=ap.Color("#0af"))\n>>> rectangle: ap.Rectangle = sprite.graphics.draw_rect(\n...     x=50, y=50, width=50, height=50\n... )\n>>> rectangle.scale_x_from_center = ap.Number(1.5)\n>>> rectangle.scale_x_from_center\nNumber(1.5)\n```': '```py\n>>> import apysc as ap\n>>> stage: ap.Stage = ap.Stage()\n>>> sprite: ap.Sprite = ap.Sprite()\n>>> sprite.graphics.begin_fill(color=ap.Color("#0af"))\n>>> rectangle: ap.Rectangle = sprite.graphics.draw_rect(\n...     x=50, y=50, width=50, height=50\n... )\n>>> rectangle.scale_x_from_center = ap.Number(1.5)\n>>> rectangle.scale_x_from_center\nNumber(1.5)\n```',  # noqa
    ##################################################
    "## scale_y_from_center property API": "## scale_y_from_center 属性のAPI",
    ##################################################
    '<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>': '<span class="inconspicuous-txt">特記事項: このAPIドキュメントはドキュメントビルド用のスクリプトによって自動で生成・同期されています。そのためもしかしたらこの節の内容は前節までの内容と重複している場合があります。</span>',  # noqa
    ##################################################
    "**[Interface summary]**": "**[インターフェイス概要]**",
    ##################################################
    "Get a scale-y value from the center of this instance.<hr>": "インスタンスの中央座標を基準とした垂直方向の拡縮の値を取得します。<hr>",  # noqa
    ##################################################
    "**[Returns]**": "**[返却値]**",
    ##################################################
    "- `scale_y_from_center`: ap.Number": "- `scale_y_from_center`: ap.Number",
    ##################################################
    "  - Scale-y value from the center of this instance.": "  - インスタンスの中央座標を基準とした垂直方向の拡縮の値。",  # noqa
    ##################################################
    "<hr>": "<hr>",
    ##################################################
    "**[Notes]**": "**[特記事項]**",
    ##################################################
    "The scale's minimum value is almost zero, and it does not become negative.<hr>": "拡縮の最小値はほぼ0となり、その値は負の値にはなりません。<hr>",  # noqa
    ##################################################
    "**[Examples]**": "**[コードサンプル]**",
    ##################################################
    '```py\n>>> import apysc as ap\n>>> stage: ap.Stage = ap.Stage()\n>>> sprite: ap.Sprite = ap.Sprite()\n>>> sprite.graphics.begin_fill(color=ap.Color("#0af"))\n>>> rectangle: ap.Rectangle = sprite.graphics.draw_rect(\n...     x=50, y=50, width=50, height=50\n... )\n>>> rectangle.scale_y_from_center = ap.Number(1.5)\n>>> rectangle.scale_y_from_center\nNumber(1.5)\n```': '```py\n>>> import apysc as ap\n>>> stage: ap.Stage = ap.Stage()\n>>> sprite: ap.Sprite = ap.Sprite()\n>>> sprite.graphics.begin_fill(color=ap.Color("#0af"))\n>>> rectangle: ap.Rectangle = sprite.graphics.draw_rect(\n...     x=50, y=50, width=50, height=50\n... )\n>>> rectangle.scale_y_from_center = ap.Number(1.5)\n>>> rectangle.scale_y_from_center\nNumber(1.5)\n```',  # noqa
}
