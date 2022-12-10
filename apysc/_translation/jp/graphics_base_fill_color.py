"""This module is for the translation mapping data of the
following document:

Document file: graphics_base_fill_color.md
Language: jp
"""

from typing import Dict

MAPPING: Dict[str, str] = {
    ##################################################
    "# GraphicsBase fill_color interface": "# GraphicsBase クラスの fill_color インターフェイス",
    ##################################################
    "This page explains the `GraphicsBase` class `fill_color` property interface.": "このページでは`GraphicsBase`クラスの`fill_color`属性のインターフェイスについて説明します。",  # noqa
    ##################################################
    "## What interface is this?": "## インターフェイス概要",
    ##################################################
    "The `fill_color` property interface updates or get the instance's fill color.": "`fill_color`属性のインターフェイスでは塗りの色の値を更新したり取得したりすることができます。",  # noqa
    ##################################################
    "## Basic usage": "## 基本的な使い方",
    ##################################################
    "The getter interface becomes the `String` hex color code value, and the setter one also requires the `String` hex color code value.": "getterのインターフェイスは`String`型の16進数のカラーコードの文字列になります。setterのインターフェイスも`String`型の16進数のカラーコードの指定が必要になります。",  # noqa
    ##################################################
    "The following example changes the fill color (from cyan to magenta and magenta to cyan) when you click the rectangle:": "以下のコード例では四角をクリックした際に塗りの色をシアンからマゼンタに変更するようにしています:",  # noqa
    ##################################################
    '```py\n# runnable\nimport apysc as ap\n\n\ndef on_click(e: ap.MouseEvent[ap.Rectangle], options: dict) -> None:\n    """\n    The handler that the rectangle calls when clicked.\n\n    Parameters\n    ----------\n    e : MouseEvent\n        Event instance.\n    options : dict\n        Optional arguments dictionary.\n    """\n    rectangle: ap.Rectangle = e.this\n    fill_color: ap.String = rectangle.fill_color\n    with ap.If(fill_color == "#00aaff"):\n        rectangle.fill_color = ap.String("#f0a")\n    with ap.Else():\n        rectangle.fill_color = ap.String("#0af")\n\n\nap.Stage(\n    stage_width=150, stage_height=150, background_color="#333", stage_elem_id="stage"\n)\nsprite: ap.Sprite = ap.Sprite()\nsprite.graphics.begin_fill(color="#0af")\nrectangle: ap.Rectangle = sprite.graphics.draw_rect(x=50, y=50, width=50, height=50)\nrectangle.click(on_click)\n\nap.save_overall_html(dest_dir_path="./graphics_base_fill_color_basic_usage/")\n```': '```py\n# runnable\nimport apysc as ap\n\n\ndef on_click(e: ap.MouseEvent[ap.Rectangle], options: dict) -> None:\n    """\n    The handler that the rectangle calls when clicked.\n\n    Parameters\n    ----------\n    e : MouseEvent\n        Event instance.\n    options : dict\n        Optional arguments dictionary.\n    """\n    rectangle: ap.Rectangle = e.this\n    fill_color: ap.String = rectangle.fill_color\n    with ap.If(fill_color == "#00aaff"):\n        rectangle.fill_color = ap.String("#f0a")\n    with ap.Else():\n        rectangle.fill_color = ap.String("#0af")\n\n\nap.Stage(\n    stage_width=150, stage_height=150, background_color="#333", stage_elem_id="stage"\n)\nsprite: ap.Sprite = ap.Sprite()\nsprite.graphics.begin_fill(color="#0af")\nrectangle: ap.Rectangle = sprite.graphics.draw_rect(x=50, y=50, width=50, height=50)\nrectangle.click(on_click)\n\nap.save_overall_html(dest_dir_path="./graphics_base_fill_color_basic_usage/")\n```',  # noqa
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
    "- `fill_color`: String": "- `fill_color`: String",
    ##################################################
    "  - Current fill color (hexadecimal string, e.g., '#00aaff'). If not be set, this interface returns a blank string.": "  - 現在の塗りの色（`'#00aaff'`などの16進数の文字列）。もしも設定されていない場合空文字が返却されます。",  # noqa
    ##################################################
    "<hr>": "<hr>",
    ##################################################
    "**[Examples]**": "**[コードサンプル]**",
    ##################################################
    '```py\n>>> import apysc as ap\n>>> stage: ap.Stage = ap.Stage()\n>>> sprite: ap.Sprite = ap.Sprite()\n>>> sprite.graphics.begin_fill(color="#0af")\n>>> rectangle: ap.Rectangle = sprite.graphics.draw_rect(\n...     x=50, y=50, width=50, height=50\n... )\n>>> rectangle.fill_color = ap.String("#f0a")\n>>> rectangle.fill_color\nString(\'#ff00aa\')\n```': '```py\n>>> import apysc as ap\n>>> stage: ap.Stage = ap.Stage()\n>>> sprite: ap.Sprite = ap.Sprite()\n>>> sprite.graphics.begin_fill(color="#0af")\n>>> rectangle: ap.Rectangle = sprite.graphics.draw_rect(\n...     x=50, y=50, width=50, height=50\n... )\n>>> rectangle.fill_color = ap.String("#f0a")\n>>> rectangle.fill_color\nString(\'#ff00aa\')\n```',  # noqa
}
