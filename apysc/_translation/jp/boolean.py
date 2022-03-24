"""This module is for the translation mapping data of the
following document:

Document file: boolean.md
Language: jp
"""

from typing import Dict

MAPPING: Dict[str, str] = {

    '# Boolean class':
    '# Boolean クラス',

    'This page explains the `Boolean` class.':
    'このページでは`Boolean`クラスについて説明します。',

    'Before reading on, maybe it is helpful to read the following page:':
    '事前に以下のページを確認しておくと読み進める上で役に立つかもしれません:',

    '- [Why the apysc library doesn\'t use the Python built-in data type](why_apysc_doesnt_use_python_builtin_data_type.md)':  # noqa
    '- [なぜapyscではPythonのビルトインのデータの型を使用していないのか](jp_why_apysc_doesnt_use_python_builtin_data_type.md)',  # noqa

    '## What is the Boolean class?':
    '## Boolean クラスの概要',

    'The `Boolean` class is the apysc boolean class. It can accept `bool` or `Boolean` values at the constructor, as follows:':  # noqa
    '`Boolean`クラスはapyscの真偽値のクラスです。コンストラクタの引数には以下のコード例のように`bool`や`Boolean`の値を受け付けます:',  # noqa

    '```py\n# runnable\nimport apysc as ap\n\nbool_1: ap.Boolean = ap.Boolean(True)\nassert bool_1\n\nbool_2: ap.Boolean = ap.Boolean(False)\nassert not bool_2\n\nbool_3: ap.Boolean = ap.Boolean(bool_1)\nassert bool_3\n```':  # noqa
    '```py\n# runnable\nimport apysc as ap\n\nbool_1: ap.Boolean = ap.Boolean(True)\nassert bool_1\n\nbool_2: ap.Boolean = ap.Boolean(False)\nassert not bool_2\n\nbool_3: ap.Boolean = ap.Boolean(bool_1)\nassert bool_3\n```',  # noqa

    '## Note for the Bool class alias':
    '## Boolクラスのエイリアスの特記事項',

    'The `Bool` class is the alias of the `Boolean` class. And it behaves the same as the `Boolean` class.':  # noqa
    '`Bool`クラスは`Boolean`クラスのエイリアスとなります。`Boolean`クラスと同じ挙動をします。',

    '```py\n# runnable\nimport apysc as ap\n\nassert ap.Boolean == ap.Bool\nassert ap.Boolean(True) == ap.Bool(True)\n```':  # noqa
    '```py\n# runnable\nimport apysc as ap\n\nassert ap.Boolean == ap.Bool\nassert ap.Boolean(True) == ap.Bool(True)\n```',  # noqa

    '## Boolean comparison':
    '## Boolean クラスの比較制御',

    'The `Boolean` comparison interface behaves like the Python built-in `bool` value.':  # noqa
    '`Boolean`クラスの比較のインターフェイスはPythonビルトインの`bool`クラスの値のように動作します。',

    'You can compare it with the equal comparison operator (`==`), and the `Boolean`\\, `bool`\\, `int`\\, `Int` types are acceptable, as follows:':  # noqa
    '等値の比較のオペレーター（`==`）を使って`Boolean`の値と比較することができ、以下のコード例のように`Boolean`や`bool`、`int`、`Int`などの型との比較を行うことができます:',  # noqa

    '```py\n# runnable\nimport apysc as ap\n\nbool_1: ap.Boolean = ap.Boolean(True)\nassert bool_1 == True  # noqa\nassert bool_1 == ap.Boolean(True)\nassert bool_1 == 1\nassert bool_1 == ap.Int(1)\n```':  # noqa
    '```py\n# runnable\nimport apysc as ap\n\nbool_1: ap.Boolean = ap.Boolean(True)\nassert bool_1 == True  # noqa\nassert bool_1 == ap.Boolean(True)\nassert bool_1 == 1\nassert bool_1 == ap.Int(1)\n```',  # noqa

    'Also, the not equal comparison operator (`!=`) is supported, as follows:':  # noqa
    '同様に以下のコード例のように非等値のオペレーター（`!=`）もサポートされています。',

    '```py\n# runnable\nimport apysc as ap\n\nbool_1: ap.Boolean = ap.Boolean(True)\nassert bool_1 != False  # noqa\nassert bool_1 != ap.Boolean(False)\nassert bool_1 != 0\nassert bool_1 != ap.Int(0)\n```':  # noqa
    '```py\n# runnable\nimport apysc as ap\n\nbool_1: ap.Boolean = ap.Boolean(True)\nassert bool_1 != False  # noqa\nassert bool_1 != ap.Boolean(False)\nassert bool_1 != 0\nassert bool_1 != ap.Int(0)\n```',  # noqa

    'You can skip the comparison operator, as follows:':
    '以下のコードのように比較のオペレーターを省略して使うこともできます:',

    '```py\n# runnable\nimport apysc as ap\n\nbool_1: ap.Boolean = ap.Boolean(True)\nassert bool_1\n\nbool_2: ap.Boolean = ap.Boolean(False)\nassert not bool_2\n```':  # noqa
    '```py\n# runnable\nimport apysc as ap\n\nbool_1: ap.Boolean = ap.Boolean(True)\nassert bool_1\n\nbool_2: ap.Boolean = ap.Boolean(False)\nassert not bool_2\n```',  # noqa

    '## Reverse a Boolean value':
    '## Boolean の値を反転させる',

    'The `not_` property returns the reversed `Boolean` value:':
    '`not_`属性は値が反転した`Boolean`の値を返却します:',

    '```py\n# runnable\nimport apysc as ap\n\nbool_1: ap.Boolean = ap.Boolean(True)\nbool_2: ap.Boolean = bool_1.not_\nassert not bool_2\n\nbool_3: ap.Boolean = bool_2.not_\nassert bool_3\n```':  # noqa
    '```py\n# runnable\nimport apysc as ap\n\nbool_1: ap.Boolean = ap.Boolean(True)\nbool_2: ap.Boolean = bool_1.not_\nassert not bool_2\n\nbool_3: ap.Boolean = bool_2.not_\nassert bool_3\n```',  # noqa

    '## Boolean class constructor API':
    '## Boolean クラスのコンストラクタのAPI',

    '<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>':  # noqa
    '<span class="inconspicuous-txt">特記事項: このAPIドキュメントはドキュメントビルド用のスクリプトによって自動で生成・同期されています。そのためもしかしたらこの節の内容は前節までの内容と重複している場合があります。</span>',  # noqa

    '**[Interface summary]** Boolean class for apysc library.<hr>':
    '**[インターフェイス概要]** apyscライブラリ用の真偽値のクラスです。<hr>',

    '**[Parameters]**':
    '**[引数]**',

    '- `value`: Boolean or Int or bool or int':
    '- `value`: Boolean or Int or bool or int',

    '  - Initial boolean value. 0 or 1 are acceptable for an integer value.':  # noqa
    '  - 真偽値の初期値。整数の場合は0か1が受け付けられます。',

    '<hr>':
    '<hr>',

    '**[Notes]**':
    '**[特記事項]**',

    'The Bool class is the alias of the Boolean, and it behaves the same as the Boolean class.<hr>':  # noqa
    'BoolクラスはBooleanクラスのエイリアスであり、Booleanクラスと同じように動作します。<hr>',

    '**[Examples]**':
    '**[コードサンプル]**',

    '```py\n>>> import apysc as ap\n>>> bool_val_1: ap.Boolean = ap.Boolean(True)\n>>> bool_val_1\nBoolean(True)\n\n>>> bool_val_2: ap.Bool = ap.Bool(True)\n>>> bool_val_2\nBoolean(True)\n```':  # noqa
    '```py\n>>> import apysc as ap\n>>> bool_val_1: ap.Boolean = ap.Boolean(True)\n>>> bool_val_1\nBoolean(True)\n\n>>> bool_val_2: ap.Bool = ap.Bool(True)\n>>> bool_val_2\nBoolean(True)\n```',  # noqa

    '## value property API':
    '## value 属性のAPI',

    '<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>':  # noqa
    '<span class="inconspicuous-txt">特記事項: このAPIドキュメントはドキュメントビルド用のスクリプトによって自動で生成・同期されています。そのためもしかしたらこの節の内容は前節までの内容と重複している場合があります。</span>',  # noqa

    '**[Interface summary]** Get a current boolean value.<hr>':
    '**[インターフェイス概要]** 現在の真偽値の値を取得します。<hr>',

    '**[Returns]**':
    '**[返却値]**',

    '- `value`: bool':
    '- `value`: bool',

    '  - Current boolean value.':
    '  - 現在の真偽値の値。',

    '<hr>':
    '<hr>',

    '**[Examples]**':
    '**[コードサンプル]**',

    '```py\n>>> import apysc as ap\n>>> bool_val: ap.Boolean = ap.Boolean(True)\n>>> bool_val.value = False\n>>> bool_val.value\nFalse\n\n>>> bool_val.value = ap.Boolean(True)\n>>> bool_val.value\nTrue\n```':  # noqa
    '```py\n>>> import apysc as ap\n>>> bool_val: ap.Boolean = ap.Boolean(True)\n>>> bool_val.value = False\n>>> bool_val.value\nFalse\n\n>>> bool_val.value = ap.Boolean(True)\n>>> bool_val.value\nTrue\n```',  # noqa

    '<hr>':
    '<hr>',

    '**[References]**':
    '**[関連資料]**',

    '- [apysc fundamental data classes value interface](https://simon-ritchie.github.io/apysc/fundamental_data_classes_value_interface.html)':  # noqa
    '- [apyscの基本的なデータクラスの value インターフェイス](https://simon-ritchie.github.io/apysc/jp_fundamental_data_classes_value_interface.html)',  # noqa

    '## not_ property API':
    '## not_ 属性のAPI',

    '<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>':  # noqa
    '<span class="inconspicuous-txt">特記事項: このAPIドキュメントはドキュメントビルド用のスクリプトによって自動で生成・同期されています。そのためもしかしたらこの節の内容は前節までの内容と重複している場合があります。</span>',  # noqa

    '**[Interface summary]** Get a not condition Boolean value.<hr>':
    '**[インターフェイス概要]** 反転（否定）させたBoolean型の真偽値を取得します。<hr>',

    '**[Returns]**':
    '**[返却値]**',

    '- `result`: Boolean':
    '- `result`: Boolean',

    '  - Not condition Boolean value.':
    '  - 反転（否定）させたBoolean型の値。',

    '<hr>':
    '<hr>',

    '**[Examples]**':
    '**[コードサンプル]**',

    '```py\n>>> import apysc as ap\n>>> bool_val: ap.Boolean = ap.Boolean(True)\n>>> bool_val.not_\nBoolean(False)\n\n>>> bool_val.value = False\n>>> bool_val.not_\nBoolean(True)\n```':  # noqa
    '```py\n>>> import apysc as ap\n>>> bool_val: ap.Boolean = ap.Boolean(True)\n>>> bool_val.not_\nBoolean(False)\n\n>>> bool_val.value = False\n>>> bool_val.not_\nBoolean(True)\n```',  # noqa

}
