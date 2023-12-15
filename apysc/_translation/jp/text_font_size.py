"""This module is for the translation mapping data of the
following document:

Document file: text_font_size.md
Language: jp
"""

from typing import Dict

MAPPING: Dict[str, str] = {
    ##################################################
    "# Text font_size property": "# テキストの font_size 属性",
    ##################################################
    "This page explains the text-related `font_size` property.": "このページではテキスト関係の`font_size`属性について説明します。",  # noqa
    ##################################################
    "## What property is this?": "## 属性の概要",
    ##################################################
    "The `font_size` property updates or gets the instance's font size (text size).": "`font_size`属性ではフォントサイズ（テキストサイズ）の更新もしくは取得を行うことができます。",  # noqa
    ##################################################
    "## Basic usage": "## 基本的な使い方",
    ##################################################
    "The getter and setter interfaces' type becomes an `ap.Int` value.": "getterとsetterの各インターフェイスの値の型は`ap.Int`になります。",  # noqa
    ##################################################
    '```py\n# runnable\nimport apysc as ap\n\nstage: ap.Stage = ap.Stage(\n    background_color=ap.Color("#333"),\n    stage_width=350,\n    stage_height=400,\n    stage_elem_id="stage",\n)\nfont_size_16_text: ap.MultiLineText = ap.MultiLineText(\n    text="Example of font-size = 16. Lorem ipsum dolor sit amet, "\n    "consectetur adipiscing elit, sed do eiusmod tempor incididunt "\n    "ut labore et dolore magna aliqua. Ut enim ad minim veniam.",\n    width=300,\n    fill_color=ap.Color("#00aaff"),\n    x=25,\n    y=25,\n)\nfont_size_16_text.font_size = ap.Int(16)\n\nfont_size_32_text: ap.MultiLineText = ap.MultiLineText(\n    text="Example of font-size = 32. Lorem ipsum dolor sit amet, consectetur.",\n    width=300,\n    fill_color=ap.Color("#00aaff"),\n    x=25,\n    y=190,\n)\nfont_size_32_text.font_size = ap.Int(32)\n\nap.save_overall_html(dest_dir_path="./text_font_size_basic_usage/")\n```': '```py\n# runnable\nimport apysc as ap\n\nstage: ap.Stage = ap.Stage(\n    background_color=ap.Color("#333"),\n    stage_width=350,\n    stage_height=400,\n    stage_elem_id="stage",\n)\nfont_size_16_text: ap.MultiLineText = ap.MultiLineText(\n    text="Example of font-size = 16. Lorem ipsum dolor sit amet, "\n    "consectetur adipiscing elit, sed do eiusmod tempor incididunt "\n    "ut labore et dolore magna aliqua. Ut enim ad minim veniam.",\n    width=300,\n    fill_color=ap.Color("#00aaff"),\n    x=25,\n    y=25,\n)\nfont_size_16_text.font_size = ap.Int(16)\n\nfont_size_32_text: ap.MultiLineText = ap.MultiLineText(\n    text="Example of font-size = 32. Lorem ipsum dolor sit amet, consectetur.",\n    width=300,\n    fill_color=ap.Color("#00aaff"),\n    x=25,\n    y=190,\n)\nfont_size_32_text.font_size = ap.Int(32)\n\nap.save_overall_html(dest_dir_path="./text_font_size_basic_usage/")\n```',  # noqa
    ##################################################
    "## font_size property API": "## font_size 属性のAPI",
    ##################################################
    '<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>': '<span class="inconspicuous-txt">特記事項: このAPIドキュメントはドキュメントビルド用のスクリプトによって自動で生成・同期されています。そのためもしかしたらこの節の内容は前節までの内容と重複している場合があります。</span>',  # noqa
    ##################################################
    "**[Interface summary]**": "**[インターフェイス概要]**",
    ##################################################
    "Get a text's font size.<hr>": "テキストのフォントサイズを取得します。<hr>",
    ##################################################
    "**[Returns]**": "**[返却値]**",
    ##################################################
    "- `font_size`: Int": "- `font_size`: Int",
    ##################################################
    "  - A text font size.": "  - テキストのフォントサイズ。",
    ##################################################
    "<hr>": "<hr>",
    ##################################################
    "**[Examples]**": "**[コードサンプル]**",
    ##################################################
    '```py\n>>> import apysc as ap\n>>> stage: ap.Stage = ap.Stage(\n...     background_color=ap.Color("#333"),\n...     stage_width=350,\n...     stage_height=250,\n...     stage_elem_id="stage",\n... )\n>>> text: ap.MultiLineText = ap.MultiLineText(\n...     text="Example of font-size = 32. Lorem ipsum dolor sit amet, "\n...     "consectetur adipiscing elit, sed do eiusmod tempor incididunt.",\n...     width=300,\n...     fill_color=ap.Color("#00aaff"),\n...     x=25,\n...     y=25,\n... )\n>>> text.font_size = ap.Int(32)\n>>> text.font_size\nInt(32)\n```': '```py\n>>> import apysc as ap\n>>> stage: ap.Stage = ap.Stage(\n...     background_color=ap.Color("#333"),\n...     stage_width=350,\n...     stage_height=250,\n...     stage_elem_id="stage",\n... )\n>>> text: ap.MultiLineText = ap.MultiLineText(\n...     text="Example of font-size = 32. Lorem ipsum dolor sit amet, "\n...     "consectetur adipiscing elit, sed do eiusmod tempor incididunt.",\n...     width=300,\n...     fill_color=ap.Color("#00aaff"),\n...     x=25,\n...     y=25,\n... )\n>>> text.font_size = ap.Int(32)\n>>> text.font_size\nInt(32)\n```',  # noqa
}
