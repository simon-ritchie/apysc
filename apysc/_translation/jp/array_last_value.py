"""This module is for the translation mapping data of the
following document:

Document file: array_last_value.md
Language: jp
"""

from typing import Dict

MAPPING: Dict[str, str] = {
    ##################################################
    "# Array class last_value property": "# Array クラスの last_value プロパティ",
    ##################################################
    "This page explains the `Array` class `last_value` property.": "このページでは`Array`クラスの`last_value`属性について説明します。",  # noqa
    ##################################################
    "## What property is this?": "## 属性の概要",
    ##################################################
    "The `last_value` property returns the last value of an array.": "`last_value`属性は配列の最後の値を返却します。",  # noqa
    ##################################################
    "## Basic usage": "## 基本的な使い方",
    ##################################################
    "The following example shows that the `last_value` property becomes 30 (the array values are `[10, 20, 30]`).": "以下の例では`last_value`属性が30になっていることを試しています（配列の値は`[10, 20, 30]`となっています）。",  # noqa
    ##################################################
    '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    stage_width=0,\n    stage_height=0,\n    background_color=ap.Color("#333"),\n    stage_elem_id="stage",\n)\narr: ap.Array[int] = ap.Array([10, 20, 30])\nlast_value: int = arr.last_value\nap.assert_equal(last_value, 30)\n\nap.save_overall_html(dest_dir_path="array_last_value_basic_usage_1/")\n```': '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    stage_width=0,\n    stage_height=0,\n    background_color=ap.Color("#333"),\n    stage_elem_id="stage",\n)\narr: ap.Array[int] = ap.Array([10, 20, 30])\nlast_value: int = arr.last_value\nap.assert_equal(last_value, 30)\n\nap.save_overall_html(dest_dir_path="array_last_value_basic_usage_1/")\n```',  # noqa
    ##################################################
    "If an array's value is empty, this property becomes the `undefined` value on the JavaScript runtime:": "もしも配列の値が空の場合、この属性の値はJavaScriptのランタイム上では`undefined`になります。",  # noqa
    ##################################################
    '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    stage_width=0,\n    stage_height=0,\n    background_color=ap.Color("#333"),\n    stage_elem_id="stage",\n)\narr: ap.Array[ap.Int] = ap.Array([], fixed_value_type=ap.Int)\nlast_value: ap.Int = arr.last_value\nap.assert_undefined(last_value)\n\nap.save_overall_html(dest_dir_path="array_last_value_basic_usage_2/")\n```': '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    stage_width=0,\n    stage_height=0,\n    background_color=ap.Color("#333"),\n    stage_elem_id="stage",\n)\narr: ap.Array[ap.Int] = ap.Array([], fixed_value_type=ap.Int)\nlast_value: ap.Int = arr.last_value\nap.assert_undefined(last_value)\n\nap.save_overall_html(dest_dir_path="array_last_value_basic_usage_2/")\n```',  # noqa
    ##################################################
    "## last_value property API": "## last_value 属性のAPI",
    ##################################################
    '<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>': '<span class="inconspicuous-txt">特記事項: このAPIドキュメントはドキュメントビルド用のスクリプトによって自動で生成・同期されています。そのためもしかしたらこの節の内容は前節までの内容と重複している場合があります。</span>',  # noqa
    ##################################################
    "**[Interface summary]**": "**[インターフェイス概要]**",
    ##################################################
    "Get an array's last index value.<hr>": "配列の最後のインデックスの値を取得します。<hr>",
    ##################################################
    "**[Returns]**": "**[返却値]**",
    ##################################################
    "- `last_value`: _ArrValue": "- `last_value`: _ArrValue",
    ##################################################
    "  - An array's last index value.": "  - 配列の最後のインデックスの値。",
    ##################################################
    "<hr>": "<hr>",
    ##################################################
    "**[Notes]**": "**[特記事項]**",
    ##################################################
    " ・The constructor's `fixed_value_type` setting affects this property's value type. ": " ・コンストラクタの`fixed_value_type`設定はこの属性の値の型に影響します。",  # noqa
    ##################################################
    "<br> ・If an array is empty, this value becomes `undefined` on the JavaScript runtime.<hr>": "<br> ・もし配列が空の場合、この値はJavaScriptのランタイム上では`undefined`となります。<hr>",  # noqa
    ##################################################
    "**[Examples]**": "**[コードサンプル]**",
    ##################################################
    '```py\n>>> import apysc as ap\n>>> _ = ap.Stage(\n...     stage_width=100,\n...     stage_height=50,\n...     background_color=ap.Color("#333"),\n...     stage_elem_id="stage",\n... )\n>>> arr: ap.Array[ap.Int] = ap.Array([], fixed_value_type=ap.Int)\n>>> last_value: ap.Int = arr.last_value\n>>> ap.assert_undefined(last_value)\n>>> arr.append(ap.Int(10))\n>>> last_value = arr.last_value\n>>> ap.assert_equal(last_value, 10)\n>>> arr.append(ap.Int(20))\n>>> last_value = arr.last_value\n>>> ap.assert_equal(last_value, 20)\n```': '```py\n>>> import apysc as ap\n>>> _ = ap.Stage(\n...     stage_width=100,\n...     stage_height=50,\n...     background_color=ap.Color("#333"),\n...     stage_elem_id="stage",\n... )\n>>> arr: ap.Array[ap.Int] = ap.Array([], fixed_value_type=ap.Int)\n>>> last_value: ap.Int = arr.last_value\n>>> ap.assert_undefined(last_value)\n>>> arr.append(ap.Int(10))\n>>> last_value = arr.last_value\n>>> ap.assert_equal(last_value, 10)\n>>> arr.append(ap.Int(20))\n>>> last_value = arr.last_value\n>>> ap.assert_equal(last_value, 20)\n```',  # noqa
}
