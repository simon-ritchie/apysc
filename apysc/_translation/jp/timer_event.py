"""This module is for the translation mapping data of the
following document:

Document file: timer_event.md
Language: jp
"""

from typing import Dict

MAPPING: Dict[str, str] = {
    ##################################################
    "# TimerEvent class": "# TimerEvent クラス",
    ##################################################
    "This page explains the `TimerEvent` class.": "このページでは`TimerEvent`クラスについて説明します。",
    ##################################################
    "## What class is this?": "## クラス概要",
    ##################################################
    "The `TimerEvent` class is the event class that a timer passes to a timer event handler function, such as the `Timer` class constructor or the `timer_complete` function\\.": "`TimerEvent`クラスは`Timer`クラスのコンストラクタや`timer_complete`などのインターフェイスで登録されるタイマー関係のイベントのハンドラに渡されるイベントのクラスです。",  # noqa
    ##################################################
    "## Basic usage": "## 基本的な使い方",
    ##################################################
    "Each timer event handler's first argument becomes the `TimerEvent` class instance.": "タイマー関係の各イベントハンドラの第一引数は`TimerEvent`クラスのインスタンスとなります。",  # noqa
    ##################################################
    '```py\n# runnable\nfrom typing_extensions import TypedDict\n\nimport apysc as ap\n\n\nclass _RectOptions(TypedDict):\n    rectangle: ap.Rectangle\n\n\ndef on_timer(e: ap.TimerEvent, options: _RectOptions) -> None:\n    """\n    The handler that the timer calls.\n\n    Parameters\n    ----------\n    e : ap.TimerEvent\n        Event instance.\n    options : dict\n        Optional arguments dictionary.\n    """\n    rectangle: ap.Rectangle = options["rectangle"]\n    rectangle.rotation_around_center += 1\n\n\ndef on_timer_complete(e: ap.TimerEvent, options: dict) -> None:\n    """\n    The handler that the timer calls when completed.\n\n    Parameters\n    ----------\n    e : ap.TimerEvent\n        Event instance.\n    options : dict\n        Optional arguments dictionary.\n    """\n    ap.trace("Timer complete!")\n\n\nap.Stage(\n    stage_width=150,\n    stage_height=150,\n    background_color=ap.Color("#333"),\n    stage_elem_id="stage",\n)\nsprite: ap.Sprite = ap.Sprite()\nsprite.graphics.begin_fill(color=ap.Color("#0af"))\nrectangle: ap.Rectangle = sprite.graphics.draw_rect(x=50, y=50, width=50, height=50)\n\noptions: _RectOptions = {"rectangle": rectangle}\ntimer: ap.Timer = ap.Timer(handler=on_timer, delay=33.3, options=options)\ntimer.start()\ntimer.timer_complete(handler=on_timer_complete)\n\nap.save_overall_html(dest_dir_path="timer_event_basic_usage/")\n```': '```py\n# runnable\nfrom typing_extensions import TypedDict\n\nimport apysc as ap\n\n\nclass _RectOptions(TypedDict):\n    rectangle: ap.Rectangle\n\n\ndef on_timer(e: ap.TimerEvent, options: _RectOptions) -> None:\n    """\n    The handler that the timer calls.\n\n    Parameters\n    ----------\n    e : ap.TimerEvent\n        Event instance.\n    options : dict\n        Optional arguments dictionary.\n    """\n    rectangle: ap.Rectangle = options["rectangle"]\n    rectangle.rotation_around_center += 1\n\n\ndef on_timer_complete(e: ap.TimerEvent, options: dict) -> None:\n    """\n    The handler that the timer calls when completed.\n\n    Parameters\n    ----------\n    e : ap.TimerEvent\n        Event instance.\n    options : dict\n        Optional arguments dictionary.\n    """\n    ap.trace("Timer complete!")\n\n\nap.Stage(\n    stage_width=150,\n    stage_height=150,\n    background_color=ap.Color("#333"),\n    stage_elem_id="stage",\n)\nsprite: ap.Sprite = ap.Sprite()\nsprite.graphics.begin_fill(color=ap.Color("#0af"))\nrectangle: ap.Rectangle = sprite.graphics.draw_rect(x=50, y=50, width=50, height=50)\n\noptions: _RectOptions = {"rectangle": rectangle}\ntimer: ap.Timer = ap.Timer(handler=on_timer, delay=33.3, options=options)\ntimer.start()\ntimer.timer_complete(handler=on_timer_complete)\n\nap.save_overall_html(dest_dir_path="timer_event_basic_usage/")\n```',  # noqa
    ##################################################
    "## this attribute": "## this 属性",
    ##################################################
    "The `TimerEvent` instance's `this` attribute becomes the target `Timer` instance, and you can use each timer instance interface from it.": "`TimerEvent`のインスタンスの`this`属性は対象の`Timer`クラスのインスタンスとなり、ぞれを参照してタイマー関係の各インターフェイスを使用することができます。",  # noqa
    ##################################################
    '```py\n# runnable\nfrom typing_extensions import TypedDict\n\nimport apysc as ap\n\n\nclass _RectOptions(TypedDict):\n    rectangle: ap.Rectangle\n\n\ndef on_timer(e: ap.TimerEvent, options: _RectOptions) -> None:\n    """\n    The handler that the timer calls.\n\n    Parameters\n    ----------\n    e : ap.TimerEvent\n        Event instance.\n    options : dict\n        Optional arguments dictionary.\n    """\n    rectangle: ap.Rectangle = options["rectangle"]\n    rectangle.rotation_around_center += 1\n    ap.trace("Current timer count: ", e.this.current_count)\n\n\nap.Stage(\n    stage_width=150,\n    stage_height=150,\n    background_color=ap.Color("#333"),\n    stage_elem_id="stage",\n)\nsprite: ap.Sprite = ap.Sprite()\nsprite.graphics.begin_fill(color=ap.Color("#0af"))\nrectangle: ap.Rectangle = sprite.graphics.draw_rect(x=50, y=50, width=50, height=50)\n\noptions: _RectOptions = {"rectangle": rectangle}\ntimer: ap.Timer = ap.Timer(handler=on_timer, delay=16.6, options=options)\ntimer.start()\n\nap.save_overall_html(dest_dir_path="timer_event_this_attribute/")\n```': '```py\n# runnable\nfrom typing_extensions import TypedDict\n\nimport apysc as ap\n\n\nclass _RectOptions(TypedDict):\n    rectangle: ap.Rectangle\n\n\ndef on_timer(e: ap.TimerEvent, options: _RectOptions) -> None:\n    """\n    The handler that the timer calls.\n\n    Parameters\n    ----------\n    e : ap.TimerEvent\n        Event instance.\n    options : dict\n        Optional arguments dictionary.\n    """\n    rectangle: ap.Rectangle = options["rectangle"]\n    rectangle.rotation_around_center += 1\n    ap.trace("Current timer count: ", e.this.current_count)\n\n\nap.Stage(\n    stage_width=150,\n    stage_height=150,\n    background_color=ap.Color("#333"),\n    stage_elem_id="stage",\n)\nsprite: ap.Sprite = ap.Sprite()\nsprite.graphics.begin_fill(color=ap.Color("#0af"))\nrectangle: ap.Rectangle = sprite.graphics.draw_rect(x=50, y=50, width=50, height=50)\n\noptions: _RectOptions = {"rectangle": rectangle}\ntimer: ap.Timer = ap.Timer(handler=on_timer, delay=16.6, options=options)\ntimer.start()\n\nap.save_overall_html(dest_dir_path="timer_event_this_attribute/")\n```',  # noqa
    ##################################################
    "## TimerEvent constructor API": "## TimerEvent クラスのコンストラクタのAPI",
    ##################################################
    '<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>': '<span class="inconspicuous-txt">特記事項: このAPIドキュメントはドキュメントビルド用のスクリプトによって自動で生成・同期されています。そのためもしかしたらこの節の内容は前節までの内容と重複している場合があります。</span>',  # noqa
    ##################################################
    "**[Interface summary]**": "**[インターフェイス概要]**",
    ##################################################
    "Timer event class.<hr>": "タイマー関係のイベントのクラスです。<hr>",
    ##################################################
    "**[Parameters]**": "**[引数]**",
    ##################################################
    "- `this`: Timer": "- `this`: Timer",
    ##################################################
    "  - Target timer instance.": "  - 対象のタイマーのインスタンス。",
    ##################################################
    "<hr>": "<hr>",
    ##################################################
    "**[Examples]**": "**[コードサンプル]**",
    ##################################################
    '```py\n>>> from typing_extensions import TypedDict\n>>> import apysc as ap\n>>> class RectOptions(TypedDict):\n...     rectangle: ap.Rectangle\n...\n>>> def on_timer(e: ap.TimerEvent, options: RectOptions) -> None:\n...     rectangle: ap.Rectangle = options["rectangle"]\n...     rectangle.x += 1\n>>> stage: ap.Stage = ap.Stage()\n>>> sprite: ap.Sprite = ap.Sprite()\n>>> sprite.graphics.begin_fill(color=ap.Color("#0af"))\n>>> rectangle: ap.Rectangle = sprite.graphics.draw_rect(\n...     x=50, y=50, width=50, height=50\n... )\n>>> options: RectOptions = {"rectangle": rectangle}\n>>> ap.Timer(\n...     on_timer,\n...     delay=ap.FPS.FPS_60,\n...     options=options,\n... ).start()\n```': '```py\n>>> from typing_extensions import TypedDict\n>>> import apysc as ap\n>>> class RectOptions(TypedDict):\n...     rectangle: ap.Rectangle\n...\n>>> def on_timer(e: ap.TimerEvent, options: RectOptions) -> None:\n...     rectangle: ap.Rectangle = options["rectangle"]\n...     rectangle.x += 1\n>>> stage: ap.Stage = ap.Stage()\n>>> sprite: ap.Sprite = ap.Sprite()\n>>> sprite.graphics.begin_fill(color=ap.Color("#0af"))\n>>> rectangle: ap.Rectangle = sprite.graphics.draw_rect(\n...     x=50, y=50, width=50, height=50\n... )\n>>> options: RectOptions = {"rectangle": rectangle}\n>>> ap.Timer(\n...     on_timer,\n...     delay=ap.FPS.FPS_60,\n...     options=options,\n... ).start()\n```',  # noqa
    ##################################################
    "## this attribute API": "## this 属性のAPI",
    ##################################################
    '<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>': '<span class="inconspicuous-txt">特記事項: このAPIドキュメントはドキュメントビルド用のスクリプトによって自動で生成・同期されています。そのためもしかしたらこの節の内容は前節までの内容と重複している場合があります。</span>',  # noqa
    ##################################################
    "**[Interface summary]**": "**[インターフェイス概要]**",
    ##################################################
    "Get a timer instance of listening to this event.<hr>": "このイベントのハンドラが設定されている対象のタイマーのインスタンス。<hr>",  # noqa
    ##################################################
    "**[Returns]**": "**[返却値]**",
    ##################################################
    "- `this`: TImer": "- `this`: TImer",
    ##################################################
    "  - Instance of listening to this event.": "  - このイベントのハンドラが設定されているインスタンス。",
    ##################################################
    "<hr>": "<hr>",
    ##################################################
    "**[Examples]**": "**[コードサンプル]**",
    ##################################################
    '```py\n>>> from typing_extensions import TypedDict\n>>> import apysc as ap\n>>> class RectOptions(TypedDict):\n...     rectangle: ap.Rectangle\n...\n>>> def on_timer(e: ap.TimerEvent, options: RectOptions) -> None:\n...     rectangle: ap.Rectangle = options["rectangle"]\n...     rectangle.x += 1\n...     with ap.If(rectangle.x >= 100):\n...         timer: ap.Timer = e.this\n...         timer.stop()\n>>> stage: ap.Stage = ap.Stage()\n>>> sprite: ap.Sprite = ap.Sprite()\n>>> sprite.graphics.begin_fill(color=ap.Color("#0af"))\n>>> rectangle: ap.Rectangle = sprite.graphics.draw_rect(\n...     x=50, y=50, width=50, height=50\n... )\n>>> options: RectOptions = {"rectangle": rectangle}\n>>> ap.Timer(\n...     on_timer,\n...     delay=ap.FPS.FPS_60,\n...     options=options,\n... ).start()\n```': '```py\n>>> from typing_extensions import TypedDict\n>>> import apysc as ap\n>>> class RectOptions(TypedDict):\n...     rectangle: ap.Rectangle\n...\n>>> def on_timer(e: ap.TimerEvent, options: RectOptions) -> None:\n...     rectangle: ap.Rectangle = options["rectangle"]\n...     rectangle.x += 1\n...     with ap.If(rectangle.x >= 100):\n...         timer: ap.Timer = e.this\n...         timer.stop()\n>>> stage: ap.Stage = ap.Stage()\n>>> sprite: ap.Sprite = ap.Sprite()\n>>> sprite.graphics.begin_fill(color=ap.Color("#0af"))\n>>> rectangle: ap.Rectangle = sprite.graphics.draw_rect(\n...     x=50, y=50, width=50, height=50\n... )\n>>> options: RectOptions = {"rectangle": rectangle}\n>>> ap.Timer(\n...     on_timer,\n...     delay=ap.FPS.FPS_60,\n...     options=options,\n... ).start()\n```',  # noqa
}
