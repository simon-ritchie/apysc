"""This module is for the translation mapping data of the
following document:

Document file: fps.md
Language: jp
"""

from typing import Dict

MAPPING: Dict[str, str] = {
    ##################################################
    "# FPS enum": "# FPS の enum",
    ##################################################
    "This page explains the `FPS` enum class.": "このページでは`FPS`のenumのクラスについて説明します。",
    ##################################################
    "## What class is this?": "## クラス概要",
    ##################################################
    "The `FPS` enum class is the definition of each FPS (frames per second). The timer uses this enum to determine the timer tick interval.": "`FPS`のenumのクラスは各FPS（frames per second）の定義です。タイマーが実行間隔を決めるために主にこのenumを使用しています。",  # noqa
    ##################################################
    "## Basic usage": "## 基本的な使い方",
    ##################################################
    "There is an enum definition of FPS in 5 intervals. The `Timer` class `delay` argument is an acceptable `FPS` enum value. For example, specify the `FPS.FPS_60` value to that argument. A timer interval becomes approximately `16.6666667` milliseconds. Similarly, it becomes `33.3333333` milliseconds when you specify the `FPS.FPS_30` value.": "FPSのenumの定義は5間隔（15, 20, 25, 30等）で存在します。`Timer`クラスの`delay`引数は`FPS`のenumの値を受け付けることができます。例えば`FPS.FPS_60`の値を`delay`引数に指定した場合、タイマーの間隔は約`16.6666667`ミリ秒ごととなります。同じように`FPS.FPS_30`を指定すると`33.3333333`ミリ秒ごとの間隔となります。",  # noqa
    ##################################################
    '```py\n# runnable\nfrom typing_extensions import TypedDict\n\nimport apysc as ap\n\n\nclass _RectOptions(TypedDict):\n    rectangle: ap.Rectangle\n\n\ndef on_timer(e: ap.TimerEvent, options: _RectOptions) -> None:\n    """\n    The handler that the timer calls.\n\n    Parameters\n    ----------\n    e : ap.TimerEvent\n        Event instance.\n    options : dict\n        Optional arguments dictionary.\n    """\n    rectangle: ap.Rectangle = options["rectangle"]\n    rectangle.rotation_around_center += 1\n\n\nap.Stage(\n    stage_width=350,\n    stage_height=150,\n    background_color=ap.Color("#333"),\n    stage_elem_id="stage",\n)\nsprite: ap.Sprite = ap.Sprite()\nsprite.graphics.begin_fill(color=ap.Color("#0af"))\n\nrectangle_1: ap.Rectangle = sprite.graphics.draw_rect(x=50, y=50, width=50, height=50)\noptions: _RectOptions = {"rectangle": rectangle_1}\ntimer_1: ap.Timer = ap.Timer(handler=on_timer, delay=ap.FPS.FPS_10, options=options)\ntimer_1.start()\n\nrectangle_2: ap.Rectangle = sprite.graphics.draw_rect(x=150, y=50, width=50, height=50)\noptions = {"rectangle": rectangle_2}\ntimer_2: ap.Timer = ap.Timer(handler=on_timer, delay=ap.FPS.FPS_30, options=options)\ntimer_2.start()\n\nrectangle_3: ap.Rectangle = sprite.graphics.draw_rect(x=250, y=50, width=50, height=50)\noptions = {"rectangle": rectangle_3}\ntimer_3: ap.Timer = ap.Timer(handler=on_timer, delay=ap.FPS.FPS_60, options=options)\ntimer_3.start()\n\nap.save_overall_html(dest_dir_path="fps_basic_usage/")\n```': '```py\n# runnable\nfrom typing_extensions import TypedDict\n\nimport apysc as ap\n\n\nclass _RectOptions(TypedDict):\n    rectangle: ap.Rectangle\n\n\ndef on_timer(e: ap.TimerEvent, options: _RectOptions) -> None:\n    """\n    The handler that the timer calls.\n\n    Parameters\n    ----------\n    e : ap.TimerEvent\n        Event instance.\n    options : dict\n        Optional arguments dictionary.\n    """\n    rectangle: ap.Rectangle = options["rectangle"]\n    rectangle.rotation_around_center += 1\n\n\nap.Stage(\n    stage_width=350,\n    stage_height=150,\n    background_color=ap.Color("#333"),\n    stage_elem_id="stage",\n)\nsprite: ap.Sprite = ap.Sprite()\nsprite.graphics.begin_fill(color=ap.Color("#0af"))\n\nrectangle_1: ap.Rectangle = sprite.graphics.draw_rect(x=50, y=50, width=50, height=50)\noptions: _RectOptions = {"rectangle": rectangle_1}\ntimer_1: ap.Timer = ap.Timer(handler=on_timer, delay=ap.FPS.FPS_10, options=options)\ntimer_1.start()\n\nrectangle_2: ap.Rectangle = sprite.graphics.draw_rect(x=150, y=50, width=50, height=50)\noptions = {"rectangle": rectangle_2}\ntimer_2: ap.Timer = ap.Timer(handler=on_timer, delay=ap.FPS.FPS_30, options=options)\ntimer_2.start()\n\nrectangle_3: ap.Rectangle = sprite.graphics.draw_rect(x=250, y=50, width=50, height=50)\noptions = {"rectangle": rectangle_3}\ntimer_3: ap.Timer = ap.Timer(handler=on_timer, delay=ap.FPS.FPS_60, options=options)\ntimer_3.start()\n\nap.save_overall_html(dest_dir_path="fps_basic_usage/")\n```',  # noqa
    ##################################################
    "## See also": "## 関連資料",
    ##################################################
    "- [Timer class delay setting](timer_delay.md)": "- [Timer クラスの delay 設定](jp_timer_delay.md)",  # noqa
}
