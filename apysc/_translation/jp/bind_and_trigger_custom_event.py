"""This module is for the translation mapping data of the
following document:

Document file: bind_and_trigger_custom_event.md
Language: jp
"""

from typing import Dict

MAPPING: Dict[str, str] = {
    ##################################################
    "# Bind and trigger the custom event":
    "# カスタムイベントの登録とイベントの発生（発火）制御",
    ##################################################
    "This page explains the `bind_custom_event` and `trigger_custom_event` interfaces.":  # noqa
    "このページでは`bind_custom_event`と`trigger_custom_event`の各インターフェイスについて説明します。",
    ##################################################
    "## What interfaces are these?":
    "## 各インターフェイスの概要",
    ##################################################
    "The `bind_custom_event` interface registers your custom event to the instance, and the `trigger_custom_event` one triggers the registered custom events at any time.":  # noqa
    "`bind_custom_event`インターフェイスは対象のインスタンスに独自のイベントを登録し、`trigger_custom_event`インターフェイスは任意の箇所でカスタムイベントの発生（発火）の制御を行います。",  # noqa
    ##################################################
    "## Basic usage":
    "## 基本的な使い方",
    ##################################################
    "The `bind_custom_event` interface has the `custom_event_type`, `handler`, `e`, and `options` arguments (`options` is optional).":  # noqa
    "`bind_custom_event`インターフェイスは`custom_event_type`と`handler`、`e`、そして`options`引数を持っています（`options`引数は省略可です）。",  # noqa
    ##################################################
    "The `custom_event_type` argument is the custom event type name\'s string. This value needs to specify the same one at the calling of the `trigger_custom_event` interface.":  # noqa
    "`custom_event_type`引数は独自のイベントの種類の文字列です。この引数の文字列は`trigger_custom_event`インターフェイスでの指定時でも同じ値を設定する必要があります。",  # noqa
    ##################################################
    "The `e` argument is an event instance that may become the subclass of the `Event` class, such as the `MouseEvent` or `TimerEvent`\\.":  # noqa
    "`e`引数はイベントのインスタンスです。場合によっては`MouseEvent`クラスや`TimerEvent`クラスなどの`Event`クラスのサブクラスを指定します。",  # noqa
    ##################################################
    "The following example rotates the rectangle when you click it. If the rectangle rotated 90 degrees, then the custom event (`rotate_90_degrees`) is triggered, and the `on_rotate_90_degrees` handler (custom event) is called and display the second rectangle (toggle the `visible` property):":  # noqa
    "以下のコード例では四角をクリックした際に回転させるようにしています。もし回転量が90度に達した場合、`rotate_90_degrees`の独自のイベントが発生し`on_rotate_90_degrees`関数のハンドラが実行されます。対象のハンドラ内では2つ目の四角を`visible`属性を有効化する形で表示しています。",  # noqa
    ##################################################
    "```py\n# runnable\nfrom typing_extensions import TypedDict\n\nimport apysc as ap\n\n# Custom event type name.\nROTATE_90_DEGREES: str = \'rotate_90_degrees\'\n\n\nclass _RectOptions(TypedDict):\n    rectangle: ap.Rectangle\n\n\ndef on_rectangle_click(\n        e: ap.MouseEvent[ap.Rectangle], options: dict) -> None:\n    \"\"\"\n    The handler that the rectangle calls when clicked.\n\n    Parameters\n    ----------\n    e : ap.MouseEvent\n        Event instance.\n    options : dict\n        Optional arguments dictionary.\n    \"\"\"\n    e.this.unbind_click(on_rectangle_click)\n    options_: _RectOptions = {\'rectangle\': e.this}\n    timer: ap.Timer = ap.Timer(\n        on_timer, delay=ap.FPS.FPS_60, repeat_count=90,\n        options=options_)\n    timer.timer_complete(\n        on_timer_complete,\n        options=options_)\n    timer.start()\n\n\ndef on_timer(e: ap.TimerEvent, options: _RectOptions) -> None:\n    \"\"\"\n    The handler that the timer calls.\n\n    Parameters\n    ----------\n    e : ap.TimerEvent\n        Event instance.\n    options : dict\n        Optional arguments dictionary.\n    \"\"\"\n    rectangle: ap.Rectangle = options[\'rectangle\']\n    rectangle.rotation_around_center += 1\n\n\ndef on_timer_complete(e: ap.TimerEvent, options: _RectOptions) -> None:\n    \"\"\"\n    The handler that timer calls when its end.\n\n    Parameters\n    ----------\n    e : ap.TimerEvent\n        Event instance.\n    options : dict\n        Optional arguments dictionary.\n    \"\"\"\n    rectangle: ap.Rectangle = options[\'rectangle\']\n    rectangle.trigger_custom_event(custom_event_type=ROTATE_90_DEGREES)\n\n\ndef on_rotate_90_degrees(e: ap.Event, options: _RectOptions) -> None:\n    \"\"\"\n    The handler that the rectangle rates 90 degrees (custom event).\n\n    Parameters\n    ----------\n    e : ap.Event\n        Event instance.\n    options : dict\n        Optional arguments dictionary.\n    \"\"\"\n    rectangle: ap.Rectangle = options[\'rectangle\']\n    rectangle.visible = ap.Boolean(True)\n\n\nap.Stage(\n    stage_width=250, stage_height=150, background_color=\'#333\',\n    stage_elem_id=\'stage\')\nsprite: ap.Sprite = ap.Sprite()\nsprite.graphics.begin_fill(color=\'#0af\')\n\nrectangle_1: ap.Rectangle = sprite.graphics.draw_rect(\n    x=50, y=50, width=50, height=50)\nrectangle_1.click(on_rectangle_click)\nrectangle_2: ap.Rectangle = sprite.graphics.draw_rect(\n    x=150, y=50, width=50, height=50)\nrectangle_2.visible = ap.Boolean(False)\n\ne: ap.Event = ap.Event(this=rectangle_1)\nrectangle_1.bind_custom_event(\n    custom_event_type=ROTATE_90_DEGREES, handler=on_rotate_90_degrees, e=e,\n    options={\'rectangle\': rectangle_2})\n\nap.save_overall_html(\n    dest_dir_path=\'bind_and_trigger_custom_event_basic_usage/\')\n```":  # noqa
    "```py\n# runnable\nfrom typing_extensions import TypedDict\n\nimport apysc as ap\n\n# Custom event type name.\nROTATE_90_DEGREES: str = \'rotate_90_degrees\'\n\n\nclass _RectOptions(TypedDict):\n    rectangle: ap.Rectangle\n\n\ndef on_rectangle_click(\n        e: ap.MouseEvent[ap.Rectangle], options: dict) -> None:\n    \"\"\"\n    The handler that the rectangle calls when clicked.\n\n    Parameters\n    ----------\n    e : ap.MouseEvent\n        Event instance.\n    options : dict\n        Optional arguments dictionary.\n    \"\"\"\n    e.this.unbind_click(on_rectangle_click)\n    options_: _RectOptions = {\'rectangle\': e.this}\n    timer: ap.Timer = ap.Timer(\n        on_timer, delay=ap.FPS.FPS_60, repeat_count=90,\n        options=options_)\n    timer.timer_complete(\n        on_timer_complete,\n        options=options_)\n    timer.start()\n\n\ndef on_timer(e: ap.TimerEvent, options: _RectOptions) -> None:\n    \"\"\"\n    The handler that the timer calls.\n\n    Parameters\n    ----------\n    e : ap.TimerEvent\n        Event instance.\n    options : dict\n        Optional arguments dictionary.\n    \"\"\"\n    rectangle: ap.Rectangle = options[\'rectangle\']\n    rectangle.rotation_around_center += 1\n\n\ndef on_timer_complete(e: ap.TimerEvent, options: _RectOptions) -> None:\n    \"\"\"\n    The handler that timer calls when its end.\n\n    Parameters\n    ----------\n    e : ap.TimerEvent\n        Event instance.\n    options : dict\n        Optional arguments dictionary.\n    \"\"\"\n    rectangle: ap.Rectangle = options[\'rectangle\']\n    rectangle.trigger_custom_event(custom_event_type=ROTATE_90_DEGREES)\n\n\ndef on_rotate_90_degrees(e: ap.Event, options: _RectOptions) -> None:\n    \"\"\"\n    The handler that the rectangle rates 90 degrees (custom event).\n\n    Parameters\n    ----------\n    e : ap.Event\n        Event instance.\n    options : dict\n        Optional arguments dictionary.\n    \"\"\"\n    rectangle: ap.Rectangle = options[\'rectangle\']\n    rectangle.visible = ap.Boolean(True)\n\n\nap.Stage(\n    stage_width=250, stage_height=150, background_color=\'#333\',\n    stage_elem_id=\'stage\')\nsprite: ap.Sprite = ap.Sprite()\nsprite.graphics.begin_fill(color=\'#0af\')\n\nrectangle_1: ap.Rectangle = sprite.graphics.draw_rect(\n    x=50, y=50, width=50, height=50)\nrectangle_1.click(on_rectangle_click)\nrectangle_2: ap.Rectangle = sprite.graphics.draw_rect(\n    x=150, y=50, width=50, height=50)\nrectangle_2.visible = ap.Boolean(False)\n\ne: ap.Event = ap.Event(this=rectangle_1)\nrectangle_1.bind_custom_event(\n    custom_event_type=ROTATE_90_DEGREES, handler=on_rotate_90_degrees, e=e,\n    options={\'rectangle\': rectangle_2})\n\nap.save_overall_html(\n    dest_dir_path=\'bind_and_trigger_custom_event_basic_usage/\')\n```",  # noqa
    ##################################################
    "## bind_custom_event API":
    "## bind_custom_event API",
    ##################################################
    "<span class=\"inconspicuous-txt\">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>":  # noqa
    "<span class=\"inconspicuous-txt\">特記事項: このAPIドキュメントはドキュメントビルド用のスクリプトによって自動で生成・同期されています。そのためもしかしたらこの節の内容は前節までの内容と重複している場合があります。</span>",  # noqa
    ##################################################
    "**[Interface summary]** Add a custom event listener setting.<hr>":
    "**[インターフェイス概要]** 独自のイベント設定を追加します。<hr>",
    ##################################################
    "**[Parameters]**":
    "**[引数]**",
    ##################################################
    "- `custom_event_type`: CustomEventType or str":
    "- `custom_event_type`: CustomEventType or str",
    ##################################################
    "  - Target custom event type.":
    "  - 対象の独自のイベントの種別値としての文字列。",
    ##################################################
    "- `handler`: _Handler":
    "- `handler`: _Handler",
    ##################################################
    "  - Callable that this instance calls when its event\'s dispatching.":
    "  - 対象のイベントが発生（発火）される時に実行されるハンドラ。",
    ##################################################
    "- `e`: Event":
    "- `e`: Event",
    ##################################################
    "  - Event instance.":
    "  - イベントのインスタンス。",
    ##################################################
    "- `options`: dict or None, default None":
    "- `options`: dict or None, default None",
    ##################################################
    "  - Optional arguments dictionary to be passed to a handler.":
    "  - ハンドラに渡される省略が可能な追加のパラメーターとしての辞書。",
    ##################################################
    "- `in_handler_head_expression`: str, default \'\'":
    "- `in_handler_head_expression`: str, default \'\'",
    ##################################################
    "  - Optional expression to be added at the handler function\'s head position.":
    "  - 省略可能なハンドラ内の先頭に加える（JavaScriptの）表現の文字列。",
    ##################################################
    "<hr>":
    "<hr>",
    ##################################################
    "**[Returns]**":
    "**[返却値]**",
    ##################################################
    "- `name`: str":
    "- `name`: str",
    ##################################################
    "  - Handler\'s name.":
    "  - ハンドラ名。",
    ##################################################
    "<hr>":
    "<hr>",
    ##################################################
    "**[Examples]**":
    "**[コードサンプル]**",
    ##################################################
    "```py\n>>> import apysc as ap\n>>> def on_custom_event(\n...         e: ap.Event[ap.Rectangle], options: dict) -> None:\n...     rectangle: ap.Rectangle = e.this\n...     rectangle.fill_color = ap.String(\'#f0a\')\n>>> stage: ap.Stage = ap.Stage()\n>>> sprite: ap.Sprite = ap.Sprite()\n>>> sprite.graphics.begin_fill(color=\'#0af\')\n>>> rectangle: ap.Rectangle = sprite.graphics.draw_rect(\n...     x=50, y=50, width=50, height=50)\n>>> e: ap.Event = ap.Event(this=rectangle)\n>>> _ = rectangle.bind_custom_event(\n...     custom_event_type=\'my_custom_event\',\n...     handler=on_custom_event, e=e)\n>>> # Do something here and then trigger the custom event\n>>> rectangle.trigger_custom_event(\n...     custom_event_type=\'my_custom_event\')\n```":  # noqa
    "```py\n>>> import apysc as ap\n>>> def on_custom_event(\n...         e: ap.Event[ap.Rectangle], options: dict) -> None:\n...     rectangle: ap.Rectangle = e.this\n...     rectangle.fill_color = ap.String(\'#f0a\')\n>>> stage: ap.Stage = ap.Stage()\n>>> sprite: ap.Sprite = ap.Sprite()\n>>> sprite.graphics.begin_fill(color=\'#0af\')\n>>> rectangle: ap.Rectangle = sprite.graphics.draw_rect(\n...     x=50, y=50, width=50, height=50)\n>>> e: ap.Event = ap.Event(this=rectangle)\n>>> _ = rectangle.bind_custom_event(\n...     custom_event_type=\'my_custom_event\',\n...     handler=on_custom_event, e=e)\n>>> # Do something here and then trigger the custom event\n>>> rectangle.trigger_custom_event(\n...     custom_event_type=\'my_custom_event\')\n```",  # noqa
    ##################################################
    "<hr>":
    "<hr>",
    ##################################################
    "**[References]**":
    "**[関連資料]**",
    ##################################################
    "- [About the handler options\' type document](https://simon-ritchie.github.io/apysc/en/about_handler_options_type.html)":  # noqa
    "- [ハンドラのoptions引数の型について](https://simon-ritchie.github.io/apysc/en/jp_about_handler_options_type.html)",  # noqa
    ##################################################
    "## trigger_custom_event API":
    "## trigger_custom_event API",
    ##################################################
    "<span class=\"inconspicuous-txt\">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>":  # noqa
    "<span class=\"inconspicuous-txt\">特記事項: このAPIドキュメントはドキュメントビルド用のスクリプトによって自動で生成・同期されています。そのためもしかしたらこの節の内容は前節までの内容と重複している場合があります。</span>",  # noqa
    ##################################################
    "**[Interface summary]** Add a custom event trigger setting.<hr>":
    "**[インターフェイス概要]** 独自のイベントの発生（発火）制御の設定を追加します。<hr>",
    ##################################################
    "**[Parameters]**":
    "**[引数]**",
    ##################################################
    "- `custom_event_type`: CustomEventType or str":
    "- `custom_event_type`: CustomEventType or str",
    ##################################################
    "  - Target custom event type.":
    "  - 対象の独自のイベントの種別値としての文字列。",
    ##################################################
    "<hr>":
    "<hr>",
    ##################################################
    "**[Examples]**":
    "**[コードサンプル]**",
    ##################################################
    "```py\n>>> import apysc as ap\n>>> def on_custom_event(\n...         e: ap.Event[ap.Rectangle], options: dict) -> None:\n...     rectangle: ap.Rectangle = e.this\n...     rectangle.fill_color = ap.String(\'#f0a\')\n>>> stage: ap.Stage = ap.Stage()\n>>> sprite: ap.Sprite = ap.Sprite()\n>>> sprite.graphics.begin_fill(color=\'#0af\')\n>>> rectangle: ap.Rectangle = sprite.graphics.draw_rect(\n...     x=50, y=50, width=50, height=50)\n>>> e: ap.Event = ap.Event(this=rectangle)\n>>> _ = rectangle.bind_custom_event(\n...     custom_event_type=\'my_custom_event\',\n...     handler=on_custom_event, e=e)\n>>> # Do something here and then trigger the custom event\n>>> rectangle.trigger_custom_event(\n...     custom_event_type=\'my_custom_event\')\n```":  # noqa
    "```py\n>>> import apysc as ap\n>>> def on_custom_event(\n...         e: ap.Event[ap.Rectangle], options: dict) -> None:\n...     rectangle: ap.Rectangle = e.this\n...     rectangle.fill_color = ap.String(\'#f0a\')\n>>> stage: ap.Stage = ap.Stage()\n>>> sprite: ap.Sprite = ap.Sprite()\n>>> sprite.graphics.begin_fill(color=\'#0af\')\n>>> rectangle: ap.Rectangle = sprite.graphics.draw_rect(\n...     x=50, y=50, width=50, height=50)\n>>> e: ap.Event = ap.Event(this=rectangle)\n>>> _ = rectangle.bind_custom_event(\n...     custom_event_type=\'my_custom_event\',\n...     handler=on_custom_event, e=e)\n>>> # Do something here and then trigger the custom event\n>>> rectangle.trigger_custom_event(\n...     custom_event_type=\'my_custom_event\')\n```",  # noqa
}
