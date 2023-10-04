"""This module is for the translation mapping data of the
following document:

Document file: array_sort.md
Language: jp
"""

from typing import Dict

MAPPING: Dict[str, str] = {
    ##################################################
    "# Array class sort interface": "# Array クラスの sort インターフェイス",
    ##################################################
    "This page explains the `Array` class `sort` method interface.": "このページでは`Array`クラスの`sort`メソッドのインターフェイスについて説明します。",  # noqa
    ##################################################
    "## What interface is this?": "## インターフェイス概要",
    ##################################################
    "The `sort` method interface sorts an array's values (default is ascending order).": "`sort`メソッドのインターフェイスは配列の値をソートします（デフォルトでは昇順となります）。",  # noqa
    ##################################################
    "## Basic usage": "## 基本的な使い方",
    ##################################################
    "The `sort` method requires no arguments and sorts values ascending in place (no return value).": "`sort`は昇順でソートする場合引数を必要とせず、配列の値は直接更新されます（返却値は設定されません）。",  # noqa
    ##################################################
    "```py\n# runnable\nimport apysc as ap\n\nap.Stage()\narr: ap.Array[int] = ap.Array([5, 1, 3])\narr.sort()\nassert arr == [1, 3, 5]\n```": "```py\n# runnable\nimport apysc as ap\n\nap.Stage()\narr: ap.Array[int] = ap.Array([5, 1, 3])\narr.sort()\nassert arr == [1, 3, 5]\n```",  # noqa
    ##################################################
    "If you specify `False` to the `ascending` option, a result value becomes descending order.": "もし`ascending`引数に`False`を指定した場合、結果は降順となります。",  # noqa
    ##################################################
    "```py\n# runnable\nimport apysc as ap\n\nap.Stage()\narr: ap.Array[int] = ap.Array([5, 1, 3])\narr.sort(ascending=False)\nassert arr == [5, 3, 1]\n```": "```py\n# runnable\nimport apysc as ap\n\nap.Stage()\narr: ap.Array[int] = ap.Array([5, 1, 3])\narr.sort(ascending=False)\nassert arr == [5, 3, 1]\n```",  # noqa
    ##################################################
    "## See also": "## 関連資料",
    ##################################################
    "- [Array class reverse interface](array_reverse.md)": "- [Array クラスの reverse インターフェイス](jp_array_reverse.md)",  # noqa
    ##################################################
    "## sort API": "## sort API",
    ##################################################
    '<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>': '<span class="inconspicuous-txt">特記事項: このAPIドキュメントはドキュメントビルド用のスクリプトによって自動で生成・同期されています。そのためもしかしたらこの節の内容は前節までの内容と重複している場合があります。</span>',  # noqa
    ##################################################
    "**[Interface summary]**": "**[インターフェイス概要]**",
    ##################################################
    "Sort this array in place.<hr>": "この配列の値を直接ソートします。<hr>",
    ##################################################
    "**[Parameters]**": "**[引数]**",
    ##################################################
    "- `ascending`: bool, default True": "- `ascending`: bool, default True",
    ##################################################
    "  - Sort by ascending or not. If False is specified, this interface sorts values descending.": "  - 昇順でソートを行うかどうかの指定です。もしFalseが指定された場合、このインターフェイスは降順で値をソートします。",  # noqa
    ##################################################
    "<hr>": "<hr>",
    ##################################################
    "**[Examples]**": "**[コードサンプル]**",
    ##################################################
    "```py\n>>> import apysc as ap\n>>> _ = ap.Stage()\n>>> arr: ap.Array = ap.Array([3, 5, 1, 4, 2])\n>>> arr.sort()\n>>> arr\nArray([1, 2, 3, 4, 5])\n\n>>> arr.sort(ascending=False)\n>>> arr\nArray([5, 4, 3, 2, 1])\n```": "```py\n>>> import apysc as ap\n>>> _ = ap.Stage()\n>>> arr: ap.Array = ap.Array([3, 5, 1, 4, 2])\n>>> arr.sort()\n>>> arr\nArray([1, 2, 3, 4, 5])\n\n>>> arr.sort(ascending=False)\n>>> arr\nArray([5, 4, 3, 2, 1])\n```",  # noqa
}
