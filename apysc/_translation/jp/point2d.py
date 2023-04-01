"""This module is for the translation mapping data of the
following document:

Document file: point2d.md
Language: jp
"""

from typing import Dict

MAPPING: Dict[str, str] = {
    ##################################################
    "# Point2D class": "# Point2D クラス",
    ##################################################
    "This page explains the `Point2D` class.": "このページでは`Point2D`クラスについて説明します。",
    ##################################################
    "## What is the Point2D class?": "## Point2D クラスの概要",
    ##################################################
    "The `Point2D` class is the 2D coordinates class interface. This interface handles the x-coordinate and y-coordinate. This interface is used, for example, the `Polygon` class drawing to specify each vertex point.": "`Point2D`クラスは2次元の座標値を扱うためのインターフェイスのクラスで、X座標とY座標を扱います。このクラスは`Polygon`クラスなどの一部のクラスで使用され、各頂点座標の設定用に参照されます。",  # noqa
    ##################################################
    "## Basic usage": "## 基本的な使い方",
    ##################################################
    "The `Point2D` class constructor requires the `x` and `y` arguments. Both parameters type is the Python built-in `int` or `Int`\\.": "`Point2D`クラスのコンストラクタでは`x`と`y`の各引数が必要になります。各引数はPythonのビルトインの`int`の値かもしくはapyscの`Int`の値を受け付けます。",  # noqa
    ##################################################
    "```py\n# runnable\nimport apysc as ap\n\npoint_1: ap.Point2D = ap.Point2D(x=10, y=20)\n\nx: ap.Int = ap.Int(10)\ny: ap.Int = ap.Int(20)\npoint_2: ap.Point2D = ap.Point2D(x=x, y=y)\n```": "```py\n# runnable\nimport apysc as ap\n\npoint_1: ap.Point2D = ap.Point2D(x=10, y=20)\n\nx: ap.Int = ap.Int(10)\ny: ap.Int = ap.Int(20)\npoint_2: ap.Point2D = ap.Point2D(x=x, y=y)\n```",  # noqa
    ##################################################
    "## X and y getter interfaces": "## XとY座標のgetterのインターフェイス",
    ##################################################
    "The `Point2D` class `x` and `y` property interfaces returns the `Int` type value, as follows:": "`Point2D`クラスの`x`と`y`の属性は以下のコード例のように`Int`型の値を返却します:",  # noqa
    ##################################################
    "```py\n# runnable\nimport apysc as ap\n\npoint: ap.Point2D = ap.Point2D(x=10, y=20)\nassert point.x == 10\nassert point.y == 20\n```": "```py\n# runnable\nimport apysc as ap\n\npoint: ap.Point2D = ap.Point2D(x=10, y=20)\nassert point.x == 10\nassert point.y == 20\n```",  # noqa
    ##################################################
    "## X and y setter interfaces": "## XとY座標のsetterのインターフェイス",
    ##################################################
    "The `x` and `y` property can be updated with an `Int` type value, as follows:": "`x`と`y`属性は以下のコード例のように`Int`型の値を使って値を更新することができます:",  # noqa
    ##################################################
    "```py\n# runnable\nimport apysc as ap\n\npoint: ap.Point2D = ap.Point2D(x=10, y=20)\npoint.x = ap.Number(30)\nassert point.x == 30\n```": "```py\n# runnable\nimport apysc as ap\n\npoint: ap.Point2D = ap.Point2D(x=10, y=20)\npoint.x = ap.Number(30)\nassert point.x == 30\n```",  # noqa
    ##################################################
    "## Usage example of the draw_polygon interface": "## draw_polygon インターフェイスにおける使用例",  # noqa
    ##################################################
    "The `draw_polygon` interface requires the `Point2D` list argument so that this section shows the example of the `Point2D` class with that drawing interface.": "`draw_polygon`インターフェイスは`Point2D`の値のリストの引数を必要とします。そのためこの節ではその描画のインターフェイスによる`Point2D`クラスを使ったコード例を載せています。",  # noqa
    ##################################################
    "The following draws the triangle vector graphics by specifying the three points:": "以下のコード例では3点の座標を指定することによって三角形のベクターグラフィックスを描画しています。",  # noqa
    ##################################################
    '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    stage_width=150, stage_height=150, background_color="#333", stage_elem_id="stage"\n)\nsprite: ap.Sprite = ap.Sprite()\nsprite.graphics.begin_fill(color="#0af")\n\nsprite.graphics.draw_polygon(\n    points=[\n        ap.Point2D(x=75, y=50),\n        ap.Point2D(x=50, y=100),\n        ap.Point2D(x=100, y=100),\n    ]\n)\n\nap.save_overall_html(dest_dir_path="point2d_basic_usage/")\n```': '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    stage_width=150, stage_height=150, background_color="#333", stage_elem_id="stage"\n)\nsprite: ap.Sprite = ap.Sprite()\nsprite.graphics.begin_fill(color="#0af")\n\nsprite.graphics.draw_polygon(\n    points=[\n        ap.Point2D(x=75, y=50),\n        ap.Point2D(x=50, y=100),\n        ap.Point2D(x=100, y=100),\n    ]\n)\n\nap.save_overall_html(dest_dir_path="point2d_basic_usage/")\n```',  # noqa
    ##################################################
    "## Point2D class constructor API": "## Point2D クラスのコンストラクタのAPI",
    ##################################################
    '<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>': '<span class="inconspicuous-txt">特記事項: このAPIドキュメントはドキュメントビルド用のスクリプトによって自動で生成・同期されています。そのためもしかしたらこの節の内容は前節までの内容と重複している場合があります。</span>',  # noqa
    ##################################################
    "**[Interface summary]**": "**[インターフェイス概要]**",
    ##################################################
    "2-dimensional geometry point.<hr>": "2次元の座標値を扱うクラスです。<hr>",
    ##################################################
    "**[Parameters]**": "**[引数]**",
    ##################################################
    "- `x`: Union[float, Number]": "- `x`: Union[float, Number]",
    ##################################################
    "  - X-coordinate.": "  - X座標。",
    ##################################################
    "- `y`: Union[float, Number]": "- `y`: Union[float, Number]",
    ##################################################
    "  - Y-coordinate.": "  - Y座標。",
    ##################################################
    "- `variable_name_suffix`: str, default ''": "- `variable_name_suffix`: str, default ''",  # noqa
    ##################################################
    "  - A JavaScript variable name suffix string. This setting is sometimes useful for JavaScript debugging.": "  - JavaScript上の変数のサフィックスの設定です。この設定はJavaScriptのデバッグ時に役立つことがあります。",  # noqa
    ##################################################
    "<hr>": "<hr>",
    ##################################################
    "**[Examples]**": "**[コードサンプル]**",
    ##################################################
    '```py\n>>> import apysc as ap\n>>> stage: ap.Stage = ap.Stage()\n>>> sprite: ap.Sprite = ap.Sprite()\n>>> sprite.graphics.begin_fill(color="#0af")\n>>> polygon: ap.Polygon = sprite.graphics.draw_polygon(\n...     points=[\n...         ap.Point2D(x=0, y=0),\n...         ap.Point2D(x=0, y=50),\n...         ap.Point2D(x=50, y=25),\n...     ]\n... )\n```': '```py\n>>> import apysc as ap\n>>> stage: ap.Stage = ap.Stage()\n>>> sprite: ap.Sprite = ap.Sprite()\n>>> sprite.graphics.begin_fill(color="#0af")\n>>> polygon: ap.Polygon = sprite.graphics.draw_polygon(\n...     points=[\n...         ap.Point2D(x=0, y=0),\n...         ap.Point2D(x=0, y=50),\n...         ap.Point2D(x=50, y=25),\n...     ]\n... )\n```',  # noqa
    ##################################################
    "## x property API": "## x属性のAPI",
    ##################################################
    '<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>': '<span class="inconspicuous-txt">特記事項: このAPIドキュメントはドキュメントビルド用のスクリプトによって自動で生成・同期されています。そのためもしかしたらこの節の内容は前節までの内容と重複している場合があります。</span>',  # noqa
    ##################################################
    "**[Interface summary]**": "**[インターフェイス概要]**",
    ##################################################
    "X-coordinate property.<hr>": "X座標の属性のインターフェイスです。<hr>",
    ##################################################
    "**[Returns]**": "**[返却値]**",
    ##################################################
    "- `x`: Number": "- `x`: Number",
    ##################################################
    "  - X-coordinate.": "  - X座標。",
    ##################################################
    "<hr>": "<hr>",
    ##################################################
    "**[Examples]**": "**[コードサンプル]**",
    ##################################################
    "```py\n>>> import apysc as ap\n>>> point: ap.Point2D = ap.Point2D(x=50, y=100)\n>>> point.x = ap.Number(150)\n>>> point.x\nNumber(150.0)\n```": "```py\n>>> import apysc as ap\n>>> point: ap.Point2D = ap.Point2D(x=50, y=100)\n>>> point.x = ap.Number(150)\n>>> point.x\nNumber(150.0)\n```",  # noqa
    ##################################################
    "## y property API": "## y属性のAPI",
    ##################################################
    '<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>': '<span class="inconspicuous-txt">特記事項: このAPIドキュメントはドキュメントビルド用のスクリプトによって自動で生成・同期されています。そのためもしかしたらこの節の内容は前節までの内容と重複している場合があります。</span>',  # noqa
    ##################################################
    "**[Interface summary]**": "**[インターフェイス概要]**",
    ##################################################
    "Y-coordinate property.<hr>": "Y座標の属性のインターフェイスです。<hr>",
    ##################################################
    "**[Returns]**": "**[返却値]**",
    ##################################################
    "- `y`: Number": "- `y`: Number",
    ##################################################
    "  - Y-coordinate.": "  - Y座標。",
    ##################################################
    "<hr>": "<hr>",
    ##################################################
    "**[Examples]**": "**[コードサンプル]**",
    ##################################################
    "```py\n>>> import apysc as ap\n>>> point: ap.Point2D = ap.Point2D(x=50, y=100)\n>>> point.y = ap.Number(150)\n>>> point.y\nNumber(150.0)\n```": "```py\n>>> import apysc as ap\n>>> point: ap.Point2D = ap.Point2D(x=50, y=100)\n>>> point.y = ap.Number(150)\n>>> point.y\nNumber(150.0)\n```",  # noqa
}
