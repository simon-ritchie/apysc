"""This module is for the translation mapping data of the
following document:

Document file: animation_event.md
Language: jp
"""

from typing import Dict

MAPPING: Dict[str, str] = {
    ##################################################
    "# AnimationEvent class": "# AnimationEvent クラス",
    ##################################################
    "This page explains the `AnimationEvent` class.": "このページでは`AnimationEvent`クラスについて説明します。",  # noqa
    ##################################################
    "## What class is this?": "## クラス概要",
    ##################################################
    "An animation-related event handler uses the `AnimationEvent` class, such as the complete animation event. Each animation interface passes this event instance to the handler.": "アニメーション終了時のイベントなどの各アニメーション関連のイベントで`AnimationEvent`クラスは使用されます。各アニメーションのインターフェイスはイベントのハンドラへこのイベントのインスタンスを渡します。",  # noqa
    ##################################################
    "## Basic usage": "## 基本的な使い方",
    ##################################################
    "The following example sets the animation complete event handler. The animation interface passes the `AnimationEvent` instance argument as the `e: ap.AnimationEvent`:": "以下の例ではアニメーション完了時のイベントのハンドラへ`e: ap.AnimationEvent`という指定で`AnimationEvent`のインスタンスの引数を設定しています。",  # noqa
    ##################################################
    '```py\n# runnable\nimport apysc as ap\n\n\ndef on_animation_complete(e: ap.AnimationEvent, options: dict) -> None:\n    """\n    The handler that animation calls when its end.\n\n    Parameters\n    ----------\n    e : ap.AnimationEvent\n        Event instance.\n    options : dict\n        Optional arguments dictionary.\n    """\n    ap.trace("Animation is completed!")\n\n\nap.Stage(\n    stage_width=200,\n    stage_height=150,\n    background_color=ap.Color("#333"),\n    stage_elem_id="stage",\n)\nsprite: ap.Sprite = ap.Sprite()\nsprite.graphics.begin_fill(color=ap.Color("#00aaff"))\nrectangle: ap.Rectangle = sprite.graphics.draw_rect(x=50, y=50, width=50, height=50)\nanimation_x: ap.AnimationX = rectangle.animation_x(x=100)\nanimation_x.animation_complete(on_animation_complete)\nanimation_x.start()\n```': '```py\n# runnable\nimport apysc as ap\n\n\ndef on_animation_complete(e: ap.AnimationEvent, options: dict) -> None:\n    """\n    The handler that animation calls when its end.\n\n    Parameters\n    ----------\n    e : ap.AnimationEvent\n        Event instance.\n    options : dict\n        Optional arguments dictionary.\n    """\n    ap.trace("Animation is completed!")\n\n\nap.Stage(\n    stage_width=200,\n    stage_height=150,\n    background_color=ap.Color("#333"),\n    stage_elem_id="stage",\n)\nsprite: ap.Sprite = ap.Sprite()\nsprite.graphics.begin_fill(color=ap.Color("#00aaff"))\nrectangle: ap.Rectangle = sprite.graphics.draw_rect(x=50, y=50, width=50, height=50)\nanimation_x: ap.AnimationX = rectangle.animation_x(x=100)\nanimation_x.animation_complete(on_animation_complete)\nanimation_x.start()\n```',  # noqa
    ##################################################
    "## this property": "## this属性",
    ##################################################
    "The `AnimationEvent` instance's `this` property is a subclass instance of the `AnimationBase` class, such as the `AnimationMove`\\, `AnimationX`\\, or other class.": "`AnimationEvent`のインスタンスの`this`属性は`AnimationMove`や`AnimationX`等の`AnimationEvent`クラスのサブクラスになります。",  # noqa
    ##################################################
    "This type depends on the called interface, e.g., if you use the `animation_x` interface, `this` property type becomes an `AnimationX` instance.": "この属性の型は呼んだアニメーションのインターフェイスによって変動します。例えば`animation_x`のインターフェイスであれば`this`属性の型は`AnimationX`クラスのインスタンスとなります。",  # noqa
    ##################################################
    '```py\n# runnable\nimport apysc as ap\n\n\ndef on_animation_complete(e: ap.AnimationEvent, options: dict) -> None:\n    """\n    The handler that animation calls when its end.\n\n    Parameters\n    ----------\n    e : ap.AnimationEvent\n        Event instance.\n    options : dict\n        Optional arguments dictionary.\n    """\n    assert isinstance(e.this, ap.AnimationX)\n\n\nap.Stage(\n    stage_width=200,\n    stage_height=150,\n    background_color=ap.Color("#333"),\n    stage_elem_id="stage",\n)\nsprite: ap.Sprite = ap.Sprite()\nsprite.graphics.begin_fill(color=ap.Color("#00aaff"))\nrectangle: ap.Rectangle = sprite.graphics.draw_rect(x=50, y=50, width=50, height=50)\nanimation_x: ap.AnimationX = rectangle.animation_x(x=100)\nanimation_x.animation_complete(on_animation_complete)\nanimation_x.start()\n```': '```py\n# runnable\nimport apysc as ap\n\n\ndef on_animation_complete(e: ap.AnimationEvent, options: dict) -> None:\n    """\n    The handler that animation calls when its end.\n\n    Parameters\n    ----------\n    e : ap.AnimationEvent\n        Event instance.\n    options : dict\n        Optional arguments dictionary.\n    """\n    assert isinstance(e.this, ap.AnimationX)\n\n\nap.Stage(\n    stage_width=200,\n    stage_height=150,\n    background_color=ap.Color("#333"),\n    stage_elem_id="stage",\n)\nsprite: ap.Sprite = ap.Sprite()\nsprite.graphics.begin_fill(color=ap.Color("#00aaff"))\nrectangle: ap.Rectangle = sprite.graphics.draw_rect(x=50, y=50, width=50, height=50)\nanimation_x: ap.AnimationX = rectangle.animation_x(x=100)\nanimation_x.animation_complete(on_animation_complete)\nanimation_x.start()\n```',  # noqa
    ##################################################
    "## Generic type annotation": "## ジェネリックの型アノテーション",
    ##################################################
    "The `AnimationEvent` class can set a generic type annotation. If you set a generic type annotation, then the animation target property type (e.g., `DisplayObject`) changes.": "`AnimationEvent`クラスはジェネリックの型アノテーションを行うことができます。もし型アノテーションをした場合にはアニメーション対象の値となる`target`属性は（`DisplayObject`などの）型アノテーションを行った型のインスタンスになります。",  # noqa
    ##################################################
    "The following example sets a `Rectangle` generic type annotation to the `AnimationEvent` and benefits from type checking libraries (such as the `mypy` or `Pylance`).": "以下のコードでは`AnimationEvent`の値に`Rectangle`のジェネリックの型アノテーションを行っており、mypyやPylanceなどでの型チェックのライブラリやエディタなどでの恩恵を受けることができます。",  # noqa
    ##################################################
    '```py\n# runnable\nimport apysc as ap\n\n\ndef on_animation_complete(e: ap.AnimationEvent[ap.Rectangle], options: dict) -> None:\n    """\n    The handler that animation calls when its end.\n\n    Parameters\n    ----------\n    e : ap.AnimationEvent\n        Event instance.\n    options : dict\n        Optional arguments dictionary.\n    """\n    rectangle: ap.Rectangle = e.this.target\n    rectangle.animation_x(x=50).start()\n\n\nap.Stage(\n    stage_width=200,\n    stage_height=150,\n    background_color=ap.Color("#333"),\n    stage_elem_id="stage",\n)\nsprite: ap.Sprite = ap.Sprite()\nsprite.graphics.begin_fill(color=ap.Color("#00aaff"))\nrectangle: ap.Rectangle = sprite.graphics.draw_rect(x=50, y=50, width=50, height=50)\nanimation_x: ap.AnimationX = rectangle.animation_x(x=100)\nanimation_x.animation_complete(on_animation_complete)\nanimation_x.start()\n```': '```py\n# runnable\nimport apysc as ap\n\n\ndef on_animation_complete(e: ap.AnimationEvent[ap.Rectangle], options: dict) -> None:\n    """\n    The handler that animation calls when its end.\n\n    Parameters\n    ----------\n    e : ap.AnimationEvent\n        Event instance.\n    options : dict\n        Optional arguments dictionary.\n    """\n    rectangle: ap.Rectangle = e.this.target\n    rectangle.animation_x(x=50).start()\n\n\nap.Stage(\n    stage_width=200,\n    stage_height=150,\n    background_color=ap.Color("#333"),\n    stage_elem_id="stage",\n)\nsprite: ap.Sprite = ap.Sprite()\nsprite.graphics.begin_fill(color=ap.Color("#00aaff"))\nrectangle: ap.Rectangle = sprite.graphics.draw_rect(x=50, y=50, width=50, height=50)\nanimation_x: ap.AnimationX = rectangle.animation_x(x=100)\nanimation_x.animation_complete(on_animation_complete)\nanimation_x.start()\n```',  # noqa
    ##################################################
    "## AnimationEvent constructor API": "## AnimationEvent クラスのコンストラクタのAPI",
    ##################################################
    '<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>': '<span class="inconspicuous-txt">特記事項: このAPIドキュメントはドキュメントビルド用のスクリプトによって自動で生成・同期されています。そのためもしかしたらこの節の内容は前節までの内容と重複している場合があります。</span>',  # noqa
    ##################################################
    "**[Interface summary]**": "**[インターフェイス概要]**",
    ##################################################
    "Animation event class.<hr>": "アニメーションイベント用のクラスです。<hr>",
    ##################################################
    "**[Parameters]**": "**[引数]**",
    ##################################################
    "- `this`: AnimationBase": "- `this`: AnimationBase",
    ##################################################
    "  - Animation setting instance.": "  - アニメーションの設定を扱うインスタンス。",
    ##################################################
    "<hr>": "<hr>",
    ##################################################
    "**[Examples]**": "**[コードサンプル]**",
    ##################################################
    '```py\n>>> import apysc as ap\n>>> def on_animation_complete(\n...     e: ap.AnimationEvent[ap.Rectangle], options: dict\n... ) -> None:\n...     rectangle: ap.Rectangle = e.this.target\n>>> stage: ap.Stage = ap.Stage()\n>>> sprite: ap.Sprite = ap.Sprite()\n>>> sprite.graphics.begin_fill(color=ap.Color("#0af"))\n>>> rectangle: ap.Rectangle = sprite.graphics.draw_rect(\n...     x=50, y=50, width=50, height=50\n... )\n>>> _ = rectangle.animation_x(x=100).animation_complete(on_animation_complete)\n```': '```py\n>>> import apysc as ap\n>>> def on_animation_complete(\n...     e: ap.AnimationEvent[ap.Rectangle], options: dict\n... ) -> None:\n...     rectangle: ap.Rectangle = e.this.target\n>>> stage: ap.Stage = ap.Stage()\n>>> sprite: ap.Sprite = ap.Sprite()\n>>> sprite.graphics.begin_fill(color=ap.Color("#0af"))\n>>> rectangle: ap.Rectangle = sprite.graphics.draw_rect(\n...     x=50, y=50, width=50, height=50\n... )\n>>> _ = rectangle.animation_x(x=100).animation_complete(on_animation_complete)\n```',  # noqa
    ##################################################
    "## this property API": "## this 属性のAPI",
    ##################################################
    '<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>': '<span class="inconspicuous-txt">特記事項: このAPIドキュメントはドキュメントビルド用のスクリプトによって自動で生成・同期されています。そのためもしかしたらこの節の内容は前節までの内容と重複している場合があります。</span>',  # noqa
    ##################################################
    "**[Interface summary]**": "**[インターフェイス概要]**",
    ##################################################
    "Get an animation setting instance of listening to this event.<hr>": "このイベントのリスナーとしてのアニメーション設定のインスタンスを取得します。<hr>",  # noqa
    ##################################################
    "**[Returns]**": "**[返却値]**",
    ##################################################
    "- `this`: AnimationBase": "- `this`: AnimationBase",
    ##################################################
    "  - Instance of listening to this event.": "  - このイベントのハンドラが設定されているインスタンス。",
    ##################################################
    "<hr>": "<hr>",
    ##################################################
    "**[Examples]**": "**[コードサンプル]**",
    ##################################################
    '```py\n>>> import apysc as ap\n>>> def on_animation_complete(\n...     e: ap.AnimationEvent[ap.Rectangle], options: dict\n... ) -> None:\n...     rectangle: ap.Rectangle = e.this.target\n>>> stage: ap.Stage = ap.Stage()\n>>> sprite: ap.Sprite = ap.Sprite()\n>>> sprite.graphics.begin_fill(color=ap.Color("#0af"))\n>>> rectangle: ap.Rectangle = sprite.graphics.draw_rect(\n...     x=50, y=50, width=50, height=50\n... )\n>>> _ = rectangle.animation_x(x=100).animation_complete(on_animation_complete)\n```': '```py\n>>> import apysc as ap\n>>> def on_animation_complete(\n...     e: ap.AnimationEvent[ap.Rectangle], options: dict\n... ) -> None:\n...     rectangle: ap.Rectangle = e.this.target\n>>> stage: ap.Stage = ap.Stage()\n>>> sprite: ap.Sprite = ap.Sprite()\n>>> sprite.graphics.begin_fill(color=ap.Color("#0af"))\n>>> rectangle: ap.Rectangle = sprite.graphics.draw_rect(\n...     x=50, y=50, width=50, height=50\n... )\n>>> _ = rectangle.animation_x(x=100).animation_complete(on_animation_complete)\n```',  # noqa
}
