"""This module is for the translation mapping data of the
following document:

Document file: assert_arrays_equal_and_arrays_not_equal.md
Language: jp
"""

from typing import Dict

MAPPING: Dict[str, str] = {
    ##################################################
    "# assert_arrays_equal and assert_arrays_not_equal interfaces": "# assert_arrays_equal と assert_arrays_not_equal インターフェイス",  # noqa
    ##################################################
    "This page explains the `assert_arrays_equal` and `assert_arrays_not_equal` function interfaces.": "このページでは`assert_arrays_equal`と`assert_arrays_not_equal`関数の各インターフェイスについて説明します。",  # noqa
    ##################################################
    "## What interfaces are these?": "## 各インターフェイスの概要",
    ##################################################
    "The `assert_arrays_equal` function interface asserts that the two arrays are equal. Conversely, the `assert_arrays_not_equal` function interface asserts that the two arrays are not equal.": "`assert_arrays_equal`関数のインターフェイスは2つの配列の値が一致していることをチェックします。逆に`assert_arrays_not_equal`関数は2つの配列の値が一致していないことをチェックします。",  # noqa
    ##################################################
    "## See also": "## 関連資料",
    ##################################################
    "- [JavaScript assertion interface basic behavior](assertion_basic_behavior.md)": "- [JavaScriptの各アサーションのインターフェイスの基本的な挙動](jp_assertion_basic_behavior.md)",  # noqa
    ##################################################
    "## Basic usage": "## 基本的な使い方",
    ##################################################
    "Both of the `assert_arrays_equal` and `assert_arrays_not_equal` interfaces require the `left` and `right` arguments. The `msg` argument is optional.": "`assert_arrays_equal`と`assert_arrays_not_equal`のインターフェイスは共に`left`と`right`という2つの引数を必要とします。`msg`引数は省略可です。",  # noqa
    ##################################################
    "The arguments accept a Python built-in `list` value and `Array` value.": "引数にはPythonビルトインの`list`の値もしくはapyscの`Array`の値を指定することができます。",  # noqa
    ##################################################
    "The following example (`assert_arrays_equal` and values are equal) passes:": "以下のコードで例では`assert_arrays_equal`関数を使って値が一致していることを確認しています:",  # noqa
    ##################################################
    '```py\n# runnable\nimport apysc as ap\n\nstage: ap.Stage = ap.Stage(\n    stage_width=0, stage_height=0, background_color="#333", stage_elem_id="stage"\n)\n\narr_1: ap.Array = ap.Array([1, 2, 3])\nap.assert_arrays_equal(left=[1, 2, 3], right=arr_1, msg="Values are not equal!")\n\nap.save_overall_html(dest_dir_path="assert_arrays_equal_basic_usage_1/")\n```': '```py\n# runnable\nimport apysc as ap\n\nstage: ap.Stage = ap.Stage(\n    stage_width=0, stage_height=0, background_color="#333", stage_elem_id="stage"\n)\n\narr_1: ap.Array = ap.Array([1, 2, 3])\nap.assert_arrays_equal(left=[1, 2, 3], right=arr_1, msg="Values are not equal!")\n\nap.save_overall_html(dest_dir_path="assert_arrays_equal_basic_usage_1/")\n```',  # noqa
    ##################################################
    "```\n[assert_arrays_equal]\nLeft value: [1, 2, 3] right value: arr_2\n```": "```\n[assert_arrays_equal]\nLeft value: [1, 2, 3] right value: arr_2\n```",  # noqa
    ##################################################
    "The following example (`assert_arrays_equal` and values are not equal) fails:": "以下のコード例では`assert_arrays_equal`関数を使って値が一致しておらずチェックが失敗していることを確認しています。",  # noqa
    ##################################################
    '```py\n# runnable\nimport apysc as ap\n\nstage: ap.Stage = ap.Stage(\n    stage_width=0, stage_height=0, background_color="#333", stage_elem_id="stage"\n)\n\narr_1: ap.Array = ap.Array([1, 2, 3])\nap.assert_arrays_equal(left=[1, 2], right=arr_1, msg="Values are not equal!")\n\nap.save_overall_html(dest_dir_path="assert_arrays_equal_basic_usage_2/")\n```': '```py\n# runnable\nimport apysc as ap\n\nstage: ap.Stage = ap.Stage(\n    stage_width=0, stage_height=0, background_color="#333", stage_elem_id="stage"\n)\n\narr_1: ap.Array = ap.Array([1, 2, 3])\nap.assert_arrays_equal(left=[1, 2], right=arr_1, msg="Values are not equal!")\n\nap.save_overall_html(dest_dir_path="assert_arrays_equal_basic_usage_2/")\n```',  # noqa
    ##################################################
    "```\n[assert_arrays_equal]\nLeft value: [1, 2] right value: arr_2\n...\nAssertion failed: Values are not equal!\n```": "```\n[assert_arrays_equal]\nLeft value: [1, 2] right value: arr_2\n...\nAssertion failed: Values are not equal!\n```",  # noqa
    ##################################################
    "The following example (`assert_arrays_not_equal` and values are not equal) passes:": "以下のコード例では`assert_arrays_not_equal`関数を使って値が一致していないためチェックを通っていることを確認しています:",  # noqa
    ##################################################
    '```py\n# runnable\nimport apysc as ap\n\nstage: ap.Stage = ap.Stage(\n    stage_width=0, stage_height=0, background_color="#333", stage_elem_id="stage"\n)\n\narr_1: ap.Array = ap.Array([1, 2, 3])\nap.assert_arrays_not_equal(left=[1, 2], right=arr_1, msg="Values are equal!")\n\nap.save_overall_html(dest_dir_path="assert_arrays_not_equal_basic_usage_1/")\n```': '```py\n# runnable\nimport apysc as ap\n\nstage: ap.Stage = ap.Stage(\n    stage_width=0, stage_height=0, background_color="#333", stage_elem_id="stage"\n)\n\narr_1: ap.Array = ap.Array([1, 2, 3])\nap.assert_arrays_not_equal(left=[1, 2], right=arr_1, msg="Values are equal!")\n\nap.save_overall_html(dest_dir_path="assert_arrays_not_equal_basic_usage_1/")\n```',  # noqa
    ##################################################
    "## Notes for the assert_equal and assert_not_equal interfaces": "## assert_equal と assert_not_equal の各インターフェイスにおける特記事項",  # noqa
    ##################################################
    "If an `Array` value is specified to the `assert_equal` or `assert_not_equal` interface's values, then the `assert_arrays_equal` or `assert_arrays_not_equal` interfaces will be called instead of the `assert_equal` or `assert_not_equal` interfaces automatically.": "もしも`assert_equal`もしくは`assert_not_equal`のインターフェイスに`Array`の値が指定された場合、自動的にそれらのインターフェイスの代わりに`assert_arrays_equal`と`assert_arrays_not_equal`のインターフェイスが使用されます。",  # noqa
    ##################################################
    '```py\n# runnable\nimport apysc as ap\n\nstage: ap.Stage = ap.Stage(\n    stage_width=0, stage_height=0, background_color="#333", stage_elem_id="stage"\n)\n\narr_1: ap.Array = ap.Array([1, 2, 3, 4, 5])\nap.assert_equal(left=[1, 2, 3, 4, 5], right=arr_1, msg="Values are equal!")\n\nap.save_overall_html(dest_dir_path="assert_arrays_equal_notes_for_the_assert_equal/")\n```': '```py\n# runnable\nimport apysc as ap\n\nstage: ap.Stage = ap.Stage(\n    stage_width=0, stage_height=0, background_color="#333", stage_elem_id="stage"\n)\n\narr_1: ap.Array = ap.Array([1, 2, 3, 4, 5])\nap.assert_equal(left=[1, 2, 3, 4, 5], right=arr_1, msg="Values are equal!")\n\nap.save_overall_html(dest_dir_path="assert_arrays_equal_notes_for_the_assert_equal/")\n```',  # noqa
    ##################################################
    "```\n[assert_arrays_equal]\nLeft value: [1, 2, 3, 4, 5] right value: arr_2\n```": "```\n[assert_arrays_equal]\nLeft value: [1, 2, 3, 4, 5] right value: arr_2\n```",  # noqa
    ##################################################
    "## assert_arrays_equal API": "## assert_arrays_equal API",
    ##################################################
    '<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>': '<span class="inconspicuous-txt">特記事項: このAPIドキュメントはドキュメントビルド用のスクリプトによって自動で生成・同期されています。そのためもしかしたらこの節の内容は前節までの内容と重複している場合があります。</span>',  # noqa
    ##################################################
    "**[Interface summary]**": "**[インターフェイス概要]**",
    ##################################################
    "JavaScript assertion interface for the Array values equal condition.<hr>": "配列の値の等値条件のためのJavaScript上のアサーションのインターフェイスです。<hr>",  # noqa
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
    "- `outer_frames_index_adjustment`: int, optional": "- `outer_frames_index_adjustment`: int, optional",  # noqa
    ##################################################
    "  - The trace's outer frames index adjustment setting. This function uses this argument to adjust the caller's information. Also, this function only uses this argument in internal logic.": "  - trace関数の関数外の参照するフレームのインデックスの調整値です。この引数は呼び出し元の情報の位置を調整するのに使用されます。また、この引数は内部のロジックでのみ使用されるため通常は設定する必要はありません。",  # noqa
    ##################################################
    "<hr>": "<hr>",
    ##################################################
    "**[Notes]**": "**[特記事項]**",
    ##################################################
    "This interface is used instead of assert_equal for Array class comparison (JavaScript can not compare arrays directly, like a Python, for example, `[1, 2] === [1, 2]` becomes false).<hr>": "このインターフェイスは`Array`クラスの値の比較時には`assert_equal`インターフェイスの代わりに使用されます（JavaScript上ではPythonのリストのように直接配列の比較が行えないため代わりにこのインターフェイスが使用されます）。<hr>",  # noqa
    ##################################################
    "**[Examples]**": "**[コードサンプル]**",
    ##################################################
    "```py\n>>> import apysc as ap\n>>> arr_1: ap.Array = ap.Array([1, 2, 3])\n>>> arr_2: ap.Array = ap.Array([1, 2, 3])\n>>> ap.assert_arrays_equal(arr_1, arr_2)\n```": "```py\n>>> import apysc as ap\n>>> arr_1: ap.Array = ap.Array([1, 2, 3])\n>>> arr_2: ap.Array = ap.Array([1, 2, 3])\n>>> ap.assert_arrays_equal(arr_1, arr_2)\n```",  # noqa
    ##################################################
    "## assert_arrays_not_equal API": "## assert_arrays_not_equal API",
    ##################################################
    '<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>': '<span class="inconspicuous-txt">特記事項: このAPIドキュメントはドキュメントビルド用のスクリプトによって自動で生成・同期されています。そのためもしかしたらこの節の内容は前節までの内容と重複している場合があります。</span>',  # noqa
    ##################################################
    "**[Interface summary]**": "**[インターフェイス概要]**",
    ##################################################
    "JavaScript assertion interface for the Array values not equal condition.<hr>": "配列の値の非等値条件のためのJavaScript上のアサーションのインターフェイスです。<hr>",  # noqa
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
    "- `outer_frames_index_adjustment`: int, optional": "- `outer_frames_index_adjustment`: int, optional",  # noqa
    ##################################################
    "  - The trace's outer frames index adjustment setting. This function uses this argument to adjust the caller's information. Also, this function only uses this argument in internal logic.": "  - trace関数の関数外の参照するフレームのインデックスの調整値です。この引数は呼び出し元の情報の位置を調整するのに使用されます。また、この引数は内部のロジックでのみ使用されるため通常は設定する必要はありません。",  # noqa
    ##################################################
    "<hr>": "<hr>",
    ##################################################
    "**[Notes]**": "**[特記事項]**",
    ##################################################
    "This interface is used instead of assert_not_equal for Array class comparison (JavaScript can not compare arrays directly, like a Python, for example, `[1, 2] === [1, 2]` becomes false).<hr>": "このインターフェイスは`Array`クラスの値の比較時には`assert_not_equal`インターフェイスの代わりに使用されます（JavaScript上ではPythonのリストのように直接配列の比較が行えないため代わりにこのインターフェイスが使用されます）。<hr>",  # noqa
    ##################################################
    "**[Examples]**": "**[コードサンプル]**",
    ##################################################
    "```py\n>>> import apysc as ap\n>>> arr_1: ap.Array = ap.Array([1, 2, 3])\n>>> arr_2: ap.Array = ap.Array([4, 5, 6])\n>>> ap.assert_arrays_not_equal(arr_1, arr_2)\n```": "```py\n>>> import apysc as ap\n>>> arr_1: ap.Array = ap.Array([1, 2, 3])\n>>> arr_2: ap.Array = ap.Array([4, 5, 6])\n>>> ap.assert_arrays_not_equal(arr_1, arr_2)\n```",  # noqa
}
