"""This module is for the translation mapping data of the
following document:

Document file: sequential_animation.md
Language: jp
"""

from typing import Dict

MAPPING: Dict[str, str] = {
    ##################################################
    "# Sequential animation setting": "# 連続したアニメーション設定",
    ##################################################
    "This page explains how to animate sequentially.": "このページではアニメーションを連続させて再生する方法について説明します。",  # noqa
    ##################################################
    "## Sequential animation interface calling on the same instance": "## 同じインスタンス上でアニメーションのインターフェイスを連続して呼び出す",  # noqa
    ##################################################
    "If you call each animation interface sequentially, these animations start in order (e.g., when the first animation completes, the second one starts).": "アニメーションのインターフェイスを連続して呼び出した場合、各アニメーションは順番にスタートします（例えば、最初のアニメーションが終わったら次のアニメーションの再生がスタートじます）。",  # noqa
    ##################################################
    "The following example sets the four animations of the coordinates. These animations do not start simultaneously:": "以下のコード例では4つの座標のアニメーションを設定しています。これらのアニメーションは同時にはスタートしません:",  # noqa
    ##################################################
    '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    stage_width=200,\n    stage_height=200,\n    background_color=ap.Color("#333"),\n    stage_elem_id="stage",\n)\nsprite: ap.Sprite = ap.Sprite()\nsprite.graphics.begin_fill(color=ap.Color("#0af"))\n\nrectangle: ap.Rectangle = sprite.graphics.draw_rect(x=50, y=50, width=50, height=50)\neasing: ap.Easing = ap.Easing.EASE_OUT_QUINT\nrectangle.animation_x(x=100, duration=1000, delay=1000, easing=easing).start()\nrectangle.animation_y(y=100, duration=1000, delay=1000, easing=easing).start()\nrectangle.animation_x(x=50, duration=1000, delay=1000, easing=easing).start()\nrectangle.animation_y(y=50, duration=1000, delay=1000, easing=easing).start()\n\nap.save_overall_html(dest_dir_path="sequential_animation_example_1/")\n```': '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    stage_width=200,\n    stage_height=200,\n    background_color=ap.Color("#333"),\n    stage_elem_id="stage",\n)\nsprite: ap.Sprite = ap.Sprite()\nsprite.graphics.begin_fill(color=ap.Color("#0af"))\n\nrectangle: ap.Rectangle = sprite.graphics.draw_rect(x=50, y=50, width=50, height=50)\neasing: ap.Easing = ap.Easing.EASE_OUT_QUINT\nrectangle.animation_x(x=100, duration=1000, delay=1000, easing=easing).start()\nrectangle.animation_y(y=100, duration=1000, delay=1000, easing=easing).start()\nrectangle.animation_x(x=50, duration=1000, delay=1000, easing=easing).start()\nrectangle.animation_y(y=50, duration=1000, delay=1000, easing=easing).start()\n\nap.save_overall_html(dest_dir_path="sequential_animation_example_1/")\n```',  # noqa
    ##################################################
    "## animation_complete handler setting": "## animation_complete のハンドラ設定",
    ##################################################
    "Also, you can use the `animation_complete` interface to register a handler for the sequential animation. For the details, please see:": "また、`animation_complete`インターフェイスを使ってアニメーション終了時のハンドラを設定して連続したアニメーションを設定することもできます。詳細は以下をご確認ください:",  # noqa
    ##################################################
    "- [animation_complete interface](animation_complete.md)": "- [animation_complete インターフェイス](jp_animation_complete.md)",  # noqa
    ##################################################
    "## See also": "## 関連資料",
    ##################################################
    "If you want to animate multiple animations simultaneously, you can use the following interface:": "もしも複数のアニメーションを同時に再生したい場合、以下のインターフェイスをお使いください。",  # noqa
    ##################################################
    "- [animation_parallel interface](animation_parallel.md)": "- [animation_parallel インターフェイス](jp_animation_parallel.md)",  # noqa
}
