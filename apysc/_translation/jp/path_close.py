"""This module is for the translation mapping data of the
following document:

Document file: path_close.md
Language: jp
"""

from typing import Dict

MAPPING: Dict[str, str] = {
    ##################################################
    "# PathClose class": "# PathClose クラス",
    ##################################################
    "This page explains the `PathClose` class.": "このページでは`PathClose`クラスについて説明します。",
    ##################################################
    "## What class is this?": "## クラス概要",
    ##################################################
    "The `PathClose` class is the class to close a path.": "`PathVertical`クラスはパス上に新しい垂直の直線の設定を追加するためのクラスです。",  # noqa
    ##################################################
    "If a path's start and end points are not connecting, this setting connects these points.": "もしもパスの始点と終点が繋がっていない場合、この設定はこれらの座標を接続します。",  # noqa
    ##################################################
    "Mainly, the `Path` class constructor or `draw_path` interfaces use this setting.": "主にこの設定は`Path`クラスのコンストラクタと`draw_path`メソッドのインターフェイスで使用されます。",  # noqa
    ##################################################
    "## Basic usage": "## 基本的な使い方",
    ##################################################
    "The `PathClose` class constructor takes no arguments.": "`PathClose`クラスのコンストラクタは引数を必要としません。",  # noqa
    ##################################################
    "The `Path` class constructor or `draw_path` interfaces' `path_data_list` argument requires its instance.": "`Path`クラスのコンストラクタもしくは`draw_path`メソッドのインターフェイスの`path_data_list`引数でそのインスタンスが必要とされます。",  # noqa
    ##################################################
    "In the following example, the left path graphics do not use this `Close` class setting.": "以下のコード例では、左側のパスのグラフィックスは`Close`クラスの設定を使用していません。",  # noqa
    ##################################################
    "Conversely, the right path graphics use the `Close` class setting, and it connects the start and end points:": "逆に右側のパスのグラフィックスでは`Close`クラスの設定を使用しており、始点と終点の座標が接続されています:",  # noqa
    ##################################################
    '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    background_color=ap.Color("#333"),\n    stage_width=250,\n    stage_height=150,\n    stage_elem_id="stage",\n)\nleft_path: ap.Path = ap.Path(\n    path_data_list=[\n        ap.PathMoveTo(x=75, y=50),\n        ap.PathLineTo(x=50, y=100),\n        ap.PathLineTo(x=100, y=100),\n    ],\n    line_color=ap.Color("#0af"),\n    line_thickness=5,\n)\n\nright_path: ap.Path = ap.Path(\n    path_data_list=[\n        ap.PathMoveTo(x=175, y=50),\n        ap.PathLineTo(x=150, y=100),\n        ap.PathLineTo(x=200, y=100),\n        ap.PathClose(),\n    ],\n    line_color=ap.Color("#0af"),\n    line_thickness=5,\n)\n\nap.save_overall_html(dest_dir_path="path_close_basic_usage/")\n```': '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    background_color=ap.Color("#333"),\n    stage_width=250,\n    stage_height=150,\n    stage_elem_id="stage",\n)\nleft_path: ap.Path = ap.Path(\n    path_data_list=[\n        ap.PathMoveTo(x=75, y=50),\n        ap.PathLineTo(x=50, y=100),\n        ap.PathLineTo(x=100, y=100),\n    ],\n    line_color=ap.Color("#0af"),\n    line_thickness=5,\n)\n\nright_path: ap.Path = ap.Path(\n    path_data_list=[\n        ap.PathMoveTo(x=175, y=50),\n        ap.PathLineTo(x=150, y=100),\n        ap.PathLineTo(x=200, y=100),\n        ap.PathClose(),\n    ],\n    line_color=ap.Color("#0af"),\n    line_thickness=5,\n)\n\nap.save_overall_html(dest_dir_path="path_close_basic_usage/")\n```',  # noqa
    ##################################################
    "## PathClose class constructor API": "## PathClose クラスのコンストラクタのAPI",
    ##################################################
    '<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>': '<span class="inconspicuous-txt">特記事項: このAPIドキュメントはドキュメントビルド用のスクリプトによって自動で生成・同期されています。そのためもしかしたらこの節の内容は前節までの内容と重複している場合があります。</span>',  # noqa
    ##################################################
    "**[Interface summary]**": "**[インターフェイス概要]**",
    ##################################################
    "Path data class for the SVG's `close path` (Z).<hr>": "SVGのパスを閉じる指定（Z）のためのパスデータのクラスです。<hr>",  # noqa
    ##################################################
    "**[Examples]**": "**[コードサンプル]**",
    ##################################################
    '```py\n>>> import apysc as ap\n>>> stage: ap.Stage = ap.Stage()\n>>> sprite: ap.Sprite = ap.Sprite()\n>>> sprite.graphics.line_style(color=ap.Color("#fff"), thickness=3)\n>>> path: ap.Path = sprite.graphics.draw_path(\n...     path_data_list=[\n...         ap.PathMoveTo(x=0, y=00),\n...         ap.PathLineTo(x=50, y=0),\n...         ap.PathLineTo(x=50, y=50),\n...         ap.PathClose(),\n...     ]\n... )\n```': '```py\n>>> import apysc as ap\n>>> stage: ap.Stage = ap.Stage()\n>>> sprite: ap.Sprite = ap.Sprite()\n>>> sprite.graphics.line_style(color=ap.Color("#fff"), thickness=3)\n>>> path: ap.Path = sprite.graphics.draw_path(\n...     path_data_list=[\n...         ap.PathMoveTo(x=0, y=00),\n...         ap.PathLineTo(x=50, y=0),\n...         ap.PathLineTo(x=50, y=50),\n...         ap.PathClose(),\n...     ]\n... )\n```',  # noqa
    ##################################################
    "<hr>": "<hr>",
    ##################################################
    "**[References]**": "**[関連資料]**",
    ##################################################
    "- [Path class](https://simon-ritchie.github.io/apysc/en/path.html)": "- [Path クラス](https://simon-ritchie.github.io/apysc/jp/jp_path.html)",  # noqa
    ##################################################
    "- [Graphics draw_path interface](https://simon-ritchie.github.io/apysc/en/graphics_draw_path.html)": "- [Graphics クラスの draw_path インターフェイス](https://simon-ritchie.github.io/apysc/jp/jp_graphics_draw_path.html)",  # noqa
}
