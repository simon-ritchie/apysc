"""This module is for the translation mapping data of the
following document:

Document file: assert_equal_and_not_equal.md
Language: jp
"""

from typing import Dict

MAPPING: Dict[str, str] = {
    ##################################################
    "# assert_equal and assert_not_equal interfaces": "# assert_equal と assert_not_equal インターフェイス",  # noqa
    ##################################################
    "This page explains the `assert_equal` and `assert_not_equal` function interfaces.": "このページでは`assert_equal`と`assert_not_equal`関数の各インターフェイスについて説明します。",  # noqa
    ##################################################
    "## What interfaces are these?": "## 各インターフェイスの概要",
    ##################################################
    "The `assert_equal` function interface asserts that two JavaScript values are equal. The `assert_not_equal` function interface asserts that the two JavaScript values are not equal.": "`assert_equal`関数のインターフェイスは2つのJavaScript上の値が等値かどうかをチェックします。逆に`assert_not_equal`関数のインターフェイスは2つの値が等値ではないことをチェックします。",  # noqa
    ##################################################
    "## See also": "## 関連資料",
    ##################################################
    "- [JavaScript assertion interface basic behavior](assertion_basic_behavior.md)": "- [JavaScriptの各アサーションのインターフェイスの基本的な挙動](jp_assertion_basic_behavior.md)",  # noqa
    ##################################################
    "## Basic usage": "## 基本的な使い方",
    ##################################################
    "The `assert_equal` and `assert_not_equal` interfaces requires the `left` and `right` arguments. The `msg` argument is optional.": "`assert_equal`と`assert_not_equal`インターフェイスは`left`と`right`の各引数の指定を必要とします。`msg`引数は省略可です。",  # noqa
    ##################################################
    "If the `left` value and `right` values are not the same, the `assert_equal` assertion fails and display an error message on the browser console:": "もしも`left`引数の値と`right`引数の値が一致していない場合、`assert_equal`関数によるチェックは失敗しブラウザ上のコンソールにエラーメッセージが表示されます。",  # noqa
    ##################################################
    '```py\n# runnable\nimport apysc as ap\n\nstage: ap.Stage = ap.Stage(\n    stage_width=0, stage_height=0, background_color="#333", stage_elem_id="stage"\n)\n\nint_1: ap.Int = ap.Int(10)\nap.assert_equal(left=11, right=int_1, msg="Values are not equal!")\n\nap.save_overall_html(dest_dir_path="assert_equal_basic_usage/")\n```': '```py\n# runnable\nimport apysc as ap\n\nstage: ap.Stage = ap.Stage(\n    stage_width=0, stage_height=0, background_color="#333", stage_elem_id="stage"\n)\n\nint_1: ap.Int = ap.Int(10)\nap.assert_equal(left=11, right=int_1, msg="Values are not equal!")\n\nap.save_overall_html(dest_dir_path="assert_equal_basic_usage/")\n```',  # noqa
    ##################################################
    "```\n[assert_equal]\nLeft-side variable name: i_11\nLeft value: 11 right value: 10\n...\nAssertion failed: Values are not equal!\n```": "```\n[assert_equal]\nLeft-side variable name: i_11\nLeft value: 11 right value: 10\n...\nAssertion failed: Values are not equal!\n```",  # noqa
    ##################################################
    "The `assert_not_equal` interface has the same arguments, and if the `left` value and `right` value are the same values, an assertion fails:": "`assert_not_equal`インターフェイスも同様の引数を持っており、もし`left`引数の値が`right`引数の値と等値の場合チェック処理は失敗します:",  # noqa
    ##################################################
    '```py\n# runnable\nimport apysc as ap\n\nstage: ap.Stage = ap.Stage(\n    stage_width=0, stage_height=0, background_color="#333", stage_elem_id="stage"\n)\n\nint_1: ap.Int = ap.Int(10)\nap.assert_not_equal(left=10, right=int_1, msg="Values are equal!")\n\nap.save_overall_html(dest_dir_path="assert_not_equal_basic_usage/")\n```': '```py\n# runnable\nimport apysc as ap\n\nstage: ap.Stage = ap.Stage(\n    stage_width=0, stage_height=0, background_color="#333", stage_elem_id="stage"\n)\n\nint_1: ap.Int = ap.Int(10)\nap.assert_not_equal(left=10, right=int_1, msg="Values are equal!")\n\nap.save_overall_html(dest_dir_path="assert_not_equal_basic_usage/")\n```',  # noqa
    ##################################################
    "```\n[assert_not_equal]\nRight-side variable name: i_11\nLeft value: 10 right value: 10\n...\nAssertion failed: Values are equal!\n```": "```\n[assert_not_equal]\nRight-side variable name: i_11\nLeft value: 10 right value: 10\n...\nAssertion failed: Values are equal!\n```",  # noqa
    ##################################################
    "## assert_equal API": "## assert_equal API",
    ##################################################
    '<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>': '<span class="inconspicuous-txt">特記事項: このAPIドキュメントはドキュメントビルド用のスクリプトによって自動で生成・同期されています。そのためもしかしたらこの節の内容は前節までの内容と重複している場合があります。</span>',  # noqa
    ##################################################
    "**[Interface summary]**": "**[インターフェイス概要]**",
    ##################################################
    "JavaScript assertion interface for equal condition.<hr>": "等値条件のためのJavaScript上のアサーションのインターフェイスです。<hr>",  # noqa
    ##################################################
    "**[Parameters]**": "**[引数]**",
    ##################################################
    "- `left`: *": "- `left`: *",
    ##################################################
    "  - Left-side value to compare.": "  - 比較用の左辺の値。",
    ##################################################
    "- `right`: *": "- `right`: *",
    ##################################################
    "  - Right-side value to compare.": "  - 比較用の右辺の値。",
    ##################################################
    "- `msg`: str, optional": "- `msg`: str, optional",
    ##################################################
    "  - Message to display when assertion failed.": "  - チェックに失敗した際に表示するメッセージ。",
    ##################################################
    "<hr>": "<hr>",
    ##################################################
    "**[Notes]**": "**[特記事項]**",
    ##################################################
    " ・If specified values are types of Array (or list), then this interface calls the assert_arrays_equal function instead. ": " ・もしも引数にArrayやlistの値が指定された場合、このインターフェイスの処理の代わりにassert_arrays_equal関数が呼ばれます。",  # noqa
    ##################################################
    "<br> ・If specified values are types of Dictionary (or dict), then this interface calls the assert_dicts_equal instead.<hr>": "<br> ・もしも引数にDictionaryやdictの値が指定された場合、このインターフェイスの処理の代わりにassert_dicts_equal関数が呼ばれます。<hr>",  # noqa
    ##################################################
    "**[Examples]**": "**[コードサンプル]**",
    ##################################################
    "```py\n>>> import apysc as ap\n>>> int_1: ap.Int = ap.Int(10)\n>>> int_2: ap.Int = ap.Int(10)\n>>> ap.assert_equal(int_1, int_2)\n```": "```py\n>>> import apysc as ap\n>>> int_1: ap.Int = ap.Int(10)\n>>> int_2: ap.Int = ap.Int(10)\n>>> ap.assert_equal(int_1, int_2)\n```",  # noqa
    ##################################################
    "## assert_not_equal API": "## assert_not_equal API",
    ##################################################
    '<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>': '<span class="inconspicuous-txt">特記事項: このAPIドキュメントはドキュメントビルド用のスクリプトによって自動で生成・同期されています。そのためもしかしたらこの節の内容は前節までの内容と重複している場合があります。</span>',  # noqa
    ##################################################
    "**[Interface summary]**": "**[インターフェイス概要]**",
    ##################################################
    "JavaScript assertion interface for not equal condition.<hr>": "非等値条件のためのJavaScript上のアサーションのインターフェイスです。<hr>",  # noqa
    ##################################################
    "**[Parameters]**": "**[引数]**",
    ##################################################
    "- `left`: *": "- `left`: *",
    ##################################################
    "  - Left-side value to compare.": "  - 比較用の左辺の値。",
    ##################################################
    "- `right`: *": "- `right`: *",
    ##################################################
    "  - Right-side value to compare.": "  - 比較用の右辺の値。",
    ##################################################
    "- `msg`: str, optional": "- `msg`: str, optional",
    ##################################################
    "  - Message to display when assertion failed.": "  - チェックに失敗した際に表示するメッセージ。",
    ##################################################
    "<hr>": "<hr>",
    ##################################################
    "**[Notes]**": "**[特記事項]**",
    ##################################################
    " ・If specified values are types of Array (or list), then this interface calls the assert_arrays_not_equal function instead. ": " ・もしも引数にArrayやlistの値が指定された場合、このインターフェイスの処理の代わりにassert_arrays_not_equal関数が呼ばれます。",  # noqa
    ##################################################
    "<br> ・If specified values are types of Dictionary (or dict), this interface calls the assert_dicts_not_equal function instead.<hr>": "<br> ・もしも引数にDictionaryやdictの値が指定された場合、このインターフェイスの代わりにassert_dicts_not_equal関数が呼ばれます。<hr>",  # noqa
    ##################################################
    "**[Examples]**": "**[コードサンプル]**",
    ##################################################
    "```py\n>>> import apysc as ap\n>>> int_1: ap.Int = ap.Int(10)\n>>> int_2: ap.Int = ap.Int(11)\n>>> ap.assert_not_equal(int_1, int_2)\n```": "```py\n>>> import apysc as ap\n>>> int_1: ap.Int = ap.Int(10)\n>>> int_2: ap.Int = ap.Int(11)\n>>> ap.assert_not_equal(int_1, int_2)\n```",  # noqa
}
