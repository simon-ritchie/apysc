"""This module is for the translation mapping data of the
following document:

Document file: path_line_to.md
Language: jp
"""

from typing import Dict

MAPPING: Dict[str, str] = {
    ##################################################
    "# PathLineTo class": "# PathLineTo クラス",
    ##################################################
    "This page explains the `PathLineTo` class.": "このページでは`PathLineTo`クラスについて説明します。",
    ##################################################
    "## What class is this?": "## クラス概要",
    ##################################################
    "The `PathLineTo` class is the class to set a new line from the current position on a path.": "`PathLineTo`クラスは現在設定されている座標位置から新たな線のパスを描画します。",  # noqa
    ##################################################
    "Mainly, the `Path` class constructor or `draw_path` interfaces use this setting.": "主にこの設定は`Path`クラスのコンストラクタと`draw_path`メソッドのインターフェイスで使用されます。",  # noqa
    ##################################################
    "## Basic usage": "## 基本的な使い方",
    ##################################################
    "The `PathLineTo` class constructor requires the `x` and `y` arguments.": "`PathLineTo`クラスのコンストラクタでは`x`と`y`の引数指定が必要となります。",  # noqa
    ##################################################
    "The `Path` class constructor or `draw_path` interfaces\' `path_data_list` argument requires its instance.": "`Path`クラスのコンストラクタもしくは`draw_path`メソッドのインターフェイスの`path_data_list`引数でそのインスタンスが必要とされます。",  # noqa
    ##################################################
    "The following example sets the line drawing from x=50 and y=50 to x=150 and y=50 with the `PathLineTo` instance:": "以下のコード例ではx=50, y=50の位置からx=150, y=50の位置に向けて`PathLineTo`のインスタンスを設定して線の描画設定を行っています:",  # noqa
    ##################################################
    "```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    background_color=\"#333\", stage_width=200, stage_height=100, stage_elem_id=\"stage\"\n)\npath: ap.Path = ap.Path(\n    path_data_list=[\n        ap.PathMoveTo(x=50, y=50),\n        ap.PathLineTo(x=150, y=50),\n    ],\n    line_color=\"#0af\",\n    line_thickness=5,\n)\n\nap.save_overall_html(dest_dir_path=\"path_line_to_basic_usage/\")\n```": "```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    background_color=\"#333\", stage_width=200, stage_height=100, stage_elem_id=\"stage\"\n)\npath: ap.Path = ap.Path(\n    path_data_list=[\n        ap.PathMoveTo(x=50, y=50),\n        ap.PathLineTo(x=150, y=50),\n    ],\n    line_color=\"#0af\",\n    line_thickness=5,\n)\n\nap.save_overall_html(dest_dir_path=\"path_line_to_basic_usage/\")\n```",  # noqa
    ##################################################
    "## Relative position setting": "## 相対座標設定",
    ##################################################
    "The constructor\'s `relative` optional argument changes its behavior.": "コンストラクタの`relative`のオプション引数はその挙動を変更します。",  # noqa
    ##################################################
    "For example, if you set True to its argument, coordinates become relative.": "例として、もしその引数にTrueを指定した場合座標は相対座標として設定されます。",  # noqa
    ##################################################
    "The default setting is False, and it becomes absolute.": "デフォルト値はFalseとなっており、この設定では絶対座標として扱われます。",  # noqa
    ##################################################
    "The following example sets the relative setting and draws the line to the 50px under position from the current position:": "以下のコード例ではrelativeの設定を行い、現在の位置から50px下の位置に向けて線の描画を行っています:",  # noqa
    ##################################################
    "```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    background_color=\"#333\", stage_width=100, stage_height=150, stage_elem_id=\"stage\"\n)\npath: ap.Path = ap.Path(\n    path_data_list=[\n        ap.PathMoveTo(x=50, y=50),\n        ap.PathLineTo(x=0, y=50, relative=True),\n    ],\n    line_color=\"#0af\",\n    line_thickness=5,\n)\n\nap.save_overall_html(dest_dir_path=\"path_line_to_relative/\")\n```": "```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    background_color=\"#333\", stage_width=100, stage_height=150, stage_elem_id=\"stage\"\n)\npath: ap.Path = ap.Path(\n    path_data_list=[\n        ap.PathMoveTo(x=50, y=50),\n        ap.PathLineTo(x=0, y=50, relative=True),\n    ],\n    line_color=\"#0af\",\n    line_thickness=5,\n)\n\nap.save_overall_html(dest_dir_path=\"path_line_to_relative/\")\n```",  # noqa
}
