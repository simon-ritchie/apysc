"""This module is for the translation mapping data of the
following document:

Document file: contains.md
Language: jp
"""

from typing import Dict

MAPPING: Dict[str, str] = {
    ##################################################
    "# contains interface": "# contains インターフェイス",
    ##################################################
    "This page explains the container class, like the `Graphics`\\, `Sprite`\\, `Stage`) `contains` method interface.": "このページでは`Graphics`や`Sprite`、`Stage`などのコンテナとしての各クラスが持つ`contains`メソッドのインターフェイスについて説明します。",  # noqa
    ##################################################
    "## What interface is this?": "## インターフェイス概要",
    ##################################################
    "The `contains` interface returns the boolean (`Boolean`) value whether a container instance has a given child or not.": "`contains`インターフェイスは引数に指定された子のインスタンスを対象のコンテナが持つかどうかの真偽値（`Boolean`）を返却します。",  # noqa
    ##################################################
    "## Basic usage": "## 基本的な使い方",
    ##################################################
    "The following example checks whether the first rectangle is a child of the `Sprite` container. If it is true, remove the rectangle from the sprite and display a log to the console (please press F12 to display that message).": "以下のコード例では最初の四角が`Sprite`のコンテナーの子かどうかをチェックしています。もしその子を含んでいればその子を取り除き、ブラウザのコンソール上にログを表示しています（ログの表示にはF12キーを押してください）。",  # noqa
    ##################################################
    '```py\n# runnable\nfrom typing_extensions import TypedDict\n\nimport apysc as ap\n\n\nclass _RectOptions(TypedDict):\n    rectangle: ap.Rectangle\n\n\ndef on_sprite_click(e: ap.MouseEvent[ap.Sprite], options: _RectOptions) -> None:\n    """\n    The handler that the sprite calls when clicked.\n\n    Parameters\n    ----------\n    e : MouseEvent\n        Event instance.\n    options : dict\n        Optional arguments dictionary.\n    """\n    sprite: ap.Sprite = e.this\n    rectangle_1: ap.Rectangle = options["rectangle"]\n    condition: ap.Boolean = sprite.graphics.contains(child=rectangle_1)\n    with ap.If(condition):\n        sprite.remove_child(child=rectangle_1)\n        ap.trace("Removed the rectangle!")\n\n\nap.Stage(\n    background_color="#333", stage_width=250, stage_height=150, stage_elem_id="stage"\n)\n\nsprite: ap.Sprite = ap.Sprite()\nsprite.graphics.begin_fill(color="#0af")\nrectangle_1: ap.Rectangle = sprite.graphics.draw_rect(x=50, y=50, width=50, height=50)\nsprite.graphics.draw_rect(x=150, y=50, width=50, height=50)\noptions: _RectOptions = {"rectangle": rectangle_1}\nsprite.click(on_sprite_click, options=options)\n\nap.save_overall_html(dest_dir_path="sprite_contains_basic_usage/")\n```': '```py\n# runnable\nfrom typing_extensions import TypedDict\n\nimport apysc as ap\n\n\nclass _RectOptions(TypedDict):\n    rectangle: ap.Rectangle\n\n\ndef on_sprite_click(e: ap.MouseEvent[ap.Sprite], options: _RectOptions) -> None:\n    """\n    The handler that the sprite calls when clicked.\n\n    Parameters\n    ----------\n    e : MouseEvent\n        Event instance.\n    options : dict\n        Optional arguments dictionary.\n    """\n    sprite: ap.Sprite = e.this\n    rectangle_1: ap.Rectangle = options["rectangle"]\n    condition: ap.Boolean = sprite.graphics.contains(child=rectangle_1)\n    with ap.If(condition):\n        sprite.remove_child(child=rectangle_1)\n        ap.trace("Removed the rectangle!")\n\n\nap.Stage(\n    background_color="#333", stage_width=250, stage_height=150, stage_elem_id="stage"\n)\n\nsprite: ap.Sprite = ap.Sprite()\nsprite.graphics.begin_fill(color="#0af")\nrectangle_1: ap.Rectangle = sprite.graphics.draw_rect(x=50, y=50, width=50, height=50)\nsprite.graphics.draw_rect(x=150, y=50, width=50, height=50)\noptions: _RectOptions = {"rectangle": rectangle_1}\nsprite.click(on_sprite_click, options=options)\n\nap.save_overall_html(dest_dir_path="sprite_contains_basic_usage/")\n```',  # noqa
    ##################################################
    "## See also": "## 関連資料",
    ##################################################
    "- [add_child and remove_child interfaces](add_child_and_remove_child.md)": "- [add_child （子の追加）と remove_child （子の削除）のインターフェイス](jp_add_child_and_remove_child.md)",  # noqa
    ##################################################
    "## contains API": "## contains API",
    ##################################################
    '<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>': '<span class="inconspicuous-txt">特記事項: このAPIドキュメントはドキュメントビルド用のスクリプトによって自動で生成・同期されています。そのためもしかしたらこの節の内容は前節までの内容と重複している場合があります。</span>',  # noqa
    ##################################################
    "**[Interface summary]**": "**[インターフェイス概要]**",
    ##################################################
    "Get a boolean whether this instance contains a specified child.<hr>": "指定された子のインスタンスを持っているかどうかの真偽値を取得します。<hr>",  # noqa
    ##################################################
    "**[Parameters]**": "**[引数]**",
    ##################################################
    "- `child`: DisplayObject": "- `child`: DisplayObject",
    ##################################################
    "  - Child instance to check.": "  - チェック対象の子のインスタンス。",
    ##################################################
    "<hr>": "<hr>",
    ##################################################
    "**[Returns]**": "**[返却値]**",
    ##################################################
    "- `result`: Boolean": "- `result`: Boolean",
    ##################################################
    "  - If this instance contains a specified child, this method returns True.": "  - このインスタンスが指定された子を持つ場合Trueが設定されます。",  # noqa
    ##################################################
    "<hr>": "<hr>",
    ##################################################
    "**[Examples]**": "**[コードサンプル]**",
    ##################################################
    '```py\n>>> import apysc as ap\n>>> stage: ap.Stage = ap.Stage()\n>>> sprite: ap.Sprite = ap.Sprite()\n>>> sprite.graphics.begin_fill(color="#0af", alpha=0.5)\n>>> rectangle: ap.Rectangle = sprite.graphics.draw_rect(\n...     x=50, y=50, width=50, height=50\n... )\n>>> sprite.graphics.contains(rectangle)\nBoolean(True)\n\n>>> rectangle.remove_from_parent()\n>>> sprite.graphics.contains(rectangle)\nBoolean(False)\n```': '```py\n>>> import apysc as ap\n>>> stage: ap.Stage = ap.Stage()\n>>> sprite: ap.Sprite = ap.Sprite()\n>>> sprite.graphics.begin_fill(color="#0af", alpha=0.5)\n>>> rectangle: ap.Rectangle = sprite.graphics.draw_rect(\n...     x=50, y=50, width=50, height=50\n... )\n>>> sprite.graphics.contains(rectangle)\nBoolean(True)\n\n>>> rectangle.remove_from_parent()\n>>> sprite.graphics.contains(rectangle)\nBoolean(False)\n```',  # noqa
}
