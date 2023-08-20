"""This module is for the translation mapping data of the
following document:

Document file: get_child_at.md
Language: jp
"""

from typing import Dict

MAPPING: Dict[str, str] = {
    ##################################################
    "# get_child_at interface": "# get_child_at インターフェイス",
    ##################################################
    "This page explains the container class, like the `Graphics`\\, `Sprite`\\, `Stage`) `get_child_at` method interface.": "このページでは`Graphisc`や`Sprite`、`Stage`などのコンテナーのクラスの`get_child_at`メソッドのインターフェイスについて説明します。",  # noqa
    ##################################################
    "## What interface is this?": "## インターフェイス概要",
    ##################################################
    "The `get_child_at` interface returns a child (`DisplayObject`) instance at the specified index.": "`get_child_at`インターフェイスは指定されたインデックスの位置の子のインスタンス（`DisplkayObject`クラスのインスタンス）を返却します。",  # noqa
    ##################################################
    "## Basic usage": "## 基本的な使い方",
    ##################################################
    "The following code example is adding the rectangle to the sprite container. The `Sprite` class adds the `Graphics` instance at the constructor so that the first child becomes the `Graphics` instance. The second child becomes the `Rectangle` instance, which the sprite added with the `add_child` method.": "以下のコード例ではSpriteのコンテナーへと四角を追加しています。`Sprite`のクラスは`Graphics`のインスタンスを子としてコンストラクタで追加するため、最初の子は`Graphics`のインスタンスとなり、2番目の子は`add_child`メソッドで追加された`Rectangle`の四角のインスタンスとなります。",  # noqa
    ##################################################
    '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    background_color=ap.Color("#333"),\n    stage_width=450,\n    stage_height=150,\n    stage_elem_id="stage",\n)\n\nsprite: ap.Sprite = ap.Sprite()\nsprite.graphics.begin_fill(color=ap.Color("#0af"))\nrectangle_1: ap.Rectangle = sprite.graphics.draw_rect(x=50, y=50, width=50, height=50)\nsprite.add_child(rectangle_1)\n\nfirst_child: ap.DisplayObject = sprite.get_child_at(index=0)\nassert isinstance(first_child, ap.Graphics)\n\nsecond_child: ap.DisplayObject = sprite.get_child_at(index=1)\nassert isinstance(second_child, ap.Rectangle)\n```': '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    background_color=ap.Color("#333"),\n    stage_width=450,\n    stage_height=150,\n    stage_elem_id="stage",\n)\n\nsprite: ap.Sprite = ap.Sprite()\nsprite.graphics.begin_fill(color=ap.Color("#0af"))\nrectangle_1: ap.Rectangle = sprite.graphics.draw_rect(x=50, y=50, width=50, height=50)\nsprite.add_child(rectangle_1)\n\nfirst_child: ap.DisplayObject = sprite.get_child_at(index=0)\nassert isinstance(first_child, ap.Graphics)\n\nsecond_child: ap.DisplayObject = sprite.get_child_at(index=1)\nassert isinstance(second_child, ap.Rectangle)\n```',  # noqa
    ##################################################
    "## get_child_at API": "## get_child_at API",
    ##################################################
    '<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>': '<span class="inconspicuous-txt">特記事項: このAPIドキュメントはドキュメントビルド用のスクリプトによって自動で生成・同期されています。そのためもしかしたらこの節の内容は前節までの内容と重複している場合があります。</span>',  # noqa
    ##################################################
    "**[Interface summary]**": "**[インターフェイス概要]**",
    ##################################################
    "Get a child at a specified index.<hr>": "指定されたインデックスの子を取得します。<hr>",
    ##################################################
    "**[Parameters]**": "**[引数]**",
    ##################################################
    "- `index`: int or Int": "- `index`: int or Int",
    ##################################################
    "  - Child's index (start from 0).": "  - 対象の子のインデックス（0からスタートします）。",
    ##################################################
    "<hr>": "<hr>",
    ##################################################
    "**[Returns]**": "**[返却値]**",
    ##################################################
    "- `child`: DisplayObject": "- `child`: DisplayObject",
    ##################################################
    "  - Target index child instance.": "  - 対象の子のインスタンス。",
    ##################################################
    "<hr>": "<hr>",
    ##################################################
    "**[Examples]**": "**[コードサンプル]**",
    ##################################################
    '```py\n>>> import apysc as ap\n>>> stage: ap.Stage = ap.Stage()\n>>> sprite: ap.Sprite = ap.Sprite()\n>>> sprite.graphics.begin_fill(color=ap.Color("#0af"), alpha=0.5)\n>>> rectangle_1: ap.Rectangle = sprite.graphics.draw_rect(\n...     x=50, y=50, width=50, height=50\n... )\n>>> rectangle_2: ap.Rectangle = sprite.graphics.draw_rect(\n...     x=150, y=50, width=50, height=50\n... )\n>>> child_at_index_1: ap.DisplayObject = sprite.graphics.get_child_at(1)\n>>> child_at_index_1 == rectangle_2\nTrue\n```': '```py\n>>> import apysc as ap\n>>> stage: ap.Stage = ap.Stage()\n>>> sprite: ap.Sprite = ap.Sprite()\n>>> sprite.graphics.begin_fill(color=ap.Color("#0af"), alpha=0.5)\n>>> rectangle_1: ap.Rectangle = sprite.graphics.draw_rect(\n...     x=50, y=50, width=50, height=50\n... )\n>>> rectangle_2: ap.Rectangle = sprite.graphics.draw_rect(\n...     x=150, y=50, width=50, height=50\n... )\n>>> child_at_index_1: ap.DisplayObject = sprite.graphics.get_child_at(1)\n>>> child_at_index_1 == rectangle_2\nTrue\n```',  # noqa
}
