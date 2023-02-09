"""This module is for the translation mapping data of the
following document:

Document file: graphics_base_skew.md
Language: jp
"""

from typing import Dict

MAPPING: Dict[str, str] = {
    ##################################################
    "# GraphicsBase skew_x and skew_y interfaces": "# GraphicsBase クラスの skew_x と skew_y インターフェイス",  # noqa
    ##################################################
    "This page explains the `GraphicsBase` class (base class of each graphic, such as the `Rectangle`) `skew_x` and `skew_y` property interfaces.": "このページでは`GraphicsBase`クラス（`Rectangle`などのグラフィッククラスの基底クラス）の`skew_x`と`skew_y`属性のインターフェイスについて説明します。",  # noqa
    ##################################################
    "## What interfaces are these?": "## 各インターフェイスの概要",
    ##################################################
    "The `skew_x` property skews an object's x-axis. Conversely, the `skew_y` property skew a y-axis. These interfaces have getter and setter interfaces.": "`skew_x`属性はオブジェクトをX軸方向に歪ませます。逆に`skew_y`属性ではY軸方向にオブジェクトを歪ませます。これらのインターフェイスはgetterとsetterの各インターフェイスを持っています。",  # noqa
    ##################################################
    "Each interface value type is the `Int` value.": "各インターフェイスの値の型は`Int`型の値となります。",
    ##################################################
    "The following example shows you the default rectangle (left) and the skewed 50px in the x-direction rectangle (right).": "以下のコード例では左側の四角はデフォルトの状態、右側の四角はX軸方向に50pxの歪みを設定しています。",  # noqa
    ##################################################
    '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    stage_width=250, stage_height=150, background_color="#333", stage_elem_id="stage"\n)\nsprite: ap.Sprite = ap.Sprite()\nsprite.graphics.begin_fill(color="#0af")\n\nleft_rectangle: ap.Rectangle = sprite.graphics.draw_rect(\n    x=50, y=50, width=50, height=50\n)\nright_rectangle: ap.Rectangle = sprite.graphics.draw_rect(\n    x=150, y=50, width=50, height=50\n)\nright_rectangle.skew_x = ap.Int(50)\n\nap.save_overall_html(dest_dir_path="graphics_base_skew_x_basic_usage/")\n```': '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    stage_width=250, stage_height=150, background_color="#333", stage_elem_id="stage"\n)\nsprite: ap.Sprite = ap.Sprite()\nsprite.graphics.begin_fill(color="#0af")\n\nleft_rectangle: ap.Rectangle = sprite.graphics.draw_rect(\n    x=50, y=50, width=50, height=50\n)\nright_rectangle: ap.Rectangle = sprite.graphics.draw_rect(\n    x=150, y=50, width=50, height=50\n)\nright_rectangle.skew_x = ap.Int(50)\n\nap.save_overall_html(dest_dir_path="graphics_base_skew_x_basic_usage/")\n```',  # noqa
    ##################################################
    "The following example skews the rectangle in the y-direction incrementally.": "以下の例ではY軸方向に四角の歪みを加算していく形で設定しています。",  # noqa
    ##################################################
    '```py\n# runnable\nfrom typing_extensions import TypedDict\n\nimport apysc as ap\n\n\nclass _RectOptions(TypedDict):\n    rectangle: ap.Rectangle\n\n\ndef on_timer(e: ap.TimerEvent, options: _RectOptions) -> None:\n    """\n    The handler that the timer calls.\n\n    Parameters\n    ----------\n    e : TimerEvent\n        Event instance.\n    options : dict\n        Optional arguments dictionary.\n    """\n    rectangle: ap.Rectangle = options["rectangle"]\n    rectangle.skew_y += 1\n\n\nap.Stage(\n    stage_width=150, stage_height=150, background_color="#333", stage_elem_id="stage"\n)\nsprite: ap.Sprite = ap.Sprite()\nsprite.graphics.begin_fill(color="#0af")\n\nrectangle: ap.Rectangle = sprite.graphics.draw_rect(x=50, y=50, width=50, height=50)\noptions: _RectOptions = {"rectangle": rectangle}\ntimer: ap.Timer = ap.Timer(handler=on_timer, delay=ap.FPS.FPS_60, options=options)\ntimer.start()\n\nap.save_overall_html(dest_dir_path="graphics_base_skew_y_incremental_basic_usage/")\n```': '```py\n# runnable\nfrom typing_extensions import TypedDict\n\nimport apysc as ap\n\n\nclass _RectOptions(TypedDict):\n    rectangle: ap.Rectangle\n\n\ndef on_timer(e: ap.TimerEvent, options: _RectOptions) -> None:\n    """\n    The handler that the timer calls.\n\n    Parameters\n    ----------\n    e : TimerEvent\n        Event instance.\n    options : dict\n        Optional arguments dictionary.\n    """\n    rectangle: ap.Rectangle = options["rectangle"]\n    rectangle.skew_y += 1\n\n\nap.Stage(\n    stage_width=150, stage_height=150, background_color="#333", stage_elem_id="stage"\n)\nsprite: ap.Sprite = ap.Sprite()\nsprite.graphics.begin_fill(color="#0af")\n\nrectangle: ap.Rectangle = sprite.graphics.draw_rect(x=50, y=50, width=50, height=50)\noptions: _RectOptions = {"rectangle": rectangle}\ntimer: ap.Timer = ap.Timer(handler=on_timer, delay=ap.FPS.FPS_60, options=options)\ntimer.start()\n\nap.save_overall_html(dest_dir_path="graphics_base_skew_y_incremental_basic_usage/")\n```',  # noqa
    ##################################################
    "## skew_x property API": "## skew_x property API",
    ##################################################
    '<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>': '<span class="inconspicuous-txt">特記事項: このAPIドキュメントはドキュメントビルド用のスクリプトによって自動で生成・同期されています。そのためもしかしたらこの節の内容は前節までの内容と重複している場合があります。</span>',  # noqa
    ##################################################
    "**[Interface summary]**": "**[インターフェイス概要]**",
    ##################################################
    "Get a current skew x value of the instance.<hr>": "インスタンスの現在のX軸の歪みの値を取得します。<hr>",
    ##################################################
    "**[Returns]**": "**[返却値]**",
    ##################################################
    "- `skew_x`: Int": "- `skew_x`: Int",
    ##################################################
    "  - Current skew x value of this instance.": "  - インスタンスの現在のX軸の歪みの値。",
    ##################################################
    "<hr>": "<hr>",
    ##################################################
    "**[Examples]**": "**[コードサンプル]**",
    ##################################################
    '```py\n>>> import apysc as ap\n>>> stage: ap.Stage = ap.Stage()\n>>> sprite: ap.Sprite = ap.Sprite()\n>>> sprite.graphics.begin_fill(color="#0af")\n>>> rectangle: ap.Rectangle = sprite.graphics.draw_rect(\n...     x=50, y=50, width=50, height=50\n... )\n>>> rectangle.skew_x = ap.Int(50)\n>>> rectangle.skew_x\nInt(50)\n```': '```py\n>>> import apysc as ap\n>>> stage: ap.Stage = ap.Stage()\n>>> sprite: ap.Sprite = ap.Sprite()\n>>> sprite.graphics.begin_fill(color="#0af")\n>>> rectangle: ap.Rectangle = sprite.graphics.draw_rect(\n...     x=50, y=50, width=50, height=50\n... )\n>>> rectangle.skew_x = ap.Int(50)\n>>> rectangle.skew_x\nInt(50)\n```',  # noqa
    ##################################################
    "## skew_y property API": "## skew_y property API",
    ##################################################
    '<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>': '<span class="inconspicuous-txt">特記事項: このAPIドキュメントはドキュメントビルド用のスクリプトによって自動で生成・同期されています。そのためもしかしたらこの節の内容は前節までの内容と重複している場合があります。</span>',  # noqa
    ##################################################
    "**[Interface summary]**": "**[インターフェイス概要]**",
    ##################################################
    "Get a current skew y value of the instance.<hr>": "インスタンスの現在のY軸の歪みの値を取得します。<hr>",
    ##################################################
    "**[Returns]**": "**[返却値]**",
    ##################################################
    "- `skew_y`: Int": "- `skew_y`: Int",
    ##################################################
    "  - Current skew y value of the instance.": "  - インスタンスの現在のY軸の歪みの値。",
    ##################################################
    "<hr>": "<hr>",
    ##################################################
    "**[Examples]**": "**[コードサンプル]**",
    ##################################################
    '```py\n>>> import apysc as ap\n>>> stage: ap.Stage = ap.Stage()\n>>> sprite: ap.Sprite = ap.Sprite()\n>>> sprite.graphics.begin_fill(color="#0af")\n>>> rectangle: ap.Rectangle = sprite.graphics.draw_rect(\n...     x=50, y=50, width=50, height=50\n... )\n>>> rectangle.skew_y = ap.Int(50)\n>>> rectangle.skew_y\nInt(50)\n```': '```py\n>>> import apysc as ap\n>>> stage: ap.Stage = ap.Stage()\n>>> sprite: ap.Sprite = ap.Sprite()\n>>> sprite.graphics.begin_fill(color="#0af")\n>>> rectangle: ap.Rectangle = sprite.graphics.draw_rect(\n...     x=50, y=50, width=50, height=50\n... )\n>>> rectangle.skew_y = ap.Int(50)\n>>> rectangle.skew_y\nInt(50)\n```',  # noqa
}
