"""This module is for the translation mapping data of the
following document:

Document file: array_index_of.md
Language: jp
"""

from typing import Dict

MAPPING: Dict[str, str] = {
    ##################################################
    "# Array class index_of interface": "# Array クラスの index_of インターフェイス",
    ##################################################
    "This page explains the `Array` class `index_of` method interface.": "このページでは`Array`クラスの`index_of`メソッドのインターフェイスについて説明します。",  # noqa
    ##################################################
    "## What interface is this?": "## インターフェイス概要",
    ##################################################
    "The `index_of` method returns the specified value's index in the array.": "`index_of`メソッドは指定された値の配列内でのインデックスを返却します。",  # noqa
    ##################################################
    "## Basic usage": "## 基本的な使い方",
    ##################################################
    "The `index_of` method requires the `value` argument and returns the found value's index in the array.": "`index_of`メソッドは`value`引数の指定を必要とし、値が配列内で見つかった場合にはそのインデックスを返却します。",  # noqa
    ##################################################
    "```py\n# runnable\nimport apysc as ap\n\nap.Stage()\narr: ap.Array[int] = ap.Array([1, 3, 5])\nindex: ap.Int = arr.index_of(value=3)\nassert index == 1\n```": "```py\n# runnable\nimport apysc as ap\n\nap.Stage()\narr: ap.Array[int] = ap.Array([1, 3, 5])\nindex: ap.Int = arr.index_of(value=3)\nassert index == 1\n```",  # noqa
    ##################################################
    "If there is no found value, the return index becomes `-1`.": "もしも配列内で値が見つからなかった場合インデックスは`-1`となります。",  # noqa
    ##################################################
    "```py\n# runnable\nimport apysc as ap\n\nap.Stage()\narr: ap.Array[int] = ap.Array([1, 3, 5])\nindex: ap.Int = arr.index_of(value=2)\nassert index == -1\n```": "```py\n# runnable\nimport apysc as ap\n\nap.Stage()\narr: ap.Array[int] = ap.Array([1, 3, 5])\nindex: ap.Int = arr.index_of(value=2)\nassert index == -1\n```",  # noqa
    ##################################################
    "## index_of API": "## index_of API",
    ##################################################
    '<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>': '<span class="inconspicuous-txt">特記事項: このAPIドキュメントはドキュメントビルド用のスクリプトによって自動で生成・同期されています。そのためもしかしたらこの節の内容は前節までの内容と重複している場合があります。</span>',  # noqa
    ##################################################
    "**[Interface summary]**": "**[インターフェイス概要]**",
    ##################################################
    "Search specified value's index and return it.<hr>": "指定された値のインデックス位置を検索しその値を返却します。<hr>",  # noqa
    ##################################################
    "**[Parameters]**": "**[引数]**",
    ##################################################
    "- `value`: *": "- `value`: *",
    ##################################################
    "  - Any value to search.": "  - 検索対象の任意の値。",
    ##################################################
    "<hr>": "<hr>",
    ##################################################
    "**[Returns]**": "**[返却値]**",
    ##################################################
    "- `index`: Int": "- `index`: Int",
    ##################################################
    "  - Found position of index. If this array does not contain a value, this interface returns -1.": "  - 値が見つかった位置のインデックス。もし配列が対象の値を含んでいない場合は-1となります。",  # noqa
    ##################################################
    "<hr>": "<hr>",
    ##################################################
    "**[Examples]**": "**[コードサンプル]**",
    ##################################################
    "```py\n>>> import apysc as ap\n>>> _ = ap.Stage()\n>>> arr: ap.Array = ap.Array([1, 3, 5])\n>>> arr.index_of(3)\nInt(1)\n```": "```py\n>>> import apysc as ap\n>>> _ = ap.Stage()\n>>> arr: ap.Array = ap.Array([1, 3, 5])\n>>> arr.index_of(3)\nInt(1)\n```",  # noqa
}
