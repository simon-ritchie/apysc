"""This module is for the translation mapping data of the
following document:

Document file: string_lower.md
Language: jp
"""

from typing import Dict

MAPPING: Dict[str, str] = {
    ##################################################
    "# String class lower method": "# String クラスの lower メソッド",
    ##################################################
    "This page explains the `String` class `lower` method.": "このページでは`String`クラスの`lower`メソッドについて説明します。",  # noqa
    ##################################################
    "## What method is this?": "## メソッド概要",
    ##################################################
    "The `lower` method returns a copied lowercase string.": "`lower`メソッドは小文字に変換された文字列のコピーを返却します。",  # noqa
    ##################################################
    "## Basic usage": "## 基本的な使い方",
    ##################################################
    "The `lower` method requires no arguments and it returns a `ap.String` type value.": "`lower`メソッドは引数を必要とせず、且つ`ap.String`型の値を返却します。",  # noqa
    ##################################################
    '```py\n# runnable\n\nimport apysc as ap\n\nap.Stage(\n    stage_width=0,\n    stage_height=0,\n    background_color=ap.Color("#333"),\n    stage_elem_id="stage",\n)\nstring: ap.String = ap.String("AbC1_")\nstring = string.lower()\nap.assert_equal(string, "abc1_")\n\nap.save_overall_html(dest_dir_path="string_lower_basic_usage/")\n```': '```py\n# runnable\n\nimport apysc as ap\n\nap.Stage(\n    stage_width=0,\n    stage_height=0,\n    background_color=ap.Color("#333"),\n    stage_elem_id="stage",\n)\nstring: ap.String = ap.String("AbC1_")\nstring = string.lower()\nap.assert_equal(string, "abc1_")\n\nap.save_overall_html(dest_dir_path="string_lower_basic_usage/")\n```',  # noqa
    ##################################################
    "## lower method API": "## lower メソッドのAPI",
    ##################################################
    '<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>': '<span class="inconspicuous-txt">特記事項: このAPIドキュメントはドキュメントビルド用のスクリプトによって自動で生成・同期されています。そのためもしかしたらこの節の内容は前節までの内容と重複している場合があります。</span>',  # noqa
    ##################################################
    "**[Interface summary]**": "**[インターフェイス概要]**",
    ##################################################
    "Get a copied lower case string.<hr>": "小文字に変換された文字列のコピーを取得します。<hr>",
    ##################################################
    "**[Returns]**": "**[返却値]**",
    ##################################################
    "- `string`: String": "- `string`: String",
    ##################################################
    "  - A copied lower case string.": "  - 小文字に変換された文字列のコピー。",
    ##################################################
    "<hr>": "<hr>",
    ##################################################
    "**[Examples]**": "**[コードサンプル]**",
    ##################################################
    '```py\n>>> import apysc as ap\n>>> string: ap.String = ap.String("HELLO")\n>>> string = string.lower()\n>>> string\nString("hello")\n```': '```py\n>>> import apysc as ap\n>>> string: ap.String = ap.String("HELLO")\n>>> string = string.lower()\n>>> string\nString("hello")\n```',  # noqa
}
