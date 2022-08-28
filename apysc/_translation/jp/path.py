"""This module is for the translation mapping data of the
following document:

Document file: path.md
Language: jp
"""

from typing import Dict

MAPPING: Dict[str, str] = {
    ##################################################
    "# Path class": "# Path クラス",
    ##################################################
    "This page explains the `Path` class.": "このページでは`Path`クラスについて説明します。",
    ##################################################
    "## What class is this?": "## クラス概要",
    ##################################################
    "The `Path` class creates a path vector graphics object.": "`Path`クラスはパスのベクターグラフィックスのオブジェクトを生成します。",  # noqa
    ##################################################
    "## Basic usage": "## 基本的な使い方",
    ##################################################
    "The `Path` class constructor requires the `path_data_list` argument.": "`Path`",
    ##################################################
    "The constructor also accepts each style\'s argument, such as the `fill_color` and `line_color`.": "コンストラクタは`fill_color`や`line_color`などのスタイル設定用の引数も受け付けます。",  # noqa
    ##################################################
    "```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    background_color=\"#333\", stage_width=200, stage_height=100, stage_elem_id=\"stage\"\n)\npath: ap.Path = ap.Path(\n    path_data_list=[\n        ap.PathMoveTo(x=50, y=50),\n        ap.PathLineTo(x=150, y=50),\n    ],\n    line_color=\"0af\",\n    line_thickness=5,\n)\n\nap.save_overall_html(dest_dir_path=\"path_basic_usage/\")\n```": "```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    background_color=\"#333\", stage_width=200, stage_height=100, stage_elem_id=\"stage\"\n)\npath: ap.Path = ap.Path(\n    path_data_list=[\n        ap.PathMoveTo(x=50, y=50),\n        ap.PathLineTo(x=150, y=50),\n    ],\n    line_color=\"0af\",\n    line_thickness=5,\n)\n\nap.save_overall_html(dest_dir_path=\"path_basic_usage/\")\n```",  # noqa
}
