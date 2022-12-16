"""This module is for the translation mapping data of the
following document:

Document file: timer.md
Language: jp
"""

from typing import Dict

MAPPING: Dict[str, str] = {
    ##################################################
    "# Timer class": "# Timer クラス",
    ##################################################
    "This page explains the `Timer` class.": "このページでは`Timer`クラスについて説明します。",
    ##################################################
    "## What is the Timer?": "## Timer クラスの概要",
    ##################################################
    "The `Timer` class handles the timer's tick. You can call a handler at any intervals by it.": "`Timer`クラスは一定間隔で処理を実行するためのタイマーの処理を扱います。任意の間隔を設定してハンドラの呼び出し設定を追加することができます。",  # noqa
    ##################################################
    "## Basic usage": "## 基本的な使い方",
    ##################################################
    "The `Timer` class requires arguments for the `handler` and `delay` (timer interval in milliseconds). And the `start` method starts that timer. A timer passes the `TimerEvent` instance and options arguments to a specified handler.": "`Timer`クラスはコンストラクタでハンドラとしての`handler`引数とタイマー実行間隔のミリ秒としての`delay`引数の指定を必要とします。そして`start`メソッドを呼び出すとタイマーがスタートします。タイマーは`TimerEvent`クラスのインスタンスとオプションとして指定できる追加のパラメーターの引数をハンドラへ渡します。",  # noqa
    ##################################################
    "The following code sets the `Timer` when clicking the rectangle (`Sprite`):": "以下のコード例では四角（`Sprite`）をクリックした際に`Timer`クラスを使用した設定を行っています:",  # noqa
    ##################################################
    '```py\n# runnable\nfrom typing_extensions import TypedDict\n\nimport apysc as ap\n\n\nclass _RectOptions(TypedDict):\n    rectangle: ap.Rectangle\n\n\ndef on_sprite_click(e: ap.MouseEvent[ap.Sprite], options: _RectOptions) -> None:\n    """\n    The Handler that the rectangle calls when clicked.\n\n    Parameters\n    ----------\n    e : MouseEvent\n        Event instance.\n    options : dict\n        Optional arguments dictionary.\n    """\n    e.this.unbind_click_all()\n    timer: ap.Timer = ap.Timer(on_timer, delay=16.6, options=options)\n    timer.start()\n\n\ndef on_timer(e: ap.TimerEvent, options: _RectOptions) -> None:\n    """\n    The Handler a timer calls.\n\n    Parameters\n    ----------\n    e : TimerEvent\n        Event instance.\n    options : dict\n        Optional arguments dictionary.\n    """\n    rectangle: ap.Rectangle = options["rectangle"]\n    rectangle.x += 1\n\n\nap.Stage(\n    stage_width=350, stage_height=150, background_color="#333", stage_elem_id="stage"\n)\nsprite: ap.Sprite = ap.Sprite()\nsprite.graphics.begin_fill(color="#0af")\nrectangle: ap.Rectangle = sprite.graphics.draw_rect(x=50, y=50, width=50, height=50)\noptions: _RectOptions = {"rectangle": rectangle}\nsprite.click(on_sprite_click, options=options)\n\nap.save_overall_html(dest_dir_path="timer_basic_usage/")\n```': '```py\n# runnable\nfrom typing_extensions import TypedDict\n\nimport apysc as ap\n\n\nclass _RectOptions(TypedDict):\n    rectangle: ap.Rectangle\n\n\ndef on_sprite_click(e: ap.MouseEvent[ap.Sprite], options: _RectOptions) -> None:\n    """\n    The Handler that the rectangle calls when clicked.\n\n    Parameters\n    ----------\n    e : MouseEvent\n        Event instance.\n    options : dict\n        Optional arguments dictionary.\n    """\n    e.this.unbind_click_all()\n    timer: ap.Timer = ap.Timer(on_timer, delay=16.6, options=options)\n    timer.start()\n\n\ndef on_timer(e: ap.TimerEvent, options: _RectOptions) -> None:\n    """\n    The Handler a timer calls.\n\n    Parameters\n    ----------\n    e : TimerEvent\n        Event instance.\n    options : dict\n        Optional arguments dictionary.\n    """\n    rectangle: ap.Rectangle = options["rectangle"]\n    rectangle.x += 1\n\n\nap.Stage(\n    stage_width=350, stage_height=150, background_color="#333", stage_elem_id="stage"\n)\nsprite: ap.Sprite = ap.Sprite()\nsprite.graphics.begin_fill(color="#0af")\nrectangle: ap.Rectangle = sprite.graphics.draw_rect(x=50, y=50, width=50, height=50)\noptions: _RectOptions = {"rectangle": rectangle}\nsprite.click(on_sprite_click, options=options)\n\nap.save_overall_html(dest_dir_path="timer_basic_usage/")\n```',  # noqa
    ##################################################
    "If you click the rectangle, the timer starts, and the Handler increases the rectangle x value.": "四角をクリックするとタイマーがスタートし、タイマーのハンドラは四角のX座標を加算していきます。",  # noqa
    ##################################################
    "## See also": "## 関連資料",
    ##################################################
    "- [TimerEvent class](timer_event.md)": "- [TimerEvent クラス](jp_timer_event.md)",
    ##################################################
    "- [Timer class delay setting](timer_delay.md)": "- [Timer クラスの delay 設定](jp_timer_delay.md)",  # noqa
    ##################################################
    "- [FPS enum](fps.md)": "- [FPS の enum](jp_fps.md)",
    ##################################################
    "- [Timer class repeat_count setting](timer_repeat_count.md)": "- [Timer クラスの repeat_count 設定](jp_timer_repeat_count.md)",  # noqa
    ##################################################
    "- [Timer class start and stop interfaces](timer_start_and_stop.md)": "- [Timer クラスの start と stop の各インターフェイス](jp_timer_start_and_stop.md)",  # noqa
    ##################################################
    "- [Timer class timer_complete interface](timer_complete.md)": "- [Timer クラスの timer_complete インターフェイス](jp_timer_complete.md)",  # noqa
    ##################################################
    "- [Timer class reset interface](timer_reset.md)": "- [Timer クラスの reset インターフェイス](jp_timer_reset.md)",  # noqa
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
    '```py\n>>> from typing_extensions import TypedDict\n>>> import apysc as ap\n>>> class RectOptions(TypedDict):\n...     rectangle: ap.Rectangle\n...\n>>> def on_timer(e: ap.TimerEvent, options: RectOptions) -> None:\n...     rectangle: ap.Rectangle = options["rectangle"]\n...     rectangle.x += 1\n>>> stage: ap.Stage = ap.Stage()\n>>> sprite: ap.Sprite = ap.Sprite()\n>>> sprite.graphics.begin_fill(color="#0af")\n>>> rectangle: ap.Rectangle = sprite.graphics.draw_rect(\n...     x=50, y=50, width=50, height=50\n... )\n>>> options: RectOptions = {"rectangle": rectangle}\n>>> _ = ap.Timer(on_timer, delay=ap.FPS.FPS_60, options=options).start()\n```': '```py\n>>> from typing_extensions import TypedDict\n>>> import apysc as ap\n>>> class RectOptions(TypedDict):\n...     rectangle: ap.Rectangle\n...\n>>> def on_timer(e: ap.TimerEvent, options: RectOptions) -> None:\n...     rectangle: ap.Rectangle = options["rectangle"]\n...     rectangle.x += 1\n>>> stage: ap.Stage = ap.Stage()\n>>> sprite: ap.Sprite = ap.Sprite()\n>>> sprite.graphics.begin_fill(color="#0af")\n>>> rectangle: ap.Rectangle = sprite.graphics.draw_rect(\n...     x=50, y=50, width=50, height=50\n... )\n>>> options: RectOptions = {"rectangle": rectangle}\n>>> _ = ap.Timer(on_timer, delay=ap.FPS.FPS_60, options=options).start()\n```',  # noqa
    ##################################################
    "<hr>": "<hr>",
    ##################################################
    "**[References]**": "**[関連資料]**",
    ##################################################
    "- [TimerEvent class](https://simon-ritchie.github.io/apysc/en/timer_event.html)": "- [TimerEvent クラス](https://simon-ritchie.github.io/apysc/jp/jp_timer_event.html)",  # noqa
    ##################################################
    "- [Timer class delay setting](https://simon-ritchie.github.io/apysc/en/timer_delay.html)": "- [Timer クラスの delay 設定](https://simon-ritchie.github.io/apysc/jp/jp_timer_delay.html)",  # noqa
    ##################################################
    "- [FPS enum](https://simon-ritchie.github.io/apysc/en/fps.html)": "- [FPS の enum](https://simon-ritchie.github.io/apysc/jp/jp_fps.html)",  # noqa
    ##################################################
    "- [Timer class repeat_count setting](https://simon-ritchie.github.io/apysc/en/timer_repeat_count.html)": "- [Timer クラスの repeat_count 設定](https://simon-ritchie.github.io/apysc/jp/jp_timer_repeat_count.html)",  # noqa
    ##################################################
    "- [About the handler options' type](https://simon-ritchie.github.io/apysc/en/about_handler_options_type.html)": "- [ハンドラのoptions引数の型について](https://simon-ritchie.github.io/apysc/jp/jp_about_handler_options_type.html)",  # noqa
}
