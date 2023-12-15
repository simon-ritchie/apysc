"""This module is for the translation mapping data of the
following document:

Document file: array_extend_and_concat.md
Language: jp
"""

from typing import Dict

MAPPING: Dict[str, str] = {
    ##################################################
    "# Array class extend and concat interfaces": "# Array クラスの extend と concat のインターフェイス",  # noqa
    ##################################################
    "This page explains the `Array` class `extend` and `concat` method interfaces.": "このページでは`Array`クラスの`extend`と`concat`メソッドの各インターフェイスについて説明します。",  # noqa
    ##################################################
    "## What interfaces are these?": "## 各インターフェイスの概要",
    ##################################################
    "The `extend` and `concat` method interfaces are the two arrays' concatenation interfaces.": "`extend`と`concat`メソッドの各インターフェイスは2つの配列の連結処理を扱います。",  # noqa
    ##################################################
    "The `extend` method updates an original array in place and returns the `None`. The `concat` method returns the concatenated array, and an original one is not updated.": "`extend`メソッドは元々の配列自体を更新し返却値は設定されずNoneとなります。`concat`メソッドでは連結結果の配列を返却します。元の配列は変化しません。",  # noqa
    ##################################################
    "## Basic usage": "## 基本的な使い方",
    ##################################################
    "The `extend` and `concat` methods require other iterable objects, like the `list`\\, `tuple`\\, or `Array` value at the first argument, as follows:": "`extend`と`concat`メソッドは以下のコード例のようにそれぞれ第一引数に連結対象の他の配列など（ビルトインのリストやタプル、apyscの`Array`など）のオブジェクトを必要とします:",  # noqa
    ##################################################
    "```py\n# runnable\nimport apysc as ap\n\nap.Stage()\narr: ap.Array[int] = ap.Array([1, 2])\narr.extend([3, 4])\nassert arr == [1, 2, 3, 4]\n\nother_arr: ap.Array[int] = arr.concat([5, 6])\nassert other_arr == [1, 2, 3, 4, 5, 6]\nassert arr == [1, 2, 3, 4]\n```": "```py\n# runnable\nimport apysc as ap\n\nap.Stage()\narr: ap.Array[int] = ap.Array([1, 2])\narr.extend([3, 4])\nassert arr == [1, 2, 3, 4]\n\nother_arr: ap.Array[int] = arr.concat([5, 6])\nassert other_arr == [1, 2, 3, 4, 5, 6]\nassert arr == [1, 2, 3, 4]\n```",  # noqa
    ##################################################
    "## extend API": "## extend API",
    ##################################################
    '<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>': '<span class="inconspicuous-txt">特記事項: このAPIドキュメントはドキュメントビルド用のスクリプトによって自動で生成・同期されています。そのためもしかしたらこの節の内容は前節までの内容と重複している場合があります。</span>',  # noqa
    ##################################################
    "**[Interface summary]**": "**[インターフェイス概要]**",
    ##################################################
    "Concatenate argument array to this one. This interface positions the argument array's values after this array values. This method is similar to the concat method. Still, there is a difference in whether updating the same variable (extend) or returning as a different variable (concat).<hr>": "引数に指定された配列をこの配列へ連結します。このインターフェイスは引数の配列の値をこの配列の後に配置します。このメソッドはconcatメソッドと似た挙動をしますが、配列の値を直接更新するか（extend）もしくは別の値として返却するか（concat）の違いがあります。<hr>",  # noqa
    ##################################################
    "**[Parameters]**": "**[引数]**",
    ##################################################
    "- `other_arr`: Array or list or tuple or range": "- `other_arr`: Array or list or tuple or range",  # noqa
    ##################################################
    "  - Other array-like values to concatenate.": "  - 連結対象となる他の配列の（もしくはそれに近しい）値。",
    ##################################################
    "<hr>": "<hr>",
    ##################################################
    "**[Examples]**": "**[コードサンプル]**",
    ##################################################
    "```py\n>>> import apysc as ap\n>>> _ = ap.Stage()\n>>> arr: ap.Array = ap.Array([1, 2, 3])\n>>> arr.extend([4, 5, 6])\n>>> arr\nArray([1, 2, 3, 4, 5, 6])\n```": "```py\n>>> import apysc as ap\n>>> _ = ap.Stage()\n>>> arr: ap.Array = ap.Array([1, 2, 3])\n>>> arr.extend([4, 5, 6])\n>>> arr\nArray([1, 2, 3, 4, 5, 6])\n```",  # noqa
    ##################################################
    "## concat API": "## concat API",
    ##################################################
    '<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>': '<span class="inconspicuous-txt">特記事項: このAPIドキュメントはドキュメントビルド用のスクリプトによって自動で生成・同期されています。そのためもしかしたらこの節の内容は前節までの内容と重複している場合があります。</span>',  # noqa
    ##################################################
    "**[Interface summary]**": "**[インターフェイス概要]**",
    ##################################################
    "Concatenate argument array to this one. This interface positions the argument array's values after this array values. This method is similar to extend method, but there is a difference in whether updating the same variable (extend) or returning as a different variable (concat).<hr>": "引数に指定された配列をこの配列へ連結します。このインターフェイスは引数の配列の値をこの配列の後に配置します。このメソッドはextendメソッドと似た挙動をしますが、配列の値を直接更新するか（extend）もしくは別の値として返却するか（concat）の違いがあります。<hr>",  # noqa
    ##################################################
    "**[Parameters]**": "**[引数]**",
    ##################################################
    "- `other_arr`: Array or list or tuple": "- `other_arr`: Array or list or tuple",
    ##################################################
    "  - Other array-like values to concatenate.": "  - 連結対象となる他の配列の（もしくはそれに近しい）値。",
    ##################################################
    "<hr>": "<hr>",
    ##################################################
    "**[Returns]**": "**[返却値]**",
    ##################################################
    "- `concatenated`: Array": "- `concatenated`: Array",
    ##################################################
    "  - Concatenated array value.": "  - 連結結果の配列の値。.",
    ##################################################
    "<hr>": "<hr>",
    ##################################################
    "**[Examples]**": "**[コードサンプル]**",
    ##################################################
    "```py\n>>> import apysc as ap\n>>> _ = ap.Stage()\n>>> arr: ap.Array = ap.Array([1, 2, 3])\n>>> arr = arr.concat([4, 5, 6])\n>>> arr\nArray([1, 2, 3, 4, 5, 6])\n```": "```py\n>>> import apysc as ap\n>>> _ = ap.Stage()\n>>> arr: ap.Array = ap.Array([1, 2, 3])\n>>> arr = arr.concat([4, 5, 6])\n>>> arr\nArray([1, 2, 3, 4, 5, 6])\n```",  # noqa
}
