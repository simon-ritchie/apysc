"""This module is for the translation mapping data of the
following document:

Document file: graphics_base_fill_color.md
Language: jp
"""

from typing import Dict

MAPPING: Dict[str, str] = {
    ##################################################
    "# GraphicsBase fill_color property": "# GraphicsBase クラスの fill_color 属性",
    ##################################################
    "This page explains the `GraphicsBase` class `fill_color` property interface.": "このページでは`GraphicsBase`クラスの`fill_color`属性のインターフェイスについて説明します。",  # noqa
    ##################################################
    "## What interface is this?": "## インターフェイス概要",
    ##################################################
    "The `fill_color` property interface updates or gets the instance's fill color.": "`fill_color`属性のインターフェイスでは塗りの色の値を更新したり取得したりすることができます。",  # noqa
    ##################################################
    "## Basic usage": "## 基本的な使い方",
    ##################################################
    "The getter interface becomes a `Color` value, and the setter one also requires a `Color` value.": "getterのインターフェイスは`Color`型の値になります。setterのインターフェイスも`Color`型の値の指定が必要になります。",  # noqa
    ##################################################
    "The following example changes the fill color (from cyan to magenta and magenta to cyan) when you click the rectangle:": "以下のコード例では四角をクリックした際に塗りの色をシアンからマゼンタに変更するようにしています:",  # noqa
    ##################################################
    '```py\n# runnable\nimport apysc as ap\n\n\ndef on_click(e: ap.MouseEvent[ap.Rectangle], options: dict) -> None:\n    """\n    The handler that the rectangle calls when clicked.\n\n    Parameters\n    ----------\n    e : MouseEvent\n        Event instance.\n    options : dict\n        Optional arguments dictionary.\n    """\n    rectangle: ap.Rectangle = e.this\n    fill_color: ap.Color = rectangle.fill_color\n    with ap.If(fill_color == ap.Color("#00aaff")):\n        rectangle.fill_color = ap.Color("#f0a")\n    with ap.Else():\n        rectangle.fill_color = ap.Color("#0af")\n\n\nap.Stage(\n    stage_width=150,\n    stage_height=150,\n    background_color=ap.Color("#333"),\n    stage_elem_id="stage",\n)\nsprite: ap.Sprite = ap.Sprite()\nsprite.graphics.begin_fill(color=ap.Color("#0af"))\nrectangle: ap.Rectangle = sprite.graphics.draw_rect(x=50, y=50, width=50, height=50)\nrectangle.click(on_click)\n\nap.save_overall_html(dest_dir_path="./graphics_base_fill_color_basic_usage/")\n```': '```py\n# runnable\nimport apysc as ap\n\n\ndef on_click(e: ap.MouseEvent[ap.Rectangle], options: dict) -> None:\n    """\n    The handler that the rectangle calls when clicked.\n\n    Parameters\n    ----------\n    e : MouseEvent\n        Event instance.\n    options : dict\n        Optional arguments dictionary.\n    """\n    rectangle: ap.Rectangle = e.this\n    fill_color: ap.Color = rectangle.fill_color\n    with ap.If(fill_color == ap.Color("#00aaff")):\n        rectangle.fill_color = ap.Color("#f0a")\n    with ap.Else():\n        rectangle.fill_color = ap.Color("#0af")\n\n\nap.Stage(\n    stage_width=150,\n    stage_height=150,\n    background_color=ap.Color("#333"),\n    stage_elem_id="stage",\n)\nsprite: ap.Sprite = ap.Sprite()\nsprite.graphics.begin_fill(color=ap.Color("#0af"))\nrectangle: ap.Rectangle = sprite.graphics.draw_rect(x=50, y=50, width=50, height=50)\nrectangle.click(on_click)\n\nap.save_overall_html(dest_dir_path="./graphics_base_fill_color_basic_usage/")\n```',  # noqa
    ##################################################
    "## fill_color property API": "## fill_color 属性のAPI",
    ##################################################
    '<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>': '<span class="inconspicuous-txt">特記事項: このAPIドキュメントはドキュメントビルド用のスクリプトによって自動で生成・同期されています。そのためもしかしたらこの節の内容は前節までの内容と重複している場合があります。</span>',  # noqa
    ##################################################
    "**[Interface summary]**": "**[インターフェイス概要]**",
    ##################################################
    "Get this instance's fill color.<hr>": "インスタンスの塗りの色を取得します。<hr>",
    ##################################################
    "**[Returns]**": "**[返却値]**",
    ##################################################
    "- `fill_color`: Color": "- `fill_color`: Color",
    ##################################################
    "  - Current fill color. If it is not set, it returns the `COLORLESS` constant.": "  - 現在の塗りの色（`'#00aaff'`などの16進数の文字列の色）。もしも設定されていない場合`COLORLESS`定数の値が返却されます。",  # noqa
    ##################################################
    "<hr>": "<hr>",
    ##################################################
    "**[Examples]**": "**[コードサンプル]**",
    ##################################################
    '```py\n>>> import apysc as ap\n>>> _ = ap.Stage(\n...     stage_width=150,\n...     stage_height=150,\n...     background_color=ap.Color("#333"),\n...     stage_elem_id="stage",\n... )\n>>> circle: ap.Circle = ap.Circle(\n...     x=75,\n...     y=75,\n...     radius=50,\n...     fill_color=ap.Color("#0af"),\n... )\n>>> circle.fill_color\nColor("#00aaff")\n\n>>> circle.fill_color = ap.Color("#ff00aa")\n>>> circle.fill_color\nColor("#ff00aa")\n```': '```py\n>>> import apysc as ap\n>>> _ = ap.Stage(\n...     stage_width=150,\n...     stage_height=150,\n...     background_color=ap.Color("#333"),\n...     stage_elem_id="stage",\n... )\n>>> circle: ap.Circle = ap.Circle(\n...     x=75,\n...     y=75,\n...     radius=50,\n...     fill_color=ap.Color("#0af"),\n... )\n>>> circle.fill_color\nColor("#00aaff")\n\n>>> circle.fill_color = ap.Color("#ff00aa")\n>>> circle.fill_color\nColor("#ff00aa")\n```',  # noqa
}
