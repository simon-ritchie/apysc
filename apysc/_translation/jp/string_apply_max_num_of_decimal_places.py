"""This module is for the translation mapping data of the
following document:

Document file: string_apply_max_num_of_decimal_places.md
Language: jp
"""

from typing import Dict

MAPPING: Dict[str, str] = {
    ##################################################
    "# String class apply_max_num_of_decimal_places interface": "# String クラスの apply_max_num_of_decimal_places インターフェイス",  # noqa
    ##################################################
    "This page explains the `String` class `apply_max_num_of_decimal_places` method interface.": "このページでは`String`クラスの`apply_max_num_of_decimal_places`メソッドのインターフェイスについて説明します。",  # noqa
    ##################################################
    "## What interface is this?": "## インターフェイス概要",
    ##################################################
    "The `apply_max_num_of_decimal_places` method applies the maximum number of decimal places to a string.": "`apply_max_num_of_decimal_places`メソッドは文字列に対して浮動小数点数の最大桁数の条件を反映します。",  # noqa
    ##################################################
    "For instance, if a string is `123.45678` and the maximum number of decimal places is `3`, this interface returns `123.456`.": "例えば、もし文字列が`123.45678`で小数点数の最大桁数が`3`だった場合、このインターフェイスは`123.456`の文字列を返却します。",  # noqa
    ##################################################
    "If a string is not in float format, this interface returns the original string.": "もしも文字列が浮動小数点数のフォーマットではない場合、このインターフェイスは元の文字列をそのまま返却します。",  # noqa
    ##################################################
    "## Basic usage": "## 基本的な使い方",
    ##################################################
    "The `apply_max_num_of_decimal_places` method requires the `max_num_of_decimal_places` (maximum number of decimal places, `int` or `Int` type) argument.": "`apply_max_num_of_decimal_places`は`max_num_of_decimal_places`（浮動小数点数の最大桁数、`int`もしくは`Int`型）引数の指定を必要とします。",  # noqa
    ##################################################
    "And this interface returns a new `String` instance.": "また、このインターフェイスは`String`型の新しいインスタンスを返却します。",  # noqa
    ##################################################
    '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    stage_width=0,\n    stage_height=0,\n    background_color=ap.Color("#333"),\n    stage_elem_id="stage",\n)\n\nstring = ap.String("123.456")\nstring = string.apply_max_num_of_decimal_places(max_num_of_decimal_places=1)\nap.assert_equal(string, "123.4")\n\n# If a string is not a `float` value, this interface returns\n# the original string.\nstring = ap.String("abc")\nstring = string.apply_max_num_of_decimal_places(max_num_of_decimal_places=1)\nap.assert_equal(string, "abc")\n\nap.save_overall_html(\n    dest_dir_path="string_apply_max_num_of_decimal_places_basic_usage_1/"\n)\n```': '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    stage_width=0,\n    stage_height=0,\n    background_color=ap.Color("#333"),\n    stage_elem_id="stage",\n)\n\nstring = ap.String("123.456")\nstring = string.apply_max_num_of_decimal_places(max_num_of_decimal_places=1)\nap.assert_equal(string, "123.4")\n\n# If a string is not a `float` value, this interface returns\n# the original string.\nstring = ap.String("abc")\nstring = string.apply_max_num_of_decimal_places(max_num_of_decimal_places=1)\nap.assert_equal(string, "abc")\n\nap.save_overall_html(\n    dest_dir_path="string_apply_max_num_of_decimal_places_basic_usage_1/"\n)\n```',  # noqa
    ##################################################
    "## apply_max_num_of_decimal_places API": "## apply_max_num_of_decimal_places API",
    ##################################################
    '<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>': '<span class="inconspicuous-txt">特記事項: このAPIドキュメントはドキュメントビルド用のスクリプトによって自動で生成・同期されています。そのためもしかしたらこの節の内容は前節までの内容と重複している場合があります。</span>',  # noqa
    ##################################################
    "**[Interface summary]**": "**[インターフェイス概要]**",
    ##################################################
    "Apply a maximum number of decimal places limit to this string.<hr>": "この文字列に浮動小数点数の最大桁数の設定を反映します。<hr>",  # noqa
    ##################################################
    "**[Parameters]**": "**[引数]**",
    ##################################################
    "- `max_num_of_decimal_places`: Union[int, Int]": "- `max_num_of_decimal_places`: Union[int, Int]",  # noqa
    ##################################################
    "  - A maximum number of decimal places.": "  - 浮動小数点数の最大桁数。",
    ##################################################
    "- `variable_name_suffix`: str, optional": "- `variable_name_suffix`: str, optional",  # noqa
    ##################################################
    "  - A JavaScript variable name suffix string. This setting is sometimes useful for JavaScript debugging.": "  - JavaScript上の変数のサフィックスの設定です。この設定はJavaScriptのデバッグ時に役立つことがあります。",  # noqa
    ##################################################
    "<hr>": "<hr>",
    ##################################################
    "**[Returns]**": "**[返却値]**",
    ##################################################
    "- `string`: String": "- `string`: String",
    ##################################################
    "  - An applied string.": "  - 反映後の文字列。",
    ##################################################
    "<hr>": "<hr>",
    ##################################################
    "**[Examples]**": "**[コードサンプル]**",
    ##################################################
    '```py\n>>> import apysc as ap\n>>> _ = ap.Stage()\n>>> string = ap.String("123.456")\n>>> string = string.apply_max_num_of_decimal_places(max_num_of_decimal_places=1)\n>>> ap.assert_equal(string, "123.4")\n```': '```py\n>>> import apysc as ap\n>>> _ = ap.Stage()\n>>> string = ap.String("123.456")\n>>> string = string.apply_max_num_of_decimal_places(max_num_of_decimal_places=1)\n>>> ap.assert_equal(string, "123.4")\n```',  # noqa
}
