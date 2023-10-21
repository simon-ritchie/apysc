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
    "The `Path` class constructor requires the `path_data_list` argument.": "`Path`クラスのコンストラクタは`path_data_list`引数を必要とします。",  # noqa
    ##################################################
    "The `path_data_list` argument is a list of each path setting, such as the `PathLineTo` or `PathBezier2D`.": "`path_data_list`引数は`PathLineTo`や`PathBezier2D`などの各パス設定を格納したリストです。",  # noqa
    ##################################################
    "The constructor also accepts each style's argument, such as the `fill_color` and `line_color`.": "コンストラクタは`fill_color`や`line_color`などのスタイル設定用の引数も受け付けます。",  # noqa
    ##################################################
    '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    background_color=ap.Color("#333"),\n    stage_width=200,\n    stage_height=100,\n    stage_elem_id="stage",\n)\npath: ap.Path = ap.Path(\n    path_data_list=[\n        ap.PathMoveTo(x=50, y=50),\n        ap.PathLineTo(x=150, y=50),\n    ],\n    line_color=ap.Color("0af"),\n    line_thickness=5,\n)\n\nap.save_overall_html(dest_dir_path="path_basic_usage/")\n```': '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    background_color=ap.Color("#333"),\n    stage_width=200,\n    stage_height=100,\n    stage_elem_id="stage",\n)\npath: ap.Path = ap.Path(\n    path_data_list=[\n        ap.PathMoveTo(x=50, y=50),\n        ap.PathLineTo(x=150, y=50),\n    ],\n    line_color=ap.Color("0af"),\n    line_thickness=5,\n)\n\nap.save_overall_html(dest_dir_path="path_basic_usage/")\n```',  # noqa
    ##################################################
    "## PathMoveTo class setting": "## PathMoveTo クラス設定",
    ##################################################
    "The `PathMoveTo` class is the class to set a new position on a path.": "`PathMoveTo`クラスはパスに新しい座標設定を追加するためのクラスです。",  # noqa
    ##################################################
    "For more information, please see:": "詳細は以下をご確認ください:",
    ##################################################
    "- [PathMoveTo class](path_move_to.md)": "- [PathMoveTo クラス](jp_path_move_to.md)",
    ##################################################
    "## PathLineTo class setting": "## PathLineTo クラス設定",
    ##################################################
    "The `PathLineTo` class is the class to set a new line from the current position on a path.": "`PathLineTo`クラスは現在設定されている座標位置から新たな線のパスを描画します。",  # noqa
    ##################################################
    "For more information, please see:": "詳細は以下をご確認ください:",
    ##################################################
    "- [PathLineTo class](path_line_to.md)": "- [PathLineTo クラス](jp_path_line_to.md)",
    ##################################################
    "## PathHorizontal class setting": "## PathHorizontal クラス設定",
    ##################################################
    "The `PathHorizontal` class is the class to set a new horizontal line on a path.": "`PathHorizontal`クラスはパス上に水平方向の直線の描画設定を追加するためのクラスです。",  # noqa
    ##################################################
    "For more information, please see:": "詳細は以下をご確認ください:",
    ##################################################
    "- [PathHorizontal class](path_horizontal.md)": "- [PathHorizontal クラス](jp_path_horizontal.md)",  # noqa
    ##################################################
    "## PathVertical class setting": "## PathVertical クラス設定",
    ##################################################
    "The `PathVertical` class is the class to set a new vertical line on a path.": "`PathVertical`クラスはパス上に新しい垂直の直線の設定を追加するためのクラスです。",  # noqa
    ##################################################
    "For more information, please see:": "詳細は以下をご確認ください:",
    ##################################################
    "- [PathVertical class](path_vertical.md)": "- [PathVertical クラス](jp_path_vertical.md)",  # noqa
    ##################################################
    "## PathClose class setting": "## PathClose クラス設定",
    ##################################################
    "The `PathClose` class is the class to close a path.": "`PathVertical`クラスはパス上に新しい垂直の直線の設定を追加するためのクラスです。",  # noqa
    ##################################################
    "For more information, please see:": "詳細は以下をご確認ください:",
    ##################################################
    "- [PathClose class](path_close.md)": "- [PathClose クラス](jp_path_close.md)",
    ##################################################
    "## PathBezier2D class setting": "## PathBezier2D クラス設定",
    ##################################################
    "The `PathBezier2D` class is the class to set a 2D bezier curve on a path.": "`PathBezier2D`クラスはパスへ2次のベジェ曲線を設定するためのクラスです。",  # noqa
    ##################################################
    "For more information, please see:": "詳細は以下をご確認ください:",
    ##################################################
    "- [PathBezier2D class](path_bezier_2d.md)": "- [PathBezier2D クラス](jp_path_bezier_2d.md)",  # noqa
    ##################################################
    "## PathBezier2DContinual class setting": "## PathBezier2DContinual クラス設定",
    ##################################################
    "The `PathBezier2DContinual` class is the class to set a continual 2D bezier curve on a path.": "PathBezier2DContinual`クラスはパスに連続した2次元のベジェ曲線を設定するためのクラスです。",  # noqa
    ##################################################
    "For more information, please see:": "詳細は以下をご確認ください:",
    ##################################################
    "- [PathBezier2DContinual class](path_bezier_2d_continual.md)": "- [PathBezier2DContinual クラス](jp_path_bezier_2d_continual.md)",  # noqa
    ##################################################
    "## PathBezier3D class setting": "## PathBezier3D クラス設定",
    ##################################################
    "The `PathBezier3D` class is the class to set a 3D bezier curve on a path.": "`PathBezier3D`クラスはパス上に3次のベジェ曲線を設定するためのクラスです。",  # noqa
    ##################################################
    "For more information, please see:": "詳細は以下をご確認ください:",
    ##################################################
    "- [PathBezier3D class](path_bezier_3d.md)": "- [PathBezier3D クラス](jp_path_bezier_3d.md)",  # noqa
    ##################################################
    "## PathBezier3DContinual class setting": "## PathBezier3DContinual クラス設定",
    ##################################################
    "The `PathBezier3DContinual` class is the class to set a continual 3D bezier curve on a path.": "`PathBezier3DContinual`クラスはパス上に連続した3次ベジェ曲線を設定するためのクラスです。",  # noqa
    ##################################################
    "For more information, please see:": "詳細は以下をご確認ください:",
    ##################################################
    "- [PathBezier3DContinual class](path_bezier_3d_continual.md)": "- [PathBezier3DContinual クラス](jp_path_bezier_3d_continual.md)",  # noqa
    ##################################################
    "## x property interface example": "## x属性のインターフェイス例",
    ##################################################
    "The `x` property updates or gets the instance's x-coordinate:": "`x`属性ではX座標の値の更新もしくは取得を行えます:",  # noqa
    ##################################################
    '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    background_color=ap.Color("#333"),\n    stage_width=150,\n    stage_height=100,\n    stage_elem_id="stage",\n)\nsprite: ap.Sprite = ap.Sprite()\npath: ap.Path = ap.Path(\n    path_data_list=[\n        ap.PathMoveTo(x=0, y=0),\n        ap.PathLineTo(x=0, y=50),\n        ap.PathLineTo(x=50, y=50),\n        ap.PathClose(),\n    ],\n    line_color=ap.Color("#0af"),\n    line_thickness=5,\n)\npath.x = ap.Number(50)\n\nap.save_overall_html(dest_dir_path="path_x/")\n```': '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    background_color=ap.Color("#333"),\n    stage_width=150,\n    stage_height=100,\n    stage_elem_id="stage",\n)\nsprite: ap.Sprite = ap.Sprite()\npath: ap.Path = ap.Path(\n    path_data_list=[\n        ap.PathMoveTo(x=0, y=0),\n        ap.PathLineTo(x=0, y=50),\n        ap.PathLineTo(x=50, y=50),\n        ap.PathClose(),\n    ],\n    line_color=ap.Color("#0af"),\n    line_thickness=5,\n)\npath.x = ap.Number(50)\n\nap.save_overall_html(dest_dir_path="path_x/")\n```',  # noqa
    ##################################################
    "## y property interface example": "## y属性のインターフェイス例",
    ##################################################
    "The `y` property updates or gets the instance's y-coordinate:": "`y`属性ではY座標の値の更新もしくは取得を行えます:",  # noqa
    ##################################################
    '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    background_color=ap.Color("#333"),\n    stage_width=100,\n    stage_height=150,\n    stage_elem_id="stage",\n)\nsprite: ap.Sprite = ap.Sprite()\npath: ap.Path = ap.Path(\n    path_data_list=[\n        ap.PathMoveTo(x=0, y=0),\n        ap.PathLineTo(x=0, y=50),\n        ap.PathLineTo(x=50, y=50),\n        ap.PathClose(),\n    ],\n    line_color=ap.Color("#0af"),\n    line_thickness=5,\n)\npath.y = ap.Number(50)\n\nap.save_overall_html(dest_dir_path="path_y/")\n```': '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    background_color=ap.Color("#333"),\n    stage_width=100,\n    stage_height=150,\n    stage_elem_id="stage",\n)\nsprite: ap.Sprite = ap.Sprite()\npath: ap.Path = ap.Path(\n    path_data_list=[\n        ap.PathMoveTo(x=0, y=0),\n        ap.PathLineTo(x=0, y=50),\n        ap.PathLineTo(x=50, y=50),\n        ap.PathClose(),\n    ],\n    line_color=ap.Color("#0af"),\n    line_thickness=5,\n)\npath.y = ap.Number(50)\n\nap.save_overall_html(dest_dir_path="path_y/")\n```',  # noqa
    ##################################################
    "## fill_color property interface example": "## fill_color属性のインターフェイス例",
    ##################################################
    "The `fill_color` property updates or gets the instance's fill color:": "`fill_color`属性は塗りの色の値の更新もしくは取得を行えます:",  # noqa
    ##################################################
    '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    background_color=ap.Color("#333"),\n    stage_width=150,\n    stage_height=150,\n    stage_elem_id="stage",\n)\nsprite: ap.Sprite = ap.Sprite()\npath: ap.Path = ap.Path(\n    path_data_list=[\n        ap.PathMoveTo(x=50, y=50),\n        ap.PathLineTo(x=50, y=100),\n        ap.PathLineTo(x=100, y=100),\n        ap.PathClose(),\n    ],\n)\npath.fill_color = ap.Color("#0af")\n\nap.save_overall_html(dest_dir_path="path_fill_color/")\n```': '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    background_color=ap.Color("#333"),\n    stage_width=150,\n    stage_height=150,\n    stage_elem_id="stage",\n)\nsprite: ap.Sprite = ap.Sprite()\npath: ap.Path = ap.Path(\n    path_data_list=[\n        ap.PathMoveTo(x=50, y=50),\n        ap.PathLineTo(x=50, y=100),\n        ap.PathLineTo(x=100, y=100),\n        ap.PathClose(),\n    ],\n)\npath.fill_color = ap.Color("#0af")\n\nap.save_overall_html(dest_dir_path="path_fill_color/")\n```',  # noqa
    ##################################################
    "## fill_alpha property interface example": "## fill_alpha属性のインターフェイス例",
    ##################################################
    "The `fill_alpha` property updates or gets the instance's fill alpha (opacity):": "`fill_alpha`属性は塗りの透明度の値の更新もしくは取得を行えます:",  # noqa
    ##################################################
    '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    background_color=ap.Color("#333"),\n    stage_width=150,\n    stage_height=150,\n    stage_elem_id="stage",\n)\nsprite: ap.Sprite = ap.Sprite()\n\npath: ap.Path = ap.Path(\n    path_data_list=[\n        ap.PathMoveTo(x=50, y=50),\n        ap.PathLineTo(x=50, y=100),\n        ap.PathLineTo(x=100, y=100),\n        ap.PathClose(),\n    ],\n    fill_color=ap.Color("#0af"),\n)\npath.fill_alpha = ap.Number(0.5)\n\nap.save_overall_html(dest_dir_path="path_fill_alpha/")\n```': '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    background_color=ap.Color("#333"),\n    stage_width=150,\n    stage_height=150,\n    stage_elem_id="stage",\n)\nsprite: ap.Sprite = ap.Sprite()\n\npath: ap.Path = ap.Path(\n    path_data_list=[\n        ap.PathMoveTo(x=50, y=50),\n        ap.PathLineTo(x=50, y=100),\n        ap.PathLineTo(x=100, y=100),\n        ap.PathClose(),\n    ],\n    fill_color=ap.Color("#0af"),\n)\npath.fill_alpha = ap.Number(0.5)\n\nap.save_overall_html(dest_dir_path="path_fill_alpha/")\n```',  # noqa
    ##################################################
    "## line_color property interface example": "## line_color属性のインターフェイス例",
    ##################################################
    "The `line_color` property updates or gets the instance's line color:": "`line_color`属性では線の色の値の更新もしくは取得を行えます:",  # noqa
    ##################################################
    '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    background_color=ap.Color("#333"),\n    stage_width=150,\n    stage_height=150,\n    stage_elem_id="stage",\n)\nsprite: ap.Sprite = ap.Sprite()\n\npath: ap.Path = ap.Path(\n    path_data_list=[\n        ap.PathMoveTo(x=50, y=50),\n        ap.PathLineTo(x=50, y=100),\n        ap.PathLineTo(x=100, y=100),\n        ap.PathClose(),\n    ],\n    line_thickness=5,\n)\npath.line_color = ap.Color("#0af")\n\nap.save_overall_html(dest_dir_path="path_line_color/")\n```': '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    background_color=ap.Color("#333"),\n    stage_width=150,\n    stage_height=150,\n    stage_elem_id="stage",\n)\nsprite: ap.Sprite = ap.Sprite()\n\npath: ap.Path = ap.Path(\n    path_data_list=[\n        ap.PathMoveTo(x=50, y=50),\n        ap.PathLineTo(x=50, y=100),\n        ap.PathLineTo(x=100, y=100),\n        ap.PathClose(),\n    ],\n    line_thickness=5,\n)\npath.line_color = ap.Color("#0af")\n\nap.save_overall_html(dest_dir_path="path_line_color/")\n```',  # noqa
    ##################################################
    "## line_alpha property interface example": "## line_alpha属性のインターフェイス例",
    ##################################################
    "The `line_alpha` property updates or gets the instance's line alpha (opacity):": "`line_alpha`属性では線の透明度の値の更新もしくは取得を行えます:",  # noqa
    ##################################################
    '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    background_color=ap.Color("#333"),\n    stage_width=150,\n    stage_height=150,\n    stage_elem_id="stage",\n)\nsprite: ap.Sprite = ap.Sprite()\n\npath: ap.Path = ap.Path(\n    path_data_list=[\n        ap.PathMoveTo(x=50, y=50),\n        ap.PathLineTo(x=50, y=100),\n        ap.PathLineTo(x=100, y=100),\n        ap.PathClose(),\n    ],\n    line_color=ap.Color("#0af"),\n    line_thickness=5,\n)\npath.line_alpha = ap.Number(0.5)\n\nap.save_overall_html(dest_dir_path="path_line_alpha/")\n```': '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    background_color=ap.Color("#333"),\n    stage_width=150,\n    stage_height=150,\n    stage_elem_id="stage",\n)\nsprite: ap.Sprite = ap.Sprite()\n\npath: ap.Path = ap.Path(\n    path_data_list=[\n        ap.PathMoveTo(x=50, y=50),\n        ap.PathLineTo(x=50, y=100),\n        ap.PathLineTo(x=100, y=100),\n        ap.PathClose(),\n    ],\n    line_color=ap.Color("#0af"),\n    line_thickness=5,\n)\npath.line_alpha = ap.Number(0.5)\n\nap.save_overall_html(dest_dir_path="path_line_alpha/")\n```',  # noqa
    ##################################################
    "## line_thickness property interface example": "## line_thickness属性のインターフェイス例",
    ##################################################
    "The `line_thickness` property updates or gets the instance's line thickness (line width):": "`line_thickness`属性では線の幅の更新もしくは取得を行えます:",  # noqa
    ##################################################
    '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    background_color=ap.Color("#333"),\n    stage_width=150,\n    stage_height=150,\n    stage_elem_id="stage",\n)\nsprite: ap.Sprite = ap.Sprite()\n\npath: ap.Path = ap.Path(\n    path_data_list=[\n        ap.PathMoveTo(x=50, y=50),\n        ap.PathLineTo(x=50, y=100),\n        ap.PathLineTo(x=100, y=100),\n        ap.PathClose(),\n    ],\n    line_color=ap.Color("#0af"),\n)\npath.line_thickness = ap.Int(10)\n\nap.save_overall_html(dest_dir_path="path_line_thickness/")\n```': '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    background_color=ap.Color("#333"),\n    stage_width=150,\n    stage_height=150,\n    stage_elem_id="stage",\n)\nsprite: ap.Sprite = ap.Sprite()\n\npath: ap.Path = ap.Path(\n    path_data_list=[\n        ap.PathMoveTo(x=50, y=50),\n        ap.PathLineTo(x=50, y=100),\n        ap.PathLineTo(x=100, y=100),\n        ap.PathClose(),\n    ],\n    line_color=ap.Color("#0af"),\n)\npath.line_thickness = ap.Int(10)\n\nap.save_overall_html(dest_dir_path="path_line_thickness/")\n```',  # noqa
    ##################################################
    "## line_dot_setting property interface example": "## line_dot_setting属性のインターフェイス例",  # noqa
    ##################################################
    "The `line_dot_setting` property updates or gets the instance's line dot-style setting:": "`line_dot_setting`属性では点線のスタイル設定の更新もしくは取得を行えます:",  # noqa
    ##################################################
    '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    background_color=ap.Color("#333"),\n    stage_width=150,\n    stage_height=150,\n    stage_elem_id="stage",\n)\nsprite: ap.Sprite = ap.Sprite()\n\npath: ap.Path = ap.Path(\n    path_data_list=[\n        ap.PathMoveTo(x=50, y=50),\n        ap.PathLineTo(x=50, y=100),\n        ap.PathLineTo(x=100, y=100),\n        ap.PathClose(),\n    ],\n    line_color=ap.Color("#0af"),\n    line_thickness=3,\n)\npath.line_dot_setting = ap.LineDotSetting(dot_size=3)\n\nap.save_overall_html(dest_dir_path="path_line_dot_setting/")\n```': '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    background_color=ap.Color("#333"),\n    stage_width=150,\n    stage_height=150,\n    stage_elem_id="stage",\n)\nsprite: ap.Sprite = ap.Sprite()\n\npath: ap.Path = ap.Path(\n    path_data_list=[\n        ap.PathMoveTo(x=50, y=50),\n        ap.PathLineTo(x=50, y=100),\n        ap.PathLineTo(x=100, y=100),\n        ap.PathClose(),\n    ],\n    line_color=ap.Color("#0af"),\n    line_thickness=3,\n)\npath.line_dot_setting = ap.LineDotSetting(dot_size=3)\n\nap.save_overall_html(dest_dir_path="path_line_dot_setting/")\n```',  # noqa
    ##################################################
    "## line_dash_setting property interface example": "## line_dash_setting属性のインターフェイス例",  # noqa
    ##################################################
    "The `line_dash_setting` property updates or gets the instance's line dash-style setting:": "`line_dash_setting`属性では破線のスタイル設定の更新もしくは取得を行えます:",  # noqa
    ##################################################
    '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    background_color=ap.Color("#333"),\n    stage_width=150,\n    stage_height=150,\n    stage_elem_id="stage",\n)\nsprite: ap.Sprite = ap.Sprite()\n\npath: ap.Path = ap.Path(\n    path_data_list=[\n        ap.PathMoveTo(x=50, y=50),\n        ap.PathLineTo(x=50, y=100),\n        ap.PathLineTo(x=100, y=100),\n        ap.PathClose(),\n    ],\n    line_color=ap.Color("#0af"),\n    line_thickness=3,\n)\npath.line_dash_setting = ap.LineDashSetting(dash_size=7, space_size=2)\n\nap.save_overall_html(dest_dir_path="path_line_dash_setting/")\n```': '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    background_color=ap.Color("#333"),\n    stage_width=150,\n    stage_height=150,\n    stage_elem_id="stage",\n)\nsprite: ap.Sprite = ap.Sprite()\n\npath: ap.Path = ap.Path(\n    path_data_list=[\n        ap.PathMoveTo(x=50, y=50),\n        ap.PathLineTo(x=50, y=100),\n        ap.PathLineTo(x=100, y=100),\n        ap.PathClose(),\n    ],\n    line_color=ap.Color("#0af"),\n    line_thickness=3,\n)\npath.line_dash_setting = ap.LineDashSetting(dash_size=7, space_size=2)\n\nap.save_overall_html(dest_dir_path="path_line_dash_setting/")\n```',  # noqa
    ##################################################
    "## line_round_dot_setting property interface example": "## line_round_dot_setting属性のインターフェイス例",  # noqa
    ##################################################
    "The `line_round_dot_setting` property updates or gets the instance's line-round dot-style setting:": "`line_round_dot_setting`属性では丸ドット線のスタイル設定の更新もしくは取得を行えます:",  # noqa
    ##################################################
    '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    background_color=ap.Color("#333"),\n    stage_width=150,\n    stage_height=150,\n    stage_elem_id="stage",\n)\nsprite: ap.Sprite = ap.Sprite()\n\npath: ap.Path = ap.Path(\n    path_data_list=[\n        ap.PathMoveTo(x=50, y=50),\n        ap.PathLineTo(x=50, y=100),\n        ap.PathLineTo(x=100, y=100),\n        ap.PathClose(),\n    ],\n    line_color=ap.Color("#0af"),\n)\npath.line_round_dot_setting = ap.LineRoundDotSetting(round_size=5, space_size=4)\n\nap.save_overall_html(dest_dir_path="path_line_round_dot_setting/")\n```': '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    background_color=ap.Color("#333"),\n    stage_width=150,\n    stage_height=150,\n    stage_elem_id="stage",\n)\nsprite: ap.Sprite = ap.Sprite()\n\npath: ap.Path = ap.Path(\n    path_data_list=[\n        ap.PathMoveTo(x=50, y=50),\n        ap.PathLineTo(x=50, y=100),\n        ap.PathLineTo(x=100, y=100),\n        ap.PathClose(),\n    ],\n    line_color=ap.Color("#0af"),\n)\npath.line_round_dot_setting = ap.LineRoundDotSetting(round_size=5, space_size=4)\n\nap.save_overall_html(dest_dir_path="path_line_round_dot_setting/")\n```',  # noqa
    ##################################################
    "## line_dash_dot_setting property interface example": "## line_dash_dot_setting属性のインターフェイス例",  # noqa
    ##################################################
    "The `line_dash_dot_setting` property updates or gets the instance's dash-dotted line style setting:": "`line_dash_dot_setting`属性では一点鎖線のスタイル設定の更新もしくは取得を行えます:",  # noqa
    ##################################################
    '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    background_color=ap.Color("#333"),\n    stage_width=150,\n    stage_height=150,\n    stage_elem_id="stage",\n)\nsprite: ap.Sprite = ap.Sprite()\n\npath: ap.Path = ap.Path(\n    path_data_list=[\n        ap.PathMoveTo(x=50, y=50),\n        ap.PathLineTo(x=50, y=100),\n        ap.PathLineTo(x=100, y=100),\n        ap.PathClose(),\n    ],\n    line_color=ap.Color("#0af"),\n    line_thickness=3,\n)\npath.line_dash_dot_setting = ap.LineDashDotSetting(\n    dot_size=3,\n    dash_size=6,\n    space_size=3,\n)\n\nap.save_overall_html(dest_dir_path="path_line_dash_dot_setting/")\n```': '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    background_color=ap.Color("#333"),\n    stage_width=150,\n    stage_height=150,\n    stage_elem_id="stage",\n)\nsprite: ap.Sprite = ap.Sprite()\n\npath: ap.Path = ap.Path(\n    path_data_list=[\n        ap.PathMoveTo(x=50, y=50),\n        ap.PathLineTo(x=50, y=100),\n        ap.PathLineTo(x=100, y=100),\n        ap.PathClose(),\n    ],\n    line_color=ap.Color("#0af"),\n    line_thickness=3,\n)\npath.line_dash_dot_setting = ap.LineDashDotSetting(\n    dot_size=3,\n    dash_size=6,\n    space_size=3,\n)\n\nap.save_overall_html(dest_dir_path="path_line_dash_dot_setting/")\n```',  # noqa
    ##################################################
    "## rotation_around_center property interface example": "## rotation_around_center属性のインターフェイス例",  # noqa
    ##################################################
    "The `rotation_around_center` property updates or gets the instance's rotation value (0 to 359) from the center point:": "`rotation_around_center`属性ではインスタンスの中央座標での回転量（0～359）の更新もしくは取得を行えます:",  # noqa
    ##################################################
    '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    background_color=ap.Color("#333"),\n    stage_width=150,\n    stage_height=150,\n    stage_elem_id="stage",\n)\nsprite: ap.Sprite = ap.Sprite()\n\npath: ap.Path = ap.Path(\n    path_data_list=[\n        ap.PathMoveTo(x=50, y=50),\n        ap.PathLineTo(x=50, y=100),\n        ap.PathLineTo(x=100, y=100),\n        ap.PathClose(),\n    ],\n    line_color=ap.Color("#0af"),\n    line_thickness=3,\n)\n\n\ndef on_timer(e: ap.TimerEvent, options: dict) -> None:\n    """\n    The timer event handler.\n\n    Parameters\n    ----------\n    e : ap.TimerEvent\n        Event instance.\n    options : dict\n        Optional arguments dictionary.\n    """\n    path.rotation_around_center += 1\n\n\nap.Timer(handler=on_timer, delay=ap.FPS.FPS_60).start()\nap.save_overall_html(dest_dir_path="path_rotation_around_center/")\n```': '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    background_color=ap.Color("#333"),\n    stage_width=150,\n    stage_height=150,\n    stage_elem_id="stage",\n)\nsprite: ap.Sprite = ap.Sprite()\n\npath: ap.Path = ap.Path(\n    path_data_list=[\n        ap.PathMoveTo(x=50, y=50),\n        ap.PathLineTo(x=50, y=100),\n        ap.PathLineTo(x=100, y=100),\n        ap.PathClose(),\n    ],\n    line_color=ap.Color("#0af"),\n    line_thickness=3,\n)\n\n\ndef on_timer(e: ap.TimerEvent, options: dict) -> None:\n    """\n    The timer event handler.\n\n    Parameters\n    ----------\n    e : ap.TimerEvent\n        Event instance.\n    options : dict\n        Optional arguments dictionary.\n    """\n    path.rotation_around_center += 1\n\n\nap.Timer(handler=on_timer, delay=ap.FPS.FPS_60).start()\nap.save_overall_html(dest_dir_path="path_rotation_around_center/")\n```',  # noqa
    ##################################################
    "## set_rotation_around_point and get_rotation_around_point methods interface example": "## set_rotation_around_pointとget_rotation_around_pointメソッドのインターフェイス例",  # noqa
    ##################################################
    "The `set_rotation_around_point` method updates the instance's rotation value (0 to 359) from a specified point.": "`set_rotation_around_point`メソッドは指定された座標からのインスタンスの回転量（0～359）を更新します。",  # noqa
    ##################################################
    "Similarly, the `get_rotation_around_point` method gets the instance's rotation value (0 to 359) from a specified point:": "同様に、`get_rotation_around_point`メソッドでは指定された座標のインスタンスの回転量（0～359）を取得します:",  # noqa
    ##################################################
    '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    background_color=ap.Color("#333"),\n    stage_width=150,\n    stage_height=150,\n    stage_elem_id="stage",\n)\nsprite: ap.Sprite = ap.Sprite()\n\npath: ap.Path = ap.Path(\n    path_data_list=[\n        ap.PathMoveTo(x=50, y=50),\n        ap.PathLineTo(x=50, y=100),\n        ap.PathLineTo(x=100, y=100),\n        ap.PathClose(),\n    ],\n    line_color=ap.Color("#0af"),\n    line_thickness=3,\n)\nX: ap.Int = ap.Int(100)\nY: ap.Int = ap.Int(100)\n\n\ndef on_timer(e: ap.TimerEvent, options: dict) -> None:\n    """\n    The timer event handler.\n\n    Parameters\n    ----------\n    e : ap.TimerEvent\n        Event instance.\n    options : dict\n        Optional arguments dictionary.\n    """\n    rotation: ap.Int = path.get_rotation_around_point(x=X, y=Y) + 1\n    path.set_rotation_around_point(rotation=rotation, x=X, y=Y)\n\n\nap.Timer(handler=on_timer, delay=ap.FPS.FPS_60).start()\nap.save_overall_html(dest_dir_path="path_rotation_around_point/")\n```': '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    background_color=ap.Color("#333"),\n    stage_width=150,\n    stage_height=150,\n    stage_elem_id="stage",\n)\nsprite: ap.Sprite = ap.Sprite()\n\npath: ap.Path = ap.Path(\n    path_data_list=[\n        ap.PathMoveTo(x=50, y=50),\n        ap.PathLineTo(x=50, y=100),\n        ap.PathLineTo(x=100, y=100),\n        ap.PathClose(),\n    ],\n    line_color=ap.Color("#0af"),\n    line_thickness=3,\n)\nX: ap.Int = ap.Int(100)\nY: ap.Int = ap.Int(100)\n\n\ndef on_timer(e: ap.TimerEvent, options: dict) -> None:\n    """\n    The timer event handler.\n\n    Parameters\n    ----------\n    e : ap.TimerEvent\n        Event instance.\n    options : dict\n        Optional arguments dictionary.\n    """\n    rotation: ap.Int = path.get_rotation_around_point(x=X, y=Y) + 1\n    path.set_rotation_around_point(rotation=rotation, x=X, y=Y)\n\n\nap.Timer(handler=on_timer, delay=ap.FPS.FPS_60).start()\nap.save_overall_html(dest_dir_path="path_rotation_around_point/")\n```',  # noqa
    ##################################################
    "## scale_x_from_center property interface example": "## scale_x_from_center属性のインターフェイス例",  # noqa
    ##################################################
    "The `scale_x_from_center` property updates or gets the instance's scale-x from the center point:": "`scale_x_from_center`属性ではインスタンスの中央座標でのX軸の拡縮値の更新もしくは取得を行えます:",  # noqa
    ##################################################
    '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    background_color=ap.Color("#333"),\n    stage_width=150,\n    stage_height=150,\n    stage_elem_id="stage",\n)\nsprite: ap.Sprite = ap.Sprite()\n\npath: ap.Path = ap.Path(\n    path_data_list=[\n        ap.PathMoveTo(x=50, y=50),\n        ap.PathLineTo(x=50, y=100),\n        ap.PathLineTo(x=100, y=100),\n        ap.PathClose(),\n    ],\n    line_color=ap.Color("#0af"),\n    line_thickness=3,\n)\ndirection: ap.Int = ap.Int(1)\n\n\ndef on_timer(e: ap.TimerEvent, options: dict) -> None:\n    """\n    The timer event handler.\n\n    Parameters\n    ----------\n    e : ap.TimerEvent\n        Event instance.\n    options : dict\n        Optional arguments dictionary.\n    """\n    scale: ap.Number = path.scale_x_from_center\n    with ap.If(scale <= 0.001):\n        direction.value = 1\n    with ap.If(scale >= 2):\n        direction.value = -1\n    path.scale_x_from_center += direction * 0.01\n\n\nap.Timer(handler=on_timer, delay=ap.FPS.FPS_60).start()\nap.save_overall_html(dest_dir_path="path_scale_x_from_center/")\n```': '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    background_color=ap.Color("#333"),\n    stage_width=150,\n    stage_height=150,\n    stage_elem_id="stage",\n)\nsprite: ap.Sprite = ap.Sprite()\n\npath: ap.Path = ap.Path(\n    path_data_list=[\n        ap.PathMoveTo(x=50, y=50),\n        ap.PathLineTo(x=50, y=100),\n        ap.PathLineTo(x=100, y=100),\n        ap.PathClose(),\n    ],\n    line_color=ap.Color("#0af"),\n    line_thickness=3,\n)\ndirection: ap.Int = ap.Int(1)\n\n\ndef on_timer(e: ap.TimerEvent, options: dict) -> None:\n    """\n    The timer event handler.\n\n    Parameters\n    ----------\n    e : ap.TimerEvent\n        Event instance.\n    options : dict\n        Optional arguments dictionary.\n    """\n    scale: ap.Number = path.scale_x_from_center\n    with ap.If(scale <= 0.001):\n        direction.value = 1\n    with ap.If(scale >= 2):\n        direction.value = -1\n    path.scale_x_from_center += direction * 0.01\n\n\nap.Timer(handler=on_timer, delay=ap.FPS.FPS_60).start()\nap.save_overall_html(dest_dir_path="path_scale_x_from_center/")\n```',  # noqa
    ##################################################
    "## scale_y_from_center property interface example": "## scale_y_from_center属性のインターフェイス例",  # noqa
    ##################################################
    "The `scale_y_from_center` property updates or gets the instance's scale-y from the center point:": "`scale_y_from_center`属性ではインスタンスの中央座標でのX軸の拡縮値の更新もしくは取得を行えます:",  # noqa
    ##################################################
    '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    background_color=ap.Color("#333"),\n    stage_width=150,\n    stage_height=150,\n    stage_elem_id="stage",\n)\nsprite: ap.Sprite = ap.Sprite()\n\npath: ap.Path = ap.Path(\n    path_data_list=[\n        ap.PathMoveTo(x=50, y=50),\n        ap.PathLineTo(x=50, y=100),\n        ap.PathLineTo(x=100, y=100),\n        ap.PathClose(),\n    ],\n    line_color=ap.Color("#0af"),\n    line_thickness=3,\n)\ndirection: ap.Int = ap.Int(1)\n\n\ndef on_timer(e: ap.TimerEvent, options: dict) -> None:\n    """\n    The timer event handler.\n\n    Parameters\n    ----------\n    e : ap.TimerEvent\n        Event instance.\n    options : dict\n        Optional arguments dictionary.\n    """\n    scale: ap.Number = path.scale_y_from_center\n    with ap.If(scale <= 0.001):\n        direction.value = 1\n    with ap.If(scale >= 2):\n        direction.value = -1\n    path.scale_y_from_center += direction * 0.01\n\n\nap.Timer(handler=on_timer, delay=ap.FPS.FPS_60).start()\nap.save_overall_html(dest_dir_path="path_scale_y_from_center/")\n```': '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    background_color=ap.Color("#333"),\n    stage_width=150,\n    stage_height=150,\n    stage_elem_id="stage",\n)\nsprite: ap.Sprite = ap.Sprite()\n\npath: ap.Path = ap.Path(\n    path_data_list=[\n        ap.PathMoveTo(x=50, y=50),\n        ap.PathLineTo(x=50, y=100),\n        ap.PathLineTo(x=100, y=100),\n        ap.PathClose(),\n    ],\n    line_color=ap.Color("#0af"),\n    line_thickness=3,\n)\ndirection: ap.Int = ap.Int(1)\n\n\ndef on_timer(e: ap.TimerEvent, options: dict) -> None:\n    """\n    The timer event handler.\n\n    Parameters\n    ----------\n    e : ap.TimerEvent\n        Event instance.\n    options : dict\n        Optional arguments dictionary.\n    """\n    scale: ap.Number = path.scale_y_from_center\n    with ap.If(scale <= 0.001):\n        direction.value = 1\n    with ap.If(scale >= 2):\n        direction.value = -1\n    path.scale_y_from_center += direction * 0.01\n\n\nap.Timer(handler=on_timer, delay=ap.FPS.FPS_60).start()\nap.save_overall_html(dest_dir_path="path_scale_y_from_center/")\n```',  # noqa
    ##################################################
    "## set_scale_x_from_point and get_scale_x_from_point methods interface example": "## set_scale_x_from_pointとget_scale_x_from_pointメソッドのインターフェイス例",  # noqa
    ##################################################
    "The `set_scale_x_from_point` method updates the instance's scale-x from a specified point.": "`set_scale_x_from_point`メソッドは指定されたX座標を基準としてX軸の拡縮値を更新します。",  # noqa
    ##################################################
    "Similarly, the `get_scale_x_from_point` method gets the instance's scale-x from a specified point:": "同様に、`get_scale_x_from_point`メソッドでは指定されたX座標を基準としたX軸の拡縮値を取得します:",  # noqa
    ##################################################
    '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    background_color=ap.Color("#333"),\n    stage_width=150,\n    stage_height=150,\n    stage_elem_id="stage",\n)\nsprite: ap.Sprite = ap.Sprite()\n\npath: ap.Path = ap.Path(\n    path_data_list=[\n        ap.PathMoveTo(x=50, y=50),\n        ap.PathLineTo(x=50, y=100),\n        ap.PathLineTo(x=100, y=100),\n        ap.PathClose(),\n    ],\n    line_color=ap.Color("#0af"),\n    line_thickness=3,\n)\ndirection: ap.Int = ap.Int(1)\nX: ap.Int = ap.Int(100)\n\n\ndef on_timer(e: ap.TimerEvent, options: dict) -> None:\n    """\n    The timer event handler.\n\n    Parameters\n    ----------\n    e : ap.TimerEvent\n        Event instance.\n    options : dict\n        Optional arguments dictionary.\n    """\n    scale: ap.Number = path.get_scale_x_from_point(x=X)\n    with ap.If(scale <= 0.001):\n        direction.value = 1\n    with ap.If(scale >= 2):\n        direction.value = -1\n    scale += direction * 0.005\n    path.set_scale_x_from_point(scale_x=scale, x=X)\n\n\nap.Timer(handler=on_timer, delay=ap.FPS.FPS_60).start()\nap.save_overall_html(dest_dir_path="path_scale_x_from_point/")\n```': '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    background_color=ap.Color("#333"),\n    stage_width=150,\n    stage_height=150,\n    stage_elem_id="stage",\n)\nsprite: ap.Sprite = ap.Sprite()\n\npath: ap.Path = ap.Path(\n    path_data_list=[\n        ap.PathMoveTo(x=50, y=50),\n        ap.PathLineTo(x=50, y=100),\n        ap.PathLineTo(x=100, y=100),\n        ap.PathClose(),\n    ],\n    line_color=ap.Color("#0af"),\n    line_thickness=3,\n)\ndirection: ap.Int = ap.Int(1)\nX: ap.Int = ap.Int(100)\n\n\ndef on_timer(e: ap.TimerEvent, options: dict) -> None:\n    """\n    The timer event handler.\n\n    Parameters\n    ----------\n    e : ap.TimerEvent\n        Event instance.\n    options : dict\n        Optional arguments dictionary.\n    """\n    scale: ap.Number = path.get_scale_x_from_point(x=X)\n    with ap.If(scale <= 0.001):\n        direction.value = 1\n    with ap.If(scale >= 2):\n        direction.value = -1\n    scale += direction * 0.005\n    path.set_scale_x_from_point(scale_x=scale, x=X)\n\n\nap.Timer(handler=on_timer, delay=ap.FPS.FPS_60).start()\nap.save_overall_html(dest_dir_path="path_scale_x_from_point/")\n```',  # noqa
    ##################################################
    "## set_scale_y_from_point and get_scale_y_from_point methods interface example": "## set_scale_y_from_pointとget_scale_y_from_pointメソッドのインターフェイス例",  # noqa
    ##################################################
    "The `set_scale_y_from_point` method updates the instance's scale-y from a specified point.": "`set_scale_y_from_point`メソッドは指定されたY座標を基準としてY軸の拡縮値を更新します。",  # noqa
    ##################################################
    "Similarly, the `get_scale_y_from_point` method gets the instance's scale-y from a specified point:": "同様に、`get_scale_y_from_point`メソッドでは指定されたY座標を基準としたY軸の拡縮値を取得します。",  # noqa
    ##################################################
    '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    background_color=ap.Color("#333"),\n    stage_width=150,\n    stage_height=150,\n    stage_elem_id="stage",\n)\nsprite: ap.Sprite = ap.Sprite()\n\npath: ap.Path = ap.Path(\n    path_data_list=[\n        ap.PathMoveTo(x=50, y=50),\n        ap.PathLineTo(x=50, y=100),\n        ap.PathLineTo(x=100, y=100),\n        ap.PathClose(),\n    ],\n    line_color=ap.Color("#0af"),\n    line_thickness=3,\n)\ndirection: ap.Int = ap.Int(1)\nY: ap.Int = ap.Int(100)\n\n\ndef on_timer(e: ap.TimerEvent, options: dict) -> None:\n    """\n    The timer event handler.\n\n    Parameters\n    ----------\n    e : ap.TimerEvent\n        Event instance.\n    options : dict\n        Optional arguments dictionary.\n    """\n    scale: ap.Number = path.get_scale_y_from_point(y=Y)\n    with ap.If(scale <= 0.001):\n        direction.value = 1\n    with ap.If(scale >= 2):\n        direction.value = -1\n    scale += direction * 0.005\n    path.set_scale_y_from_point(scale_y=scale, y=Y)\n\n\nap.Timer(handler=on_timer, delay=ap.FPS.FPS_60).start()\nap.save_overall_html(dest_dir_path="path_scale_y_from_point/")\n```': '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    background_color=ap.Color("#333"),\n    stage_width=150,\n    stage_height=150,\n    stage_elem_id="stage",\n)\nsprite: ap.Sprite = ap.Sprite()\n\npath: ap.Path = ap.Path(\n    path_data_list=[\n        ap.PathMoveTo(x=50, y=50),\n        ap.PathLineTo(x=50, y=100),\n        ap.PathLineTo(x=100, y=100),\n        ap.PathClose(),\n    ],\n    line_color=ap.Color("#0af"),\n    line_thickness=3,\n)\ndirection: ap.Int = ap.Int(1)\nY: ap.Int = ap.Int(100)\n\n\ndef on_timer(e: ap.TimerEvent, options: dict) -> None:\n    """\n    The timer event handler.\n\n    Parameters\n    ----------\n    e : ap.TimerEvent\n        Event instance.\n    options : dict\n        Optional arguments dictionary.\n    """\n    scale: ap.Number = path.get_scale_y_from_point(y=Y)\n    with ap.If(scale <= 0.001):\n        direction.value = 1\n    with ap.If(scale >= 2):\n        direction.value = -1\n    scale += direction * 0.005\n    path.set_scale_y_from_point(scale_y=scale, y=Y)\n\n\nap.Timer(handler=on_timer, delay=ap.FPS.FPS_60).start()\nap.save_overall_html(dest_dir_path="path_scale_y_from_point/")\n```',  # noqa
    ##################################################
    "## flip_x property interface example": "## flip_x属性のインターフェイス例",
    ##################################################
    "The `flip_x` property updates or gets the instance's flip-x (reflecting state) boolean value:": "`flip_x`属性ではインスタンスのX軸の反転状況の真偽値の更新もしくは取得を行えます:",  # noqa
    ##################################################
    '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    background_color=ap.Color("#333"),\n    stage_width=150,\n    stage_height=150,\n    stage_elem_id="stage",\n)\nsprite: ap.Sprite = ap.Sprite()\n\npath: ap.Path = ap.Path(\n    path_data_list=[\n        ap.PathMoveTo(x=50, y=50),\n        ap.PathLineTo(x=50, y=100),\n        ap.PathLineTo(x=100, y=100),\n        ap.PathClose(),\n    ],\n    line_color=ap.Color("#0af"),\n    line_thickness=3,\n)\n\n\ndef on_timer(e: ap.TimerEvent, options: dict) -> None:\n    """\n    The timer event handler.\n\n    Parameters\n    ----------\n    e : ap.TimerEvent\n        Event instance.\n    options : dict\n        Optional arguments dictionary.\n    """\n    path.flip_x = path.flip_x.not_\n\n\nap.Timer(handler=on_timer, delay=1000).start()\nap.save_overall_html(dest_dir_path="path_flip_x/")\n```': '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    background_color=ap.Color("#333"),\n    stage_width=150,\n    stage_height=150,\n    stage_elem_id="stage",\n)\nsprite: ap.Sprite = ap.Sprite()\n\npath: ap.Path = ap.Path(\n    path_data_list=[\n        ap.PathMoveTo(x=50, y=50),\n        ap.PathLineTo(x=50, y=100),\n        ap.PathLineTo(x=100, y=100),\n        ap.PathClose(),\n    ],\n    line_color=ap.Color("#0af"),\n    line_thickness=3,\n)\n\n\ndef on_timer(e: ap.TimerEvent, options: dict) -> None:\n    """\n    The timer event handler.\n\n    Parameters\n    ----------\n    e : ap.TimerEvent\n        Event instance.\n    options : dict\n        Optional arguments dictionary.\n    """\n    path.flip_x = path.flip_x.not_\n\n\nap.Timer(handler=on_timer, delay=1000).start()\nap.save_overall_html(dest_dir_path="path_flip_x/")\n```',  # noqa
    ##################################################
    "## flip_y property interface example": "## flip_y属性のインターフェイス例",
    ##################################################
    "The `flip_y` property updates or gets the instance's flip-y (reflecting state) boolean value:": "`flip_y`属性ではインスタンスのX軸の反転状況の真偽値の更新もしくは取得を行えます:",  # noqa
    ##################################################
    '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    background_color=ap.Color("#333"),\n    stage_width=150,\n    stage_height=150,\n    stage_elem_id="stage",\n)\nsprite: ap.Sprite = ap.Sprite()\n\npath: ap.Path = ap.Path(\n    path_data_list=[\n        ap.PathMoveTo(x=50, y=50),\n        ap.PathLineTo(x=50, y=100),\n        ap.PathLineTo(x=100, y=100),\n        ap.PathClose(),\n    ],\n    line_color=ap.Color("#0af"),\n    line_thickness=3,\n)\n\n\ndef on_timer(e: ap.TimerEvent, options: dict) -> None:\n    """\n    The timer event handler.\n\n    Parameters\n    ----------\n    e : ap.TimerEvent\n        Event instance.\n    options : dict\n        Optional arguments dictionary.\n    """\n    path.flip_y = path.flip_y.not_\n\n\nap.Timer(handler=on_timer, delay=1000).start()\nap.save_overall_html(dest_dir_path="path_flip_y/")\n```': '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    background_color=ap.Color("#333"),\n    stage_width=150,\n    stage_height=150,\n    stage_elem_id="stage",\n)\nsprite: ap.Sprite = ap.Sprite()\n\npath: ap.Path = ap.Path(\n    path_data_list=[\n        ap.PathMoveTo(x=50, y=50),\n        ap.PathLineTo(x=50, y=100),\n        ap.PathLineTo(x=100, y=100),\n        ap.PathClose(),\n    ],\n    line_color=ap.Color("#0af"),\n    line_thickness=3,\n)\n\n\ndef on_timer(e: ap.TimerEvent, options: dict) -> None:\n    """\n    The timer event handler.\n\n    Parameters\n    ----------\n    e : ap.TimerEvent\n        Event instance.\n    options : dict\n        Optional arguments dictionary.\n    """\n    path.flip_y = path.flip_y.not_\n\n\nap.Timer(handler=on_timer, delay=1000).start()\nap.save_overall_html(dest_dir_path="path_flip_y/")\n```',  # noqa
    ##################################################
    "## skew_x property interface example": "## skew_x属性のインターフェイス例",
    ##################################################
    "The `skew_x` property updates or gets the instance's skew-x (distortion) value:": "`skew_x`属性ではインスタンスのX軸の歪みの値の更新もしくは取得を行えます:",  # noqa
    ##################################################
    '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    background_color=ap.Color("#333"),\n    stage_width=150,\n    stage_height=150,\n    stage_elem_id="stage",\n)\nsprite: ap.Sprite = ap.Sprite()\n\npath: ap.Path = ap.Path(\n    path_data_list=[\n        ap.PathMoveTo(x=50, y=50),\n        ap.PathLineTo(x=50, y=100),\n        ap.PathLineTo(x=100, y=100),\n        ap.PathClose(),\n    ],\n    line_color=ap.Color("#0af"),\n    line_thickness=3,\n)\n\n\ndef on_timer(e: ap.TimerEvent, options: dict) -> None:\n    """\n    The timer event handler.\n\n    Parameters\n    ----------\n    e : ap.TimerEvent\n        Event instance.\n    options : dict\n        Optional arguments dictionary.\n    """\n    path.skew_x += 1\n\n\nap.Timer(handler=on_timer, delay=ap.FPS.FPS_60).start()\nap.save_overall_html(dest_dir_path="path_skew_x/")\n```': '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    background_color=ap.Color("#333"),\n    stage_width=150,\n    stage_height=150,\n    stage_elem_id="stage",\n)\nsprite: ap.Sprite = ap.Sprite()\n\npath: ap.Path = ap.Path(\n    path_data_list=[\n        ap.PathMoveTo(x=50, y=50),\n        ap.PathLineTo(x=50, y=100),\n        ap.PathLineTo(x=100, y=100),\n        ap.PathClose(),\n    ],\n    line_color=ap.Color("#0af"),\n    line_thickness=3,\n)\n\n\ndef on_timer(e: ap.TimerEvent, options: dict) -> None:\n    """\n    The timer event handler.\n\n    Parameters\n    ----------\n    e : ap.TimerEvent\n        Event instance.\n    options : dict\n        Optional arguments dictionary.\n    """\n    path.skew_x += 1\n\n\nap.Timer(handler=on_timer, delay=ap.FPS.FPS_60).start()\nap.save_overall_html(dest_dir_path="path_skew_x/")\n```',  # noqa
    ##################################################
    "## skew_y property interface example": "## skew_y属性のインターフェイス例",
    ##################################################
    "The `skew_y` property updates or gets the instance's skew-y (distortion) value:": "`skew_y`属性ではインスタンスのY軸の歪みの値の更新もしくは取得を行えます:",  # noqa
    ##################################################
    '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    background_color=ap.Color("#333"),\n    stage_width=150,\n    stage_height=150,\n    stage_elem_id="stage",\n)\nsprite: ap.Sprite = ap.Sprite()\n\npath: ap.Path = ap.Path(\n    path_data_list=[\n        ap.PathMoveTo(x=50, y=50),\n        ap.PathLineTo(x=50, y=100),\n        ap.PathLineTo(x=100, y=100),\n        ap.PathClose(),\n    ],\n    line_color=ap.Color("#0af"),\n    line_thickness=3,\n)\n\n\ndef on_timer(e: ap.TimerEvent, options: dict) -> None:\n    """\n    The timer event handler.\n\n    Parameters\n    ----------\n    e : ap.TimerEvent\n        Event instance.\n    options : dict\n        Optional arguments dictionary.\n    """\n    path.skew_y += 1\n\n\nap.Timer(handler=on_timer, delay=ap.FPS.FPS_60).start()\nap.save_overall_html(dest_dir_path="path_skew_y/")\n```': '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    background_color=ap.Color("#333"),\n    stage_width=150,\n    stage_height=150,\n    stage_elem_id="stage",\n)\nsprite: ap.Sprite = ap.Sprite()\n\npath: ap.Path = ap.Path(\n    path_data_list=[\n        ap.PathMoveTo(x=50, y=50),\n        ap.PathLineTo(x=50, y=100),\n        ap.PathLineTo(x=100, y=100),\n        ap.PathClose(),\n    ],\n    line_color=ap.Color("#0af"),\n    line_thickness=3,\n)\n\n\ndef on_timer(e: ap.TimerEvent, options: dict) -> None:\n    """\n    The timer event handler.\n\n    Parameters\n    ----------\n    e : ap.TimerEvent\n        Event instance.\n    options : dict\n        Optional arguments dictionary.\n    """\n    path.skew_y += 1\n\n\nap.Timer(handler=on_timer, delay=ap.FPS.FPS_60).start()\nap.save_overall_html(dest_dir_path="path_skew_y/")\n```',  # noqa
    ##################################################
    "## Path class constructor API": "## Path クラスのコンストラクタのAPI",
    ##################################################
    '<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>': '<span class="inconspicuous-txt">特記事項: このAPIドキュメントはドキュメントビルド用のスクリプトによって自動で生成・同期されています。そのためもしかしたらこの節の内容は前節までの内容と重複している場合があります。</span>',  # noqa
    ##################################################
    "**[Interface summary]**": "**[インターフェイス概要]**",
    ##################################################
    "Create a path vector graphic.<hr>": "パスのベクターグラフィックスを生成します。<hr>",
    ##################################################
    "**[Parameters]**": "**[引数]**",
    ##################################################
    "- `path_data_list`: list of PathDataBase": "- `path_data_list`: list of PathDataBase",  # noqa
    ##################################################
    "  - Target path data settings, such as the ap.PathData.MoveTo.": "  - ap.PathData.MoveToなどの対象のパスデータの設定のリスト。",  # noqa
    ##################################################
    "- `fill_color`: Color, default COLORLESS": "- `fill_color`: Color, default COLORLESS",  # noqa
    ##################################################
    "  - A fill-color to set.": "  - 設定する塗りの色。",
    ##################################################
    "- `fill_alpha`: float or Number, default 1.0": "- `fill_alpha`: float or Number, default 1.0",  # noqa
    ##################################################
    "  - A fill-alpha to set.": "  - 設定する塗りの透明度。",
    ##################################################
    "- `line_color`: Color, default COLORLESS": "- `line_color`: Color, default COLORLESS",  # noqa
    ##################################################
    "  - A line-color to set.": "  - 設定する線の色。",
    ##################################################
    "- `line_alpha`: float or Number, default 1.0": "- `line_alpha`: float or Number, default 1.0",  # noqa
    ##################################################
    "  - A line-alpha to set.": "  - 設定する線の透明度。",
    ##################################################
    "- `line_thickness`: int or Int, default 1": "- `line_thickness`: int or Int, default 1",  # noqa
    ##################################################
    "  - A line-thickness (line-width) to set.": "  - 設定の線幅。",
    ##################################################
    "- `line_cap`: String or LineCaps or None, default None": "- `line_cap`: String or LineCaps or None, default None",  # noqa
    ##################################################
    "  - A line-cap setting to set.": "  - 設定する線の端のスタイル設定。",
    ##################################################
    "- `line_joints`: String or LineJoints or None, default None": "- `line_joints`: String or LineJoints or None, default None",  # noqa
    ##################################################
    "  - A line-joints setting to set.": "  - 設定する線の連結部分のスタイル設定。",
    ##################################################
    "- `line_dot_setting`: LineDotSetting or None, default None": "- `line_dot_setting`: LineDotSetting or None, default None",  # noqa
    ##################################################
    "  - A dot setting to set.": "  - 設定する点線のスタイル設定。",
    ##################################################
    "- `line_dash_setting`: LineDashSetting or None, default None": "- `line_dash_setting`: LineDashSetting or None, default None",  # noqa
    ##################################################
    "  - A dash setting to set.": "  - 設定する破線のスタイル設定。",
    ##################################################
    "- `line_round_dot_setting`: LineRoundDotSetting or None, default None": "- `line_round_dot_setting`: LineRoundDotSetting or None, default None",  # noqa
    ##################################################
    "  - A round-dot setting to set.": "  - 設定する丸ドットのスタイル設定。",
    ##################################################
    "- `line_dash_dot_setting`: LineDashDotSetting or None, default None": "- `line_dash_dot_setting`: LineDashDotSetting or None, default None",  # noqa
    ##################################################
    "  - A dash-dot (1-dot chain) setting to set.": "  - 設定する一点鎖線のスタイル設定。",
    ##################################################
    "- `parent`: ChildMixIn or None, default None": "- `parent`: ChildMixIn or None, default None",  # noqa
    ##################################################
    "  - A parent instance to add this instance. If the specified value is None, this interface uses a stage instance.": "  - このインスタンスを追加する親のインスタンス。もしもNoneが指定された場合、このインスタンスはステージのインスタンスへと追加されます。",  # noqa
    ##################################################
    '- `variable_name_suffix`: str, default ""': '- `variable_name_suffix`: str, default ""',  # noqa
    ##################################################
    "  - A JavaScript variable name suffix string. This setting is sometimes useful for JavaScript debugging.": "  - JavaScript上の変数のサフィックスの設定です。この設定はJavaScriptのデバッグ時に役立つことがあります。",  # noqa
    ##################################################
    "<hr>": "<hr>",
    ##################################################
    "**[Examples]**": "**[コードサンプル]**",
    ##################################################
    '```py\n>>> import apysc as ap\n>>> stage: ap.Stage = ap.Stage()\n>>> path: ap.Path = ap.Path(\n...     path_data_list=[\n...         ap.PathMoveTo(x=0, y=50),\n...         ap.PathBezier2D(control_x=50, control_y=0, dest_x=100, dest_y=50),\n...     ],\n...     line_color=ap.Color("#ffffff"),\n...     line_thickness=3,\n... )\n>>> path.line_color\nColor("#ffffff")\n\n>>> path.line_thickness\nInt(3)\n```': '```py\n>>> import apysc as ap\n>>> stage: ap.Stage = ap.Stage()\n>>> path: ap.Path = ap.Path(\n...     path_data_list=[\n...         ap.PathMoveTo(x=0, y=50),\n...         ap.PathBezier2D(control_x=50, control_y=0, dest_x=100, dest_y=50),\n...     ],\n...     line_color=ap.Color("#ffffff"),\n...     line_thickness=3,\n... )\n>>> path.line_color\nColor("#ffffff")\n\n>>> path.line_thickness\nInt(3)\n```',  # noqa
    ##################################################
    "<hr>": "<hr>",
    ##################################################
    "**[References]**": "**[関連資料]**",
    ##################################################
    "- [Graphics draw_path interface](https://simon-ritchie.github.io/apysc/en/graphics_draw_path.html)": "- [Graphics クラスの draw_path インターフェイス](https://simon-ritchie.github.io/apysc/jp/jp_graphics_draw_path.html)",  # noqa
    ##################################################
    "- [PathMoveTo class](https://simon-ritchie.github.io/apysc/en/path_move_to.html)": "- [PathMoveTo クラス](https://simon-ritchie.github.io/apysc/jp/jp_path_move_to.html)",  # noqa
    ##################################################
    "- [PathLineTo class](https://simon-ritchie.github.io/apysc/en/path_line_to.html)": "- [PathLineTo クラス](https://simon-ritchie.github.io/apysc/jp/jp_path_line_to.html)",  # noqa
    ##################################################
    "- [PathHorizontal class](https://simon-ritchie.github.io/apysc/en/path_horizontal.html)": "- [PathHorizontal クラス](https://simon-ritchie.github.io/apysc/jp/jp_path_horizontal.html)",  # noqa
    ##################################################
    "- [PathVertical class](https://simon-ritchie.github.io/apysc/en/path_vertical.html)": "- [PathVertical クラス](https://simon-ritchie.github.io/apysc/jp/jp_path_vertical.html)",  # noqa
    ##################################################
    "- [PathClose class](https://simon-ritchie.github.io/apysc/en/path_close.html)": "- [PathClose クラス](https://simon-ritchie.github.io/apysc/jp/jp_path_close.html)",  # noqa
    ##################################################
    "- [PathBezier2D class](https://simon-ritchie.github.io/apysc/en/path_bezier_2d.html)": "- [PathBezier2D クラス](https://simon-ritchie.github.io/apysc/jp/jp_path_bezier_2d.html)",  # noqa
    ##################################################
    "- [PathBezier2DContinual class](https://simon-ritchie.github.io/apysc/en/path_bezier_2d_continual.html)": "- [PathBezier2DContinual クラス](https://simon-ritchie.github.io/apysc/jp/jp_path_bezier_2d_continual.html)",  # noqa
    ##################################################
    "- [PathBezier3D class](https://simon-ritchie.github.io/apysc/en/path_bezier_3d.html)": "- [PathBezier3D クラス](https://simon-ritchie.github.io/apysc/jp/jp_path_bezier_3d.html)",  # noqa
    ##################################################
    "- [PathBezier3DContinual class](https://simon-ritchie.github.io/apysc/en/path_bezier_3d_continual.html)": "- [PathBezier3DContinual クラス](https://simon-ritchie.github.io/apysc/jp/jp_path_bezier_3d_continual.html)",  # noqa
}
