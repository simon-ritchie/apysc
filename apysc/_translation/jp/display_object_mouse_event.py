"""This module is for the translation mapping data of the
following document:

Document file: display_object_mouse_event.md
Language: jp
"""

from typing import Dict

MAPPING: Dict[str, str] = {
    ##################################################
    "# DisplayObject class mouse event binding interfaces": "# DisplayObject クラスのマウスイベント設定の各インターフェイス",  # noqa
    ##################################################
    "This page explains the `DisplayObject` class mouse event binding interfaces.": "このページでは`DisplayObject`クラスのマウスイベントの登録の各インターフェイスについて説明します。",  # noqa
    ##################################################
    "## What interfaces are these?": "## 各インターフェイスの概要",
    ##################################################
    "Each `DisplayObject` instance has the mouse event binding interfaces, like the click, mouse over, mouse move.": "各`DisplayObject`のインスタンスはクリックやマウスオーバーなどのマウスイベント登録用の各インターフェイスを持っています。",  # noqa
    ##################################################
    "These interfaces can bind the mouse event to a `DisplayObject` instance. So, for instance, you can assign any function to handle when a click of `DisplayObject` instance.": "これらのインターフェイスは`DisplayObject`にマウスイベントを設定でき、例えばクリック時に実行したい関数などを登録することができます。",  # noqa
    ##################################################
    "## Basic usage": "## 基本的な使い方",
    ##################################################
    "You can bind an event handler (callable) with each interface like the `click`, `mouseover`.": "`click`や`mouseover`などの各インターフェイスで任意のイベントハンドラ（Callableオブジェクト）を登録することができます。",  # noqa
    ##################################################
    "The following example binds the click event handler, and if you click the rectangle, the fill color is changed.": "以下のコード例ではクリックのイベントハンドラを設定しており、四角をクリックすると色が変わるようにしています。",  # noqa
    ##################################################
    '```py\n# runnable\nimport apysc as ap\n\n\ndef on_click(e: ap.MouseEvent[ap.Rectangle], options: dict) -> None:\n    """\n    The handler that the rectangle calls when clicked.\n\n    Parameters\n    ----------\n    e : MouseEvent\n        Event instance.\n    options : dict\n        Optional arguments dictionary.\n    """\n    rectangle: ap.Rectangle = e.this\n    rectangle.fill_color = ap.Color("#f0a")\n\n\nap.Stage(\n    background_color=ap.Color("#333"),\n    stage_width=150,\n    stage_height=150,\n    stage_elem_id="stage",\n)\n\nsprite: ap.Sprite = ap.Sprite()\nsprite.graphics.begin_fill(color=ap.Color("#0af"))\nrectangle: ap.Rectangle = sprite.graphics.draw_rect(x=50, y=50, width=50, height=50)\nrectangle.click(on_click)\n\nap.save_overall_html(dest_dir_path="display_object_mouse_event_basic_usage/")\n```': '```py\n# runnable\nimport apysc as ap\n\n\ndef on_click(e: ap.MouseEvent[ap.Rectangle], options: dict) -> None:\n    """\n    The handler that the rectangle calls when clicked.\n\n    Parameters\n    ----------\n    e : MouseEvent\n        Event instance.\n    options : dict\n        Optional arguments dictionary.\n    """\n    rectangle: ap.Rectangle = e.this\n    rectangle.fill_color = ap.Color("#f0a")\n\n\nap.Stage(\n    background_color=ap.Color("#333"),\n    stage_width=150,\n    stage_height=150,\n    stage_elem_id="stage",\n)\n\nsprite: ap.Sprite = ap.Sprite()\nsprite.graphics.begin_fill(color=ap.Color("#0af"))\nrectangle: ap.Rectangle = sprite.graphics.draw_rect(x=50, y=50, width=50, height=50)\nrectangle.click(on_click)\n\nap.save_overall_html(dest_dir_path="display_object_mouse_event_basic_usage/")\n```',  # noqa
    ##################################################
    "## See also": "## 関連資料",
    ##################################################
    "For more details, please see the following pages:": "詳細については以下の各ページをご確認ください:",
    ##################################################
    "- [Basic mouse event interfaces](mouse_event_basic.md)": "- [基本的なマウスイベントの各インターフェイス](jp_mouse_event_basic.md)",  # noqa
    ##################################################
    "- [click interface](click.md)": "- [click インターフェイス](jp_click.md)",
    ##################################################
    "- [mousedown and mouseup interfaces](mousedown_and_mouseup.md)": "- [mousedown と mouseup のインターフェイス](jp_mousedown_and_mouseup.md)",  # noqa
    ##################################################
    "- [mouseover and mouseout interfaces](mouseover_and_mouseout.md)": "- [mouseover と mouseout のインターフェイス](jp_mouseover_and_mouseout.md)",  # noqa
    ##################################################
    "- [mousemove interface](mousemove.md)": "- [mousemove インターフェイス](jp_mousemove.md)",
}
