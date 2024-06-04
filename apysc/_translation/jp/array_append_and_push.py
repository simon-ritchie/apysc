"""This module is for the translation mapping data of the
following document:

Document file: array_append_and_push.md
Language: jp
"""

from typing import Dict

MAPPING: Dict[str, str] = {
    ##################################################
    "# Array class append and push interfaces": "# Array クラスの append と push のインターフェイス",
    ##################################################
    "This page explains the `Array` class `append` and `push` method interfaces.": "このページでは`Array`クラスの`append`と`push`メソッドの各インターフェイスについて説明します。",  # noqa
    ##################################################
    "## What interfaces are these?": "## 各インターフェイスの概要",
    ##################################################
    "The `append` and `push` method interfaces append any value to the end of an array. These interfaces behave the same (`append` is similar to the Python built-in and the `push` interface is similar to the JavaScript).": "`append`と`push`メソッドの各インターフェイスは配列の末端に任意の値を追加します。これらの各インターフェイスはお互いに同じ挙動をします（`append`はPython寄りな名前であり、`push`はJavaScript寄りな名前でエイリアスとして設けてあります）。",  # noqa
    ##################################################
    "## Basic usage": "## 基本的な使い方",
    ##################################################
    "The `append` and `push` methods require the first argument of the `value`\\.": "`append`と`push`の各メソッドは第一引数に`value`という引数名で追加する値の指定が必要になります。",  # noqa
    ##################################################
    "```py\n# runnable\nimport apysc as ap\n\nap.Stage()\narr: ap.Array[int] = ap.Array([1, 2])\narr.append(value=3)\nassert arr == [1, 2, 3]\n\narr.push(value=4)\nassert arr == [1, 2, 3, 4]\n```": "```py\n# runnable\nimport apysc as ap\n\nap.Stage()\narr: ap.Array[int] = ap.Array([1, 2])\narr.append(value=3)\nassert arr == [1, 2, 3]\n\narr.push(value=4)\nassert arr == [1, 2, 3, 4]\n```",  # noqa
    ##################################################
    "## append API": "## append API",
    ##################################################
    '<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>': '<span class="inconspicuous-txt">特記事項: このAPIドキュメントはドキュメントビルド用のスクリプトによって自動で生成・同期されています。そのためもしかしたらこの節の内容は前節までの内容と重複している場合があります。</span>',  # noqa
    ##################################################
    "**[Interface summary]**": "**[インターフェイス概要]**",
    ##################################################
    "Add any value to the end of this array. This method behaves the same `push` method.<hr>": "任意の値をこの配列の末尾に加えます。このメソッドは`push`メソッドと同様に動作します。<hr>",  # noqa
    ##################################################
    "**[Parameters]**": "**[引数]**",
    ##################################################
    "- `value`: *": "- `value`: *",
    ##################################################
    "  - Any value to append.": "  - 追加対象の任意の値。",
    ##################################################
    "<hr>": "<hr>",
    ##################################################
    "**[Examples]**": "**[コードサンプル]**",
    ##################################################
    "```py\n>>> import apysc as ap\n>>> _ = ap.Stage()\n>>> arr: ap.Array = ap.Array([1, 2, 3])\n>>> arr.append(4)\n>>> arr\nArray([1, 2, 3, 4])\n```": "```py\n>>> import apysc as ap\n>>> _ = ap.Stage()\n>>> arr: ap.Array = ap.Array([1, 2, 3])\n>>> arr.append(4)\n>>> arr\nArray([1, 2, 3, 4])\n```",  # noqa
    ##################################################
    "## push API": "## push API",
    ##################################################
    '<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>': '<span class="inconspicuous-txt">特記事項: このAPIドキュメントはドキュメントビルド用のスクリプトによって自動で生成・同期されています。そのためもしかしたらこの節の内容は前節までの内容と重複している場合があります。</span>',  # noqa
    ##################################################
    "**[Interface summary]**": "**[インターフェイス概要]**",
    ##################################################
    "Add any value to the end of this array. This interface behaves the same as the `append` method.<hr>": "任意の値をこの配列の末尾に加えます。このメソッドは`append`メソッドと同様に動作します。<hr>",  # noqa
    ##################################################
    "**[Parameters]**": "**[引数]**",
    ##################################################
    "- `value`: *": "- `value`: *",
    ##################################################
    "  - Any value to append.": "  - 追加対象の任意の値。",
    ##################################################
    "<hr>": "<hr>",
    ##################################################
    "**[Examples]**": "**[コードサンプル]**",
    ##################################################
    "```py\n>>> import apysc as ap\n>>> _ = ap.Stage()\n>>> arr: ap.Array = ap.Array([1, 2, 3])\n>>> arr.push(4)\n>>> arr\nArray([1, 2, 3, 4])\n```": "```py\n>>> import apysc as ap\n>>> _ = ap.Stage()\n>>> arr: ap.Array = ap.Array([1, 2, 3])\n>>> arr.push(4)\n>>> arr\nArray([1, 2, 3, 4])\n```",  # noqa
}
