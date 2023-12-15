"""This module is for the translation mapping data of the
following document:

Document file: animation_reset.md
Language: jp
"""

from typing import Dict

MAPPING: Dict[str, str] = {
    ##################################################
    "# animation_reset interface": "# animation_reset インターフェイス",
    ##################################################
    "This page explains the `animation_reset` method interface.": "このページでは`animation_reset`メソッドのインターフェイスについて説明します。",  # noqa
    ##################################################
    "## What interface is this?": "## インターフェイス概要",
    ##################################################
    "The `animation_reset` interface resets all animations and stop.": "`animation_reset`インターフェイスは全てのアニメーションのリセットと停止を行います。",  # noqa
    ##################################################
    "This interface exists in the instances that have the animation interfaces (such as the `animation_x`\\, `animation_move`).": "このインターフェイスは`animation_x`や`animation_move`などのアニメーション関係のインターフェイスを持つクラスのインスタンス上に存在します。",  # noqa
    ##################################################
    "## Basic usage": "## 基本的な使い方",
    ##################################################
    "The following example sets the click event to the rectangle. If you click the rectangle, the x-coordinate animation starts. After 1 second has passed, the `animation_reset` interface resets the x-coordinate animation:": "以下のコード例では四角にクリックイベントを設定し、四角をクリックした際にX座標にアニメーションがスタートするようにしてあります。アニメーションがスタートしてから1秒経過した時点で`animation_reset`インターフェイスによってX座標のリセットが実行されています。",  # noqa
    ##################################################
    '```py\n# runnable\nfrom typing_extensions import TypedDict\n\nimport apysc as ap\n\n\nclass _RectOptions(TypedDict):\n    rectangle: ap.Rectangle\n\n\ndef on_click(e: ap.MouseEvent[ap.Rectangle], options: dict) -> None:\n    """\n    The handler that the rectangle calls when clicked.\n\n    Parameters\n    ----------\n    e : ap.Rectangle\n        Event instance.\n    options : dict\n        Optional arguments dictionary.\n    """\n    e.this.animation_x(x=500, duration=3000).start()\n    options_: _RectOptions = {"rectangle": e.this}\n    timer: ap.Timer = ap.Timer(on_timer, delay=1000, repeat_count=1, options=options_)\n    timer.start()\n\n\ndef on_timer(e: ap.TimerEvent, options: _RectOptions) -> None:\n    """\n    The handler that the timer calls.\n\n    Parameters\n    ----------\n    e : ap.TimerEvent\n        Event instance.\n    options : _RectOptions\n        Optional arguments dictionary.\n    """\n    options["rectangle"].animation_reset()\n\n\nap.Stage(\n    stage_width=600,\n    stage_height=150,\n    background_color=ap.Color("#333"),\n    stage_elem_id="stage",\n)\nsprite: ap.Sprite = ap.Sprite()\nsprite.graphics.begin_fill(color=ap.Color("#00aaff"))\nrectangle: ap.Rectangle = sprite.graphics.draw_rect(x=50, y=50, width=50, height=50)\nrectangle.click(on_click)\n\nap.save_overall_html(dest_dir_path="./animation_reset_basic_usage/")\n```': '```py\n# runnable\nfrom typing_extensions import TypedDict\n\nimport apysc as ap\n\n\nclass _RectOptions(TypedDict):\n    rectangle: ap.Rectangle\n\n\ndef on_click(e: ap.MouseEvent[ap.Rectangle], options: dict) -> None:\n    """\n    The handler that the rectangle calls when clicked.\n\n    Parameters\n    ----------\n    e : ap.Rectangle\n        Event instance.\n    options : dict\n        Optional arguments dictionary.\n    """\n    e.this.animation_x(x=500, duration=3000).start()\n    options_: _RectOptions = {"rectangle": e.this}\n    timer: ap.Timer = ap.Timer(on_timer, delay=1000, repeat_count=1, options=options_)\n    timer.start()\n\n\ndef on_timer(e: ap.TimerEvent, options: _RectOptions) -> None:\n    """\n    The handler that the timer calls.\n\n    Parameters\n    ----------\n    e : ap.TimerEvent\n        Event instance.\n    options : _RectOptions\n        Optional arguments dictionary.\n    """\n    options["rectangle"].animation_reset()\n\n\nap.Stage(\n    stage_width=600,\n    stage_height=150,\n    background_color=ap.Color("#333"),\n    stage_elem_id="stage",\n)\nsprite: ap.Sprite = ap.Sprite()\nsprite.graphics.begin_fill(color=ap.Color("#00aaff"))\nrectangle: ap.Rectangle = sprite.graphics.draw_rect(x=50, y=50, width=50, height=50)\nrectangle.click(on_click)\n\nap.save_overall_html(dest_dir_path="./animation_reset_basic_usage/")\n```',  # noqa
    ##################################################
    "## animation_reset API": "## animation_reset API",
    ##################################################
    '<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>': '<span class="inconspicuous-txt">特記事項: このAPIドキュメントはドキュメントビルド用のスクリプトによって自動で生成・同期されています。そのためもしかしたらこの節の内容は前節までの内容と重複している場合があります。</span>',  # noqa
    ##################################################
    "**[Interface summary]**": "**[インターフェイス概要]**",
    ##################################################
    "Stop all animations and reset.<hr>": "全てのアニメーションを停止しアニメーション内容をリセットします。<hr>",
    ##################################################
    "**[Examples]**": "**[コードサンプル]**",
    ##################################################
    '```py\n>>> from typing_extensions import TypedDict\n>>> import apysc as ap\n>>> class RectOptions(TypedDict):\n...     rectangle: ap.Rectangle\n...\n>>> def on_timer(e: ap.TimerEvent, options: RectOptions) -> None:\n...     rectangle: ap.Rectangle = options["rectangle"]\n...     rectangle.animation_reset()\n>>> stage: ap.Stage = ap.Stage()\n>>> sprite: ap.Sprite = ap.Sprite()\n>>> sprite.graphics.begin_fill(color=ap.Color("#0af"))\n>>> rectangle: ap.Rectangle = sprite.graphics.draw_rect(\n...     x=50, y=50, width=50, height=50\n... )\n>>> _ = rectangle.animation_x(\n...     x=100,\n...     duration=1500,\n...     easing=ap.Easing.EASE_OUT_QUINT,\n... ).start()\n>>> options: RectOptions = {"rectangle": rectangle}\n>>> ap.Timer(on_timer, delay=750, options=options).start()\n```': '```py\n>>> from typing_extensions import TypedDict\n>>> import apysc as ap\n>>> class RectOptions(TypedDict):\n...     rectangle: ap.Rectangle\n...\n>>> def on_timer(e: ap.TimerEvent, options: RectOptions) -> None:\n...     rectangle: ap.Rectangle = options["rectangle"]\n...     rectangle.animation_reset()\n>>> stage: ap.Stage = ap.Stage()\n>>> sprite: ap.Sprite = ap.Sprite()\n>>> sprite.graphics.begin_fill(color=ap.Color("#0af"))\n>>> rectangle: ap.Rectangle = sprite.graphics.draw_rect(\n...     x=50, y=50, width=50, height=50\n... )\n>>> _ = rectangle.animation_x(\n...     x=100,\n...     duration=1500,\n...     easing=ap.Easing.EASE_OUT_QUINT,\n... ).start()\n>>> options: RectOptions = {"rectangle": rectangle}\n>>> ap.Timer(on_timer, delay=750, options=options).start()\n```',  # noqa
}
