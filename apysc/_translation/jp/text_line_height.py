"""This module is for the translation mapping data of the
following document:

Document file: text_line_height.md
Language: jp
"""

from typing import Dict

MAPPING: Dict[str, str] = {
    ##################################################
    "# Text line_height property": "# テキストの line_height 属性",
    ##################################################
    "This page explains the text-related `line_height` property.": "このページではテキスト関係の`line_height`属性について説明します。",  # noqa
    ##################################################
    "## What property is this?": "## 属性の概要",
    ##################################################
    "The `line_height` property updates or gets the instance's line height (leading) setting.": "`line_height`属性ではインスタンスの行間の設定の更新もしくは取得を行うことができます。",  # noqa
    ##################################################
    "## Basic usage": "## 基本的な使い方",
    ##################################################
    "The getter and setter interfaces' type becomes an `ap.Number` value.": "getterとsetterの各インターフェイスの型は`ap.Number`の値になります。",  # noqa
    ##################################################
    "If you specify a value of 1.5 to this property, the line height becomes 1.5 times the font size.": "もしこの属性に1.5を指定した場合、行間はフォントサイズの1.5倍の大きさになります。",  # noqa
    ##################################################
    '```py\n# runnable\nimport apysc as ap\n\nstage: ap.Stage = ap.Stage(\n    background_color=ap.Color("#333"),\n    stage_width=300,\n    stage_height=250,\n    stage_elem_id="stage",\n)\n\nmulti_line_text: ap.MultiLineText = ap.MultiLineText(\n    text="Lorem ipsum dolor sit amet, consectetur adipiscing elit, "\n    "sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. "\n    "Ut enim ad minim veniam",\n    width=250,\n    fill_color=ap.Colors.GRAY_AAAAAA,\n    x=25,\n    y=25,\n)\nmulti_line_text.line_height = ap.Number(2.0)\n\nap.save_overall_html(dest_dir_path="./text_line_height_basic_usage/")\n```': '```py\n# runnable\nimport apysc as ap\n\nstage: ap.Stage = ap.Stage(\n    background_color=ap.Color("#333"),\n    stage_width=300,\n    stage_height=250,\n    stage_elem_id="stage",\n)\n\nmulti_line_text: ap.MultiLineText = ap.MultiLineText(\n    text="Lorem ipsum dolor sit amet, consectetur adipiscing elit, "\n    "sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. "\n    "Ut enim ad minim veniam",\n    width=250,\n    fill_color=ap.Colors.GRAY_AAAAAA,\n    x=25,\n    y=25,\n)\nmulti_line_text.line_height = ap.Number(2.0)\n\nap.save_overall_html(dest_dir_path="./text_line_height_basic_usage/")\n```',  # noqa
    ##################################################
    "## line_height property API": "## line_height 属性のAPI",
    ##################################################
    '<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>': '<span class="inconspicuous-txt">特記事項: このAPIドキュメントはドキュメントビルド用のスクリプトによって自動で生成・同期されています。そのためもしかしたらこの節の内容は前節までの内容と重複している場合があります。</span>',  # noqa
    ##################################################
    "**[Interface summary]**": "**[インターフェイス概要]**",
    ##################################################
    "Get a line-height value.<hr>": "行間の値を取得します。<hr>",
    ##################################################
    "**[Returns]**": "**[返却値]**",
    ##################################################
    "- `line_height`: Number": "- `line_height`: Number",
    ##################################################
    "  - A line-height value.": "  - 行間の値。",
    ##################################################
    "<hr>": "<hr>",
    ##################################################
    "**[Examples]**": "**[コードサンプル]**",
    ##################################################
    '```py\n>>> import apysc as ap\n>>> stage: ap.Stage = ap.Stage(\n...     background_color=ap.Color("#333"),\n...     stage_width=300,\n...     stage_height=250,\n...     stage_elem_id="stage",\n... )\n>>> multi_line_text: ap.MultiLineText = ap.MultiLineText(\n...     text="Lorem ipsum dolor sit amet, consectetur adipiscing elit, "\n...     "sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. "\n...     "Ut enim ad minim veniam",\n...     width=250,\n...     fill_color=ap.Colors.GRAY_AAAAAA,\n...     x=25,\n...     y=25,\n... )\n>>> multi_line_text.line_height = ap.Number(2.0)\n>>> multi_line_text.line_height\nNumber(2.0)\n```': '```py\n>>> import apysc as ap\n>>> stage: ap.Stage = ap.Stage(\n...     background_color=ap.Color("#333"),\n...     stage_width=300,\n...     stage_height=250,\n...     stage_elem_id="stage",\n... )\n>>> multi_line_text: ap.MultiLineText = ap.MultiLineText(\n...     text="Lorem ipsum dolor sit amet, consectetur adipiscing elit, "\n...     "sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. "\n...     "Ut enim ad minim veniam",\n...     width=250,\n...     fill_color=ap.Colors.GRAY_AAAAAA,\n...     x=25,\n...     y=25,\n... )\n>>> multi_line_text.line_height = ap.Number(2.0)\n>>> multi_line_text.line_height\nNumber(2.0)\n```',  # noqa
}
