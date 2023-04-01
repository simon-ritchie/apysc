"""This module is for the translation mapping data of the
following document:

Document file: math_max.md
Language: jp
"""

from typing import Dict

MAPPING: Dict[str, str] = {
    ##################################################
    "# Math max interface": "# Math クラスの max インターフェイス",
    ##################################################
    "This page explains the `Math` class's `max` class method interface.": "このページでは`Math`クラスの`max`クラスメソッドのインターフェイスについて説明します。",  # noqa
    ##################################################
    "## What interface is this?": "## インターフェイス概要",
    ##################################################
    "The `max` class method interface returns a maximum number from a specified array of numbers.": "`max`クラスメソッドのインターフェイスは指定された数値を格納した配列の中での最大値を返却します。",  # noqa
    ##################################################
    "## Basic usage": "## 基本的な使い方",
    ##################################################
    "The `max` interface requires an `Array` value argument (`values`).": "`max`インターフェイスでは`Array`型の値の引数（`values`）が必要になります。",  # noqa
    ##################################################
    "It returns a `Number` value.": "このインターフェイスは`Number`型の値を返却します。",
    ##################################################
    "Notes: Regardless of the `Array` values' type, this interface returns a `Number` type value.": "特記事項: `Array`内の各値の型に関わらず、このインターフェイスは`Number`型の値を返却します。",  # noqa
    ##################################################
    "```py\n# runnable\nimport apysc as ap\n\narr: ap.Array = ap.Array([9, 10, ap.Int(8), ap.Number(9.5), 11])\nmax_value: ap.Number = ap.Math.max(values=arr)\nassert max_value == 11\n```": "```py\n# runnable\nimport apysc as ap\n\narr: ap.Array = ap.Array([9, 10, ap.Int(8), ap.Number(9.5), 11])\nmax_value: ap.Number = ap.Math.max(values=arr)\nassert max_value == 11\n```",  # noqa
    ##################################################
    "## Math.max API": "## Math.max のAPI",
    ##################################################
    '<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>': '<span class="inconspicuous-txt">特記事項: このAPIドキュメントはドキュメントビルド用のスクリプトによって自動で生成・同期されています。そのためもしかしたらこの節の内容は前節までの内容と重複している場合があります。</span>',  # noqa
    ##################################################
    "**[Interface summary]**": "**[インターフェイス概要]**",
    ##################################################
    "Get a maximum number from a specified array's values.<hr>": "指定された配列の値の中から最大値の数値を取得します。<hr>",  # noqa
    ##################################################
    "**[Parameters]**": "**[引数]**",
    ##################################################
    "- `values`: Array[Union[Int, Number, int, float]]": "- `values`: Array[Union[Int, Number, int, float]]",  # noqa
    ##################################################
    "  - An array of numbers.": "  - 数値を格納した配列。",
    ##################################################
    "<hr>": "<hr>",
    ##################################################
    "**[Returns]**": "**[返却値]**",
    ##################################################
    "- `max_value`: Number": "- `max_value`: Number",
    ##################################################
    "  - Maximum number in an array.": "  - 配列の中の数値の最大値。",
    ##################################################
    "<hr>": "<hr>",
    ##################################################
    "**[Examples]**": "**[コードサンプル]**",
    ##################################################
    "```py\n>>> import apysc as ap\n>>> arr: ap.Array = ap.Array([10, 9.5, ap.Int(8), ap.Number(8.5)])\n>>> max_value: ap.Number = ap.Math.max(values=arr)\n>>> max_value\nNumber(10.0)\n```": "```py\n>>> import apysc as ap\n>>> arr: ap.Array = ap.Array([10, 9.5, ap.Int(8), ap.Number(8.5)])\n>>> max_value: ap.Number = ap.Math.max(values=arr)\n>>> max_value\nNumber(10.0)\n```",  # noqa
}
