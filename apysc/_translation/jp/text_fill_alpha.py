"""This module is for the translation mapping data of the
following document:

Document file: text_fill_alpha.md
Language: jp
"""

from typing import Dict

MAPPING: Dict[str, str] = {
    ##################################################
    "# Text fill_alpha property": "# テキストの fill_alpha 属性",
    ##################################################
    "This page explains the text-related `fill_alpha` property.": "このページではテキスト関係の`fill_alpha`属性について説明します。",  # noqa
    ##################################################
    "## What property is this?": "## 属性の概要",
    ##################################################
    "The `fill_alpha` property interface updates or gets the instance's fill alpha (opacity).": "fill_alpha`属性のインターフェイスではインスタンスの塗りの透明度更新や取得を行うことができます。",  # noqa
    ##################################################
    "## Basic usage": "## 基本的な使い方",
    ##################################################
    "The getter or setter interface value becomes (or requires) the `Number` value (0.0 to 1.0).": "getterとsetterの両方のインターフェイスの値は`Number`型の0.0～1.0の範囲の値となります。",  # noqa
    ##################################################
    '```py\n# runnable\nimport apysc as ap\n\nstage: ap.Stage = ap.Stage(\n    background_color=ap.Color("#333"),\n    stage_width=350,\n    stage_height=170,\n    stage_elem_id="stage",\n)\nmulti_line_text: ap.MultiLineText = ap.MultiLineText(\n    text="Lorem ipsum dolor sit amet, consectetur adipiscing elit, "\n    "sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. "\n    "Ut enim ad minim veniam",\n    width=300,\n    font_size=16,\n    fill_color=ap.Color("#00aaff"),\n    x=25,\n    y=25,\n)\nmulti_line_text.fill_alpha = ap.Number(0.5)\nap.assert_equal(multi_line_text.fill_alpha, 0.5)\n\nap.save_overall_html(dest_dir_path="./text_fill_alpha_basic_usage/")\n```': '```py\n# runnable\nimport apysc as ap\n\nstage: ap.Stage = ap.Stage(\n    background_color=ap.Color("#333"),\n    stage_width=350,\n    stage_height=170,\n    stage_elem_id="stage",\n)\nmulti_line_text: ap.MultiLineText = ap.MultiLineText(\n    text="Lorem ipsum dolor sit amet, consectetur adipiscing elit, "\n    "sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. "\n    "Ut enim ad minim veniam",\n    width=300,\n    font_size=16,\n    fill_color=ap.Color("#00aaff"),\n    x=25,\n    y=25,\n)\nmulti_line_text.fill_alpha = ap.Number(0.5)\nap.assert_equal(multi_line_text.fill_alpha, 0.5)\n\nap.save_overall_html(dest_dir_path="./text_fill_alpha_basic_usage/")\n```',  # noqa
    ##################################################
    "## fill_alpha property API": "## fill_alpha 属性のAPI",
    ##################################################
    '<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>': '<span class="inconspicuous-txt">特記事項: このAPIドキュメントはドキュメントビルド用のスクリプトによって自動で生成・同期されています。そのためもしかしたらこの節の内容は前節までの内容と重複している場合があります。</span>',  # noqa
    ##################################################
    "**[Interface summary]**": "**[インターフェイス概要]**",
    ##################################################
    "Get a fill-alpha (opacity) value.<hr>": "塗りの透明度の値を取得します。<hr>",
    ##################################################
    "**[Returns]**": "**[返却値]**",
    ##################################################
    "- `alpha`: Number": "- `alpha`: Number",
    ##################################################
    "  - A fill-alpha (opacity) value.": "  - 塗りの透明度の値。",
    ##################################################
    "<hr>": "<hr>",
    ##################################################
    "**[Examples]**": "**[コードサンプル]**",
    ##################################################
    '```py\n>>> import apysc as ap\n>>> stage: ap.Stage = ap.Stage(\n...     background_color=ap.Color("#333"),\n...     stage_width=350,\n...     stage_height=170,\n...     stage_elem_id="stage",\n... )\n>>> multi_line_text: ap.MultiLineText = ap.MultiLineText(\n...     text="Lorem ipsum dolor sit amet, consectetur adipiscing elit, "\n...     "sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. "\n...     "Ut enim ad minim veniam",\n...     width=300,\n...     font_size=16,\n...     fill_color=ap.Color("#00aaff"),\n...     x=25,\n...     y=25,\n... )\n>>> multi_line_text.fill_alpha = ap.Number(0.5)\n>>> multi_line_text.fill_alpha\nNumber(0.5)\n```': '```py\n>>> import apysc as ap\n>>> stage: ap.Stage = ap.Stage(\n...     background_color=ap.Color("#333"),\n...     stage_width=350,\n...     stage_height=170,\n...     stage_elem_id="stage",\n... )\n>>> multi_line_text: ap.MultiLineText = ap.MultiLineText(\n...     text="Lorem ipsum dolor sit amet, consectetur adipiscing elit, "\n...     "sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. "\n...     "Ut enim ad minim veniam",\n...     width=300,\n...     font_size=16,\n...     fill_color=ap.Color("#00aaff"),\n...     x=25,\n...     y=25,\n... )\n>>> multi_line_text.fill_alpha = ap.Number(0.5)\n>>> multi_line_text.fill_alpha\nNumber(0.5)\n```',  # noqa
}
