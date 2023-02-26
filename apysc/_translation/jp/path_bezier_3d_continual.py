"""This module is for the translation mapping data of the
following document:

Document file: path_bezier_3d_continual.md
Language: jp
"""

from typing import Dict

MAPPING: Dict[str, str] = {
    ##################################################
    "# PathBezier3DContinual class": "# PathBezier3DContinual クラス",
    ##################################################
    "This page explains the `PathBezier3DContinual` class.": "このページでは`PathBezier3DContinual`クラスについて説明しるます。",  # noqa
    ##################################################
    "## What class is this?": "## クラス概要",
    ##################################################
    "The `PathBezier3DContinual` class is the class to set a continual 3D bezier curve on a path.": "`PathBezier3DContinual`クラスはパス上に連続した3次ベジェ曲線を設定するためのクラスです。",  # noqa
    ##################################################
    "This setting draws a smooth curve by using a line-symmetric control point.": "この設定は制御点に線対称位置を使用することで滑らかな曲線を描画します。",  # noqa
    ##################################################
    "Mainly, the `Path` class constructor or `draw_path` interfaces use this setting.": "主にこの設定は`Path`クラスのコンストラクタと`draw_path`メソッドのインターフェイスで使用されます。",  # noqa
    ##################################################
    "## Basic usage": "## 基本的な使い方",
    ##################################################
    "The `PathBezier3DContinual` class constructor requires the `control_x`, `control_y`, `dest_x`, and `dest_y` arguments.": "`PathBezier3DContinual`クラスのコンストラクタでは`control_x`、`control_y`、`dest_x`、`dest_y`の各引数の指定が必要になります。",  # noqa
    ##################################################
    "The `control_x` and `control_y` are the second control point of a bezier curve.": "`control_x`と`control_y`はベジェ曲線の2つ目の制御点の位置となります。",  # noqa
    ##################################################
    "A line-symmetric control point of a bezier curve's second control point becomes the first control point of the `PathBezier3DContinual` setting.": "ベジェ曲線の2つ目の制御点の線対称の位置は`PathBezier3DContinual`クラスの1つ目の制御点の位置として設定されます。",  # noqa
    ##################################################
    "So there are no arguments to set the first control point in the `PathBezier3DContinual` constructor.": "そのため`PathBezier3DContinual`クラスのコンストラクタには1つ目の制御点の位置の指定の引数は存在しません。",  # noqa
    ##################################################
    "The `dest_x` and `dest_y` are the destination point of a bezier curve.": "`dest_x`と`dest_y`引数はベジェ曲線の終点位置の指定となります。",  # noqa
    ##################################################
    "The `PathBezier3DContinual` class has the restriction, and you can use this class only after the `PathBezier3D` or `PathBezier3DContinual`.": "`PathBezier3DContinual`クラスには`PathBezier3D`や`PathBezier3DContinual`クラスの直後でのみ使用できるという制限が存在します。",  # noqa
    ##################################################
    '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    background_color="#333", stage_width=400, stage_height=420, stage_elem_id="stage"\n)\n\npath: ap.Path = ap.Path(\n    path_data_list=[\n        ap.PathMoveTo(x=50, y=200),\n        ap.PathBezier3D(\n            control_x1=50,\n            control_y1=25,\n            control_x2=200,\n            control_y2=25,\n            dest_x=200,\n            dest_y=200,\n        ),\n        ap.PathBezier3DContinual(\n            control_x=350,\n            control_y=375,\n            dest_x=350,\n            dest_y=200,\n        ),\n    ],\n    line_color="#0af",\n    line_thickness=5,\n)\n\nap.save_overall_html(dest_dir_path="path_bezier_3d_continual_basic_usage_1/")\n```': '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    background_color="#333", stage_width=400, stage_height=420, stage_elem_id="stage"\n)\n\npath: ap.Path = ap.Path(\n    path_data_list=[\n        ap.PathMoveTo(x=50, y=200),\n        ap.PathBezier3D(\n            control_x1=50,\n            control_y1=25,\n            control_x2=200,\n            control_y2=25,\n            dest_x=200,\n            dest_y=200,\n        ),\n        ap.PathBezier3DContinual(\n            control_x=350,\n            control_y=375,\n            dest_x=350,\n            dest_y=200,\n        ),\n    ],\n    line_color="#0af",\n    line_thickness=5,\n)\n\nap.save_overall_html(dest_dir_path="path_bezier_3d_continual_basic_usage_1/")\n```',  # noqa
    ##################################################
    "In the following example, the cyan circle shows the control point (`control_x` and `control_y`), and the magenta circle shows the destination point (`dest_x` and `dest_y`):": "以下のコード例ではシアンの円は制御点（`control_x`と`control_y`）の位置を示し、マゼンタの円では終点の位置（`dest_x`と`dest_y`）を示します。",  # noqa
    ##################################################
    '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    background_color="#333", stage_width=400, stage_height=420, stage_elem_id="stage"\n)\n\nCONTROL_X: float = 350\nCONTROL_Y: float = 375\nDEST_X: float = 350\nDEST_Y: float = 200\n\npath: ap.Path = ap.Path(\n    path_data_list=[\n        ap.PathMoveTo(x=50, y=200),\n        ap.PathBezier3D(\n            control_x1=50,\n            control_y1=25,\n            control_x2=200,\n            control_y2=25,\n            dest_x=200,\n            dest_y=200,\n        ),\n        ap.PathBezier3DContinual(\n            control_x=CONTROL_X,\n            control_y=CONTROL_Y,\n            dest_x=DEST_X,\n            dest_y=DEST_Y,\n        ),\n    ],\n    line_color="#fff",\n    line_thickness=5,\n)\n\nRADIUS: int = 10\n\ncyan_circle: ap.Circle = ap.Circle(\n    x=CONTROL_X,\n    y=CONTROL_Y,\n    radius=RADIUS,\n    fill_color="#0af",\n)\n\nmagenta_circle: ap.Circle = ap.Circle(\n    x=DEST_X,\n    y=DEST_Y,\n    radius=RADIUS,\n    fill_color="#f0a",\n)\n\nap.save_overall_html(dest_dir_path="path_bezier_3d_continual_basic_usage_2/")\n```': '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    background_color="#333", stage_width=400, stage_height=420, stage_elem_id="stage"\n)\n\nCONTROL_X: float = 350\nCONTROL_Y: float = 375\nDEST_X: float = 350\nDEST_Y: float = 200\n\npath: ap.Path = ap.Path(\n    path_data_list=[\n        ap.PathMoveTo(x=50, y=200),\n        ap.PathBezier3D(\n            control_x1=50,\n            control_y1=25,\n            control_x2=200,\n            control_y2=25,\n            dest_x=200,\n            dest_y=200,\n        ),\n        ap.PathBezier3DContinual(\n            control_x=CONTROL_X,\n            control_y=CONTROL_Y,\n            dest_x=DEST_X,\n            dest_y=DEST_Y,\n        ),\n    ],\n    line_color="#fff",\n    line_thickness=5,\n)\n\nRADIUS: int = 10\n\ncyan_circle: ap.Circle = ap.Circle(\n    x=CONTROL_X,\n    y=CONTROL_Y,\n    radius=RADIUS,\n    fill_color="#0af",\n)\n\nmagenta_circle: ap.Circle = ap.Circle(\n    x=DEST_X,\n    y=DEST_Y,\n    radius=RADIUS,\n    fill_color="#f0a",\n)\n\nap.save_overall_html(dest_dir_path="path_bezier_3d_continual_basic_usage_2/")\n```',  # noqa
    ##################################################
    "## Relative position setting": "## 相対座標設定",
    ##################################################
    "The constructor's `relative` optional argument changes its behavior.": "コンストラクタの`relative`のオプション引数はその挙動を変更します。",  # noqa
    ##################################################
    "For example, if you set True to its argument, coordinates become relative.": "例として、もしその引数にTrueを指定した場合座標は相対座標として設定されます。",  # noqa
    ##################################################
    "The default setting is False, and it becomes absolute.": "デフォルト値はFalseとなっており、この設定では絶対座標として扱われます。",  # noqa
    ##################################################
    "A criteria point is a starting point, not a control point.": "基準となる位置は制御点などではなく始点の位置となります。",  # noqa
    ##################################################
    '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    background_color="#333", stage_width=400, stage_height=420, stage_elem_id="stage"\n)\n\npath: ap.Path = ap.Path(\n    path_data_list=[\n        ap.PathMoveTo(x=50, y=200),\n        ap.PathBezier3D(\n            control_x1=50,\n            control_y1=25,\n            control_x2=200,\n            control_y2=25,\n            dest_x=200,\n            dest_y=200,\n        ),\n        ap.PathBezier3DContinual(\n            control_x=150,\n            control_y=175,\n            dest_x=150,\n            dest_y=0,\n            relative=True,\n        ),\n    ],\n    line_color="#0af",\n    line_thickness=5,\n)\n\nap.save_overall_html(dest_dir_path="path_bezier_3d_continual_relative/")\n```': '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    background_color="#333", stage_width=400, stage_height=420, stage_elem_id="stage"\n)\n\npath: ap.Path = ap.Path(\n    path_data_list=[\n        ap.PathMoveTo(x=50, y=200),\n        ap.PathBezier3D(\n            control_x1=50,\n            control_y1=25,\n            control_x2=200,\n            control_y2=25,\n            dest_x=200,\n            dest_y=200,\n        ),\n        ap.PathBezier3DContinual(\n            control_x=150,\n            control_y=175,\n            dest_x=150,\n            dest_y=0,\n            relative=True,\n        ),\n    ],\n    line_color="#0af",\n    line_thickness=5,\n)\n\nap.save_overall_html(dest_dir_path="path_bezier_3d_continual_relative/")\n```',  # noqa
    ##################################################
    "## PathBezier3DContinual class constructor API": "## PathBezier3DContinual クラスのコンストラクタのAPI",  # noqa
    ##################################################
    '<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>': '<span class="inconspicuous-txt">特記事項: このAPIドキュメントはドキュメントビルド用のスクリプトによって自動で生成・同期されています。そのためもしかしたらこの節の内容は前節までの内容と重複している場合があります。</span>',  # noqa
    ##################################################
    "**[Interface summary]**": "**[インターフェイス概要]**",
    ##################################################
    "Path data class for SVG's `continual 3D bezier curve` (S).<hr>": "SVGの連続した3次ベジェ曲線（S）のためのパスデータのクラスです。<hr>",  # noqa
    ##################################################
    "**[Parameters]**": "**[引数]**",
    ##################################################
    "- `control_x`: float or Number": "- `control_x`: float or Number",
    ##################################################
    "  - X-coordinate of the bezier's control point.": "  - ベジェ曲線の制御点のX座標。",
    ##################################################
    "- `control_y`: float or Number": "- `control_y`: float or Number",
    ##################################################
    "  - Y-coordinate of the bezier's control point.": "  - ベジェ曲線の制御点のY座標。",
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
    "- [PathBezier3D class](https://simon-ritchie.github.io/apysc/en/path_bezier_3d.html)": "- [PathBezier3D クラス](https://simon-ritchie.github.io/apysc/jp/jp_path_bezier_3d.html)",  # noqa
}
