"""This module is for the translation mapping data of the
following document:

Document file: range.md
Language: jp
"""

from typing import Dict

MAPPING: Dict[str, str] = {
    ##################################################
    "# range function": "# range 関数",
    ##################################################
    "This page explains the `range` function.": "このページでは`range`関数について説明していきます。",
    ##################################################
    "## What function is this?": "## 関数概要",
    ##################################################
    "The `range` function creates a range array of `ap.Int` (e.g., `[0, 1, 2, 3, 4, 5]`).": "`range`関数は`ap.Int`型の指定の範囲の配列を作成します（例 : `[0, 1, 2, 3, 4, 5]`）。",  # noqa
    ##################################################
    "## Basic usage": "## 基本的な使い方",
    ##################################################
    "If you specify only one argument, a range array becomes 0 to argument value -1.": "もしも引数を1つだけ指定した場合、範囲の配列は0から指定された引数の値を-1した範囲になります。",  # noqa
    ##################################################
    '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    stage_width=0,\n    stage_height=0,\n    background_color=ap.Color("#333"),\n    stage_elem_id="stage",\n)\nrange_arr: ap.Array[ap.Int] = ap.range(5)\nap.assert_equal(range_arr, [0, 1, 2, 3, 4])\nap.save_overall_html(dest_dir_path="range_basics_usage_1/")\n```': '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    stage_width=0,\n    stage_height=0,\n    background_color=ap.Color("#333"),\n    stage_elem_id="stage",\n)\nrange_arr: ap.Array[ap.Int] = ap.range(5)\nap.assert_equal(range_arr, [0, 1, 2, 3, 4])\nap.save_overall_html(dest_dir_path="range_basics_usage_1/")\n```',  # noqa
    ##################################################
    "Also, if you specify two arguments, a range array becomes a first argument value to a second argument value -1.": "また、もし2つの引数を指定した場合には範囲の配列は最初の引数の値～2つ目の引数の値を-1した範囲になります。",  # noqa
    ##################################################
    '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    stage_width=0,\n    stage_height=0,\n    background_color=ap.Color("#333"),\n    stage_elem_id="stage",\n)\nrange_arr: ap.Array[ap.Int] = ap.range(2, 4)\nap.assert_equal(range_arr, [2, 3])\nap.save_overall_html(dest_dir_path="range_basics_usage_2/")\n```': '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    stage_width=0,\n    stage_height=0,\n    background_color=ap.Color("#333"),\n    stage_elem_id="stage",\n)\nrange_arr: ap.Array[ap.Int] = ap.range(2, 4)\nap.assert_equal(range_arr, [2, 3])\nap.save_overall_html(dest_dir_path="range_basics_usage_2/")\n```',  # noqa
    ##################################################
    "If three arguments, a range array becomes a first argument value to a second argument value, and a step between each value becomes a third argument value.": "もし3つ引数を指定した場合には範囲の配列は最初の引数の値～2つ目の引数の値を-1した範囲となり、各値は3つ目に指定された引数の値のステップで設定されます。",  # noqa
    ##################################################
    '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    stage_width=0,\n    stage_height=0,\n    background_color=ap.Color("#333"),\n    stage_elem_id="stage",\n)\nrange_arr: ap.Array[ap.Int] = ap.range(2, 10, 2)\nap.assert_equal(range_arr, [2, 4, 6, 8])\nap.save_overall_html(dest_dir_path="range_basics_usage_3/")\n```': '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    stage_width=0,\n    stage_height=0,\n    background_color=ap.Color("#333"),\n    stage_elem_id="stage",\n)\nrange_arr: ap.Array[ap.Int] = ap.range(2, 10, 2)\nap.assert_equal(range_arr, [2, 4, 6, 8])\nap.save_overall_html(dest_dir_path="range_basics_usage_3/")\n```',  # noqa
    ##################################################
    "## range function API": "## range 関数のAPI",
    ##################################################
    '<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>': '<span class="inconspicuous-txt">特記事項: このAPIドキュメントはドキュメントビルド用のスクリプトによって自動で生成・同期されています。そのためもしかしたらこの節の内容は前節までの内容と重複している場合があります。</span>',  # noqa
    ##################################################
    "**[Interface summary]**": "**[インターフェイス概要]**",
    ##################################################
    "Create a range array of integers.<hr>": "整数の指定範囲の配列を生成します。<hr>",
    ##################################################
    "**[Returns]**": "**[返却値]**",
    ##################################################
    "- `arr`: Array[Int]": "- `arr`: Array[Int]",
    ##################################################
    "  - A created array.": "  - 生成された配列。",
    ##################################################
    "<hr>": "<hr>",
    ##################################################
    "**[Examples]**": "**[コードサンプル]**",
    ##################################################
    "```py\n>>> import apysc as ap\n>>> range_arr: ap.Array[ap.Int] = ap.range(5)\n>>> ap.assert_equal(range_arr, [0, 1, 2, 3, 4])\n>>> range_arr = ap.range(2, 4)\n>>> ap.assert_equal(range_arr, [2, 3])\n>>> range_arr = ap.range(2, 10, 2)\n>>> ap.assert_equal(range_arr, [2, 4, 6, 8])\n```": "```py\n>>> import apysc as ap\n>>> range_arr: ap.Array[ap.Int] = ap.range(5)\n>>> ap.assert_equal(range_arr, [0, 1, 2, 3, 4])\n>>> range_arr = ap.range(2, 4)\n>>> ap.assert_equal(range_arr, [2, 3])\n>>> range_arr = ap.range(2, 10, 2)\n>>> ap.assert_equal(range_arr, [2, 4, 6, 8])\n```",  # noqa
}
