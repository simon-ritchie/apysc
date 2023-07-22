"""This module is for the translation mapping data of the
following document:

Document file: path_bezier_3d.md
Language: jp
"""

from typing import Dict

MAPPING: Dict[str, str] = {
    ##################################################
    "# PathBezier3D class": "# PathBezier3D クラス",
    ##################################################
    "This page explains the `PathBezier3D` class.": "このページでは`PathBezier3D`クラスについて説明します。",  # noqa
    ##################################################
    "## What class is this?": "## クラス概要",
    ##################################################
    "The `PathBezier3D` class is the class to set a 3D bezier curve on a path.": "`PathBezier3D`クラスはパス上に3次のベジェ曲線を設定するためのクラスです。",  # noqa
    ##################################################
    "This class has two control points (as a comparison, the 2D bezier class has one control point).": "このクラスは2つの制御点を持ちます（比較対象として、2次のベジェ曲線では1つの制御点のみを持ちます）。",  # noqa
    ##################################################
    "Mainly, the `Path` class constructor or `draw_path` interfaces use this setting.": "主にこの設定は`Path`クラスのコンストラクタと`draw_path`メソッドのインターフェイスで使用されます。",  # noqa
    ##################################################
    "## Basic usage": "## 基本的な使い方",
    ##################################################
    "The `PathBezier3D` class constructor requires the `control_x1`, `control_y1`, `control_x2`, `control_y2`, `dest_x`, and `dest_y` arguments.": "`PathBezier3D`クラスのコンストラクタでは`control_x1`、`control_y1`、`control_x2`、`control_y2`、`dest_x`、`dest_y`の各引数の指定が必要です。",  # noqa
    ##################################################
    "The `control_x1` and `control_y1` are the coordinates to determine the first control point of the bezier curve.": "`control_x1`と`control_y1`はベジェ曲線の最初の制御点の位置を決定するための座標指定です。",  # noqa
    ##################################################
    "Similarly, the `control_x2` and `control_y2` are the coordinates to determine the second control point of the bezier curve.": "同様に、`control_x2`と`control_y2`はベジェ曲線の2番目の制御点の位置を決定するための座標指定です。",  # noqa
    ##################################################
    "The `dest_x` and `dest_y` are the bezier curve's destination coordinates.": "`dest_x`と`dest_y`はベジェ曲線の終点座標の指定となります。",  # noqa
    ##################################################
    '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    background_color="#333", stage_width=250, stage_height=270, stage_elem_id="stage"\n)\n\npath: ap.Path = ap.Path(\n    path_data_list=[\n        ap.PathMoveTo(x=50, y=200),\n        ap.PathBezier3D(\n            control_x1=50,\n            control_y1=25,\n            control_x2=200,\n            control_y2=25,\n            dest_x=200,\n            dest_y=200,\n        ),\n    ],\n    line_color="#0af",\n    line_thickness=5,\n)\n\nap.save_overall_html(dest_dir_path="path_bezier_3d_basic_usage_1/")\n```': '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    background_color="#333", stage_width=250, stage_height=270, stage_elem_id="stage"\n)\n\npath: ap.Path = ap.Path(\n    path_data_list=[\n        ap.PathMoveTo(x=50, y=200),\n        ap.PathBezier3D(\n            control_x1=50,\n            control_y1=25,\n            control_x2=200,\n            control_y2=25,\n            dest_x=200,\n            dest_y=200,\n        ),\n    ],\n    line_color="#0af",\n    line_thickness=5,\n)\n\nap.save_overall_html(dest_dir_path="path_bezier_3d_basic_usage_1/")\n```',  # noqa
    ##################################################
    "In the following example, the cyan circle shows the first control point of the bezier curve.": "以下のコード例では、シアン色の円はベジェ曲線の最初の制御点を示しています。",  # noqa
    ##################################################
    "The magenta circle shows the second control point of the bezier curve.": "マゼンタの円ではベジェ曲線の2つ目の制御点を示しています。",  # noqa
    ##################################################
    "And also, the yellow circle shows the destination point of the bezier curve.": "また、黄色の円ではベジェ曲線の終点座標を示しています。",  # noqa
    ##################################################
    '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    background_color="#333", stage_width=250, stage_height=270, stage_elem_id="stage"\n)\n\nCONTROL_X1: float = 50\nCONTROL_Y1: float = 25\nCONTROL_X2: float = 200\nCONTROL_Y2: float = 25\nDEST_X: float = 200\nDEST_Y: float = 200\n\npath: ap.Path = ap.Path(\n    path_data_list=[\n        ap.PathMoveTo(x=50, y=200),\n        ap.PathBezier3D(\n            control_x1=CONTROL_X1,\n            control_y1=CONTROL_Y1,\n            control_x2=CONTROL_X2,\n            control_y2=CONTROL_Y2,\n            dest_x=DEST_X,\n            dest_y=DEST_Y,\n        ),\n    ],\n    line_color="#fff",\n    line_thickness=5,\n)\n\nRADIUS: int = 10\ncyan_circle: ap.Circle = ap.Circle(\n    x=CONTROL_X1,\n    y=CONTROL_Y1,\n    radius=RADIUS,\n    fill_color="#0af",\n)\n\nmagenta_circle: ap.Circle = ap.Circle(\n    x=CONTROL_X2,\n    y=CONTROL_Y2,\n    radius=RADIUS,\n    fill_color="#f0a",\n)\n\nyellow_circle: ap.Circle = ap.Circle(\n    x=DEST_X,\n    y=DEST_Y,\n    radius=RADIUS,\n    fill_color="#ff0",\n)\n\nap.save_overall_html(dest_dir_path="path_bezier_3d_basic_usage_2/")\n```': '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    background_color="#333", stage_width=250, stage_height=270, stage_elem_id="stage"\n)\n\nCONTROL_X1: float = 50\nCONTROL_Y1: float = 25\nCONTROL_X2: float = 200\nCONTROL_Y2: float = 25\nDEST_X: float = 200\nDEST_Y: float = 200\n\npath: ap.Path = ap.Path(\n    path_data_list=[\n        ap.PathMoveTo(x=50, y=200),\n        ap.PathBezier3D(\n            control_x1=CONTROL_X1,\n            control_y1=CONTROL_Y1,\n            control_x2=CONTROL_X2,\n            control_y2=CONTROL_Y2,\n            dest_x=DEST_X,\n            dest_y=DEST_Y,\n        ),\n    ],\n    line_color="#fff",\n    line_thickness=5,\n)\n\nRADIUS: int = 10\ncyan_circle: ap.Circle = ap.Circle(\n    x=CONTROL_X1,\n    y=CONTROL_Y1,\n    radius=RADIUS,\n    fill_color="#0af",\n)\n\nmagenta_circle: ap.Circle = ap.Circle(\n    x=CONTROL_X2,\n    y=CONTROL_Y2,\n    radius=RADIUS,\n    fill_color="#f0a",\n)\n\nyellow_circle: ap.Circle = ap.Circle(\n    x=DEST_X,\n    y=DEST_Y,\n    radius=RADIUS,\n    fill_color="#ff0",\n)\n\nap.save_overall_html(dest_dir_path="path_bezier_3d_basic_usage_2/")\n```',  # noqa
    ##################################################
    "## Relative position setting": "## 相対座標設定",
    ##################################################
    "The constructor's `relative` optional argument changes its behavior.": "コンストラクタの`relative`のオプション引数はその挙動を変更します。",  # noqa
    ##################################################
    "For example, if you set True to its argument, coordinates become relative.": "例として、もしその引数にTrueを指定した場合座標は相対座標として設定されます。",  # noqa
    ##################################################
    "The default setting is False, and it becomes absolute.": "デフォルト値はFalseとなっており、この設定では絶対座標として扱われます。",  # noqa
    ##################################################
    "A criteria point is a starting point, neither a first control point nor a second control point.": "基準点は開始位置の座標となります。最初の制御点や2つ目の制御点ではありません。",  # noqa
    ##################################################
    "The following example sets the relative setting and draws the bezier curve.": "以下のコード例ではrelativeの設定をしてベジェ曲線を描画しています。",  # noqa
    ##################################################
    '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    background_color="#333", stage_width=250, stage_height=270, stage_elem_id="stage"\n)\n\npath: ap.Path = ap.Path(\n    path_data_list=[\n        ap.PathMoveTo(x=50, y=200),\n        ap.PathBezier3D(\n            control_x1=0,\n            control_y1=-175,\n            control_x2=150,\n            control_y2=-175,\n            dest_x=150,\n            dest_y=0,\n            relative=True,\n        ),\n    ],\n    line_color="#0af",\n    line_thickness=5,\n)\n\nap.save_overall_html(dest_dir_path="path_bezier_3d_relative/")\n```': '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    background_color="#333", stage_width=250, stage_height=270, stage_elem_id="stage"\n)\n\npath: ap.Path = ap.Path(\n    path_data_list=[\n        ap.PathMoveTo(x=50, y=200),\n        ap.PathBezier3D(\n            control_x1=0,\n            control_y1=-175,\n            control_x2=150,\n            control_y2=-175,\n            dest_x=150,\n            dest_y=0,\n            relative=True,\n        ),\n    ],\n    line_color="#0af",\n    line_thickness=5,\n)\n\nap.save_overall_html(dest_dir_path="path_bezier_3d_relative/")\n```',  # noqa
    ##################################################
    "## PathBezier3D class constructor API": "## PathBezier3D クラスのコンストラクタのAPI",
    ##################################################
    '<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>': '<span class="inconspicuous-txt">特記事項: このAPIドキュメントはドキュメントビルド用のスクリプトによって自動で生成・同期されています。そのためもしかしたらこの節の内容は前節までの内容と重複している場合があります。</span>',  # noqa
    ##################################################
    "**[Interface summary]**": "**[インターフェイス概要]**",
    ##################################################
    "Path data class for the SVG's `3D bezier curve` (C).<hr>": "SVGの3次のベジェ曲線（C）のパスデータのためのクラスです。<hr>",  # noqa
    ##################################################
    "**[Parameters]**": "**[引数]**",
    ##################################################
    "- `control_x1`: float or Number": "- `control_x1`: float or Number",
    ##################################################
    "  - X-coordinate of the bezier's first control point.": "  - ベジェ曲線の最初の制御点のX座標。",
    ##################################################
    "- `control_y1`: float or Number": "- `control_y1`: float or Number",
    ##################################################
    "  - Y-coordinate of the bezier's first control point.": "  - ベジェ曲線の最初の制御点のY座標。",
    ##################################################
    "- `control_x2`: float or Number": "- `control_x2`: float or Number",
    ##################################################
    "  - X-coordinate of the bezier's second control point.": "  - ベジェ曲線の2つ目の制御点のX座標。",  # noqa
    ##################################################
    "- `control_y2`: float or Number": "- `control_y2`: float or Number",
    ##################################################
    "  - Y-coordinate of the bezier's second control point.": "  - ベジェ曲線の2つ目の制御点のY座標。",  # noqa
    ##################################################
    "- `dest_x`: float or Number": "- `dest_x`: float or Number",
    ##################################################
    "  - X-coordinate of the destination point.": "  - 終点のX座標。",
    ##################################################
    "- `dest_y`: float or Number": "- `dest_y`: float or Number",
    ##################################################
    "  - Y-coordinate of the destination point.": "  - 終点のY座標。",
    ##################################################
    "- `relative`: bool or Boolean, default False": "- `relative`: bool or Boolean, default False",  # noqa
    ##################################################
    "  - A boolean value indicates whether the path coordinates are relative or not (absolute).": "  - パスの座標が相対座標として扱うかもしくは絶対座標として扱うかどうかの真偽値。",  # noqa
    ##################################################
    "- `variable_name_suffix`: str, default ''": "- `variable_name_suffix`: str, default ''",  # noqa
    ##################################################
    "  - A JavaScript variable name suffix string. This setting is sometimes useful for JavaScript debugging.": "  - JavaScript上の変数のサフィックスの設定です。この設定はJavaScriptのデバッグ時に役立つことがあります。",  # noqa
    ##################################################
    "<hr>": "<hr>",
    ##################################################
    "**[Examples]**": "**[コードサンプル]**",
    ##################################################
    '```py\n>>> import apysc as ap\n>>> stage: ap.Stage = ap.Stage()\n>>> sprite: ap.Sprite = ap.Sprite()\n>>> sprite.graphics.line_style(color="#fff", thickness=3)\n>>> path: ap.Path = sprite.graphics.draw_path(\n...     path_data_list=[\n...         ap.PathMoveTo(x=0, y=50),\n...         ap.PathBezier3D(\n...             control_x1=0,\n...             control_y1=0,\n...             control_x2=50,\n...             control_y2=0,\n...             dest_x=50,\n...             dest_y=50,\n...         ),\n...         ap.PathBezier3DContinual(\n...             control_x=100, control_y=100, dest_x=100, dest_y=50\n...         ),\n...     ]\n... )\n```': '```py\n>>> import apysc as ap\n>>> stage: ap.Stage = ap.Stage()\n>>> sprite: ap.Sprite = ap.Sprite()\n>>> sprite.graphics.line_style(color="#fff", thickness=3)\n>>> path: ap.Path = sprite.graphics.draw_path(\n...     path_data_list=[\n...         ap.PathMoveTo(x=0, y=50),\n...         ap.PathBezier3D(\n...             control_x1=0,\n...             control_y1=0,\n...             control_x2=50,\n...             control_y2=0,\n...             dest_x=50,\n...             dest_y=50,\n...         ),\n...         ap.PathBezier3DContinual(\n...             control_x=100, control_y=100, dest_x=100, dest_y=50\n...         ),\n...     ]\n... )\n```',  # noqa
    ##################################################
    "<hr>": "<hr>",
    ##################################################
    "**[References]**": "**[関連資料]**",
    ##################################################
    "- [Path class](https://simon-ritchie.github.io/apysc/en/path.html)": "- [Path クラス](https://simon-ritchie.github.io/apysc/jp/jp_path.html)",  # noqa
    ##################################################
    "- [Graphics draw_path interface](https://simon-ritchie.github.io/apysc/en/graphics_draw_path.html)": "- [Graphics クラスの draw_path インターフェイス](https://simon-ritchie.github.io/apysc/jp/jp_graphics_draw_path.html)",  # noqa
    ##################################################
    "- [PathBezier3DContinual class](https://simon-ritchie.github.io/apysc/en/path_bezier_3d_continual.html)": "- [PathBezier3DContinual クラス](https://simon-ritchie.github.io/apysc/jp/jp_path_bezier_3d_continual.html)",  # noqa
}
