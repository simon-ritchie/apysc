"""This module is for the translation mapping data of the
following document:

Document file: path_bezier_2d.md
Language: jp
"""

from typing import Dict

MAPPING: Dict[str, str] = {
    ##################################################
    "# PathBezier2D class": "# PathBezier2D クラス",
    ##################################################
    "This page explains the `PathBezier2D` class.": "このページでは`PathBezier2D`クラスについて説明します。",  # noqa
    ##################################################
    "## What class is this?": "## クラス概要",
    ##################################################
    "The `PathBezier2D` class is the class to set a 2D bezier curve on a path.": "`PathBezier2D`クラスはパスへ2次のベジェ曲線を設定するためのクラスです。",  # noqa
    ##################################################
    "Mainly, the `Path` class constructor or `draw_path` interfaces use this setting.": "主にこの設定は`Path`クラスのコンストラクタと`draw_path`メソッドのインターフェイスで使用されます。",  # noqa
    ##################################################
    "## Basic usage": "## 基本的な使い方",
    ##################################################
    "The `PathBezier2D` class constructor requires the `control_x`, `control_y`, `dest_x`, and `dest_y` arguments.": "`PathBezier2D`クラスのコンストラクタでは`control_x`、`control_y`、`dest_x`、`dest_y`の各パラメーターが必要になります。",  # noqa
    ##################################################
    "The `control_x` and `control_y` are the coordinates to determine the control point of the bezier curve.": "`control_x`と`control_y`はベジェ曲線の制御点の座標となります。",  # noqa
    ##################################################
    "The `dest_x` and `dest_y` are the bezier curve's destination coordinates.": "`dest_x`と`dest_y`はベジェ曲線の終点座標の指定となります。",  # noqa
    ##################################################
    '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    background_color="#333", stage_width=200, stage_height=150, stage_elem_id="stage"\n)\npath: ap.Path = ap.Path(\n    path_data_list=[\n        ap.PathMoveTo(x=50, y=100),\n        ap.PathBezier2D(\n            control_x=100,\n            control_y=25,\n            dest_x=150,\n            dest_y=100,\n        ),\n    ],\n    line_color="#0af",\n    line_thickness=5,\n)\n\nap.save_overall_html(dest_dir_path="path_bezier_2d_basic_usage_1/")\n```': '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    background_color="#333", stage_width=200, stage_height=150, stage_elem_id="stage"\n)\npath: ap.Path = ap.Path(\n    path_data_list=[\n        ap.PathMoveTo(x=50, y=100),\n        ap.PathBezier2D(\n            control_x=100,\n            control_y=25,\n            dest_x=150,\n            dest_y=100,\n        ),\n    ],\n    line_color="#0af",\n    line_thickness=5,\n)\n\nap.save_overall_html(dest_dir_path="path_bezier_2d_basic_usage_1/")\n```',  # noqa
    ##################################################
    "In the following example, the magenta circle shows the control point.": "以下のコード例ではマゼンタ色の円で制御点の座標を示しています。",  # noqa
    ##################################################
    "Similarly, the cyan circle shows the destination point.": "同様に、シアンの色では終点座標を示しています。",  # noqa
    ##################################################
    '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    background_color="#333", stage_width=200, stage_height=150, stage_elem_id="stage"\n)\n\nCONTROL_X: int = 100\nCONTROL_Y: int = 25\nDEST_X: int = 150\nDEST_Y: int = 100\npath: ap.Path = ap.Path(\n    path_data_list=[\n        ap.PathMoveTo(x=50, y=100),\n        ap.PathBezier2D(\n            control_x=CONTROL_X,\n            control_y=CONTROL_Y,\n            dest_x=DEST_X,\n            dest_y=DEST_Y,\n        ),\n    ],\n    line_color="#fff",\n    line_thickness=5,\n)\n\nRADIUS: int = 5\nmagenta_circle: ap.Circle = ap.Circle(\n    x=CONTROL_X,\n    y=CONTROL_Y,\n    radius=RADIUS,\n    fill_color="#f0a",\n)\ncyan_circle: ap.Circle = ap.Circle(\n    x=DEST_X,\n    y=DEST_Y,\n    radius=RADIUS,\n    fill_color="#0af",\n)\n\nap.save_overall_html(dest_dir_path="path_bezier_2d_basic_usage_2/")\n```': '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    background_color="#333", stage_width=200, stage_height=150, stage_elem_id="stage"\n)\n\nCONTROL_X: int = 100\nCONTROL_Y: int = 25\nDEST_X: int = 150\nDEST_Y: int = 100\npath: ap.Path = ap.Path(\n    path_data_list=[\n        ap.PathMoveTo(x=50, y=100),\n        ap.PathBezier2D(\n            control_x=CONTROL_X,\n            control_y=CONTROL_Y,\n            dest_x=DEST_X,\n            dest_y=DEST_Y,\n        ),\n    ],\n    line_color="#fff",\n    line_thickness=5,\n)\n\nRADIUS: int = 5\nmagenta_circle: ap.Circle = ap.Circle(\n    x=CONTROL_X,\n    y=CONTROL_Y,\n    radius=RADIUS,\n    fill_color="#f0a",\n)\ncyan_circle: ap.Circle = ap.Circle(\n    x=DEST_X,\n    y=DEST_Y,\n    radius=RADIUS,\n    fill_color="#0af",\n)\n\nap.save_overall_html(dest_dir_path="path_bezier_2d_basic_usage_2/")\n```',  # noqa
    ##################################################
    "## Relative position setting": "## 相対座標設定",
    ##################################################
    "The constructor's `relative` optional argument changes its behavior.": "コンストラクタの`relative`のオプション引数はその挙動を変更します。",  # noqa
    ##################################################
    "For example, if you set True to its argument, coordinates become relative.": "例として、もしその引数にTrueを指定した場合座標は相対座標として設定されます。",  # noqa
    ##################################################
    "The default setting is False, and it becomes absolute.": "デフォルト値はFalseとなっており、この設定では絶対座標として扱われます。",  # noqa
    ##################################################
    "A criteria point is a starting point, not a control point.": "基準となる座標は制御点などではなく開始点となります。",  # noqa
    ##################################################
    "The following example sets the relative setting and draws the bezier curve.": "以下のコード例ではrelativeの設定を行いつつベジェ曲線を描画しています。",  # noqa
    ##################################################
    "Since it uses the `relative` setting, the `control_y` parameter becomes the minus value, and the `dest_y` becomes zero:": "`relative`の設定を使用しているため`control_y`のパラメーターは負の値となり、`dest_y`のパラメーターは0になっています:",  # noqa
    ##################################################
    '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    background_color="#333", stage_width=200, stage_height=150, stage_elem_id="stage"\n)\n\npath: ap.Path = ap.Path(\n    path_data_list=[\n        ap.PathMoveTo(x=50, y=100),\n        ap.PathBezier2D(\n            control_x=50, control_y=-75, dest_x=100, dest_y=0, relative=True\n        ),\n    ],\n    line_color="#0af",\n    line_thickness=5,\n)\n\nap.save_overall_html(dest_dir_path="path_bezier_2d_relative/")\n```': '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    background_color="#333", stage_width=200, stage_height=150, stage_elem_id="stage"\n)\n\npath: ap.Path = ap.Path(\n    path_data_list=[\n        ap.PathMoveTo(x=50, y=100),\n        ap.PathBezier2D(\n            control_x=50, control_y=-75, dest_x=100, dest_y=0, relative=True\n        ),\n    ],\n    line_color="#0af",\n    line_thickness=5,\n)\n\nap.save_overall_html(dest_dir_path="path_bezier_2d_relative/")\n```',  # noqa
    ##################################################
    "## PathBezier2D class constructor API": "## PathBezier2D クラスのコンストラクタのAPI",
    ##################################################
    '<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>': '<span class="inconspicuous-txt">特記事項: このAPIドキュメントはドキュメントビルド用のスクリプトによって自動で生成・同期されています。そのためもしかしたらこの節の内容は前節までの内容と重複している場合があります。</span>',  # noqa
    ##################################################
    "**[Interface summary]**": "**[インターフェイス概要]**",
    ##################################################
    "Path data class for the SVG's `2D bezier curve` (Q).<hr>": "SVGの2次のベジェ曲線（Q）のデータを設定するためのクラスです。<hr>",  # noqa
    ##################################################
    "**[Parameters]**": "**[引数]**",
    ##################################################
    "- `control_x`: Int or int": "- `control_x`: Int or int",
    ##################################################
    "  - X-coordinate of the bezier's control point.": "  - ベジェ曲線の制御点のX座標。",
    ##################################################
    "- `control_y`: Int or int": "- `control_y`: Int or int",
    ##################################################
    "  - Y-coordinate of the bezier's control point.": "  - ベジェ曲線の制御点のY座標。",
    ##################################################
    "- `dest_x`: Int or int": "- `dest_x`: Int or int",
    ##################################################
    "  - X-coordinate of the destination point.": "  - 終点のX座標。",
    ##################################################
    "- `dest_y`: Int or int": "- `dest_y`: Int or int",
    ##################################################
    "  - Y-coordinate of the destination point.": "  - 終点のY座標。",
    ##################################################
    "- `relative`: bool or Boolean, default False": "- `relative`: bool or Boolean, default False",  # noqa
    ##################################################
    "  - A boolean value indicates whether the path coordinates are relative or not (absolute).": "  - パスの座標が相対座標として扱うかもしくは絶対座標として扱うかどうかの真偽値。",  # noqa
    ##################################################
    "- `variable_name_suffix`: str, default ''": "- `variable_name_suffix`: str, default ''",  # noqa
    ##################################################
    "  - A JavaScript variable name suffix string. This setting is sometimes useful for JavaScript's debugging.": "  - JavaScript上の変数のサフィックスの設定です。この設定はJavaScriptのデバッグ時に役立つことがあります。",  # noqa
    ##################################################
    "<hr>": "<hr>",
    ##################################################
    "**[Examples]**": "**[コードサンプル]**",
    ##################################################
    '```py\n>>> import apysc as ap\n>>> stage: ap.Stage = ap.Stage()\n>>> sprite: ap.Sprite = ap.Sprite()\n>>> sprite.graphics.line_style(color="#fff", thickness=3)\n>>> path: ap.Path = sprite.graphics.draw_path(\n...     path_data_list=[\n...         ap.PathMoveTo(x=0, y=50),\n...         ap.PathBezier2D(control_x=50, control_y=0, dest_x=100, dest_y=50),\n...     ]\n... )\n```': '```py\n>>> import apysc as ap\n>>> stage: ap.Stage = ap.Stage()\n>>> sprite: ap.Sprite = ap.Sprite()\n>>> sprite.graphics.line_style(color="#fff", thickness=3)\n>>> path: ap.Path = sprite.graphics.draw_path(\n...     path_data_list=[\n...         ap.PathMoveTo(x=0, y=50),\n...         ap.PathBezier2D(control_x=50, control_y=0, dest_x=100, dest_y=50),\n...     ]\n... )\n```',  # noqa
    ##################################################
    "<hr>": "<hr>",
    ##################################################
    "**[References]**": "**[関連資料]**",
    ##################################################
    "- [Path class](https://simon-ritchie.github.io/apysc/en/path.html)": "- [Path クラス](https://simon-ritchie.github.io/apysc/jp/jp_path.html)",  # noqa
    ##################################################
    "- [Graphics draw_path interface](https://simon-ritchie.github.io/apysc/en/graphics_draw_path.html)": "- [Graphics クラスの draw_path インターフェイス](https://simon-ritchie.github.io/apysc/jp/jp_graphics_draw_path.html)",  # noqa
    ##################################################
    "- [PathBezier2DContinual class](https://simon-ritchie.github.io/apysc/en/path_bezier_2d_continual.html)": "- [PathBezier2DContinual クラス](https://simon-ritchie.github.io/apysc/jp/jp_path_bezier_2d_continual.html)",  # noqa
}
