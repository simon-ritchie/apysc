"""This module is for the translation mapping data of the
following document:

Document file: graphics_base_rotation_around_point.md
Language: jp
"""

from typing import Dict

MAPPING: Dict[str, str] = {
    ##################################################
    "# GraphicsBase rotation_around_point interfaces": "# GraphicsBase クラスの rotation_around_point インターフェイス",  # noqa
    ##################################################
    "This page explains the `GraphicsBase` class (base class of each graphic, such as the `Rectangle`) `get_rotation_around_point` and `set_rotation_around_point` method interfaces.": "このページでは`GraphicsBase`クラス（`Rectangle`などの各グラフィックスクラスの基底クラス）の`get_rotation_around_point`と`set_rotation_around_point`の各メソッドのインターフェイスについて説明します。",  # noqa
    ##################################################
    "## What interfaces are these?": "## 各インターフェイスの概要",
    ##################################################
    "The `get_rotation_around_point` method will return a rotation value around the given coordinates, and the `set_rotation_around_point` method will update a rotation value around the given coordinates.": "`get_rotation_around_point`メソッドは指定された座標基準の回転量を取得し、`set_rotation_around_point`メソッドは指定された座標を基準とした回転量を更新します。",  # noqa
    ##################################################
    "These rotation values are relative, and each point has the rotation value. For example, the coordinates of the `(x=50, y=50)` and the other coordinates of the `(x=100, y=100)` have different rotation values.": "これらの回転量は相対値であり、各回転量は座標ごとに異なる値が保持されます。例えばx=50, y=50の座標とx=100, y=100の座標の回転量の値はそれぞれ別の値になります。",  # noqa
    ##################################################
    "## Basic usage": "## 基本的な使い方",
    ##################################################
    "The `get_rotation_around_point` method requires the `x` and `y` arguments and return a rotation value around the given coordinates. The `set_rotation_around_point` requires `x`, `y` and `rotation` arguments. All the arguments and return value are `Int` type.": "`get_rotation_around_point`メソッドは`x`と`y`の引数の指定を必要とし、指定された座標での回転量を返却します。`set_rotation_around_point`メソッドは`x`と`y`、そして`rotation`の引数の指定を必要とします。全ての引数と返却値は`Int`型になります。",  # noqa
    ##################################################
    "The following example creates the two rectangles and rotates each rectangle in the timer handler. The first rectangle rotates around the top-left coordinates (`x=50, y=50`). Also, the second one rotates around the bottom-right coordinates (`x=100, y=100`).": "以下の例では二つの四角を作成し、各四角をタイマーのハンドラ内で回転させています。1つ目の四角は左上の座標（`x=50, y=50`）で回転させていて、2つ目の四角は右下の座標（`x=100, y=100`）で回転させています。",  # noqa
    ##################################################
    '```py\n# runnable\nfrom typing_extensions import TypedDict\n\nimport apysc as ap\n\n\nclass _RectanglesOptions(TypedDict):\n    rectangle_1: ap.Rectangle\n    rectangle_2: ap.Rectangle\n\n\ndef on_timer(e: ap.TimerEvent, options: _RectanglesOptions) -> None:\n    """\n    The handler that the timer calls.\n\n    Parameters\n    ----------\n    e : ap.TimerEvent\n        Event instance.\n    options : dict\n        Optional arguments dictionary.\n    """\n    x: ap.Int = ap.Int(50)\n    y: ap.Int = ap.Int(50)\n    rectangle_1: ap.Rectangle = options["rectangle_1"]\n    rotation: ap.Int = rectangle_1.get_rotation_around_point(x=x, y=y)\n    rotation += 1\n    rectangle_1.set_rotation_around_point(rotation=rotation, x=x, y=y)\n\n    rectangle_2: ap.Rectangle = options["rectangle_2"]\n    x = ap.Int(100)\n    y = ap.Int(100)\n    rotation = rectangle_2.get_rotation_around_point(x=x, y=y)\n    rotation += 1\n    rectangle_2.set_rotation_around_point(rotation=rotation, x=x, y=y)\n\n\nap.Stage(\n    stage_width=150,\n    stage_height=150,\n    background_color=ap.Color("#333"),\n    stage_elem_id="stage",\n)\nsprite: ap.Sprite = ap.Sprite()\nsprite.graphics.begin_fill(color=ap.Color("#0af"), alpha=0.5)\n\nrectangle_1: ap.Rectangle = sprite.graphics.draw_rect(x=50, y=50, width=50, height=50)\nrectangle_2: ap.Rectangle = sprite.graphics.draw_rect(x=50, y=50, width=50, height=50)\n\noptions: _RectanglesOptions = {"rectangle_1": rectangle_1, "rectangle_2": rectangle_2}\ntimer: ap.Timer = ap.Timer(on_timer, delay=ap.FPS.FPS_60, options=options)\ntimer.start()\n\nap.save_overall_html(dest_dir_path="graphics_base_rotation_around_point_basic_usage/")\n```': '```py\n# runnable\nfrom typing_extensions import TypedDict\n\nimport apysc as ap\n\n\nclass _RectanglesOptions(TypedDict):\n    rectangle_1: ap.Rectangle\n    rectangle_2: ap.Rectangle\n\n\ndef on_timer(e: ap.TimerEvent, options: _RectanglesOptions) -> None:\n    """\n    The handler that the timer calls.\n\n    Parameters\n    ----------\n    e : ap.TimerEvent\n        Event instance.\n    options : dict\n        Optional arguments dictionary.\n    """\n    x: ap.Int = ap.Int(50)\n    y: ap.Int = ap.Int(50)\n    rectangle_1: ap.Rectangle = options["rectangle_1"]\n    rotation: ap.Int = rectangle_1.get_rotation_around_point(x=x, y=y)\n    rotation += 1\n    rectangle_1.set_rotation_around_point(rotation=rotation, x=x, y=y)\n\n    rectangle_2: ap.Rectangle = options["rectangle_2"]\n    x = ap.Int(100)\n    y = ap.Int(100)\n    rotation = rectangle_2.get_rotation_around_point(x=x, y=y)\n    rotation += 1\n    rectangle_2.set_rotation_around_point(rotation=rotation, x=x, y=y)\n\n\nap.Stage(\n    stage_width=150,\n    stage_height=150,\n    background_color=ap.Color("#333"),\n    stage_elem_id="stage",\n)\nsprite: ap.Sprite = ap.Sprite()\nsprite.graphics.begin_fill(color=ap.Color("#0af"), alpha=0.5)\n\nrectangle_1: ap.Rectangle = sprite.graphics.draw_rect(x=50, y=50, width=50, height=50)\nrectangle_2: ap.Rectangle = sprite.graphics.draw_rect(x=50, y=50, width=50, height=50)\n\noptions: _RectanglesOptions = {"rectangle_1": rectangle_1, "rectangle_2": rectangle_2}\ntimer: ap.Timer = ap.Timer(on_timer, delay=ap.FPS.FPS_60, options=options)\ntimer.start()\n\nap.save_overall_html(dest_dir_path="graphics_base_rotation_around_point_basic_usage/")\n```',  # noqa
    ##################################################
    "## get_rotation_around_point API": "## get_rotation_around_point API",
    ##################################################
    '<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>': '<span class="inconspicuous-txt">特記事項: このAPIドキュメントはドキュメントビルド用のスクリプトによって自動で生成・同期されています。そのためもしかしたらこの節の内容は前節までの内容と重複している場合があります。</span>',  # noqa
    ##################################################
    "**[Interface summary]**": "**[インターフェイス概要]**",
    ##################################################
    "Get a rotation value around the given coordinates.<hr>": "指定された座標を基準とした回転量を取得します。<hr>",  # noqa
    ##################################################
    "**[Parameters]**": "**[引数]**",
    ##################################################
    "- `x`: Number": "- `x`: Number",
    ##################################################
    "  - X-coordinate.": "  - X座標。",
    ##################################################
    "- `y`: Number": "- `y`: Number",
    ##################################################
    "  - Y-coordinate.": "  - Y座標。",
    ##################################################
    "<hr>": "<hr>",
    ##################################################
    "**[Returns]**": "**[返却値]**",
    ##################################################
    "- `rotation`: Int": "- `rotation`: Int",
    ##################################################
    "  - Rotation value around the given coordinates.": "  - 指定された座標基準による回転量。",
    ##################################################
    "<hr>": "<hr>",
    ##################################################
    "**[Examples]**": "**[コードサンプル]**",
    ##################################################
    '```py\n>>> import apysc as ap\n>>> stage: ap.Stage = ap.Stage()\n>>> sprite: ap.Sprite = ap.Sprite()\n>>> sprite.graphics.begin_fill(color=ap.Color("#0af"))\n>>> rectangle: ap.Rectangle = sprite.graphics.draw_rect(\n...     x=50, y=50, width=50, height=50\n... )\n>>> x: ap.Number = ap.Number(100)\n>>> y: ap.Number = ap.Number(100)\n>>> rectangle.set_rotation_around_point(rotation=ap.Int(45), x=x, y=y)\n>>> rectangle.get_rotation_around_point(x=x, y=y)\nInt(45)\n```': '```py\n>>> import apysc as ap\n>>> stage: ap.Stage = ap.Stage()\n>>> sprite: ap.Sprite = ap.Sprite()\n>>> sprite.graphics.begin_fill(color=ap.Color("#0af"))\n>>> rectangle: ap.Rectangle = sprite.graphics.draw_rect(\n...     x=50, y=50, width=50, height=50\n... )\n>>> x: ap.Number = ap.Number(100)\n>>> y: ap.Number = ap.Number(100)\n>>> rectangle.set_rotation_around_point(rotation=ap.Int(45), x=x, y=y)\n>>> rectangle.get_rotation_around_point(x=x, y=y)\nInt(45)\n```',  # noqa
    ##################################################
    "## set_rotation_around_point API": "## set_rotation_around_point API",
    ##################################################
    '<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>': '<span class="inconspicuous-txt">特記事項: このAPIドキュメントはドキュメントビルド用のスクリプトによって自動で生成・同期されています。そのためもしかしたらこの節の内容は前節までの内容と重複している場合があります。</span>',  # noqa
    ##################################################
    "**[Interface summary]**": "**[インターフェイス概要]**",
    ##################################################
    "Update a rotation value around the given coordinates.<hr>": "指定された座標基準の回転量を更新します。<hr>",  # noqa
    ##################################################
    "**[Parameters]**": "**[引数]**",
    ##################################################
    "- `rotation`: Int": "- `rotation`: Int",
    ##################################################
    "  - Rotation value to set.": "  - 設定する回転量。",
    ##################################################
    "- `x`: Number": "- `x`: Number",
    ##################################################
    "  - X-coordinate.": "  - X座標。",
    ##################################################
    "- `y`: Number": "- `y`: Number",
    ##################################################
    "  - Y-coordinate.": "  - Y座標。",
}
