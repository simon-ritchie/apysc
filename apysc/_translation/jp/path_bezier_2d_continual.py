"""This module is for the translation mapping data of the
following document:

Document file: path_bezier_2d_continual.md
Language: jp
"""

from typing import Dict

MAPPING: Dict[str, str] = {
    ##################################################
    "# PathBezier2DContinual class": "# PathBezier2DContinual クラス",
    ##################################################
    "This page explains the `PathBezier2DContinual` class.": "このページでは`PathBezier2DContinual`クラスについて説明します。",  # noqa
    ##################################################
    "## What class is this?": "## クラス概要",
    ##################################################
    "The `PathBezier2DContinual` class is the class to set a continual 2D bezier curve on a path.": "PathBezier2DContinual`クラスはパスに連続した2次元のベジェ曲線を設定するためのクラスです。",  # noqa
    ##################################################
    "This setting draws a smooth curve by using a line-symmetric control point.": "この設定は線対称な位置の制御点を使うことで滑らかな曲線を描画します。",  # noqa
    ##################################################
    "Mainly, the `Path` class constructor or `draw_path` interfaces use this setting.": "主にこの設定は`Path`クラスのコンストラクタと`draw_path`メソッドのインターフェイスで使用されます。",  # noqa
    ##################################################
    "## Basic usage": "## 基本的な使い方",
    ##################################################
    "The `PathBezier2DContinual` class constructor requires the `x` and `y` arguments.": "`PathBezier2DContinual`クラスのコンストラクタは`x`と`y`の引数を必要とします。",  # noqa
    ##################################################
    "These coordinates are the destination points of the bezier curve.": "これらの座標はベジェ曲線の終点座標の指定となります。",  # noqa
    ##################################################
    "The `PathBezier2DContinual` class has a restriction, and you can use this class only after the `PathBezier2D` or `PathBezier2DContinual`.": "`PathBezier2DContinual`クラスは`PathBezier2D`もしくは`PathBezier2DContinual`クラスの直後でのみ使用することができるという制限があります。",  # noqa
    ##################################################
    '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    background_color=ap.Color("#333"),\n    stage_width=400,\n    stage_height=200,\n    stage_elem_id="stage",\n)\n\npath: ap.Path = ap.Path(\n    path_data_list=[\n        ap.PathMoveTo(x=50, y=100),\n        ap.PathBezier2D(\n            control_x=100,\n            control_y=25,\n            dest_x=150,\n            dest_y=100,\n        ),\n        ap.PathBezier2DContinual(\n            x=250,\n            y=100,\n        ),\n        ap.PathBezier2DContinual(\n            x=350,\n            y=100,\n        ),\n    ],\n    line_color=ap.Color("#0af"),\n    line_thickness=5,\n)\n\nap.save_overall_html(dest_dir_path="path_bezier_2d_continual_basic_usage/")\n```': '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    background_color=ap.Color("#333"),\n    stage_width=400,\n    stage_height=200,\n    stage_elem_id="stage",\n)\n\npath: ap.Path = ap.Path(\n    path_data_list=[\n        ap.PathMoveTo(x=50, y=100),\n        ap.PathBezier2D(\n            control_x=100,\n            control_y=25,\n            dest_x=150,\n            dest_y=100,\n        ),\n        ap.PathBezier2DContinual(\n            x=250,\n            y=100,\n        ),\n        ap.PathBezier2DContinual(\n            x=350,\n            y=100,\n        ),\n    ],\n    line_color=ap.Color("#0af"),\n    line_thickness=5,\n)\n\nap.save_overall_html(dest_dir_path="path_bezier_2d_continual_basic_usage/")\n```',  # noqa
    ##################################################
    "## Relative position setting": "## 相対座標設定",
    ##################################################
    "The constructor's `relative` optional argument changes its behavior.": "コンストラクタの`relative`のオプション引数はその挙動を変更します。",  # noqa
    ##################################################
    "For example, if you set True to its argument, coordinates become relative.": "例として、もしその引数にTrueを指定した場合座標は相対座標として設定されます。",  # noqa
    ##################################################
    "The default setting is False, and it becomes absolute.": "デフォルト値はFalseとなっており、この設定では絶対座標として扱われます。",  # noqa
    ##################################################
    '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    background_color=ap.Color("#333"),\n    stage_width=400,\n    stage_height=200,\n    stage_elem_id="stage",\n)\n\npath: ap.Path = ap.Path(\n    path_data_list=[\n        ap.PathMoveTo(x=50, y=100),\n        ap.PathBezier2D(\n            control_x=100,\n            control_y=25,\n            dest_x=150,\n            dest_y=100,\n        ),\n        ap.PathBezier2DContinual(\n            x=100,\n            y=0,\n            relative=True,\n        ),\n        ap.PathBezier2DContinual(\n            x=100,\n            y=0,\n            relative=True,\n        ),\n    ],\n    line_color=ap.Color("#0af"),\n    line_thickness=5,\n)\n\nap.save_overall_html(dest_dir_path="path_bezier_2d_continual_relative/")\n```': '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    background_color=ap.Color("#333"),\n    stage_width=400,\n    stage_height=200,\n    stage_elem_id="stage",\n)\n\npath: ap.Path = ap.Path(\n    path_data_list=[\n        ap.PathMoveTo(x=50, y=100),\n        ap.PathBezier2D(\n            control_x=100,\n            control_y=25,\n            dest_x=150,\n            dest_y=100,\n        ),\n        ap.PathBezier2DContinual(\n            x=100,\n            y=0,\n            relative=True,\n        ),\n        ap.PathBezier2DContinual(\n            x=100,\n            y=0,\n            relative=True,\n        ),\n    ],\n    line_color=ap.Color("#0af"),\n    line_thickness=5,\n)\n\nap.save_overall_html(dest_dir_path="path_bezier_2d_continual_relative/")\n```',  # noqa
    ##################################################
    "## PathBezier2DContinual class constructor API": "## PathBezier2DContinual クラスのコンストラクタのAPI",  # noqa
    ##################################################
    '<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>': '<span class="inconspicuous-txt">特記事項: このAPIドキュメントはドキュメントビルド用のスクリプトによって自動で生成・同期されています。そのためもしかしたらこの節の内容は前節までの内容と重複している場合があります。</span>',  # noqa
    ##################################################
    "**[Interface summary]**": "**[インターフェイス概要]**",
    ##################################################
    "Path data class for the SVG `continual 2D bezier curve` (T).<hr>": "SVGの連続した2次元のベジェ曲線のデータ設定用のクラスです。<hr>",  # noqa
    ##################################################
    "**[Parameters]**": "**[引数]**",
    ##################################################
    "- `x`: float or Number": "- `x`: float or Number",
    ##################################################
    "  - X-coordinate of the destination point.": "  - 終点のX座標。",
    ##################################################
    "- `y`: float or Number": "- `y`: float or Number",
    ##################################################
    "  - Y-coordinate of the destination point.": "  - 終点のY座標。",
    ##################################################
    "- `relative`: bool or Boolean, default False": "- `relative`: bool or Boolean, default False",  # noqa
    ##################################################
    "  - A boolean value indicates whether the path coordinates are relative or not (absolute).": "  - パスの座標が相対座標として扱うかもしくは絶対座標として扱うかどうかの真偽値。",  # noqa
    ##################################################
    '- `variable_name_suffix`: str, default ""': '- `variable_name_suffix`: str, default ""',  # noqa
    ##################################################
    "  - A JavaScript variable name suffix string. This setting is sometimes useful for JavaScript debugging.": "  - JavaScript上の変数のサフィックスの設定です。この設定はJavaScriptのデバッグ時に役立つことがあります。",  # noqa
    ##################################################
    "<hr>": "<hr>",
    ##################################################
    "**[Examples]**": "**[コードサンプル]**",
    ##################################################
    '```py\n>>> import apysc as ap\n>>> stage: ap.Stage = ap.Stage()\n>>> sprite: ap.Sprite = ap.Sprite()\n>>> sprite.graphics.line_style(color=ap.Color("#fff"), thickness=3)\n>>> path: ap.Path = sprite.graphics.draw_path(\n...     path_data_list=[\n...         ap.PathMoveTo(x=0, y=50),\n...         ap.PathBezier2D(control_x=50, control_y=0, dest_x=100, dest_y=50),\n...         ap.PathBezier2DContinual(x=150, y=50),\n...     ]\n... )\n```': '```py\n>>> import apysc as ap\n>>> stage: ap.Stage = ap.Stage()\n>>> sprite: ap.Sprite = ap.Sprite()\n>>> sprite.graphics.line_style(color=ap.Color("#fff"), thickness=3)\n>>> path: ap.Path = sprite.graphics.draw_path(\n...     path_data_list=[\n...         ap.PathMoveTo(x=0, y=50),\n...         ap.PathBezier2D(control_x=50, control_y=0, dest_x=100, dest_y=50),\n...         ap.PathBezier2DContinual(x=150, y=50),\n...     ]\n... )\n```',  # noqa
    ##################################################
    "<hr>": "<hr>",
    ##################################################
    "**[References]**": "**[関連資料]**",
    ##################################################
    "- [Path class](https://simon-ritchie.github.io/apysc/en/path.html)": "- [Path クラス](https://simon-ritchie.github.io/apysc/jp/jp_path.html)",  # noqa
    ##################################################
    "- [Graphics draw_path interface](https://simon-ritchie.github.io/apysc/en/graphics_draw_path.html)": "- [Graphics クラスの draw_path インターフェイス](https://simon-ritchie.github.io/apysc/jp/jp_graphics_draw_path.html)",  # noqa
    ##################################################
    "- [PathBezier2D class](https://simon-ritchie.github.io/apysc/en/path_bezier_2d.html)": "- [PathBezier2D クラス](https://simon-ritchie.github.io/apysc/jp/jp_path_bezier_2d.html)",  # noqa
}
