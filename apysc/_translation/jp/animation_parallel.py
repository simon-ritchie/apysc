"""This module is for the translation mapping data of the
following document:

Document file: animation_parallel.md
Language: jp
"""

from typing import Dict

MAPPING: Dict[str, str] = {
    ##################################################
    "# animation_parallel interface": "# animation_parallel インターフェイス",
    ##################################################
    "This page explains the `animation_parallel` interface.": "このページでは`animation_parallel`のインターフェイスについて説明します。",  # noqa
    ##################################################
    "## What interface is this?": "## インターフェイス概要",
    ##################################################
    "The `animation_parallel` method interface creates an `AnimationParallel` instance. You can set multiple simultaneous animations to the same instance with it.": "`animation_parallel`メソッドのインターフェイスは`AnimationParallel`クラスのインスタンスを生成します。このインスタンスを使うことで複数のアニメーションの同時実行の設定を行うことができます。",  # noqa
    ##################################################
    "This interface exists on a `DisplayObject` subclass instance, such as the `Sprite` or `Rectangle` class.": "このインターフェイスは`Sprite`や`Rectangle`などの`DisplayObject`の各サブクラスに存在します。",  # noqa
    ##################################################
    "## Basic usage": "## 基本的な使い方",
    ##################################################
    "You can use this interface with the `animation_parallel` method. The `animations` list argument does not require any animation settings.": "`animation_parallel`メソッドを使ってこのインターフェイスを使用することができます。`animations`引数の値は各アニメーションの設定値の指定を必要としません。",  # noqa
    ##################################################
    "The following example sets the simultaneous animations of the x, fill alpha, fill color, and line thickness.": "以下のコード例ではX座標、塗りの透明度、塗りの色、そして線の幅に対するアニメーションを同時に実行しています。",  # noqa
    ##################################################
    '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    stage_width=400, stage_height=150, background_color="#333", stage_elem_id="stage"\n)\nsprite: ap.Sprite = ap.Sprite()\nsprite.graphics.begin_fill(color="#0af")\nsprite.graphics.line_style(color="#fff", thickness=3)\n\nrectangle: ap.Rectangle = sprite.graphics.draw_rect(x=50, y=50, width=50, height=50)\nrectangle.animation_parallel(\n    animations=[\n        rectangle.animation_x(x=300),\n        rectangle.animation_fill_color(fill_color="#f0a"),\n        rectangle.animation_fill_alpha(alpha=0.3),\n        rectangle.animation_line_thickness(thickness=7),\n    ],\n    duration=3000,\n    delay=3000,\n    easing=ap.Easing.EASE_OUT_QUINT,\n).start()\n\nap.save_overall_html(dest_dir_path="animation_parallel_basic_usage/")\n```': '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    stage_width=400, stage_height=150, background_color="#333", stage_elem_id="stage"\n)\nsprite: ap.Sprite = ap.Sprite()\nsprite.graphics.begin_fill(color="#0af")\nsprite.graphics.line_style(color="#fff", thickness=3)\n\nrectangle: ap.Rectangle = sprite.graphics.draw_rect(x=50, y=50, width=50, height=50)\nrectangle.animation_parallel(\n    animations=[\n        rectangle.animation_x(x=300),\n        rectangle.animation_fill_color(fill_color="#f0a"),\n        rectangle.animation_fill_alpha(alpha=0.3),\n        rectangle.animation_line_thickness(thickness=7),\n    ],\n    duration=3000,\n    delay=3000,\n    easing=ap.Easing.EASE_OUT_QUINT,\n).start()\n\nap.save_overall_html(dest_dir_path="animation_parallel_basic_usage/")\n```',  # noqa
    ##################################################
    "## Note for each animation's duration, delay, and easing setting": "## 各アニメーションのduration、delay、easingの設定についての特記事項",  # noqa
    ##################################################
    "Animation settings of the `duration`\\, `delay`\\, and `easing` in the `animations` argument can't be changed since these animation settings are referring to the `animation_parallel` arguments. If you set these parameters in the `animations` arguments, setting raise an error:": "各アニメーションごとの`duration`や`delay`、`easing`の引数設定は`animation_parallel`メソッド側の値が使用されるため設定できません。もし何らかの値を設定した場合にはエラーとなります。",  # noqa
    ##################################################
    "```py\n...\nrectangle.animation_parallel(\n    animations=[\n        rectangle.animation_x(x=300, duration=1000),\n    ],\n    duration=3000,\n    delay=2000,\n    easing=ap.Easing.EASE_OUT_QUINT,\n)\n...\n```": "```py\n...\nrectangle.animation_parallel(\n    animations=[\n        rectangle.animation_x(x=300, duration=1000),\n    ],\n    duration=3000,\n    delay=2000,\n    easing=ap.Easing.EASE_OUT_QUINT,\n)\n...\n```",  # noqa
    ##################################################
    "```\nValueError: There is an animation target that is changed duration setting: 1000\nThe duration setting of animation in the `animations` argument can not be changed.\nTarget animation type: <class 'apysc._animation.animation_x.AnimationX'>\n```": "```\nValueError: There is an animation target that is changed duration setting: 1000\nThe duration setting of animation in the `animations` argument can not be changed.\nTarget animation type: <class 'apysc._animation.animation_x.AnimationX'>\n```",  # noqa
    ##################################################
    "## animation_parallel API": "## animation_parallel API",
    ##################################################
    '<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>': '<span class="inconspicuous-txt">特記事項: このAPIドキュメントはドキュメントビルド用のスクリプトによって自動で生成・同期されています。そのためもしかしたらこの節の内容は前節までの内容と重複している場合があります。</span>',  # noqa
    ##################################################
    "**[Interface summary]**": "**[インターフェイス概要]**",
    ##################################################
    "Set the parallel animation setting.<hr>": "並列実行されるアニメーション設定を行います。<hr>",
    ##################################################
    "**[Parameters]**": "**[引数]**",
    ##################################################
    "- `animations`: list of AnimationBase": "- `animations`: list of AnimationBase",
    ##################################################
    "  - Target animation settings.": "  - 対象の各アニメーションの設定。",
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
    "- `animation_parallel`: AnimationParallel": "- `animation_parallel`: AnimationParallel",  # noqa
    ##################################################
    "  - Created animation setting instance.": "  - 生成されたアニメーションのインスタンス。",
    ##################################################
    "<hr>": "<hr>",
    ##################################################
    "**[Raises]**": "**[エラー発生条件]**",
    ##################################################
    "- ValueError: ": "- ValueError: ",
    ##################################################
    "<br> ・If the animations' target is not this instance. ": "<br> ・もし各アニメーションの対象のインスタンスがこのインスタンスでは無い場合。",  # noqa
    ##################################################
    "<br> ・If there are changed duration, delay, or easing animation settings in the `animations` list.": "<br> ・もし`animations`引数の各アニメーションのderationやdelay、easingの設定が変更去れている場合。",  # noqa
    ##################################################
    "<hr>": "<hr>",
    ##################################################
    "**[Notes]**": "**[特記事項]**",
    ##################################################
    " ・To start this animation, you need to call the `start` method of the returned instance. ": " ・アニメーションを開始するには返却されたインスタンスの`start`メソッドを呼び出す必要があります。 ",  # noqa
    ##################################################
    "<br> ・The `animations` argument can't contains the `AnimationParallel` instance. ": "<br> ・`animations`引数の値には`AnimationParallel`クラスのインスタンスを含めることはできません。 ",  # noqa
    ##################################################
    "<br> ・This interface ignores the duration, delay, and easing arguments in the `animations` argument (this interface uses self-arguments instead).<hr>": "<br> ・このインターフェイスは`animations`引数内の値のduration, delay, easingの各引数の設定を無視します（代わりにこのインターフェイス自身のそれらの引数の設定を利用してください）。<hr>",  # noqa
    ##################################################
    "**[Examples]**": "**[コードサンプル]**",
    ##################################################
    '```py\n>>> import apysc as ap\n>>> stage: ap.Stage = ap.Stage()\n>>> sprite: ap.Sprite = ap.Sprite()\n>>> sprite.graphics.begin_fill(color="#0af")\n>>> rectangle: ap.Rectangle = sprite.graphics.draw_rect(\n...     x=50, y=50, width=50, height=50\n... )\n>>> _ = rectangle.animation_parallel(\n...     animations=[\n...         rectangle.animation_x(x=100),\n...         rectangle.animation_fill_color(fill_color="#f0a"),\n...         rectangle.animation_fill_alpha(alpha=0.5),\n...     ],\n...     duration=1500,\n...     easing=ap.Easing.EASE_OUT_QUINT,\n... ).start()\n```': '```py\n>>> import apysc as ap\n>>> stage: ap.Stage = ap.Stage()\n>>> sprite: ap.Sprite = ap.Sprite()\n>>> sprite.graphics.begin_fill(color="#0af")\n>>> rectangle: ap.Rectangle = sprite.graphics.draw_rect(\n...     x=50, y=50, width=50, height=50\n... )\n>>> _ = rectangle.animation_parallel(\n...     animations=[\n...         rectangle.animation_x(x=100),\n...         rectangle.animation_fill_color(fill_color="#f0a"),\n...         rectangle.animation_fill_alpha(alpha=0.5),\n...     ],\n...     duration=1500,\n...     easing=ap.Easing.EASE_OUT_QUINT,\n... ).start()\n```',  # noqa
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
    "- [Easing enum](https://simon-ritchie.github.io/apysc/en/easing_enum.html)": "- [イージングのenum](https://simon-ritchie.github.io/apysc/jp/jp_easing_enum.html)",  # noqa
}
