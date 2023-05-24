"""This module is for the translation mapping data of the
following document:

Document file: assertion_basic_behavior.md
Language: jp
"""

from typing import Dict

MAPPING: Dict[str, str] = {
    ##################################################
    "# JavaScript assertion interface basic behaviors": "# JavaScript 上のアサーションのインターフェイスの基本的な挙動",  # noqa
    ##################################################
    "This page explains the JavaScript assertion interface basic behavior.": "このページではJavaScript上でのアサーション（テストなどのチェック処理）の各インターフェイスの基本的な挙動について説明します。",  # noqa
    ##################################################
    "## Interface names": "## 各インターフェイス名について",
    ##################################################
    "Each JavaScript assertion interface has the prefix of the `assert_` (e.g., `assert_equal`, `assert_true`, and so on).": "JavaScript上の各アサーションのインターフェイスは`assert_`のプレフィックスを持っています（例 : `assert_equal`や`assert_true`など）。",  # noqa
    ##################################################
    "These interfaces are positioned in the root package so you can use them, for example, `ap.assert_equal(...)`.": "これらのインターフェイスはapyscのルートのパッケージに配置されているため、たとえば`ap.assert_equal(...)`といった記述で使うことができます。",  # noqa
    ##################################################
    "## Assertion results": "## アサーションの結果について",
    ##################################################
    "These interfaces display the results on the browser console, as follows:": "これらのインターフェイスのチェック結果は以下の例のようにブラウザのコンソール上に表示されます:",  # noqa
    ##################################################
    '```py\n# runnable\nimport apysc as ap\n\nstage: ap.Stage = ap.Stage(\n    stage_width=0, stage_height=0, background_color="#333", stage_elem_id="stage"\n)\nint_1: ap.Int = ap.Int(10)\nap.assert_equal(left=10, right=int_1)\nap.save_overall_html(dest_dir_path="assertion_basic_behavior_results/")\n```': '```py\n# runnable\nimport apysc as ap\n\nstage: ap.Stage = ap.Stage(\n    stage_width=0, stage_height=0, background_color="#333", stage_elem_id="stage"\n)\nint_1: ap.Int = ap.Int(10)\nap.assert_equal(left=10, right=int_1)\nap.save_overall_html(dest_dir_path="assertion_basic_behavior_results/")\n```',  # noqa
    ##################################################
    "This code displays the information message on the browser console, like this (please press the F12 key to see):": "上記のコード例ではブラウザのコンソール上に以下のような結果の情報が表示されます（ブラウザ上でF12キーを押して確認してください）:",  # noqa
    ##################################################
    "```\n[assert_equal]\nRight-side variable name: i_11\nLeft value: 10 right value: 10\n```": "```\n[assert_equal]\nRight-side variable name: i_11\nLeft value: 10 right value: 10\n```",  # noqa
    ##################################################
    "If the assertion fails, then an error message also is displayed on the browser console:": "もしチェック処理に失敗した場合も同様にブラウザのコンソール上にエラーメッセージが表示されます:",  # noqa
    ##################################################
    '```py\n# runnable\nimport apysc as ap\n\nstage: ap.Stage = ap.Stage(\n    stage_width=0, stage_height=0, background_color="#333", stage_elem_id="stage"\n)\nint_1: ap.Int = ap.Int(10)\nap.assert_equal(left=11, right=int_1)\nap.save_overall_html(dest_dir_path="assertion_basic_behavior_results_failed/")\n```': '```py\n# runnable\nimport apysc as ap\n\nstage: ap.Stage = ap.Stage(\n    stage_width=0, stage_height=0, background_color="#333", stage_elem_id="stage"\n)\nint_1: ap.Int = ap.Int(10)\nap.assert_equal(left=11, right=int_1)\nap.save_overall_html(dest_dir_path="assertion_basic_behavior_results_failed/")\n```',  # noqa
    ##################################################
    "```\n[assert_equal]\nRight-side variable name: i_11\nLeft value: 11 right value: 10\n...\nAssertion failed:\n...\n```": "```\n[assert_equal]\nRight-side variable name: i_11\nLeft value: 11 right value: 10\n...\nAssertion failed:\n...\n```",  # noqa
    ##################################################
    "## Optional msg argument": "## 省略可能なmsg引数について",
    ##################################################
    "Each assertion interface has the `msg` optional argument. If you provide this argument, the error message is displayed on the browser console when an assertion fails.": "各インターフェイスは共通して`msg`という省略可能な引数のとオプションを持っています。もしこの引数に値を指定した場合、チェック処理に失敗した場合にエラーの詳細のメッセージとしてブラウザのコンソール上に表示されます。",  # noqa
    ##################################################
    '```py\n# runnable\nimport apysc as ap\n\nstage: ap.Stage = ap.Stage(\n    stage_width=0, stage_height=0, background_color="#333", stage_elem_id="stage"\n)\nint_1: ap.Int = ap.Int(10)\nap.assert_equal(left=11, right=int_1, msg="Values are not equal!")\nap.save_overall_html(dest_dir_path="assertion_basic_behavior_msg/")\n```': '```py\n# runnable\nimport apysc as ap\n\nstage: ap.Stage = ap.Stage(\n    stage_width=0, stage_height=0, background_color="#333", stage_elem_id="stage"\n)\nint_1: ap.Int = ap.Int(10)\nap.assert_equal(left=11, right=int_1, msg="Values are not equal!")\nap.save_overall_html(dest_dir_path="assertion_basic_behavior_msg/")\n```',  # noqa
    ##################################################
    "```\n[assert_equal]\nRight-side variable name: i_11\nLeft value: 11 right value: 10\n...\nAssertion failed: Values are not equal!\n```": "```\n[assert_equal]\nRight-side variable name: i_11\nLeft value: 11 right value: 10\n...\nAssertion failed: Values are not equal!\n```",  # noqa
}
