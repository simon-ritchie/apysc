"""This module is for the translation mapping data of the
following document:

Document file: array_clear.md
Language: jp
"""

from typing import Dict

MAPPING: Dict[str, str] = {
    ##################################################
    "# Array class clear interface": "# Array クラスの clear インターフェイス",
    ##################################################
    "This page explains the `Array` class `clear` method interface.": "このページでは`Array`クラスの`clear`メソッドのインターフェイスについて説明します。",  # noqa
    ##################################################
    "## What interface is this?": "## インターフェイス概要",
    ##################################################
    "The `clear` method clears an Array's value. This interface makes an Array's value empty.": "`clear`メソッドは配列の値を空にします。",  # noqa
    ##################################################
    "## Basic usage": "## 基本的な使い方",
    ##################################################
    "The `clear` method requires no arguments.": "`clear`メソッドは呼び出しに特に引数を必要としません。",
    ##################################################
    "```py\n# runnable\nimport apysc as ap\n\narr: ap.Array = ap.Array([10, 20, 30])\narr.clear()\nassert arr == []\n```": "```py\n# runnable\nimport apysc as ap\n\narr: ap.Array = ap.Array([10, 20, 30])\narr.clear()\nassert arr == []\n```",  # noqa
}
