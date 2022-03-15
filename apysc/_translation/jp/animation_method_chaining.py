"""This module is for the translation mapping data of the
following document:

Document file: animation_method_chaining.md
Language: jp
"""

from typing import Dict

MAPPING: Dict[str, str] = {

    '# AnimationBase class interfaces method chaining':
    '# AnimationBase クラスのインターフェイスのメソッドチェーン',

    'This page describes the method chaining of the animation interfaces.':
    'このページでは各アニメーションのインターフェイスのメソッドチェーンについて説明します。',

    '## Each AnimationBase related interface returns its instance':
    '## AnimationBaseクラスに関係した各インターフェイスは自身のインスタンスを返却します',

    'Each `AnimationBase` class-related interface (such as the `animation_x`\\, `start`\\, `animation_complete`) returns its instance. So that these interfaces can be used with the method chaining, as follows (method chaining of the `animation_x`\\, `animation_complete`\\, and `start` methods):':  # noqa
    '`animation_x`や`start`、`animation_complete`メソッドなどの`AnimationBase`クラスに絡んだ各インターフェイスは自身のインスタンスを返却します。それを利用して以下のコード例のようにメソッドチェーンを利用することができます（`animation_x`、`animation_complete`、`start`の各インターフェイスで利用しています）。',  # noqa

    '```py\n# runnable\nimport apysc as ap\n\n\ndef on_animation_complete(\n        e: ap.AnimationEvent[ap.Rectangle], options: dict) -> None:\n    """\n    The handler that the animation calls when its end.\n\n    Parameters\n    ----------\n    e : AnimationEvent\n        Event instance.\n    options : dict\n        Optional arguments dictionary.\n    """\n    ap.trace(\'Animation is completed!\')\n\n\nap.Stage(\n    stage_width=200, stage_height=150,\n    background_color=\'#333\', stage_elem_id=\'stage\')\nsprite: ap.Sprite = ap.Sprite()\nsprite.graphics.begin_fill(color=\'#00aaff\')\nrectangle: ap.Rectangle = sprite.graphics.draw_rect(\n    x=50, y=50, width=50, height=50)\nrectangle.animation_x(\n    x=100,\n    duration=1000,\n).animation_complete(on_animation_complete).start()\n\nap.save_overall_html(\n    dest_dir_path=\'./animation_method_chaining_basic_usage_1/\')\n```':  # noqa
    '```py\n# runnable\nimport apysc as ap\n\n\ndef on_animation_complete(\n        e: ap.AnimationEvent[ap.Rectangle], options: dict) -> None:\n    """\n    The handler that the animation calls when its end.\n\n    Parameters\n    ----------\n    e : AnimationEvent\n        Event instance.\n    options : dict\n        Optional arguments dictionary.\n    """\n    ap.trace(\'Animation is completed!\')\n\n\nap.Stage(\n    stage_width=200, stage_height=150,\n    background_color=\'#333\', stage_elem_id=\'stage\')\nsprite: ap.Sprite = ap.Sprite()\nsprite.graphics.begin_fill(color=\'#00aaff\')\nrectangle: ap.Rectangle = sprite.graphics.draw_rect(\n    x=50, y=50, width=50, height=50)\nrectangle.animation_x(\n    x=100,\n    duration=1000,\n).animation_complete(on_animation_complete).start()\n\nap.save_overall_html(\n    dest_dir_path=\'./animation_method_chaining_basic_usage_1/\')\n```',  # noqa

    'These method chainings are sometimes useful for code simplicity.':
    'これらのメソッドチェーンの記述はコードの記述をシンプルにしたい際に役立つことがあります。',

    'If you want to chain the methods like JavaScript (e.g., `D3.js`), you can use backslashes at the line end, as follows:':  # noqa
    'もしD3.jsなどでのJavaScriptでの記述に近い形でメソッドチェーンを使いたい場合には以下のコード例のように行末にバックスラッシュを記述することで設定することができます:',  # noqa

    '```py\n# runnable\nimport apysc as ap\n\n\ndef on_animation_complete(\n        e: ap.AnimationEvent[ap.Rectangle], options: dict) -> None:\n    """\n    The handler that the animation calls when its end.\n\n    Parameters\n    ----------\n    e : AnimationEvent\n        Event instance.\n    options : dict\n        Optional arguments dictionary.\n    """\n    ap.trace(\'Animation is completed!\')\n\n\nap.Stage(\n    stage_width=200, stage_height=150,\n    background_color=\'#333\', stage_elem_id=\'stage\')\nsprite: ap.Sprite = ap.Sprite()\nsprite.graphics.begin_fill(color=\'#00aaff\')\nrectangle: ap.Rectangle = sprite.graphics.draw_rect(\n    x=50, y=50, width=50, height=50)\nrectangle\\\n    .animation_x(x=100, duration=1000)\\\n    .animation_complete(on_animation_complete)\\\n    .start()\n\nap.save_overall_html(\n    dest_dir_path=\'./animation_method_chaining_basic_usage_2/\')\n```':  # noqa
    '```py\n# runnable\nimport apysc as ap\n\n\ndef on_animation_complete(\n        e: ap.AnimationEvent[ap.Rectangle], options: dict) -> None:\n    """\n    The handler that the animation calls when its end.\n\n    Parameters\n    ----------\n    e : AnimationEvent\n        Event instance.\n    options : dict\n        Optional arguments dictionary.\n    """\n    ap.trace(\'Animation is completed!\')\n\n\nap.Stage(\n    stage_width=200, stage_height=150,\n    background_color=\'#333\', stage_elem_id=\'stage\')\nsprite: ap.Sprite = ap.Sprite()\nsprite.graphics.begin_fill(color=\'#00aaff\')\nrectangle: ap.Rectangle = sprite.graphics.draw_rect(\n    x=50, y=50, width=50, height=50)\nrectangle\\\n    .animation_x(x=100, duration=1000)\\\n    .animation_complete(on_animation_complete)\\\n    .start()\n\nap.save_overall_html(\n    dest_dir_path=\'./animation_method_chaining_basic_usage_2/\')\n```',  # noqa

}
