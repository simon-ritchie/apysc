"""This module is for the translation mapping data of the
following document:

Document file: mouse_event_abstract.md
Language: jp
"""

from typing import Dict

MAPPING: Dict[str, str] = {
    ##################################################
    "# MouseEvent interfaces abstract": "# MouseEvent の各インターフェイスの概要",
    ##################################################
    "This page explains the MouseEvent interfaces abstract.": "このページでは MouseEvent クラスの各インターフェイスの概要について説明します。",  # noqa
    ##################################################
    "## What apysc can do in its interfaces": "## これらの各インターフェイスでapyscが出来ること",
    ##################################################
    "- You can set the `MouseEvent` handlers, such as the click, mouse down, mouse over, and so on, to each graphic instance.": "- クリックやマウスダウン、マウスオーバーなどの`MouseEvent`の各ハンドラをグラフィックスのインスタンスへ設定することができます。",  # noqa
    ##################################################
    "- You can pass the optional arguments to the handler.": "- ハンドラの引数へ任意のパラメーターを渡すことができます。",  # noqa
    ##################################################
    "## Example of the click event": "## クリックイベントの例",
    ##################################################
    "To bind MouseEvent, defining the handler function (or method) would be necessary (e.g., `on_click`).": "マウスイベントを設定するにはまずはハンドラ用の関数（もしくはメソッド）の定義が必要になります（例: `on_click`）。",  # noqa
    ##################################################
    "These handlers can bind with the click interface.": "これらのハンドラは click のインターフェイスで登録することができます。",  # noqa
    ##################################################
    '```py\n# runnable\nimport apysc as ap\n\n\ndef on_click(e: ap.MouseEvent[ap.Rectangle], options: dict) -> None:\n    """\n    The handler that the rectangle calls when clicked.\n\n    Parameters\n    ----------\n    e : ap.MouseEvent\n        Event instance.\n    options : dict\n        Optional arguments dictionary.\n    """\n    rectangle: ap.Rectangle = e.this\n    with ap.If(rectangle.fill_color == "#00aaff"):\n        rectangle.fill_color = ap.String("#f0a")\n        ap.Return()\n\n    with ap.If(rectangle.fill_color == "#ff00aa"):\n        rectangle.fill_color = ap.String("#0af")\n        ap.Return()\n\n\nap.Stage(\n    background_color="#333", stage_width=150, stage_height=150, stage_elem_id="stage"\n)\nsprite: ap.Sprite = ap.Sprite()\nsprite.graphics.begin_fill(color="#0af")\nrectangle: ap.Rectangle = sprite.graphics.draw_rect(x=50, y=50, width=50, height=50)\nrectangle.click(on_click)\n\nap.save_overall_html(dest_dir_path="mouse_event_abstract_click/")\n```': '```py\n# runnable\nimport apysc as ap\n\n\ndef on_click(e: ap.MouseEvent[ap.Rectangle], options: dict) -> None:\n    """\n    The handler that the rectangle calls when clicked.\n\n    Parameters\n    ----------\n    e : ap.MouseEvent\n        Event instance.\n    options : dict\n        Optional arguments dictionary.\n    """\n    rectangle: ap.Rectangle = e.this\n    with ap.If(rectangle.fill_color == "#00aaff"):\n        rectangle.fill_color = ap.String("#f0a")\n        ap.Return()\n\n    with ap.If(rectangle.fill_color == "#ff00aa"):\n        rectangle.fill_color = ap.String("#0af")\n        ap.Return()\n\n\nap.Stage(\n    background_color="#333", stage_width=150, stage_height=150, stage_elem_id="stage"\n)\nsprite: ap.Sprite = ap.Sprite()\nsprite.graphics.begin_fill(color="#0af")\nrectangle: ap.Rectangle = sprite.graphics.draw_rect(x=50, y=50, width=50, height=50)\nrectangle.click(on_click)\n\nap.save_overall_html(dest_dir_path="mouse_event_abstract_click/")\n```',  # noqa
    ##################################################
    "## See also": "## 関連資料",
    ##################################################
    "There are a lot of other mouse event binding interfaces, such as the mouse down, mouse over, and mouse move. For more details, please see the following:": "他にもマウスダウンやマウスオーバー、マウスムーブなど様々なイベント設定用のインターフェイスが存在します。詳細は以下をご確認ください:",  # noqa
    ##################################################
    "- [Basic mouse event interfaces](mouse_event_basic.md)": "- [基本的なマウスイベントの各インターフェイス](jp_mouse_event_basic.md)",  # noqa
    ##################################################
    "- [click interface](click.md)": "- [click インターフェイス](jp_click.md)",
    ##################################################
    "- [dblclick interface](dblclick.md)": "- [dblclick インターフェイス](jp_dblclick.md)",
    ##################################################
    "- [mousedown and mouseup interfaces](mousedown_and_mouseup.md)": "- [mousedown と mouseup のインターフェイス](jp_mousedown_and_mouseup.md)",  # noqa
    ##################################################
    "- [mouseover and mouseout interfaces](mouseover_and_mouseout.md)": "- [mouseover と mouseout のインターフェイス](jp_mouseover_and_mouseout.md)",  # noqa
    ##################################################
    "- [mousemove interface](mousemove.md)": "- [mousemove インターフェイス](jp_mousemove.md)",
}
