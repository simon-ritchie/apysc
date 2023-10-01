"""This module is for the translation mapping data of the
following document:

Document file: assert_greater_and_greater_equal.md
Language: jp
"""

from typing import Dict

MAPPING: Dict[str, str] = {
    ##################################################
    "# assert_greater and assert_greater_equal interfaces": "# assert_greater と assert_greater_equal の各インターフェイス",  # noqa
    ##################################################
    "This page explains the `assert_greater` and `assert_greater_equal` function interfaces.": "このページでは`assert_greater`と`assert_greater_equal`関数の各インターフェイスについて説明します。",  # noqa
    ##################################################
    "## What interfaces are these?": "## 各インターフェイスの概要",
    ##################################################
    "The `assert_greater` function interface asserts a specified first value is greater than a specified second value.": "`assert_greater`関数のインターフェイスでは1つ目に指定された値が2つ目に指定された値よりも大きいことをチェックします。",  # noqa
    ##################################################
    "Similarly, the `assert_greater_equal` function interface asserts a specified first value is greater than or equal to a specified second value.": "似たような形で、`assert_greater_equal`関数では最初に指定された値が2つ目の値よりも大きいかもしくは同値なことをチェックします。",  # noqa
    ##################################################
    "## See also": "## 関連資料",
    ##################################################
    "- [JavaScript assertion interface basic behavior](assertion_basic_behavior.md)": "- [JavaScriptの各アサーションのインターフェイスの基本的な挙動](jp_assertion_basic_behavior.md)",  # noqa
    ##################################################
    "## Basic usage": "## 基本的な使い方",
    ##################################################
    "The `assert_greater` and `assert_greater_equal` interfaces require the `left` and `right` arguments.": "`assert_greater`と`assert_greater_equal`インターフェイスは`left`と`right`の引数を必要とします。",  # noqa
    ##################################################
    "These arguments only accept numeric values, such as the Python built-in `int`, `float`, apysc `Int`, or `Number` value.": "これらの引数はPythonビルトインの`int`や`float`、apyscの`Int`や`Number`などの数値の値のみ受け付けます。",  # noqa
    ##################################################
    "The `msg` argument is optional.": "`msg`引数は省略可です。",
    ##################################################
    "This interface displays a specified `msg` (message) argument to the browser console when an assertion fails.": "このインターフェイスはアサーションが失敗した際に`msg`（message）引数の値をブラウザのコンソール上に表示します。",  # noqa
    ##################################################
    '```py\n# runnable\nimport apysc as ap\n\nstage: ap.Stage = ap.Stage(\n    stage_width=0,\n    stage_height=0,\n    background_color=ap.Color("#333"),\n    stage_elem_id="stage",\n)\nint_val_1: ap.Int = ap.Int(10)\nint_val_2: ap.Int = ap.Int(9)\nap.assert_greater(left=int_val_1, right=int_val_2, msg="Assertion failed")\n\nint_val_3: ap.Int = ap.Int(10)\nap.assert_greater_equal(left=int_val_1, right=int_val_3, msg="Assertion failed")\n\nap.save_overall_html(dest_dir_path="assert_greater_and_greater_equal_basic_usage_1/")\n```': '```py\n# runnable\nimport apysc as ap\n\nstage: ap.Stage = ap.Stage(\n    stage_width=0,\n    stage_height=0,\n    background_color=ap.Color("#333"),\n    stage_elem_id="stage",\n)\nint_val_1: ap.Int = ap.Int(10)\nint_val_2: ap.Int = ap.Int(9)\nap.assert_greater(left=int_val_1, right=int_val_2, msg="Assertion failed")\n\nint_val_3: ap.Int = ap.Int(10)\nap.assert_greater_equal(left=int_val_1, right=int_val_3, msg="Assertion failed")\n\nap.save_overall_html(dest_dir_path="assert_greater_and_greater_equal_basic_usage_1/")\n```',  # noqa
    ##################################################
    "The following example fails an assertion and displays the `Assertion failed` message on the browser console:": "`以下の例ではアサーションが失敗し、`Assertion failed`というメッセージがブラウザ上のコンソールに表示されます:",  # noqa
    ##################################################
    '```py\n# runnable\nimport apysc as ap\n\nstage: ap.Stage = ap.Stage(\n    stage_width=0,\n    stage_height=0,\n    background_color=ap.Color("#333"),\n    stage_elem_id="stage",\n)\nint_val_1: ap.Int = ap.Int(9)\nint_val_2: ap.Int = ap.Int(10)\nap.assert_greater(left=int_val_1, right=int_val_2, msg="Assertion failed")\n\nap.save_overall_html(dest_dir_path="assert_greater_and_greater_equal_basic_usage_2/")\n```': '```py\n# runnable\nimport apysc as ap\n\nstage: ap.Stage = ap.Stage(\n    stage_width=0,\n    stage_height=0,\n    background_color=ap.Color("#333"),\n    stage_elem_id="stage",\n)\nint_val_1: ap.Int = ap.Int(9)\nint_val_2: ap.Int = ap.Int(10)\nap.assert_greater(left=int_val_1, right=int_val_2, msg="Assertion failed")\n\nap.save_overall_html(dest_dir_path="assert_greater_and_greater_equal_basic_usage_2/")\n```',  # noqa
    ##################################################
    "## assert_greater API": "## assert_greater のAPI",
    ##################################################
    '<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>': '<span class="inconspicuous-txt">特記事項: このAPIドキュメントはドキュメントビルド用のスクリプトによって自動で生成・同期されています。そのためもしかしたらこの節の内容は前節までの内容と重複している場合があります。</span>',  # noqa
    ##################################################
    "**[Interface summary]**": "**[インターフェイス概要]**",
    ##################################################
    "JavaScript assertion interface for the greater than condition.<hr>": "JavaScriptの超過条件のアサーションのためのインターフェイスです。<hr>",  # noqa
    ##################################################
    "**[Parameters]**": "**[引数]**",
    ##################################################
    "- `left`: Union[int, float, Int, Number]": "- `left`: Union[int, float, Int, Number]",  # noqa
    ##################################################
    "  - Left-side (greater) value to compare.": "  - 比較用の左辺の値（大きい側の値）。",
    ##################################################
    "- `right`: Union[int, float, Int, Number]": "- `right`: Union[int, float, Int, Number]",  # noqa
    ##################################################
    "  - Right-side (less) value to compare.": "  - 比較用の右辺の値（小さい側の値）。",
    ##################################################
    "- `msg`: str, optional": "- `msg`: str, optional",
    ##################################################
    "  - Message to display when assertion failed.": "  - チェックに失敗した際に表示するメッセージ。",
    ##################################################
    "<hr>": "<hr>",
    ##################################################
    "**[Examples]**": "**[コードサンプル]**",
    ##################################################
    "```py\n>>> import apysc as ap\n>>> int_val_1: ap.Int = ap.Int(10)\n>>> int_val_2: ap.Int = ap.Int(9)\n>>> ap.assert_greater(left=int_val_1, right=int_val_2)\n```": "```py\n>>> import apysc as ap\n>>> int_val_1: ap.Int = ap.Int(10)\n>>> int_val_2: ap.Int = ap.Int(9)\n>>> ap.assert_greater(left=int_val_1, right=int_val_2)\n```",  # noqa
    ##################################################
    "## assert_greater_equal API": "## assert_greater_equal のAPI",
    ##################################################
    '<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>': '<span class="inconspicuous-txt">特記事項: このAPIドキュメントはドキュメントビルド用のスクリプトによって自動で生成・同期されています。そのためもしかしたらこの節の内容は前節までの内容と重複している場合があります。</span>',  # noqa
    ##################################################
    "**[Interface summary]**": "**[インターフェイス概要]**",
    ##################################################
    "JavaScript assertion interface for the greater than or equal to condition.<hr>": "JavaScriptの以上の条件のアサーションのためのインターフェイスです。<hr>",  # noqa
    ##################################################
    "**[Parameters]**": "**[引数]**",
    ##################################################
    "- `left`: Union[int, float, Int, Number]": "- `left`: Union[int, float, Int, Number]",  # noqa
    ##################################################
    "  - Left-side (greater) value to compare.": "  - 比較用の左辺の値（大きい側の値）。",
    ##################################################
    "- `right`: Union[int, float, Int, Number]": "- `right`: Union[int, float, Int, Number]",  # noqa
    ##################################################
    "  - Right-side (less) value to compare.": "  - 比較用の右辺の値（小さい側の値）。",
    ##################################################
    "- `msg`: str, optional": "- `msg`: str, optional",
    ##################################################
    "  - Message to display when assertion failed.": "  - チェックに失敗した際に表示するメッセージ。",
    ##################################################
    "<hr>": "<hr>",
    ##################################################
    "**[Examples]**": "**[コードサンプル]**",
    ##################################################
    "```py\n>>> import apysc as ap\n>>> int_val_1: ap.Int = ap.Int(10)\n>>> int_val_2: ap.Int = ap.Int(9)\n>>> ap.assert_greater_equal(left=int_val_1, right=int_val_2)\n>>> int_val_3: ap.Int = ap.Int(10)\n>>> ap.assert_greater_equal(left=int_val_1, right=int_val_3)\n```": "```py\n>>> import apysc as ap\n>>> int_val_1: ap.Int = ap.Int(10)\n>>> int_val_2: ap.Int = ap.Int(9)\n>>> ap.assert_greater_equal(left=int_val_1, right=int_val_2)\n>>> int_val_3: ap.Int = ap.Int(10)\n>>> ap.assert_greater_equal(left=int_val_1, right=int_val_3)\n```",  # noqa
}
