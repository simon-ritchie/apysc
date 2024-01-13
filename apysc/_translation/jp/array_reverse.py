"""This module is for the translation mapping data of the
following document:

Document file: array_reverse.md
Language: jp
"""

from typing import Dict

MAPPING: Dict[str, str] = {
    ##################################################
    "# Array class reverse interface": "# Array クラスの reverse インターフェイス",
    ##################################################
    "This page explains the `Array` class `reverse` method interface.": "このページでは`Array`クラスの`reverse`メソッドのインターフェイスについて説明します。",  # noqa
    ##################################################
    "## What interface is this?": "## インターフェイス概要",
    ##################################################
    "The `reverse` method interface reverses an array's values order in place.": "`reverse`メソッドは配列の値を直接更新する形で値の順番を逆順にします。",  # noqa
    ##################################################
    "## Basic usage": "## 基本的な使い方",
    ##################################################
    "The `reverse` method requires no arguments and returns no value.": "`reverse`メソッドは引数の指定を必要としません。",  # noqa
    ##################################################
    "```py\n# runnable\nimport apysc as ap\n\nap.Stage()\narr: ap.Array[int] = ap.Array([1, 3, 5])\narr.reverse()\nassert arr == [5, 3, 1]\n```": "```py\n# runnable\nimport apysc as ap\n\nap.Stage()\narr: ap.Array[int] = ap.Array([1, 3, 5])\narr.reverse()\nassert arr == [5, 3, 1]\n```",  # noqa
    ##################################################
    "## See also": "## 関連資料",
    ##################################################
    "- [Array class sort interface](array_sort.md)": "- [Array クラスの sort インターフェイス](jp_array_sort.md)",  # noqa
    ##################################################
    "## reverse API": "## reverse API",
    ##################################################
    '<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>': '<span class="inconspicuous-txt">特記事項: このAPIドキュメントはドキュメントビルド用のスクリプトによって自動で生成・同期されています。そのためもしかしたらこの節の内容は前節までの内容と重複している場合があります。</span>',  # noqa
    ##################################################
    "**[Interface summary]**": "**[インターフェイス概要]**",
    ##################################################
    "Reverse this array in place.<hr>": "この配列の値を直接逆順にします。<hr>",
    ##################################################
    "**[Examples]**": "**[コードサンプル]**",
    ##################################################
    "```py\n>>> import apysc as ap\n>>> _ = ap.Stage()\n>>> arr: ap.Array = ap.Array([1, 2, 3])\n>>> arr.reverse()\n>>> arr\nArray([3, 2, 1])\n```": "```py\n>>> import apysc as ap\n>>> _ = ap.Stage()\n>>> arr: ap.Array = ap.Array([1, 2, 3])\n>>> arr.reverse()\n>>> arr\nArray([3, 2, 1])\n```",  # noqa
}
