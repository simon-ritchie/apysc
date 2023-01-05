"""This module is for the translation mapping data of the
following document:

Document file: graphics_base_scale_from_point.md
Language: jp
"""

from typing import Dict

MAPPING: Dict[str, str] = {
    ##################################################
    "# GraphicsBase get_scale_from_point and set_scale_from_point interfaces": "# GraphicsBase クラスの get_scale_from_point と set_scale_from_point のインターフェイス",  # noqa
    ##################################################
    "This page explains the `GraphicsBase` class (base class of each graphic, such as the `Rectangle`) `get_scale_x_from_point`, `get_scale_y_from_point`, `set_scale_x_from_point`, and `set_scale_y_from_point` method interfaces.": "このページでは`GraphicsBase`クラス（`Rectangle`などのグラフィッククラスの基底クラス）の`get_scale_x_from_point`、`get_scale_y_from_point`、`set_scale_x_from_point`、`set_scale_y_from_point`メソッドの各インターフェイスについて説明します。",  # noqa
    ##################################################
    "## What interfaces are these?": "## 各インターフェイスの概要",
    ##################################################
    "The `set_scale_x_from_point` method changes the object's horizontal scale from a given x-coordinate. Similarly, the `set_scale_y_from_point` method changes the object's vertical scale from a given y-coordinate.": "`set_scale_x_from_point`メソッドは指定された座標を基準にオブジェクトの水平方向の拡縮を変更します。同様に`set_scale_y_from_point`メソッドは指定された座標を基準にオブジェクトの垂直方向の拡縮を変更します。",  # noqa
    ##################################################
    "The `scale_x_from_center` and `scale_y_from_center` interfaces are property, but the `set_scale_x_from_point` and `set_scale_y_from_point` interfaces are methods since these interfaces require a coodinate argument.": "`scale_x_from_center`や`scale_y_from_center`のインターフェイスは属性になっていますが、`set_scale_x_from_point`や`set_scale_y_from_point`のインターフェイスは座標の指定が必要なためメソッドのインターフェイスになっています。",  # noqa
    ##################################################
    "Similarly, the `get_scale_x_from_point` and `get_scale_y_from_point` methods will return the current scale from a given point. These interfaces also require a coordinate argument.": "同様に`get_scale_x_from_point`と`get_scale_y_from_point`のメソッドは指定された座標における拡縮値を返却します。これらのインターフェイスも引数に座標の指定が必要になります。",  # noqa
    ##################################################
    "Return value is set for each coordinate. For example, if you set the scale-x value at the 50px x-coordinate, 100px x-coordinate scale will not be affected.": "返却値は各座標ごとに設定されます。例えば水平方向の拡縮を50pxのX座標の位置で設定した場合、100pxのX座標の位置における拡縮値には影響しません。",  # noqa
    ##################################################
    "## Basic usage": "## 基本的な使い方",
    ##################################################
    "The `get_scale_x_from_point` method requires the `x` argument (`Int` value), and the `set_scale_x_from_point` requires the `scale_x` (`Number` value) and `x` arguments.": "`get_scale_x_from_point`メソッドは`Int`型の`x`引数の指定を必要とし、`set_scale_x_from_point`メソッドは`Number`型の`scale_x`と`x`の各引く数の指定が必要になります。",  # noqa
    ##################################################
    "The following example creates three rectangles and increments (or decrements) for each rectangle scale-x value. The top rectangle scales from the left-x position. The middle one scales from the center-x. And the bottom one scales from the right-x.": "以下のコード例では3つの四角を生成し水平方向の拡縮を増減させています。上の四角は左端を基準に拡縮を、真ん中の四角は中央を基準に拡縮を、そして下の四角では右右端を基準に拡縮を行っています。",  # noqa
    ##################################################
    '```py\n# runnable\nfrom typing_extensions import TypedDict\n\nimport apysc as ap\n\n\nclass _Options(TypedDict):\n    rectangle: ap.Rectangle\n    x: ap.Int\n    direction: ap.Int\n\n\ndef on_timer(e: ap.TimerEvent, options: _Options) -> None:\n    """\n    The handler that the timer calls.\n\n    Parameters\n    ----------\n    e : ap.TimerEvent\n        Event instance.\n    options : dict\n        Optional arguments dictionary.\n    """\n    rectangle: ap.Rectangle = options["rectangle"]\n    x: ap.Int = options["x"]\n    direction: ap.Int = options["direction"]\n    current_scale_x: ap.Number = rectangle.get_scale_x_from_point(x=x)\n    current_scale_x += direction * 0.03\n    rectangle.set_scale_x_from_point(scale_x=current_scale_x, x=x)\n    with ap.If(current_scale_x >= 2.0):\n        direction *= -1\n    with ap.If(current_scale_x <= 0.0):\n        direction *= -1\n\n\nap.Stage(\n    stage_width=150, stage_height=350, background_color="#333", stage_elem_id="stage"\n)\nsprite: ap.Sprite = ap.Sprite()\nsprite.graphics.begin_fill(color="#0af")\n\ntop_rect: ap.Rectangle = sprite.graphics.draw_rect(x=50, y=50, width=50, height=50)\nmiddle_rect: ap.Rectangle = sprite.graphics.draw_rect(x=50, y=150, width=50, height=50)\nbottom_rect: ap.Rectangle = sprite.graphics.draw_rect(x=50, y=250, width=50, height=50)\n\ntop_rect_direction: ap.Int = ap.Int(1)\noptions: _Options = {\n    "rectangle": top_rect,\n    "x": ap.Int(50),\n    "direction": top_rect_direction,\n}\ntop_rect_timer: ap.Timer = ap.Timer(on_timer, delay=ap.FPS.FPS_60, options=options)\ntop_rect_timer.start()\n\nmiddle_rect_direction: ap.Int = ap.Int(1)\noptions = {\n    "rectangle": middle_rect,\n    "x": ap.Int(75),\n    "direction": middle_rect_direction,\n}\nmiddle_rect_timer: ap.Timer = ap.Timer(on_timer, delay=ap.FPS.FPS_60, options=options)\nmiddle_rect_timer.start()\n\nbottom_rect_direction: ap.Int = ap.Int(1)\noptions = {\n    "rectangle": bottom_rect,\n    "x": ap.Int(100),\n    "direction": bottom_rect_direction,\n}\nbottom_rect_timer: ap.Timer = ap.Timer(on_timer, delay=ap.FPS.FPS_60, options=options)\nbottom_rect_timer.start()\n\nap.save_overall_html(dest_dir_path="graphics_base_scale_from_point_basic_usage_x/")\n```': '```py\n# runnable\nfrom typing_extensions import TypedDict\n\nimport apysc as ap\n\n\nclass _Options(TypedDict):\n    rectangle: ap.Rectangle\n    x: ap.Int\n    direction: ap.Int\n\n\ndef on_timer(e: ap.TimerEvent, options: _Options) -> None:\n    """\n    The handler that the timer calls.\n\n    Parameters\n    ----------\n    e : ap.TimerEvent\n        Event instance.\n    options : dict\n        Optional arguments dictionary.\n    """\n    rectangle: ap.Rectangle = options["rectangle"]\n    x: ap.Int = options["x"]\n    direction: ap.Int = options["direction"]\n    current_scale_x: ap.Number = rectangle.get_scale_x_from_point(x=x)\n    current_scale_x += direction * 0.03\n    rectangle.set_scale_x_from_point(scale_x=current_scale_x, x=x)\n    with ap.If(current_scale_x >= 2.0):\n        direction *= -1\n    with ap.If(current_scale_x <= 0.0):\n        direction *= -1\n\n\nap.Stage(\n    stage_width=150, stage_height=350, background_color="#333", stage_elem_id="stage"\n)\nsprite: ap.Sprite = ap.Sprite()\nsprite.graphics.begin_fill(color="#0af")\n\ntop_rect: ap.Rectangle = sprite.graphics.draw_rect(x=50, y=50, width=50, height=50)\nmiddle_rect: ap.Rectangle = sprite.graphics.draw_rect(x=50, y=150, width=50, height=50)\nbottom_rect: ap.Rectangle = sprite.graphics.draw_rect(x=50, y=250, width=50, height=50)\n\ntop_rect_direction: ap.Int = ap.Int(1)\noptions: _Options = {\n    "rectangle": top_rect,\n    "x": ap.Int(50),\n    "direction": top_rect_direction,\n}\ntop_rect_timer: ap.Timer = ap.Timer(on_timer, delay=ap.FPS.FPS_60, options=options)\ntop_rect_timer.start()\n\nmiddle_rect_direction: ap.Int = ap.Int(1)\noptions = {\n    "rectangle": middle_rect,\n    "x": ap.Int(75),\n    "direction": middle_rect_direction,\n}\nmiddle_rect_timer: ap.Timer = ap.Timer(on_timer, delay=ap.FPS.FPS_60, options=options)\nmiddle_rect_timer.start()\n\nbottom_rect_direction: ap.Int = ap.Int(1)\noptions = {\n    "rectangle": bottom_rect,\n    "x": ap.Int(100),\n    "direction": bottom_rect_direction,\n}\nbottom_rect_timer: ap.Timer = ap.Timer(on_timer, delay=ap.FPS.FPS_60, options=options)\nbottom_rect_timer.start()\n\nap.save_overall_html(dest_dir_path="graphics_base_scale_from_point_basic_usage_x/")\n```',  # noqa
    ##################################################
    "The `get_scale_y_from_point` and `set_scale_y_from_point` methods have the similar arguments, `scale_y` and `y`. These interfaces work the same way as the x-axis interfaces, except that the axis directions are different.": "似たような形で`get_scale_y_from_point`と`set_scale_y_from_point`のメソッドは`scale_y`と`y`の引数を必要とします。これらは拡縮の方向が垂直方向になっている以外は水平方向のインターフェイスと同じように動作します。",  # noqa
    ##################################################
    '```py\n# runnable\nfrom typing_extensions import TypedDict\n\nimport apysc as ap\n\n\nclass _Options(TypedDict):\n    rectangle: ap.Rectangle\n    y: ap.Int\n    direction: ap.Int\n\n\ndef on_timer(e: ap.TimerEvent, options: _Options) -> None:\n    """\n    The handler that the timer calls.\n\n    Parameters\n    ----------\n    e : ap.TimerEvent\n        Event instance.\n    options : dict\n        Optional arguments dictionary.\n    """\n    rectangle: ap.Rectangle = options["rectangle"]\n    y: ap.Int = options["y"]\n    direction: ap.Int = options["direction"]\n    current_scale_y: ap.Number = rectangle.get_scale_y_from_point(y=y)\n    current_scale_y += direction * 0.03\n    rectangle.set_scale_y_from_point(scale_y=current_scale_y, y=y)\n    with ap.If(current_scale_y >= 2.0):\n        direction *= -1\n    with ap.If(current_scale_y <= 0.0):\n        direction *= -1\n\n\nap.Stage(\n    stage_width=150, stage_height=150, background_color="#333", stage_elem_id="stage"\n)\nsprite: ap.Sprite = ap.Sprite()\nsprite.graphics.begin_fill(color="#0af")\n\nrectangle: ap.Rectangle = sprite.graphics.draw_rect(x=50, y=50, width=50, height=50)\ndirection: ap.Int = ap.Int(1)\noptions: _Options = {"rectangle": rectangle, "y": ap.Int(50), "direction": direction}\ntimer: ap.Timer = ap.Timer(on_timer, delay=ap.FPS.FPS_60, options=options)\ntimer.start()\n\nap.save_overall_html(dest_dir_path="graphics_base_scale_from_point_basic_usage_y/")\n```': '```py\n# runnable\nfrom typing_extensions import TypedDict\n\nimport apysc as ap\n\n\nclass _Options(TypedDict):\n    rectangle: ap.Rectangle\n    y: ap.Int\n    direction: ap.Int\n\n\ndef on_timer(e: ap.TimerEvent, options: _Options) -> None:\n    """\n    The handler that the timer calls.\n\n    Parameters\n    ----------\n    e : ap.TimerEvent\n        Event instance.\n    options : dict\n        Optional arguments dictionary.\n    """\n    rectangle: ap.Rectangle = options["rectangle"]\n    y: ap.Int = options["y"]\n    direction: ap.Int = options["direction"]\n    current_scale_y: ap.Number = rectangle.get_scale_y_from_point(y=y)\n    current_scale_y += direction * 0.03\n    rectangle.set_scale_y_from_point(scale_y=current_scale_y, y=y)\n    with ap.If(current_scale_y >= 2.0):\n        direction *= -1\n    with ap.If(current_scale_y <= 0.0):\n        direction *= -1\n\n\nap.Stage(\n    stage_width=150, stage_height=150, background_color="#333", stage_elem_id="stage"\n)\nsprite: ap.Sprite = ap.Sprite()\nsprite.graphics.begin_fill(color="#0af")\n\nrectangle: ap.Rectangle = sprite.graphics.draw_rect(x=50, y=50, width=50, height=50)\ndirection: ap.Int = ap.Int(1)\noptions: _Options = {"rectangle": rectangle, "y": ap.Int(50), "direction": direction}\ntimer: ap.Timer = ap.Timer(on_timer, delay=ap.FPS.FPS_60, options=options)\ntimer.start()\n\nap.save_overall_html(dest_dir_path="graphics_base_scale_from_point_basic_usage_y/")\n```',  # noqa
    ##################################################
    "## get_scale_x_from_point API": "## get_scale_x_from_point API",
    ##################################################
    '<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>': '<span class="inconspicuous-txt">特記事項: このAPIドキュメントはドキュメントビルド用のスクリプトによって自動で生成・同期されています。そのためもしかしたらこの節の内容は前節までの内容と重複している場合があります。</span>',  # noqa
    ##################################################
    "**[Interface summary]**": "**[インターフェイス概要]**",
    ##################################################
    "Get a scale-x value from the given x-coordinate.<hr>": "指定されたX座標を基準として水平方向の拡縮の値を取得します。<hr>",  # noqa
    ##################################################
    "**[Parameters]**": "**[引数]**",
    ##################################################
    "- `x`: Int": "- `x`: Int",
    ##################################################
    "  - X-coordinate.": "  - X座標。",
    ##################################################
    "<hr>": "<hr>",
    ##################################################
    "**[Returns]**": "**[返却値]**",
    ##################################################
    "- `scale_x`: Number": "- `scale_x`: Number",
    ##################################################
    "  - Scale-x value from the given x-coordinate.": "  - 指定されたX座標を基準とした水平方向の拡縮値。",
    ##################################################
    "<hr>": "<hr>",
    ##################################################
    "**[Notes]**": "**[特記事項]**",
    ##################################################
    "The scale's minimum value is almost zero, and it does not become negative.<hr>": "拡縮の最小値はほぼ0となり、その値は負の値にはなりません。<hr>",  # noqa
    ##################################################
    "**[Examples]**": "**[コードサンプル]**",
    ##################################################
    '```py\n>>> import apysc as ap\n>>> stage: ap.Stage = ap.Stage()\n>>> sprite: ap.Sprite = ap.Sprite()\n>>> sprite.graphics.begin_fill(color="#0af")\n>>> rectangle: ap.Rectangle = sprite.graphics.draw_rect(\n...     x=50, y=50, width=50, height=50\n... )\n>>> x: ap.Int = ap.Int(100)\n>>> rectangle.set_scale_x_from_point(scale_x=ap.Number(1.5), x=x)\n>>> rectangle.get_scale_x_from_point(x=x)\nNumber(1.5)\n```': '```py\n>>> import apysc as ap\n>>> stage: ap.Stage = ap.Stage()\n>>> sprite: ap.Sprite = ap.Sprite()\n>>> sprite.graphics.begin_fill(color="#0af")\n>>> rectangle: ap.Rectangle = sprite.graphics.draw_rect(\n...     x=50, y=50, width=50, height=50\n... )\n>>> x: ap.Int = ap.Int(100)\n>>> rectangle.set_scale_x_from_point(scale_x=ap.Number(1.5), x=x)\n>>> rectangle.get_scale_x_from_point(x=x)\nNumber(1.5)\n```',  # noqa
    ##################################################
    "## set_scale_x_from_point API": "## set_scale_x_from_point API",
    ##################################################
    '<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>': '<span class="inconspicuous-txt">特記事項: このAPIドキュメントはドキュメントビルド用のスクリプトによって自動で生成・同期されています。そのためもしかしたらこの節の内容は前節までの内容と重複している場合があります。</span>',  # noqa
    ##################################################
    "**[Interface summary]**": "**[インターフェイス概要]**",
    ##################################################
    "Update a scale-x value from the given x-coordinate.<hr>": "指定されたX座病を基準とした水平方向の拡縮値を更新します。<hr>",  # noqa
    ##################################################
    "**[Parameters]**": "**[引数]**",
    ##################################################
    "- `scale_x`: Number": "- `scale_x`: Number",
    ##################################################
    "  - Scale-x value to set.": "  - 設定する水平方向の拡縮値。",
    ##################################################
    "- `x`: Int": "- `x`: Int",
    ##################################################
    "  - X-coordinate.": "  - X座標。",
    ##################################################
    "<hr>": "<hr>",
    ##################################################
    "**[Notes]**": "**[特記事項]**",
    ##################################################
    "The scale's minimum value is almost zero, and it does not become negative.<hr>": "拡縮の最小値はほぼ0となり、その値は負の値にはなりません。<hr>",  # noqa
    ##################################################
    "**[Examples]**": "**[コードサンプル]**",
    ##################################################
    '```py\n>>> import apysc as ap\n>>> stage: ap.Stage = ap.Stage()\n>>> sprite: ap.Sprite = ap.Sprite()\n>>> sprite.graphics.begin_fill(color="#0af")\n>>> rectangle: ap.Rectangle = sprite.graphics.draw_rect(\n...     x=50, y=50, width=50, height=50\n... )\n>>> x: ap.Int = ap.Int(100)\n>>> rectangle.set_scale_x_from_point(scale_x=ap.Number(1.5), x=x)\n>>> rectangle.get_scale_x_from_point(x=x)\nNumber(1.5)\n```': '```py\n>>> import apysc as ap\n>>> stage: ap.Stage = ap.Stage()\n>>> sprite: ap.Sprite = ap.Sprite()\n>>> sprite.graphics.begin_fill(color="#0af")\n>>> rectangle: ap.Rectangle = sprite.graphics.draw_rect(\n...     x=50, y=50, width=50, height=50\n... )\n>>> x: ap.Int = ap.Int(100)\n>>> rectangle.set_scale_x_from_point(scale_x=ap.Number(1.5), x=x)\n>>> rectangle.get_scale_x_from_point(x=x)\nNumber(1.5)\n```',  # noqa
    ##################################################
    "## get_scale_y_from_point API": "## get_scale_y_from_point API",
    ##################################################
    '<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>': '<span class="inconspicuous-txt">特記事項: このAPIドキュメントはドキュメントビルド用のスクリプトによって自動で生成・同期されています。そのためもしかしたらこの節の内容は前節までの内容と重複している場合があります。</span>',  # noqa
    ##################################################
    "**[Interface summary]**": "**[インターフェイス概要]**",
    ##################################################
    "Get a scale-y value from the given y-coordinate.<hr>": "指定されたY座標を基準とした垂直方向の拡縮の値を取得します。<hr>",  # noqa
    ##################################################
    "**[Parameters]**": "**[引数]**",
    ##################################################
    "- `y`: Int": "- `y`: Int",
    ##################################################
    "  - Y-coordinate.": "  - Y座標。",
    ##################################################
    "<hr>": "<hr>",
    ##################################################
    "**[Returns]**": "**[返却値]**",
    ##################################################
    "- `scale_y`: ap.Number": "- `scale_y`: ap.Number",
    ##################################################
    "  - Scale-y value from the given y-coordinate.": "  - 指定されたY座標を基準とした垂直方向の拡縮値。",
    ##################################################
    "<hr>": "<hr>",
    ##################################################
    "**[Examples]**": "**[コードサンプル]**",
    ##################################################
    '```py\n>>> import apysc as ap\n>>> stage: ap.Stage = ap.Stage()\n>>> sprite: ap.Sprite = ap.Sprite()\n>>> sprite.graphics.begin_fill(color="#0af")\n>>> rectangle: ap.Rectangle = sprite.graphics.draw_rect(\n...     x=50, y=50, width=50, height=50\n... )\n>>> y: ap.Int = ap.Int(100)\n>>> rectangle.set_scale_y_from_point(scale_y=ap.Number(1.5), y=y)\n>>> rectangle.get_scale_y_from_point(y=y)\nNumber(1.5)\n```': '```py\n>>> import apysc as ap\n>>> stage: ap.Stage = ap.Stage()\n>>> sprite: ap.Sprite = ap.Sprite()\n>>> sprite.graphics.begin_fill(color="#0af")\n>>> rectangle: ap.Rectangle = sprite.graphics.draw_rect(\n...     x=50, y=50, width=50, height=50\n... )\n>>> y: ap.Int = ap.Int(100)\n>>> rectangle.set_scale_y_from_point(scale_y=ap.Number(1.5), y=y)\n>>> rectangle.get_scale_y_from_point(y=y)\nNumber(1.5)\n```',  # noqa
    ##################################################
    "## set_scale_y_from_point API": "## set_scale_y_from_point API",
    ##################################################
    '<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>': '<span class="inconspicuous-txt">特記事項: このAPIドキュメントはドキュメントビルド用のスクリプトによって自動で生成・同期されています。そのためもしかしたらこの節の内容は前節までの内容と重複している場合があります。</span>',  # noqa
    ##################################################
    "**[Interface summary]**": "**[インターフェイス概要]**",
    ##################################################
    "Update a scale-y value from the given y-coordinate.<hr>": "指定されたY座標を基準とした垂直方向の拡縮値を更新します。<hr>",  # noqa
    ##################################################
    "**[Parameters]**": "**[引数]**",
    ##################################################
    "- `scale_y`: Number": "- `scale_y`: Number",
    ##################################################
    "  - Scale-y value to set.": "  - 設定すの垂直方向の拡縮値。",
    ##################################################
    "- `y`: Int": "- `y`: Int",
    ##################################################
    "  - Y-coordinate.": "  - Y座標。",
    ##################################################
    "<hr>": "<hr>",
    ##################################################
    "**[Examples]**": "**[コードサンプル]**",
    ##################################################
    '```py\n>>> import apysc as ap\n>>> stage: ap.Stage = ap.Stage()\n>>> sprite: ap.Sprite = ap.Sprite()\n>>> sprite.graphics.begin_fill(color="#0af")\n>>> rectangle: ap.Rectangle = sprite.graphics.draw_rect(\n...     x=50, y=50, width=50, height=50\n... )\n>>> y: ap.Int = ap.Int(100)\n>>> rectangle.set_scale_y_from_point(scale_y=ap.Number(1.5), y=y)\n>>> rectangle.get_scale_y_from_point(y=y)\nNumber(1.5)\n```': '```py\n>>> import apysc as ap\n>>> stage: ap.Stage = ap.Stage()\n>>> sprite: ap.Sprite = ap.Sprite()\n>>> sprite.graphics.begin_fill(color="#0af")\n>>> rectangle: ap.Rectangle = sprite.graphics.draw_rect(\n...     x=50, y=50, width=50, height=50\n... )\n>>> y: ap.Int = ap.Int(100)\n>>> rectangle.set_scale_y_from_point(scale_y=ap.Number(1.5), y=y)\n>>> rectangle.get_scale_y_from_point(y=y)\nNumber(1.5)\n```',  # noqa
}
