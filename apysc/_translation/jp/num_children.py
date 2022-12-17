"""This module is for the translation mapping data of the
following document:

Document file: num_children.md
Language: jp
"""

from typing import Dict

MAPPING: Dict[str, str] = {
    ##################################################
    "# num_children interface": "# num_children インターフェイス",
    ##################################################
    "This page explains the container class, like the `Graphics`\\, `Sprite`\\, `Stage`) `num_children` property interface.": "このページでは`Graphics`や`Sprite`、`Stage`などのコンテナのクラスの`num_children`属性のインターフェイスについて説明します。",  # noqa
    ##################################################
    "## What interface is this?": "## インターフェイス概要",
    ##################################################
    "The `num_children` property interface returns the integer (`Int`) value of the number of children.": "`num_children`属性のインターフェイスは子の数の`Int`型の整数の値を返却します。",  # noqa
    ##################################################
    "## Notes": "## 特記事項",
    ##################################################
    "The `Sprite` instance's initial children number is 1, not 0 since a sprite instance has a `graphics` child.": "`Sprite`インスタンスの初期値は`graphics`インスタンスの子を持つため0ではなく1になっています。",  # noqa
    ##################################################
    "## Basic usage": "## 基本的な使い方",
    ##################################################
    "The `num_children` property returns the number of children (`Int` value). You can use it for the calculation, for instance, coordinates calculation.": "`num_children`属性は`Int`型の整数の子の数を返却します。その値を使って座標の計算などを行うことができます。",  # noqa
    ##################################################
    "The following example appends a new rectangle when you click the sprite (rectangle) instance. The `num_children` property determines a new rectangle x-coordinate. When clicking a rectangle, this code also displays the current `num_children` property value to the browser console (please press the F12 key).": "以下のコード例では四角をクリックした際に新しい四角を追加しています。`num_children`属性の値は新しい四角のX座標を決めるのに使われています。また、このコードではクリックされた際に現在の`num_children`属性の値をブラウザのコンソールに表示しています（F12キーを押してコンソールを開いて確認してください）。",  # noqa
    ##################################################
    '```py\n# runnable\nimport apysc as ap\n\n\ndef on_sprite_click(e: ap.MouseEvent[ap.Sprite], options: dict) -> None:\n    """\n    The handler that the sprite calls when clicked.\n\n    Parameters\n    ----------\n    e : MouseEvent\n        Event instance.\n    options : dict\n        Optional arguments dictionary.\n    """\n    sprite: ap.Sprite = e.this\n    rectangle_x: ap.Int = (sprite.num_children - 1) * 100 + 50\n    new_rect: ap.Rectangle = sprite.graphics.draw_rect(\n        x=rectangle_x, y=50, width=50, height=50\n    )\n    sprite.add_child(new_rect)\n    ap.trace(\n        "Current sprite children number:",\n        sprite.num_children,\n        "rectangle x:",\n        rectangle_x,\n    )\n\n\nap.Stage(\n    background_color="#333", stage_width=450, stage_height=150, stage_elem_id="stage"\n)\n\nsprite: ap.Sprite = ap.Sprite()\nsprite.graphics.begin_fill(color="#0af")\nrectangle_1: ap.Rectangle = sprite.graphics.draw_rect(x=50, y=50, width=50, height=50)\nsprite.add_child(rectangle_1)\nsprite.click(on_sprite_click)\n\nap.save_overall_html(dest_dir_path="num_children_basic_usage/")\n```': '```py\n# runnable\nimport apysc as ap\n\n\ndef on_sprite_click(e: ap.MouseEvent[ap.Sprite], options: dict) -> None:\n    """\n    The handler that the sprite calls when clicked.\n\n    Parameters\n    ----------\n    e : MouseEvent\n        Event instance.\n    options : dict\n        Optional arguments dictionary.\n    """\n    sprite: ap.Sprite = e.this\n    rectangle_x: ap.Int = (sprite.num_children - 1) * 100 + 50\n    new_rect: ap.Rectangle = sprite.graphics.draw_rect(\n        x=rectangle_x, y=50, width=50, height=50\n    )\n    sprite.add_child(new_rect)\n    ap.trace(\n        "Current sprite children number:",\n        sprite.num_children,\n        "rectangle x:",\n        rectangle_x,\n    )\n\n\nap.Stage(\n    background_color="#333", stage_width=450, stage_height=150, stage_elem_id="stage"\n)\n\nsprite: ap.Sprite = ap.Sprite()\nsprite.graphics.begin_fill(color="#0af")\nrectangle_1: ap.Rectangle = sprite.graphics.draw_rect(x=50, y=50, width=50, height=50)\nsprite.add_child(rectangle_1)\nsprite.click(on_sprite_click)\n\nap.save_overall_html(dest_dir_path="num_children_basic_usage/")\n```',  # noqa
    ##################################################
    "## num_children API": "## num_children API",
    ##################################################
    '<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>': '<span class="inconspicuous-txt">特記事項: このAPIドキュメントはドキュメントビルド用のスクリプトによって自動で生成・同期されています。そのためもしかしたらこの節の内容は前節までの内容と重複している場合があります。</span>',  # noqa
    ##################################################
    "**[Interface summary]**": "**[インターフェイス概要]**",
    ##################################################
    "Get a current children's number.<hr>": "現在の子の数を取得します。<hr>",
    ##################################################
    "**[Returns]**": "**[返却値]**",
    ##################################################
    "- `num_children`: int": "- `num_children`: int",
    ##################################################
    "  - Current children number.": "  - 現在の子の数。",
    ##################################################
    "<hr>": "<hr>",
    ##################################################
    "**[Examples]**": "**[コードサンプル]**",
    ##################################################
    '```py\n>>> import apysc as ap\n>>> stage: ap.Stage = ap.Stage()\n>>> sprite: ap.Sprite = ap.Sprite()\n>>> sprite.graphics.begin_fill(color="#0af", alpha=0.5)\n>>> rectangle_1: ap.Rectangle = sprite.graphics.draw_rect(\n...     x=50, y=50, width=50, height=50\n... )\n>>> rectangle_2: ap.Rectangle = sprite.graphics.draw_rect(\n...     x=150, y=50, width=50, height=50\n... )\n>>> sprite.graphics.num_children\nInt(2)\n```': '```py\n>>> import apysc as ap\n>>> stage: ap.Stage = ap.Stage()\n>>> sprite: ap.Sprite = ap.Sprite()\n>>> sprite.graphics.begin_fill(color="#0af", alpha=0.5)\n>>> rectangle_1: ap.Rectangle = sprite.graphics.draw_rect(\n...     x=50, y=50, width=50, height=50\n... )\n>>> rectangle_2: ap.Rectangle = sprite.graphics.draw_rect(\n...     x=150, y=50, width=50, height=50\n... )\n>>> sprite.graphics.num_children\nInt(2)\n```',  # noqa
}
