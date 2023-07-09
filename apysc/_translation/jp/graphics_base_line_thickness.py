"""This module is for the translation mapping data of the
following document:

Document file: graphics_base_line_thickness.md
Language: jp
"""

from typing import Dict

MAPPING: Dict[str, str] = {
    ##################################################
    "# GraphicsBase line_thickness interface": "# GraphicsBase クラスの line_thickness インターフェイス",  # noqa
    ##################################################
    "This page explains the `GraphicsBase` class `line_thickness` property interface.": "このページでは`GraphicsBase`クラスの`line_thickness`属性のインターフェイスについて説明します。",  # noqa
    ##################################################
    "## What interface is this?": "## インターフェイス概要",
    ##################################################
    "The `line_thickness` property interface updates or get the instance's line thickness (line width).": "`line_thickness`属性のインターフェイスではインスタンスの線幅の値の更新や取得が行えます。",  # noqa
    ##################################################
    "## Basic usage": "## 基本的な使い方",
    ##################################################
    "The getter or setter interface value becomes (or requires) the `Int` value.": "getterもしくはsetterの各インターフェイスの値は`Int`型の値になります。",  # noqa
    ##################################################
    "The following example sets the 5-pixel line thickness to the first rectangle and the 10-pixel line thickness to the second one:": "以下のコード例では1つ目の四角に5pxの線幅を設定しており、2つ目の四角には10pxの線幅を設定しています:",  # noqa
    ##################################################
    '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    stage_width=250, stage_height=150, background_color="#333", stage_elem_id="stage"\n)\nsprite: ap.Sprite = ap.Sprite()\nsprite.graphics.line_style(color="#0af", thickness=1)\n\nrectangle_1: ap.Rectangle = sprite.graphics.draw_rect(x=50, y=50, width=50, height=50)\nrectangle_1.line_thickness = ap.Int(5)\n\nrectangle_2: ap.Rectangle = sprite.graphics.draw_rect(x=150, y=50, width=50, height=50)\nrectangle_2.line_thickness = ap.Int(10)\n\nap.save_overall_html(dest_dir_path="./graphics_base_line_thickness_basic_usage/")\n```': '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    stage_width=250, stage_height=150, background_color="#333", stage_elem_id="stage"\n)\nsprite: ap.Sprite = ap.Sprite()\nsprite.graphics.line_style(color="#0af", thickness=1)\n\nrectangle_1: ap.Rectangle = sprite.graphics.draw_rect(x=50, y=50, width=50, height=50)\nrectangle_1.line_thickness = ap.Int(5)\n\nrectangle_2: ap.Rectangle = sprite.graphics.draw_rect(x=150, y=50, width=50, height=50)\nrectangle_2.line_thickness = ap.Int(10)\n\nap.save_overall_html(dest_dir_path="./graphics_base_line_thickness_basic_usage/")\n```',  # noqa
    ##################################################
    "## line_thickness property API": "## line_thickness 属性のAPI",
    ##################################################
    '<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>': '<span class="inconspicuous-txt">特記事項: このAPIドキュメントはドキュメントビルド用のスクリプトによって自動で生成・同期されています。そのためもしかしたらこの節の内容は前節までの内容と重複している場合があります。</span>',  # noqa
    ##################################################
    "**[Interface summary]**": "**[インターフェイス概要]**",
    ##################################################
    "Get this instance's line thickness.<hr>": "このインスタンスの線幅を取得します。<hr>",
    ##################################################
    "**[Returns]**": "**[返却値]**",
    ##################################################
    "- `line_thickness`: Int": "- `line_thickness`: Int",
    ##################################################
    "  - Current line thickness.": "  - 現在の線幅。",
    ##################################################
    "<hr>": "<hr>",
    ##################################################
    "**[Examples]**": "**[コードサンプル]**",
    ##################################################
    '```py\n>>> import apysc as ap\n>>> stage: ap.Stage = ap.Stage()\n>>> sprite: ap.Sprite = ap.Sprite()\n>>> sprite.graphics.line_style(color="#fff", thickness=5)\n>>> line: ap.Line = sprite.graphics.draw_line(\n...     x_start=50, y_start=50, x_end=150, y_end=50\n... )\n>>> line.line_thickness\nInt(5)\n```': '```py\n>>> import apysc as ap\n>>> stage: ap.Stage = ap.Stage()\n>>> sprite: ap.Sprite = ap.Sprite()\n>>> sprite.graphics.line_style(color="#fff", thickness=5)\n>>> line: ap.Line = sprite.graphics.draw_line(\n...     x_start=50, y_start=50, x_end=150, y_end=50\n... )\n>>> line.line_thickness\nInt(5)\n```',  # noqa
}
