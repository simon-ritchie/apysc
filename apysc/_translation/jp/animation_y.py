"""This module is for the translation mapping data of the
following document:

Document file: animation_y.md
Language: jp
"""

from typing import Dict

MAPPING: Dict[str, str] = {
    ##################################################
    "# animation_y interface": "# animation_y インターフェイス",
    ##################################################
    "This page explains the `animation_y` method interface.": "このページでは`animation_y`メソッドのインターフェイスについて説明します。",  # noqa
    ##################################################
    "## What interface is this?": "## インターフェイス概要",
    ##################################################
    "The `animation_y` method interface creates an `AnimationY` instance. You can animate y-coordinate with it.": "`animation_y`メソッドのインターフェイスは`AnimationY`クラスのインスタンスを生成します。このインスタンスを使ってY座標のアニメーションを設定することができます。",  # noqa
    ##################################################
    "This interface exists on a `DisplayObject` subclass instance, such as the `Sprite` or `Rectangle` class.": "このインターフェイスは`Sprite`や`Rectangle`などの`DisplayObject`の各サブクラスに存在します。",  # noqa
    ##################################################
    "## Basic usage": "## 基本的な使い方",
    ##################################################
    "The following example sets the y-coordinate animation (from 50 to 100) with the `animation_y` method.": "以下のコード例では`animation_y`メソッドを使ってY座標（50から100）のアニメーションを設定しています。",  # noqa
    ##################################################
    '```py\n# runnable\nimport apysc as ap\n\nEASING: ap.Easing = ap.Easing.EASE_OUT_QUINT\nDURATION: int = 1000\n\n\ndef on_animation_complete_1(e: ap.AnimationEvent[ap.Rectangle], options: dict) -> None:\n    """\n    The handler that the animation calls when its end.\n\n    Parameters\n    ----------\n    e : ap.AnimationEvent\n        Event instance.\n    options : dict\n        Optional arguments dictionary.\n    """\n    rectangle: ap.Rectangle = e.this.target\n    animation_y: ap.AnimationY = rectangle.animation_y(\n        y=50, duration=DURATION, easing=EASING\n    )\n    animation_y.animation_complete(on_animation_complete_2)\n    animation_y.start()\n\n\ndef on_animation_complete_2(e: ap.AnimationEvent[ap.Rectangle], options: dict) -> None:\n    """\n    The handler that the animation calls when its end.\n\n    Parameters\n    ----------\n    e : ap.AnimationEvent\n        Event instance.\n    options : dict\n        Optional arguments dictionary.\n    """\n    rectangle: ap.Rectangle = e.this.target\n    animation_y: ap.AnimationY = rectangle.animation_y(\n        y=100, duration=DURATION, easing=EASING\n    )\n    animation_y.animation_complete(on_animation_complete_1)\n    animation_y.start()\n\n\nap.Stage(\n    stage_width=150, stage_height=200, background_color="#333", stage_elem_id="stage"\n)\nsprite: ap.Sprite = ap.Sprite()\nsprite.graphics.begin_fill(color="#00aaff")\nrectangle: ap.Rectangle = sprite.graphics.draw_rect(x=50, y=50, width=50, height=50)\nanimation_y: ap.AnimationY = rectangle.animation_y(\n    y=100, duration=DURATION, easing=EASING\n)\nanimation_y.animation_complete(on_animation_complete_1)\nanimation_y.start()\n\nap.save_overall_html(dest_dir_path="./animation_y_basic_usage/")\n```': '```py\n# runnable\nimport apysc as ap\n\nEASING: ap.Easing = ap.Easing.EASE_OUT_QUINT\nDURATION: int = 1000\n\n\ndef on_animation_complete_1(e: ap.AnimationEvent[ap.Rectangle], options: dict) -> None:\n    """\n    The handler that the animation calls when its end.\n\n    Parameters\n    ----------\n    e : ap.AnimationEvent\n        Event instance.\n    options : dict\n        Optional arguments dictionary.\n    """\n    rectangle: ap.Rectangle = e.this.target\n    animation_y: ap.AnimationY = rectangle.animation_y(\n        y=50, duration=DURATION, easing=EASING\n    )\n    animation_y.animation_complete(on_animation_complete_2)\n    animation_y.start()\n\n\ndef on_animation_complete_2(e: ap.AnimationEvent[ap.Rectangle], options: dict) -> None:\n    """\n    The handler that the animation calls when its end.\n\n    Parameters\n    ----------\n    e : ap.AnimationEvent\n        Event instance.\n    options : dict\n        Optional arguments dictionary.\n    """\n    rectangle: ap.Rectangle = e.this.target\n    animation_y: ap.AnimationY = rectangle.animation_y(\n        y=100, duration=DURATION, easing=EASING\n    )\n    animation_y.animation_complete(on_animation_complete_1)\n    animation_y.start()\n\n\nap.Stage(\n    stage_width=150, stage_height=200, background_color="#333", stage_elem_id="stage"\n)\nsprite: ap.Sprite = ap.Sprite()\nsprite.graphics.begin_fill(color="#00aaff")\nrectangle: ap.Rectangle = sprite.graphics.draw_rect(x=50, y=50, width=50, height=50)\nanimation_y: ap.AnimationY = rectangle.animation_y(\n    y=100, duration=DURATION, easing=EASING\n)\nanimation_y.animation_complete(on_animation_complete_1)\nanimation_y.start()\n\nap.save_overall_html(dest_dir_path="./animation_y_basic_usage/")\n```',  # noqa
    ##################################################
    "## Notes for the Circle and Ellipse classes": "## Circle と Ellipse の各クラスの特記事項",
    ##################################################
    "The `Circle` and `Ellipse` classes' `animation_y` interface will return an `AnimationCy` (center-y) class instance, instead of a `AnimationY` instance, for internal implementation reason.": "内部の実装が異なる都合で`Circle`と`Ellipse`の各クラスの`animation_y`のインターフェイスは`AnimationY`クラスの代わりに`AnimationCy`クラスのインスタンスを返却します。",  # noqa
    ##################################################
    '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    stage_width=200, stage_height=150, background_color="#333", stage_elem_id="stage"\n)\nsprite: ap.Sprite = ap.Sprite()\nsprite.graphics.begin_fill(color="#00aaff")\ncircle: ap.Circle = sprite.graphics.draw_circle(x=100, y=100, radius=50)\nanimation_cy: ap.AnimationCy = circle.animation_y(\n    y=100, duration=1000, easing=ap.Easing.EASE_OUT_QUINT\n)\n```': '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    stage_width=200, stage_height=150, background_color="#333", stage_elem_id="stage"\n)\nsprite: ap.Sprite = ap.Sprite()\nsprite.graphics.begin_fill(color="#00aaff")\ncircle: ap.Circle = sprite.graphics.draw_circle(x=100, y=100, radius=50)\nanimation_cy: ap.AnimationCy = circle.animation_y(\n    y=100, duration=1000, easing=ap.Easing.EASE_OUT_QUINT\n)\n```',  # noqa
    ##################################################
    "## animation_y API": "## animation_y API",
    ##################################################
    '<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>': '<span class="inconspicuous-txt">特記事項: このAPIドキュメントはドキュメントビルド用のスクリプトによって自動で生成・同期されています。そのためもしかしたらこの節の内容は前節までの内容と重複している場合があります。</span>',  # noqa
    ##################################################
    "**[Interface summary]**": "**[インターフェイス概要]**",
    ##################################################
    "Set the y-coordinate animation setting.<hr>": "Y座標のアニメーションを設定します。<hr>",
    ##################################################
    "**[Parameters]**": "**[引数]**",
    ##################################################
    "- `y`: float or Number": "- `y`: float or Number",
    ##################################################
    "  - Destination of the y-coordinate.": "  - 最終的なY座標。",
    ##################################################
    "- `duration`: Int or int, default 3000": "- `duration`: Int or int, default 3000",
    ##################################################
    "  - Milliseconds before an animation ends.": "  - アニメーション完了までのミリ秒。",
    ##################################################
    "- `delay`: Int or int, default 0": "- `delay`: Int or int, default 0",
    ##################################################
    "  - Milliseconds before an animation starts.": "  - アニメーション開始までの遅延時間のミリ秒。",
    ##################################################
    "- `easing`: Easing, default Easing.LINEAR": "- `easing`: Easing, default Easing.LINEAR",  # noqa
    ##################################################
    "  - Easing setting.": "  - イージング設定。",
    ##################################################
    "<hr>": "<hr>",
    ##################################################
    "**[Returns]**": "**[返却値]**",
    ##################################################
    "- `animation_y`: AnimationY": "- `animation_y`: AnimationY",
    ##################################################
    "  - Created animation setting instance.": "  - 生成されたアニメーションのインスタンス。",
    ##################################################
    "<hr>": "<hr>",
    ##################################################
    "**[Notes]**": "**[特記事項]**",
    ##################################################
    "To start this animation, you need to call the `start` method of the returned instance.<hr>": "アニメーションを開始するには返却されたインスタンスの`start`メソッドを呼び出す必要があります。<hr>",  # noqa
    ##################################################
    "**[Examples]**": "**[コードサンプル]**",
    ##################################################
    '```py\n>>> import apysc as ap\n>>> stage: ap.Stage = ap.Stage()\n>>> sprite: ap.Sprite = ap.Sprite()\n>>> sprite.graphics.begin_fill(color="#0af")\n>>> rectangle: ap.Rectangle = sprite.graphics.draw_rect(\n...     x=50, y=50, width=50, height=50\n... )\n>>> _ = rectangle.animation_y(\n...     y=100,\n...     duration=1500,\n...     easing=ap.Easing.EASE_OUT_QUINT,\n... ).start()\n```': '```py\n>>> import apysc as ap\n>>> stage: ap.Stage = ap.Stage()\n>>> sprite: ap.Sprite = ap.Sprite()\n>>> sprite.graphics.begin_fill(color="#0af")\n>>> rectangle: ap.Rectangle = sprite.graphics.draw_rect(\n...     x=50, y=50, width=50, height=50\n... )\n>>> _ = rectangle.animation_y(\n...     y=100,\n...     duration=1500,\n...     easing=ap.Easing.EASE_OUT_QUINT,\n... ).start()\n```',  # noqa
    ##################################################
    "<hr>": "<hr>",
    ##################################################
    "**[References]**": "**[関連資料]**",
    ##################################################
    "- [Animation interfaces duration setting](https://simon-ritchie.github.io/apysc/en/animation_duration.html)": "- [各アニメーションインターフェイスの duration （アニメーション時間）設定](https://simon-ritchie.github.io/apysc/jp/jp_animation_duration.html)",  # noqa
    ##################################################
    "- [Animation interfaces delay setting](https://simon-ritchie.github.io/apysc/en/animation_delay.html)": "- [各アニメーションインターフェイスの delay （遅延時間）設定](https://simon-ritchie.github.io/apysc/jp/jp_animation_delay.html)",  # noqa
    ##################################################
    "- [Each animation interface return value](https://simon-ritchie.github.io/apysc/en/animation_return_value.html)": "- [各アニメーションインターフェイスの返却値](https://simon-ritchie.github.io/apysc/jp/jp_animation_return_value.html)",  # noqa
    ##################################################
    "- [Sequential animation setting](https://simon-ritchie.github.io/apysc/en/sequential_animation.html)": "- [連続したアニメーション設定](https://simon-ritchie.github.io/apysc/jp/jp_sequential_animation.html)",  # noqa
    ##################################################
    "- [animation_parallel interface](https://simon-ritchie.github.io/apysc/en/animation_parallel.html)": "- [animation_parallel インターフェイス](https://simon-ritchie.github.io/apysc/jp/jp_animation_parallel.html)",  # noqa
    ##################################################
    "- [Easing enum](https://simon-ritchie.github.io/apysc/en/easing_enum.html)": "- [イージングのenum](https://simon-ritchie.github.io/apysc/jp/jp_easing_enum.html)",  # noqa
}
