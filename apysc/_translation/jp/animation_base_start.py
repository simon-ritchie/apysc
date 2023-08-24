"""This module is for the translation mapping data of the
following document:

Document file: animation_base_start.md
Language: jp
"""

from typing import Dict

MAPPING: Dict[str, str] = {
    ##################################################
    "# AnimationBase class start interface": "# AnimationBaseクラス start インターフェイス",
    ##################################################
    "This page explains the `AnimationBase` class `start` method interface.": "このページでの`AnimationBase`クラスの`start`メソッドのインターフェイスについて説明します。",  # noqa
    ##################################################
    "## What interface is this?": "## インターフェイス概要",
    ##################################################
    "The `start` method interface starts the target animation. Each animation interface returns the `AnimationBase` subclass instance is when you call each animation interface, such as the `animation_move` or `animation_x`\\, and it has the `start` method.": "`start`メソッドは対象のアニメーションを開始します。各アニメーションのインターフェイスは`AnimationBase`クラスのサブクラスのインスタンスを返却します。例えば`animation_move`や`animation_x`などが該当し、それらのインスタンスはこの`start`メソッドを持っています。",  # noqa
    ##################################################
    "## Basic usage": "## 基本的な使い方",
    ##################################################
    "Notes: you need to call the `start` method to start an animation after the calling of the animation method, such as the `animation_x`\\, as follows:": "特記事項: 以下のコードのようにアニメーションを開始するには`animation_x`などの各アニメーションのインターフェイスを呼び出した後に`start`メソッドを呼ぶ必要があります。",  # noqa
    ##################################################
    '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    stage_width=200,\n    stage_height=150,\n    background_color=ap.Color("#333"),\n    stage_elem_id="stage",\n)\nsprite: ap.Sprite = ap.Sprite()\nsprite.graphics.begin_fill(color=ap.Color("#0af"))\nrectangle: ap.Rectangle = sprite.graphics.draw_rect(x=50, y=50, width=50, height=50)\n\nanimation_x: ap.AnimationX = rectangle.animation_x(x=100, duration=3000, delay=3000)\nanimation_x.start()\n\nap.save_overall_html(dest_dir_path="./animation_base_start_basic_usage_1/")\n```': '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    stage_width=200,\n    stage_height=150,\n    background_color=ap.Color("#333"),\n    stage_elem_id="stage",\n)\nsprite: ap.Sprite = ap.Sprite()\nsprite.graphics.begin_fill(color=ap.Color("#0af"))\nrectangle: ap.Rectangle = sprite.graphics.draw_rect(x=50, y=50, width=50, height=50)\n\nanimation_x: ap.AnimationX = rectangle.animation_x(x=100, duration=3000, delay=3000)\nanimation_x.start()\n\nap.save_overall_html(dest_dir_path="./animation_base_start_basic_usage_1/")\n```',  # noqa
    ##################################################
    "You can also use the method chain for code simplicity:": "シンプルに書くためにメソッドチェーンを使う形でも書くことができます:",  # noqa
    ##################################################
    '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    stage_width=200,\n    stage_height=150,\n    background_color=ap.Color("#333"),\n    stage_elem_id="stage",\n)\nsprite: ap.Sprite = ap.Sprite()\nsprite.graphics.begin_fill(color=ap.Color("#0af"))\nrectangle: ap.Rectangle = sprite.graphics.draw_rect(x=50, y=50, width=50, height=50)\n\nrectangle.animation_x(x=100, duration=3000, delay=3000).start()\n\nap.save_overall_html(dest_dir_path="./animation_base_start_basic_usage_2/")\n```': '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    stage_width=200,\n    stage_height=150,\n    background_color=ap.Color("#333"),\n    stage_elem_id="stage",\n)\nsprite: ap.Sprite = ap.Sprite()\nsprite.graphics.begin_fill(color=ap.Color("#0af"))\nrectangle: ap.Rectangle = sprite.graphics.draw_rect(x=50, y=50, width=50, height=50)\n\nrectangle.animation_x(x=100, duration=3000, delay=3000).start()\n\nap.save_overall_html(dest_dir_path="./animation_base_start_basic_usage_2/")\n```',  # noqa
    ##################################################
    "## start API": "## start API",
    ##################################################
    '<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>': '<span class="inconspicuous-txt">特記事項: このAPIドキュメントはドキュメントビルド用のスクリプトによって自動で生成・同期されています。そのためもしかしたらこの節の内容は前節までの内容と重複している場合があります。</span>',  # noqa
    ##################################################
    "**[Interface summary]**": "**[インターフェイス概要]**",
    ##################################################
    "Start an animation with current settings.<hr>": "現在の設定を使ってアニメーションを開始します。<hr>",
    ##################################################
    "**[Returns]**": "**[返却値]**",
    ##################################################
    "- `self`: AnimatonBase": "- `self`: AnimatonBase",
    ##################################################
    "  - This instance.": "  - このインスタンス。",
    ##################################################
    "<hr>": "<hr>",
    ##################################################
    "**[Examples]**": "**[コードサンプル]**",
    ##################################################
    '```py\n>>> import apysc as ap\n>>> stage: ap.Stage = ap.Stage()\n>>> sprite: ap.Sprite = ap.Sprite()\n>>> sprite.graphics.begin_fill(color=ap.Color("#0af"))\n>>> rectangle: ap.Rectangle = sprite.graphics.draw_rect(\n...     x=50, y=50, width=50, height=50\n... )\n>>> _ = rectangle.animation_x(x=100).start()\n```': '```py\n>>> import apysc as ap\n>>> stage: ap.Stage = ap.Stage()\n>>> sprite: ap.Sprite = ap.Sprite()\n>>> sprite.graphics.begin_fill(color=ap.Color("#0af"))\n>>> rectangle: ap.Rectangle = sprite.graphics.draw_rect(\n...     x=50, y=50, width=50, height=50\n... )\n>>> _ = rectangle.animation_x(x=100).start()\n```',  # noqa
}
