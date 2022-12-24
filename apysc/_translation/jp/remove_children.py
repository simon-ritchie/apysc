"""This module is for the translation mapping data of the
following document:

Document file: remove_children.md
Language: jp
"""

from typing import Dict

MAPPING: Dict[str, str] = {
    ##################################################
    "# remove_children interface": "# remove_children インターフェイス",
    ##################################################
    "This page explains the `remove_children` method interface of container classes.": "このページではコンテナの各クラスの`remove_children`メソッドのインターフェイスについて説明します。",  # noqa
    ##################################################
    "## What interface is this?": "## インターフェイス概要",
    ##################################################
    "The `remove_children` method removes all children from a container instance.": "`remove_children`メソッドはコンテナのインスタンスから全ての子のインスタンスを取り除きます。",  # noqa
    ##################################################
    "## Basic usage": "## 基本的な使い方",
    ##################################################
    "The `remove_children` method takes no arguments to use.": "`remove_children`メソッドは引数の指定を必要としません。",  # noqa
    ##################################################
    "In the following example, if you click any rectangle, the handler calls the `remove_children` method and removes all children:": "以下の例では、いずれかの四角をクリックした場合`remove_children`メソッドが呼ばれ全ての子が取り除かれます:",  # noqa
    ##################################################
    '```py\n# runnable\nimport apysc as ap\n\n\ndef on_click(e: ap.MouseEvent[ap.Sprite], options: dict) -> None:\n    """\n    The click event handler.\n\n    Parameters\n    ----------\n    e : ap.MouseEvent[ap.Sprite]\n        Event instance.\n    options : dict\n        Optional arguments dictionary.\n    """\n    sprite: ap.Sprite = e.this\n    sprite.remove_children()\n\n\nap.Stage(\n    stage_width=250, stage_height=150, background_color="#333", stage_elem_id="stage"\n)\nsprite: ap.Sprite = ap.Sprite()\nsprite.graphics.begin_fill(color="#0af")\nsprite.graphics.draw_rect(x=50, y=50, width=50, height=50)\nsprite.graphics.draw_rect(x=150, y=50, width=50, height=50)\nsprite.click(on_click)\n\nap.save_overall_html(dest_dir_path="remove_children_basic_usage/")\n```': '```py\n# runnable\nimport apysc as ap\n\n\ndef on_click(e: ap.MouseEvent[ap.Sprite], options: dict) -> None:\n    """\n    The click event handler.\n\n    Parameters\n    ----------\n    e : ap.MouseEvent[ap.Sprite]\n        Event instance.\n    options : dict\n        Optional arguments dictionary.\n    """\n    sprite: ap.Sprite = e.this\n    sprite.remove_children()\n\n\nap.Stage(\n    stage_width=250, stage_height=150, background_color="#333", stage_elem_id="stage"\n)\nsprite: ap.Sprite = ap.Sprite()\nsprite.graphics.begin_fill(color="#0af")\nsprite.graphics.draw_rect(x=50, y=50, width=50, height=50)\nsprite.graphics.draw_rect(x=150, y=50, width=50, height=50)\nsprite.click(on_click)\n\nap.save_overall_html(dest_dir_path="remove_children_basic_usage/")\n```',  # noqa
    ##################################################
    "## remove_children API": "## remove_children のAPI",
    ##################################################
    '<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>': '<span class="inconspicuous-txt">特記事項: このAPIドキュメントはドキュメントビルド用のスクリプトによって自動で生成・同期されています。そのためもしかしたらこの節の内容は前節までの内容と重複している場合があります。</span>',  # noqa
    ##################################################
    "**[Interface summary]**": "**[インターフェイス概要]**",
    ##################################################
    "Remove all children from this instance.<hr>": "このインスタンスから全ての子要素を取り除きます。<hr>",
    ##################################################
    "**[Examples]**": "**[コードサンプル]**",
    ##################################################
    '```py\n>>> import apysc as ap\n>>> sprite: ap.Sprite = ap.Sprite()\n>>> rectangle_1: ap.Rectangle = ap.Rectangle(\n...     x=50, y=50, width=50, height=50, fill_color="#0af"\n... )\n>>> rectangle_2: ap.Rectangle = ap.Rectangle(\n...     x=150, y=50, width=50, height=50, fill_color="#0af"\n... )\n>>> sprite.add_child(child=rectangle_1)\n>>> sprite.add_child(child=rectangle_2)\n>>> sprite.remove_children()\n>>> sprite.num_children\nInt(0)\n```': '```py\n>>> import apysc as ap\n>>> sprite: ap.Sprite = ap.Sprite()\n>>> rectangle_1: ap.Rectangle = ap.Rectangle(\n...     x=50, y=50, width=50, height=50, fill_color="#0af"\n... )\n>>> rectangle_2: ap.Rectangle = ap.Rectangle(\n...     x=150, y=50, width=50, height=50, fill_color="#0af"\n... )\n>>> sprite.add_child(child=rectangle_1)\n>>> sprite.add_child(child=rectangle_2)\n>>> sprite.remove_children()\n>>> sprite.num_children\nInt(0)\n```',  # noqa
}
