"""This module is for the translation mapping data of the
following document:

Document file: array_remove_and_remove_at.md
Language: jp
"""

from typing import Dict

MAPPING: Dict[str, str] = {
    ##################################################
    "# Array class remove and remove_at interfaces": "# Array クラスの remove と remove_at のインターフェイス",  # noqa
    ##################################################
    "This page explains the `Array` class `remove` and `remove_at` method interfaces.": "このページでは`Array`クラスの`remove`と`remove_at`メソッドの各インターフェイスについて説明します。",  # noqa
    ##################################################
    "## What interfaces are these?": "## 各インターフェイスの概要",
    ##################################################
    "The `remove` method removes a specified value from an array, and the `remove_at` method removes a specified index value.": "`remove`メソッドは配列から指定された値を取り除き、`remove_at`メソッドは配列から指定されたインデックスの値を取り除きます。",  # noqa
    ##################################################
    "## Basic usage": "## 基本的な使い方",
    ##################################################
    "The `remove` method requires target value at the first argument, as follows:": "`remove`メソッドは以下のコード例のように取り除く対象の値を第一引数に必要とします。",  # noqa
    ##################################################
    "```py\n# runnable\nimport apysc as ap\n\nap.Stage()\narr: ap.Array[int] = ap.Array([1, 2, 3])\narr.remove(value=2)\nassert arr == [1, 3]\n```": "```py\n# runnable\nimport apysc as ap\n\nap.Stage()\narr: ap.Array[int] = ap.Array([1, 2, 3])\narr.remove(value=2)\nassert arr == [1, 3]\n```",  # noqa
    ##################################################
    "The `remove_at` method requires index (`int` or `Int` value) at the first argument, as follows:": "`remove_at`メソッドは以下のコード例のように配列のインデックスの整数（Pythonビルトインの`int`もしくはapyscの`Int`）を第一引数に必要とします。",  # noqa
    ##################################################
    "```py\n# runnable\nimport apysc as ap\n\nap.Stage()\narr: ap.Array[int] = ap.Array([1, 2, 3])\narr.remove_at(index=1)\nassert arr == [1, 3]\n```": "```py\n# runnable\nimport apysc as ap\n\nap.Stage()\narr: ap.Array[int] = ap.Array([1, 2, 3])\narr.remove_at(index=1)\nassert arr == [1, 3]\n```",  # noqa
    ##################################################
    "## remove API": "## remove API",
    ##################################################
    '<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>': '<span class="inconspicuous-txt">特記事項: このAPIドキュメントはドキュメントビルド用のスクリプトによって自動で生成・同期されています。そのためもしかしたらこの節の内容は前節までの内容と重複している場合があります。</span>',  # noqa
    ##################################################
    "**[Interface summary]**": "**[インターフェイス概要]**",
    ##################################################
    "Remove a specified value from this array.<hr>": "指定された値をこの配列から取り除きます。<hr>",
    ##################################################
    "**[Parameters]**": "**[引数]**",
    ##################################################
    "- `value`: Any": "- `value`: Any",
    ##################################################
    "  - Value to remove.": "  - 取り除く対象の値。",
    ##################################################
    "<hr>": "<hr>",
    ##################################################
    "**[Examples]**": "**[コードサンプル]**",
    ##################################################
    "```py\n>>> import apysc as ap\n>>> _ = ap.Stage()\n>>> arr: ap.Array = ap.Array([1, 3, 5])\n>>> arr.remove(3)\n>>> arr\nArray([1, 5])\n```": "```py\n>>> import apysc as ap\n>>> _ = ap.Stage()\n>>> arr: ap.Array = ap.Array([1, 3, 5])\n>>> arr.remove(3)\n>>> arr\nArray([1, 5])\n```",  # noqa
    ##################################################
    "## remove_at API": "## remove_at API",
    ##################################################
    '<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>': '<span class="inconspicuous-txt">特記事項: このAPIドキュメントはドキュメントビルド用のスクリプトによって自動で生成・同期されています。そのためもしかしたらこの節の内容は前節までの内容と重複している場合があります。</span>',  # noqa
    ##################################################
    "**[Interface summary]**": "**[インターフェイス概要]**",
    ##################################################
    "Remove a specified index value from this array.<hr>": "指定されたインデックスの値をこの配列から取り除きます。<hr>",  # noqa
    ##################################################
    "**[Parameters]**": "**[引数]**",
    ##################################################
    "- `index`: Int or int": "- `index`: Int or int",
    ##################################################
    "  - Index to remove value.": "  - 取り除く値のインデックス。",
    ##################################################
    "<hr>": "<hr>",
    ##################################################
    "**[Examples]**": "**[コードサンプル]**",
    ##################################################
    "```py\n>>> import apysc as ap\n>>> _ = ap.Stage()\n>>> arr: ap.Array = ap.Array([1, 2, 3])\n>>> arr.remove_at(1)\n>>> arr\nArray([1, 3])\n```": "```py\n>>> import apysc as ap\n>>> _ = ap.Stage()\n>>> arr: ap.Array = ap.Array([1, 2, 3])\n>>> arr.remove_at(1)\n>>> arr\nArray([1, 3])\n```",  # noqa
}
