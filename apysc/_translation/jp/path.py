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
    "The constructor also accepts each style\'s argument, such as the `fill_color` and `line_color`.": "コンストラクタは`fill_color`や`line_color`などのスタイル設定用の引数も受け付けます。",  # noqa
    ##################################################
    "```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    background_color=\"#333\", stage_width=200, stage_height=100, stage_elem_id=\"stage\"\n)\npath: ap.Path = ap.Path(\n    path_data_list=[\n        ap.PathMoveTo(x=50, y=50),\n        ap.PathLineTo(x=150, y=50),\n    ],\n    line_color=\"0af\",\n    line_thickness=5,\n)\n\nap.save_overall_html(dest_dir_path=\"path_basic_usage/\")\n```": "```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    background_color=\"#333\", stage_width=200, stage_height=100, stage_elem_id=\"stage\"\n)\npath: ap.Path = ap.Path(\n    path_data_list=[\n        ap.PathMoveTo(x=50, y=50),\n        ap.PathLineTo(x=150, y=50),\n    ],\n    line_color=\"0af\",\n    line_thickness=5,\n)\n\nap.save_overall_html(dest_dir_path=\"path_basic_usage/\")\n```",  # noqa
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
    "## Path class constructor API": "## Path クラスのコンストラクタのAPI",
    ##################################################
    "<span class=\"inconspicuous-txt\">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>": "<span class=\"inconspicuous-txt\">特記事項: このAPIドキュメントはドキュメントビルド用のスクリプトによって自動で生成・同期されています。そのためもしかしたらこの節の内容は前節までの内容と重複している場合があります。</span>",  # noqa
    ##################################################
    "**[Interface summary]** Create a path vector graphic.<hr>": "**[インターフェイス概要]** パスのベクターグラフィックスを生成します。<hr>",  # noqa
    ##################################################
    "**[Parameters]**": "**[引数]**",
    ##################################################
    "- `path_data_list`: list of PathDataBase": "- `path_data_list`: list of PathDataBase",  # noqa
    ##################################################
    "  - Target path data settings, such as the ap.PathData.MoveTo.": "  - ap.PathData.MoveToなどの対象のパスデータの設定のリスト。",  # noqa
    ##################################################
    "- `fill_color`: str or String, default \'\'": "- `fill_color`: str or String, default \'\'",  # noqa
    ##################################################
    "  - A fill-color to set.": "  - 設定する塗りの色。",
    ##################################################
    "- `fill_alpha`: float or Number, default 1.0": "- `fill_alpha`: float or Number, default 1.0",  # noqa
    ##################################################
    "  - A fill-alpha to set.": "  - 設定する塗りの透明度。",
    ##################################################
    "- `line_color`: str or String, default \'\'": "- `line_color`: str or String, default \'\'",  # noqa
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
    "  - A dash dot (1-dot chain) setting to set.": "  - 設定する一点鎖線のスタイル設定。",
    ##################################################
    "- `parent`: ChildInterface or None, default None": "- `parent`: ChildInterface or None, default None",  # noqa
    ##################################################
    "  - A parent instance to add this instance. If a specified value is None, this interface uses a stage instance.": "  - このインスタンスを追加する親のインスタンス。もしもNoneが指定された場合、このインスタンスはステージのインスタンスへと追加されます。",  # noqa
    ##################################################
    "- `variable_name_suffix`: str, default \'\'": "- `variable_name_suffix`: str, default \'\'",  # noqa
    ##################################################
    "  - A JavaScript variable name suffix string. This setting is sometimes useful for JavaScript\'s debugging.": "  - JavaScript上の変数のサフィックスの設定です。この設定はJavaScriptのデバッグ時に役立つことがあります。",  # noqa
    ##################################################
    "<hr>": "<hr>",
    ##################################################
    "**[Examples]**": "**[コードサンプル]**",
    ##################################################
    "```py\n>>> import apysc as ap\n>>> stage: ap.Stage = ap.Stage()\n>>> path: ap.Path = ap.Path(\n...     path_data_list=[\n...         ap.PathMoveTo(x=0, y=50),\n...         ap.PathBezier2D(control_x=50, control_y=0, dest_x=100, dest_y=50),\n...     ],\n...     line_color=\"#ffffff\",\n...     line_thickness=3,\n... )\n>>> path.line_color\nString(\'#ffffff\')\n\n>>> path.line_thickness\nInt(3)\n```": "```py\n>>> import apysc as ap\n>>> stage: ap.Stage = ap.Stage()\n>>> path: ap.Path = ap.Path(\n...     path_data_list=[\n...         ap.PathMoveTo(x=0, y=50),\n...         ap.PathBezier2D(control_x=50, control_y=0, dest_x=100, dest_y=50),\n...     ],\n...     line_color=\"#ffffff\",\n...     line_thickness=3,\n... )\n>>> path.line_color\nString(\'#ffffff\')\n\n>>> path.line_thickness\nInt(3)\n```",  # noqa
    ##################################################
    "<hr>": "<hr>",
    ##################################################
    "**[References]**": "**[関連資料]**",
    ##################################################
    "- [Graphics draw_path interface](https://simon-ritchie.github.io/apysc/en/graphics_draw_path.html)": "- [Graphics クラスの draw_path インターフェイス](https://simon-ritchie.github.io/apysc/en/jp_graphics_draw_path.html)",  # noqa
    ##################################################
    "- [PathMoveTo class](https://simon-ritchie.github.io/apysc/en/path_move_to.html)": "- [PathMoveTo クラス](https://simon-ritchie.github.io/apysc/en/jp_path_move_to.html)",  # noqa
    ##################################################
    "- [PathLineTo class](https://simon-ritchie.github.io/apysc/en/path_line_to.html)": "- [PathLineTo クラス](https://simon-ritchie.github.io/apysc/en/jp_path_line_to.html)",  # noqa
    ##################################################
    "- [PathHorizontal class](https://simon-ritchie.github.io/apysc/en/path_horizontal.html)": "- [PathHorizontal クラス](https://simon-ritchie.github.io/apysc/en/jp_path_horizontal.html)",  # noqa
    ##################################################
    "- [PathVertical class](https://simon-ritchie.github.io/apysc/en/path_vertical.html)": "- [PathVertical クラス](https://simon-ritchie.github.io/apysc/en/jp_path_vertical.html)",  # noqa
    ##################################################
    "- [PathClose class](https://simon-ritchie.github.io/apysc/en/path_close.html)": "- [PathClose クラス](https://simon-ritchie.github.io/apysc/en/jp_path_close.html)",  # noqa
    ##################################################
    "- [PathBezier2D class](https://simon-ritchie.github.io/apysc/en/path_bezier_2d.html)": "- [PathBezier2D クラス](https://simon-ritchie.github.io/apysc/en/jp_path_bezier_2d.html)",  # noqa
    ##################################################
    "- [PathBezier2DContinual class](https://simon-ritchie.github.io/apysc/en/path_bezier_2d_continual.html)": "- [PathBezier2DContinual クラス](https://simon-ritchie.github.io/apysc/en/jp_path_bezier_2d_continual.html)",  # noqa
    ##################################################
    "- [PathBezier3D class](https://simon-ritchie.github.io/apysc/en/path_bezier_3d.html)": "- [PathBezier3D クラス](https://simon-ritchie.github.io/apysc/en/jp_path_bezier_3d.html)",  # noqa
    ##################################################
    "- [PathBezier3DContinual class](https://simon-ritchie.github.io/apysc/en/path_bezier_3d_continual.html)": "- [PathBezier3DContinual クラス](https://simon-ritchie.github.io/apysc/en/jp_path_bezier_3d_continual.html)",  # noqa
}
