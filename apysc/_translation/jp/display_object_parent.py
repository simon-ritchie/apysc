"""This module is for the translation mapping data of the
following document:

Document file: display_object_parent.md
Language: jp
"""

from typing import Dict

MAPPING: Dict[str, str] = {
    ##################################################
    "# DisplayObject class parent interfaces": "# DisplayObject クラスの parent インターフェイス",
    ##################################################
    "This page explains the `DisplayObject` class `parent` interfaces (the `parent` property and `remove_from_parent` method).": "このページでは`DisplayObject`クラスの`parent`関係のインターフェイス（`parent`属性と`remove_from_parent`メソッド）について説明します。",  # noqa
    ##################################################
    "## What interfaces are these?": "## 各インターフェイスの概要",
    ##################################################
    "The `parent` attribute is the getter property. This attribute becomes a `Stage` instance or a container instance like a `Sprite` instance.": "`parent`属性はgetterのみのインターフェイスとなります。この属性値は`Stage`のインスタンスもしくは`Sprite`などのコンテナのインスタンスとなります。",  # noqa
    ##################################################
    '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    background_color=ap.Color("#333"),\n    stage_width=150,\n    stage_height=200,\n    stage_elem_id="stage",\n)\n\nsprite: ap.Sprite = ap.Sprite()\nrectangle: ap.Rectangle = sprite.graphics.draw_rect(x=50, y=50, width=50, height=50)\n\nassert isinstance(sprite.parent, ap.Stage)\nassert isinstance(sprite.graphics.parent, ap.Sprite)\nassert isinstance(rectangle.parent, ap.Graphics)\n```': '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    background_color=ap.Color("#333"),\n    stage_width=150,\n    stage_height=200,\n    stage_elem_id="stage",\n)\n\nsprite: ap.Sprite = ap.Sprite()\nrectangle: ap.Rectangle = sprite.graphics.draw_rect(x=50, y=50, width=50, height=50)\n\nassert isinstance(sprite.parent, ap.Stage)\nassert isinstance(sprite.graphics.parent, ap.Sprite)\nassert isinstance(rectangle.parent, ap.Graphics)\n```',  # noqa
    ##################################################
    "The `remove_from_parent` interface removes self-instance from the parent (and not be displayed on the stage).": "`remove_from_parent`インターフェイスは自身のインスタンスを親のインスタンスから取り除き、画面上に表示されない状態にします。",  # noqa
    ##################################################
    "## Basic usage of the remove_from_parent interface": "## remove_from_parent インターフェイスの基本的な使い方",  # noqa
    ##################################################
    "The `remove_from_parent` method interface (no argument options) removes the self-instance from the parent. A Removed instance is not displayed until any parent adds it again.": "`remove_from_parent`メソッドのインターフェイス（引数を必要としません）は自身のインスタンスを親のインスタンスから取り除きます。取り除かれたインスタンスは他の親（コンテナ）のインスタンスへと追加されるまで画面に表示されません。",  # noqa
    ##################################################
    '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    background_color=ap.Color("#333"),\n    stage_width=150,\n    stage_height=150,\n    stage_elem_id="stage",\n)\n\nsprite: ap.Sprite = ap.Sprite()\nrectangle: ap.Rectangle = sprite.graphics.draw_rect(x=50, y=50, width=50, height=50)\n\n# Remove the rectangle from the parent, and nothing displays\n# on the stage.\nrectangle.remove_from_parent()\n\nap.save_overall_html(dest_dir_path="display_object_remove_from_parent_basic_usage/")\n```': '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    background_color=ap.Color("#333"),\n    stage_width=150,\n    stage_height=150,\n    stage_elem_id="stage",\n)\n\nsprite: ap.Sprite = ap.Sprite()\nrectangle: ap.Rectangle = sprite.graphics.draw_rect(x=50, y=50, width=50, height=50)\n\n# Remove the rectangle from the parent, and nothing displays\n# on the stage.\nrectangle.remove_from_parent()\n\nap.save_overall_html(dest_dir_path="display_object_remove_from_parent_basic_usage/")\n```',  # noqa
    ##################################################
    "## See also": "## 関連資料",
    ##################################################
    "- [add_child and remove_child interfaces](add_child_and_remove_child.md)": "- [add_child （子の追加）と remove_child （子の削除）のインターフェイス](jp_add_child_and_remove_child.md)",  # noqa
    ##################################################
    "## parent API": "## parent API",
    ##################################################
    '<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>': '<span class="inconspicuous-txt">特記事項: このAPIドキュメントはドキュメントビルド用のスクリプトによって自動で生成・同期されています。そのためもしかしたらこの節の内容は前節までの内容と重複している場合があります。</span>',  # noqa
    ##################################################
    "**[Interface summary]**": "**[インターフェイス概要]**",
    ##################################################
    "Get a parent instance that has an add_child and remove_child interfaces.<hr>": "add_childやremove_childなどのインターフェイスを持った親のインスタンスを取得します。<hr>",  # noqa
    ##################################################
    "**[Returns]**": "**[返却値]**",
    ##################################################
    "- `parent`: any parent instance (ChildMixIn) or None": "- `parent`: any parent instance (ChildMixIn) or None",  # noqa
    ##################################################
    "  - Parent instance with `add_child` and `remove_child` interfaces. If this instance does not have a parent instance (not added child), this interface returns None.": "  - `add_child`や`remove_child`などのインターフェイスを持っている親のインスタンス。もしこのインスタンスが親を持っていない（画面に追加されていない）場合、このインターフェイスはNoneを返却します。",  # noqa
    ##################################################
    "<hr>": "<hr>",
    ##################################################
    "**[Examples]**": "**[コードサンプル]**",
    ##################################################
    '```py\n>>> import apysc as ap\n>>> stage: ap.Stage = ap.Stage()\n>>> sprite_1: ap.Sprite = ap.Sprite()\n>>> sprite_1.graphics.begin_fill(color=ap.Color("#0af"))\n>>> rectangle: ap.Rectangle = sprite_1.graphics.draw_rect(\n...     x=50, y=50, width=50, height=50\n... )\n>>> sprite_2: ap.Sprite = ap.Sprite()\n>>> sprite_2.add_child(rectangle)\n>>> rectangle.parent == sprite_2\nTrue\n```': '```py\n>>> import apysc as ap\n>>> stage: ap.Stage = ap.Stage()\n>>> sprite_1: ap.Sprite = ap.Sprite()\n>>> sprite_1.graphics.begin_fill(color=ap.Color("#0af"))\n>>> rectangle: ap.Rectangle = sprite_1.graphics.draw_rect(\n...     x=50, y=50, width=50, height=50\n... )\n>>> sprite_2: ap.Sprite = ap.Sprite()\n>>> sprite_2.add_child(rectangle)\n>>> rectangle.parent == sprite_2\nTrue\n```',  # noqa
    ##################################################
    "## remove_from_parent API": "## remove_from_parent API",
    ##################################################
    '<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>': '<span class="inconspicuous-txt">特記事項: このAPIドキュメントはドキュメントビルド用のスクリプトによって自動で生成・同期されています。そのためもしかしたらこの節の内容は前節までの内容と重複している場合があります。</span>',  # noqa
    ##################################################
    "**[Interface summary]**": "**[インターフェイス概要]**",
    ##################################################
    "Remove this instance from a parent.<hr>": "親のインスタンスからこのインスタンスを取り除きます。<hr>",
    ##################################################
    "**[Raises]**": "**[エラー発生条件]**",
    ##################################################
    "- ValueError: If a parent is None (there is no parent).": "- ValueError: もしも親のインスタンスがNoneの場合（親の無い状態の場合）。",  # noqa
}
