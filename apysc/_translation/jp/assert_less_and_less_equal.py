"""This module is for the translation mapping data of the
following document:

Document file: assert_less_and_less_equal.md
Language: jp
"""

from typing import Dict

MAPPING: Dict[str, str] = {
    ##################################################
    "# assert_less and assert_less_equal interfaces": "# assert_less と assert_less_equal の各インターフェイス",  # noqa
    ##################################################
    "This page explains the `assert_less` and `assert_less_equal` function interfaces.": "このページでは`assert_less`と`assert_less_equal`関数の各インターフェイスについて説明します。",  # noqa
    ##################################################
    "## What interfaces are these?": "## 各インターフェイスの概要",
    ##################################################
    "The `assert_less` function interface asserts a specified first value is less than a specified second value.": "`assert_less`関数のインターフェイスは1つ目に指定された値が2つ目の値よりも小さいことをチェックします。",  # noqa
    ##################################################
    "Similarly, the `assert_less_equal` function interface asserts a specified first value is less than or equal to a specified second value.": "似たような形で、`assert_less_equal`関数では最初に指定された値が2つ目に指定された値よりも小さいかもしくは同値なことをチェックします。",  # noqa
    ##################################################
    "## See also": "## 関連資料",
    ##################################################
    "- [JavaScript assertion interface basic behavior](assertion_basic_behavior.md)": "- [JavaScriptの各アサーションのインターフェイスの基本的な挙動](jp_assertion_basic_behavior.md)",  # noqa
    ##################################################
    "## Basic usage": "## 基本的な使い方",
    ##################################################
    "The `assert_less` and `assert_less_equal` interfaces require the `left` and `right` arguments.": "`assert_less`と`assert_less_equal`のインターフェイスは`left`引数と`right`引数の指定を必要とします。",  # noqa
    ##################################################
    "These arguments only accept numeric values, such as the Python built-in `int`, `float`, apysc `Int`, or `Number` value.": "これらの引数はPythonビルトインの`int`や`float`、apyscの`Int`や`Number`などの数値の値のみ受け付けます。",  # noqa
    ##################################################
    "The `msg` argument is optional.": "`msg`引数は省略可です。",
    ##################################################
    "This interface displays a specified `msg` (message) argument to the browser console when an assertion fails.": "このインターフェイスはアサーションが失敗した際に`msg`（message）引数の値をブラウザのコンソール上に表示します。",  # noqa
    ##################################################
    '```py\n# runnable\nimport apysc as ap\n\nstage: ap.Stage = ap.Stage(\n    stage_width=0, stage_height=0, background_color="#333", stage_elem_id="stage"\n)\nint_val_1: ap.Int = ap.Int(10)\nint_val_2: ap.Int = ap.Int(9)\nap.assert_less(left=int_val_1, right=int_val_2, msg="Assertion failed")\n\nap.assert_less_equal(left=int_val_1, right=10, msg="Assertion failed")\n\nap.save_overall_html(dest_dir_path="assert_less_and_less_equal_basic_usage_1/")\n```': '```py\n# runnable\nimport apysc as ap\n\nstage: ap.Stage = ap.Stage(\n    stage_width=0, stage_height=0, background_color="#333", stage_elem_id="stage"\n)\nint_val_1: ap.Int = ap.Int(10)\nint_val_2: ap.Int = ap.Int(9)\nap.assert_less(left=int_val_1, right=int_val_2, msg="Assertion failed")\n\nap.assert_less_equal(left=int_val_1, right=10, msg="Assertion failed")\n\nap.save_overall_html(dest_dir_path="assert_less_and_less_equal_basic_usage_1/")\n```',  # noqa
    ##################################################
    "The following example fails an assertion and displays the `Assertion failed` message on the browser console:": "`以下の例ではアサーションが失敗し、`Assertion failed`というメッセージがブラウザ上のコンソールに表示されます:",  # noqa
    ##################################################
    '```py\n# runnable\nimport apysc as ap\n\nstage: ap.Stage = ap.Stage(\n    stage_width=0, stage_height=0, background_color="#333", stage_elem_id="stage"\n)\nint_val_1: ap.Int = ap.Int(9)\nint_val_2: ap.Int = ap.Int(9)\nap.assert_less(left=int_val_1, right=int_val_2, msg="Assertion failed")\n\nap.save_overall_html(dest_dir_path="assert_less_and_less_equal_basic_usage_2/")\n```': '```py\n# runnable\nimport apysc as ap\n\nstage: ap.Stage = ap.Stage(\n    stage_width=0, stage_height=0, background_color="#333", stage_elem_id="stage"\n)\nint_val_1: ap.Int = ap.Int(9)\nint_val_2: ap.Int = ap.Int(9)\nap.assert_less(left=int_val_1, right=int_val_2, msg="Assertion failed")\n\nap.save_overall_html(dest_dir_path="assert_less_and_less_equal_basic_usage_2/")\n```',  # noqa
    ##################################################
    "## assert_less API": "## assert_less のAPI",
    ##################################################
    '<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>': '<span class="inconspicuous-txt">特記事項: このAPIドキュメントはドキュメントビルド用のスクリプトによって自動で生成・同期されています。そのためもしかしたらこの節の内容は前節までの内容と重複している場合があります。</span>',  # noqa
    ##################################################
    "**[Interface summary]**": "**[インターフェイス概要]**",
    ##################################################
    "JavaScript assertion interface for the less than condition.<hr>": "JavaScriptの未満条件のアサーションのインターフェイスです。<hr>",  # noqa
    ##################################################
    "**[Parameters]**": "**[引数]**",
    ##################################################
    "- `left`: Union[int, float, Int, Number]": "- `left`: Union[int, float, Int, Number]",  # noqa
    ##################################################
    "  - Left-side (less) value to compare.": "  - 比較用の左辺側の値（小さい側の値）。",
    ##################################################
    "- `right`: Union[int, float, Int, Number]": "- `right`: Union[int, float, Int, Number]",  # noqa
    ##################################################
    "  - Right-side (greater) value to compare.": "  - 比較用の右辺側の値（大きい側の値）。",
    ##################################################
    "- `msg`: str, optional": "- `msg`: str, optional",
    ##################################################
    "  - Message to display when assertion failed.": "  - チェックに失敗した際に表示するメッセージ。",
    ##################################################
    "<hr>": "<hr>",
    ##################################################
    "**[Examples]**": "**[コードサンプル]**",
    ##################################################
    "```py\n>>> import apysc as ap\n>>> int_val_1: ap.Int = ap.Int(9)\n>>> int_val_2: ap.Int = ap.Int(10)\n>>> ap.assert_greater_equal(left=int_val_1, right=int_val_2)\n```": "```py\n>>> import apysc as ap\n>>> int_val_1: ap.Int = ap.Int(9)\n>>> int_val_2: ap.Int = ap.Int(10)\n>>> ap.assert_greater_equal(left=int_val_1, right=int_val_2)\n```",  # noqa
    ##################################################
    "## assert_less_equal API": "## assert_less_equal のAPI",
    ##################################################
    '<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>': '<span class="inconspicuous-txt">特記事項: このAPIドキュメントはドキュメントビルド用のスクリプトによって自動で生成・同期されています。そのためもしかしたらこの節の内容は前節までの内容と重複している場合があります。</span>',  # noqa
    ##################################################
    "**[Interface summary]**": "**[インターフェイス概要]**",
    ##################################################
    "JavaScript assertion interface for the less than or equal to condition.<hr>": "JavaScriptの以下条件のアサーションのインターフェイスです。<hr>",  # noqa
    ##################################################
    "**[Parameters]**": "**[引数]**",
    ##################################################
    "- `left`: Union[int, float, Int, Number]": "- `left`: Union[int, float, Int, Number]",  # noqa
    ##################################################
    "  - Left-side (less) value to compare.": "  - 比較用の左辺側の値（小さい側の値）。",
    ##################################################
    "- `right`: Union[int, float, Int, Number]": "- `right`: Union[int, float, Int, Number]",  # noqa
    ##################################################
    "  - Right-side (greater) value to compare.": "  - 比較用の右辺側の値（大きい側の値）。",
    ##################################################
    "- `msg`: str, optional": "- `msg`: str, optional",
    ##################################################
    "  - Message to display when assertion failed.": "  - チェックに失敗した際に表示するメッセージ。",
    ##################################################
    "<hr>": "<hr>",
    ##################################################
    "**[Examples]**": "**[コードサンプル]**",
    ##################################################
    "```py\n>>> import apysc as ap\n>>> int_val_1: ap.Int = ap.Int(9)\n>>> int_val_2: ap.Int = ap.Int(10)\n>>> ap.assert_greater_equal(left=int_val_1, right=int_val_2)\n>>> int_val_3: ap.Int = ap.Int(9)\n>>> ap.assert_greater_equal(left=int_val_1, right=int_val_3)\n```": "```py\n>>> import apysc as ap\n>>> int_val_1: ap.Int = ap.Int(9)\n>>> int_val_2: ap.Int = ap.Int(10)\n>>> ap.assert_greater_equal(left=int_val_1, right=int_val_2)\n>>> int_val_3: ap.Int = ap.Int(9)\n>>> ap.assert_greater_equal(left=int_val_1, right=int_val_3)\n```",  # noqa
}
