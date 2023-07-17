"""This module is for the translation mapping data of the
following document:

Document file: array_comparison.md
Language: jp
"""

from typing import Dict

MAPPING: Dict[str, str] = {
    ##################################################
    "# Array class comparison interfaces": "# Array クラスの比較の各インターフェイス",
    ##################################################
    "This page explains the `Array` class comparison interfaces (equal and not equal comparison).": "このページでは`Array`クラスにおける等値と非等値の比較の各インターフェイスについて説明します。",  # noqa
    ##################################################
    "## Basic usage": "## 基本的な使い方",
    ##################################################
    "The `Array` value can compare with a Python built-in `list` value and `Array` value. A return value becomes the `Boolean` type.": "`Array`クラスの値はPythonビルトインのリスト及び別の`Array`クラスの値と比較を行うことができます。結果は`Boolean`型となります。",  # noqa
    ##################################################
    "```py\n# runnable\nimport apysc as ap\n\nap.Stage()\narr: ap.Array[int] = ap.Array([1, 3, 5])\nresult: ap.Boolean = arr == [1, 3, 5]\nassert result\n```": "```py\n# runnable\nimport apysc as ap\n\nap.Stage()\narr: ap.Array[int] = ap.Array([1, 3, 5])\nresult: ap.Boolean = arr == [1, 3, 5]\nassert result\n```",  # noqa
    ##################################################
    "```py\n# runnable\nimport apysc as ap\n\nap.Stage()\narr: ap.Array[int] = ap.Array([1, 3, 5])\nother_arr: ap.Array[int] = ap.Array([1, 3, 5])\nresult: ap.Boolean = arr == other_arr\nassert result\n```": "```py\n# runnable\nimport apysc as ap\n\nap.Stage()\narr: ap.Array[int] = ap.Array([1, 3, 5])\nother_arr: ap.Array[int] = ap.Array([1, 3, 5])\nresult: ap.Boolean = arr == other_arr\nassert result\n```",  # noqa
    ##################################################
    "The equal comparison operator (`==`) and not equal comparison operator (`!=`) are supported:": "等値の比較記号（`==`）と非等値の比較記号（`!=`）をサポートしています:",  # noqa
    ##################################################
    "```py\n# runnable\nimport apysc as ap\n\nap.Stage()\narr: ap.Array[int] = ap.Array([1, 3, 5])\nresult: ap.Boolean = arr != [2, 4, 6]\nassert result\n```": "```py\n# runnable\nimport apysc as ap\n\nap.Stage()\narr: ap.Array[int] = ap.Array([1, 3, 5])\nresult: ap.Boolean = arr != [2, 4, 6]\nassert result\n```",  # noqa
}
