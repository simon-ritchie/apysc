"""This module is for the translation mapping data of the
following document:

Document file: string_lstrip.md
Language: jp
"""

from typing import Dict

MAPPING: Dict[str, str] = {
    ##################################################
    "# String class lstrip interface": "# String クラスの lstrip インターフェイス",
    ##################################################
    "This page explains the `String` class `lstrip` method interface.": "このページでは`String`クラスの`lstrip`メソッドのインターフェイスについて説明します。",  # noqa
    ##################################################
    "## What interface is this?": "## インターフェイス概要",
    ##################################################
    "The `lstrip` method interface removes whitespaces or a specified character(s) from a string's left edge.": "`lstrip`メソッドのインターフェイスは文字列の左端から空白文字もしくは指定された文字（もしくは文字列）を取り除きます。",  # noqa
    ##################################################
    "## Basic usage": "## 基本的な使い方",
    ##################################################
    "The `lstrip` accepts the optional `string` argument.": "`lstrip`メソッドは省略可能な`string`引数を受け付けます。",  # noqa
    ##################################################
    "If you skip this argument, this interface removes whitespaces (and line breaks) from a string's left edge.": "もしもこの引数の指定を省略した場合、このインターフェイスは空白文字（スペースや改行など）を文字列の左端から取り除きます。",  # noqa
    ##################################################
    '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    stage_width=0,\n    stage_height=0,\n    background_color=ap.Color("#333"),\n    stage_elem_id="stage",\n)\n\nstring: ap.String = ap.String("  \n　 aabbaa  ")\nstring = string.lstrip()\nap.assert_equal(string, "aabbaa  ")\n\nap.save_overall_html(dest_dir_path="string_lstrip_basic_usage_1/")\n```': '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    stage_width=0,\n    stage_height=0,\n    background_color=ap.Color("#333"),\n    stage_elem_id="stage",\n)\n\nstring: ap.String = ap.String("  \n　 aabbaa  ")\nstring = string.lstrip()\nap.assert_equal(string, "aabbaa  ")\n\nap.save_overall_html(dest_dir_path="string_lstrip_basic_usage_1/")\n```',  # noqa
    ##################################################
    "Also, if you specify any value to the `string` argument, this interface removes its character(s) from a string's left edge.": "また、もしも何らかの文字列の値を`string`引数に指定した場合、このインターフェイスは文字列の左端からその文字（もしくは文字列）を取り除きます。",  # noqa
    ##################################################
    '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    stage_width=0,\n    stage_height=0,\n    background_color=ap.Color("#333"),\n    stage_elem_id="stage",\n)\n\nstring: ap.String = ap.String("aabbaa")\nstring = string.lstrip(string="a")\nap.assert_equal(string, "bbaa")\n\nap.save_overall_html(dest_dir_path="string_lstrip_basic_usage_2/")\n```': '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    stage_width=0,\n    stage_height=0,\n    background_color=ap.Color("#333"),\n    stage_elem_id="stage",\n)\n\nstring: ap.String = ap.String("aabbaa")\nstring = string.lstrip(string="a")\nap.assert_equal(string, "bbaa")\n\nap.save_overall_html(dest_dir_path="string_lstrip_basic_usage_2/")\n```',  # noqa
    ##################################################
    "## lstrip API": "## lstrip API",
    ##################################################
    '<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>': '<span class="inconspicuous-txt">特記事項: このAPIドキュメントはドキュメントビルド用のスクリプトによって自動で生成・同期されています。そのためもしかしたらこの節の内容は前節までの内容と重複している場合があります。</span>',  # noqa
    ##################################################
    "**[Interface summary]**": "**[インターフェイス概要]**",
    ##################################################
    "Remove a specified character or string from the beginning of this value.<hr>": "この値の左端から指定された文字もしく文字列を取り除きます。<hr>",  # noqa
    ##################################################
    "**[Parameters]**": "**[引数]**",
    ##################################################
    '- `string`: Optional[Union[str, "String"]], optional': '- `string`: Optional[Union[str, "String"]], optional',  # noqa
    ##################################################
    "  - A character or string to remove from the beginning of this value. If this argument is `None` (default), this method removes spaces and line breaks.": "  - この値の左端から取り除く文字もしくは文字列。もしもこの引数がの値がNone（デフォルト）だった場合、このメソッドはスペースや改行などを取り除きます。",  # noqa
    ##################################################
    "- `variable_name_suffix`: str, optional": "- `variable_name_suffix`: str, optional",  # noqa
    ##################################################
    "  - A JavaScript variable name suffix string. This setting is sometimes useful for JavaScript debugging.": "  - JavaScript上の変数のサフィックスの設定です。この設定はJavaScriptのデバッグ時に役立つことがあります。",  # noqa
    ##################################################
    "<hr>": "<hr>",
    ##################################################
    "**[Returns]**": "**[返却値]**",
    ##################################################
    "- `result`: String": "- `result`: String",
    ##################################################
    "  - A stripped result string.": "  - 除外処理実行後の文字列。",
    ##################################################
    "<hr>": "<hr>",
    ##################################################
    "**[Examples]**": "**[コードサンプル]**",
    ##################################################
    '```py\n>>> import apysc as ap\n>>> _ = ap.Stage()\n>>> string: ap.String = ap.String("   aabbcc  ")\n>>> string = string.lstrip()\n>>> string\nString("aabbcc  ")\n\n>>> string = ap.String("aabbccaa")\n>>> string = string.lstrip(string="a")\n>>> string\nString("bbccaa")\n```': '```py\n>>> import apysc as ap\n>>> _ = ap.Stage()\n>>> string: ap.String = ap.String("   aabbcc  ")\n>>> string = string.lstrip()\n>>> string\nString("aabbcc  ")\n\n>>> string = ap.String("aabbccaa")\n>>> string = string.lstrip(string="a")\n>>> string\nString("bbccaa")\n```',  # noqa
}
