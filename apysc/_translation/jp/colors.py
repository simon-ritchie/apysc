"""This module is for the translation mapping data of the
following document:

Document file: colors.md
Language: jp
"""

from typing import Dict

MAPPING: Dict[str, str] = {
    ##################################################
    "# Colors class": "# Colors クラス",
    ##################################################
    "This page explains the `Colors` class.": "このページでは`Colors`クラスについて説明します。",
    ##################################################
    "## What class is this?": "## クラス概要",
    ##################################################
    "The `Colors` class has `Color` constants, such as the `BLACK_000000`, `GRAY_999999`, `WHITE_FFFFFF`, and `RED_FF0000`.": "`Colors`クラスは`BLACK_000000`や`GRAY_999999`、`WHITE_FFFFFF`、`RED_FF0000`などの`Color`クラスの各定数定義を持ちます。",  # noqa
    ##################################################
    "Each suffix is a hexadecimal color code of its color.": "各サフィックスはその色の16進数のカラーコードになっています。",  # noqa
    ##################################################
    "## Basic usage": "## 基本的な使い方",
    ##################################################
    "These class constants behave the same as a `Color` value.": "これらのクラス定数は`Color`クラスの値と同様に動作します。",  # noqa
    ##################################################
    "```py\n# runnable\nimport apysc as ap\n\nstage: ap.Stage = ap.Stage(\n    stage_width=150,\n    stage_height=150,\n    background_color=ap.Colors.GRAY_333333,\n    stage_elem_id=\"stage\",\n)\n\nrectangle: ap.Rectangle = ap.Rectangle(\n    x=50,\n    y=50,\n    width=50,\n    height=50,\n    fill_color=ap.Colors.CYAN_00FFFF,\n    line_color=ap.Colors.WHITE_FFFFFF,\n    line_thickness=3,\n)\n\nap.save_overall_html(dest_dir_path=\"./colors_basic_usage/\")\n```": "```py\n# runnable\nimport apysc as ap\n\nstage: ap.Stage = ap.Stage(\n    stage_width=150,\n    stage_height=150,\n    background_color=ap.Colors.GRAY_333333,\n    stage_elem_id=\"stage\",\n)\n\nrectangle: ap.Rectangle = ap.Rectangle(\n    x=50,\n    y=50,\n    width=50,\n    height=50,\n    fill_color=ap.Colors.CYAN_00FFFF,\n    line_color=ap.Colors.WHITE_FFFFFF,\n    line_thickness=3,\n)\n\nap.save_overall_html(dest_dir_path=\"./colors_basic_usage/\")\n```",  # noqa
    ##################################################
    "## Defined colors": "## 定義されている各色",
    ##################################################
    "`ap.Colors`:": "`ap.Colors`:",
    ##################################################
    "<details>\n<summary>Display the code block:</summary>": "<details>\n<summary>コードブロックを表示:</summary>",  # noqa
    ##################################################
    "```py\n# runnable\nimport apysc as ap\n\nRECT_SIZE: int = 25\nFONT_SIZE: int = 12\nOUTER_MARGIN: int = 20\n_: ap.Stage = ap.Stage(\n    background_color=ap.Color(\"#333\"),\n    stage_width=450,\n    stage_height=(len(ap.Colors.get_colors_members()) // 2) * (RECT_SIZE + 10)\n    + OUTER_MARGIN * 2\n    - 10,\n)\n\ni: int\nconstant_name: str\ncolor: ap.Color\nfor i, (constant_name, color) in enumerate(ap.Colors.get_colors_members()):\n    if i % 2 == 0:\n        x = 20\n    else:\n        x = 250\n    y: int = (i // 2) * (RECT_SIZE + 10) + 20\n    ap.Rectangle(\n        x=x,\n        y=y,\n        width=RECT_SIZE,\n        height=RECT_SIZE,\n        fill_color=color,\n        line_color=ap.Color(\"#fff\"),\n        line_thickness=1,\n        line_alpha=0.5,\n    )\n    ap.SVGText(\n        text=constant_name,\n        x=x + RECT_SIZE + 10,\n        y=y + RECT_SIZE / 2 + FONT_SIZE / 2 - 2,\n        font_size=FONT_SIZE,\n        fill_color=ap.Color(\"#ccc\"),\n    )\n\nap.save_overall_html(dest_dir_path=\"./colors_definitions/\")\n```": "```py\n# runnable\nimport apysc as ap\n\nRECT_SIZE: int = 25\nFONT_SIZE: int = 12\nOUTER_MARGIN: int = 20\n_: ap.Stage = ap.Stage(\n    background_color=ap.Color(\"#333\"),\n    stage_width=450,\n    stage_height=(len(ap.Colors.get_colors_members()) // 2) * (RECT_SIZE + 10)\n    + OUTER_MARGIN * 2\n    - 10,\n)\n\ni: int\nconstant_name: str\ncolor: ap.Color\nfor i, (constant_name, color) in enumerate(ap.Colors.get_colors_members()):\n    if i % 2 == 0:\n        x = 20\n    else:\n        x = 250\n    y: int = (i // 2) * (RECT_SIZE + 10) + 20\n    ap.Rectangle(\n        x=x,\n        y=y,\n        width=RECT_SIZE,\n        height=RECT_SIZE,\n        fill_color=color,\n        line_color=ap.Color(\"#fff\"),\n        line_thickness=1,\n        line_alpha=0.5,\n    )\n    ap.SVGText(\n        text=constant_name,\n        x=x + RECT_SIZE + 10,\n        y=y + RECT_SIZE / 2 + FONT_SIZE / 2 - 2,\n        font_size=FONT_SIZE,\n        fill_color=ap.Color(\"#ccc\"),\n    )\n\nap.save_overall_html(dest_dir_path=\"./colors_definitions/\")\n```",  # noqa
    ##################################################
    "</details>": "</details>",
}
