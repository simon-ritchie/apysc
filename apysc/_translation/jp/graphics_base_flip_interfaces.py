"""This module is for the translation mapping data of the
following document:

Document file: graphics_base_flip_interfaces.md
Language: jp
"""

from typing import Dict

MAPPING: Dict[str, str] = {
    ##################################################
    "# GraphicsBase flip_x and flip_y interfaces": "# GraphicsBase クラスの flip_x と flip_y インターフェイス",  # noqa
    ##################################################
    "This page explains the `GraphicsBase` class (base class of each graphic, such as the `Rectangle`) `flip_x` and `flip_y` property interfaces.": "このページでは`GraphicsBase`クラス（`Rectangle`などの各グラフィッククラスの基底クラス）の`flip_x`と`flip_y`属性のインターフェイスについて説明します。",  # noqa
    ##################################################
    "## What interfaces are these?": "## 各インターフェイスの概要",
    ##################################################
    "The `flip_x` property flips an object in the x-axis direction, and the `flip_y` property flips in the y-axis direction.": "`flip_x`属性はオブジェクトを横方向に反転し、`flip_y`属性はオブジェクトを縦方向に反転します。",  # noqa
    ##################################################
    "## Basic usage": "## 基本的な使い方",
    ##################################################
    "The `flip_x` and `flip_y` can be set a `Boolean` value. If you set the `True`\\, an object becomes flipped. Conversely, if you set the `False`\\, an object resets flipping.": "`flip_x`と`flip_y`には`Boolean`型の値を設定できます。もし`True`を指定すれば反転した状態になり、`False`を設定すれ反転がリセットされます。",  # noqa
    ##################################################
    "The getter interface returns a `Boolean` value of a current flipping value.": "getterのインターフェイスでは現在の反転設定の`Boolean`型の値を返却します。",  # noqa
    ##################################################
    "The following example flips the triangle polygon in the x-axis direction and resets per second:": "以下のコード例では1秒ごとに三角形の反転とリセットを行っています。",  # noqa
    ##################################################
    '```py\n# runnable\nfrom typing_extensions import TypedDict\n\nimport apysc as ap\n\n\nclass _PolygonOptions(TypedDict):\n    polygon: ap.Polygon\n\n\ndef on_timer(e: ap.TimerEvent, options: _PolygonOptions) -> None:\n    """\n    The handler that the timer calls.\n\n    Parameters\n    ----------\n    e : ap.TimerEvent\n        Event instance.\n    options : dict\n        Optional arguments dictionary.\n    """\n    polygon: ap.Polygon = options["polygon"]\n    flip_x: ap.Boolean = polygon.flip_x\n    flip_x = flip_x.not_\n    polygon.flip_x = flip_x\n\n\nap.Stage(\n    stage_width=150, stage_height=150, background_color="#333", stage_elem_id="stage"\n)\nsprite: ap.Sprite = ap.Sprite()\nsprite.graphics.begin_fill(color="#0af")\n\npolygon: ap.Polygon = sprite.graphics.draw_polygon(\n    points=[\n        ap.Point2D(x=50, y=50),\n        ap.Point2D(x=50, y=100),\n        ap.Point2D(x=100, y=75),\n    ]\n)\noptions: _PolygonOptions = {"polygon": polygon}\ntimer: ap.Timer = ap.Timer(on_timer, delay=1000, options=options)\ntimer.start()\n\nap.save_overall_html(dest_dir_path="graphics_base_flip_x_basic_usage/")\n```': '```py\n# runnable\nfrom typing_extensions import TypedDict\n\nimport apysc as ap\n\n\nclass _PolygonOptions(TypedDict):\n    polygon: ap.Polygon\n\n\ndef on_timer(e: ap.TimerEvent, options: _PolygonOptions) -> None:\n    """\n    The handler that the timer calls.\n\n    Parameters\n    ----------\n    e : ap.TimerEvent\n        Event instance.\n    options : dict\n        Optional arguments dictionary.\n    """\n    polygon: ap.Polygon = options["polygon"]\n    flip_x: ap.Boolean = polygon.flip_x\n    flip_x = flip_x.not_\n    polygon.flip_x = flip_x\n\n\nap.Stage(\n    stage_width=150, stage_height=150, background_color="#333", stage_elem_id="stage"\n)\nsprite: ap.Sprite = ap.Sprite()\nsprite.graphics.begin_fill(color="#0af")\n\npolygon: ap.Polygon = sprite.graphics.draw_polygon(\n    points=[\n        ap.Point2D(x=50, y=50),\n        ap.Point2D(x=50, y=100),\n        ap.Point2D(x=100, y=75),\n    ]\n)\noptions: _PolygonOptions = {"polygon": polygon}\ntimer: ap.Timer = ap.Timer(on_timer, delay=1000, options=options)\ntimer.start()\n\nap.save_overall_html(dest_dir_path="graphics_base_flip_x_basic_usage/")\n```',  # noqa
    ##################################################
    "The `flip_y` interface behaves the same as the `flip_x` interface, except the axis direction.": "`flip_y`インターフェイスは軸の方向の違いを除いて`flip_x`の員スターフェイスと同様に動作します。",  # noqa
    ##################################################
    "## flip_x property API": "## flip_x 属性のAPI",
    ##################################################
    '<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>': '<span class="inconspicuous-txt">特記事項: このAPIドキュメントはドキュメントビルド用のスクリプトによって自動で生成・同期されています。そのためもしかしたらこの節の内容は前節までの内容と重複している場合があります。</span>',  # noqa
    ##################################################
    "**[Interface summary]**": "**[インターフェイス概要]**",
    ##################################################
    "Get a boolean value whether the x-axis is flipping or not.<hr>": "横軸に対して反転しているかどうかの真偽値を取得します。<hr>",  # noqa
    ##################################################
    "**[Returns]**": "**[返却値]**",
    ##################################################
    "- `flip_x`: Boolean": "- `flip_x`: Boolean",
    ##################################################
    "  - A boolean value whether the x-axis is flipping or not.": "  - 横方向に反転しているかどうかのBooleanの真偽値。",  # noqa
    ##################################################
    "<hr>": "<hr>",
    ##################################################
    "**[Examples]**": "**[コードサンプル]**",
    ##################################################
    '```py\n>>> import apysc as ap\n>>> stage: ap.Stage = ap.Stage()\n>>> sprite: ap.Sprite = ap.Sprite()\n>>> sprite.graphics.begin_fill(color="#0af")\n>>> polygon: ap.Polygon = sprite.graphics.draw_polygon(\n...     points=[\n...         ap.Point2D(x=0, y=0),\n...         ap.Point2D(x=0, y=50),\n...         ap.Point2D(x=50, y=25),\n...     ]\n... )\n>>> polygon.flip_x = ap.Boolean(True)\n>>> polygon.flip_x\nBoolean(True)\n```': '```py\n>>> import apysc as ap\n>>> stage: ap.Stage = ap.Stage()\n>>> sprite: ap.Sprite = ap.Sprite()\n>>> sprite.graphics.begin_fill(color="#0af")\n>>> polygon: ap.Polygon = sprite.graphics.draw_polygon(\n...     points=[\n...         ap.Point2D(x=0, y=0),\n...         ap.Point2D(x=0, y=50),\n...         ap.Point2D(x=50, y=25),\n...     ]\n... )\n>>> polygon.flip_x = ap.Boolean(True)\n>>> polygon.flip_x\nBoolean(True)\n```',  # noqa
    ##################################################
    "## flip_y property API": "## flip_y 属性のAPI",
    ##################################################
    '<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>': '<span class="inconspicuous-txt">特記事項: このAPIドキュメントはドキュメントビルド用のスクリプトによって自動で生成・同期されています。そのためもしかしたらこの節の内容は前節までの内容と重複している場合があります。</span>',  # noqa
    ##################################################
    "**[Interface summary]**": "**[インターフェイス概要]**",
    ##################################################
    "Get a boolean value whether the y-axis is flipping or not.<hr>": "縦軸に対して反転しているかどうかの真偽値を取得します。<hr>",  # noqa
    ##################################################
    "**[Returns]**": "**[返却値]**",
    ##################################################
    "- `flip_y`: Boolean": "- `flip_y`: Boolean",
    ##################################################
    "  - A boolean value whether the y-axis is flipping or not.": "  - 縦方向に反転しているかどうかのBooleanの真偽値。",  # noqa
    ##################################################
    "<hr>": "<hr>",
    ##################################################
    "**[Examples]**": "**[コードサンプル]**",
    ##################################################
    '```py\n>>> import apysc as ap\n>>> stage: ap.Stage = ap.Stage()\n>>> sprite: ap.Sprite = ap.Sprite()\n>>> sprite.graphics.begin_fill(color="#0af")\n>>> polygon: ap.Polygon = sprite.graphics.draw_polygon(\n...     points=[\n...         ap.Point2D(x=0, y=0),\n...         ap.Point2D(x=50, y=0),\n...         ap.Point2D(x=25, y=50),\n...     ]\n... )\n>>> polygon.flip_y = ap.Boolean(True)\n>>> polygon.flip_y\nBoolean(True)\n```': '```py\n>>> import apysc as ap\n>>> stage: ap.Stage = ap.Stage()\n>>> sprite: ap.Sprite = ap.Sprite()\n>>> sprite.graphics.begin_fill(color="#0af")\n>>> polygon: ap.Polygon = sprite.graphics.draw_polygon(\n...     points=[\n...         ap.Point2D(x=0, y=0),\n...         ap.Point2D(x=50, y=0),\n...         ap.Point2D(x=25, y=50),\n...     ]\n... )\n>>> polygon.flip_y = ap.Boolean(True)\n>>> polygon.flip_y\nBoolean(True)\n```',  # noqa
}
