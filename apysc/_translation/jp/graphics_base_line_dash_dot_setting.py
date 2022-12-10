"""This module is for the translation mapping data of the
following document:

Document file: graphics_base_line_dash_dot_setting.md
Language: jp
"""

from typing import Dict

MAPPING: Dict[str, str] = {
    ##################################################
    "# GraphicsBase line_dash_dot_setting interface": "# GraphicsBase クラスの line_dash_dot_setting インターフェイス",  # noqa
    ##################################################
    "This page explains the `GraphicsBase` class `line_dash_dot_setting` property interface.": "このページでは`GraphicsBase`クラスの`line_dash_dot_setting`属性のインターフェイスについて説明します。",  # noqa
    ##################################################
    "## What interface is this?": "## インターフェイス概要",
    ##################################################
    "The `line_dash_dot_setting` property interface updates or get the instance's current line dash-dot setting.": "`line_dash_dot_setting`属性のインターフェイスでは現在の一点鎖線のスタイル設定の更新もしくは取得を行えます。",  # noqa
    ##################################################
    "## Basic usage": "## 基本的な使い方",
    ##################################################
    "The getter or setter interface value becomes (or requires) the `LineDashDotSetting` instance value.": "getterやsetterのインターフェイスの値は`LineDashDotSetting`インスタンスの値となります。",  # noqa
    ##################################################
    "The following example sets the 10-pixel dash and 3-pixel dot to the line:": "以下のコード例では10pxの破線と3pxの点線の一点鎖線を設定しています。",  # noqa
    ##################################################
    '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    stage_width=250, stage_height=100, background_color="#333", stage_elem_id="stage"\n)\nsprite: ap.Sprite = ap.Sprite()\nsprite.graphics.line_style(color="#0af", thickness=5)\n\nline: ap.Line = sprite.graphics.draw_line(x_start=50, y_start=50, x_end=200, y_end=50)\nline.line_dash_dot_setting = ap.LineDashDotSetting(\n    dot_size=10, dash_size=3, space_size=3\n)\n\nap.save_overall_html(dest_dir_path="./graphics_base_line_dash_dot_setting_basic_usage/")\n```': '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    stage_width=250, stage_height=100, background_color="#333", stage_elem_id="stage"\n)\nsprite: ap.Sprite = ap.Sprite()\nsprite.graphics.line_style(color="#0af", thickness=5)\n\nline: ap.Line = sprite.graphics.draw_line(x_start=50, y_start=50, x_end=200, y_end=50)\nline.line_dash_dot_setting = ap.LineDashDotSetting(\n    dot_size=10, dash_size=3, space_size=3\n)\n\nap.save_overall_html(dest_dir_path="./graphics_base_line_dash_dot_setting_basic_usage/")\n```',  # noqa
    ##################################################
    "## line_dash_dot_setting API": "## line_dash_dot_setting API",
    ##################################################
    '<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>': '<span class="inconspicuous-txt">特記事項: このAPIドキュメントはドキュメントビルド用のスクリプトによって自動で生成・同期されています。そのためもしかしたらこの節の内容は前節までの内容と重複している場合があります。</span>',  # noqa
    ##################################################
    "**[Interface summary]**": "**[インターフェイス概要]**",
    ##################################################
    "Get current dash dot (1-dot chain) setting.<hr>": "現在の一点鎖線のスタイル設定を取得します。<hr>",
    ##################################################
    "**[Returns]**": "**[返却値]**",
    ##################################################
    "- `line_dash_dot_setting`: LineDashDotSetting or None": "- `line_dash_dot_setting`: LineDashDotSetting or None",  # noqa
    ##################################################
    "  - Dash dot (1-dot chain) setting.": "  - 一点鎖線の設定。",
    ##################################################
    "<hr>": "<hr>",
    ##################################################
    "**[Examples]**": "**[コードサンプル]**",
    ##################################################
    '```py\n>>> import apysc as ap\n>>> stage: ap.Stage = ap.Stage()\n>>> sprite: ap.Sprite = ap.Sprite()\n>>> sprite.graphics.line_style(color="#fff", thickness=10)\n>>> line: ap.Line = sprite.graphics.draw_line(\n...     x_start=50, y_start=50, x_end=150, y_end=50\n... )\n>>> line.line_dash_dot_setting = ap.LineDashDotSetting(\n...     dot_size=2, dash_size=5, space_size=3\n... )\n>>> line.line_dash_dot_setting.dot_size\nInt(2)\n\n>>> line.line_dash_dot_setting.dash_size\nInt(5)\n\n>>> line.line_dash_dot_setting.space_size\nInt(3)\n```': '```py\n>>> import apysc as ap\n>>> stage: ap.Stage = ap.Stage()\n>>> sprite: ap.Sprite = ap.Sprite()\n>>> sprite.graphics.line_style(color="#fff", thickness=10)\n>>> line: ap.Line = sprite.graphics.draw_line(\n...     x_start=50, y_start=50, x_end=150, y_end=50\n... )\n>>> line.line_dash_dot_setting = ap.LineDashDotSetting(\n...     dot_size=2, dash_size=5, space_size=3\n... )\n>>> line.line_dash_dot_setting.dot_size\nInt(2)\n\n>>> line.line_dash_dot_setting.dash_size\nInt(5)\n\n>>> line.line_dash_dot_setting.space_size\nInt(3)\n```',  # noqa
}
