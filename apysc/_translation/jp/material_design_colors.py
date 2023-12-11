"""This module is for the translation mapping data of the
following document:

Document file: material_design_colors.md
Language: jp
"""

from typing import Dict

MAPPING: Dict[str, str] = {
    ##################################################
    "# MaterialDesignColors class": "# MaterialDesignColors クラス",
    ##################################################
    "This page explains the `MaterialDesignColors` class.": "このページでは`MaterialDesignColors`クラスについて説明します。",  # noqa
    ##################################################
    "## What class is this?": "## クラス概要",
    ##################################################
    "The `MaterialDesignColors` class has material design's `Color` constants, such as the `RED_100_FFCDD2`, `RED_300_E57373`, `INDIGO_800_283593`, and `INDIGO_A200_536DFE`.": "`MaterialDesignColors`クラスは`RED_100_FFCDD2`や`RED_300_E57373`、`INDIGO_800_283593`、`INDIGO_A200_536DFE`などのマテリアルデザインの色の定数を持ちます。",  # noqa
    ##################################################
    "Each suffix is a hexadecimal color code of its color.": "各サフィックスはその色の16進数のカラーコードになっています。",  # noqa
    ##################################################
    "## Basic usage": "## 基本的な使い方",
    ##################################################
    "These class constants behave the same as a `Color` value.": "これらのクラス定数は`Color`クラスの値と同様に動作します。",  # noqa
    ##################################################
    '```py\n# runnable\nimport apysc as ap\n\nstage: ap.Stage = ap.Stage(\n    stage_width=150,\n    stage_height=150,\n    background_color=ap.MaterialDesignColors.GRAY_800_424242,\n    stage_elem_id="stage",\n)\n\nrectangle: ap.Rectangle = ap.Rectangle(\n    x=50,\n    y=50,\n    width=50,\n    height=50,\n    fill_color=ap.MaterialDesignColors.CYAN_200_80DEEA,\n    line_color=ap.MaterialDesignColors.WHITE_FFFFFF,\n    line_thickness=3,\n)\n\nap.save_overall_html(dest_dir_path="./material_design_colors_basic_usage/")\n```': '```py\n# runnable\nimport apysc as ap\n\nstage: ap.Stage = ap.Stage(\n    stage_width=150,\n    stage_height=150,\n    background_color=ap.MaterialDesignColors.GRAY_800_424242,\n    stage_elem_id="stage",\n)\n\nrectangle: ap.Rectangle = ap.Rectangle(\n    x=50,\n    y=50,\n    width=50,\n    height=50,\n    fill_color=ap.MaterialDesignColors.CYAN_200_80DEEA,\n    line_color=ap.MaterialDesignColors.WHITE_FFFFFF,\n    line_thickness=3,\n)\n\nap.save_overall_html(dest_dir_path="./material_design_colors_basic_usage/")\n```',  # noqa
    ##################################################
    "## Defined colors": "## 定義されている各色",
    ##################################################
    "<br>\n<details>\n<summary>Display the code block:</summary>": "<br>\n<details>\n<summary>コードブロックを表示:</summary>",  # noqa
    ##################################################
    '```py\n# runnable\nfrom typing import List, Tuple\n\nimport apysc as ap\n\nRECT_SIZE: int = 25\nFONT_SIZE: int = 12\nOUTER_MARGIN: int = 20\n_: ap.Stage = ap.Stage(\n    background_color=ap.Color("#333"),\n    stage_width=700,\n    stage_height=((len(ap.MaterialDesignColors.get_colors_members()) + 1) // 2)\n    * (RECT_SIZE + 10)\n    + OUTER_MARGIN * 2\n    - 10,\n)\n\ncolor: ap.Color\ncolors_members: List[\n    Tuple[str, ap.Color]\n] = ap.MaterialDesignColors.get_colors_members()\ncolor_names: List[ap.String] = []\ncolors: List[ap.Color] = []\nfor color_name, color in colors_members:\n    color_names.append(ap.String(color_name))\n    colors.append(color)\nconstant_names_arr: ap.Array[ap.String] = ap.Array(color_names)\ncolors_arr: ap.Array[ap.Color] = ap.Array(colors)\n\ni: ap.Int\nx: ap.Number = ap.Number(0)\ny: ap.Number = ap.Number(0)\nwith ap.ForArrayIndices(constant_names_arr) as i:\n    with ap.If(i % 2 == 0):\n        x.value = OUTER_MARGIN\n    with ap.Else():\n        x.value = 350\n    y.value = (i // 2) * (RECT_SIZE + 10) + 20\n    color = colors_arr[i]\n    constant_name: ap.String = constant_names_arr[i]\n    ap.Rectangle(\n        x=x,\n        y=y,\n        width=RECT_SIZE,\n        height=RECT_SIZE,\n        fill_color=color,\n        line_color=ap.Color("#fff"),\n        line_thickness=1,\n        line_alpha=0.5,\n    )\n    ap.SvgText(\n        text=constant_name,\n        x=x + RECT_SIZE + 10,\n        y=y + RECT_SIZE / 2 + FONT_SIZE / 2 - 2,\n        font_size=FONT_SIZE,\n        fill_color=ap.Color("#ccc"),\n    )\n\nap.save_overall_html(dest_dir_path="./material_design_colors_definitions/")\n```': '```py\n# runnable\nfrom typing import List, Tuple\n\nimport apysc as ap\n\nRECT_SIZE: int = 25\nFONT_SIZE: int = 12\nOUTER_MARGIN: int = 20\n_: ap.Stage = ap.Stage(\n    background_color=ap.Color("#333"),\n    stage_width=700,\n    stage_height=((len(ap.MaterialDesignColors.get_colors_members()) + 1) // 2)\n    * (RECT_SIZE + 10)\n    + OUTER_MARGIN * 2\n    - 10,\n)\n\ncolor: ap.Color\ncolors_members: List[\n    Tuple[str, ap.Color]\n] = ap.MaterialDesignColors.get_colors_members()\ncolor_names: List[ap.String] = []\ncolors: List[ap.Color] = []\nfor color_name, color in colors_members:\n    color_names.append(ap.String(color_name))\n    colors.append(color)\nconstant_names_arr: ap.Array[ap.String] = ap.Array(color_names)\ncolors_arr: ap.Array[ap.Color] = ap.Array(colors)\n\ni: ap.Int\nx: ap.Number = ap.Number(0)\ny: ap.Number = ap.Number(0)\nwith ap.ForArrayIndices(constant_names_arr) as i:\n    with ap.If(i % 2 == 0):\n        x.value = OUTER_MARGIN\n    with ap.Else():\n        x.value = 350\n    y.value = (i // 2) * (RECT_SIZE + 10) + 20\n    color = colors_arr[i]\n    constant_name: ap.String = constant_names_arr[i]\n    ap.Rectangle(\n        x=x,\n        y=y,\n        width=RECT_SIZE,\n        height=RECT_SIZE,\n        fill_color=color,\n        line_color=ap.Color("#fff"),\n        line_thickness=1,\n        line_alpha=0.5,\n    )\n    ap.SvgText(\n        text=constant_name,\n        x=x + RECT_SIZE + 10,\n        y=y + RECT_SIZE / 2 + FONT_SIZE / 2 - 2,\n        font_size=FONT_SIZE,\n        fill_color=ap.Color("#ccc"),\n    )\n\nap.save_overall_html(dest_dir_path="./material_design_colors_definitions/")\n```',  # noqa
    ##################################################
    "</details>": "</details>",
    ##################################################
    "## References": "## 参考文献・参考資料",
    ##################################################
    "- [Overview, Material Design](https://m3.material.io/styles/color/overview)": "- [Overview, Material Design](https://m3.material.io/styles/color/overview)",  # noqa
    ##################################################
    "- [Style, Material Design](https://m1.material.io/style/color.html#)": "- [Style, Material Design](https://m1.material.io/style/color.html#)",  # noqa
}
