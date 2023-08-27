"""This module is for the translation mapping data of the
following document:

Document file: colorless.md
Language: jp
"""

from typing import Dict

MAPPING: Dict[str, str] = {
    ##################################################
    "# COLORLESS constant": "# COLORLESS 定数",
    ##################################################
    "This page explains the `COLORLESS` constant.": "このページでは `COLORLESS` 定数について説明します。",
    ##################################################
    "## What constant is this?": "## 定数の概要",
    ##################################################
    "The `COLORLESS` constant is the no-color setting.": "`COLORLESS`定数は無色の指定用の設定です。",
    ##################################################
    "If you set this constant to each color-related argument or property, the `apysc` clears its color.": "もし各色関係の引数や属性にこの定数を設定した場合、`apysc`ライブラリではその色の指定箇所で色を削除します。",  # noqa
    ##################################################
    "## Basic usage": "## 基本的な使い方",
    ##################################################
    "The `COLORLESS` constant is a subclass of the `Color` class.": "`COLORLESS`定数は`Color`クラスのサブクラスです。",  # noqa
    ##################################################
    "So, you can specify its constant to each color-related argument or property.": "そのため、色関係の引数や属性にこの定数を指定することができます。",  # noqa
    ##################################################
    "The `apysc` displays no color since the `fill_color` and `line_color` argument's values are the `COLORLESS` constant in the following example:": "以下の例では`fill_color`と`line_color`引数の各値に`COLORLESS`定数が指定されているため`apysc`ライブラリでは色を表示しません:",  # noqa
    ##################################################
    '```py\n# runnable\nimport apysc as ap\n\n_ = ap.Stage(\n    stage_width=150,\n    stage_height=150,\n    background_color=ap.Color("#333"),\n    stage_elem_id="stage",\n)\n_ = ap.Rectangle(\n    x=50,\n    y=50,\n    width=50,\n    height=50,\n    fill_color=ap.COLORLESS,\n    line_color=ap.COLORLESS,\n    line_thickness=3,\n)\n\nap.save_overall_html(dest_dir_path="./colorless_basic_usage/")\n```': '```py\n# runnable\nimport apysc as ap\n\n_ = ap.Stage(\n    stage_width=150,\n    stage_height=150,\n    background_color=ap.Color("#333"),\n    stage_elem_id="stage",\n)\n_ = ap.Rectangle(\n    x=50,\n    y=50,\n    width=50,\n    height=50,\n    fill_color=ap.COLORLESS,\n    line_color=ap.COLORLESS,\n    line_thickness=3,\n)\n\nap.save_overall_html(dest_dir_path="./colorless_basic_usage/")\n```',  # noqa
}
