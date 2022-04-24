"""This module is for the translation mapping data of the
following document:

Document file: string.md
Language: jp
"""

from typing import Dict

MAPPING: Dict[str, str] = {

    '# String class':
    '# String クラス',

    'This page explains the `String` class.':
    'このページでは`String`クラスについて説明します。',

    'Before reading on, maybe it is helpful to read the following page:':
    '事前に以下のページを確認しておくと読み進める上で役に立つかもしれません:',

    '- [Why the apysc library doesn\'t use the Python built-in data type](why_apysc_doesnt_use_python_builtin_data_type.md)':  # noqa
    '- [なぜapyscではPythonのビルトインのデータの型を使用していないのか](jp_why_apysc_doesnt_use_python_builtin_data_type.md)',  # noqa

    '## What is the String class?':
    '## String クラスの概要',

    'The `String` class is the apysc string class. It can accept `str` or `String` values at the constructor, as follows:':  # noqa
    '`String`クラスはapyscの文字列用のクラスです。このクラスは以下のコード例のようにコンストラクタの引数に`str`もしくは`String`型の値を受け付けます:',  # noqa

    '```py\n# runnable\nimport apysc as ap\n\nstring_1: ap.String = ap.String(\'Hello\')\nassert string_1 == \'Hello\'\n\nstring_2: ap.String = ap.String(string_1)\nassert string_2 == \'Hello\'\n```':  # noqa
    '```py\n# runnable\nimport apysc as ap\n\nstring_1: ap.String = ap.String(\'Hello\')\nassert string_1 == \'Hello\'\n\nstring_2: ap.String = ap.String(string_1)\nassert string_2 == \'Hello\'\n```',  # noqa

    '## String class interfaces':
    '## String クラスの各インターフェイス',

    'For more details about the `String` class each interface, please see the following:':  # noqa
    '`String`クラスの各インターフェイスの詳細については以下の資料などをご確認ください:',

    '- [String class comparison operations](string_comparison_operations.md)':  # noqa
    '- [String クラスの比較制御](jp_string_comparison_operations.md)',

    '- [String class addition and multiplication operations](string_addition_and_multiplication.md)':  # noqa
    '- [String クラスの加算と乗算の制御](jp_string_addition_and_multiplication.md)',

    '## String class constructor API':
    '## String クラスのコンストラクタのAPI',

    '<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>':  # noqa
    '<span class="inconspicuous-txt">特記事項: このAPIドキュメントはドキュメントビルド用のスクリプトによって自動で生成・同期されています。そのためもしかしたらこの節の内容は前節までの内容と重複している場合があります。</span>',  # noqa

    '**[Interface summary]** String class for apysc library.<hr>':
    '**[インターフェイス概要]** apyscライブラリにおける文字列用のクラスです。<hr>',

    '**[Parameters]**':
    '**[引数]**',

    '- `value`: String or str':
    '- `value`: String or str',

    '  - Initial string value.':
    '  - 文字列の値の初期値。',

    '<hr>':
    '<hr>',

    '**[Examples]**':
    '**[コードサンプル]**',

    '```py\n>>> import apysc as ap\n>>> string: ap.String = ap.String(\'Hello\')\n>>> string\nString(\'Hello\')\n\n>>> string += \' World!\'\n>>> string\nString(\'Hello World!\')\n```':  # noqa
    '```py\n>>> import apysc as ap\n>>> string: ap.String = ap.String(\'Hello\')\n>>> string\nString(\'Hello\')\n\n>>> string += \' World!\'\n>>> string\nString(\'Hello World!\')\n```',  # noqa

    '<hr>':
    '<hr>',

    '**[References]**':
    '**[関連資料]**',

    '- [String class comparison operations document](https://simon-ritchie.github.io/apysc/string_comparison_operations.html)':  # noqa
    '- [String クラスの比較制御](https://simon-ritchie.github.io/apysc/jp_string_comparison_operations.html)',  # noqa

    '- [String class addition and multiplication operations document](https://simon-ritchie.github.io/apysc/string_addition_and_multiplication.html)':  # noqa
    '- [String クラスの加算と乗算の制御](https://simon-ritchie.github.io/apysc/jp_string_addition_and_multiplication.html)',  # noqa

    '## value property API':
    '## value 属性のAPI',

    '<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>':  # noqa
    '<span class="inconspicuous-txt">特記事項: このAPIドキュメントはドキュメントビルド用のスクリプトによって自動で生成・同期されています。そのためもしかしたらこの節の内容は前節までの内容と重複している場合があります。</span>',  # noqa

    '**[Interface summary]** Get a current string value.<hr>':
    '**[インターフェイス概要]** 現在の文字列の値を取得します。<hr>',

    '**[Returns]**':
    '**[返却値]**',

    '- `value`: str':
    '- `value`: str',

    '  - Current string value.':
    '  - 現在の文字列の値。',

    '<hr>':
    '<hr>',

    '**[Examples]**':
    '**[コードサンプル]**',

    '```py\n>>> import apysc as ap\n>>> string: ap.String = ap.String(\'Hello\')\n>>> string.value = \'World!\'\n>>> string.value\n\'World!\'\n```':  # noqa
    '```py\n>>> import apysc as ap\n>>> string: ap.String = ap.String(\'Hello\')\n>>> string.value = \'World!\'\n>>> string.value\n\'World!\'\n```',  # noqa

    '<hr>':
    '<hr>',

    '**[References]**':
    '**[関連資料]**',

    '- [apysc fundamental data classes value interface](https://simon-ritchie.github.io/apysc/fundamental_data_classes_value_interface.html)':  # noqa
    '- [apyscの基本的なデータクラスの value インターフェイス](https://simon-ritchie.github.io/apysc/jp_fundamental_data_classes_value_interface.html)',  # noqa

}
