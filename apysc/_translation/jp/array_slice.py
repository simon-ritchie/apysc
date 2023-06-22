"""This module is for the translation mapping data of the
following document:

Document file: array_slice.md
Language: jp
"""

from typing import Dict

MAPPING: Dict[str, str] = {
    ##################################################
    "# Array class slice interface": "# Array クラスの slice インターフェイス",
    ##################################################
    "This page explains the `Array` class `slice` method interface.": "このページでは`Array`クラスの`slice`メソッドのインターフェイスについて説明します。",  # noqa
    ##################################################
    "## What interface is this?": "## インターフェイス概要",
    ##################################################
    "The `slice` method interface extracts the specified index range array's values and returns a new array.": "`slice`メソッドのインターフェイスは指定されたインデックスの範囲の配列の値を抽出し新しい配列を返却します。",  # noqa
    ##################################################
    "## Basic usage": "## 基本的な使い方",
    ##################################################
    "The `slice` method requires the `start` and `end` arguments (`int` or `Int` values) and returns a new array.": "`slice`メソッドは`start`と`end`の各引数（Pythonビルトインの`int`もしくはapyscの`Int`の整数）を必要とし、返却値として新しい配列を返します。",  # noqa
    ##################################################
    "If you specify 1 to the `start` argument and 3 to the `end` argument, this method behaves like the Python built-in list slice of `[1:3]`.": "例として`start`引数に1を指定し`end`引数に3を指定した場合、このメソッドはPythonビルトインの`[1:3]`という指定によるスライスと同じように動作します。",  # noqa
    ##################################################
    "An original array is not modified.": "元々の配列の値は変更されません。",
    ##################################################
    "```py\n# runnable\nimport apysc as ap\n\narr: ap.Array[int] = ap.Array([1, 2, 3, 4])\nsliced_arr: ap.Array[int] = arr.slice(start=1, end=3)\nassert sliced_arr == [2, 3]\nassert arr == [1, 2, 3, 4]\n```": "```py\n# runnable\nimport apysc as ap\n\narr: ap.Array[int] = ap.Array([1, 2, 3, 4])\nsliced_arr: ap.Array[int] = arr.slice(start=1, end=3)\nassert sliced_arr == [2, 3]\nassert arr == [1, 2, 3, 4]\n```",  # noqa
    ##################################################
    "## slice API": "## slice API",
    ##################################################
    '<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>': '<span class="inconspicuous-txt">特記事項: このAPIドキュメントはドキュメントビルド用のスクリプトによって自動で生成・同期されています。そのためもしかしたらこの節の内容は前節までの内容と重複している場合があります。</span>',  # noqa
    ##################################################
    "**[Interface summary]**": "**[インターフェイス概要]**",
    ##################################################
    "Slice this array by specified start and end indexes.<hr>": "指定された開始と終了のインデックス範囲でこの配列をスライスします。<hr>",  # noqa
    ##################################################
    "**[Parameters]**": "**[引数]**",
    ##################################################
    "- `start`: Int or int or None, default None": "- `start`: Int or int or None, default None",  # noqa
    ##################################################
    "  - Slicing start index.": "  - スライス範囲の開始インデックス。",
    ##################################################
    "- `end`: Int or int or None, default None": "- `end`: Int or int or None, default None",  # noqa
    ##################################################
    "  - Slicing end index (a result array does not contain this index).": "  - スライス範囲の終了インデックス（結果の配列のこのインデックスの値を含みません）。",  # noqa
    ##################################################
    "<hr>": "<hr>",
    ##################################################
    "**[Returns]**": "**[返却値]**",
    ##################################################
    "- `sliced_arr`: Array": "- `sliced_arr`: Array",
    ##################################################
    "  - Sliced array.": "  - スライスされた配列。",
    ##################################################
    "<hr>": "<hr>",
    ##################################################
    "**[Examples]**": "**[コードサンプル]**",
    ##################################################
    "```py\n>>> import apysc as ap\n>>> arr: ap.Array = ap.Array([1, 2, 3, 4])\n>>> arr.slice(start=1, end=3)\nArray([2, 3])\n\n>>> arr.slice(start=1)\nArray([2, 3, 4])\n\n>>> arr.slice(end=2)\nArray([1, 2])\n```": "```py\n>>> import apysc as ap\n>>> arr: ap.Array = ap.Array([1, 2, 3, 4])\n>>> arr.slice(start=1, end=3)\nArray([2, 3])\n\n>>> arr.slice(start=1)\nArray([2, 3, 4])\n\n>>> arr.slice(end=2)\nArray([1, 2])\n```",  # noqa
}
