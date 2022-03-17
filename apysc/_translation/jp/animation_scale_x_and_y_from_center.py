"""This module is for the translation mapping data of the
following document:

Document file: animation_scale_x_and_y_from_center.md
Language: jp
"""

from typing import Dict

MAPPING: Dict[str, str] = {

    '# animation_scale_x_from_center and animation_scale_y_from_center interfaces':  # noqa
    '# animation_scale_x_from_center と animation_scale_y_from_center のインターフェイス',  # noqa

    'This page explains the `animation_scale_x_from_center` and `animation_scale_y_from_center` method interfaces.':  # noqa
    'このページでは`animation_scale_x_from_center`と`animation_scale_y_from_center`メソッドの各インターフェイスについて説明します。',  # noqa

    '## What interfaces are these?':
    '## 各インターフェイスの概要',

    'The `animation_scale_x_from_center` method interface creates an `ap.AnimationScaleXFromCenter` instance. You can animate x-direction\'s scale with it.':  # noqa
    '`animation_scale_x_from_center`メソッドのインターフェイスは`ap.AnimationScaleXFromCenter`クラスのインスタンスを生成します。そのインスタンスを使って中央座標を基準としたX軸方向の拡縮のアニメーションを設定することができます。',  # noqa

    'Similarly, the `animation_scale_y_from_center` method interface creates an `ap.AnimationScaleYFromCenter` instance. You can animate y-direction\'s scale with it.':  # noqa
    '同様に`animation_scale_y_from_center`メソッドのインターフェイスでは`ap.AnimationScaleYFromCenter`クラスのインスタンスを生成します。そのインスタンスを使ってY軸方向の拡縮のアニメーションを設定することができます。',  # noqa

    'These interfaces exist on a `GraphicsBase` subclass (that has the `scale_x_from_center` and `scale_y_from_center` interfaces), such as the `Rectangle` or `Circle`.':  # noqa
    'これらのインターフェイスは`scale_x_from_center`や`scale_y_from_center`などのインターフェイスを持つ`Rectangle`や`Circle`などの`GraphicsBase`のサブクラス上に存在します。',  # noqa

    '## Basic usage':
    '## 基本的な使い方',

    'The following example sets the scale-x (left-side rectangle) and scale-y (right-side rectangle) animation (from 1.0 to 2.0) with the `animation_scale_x_from_center` and `animation_scale_y_from_center` methods:':  # noqa
    '以下のコード例ではX軸方向の拡縮（1.0から2.0）のアニメーションを`animation_scale_x_from_center`メソッドを使って左側の四角に設定しています。同様にY軸方向の拡縮のアニメーションを右側の四角に設定しています。',  # noqa

    '```py\n# runnable\nfrom enum import Enum\n\nfrom typing_extensions import TypedDict\n\nimport apysc as ap\n\nDURATION: int = 1000\nEASING: ap.Easing = ap.Easing.EASE_OUT_QUINT\n\n\nclass Direction(Enum):\n    X = 1\n    Y = 2\n\n\nclass Options(TypedDict):\n    direction: Direction\n\n\ndef on_animation_complete_1(\n        e: ap.AnimationEvent[ap.Rectangle], options: Options) -> None:\n    """\n    The handler that the animation calls when its end.\n\n    Parameters\n    ----------\n    e : AnimationEvent\n        Event instance.\n    options : dict\n        Optional arguments dictionary.\n    """\n    rectangle: ap.Rectangle = e.this.target\n    SCALE: float = 1.0\n    if options[\'direction\'] == Direction.X:\n        rectangle.animation_scale_x_from_center(\n            scale_x_from_center=SCALE,\n            duration=DURATION,\n            easing=EASING,\n        ).animation_complete(\n            on_animation_complete_2,\n            options=options,\n        ).start()\n    elif options[\'direction\'] == Direction.Y:\n        rectangle.animation_scale_y_from_center(\n            scale_y_from_center=SCALE,\n            duration=DURATION,\n            easing=EASING,\n        ).animation_complete(\n            on_animation_complete_2,\n            options=options,\n        ).start()\n\n\ndef on_animation_complete_2(\n        e: ap.AnimationEvent[ap.Rectangle], options: Options) -> None:\n    """\n    The handler that the animation calls when its end.\n\n    Parameters\n    ----------\n    e : AnimationEvent\n        Event instance.\n    options : dict\n        Optional arguments dictionary.\n    """\n    rectangle: ap.Rectangle = e.this.target\n    SCALE: float = 2.0\n    if options[\'direction\'] == Direction.X:\n        rectangle.animation_scale_x_from_center(\n            scale_x_from_center=SCALE,\n            duration=DURATION,\n            easing=EASING,\n        ).animation_complete(\n            on_animation_complete_1,\n            options=options,\n        ).start()\n    elif options[\'direction\'] == Direction.Y:\n        rectangle.animation_scale_y_from_center(\n            scale_y_from_center=SCALE,\n            duration=DURATION,\n            easing=EASING,\n        ).animation_complete(\n            on_animation_complete_1,\n            options=options,\n        ).start()\n\n\nap.Stage(\n    stage_width=250, stage_height=150,\n    background_color=\'#333\', stage_elem_id=\'stage\')\nsprite: ap.Sprite = ap.Sprite()\nsprite.graphics.begin_fill(color=\'#0af\')\nleft_rectangle: ap.Rectangle = sprite.graphics.draw_rect(\n    x=50, y=50, width=50, height=50)\nright_rectangle: ap.Rectangle = sprite.graphics.draw_rect(\n    x=150, y=50, width=50, height=50)\n\noptions: Options = {\'direction\': Direction.X}\nleft_rectangle.animation_scale_x_from_center(\n    scale_x_from_center=2.0,\n    duration=DURATION,\n    easing=EASING,\n).animation_complete(\n    on_animation_complete_1,\n    options=options,\n).start()\n\noptions = {\'direction\': Direction.Y}\nright_rectangle.animation_scale_y_from_center(\n    scale_y_from_center=2.0,\n    duration=DURATION,\n    easing=EASING,\n).animation_complete(\n    on_animation_complete_1,\n    options=options,\n).start()\n\nap.save_overall_html(\n    dest_dir_path=\'./animation_scale_x_and_y_from_center_basic_usage/\')\n```':  # noqa
    '```py\n# runnable\nfrom enum import Enum\n\nfrom typing_extensions import TypedDict\n\nimport apysc as ap\n\nDURATION: int = 1000\nEASING: ap.Easing = ap.Easing.EASE_OUT_QUINT\n\n\nclass Direction(Enum):\n    X = 1\n    Y = 2\n\n\nclass Options(TypedDict):\n    direction: Direction\n\n\ndef on_animation_complete_1(\n        e: ap.AnimationEvent[ap.Rectangle], options: Options) -> None:\n    """\n    The handler that the animation calls when its end.\n\n    Parameters\n    ----------\n    e : AnimationEvent\n        Event instance.\n    options : dict\n        Optional arguments dictionary.\n    """\n    rectangle: ap.Rectangle = e.this.target\n    SCALE: float = 1.0\n    if options[\'direction\'] == Direction.X:\n        rectangle.animation_scale_x_from_center(\n            scale_x_from_center=SCALE,\n            duration=DURATION,\n            easing=EASING,\n        ).animation_complete(\n            on_animation_complete_2,\n            options=options,\n        ).start()\n    elif options[\'direction\'] == Direction.Y:\n        rectangle.animation_scale_y_from_center(\n            scale_y_from_center=SCALE,\n            duration=DURATION,\n            easing=EASING,\n        ).animation_complete(\n            on_animation_complete_2,\n            options=options,\n        ).start()\n\n\ndef on_animation_complete_2(\n        e: ap.AnimationEvent[ap.Rectangle], options: Options) -> None:\n    """\n    The handler that the animation calls when its end.\n\n    Parameters\n    ----------\n    e : AnimationEvent\n        Event instance.\n    options : dict\n        Optional arguments dictionary.\n    """\n    rectangle: ap.Rectangle = e.this.target\n    SCALE: float = 2.0\n    if options[\'direction\'] == Direction.X:\n        rectangle.animation_scale_x_from_center(\n            scale_x_from_center=SCALE,\n            duration=DURATION,\n            easing=EASING,\n        ).animation_complete(\n            on_animation_complete_1,\n            options=options,\n        ).start()\n    elif options[\'direction\'] == Direction.Y:\n        rectangle.animation_scale_y_from_center(\n            scale_y_from_center=SCALE,\n            duration=DURATION,\n            easing=EASING,\n        ).animation_complete(\n            on_animation_complete_1,\n            options=options,\n        ).start()\n\n\nap.Stage(\n    stage_width=250, stage_height=150,\n    background_color=\'#333\', stage_elem_id=\'stage\')\nsprite: ap.Sprite = ap.Sprite()\nsprite.graphics.begin_fill(color=\'#0af\')\nleft_rectangle: ap.Rectangle = sprite.graphics.draw_rect(\n    x=50, y=50, width=50, height=50)\nright_rectangle: ap.Rectangle = sprite.graphics.draw_rect(\n    x=150, y=50, width=50, height=50)\n\noptions: Options = {\'direction\': Direction.X}\nleft_rectangle.animation_scale_x_from_center(\n    scale_x_from_center=2.0,\n    duration=DURATION,\n    easing=EASING,\n).animation_complete(\n    on_animation_complete_1,\n    options=options,\n).start()\n\noptions = {\'direction\': Direction.Y}\nright_rectangle.animation_scale_y_from_center(\n    scale_y_from_center=2.0,\n    duration=DURATION,\n    easing=EASING,\n).animation_complete(\n    on_animation_complete_1,\n    options=options,\n).start()\n\nap.save_overall_html(\n    dest_dir_path=\'./animation_scale_x_and_y_from_center_basic_usage/\')\n```',  # noqa

    '## animation_scale_x_from_center API':
    '## animation_scale_x_from_center API',

    '<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>':  # noqa
    '<span class="inconspicuous-txt">特記事項: このAPIドキュメントはドキュメントビルド用のスクリプトによって自動で生成・同期されています。そのためもしかしたらこの節の内容は前節までの内容と重複している場合があります。</span>',  # noqa

    '**[Interface summary]** Set the scale-x from the center point animation setting.<hr>':  # noqa
    '**[インターフェイス概要]** 中央座標を基準としたX軸の拡縮アニメーションを設定します。<hr>',

    '**[Parameters]**':
    '**[引数]**',

    '- `scale_x_from_center`: Number or float':
    '- `scale_x_from_center`: Number or float',

    '  - The final scale-x of the animation.':
    '  - X軸の拡縮のアニメーションの最終値。',

    '- `duration`: Int or int, default 3000':
    '- `duration`: Int or int, default 3000',

    '  - Milliseconds before an animation ends.':
    '  - アニメーション完了までのミリ秒。',

    '- `delay`: Int or int, default 0':
    '- `delay`: Int or int, default 0',

    '  - Milliseconds before an animation starts.':
    '  - アニメーション開始までの遅延時間のミリ秒。',

    '- `easing`: Easing, default Easing.LINEAR':
    '- `easing`: Easing, default Easing.LINEAR',

    '  - Easing setting.':
    '  - イージング設定。',

    '<hr>':
    '<hr>',

    '**[Returns]**':
    '**[返却値]**',

    '- `animation_scale_x_from_center`: AnimationScaleXFromCenter':
    '- `animation_scale_x_from_center`: AnimationScaleXFromCenter',

    '  - Created animation setting instance.':
    '  - 生成されたアニメーションのインスタンス。',

    '<hr>':
    '<hr>',

    '**[Notes]**':
    '**[特記事項]**',

    'To start this animation, you need to call the `start` method of the returned instance.<hr>':  # noqa
    'アニメーションを開始するには返却されたインスタンスの`start`メソッドを呼び出す必要があります。<hr>',

    '**[Examples]**':
    '**[コードサンプル]**',

    '```py\n>>> import apysc as ap\n>>> stage: ap.Stage = ap.Stage()\n>>> sprite: ap.Sprite = ap.Sprite()\n>>> sprite.graphics.begin_fill(color=\'#0af\')\n>>> rectangle: ap.Rectangle = sprite.graphics.draw_rect(\n...     x=50, y=50, width=50, height=50)\n>>> _ = rectangle.animation_scale_x_from_center(\n...     scale_x_from_center=0.5,\n...     duration=1500,\n...     easing=ap.Easing.EASE_OUT_QUINT,\n... ).start()\n```':  # noqa
    '```py\n>>> import apysc as ap\n>>> stage: ap.Stage = ap.Stage()\n>>> sprite: ap.Sprite = ap.Sprite()\n>>> sprite.graphics.begin_fill(color=\'#0af\')\n>>> rectangle: ap.Rectangle = sprite.graphics.draw_rect(\n...     x=50, y=50, width=50, height=50)\n>>> _ = rectangle.animation_scale_x_from_center(\n...     scale_x_from_center=0.5,\n...     duration=1500,\n...     easing=ap.Easing.EASE_OUT_QUINT,\n... ).start()\n```',  # noqa

    '<hr>':
    '<hr>',

    '**[References]**':
    '**[関連資料]**',

    '- [Animation interfaces duration setting document](https://simon-ritchie.github.io/apysc/animation_duration.html)':  # noqa
    '- [各アニメーションインターフェイスの duration （アニメーション時間）設定](https://simon-ritchie.github.io/apysc/jp_animation_duration.html)',  # noqa

    '- [Animation interfaces delay setting document](https://simon-ritchie.github.io/apysc/animation_delay.html)':  # noqa
    '- [各アニメーションインターフェイスの delay （遅延時間）設定](https://simon-ritchie.github.io/apysc/jp_animation_delay.html)',  # noqa

    '- [Each animation interface return value document](https://simon-ritchie.github.io/apysc/animation_return_value.html)':  # noqa
    '- [各アニメーションインターフェイスの返却値](https://simon-ritchie.github.io/apysc/jp_animation_return_value.html)',  # noqa

    '- [Sequential animation setting document](https://simon-ritchie.github.io/apysc/sequential_animation.html)':  # noqa
    '- [連続したアニメーション設定](https://simon-ritchie.github.io/apysc/jp_sequential_animation.html)',  # noqa

    '- [animation_parallel interface document](https://simon-ritchie.github.io/apysc/animation_parallel.html)':  # noqa
    '- [animation_parallel （並列アニメーション設定）のインターフェイス](https://simon-ritchie.github.io/apysc/jp_animation_parallel.html)',  # noqa

    '- [Easing enum document](https://simon-ritchie.github.io/apysc/easing_enum.html)':  # noqa
    '- [イージングのenum](https://simon-ritchie.github.io/apysc/jp_easing_enum.html)',  # noqa

    '## animation_scale_y_from_center API':
    '## animation_scale_y_from_center API',

    '<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>':  # noqa
    '<span class="inconspicuous-txt">特記事項: このAPIドキュメントはドキュメントビルド用のスクリプトによって自動で生成・同期されています。そのためもしかしたらこの節の内容は前節までの内容と重複している場合があります。</span>',  # noqa

    '**[Interface summary]** Set the scale-y from the center point animation setting.<hr>':  # noqa
    '**[インターフェイス概要]** 中央座標を基準としたY軸の拡縮アニメーションを設定します。<hr>',

    '**[Parameters]**':
    '**[引数]**',

    '- `scale_y_from_center`: Number or float':
    '- `scale_y_from_center`: Number or float',

    '  - The final scale-y of the animation.':
    '  - Y軸の拡縮のアニメーションの最終値。',

    '- `duration`: Int or int, default 3000':
    '- `duration`: Int or int, default 3000',

    '  - Milliseconds before an animation ends.':
    '  - アニメーション完了までのミリ秒。',

    '- `delay`: Int or int, default 0':
    '- `delay`: Int or int, default 0',

    '  - Milliseconds before an animation starts.':
    '  - アニメーション開始までの遅延時間のミリ秒。',

    '- `easing`: Easing, default Easing.LINEAR':
    '- `easing`: Easing, default Easing.LINEAR',

    '  - Easing setting.':
    '  - イージング設定。',

    '<hr>':
    '<hr>',

    '**[Returns]**':
    '**[返却値]**',

    '- `animation_scale_y_from_center`: AnimationScaleYFromCenter':
    '- `animation_scale_y_from_center`: AnimationScaleYFromCenter',

    '  - Created animation setting instance.':
    '  - 生成されたアニメーションのインスタンス。',

    '<hr>':
    '<hr>',

    '**[Notes]**':
    '**[特記事項]**',

    'To start this animation, you need to call the `start` method of the returned instance.<hr>':  # noqa
    'アニメーションを開始するには返却されたインスタンスの`start`メソッドを呼び出す必要があります。<hr>',

    '**[Examples]**':
    '**[コードサンプル]**',

    '```py\n>>> import apysc as ap\n>>> stage: ap.Stage = ap.Stage()\n>>> sprite: ap.Sprite = ap.Sprite()\n>>> sprite.graphics.begin_fill(color=\'#0af\')\n>>> rectangle: ap.Rectangle = sprite.graphics.draw_rect(\n...     x=50, y=50, width=50, height=50)\n>>> _ = rectangle.animation_scale_y_from_center(\n...     scale_y_from_center=0.5,\n...     duration=1500,\n...     easing=ap.Easing.EASE_OUT_QUINT,\n... ).start()\n```':  # noqa
    '```py\n>>> import apysc as ap\n>>> stage: ap.Stage = ap.Stage()\n>>> sprite: ap.Sprite = ap.Sprite()\n>>> sprite.graphics.begin_fill(color=\'#0af\')\n>>> rectangle: ap.Rectangle = sprite.graphics.draw_rect(\n...     x=50, y=50, width=50, height=50)\n>>> _ = rectangle.animation_scale_y_from_center(\n...     scale_y_from_center=0.5,\n...     duration=1500,\n...     easing=ap.Easing.EASE_OUT_QUINT,\n... ).start()\n```',  # noqa

    '<hr>':
    '<hr>',

    '**[References]**':
    '**[関連資料]**',

    '- [Animation interfaces duration setting document](https://simon-ritchie.github.io/apysc/animation_duration.html)':  # noqa
    '- [各アニメーションインターフェイスの duration （アニメーション時間）設定](https://simon-ritchie.github.io/apysc/jp_animation_duration.html)',  # noqa

    '- [Animation interfaces delay setting document](https://simon-ritchie.github.io/apysc/animation_delay.html)':  # noqa
    '- [各アニメーションインターフェイスの delay （遅延時間）設定](https://simon-ritchie.github.io/apysc/jp_animation_delay.html)',  # noqa

    '- [Each animation interface return value document](https://simon-ritchie.github.io/apysc/animation_return_value.html)':  # noqa
    '- [各アニメーションインターフェイスの返却値](https://simon-ritchie.github.io/apysc/jp_animation_return_value.html)',  # noqa

    '- [Sequential animation setting document](https://simon-ritchie.github.io/apysc/sequential_animation.html)':  # noqa
    '- [連続したアニメーション設定](https://simon-ritchie.github.io/apysc/jp_sequential_animation.html)',  # noqa

    '- [animation_parallel interface document](https://simon-ritchie.github.io/apysc/animation_parallel.html)':  # noqa
    '- [animation_parallel （並列アニメーション設定）のインターフェイス](https://simon-ritchie.github.io/apysc/jp_animation_parallel.html)',  # noqa

    '- [Easing enum document](https://simon-ritchie.github.io/apysc/easing_enum.html)':  # noqa
    '- [イージングのenum](https://simon-ritchie.github.io/apysc/jp_easing_enum.html)',  # noqa

}
