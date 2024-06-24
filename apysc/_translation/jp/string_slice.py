"""This module is for the translation mapping data of the
following document:

Document file: string_slice.md
Language: jp
"""

from typing import Dict

MAPPING: Dict[str, str] = {
    ##################################################
    "# String class slice method": "# String クラスの slice メソッド",
    ##################################################
    "This page explains the `String` class `slice` method.": "このページでは`String`クラスの`slice`メソッドについて説明します。",  # noqa
    ##################################################
    "## What method is this?": "## メソッド概要",
    ##################################################
    "The `slice` method slices a string with the specified start and end indices.": "`slice`メソッドはインデックスの開始と終了の指定値を使って文字列をスライス（文字列の一部の抽出を）します。",  # noqa
    ##################################################
    "## Basic usage": "## 基本的な使い方",
    ##################################################
    "The `slice` method requires the `start` and `end` arguments.": "`slice`メソッドは`start`と`end`の2つの引数を必要とします。",  # noqa
    ##################################################
    "The `start` argument is the starting index of slicing.": "`start`引数はスライスの開始インデックスです。",  # noqa
    ##################################################
    "Similarly, the `end` argument is the end index of slicing, with the range being up to (but not including) this index.": "同様に、`end`引数はスライスの終点のインデックスの指定となります。スライス範囲の最後はこのインデックス（ただしこのインデックス自体は含みません）が使われます。",  # noqa
    ##################################################
    '```py\n# runnable\nimport apysc as ap\n\nstage: ap.Stage = ap.Stage(\n    stage_width=0,\n    stage_height=0,\n    background_color=ap.Color("#333"),\n    stage_elem_id="stage",\n)\n\nstring: ap.String = ap.String("012345")\nresult_string: ap.String = string.slice(start=0)\nap.assert_equal(result_string, "012345")\n\nresult_string = string.slice(start=1)\nap.assert_equal(result_string, "12345")\n\nresult_string = string.slice(start=0, end=2)\nap.assert_equal(result_string, "01")\n\nresult_string = string.slice(start=2, end=4)\nap.assert_equal(result_string, "23")\n\nresult_string = string.slice(start=-2)\nap.assert_equal(result_string, "45")\n\nresult_string = string.slice(start=-3, end=-1)\nap.assert_equal(result_string, "34")\n\nap.save_overall_html(dest_dir_path="string_slice_basic_usage/")\n```': '```py\n# runnable\nimport apysc as ap\n\nstage: ap.Stage = ap.Stage(\n    stage_width=0,\n    stage_height=0,\n    background_color=ap.Color("#333"),\n    stage_elem_id="stage",\n)\n\nstring: ap.String = ap.String("012345")\nresult_string: ap.String = string.slice(start=0)\nap.assert_equal(result_string, "012345")\n\nresult_string = string.slice(start=1)\nap.assert_equal(result_string, "12345")\n\nresult_string = string.slice(start=0, end=2)\nap.assert_equal(result_string, "01")\n\nresult_string = string.slice(start=2, end=4)\nap.assert_equal(result_string, "23")\n\nresult_string = string.slice(start=-2)\nap.assert_equal(result_string, "45")\n\nresult_string = string.slice(start=-3, end=-1)\nap.assert_equal(result_string, "34")\n\nap.save_overall_html(dest_dir_path="string_slice_basic_usage/")\n```',  # noqa
    ##################################################
    "## slice method API": "## slice メソッドのAPI",
    ##################################################
    '<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>': '<span class="inconspicuous-txt">特記事項: このAPIドキュメントはドキュメントビルド用のスクリプトによって自動で生成・同期されています。そのためもしかしたらこの節の内容は前節までの内容と重複している場合があります。</span>',  # noqa
    ##################################################
    "**[Interface summary]**": "**[インターフェイス概要]**",
    ##################################################
    "Get a sliced string based on the specified arguments range.<hr>": "指定された引数の範囲に基づいてスライスされた文字列を取得します。<hr>",  # noqa
    ##################################################
    "**[Parameters]**": "**[引数]**",
    ##################################################
    '- `start`: Union[int, "Int"]': '- `start`: Union[int, "Int"]',
    ##################################################
    "  - A start index of the slice range.": "  - スライス範囲の開始インデックス。",
    ##################################################
    '- `end`: Optional[Union[int, "Int"]], optional': '- `end`: Optional[Union[int, "Int"]], optional',  # noqa
    ##################################################
    "  - An end index of the slice range. If this argument is not specified, this method skips the end position's slicing.": "  - スライス範囲の終了インデックス。もしもこの引数が指定されなかった場合、このメソッドは終了位置のスライスをスキップします。",  # noqa
    ##################################################
    '- `variable_name_suffix`: str, default ""': '- `variable_name_suffix`: str, default ""',  # noqa
    ##################################################
    "  - A JavaScript variable name suffix string. This setting is sometimes useful for JavaScript debugging.": "  - JavaScript上の変数のサフィックスの設定です。この設定はJavaScriptのデバッグ時に役立つことがあります。",  # noqa
    ##################################################
    "<hr>": "<hr>",
    ##################################################
    "**[Returns]**": "**[返却値]**",
    ##################################################
    "- `result`: String": "- `result`: String",
    ##################################################
    "  - A sliced result string.": "  - スライス結果の文字列。",
    ##################################################
    "<hr>": "<hr>",
    ##################################################
    "**[Examples]**": "**[コードサンプル]**",
    ##################################################
    '```py\n>>> import apysc as ap\n>>> stage: ap.Stage = ap.Stage(\n...     stage_width=0,\n...     stage_height=0,\n...     background_color=ap.Color("#333"),\n...     stage_elem_id="stage",\n... )\n>>> string: ap.String = ap.String("012345")\n>>> result_string: ap.String = string.slice(start=0)\n>>> result_string\nString("012345")\n\n>>> result_string = string.slice(start=1)\n>>> result_string\nString("12345")\n\n>>> result_string = string.slice(start=0, end=2)\n>>> result_string\nString("01")\n\n>>> result_string = string.slice(start=2, end=4)\n>>> result_string\nString("23")\n\n>>> result_string = string.slice(start=-2)\n>>> result_string\nString("45")\n\n>>> result_string = string.slice(start=-3, end=-1)\n>>> result_string\nString("34")\n```': '```py\n>>> import apysc as ap\n>>> stage: ap.Stage = ap.Stage(\n...     stage_width=0,\n...     stage_height=0,\n...     background_color=ap.Color("#333"),\n...     stage_elem_id="stage",\n... )\n>>> string: ap.String = ap.String("012345")\n>>> result_string: ap.String = string.slice(start=0)\n>>> result_string\nString("012345")\n\n>>> result_string = string.slice(start=1)\n>>> result_string\nString("12345")\n\n>>> result_string = string.slice(start=0, end=2)\n>>> result_string\nString("01")\n\n>>> result_string = string.slice(start=2, end=4)\n>>> result_string\nString("23")\n\n>>> result_string = string.slice(start=-2)\n>>> result_string\nString("45")\n\n>>> result_string = string.slice(start=-3, end=-1)\n>>> result_string\nString("34")\n```',  # noqa
}
