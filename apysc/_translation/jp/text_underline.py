"""This module is for the translation mapping data of the
following document:

Document file: text_underline.md
Language: jp
"""

from typing import Dict

MAPPING: Dict[str, str] = {
    ##################################################
    "# Text underline property": "# テキストの underline 属性",
    ##################################################
    "This page explains the text-related `underline` property.": "このページではテキスト関係の`underline`属性について説明します。",  # noqa
    ##################################################
    "## What property is this?": "## 属性の概要",
    ##################################################
    "The `underline` property sets or gets the text's underline style setting.": "`underline`属性はテキストの下線のスタイル設定の更新もしくは取得を行います。",  # noqa
    ##################################################
    "## Basic usage": "## 基本的な使い方",
    ##################################################
    "The getter and setter interfaces' type becomes an `ap.Boolean` value.": "getterもしくはsetterの各インターフェイスの値は`ap.Boolean`の型となります。",  # noqa
    ##################################################
    "If you specify the `ap.Boolean(True)` (or `ap.True_`) value, a text displays an underline.": "もし`ap.Boolean(True)`（もしくは`ap.True_`）の値を指定した場合、テキストは下線を表示します。",  # noqa
    ##################################################
    '```py\n# runnable\nimport apysc as ap\n\nstage: ap.Stage = ap.Stage(\n    background_color=ap.Color("#333"),\n    stage_width=300,\n    stage_height=195,\n    stage_elem_id="stage",\n)\n\nmulti_line_text: ap.MultiLineText = ap.MultiLineText(\n    text="Lorem ipsum dolor sit amet, consectetur adipiscing elit, "\n    "sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. "\n    "Ut enim ad minim veniam",\n    width=250,\n    fill_color=ap.Colors.GRAY_AAAAAA,\n    x=25,\n    y=25,\n)\nmulti_line_text.underline = ap.True_\n\nap.save_overall_html(dest_dir_path="./text_underline_basic_usage/")\n```': '```py\n# runnable\nimport apysc as ap\n\nstage: ap.Stage = ap.Stage(\n    background_color=ap.Color("#333"),\n    stage_width=300,\n    stage_height=195,\n    stage_elem_id="stage",\n)\n\nmulti_line_text: ap.MultiLineText = ap.MultiLineText(\n    text="Lorem ipsum dolor sit amet, consectetur adipiscing elit, "\n    "sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. "\n    "Ut enim ad minim veniam",\n    width=250,\n    fill_color=ap.Colors.GRAY_AAAAAA,\n    x=25,\n    y=25,\n)\nmulti_line_text.underline = ap.True_\n\nap.save_overall_html(dest_dir_path="./text_underline_basic_usage/")\n```',  # noqa
    ##################################################
    "## underline property API": "## underline 属性のAPI",
    ##################################################
    '<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>': '<span class="inconspicuous-txt">特記事項: このAPIドキュメントはドキュメントビルド用のスクリプトによって自動で生成・同期されています。そのためもしかしたらこの節の内容は前節までの内容と重複している場合があります。</span>',  # noqa
    ##################################################
    "**[Interface summary]**": "**[インターフェイス概要]**",
    ##################################################
    "Get a text underline (`text-decoration: underline`) setting.<hr>": "テキストの下線（`text-decoration: underline`）設定を取得します。<hr>",  # noqa
    ##################################################
    "**[Returns]**": "**[返却値]**",
    ##################################################
    "- `underline`: Boolean": "- `underline`: Boolean",
    ##################################################
    "  - A text underline setting.": "  - テキストの下線の設定。",
    ##################################################
    "<hr>": "<hr>",
    ##################################################
    "**[Examples]**": "**[コードサンプル]**",
    ##################################################
    '```py\n>>> import apysc as ap\n>>> stage: ap.Stage = ap.Stage(\n...     background_color=ap.Color("#333"),\n...     stage_width=300,\n...     stage_height=195,\n...     stage_elem_id="stage",\n... )\n>>> multi_line_text: ap.MultiLineText = ap.MultiLineText(\n...     text="Lorem ipsum dolor sit amet, consectetur adipiscing elit, "\n...     "sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. "\n...     "Ut enim ad minim veniam",\n...     width=250,\n...     fill_color=ap.Colors.GRAY_AAAAAA,\n...     x=25,\n...     y=25,\n... )\n>>> multi_line_text.underline = ap.True_\n>>> multi_line_text.underline\nBoolean(True)\n```': '```py\n>>> import apysc as ap\n>>> stage: ap.Stage = ap.Stage(\n...     background_color=ap.Color("#333"),\n...     stage_width=300,\n...     stage_height=195,\n...     stage_elem_id="stage",\n... )\n>>> multi_line_text: ap.MultiLineText = ap.MultiLineText(\n...     text="Lorem ipsum dolor sit amet, consectetur adipiscing elit, "\n...     "sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. "\n...     "Ut enim ad minim veniam",\n...     width=250,\n...     fill_color=ap.Colors.GRAY_AAAAAA,\n...     x=25,\n...     y=25,\n... )\n>>> multi_line_text.underline = ap.True_\n>>> multi_line_text.underline\nBoolean(True)\n```',  # noqa
}
