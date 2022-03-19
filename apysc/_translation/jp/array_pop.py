"""This module is for the translation mapping data of the
following document:

Document file: array_pop.md
Language: jp
"""

from typing import Dict

MAPPING: Dict[str, str] = {

    '# Array class pop interface':
    '# Array クラスの pop インターフェイス',

    'This page explains the `Array` class `pop` method interface.':
    'このページでは`Array`クラスの`pop`メソッドのインターフェイスについて説明します。',

    '## What interface is this?':
    '## インターフェイス概要',

    'The `pop` method interface removes the last value from an array and returns that value.':  # noqa
    '`pop`メソッドは配列内の最後の値を配列から取り除き、そしてその取り除いた値を返却します。',

    '## Basic usage':
    '## 基本的な使い方',

    'The `pop` method accepts no arguments and returns the last value, as follows:':  # noqa
    '`pop`メソッドには必要な引数は無く、以下のコード例のように配列の最後の値を返却します:',

    '```py\n# runnable\nimport apysc as ap\n\narr: ap.Array[int] = ap.Array([1, 2, 3])\nlast_value: int = arr.pop()\nassert last_value == 3\n```':  # noqa
    '```py\n# runnable\nimport apysc as ap\n\narr: ap.Array[int] = ap.Array([1, 2, 3])\nlast_value: int = arr.pop()\nassert last_value == 3\n```',  # noqa

    '## pop API':
    '## pop API',

    '<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>':  # noqa
    '<span class="inconspicuous-txt">特記事項: このAPIドキュメントはドキュメントビルド用のスクリプトによって自動で生成・同期されています。そのためもしかしたらこの節の内容は前節までの内容と重複している場合があります。</span>',  # noqa

    '**[Interface summary]** Remove this array\'s last value and return it.<hr>':  # noqa
    '**[インターフェイス概要]** 配列の最後の値を配列から取り除き、その値を返却します。<hr>',

    '**[Returns]**':
    '**[返却値]**',

    '- `value`: *':
    '- `value`: *',

    '  - Removed value.':
    '  - 取り除かれた値。',

    '<hr>':
    '<hr>',

    '**[Examples]**':
    '**[コードサンプル]**',

    '```py\n>>> import apysc as ap\n>>> arr: ap.Array = ap.Array([1, 2, 3])\n>>> popped_val: int = arr.pop()\n>>> popped_val\n3\n\n>>> arr\nArray([1, 2])\n```':  # noqa
    '```py\n>>> import apysc as ap\n>>> arr: ap.Array = ap.Array([1, 2, 3])\n>>> popped_val: int = arr.pop()\n>>> popped_val\n3\n\n>>> arr\nArray([1, 2])\n```',  # noqa

}
