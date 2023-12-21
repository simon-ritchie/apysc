"""This module is for the translation mapping data of the
following document:

Document file: text_fill_color.md
Language: jp
"""

from typing import Dict

MAPPING: Dict[str, str] = {
    ##################################################
    "# Text fill_color property": "# テキストの fill_color 属性",
    ##################################################
    "This page explains the text-related `fill_color` property.": "このページではテキスト関係の`fill_color`属性について説明します。",  # noqa
    ##################################################
    "## What property is this?": "## 属性の概要",
    ##################################################
    "The `fill_color` property interface updates or gets the instance's fill color.": "`fill_color`属性のインターフェイスでは塗りの色の値を更新したり取得したりすることができます。",  # noqa
    ##################################################
    "## Basic usage": "## 基本的な使い方",
    ##################################################
    "The getter interface becomes a `Color` value, and the setter one also requires a `Color` value.": "getterのインターフェイスは`Color`型の値になります。setterのインターフェイスも`Color`型の値の指定が必要になります。",  # noqa
    ##################################################
    '```py\n# runnable\nimport apysc as ap\n\nstage: ap.Stage = ap.Stage(\n    background_color=ap.Color("#333"),\n    stage_width=300,\n    stage_height=200,\n    stage_elem_id="stage",\n)\n\nmulti_line_text: ap.MultiLineText = ap.MultiLineText(\n    text="Lorem ipsum dolor sit amet, consectetur adipiscing elit, "\n    "sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. "\n    "Ut enim ad minim veniam",\n    width=250,\n    font_size=16,\n    x=25,\n    y=25,\n)\nmulti_line_text.fill_color = ap.Colors.CYAN_00AAFF\nap.assert_equal(multi_line_text.fill_color, ap.Colors.CYAN_00AAFF)\nap.save_overall_html(dest_dir_path="text_fill_color_basic_usage/")\n```': '```py\n# runnable\nimport apysc as ap\n\nstage: ap.Stage = ap.Stage(\n    background_color=ap.Color("#333"),\n    stage_width=300,\n    stage_height=200,\n    stage_elem_id="stage",\n)\n\nmulti_line_text: ap.MultiLineText = ap.MultiLineText(\n    text="Lorem ipsum dolor sit amet, consectetur adipiscing elit, "\n    "sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. "\n    "Ut enim ad minim veniam",\n    width=250,\n    font_size=16,\n    x=25,\n    y=25,\n)\nmulti_line_text.fill_color = ap.Colors.CYAN_00AAFF\nap.assert_equal(multi_line_text.fill_color, ap.Colors.CYAN_00AAFF)\nap.save_overall_html(dest_dir_path="text_fill_color_basic_usage/")\n```',  # noqa
    ##################################################
    "## fill_color property API": "## fill_color 属性のAPI",
    ##################################################
    '<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>': '<span class="inconspicuous-txt">特記事項: このAPIドキュメントはドキュメントビルド用のスクリプトによって自動で生成・同期されています。そのためもしかしたらこの節の内容は前節までの内容と重複している場合があります。</span>',  # noqa
    ##################################################
    "**[Interface summary]**": "**[インターフェイス概要]**",
    ##################################################
    "Get a text's fill color.<hr>": "テキストの塗りの色を取得します。<hr>",
    ##################################################
    "**[Returns]**": "**[返却値]**",
    ##################################################
    "- `color`: Color": "- `color`: Color",
    ##################################################
    "  - A text color.": "  - テキストの色。",
    ##################################################
    "<hr>": "<hr>",
    ##################################################
    "**[Examples]**": "**[コードサンプル]**",
    ##################################################
    '```py\n>>> import apysc as ap\n>>> stage: ap.Stage = ap.Stage(\n...     background_color=ap.Color("#333"),\n...     stage_width=300,\n...     stage_height=100,\n...     stage_elem_id="stage",\n... )\n>>> multi_line_text: ap.MultiLineText = ap.MultiLineText(\n...     text="Lorem ipsum dolor sit amet, consectetur adipiscing elit, "\n...     "sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. "\n...     "Ut enim ad minim veniam",\n...     width=300,\n...     font_size=16,\n...     x=20,\n...     y=20,\n... )\n>>> multi_line_text.fill_color = ap.Colors.CYAN_00AAFF\n>>> assert multi_line_text.fill_color == ap.Colors.CYAN_00AAFF\n```': '```py\n>>> import apysc as ap\n>>> stage: ap.Stage = ap.Stage(\n...     background_color=ap.Color("#333"),\n...     stage_width=300,\n...     stage_height=100,\n...     stage_elem_id="stage",\n... )\n>>> multi_line_text: ap.MultiLineText = ap.MultiLineText(\n...     text="Lorem ipsum dolor sit amet, consectetur adipiscing elit, "\n...     "sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. "\n...     "Ut enim ad minim veniam",\n...     width=300,\n...     font_size=16,\n...     x=20,\n...     y=20,\n... )\n>>> multi_line_text.fill_color = ap.Colors.CYAN_00AAFF\n>>> assert multi_line_text.fill_color == ap.Colors.CYAN_00AAFF\n```',  # noqa
    ##################################################
    "<hr>": "<hr>",
    ##################################################
    "**[References]**": "**[関連資料]**",
    ##################################################
    "- [MultiLineText class](https://simon-ritchie.github.io/apysc/en/multi_line_text.html)": "- [MultiLineText クラス](https://simon-ritchie.github.io/apysc/jp/jp_multi_line_text.html)",  # noqa
}
