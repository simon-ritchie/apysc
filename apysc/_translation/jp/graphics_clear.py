"""This module is for the translation mapping data of the
following document:

Document file: graphics_clear.md
Language: jp
"""

from typing import Dict

MAPPING: Dict[str, str] = {
    ##################################################
    "# Graphics clear interface": "# Graphics クラスの clear インターフェイス",
    ##################################################
    "This page explains the `Graphics` class `clear` method interface.": "このページでは`Graphics`クラスの`clear`メソッドのインターフェイスについて説明します。",  # noqa
    ##################################################
    "## What interface is this?": "## インターフェイス概要",
    ##################################################
    "The `clear` method removes all graphics and clears (resets) fill and line settings.": "`clear`メソッドは全ての描画済みグラフィックスを取り除き、塗りと線の設定をリセットします。",  # noqa
    ##################################################
    "## Basic usage": "## 基本的な使い方",
    ##################################################
    "The `clear` method takes no arguments.": "`clear`メソッドは引数の指定を必要としません。",
    ##################################################
    "The handler calls the `clear` method in the following example if you click any rectangle.": "以下の例では四角をクリックした際にハンドラ内で`clear`メソッドが呼ばれます:",  # noqa
    ##################################################
    '```py\n# runnable\nimport apysc as ap\n\n\ndef on_click(e: ap.MouseEvent[ap.Sprite], options: dict) -> None:\n    """\n    The click event handler.\n\n    Parameters\n    ----------\n    e : ap.MouseEvent[ap.Sprite]\n        Event instance.\n    options : dict\n        Optional arguments dictionary.\n    """\n    sprite: ap.Sprite = e.this\n    ap.assert_equal(sprite.graphics.fill_color, "#00aaff")\n    sprite.graphics.clear()\n    ap.assert_equal(sprite.graphics.fill_color, "")\n\n\nap.Stage(\n    stage_width=250,\n    stage_height=150,\n    background_color=ap.Color("#333"),\n    stage_elem_id="stage",\n)\nsprite: ap.Sprite = ap.Sprite()\nsprite.graphics.begin_fill(color=ap.Color("#0af"))\nsprite.graphics.draw_rect(x=50, y=50, width=50, height=50)\nsprite.graphics.draw_rect(x=150, y=50, width=50, height=50)\nsprite.click(on_click)\n\nap.save_overall_html(dest_dir_path="graphics_clear_basic_usage/")\n```': '```py\n# runnable\nimport apysc as ap\n\n\ndef on_click(e: ap.MouseEvent[ap.Sprite], options: dict) -> None:\n    """\n    The click event handler.\n\n    Parameters\n    ----------\n    e : ap.MouseEvent[ap.Sprite]\n        Event instance.\n    options : dict\n        Optional arguments dictionary.\n    """\n    sprite: ap.Sprite = e.this\n    ap.assert_equal(sprite.graphics.fill_color, "#00aaff")\n    sprite.graphics.clear()\n    ap.assert_equal(sprite.graphics.fill_color, "")\n\n\nap.Stage(\n    stage_width=250,\n    stage_height=150,\n    background_color=ap.Color("#333"),\n    stage_elem_id="stage",\n)\nsprite: ap.Sprite = ap.Sprite()\nsprite.graphics.begin_fill(color=ap.Color("#0af"))\nsprite.graphics.draw_rect(x=50, y=50, width=50, height=50)\nsprite.graphics.draw_rect(x=150, y=50, width=50, height=50)\nsprite.click(on_click)\n\nap.save_overall_html(dest_dir_path="graphics_clear_basic_usage/")\n```',  # noqa
}
