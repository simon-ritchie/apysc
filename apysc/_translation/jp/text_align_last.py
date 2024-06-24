"""This module is for the translation mapping data of the
following document:

Document file: text_align_last.md
Language: jp
"""

from typing import Dict

MAPPING: Dict[str, str] = {
    ##################################################
    "# text_align_last property": "# text_align_last 属性",
    ##################################################
    "This page explains the text-related `text_align_last` property.": "このページではテキスト関係の`text_align_last`属性について説明します。",  # noqa
    ##################################################
    "## What property is this?": "## 属性の概要",
    ##################################################
    "The `text_align_last` property updates or gets the text last line's alignment setting.": "`text_align_last`属性では最終行の行揃えの設定の更新もしくは取得を行えます。",  # noqa
    ##################################################
    "## Basic usage": "## 基本的な使い方",
    ##################################################
    "The getter and setter interfaces' type becomes an `ap.CssTextAlignLast` enum value.": "getterとsetterの各インターフェイスの型は`ap.CssTextAlignLast`のenumの値となります。",  # noqa
    ##################################################
    "The acceptable enum values are as follows:": "指定できるenumの値は以下の通りです:",
    ##################################################
    "- `CssTextAlignLast.AUTO` (default)": "- `CssTextAlignLast.AUTO` （デフォルト）",
    ##################################################
    "- `CssTextAlignLast.LEFT`": "- `CssTextAlignLast.LEFT`",
    ##################################################
    "- `CssTextAlignLast.CENTER`": "- `CssTextAlignLast.CENTER`",
    ##################################################
    "- `CssTextAlignLast.RIGHT`": "- `CssTextAlignLast.RIGHT`",
    ##################################################
    "- `CssTextAlignLast.JUSTIFY`": "- `CssTextAlignLast.JUSTIFY`",
    ##################################################
    "## Example of CssTextAlignLast.AUTO": "## CssTextAlignLast.AUTOの例",
    ##################################################
    "Notes: This setting is a default setting.": "特記事項: この設定はデフォルトの設定です。",
    ##################################################
    "The `CssTextAlignLast.AUTO` setting inherits the `text_align` setting.": "`CssTextAlignLast.AUTO`設定（挙動）は`text_align`の設定を継承します。",  # noqa
    ##################################################
    "For example, if the `text_align` setting is the `CssTextAlign.CENTER`, the `text_align_last` property also behaves as the center align.": "例えば、もし`text_align`設定が`CssTextAlign.CENTER`の場合には`text_align_last`属性も中央寄せとして振る舞います。",  # noqa
    ##################################################
    '```py\n# runnable\nimport apysc as ap\n\nstage: ap.Stage = ap.Stage(\n    background_color=ap.Color("#333"),\n    stage_width=350,\n    stage_height=170,\n    stage_elem_id="stage",\n)\nmulti_line_text: ap.MultiLineText = ap.MultiLineText(\n    text="Lorem ipsum dolor sit amet, consectetur adipiscing elit, "\n    "sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. "\n    "Ut enim ad minim veniam",\n    width=300,\n    font_size=16,\n    fill_color=ap.Color("#00aaff"),\n    x=25,\n    y=25,\n)\nmulti_line_text.text_align = ap.CssTextAlign.CENTER\nmulti_line_text.text_align_last = ap.CssTextAlignLast.AUTO\n\nap.save_overall_html(dest_dir_path="./css_text_align_last_auto/")\n```': '```py\n# runnable\nimport apysc as ap\n\nstage: ap.Stage = ap.Stage(\n    background_color=ap.Color("#333"),\n    stage_width=350,\n    stage_height=170,\n    stage_elem_id="stage",\n)\nmulti_line_text: ap.MultiLineText = ap.MultiLineText(\n    text="Lorem ipsum dolor sit amet, consectetur adipiscing elit, "\n    "sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. "\n    "Ut enim ad minim veniam",\n    width=300,\n    font_size=16,\n    fill_color=ap.Color("#00aaff"),\n    x=25,\n    y=25,\n)\nmulti_line_text.text_align = ap.CssTextAlign.CENTER\nmulti_line_text.text_align_last = ap.CssTextAlignLast.AUTO\n\nap.save_overall_html(dest_dir_path="./css_text_align_last_auto/")\n```',  # noqa
    ##################################################
    "## Example of CssTextAlignLast.LEFT": "## CssTextAlignLast.LEFTの例",
    ##################################################
    '```py\n# runnable\nimport apysc as ap\n\nstage: ap.Stage = ap.Stage(\n    background_color=ap.Color("#333"),\n    stage_width=350,\n    stage_height=170,\n    stage_elem_id="stage",\n)\nmulti_line_text: ap.MultiLineText = ap.MultiLineText(\n    text="Lorem ipsum dolor sit amet, consectetur adipiscing elit, "\n    "sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. "\n    "Ut enim ad minim veniam",\n    width=300,\n    font_size=16,\n    fill_color=ap.Color("#00aaff"),\n    x=25,\n    y=25,\n)\nmulti_line_text.text_align = ap.CssTextAlign.JUSTIFY\nmulti_line_text.text_align_last = ap.CssTextAlignLast.LEFT\n\nap.save_overall_html(dest_dir_path="./css_text_align_last_left/")\n```': '```py\n# runnable\nimport apysc as ap\n\nstage: ap.Stage = ap.Stage(\n    background_color=ap.Color("#333"),\n    stage_width=350,\n    stage_height=170,\n    stage_elem_id="stage",\n)\nmulti_line_text: ap.MultiLineText = ap.MultiLineText(\n    text="Lorem ipsum dolor sit amet, consectetur adipiscing elit, "\n    "sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. "\n    "Ut enim ad minim veniam",\n    width=300,\n    font_size=16,\n    fill_color=ap.Color("#00aaff"),\n    x=25,\n    y=25,\n)\nmulti_line_text.text_align = ap.CssTextAlign.JUSTIFY\nmulti_line_text.text_align_last = ap.CssTextAlignLast.LEFT\n\nap.save_overall_html(dest_dir_path="./css_text_align_last_left/")\n```',  # noqa
    ##################################################
    "## Example of CssTextAlignLast.CENTER": "## CssTextAlignLast.CENTERの例",
    ##################################################
    '```py\n# runnable\nimport apysc as ap\n\nstage: ap.Stage = ap.Stage(\n    background_color=ap.Color("#333"),\n    stage_width=350,\n    stage_height=170,\n    stage_elem_id="stage",\n)\nmulti_line_text: ap.MultiLineText = ap.MultiLineText(\n    text="Lorem ipsum dolor sit amet, consectetur adipiscing elit, "\n    "sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. "\n    "Ut enim ad minim veniam",\n    width=300,\n    font_size=16,\n    fill_color=ap.Color("#00aaff"),\n    x=25,\n    y=25,\n)\nmulti_line_text.text_align = ap.CssTextAlign.JUSTIFY\nmulti_line_text.text_align_last = ap.CssTextAlignLast.CENTER\n\nap.save_overall_html(dest_dir_path="./css_text_align_last_center/")\n```': '```py\n# runnable\nimport apysc as ap\n\nstage: ap.Stage = ap.Stage(\n    background_color=ap.Color("#333"),\n    stage_width=350,\n    stage_height=170,\n    stage_elem_id="stage",\n)\nmulti_line_text: ap.MultiLineText = ap.MultiLineText(\n    text="Lorem ipsum dolor sit amet, consectetur adipiscing elit, "\n    "sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. "\n    "Ut enim ad minim veniam",\n    width=300,\n    font_size=16,\n    fill_color=ap.Color("#00aaff"),\n    x=25,\n    y=25,\n)\nmulti_line_text.text_align = ap.CssTextAlign.JUSTIFY\nmulti_line_text.text_align_last = ap.CssTextAlignLast.CENTER\n\nap.save_overall_html(dest_dir_path="./css_text_align_last_center/")\n```',  # noqa
    ##################################################
    "## Example of CssTextAlignLast.RIGHT": "## CssTextAlignLast.RIGHTの例",
    ##################################################
    '```py\n# runnable\nimport apysc as ap\n\nstage: ap.Stage = ap.Stage(\n    background_color=ap.Color("#333"),\n    stage_width=350,\n    stage_height=170,\n    stage_elem_id="stage",\n)\nmulti_line_text: ap.MultiLineText = ap.MultiLineText(\n    text="Lorem ipsum dolor sit amet, consectetur adipiscing elit, "\n    "sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. "\n    "Ut enim ad minim veniam",\n    width=300,\n    font_size=16,\n    fill_color=ap.Color("#00aaff"),\n    x=25,\n    y=25,\n)\nmulti_line_text.text_align = ap.CssTextAlign.JUSTIFY\nmulti_line_text.text_align_last = ap.CssTextAlignLast.RIGHT\n\nap.save_overall_html(dest_dir_path="./css_text_align_last_right/")\n```': '```py\n# runnable\nimport apysc as ap\n\nstage: ap.Stage = ap.Stage(\n    background_color=ap.Color("#333"),\n    stage_width=350,\n    stage_height=170,\n    stage_elem_id="stage",\n)\nmulti_line_text: ap.MultiLineText = ap.MultiLineText(\n    text="Lorem ipsum dolor sit amet, consectetur adipiscing elit, "\n    "sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. "\n    "Ut enim ad minim veniam",\n    width=300,\n    font_size=16,\n    fill_color=ap.Color("#00aaff"),\n    x=25,\n    y=25,\n)\nmulti_line_text.text_align = ap.CssTextAlign.JUSTIFY\nmulti_line_text.text_align_last = ap.CssTextAlignLast.RIGHT\n\nap.save_overall_html(dest_dir_path="./css_text_align_last_right/")\n```',  # noqa
    ##################################################
    "## Example of CssTextAlignLast.JUSTIFY": "## CssTextAlignLast.JUSTIFYの例",
    ##################################################
    "Notes: This enum setting justifies the last line text evenly.": "特記事項: このenumの設定は最終行のテキストを均等に行揃えします。",  # noqa
    ##################################################
    '```py\n# runnable\nimport apysc as ap\n\nstage: ap.Stage = ap.Stage(\n    background_color=ap.Color("#333"),\n    stage_width=350,\n    stage_height=170,\n    stage_elem_id="stage",\n)\nmulti_line_text: ap.MultiLineText = ap.MultiLineText(\n    text="Lorem ipsum dolor sit amet, consectetur adipiscing elit, "\n    "sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. "\n    "Ut enim ad minim veniam",\n    width=300,\n    font_size=16,\n    fill_color=ap.Color("#00aaff"),\n    x=25,\n    y=25,\n)\nmulti_line_text.text_align = ap.CssTextAlign.JUSTIFY\nmulti_line_text.text_align_last = ap.CssTextAlignLast.JUSTIFY\n\nap.save_overall_html(dest_dir_path="./css_text_align_last_justify/")\n```': '```py\n# runnable\nimport apysc as ap\n\nstage: ap.Stage = ap.Stage(\n    background_color=ap.Color("#333"),\n    stage_width=350,\n    stage_height=170,\n    stage_elem_id="stage",\n)\nmulti_line_text: ap.MultiLineText = ap.MultiLineText(\n    text="Lorem ipsum dolor sit amet, consectetur adipiscing elit, "\n    "sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. "\n    "Ut enim ad minim veniam",\n    width=300,\n    font_size=16,\n    fill_color=ap.Color("#00aaff"),\n    x=25,\n    y=25,\n)\nmulti_line_text.text_align = ap.CssTextAlign.JUSTIFY\nmulti_line_text.text_align_last = ap.CssTextAlignLast.JUSTIFY\n\nap.save_overall_html(dest_dir_path="./css_text_align_last_justify/")\n```',  # noqa
    ##################################################
    "## text_align_last property API": "## text_align_last 属性のAPI",
    ##################################################
    '<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>': '<span class="inconspicuous-txt">特記事項: このAPIドキュメントはドキュメントビルド用のスクリプトによって自動で生成・同期されています。そのためもしかしたらこの節の内容は前節までの内容と重複している場合があります。</span>',  # noqa
    ##################################################
    "**[Interface summary]**": "**[インターフェイス概要]**",
    ##################################################
    "Get a text-align-last value.<hr>": "text-align-last属性の値を取得します。<hr>",
    ##################################################
    "**[Returns]**": "**[返却値]**",
    ##################################################
    "- `text_align_last`: CssTextAlignLast": "- `text_align_last`: CssTextAlignLast",
    ##################################################
    "  - A text-align-last value.": "  - text-align-last属性の値。",
    ##################################################
    "<hr>": "<hr>",
    ##################################################
    "**[Examples]**": "**[コードサンプル]**",
    ##################################################
    '```py\n>>> import apysc as ap\n>>> stage: ap.Stage = ap.Stage(\n...     background_color=ap.Color("#333"),\n...     stage_width=350,\n...     stage_height=170,\n...     stage_elem_id="stage",\n... )\n>>> multi_line_text: ap.MultiLineText = ap.MultiLineText(\n...     text="Lorem ipsum dolor sit amet, consectetur adipiscing elit, "\n...     "sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. "\n...     "Ut enim ad minim veniam",\n...     width=300,\n...     font_size=16,\n...     fill_color=ap.Color("#00aaff"),\n...     x=25,\n...     y=25,\n... )\n>>> multi_line_text.text_align = ap.CssTextAlign.JUSTIFY\n>>> multi_line_text.text_align_last = ap.CssTextAlignLast.RIGHT\n>>> assert multi_line_text.text_align_last == ap.CssTextAlignLast.RIGHT\n```': '```py\n>>> import apysc as ap\n>>> stage: ap.Stage = ap.Stage(\n...     background_color=ap.Color("#333"),\n...     stage_width=350,\n...     stage_height=170,\n...     stage_elem_id="stage",\n... )\n>>> multi_line_text: ap.MultiLineText = ap.MultiLineText(\n...     text="Lorem ipsum dolor sit amet, consectetur adipiscing elit, "\n...     "sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. "\n...     "Ut enim ad minim veniam",\n...     width=300,\n...     font_size=16,\n...     fill_color=ap.Color("#00aaff"),\n...     x=25,\n...     y=25,\n... )\n>>> multi_line_text.text_align = ap.CssTextAlign.JUSTIFY\n>>> multi_line_text.text_align_last = ap.CssTextAlignLast.RIGHT\n>>> assert multi_line_text.text_align_last == ap.CssTextAlignLast.RIGHT\n```',  # noqa
}
