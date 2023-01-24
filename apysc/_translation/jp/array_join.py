"""This module is for the translation mapping data of the
following document:

Document file: array_join.md
Language: jp
"""

from typing import Dict

MAPPING: Dict[str, str] = {
    ##################################################
    "# Array class join interface": "# Array クラスの join インターフェイス",
    ##################################################
    "This page explains the `Array` class `join` method interface.": "このページでは`Array`クラスの`join`メソッドのインターフェイスについて説明します。",  # noqa
    ##################################################
    "## What interface is this?": "## インターフェイス概要",
    ##################################################
    "The `join` method returns a joined `String` with the specified separator string.": "`join`メソッドは引数に指定された区切り文字で連結された配列の値の`String`クラスの文字列を返却します。",  # noqa
    ##################################################
    "## Basic usage": "## 基本的な使い方",
    ##################################################
    "The `join` method requires the `sep` argument as the separator, as follows:": "`join`メソッドは以下のコード例のように区切り文字としての`sep`引数が必要になります。",  # noqa
    ##################################################
    '```py\n# runnable\nimport apysc as ap\n\narr: ap.Array[int] = ap.Array([1, 2, 3])\njoined: ap.String = arr.join(sep=",")\nassert joined == "1,2,3"\n```': '```py\n# runnable\nimport apysc as ap\n\narr: ap.Array[int] = ap.Array([1, 2, 3])\njoined: ap.String = arr.join(sep=",")\nassert joined == "1,2,3"\n```',  # noqa
    ##################################################
    "## join API": "## join API",
    ##################################################
    '<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>': '<span class="inconspicuous-txt">特記事項: このAPIドキュメントはドキュメントビルド用のスクリプトによって自動で生成・同期されています。そのためもしかしたらこの節の内容は前節までの内容と重複している場合があります。</span>',  # noqa
    ##################################################
    "**[Interface summary]**": "**[インターフェイス概要]**",
    ##################################################
    "Join this array value with a specified separator string.<hr>": "指定された区切り用の文字列を使って配列の値を連結します。<hr>",  # noqa
    ##################################################
    "**[Parameters]**": "**[引数]**",
    ##################################################
    "- `sep`: String or str": "- `sep`: String or str",
    ##################################################
    "  - Separator string.": "  - 区切り文字。",
    ##################################################
    "<hr>": "<hr>",
    ##################################################
    "**[Returns]**": "**[返却値]**",
    ##################################################
    "- `joined`: String": "- `joined`: String",
    ##################################################
    "  - Joined string.": "  - 連結された文字列。",
    ##################################################
    "<hr>": "<hr>",
    ##################################################
    "**[Examples]**": "**[コードサンプル]**",
    ##################################################
    "```py\n>>> import apysc as ap\n>>> arr: ap.Array = ap.Array([1, 2, 3])\n>>> arr.join(sep=\", \")\nString('1, 2, 3')\n```": "```py\n>>> import apysc as ap\n>>> arr: ap.Array = ap.Array([1, 2, 3])\n>>> arr.join(sep=\", \")\nString('1, 2, 3')\n```",  # noqa
}
