"""This module is for the translation mapping data of the
following document:

Document file: timer_repeat_count.md
Language: jp
"""

from typing import Dict

MAPPING: Dict[str, str] = {
    ##################################################
    "# Timer class repeat_count setting": "# Timer クラスの repeat_count 設定",
    ##################################################
    "This page explains the `Timer` class `repeat_count` argument setting.": "このページでは`Timer`クラスの`repeat_count`引数の設定について説明します。",  # noqa
    ##################################################
    "## What argument is this?": "## 引数の概要",
    ##################################################
    "The `repeat_count` argument setting determines the max handler calling number. For example, if you specify the 10 value, a timer calls the handler 10 times and stops.": "`repeat_count`引数の設定ではハンドラが呼ばれる最大数を設定できます。例えば、もし10を指定した場合タイマーは10回ハンドラを呼び出した後に停止します。",  # noqa
    ##################################################
    "## Basic usage": "## 基本的な使い方",
    ##################################################
    "You can set the `repeat_count` parameter at the `Timer` constructor. The following example sets the timer with the 100 times `repeat_count` value when clicking the rectangle.": "`Timer`クラスのコンストラクタにて`repeat_count`引数のパラメーターを設定することができます。以下のコード例では四角をクリックした際に`repeat_count`の値が100のタイマーを設定しています。",  # noqa
    ##################################################
    "If the timer moves the rectangle 100 times (100-pixels to the right), the timer stops.": "もしタイマーがハンドラ内で四角を100回分動かした場合（100px分右に動いた場合）タイマーは停止します。",  # noqa
    ##################################################
    '```py\n# runnable\nfrom typing_extensions import TypedDict\n\nimport apysc as ap\n\n\nclass _RectOptions(TypedDict):\n    rectangle: ap.Rectangle\n\n\ndef on_rectangle_click(e: ap.MouseEvent[ap.Rectangle], options: dict) -> None:\n    """\n    The handler that a rectangle calls when clicked.\n\n    Parameters\n    ----------\n    e : ap.MouseEvent\n        Event instance.\n    options : dict\n        Optional arguments dictionary.\n    """\n    options_: _RectOptions = {"rectangle": e.this}\n    timer: ap.Timer = ap.Timer(\n        handler=on_timer, delay=16, repeat_count=100, options=options_\n    )\n    timer.start()\n    e.this.unbind_click(handler=on_rectangle_click)\n\n\ndef on_timer(e: ap.TimerEvent, options: _RectOptions) -> None:\n    """\n    The handler that a timer calls.\n\n    Parameters\n    ----------\n    e : ap.TimerEvent\n        Event instance.\n    options : dict\n        Optional arguments dictionary.\n    """\n    rectangle: ap.Rectangle = options["rectangle"]\n    rectangle.x += 1\n\n\nap.Stage(\n    stage_width=250,\n    stage_height=150,\n    background_color=ap.Color("#333"),\n    stage_elem_id="stage",\n)\nsprite: ap.Sprite = ap.Sprite()\nsprite.graphics.begin_fill(color=ap.Color("#0af"))\nrectangle: ap.Rectangle = sprite.graphics.draw_rect(x=50, y=50, width=50, height=50)\nrectangle.click(on_rectangle_click)\n\nap.save_overall_html(dest_dir_path="timer_repeat_count_basic_usage/")\n```': '```py\n# runnable\nfrom typing_extensions import TypedDict\n\nimport apysc as ap\n\n\nclass _RectOptions(TypedDict):\n    rectangle: ap.Rectangle\n\n\ndef on_rectangle_click(e: ap.MouseEvent[ap.Rectangle], options: dict) -> None:\n    """\n    The handler that a rectangle calls when clicked.\n\n    Parameters\n    ----------\n    e : ap.MouseEvent\n        Event instance.\n    options : dict\n        Optional arguments dictionary.\n    """\n    options_: _RectOptions = {"rectangle": e.this}\n    timer: ap.Timer = ap.Timer(\n        handler=on_timer, delay=16, repeat_count=100, options=options_\n    )\n    timer.start()\n    e.this.unbind_click(handler=on_rectangle_click)\n\n\ndef on_timer(e: ap.TimerEvent, options: _RectOptions) -> None:\n    """\n    The handler that a timer calls.\n\n    Parameters\n    ----------\n    e : ap.TimerEvent\n        Event instance.\n    options : dict\n        Optional arguments dictionary.\n    """\n    rectangle: ap.Rectangle = options["rectangle"]\n    rectangle.x += 1\n\n\nap.Stage(\n    stage_width=250,\n    stage_height=150,\n    background_color=ap.Color("#333"),\n    stage_elem_id="stage",\n)\nsprite: ap.Sprite = ap.Sprite()\nsprite.graphics.begin_fill(color=ap.Color("#0af"))\nrectangle: ap.Rectangle = sprite.graphics.draw_rect(x=50, y=50, width=50, height=50)\nrectangle.click(on_rectangle_click)\n\nap.save_overall_html(dest_dir_path="timer_repeat_count_basic_usage/")\n```',  # noqa
    ##################################################
    "## Timer constructor API": "## Timer クラスのコンストラクタのAPI",
    ##################################################
    '<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>': '<span class="inconspicuous-txt">特記事項: このAPIドキュメントはドキュメントビルド用のスクリプトによって自動で生成・同期されています。そのためもしかしたらこの節の内容は前節までの内容と重複している場合があります。</span>',  # noqa
    ##################################################
    "**[Interface summary]**": "**[インターフェイス概要]**",
    ##################################################
    "Timer class to handle function calling at regular intervals.<hr>": "一定間隔ごとにハンドラの関数を実行するためのタイマーのクラスです。<hr>",  # noqa
    ##################################################
    "**[Parameters]**": "**[引数]**",
    ##################################################
    "- `handler`: _Handler": "- `handler`: _Handler",
    ##################################################
    "  - A handler would be called at regular intervals.": "  - 一定間隔ごとに呼ばれる関数もしくはメソッドのハンドラ。",  # noqa
    ##################################################
    "- `delay`: Int or int or Number or float or FPS": "- `delay`: Int or int or Number or float or FPS",  # noqa
    ##################################################
    "  - A delay between each `Handler` calling in a millisecond or FPS value. If an `FPS` value is specified, this value becomes a millisecond calculated with that FPS value (e.g., if the `FPS_60` value is specified, then `delay` becomes 16.6666667).": "  - ハンドラの実行間隔となるミリ秒もしくはFPSのenumの値。もし`FPS`の値が指定された場合、FPSに応じて計算されたミリ秒が設定されます（例えば、もし`FPS_60`が指定されていれば`delay`の値は16.6666667ミリ秒相当になります。）。",  # noqa
    ##################################################
    "- `repeat_count`: Int or int": "- `repeat_count`: Int or int",
    ##################################################
    "  - Max count of a `Handler`'s calling. A timer stops if the `Handler`'s calling count has reached this value. If 0 is specified, then a timer loops forever.": "  - ハンドラの実行回数の上限値。ハンドラの実行回数がこの値に到達した場合タイマーは停止します。もし0が指定された場合にはタイマーは停止しなくなります。",  # noqa
    ##################################################
    "- `options`: dict or None, default None": "- `options`: dict or None, default None",  # noqa
    ##################################################
    "  - Optional arguments dictionary to pass a `Handler` callable.": "  - ハンドラの関数もしくはメソッドへ渡すオプションとしての各パラメーターを格納した辞書。",  # noqa
    ##################################################
    "<hr>": "<hr>",
    ##################################################
    "**[Examples]**": "**[コードサンプル]**",
    ##################################################
    '```py\n>>> from typing_extensions import TypedDict\n>>> import apysc as ap\n>>> _ = ap.Stage()\n>>> class RectOptions(TypedDict):\n...     rectangle: ap.Rectangle\n...\n>>> def on_timer(e: ap.TimerEvent, options: RectOptions) -> None:\n...     rectangle: ap.Rectangle = options["rectangle"]\n...     rectangle.x += 1\n>>> stage: ap.Stage = ap.Stage()\n>>> sprite: ap.Sprite = ap.Sprite()\n>>> sprite.graphics.begin_fill(color=ap.Color("#0af"))\n>>> rectangle: ap.Rectangle = sprite.graphics.draw_rect(\n...     x=50, y=50, width=50, height=50\n... )\n>>> options: RectOptions = {"rectangle": rectangle}\n>>> _ = ap.Timer(on_timer, delay=ap.FPS.FPS_60, options=options).start()\n```': '```py\n>>> from typing_extensions import TypedDict\n>>> import apysc as ap\n>>> _ = ap.Stage()\n>>> class RectOptions(TypedDict):\n...     rectangle: ap.Rectangle\n...\n>>> def on_timer(e: ap.TimerEvent, options: RectOptions) -> None:\n...     rectangle: ap.Rectangle = options["rectangle"]\n...     rectangle.x += 1\n>>> stage: ap.Stage = ap.Stage()\n>>> sprite: ap.Sprite = ap.Sprite()\n>>> sprite.graphics.begin_fill(color=ap.Color("#0af"))\n>>> rectangle: ap.Rectangle = sprite.graphics.draw_rect(\n...     x=50, y=50, width=50, height=50\n... )\n>>> options: RectOptions = {"rectangle": rectangle}\n>>> _ = ap.Timer(on_timer, delay=ap.FPS.FPS_60, options=options).start()\n```',  # noqa
    ##################################################
    "<hr>": "<hr>",
    ##################################################
    "**[References]**": "**[関連資料]**",
    ##################################################
    "- [Timer](https://simon-ritchie.github.io/apysc/en/timer.html)": "- [Timer クラス](https://simon-ritchie.github.io/apysc/jp/jp_timer.html)",  # noqa
    ##################################################
    "- [TimerEvent class](https://simon-ritchie.github.io/apysc/en/timer_event.html)": "- [TimerEvent クラス](https://simon-ritchie.github.io/apysc/jp/jp_timer_event.html)",  # noqa
    ##################################################
    "- [Timer class delay setting](https://simon-ritchie.github.io/apysc/en/timer_delay.html)": "- [Timer クラスの delay 設定](https://simon-ritchie.github.io/apysc/jp/jp_timer_delay.html)",  # noqa
    ##################################################
    "- [FPS enum](https://simon-ritchie.github.io/apysc/en/fps.html)": "- [FPS の enum](https://simon-ritchie.github.io/apysc/jp/jp_fps.html)",  # noqa
    ##################################################
    "- [About the handler options' type](https://simon-ritchie.github.io/apysc/en/about_handler_options_type.html)": "- [ハンドラのoptions引数の型について](https://simon-ritchie.github.io/apysc/jp/jp_about_handler_options_type.html)",  # noqa
    ##################################################
    "## repeat_count property API": "## repeat_count 属性のAPI",
    ##################################################
    '<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>': '<span class="inconspicuous-txt">特記事項: このAPIドキュメントはドキュメントビルド用のスクリプトによって自動で生成・同期されています。そのためもしかしたらこの節の内容は前節までの内容と重複している場合があります。</span>',  # noqa
    ##################################################
    "**[Interface summary]**": "**[インターフェイス概要]**",
    ##################################################
    "Get a max count value of a handler's calling.<hr>": "ハンドラが呼ばれる最大数を取得します。<hr>",
    ##################################################
    "**[Returns]**": "**[返却値]**",
    ##################################################
    "- `repeat_count`: Int": "- `repeat_count`: Int",
    ##################################################
    "  - Max count of a handler's calling. If this value is 0, then a timer loop forever.": "  - ハンドラの呼び出しの上限回数。もし0が指定された場合、タイマーはずっと実行され続けます（ハンドラを呼び続けます）。",  # noqa
    ##################################################
    "<hr>": "<hr>",
    ##################################################
    "**[Examples]**": "**[コードサンプル]**",
    ##################################################
    "```py\n>>> import apysc as ap\n>>> _ = ap.Stage()\n>>> def on_timer(e: ap.TimerEvent, options: dict) -> None:\n...     pass\n>>> timer: ap.Timer = ap.Timer(on_timer, delay=33.3, repeat_count=50)\n>>> timer.repeat_count\nInt(50)\n```": "```py\n>>> import apysc as ap\n>>> _ = ap.Stage()\n>>> def on_timer(e: ap.TimerEvent, options: dict) -> None:\n...     pass\n>>> timer: ap.Timer = ap.Timer(on_timer, delay=33.3, repeat_count=50)\n>>> timer.repeat_count\nInt(50)\n```",  # noqa
}
