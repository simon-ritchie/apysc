"""This module is for the translation mapping data of the
following document:

Document file: timer_delay.md
Language: jp
"""

from typing import Dict

MAPPING: Dict[str, str] = {
    ##################################################
    "# Timer class delay setting": "# Timer クラスの delay 設定",
    ##################################################
    "This page explains the `Timer` class `delay` argument setting.": "このページでは`Timer`クラスの`delay`引数の設定について説明します。",  # noqa
    ##################################################
    "## What argument is this?": "## 引数の概要",
    ##################################################
    "The `delay` argument setting determines the timer tick interval. This setting is a milliseconds unit, so a value of 1000 ticks every 1 second.": "`delay`引数の設定ではタイマーの間隔を設定できます。この設定はミリ秒単位となり、1000の値を指定すれば1秒ごとの間隔になります。",  # noqa
    ##################################################
    "The `int`\\, `float`\\, `Int`\\, `Number`\\, and `FPS` enum can be acceptable.": "この引数は`int`、`float`、`Int`、`Number`型の値、もしくは`FPS`のenumの値を受け付けます。",  # noqa
    ##################################################
    "## Basic usage": "## 基本的な使い方",
    ##################################################
    "You can set the `delay` parameter at the `Timer` class constructor. The following example sets each timer (`timer_1`, `timer_2`, `timer_3`) and passes the delay values of `100`, `333.3333333`, `16.6666667`.": "`Timer`クラスのコンストラクタで`deplay`引数のパラメーターを設定することができます。以下のコード例では`timer_1`、`timer_2`、`timer_3`の3つのタイマーを生成し、それぞれdelayの値に`100`、`33.3333333`、`16.6666667`の各値を設定しています。",  # noqa
    ##################################################
    "The first-timer (`delay` is 100) is called 10 times in a second, and the second one (`delay` is 33.3333333) is 30 times in a second, and the third one (`delay` is 16.6666667) is 60 times.": "1番目のタイマー（`delay`の値は100）では1秒間に10回ハンドラの呼び出しを行い、2番目のタイマー（`delay`の値は33.3333333）では1秒間に30回の呼び出しを行い、3番目のタイマー（`delay`の値は16.6666667）では60回の呼び出しを行います。",  # noqa
    ##################################################
    '```py\n# runnable\nfrom typing_extensions import TypedDict\n\nimport apysc as ap\n\nap.Stage(\n    stage_width=350, stage_height=150, background_color="#333", stage_elem_id="stage"\n)\nsprite: ap.Sprite = ap.Sprite()\n\nsprite.graphics.begin_fill(color="#0af")\nrectangle_1: ap.Rectangle = sprite.graphics.draw_rect(x=50, y=50, width=50, height=50)\nrectangle_2: ap.Rectangle = sprite.graphics.draw_rect(x=150, y=50, width=50, height=50)\nrectangle_3: ap.Rectangle = sprite.graphics.draw_rect(x=250, y=50, width=50, height=50)\n\n\nclass _RectOptions(TypedDict):\n    rectangle: ap.Rectangle\n\n\ndef on_timer(e: ap.TimerEvent, options: _RectOptions) -> None:\n    """\n    The Handler would be called every timer tick.\n\n    Parameters\n    ----------\n    e : ap.TimerEvent\n        Event instance.\n    options : dict\n        Optional arguments dictionary.\n    """\n    rectangle: ap.Rectangle = options["rectangle"]\n    rectangle.rotation_around_center += 1\n\n\noptions: _RectOptions = {"rectangle": rectangle_1}\ntimer_1: ap.Timer = ap.Timer(handler=on_timer, delay=100, options=options)\ntimer_1.start()\n\noptions = {"rectangle": rectangle_2}\ntimer_2: ap.Timer = ap.Timer(handler=on_timer, delay=33.3333333, options=options)\ntimer_2.start()\n\noptions = {"rectangle": rectangle_3}\ntimer_3: ap.Timer = ap.Timer(handler=on_timer, delay=16.6666667, options=options)\ntimer_3.start()\n\nap.save_overall_html(dest_dir_path="timer_delay_basic_usage/")\n```': '```py\n# runnable\nfrom typing_extensions import TypedDict\n\nimport apysc as ap\n\nap.Stage(\n    stage_width=350, stage_height=150, background_color="#333", stage_elem_id="stage"\n)\nsprite: ap.Sprite = ap.Sprite()\n\nsprite.graphics.begin_fill(color="#0af")\nrectangle_1: ap.Rectangle = sprite.graphics.draw_rect(x=50, y=50, width=50, height=50)\nrectangle_2: ap.Rectangle = sprite.graphics.draw_rect(x=150, y=50, width=50, height=50)\nrectangle_3: ap.Rectangle = sprite.graphics.draw_rect(x=250, y=50, width=50, height=50)\n\n\nclass _RectOptions(TypedDict):\n    rectangle: ap.Rectangle\n\n\ndef on_timer(e: ap.TimerEvent, options: _RectOptions) -> None:\n    """\n    The Handler would be called every timer tick.\n\n    Parameters\n    ----------\n    e : ap.TimerEvent\n        Event instance.\n    options : dict\n        Optional arguments dictionary.\n    """\n    rectangle: ap.Rectangle = options["rectangle"]\n    rectangle.rotation_around_center += 1\n\n\noptions: _RectOptions = {"rectangle": rectangle_1}\ntimer_1: ap.Timer = ap.Timer(handler=on_timer, delay=100, options=options)\ntimer_1.start()\n\noptions = {"rectangle": rectangle_2}\ntimer_2: ap.Timer = ap.Timer(handler=on_timer, delay=33.3333333, options=options)\ntimer_2.start()\n\noptions = {"rectangle": rectangle_3}\ntimer_3: ap.Timer = ap.Timer(handler=on_timer, delay=16.6666667, options=options)\ntimer_3.start()\n\nap.save_overall_html(dest_dir_path="timer_delay_basic_usage/")\n```',  # noqa
    ##################################################
    "## Set the FPS enum value to the delay argument": "## delay 引数にFPSのenumの値を設定する",
    ##################################################
    "You can also pass the `FPS` (frames per second) enum value to the `delay` argument. For example, if the `FPS.FPS_60` is specified, a timer delay becomes 60 frames per second (16.6666667 milliseconds). Likely, the `FPS.FPS_30` is specified, a timer delay becomes 30 frames per second (33.3333333 milliseconds).": "`delay`の引数には`FPS`（frames per second / 1秒当たりのフレーム数）のenumの値を指定することもできます。例えば、`FPS.FPS_60`を指定すれば60FPS相当の実行回数（16.6666667ミリ秒ごとの実行）となります。同様に`FPS.FPS_30`を指定すれば30FPS相当（33.3333333ミリ秒ごとの実行）となります。",  # noqa
    ##################################################
    '```py\n# runnable\nfrom typing_extensions import TypedDict\n\nimport apysc as ap\n\nap.Stage(\n    stage_width=150, stage_height=150, background_color="#333", stage_elem_id="stage"\n)\nsprite: ap.Sprite = ap.Sprite()\nsprite.graphics.begin_fill(color="#0af")\nrectangle: ap.Rectangle = sprite.graphics.draw_rect(x=50, y=50, width=50, height=50)\n\n\nclass _RectOptions(TypedDict):\n    rectangle: ap.Rectangle\n\n\ndef on_timer(e: ap.TimerEvent, options: _RectOptions) -> None:\n    """\n    The Handler would be called every timer tick.\n\n    Parameters\n    ----------\n    e : ap.TimerEvent\n        Event instance.\n    options : dict\n        Optional arguments dictionary.\n    """\n    rectangle: ap.Rectangle = options["rectangle"]\n    rectangle.rotation_around_center += 1\n\n\noptions: _RectOptions = {"rectangle": rectangle}\ntimer: ap.Timer = ap.Timer(handler=on_timer, delay=ap.FPS.FPS_60, options=options)\ntimer.start()\n\nap.save_overall_html(dest_dir_path="timer_delay_fps_enum/")\n```': '```py\n# runnable\nfrom typing_extensions import TypedDict\n\nimport apysc as ap\n\nap.Stage(\n    stage_width=150, stage_height=150, background_color="#333", stage_elem_id="stage"\n)\nsprite: ap.Sprite = ap.Sprite()\nsprite.graphics.begin_fill(color="#0af")\nrectangle: ap.Rectangle = sprite.graphics.draw_rect(x=50, y=50, width=50, height=50)\n\n\nclass _RectOptions(TypedDict):\n    rectangle: ap.Rectangle\n\n\ndef on_timer(e: ap.TimerEvent, options: _RectOptions) -> None:\n    """\n    The Handler would be called every timer tick.\n\n    Parameters\n    ----------\n    e : ap.TimerEvent\n        Event instance.\n    options : dict\n        Optional arguments dictionary.\n    """\n    rectangle: ap.Rectangle = options["rectangle"]\n    rectangle.rotation_around_center += 1\n\n\noptions: _RectOptions = {"rectangle": rectangle}\ntimer: ap.Timer = ap.Timer(handler=on_timer, delay=ap.FPS.FPS_60, options=options)\ntimer.start()\n\nap.save_overall_html(dest_dir_path="timer_delay_fps_enum/")\n```',  # noqa
    ##################################################
    "## See also": "## 関連資料",
    ##################################################
    "- [FPS enum](fps.md)": "- [FPS の enum](jp_fps.md)",
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
    "- [Timer](https://simon-ritchie.github.io/apysc/en/timer.html)": "- [Timer クラス](https://simon-ritchie.github.io/apysc/jp/jp_timer.html)",  # noqa
    ##################################################
    "- [TimerEvent class](https://simon-ritchie.github.io/apysc/en/timer_event.html)": "- [TimerEvent クラス](https://simon-ritchie.github.io/apysc/jp/jp_timer_event.html)",  # noqa
    ##################################################
    "- [FPS enum](https://simon-ritchie.github.io/apysc/en/fps.html)": "- [FPS の enum](https://simon-ritchie.github.io/apysc/jp/jp_fps.html)",  # noqa
    ##################################################
    "- [Timer class repeat_count setting](https://simon-ritchie.github.io/apysc/en/timer_repeat_count.html)": "- [Timer クラスの repeat_count 設定](https://simon-ritchie.github.io/apysc/jp/jp_timer_repeat_count.html)",  # noqa
    ##################################################
    "- [About the handler options' type](https://simon-ritchie.github.io/apysc/en/about_handler_options_type.html)": "- [ハンドラのoptions引数の型について](https://simon-ritchie.github.io/apysc/jp/jp_about_handler_options_type.html)",  # noqa
    ##################################################
    "## delay property API": "## delay 属性のAPI",
    ##################################################
    '<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>': '<span class="inconspicuous-txt">特記事項: このAPIドキュメントはドキュメントビルド用のスクリプトによって自動で生成・同期されています。そのためもしかしたらこの節の内容は前節までの内容と重複している場合があります。</span>',  # noqa
    ##################################################
    "**[Interface summary]**": "**[インターフェイス概要]**",
    ##################################################
    "Get a delay value.<hr>": "遅延（間隔）値を取得します。<hr>",
    ##################################################
    "**[Returns]**": "**[返却値]**",
    ##################################################
    "- `delay`: Number": "- `delay`: Number",
    ##################################################
    "  - A delay value of each `Handler` calling in milliseconds.": "  - ハンドラの実行ごとのミリ秒の間隔値。",  # noqa
    ##################################################
    "<hr>": "<hr>",
    ##################################################
    "**[Examples]**": "**[コードサンプル]**",
    ##################################################
    "```py\n>>> import apysc as ap\n>>> def on_timer(e: ap.TimerEvent, options: dict) -> None:\n...     pass\n>>> timer: ap.Timer = ap.Timer(on_timer, delay=33.3, repeat_count=50)\n>>> timer.delay\nNumber(33.3)\n```": "```py\n>>> import apysc as ap\n>>> def on_timer(e: ap.TimerEvent, options: dict) -> None:\n...     pass\n>>> timer: ap.Timer = ap.Timer(on_timer, delay=33.3, repeat_count=50)\n>>> timer.delay\nNumber(33.3)\n```",  # noqa
}
