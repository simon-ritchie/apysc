"""This module is for the translation mapping data of the
following document:

Document file: timer_complete.md
Language: jp
"""

from typing import Dict

MAPPING: Dict[str, str] = {
    ##################################################
    "# Timer class timer_complete interface": "# Timer クラスの timer_complete インターフェイス",
    ##################################################
    "This page explains the `Timer` class `timer_complete` method interface.": "このページでは`Timer`クラスの`timer_complete`メソッドのインターフェイスについて説明します。",  # noqa
    ##################################################
    "## What interface is this?": "## インターフェイス概要",
    ##################################################
    "The `timer_complete` method interface binds a new handler that a timer calls when it is complete. For instance, if the `repeat_count` argument is 100, it calls this handler when a timer count reaches 100 times.": "`timer_complete`メソッドのインターフェイスはタイマーが終了（完了）した際に呼ばれるハンドラを設定します。例えば`repeat_count`の引数に100を設定した場合そのハンドラはタイマーのカウントが100回に到達したタイミングで呼ばれます。",  # noqa
    ##################################################
    "## Basic usage": "## 基本的な使い方",
    ##################################################
    "The `timer_complete` method has the same interface as the other event binding interface (arguments of the `handler` callable and `options` dictionary).": "`timer_complete`メソッドは他のイベント設定のインターフェイスと同様に関数やメソッドのハンドラとしての`handler`の引数とハンドラに渡すオプションのパラメーターとしての`options`引数の辞書を受け付けます。",  # noqa
    ##################################################
    "The following example starts the first timer (rotating the left-side rectangle) when you click the rectangle. If that one completes, then the second timer starts:": "以下のコード例では四角をクリックした際に1つ目の左側の四角に対する回転設定用のタイマーを開始しています。1つ目のタイマーが終了したタイミングで2つ目のタイマーを開始しています:",  # noqa
    ##################################################
    '```py\n# runnable\nfrom typing_extensions import TypedDict\n\nimport apysc as ap\n\n\nclass _RectsOptions(TypedDict):\n    rectangle_1: ap.Rectangle\n    rectangle_2: ap.Rectangle\n\n\nclass _RectOptions(TypedDict):\n    rectangle: ap.Rectangle\n\n\ndef on_click(e: ap.MouseEvent[ap.Sprite], options: _RectsOptions) -> None:\n    """\n    The handler that a rectangle calls when clicked.\n\n    Parameters\n    ----------\n    e : ap.MouseEvent\n        Event instance.\n    options : dict\n        Optional arguments dictionary.\n    """\n    e.this.unbind_click(on_click)\n    rectangle_1: ap.Rectangle = options["rectangle_1"]\n    rectangle_2: ap.Rectangle = options["rectangle_2"]\n    options_: _RectOptions = {"rectangle": rectangle_1}\n    timer_1: ap.Timer = ap.Timer(\n        handler=on_timer, delay=ap.FPS.FPS_60, repeat_count=90, options=options_\n    )\n    options_ = {"rectangle": rectangle_2}\n    timer_1.timer_complete(handler=on_timer_1_complete, options=options_)\n    timer_1.start()\n\n\ndef on_timer(e: ap.TimerEvent, options: _RectOptions) -> None:\n    """\n    The handler that a timer calls.\n\n    Parameters\n    ----------\n    e : ap.TimerEvent\n        Event instance.\n    options : dict\n        Optional arguments dictionary.\n    """\n    rectangle: ap.Rectangle = options["rectangle"]\n    rectangle.rotation_around_center += 1\n\n\ndef on_timer_1_complete(e: ap.TimerEvent, options: _RectOptions) -> None:\n    """\n    The handler that the first time calls when completed.\n\n    Parameters\n    ----------\n    e : ap.TimerEvent\n        Event instance.\n    options : dict\n        Optional arguments dictionary.\n    """\n    rectangle_2: ap.Rectangle = options["rectangle"]\n    options_: _RectOptions = {"rectangle": rectangle_2}\n    timer_2: ap.Timer = ap.Timer(\n        handler=on_timer, delay=ap.FPS.FPS_60, repeat_count=90, options=options_\n    )\n    timer_2.start()\n\n\nap.Stage(\n    stage_width=250, stage_height=150, background_color="#333", stage_elem_id="stage"\n)\nsprite: ap.Sprite = ap.Sprite()\nsprite.graphics.begin_fill(color="#0af")\n\nrectangle_1: ap.Rectangle = sprite.graphics.draw_rect(x=50, y=50, width=50, height=50)\nrectangle_2: ap.Rectangle = sprite.graphics.draw_rect(x=150, y=50, width=50, height=50)\noptions: _RectsOptions = {"rectangle_1": rectangle_1, "rectangle_2": rectangle_2}\nsprite.click(handler=on_click, options=options)\n\nap.save_overall_html(dest_dir_path="timer_complete_basic_usage/")\n```': '```py\n# runnable\nfrom typing_extensions import TypedDict\n\nimport apysc as ap\n\n\nclass _RectsOptions(TypedDict):\n    rectangle_1: ap.Rectangle\n    rectangle_2: ap.Rectangle\n\n\nclass _RectOptions(TypedDict):\n    rectangle: ap.Rectangle\n\n\ndef on_click(e: ap.MouseEvent[ap.Sprite], options: _RectsOptions) -> None:\n    """\n    The handler that a rectangle calls when clicked.\n\n    Parameters\n    ----------\n    e : ap.MouseEvent\n        Event instance.\n    options : dict\n        Optional arguments dictionary.\n    """\n    e.this.unbind_click(on_click)\n    rectangle_1: ap.Rectangle = options["rectangle_1"]\n    rectangle_2: ap.Rectangle = options["rectangle_2"]\n    options_: _RectOptions = {"rectangle": rectangle_1}\n    timer_1: ap.Timer = ap.Timer(\n        handler=on_timer, delay=ap.FPS.FPS_60, repeat_count=90, options=options_\n    )\n    options_ = {"rectangle": rectangle_2}\n    timer_1.timer_complete(handler=on_timer_1_complete, options=options_)\n    timer_1.start()\n\n\ndef on_timer(e: ap.TimerEvent, options: _RectOptions) -> None:\n    """\n    The handler that a timer calls.\n\n    Parameters\n    ----------\n    e : ap.TimerEvent\n        Event instance.\n    options : dict\n        Optional arguments dictionary.\n    """\n    rectangle: ap.Rectangle = options["rectangle"]\n    rectangle.rotation_around_center += 1\n\n\ndef on_timer_1_complete(e: ap.TimerEvent, options: _RectOptions) -> None:\n    """\n    The handler that the first time calls when completed.\n\n    Parameters\n    ----------\n    e : ap.TimerEvent\n        Event instance.\n    options : dict\n        Optional arguments dictionary.\n    """\n    rectangle_2: ap.Rectangle = options["rectangle"]\n    options_: _RectOptions = {"rectangle": rectangle_2}\n    timer_2: ap.Timer = ap.Timer(\n        handler=on_timer, delay=ap.FPS.FPS_60, repeat_count=90, options=options_\n    )\n    timer_2.start()\n\n\nap.Stage(\n    stage_width=250, stage_height=150, background_color="#333", stage_elem_id="stage"\n)\nsprite: ap.Sprite = ap.Sprite()\nsprite.graphics.begin_fill(color="#0af")\n\nrectangle_1: ap.Rectangle = sprite.graphics.draw_rect(x=50, y=50, width=50, height=50)\nrectangle_2: ap.Rectangle = sprite.graphics.draw_rect(x=150, y=50, width=50, height=50)\noptions: _RectsOptions = {"rectangle_1": rectangle_1, "rectangle_2": rectangle_2}\nsprite.click(handler=on_click, options=options)\n\nap.save_overall_html(dest_dir_path="timer_complete_basic_usage/")\n```',  # noqa
    ##################################################
    "## timer_complete API": "## timer_complete API",
    ##################################################
    '<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>': '<span class="inconspicuous-txt">特記事項: このAPIドキュメントはドキュメントビルド用のスクリプトによって自動で生成・同期されています。そのためもしかしたらこの節の内容は前節までの内容と重複している場合があります。</span>',  # noqa
    ##################################################
    "**[Interface summary]**": "**[インターフェイス概要]**",
    ##################################################
    "Add a timer complete event listener setting.<hr>": "タイマー終了時のイベントハンドラの設定を追加します。<hr>",  # noqa
    ##################################################
    "**[Parameters]**": "**[引数]**",
    ##################################################
    "- `handler`: _Handler": "- `handler`: _Handler",
    ##################################################
    "  - A callable that a timer calls when complete.": "  - タイマー終了時に呼ばれる関数もしくはメソッド。",
    ##################################################
    "- `options`: dict or None, default None": "- `options`: dict or None, default None",  # noqa
    ##################################################
    "  - Optional arguments dictionary to be passed to a handler.": "  - ハンドラに渡される省略が可能な追加のパラメーターとしての辞書。",  # noqa
    ##################################################
    "<hr>": "<hr>",
    ##################################################
    "**[Returns]**": "**[返却値]**",
    ##################################################
    "- `name`: str": "- `name`: str",
    ##################################################
    "  - Handler's name.": "  - ハンドラ名。",
    ##################################################
    "<hr>": "<hr>",
    ##################################################
    "**[Examples]**": "**[コードサンプル]**",
    ##################################################
    '```py\n>>> from typing_extensions import TypedDict\n>>> import apysc as ap\n>>> class RectOptions(TypedDict):\n...     rectangle: ap.Rectangle\n...\n>>> def on_timer(e: ap.TimerEvent, options: RectOptions) -> None:\n...     rectangle: ap.Rectangle = options["rectangle"]\n...     rectangle.x += 1\n>>> def on_timer_complete(e: ap.TimerEvent, options: RectOptions) -> None:\n...     ap.trace("Timer completed!")\n>>> stage: ap.Stage = ap.Stage()\n>>> sprite: ap.Sprite = ap.Sprite()\n>>> sprite.graphics.begin_fill(color="#0af")\n>>> rectangle: ap.Rectangle = sprite.graphics.draw_rect(\n...     x=50, y=50, width=50, height=50\n... )\n>>> options: RectOptions = {"rectangle": rectangle}\n>>> timer: ap.Timer = ap.Timer(on_timer, delay=33.3, options=options)\n>>> _ = timer.timer_complete(on_timer_complete)\n>>> timer.start()\n```': '```py\n>>> from typing_extensions import TypedDict\n>>> import apysc as ap\n>>> class RectOptions(TypedDict):\n...     rectangle: ap.Rectangle\n...\n>>> def on_timer(e: ap.TimerEvent, options: RectOptions) -> None:\n...     rectangle: ap.Rectangle = options["rectangle"]\n...     rectangle.x += 1\n>>> def on_timer_complete(e: ap.TimerEvent, options: RectOptions) -> None:\n...     ap.trace("Timer completed!")\n>>> stage: ap.Stage = ap.Stage()\n>>> sprite: ap.Sprite = ap.Sprite()\n>>> sprite.graphics.begin_fill(color="#0af")\n>>> rectangle: ap.Rectangle = sprite.graphics.draw_rect(\n...     x=50, y=50, width=50, height=50\n... )\n>>> options: RectOptions = {"rectangle": rectangle}\n>>> timer: ap.Timer = ap.Timer(on_timer, delay=33.3, options=options)\n>>> _ = timer.timer_complete(on_timer_complete)\n>>> timer.start()\n```',  # noqa
    ##################################################
    "<hr>": "<hr>",
    ##################################################
    "**[References]**": "**[関連資料]**",
    ##################################################
    "- [About the handler options' type](https://simon-ritchie.github.io/apysc/en/about_handler_options_type.html)": "- [ハンドラのoptions引数の型について](https://simon-ritchie.github.io/apysc/jp/jp_about_handler_options_type.html)",  # noqa
}
