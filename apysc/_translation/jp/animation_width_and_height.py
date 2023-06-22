"""This module is for the translation mapping data of the
following document:

Document file: animation_width_and_height.md
Language: jp
"""

from typing import Dict

MAPPING: Dict[str, str] = {
    ##################################################
    "# animation_width and animation_height interfaces": "# animation_width と animation_height のインターフェイス",  # noqa
    ##################################################
    "This page explains the `animation_width` and `animation_height` interfaces.": "このページでは`animation_width`と`animation_height`メソッドの各インターフェイスについて説明します。",  # noqa
    ##################################################
    "## What interfaces are these?": "## 各インターフェイスの概要",
    ##################################################
    "The `animation_width` method interface creates an `AnimationWidth` instance. You can animate object width with it.": "`animation_width`インターフェイスは`AnimationWidth`クラスのインスタンスを生成します。そのインスタンスを使って幅のアニメーションを設定することができます。",  # noqa
    ##################################################
    "Similarly, the `animation_height` method interface creates an `AnimationHeight` instance. You can animate object height with it.": "同様に`animation_height`メソッドのインターフェイスは`AnimationHeight`クラスのインスタンスを生成します。そのインスタンスを使って高さのアニメーションを設定することができます。",  # noqa
    ##################################################
    "These interfaces exist on some `DisplayObject` instances, such as the `Rectangle` class.": "これらの各インターフェイスは`Rectangle`クラスなどの`DisplayObject`の各サブクラス上に存在します。",  # noqa
    ##################################################
    "## Basic usage": "## 基本的な使い方",
    ##################################################
    "The following example sets the width animation (from 50 to 100) with the `animation_width` method:": "以下のコード例では`animation_width`メソッドを使って幅（50から100）のアニメーションを設定しています。",  # noqa
    ##################################################
    '```py\n# runnable\nimport apysc as ap\n\nDURATION: int = 1000\nEASING: ap.Easing = ap.Easing.EASE_OUT_QUINT\n\n\ndef on_animation_complete_1(e: ap.AnimationEvent[ap.Rectangle], options: dict) -> None:\n    """\n    The handler that the animation calls when its end.\n\n    Parameters\n    ----------\n    e : ap.AnimationEvent\n        Event instance.\n    options : dict\n        Optional arguments dictionary.\n    """\n    rectangle: ap.Rectangle = e.this.target\n    animation_width: ap.AnimationWidth = rectangle.animation_width(\n        width=50, duration=DURATION, easing=EASING\n    )\n    animation_width.animation_complete(on_animation_complete_2)\n    animation_width.start()\n\n\ndef on_animation_complete_2(e: ap.AnimationEvent[ap.Rectangle], options: dict) -> None:\n    """\n    The handler that the animation calls when its end.\n\n    Parameters\n    ----------\n    e : ap.AnimationEvent\n        Event instance.\n    options : dict\n        Optional arguments dictionary.\n    """\n    rectangle: ap.Rectangle = e.this.target\n    animation_width: ap.AnimationWidth = rectangle.animation_width(\n        width=100, duration=DURATION, easing=EASING\n    )\n    animation_width.animation_complete(on_animation_complete_1)\n    animation_width.start()\n\n\nap.Stage(\n    stage_width=200, stage_height=150, background_color="#333", stage_elem_id="stage"\n)\nsprite: ap.Sprite = ap.Sprite()\nsprite.graphics.begin_fill(color="#00aaff")\nrectangle: ap.Rectangle = sprite.graphics.draw_rect(x=50, y=50, width=50, height=50)\nanimation_width: ap.AnimationWidth = rectangle.animation_width(\n    width=100, duration=DURATION, easing=EASING\n)\nanimation_width.animation_complete(on_animation_complete_1)\nanimation_width.start()\n\nap.save_overall_html(dest_dir_path="./animation_width_basic_usage/")\n```': '```py\n# runnable\nimport apysc as ap\n\nDURATION: int = 1000\nEASING: ap.Easing = ap.Easing.EASE_OUT_QUINT\n\n\ndef on_animation_complete_1(e: ap.AnimationEvent[ap.Rectangle], options: dict) -> None:\n    """\n    The handler that the animation calls when its end.\n\n    Parameters\n    ----------\n    e : ap.AnimationEvent\n        Event instance.\n    options : dict\n        Optional arguments dictionary.\n    """\n    rectangle: ap.Rectangle = e.this.target\n    animation_width: ap.AnimationWidth = rectangle.animation_width(\n        width=50, duration=DURATION, easing=EASING\n    )\n    animation_width.animation_complete(on_animation_complete_2)\n    animation_width.start()\n\n\ndef on_animation_complete_2(e: ap.AnimationEvent[ap.Rectangle], options: dict) -> None:\n    """\n    The handler that the animation calls when its end.\n\n    Parameters\n    ----------\n    e : ap.AnimationEvent\n        Event instance.\n    options : dict\n        Optional arguments dictionary.\n    """\n    rectangle: ap.Rectangle = e.this.target\n    animation_width: ap.AnimationWidth = rectangle.animation_width(\n        width=100, duration=DURATION, easing=EASING\n    )\n    animation_width.animation_complete(on_animation_complete_1)\n    animation_width.start()\n\n\nap.Stage(\n    stage_width=200, stage_height=150, background_color="#333", stage_elem_id="stage"\n)\nsprite: ap.Sprite = ap.Sprite()\nsprite.graphics.begin_fill(color="#00aaff")\nrectangle: ap.Rectangle = sprite.graphics.draw_rect(x=50, y=50, width=50, height=50)\nanimation_width: ap.AnimationWidth = rectangle.animation_width(\n    width=100, duration=DURATION, easing=EASING\n)\nanimation_width.animation_complete(on_animation_complete_1)\nanimation_width.start()\n\nap.save_overall_html(dest_dir_path="./animation_width_basic_usage/")\n```',  # noqa
    ##################################################
    "Similarly, the following example animates the height with the `animation_height` method:": "同様に以下のコード例では`animation_height`メソッドを使って高さのアニメーションを設定しています。",  # noqa
    ##################################################
    '```py\n# runnable\nimport apysc as ap\n\nDURATION: int = 1000\nEASING: ap.Easing = ap.Easing.EASE_OUT_QUINT\n\n\ndef on_animation_complete_1(e: ap.AnimationEvent[ap.Rectangle], options: dict) -> None:\n    """\n    The handler that the animation calls when its end.\n\n    Parameters\n    ----------\n    e : ap.AnimationEvent\n        Event instance.\n    options : dict\n        Optional arguments dictionary.\n    """\n    rectangle: ap.Rectangle = e.this.target\n    animation_height: ap.AnimationHeight = rectangle.animation_height(\n        height=50, duration=DURATION, easing=EASING\n    )\n    animation_height.animation_complete(on_animation_complete_2)\n    animation_height.start()\n\n\ndef on_animation_complete_2(e: ap.AnimationEvent[ap.Rectangle], options: dict) -> None:\n    """\n    The handler that the animation calls when its end.\n\n    Parameters\n    ----------\n    e : ap.AnimationEvent\n        Event instance.\n    options : dict\n        Optional arguments dictionary.\n    """\n    rectangle: ap.Rectangle = e.this.target\n    animation_height: ap.AnimationHeight = rectangle.animation_height(\n        height=100, duration=DURATION, easing=EASING\n    )\n    animation_height.animation_complete(on_animation_complete_1)\n    animation_height.start()\n\n\nap.Stage(\n    stage_width=150, stage_height=200, background_color="#333", stage_elem_id="stage"\n)\nsprite: ap.Sprite = ap.Sprite()\nsprite.graphics.begin_fill(color="#00aaff")\nrectangle: ap.Rectangle = sprite.graphics.draw_rect(x=50, y=50, width=50, height=50)\nanimation_height: ap.AnimationHeight = rectangle.animation_height(\n    height=100, duration=DURATION, easing=EASING\n)\nanimation_height.animation_complete(on_animation_complete_1)\nanimation_height.start()\n\nap.save_overall_html(dest_dir_path="./animation_height_basic_usage/")\n```': '```py\n# runnable\nimport apysc as ap\n\nDURATION: int = 1000\nEASING: ap.Easing = ap.Easing.EASE_OUT_QUINT\n\n\ndef on_animation_complete_1(e: ap.AnimationEvent[ap.Rectangle], options: dict) -> None:\n    """\n    The handler that the animation calls when its end.\n\n    Parameters\n    ----------\n    e : ap.AnimationEvent\n        Event instance.\n    options : dict\n        Optional arguments dictionary.\n    """\n    rectangle: ap.Rectangle = e.this.target\n    animation_height: ap.AnimationHeight = rectangle.animation_height(\n        height=50, duration=DURATION, easing=EASING\n    )\n    animation_height.animation_complete(on_animation_complete_2)\n    animation_height.start()\n\n\ndef on_animation_complete_2(e: ap.AnimationEvent[ap.Rectangle], options: dict) -> None:\n    """\n    The handler that the animation calls when its end.\n\n    Parameters\n    ----------\n    e : ap.AnimationEvent\n        Event instance.\n    options : dict\n        Optional arguments dictionary.\n    """\n    rectangle: ap.Rectangle = e.this.target\n    animation_height: ap.AnimationHeight = rectangle.animation_height(\n        height=100, duration=DURATION, easing=EASING\n    )\n    animation_height.animation_complete(on_animation_complete_1)\n    animation_height.start()\n\n\nap.Stage(\n    stage_width=150, stage_height=200, background_color="#333", stage_elem_id="stage"\n)\nsprite: ap.Sprite = ap.Sprite()\nsprite.graphics.begin_fill(color="#00aaff")\nrectangle: ap.Rectangle = sprite.graphics.draw_rect(x=50, y=50, width=50, height=50)\nanimation_height: ap.AnimationHeight = rectangle.animation_height(\n    height=100, duration=DURATION, easing=EASING\n)\nanimation_height.animation_complete(on_animation_complete_1)\nanimation_height.start()\n\nap.save_overall_html(dest_dir_path="./animation_height_basic_usage/")\n```',  # noqa
    ##################################################
    "## Notes for the Ellipse instance": "## Ellipse のインスタンスにおける特記事項",
    ##################################################
    "The ellipse instance's `animation_width` and `animation_height` interfaces will return an `AnimationWidthForEllipse` and `AnimationHeightForEllipse` instance instead of an `AnimationWidth` instance, for the reason of the internal implementation, as follows:": "楕円のインスタンス（`Ellipse`クラス）の`animation_width`と`animation_height`の各インターフェイスは内部実行が異なる都合で`AnimationWidth`クラスなどの代わりに`以下のコード例のようにAnimationWidthForEllipse`クラスと`AnimationHeightForEllipse`クラスのインスタンスを返却します:",  # noqa
    ##################################################
    '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    stage_width=150, stage_height=200, background_color="#333", stage_elem_id="stage"\n)\nsprite: ap.Sprite = ap.Sprite()\nsprite.graphics.begin_fill(color="#00aaff")\nellipse: ap.Ellipse = sprite.graphics.draw_ellipse(x=100, y=100, width=100, height=100)\nanimation_width: ap.AnimationWidthForEllipse = ellipse.animation_width(\n    width=200, duration=1000\n)\nanimation_width.start()\n```': '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    stage_width=150, stage_height=200, background_color="#333", stage_elem_id="stage"\n)\nsprite: ap.Sprite = ap.Sprite()\nsprite.graphics.begin_fill(color="#00aaff")\nellipse: ap.Ellipse = sprite.graphics.draw_ellipse(x=100, y=100, width=100, height=100)\nanimation_width: ap.AnimationWidthForEllipse = ellipse.animation_width(\n    width=200, duration=1000\n)\nanimation_width.start()\n```',  # noqa
    ##################################################
    "## animation_width API": "## animation_width API",
    ##################################################
    '<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>': '<span class="inconspicuous-txt">特記事項: このAPIドキュメントはドキュメントビルド用のスクリプトによって自動で生成・同期されています。そのためもしかしたらこの節の内容は前節までの内容と重複している場合があります。</span>',  # noqa
    ##################################################
    "**[Interface summary]**": "**[インターフェイス概要]**",
    ##################################################
    "Set the width animation setting.<hr>": "幅のアニメーションを設定します。<hr>",
    ##################################################
    "**[Parameters]**": "**[引数]**",
    ##################################################
    "- `width`: Int or int": "- `width`: Int or int",
    ##################################################
    "  - The final width of the animation.": "  - 幅のアニメーションの最終値。",
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
    "- `animation_width`: AnimationWidth": "- `animation_width`: AnimationWidth",
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
    '```py\n>>> import apysc as ap\n>>> stage: ap.Stage = ap.Stage()\n>>> sprite: ap.Sprite = ap.Sprite()\n>>> sprite.graphics.begin_fill(color="#0af")\n>>> rectangle: ap.Rectangle = sprite.graphics.draw_rect(\n...     x=50, y=50, width=50, height=50\n... )\n>>> _ = rectangle.animation_width(\n...     width=100,\n...     duration=1500,\n...     easing=ap.Easing.EASE_OUT_QUINT,\n... ).start()\n```': '```py\n>>> import apysc as ap\n>>> stage: ap.Stage = ap.Stage()\n>>> sprite: ap.Sprite = ap.Sprite()\n>>> sprite.graphics.begin_fill(color="#0af")\n>>> rectangle: ap.Rectangle = sprite.graphics.draw_rect(\n...     x=50, y=50, width=50, height=50\n... )\n>>> _ = rectangle.animation_width(\n...     width=100,\n...     duration=1500,\n...     easing=ap.Easing.EASE_OUT_QUINT,\n... ).start()\n```',  # noqa
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
    ##################################################
    "## animation_height API": "## animation_height API",
    ##################################################
    '<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>': '<span class="inconspicuous-txt">特記事項: このAPIドキュメントはドキュメントビルド用のスクリプトによって自動で生成・同期されています。そのためもしかしたらこの節の内容は前節までの内容と重複している場合があります。</span>',  # noqa
    ##################################################
    "**[Interface summary]**": "**[インターフェイス概要]**",
    ##################################################
    "Set the height animation setting.<hr>": "高さのアニメーションを設定します。<hr>",
    ##################################################
    "**[Parameters]**": "**[引数]**",
    ##################################################
    "- `height`: Int or int": "- `height`: Int or int",
    ##################################################
    "  - The final height of the animation.": "  - 高さのアニメーションの最終値。",
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
    "- `animation_height`: AnimationHeight": "- `animation_height`: AnimationHeight",
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
    '```py\n>>> import apysc as ap\n>>> stage: ap.Stage = ap.Stage()\n>>> sprite: ap.Sprite = ap.Sprite()\n>>> sprite.graphics.begin_fill(color="#0af")\n>>> rectangle: ap.Rectangle = sprite.graphics.draw_rect(\n...     x=50, y=50, width=50, height=50\n... )\n>>> _ = rectangle.animation_height(\n...     height=100,\n...     duration=1500,\n...     easing=ap.Easing.EASE_OUT_QUINT,\n... ).start()\n```': '```py\n>>> import apysc as ap\n>>> stage: ap.Stage = ap.Stage()\n>>> sprite: ap.Sprite = ap.Sprite()\n>>> sprite.graphics.begin_fill(color="#0af")\n>>> rectangle: ap.Rectangle = sprite.graphics.draw_rect(\n...     x=50, y=50, width=50, height=50\n... )\n>>> _ = rectangle.animation_height(\n...     height=100,\n...     duration=1500,\n...     easing=ap.Easing.EASE_OUT_QUINT,\n... ).start()\n```',  # noqa
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
