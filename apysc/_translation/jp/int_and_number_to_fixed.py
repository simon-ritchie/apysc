"""This module is for the translation mapping data of the
following document:

Document file: int_and_number_to_fixed.md
Language: jp
"""

from typing import Dict

MAPPING: Dict[str, str] = {
    ##################################################
    "# Int and Number classes to_fixed interface": "# Int と Number クラスの to_fixed インターフェイス",  # noqa
    ##################################################
    "This page explains the `Int` and `Number` classes `to_fixed` method interface.": "このページでは`Int`と`Number`クラスの`to_fixed`メソッドのインターフェイスについて説明します。",  # noqa
    ##################################################
    "## What interface is this?": "## インターフェイス概要",
    ##################################################
    "The `to_fixed` method converts a number to a fixed floating-point string notation.": "`to_fixed`メソッドは数値を固定の桁数の浮動小数点数を持った文字列へと変換します。",  # noqa
    ##################################################
    "## Basic usage": "## 基本的な使い方",
    ##################################################
    "The `to_fixed` method requires a `digits` argument.": "`to_fixed`メソッドは`digits`引数の指定を必要とします。",  # noqa
    ##################################################
    "Its argument accepts between 0 to 100 range value.": "その引数は0～100の範囲の値を受け付けます。",
    ##################################################
    "If you specify 0 to the `digits` argument, a result string becomes an integer string.": "もし`digits`引数に0を指定した場合、結果の文字列は整数の形式の文字列になります。",  # noqa
    ##################################################
    "Also, if you set 2 to the `digits` argument, a result string becomes a number with two decimal places string (e.g., 10.34).": "また、`digits`引数に2を指定した場合には結果の文字列は小数点以下が2桁の数値の文字列になります（例 : 10.34）。",  # noqa
    ##################################################
    "This interface reflects even rounding to a truncated floating-point number.": "このインターフェイスは切り捨てられた浮動小数点数に偶数丸めの処理を反映します。",  # noqa
    ##################################################
    "For example, if a number is 10.678, and a `digits` argument is 2, a result string becomes 10.68.": "例えばもし数値が10.678であり`digits`引数がに2が指定されたばあぽ、結果の文字列は10.68になります。",  # noqa
    ##################################################
    '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    stage_width=0,\n    stage_height=0,\n    background_color=ap.Color("#333"),\n    stage_elem_id="stage",\n)\nnum: ap.Number = ap.Number(10.789)\nfixed_float_str: ap.String = num.to_fixed(digits=2)\nap.assert_equal(fixed_float_str, "10.79")\n\nfixed_float_str = num.to_fixed(digits=5)\nap.assert_equal(fixed_float_str, "10.78900")\n\nfixed_float_str = num.to_fixed(digits=0)\nap.assert_equal(fixed_float_str, "11")\n\nap.save_overall_html(dest_dir_path="to_fixed_basics_usage/")\n```': '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    stage_width=0,\n    stage_height=0,\n    background_color=ap.Color("#333"),\n    stage_elem_id="stage",\n)\nnum: ap.Number = ap.Number(10.789)\nfixed_float_str: ap.String = num.to_fixed(digits=2)\nap.assert_equal(fixed_float_str, "10.79")\n\nfixed_float_str = num.to_fixed(digits=5)\nap.assert_equal(fixed_float_str, "10.78900")\n\nfixed_float_str = num.to_fixed(digits=0)\nap.assert_equal(fixed_float_str, "11")\n\nap.save_overall_html(dest_dir_path="to_fixed_basics_usage/")\n```',  # noqa
    ##################################################
    "## to_fixed API": "## to_fixed API",
    ##################################################
    '<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>': '<span class="inconspicuous-txt">特記事項: このAPIドキュメントはドキュメントビルド用のスクリプトによって自動で生成・同期されています。そのためもしかしたらこの節の内容は前節までの内容と重複している場合があります。</span>',  # noqa
    ##################################################
    "**[Interface summary]**": "**[インターフェイス概要]**",
    ##################################################
    "Convert value to fixed floating point string notation.<hr>": "値を固定の小数点以下の桁数の文字列へと変換します。<hr>",  # noqa
    ##################################################
    "**[Parameters]**": "**[引数]**",
    ##################################################
    "- `digits`: int or Int": "- `digits`: int or Int",
    ##################################################
    "  - A floating point digit number (0 to 100 value is acceptable).": "  - 浮動小数点数の桁数（0～100の範囲の値を受け付けることができます）。",  # noqa
    ##################################################
    "- `variable_name_suffix`: str, optional": "- `variable_name_suffix`: str, optional",  # noqa
    ##################################################
    "  - A JavaScript variable name suffix string. This setting is sometimes useful for JavaScript debugging.": "  - JavaScript上の変数のサフィックスの設定です。この設定はJavaScriptのデバッグ時に役立つことがあります。",  # noqa
    ##################################################
    "<hr>": "<hr>",
    ##################################################
    "**[Returns]**": "**[返却値]**",
    ##################################################
    "- `result_str`: String": "- `result_str`: String",
    ##################################################
    "  - A converted string.": "  - 変換された文字列。",
    ##################################################
    "<hr>": "<hr>",
    ##################################################
    "**[Examples]**": "**[コードサンプル]**",
    ##################################################
    '```py\n>>> import apysc as ap\n>>> _ = ap.Stage()\n>>> num: ap.Number = ap.Number(10.789)\n>>> fixed_float_str: ap.String = num.to_fixed(digits=2)\n>>> fixed_float_str\nString("10.79")\n\n>>> fixed_float_str = num.to_fixed(digits=5)\n>>> fixed_float_str\nString("10.78900")\n\n>>> fixed_float_str = num.to_fixed(digits=0)\n>>> fixed_float_str\nString("11")\n```': '```py\n>>> import apysc as ap\n>>> _ = ap.Stage()\n>>> num: ap.Number = ap.Number(10.789)\n>>> fixed_float_str: ap.String = num.to_fixed(digits=2)\n>>> fixed_float_str\nString("10.79")\n\n>>> fixed_float_str = num.to_fixed(digits=5)\n>>> fixed_float_str\nString("10.78900")\n\n>>> fixed_float_str = num.to_fixed(digits=0)\n>>> fixed_float_str\nString("11")\n```',  # noqa
}
