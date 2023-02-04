"""This module is for the translation mapping data of the
following document:

Document file: graphics_base_line_color.md
Language: jp
"""

from typing import Dict

MAPPING: Dict[str, str] = {
    ##################################################
    "# GraphicsBase line_color interface": "# GraphicsBase クラスの line_color インターフェイス",
    ##################################################
    "This page explains the `GraphicsBase` class `line_color` property interface.": "このページでは`GraphicsBase`クラスの`line_color`属性のインターフェイスについて説明します。",  # noqa
    ##################################################
    "## What interface is this?": "## インターフェイス概要",
    ##################################################
    "The `line_color` property interface updates or get the instance's line color.": "`line_color`属性のインターフェイスではインスタンスの線の色の更新や取得を行うことができます。",  # noqa
    ##################################################
    "## Basic usage": "## 基本的な使い方",
    ##################################################
    "The getter or setter interface value becomes (or requires) the `String` hex color code value.": "getterとsetterのインターフェイスで扱う値は`String`型の16進数のカラーコードの文字列となります。",  # noqa
    ##################################################
    "The following example changes the line color (from cyan to magenta and magenta to cyan) when you click the rectangle:": "以下のコード例では四角をクリックした際に線の色をシアンからマゼンタに変更しています:",  # noqa
    ##################################################
    '```py\n# runnable\nimport apysc as ap\n\n\ndef on_click(e: ap.MouseEvent[ap.Rectangle], options: dict) -> None:\n    """\n    The handler that the rectangle calls when clicked.\n\n    Parameters\n    ----------\n    e : MouseEvent\n        Event instance.\n    options : dict\n        Optional arguments dictionary.\n    """\n    rectangle: ap.Rectangle = e.this\n    line_color: ap.String = rectangle.line_color\n    with ap.If(line_color == "#00aaff"):\n        rectangle.line_color = ap.String("#f0a")\n    with ap.Else():\n        rectangle.line_color = ap.String("#0af")\n\n\nap.Stage(\n    stage_width=150, stage_height=150, background_color="#333", stage_elem_id="stage"\n)\nsprite: ap.Sprite = ap.Sprite()\nsprite.graphics.begin_fill(color="#0", alpha=0.0)\nsprite.graphics.line_style(color="#0af", thickness=5)\n\nrectangle: ap.Rectangle = sprite.graphics.draw_rect(x=50, y=50, width=50, height=50)\nrectangle.click(on_click)\n\nap.save_overall_html(dest_dir_path="./graphics_base_line_color_basic_usage/")\n```': '```py\n# runnable\nimport apysc as ap\n\n\ndef on_click(e: ap.MouseEvent[ap.Rectangle], options: dict) -> None:\n    """\n    The handler that the rectangle calls when clicked.\n\n    Parameters\n    ----------\n    e : MouseEvent\n        Event instance.\n    options : dict\n        Optional arguments dictionary.\n    """\n    rectangle: ap.Rectangle = e.this\n    line_color: ap.String = rectangle.line_color\n    with ap.If(line_color == "#00aaff"):\n        rectangle.line_color = ap.String("#f0a")\n    with ap.Else():\n        rectangle.line_color = ap.String("#0af")\n\n\nap.Stage(\n    stage_width=150, stage_height=150, background_color="#333", stage_elem_id="stage"\n)\nsprite: ap.Sprite = ap.Sprite()\nsprite.graphics.begin_fill(color="#0", alpha=0.0)\nsprite.graphics.line_style(color="#0af", thickness=5)\n\nrectangle: ap.Rectangle = sprite.graphics.draw_rect(x=50, y=50, width=50, height=50)\nrectangle.click(on_click)\n\nap.save_overall_html(dest_dir_path="./graphics_base_line_color_basic_usage/")\n```',  # noqa
    ##################################################
    "## line_color property API": "## line_color 属性のAPI",
    ##################################################
    '<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>': '<span class="inconspicuous-txt">特記事項: このAPIドキュメントはドキュメントビルド用のスクリプトによって自動で生成・同期されています。そのためもしかしたらこの節の内容は前節までの内容と重複している場合があります。</span>',  # noqa
    ##################################################
    "**[Interface summary]**": "**[インターフェイス概要]**",
    ##################################################
    "Get this instance's line color.<hr>": "インスタンスの線の色を取得します。<hr>",
    ##################################################
    "**[Returns]**": "**[返却値]**",
    ##################################################
    "- `line_color`: String": "- `line_color`: String",
    ##################################################
    "  - Current line color (hexadecimal string, e.g., '#00aaff'). If not be set, this interface returns a blank string.": "  - '#00aaff'などの16進数の線の色。もし設定されていない場合はこの空文字となります。",  # noqa
    ##################################################
    "<hr>": "<hr>",
    ##################################################
    "**[Examples]**": "**[コードサンプル]**",
    ##################################################
    '```py\n>>> import apysc as ap\n>>> stage: ap.Stage = ap.Stage()\n>>> sprite: ap.Sprite = ap.Sprite()\n>>> sprite.graphics.line_style(color="#fff", thickness=10)\n>>> line: ap.Line = sprite.graphics.draw_line(\n...     x_start=50, y_start=50, x_end=150, y_end=50\n... )\n>>> line.line_color = ap.String("#0af")\n>>> line.line_color\nString(\'#00aaff\')\n```': '```py\n>>> import apysc as ap\n>>> stage: ap.Stage = ap.Stage()\n>>> sprite: ap.Sprite = ap.Sprite()\n>>> sprite.graphics.line_style(color="#fff", thickness=10)\n>>> line: ap.Line = sprite.graphics.draw_line(\n...     x_start=50, y_start=50, x_end=150, y_end=50\n... )\n>>> line.line_color = ap.String("#0af")\n>>> line.line_color\nString(\'#00aaff\')\n```',  # noqa
}
