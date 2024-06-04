"""This module is for the translation mapping data of the
following document:

Document file: red_color.md
Language: jp
"""

from typing import Dict

MAPPING: Dict[str, str] = {
    ##################################################
    "# Color class red_color property": "# Color クラスの red_color プロパティ",
    ##################################################
    "This page explains the `Color` class `red_color` property.": "このページでは`Color`クラスの`red_color`属性について説明します。",  # noqa
    ##################################################
    "## What property is this?": "## 属性の概要",
    ##################################################
    "The `red_color` property returns or sets a red color `ap.Int` value.": "`red_color`属性は赤色の`ap.Int`型の値の返却もしくは設定を行います。",  # noqa
    ##################################################
    "This value takes the range from 0 to 255.": "この値は0～255の範囲を取ります。",
    ##################################################
    "## Basic usage": "## 基本的な使い方",
    ##################################################
    "The following example shows how to use the `red_color` getter and setter interfaces:": "以下の例は`red_color`属性のgetterとsetterの各インターフェイスの使用例となります:",  # noqa
    ##################################################
    '```py\n# runnable\nimport apysc as ap\n\nstage: ap.Stage = ap.Stage(\n    stage_width=0,\n    stage_height=0,\n    background_color=ap.Color("#333"),\n    stage_elem_id="stage",\n)\n\ncolor: ap.Color = ap.Color("#00aaff")\nred_color: ap.Int = color.red_color\nap.assert_equal(red_color, 0)\n\ncolor = ap.Color("#ff00aa")\nred_color = color.red_color\nap.assert_equal(red_color, 255)\n\ncolor.red_color = ap.Int(0)\nred_color = color.red_color\nap.assert_equal(red_color, 0)\n\ncolor.red_color = ap.Int(255)\nred_color = color.red_color\nap.assert_equal(red_color, 255)\n\nap.save_overall_html(dest_dir_path="./red_color_basic_usage/")\n```': '```py\n# runnable\nimport apysc as ap\n\nstage: ap.Stage = ap.Stage(\n    stage_width=0,\n    stage_height=0,\n    background_color=ap.Color("#333"),\n    stage_elem_id="stage",\n)\n\ncolor: ap.Color = ap.Color("#00aaff")\nred_color: ap.Int = color.red_color\nap.assert_equal(red_color, 0)\n\ncolor = ap.Color("#ff00aa")\nred_color = color.red_color\nap.assert_equal(red_color, 255)\n\ncolor.red_color = ap.Int(0)\nred_color = color.red_color\nap.assert_equal(red_color, 0)\n\ncolor.red_color = ap.Int(255)\nred_color = color.red_color\nap.assert_equal(red_color, 255)\n\nap.save_overall_html(dest_dir_path="./red_color_basic_usage/")\n```',  # noqa
    ##################################################
    "## red_color property API": "## red_color 属性のAPI",
    ##################################################
    '<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>': '<span class="inconspicuous-txt">特記事項: このAPIドキュメントはドキュメントビルド用のスクリプトによって自動で生成・同期されています。そのためもしかしたらこの節の内容は前節までの内容と重複している場合があります。</span>',  # noqa
    ##################################################
    "**[Interface summary]**": "**[インターフェイス概要]**",
    ##################################################
    "Get a red color integer value (0 to 255).<hr>": "赤色の整数値（0～255）を取得します。<hr>",
    ##################################################
    "**[Returns]**": "**[返却値]**",
    ##################################################
    "- `red_color`: Int": "- `red_color`: Int",
    ##################################################
    "  - Red color integer value (0 to 255).": "  - 赤色の整数値（0～255）。",
    ##################################################
    "<hr>": "<hr>",
    ##################################################
    "**[Examples]**": "**[コードサンプル]**",
    ##################################################
    '```py\n>>> import apysc as ap\n>>> color: ap.Color = ap.Color("#00aaff")\n>>> red_color: ap.Int = color.red_color\n>>> red_color\nInt(0)\n\n>>> color = ap.Color("#ff00aa")\n>>> red_color = color.red_color\n>>> red_color\nInt(255)\n\n>>> color.red_color = ap.Int(0)\n>>> red_color = color.red_color\n>>> red_color\nInt(0)\n```': '```py\n>>> import apysc as ap\n>>> color: ap.Color = ap.Color("#00aaff")\n>>> red_color: ap.Int = color.red_color\n>>> red_color\nInt(0)\n\n>>> color = ap.Color("#ff00aa")\n>>> red_color = color.red_color\n>>> red_color\nInt(255)\n\n>>> color.red_color = ap.Int(0)\n>>> red_color = color.red_color\n>>> red_color\nInt(0)\n```',  # noqa
}
