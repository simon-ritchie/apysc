"""This module is for the translation mapping data of the
following document:

Document file: delete.md
Language: jp
"""

from typing import Dict

MAPPING: Dict[str, str] = {
    ##################################################
    "# delete interface": "# delete インターフェイス",
    ##################################################
    "This page explains the `delete` function interface.": "このページでは`delete`関数のインターフェイスについて説明します。",  # noqa
    ##################################################
    "## What interface is this?": "## インターフェイス概要",
    ##################################################
    "The `delete` function deletes any instance, and it becomes an `undefined` object.": "`delete`関数は任意のインスタンスの削除を行います。削除された対象は`undefined`のオブジェクトになります。",  # noqa
    ##################################################
    "If an instance is a `DisplayObject` instance, this interface removes an instance from a stage.": "もし対象のインスタンスが`DisplayObject`のインスタンスであれば、このインターフェイスはそのインスタンスをステージから取り除きます。",  # noqa
    ##################################################
    "For example, this interface removes a `Sprite` or `Rectangle` instance.": "例えば`Sprite`や`Rectangle`などのインスタンスであればこのインターフェイスはそれらのインスタンスを取り除きます。",  # noqa
    ##################################################
    "## Basic usage": "## 基本的な使い方",
    ##################################################
    "You can specify any apysc instance to the `delete` argument.": "`delete`関数の引数へは任意のapyscのインスタンスを指定することができます。",  # noqa
    ##################################################
    "```py\n# runnable\nimport apysc as ap\n\nint_val: ap.Int = ap.Int(10)\nap.delete(int_val)\n```": "```py\n# runnable\nimport apysc as ap\n\nint_val: ap.Int = ap.Int(10)\nap.delete(int_val)\n```",  # noqa
    ##################################################
    "If a specified instance is a `DisplayObject` instance, the `delete` function removes it from a stage.": "もし指定されたインスタンスが`DisplayObject`のインスタンスであれば、`delete`関数はそのインスタンスをステージから取り除きます。",  # noqa
    ##################################################
    "Also, it becomes an undefined object.": "また、削除されたインスタンスはundefinedのオブジェクトになります。",
    ##################################################
    '```py\n# runnable\nimport apysc as ap\n\n\ndef on_click(e: ap.MouseEvent[ap.Sprite], options: dict) -> None:\n    """\n    The click event handler that a sprite calls.\n\n    Parameters\n    ----------\n    e : ap.MouseEvent[ap.Sprite]\n        Event instance.\n    options : dict\n        Optional arguments dictionary.\n    """\n    sprite: ap.Sprite = e.this\n    ap.delete(sprite)\n    ap.assert_undefined(sprite)\n\n\nap.Stage(\n    stage_width=150, stage_height=150, background_color="#333", stage_elem_id="stage"\n)\nsprite: ap.Sprite = ap.Sprite()\nsprite.graphics.begin_fill(color="#0af")\nsprite.graphics.draw_rect(x=50, y=50, width=50, height=50)\nsprite.click(on_click)\n\nap.save_overall_html(dest_dir_path="delete_basic_usage/")\n```': '```py\n# runnable\nimport apysc as ap\n\n\ndef on_click(e: ap.MouseEvent[ap.Sprite], options: dict) -> None:\n    """\n    The click event handler that a sprite calls.\n\n    Parameters\n    ----------\n    e : ap.MouseEvent[ap.Sprite]\n        Event instance.\n    options : dict\n        Optional arguments dictionary.\n    """\n    sprite: ap.Sprite = e.this\n    ap.delete(sprite)\n    ap.assert_undefined(sprite)\n\n\nap.Stage(\n    stage_width=150, stage_height=150, background_color="#333", stage_elem_id="stage"\n)\nsprite: ap.Sprite = ap.Sprite()\nsprite.graphics.begin_fill(color="#0af")\nsprite.graphics.draw_rect(x=50, y=50, width=50, height=50)\nsprite.click(on_click)\n\nap.save_overall_html(dest_dir_path="delete_basic_usage/")\n```',  # noqa
    ##################################################
    "If you click the following rectangle, the `delete` function removes it from the stage.": "もし以下の四角をクリックすると、`delete`関数は対象のインスタンスをステージから取り除きます。",  # noqa
}
