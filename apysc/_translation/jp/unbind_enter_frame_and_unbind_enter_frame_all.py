"""This module is for the translation mapping data of the
following document:

Document file: unbind_enter_frame_and_unbind_enter_frame_all.md
Language: jp
"""

from typing import Dict

MAPPING: Dict[str, str] = {
    ##################################################
    "# unbind_enter_frame and unbind_enter_frame_all interfaces": "# unbind_enter_frame と unbind_enter_frame_all の各インターフェイス",  # noqa
    ##################################################
    "This page explains the `unbind_enter_frame` and `unbind_enter_frame_all` methods interfaces.": "このページでは`unbind_enter_frame`と`unbind_enter_frame_all`メソッドの各インターフェイスについて説明します。",  # noqa
    ##################################################
    "## What interfaces are these?": "## 各インターフェイスの概要",
    ##################################################
    "The `unbind_enter_frame` and `unbind_enter_frame_all` methods disable an enter frame event's handler setting(s).": "`unbind_enter_frame`と`unbind_enter_frame_all`メソッドの各インターフェイスはenter frameイベントのハンドラ設定を取り除きます。",  # noqa
    ##################################################
    "The `unbind_enter_frame` interface disables a specified single handler, and the `unbind_enter_frame_all` interface disables all handlers.": "`unbind_enter_frame`インターフェイスは指定された一つのハンドラを無効化し、`unbind_enter_frame_all`インターフェイスはすべてのハンドラ設定を無効化します。",  # noqa
    ##################################################
    "## Basic usage": "## 基本的な使い方",
    ##################################################
    "The `unbind_enter_frame` interface requires the `handler` argument.": "`unbind_enter_frame`インターフェイスは`handler`引数の指定を必要とします。",  # noqa
    ##################################################
    "In addition, this interface raises an exception if a specified `handler` is not registered yet.": "加えて、このインターフェイスはもし指定されたハンドラがまだ未設定だった場合にはエラーとなります。",  # noqa
    ##################################################
    "In the following example, if you click the rectangle, the handler disables an enter frame event.": "以下の例では、四角をクリックした際にenter frameのイベントを無効化しています。",  # noqa
    ##################################################
    '```py\n# runnable\nimport apysc as ap\n\nstage: ap.Stage = ap.Stage(\n    stage_width=150,\n    stage_height=150,\n    background_color="#333",\n    stage_elem_id="stage",\n)\nrectangle: ap.Rectangle = ap.Rectangle(\n    x=50, y=50, width=50, height=50, fill_color="#0af"\n)\n\n\ndef on_enter_frame(e: ap.EnterFrameEvent, options: dict) -> None:\n    """\n    The handler to handle an enter frame event.\n\n    Parameters\n    ----------\n    e : ap.EnterFrameEvent\n        Event instance.\n    options : dict\n        Optional argument dictionary.\n    """\n    rectangle.rotation_around_center += 1\n\n\ndef on_rectangle_click(\n    e: ap.MouseEvent[ap.Rectangle],\n    options: dict,\n) -> None:\n    """\n    The handler to handle a rectangle click event.\n\n    Parameters\n    ----------\n    e : ap.MouseEvent\n        Event instance.\n    options : dict\n        Optional argument dictionary.\n    """\n    stage.unbind_enter_frame(handler=on_enter_frame)\n\n\nstage.enter_frame(handler=on_enter_frame, fps=ap.FPS.FPS_30)\nrectangle.click(handler=on_rectangle_click)\nap.save_overall_html(dest_dir_path="unbind_enter_frame_basic_usage/")\n```': '```py\n# runnable\nimport apysc as ap\n\nstage: ap.Stage = ap.Stage(\n    stage_width=150,\n    stage_height=150,\n    background_color="#333",\n    stage_elem_id="stage",\n)\nrectangle: ap.Rectangle = ap.Rectangle(\n    x=50, y=50, width=50, height=50, fill_color="#0af"\n)\n\n\ndef on_enter_frame(e: ap.EnterFrameEvent, options: dict) -> None:\n    """\n    The handler to handle an enter frame event.\n\n    Parameters\n    ----------\n    e : ap.EnterFrameEvent\n        Event instance.\n    options : dict\n        Optional argument dictionary.\n    """\n    rectangle.rotation_around_center += 1\n\n\ndef on_rectangle_click(\n    e: ap.MouseEvent[ap.Rectangle],\n    options: dict,\n) -> None:\n    """\n    The handler to handle a rectangle click event.\n\n    Parameters\n    ----------\n    e : ap.MouseEvent\n        Event instance.\n    options : dict\n        Optional argument dictionary.\n    """\n    stage.unbind_enter_frame(handler=on_enter_frame)\n\n\nstage.enter_frame(handler=on_enter_frame, fps=ap.FPS.FPS_30)\nrectangle.click(handler=on_rectangle_click)\nap.save_overall_html(dest_dir_path="unbind_enter_frame_basic_usage/")\n```',  # noqa
    ##################################################
    "The `unbind_enter_frame_all` interface requires no argument.": "`unbind_enter_frame_all`インターフェイスは引数の指定を必要としません。",  # noqa
    ##################################################
    "In the following example, if you click any rectangle, the handler disables all enter frame events.": "以下の例では四角をクリックした際にすべてのenter frameのイベントを無効化しています。",  # noqa
    ##################################################
    '```py\n# runnable\nimport apysc as ap\n\nstage: ap.Stage = ap.Stage(\n    stage_width=250,\n    stage_height=150,\n    background_color="#333",\n    stage_elem_id="stage",\n)\nleft_rectangle: ap.Rectangle = ap.Rectangle(\n    x=50, y=50, width=50, height=50, fill_color="#0af"\n)\nright_rectangle: ap.Rectangle = ap.Rectangle(\n    x=150, y=50, width=50, height=50, fill_color="#f0a"\n)\n\n\ndef on_enter_frame_1(e: ap.EnterFrameEvent, options: dict) -> None:\n    """\n    The handler to handle an enter frame event.\n\n    Parameters\n    ----------\n    e : ap.EnterFrameEvent\n        Event instance.\n    options : dict\n        Optional argument dictionary.\n    """\n    left_rectangle.rotation_around_center += 1\n\n\ndef on_enter_frame_2(e: ap.EnterFrameEvent, options: dict) -> None:\n    """\n    The handler to handle an enter frame event.\n\n    Parameters\n    ----------\n    e : ap.EnterFrameEvent\n        Event instance.\n    options : dict\n        Optional argument dictionary.\n    """\n    right_rectangle.rotation_around_center -= 1\n\n\ndef on_rectangle_click(e: ap.MouseEvent, options: dict) -> None:\n    """\n    The handler to handle a rectangle click event.\n\n    Parameters\n    ----------\n    e : ap.MouseEvent\n        Event instance.\n    options : dict\n        Optional argument dictionary.\n    """\n    stage.unbind_enter_frame_all()\n\n\nstage.enter_frame(handler=on_enter_frame_1, fps=ap.FPS.FPS_30)\nstage.enter_frame(handler=on_enter_frame_2, fps=ap.FPS.FPS_30)\nleft_rectangle.click(handler=on_rectangle_click)\nright_rectangle.click(handler=on_rectangle_click)\n\nap.save_overall_html(dest_dir_path="unbind_enter_frame_all_basic_usage/")\n```': '```py\n# runnable\nimport apysc as ap\n\nstage: ap.Stage = ap.Stage(\n    stage_width=250,\n    stage_height=150,\n    background_color="#333",\n    stage_elem_id="stage",\n)\nleft_rectangle: ap.Rectangle = ap.Rectangle(\n    x=50, y=50, width=50, height=50, fill_color="#0af"\n)\nright_rectangle: ap.Rectangle = ap.Rectangle(\n    x=150, y=50, width=50, height=50, fill_color="#f0a"\n)\n\n\ndef on_enter_frame_1(e: ap.EnterFrameEvent, options: dict) -> None:\n    """\n    The handler to handle an enter frame event.\n\n    Parameters\n    ----------\n    e : ap.EnterFrameEvent\n        Event instance.\n    options : dict\n        Optional argument dictionary.\n    """\n    left_rectangle.rotation_around_center += 1\n\n\ndef on_enter_frame_2(e: ap.EnterFrameEvent, options: dict) -> None:\n    """\n    The handler to handle an enter frame event.\n\n    Parameters\n    ----------\n    e : ap.EnterFrameEvent\n        Event instance.\n    options : dict\n        Optional argument dictionary.\n    """\n    right_rectangle.rotation_around_center -= 1\n\n\ndef on_rectangle_click(e: ap.MouseEvent, options: dict) -> None:\n    """\n    The handler to handle a rectangle click event.\n\n    Parameters\n    ----------\n    e : ap.MouseEvent\n        Event instance.\n    options : dict\n        Optional argument dictionary.\n    """\n    stage.unbind_enter_frame_all()\n\n\nstage.enter_frame(handler=on_enter_frame_1, fps=ap.FPS.FPS_30)\nstage.enter_frame(handler=on_enter_frame_2, fps=ap.FPS.FPS_30)\nleft_rectangle.click(handler=on_rectangle_click)\nright_rectangle.click(handler=on_rectangle_click)\n\nap.save_overall_html(dest_dir_path="unbind_enter_frame_all_basic_usage/")\n```',  # noqa
    ##################################################
    "## See also": "## 関連資料",
    ##################################################
    "- [enter_frame interface](enter_frame.md)": "- [enter_frame インターフェイス](jp_enter_frame.md)",  # noqa
    ##################################################
    "## unbind_enter_frame API": "## unbind_enter_frame のAPI",
    ##################################################
    '<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>': '<span class="inconspicuous-txt">特記事項: このAPIドキュメントはドキュメントビルド用のスクリプトによって自動で生成・同期されています。そのためもしかしたらこの節の内容は前節までの内容と重複している場合があります。</span>',  # noqa
    ##################################################
    "**[Interface summary]**": "**[インターフェイス概要]**",
    ##################################################
    "Unbind a specified handler's enter-frame event.<hr>": "指定されたハンドラのenter-frameイベントの設定を解除します。<hr>",  # noqa
    ##################################################
    "**[Parameters]**": "**[引数]**",
    ##################################################
    "- `handler`: Callable[[EnterFrameEvent, _Options], None]": "- `handler`: Callable[[EnterFrameEvent, _Options], None]",  # noqa
    ##################################################
    "  - Unbinding target callable.": "  - 設定を取り除く対象のcallableオブジェクト。",
    ##################################################
    "<hr>": "<hr>",
    ##################################################
    "**[Raises]**": "**[エラー発生条件]**",
    ##################################################
    "- _EnterFrameEventNotRegistered: If there is no unbinding target of a specified handler.": "- _EnterFrameEventNotRegistered: もし指定されたハンドラの設定削除対象が存在しない場合。",  # noqa
    ##################################################
    "<hr>": "<hr>",
    ##################################################
    "**[Examples]**": "**[コードサンプル]**",
    ##################################################
    '```py\n>>> import apysc as ap\n>>> stage: ap.Stage = ap.Stage()\n>>> rectangle: ap.Rectangle = ap.Rectangle(\n...     x=50, y=50, width=50, height=50, fill_color="#0af"\n... )\n>>> def on_enter_frame(e: ap.EnterFrameEvent, options: dict) -> None:\n...     rectangle.x += 1\n>>> stage.enter_frame(handler=on_enter_frame, fps=ap.FPS.FPS_30)\n>>> # Any implementations here...\n>>> stage.unbind_enter_frame(handler=on_enter_frame)\n```': '```py\n>>> import apysc as ap\n>>> stage: ap.Stage = ap.Stage()\n>>> rectangle: ap.Rectangle = ap.Rectangle(\n...     x=50, y=50, width=50, height=50, fill_color="#0af"\n... )\n>>> def on_enter_frame(e: ap.EnterFrameEvent, options: dict) -> None:\n...     rectangle.x += 1\n>>> stage.enter_frame(handler=on_enter_frame, fps=ap.FPS.FPS_30)\n>>> # Any implementations here...\n>>> stage.unbind_enter_frame(handler=on_enter_frame)\n```',  # noqa
    ##################################################
    "## unbind_enter_frame_all API": "## unbind_enter_frame_all のAPI",
    ##################################################
    '<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>': '<span class="inconspicuous-txt">特記事項: このAPIドキュメントはドキュメントビルド用のスクリプトによって自動で生成・同期されています。そのためもしかしたらこの節の内容は前節までの内容と重複している場合があります。</span>',  # noqa
    ##################################################
    "**[Interface summary]**": "**[インターフェイス概要]**",
    ##################################################
    "Unbind all enter-frame events.<hr>": "すべてのenter-frameイベントの設定を解除します。<hr>",
    ##################################################
    "**[Examples]**": "**[コードサンプル]**",
    ##################################################
    '```py\n>>> import apysc as ap\n>>> stage: ap.Stage = ap.Stage()\n>>> rectangle: ap.Rectangle = ap.Rectangle(\n...     x=50, y=50, width=50, height=50, fill_color="#0af"\n... )\n>>> def on_enter_frame(e: ap.EnterFrameEvent, options: dict) -> None:\n...     rectangle.x += 1\n>>> stage.enter_frame(handler=on_enter_frame, fps=ap.FPS.FPS_30)\n>>> # Any implementations here...\n>>> stage.unbind_enter_frame_all()\n```': '```py\n>>> import apysc as ap\n>>> stage: ap.Stage = ap.Stage()\n>>> rectangle: ap.Rectangle = ap.Rectangle(\n...     x=50, y=50, width=50, height=50, fill_color="#0af"\n... )\n>>> def on_enter_frame(e: ap.EnterFrameEvent, options: dict) -> None:\n...     rectangle.x += 1\n>>> stage.enter_frame(handler=on_enter_frame, fps=ap.FPS.FPS_30)\n>>> # Any implementations here...\n>>> stage.unbind_enter_frame_all()\n```',  # noqa
}
