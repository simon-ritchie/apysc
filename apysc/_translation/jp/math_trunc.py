"""This module is for the translation mapping data of the
following document:

Document file: math_trunc.md
Language: jp
"""

from typing import Dict

MAPPING: Dict[str, str] = {
    ##################################################
    "# Math trunc interface": "# Math クラスの trunc インターフェイス",
    ##################################################
    "This page explains the `Math` class's `trunc` class method interface.": "このページでは`Math`クラスの`trunc`クラスメソッドのインターフェイスについて説明します。",  # noqa
    ##################################################
    "## What interface is this?": "## インターフェイス概要",
    ##################################################
    "The `trunc` class method interface truncates a fraction value and returns an integer value.": "`trunc`クラスメソッドのインターフェイスは指定された値の小数点以下の値を切り捨てて整数の値を返却します。",  # noqa
    ##################################################
    "## Basic usage": "## 基本的な使い方",
    ##################################################
    "The `trunc` interface requires `Int`, `Number`, `String`, or `Boolean` value argument.": "`trunc`インターフェイスは`Int`、`Number`、`String`、もしくは`Boolean`のいずれかの型の値の引数を必要とします。",  # noqa
    ##################################################
    "If an argument is a `Number` or `String` value, this interface truncates a fraction value and converts it to the `Int` type.": "もしも引数の値が`Number`もしくは`String`型の値であればこのインターフェイスは小数点以下の値を切り捨てて`Int`型に変換した状態で返却します。",  # noqa
    ##################################################
    "If an argument is a `Boolean` value, this interface returns 0 or 1 `Int` value.": "もしも引数の値が`Boolean`の型の値であれば、このインターフェイスは0もしくは1の`Int`型の値を返却します。",  # noqa
    ##################################################
    '```py\n# runnable\nimport apysc as ap\n\nap.Stage()\nresult_int: ap.Int = ap.Math.trunc(value=ap.Int(10))\nassert result_int == 10\n\nresult_int = ap.Math.trunc(value=ap.Number(8.5))\nassert result_int == 8\n\nresult_int = ap.Math.trunc(value=ap.String("7.6"))\nassert result_int == 7\n\nresult_int = ap.Math.trunc(value=ap.Boolean(True))\nassert result_int == 1\n```': '```py\n# runnable\nimport apysc as ap\n\nap.Stage()\nresult_int: ap.Int = ap.Math.trunc(value=ap.Int(10))\nassert result_int == 10\n\nresult_int = ap.Math.trunc(value=ap.Number(8.5))\nassert result_int == 8\n\nresult_int = ap.Math.trunc(value=ap.String("7.6"))\nassert result_int == 7\n\nresult_int = ap.Math.trunc(value=ap.Boolean(True))\nassert result_int == 1\n```',  # noqa
    ##################################################
    "## Math.trunc API": "## Math.trunc のAPI",
    ##################################################
    '<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>': '<span class="inconspicuous-txt">特記事項: このAPIドキュメントはドキュメントビルド用のスクリプトによって自動で生成・同期されています。そのためもしかしたらこの節の内容は前節までの内容と重複している場合があります。</span>',  # noqa
    ##################################################
    "**[Interface summary]**": "**[インターフェイス概要]**",
    ##################################################
    "Truncate a fraction value from a specified value.<hr>": "指定された値から小数点以下の値を切り落とします。<hr>",  # noqa
    ##################################################
    "**[Parameters]**": "**[引数]**",
    ##################################################
    "- `value`: Union[Int, Number, String, Boolean]": "- `value`: Union[Int, Number, String, Boolean]",  # noqa
    ##################################################
    "  - A value to truncate a fraction value. If a specified value is the `Number`'s, `String`'s, or `Boolean`'s type, the return value becomes an `Int`'s value.": "  - 小数点以下を切り捨てる対象の値。もし指定された値が`Number`、`String`、もしくは`Boolean`型の値の場合、変逆値は`Int`型の値となります。",  # noqa
    ##################################################
    "<hr>": "<hr>",
    ##################################################
    "**[Returns]**": "**[返却値]**",
    ##################################################
    "- `result`: Int": "- `result`: Int",
    ##################################################
    "  - Truncated and converted to `Int`'s value.": "  - 切り捨て処理と`Int`型への変換が反映された値。",
    ##################################################
    "<hr>": "<hr>",
    ##################################################
    "**[Examples]**": "**[コードサンプル]**",
    ##################################################
    '```py\n>>> import apysc as ap\n>>> _ = ap.Stage()\n>>> result_int: ap.Int = ap.Math.trunc(value=ap.Int(10))\n>>> result_int\nInt(10)\n\n>>> result_int = ap.Math.trunc(value=ap.Number(8.5))\n>>> result_int\nInt(8)\n\n>>> result_int = ap.Math.trunc(value=ap.String("7.6"))\n>>> result_int\nInt(7)\n\n>>> result_int = ap.Math.trunc(value=ap.Boolean(True))\n>>> result_int\nInt(1)\n\n>>> result_int = ap.Math.trunc(value=ap.Boolean(False))\n>>> result_int\nInt(0)\n```': '```py\n>>> import apysc as ap\n>>> _ = ap.Stage()\n>>> result_int: ap.Int = ap.Math.trunc(value=ap.Int(10))\n>>> result_int\nInt(10)\n\n>>> result_int = ap.Math.trunc(value=ap.Number(8.5))\n>>> result_int\nInt(8)\n\n>>> result_int = ap.Math.trunc(value=ap.String("7.6"))\n>>> result_int\nInt(7)\n\n>>> result_int = ap.Math.trunc(value=ap.Boolean(True))\n>>> result_int\nInt(1)\n\n>>> result_int = ap.Math.trunc(value=ap.Boolean(False))\n>>> result_int\nInt(0)\n```',  # noqa
}
