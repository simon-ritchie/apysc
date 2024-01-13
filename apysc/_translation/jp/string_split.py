"""This module is for the translation mapping data of the
following document:

Document file: string_split.md
Language: jp
"""

from typing import Dict

MAPPING: Dict[str, str] = {
    ##################################################
    "# String class split interface": "# String クラスの split インターフェイス",
    ##################################################
    "This page explains the `String` class `split` method interface.": "このページでは`String`クラスの`split`メソッドのインターフェイスについて説明します。",  # noqa
    ##################################################
    "## What interface is this?": "## インターフェイス概要",
    ##################################################
    "The `split` method interface splits a string into an `Array` instance of `String`s.": "`split`メソッドのインターフェイスは文字列を分割して`String`の値を格納した`Array`の配列を作成します。",  # noqa
    ##################################################
    "## Basic usage": "## 基本的な使い方",
    ##################################################
    "The `split` method requires the `sep` `String` argument as a separator.": "`split`メソッドは区切り文字としての`sep`の`String`型の引数を必要とします。",  # noqa
    ##################################################
    '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    stage_width=0,\n    stage_height=0,\n    background_color=ap.Color("#333"),\n    stage_elem_id="stage",\n)\n\nstr_value: ap.String = ap.String("Lorem ipsum dolor sit")\nsplitted_strs: ap.Array[ap.String] = str_value.split(sep=ap.String(" "))\nap.assert_arrays_equal(splitted_strs, ["Lorem", "ipsum", "dolor", "sit"])\n\nap.save_overall_html(dest_dir_path="string_split_basic_usage/")\n```': '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    stage_width=0,\n    stage_height=0,\n    background_color=ap.Color("#333"),\n    stage_elem_id="stage",\n)\n\nstr_value: ap.String = ap.String("Lorem ipsum dolor sit")\nsplitted_strs: ap.Array[ap.String] = str_value.split(sep=ap.String(" "))\nap.assert_arrays_equal(splitted_strs, ["Lorem", "ipsum", "dolor", "sit"])\n\nap.save_overall_html(dest_dir_path="string_split_basic_usage/")\n```',  # noqa
    ##################################################
    "## split API": "## split API",
    ##################################################
    '<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>': '<span class="inconspicuous-txt">特記事項: このAPIドキュメントはドキュメントビルド用のスクリプトによって自動で生成・同期されています。そのためもしかしたらこの節の内容は前節までの内容と重複している場合があります。</span>',  # noqa
    ##################################################
    "**[Interface summary]**": "**[インターフェイス概要]**",
    ##################################################
    "Split a current string with a separator string.<hr>": "現在の文字列を指定された区切り文字（列）を使って分割します。<hr>",  # noqa
    ##################################################
    "**[Parameters]**": "**[引数]**",
    ##################################################
    "- `sep`: String": "- `sep`: String",
    ##################################################
    "  - A separator string.": "  - 区切り文字（列）。",
    ##################################################
    "<hr>": "<hr>",
    ##################################################
    "**[Returns]**": "**[返却値]**",
    ##################################################
    "- `splitted_strs`: Array[String]": "- `splitted_strs`: Array[String]",
    ##################################################
    "  - A splitted strings' array.": "  - 分割された文字列を格納した配列。",
    ##################################################
    "<hr>": "<hr>",
    ##################################################
    "**[Examples]**": "**[コードサンプル]**",
    ##################################################
    '```py\n>>> import apysc as ap\n>>> _ = ap.Stage()\n>>> str_value: ap.String = ap.String("Lorem ipsum dolor sit")\n>>> splitted_strs: ap.Array[ap.String] = str_value.split(sep=ap.String(" "))\n>>> ap.assert_arrays_equal(splitted_strs, ["Lorem", "ipsum", "dolor", "sit"])\n```': '```py\n>>> import apysc as ap\n>>> _ = ap.Stage()\n>>> str_value: ap.String = ap.String("Lorem ipsum dolor sit")\n>>> splitted_strs: ap.Array[ap.String] = str_value.split(sep=ap.String(" "))\n>>> ap.assert_arrays_equal(splitted_strs, ["Lorem", "ipsum", "dolor", "sit"])\n```',  # noqa
}
