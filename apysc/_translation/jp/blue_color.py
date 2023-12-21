"""This module is for the translation mapping data of the
following document:

Document file: blue_color.md
Language: jp
"""

from typing import Dict

MAPPING: Dict[str, str] = {
    ##################################################
    "# Color class blue_color property": "# Color クラスの blue_color プロパティ",
    ##################################################
    "This page explains the `Color` class `blue_color` property.": "このページでは`Color`クラスの`blue_color`属性について説明します。",  # noqa
    ##################################################
    "## What property is this?": "## 属性の概要",
    ##################################################
    "The `blue_color` property returns or sets a blue color `ap.Int` value.": "`blue_color`属性は青色の`ap.Int`型の値の返却もしくは設定を行います。",  # noqa
    ##################################################
    "This value takes the range from 0 to 255.": "この値は0～255の範囲を取ります。",
    ##################################################
    "## Basic usage": "## 基本的な使い方",
    ##################################################
    "The following example shows how to use the `blue_color` getter and setter interface:": "以下の例では`blue_color`のgetterとsetterの各インターフェイスの使い方を示します:",  # noqa
    ##################################################
    '```py\n# runnable\nimport apysc as ap\n\nstage: ap.Stage = ap.Stage(\n    stage_width=0,\n    stage_height=0,\n    background_color=ap.Color("#333"),\n    stage_elem_id="stage",\n)\n\ncolor: ap.Color = ap.Color("#ffaa00")\nblue_color: ap.Int = color.blue_color\nap.assert_equal(blue_color, 0)\n\ncolor = ap.Color("#00aaff")\nblue_color = color.blue_color\nap.assert_equal(blue_color, 255)\n\ncolor.blue_color = ap.Int(0)\nblue_color = color.blue_color\nap.assert_equal(blue_color, 0)\n\ncolor.blue_color = ap.Int(255)\nblue_color = color.blue_color\nap.assert_equal(blue_color, 255)\n\nap.save_overall_html(dest_dir_path="./blue_color_basic_usage/")\n```': '```py\n# runnable\nimport apysc as ap\n\nstage: ap.Stage = ap.Stage(\n    stage_width=0,\n    stage_height=0,\n    background_color=ap.Color("#333"),\n    stage_elem_id="stage",\n)\n\ncolor: ap.Color = ap.Color("#ffaa00")\nblue_color: ap.Int = color.blue_color\nap.assert_equal(blue_color, 0)\n\ncolor = ap.Color("#00aaff")\nblue_color = color.blue_color\nap.assert_equal(blue_color, 255)\n\ncolor.blue_color = ap.Int(0)\nblue_color = color.blue_color\nap.assert_equal(blue_color, 0)\n\ncolor.blue_color = ap.Int(255)\nblue_color = color.blue_color\nap.assert_equal(blue_color, 255)\n\nap.save_overall_html(dest_dir_path="./blue_color_basic_usage/")\n```',  # noqa
    ##################################################
    "## blue_color property API": "## blue_color 属性のAPI",
    ##################################################
    '<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>': '<span class="inconspicuous-txt">特記事項: このAPIドキュメントはドキュメントビルド用のスクリプトによって自動で生成・同期されています。そのためもしかしたらこの節の内容は前節までの内容と重複している場合があります。</span>',  # noqa
    ##################################################
    "**[Interface summary]**": "**[インターフェイス概要]**",
    ##################################################
    "Get a blue color integer value (0 to 255).<hr>": "青色の整数の値（0～255）を取得します。<hr>",
    ##################################################
    "**[Returns]**": "**[返却値]**",
    ##################################################
    "- `blue_color`: Int": "- `blue_color`: Int",
    ##################################################
    "  - Blue color integer value (0 to 255).": "  - 青色の整数値（0～255）。",
    ##################################################
    "<hr>": "<hr>",
    ##################################################
    "**[Examples]**": "**[コードサンプル]**",
    ##################################################
    '```py\n>>> import apysc as ap\n>>> stage: ap.Stage = ap.Stage(\n...     background_color=ap.Color("#333"),\n...     stage_elem_id="stage",\n... )\n>>> color: ap.Color = ap.Color("#aaff00")\n>>> blue_color: ap.Int = color.blue_color\n>>> blue_color\nInt(0)\n\n>>> color = ap.Color("#00aaff")\n>>> blue_color = color.blue_color\n>>> blue_color\nInt(255)\n\n>>> color.blue_color = ap.Int(0)\n>>> blue_color = color.blue_color\n>>> blue_color\nInt(0)\n\n>>> color.blue_color = ap.Int(255)\n>>> blue_color = color.blue_color\n>>> blue_color\nInt(255)\n```': '```py\n>>> import apysc as ap\n>>> stage: ap.Stage = ap.Stage(\n...     background_color=ap.Color("#333"),\n...     stage_elem_id="stage",\n... )\n>>> color: ap.Color = ap.Color("#aaff00")\n>>> blue_color: ap.Int = color.blue_color\n>>> blue_color\nInt(0)\n\n>>> color = ap.Color("#00aaff")\n>>> blue_color = color.blue_color\n>>> blue_color\nInt(255)\n\n>>> color.blue_color = ap.Int(0)\n>>> blue_color = color.blue_color\n>>> blue_color\nInt(0)\n\n>>> color.blue_color = ap.Int(255)\n>>> blue_color = color.blue_color\n>>> blue_color\nInt(255)\n```',  # noqa
}
