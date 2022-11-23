"""This module is for the translation mapping data of the
following document:

Document file: assert_true_and_false.md
Language: jp
"""

from typing import Dict

MAPPING: Dict[str, str] = {
    ##################################################
    "# assert_true and assert_false interfaces": "# assert_true と assert_false インターフェイス",  # noqa
    ##################################################
    "This page explains the `assert_true` and `assert_false` function interfaces.": "このページでは`assert_true`と`assert_false`関数の各インターフェイスについて説明します。",  # noqa
    ##################################################
    "## What interfaces are these?": "## 各インターフェイスの概要",
    ##################################################
    "The `assert_true` function interface asserts a specified `Boolean` value is true. Conversely, the `assert_false` function interface asserts a specified `Boolean` value is false.": "`assert_true`関数のインターフェイスは指定された`Boolean`の値が真（true）であることをチェックします。逆に`assert_false`関数のインターフェイスは指定された`Boolean`の値が偽（false）であることをチェックします。",  # noqa
    ##################################################
    "## See also": "## 関連資料",
    ##################################################
    "- [JavaScript assertion interface basic behavior](assertion_basic_behavior.md)": "- [JavaScriptの各アサーションのインターフェイスの基本的な挙動](jp_assertion_basic_behavior.md)",  # noqa
    ##################################################
    "## Basic usage": "## 基本的な使い方",
    ##################################################
    "The `assert_true` and `assert_false` interfaces requires `value` argument. The `type_strict` and `msg` arguments are optional (default value of the `type_strict` argument is `True`).": "`assert_true`と`assert_false`の各インターフェイスは`value`引数を必要とします。`type_strict`と`msg`引数は省略可です。`type_strict`引数のデフォルト値は`True`となります。",  # noqa
    ##################################################
    "If the `type_strict` argument is `True`, the assertion will use the JavaScript strict comparison operator (`===`). For instance, if the `value` is `Int(1)` and the `type_strict` is `True`, an assertion will fail (because of the comparison between the `Boolean` and `Int`). Conversely, if the `type_strict` is `False`, `Int(1)` will pass the `assert_true` assertion.": "もしも`type_strict`引数に`True`が指定された場合チェック処理はJavaScriptの厳密な型の比較（`===`による比較）によって行われます。たとえばもし`value`引数の値が`Int(1)`で且つ`type_strict`引数が`True`の場合チェック処理は真偽値と整数（`Int`）間の比較となるため失敗します。逆に`type_strict`が`False`で且つ値が`Int(1)`であれば`assert_true`関数によるチェック処理は通ります。",  # noqa
    ##################################################
    "These interfaces display an assertion result on the browser console.": "これらのインターフェイスによるチェック結果はブラウザ上のコンソールに表示されます。",  # noqa
    ##################################################
    "The following assertion example (`assert_true` and value is the `Boolean(True)`) passes:": "以下の`assert_true`関数と`Boolean(True)`の値を使用した処理のコード例ではチェックを通ります:",  # noqa
    ##################################################
    '```py\n# runnable\nimport apysc as ap\n\nstage: ap.Stage = ap.Stage(\n    stage_width=0, stage_height=0, background_color="#333", stage_elem_id="stage"\n)\n\nbool_1: ap.Boolean = ap.Boolean(True)\nap.assert_true(bool_1, msg="Boolean value is not True!")\n\nap.save_overall_html(dest_dir_path="assert_true_basic_usage_1/")\n```': '```py\n# runnable\nimport apysc as ap\n\nstage: ap.Stage = ap.Stage(\n    stage_width=0, stage_height=0, background_color="#333", stage_elem_id="stage"\n)\n\nbool_1: ap.Boolean = ap.Boolean(True)\nap.assert_true(bool_1, msg="Boolean value is not True!")\n\nap.save_overall_html(dest_dir_path="assert_true_basic_usage_1/")\n```',  # noqa
    ##################################################
    "```\n[assert_true]\nRight-side variable name: b_3\nLeft value: true right value: true\n```": "```\n[assert_true]\nRight-side variable name: b_3\nLeft value: true right value: true\n```",  # noqa
    ##################################################
    "The following assertion example (`assert_true` and value is the `Boolean(False)`) fails:": "以下の`assert_true`関数と`Boolean(False)`の値を使った処理ではチェックが失敗します:",  # noqa
    ##################################################
    '```py\n# runnable\nimport apysc as ap\n\nstage: ap.Stage = ap.Stage(\n    stage_width=0, stage_height=0, background_color="#333", stage_elem_id="stage"\n)\n\nbool_1: ap.Boolean = ap.Boolean(False)\nap.assert_true(bool_1, msg="Boolean value is not True!")\n\nap.save_overall_html(dest_dir_path="assert_true_basic_usage_2/")\n```': '```py\n# runnable\nimport apysc as ap\n\nstage: ap.Stage = ap.Stage(\n    stage_width=0, stage_height=0, background_color="#333", stage_elem_id="stage"\n)\n\nbool_1: ap.Boolean = ap.Boolean(False)\nap.assert_true(bool_1, msg="Boolean value is not True!")\n\nap.save_overall_html(dest_dir_path="assert_true_basic_usage_2/")\n```',  # noqa
    ##################################################
    "```\n[assert_true]\nRight-side variable name: b_3\nLeft value: true right value: false\n...\nAssertion failed: Boolean value is not True!\n```": "```\n[assert_true]\nRight-side variable name: b_3\nLeft value: true right value: false\n...\nAssertion failed: Boolean value is not True!\n```",  # noqa
    ##################################################
    "The following assertion example (`assert_true` and value is the `Int(1)` and `type_strict` is `True`) will fail:": "以下の`assert_true`関数と`Int(1)`の値を使い、`type_strict`に`True`を指定した例ではチェックが失敗します:",  # noqa
    ##################################################
    '```py\n# runnable\nimport apysc as ap\n\nstage: ap.Stage = ap.Stage(\n    stage_width=0, stage_height=0, background_color="#333", stage_elem_id="stage"\n)\n\nint_1: ap.Int = ap.Int(1)\nap.assert_true(int_1, type_strict=True, msg="Value is not Boolean(True)!")\n\nap.save_overall_html(dest_dir_path="assert_true_basic_usage_3/")\n```': '```py\n# runnable\nimport apysc as ap\n\nstage: ap.Stage = ap.Stage(\n    stage_width=0, stage_height=0, background_color="#333", stage_elem_id="stage"\n)\n\nint_1: ap.Int = ap.Int(1)\nap.assert_true(int_1, type_strict=True, msg="Value is not Boolean(True)!")\n\nap.save_overall_html(dest_dir_path="assert_true_basic_usage_3/")\n```',  # noqa
    ##################################################
    "```\n[assert_true]\nRight-side variable name: i_11\nLeft value: true right value: 1\n...\nAssertion failed: Value is not Boolean(True)!\n```": "```\n[assert_true]\nRight-side variable name: i_11\nLeft value: true right value: 1\n...\nAssertion failed: Value is not Boolean(True)!\n```",  # noqa
    ##################################################
    "The following assertion example (`assert_true` and value is the `Int(1)` and `type_strict` is `False`) will pass:": "以下の`assert_true`関数と`Int(1)`の値を使い`type_strict`に`False`を設定した処理ではチェックが通ります:",  # noqa
    ##################################################
    '```py\n# runnable\nimport apysc as ap\n\nstage: ap.Stage = ap.Stage(\n    stage_width=0, stage_height=0, background_color="#333", stage_elem_id="stage"\n)\n\nint_1: ap.Int = ap.Int(1)\nap.assert_true(int_1, type_strict=False, msg="Value is not True!")\n\nap.save_overall_html(dest_dir_path="assert_true_basic_usage_4/")\n```': '```py\n# runnable\nimport apysc as ap\n\nstage: ap.Stage = ap.Stage(\n    stage_width=0, stage_height=0, background_color="#333", stage_elem_id="stage"\n)\n\nint_1: ap.Int = ap.Int(1)\nap.assert_true(int_1, type_strict=False, msg="Value is not True!")\n\nap.save_overall_html(dest_dir_path="assert_true_basic_usage_4/")\n```',  # noqa
    ##################################################
    "```\n[assert_true]\nRight-side variable name: i_11\nLeft value: true right value: 1\n```": "```\n[assert_true]\nRight-side variable name: i_11\nLeft value: true right value: 1\n```",  # noqa
    ##################################################
    "The following assertion example (`assert_false` and value is the `Boolean(False)`) passes:": "以下の`assert_false`関数と`Boolean(False)`の値を使った処理ではチェックを通ります:",  # noqa
    ##################################################
    '```py\n# runnable\nimport apysc as ap\n\nstage: ap.Stage = ap.Stage(\n    stage_width=0, stage_height=0, background_color="#333", stage_elem_id="stage"\n)\n\nbool_1: ap.Boolean = ap.Boolean(False)\nap.assert_false(bool_1, msg="Value is not False!")\n\nap.save_overall_html(dest_dir_path="assert_false_basic_usage_1/")\n```': '```py\n# runnable\nimport apysc as ap\n\nstage: ap.Stage = ap.Stage(\n    stage_width=0, stage_height=0, background_color="#333", stage_elem_id="stage"\n)\n\nbool_1: ap.Boolean = ap.Boolean(False)\nap.assert_false(bool_1, msg="Value is not False!")\n\nap.save_overall_html(dest_dir_path="assert_false_basic_usage_1/")\n```',  # noqa
    ##################################################
    "```\n[assert_false]\nRight-side variable name: b_3\nLeft value: false right value: false\n```": "```\n[assert_false]\nRight-side variable name: b_3\nLeft value: false right value: false\n```",  # noqa
    ##################################################
    "## assert_true API": "## assert_true API",
    ##################################################
    '<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>': '<span class="inconspicuous-txt">特記事項: このAPIドキュメントはドキュメントビルド用のスクリプトによって自動で生成・同期されています。そのためもしかしたらこの節の内容は前節までの内容と重複している場合があります。</span>',  # noqa
    ##################################################
    "**[Interface summary]**": "**[インターフェイス概要]**",
    ##################################################
    "JavaScript assertion interface for true condition.<hr>": "真偽値の真の値のためのJavaScript上のアサーションのインターフェイスです。<hr>",  # noqa
    ##################################################
    "**[Parameters]**": "**[引数]**",
    ##################################################
    "- `value`: *": "- `value`: *",
    ##################################################
    "  - Target value to check.": "  - チェック対象の値。",
    ##################################################
    "- `type_strict`: bool, default True": "- `type_strict`: bool, default True",
    ##################################################
    "  - Whether strictly check actual value or not. For example, if type_strict is True, an integer of 1 fails tests. On the contrary (if type_strict is False), an integer of 1 passes tests.": "  - 厳密な型でのチェックを行うかどうかの設定です。たとえばtype_strictにTrueを指定した場合は整数の1ではテストは失敗します。逆にtype_strictがFalseの場合整数の1はテストを通過します。",  # noqa
    ##################################################
    "- `msg`: str, optional": "- `msg`: str, optional",
    ##################################################
    "  - Message to display when assertion failed.": "  - チェックに失敗した際に表示するメッセージ。",
    ##################################################
    "<hr>": "<hr>",
    ##################################################
    "**[Examples]**": "**[コードサンプル]**",
    ##################################################
    "```py\n>>> import apysc as ap\n>>> int_val: ap.Int = ap.Int(10)\n>>> boolean: ap.Boolean = int_val == 10\n>>> ap.assert_true(boolean)\n```": "```py\n>>> import apysc as ap\n>>> int_val: ap.Int = ap.Int(10)\n>>> boolean: ap.Boolean = int_val == 10\n>>> ap.assert_true(boolean)\n```",  # noqa
    ##################################################
    "## assert_false API": "## assert_false API",
    ##################################################
    '<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>': '<span class="inconspicuous-txt">特記事項: このAPIドキュメントはドキュメントビルド用のスクリプトによって自動で生成・同期されています。そのためもしかしたらこの節の内容は前節までの内容と重複している場合があります。</span>',  # noqa
    ##################################################
    "**[Interface summary]**": "**[インターフェイス概要]**",
    ##################################################
    "JavaScript assertion interface for false condition.<hr>": "真偽値の偽の値のためのJavaScript上のアサーションのインターフェイスです。<hr>",  # noqa
    ##################################################
    "**[Parameters]**": "**[引数]**",
    ##################################################
    "- `value`: *": "- `value`: *",
    ##################################################
    "  - Target value to check.": "  - チェック対象の値。",
    ##################################################
    "- `type_strict`: bool, default True": "- `type_strict`: bool, default True",
    ##################################################
    "  - Whether strictly check actual value or not. For example, if type_strict is True, an integer of 0 fails tests. On the contrary (if type_strict is False), an integer of 0 passes tests.": "  - 厳密な型でのチェックを行うかどうかの設定です。たとえばtype_strictにTrueを指定した場合は整数の0ではテストは失敗します。逆にtype_strictがFalseの場合整数の0はテストを通過します。",  # noqa
    ##################################################
    "- `msg`: str, optional": "- `msg`: str, optional",
    ##################################################
    "  - Message to display when assertion failed.": "  - チェックに失敗した際に表示するメッセージ。",
    ##################################################
    "<hr>": "<hr>",
    ##################################################
    "**[Examples]**": "**[コードサンプル]**",
    ##################################################
    "```py\n>>> import apysc as ap\n>>> int_val: ap.Int = ap.Int(10)\n>>> boolean: ap.Boolean = int_val == 11\n>>> ap.assert_false(boolean)\n```": "```py\n>>> import apysc as ap\n>>> int_val: ap.Int = ap.Int(10)\n>>> boolean: ap.Boolean = int_val == 11\n>>> ap.assert_false(boolean)\n```",  # noqa
}
