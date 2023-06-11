"""This module is for the translation mapping data of the
following document:

Document file: animation_complete.md
Language: jp
"""

from typing import Dict

MAPPING: Dict[str, str] = {
    ##################################################
    "# AnimationBase class animation_complete interface": "# AnimationBase クラス animation_complete インターフェイス",  # noqa
    ##################################################
    "This page explains the `AnimationBase` class `animation_complete` method interface.": "このページでは`AnimationBase`クラスの`animation_complete`メソッドのインターフェイスについて説明します。",  # noqa
    ##################################################
    "## What interface is this?": "## インターフェイス概要",
    ##################################################
    "The `animation_complete` method binds a handler that the animation calls when its end.": "`animation_complete`メソッドはアニメーションが終了したときのハンドラを設定します。",  # noqa
    ##################################################
    "The handler's arguments require the event instance (`ap.AnimationEvent`) at the first argument and the options dictionary at the second argument.": "ハンドラの引数には第一引数にイベントのインスタンス（`ap.AnimationEvent`）、第二引数にはオプションのパラメーターとなる辞書が必要になります。",  # noqa
    ##################################################
    "## Basic usage": "## 基本的な使い方",
    ##################################################
    "The `animation_complete` method requires a handler at the first argument and the optional options dictionary at the second argument.": "`animation_complete`メソッドは第一引数にハンドラが必要となり、第二引数にはオプションのパラメーターの辞書を設定することができます。",  # noqa
    ##################################################
    "The following example calls the `animation_complete` method at the x-coordinate animation end. It starts another animation to reset the x-coordinate:": "以下のコード例ではX座標のアニメーション終了時用に`animation_complete`メソッドを読んでハンドラを設定しています。そのハンドラ内ではX座標をリセットするための別のアニメーションを開始しています。",  # noqa
    ##################################################
    '```py\n# runnable\nimport apysc as ap\n\nDURATION: int = 1000\n\n\ndef on_animation_complete_1(e: ap.AnimationEvent[ap.Rectangle], options: dict) -> None:\n    """\n    The handler that animation calls when its end.\n\n    Parameters\n    ----------\n    e : ap.AnimationEvent\n        Event instance.\n    options : dict\n        Optional arguments dictionary.\n    """\n    rectangle: ap.Rectangle = e.this.target\n    animation_x: ap.AnimationX = rectangle.animation_x(x=50, duration=DURATION)\n    animation_x.animation_complete(on_animation_complete_2)\n    animation_x.start()\n\n\ndef on_animation_complete_2(e: ap.AnimationEvent[ap.Rectangle], options: dict) -> None:\n    """\n    The handler that animation calls when its end.\n\n    Parameters\n    ----------\n    e : ap.AnimationEvent\n        Event instance.\n    options : dict\n        Optional arguments dictionary.\n    """\n    rectangle: ap.Rectangle = e.this.target\n    animation_x: ap.AnimationX = rectangle.animation_x(x=100, duration=DURATION)\n    animation_x.animation_complete(on_animation_complete_1)\n    animation_x.start()\n\n\nap.Stage(\n    stage_width=200, stage_height=150, background_color="#333", stage_elem_id="stage"\n)\nsprite: ap.Sprite = ap.Sprite()\nsprite.graphics.begin_fill(color="#0af")\nrectangle: ap.Rectangle = sprite.graphics.draw_rect(x=50, y=50, width=50, height=50)\n\nanimation_x: ap.AnimationX = rectangle.animation_x(x=100, duration=1000)\nanimation_x.animation_complete(on_animation_complete_1)\nanimation_x.start()\n\nap.save_overall_html(dest_dir_path="./animation_complete_basic_usage/")\n```': '```py\n# runnable\nimport apysc as ap\n\nDURATION: int = 1000\n\n\ndef on_animation_complete_1(e: ap.AnimationEvent[ap.Rectangle], options: dict) -> None:\n    """\n    The handler that animation calls when its end.\n\n    Parameters\n    ----------\n    e : ap.AnimationEvent\n        Event instance.\n    options : dict\n        Optional arguments dictionary.\n    """\n    rectangle: ap.Rectangle = e.this.target\n    animation_x: ap.AnimationX = rectangle.animation_x(x=50, duration=DURATION)\n    animation_x.animation_complete(on_animation_complete_2)\n    animation_x.start()\n\n\ndef on_animation_complete_2(e: ap.AnimationEvent[ap.Rectangle], options: dict) -> None:\n    """\n    The handler that animation calls when its end.\n\n    Parameters\n    ----------\n    e : ap.AnimationEvent\n        Event instance.\n    options : dict\n        Optional arguments dictionary.\n    """\n    rectangle: ap.Rectangle = e.this.target\n    animation_x: ap.AnimationX = rectangle.animation_x(x=100, duration=DURATION)\n    animation_x.animation_complete(on_animation_complete_1)\n    animation_x.start()\n\n\nap.Stage(\n    stage_width=200, stage_height=150, background_color="#333", stage_elem_id="stage"\n)\nsprite: ap.Sprite = ap.Sprite()\nsprite.graphics.begin_fill(color="#0af")\nrectangle: ap.Rectangle = sprite.graphics.draw_rect(x=50, y=50, width=50, height=50)\n\nanimation_x: ap.AnimationX = rectangle.animation_x(x=100, duration=1000)\nanimation_x.animation_complete(on_animation_complete_1)\nanimation_x.start()\n\nap.save_overall_html(dest_dir_path="./animation_complete_basic_usage/")\n```',  # noqa
    ##################################################
    "## Notes about the other interface calling order": "## 他のインターフェイスを呼び出す際の特記事項",
    ##################################################
    "You can only call the `animation_complete` before the animation start, so if you call the `animation_complete` method after the `start` method, it raises an exception:": "`animation_complete`メソッドはアニメーション開始前にのみ設定することができます。`start`メソッド呼び出し後に`animation_complete`メソッドを呼び出すとエラーになります。",  # noqa
    ##################################################
    '```py\nimport apysc as ap\n\n\ndef on_animation_complete(e: ap.AnimationEvent[ap.Rectangle], options: dict) -> None:\n    """\n    The handler that animation calls when its end.\n\n    Parameters\n    ----------\n    e : ap.AnimationEvent\n        Event instance.\n    options : dict\n        Optional arguments dictionary.\n    """\n    ap.trace("Animation complete!")\n\n\nap.Stage(\n    stage_width=200, stage_height=200, background_color="#333", stage_elem_id="stage"\n)\nsprite: ap.Sprite = ap.Sprite()\nsprite.graphics.begin_fill(color="#0af")\nrectangle: ap.Rectangle = sprite.graphics.draw_rect(x=50, y=50, width=50, height=50)\n\nanimation_move: ap.AnimationMove = rectangle.animation_move(x=100, y=100, duration=1000)\nanimation_move.start()\nanimation_move.animation_complete(on_animation_complete)\n```': '```py\nimport apysc as ap\n\n\ndef on_animation_complete(e: ap.AnimationEvent[ap.Rectangle], options: dict) -> None:\n    """\n    The handler that animation calls when its end.\n\n    Parameters\n    ----------\n    e : ap.AnimationEvent\n        Event instance.\n    options : dict\n        Optional arguments dictionary.\n    """\n    ap.trace("Animation complete!")\n\n\nap.Stage(\n    stage_width=200, stage_height=200, background_color="#333", stage_elem_id="stage"\n)\nsprite: ap.Sprite = ap.Sprite()\nsprite.graphics.begin_fill(color="#0af")\nrectangle: ap.Rectangle = sprite.graphics.draw_rect(x=50, y=50, width=50, height=50)\n\nanimation_move: ap.AnimationMove = rectangle.animation_move(x=100, y=100, duration=1000)\nanimation_move.start()\nanimation_move.animation_complete(on_animation_complete)\n```',  # noqa
    ##################################################
    "```\nException: This interface can not be called after the animation is started.\n```": "```\nException: This interface can not be called after the animation is started.\n```",  # noqa
    ##################################################
    "The calling of the `animation_complete` method before the `start` method works correctly:": "`start`メソッド呼び出し前に`animation_complete`メソッドを呼び出すことで正常に動作します:",  # noqa
    ##################################################
    '```py\n# runnable\nimport apysc as ap\n\n\ndef on_animation_complete(e: ap.AnimationEvent[ap.Rectangle], options: dict) -> None:\n    """\n    The handler that animation calls when its end.\n\n    Parameters\n    ----------\n    e : ap.AnimationEvent\n        Event instance.\n    options : dict\n        Optional arguments dictionary.\n    """\n    ap.trace("Animation complete!")\n\n\nap.Stage(\n    stage_width=200, stage_height=200, background_color="#333", stage_elem_id="stage"\n)\nsprite: ap.Sprite = ap.Sprite()\nsprite.graphics.begin_fill(color="#0af")\nrectangle: ap.Rectangle = sprite.graphics.draw_rect(x=50, y=50, width=50, height=50)\n\nanimation_move: ap.AnimationMove = rectangle.animation_move(x=100, y=100, duration=1000)\nanimation_move.animation_complete(on_animation_complete)\nanimation_move.start()\n```': '```py\n# runnable\nimport apysc as ap\n\n\ndef on_animation_complete(e: ap.AnimationEvent[ap.Rectangle], options: dict) -> None:\n    """\n    The handler that animation calls when its end.\n\n    Parameters\n    ----------\n    e : ap.AnimationEvent\n        Event instance.\n    options : dict\n        Optional arguments dictionary.\n    """\n    ap.trace("Animation complete!")\n\n\nap.Stage(\n    stage_width=200, stage_height=200, background_color="#333", stage_elem_id="stage"\n)\nsprite: ap.Sprite = ap.Sprite()\nsprite.graphics.begin_fill(color="#0af")\nrectangle: ap.Rectangle = sprite.graphics.draw_rect(x=50, y=50, width=50, height=50)\n\nanimation_move: ap.AnimationMove = rectangle.animation_move(x=100, y=100, duration=1000)\nanimation_move.animation_complete(on_animation_complete)\nanimation_move.start()\n```',  # noqa
    ##################################################
    "## animation_complete API": "## animation_complete API",
    ##################################################
    '<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>': '<span class="inconspicuous-txt">特記事項: このAPIドキュメントはドキュメントビルド用のスクリプトによって自動で生成・同期されています。そのためもしかしたらこの節の内容は前節までの内容と重複している場合があります。</span>',  # noqa
    ##################################################
    "**[Interface summary]**": "**[インターフェイス概要]**",
    ##################################################
    "Add an animation complete event listener setting.<hr>": "アニメーション終了時のイベントリスナーの設定を追加します。<hr>",  # noqa
    ##################################################
    "**[Parameters]**": "**[引数]**",
    ##################################################
    "- `handler`: _Handler": "- `handler`: _Handler",
    ##################################################
    "  - A callable that an instance calls when an animation is complete.": "  - アニメーション終了時に実行される関数もしくはメソッド。",  # noqa
    ##################################################
    "- `options`: dict or None, default None": "- `options`: dict or None, default None",  # noqa
    ##################################################
    "  - Optional arguments dictionary to be passed to a handler.": "  - ハンドラに渡される省略が可能な追加のパラメーターとしての辞書。",  # noqa
    ##################################################
    "<hr>": "<hr>",
    ##################################################
    "**[Returns]**": "**[返却値]**",
    ##################################################
    "- `self`: AnimatonBase": "- `self`: AnimatonBase",
    ##################################################
    "  - This instance.": "  - このインスタンス。",
    ##################################################
    "<hr>": "<hr>",
    ##################################################
    "**[Raises]**": "**[エラー発生条件]**",
    ##################################################
    "- Exception: If calling this interface after an animation starts": "- Exception: もしアニメーション開始後にこのインターフェイスを呼び出している場合。",  # noqa
    ##################################################
    "<hr>": "<hr>",
    ##################################################
    "**[Notes]**": "**[特記事項]**",
    ##################################################
    "This interface can only use before an animation starts<hr>": "このインターフェイスはアニメーション開始前にのみ利用することができます。<hr>",  # noqa
    ##################################################
    "**[Examples]**": "**[コードサンプル]**",
    ##################################################
    '```py\n>>> import apysc as ap\n>>> def on_animation_complete(\n...     e: ap.AnimationEvent[ap.Rectangle], options: dict\n... ) -> None:\n...     ap.trace("Animation completed!")\n>>> stage: ap.Stage = ap.Stage()\n>>> sprite: ap.Sprite = ap.Sprite()\n>>> sprite.graphics.begin_fill(color="#0af")\n>>> rectangle: ap.Rectangle = sprite.graphics.draw_rect(\n...     x=50, y=50, width=50, height=50\n... )\n>>> _ = (\n...     rectangle.animation_x(\n...         x=100,\n...     )\n...     .animation_complete(on_animation_complete)\n...     .start()\n... )\n```': '```py\n>>> import apysc as ap\n>>> def on_animation_complete(\n...     e: ap.AnimationEvent[ap.Rectangle], options: dict\n... ) -> None:\n...     ap.trace("Animation completed!")\n>>> stage: ap.Stage = ap.Stage()\n>>> sprite: ap.Sprite = ap.Sprite()\n>>> sprite.graphics.begin_fill(color="#0af")\n>>> rectangle: ap.Rectangle = sprite.graphics.draw_rect(\n...     x=50, y=50, width=50, height=50\n... )\n>>> _ = (\n...     rectangle.animation_x(\n...         x=100,\n...     )\n...     .animation_complete(on_animation_complete)\n...     .start()\n... )\n```',  # noqa
    ##################################################
    "<hr>": "<hr>",
    ##################################################
    "**[References]**": "**[関連資料]**",
    ##################################################
    "- [About the handler options' type](https://simon-ritchie.github.io/apysc/en/about_handler_options_type.html)": "- [ハンドラのoptions引数の型について](https://simon-ritchie.github.io/apysc/jp/jp_about_handler_options_type.html)",  # noqa
}
