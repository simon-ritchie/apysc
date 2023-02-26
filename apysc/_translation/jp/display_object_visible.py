"""This module is for the translation mapping data of the
following document:

Document file: display_object_visible.md
Language: jp
"""

from typing import Dict

MAPPING: Dict[str, str] = {
    ##################################################
    "# DisplayObject class visible interface": "# DisplayObject クラスの visible インターフェイス",
    ##################################################
    "This page explains the `DisplayObject` class `visible` property interface.": "このページでは`DisplayObject`クラスの`visible`属性のインターフェイスについて説明します。",  # noqa
    ##################################################
    "## What interface is this?": "## インターフェイス概要",
    ##################################################
    "The `visible` property interface will change the `DisplayObject` visible / invisible state.": "`visible`属性は`DisplayObject`の表示・非表示の状態を切り替えます。",  # noqa
    ##################################################
    "## Basic usage": "## 基本的な使い方",
    ##################################################
    "The `visible` property accepts a `Boolean` value. If you set the True value, a `DisplayObject` instance becomes visible (default). Conversely, if you set the False value, a `DisplayObject` instance becomes invisible.": "`visible`属性は`Boolean`の値を受け付けます。Trueを設定した場合その`DisplayObject`のインスタンスは表示状態になります（デフォルトの状態になります）。Falseを設定するとその`DisplayObject`のインスタンスは非表示になります。",  # noqa
    ##################################################
    "The following example switches the visible values when you click the rectangle. For example, suppose you click the left rectangle (the rectangle_1). In that case, the left rectangle becomes invisible, and the right rectangle (rectangle_2) becomes visible.": "以下のコード例では四角をクリックした時にvisibleの設定を切り替えています。左側の四角をクリックした際には左側の四角は非表示となり、右側に別の四角が表示されます。",  # noqa
    ##################################################
    '```py\n# runnable\nfrom typing_extensions import TypedDict\n\nimport apysc as ap\n\n\nclass _RectOptions(TypedDict):\n    rectangle: ap.Rectangle\n\n\ndef on_rectangle_1_click(e: ap.MouseEvent[ap.Rectangle], options: _RectOptions) -> None:\n    """\n    The handler that the first rectangle calls when clicked.\n\n    Parameters\n    ----------\n    e : MouseEvent\n        Event instance.\n    options : dict\n        Optional arguments dictionary.\n    """\n    rectangle_1: ap.Rectangle = e.this\n    rectangle_2: ap.Rectangle = options["rectangle"]\n    rectangle_1.visible = ap.Boolean(False)\n    rectangle_2.visible = ap.Boolean(True)\n\n\ndef on_rectangle_2_click(e: ap.MouseEvent[ap.Rectangle], options: _RectOptions) -> None:\n    """\n    The handler that the second rectangle calls when clicked.\n\n    Parameters\n    ----------\n    e : MouseEvent\n        Event instance.\n    options : dict\n        Optional arguments dictionary.\n    """\n    rectangle_1: ap.Rectangle = options["rectangle"]\n    rectangle_2: ap.Rectangle = e.this\n    rectangle_1.visible = ap.Boolean(True)\n    rectangle_2.visible = ap.Boolean(False)\n\n\nap.Stage(\n    background_color="#333", stage_width=250, stage_height=150, stage_elem_id="stage"\n)\n\nsprite: ap.Sprite = ap.Sprite()\n\nsprite.graphics.begin_fill(color="#0af")\nrectangle_1: ap.Rectangle = sprite.graphics.draw_rect(x=50, y=50, width=50, height=50)\n\nsprite.graphics.begin_fill(color="#f0a")\nrectangle_2: ap.Rectangle = sprite.graphics.draw_rect(x=150, y=50, width=50, height=50)\nrectangle_2.visible = ap.Boolean(False)\n\noptions: _RectOptions = {"rectangle": rectangle_2}\nrectangle_1.click(on_rectangle_1_click, options=options)\noptions = {"rectangle": rectangle_1}\nrectangle_2.click(on_rectangle_2_click, options=options)\n\nap.save_overall_html(dest_dir_path="display_object_visible_basic_usage/")\n```': '```py\n# runnable\nfrom typing_extensions import TypedDict\n\nimport apysc as ap\n\n\nclass _RectOptions(TypedDict):\n    rectangle: ap.Rectangle\n\n\ndef on_rectangle_1_click(e: ap.MouseEvent[ap.Rectangle], options: _RectOptions) -> None:\n    """\n    The handler that the first rectangle calls when clicked.\n\n    Parameters\n    ----------\n    e : MouseEvent\n        Event instance.\n    options : dict\n        Optional arguments dictionary.\n    """\n    rectangle_1: ap.Rectangle = e.this\n    rectangle_2: ap.Rectangle = options["rectangle"]\n    rectangle_1.visible = ap.Boolean(False)\n    rectangle_2.visible = ap.Boolean(True)\n\n\ndef on_rectangle_2_click(e: ap.MouseEvent[ap.Rectangle], options: _RectOptions) -> None:\n    """\n    The handler that the second rectangle calls when clicked.\n\n    Parameters\n    ----------\n    e : MouseEvent\n        Event instance.\n    options : dict\n        Optional arguments dictionary.\n    """\n    rectangle_1: ap.Rectangle = options["rectangle"]\n    rectangle_2: ap.Rectangle = e.this\n    rectangle_1.visible = ap.Boolean(True)\n    rectangle_2.visible = ap.Boolean(False)\n\n\nap.Stage(\n    background_color="#333", stage_width=250, stage_height=150, stage_elem_id="stage"\n)\n\nsprite: ap.Sprite = ap.Sprite()\n\nsprite.graphics.begin_fill(color="#0af")\nrectangle_1: ap.Rectangle = sprite.graphics.draw_rect(x=50, y=50, width=50, height=50)\n\nsprite.graphics.begin_fill(color="#f0a")\nrectangle_2: ap.Rectangle = sprite.graphics.draw_rect(x=150, y=50, width=50, height=50)\nrectangle_2.visible = ap.Boolean(False)\n\noptions: _RectOptions = {"rectangle": rectangle_2}\nrectangle_1.click(on_rectangle_1_click, options=options)\noptions = {"rectangle": rectangle_1}\nrectangle_2.click(on_rectangle_2_click, options=options)\n\nap.save_overall_html(dest_dir_path="display_object_visible_basic_usage/")\n```',  # noqa
    ##################################################
    "## visible property API": "## visible 属性のAPI",
    ##################################################
    '<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>': '<span class="inconspicuous-txt">特記事項: このAPIドキュメントはドキュメントビルド用のスクリプトによって自動で生成・同期されています。そのためもしかしたらこの節の内容は前節までの内容と重複している場合があります。</span>',  # noqa
    ##################################################
    "**[Interface summary]**": "**[インターフェイス概要]**",
    ##################################################
    "Get a visibility value of this instance.<hr>": "このインスタンスの可視状態かどうかの値を取得します。<hr>",
    ##################################################
    "**[Returns]**": "**[返却値]**",
    ##################################################
    "- `result`: Boolean": "- `result`: Boolean",
    ##################################################
    "  - If this instance is visible, this interface returns True.": "  - もしこのインスタンスが表示状態であればTrueとなります。",  # noqa
    ##################################################
    "<hr>": "<hr>",
    ##################################################
    "**[Examples]**": "**[コードサンプル]**",
    ##################################################
    '```py\n>>> import apysc as ap\n>>> stage: ap.Stage = ap.Stage()\n>>> sprite: ap.Sprite = ap.Sprite()\n>>> sprite.graphics.begin_fill(color="#0af")\n>>> rectangle: ap.Rectangle = sprite.graphics.draw_rect(\n...     x=50, y=50, width=50, height=50\n... )\n>>> rectangle.visible = ap.Boolean(False)\n>>> rectangle.visible\nBoolean(False)\n```': '```py\n>>> import apysc as ap\n>>> stage: ap.Stage = ap.Stage()\n>>> sprite: ap.Sprite = ap.Sprite()\n>>> sprite.graphics.begin_fill(color="#0af")\n>>> rectangle: ap.Rectangle = sprite.graphics.draw_rect(\n...     x=50, y=50, width=50, height=50\n... )\n>>> rectangle.visible = ap.Boolean(False)\n>>> rectangle.visible\nBoolean(False)\n```',  # noqa
}
