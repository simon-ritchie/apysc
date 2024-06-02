"""This module is for the translation mapping data of the
following document:

Document file: to_string.md
Language: jp
"""

from typing import Dict

MAPPING: Dict[str, str] = {
    ##################################################
    "# to_string interface": "# to_string インターフェイス",
    ##################################################
    "This page explains the `to_string` method interface.": "このページでは`to_string`メソッドのインターフェイスについて説明します。",  # noqa
    ##################################################
    "## What interface is this?": "## インターフェイス概要",
    ##################################################
    "The `to_string` method returns a `String` representation of itself.": "`to_string`メソッドはそのインスタンス自体の`String`型での表現の値を返却します。",  # noqa
    ##################################################
    "This interface exists on each basic data class, such as the `Int`, `Number`,  `Boolean`, or `Array`.": "このインターフェイスは`Int`や`Number`、`Boolean`や`Array`などの基本的な各データクラスに存在します。",  # noqa
    ##################################################
    "## Basic usage": "## 基本的な使い方",
    ##################################################
    "The `to_string` method requires no arguments.": "`to_string`メソッドは引数の指定を必要としません。",
    ##################################################
    "A result value becomes a JavaScript-based value.": "返却値はJavaScriptに準じた値となります。",
    ##################################################
    "For instance, a `Boolean` value becomes `true` or `false`, not `True` or `False`.": "たとえば、`Boolean`の値であれば`True`や`False`などの値ではなく`true`や`false`といった文字列の値になります。",  # noqa
    ##################################################
    '```py\n# runnable\nimport apysc as ap\n\nstage: ap.Stage = ap.Stage(\n    background_color=ap.Color("#333"),\n    stage_width=0,\n    stage_height=0,\n    stage_elem_id="stage",\n)\nint_value: ap.Int = ap.Int(100)\nstring: ap.String = int_value.to_string()\nap.assert_equal(string, "100")\n\nnumber_value: ap.Number = ap.Number(10.5)\nstring = number_value.to_string()\nap.assert_equal(string, "10.5")\n\nbool_value: ap.Boolean = ap.Boolean(True)\nstring = bool_value.to_string()\nap.assert_equal(string, "true")\n\narray_value: ap.Array = ap.Array([10, 20, 30])\nstring = array_value.to_string()\nap.assert_equal(string, "10,20,30")\n\nap.save_overall_html(dest_dir_path="to_string_basic_usage_1/")\n```': '```py\n# runnable\nimport apysc as ap\n\nstage: ap.Stage = ap.Stage(\n    background_color=ap.Color("#333"),\n    stage_width=0,\n    stage_height=0,\n    stage_elem_id="stage",\n)\nint_value: ap.Int = ap.Int(100)\nstring: ap.String = int_value.to_string()\nap.assert_equal(string, "100")\n\nnumber_value: ap.Number = ap.Number(10.5)\nstring = number_value.to_string()\nap.assert_equal(string, "10.5")\n\nbool_value: ap.Boolean = ap.Boolean(True)\nstring = bool_value.to_string()\nap.assert_equal(string, "true")\n\narray_value: ap.Array = ap.Array([10, 20, 30])\nstring = array_value.to_string()\nap.assert_equal(string, "10,20,30")\n\nap.save_overall_html(dest_dir_path="to_string_basic_usage_1/")\n```',  # noqa
    ##################################################
    "Sometimes this method becomes useful when using text-related interfaces with its string.": "このメソッドはその文字列を使ってテキスト関係のインターフェイスを使う際に便利なことがあります。",  # noqa
    ##################################################
    '```py\n# runnable\nimport apysc as ap\n\nstage: ap.Stage = ap.Stage(\n    background_color=ap.Color("#333"),\n    stage_width=300,\n    stage_height=50,\n    stage_elem_id="stage",\n)\nwidth: ap.Int = ap.Int(50)\ntext: ap.SvgText = ap.SvgText(\n    text=ap.String("width is: ") + width.to_string(),\n    fill_color=ap.Color("#aaa"),\n    x=20,\n    y=30,\n)\nap.save_overall_html(dest_dir_path="to_string_basic_usage_2/")\n```': '```py\n# runnable\nimport apysc as ap\n\nstage: ap.Stage = ap.Stage(\n    background_color=ap.Color("#333"),\n    stage_width=300,\n    stage_height=50,\n    stage_elem_id="stage",\n)\nwidth: ap.Int = ap.Int(50)\ntext: ap.SvgText = ap.SvgText(\n    text=ap.String("width is: ") + width.to_string(),\n    fill_color=ap.Color("#aaa"),\n    x=20,\n    y=30,\n)\nap.save_overall_html(dest_dir_path="to_string_basic_usage_2/")\n```',  # noqa
    ##################################################
    "## to_string method API": "## to_string メソッドのAPI",
    ##################################################
    '<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>': '<span class="inconspicuous-txt">特記事項: このAPIドキュメントはドキュメントビルド用のスクリプトによって自動で生成・同期されています。そのためもしかしたらこの節の内容は前節までの内容と重複している場合があります。</span>',  # noqa
    ##################################################
    "**[Interface summary]**": "**[インターフェイス概要]**",
    ##################################################
    "Convert this instance to a string.<hr>": "このインスタンスを文字列へと変換します。<hr>",
    ##################################################
    "**[Returns]**": "**[返却値]**",
    ##################################################
    "- `string`: String": "- `string`: String",
    ##################################################
    "  - A converted string.": "  - 変換された文字列。",
    ##################################################
    "<hr>": "<hr>",
    ##################################################
    "**[Examples]**": "**[コードサンプル]**",
    ##################################################
    '```py\n>>> import apysc as ap\n>>> stage: ap.Stage = ap.Stage(\n...     background_color=ap.Color("#333"), stage_width=200, stage_height=200\n... )\n>>> int_value: ap.Int = ap.Int(value=100)\n>>> string: ap.String = int_value.to_string()\n>>> ap.assert_equal(string, "100")\n```': '```py\n>>> import apysc as ap\n>>> stage: ap.Stage = ap.Stage(\n...     background_color=ap.Color("#333"), stage_width=200, stage_height=200\n... )\n>>> int_value: ap.Int = ap.Int(value=100)\n>>> string: ap.String = int_value.to_string()\n>>> ap.assert_equal(string, "100")\n```',  # noqa
}
