"""This module is for the translation mapping data of the
following document:

Document file: math_min.md
Language: jp
"""

from typing import Dict

MAPPING: Dict[str, str] = {
    ##################################################
    "# Math min interface": "# Math クラスの min インターフェイス",
    ##################################################
    "This page explains the `Math` class's `min` class method interface.": "このページでは`Math`クラスの`min`のクラスメソッドのインターフェイスについて説明します。",  # noqa
    ##################################################
    "## What interface is this?": "## インターフェイス概要",
    ##################################################
    "The `min` class method interface returns a minimum number from a specified array of numbers.": "`min`のクラスメソッドのインターフェイスでは指定された数値の配列の中の最小値を返却します。",  # noqa
    ##################################################
    "## Basic usage": "## 基本的な使い方",
    ##################################################
    "The `min` interface requires an `Array` value argument (`values`).": "`min`インターフェイスは`Array`クラスの値の引数（`values`）を必要とします。",  # noqa
    ##################################################
    "It returns a `Number` value.": "このインターフェイスは`Number`型の値を返却します。",
    ##################################################
    "Notes: Regardless of the `Array` values' type, this interface returns a `Number` type value.": "特記事項: `Array`内の各値の型に関わらず、このインターフェイスは`Number`型の値を返却します。",  # noqa
    ##################################################
    "```py\n# runnable\nimport apysc as ap\n\nap.Stage()\narr: ap.Array = ap.Array([9, 10, ap.Int(8), ap.Number(9.5), 11])\nmin_value: ap.Number = ap.Math.min(values=arr)\nassert min_value == 8\n```": "```py\n# runnable\nimport apysc as ap\n\nap.Stage()\narr: ap.Array = ap.Array([9, 10, ap.Int(8), ap.Number(9.5), 11])\nmin_value: ap.Number = ap.Math.min(values=arr)\nassert min_value == 8\n```",  # noqa
    ##################################################
    "## Math.min API": "## Math.min のAPI",
    ##################################################
    '<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>': '<span class="inconspicuous-txt">特記事項: このAPIドキュメントはドキュメントビルド用のスクリプトによって自動で生成・同期されています。そのためもしかしたらこの節の内容は前節までの内容と重複している場合があります。</span>',  # noqa
    ##################################################
    "**[Interface summary]**": "**[インターフェイス概要]**",
    ##################################################
    "Get a minimum number from a specified array's values.<hr>": "指定された配列の各値の中から最小値の数値を取得します。<hr>",  # noqa
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
    "- `min_value`: Number": "- `min_value`: Number",
    ##################################################
    "  - Minimum number in an array.": "  - 配列の中で最小の数値。",
    ##################################################
    "<hr>": "<hr>",
    ##################################################
    "**[Examples]**": "**[コードサンプル]**",
    ##################################################
    "```py\n>>> import apysc as ap\n>>> _ = ap.Stage()\n>>> arr: ap.Array = ap.Array([10, 9.5, ap.Int(8), ap.Number(8.5)])\n>>> min_value: ap.Number = ap.Math.min(values=arr)\n>>> min_value\nNumber(8.0)\n```": "```py\n>>> import apysc as ap\n>>> _ = ap.Stage()\n>>> arr: ap.Array = ap.Array([10, 9.5, ap.Int(8), ap.Number(8.5)])\n>>> min_value: ap.Number = ap.Math.min(values=arr)\n>>> min_value\nNumber(8.0)\n```",  # noqa
}
