"""This module is for the translation mapping data of the
following document:

Document file: enter_frame.md
Language: jp
"""

from typing import Dict

MAPPING: Dict[str, str] = {
    ##################################################
    "# enter_frame interface": "# enter_frame インターフェイス",
    ##################################################
    "This page explains the `enter_frame` method interface.": "このページでは`enter_frame`メソッドのインターフェイスについて説明します。",  # noqa
    ##################################################
    "## What interface is this?": "## インターフェイス概要",
    ##################################################
    "The `enter_frame` interface sets a handler for an animation.": "`enter_frame`インターフェイスはアニメーションのためのハンドラを設定します。",  # noqa
    ##################################################
    "This interface calls a specified handler at each frame.": "このインターフェイスでは指定されたハンドラを各フレームごとに呼び出します。",  # noqa
    ##################################################
    "## Which should we use, the Timer class or the enter_frame interface?": "## Timer クラスと enter_frame のインターフェイスのどちらを使うべきか",  # noqa
    ##################################################
    "The `Timer` class also can handle animation.": "`Timer`クラスでも同様にアニメーションを扱うことができます。",  # noqa
    ##################################################
    "So, Which should we use, the `Timer` class or the `enter_frame` interface for an animation?": "そのため、アニメーション用途の場合`Timer`クラスと`enter_frame`のインターフェイスのどちらを使うべきなのでしょうか？",  # noqa
    ##################################################
    "The answer is, basically, the `enter_frame`.": "回答としては基本的には`enter_frame`側となります。",
    ##################################################
    "The `enter_frame` interface is less likely to shift the pace of handler calling.": "`enter_frame`のインターフェイスはハンドラの呼び出しの間隔が`Timer`クラスよりもずれにくくなっています。",  # noqa
    ##################################################
    "On the other hand, the `Timer` class's calling timing can be off if a CPU is busy.": "一方で、`Timer`クラス側はCPU負荷が高い場合などに呼び出しタイミングがずれるケースが発生します。",  # noqa
    ##################################################
    "## Basic usage": "## 基本的な使い方",
    ##################################################
    "The `enter_frame` interface exists in classes, such as the `Stage` or `Sprite`.": "`enter_frame`インターフェイスは`Stage`や`Sprite`などのクラスに存在します。",  # noqa
    ##################################################
    "The `enter_frame` interface requires the `handler` argument (callable object, such as the function or method).": "`enter_frame`インターフェイスは`handler`引数（関数やメソッドなどのcallableオブジェクト）の指定を必要とします。",  # noqa
    ##################################################
    "The `fps` argument is optional and determines an animation's frame rate (it accepts the `FPS` enum).": "`fps`引数は省略可で、この引数はフレームレートを決定します（`FPS`のenumの指定が可能です）。",  # noqa
    ##################################################
    "Also, the `options` argument is an optional dictionary and passes optional parameters to a handler.": "また、`options`引数も省略可であり、この指定はハンドラへと追加のパラメーターを渡すことができます。",  # noqa
    ##################################################
    '```py\n# runnable\nimport apysc as ap\n\nstage: ap.Stage = ap.Stage(\n    stage_width=150,\n    stage_height=150,\n    background_color="#333",\n    stage_elem_id="stage",\n)\nrectangle: ap.Rectangle = ap.Rectangle(\n    x=50, y=50, width=50, height=50, fill_color="#0af"\n)\n\n\ndef on_enter_frame(e: ap.EnterFrameEvent, options: dict) -> None:\n    """\n    The handler to handle an enter frame event.\n\n    Parameters\n    ----------\n    e : ap.EnterFrameEvent\n        Event instance.\n    options : dict\n        Optional argument dictionary.\n    """\n    rectangle.rotation_around_center += 1\n\n\nstage.enter_frame(handler=on_enter_frame, fps=ap.FPS.FPS_30)\nap.save_overall_html(dest_dir_path="enter_frame_basic_usage/")\n```': '```py\n# runnable\nimport apysc as ap\n\nstage: ap.Stage = ap.Stage(\n    stage_width=150,\n    stage_height=150,\n    background_color="#333",\n    stage_elem_id="stage",\n)\nrectangle: ap.Rectangle = ap.Rectangle(\n    x=50, y=50, width=50, height=50, fill_color="#0af"\n)\n\n\ndef on_enter_frame(e: ap.EnterFrameEvent, options: dict) -> None:\n    """\n    The handler to handle an enter frame event.\n\n    Parameters\n    ----------\n    e : ap.EnterFrameEvent\n        Event instance.\n    options : dict\n        Optional argument dictionary.\n    """\n    rectangle.rotation_around_center += 1\n\n\nstage.enter_frame(handler=on_enter_frame, fps=ap.FPS.FPS_30)\nap.save_overall_html(dest_dir_path="enter_frame_basic_usage/")\n```',  # noqa
    ##################################################
    "## See also": "## 関連資料",
    ##################################################
    "- [Timer class](timer.md)": "- [Timer クラス](jp_timer.md)",
    ##################################################
    "- [FPS enum](fps.md)": "- [FPS の enum](jp_fps.md)",
    ##################################################
    "## enter_frame API": "## enter_frame のAPI",
    ##################################################
    '<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>': '<span class="inconspicuous-txt">特記事項: このAPIドキュメントはドキュメントビルド用のスクリプトによって自動で生成・同期されています。そのためもしかしたらこの節の内容は前節までの内容と重複している場合があります。</span>',  # noqa
    ##################################################
    "**[Interface summary]**": "**[インターフェイス概要]**",
    ##################################################
    "Add an enter frame event listener setting.<hr>": "enter frameのイベントのリスナー設定を追加します。<hr>",  # noqa
    ##################################################
    "**[Parameters]**": "**[引数]**",
    ##################################################
    "- `handler`: Callable[[EnterFrameEvent, _Options], None]": "- `handler`: Callable[[EnterFrameEvent, _Options], None]",  # noqa
    ##################################################
    "  - A handler function to handle the enter frame event.": "  - enter frameイベントを扱うためのハンドラの関数。",  # noqa
    ##################################################
    "- `fps`: FPS, default FPS.FPS_60": "- `fps`: FPS, default FPS.FPS_60",
    ##################################################
    "  - Frame per second to set.": "  - 設定する1秒辺りのフレーム数（frame per second）。",
    ##################################################
    "- `options`: Optional[_Options], optional": "- `options`: Optional[_Options], optional",  # noqa
    ##################################################
    "  - Optional arguments to pass to a handler function.": "  - ハンドラの関数へと渡される追加のパラメーターの引数値。",  # noqa
    ##################################################
    "<hr>": "<hr>",
    ##################################################
    "**[Notes]**": "**[特記事項]**",
    ##################################################
    "If this is the second call of this interface and an argument is the same function, this interface ignores `options` argument (it changes only the running status and `fps` setting).<hr>": "もしこのインターフェイスの呼び出しが2回目且つ指定されたハンドラの引数の値が同一の場合、このインターフェイスは`options`引数の指定を無視します（実行中かどうかのステータスと`fps`の設定のみ更新します）。<hr>",  # noqa
    ##################################################
    "**[Examples]**": "**[コードサンプル]**",
    ##################################################
    '```py\n>>> import apysc as ap\n>>> stage: ap.Stage = ap.Stage()\n>>> rectangle: ap.Rectangle = ap.Rectangle(\n...     x=50, y=50, width=50, height=50, fill_color="#0af"\n... )\n>>> def on_enter_frame(e: ap.EnterFrameEvent, options: dict) -> None:\n...     rectangle.x += 1\n>>> stage.enter_frame(handler=on_enter_frame, fps=ap.FPS.FPS_30)\n```': '```py\n>>> import apysc as ap\n>>> stage: ap.Stage = ap.Stage()\n>>> rectangle: ap.Rectangle = ap.Rectangle(\n...     x=50, y=50, width=50, height=50, fill_color="#0af"\n... )\n>>> def on_enter_frame(e: ap.EnterFrameEvent, options: dict) -> None:\n...     rectangle.x += 1\n>>> stage.enter_frame(handler=on_enter_frame, fps=ap.FPS.FPS_30)\n```',  # noqa
}
