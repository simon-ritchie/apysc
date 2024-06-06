"""This module is for the translation mapping data of the
following document:

Document file: animation_delay.md
Language: jp
"""

from typing import Dict

MAPPING: Dict[str, str] = {
    ##################################################
    "# Animation interfaces delay setting": "# 各アニメーションのインターフェイスのdelayの設定",
    ##################################################
    "This page explains the animation interfaces `delay` setting.": "このページでは各アニメーションのインターフェイスの`delay`の設定について説明します。",  # noqa
    ##################################################
    "## What setting is this?": "## 設定概要",
    ##################################################
    "The `delay` setting determines the delay time before the animation starts. For instance, if you specify 3000 to the `delay` argument, the animation starts after 3 seconds after.": "`delay`の設定はアニメーション開始前の遅延時間を値を設定することができます。たとえば`delay`の引数に3000を指定すればアニメーションは3秒後に開始します。",  # noqa
    ##################################################
    "Each animation method interface (such as the `animation_move`, `animation_x`, and so on) has the `delay`'s argument.": "`animation_move`や`animation_x`などの各アニメーションのインターフェイスはこの`delay`引数を持っています。",  # noqa
    ##################################################
    "## Basic usage": "## 基本的な使い方",
    ##################################################
    "The following example sets 2 seconds between each x-coordinate animation (pause 2 seconds before animation starts):": "以下の例では各X座標のアニメーション間で2秒の遅延設定(delay)を行っています。2秒間停止してからアニメーションが開始します。",  # noqa
    ##################################################
    '```py\n# runnable\nimport apysc as ap\n\nDURATION: int = 3000\nDELAY: int = 2000\nEASING: ap.Easing = ap.Easing.EASE_OUT_QUINT\n\n\ndef on_animation_complete_1(e: ap.AnimationEvent[ap.Rectangle], options: dict) -> None:\n    """\n    The handler that animation calls when its end.\n\n    Parameters\n    ----------\n    e : ap.AnimationEvent\n        Event instance.\n    options : dict\n        Optional arguments dictionary.\n    """\n    rectangle: ap.Rectangle = e.this.target\n    animation_x: ap.AnimationX = rectangle.animation_x(\n        x=50, duration=DURATION, delay=DELAY, easing=EASING\n    )\n    animation_x.animation_complete(on_animation_complete_2)\n    animation_x.start()\n\n\ndef on_animation_complete_2(e: ap.AnimationEvent[ap.Rectangle], options: dict) -> None:\n    """\n    The handler that animation calls when its end.\n\n    Parameters\n    ----------\n    e : ap.AnimationEvent\n        Event instance.\n    options : dict\n        Optional arguments dictionary.\n    """\n    rectangle: ap.Rectangle = e.this.target\n    animation_x: ap.AnimationX = rectangle.animation_x(\n        x=300, duration=DURATION, delay=DELAY, easing=EASING\n    )\n    animation_x.animation_complete(on_animation_complete_1)\n    animation_x.start()\n\n\nap.Stage(\n    stage_width=400,\n    stage_height=150,\n    background_color=ap.Color("#333"),\n    stage_elem_id="stage",\n)\nsprite: ap.Sprite = ap.Sprite()\nsprite.graphics.begin_fill(color=ap.Color("#0af"))\nrectangle: ap.Rectangle = sprite.graphics.draw_rect(x=50, y=50, width=50, height=50)\n\nanimation_x: ap.AnimationX = rectangle.animation_x(\n    x=300, duration=DURATION, delay=DELAY, easing=EASING\n)\nanimation_x.animation_complete(on_animation_complete_1)\nanimation_x.start()\n\nap.save_overall_html(dest_dir_path="./animation_delay_basic_usage/")\n```': '```py\n# runnable\nimport apysc as ap\n\nDURATION: int = 3000\nDELAY: int = 2000\nEASING: ap.Easing = ap.Easing.EASE_OUT_QUINT\n\n\ndef on_animation_complete_1(e: ap.AnimationEvent[ap.Rectangle], options: dict) -> None:\n    """\n    The handler that animation calls when its end.\n\n    Parameters\n    ----------\n    e : ap.AnimationEvent\n        Event instance.\n    options : dict\n        Optional arguments dictionary.\n    """\n    rectangle: ap.Rectangle = e.this.target\n    animation_x: ap.AnimationX = rectangle.animation_x(\n        x=50, duration=DURATION, delay=DELAY, easing=EASING\n    )\n    animation_x.animation_complete(on_animation_complete_2)\n    animation_x.start()\n\n\ndef on_animation_complete_2(e: ap.AnimationEvent[ap.Rectangle], options: dict) -> None:\n    """\n    The handler that animation calls when its end.\n\n    Parameters\n    ----------\n    e : ap.AnimationEvent\n        Event instance.\n    options : dict\n        Optional arguments dictionary.\n    """\n    rectangle: ap.Rectangle = e.this.target\n    animation_x: ap.AnimationX = rectangle.animation_x(\n        x=300, duration=DURATION, delay=DELAY, easing=EASING\n    )\n    animation_x.animation_complete(on_animation_complete_1)\n    animation_x.start()\n\n\nap.Stage(\n    stage_width=400,\n    stage_height=150,\n    background_color=ap.Color("#333"),\n    stage_elem_id="stage",\n)\nsprite: ap.Sprite = ap.Sprite()\nsprite.graphics.begin_fill(color=ap.Color("#0af"))\nrectangle: ap.Rectangle = sprite.graphics.draw_rect(x=50, y=50, width=50, height=50)\n\nanimation_x: ap.AnimationX = rectangle.animation_x(\n    x=300, duration=DURATION, delay=DELAY, easing=EASING\n)\nanimation_x.animation_complete(on_animation_complete_1)\nanimation_x.start()\n\nap.save_overall_html(dest_dir_path="./animation_delay_basic_usage/")\n```',  # noqa
}
