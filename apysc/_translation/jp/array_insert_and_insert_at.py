"""This module is for the translation mapping data of the
following document:

Document file: array_insert_and_insert_at.md
Language: jp
"""

from typing import Dict

MAPPING: Dict[str, str] = {
    ##################################################
    "# Array class insert and insert_at interfaces": "# Array クラスの insert と insert_at のインターフェイス",  # noqa
    ##################################################
    "This page explains the `Array` class `insert` and `insert_at` method interfaces.": "このページでは`Array`クラスの`insert`と`insert_at`メソッドの各インターフェイスについて説明します。",  # noqa
    ##################################################
    "## What interfaces are these?": "## 各インターフェイスの概要",
    ##################################################
    "The `insert` and `insert_at` method interfaces append any value at the specified index. Both interfaces behave the same way (the `insert` is the alias of the `insert_at`).": "`insert`と`insert_at`メソッドの各インターフェイスは任意の値を配列の指定されたインデックスへと追加します。それぞれの員スターフェイスは同じ挙動をします（`insert`メソッドは`insert_at`メソッドのエイリアスとなっています）。",  # noqa
    ##################################################
    "## Basic usage": "## 基本的な使い方",
    ##################################################
    "The `insert` and `insert_at` have the same argument, the `index` and `value`\\. The `index` argument accepts an `int` and `Int` value.": "`insert`と`insert_at`メソッドは`index`と`value`の同じ引数を持っています。`index`引数はPythonビルトインの`int`とapyscの`Int`クラスの値を受け付けます。",  # noqa
    ##################################################
    "```py\n# runnable\nimport apysc as ap\n\narr: ap.Array[int] = ap.Array([1, 4])\narr.insert(index=1, value=2)\nassert arr == [1, 2, 4]\n\nindex: ap.Int = ap.Int(2)\narr.insert_at(index=index, value=3)\nassert arr == [1, 2, 3, 4]\n```": "```py\n# runnable\nimport apysc as ap\n\narr: ap.Array[int] = ap.Array([1, 4])\narr.insert(index=1, value=2)\nassert arr == [1, 2, 4]\n\nindex: ap.Int = ap.Int(2)\narr.insert_at(index=index, value=3)\nassert arr == [1, 2, 3, 4]\n```",  # noqa
    ##################################################
    "## insert API": "## insert API",
    ##################################################
    '<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>': '<span class="inconspicuous-txt">特記事項: このAPIドキュメントはドキュメントビルド用のスクリプトによって自動で生成・同期されています。そのためもしかしたらこの節の内容は前節までの内容と重複している場合があります。</span>',  # noqa
    ##################################################
    "**[Interface summary]**": "**[インターフェイス概要]**",
    ##################################################
    "Insert value to this array at a specified index. This interface behaves in the same `insert_at` method.<hr>": "この配列の指定されたインデックスの位置へ値を挿入します。このインターフェイスは`insert_at`メソッドと同じ挙動をします。<hr>",  # noqa
    ##################################################
    "**[Parameters]**": "**[引数]**",
    ##################################################
    "- `index`: Int or int": "- `index`: Int or int",
    ##################################################
    "  - Index to append value.": "  - 値を追加するインデックス。",
    ##################################################
    "- `value`: *": "- `value`: *",
    ##################################################
    "  - Any value to append.": "  - 追加対象の任意の値。",
    ##################################################
    "<hr>": "<hr>",
    ##################################################
    "**[Examples]**": "**[コードサンプル]**",
    ##################################################
    "```py\n>>> import apysc as ap\n>>> arr: ap.Array = ap.Array([1, 3])\n>>> arr.insert(index=1, value=2)\n>>> arr\nArray([1, 2, 3])\n```": "```py\n>>> import apysc as ap\n>>> arr: ap.Array = ap.Array([1, 3])\n>>> arr.insert(index=1, value=2)\n>>> arr\nArray([1, 2, 3])\n```",  # noqa
    ##################################################
    "## insert_at API": "## insert_at API",
    ##################################################
    '<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>': '<span class="inconspicuous-txt">特記事項: このAPIドキュメントはドキュメントビルド用のスクリプトによって自動で生成・同期されています。そのためもしかしたらこの節の内容は前節までの内容と重複している場合があります。</span>',  # noqa
    ##################################################
    "**[Interface summary]**": "**[インターフェイス概要]**",
    ##################################################
    "Insert value to this array at a specified index. This interface behaves in the same `insert` method.<hr>": "この配列の指定されたインデックスの位置へ値を挿入します。このインターフェイスは`insert`メソッドと同じ挙動をします。<hr>",  # noqa
    ##################################################
    "**[Parameters]**": "**[引数]**",
    ##################################################
    "- `index`: Int or int": "- `index`: Int or int",
    ##################################################
    "  - Index to append value.": "  - 値を追加するインデックス。",
    ##################################################
    "- `value`: *": "- `value`: *",
    ##################################################
    "  - Any value to append.": "  - 追加対象の任意の値。",
    ##################################################
    "<hr>": "<hr>",
    ##################################################
    "**[Examples]**": "**[コードサンプル]**",
    ##################################################
    "```py\n>>> import apysc as ap\n>>> arr: ap.Array = ap.Array([1, 3])\n>>> arr.insert_at(index=1, value=2)\n>>> arr\nArray([1, 2, 3])\n```": "```py\n>>> import apysc as ap\n>>> arr: ap.Array = ap.Array([1, 3])\n>>> arr.insert_at(index=1, value=2)\n>>> arr\nArray([1, 2, 3])\n```",  # noqa
}
