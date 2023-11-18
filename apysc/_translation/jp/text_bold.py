"""This module is for the translation mapping data of the
following document:

Document file: text_bold.md
Language: jp
"""

from typing import Dict

MAPPING: Dict[str, str] = {
    ##################################################
    "# Text bold property": "# テキストの bold 属性",
    ##################################################
    "This page explains the text-related `bold` property.": "このページではテキスト関係の`bold`属性について説明します。",  # noqa
    ##################################################
    "## What property is this?": "## 属性の概要",
    ##################################################
    "The `bold` property updates or gets the instance\'s bold setting.": "`bold`属性はインスタンスの太字設定の更新もしくは取得を行います。",  # noqa
    ##################################################
    "## Basic usage": "## 基本的な使い方",
    ##################################################
    "The getter and setter interfaces accept an `ap.Boolean` value.": "getterもしくはsetterの各インターフェイスでは`ap.Boolean`型の値を指定できます。",  # noqa
    ##################################################
    "If you specify the `ap.Boolean(True)` (or `ap.True_`) value, a text instance becomes bold style.": "もし`ap.Boolean(True)`（もしくは`ap.True_`）の値を指定した場合、テキストのインスタンスは太字のスタイルになります。",  # noqa
    ##################################################
    "```py\n# runnable\nimport apysc as ap\n\nstage: ap.Stage = ap.Stage(\n    background_color=ap.Color(\"#333\"),\n    stage_width=350,\n    stage_height=170,\n    stage_elem_id=\"stage\",\n)\nmulti_line_text: ap.MultiLineText = ap.MultiLineText(\n    text=\"Lorem ipsum dolor sit amet, consectetur adipiscing elit, \"\n    \"sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. \"\n    \"Ut enim ad minim veniam\",\n    width=300,\n    font_size=16,\n    fill_color=ap.Color(\"#00aaff\"),\n    x=25,\n    y=25,\n)\nmulti_line_text.bold = ap.True_\n\nap.save_overall_html(dest_dir_path=\"./text_bold_basic_usage/\")\n```": "```py\n# runnable\nimport apysc as ap\n\nstage: ap.Stage = ap.Stage(\n    background_color=ap.Color(\"#333\"),\n    stage_width=350,\n    stage_height=170,\n    stage_elem_id=\"stage\",\n)\nmulti_line_text: ap.MultiLineText = ap.MultiLineText(\n    text=\"Lorem ipsum dolor sit amet, consectetur adipiscing elit, \"\n    \"sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. \"\n    \"Ut enim ad minim veniam\",\n    width=300,\n    font_size=16,\n    fill_color=ap.Color(\"#00aaff\"),\n    x=25,\n    y=25,\n)\nmulti_line_text.bold = ap.True_\n\nap.save_overall_html(dest_dir_path=\"./text_bold_basic_usage/\")\n```",  # noqa
    ##################################################
    "## bold property API": "## bold 属性のAPI",
    ##################################################
    "<span class=\"inconspicuous-txt\">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>": "<span class=\"inconspicuous-txt\">特記事項: このAPIドキュメントはドキュメントビルド用のスクリプトによって自動で生成・同期されています。そのためもしかしたらこの節の内容は前節までの内容と重複している場合があります。</span>",  # noqa
    ##################################################
    "**[Interface summary]**": "**[インターフェイス概要]**",
    ##################################################
    "Get a bold (font-weight) value.<hr>": "太字設定（font-weight）の値を取得します。<hr>",
    ##################################################
    "**[Returns]**": "**[返却値]**",
    ##################################################
    "- `bold`: Boolean": "- `bold`: Boolean",
    ##################################################
    "  - A bold (font-weight) value.": "  - 太字（font-weight）設定の値。",
    ##################################################
    "<hr>": "<hr>",
    ##################################################
    "**[Examples]**": "**[コードサンプル]**",
    ##################################################
    "```py\n>>> import apysc as ap\n>>> stage: ap.Stage = ap.Stage(\n...     background_color=ap.Color(\"#333\"),\n...     stage_width=350,\n...     stage_height=170,\n...     stage_elem_id=\"stage\",\n... )\n>>> multi_line_text: ap.MultiLineText = ap.MultiLineText(\n...     text=\"Lorem ipsum dolor sit amet, consectetur adipiscing elit, \"\n...     \"sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. \"\n...     \"Ut enim ad minim veniam\",\n...     width=300,\n...     font_size=16,\n...     fill_color=ap.Color(\"#00aaff\"),\n...     x=25,\n...     y=25,\n... )\n>>> multi_line_text.bold = ap.True_\n>>> multi_line_text.bold\nBoolean(True)\n```": "```py\n>>> import apysc as ap\n>>> stage: ap.Stage = ap.Stage(\n...     background_color=ap.Color(\"#333\"),\n...     stage_width=350,\n...     stage_height=170,\n...     stage_elem_id=\"stage\",\n... )\n>>> multi_line_text: ap.MultiLineText = ap.MultiLineText(\n...     text=\"Lorem ipsum dolor sit amet, consectetur adipiscing elit, \"\n...     \"sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. \"\n...     \"Ut enim ad minim veniam\",\n...     width=300,\n...     font_size=16,\n...     fill_color=ap.Color(\"#00aaff\"),\n...     x=25,\n...     y=25,\n... )\n>>> multi_line_text.bold = ap.True_\n>>> multi_line_text.bold\nBoolean(True)\n```",  # noqa
}
