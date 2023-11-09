"""This module is for the translation mapping data of the
following document:

Document file: true_and_false.md
Language: jp
"""

from typing import Dict

MAPPING: Dict[str, str] = {
    ##################################################
    "# True_ and False_ constants": "# True_ と False_ の各定数",
    ##################################################
    "This page explains the `ap.True_` and `ap.False_` constants.": "このページでは`ap.True_`と`ap.False_`の各定数について説明します。",  # noqa
    ##################################################
    "## What constants are these?": "## 各定数の概要",
    ##################################################
    "The `ap.True_` is the constant that indicates `Boolean`'s `True` value (it is almost the same as `ap.Boolean(True)`).": "`ap.True_`は`Boolean`の`True`の値を示すたの定数値です（これは`ap.Boolean(True)`とほぼ同じ値となります）。",  # noqa
    ##################################################
    "Conversely, the `ap.False_` is the constant that indicates `Boolean`'s `False` value.": "反対に、`ap.False_`は`Boolean`の`False`の値を示すための定数となります。",  # noqa
    ##################################################
    "## Basic usage": "## 基本的な使い方",
    ##################################################
    "The `True_` and `False_` constants behave like `ap.Boolean(True)` and `ap.Boolean(False)`.": "`True_`と`False_`の各定数は`ap.Boolean(True)`や`ap.Boolean(False)`などと同じように振る舞います。",  # noqa
    ##################################################
    "A function or method that takes a `Boolean` argument can accept these constants.": "`Boolean`の引数を取る関数やメソッドなどではこれらの定数を指定することができます。",  # noqa
    ##################################################
    '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    stage_width=100,\n    stage_height=50,\n    background_color=ap.Color("#333"),\n    stage_elem_id="stage",\n)\ntext: ap.SvgText = ap.SvgText(\n    text="Hello!",\n    x=10,\n    y=31,\n    fill_color=ap.Color("#aaa"),\n    bold=ap.True_,\n    italic=ap.False_,\n)\n\nap.save_overall_html(dest_dir_path="true_and_false_basic_usage/")\n```': '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    stage_width=100,\n    stage_height=50,\n    background_color=ap.Color("#333"),\n    stage_elem_id="stage",\n)\ntext: ap.SvgText = ap.SvgText(\n    text="Hello!",\n    x=10,\n    y=31,\n    fill_color=ap.Color("#aaa"),\n    bold=ap.True_,\n    italic=ap.False_,\n)\n\nap.save_overall_html(dest_dir_path="true_and_false_basic_usage/")\n```',  # noqa
}
