"""This module is for the translation mapping data of the
following document:

Document file: int_and_number_to_hex.md
Language: jp
"""

from typing import Dict

MAPPING: Dict[str, str] = {
    ##################################################
    "# Int and Number classes to_hex method": "# Int と Number クラスの to_hex メソッド",
    ##################################################
    "This page explains the `Int` and `Number` classes `to_hex` method.": "このページでは`Int`と`Number`クラスの`to_hex`メソッドについて説明します。",  # noqa
    ##################################################
    "## What method is this?": "## メソッド概要",
    ##################################################
    'The `to_hex` method returns a hexadecimal string (e.g., "1f") from an `ap.Int` or `ap.Number` value.': '`to_hex`メソッドは`ap.Int`や`ap.Number`型の値から16進数の文字列（例 : "1f"）を返却します。',  # noqa
    ##################################################
    "## Note for `ap.Number` value": "## `ap.Number`型の値における特記事項",
    ##################################################
    "If you use this method with an `ap.Number` value, this method ignores floating-point number.": "`ap.Number`の値でこのメソッドを使った場合浮動小数点数の値は無視されます。",  # noqa
    ##################################################
    "## Basic usage": "## 基本的な使い方",
    ##################################################
    "The `to_hex` method requires no arguments.": "`to_hex`メソッドは引数の指定を必要としません。",
    ##################################################
    "This method returns a hexadecimal string (`ap.String` type value).": "このメソッドは16進数の文字列（`ap.String`型の値）を返却します。",  # noqa
    ##################################################
    '```py\n# runnable\n\nimport apysc as ap\n\nap.Stage(\n    stage_width=0,\n    stage_height=0,\n    background_color=ap.Color("#333"),\n    stage_elem_id="stage",\n)\nint_value: ap.Int = ap.Int(28)\nhex_str: ap.String = int_value.to_hex()\nap.assert_equal(hex_str, "1c")\n\nnumber: ap.Number = ap.Number(28.5)\nhex_str = int_value.to_hex()\nap.assert_equal(hex_str, "1c")\n\nap.save_overall_html(dest_dir_path="int_and_number_to_hex_basic_usage/")\n```': '```py\n# runnable\n\nimport apysc as ap\n\nap.Stage(\n    stage_width=0,\n    stage_height=0,\n    background_color=ap.Color("#333"),\n    stage_elem_id="stage",\n)\nint_value: ap.Int = ap.Int(28)\nhex_str: ap.String = int_value.to_hex()\nap.assert_equal(hex_str, "1c")\n\nnumber: ap.Number = ap.Number(28.5)\nhex_str = int_value.to_hex()\nap.assert_equal(hex_str, "1c")\n\nap.save_overall_html(dest_dir_path="int_and_number_to_hex_basic_usage/")\n```',  # noqa
    ##################################################
    "## to_hex method API": "## to_hex メソッドのAPI",
    ##################################################
    '<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>': '<span class="inconspicuous-txt">特記事項: このAPIドキュメントはドキュメントビルド用のスクリプトによって自動で生成・同期されています。そのためもしかしたらこの節の内容は前節までの内容と重複している場合があります。</span>',  # noqa
    ##################################################
    "**[Interface summary]**": "**[インターフェイス概要]**",
    ##################################################
    'Get a hexadecimal string (e.g., "1f").<hr>': '16進数の文字列（例 : "1f"）を取得します。<hr>',
    ##################################################
    "**[Parameters]**": "**[引数]**",
    ##################################################
    "- `variable_name_suffix`: str, default ''": "- `variable_name_suffix`: str, default ''",  # noqa
    ##################################################
    "  - A JavaScript variable name suffix string. This setting is sometimes useful for JavaScript debugging.": "  - JavaScript上の変数のサフィックスの設定です。この設定はJavaScriptのデバッグ時に役立つことがあります。",  # noqa
    ##################################################
    "<hr>": "<hr>",
    ##################################################
    "**[Returns]**": "**[返却値]**",
    ##################################################
    "- `hex_str`: String": "- `hex_str`: String",
    ##################################################
    '  - A hexadecimal string (e.g., "1f").': '  - 16進数の文字列（例 : "1f"）',
    ##################################################
    "<hr>": "<hr>",
    ##################################################
    "**[Notes]**": "**[特記事項]**",
    ##################################################
    "This method ignores floating point numbers.<hr>": "このメソッドは浮動小数点数を無視します。<hr>",
    ##################################################
    "**[Examples]**": "**[コードサンプル]**",
    ##################################################
    '```py\n>>> import apysc as ap\n>>> int_value: ap.Int = ap.Int(28)\n>>> hex_str: ap.String = int_value.to_hex()\n>>> hex_str\nString("1c")\n\n>>> number: ap.Number = ap.Number(28.5)\n>>> hex_str = int_value.to_hex()\n>>> hex_str\nString("1c")\n```': '```py\n>>> import apysc as ap\n>>> int_value: ap.Int = ap.Int(28)\n>>> hex_str: ap.String = int_value.to_hex()\n>>> hex_str\nString("1c")\n\n>>> number: ap.Number = ap.Number(28.5)\n>>> hex_str = int_value.to_hex()\n>>> hex_str\nString("1c")\n```',  # noqa
}
