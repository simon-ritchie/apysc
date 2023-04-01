"""This module is for the translation mapping data of the
following document:

Document file: timer_start_and_stop.md
Language: jp
"""

from typing import Dict

MAPPING: Dict[str, str] = {
    ##################################################
    "# Timer class start and stop interfaces": "# Timer クラスの start と stop のインターフェイス",
    ##################################################
    "This page explains the interface of the Timer class `start` and `stop` methods.": "このページでTimerクラスの`start`と`stop`メソッドの各インターフェイスについて説明します。",  # noqa
    ##################################################
    "## What interfaces are these?": "## 各インターフェイスの概要",
    ##################################################
    "The `start` method interface starts a timer. Conversely, the `stop` method interface stops a timer.": "`start`メソッドのインターフェイスはタイマーをスタートさせます。逆に`stop`メソッドのインターフェイスはタイマーを停止させます。",  # noqa
    ##################################################
    "## Basic usage": "## 基本的な使い方",
    ##################################################
    "Each `start` and `stop` method has no arguments. The following example starts the timer when you click the rectangle and stops when the count reaches 100.": "`start`と`stop`の各メソッドは引数を必要としません。以下のコード例では四角をクリックした際にタイマーをスタートさせ、タイマーのカウントが100に達した時点でタイマーを停止させています。",  # noqa
    ##################################################
    '```py\n# runnable\nfrom typing_extensions import TypedDict\n\nimport apysc as ap\n\n\nclass _RectOptions(TypedDict):\n    rectangle: ap.Rectangle\n\n\ndef on_rectangle_click(e: ap.MouseEvent[ap.Rectangle], options: dict) -> None:\n    """\n    The handler that a rectangle calls when clicked.\n\n    Parameters\n    ----------\n    e : ap.MouseEvent\n        Event instance.\n    options : dict\n        Optional arguments dictionary.\n    """\n    options_: _RectOptions = {"rectangle": e.this}\n    timer: ap.Timer = ap.Timer(\n        handler=on_timer, delay=16, repeat_count=100, options=options_\n    )\n    timer.start()\n    e.this.unbind_click(handler=on_rectangle_click)\n\n\ndef on_timer(e: ap.TimerEvent, options: _RectOptions) -> None:\n    """\n    The handler what a timer calls.\n\n    Parameters\n    ----------\n    e : ap.TimerEvent\n        Event instance.\n    options : dict\n        Optional arguments dictionary.\n    """\n    rectangle: ap.Rectangle = options["rectangle"]\n    rectangle.x += 1\n    timer: ap.Timer = e.this\n    condition: ap.Boolean = timer.current_count == 100\n    with ap.If(condition):\n        timer.stop()\n\n\nap.Stage(\n    stage_width=250, stage_height=150, background_color="#333", stage_elem_id="stage"\n)\nsprite: ap.Sprite = ap.Sprite()\nsprite.graphics.begin_fill(color="#0af")\nrectangle: ap.Rectangle = sprite.graphics.draw_rect(x=50, y=50, width=50, height=50)\nrectangle.click(on_rectangle_click)\n\nap.save_overall_html(dest_dir_path="timer_start_and_stop_basic_usage/")\n```': '```py\n# runnable\nfrom typing_extensions import TypedDict\n\nimport apysc as ap\n\n\nclass _RectOptions(TypedDict):\n    rectangle: ap.Rectangle\n\n\ndef on_rectangle_click(e: ap.MouseEvent[ap.Rectangle], options: dict) -> None:\n    """\n    The handler that a rectangle calls when clicked.\n\n    Parameters\n    ----------\n    e : ap.MouseEvent\n        Event instance.\n    options : dict\n        Optional arguments dictionary.\n    """\n    options_: _RectOptions = {"rectangle": e.this}\n    timer: ap.Timer = ap.Timer(\n        handler=on_timer, delay=16, repeat_count=100, options=options_\n    )\n    timer.start()\n    e.this.unbind_click(handler=on_rectangle_click)\n\n\ndef on_timer(e: ap.TimerEvent, options: _RectOptions) -> None:\n    """\n    The handler what a timer calls.\n\n    Parameters\n    ----------\n    e : ap.TimerEvent\n        Event instance.\n    options : dict\n        Optional arguments dictionary.\n    """\n    rectangle: ap.Rectangle = options["rectangle"]\n    rectangle.x += 1\n    timer: ap.Timer = e.this\n    condition: ap.Boolean = timer.current_count == 100\n    with ap.If(condition):\n        timer.stop()\n\n\nap.Stage(\n    stage_width=250, stage_height=150, background_color="#333", stage_elem_id="stage"\n)\nsprite: ap.Sprite = ap.Sprite()\nsprite.graphics.begin_fill(color="#0af")\nrectangle: ap.Rectangle = sprite.graphics.draw_rect(x=50, y=50, width=50, height=50)\nrectangle.click(on_rectangle_click)\n\nap.save_overall_html(dest_dir_path="timer_start_and_stop_basic_usage/")\n```',  # noqa
    ##################################################
    "## start API": "## start API",
    ##################################################
    '<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>': '<span class="inconspicuous-txt">特記事項: このAPIドキュメントはドキュメントビルド用のスクリプトによって自動で生成・同期されています。そのためもしかしたらこの節の内容は前節までの内容と重複している場合があります。</span>',  # noqa
    ##################################################
    "**[Interface summary]**": "**[インターフェイス概要]**",
    ##################################################
    "Start this timer.<hr>": "タイマーを開始します。<hr>",
    ##################################################
    "**[Examples]**": "**[コードサンプル]**",
    ##################################################
    "```py\n>>> import apysc as ap\n>>> def on_timer(e: ap.TimerEvent, options: dict) -> None:\n...     pass\n>>> _ = ap.Timer(on_timer, delay=33.3, repeat_count=50).start()\n```": "```py\n>>> import apysc as ap\n>>> def on_timer(e: ap.TimerEvent, options: dict) -> None:\n...     pass\n>>> _ = ap.Timer(on_timer, delay=33.3, repeat_count=50).start()\n```",  # noqa
    ##################################################
    "## stop API": "## stop API",
    ##################################################
    '<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>': '<span class="inconspicuous-txt">特記事項: このAPIドキュメントはドキュメントビルド用のスクリプトによって自動で生成・同期されています。そのためもしかしたらこの節の内容は前節までの内容と重複している場合があります。</span>',  # noqa
    ##################################################
    "**[Interface summary]**": "**[インターフェイス概要]**",
    ##################################################
    "Stop this timer.<hr>": "タイマーを停止します。<hr>",
    ##################################################
    "**[Examples]**": "**[コードサンプル]**",
    ##################################################
    '```py\n>>> from typing_extensions import TypedDict\n>>> import apysc as ap\n>>> class RectOptions(TypedDict):\n...     rectangle: ap.Rectangle\n...\n>>> def on_timer(e: ap.TimerEvent, options: RectOptions) -> None:\n...     rectangle: ap.Rectangle = options["rectangle"]\n...     rectangle.x += 1\n...     with ap.If(rectangle.x > 100):\n...         timer: ap.Timer = e.this\n...         timer.stop()\n>>> stage: ap.Stage = ap.Stage()\n>>> sprite: ap.Sprite = ap.Sprite()\n>>> sprite.graphics.begin_fill(color="#0af")\n>>> rectangle: ap.Rectangle = sprite.graphics.draw_rect(\n...     x=50, y=50, width=50, height=50\n... )\n>>> options: RectOptions = {"rectangle": rectangle}\n>>> _ = ap.Timer(on_timer, delay=33.3, options=options).start()\n```': '```py\n>>> from typing_extensions import TypedDict\n>>> import apysc as ap\n>>> class RectOptions(TypedDict):\n...     rectangle: ap.Rectangle\n...\n>>> def on_timer(e: ap.TimerEvent, options: RectOptions) -> None:\n...     rectangle: ap.Rectangle = options["rectangle"]\n...     rectangle.x += 1\n...     with ap.If(rectangle.x > 100):\n...         timer: ap.Timer = e.this\n...         timer.stop()\n>>> stage: ap.Stage = ap.Stage()\n>>> sprite: ap.Sprite = ap.Sprite()\n>>> sprite.graphics.begin_fill(color="#0af")\n>>> rectangle: ap.Rectangle = sprite.graphics.draw_rect(\n...     x=50, y=50, width=50, height=50\n... )\n>>> options: RectOptions = {"rectangle": rectangle}\n>>> _ = ap.Timer(on_timer, delay=33.3, options=options).start()\n```',  # noqa
}
