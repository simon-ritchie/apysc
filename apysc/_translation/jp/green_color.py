"""This module is for the translation mapping data of the
following document:

Document file: green_color.md
Language: jp
"""

from typing import Dict

MAPPING: Dict[str, str] = {
    ##################################################
    "# Color class green_color property": "# Color クラスの green_color プロパティ",
    ##################################################
    "This page explains the `Color` class `green_color` property.": "このページでは`Color`クラスの`green_color`プロパティについて説明します。",  # noqa
    ##################################################
    "## What property is this?": "## 属性の概要",
    ##################################################
    "The `green_color` property returns or sets a green color `ap.Int` value.": "`green_color`プロパティは緑色の色の`ap.Int`型の値の返却もしくは設定を行います。",  # noqa
    ##################################################
    "This value takes the range from 0 to 255.": "この値は0～255の範囲を取ります。",
    ##################################################
    "## Basic usage": "## 基本的な使い方",
    ##################################################
    "The following example shows how to use the `green_color` getter and setter interfaces:": "以下のコードでは`green_color`のgetterとsetterの各インターフェイスの例を示します:",  # noqa
    ##################################################
    '```py\n# runnable\nimport apysc as ap\n\nstage: ap.Stage = ap.Stage(\n    stage_width=0,\n    stage_height=0,\n    background_color=ap.Color("#333"),\n    stage_elem_id="stage",\n)\n\ncolor: ap.Color = ap.Color("#aa00ff")\ngreen_color: ap.Int = color.green_color\nap.assert_equal(green_color, 0)\n\ncolor = ap.Color("#00ffaa")\ngreen_color = color.green_color\nap.assert_equal(green_color, 255)\n\ncolor.green_color = ap.Int(0)\ngreen_color = color.green_color\nap.assert_equal(green_color, 0)\n\ncolor.green_color = ap.Int(255)\ngreen_color = color.green_color\nap.assert_equal(green_color, 255)\n\nap.save_overall_html(dest_dir_path="./green_color_basic_usage/")\n```': '```py\n# runnable\nimport apysc as ap\n\nstage: ap.Stage = ap.Stage(\n    stage_width=0,\n    stage_height=0,\n    background_color=ap.Color("#333"),\n    stage_elem_id="stage",\n)\n\ncolor: ap.Color = ap.Color("#aa00ff")\ngreen_color: ap.Int = color.green_color\nap.assert_equal(green_color, 0)\n\ncolor = ap.Color("#00ffaa")\ngreen_color = color.green_color\nap.assert_equal(green_color, 255)\n\ncolor.green_color = ap.Int(0)\ngreen_color = color.green_color\nap.assert_equal(green_color, 0)\n\ncolor.green_color = ap.Int(255)\ngreen_color = color.green_color\nap.assert_equal(green_color, 255)\n\nap.save_overall_html(dest_dir_path="./green_color_basic_usage/")\n```',  # noqa
    ##################################################
    "## green_color property API": "## green_color 属性のAPI",
    ##################################################
    '<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>': '<span class="inconspicuous-txt">特記事項: このAPIドキュメントはドキュメントビルド用のスクリプトによって自動で生成・同期されています。そのためもしかしたらこの節の内容は前節までの内容と重複している場合があります。</span>',  # noqa
    ##################################################
    "**[Interface summary]**": "**[インターフェイス概要]**",
    ##################################################
    "Get a green color integer value (0 to 255).<hr>": "緑色の整数値（0～255）を取得します。<hr>",
    ##################################################
    "**[Returns]**": "**[返却値]**",
    ##################################################
    "- `green_color`: Int": "- `green_color`: Int",
    ##################################################
    "  - Green color integer value (0 to 255).": "  - 緑色の整数値（0～255）。",
    ##################################################
    "<hr>": "<hr>",
    ##################################################
    "**[Examples]**": "**[コードサンプル]**",
    ##################################################
    '```py\n>>> import apysc as ap\n>>> _ = ap.Stage(\n...     background_color=ap.Color("#333"),\n...     stage_elem_id="stage",\n... )\n>>> color: ap.Color = ap.Color("#aa00ff")\n>>> green_color: ap.Int = color.green_color\n>>> green_color\nInt(0)\n\n>>> color = ap.Color("#00ffaa")\n>>> green_color = color.green_color\n>>> green_color\nInt(255)\n\n>>> color.green_color = ap.Int(0)\n>>> green_color = color.green_color\n>>> green_color\nInt(0)\n\n>>> color.green_color = ap.Int(255)\n>>> green_color = color.green_color\n>>> green_color\nInt(255)\n```': '```py\n>>> import apysc as ap\n>>> _ = ap.Stage(\n...     background_color=ap.Color("#333"),\n...     stage_elem_id="stage",\n... )\n>>> color: ap.Color = ap.Color("#aa00ff")\n>>> green_color: ap.Int = color.green_color\n>>> green_color\nInt(0)\n\n>>> color = ap.Color("#00ffaa")\n>>> green_color = color.green_color\n>>> green_color\nInt(255)\n\n>>> color.green_color = ap.Int(0)\n>>> green_color = color.green_color\n>>> green_color\nInt(0)\n\n>>> color.green_color = ap.Int(255)\n>>> green_color = color.green_color\n>>> green_color\nInt(255)\n```',  # noqa
}
