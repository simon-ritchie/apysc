"""This module is for the translation mapping data of the
following document:

Document file: graphics_draw_path.md
Language: jp
"""

from typing import Dict

MAPPING: Dict[str, str] = {
    ##################################################
    "# Graphics draw_path interface": "# Graphics クラスの draw_path インターフェイス",
    ##################################################
    "This page explains the `Graphics` class `draw_path` interface.": "このページでは`Graphics`クラスの`draw_path`インターフェイスについて説明します。",  # noqa
    ##################################################
    "## What interface is this?": "## インターフェイス概要",
    ##################################################
    "The `draw_path` interface draws vector graphics of a path.": "`draw_path`インターフェイスはベクターグラフィックスのパスを描画します。",  # noqa
    ##################################################
    "## Basic usage": "## 基本的な使い方",
    ##################################################
    "The `draw_path` interface requires the `path_data_list` argument.": "`draw_path`インターフェイスは`path_data_list`引数の指定を必要とします。",  # noqa
    ##################################################
    "The `path_data_list` argument is a list of path data, such as the `PathLineTo` or `PathBezier2D`.": "`path_data_list`引数は`PathLineTo`や`PathBezier2D`などのパスデータの配列となります。",  # noqa
    ##################################################
    '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    background_color="#333", stage_width=300, stage_height=150, stage_elem_id="stage"\n)\nsprite: ap.Sprite = ap.Sprite()\nsprite.graphics.line_style(color="#0af", thickness=5)\npath: ap.Path = sprite.graphics.draw_path(\n    path_data_list=[\n        ap.PathMoveTo(x=50, y=100),\n        ap.PathLineTo(x=100, y=100),\n        ap.PathLineTo(x=150, y=50),\n        ap.PathBezier2D(\n            control_x=200,\n            control_y=100,\n            dest_x=250,\n            dest_y=50,\n        ),\n    ],\n)\n\nap.save_overall_html(dest_dir_path="graphics_draw_path_basic_usage/")\n```': '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    background_color="#333", stage_width=300, stage_height=150, stage_elem_id="stage"\n)\nsprite: ap.Sprite = ap.Sprite()\nsprite.graphics.line_style(color="#0af", thickness=5)\npath: ap.Path = sprite.graphics.draw_path(\n    path_data_list=[\n        ap.PathMoveTo(x=50, y=100),\n        ap.PathLineTo(x=100, y=100),\n        ap.PathLineTo(x=150, y=50),\n        ap.PathBezier2D(\n            control_x=200,\n            control_y=100,\n            dest_x=250,\n            dest_y=50,\n        ),\n    ],\n)\n\nap.save_overall_html(dest_dir_path="graphics_draw_path_basic_usage/")\n```',  # noqa
    ##################################################
    "## See also": "## 関連資料",
    ##################################################
    "- [Path class](path.md)": "- [Path クラス](jp_path.md)",
    ##################################################
    "- [PathMoveTo class](path_move_to.md)": "- [PathMoveTo クラス](jp_path_move_to.md)",
    ##################################################
    "- [PathLineTo class](path_line_to.md)": "- [PathLineTo クラス](jp_path_line_to.md)",
    ##################################################
    "- [PathHorizontal class](path_horizontal.md)": "- [PathHorizontal クラス](jp_path_horizontal.md)",  # noqa
    ##################################################
    "- [PathVertical class](path_vertical.md)": "- [PathVertical クラス](jp_path_vertical.md)",  # noqa
    ##################################################
    "- [PathClose class](path_close.md)": "- [PathClose クラス](jp_path_close.md)",
    ##################################################
    "- [PathBezier2D class](path_bezier_2d.md)": "- [PathBezier2D クラス](jp_path_bezier_2d.md)",  # noqa
    ##################################################
    "- [PathBezier2DContinual class](path_bezier_3d.md)": "- [PathBezier2DContinual クラス](jp_path_bezier_3d.md)",  # noqa
    ##################################################
    "- [PathBezier3DContinual class](path_bezier_3d_continual.md)": "- [PathBezier3DContinual クラス](jp_path_bezier_3d_continual.md)",  # noqa
    ##################################################
    "## draw_path API": "## draw_path API",
    ##################################################
    '<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>': '<span class="inconspicuous-txt">特記事項: このAPIドキュメントはドキュメントビルド用のスクリプトによって自動で生成・同期されています。そのためもしかしたらこの節の内容は前節までの内容と重複している場合があります。</span>',  # noqa
    ##################################################
    "**[Interface summary]**": "**[インターフェイス概要]**",
    ##################################################
    "Draw a path vector graphics.<hr>": "パスのベクターグラフィックスを描画します。<hr>",
    ##################################################
    "**[Parameters]**": "**[引数]**",
    ##################################################
    "- `path_data_list`: list of PathDataBase": "- `path_data_list`: list of PathDataBase",  # noqa
    ##################################################
    "  - Target path data settings, such as the ap.PathData.MoveTo.": "  - ap.PathData.MoveToなどの対象のパスデータの設定のリスト。",  # noqa
    ##################################################
    "- `variable_name_suffix`: str, default ''": "- `variable_name_suffix`: str, default ''",  # noqa
    ##################################################
    "  - A JavaScript variable name suffix string. This setting is sometimes useful for JavaScript's debugging.": "  - JavaScript上の変数のサフィックスの設定です。この設定はJavaScriptのデバッグ時に役立つことがあります。",  # noqa
    ##################################################
    "<hr>": "<hr>",
    ##################################################
    "**[Returns]**": "**[返却値]**",
    ##################################################
    "- `path`: Path": "- `path`: Path",
    ##################################################
    "  - Created path graphics instance.": "  - 作成されたパスのグラフィックスのインスタンス。",
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
