"""This module is for the translation mapping data of the
following document:

Document file: dictionary_get.md
Language: jp
"""

from typing import Dict

MAPPING: Dict[str, str] = {
    ##################################################
    "# Dictionary get interface": "# Dictionary クラスの get インターフェイス",
    ##################################################
    "This page explains the `Dictionary` class `get` method interface.": "このページでは`Dictionary`クラスの`get`メソッドのインターフェイスについて説明します。",  # noqa
    ##################################################
    "## What interface is this?": "## インターフェイス概要",
    ##################################################
    "The `get` method returns the specified key's value. If that key does not exist in the dictionary, it returns the default value (not raising an exception).": "`get`メソッドは引数に指定されたキーの値を返却します。もし指定されたキーが辞書内に存在しなければデフォルトの値を返却します（キーが無くともエラーにはなりません）。",  # noqa
    ##################################################
    "## Basic usage": "## 基本的な使い方",
    ##################################################
    "The `get` method requires the first argument, `key` (dictionary key). The second argument of the `default` is optional, and if not provided, it returns the `None` value.": "`get`メソッドは`key`（辞書のキー）の第一引数を必要とします。第二引数の`default`引数は省略可で、もし指定されなければ`None`がデフォルト値となります。",  # noqa
    ##################################################
    '```py\n# runnable\nfrom typing import Any, Optional\n\nimport apysc as ap\n\ndict_val: ap.Dictionary = ap.Dictionary({"a": 10})\ngot_val_1: int = dict_val.get(key="a", default=0)\nassert got_val_1 == 10\n\ngot_val_2: int = dict_val.get(key="b", default=0)\nassert got_val_2 == 0\n\ngot_val_3: Optional[Any] = dict_val.get(key="b")\nassert got_val_3 is None\n```': '```py\n# runnable\nfrom typing import Any, Optional\n\nimport apysc as ap\n\ndict_val: ap.Dictionary = ap.Dictionary({"a": 10})\ngot_val_1: int = dict_val.get(key="a", default=0)\nassert got_val_1 == 10\n\ngot_val_2: int = dict_val.get(key="b", default=0)\nassert got_val_2 == 0\n\ngot_val_3: Optional[Any] = dict_val.get(key="b")\nassert got_val_3 is None\n```',  # noqa
    ##################################################
    "## get API": "## get API",
    ##################################################
    '<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>': '<span class="inconspicuous-txt">特記事項: このAPIドキュメントはドキュメントビルド用のスクリプトによって自動で生成・同期されています。そのためもしかしたらこの節の内容は前節までの内容と重複している場合があります。</span>',  # noqa
    ##################################################
    "**[Interface summary]**": "**[インターフェイス概要]**",
    ##################################################
    "Get a specified key dictionary value. If this dictionary hasn't a specified key, this interface returns a default value.<hr>": "指定されたキーの辞書内の値を取得します。もし指定されたキーが辞書に存在しない場合、このインターフェイスはデフォルト値を返却します。<hr>",  # noqa
    ##################################################
    "**[Parameters]**": "**[引数]**",
    ##################################################
    "- `key`: _Key": "- `key`: _Key",
    ##################################################
    "  - Target key.": "  - 対象のキー。",
    ##################################################
    "- `default`: DefaultType or None, optional": "- `default`: DefaultType or None, optional",  # noqa
    ##################################################
    "  - Any default value.": "  - 任意のデフォルト値の値。",
    ##################################################
    "<hr>": "<hr>",
    ##################################################
    "**[Returns]**": "**[返却値]**",
    ##################################################
    "- `result_value`: Any": "- `result_value`: Any",
    ##################################################
    "  - Extracted value or a default value.": "  - 抽出された値もしくはデフォルト値。",
    ##################################################
    "<hr>": "<hr>",
    ##################################################
    "**[Examples]**": "**[コードサンプル]**",
    ##################################################
    '```py\n>>> from typing import Optional\n>>> import apysc as ap\n>>> dictionary: ap.Dictionary = ap.Dictionary({"a": 10})\n>>> value_1: Optional[int] = dictionary.get("a")\n>>> value_1\n10\n\n>>> value_2: Optional[int] = dictionary.get("b")\n>>> print(value_2)\nNone\n\n>>> value_3: int = dictionary.get("c", default=0)\n>>> value_3\n0\n```': '```py\n>>> from typing import Optional\n>>> import apysc as ap\n>>> dictionary: ap.Dictionary = ap.Dictionary({"a": 10})\n>>> value_1: Optional[int] = dictionary.get("a")\n>>> value_1\n10\n\n>>> value_2: Optional[int] = dictionary.get("b")\n>>> print(value_2)\nNone\n\n>>> value_3: int = dictionary.get("c", default=0)\n>>> value_3\n0\n```',  # noqa
}
