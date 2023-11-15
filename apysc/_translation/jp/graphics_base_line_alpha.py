"""This module is for the translation mapping data of the
following document:

Document file: graphics_base_line_alpha.md
Language: jp
"""

from typing import Dict

MAPPING: Dict[str, str] = {
    ##################################################
    "# GraphicsBase line_alpha interface": "# GraphicsBase クラスの line_alpha インターフェイス",
    ##################################################
    "This page explains the `GraphicsBase` class `line_alpha` property interface.": "このページでは`GraphicsBase`クラスの`line_alpha`属性のインターフェイスについて説明します。",  # noqa
    ##################################################
    "## What interface is this?": "## インターフェイス概要",
    ##################################################
    "The `line_alpha` property interface updates or gets the instance's line alpha (opacity).": "`line_alpha`属性のインターフェイスではインスタンスの線の透明度の更新や取得を行うことができます。",  # noqa
    ##################################################
    "## Basic usage": "## 基本的な使い方",
    ##################################################
    "The getter or setter interface value becomes (or requires) the `Number` value (0.0 to 1.0).": "getterとsetterの両方のインターフェイスの値は`Number`型の0.0～1.0の範囲の値となります。",  # noqa
    ##################################################
    "The following example sets the 0.5 line alpha to the second rectangle and 0.25 to the third rectangle:": "以下のコード例では0.5の線の透明度を2番目の四角に設定し、0.25の線の透明度を3番目の四角に設定しています:",  # noqa
    ##################################################
    '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    stage_width=350,\n    stage_height=150,\n    background_color=ap.Color("#333"),\n    stage_elem_id="stage",\n)\nsprite: ap.Sprite = ap.Sprite()\nsprite.graphics.line_style(color=ap.Color("#0af"), thickness=5)\n\nrectangle_1: ap.Rectangle = sprite.graphics.draw_rect(x=50, y=50, width=50, height=50)\n\nrectangle_2: ap.Rectangle = sprite.graphics.draw_rect(x=150, y=50, width=50, height=50)\nrectangle_2.line_alpha = ap.Number(0.5)\n\nrectangle_3: ap.Rectangle = sprite.graphics.draw_rect(x=250, y=50, width=50, height=50)\nrectangle_3.line_alpha = ap.Number(0.25)\n\nap.save_overall_html(dest_dir_path="./graphics_base_line_alpha_basic_usage/")\n```': '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    stage_width=350,\n    stage_height=150,\n    background_color=ap.Color("#333"),\n    stage_elem_id="stage",\n)\nsprite: ap.Sprite = ap.Sprite()\nsprite.graphics.line_style(color=ap.Color("#0af"), thickness=5)\n\nrectangle_1: ap.Rectangle = sprite.graphics.draw_rect(x=50, y=50, width=50, height=50)\n\nrectangle_2: ap.Rectangle = sprite.graphics.draw_rect(x=150, y=50, width=50, height=50)\nrectangle_2.line_alpha = ap.Number(0.5)\n\nrectangle_3: ap.Rectangle = sprite.graphics.draw_rect(x=250, y=50, width=50, height=50)\nrectangle_3.line_alpha = ap.Number(0.25)\n\nap.save_overall_html(dest_dir_path="./graphics_base_line_alpha_basic_usage/")\n```',  # noqa
    ##################################################
    "## line_alpha property API": "## line_alpha 属性のAPI",
    ##################################################
    '<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>': '<span class="inconspicuous-txt">特記事項: このAPIドキュメントはドキュメントビルド用のスクリプトによって自動で生成・同期されています。そのためもしかしたらこの節の内容は前節までの内容と重複している場合があります。</span>',  # noqa
    ##################################################
    "**[Interface summary]**": "**[インターフェイス概要]**",
    ##################################################
    "Get this instance's line alpha (opacity).<hr>": "インスタンスの線の透明度を取得します。<hr>",
    ##################################################
    "**[Returns]**": "**[返却値]**",
    ##################################################
    "- `line_alpha`: Number": "- `line_alpha`: Number",
    ##################################################
    "  - Current line alpha (opacity. 0.0 to 1.0).": "  - 現在の線の透明度（0.0～1.0）。",
    ##################################################
    "<hr>": "<hr>",
    ##################################################
    "**[Examples]**": "**[コードサンプル]**",
    ##################################################
    '```py\n>>> import apysc as ap\n>>> stage: ap.Stage = ap.Stage()\n>>> sprite: ap.Sprite = ap.Sprite()\n>>> sprite.graphics.line_style(color=ap.Color("#fff"), thickness=5, alpha=1.0)\n>>> rectangle: ap.Rectangle = sprite.graphics.draw_rect(\n...     x=50, y=50, width=50, height=50\n... )\n>>> rectangle.line_alpha = ap.Number(0.5)\n>>> rectangle.line_alpha\nNumber(0.5)\n```': '```py\n>>> import apysc as ap\n>>> stage: ap.Stage = ap.Stage()\n>>> sprite: ap.Sprite = ap.Sprite()\n>>> sprite.graphics.line_style(color=ap.Color("#fff"), thickness=5, alpha=1.0)\n>>> rectangle: ap.Rectangle = sprite.graphics.draw_rect(\n...     x=50, y=50, width=50, height=50\n... )\n>>> rectangle.line_alpha = ap.Number(0.5)\n>>> rectangle.line_alpha\nNumber(0.5)\n```',  # noqa
}
