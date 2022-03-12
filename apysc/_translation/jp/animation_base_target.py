"""This module is for the translation mapping data of the
following document:

Document file: animation_base_target.md
Language: jp
"""

from typing import Dict

MAPPING: Dict[str, str] = {

    '# AnimationBase class target property interface':
    '# AnimationBase クラス target 属性のインターフェイス',

    'This page explains the `AnimationBase` class `target` property interface.':  # noqa
    'このページでは`AnimationBase`クラスの`target`属性のインターフェイスについて説明します。',

    '## What property is this?':
    '## 属性の概要',

    'The `target` property returns the animation target instance (e.g., `Sprite`\\, `Rectangle`).':  # noqa
    '`target`属性はアニメーション対象のインスタンス（例: `Sprite`や`Rectangle`などのインスタンス）を返却します。',

    '## Basic usage':
    '## 基本的な使い方',

    'Each subclass of the `AnimationBase` (e.g., `AnimationMove`\\, `AnimationX`) has the `target` getter property.':  # noqa
    '`AnimationBase`クラスの各サブクラス（例: `AnimationMove`や`AnimationX`クラスなど）はgetterの`target`属性を持っています。',  # noqa

    '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    stage_width=200, stage_height=150,\n    background_color=\'#333\', stage_elem_id=\'stage\')\nsprite: ap.Sprite = ap.Sprite()\nsprite.graphics.begin_fill(color=\'#00aaff\')\nrectangle: ap.Rectangle = sprite.graphics.draw_rect(\n    x=50, y=50, width=50, height=50)\nanimation_x: ap.AnimationX = rectangle.animation_x(x=100)\nassert isinstance(animation_x.target, ap.Rectangle)\n```':  # noqa
    '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    stage_width=200, stage_height=150,\n    background_color=\'#333\', stage_elem_id=\'stage\')\nsprite: ap.Sprite = ap.Sprite()\nsprite.graphics.begin_fill(color=\'#00aaff\')\nrectangle: ap.Rectangle = sprite.graphics.draw_rect(\n    x=50, y=50, width=50, height=50)\nanimation_x: ap.AnimationX = rectangle.animation_x(x=100)\nassert isinstance(animation_x.target, ap.Rectangle)\n```',  # noqa

    '## Generic type annotation setting':
    '## ジェネリックの型アノテーションについて',

    'The `AnimationBase` class and its subclasses can set a generic type annotation. For example, the `target` property type becomes its type if you set it.':  # noqa
    '`AnimationBase`クラスとその各サブクラスにはジェネリックの型アノテーションを行うことができます。型アノテーションをした場合`target`属性の型はその型のインスタンスとなります。',  # noqa

    'The following code sets the `[ap.Rectangle]` generic type annotation:':
    '以下のコードでは`[ap.Rectangle]`というジェネリックの型アノテーションを行っています。',

    '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    stage_width=200, stage_height=150,\n    background_color=\'#333\', stage_elem_id=\'stage\')\nsprite: ap.Sprite = ap.Sprite()\nsprite.graphics.begin_fill(color=\'#00aaff\')\nrectangle: ap.Rectangle = sprite.graphics.draw_rect(\n    x=50, y=50, width=50, height=50)\nanimation_x: ap.AnimationX[ap.Rectangle] = rectangle.animation_x(x=100)\nassert isinstance(animation_x.target, ap.Rectangle)\n```':  # noqa
    '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    stage_width=200, stage_height=150,\n    background_color=\'#333\', stage_elem_id=\'stage\')\nsprite: ap.Sprite = ap.Sprite()\nsprite.graphics.begin_fill(color=\'#00aaff\')\nrectangle: ap.Rectangle = sprite.graphics.draw_rect(\n    x=50, y=50, width=50, height=50)\nanimation_x: ap.AnimationX[ap.Rectangle] = rectangle.animation_x(x=100)\nassert isinstance(animation_x.target, ap.Rectangle)\n```',  # noqa

    'It is also sometimes useful to annotate generic type to the handler\'s `AnimationEvent`\\. This generic type annotation also affects the `target` type (`e.this.target`), as follows:':  # noqa
    'イベントハンドラの`AnimationEvent`のインスタンスへジェネリックの型アノテーションを行うことも有益なケースがあります。この型アノテーションも`target`属性（`e.this.target`）の型に影響します。',  # noqa

    '```py\n# runnable\nimport apysc as ap\n\n\ndef on_animation_complete(\n        e: ap.AnimationEvent[ap.Rectangle], options: dict) -> None:\n    """\n    The handler the animation calls when its end.\n\n    Parameters\n    ----------\n    e : ap.AnimationEvent\n        Event instance.\n    options : dict\n        Optional arguments dictionary.\n    """\n    rectangle: ap.Rectangle = e.this.target\n    rectangle.animation_x(x=50).start()\n\n\nap.Stage(\n    stage_width=200, stage_height=150,\n    background_color=\'#333\', stage_elem_id=\'stage\')\nsprite: ap.Sprite = ap.Sprite()\nsprite.graphics.begin_fill(color=\'#00aaff\')\nrectangle: ap.Rectangle = sprite.graphics.draw_rect(\n    x=50, y=50, width=50, height=50)\nanimation_x: ap.AnimationX = rectangle.animation_x(x=100)\nanimation_x.animation_complete(on_animation_complete)\n```':  # noqa
    '```py\n# runnable\nimport apysc as ap\n\n\ndef on_animation_complete(\n        e: ap.AnimationEvent[ap.Rectangle], options: dict) -> None:\n    """\n    The handler the animation calls when its end.\n\n    Parameters\n    ----------\n    e : ap.AnimationEvent\n        Event instance.\n    options : dict\n        Optional arguments dictionary.\n    """\n    rectangle: ap.Rectangle = e.this.target\n    rectangle.animation_x(x=50).start()\n\n\nap.Stage(\n    stage_width=200, stage_height=150,\n    background_color=\'#333\', stage_elem_id=\'stage\')\nsprite: ap.Sprite = ap.Sprite()\nsprite.graphics.begin_fill(color=\'#00aaff\')\nrectangle: ap.Rectangle = sprite.graphics.draw_rect(\n    x=50, y=50, width=50, height=50)\nanimation_x: ap.AnimationX = rectangle.animation_x(x=100)\nanimation_x.animation_complete(on_animation_complete)\n```',  # noqa

    '## target property API':
    '## target 属性のAPI',

    '<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>':  # noqa
    '<span class="inconspicuous-txt">特記事項: このAPIドキュメントはドキュメントビルド用のスクリプトによって自動で生成・同期されています。そのためもしかしたらこの節の内容は前節までの内容と重複している場合があります。</span>',  # noqa

    '**[Interface summary]** Get an animation target instance.<hr>':
    '**[インターフェイス概要]** アニメーション対象のインスタンスを取得します。<hr>',

    '**[Returns]**':
    '**[返却値]**',

    '- `target`: VariableNameInterface':
    '- `target`: VariableNameInterface',

    '  - An animation target instance.':
    '  - アニメーション対象のインスタンス。',

    '**[Examples]**':
    '**[コードサンプル]**',

    '```py\n>>> import apysc as ap\n>>> def on_animation_complete(\n...         e: ap.AnimationEvent[ap.Rectangle],\n...         options: dict) -> None:\n...     rectangle: ap.Rectangle = e.this.target\n>>> stage: ap.Stage = ap.Stage()\n>>> sprite: ap.Sprite = ap.Sprite()\n>>> sprite.graphics.begin_fill(color=\'#0af\')\n>>> rectangle: ap.Rectangle = sprite.graphics.draw_rect(\n...     x=50, y=50, width=50, height=50)\n>>> _ = rectangle.animation_x(\n...     x=100,\n... ).animation_complete(on_animation_complete).start()\n```':  # noqa
    '```py\n>>> import apysc as ap\n>>> def on_animation_complete(\n...         e: ap.AnimationEvent[ap.Rectangle],\n...         options: dict) -> None:\n...     rectangle: ap.Rectangle = e.this.target\n>>> stage: ap.Stage = ap.Stage()\n>>> sprite: ap.Sprite = ap.Sprite()\n>>> sprite.graphics.begin_fill(color=\'#0af\')\n>>> rectangle: ap.Rectangle = sprite.graphics.draw_rect(\n...     x=50, y=50, width=50, height=50)\n>>> _ = rectangle.animation_x(\n...     x=100,\n... ).animation_complete(on_animation_complete).start()\n```',  # noqa

}
