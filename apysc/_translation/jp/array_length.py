"""This module is for the translation mapping data of the
following document:

Document file: array_length.md
Language: jp
"""

from typing import Dict

MAPPING: Dict[str, str] = {
    ##################################################
    "# Array class length interface": "# Array クラスの length インターフェイス",
    ##################################################
    "This page explains the `Array` class `length` property interface.": "このページでは`Array`クラスの`length`属性のインターフェイスについて説明します。",  # noqa
    ##################################################
    "## What interface is this?": "## インターフェイス概要",
    ##################################################
    "The `length` property interface returns a current array value length.": "`length`属性のインターフェイスは配列の値の長さ（件数）を返却します。",  # noqa
    ##################################################
    "## Basic usage": "## 基本的な使い方",
    ##################################################
    "The `length` property has the only getter interface. The return value type is the `Int` type.": "`length`属性はgetterのインターフェイスのみを持ちます。返却値はapyscの`Int`クラスの整数値となります。",  # noqa
    ##################################################
    "```py\n# runnable\nimport apysc as ap\n\nap.Stage()\narr: ap.Array[int] = ap.Array([1, 2, 3, 4])\nlength: ap.Int = arr.length\nassert length == 4\n```": "```py\n# runnable\nimport apysc as ap\n\nap.Stage()\narr: ap.Array[int] = ap.Array([1, 2, 3, 4])\nlength: ap.Int = arr.length\nassert length == 4\n```",  # noqa
    ##################################################
    "## Notes of the len() function": "## len()関数における特記事項",
    ##################################################
    "The `Array` class is not supported the Python built-in `len()` function, and its function raises an exception. Please use the `length` property instead.": "`Array`クラスはPythonビルトインの`len()`関数をサポートしておらず、もし使用した場合にはエラーとなります。代わりに`length`属性を使用してください。",  # noqa
    ##################################################
    "```py\nimport apysc as ap\n\nap.Stage()\narr: ap.Array[int] = ap.Array([1, 2, 3, 4])\nlen(arr)\n```": "```py\nimport apysc as ap\n\nap.Stage()\narr: ap.Array[int] = ap.Array([1, 2, 3, 4])\nlen(arr)\n```",  # noqa
    ##################################################
    "```\nException: Array instance can't apply len function. Please use length property instead.\n```": "```\nException: Array instance can't apply len function. Please use length property instead.\n```",  # noqa
    ##################################################
    "## length property API": "## length 属性のAPI",
    ##################################################
    '<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>': '<span class="inconspicuous-txt">特記事項: このAPIドキュメントはドキュメントビルド用のスクリプトによって自動で生成・同期されています。そのためもしかしたらこの節の内容は前節までの内容と重複している場合があります。</span>',  # noqa
    ##################################################
    "**[Interface summary]**": "**[インターフェイス概要]**",
    ##################################################
    "Get length of this array.<hr>": "この配列の長さ（値の数）を取得します。<hr>",
    ##################################################
    "**[Returns]**": "**[返却値]**",
    ##################################################
    "- `length`: Int": "- `length`: Int",
    ##################################################
    "  - This array's length.": "  - この配列の長さ（値の件数）。",
    ##################################################
    "<hr>": "<hr>",
    ##################################################
    "**[Examples]**": "**[コードサンプル]**",
    ##################################################
    "```py\n>>> import apysc as ap\n>>> _ = ap.Stage()\n>>> arr: ap.Array = ap.Array([1, 2, 3])\n>>> arr.length\nInt(3)\n```": "```py\n>>> import apysc as ap\n>>> _ = ap.Stage()\n>>> arr: ap.Array = ap.Array([1, 2, 3])\n>>> arr.length\nInt(3)\n```",  # noqa
}
