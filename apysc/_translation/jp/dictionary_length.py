"""This module is for the translation mapping data of the
following document:

Document file: dictionary_length.md
Language: jp
"""

from typing import Dict

MAPPING: Dict[str, str] = {
    ##################################################
    "# Dictionary length interface": "# Dictionary クラスの length インターフェイス",
    ##################################################
    "This page explains the `Dictionary` class `length` property interface.": "このページでは`Dictionary`クラスの`length`属性のインターフェイスについて説明します。",  # noqa
    ##################################################
    "## What interface is this?": "## インターフェイス概要",
    ##################################################
    "The `length` property returns the length of dictionary keys.": "`length`属性は辞書のキーの長さ（件数）を返却します。",  # noqa
    ##################################################
    "## Basic usage": "## 基本的な使い方",
    ##################################################
    "The `length` property interface returns the `Int` value. There is no setter interface.": "`length`属性は`Int`型の整数を返却します。setterのインターフェイスは存在しません。",  # noqa
    ##################################################
    '```py\n# runnable\nimport apysc as ap\n\nap.Stage()\ndict_1: ap.Dictionary = ap.Dictionary({"a": 10, "b": 20})\nassert dict_1.length == 2\nassert isinstance(dict_1.length, ap.Int)\n```': '```py\n# runnable\nimport apysc as ap\n\nap.Stage()\ndict_1: ap.Dictionary = ap.Dictionary({"a": 10, "b": 20})\nassert dict_1.length == 2\nassert isinstance(dict_1.length, ap.Int)\n```',  # noqa
    ##################################################
    "## Note for the len function": "## len関数における特記事項",
    ##################################################
    "The Python built-in `len` function is not supported and raises an exception:": "Pythonビルトインの`len`関数はサポートされておらずエラーとなります:",  # noqa
    ##################################################
    '```py\nimport apysc as ap\n\ndict_1: ap.Dictionary = ap.Dictionary({"a": 10, "b": 20})\nlen(dict_1)\n```': '```py\nimport apysc as ap\n\ndict_1: ap.Dictionary = ap.Dictionary({"a": 10, "b": 20})\nlen(dict_1)\n```',  # noqa
    ##################################################
    "```\nException: Dictionary instance can't apply len function. Please use length property instead.\n```": "```\nException: Dictionary instance can't apply len function. Please use length property instead.\n```",  # noqa
    ##################################################
    "## length property API": "## length 属性のAPI",
    ##################################################
    '<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>': '<span class="inconspicuous-txt">特記事項: このAPIドキュメントはドキュメントビルド用のスクリプトによって自動で生成・同期されています。そのためもしかしたらこの節の内容は前節までの内容と重複している場合があります。</span>',  # noqa
    ##################################################
    "**[Interface summary]**": "**[インターフェイス概要]**",
    ##################################################
    "Get length of this dictionary values.<hr>": "辞書の値の長さ（件数）を取得します。<hr>",
    ##################################################
    "**[Returns]**": "**[返却値]**",
    ##################################################
    "- `length`: Int": "- `length`: Int",
    ##################################################
    "  - This dictionary value's length.": "  - この辞書の値の長さ。",
    ##################################################
    "<hr>": "<hr>",
    ##################################################
    "**[Examples]**": "**[コードサンプル]**",
    ##################################################
    '```py\n>>> import apysc as ap\n>>> _ = ap.Stage()\n>>> dictionary: ap.Dictionary = ap.Dictionary({"a": 1, "b": 2})\n>>> dictionary.length\nInt(2)\n```': '```py\n>>> import apysc as ap\n>>> _ = ap.Stage()\n>>> dictionary: ap.Dictionary = ap.Dictionary({"a": 1, "b": 2})\n>>> dictionary.length\nInt(2)\n```',  # noqa
}
