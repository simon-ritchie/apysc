"""This module is for the translation mapping data of the
following document:

Document file: animation_time.md
Language: jp
"""

from typing import Dict

MAPPING: Dict[str, str] = {
    ##################################################
    "# animation_time interface": "# animation_time インターフェイス",
    ##################################################
    "This page explains the `animation_time` method interface.": "このページでは`animation_time`メソッドのインターフェイスについて説明します。",  # noqa
    ##################################################
    "## What interface is this?": "## インターフェイス概要",
    ##################################################
    "The `animation_time` interface returns the current animation elapsed time in milliseconds (`Number` type value).": "`animation_time`インターフェイスは現在のアニメーションの経過時間をミリ秒で返却します（`Number`型の値で設定されます）。",  # noqa
    ##################################################
    "## Basic usage": "## 基本的な使い方",
    ##################################################
    "The following example sets the x-coordinate animation of the rectangle and the 1-second interval timer to display an animation's current elapsed time to console (please press the F12 key).": "以下のコード例では四角に対してX座標のアニメーションを設定し、1秒ごとにアニメーションの経過時間をコンソールに出力しています（出力内容はF12キーを押してブラウザで確認してください）。",  # noqa
    ##################################################
    '```py\n# runnable\nfrom typing_extensions import TypedDict\n\nimport apysc as ap\n\n\nclass _RectOptions(TypedDict):\n    rectangle: ap.Rectangle\n\n\ndef on_timer(e: ap.TimerEvent, options: _RectOptions) -> None:\n    """\n    The handler that the animation calls.\n\n    Parameters\n    ----------\n    e : ap.TimerEvent\n        Event instance.\n    options : dict\n        Optional arguments dictionary.\n    """\n    rectangle: ap.Rectangle = options["rectangle"]\n    ap.trace("Animation elapsed time:", rectangle.animation_time())\n\n\nap.Stage(\n    stage_width=500, stage_height=150, background_color="#333", stage_elem_id="stage"\n)\nsprite: ap.Sprite = ap.Sprite()\nsprite.graphics.begin_fill(color="#0af")\n\nrectangle: ap.Rectangle = sprite.graphics.draw_rect(x=50, y=50, width=50, height=50)\nrectangle.animation_x(x=400, duration=10000).start()\n\noptions: _RectOptions = {"rectangle": rectangle}\nap.Timer(on_timer, delay=1000, options=options).start()\n\nap.save_overall_html(dest_dir_path="animation_time_basic_usage/")\n```': '```py\n# runnable\nfrom typing_extensions import TypedDict\n\nimport apysc as ap\n\n\nclass _RectOptions(TypedDict):\n    rectangle: ap.Rectangle\n\n\ndef on_timer(e: ap.TimerEvent, options: _RectOptions) -> None:\n    """\n    The handler that the animation calls.\n\n    Parameters\n    ----------\n    e : ap.TimerEvent\n        Event instance.\n    options : dict\n        Optional arguments dictionary.\n    """\n    rectangle: ap.Rectangle = options["rectangle"]\n    ap.trace("Animation elapsed time:", rectangle.animation_time())\n\n\nap.Stage(\n    stage_width=500, stage_height=150, background_color="#333", stage_elem_id="stage"\n)\nsprite: ap.Sprite = ap.Sprite()\nsprite.graphics.begin_fill(color="#0af")\n\nrectangle: ap.Rectangle = sprite.graphics.draw_rect(x=50, y=50, width=50, height=50)\nrectangle.animation_x(x=400, duration=10000).start()\n\noptions: _RectOptions = {"rectangle": rectangle}\nap.Timer(on_timer, delay=1000, options=options).start()\n\nap.save_overall_html(dest_dir_path="animation_time_basic_usage/")\n```',  # noqa
    ##################################################
    "## animation_time API": "## animation_time API",
    ##################################################
    '<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>': '<span class="inconspicuous-txt">特記事項: このAPIドキュメントはドキュメントビルド用のスクリプトによって自動で生成・同期されています。そのためもしかしたらこの節の内容は前節までの内容と重複している場合があります。</span>',  # noqa
    ##################################################
    "**[Interface summary]**": "**[インターフェイス概要]**",
    ##################################################
    "Get an animation elapsed millisecond.<hr>": "アニメーションの経過時間のミリ秒を取得します。<hr>",
    ##################################################
    "**[Returns]**": "**[返却値]**",
    ##################################################
    "- `elapsed_time`: Number": "- `elapsed_time`: Number",
    ##################################################
    "  - An animation elapsed millisecond.": "  - アニメーションの経過時間のミリ秒。",
    ##################################################
    "<hr>": "<hr>",
    ##################################################
    "**[Examples]**": "**[コードサンプル]**",
    ##################################################
    '```py\n>>> from typing_extensions import TypedDict\n>>> import apysc as ap\n>>> class RectOptions(TypedDict):\n...     rectangle: ap.Rectangle\n...\n>>> def on_timer(e: ap.TimerEvent, options: RectOptions) -> None:\n...     rectangle: ap.Rectangle = options["rectangle"]\n...     animation_time: ap.Number = rectangle.animation_time()\n...     ap.trace("animation_time:", animation_time)\n>>> stage: ap.Stage = ap.Stage()\n>>> sprite: ap.Sprite = ap.Sprite()\n>>> sprite.graphics.begin_fill(color="#0af")\n>>> rectangle: ap.Rectangle = sprite.graphics.draw_rect(\n...     x=50, y=50, width=50, height=50\n... )\n>>> _ = rectangle.animation_x(\n...     x=100,\n...     duration=1500,\n...     easing=ap.Easing.EASE_OUT_QUINT,\n... ).start()\n>>> options: RectOptions = {"rectangle": rectangle}\n>>> ap.Timer(on_timer, delay=ap.FPS.FPS_60, options=options).start()\n```': '```py\n>>> from typing_extensions import TypedDict\n>>> import apysc as ap\n>>> class RectOptions(TypedDict):\n...     rectangle: ap.Rectangle\n...\n>>> def on_timer(e: ap.TimerEvent, options: RectOptions) -> None:\n...     rectangle: ap.Rectangle = options["rectangle"]\n...     animation_time: ap.Number = rectangle.animation_time()\n...     ap.trace("animation_time:", animation_time)\n>>> stage: ap.Stage = ap.Stage()\n>>> sprite: ap.Sprite = ap.Sprite()\n>>> sprite.graphics.begin_fill(color="#0af")\n>>> rectangle: ap.Rectangle = sprite.graphics.draw_rect(\n...     x=50, y=50, width=50, height=50\n... )\n>>> _ = rectangle.animation_x(\n...     x=100,\n...     duration=1500,\n...     easing=ap.Easing.EASE_OUT_QUINT,\n... ).start()\n>>> options: RectOptions = {"rectangle": rectangle}\n>>> ap.Timer(on_timer, delay=ap.FPS.FPS_60, options=options).start()\n```',  # noqa
}
