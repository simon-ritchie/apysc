"""This module is for the translation mapping data of the
following document:

Document file: animation_pause_and_play.md
Language: jp
"""

from typing import Dict

MAPPING: Dict[str, str] = {
    ##################################################
    "# animation_pause and animation_play interfaces": "# animation_pause と animation_play インターフェイス",  # noqa
    ##################################################
    "This page explains the `animation_pause` and `animation_play` method interfaces.": "このページでは`animation_pause`と`animation_play`のメソッドの各インターフェイスについて説明します。",  # noqa
    ##################################################
    "## What interface are these?": "## 各インターフェイス概要",
    ##################################################
    "The `animation_pause` interface pauses all the running animations of the target instance. The `animation_play` interface restarts the paused animation.": "`animation_pause`インターフェイスは対象のインスタンスで動いている全てのアニメーションを停止します。`animation_play`インターフェイスは停止しているアニメーションを再開します。",  # noqa
    ##################################################
    "These interfaces exist in the instances that have the animation interfaces (such as the `animation_x`\\, `animation_move`).": "これらのインターフェイスは`animation_x`や`animation_move`などのアニメーション関係のインターフェイスを持つクラスのインスタンス上に存在します。",  # noqa
    ##################################################
    "## Basic usage": "## 基本的な使い方",
    ##################################################
    "The following example starts the x-coordinate animation and stops after 1 second. After stopping the animation and additionally 500 milliseconds passed, restarting the animation:": "以下のコード例ではX座標のアニメーションをスタートし、その1秒後にアニメーションを停止しています。加えて、停止してからさらに500ミリ秒経過した時点でアニメーションを再開しています。",  # noqa
    ##################################################
    '```py\n# runnable\nfrom typing_extensions import TypedDict\n\nimport apysc as ap\n\n\nclass _RectOptions(TypedDict):\n    rectangle: ap.Rectangle\n\n\ndef on_timer_1(e: ap.TimerEvent, options: _RectOptions) -> None:\n    """\n    The handler that the timer calls.\n\n    Parameters\n    ----------\n    e : ap.TimerEvent\n        Event instance.\n    options : _RectOptions\n        Optional arguments dictionary.\n    """\n    options["rectangle"].animation_pause()\n    timer: ap.Timer = ap.Timer(on_timer_2, delay=500, options=options, repeat_count=1)\n    timer.start()\n\n\ndef on_timer_2(e: ap.TimerEvent, options: _RectOptions) -> None:\n    """\n    The handler that the timer calls.\n\n    Parameters\n    ----------\n    e : ap.TimerEvent\n        Event instance.\n    options : _RectOptions\n        Optional arguments dictionary.\n    """\n    options["rectangle"].animation_play()\n\n\nap.Stage(\n    stage_width=600, stage_height=150, background_color="#333", stage_elem_id="stage"\n)\nsprite: ap.Sprite = ap.Sprite()\nsprite.graphics.begin_fill(color="#00aaff")\nrectangle: ap.Rectangle = sprite.graphics.draw_rect(x=50, y=50, width=50, height=50)\nrectangle.animation_x(x=500, duration=15_000).start()\n\noptions: _RectOptions = {"rectangle": rectangle}\ntimer: ap.Timer = ap.Timer(on_timer_1, delay=1000, options=options)\ntimer.start()\n\nap.save_overall_html(dest_dir_path="./animation_pause_basic_usage/")\n```': '```py\n# runnable\nfrom typing_extensions import TypedDict\n\nimport apysc as ap\n\n\nclass _RectOptions(TypedDict):\n    rectangle: ap.Rectangle\n\n\ndef on_timer_1(e: ap.TimerEvent, options: _RectOptions) -> None:\n    """\n    The handler that the timer calls.\n\n    Parameters\n    ----------\n    e : ap.TimerEvent\n        Event instance.\n    options : _RectOptions\n        Optional arguments dictionary.\n    """\n    options["rectangle"].animation_pause()\n    timer: ap.Timer = ap.Timer(on_timer_2, delay=500, options=options, repeat_count=1)\n    timer.start()\n\n\ndef on_timer_2(e: ap.TimerEvent, options: _RectOptions) -> None:\n    """\n    The handler that the timer calls.\n\n    Parameters\n    ----------\n    e : ap.TimerEvent\n        Event instance.\n    options : _RectOptions\n        Optional arguments dictionary.\n    """\n    options["rectangle"].animation_play()\n\n\nap.Stage(\n    stage_width=600, stage_height=150, background_color="#333", stage_elem_id="stage"\n)\nsprite: ap.Sprite = ap.Sprite()\nsprite.graphics.begin_fill(color="#00aaff")\nrectangle: ap.Rectangle = sprite.graphics.draw_rect(x=50, y=50, width=50, height=50)\nrectangle.animation_x(x=500, duration=15_000).start()\n\noptions: _RectOptions = {"rectangle": rectangle}\ntimer: ap.Timer = ap.Timer(on_timer_1, delay=1000, options=options)\ntimer.start()\n\nap.save_overall_html(dest_dir_path="./animation_pause_basic_usage/")\n```',  # noqa
    ##################################################
    "## animation_pause API": "## animation_pause API",
    ##################################################
    '<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>': '<span class="inconspicuous-txt">特記事項: このAPIドキュメントはドキュメントビルド用のスクリプトによって自動で生成・同期されています。そのためもしかしたらこの節の内容は前節までの内容と重複している場合があります。</span>',  # noqa
    ##################################################
    "**[Interface summary]**": "**[インターフェイス概要]**",
    ##################################################
    "Stop all animations.<hr>": "全てのアニメーションを停止します。<hr>",
    ##################################################
    "**[Examples]**": "**[コードサンプル]**",
    ##################################################
    '```py\n>>> from typing_extensions import TypedDict\n>>> import apysc as ap\n>>> class RectOptions(TypedDict):\n...     rectangle: ap.Rectangle\n...\n>>> def on_timer(e: ap.TimerEvent, options: RectOptions) -> None:\n...     rectangle: ap.Rectangle = options["rectangle"]\n...     rectangle.animation_pause()\n>>> stage: ap.Stage = ap.Stage()\n>>> sprite: ap.Sprite = ap.Sprite()\n>>> sprite.graphics.begin_fill(color="#0af")\n>>> rectangle: ap.Rectangle = sprite.graphics.draw_rect(\n...     x=50, y=50, width=50, height=50\n... )\n>>> _ = rectangle.animation_x(\n...     x=100,\n...     duration=1500,\n...     easing=ap.Easing.EASE_OUT_QUINT,\n... ).start()\n>>> options: RectOptions = {"rectangle": rectangle}\n>>> ap.Timer(on_timer, delay=750, options=options).start()\n```': '```py\n>>> from typing_extensions import TypedDict\n>>> import apysc as ap\n>>> class RectOptions(TypedDict):\n...     rectangle: ap.Rectangle\n...\n>>> def on_timer(e: ap.TimerEvent, options: RectOptions) -> None:\n...     rectangle: ap.Rectangle = options["rectangle"]\n...     rectangle.animation_pause()\n>>> stage: ap.Stage = ap.Stage()\n>>> sprite: ap.Sprite = ap.Sprite()\n>>> sprite.graphics.begin_fill(color="#0af")\n>>> rectangle: ap.Rectangle = sprite.graphics.draw_rect(\n...     x=50, y=50, width=50, height=50\n... )\n>>> _ = rectangle.animation_x(\n...     x=100,\n...     duration=1500,\n...     easing=ap.Easing.EASE_OUT_QUINT,\n... ).start()\n>>> options: RectOptions = {"rectangle": rectangle}\n>>> ap.Timer(on_timer, delay=750, options=options).start()\n```',  # noqa
    ##################################################
    "## animation_play API": "## animation_play API",
    ##################################################
    '<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>': '<span class="inconspicuous-txt">特記事項: このAPIドキュメントはドキュメントビルド用のスクリプトによって自動で生成・同期されています。そのためもしかしたらこの節の内容は前節までの内容と重複している場合があります。</span>',  # noqa
    ##################################################
    "**[Interface summary]**": "**[インターフェイス概要]**",
    ##################################################
    "Restart all paused animations.<hr>": "停止している全てのアニメーションを再開します。<hr>",
    ##################################################
    "**[Examples]**": "**[コードサンプル]**",
    ##################################################
    '```py\n>>> from typing_extensions import TypedDict\n>>> import apysc as ap\n>>> class RectOptions(TypedDict):\n...     rectangle: ap.Rectangle\n...\n>>> def on_timer_1(e: ap.TimerEvent, options: RectOptions) -> None:\n...     rectangle: ap.Rectangle = options["rectangle"]\n...     rectangle.animation_pause()\n>>> def on_timer_2(e: ap.TimerEvent, options: RectOptions) -> None:\n...     rectangle: ap.Rectangle = options["rectangle"]\n...     rectangle.animation_play()\n>>> stage: ap.Stage = ap.Stage()\n>>> sprite: ap.Sprite = ap.Sprite()\n>>> sprite.graphics.begin_fill(color="#0af")\n>>> rectangle: ap.Rectangle = sprite.graphics.draw_rect(\n...     x=50, y=50, width=50, height=50\n... )\n>>> _ = rectangle.animation_x(\n...     x=100,\n...     duration=1500,\n...     easing=ap.Easing.EASE_OUT_QUINT,\n... ).start()\n>>> options: RectOptions = {"rectangle": rectangle}\n>>> ap.Timer(on_timer_1, delay=500, options=options).start()\n>>> ap.Timer(on_timer_2, delay=1000, options=options).start()\n```': '```py\n>>> from typing_extensions import TypedDict\n>>> import apysc as ap\n>>> class RectOptions(TypedDict):\n...     rectangle: ap.Rectangle\n...\n>>> def on_timer_1(e: ap.TimerEvent, options: RectOptions) -> None:\n...     rectangle: ap.Rectangle = options["rectangle"]\n...     rectangle.animation_pause()\n>>> def on_timer_2(e: ap.TimerEvent, options: RectOptions) -> None:\n...     rectangle: ap.Rectangle = options["rectangle"]\n...     rectangle.animation_play()\n>>> stage: ap.Stage = ap.Stage()\n>>> sprite: ap.Sprite = ap.Sprite()\n>>> sprite.graphics.begin_fill(color="#0af")\n>>> rectangle: ap.Rectangle = sprite.graphics.draw_rect(\n...     x=50, y=50, width=50, height=50\n... )\n>>> _ = rectangle.animation_x(\n...     x=100,\n...     duration=1500,\n...     easing=ap.Easing.EASE_OUT_QUINT,\n... ).start()\n>>> options: RectOptions = {"rectangle": rectangle}\n>>> ap.Timer(on_timer_1, delay=500, options=options).start()\n>>> ap.Timer(on_timer_2, delay=1000, options=options).start()\n```',  # noqa
}
