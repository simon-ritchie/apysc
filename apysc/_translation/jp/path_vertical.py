"""This module is for the translation mapping data of the
following document:

Document file: path_vertical.md
Language: jp
"""

from typing import Dict

MAPPING: Dict[str, str] = {
    ##################################################
    "# PathVertical class": "# PathVertical クラス",
    ##################################################
    "This page explains the `PathVertical` class.": "このページでは`PathVertical`クラスについて説明します。",  # noqa
    ##################################################
    "## What class is this?": "## クラス概要",
    ##################################################
    "The `PathVertical` class is the class to set a new vertical line on a path.": "`PathVertical`クラスはパス上に新しい垂直の直線の設定を追加するためのクラスです。",  # noqa
    ##################################################
    "It simplifies an implementation if you need to draw a vertical line and not change a horizontal coordinate.": "この設定はもし垂直方向の線の描画のみが必要で水平方向の座標設定が不要な場合にコードの記述をシンプルにします。",  # noqa
    ##################################################
    "Mainly, the `Path` class constructor or `draw_path` interfaces use this setting.": "主にこの設定は`Path`クラスのコンストラクタと`draw_path`メソッドのインターフェイスで使用されます。",  # noqa
    ##################################################
    "## Basic usage": "## 基本的な使い方",
    ##################################################
    "The `PathVertical` class constructor requires only one argument, `y`.": "`PathVertical`クラスのコンストラクタでは`y`の引数指定のみ必要とします。",  # noqa
    ##################################################
    "The `Path` class constructor or `draw_path` interfaces' `path_data_list` argument requires its instance.": "`Path`クラスのコンストラクタもしくは`draw_path`メソッドのインターフェイスの`path_data_list`引数でそのインスタンスが必要とされます。",  # noqa
    ##################################################
    "The following example sets the y=150 coordinates and draws the vertical line from the y=50 coordinate:": "以下のコード例ではy=50の座標からy=150の座標に向けて垂直の直線を描画しています:",  # noqa
    ##################################################
    '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    background_color=ap.Color("#333"),\n    stage_width=100,\n    stage_height=200,\n    stage_elem_id="stage",\n)\npath: ap.Path = ap.Path(\n    path_data_list=[\n        ap.PathMoveTo(x=50, y=50),\n        ap.PathVertical(y=150),\n    ],\n    line_color=ap.Color("#0af"),\n    line_thickness=5,\n)\n\nap.save_overall_html(dest_dir_path="path_vertical_basic_usage/")\n```': '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    background_color=ap.Color("#333"),\n    stage_width=100,\n    stage_height=200,\n    stage_elem_id="stage",\n)\npath: ap.Path = ap.Path(\n    path_data_list=[\n        ap.PathMoveTo(x=50, y=50),\n        ap.PathVertical(y=150),\n    ],\n    line_color=ap.Color("#0af"),\n    line_thickness=5,\n)\n\nap.save_overall_html(dest_dir_path="path_vertical_basic_usage/")\n```',  # noqa
    ##################################################
    "## Relative position setting": "## 相対座標設定",
    ##################################################
    "The constructor's `relative` optional argument changes its behavior.": "コンストラクタの`relative`のオプション引数はその挙動を変更します。",  # noqa
    ##################################################
    "For example, if you set True to its argument, coordinates become relative.": "例として、もしその引数にTrueを指定した場合座標は相対座標として設定されます。",  # noqa
    ##################################################
    "The default setting is False, and it becomes absolute.": "デフォルト値はFalseとなっており、この設定では絶対座標として扱われます。",  # noqa
    ##################################################
    "The following example sets the relative setting and draws the line to the 50px under position from the current position:": "以下のコード例ではrelativeの設定をして現在の座標から垂直方向に50px下の位置に直線を描画しています:",  # noqa
    ##################################################
    '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    background_color=ap.Color("#333"),\n    stage_width=100,\n    stage_height=150,\n    stage_elem_id="stage",\n)\npath: ap.Path = ap.Path(\n    path_data_list=[\n        ap.PathMoveTo(x=50, y=50),\n        ap.PathVertical(y=50, relative=True),\n    ],\n    line_color=ap.Color("#0af"),\n    line_thickness=5,\n)\n\nap.save_overall_html(dest_dir_path="path_vertical_relative/")\n```': '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    background_color=ap.Color("#333"),\n    stage_width=100,\n    stage_height=150,\n    stage_elem_id="stage",\n)\npath: ap.Path = ap.Path(\n    path_data_list=[\n        ap.PathMoveTo(x=50, y=50),\n        ap.PathVertical(y=50, relative=True),\n    ],\n    line_color=ap.Color("#0af"),\n    line_thickness=5,\n)\n\nap.save_overall_html(dest_dir_path="path_vertical_relative/")\n```',  # noqa
    ##################################################
    "## PathVertical class constructor API": "## PathVertical クラスのコンストラクタのAPI",
    ##################################################
    '<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>': '<span class="inconspicuous-txt">特記事項: このAPIドキュメントはドキュメントビルド用のスクリプトによって自動で生成・同期されています。そのためもしかしたらこの節の内容は前節までの内容と重複している場合があります。</span>',  # noqa
    ##################################################
    "**[Interface summary]**": "**[インターフェイス概要]**",
    ##################################################
    "Path data class for the SVG `vertical line' (V).<hr>": "SVGの垂直方向への線（V）の描画のためのパスデータのクラスです。<hr>",  # noqa
    ##################################################
    "**[Parameters]**": "**[引数]**",
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
    '```py\n>>> import apysc as ap\n>>> stage: ap.Stage = ap.Stage()\n>>> sprite: ap.Sprite = ap.Sprite()\n>>> sprite.graphics.line_style(color=ap.Color("#fff"), thickness=3)\n>>> path: ap.Path = sprite.graphics.draw_path(\n...     path_data_list=[\n...         ap.PathMoveTo(x=0, y=50),\n...         ap.PathVertical(y=100),\n...     ]\n... )\n```': '```py\n>>> import apysc as ap\n>>> stage: ap.Stage = ap.Stage()\n>>> sprite: ap.Sprite = ap.Sprite()\n>>> sprite.graphics.line_style(color=ap.Color("#fff"), thickness=3)\n>>> path: ap.Path = sprite.graphics.draw_path(\n...     path_data_list=[\n...         ap.PathMoveTo(x=0, y=50),\n...         ap.PathVertical(y=100),\n...     ]\n... )\n```',  # noqa
    ##################################################
    "<hr>": "<hr>",
    ##################################################
    "**[References]**": "**[関連資料]**",
    ##################################################
    "- [Path class](https://simon-ritchie.github.io/apysc/en/path.html)": "- [Path クラス](https://simon-ritchie.github.io/apysc/jp/jp_path.html)",  # noqa
    ##################################################
    "- [Graphics draw_path interface](https://simon-ritchie.github.io/apysc/en/graphics_draw_path.html)": "- [Graphics クラスの draw_path インターフェイス](https://simon-ritchie.github.io/apysc/jp/jp_graphics_draw_path.html)",  # noqa
}
