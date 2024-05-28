"""This module is for the translation mapping data of the
following document:

Document file: text_align.md
Language: jp
"""

from typing import Dict

MAPPING: Dict[str, str] = {
    ##################################################
    "# text_align property": "# text_align 属性",
    ##################################################
    "This page explains the text-related `text_align` property.": "このページではテキスト関係の`text_align`属性について説明します。",  # noqa
    ##################################################
    "## What property is this?": "## 属性の概要",
    ##################################################
    "The `text_align` property updates or gets the instance's text alignment setting.": "`text_align`属性ではインスタンスのテキストの行揃えの設定値の更新もしくは取得を行うことができます。",  # noqa
    ##################################################
    "## Basic usage": "## 基本的な使い方",
    ##################################################
    "The getter and setter interfaces' type becomes a `CssTextAlign` enum value.": "getterとsetterの各インターフェイスの値は`CssTextAlign`の型のenumの値となります。",  # noqa
    ##################################################
    "The acceptable enum values are as follows:": "設定できるenumの値は以下の通りです:",
    ##################################################
    "- `CssTextAlign.LEFT` (default)": "- `CssTextAlign.LEFT`（デフォルト）",
    ##################################################
    "- `CssTextAlign.CENTER`": "- `CssTextAlign.CENTER`",
    ##################################################
    "- `CssTextAlign.RIGHT`": "- `CssTextAlign.RIGHT`",
    ##################################################
    "- `CssTextAlign.JUSTIFY`": "- `CssTextAlign.JUSTIFY",
    ##################################################
    "## Example of CssTextAlign.LEFT": "## CssTextAlign.LEFTの例",
    ##################################################
    "Notes: This setting is a default setting.": "特記事項 : この設定はデフォルトの設定です。",
    ##################################################
    '```py\n# runnable\nimport apysc as ap\n\nstage: ap.Stage = ap.Stage(\n    background_color=ap.Color("#333"),\n    stage_width=350,\n    stage_height=170,\n    stage_elem_id="stage",\n)\nmulti_line_text: ap.MultiLineText = ap.MultiLineText(\n    text="Lorem ipsum dolor sit amet, consectetur adipiscing elit, "\n    "sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. "\n    "Ut enim ad minim veniam",\n    width=300,\n    font_size=16,\n    fill_color=ap.Color("#00aaff"),\n    x=25,\n    y=25,\n)\nmulti_line_text.text_align = ap.CssTextAlign.LEFT\n\nap.save_overall_html(dest_dir_path="./css_text_align_left/")\n```': '```py\n# runnable\nimport apysc as ap\n\nstage: ap.Stage = ap.Stage(\n    background_color=ap.Color("#333"),\n    stage_width=350,\n    stage_height=170,\n    stage_elem_id="stage",\n)\nmulti_line_text: ap.MultiLineText = ap.MultiLineText(\n    text="Lorem ipsum dolor sit amet, consectetur adipiscing elit, "\n    "sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. "\n    "Ut enim ad minim veniam",\n    width=300,\n    font_size=16,\n    fill_color=ap.Color("#00aaff"),\n    x=25,\n    y=25,\n)\nmulti_line_text.text_align = ap.CssTextAlign.LEFT\n\nap.save_overall_html(dest_dir_path="./css_text_align_left/")\n```',  # noqa
    ##################################################
    "## Example of CssTextAlign.CENTER": "## CssTextAlign.CENTERの例",
    ##################################################
    '```py\n# runnable\nimport apysc as ap\n\nstage: ap.Stage = ap.Stage(\n    background_color=ap.Color("#333"),\n    stage_width=350,\n    stage_height=170,\n    stage_elem_id="stage",\n)\nmulti_line_text: ap.MultiLineText = ap.MultiLineText(\n    text="Lorem ipsum dolor sit amet, consectetur adipiscing elit, "\n    "sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. "\n    "Ut enim ad minim veniam",\n    width=300,\n    font_size=16,\n    fill_color=ap.Color("#00aaff"),\n    x=25,\n    y=25,\n)\nmulti_line_text.text_align = ap.CssTextAlign.CENTER\n\nap.save_overall_html(dest_dir_path="./css_text_align_center/")\n```': '```py\n# runnable\nimport apysc as ap\n\nstage: ap.Stage = ap.Stage(\n    background_color=ap.Color("#333"),\n    stage_width=350,\n    stage_height=170,\n    stage_elem_id="stage",\n)\nmulti_line_text: ap.MultiLineText = ap.MultiLineText(\n    text="Lorem ipsum dolor sit amet, consectetur adipiscing elit, "\n    "sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. "\n    "Ut enim ad minim veniam",\n    width=300,\n    font_size=16,\n    fill_color=ap.Color("#00aaff"),\n    x=25,\n    y=25,\n)\nmulti_line_text.text_align = ap.CssTextAlign.CENTER\n\nap.save_overall_html(dest_dir_path="./css_text_align_center/")\n```',  # noqa
    ##################################################
    "## Example of CssTextAlign.RIGHT": "## CssTextAlign.RIGHTの例",
    ##################################################
    '```py\n# runnable\nimport apysc as ap\n\nstage: ap.Stage = ap.Stage(\n    background_color=ap.Color("#333"),\n    stage_width=350,\n    stage_height=170,\n    stage_elem_id="stage",\n)\nmulti_line_text: ap.MultiLineText = ap.MultiLineText(\n    text="Lorem ipsum dolor sit amet, consectetur adipiscing elit, "\n    "sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. "\n    "Ut enim ad minim veniam",\n    width=300,\n    font_size=16,\n    fill_color=ap.Color("#00aaff"),\n    x=25,\n    y=25,\n)\nmulti_line_text.text_align = ap.CssTextAlign.RIGHT\n\nap.save_overall_html(dest_dir_path="./css_text_align_right/")\n```': '```py\n# runnable\nimport apysc as ap\n\nstage: ap.Stage = ap.Stage(\n    background_color=ap.Color("#333"),\n    stage_width=350,\n    stage_height=170,\n    stage_elem_id="stage",\n)\nmulti_line_text: ap.MultiLineText = ap.MultiLineText(\n    text="Lorem ipsum dolor sit amet, consectetur adipiscing elit, "\n    "sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. "\n    "Ut enim ad minim veniam",\n    width=300,\n    font_size=16,\n    fill_color=ap.Color("#00aaff"),\n    x=25,\n    y=25,\n)\nmulti_line_text.text_align = ap.CssTextAlign.RIGHT\n\nap.save_overall_html(dest_dir_path="./css_text_align_right/")\n```',  # noqa
    ##################################################
    "## Example of CSSTextAlign.JUSTIFY": "## CssTextAlign.JUSTIFYの例",
    ##################################################
    "Notes: This enum setting justifies a text evenly.": "特記じこを : このenumの設定はテキストを均等配置します。",  # noqa
    ##################################################
    '```py\n# runnable\nimport apysc as ap\n\nstage: ap.Stage = ap.Stage(\n    background_color=ap.Color("#333"),\n    stage_width=350,\n    stage_height=170,\n    stage_elem_id="stage",\n)\nmulti_line_text: ap.MultiLineText = ap.MultiLineText(\n    text="Lorem ipsum dolor sit amet, consectetur adipiscing elit, "\n    "sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. "\n    "Ut enim ad minim veniam",\n    width=300,\n    font_size=16,\n    fill_color=ap.Color("#00aaff"),\n    x=25,\n    y=25,\n)\nmulti_line_text.text_align = ap.CssTextAlign.JUSTIFY\n\nap.save_overall_html(dest_dir_path="./css_text_align_justify/")\n```': '```py\n# runnable\nimport apysc as ap\n\nstage: ap.Stage = ap.Stage(\n    background_color=ap.Color("#333"),\n    stage_width=350,\n    stage_height=170,\n    stage_elem_id="stage",\n)\nmulti_line_text: ap.MultiLineText = ap.MultiLineText(\n    text="Lorem ipsum dolor sit amet, consectetur adipiscing elit, "\n    "sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. "\n    "Ut enim ad minim veniam",\n    width=300,\n    font_size=16,\n    fill_color=ap.Color("#00aaff"),\n    x=25,\n    y=25,\n)\nmulti_line_text.text_align = ap.CssTextAlign.JUSTIFY\n\nap.save_overall_html(dest_dir_path="./css_text_align_justify/")\n```',  # noqa
    ##################################################
    "## text_align property API": "## text_align 属性のAPI",
    ##################################################
    '<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>': '<span class="inconspicuous-txt">特記事項: このAPIドキュメントはドキュメントビルド用のスクリプトによって自動で生成・同期されています。そのためもしかしたらこの節の内容は前節までの内容と重複している場合があります。</span>',  # noqa
    ##################################################
    "**[Interface summary]**": "**[インターフェイス概要]**",
    ##################################################
    "Get a text-align value.<hr>": "テキストの行揃え設定の値を取得します。<hr>",
    ##################################################
    "**[Returns]**": "**[返却値]**",
    ##################################################
    "- `text_align`: CssTextAlign": "- `text_align`: CssTextAlign",
    ##################################################
    "  - A text-align value.": "  - 行揃え設定。",
    ##################################################
    "<hr>": "<hr>",
    ##################################################
    "**[Examples]**": "**[コードサンプル]**",
    ##################################################
    '```py\n>>> import apysc as ap\n>>> stage: ap.Stage = ap.Stage(\n...     background_color=ap.Color("#333"),\n...     stage_width=350,\n...     stage_height=170,\n...     stage_elem_id="stage",\n... )\n>>> multi_line_text: ap.MultiLineText = ap.MultiLineText(\n...     text="Lorem ipsum dolor sit amet, consectetur adipiscing elit, "\n...     "sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. "\n...     "Ut enim ad minim veniam",\n...     width=300,\n...     font_size=16,\n...     fill_color=ap.Color("#00aaff"),\n...     x=25,\n...     y=25,\n... )\n>>> multi_line_text.text_align = ap.CssTextAlign.RIGHT\n>>> assert multi_line_text.text_align == ap.CssTextAlign.RIGHT\n```': '```py\n>>> import apysc as ap\n>>> stage: ap.Stage = ap.Stage(\n...     background_color=ap.Color("#333"),\n...     stage_width=350,\n...     stage_height=170,\n...     stage_elem_id="stage",\n... )\n>>> multi_line_text: ap.MultiLineText = ap.MultiLineText(\n...     text="Lorem ipsum dolor sit amet, consectetur adipiscing elit, "\n...     "sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. "\n...     "Ut enim ad minim veniam",\n...     width=300,\n...     font_size=16,\n...     fill_color=ap.Color("#00aaff"),\n...     x=25,\n...     y=25,\n... )\n>>> multi_line_text.text_align = ap.CssTextAlign.RIGHT\n>>> assert multi_line_text.text_align == ap.CssTextAlign.RIGHT\n```',  # noqa
}
