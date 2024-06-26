"""This module is for the translation mapping data of the
following document:

Document file: add_child_and_remove_child.md
Language: jp
"""

from typing import Dict

MAPPING: Dict[str, str] = {
    ##################################################
    "# add_child and remove_child interfaces": "# add_child と remove_child インターフェイス",
    ##################################################
    "This page explains the container class, like the `Graphics`\\, `Sprite`\\, `Stage`) `add_child` and `remove_child` method interfaces.": "このページではGraphicsクラスやSprite、Stageクラスなどのコンテナーとして扱えるクラスが持つ`add_child`と`remove_child`のインターフェイスについて説明します。",  # noqa
    ##################################################
    "## What interfaces are these?": "## 各インターフェイスの概要",
    ##################################################
    "The `add_child` and `remove_child` add or remove a `DisplayObject` child instance from a container instance. The apysc does not display a removed `DisplayObject` instance.": "`add_child`インターフェイスではコンテナーのインスタンスへ子となる各`DisplayObject`を継承したインスタンスを追加し、逆に`remove_child`インターフェイスでは子のインスタンスをコンテナーから取り除きます。apyscでは取り除かれた子のインスタンスは表示されなくなります。",  # noqa
    ##################################################
    "## Automatic addition of the children": "## 子のインスタンスの自動追加について",
    ##################################################
    "The apysc appends each `DisplayObject` instance to a parent at the constructor. So, for example, it appends a `Sprite` instance to a parent stage. Similarly, it appends an instance of a graphic to a parent `Sprite` instance.": "apyscでは各`DisplayObject`のインスタンスはコンストラクタの時点で親のインスタンスへと自動で追加されます。例えば`Sprite`クラスであれば`Stage`クラスのインスタンスを親として追加され、`Sprite`クラスを親として内部で作成される`graphics`プロパティのインスタンスは`Sprite`クラスのインスタンスへと自動で追加されます。",  # noqa
    ##################################################
    "If you need to adjust a parent, it is necessary to call the `add_child` or `remove_child` interfaces manually (for instance, set a `Sprite` parent to the other `Sprite`).": "もし親のインスタンスを調整したい場合には手動で`add_child`や`remove_child`などのインターフェイスを呼ぶ必要があります。例えば親としてのとある`Sprite`クラスのインスタンスから別の`Sprite`クラスのインスタンスに子を移したい場合などが該当します。",  # noqa
    ##################################################
    "## Basic usage of the remove_child interface": "## remove_child インターフェイスの基本的な使い方",
    ##################################################
    "The `remove_child` interface removes a child from a parent container instance. The apysc does not display a removed `DisplayObject` instance.": "`remove_child`インターフェイスでは子を親のコンテナー要素から取り除きます。apyscは取り除かれた`DisplayObject`の子のインスタンスを表示しません。",  # noqa
    ##################################################
    "For example, the following code calls the `remove_child` interface in the click handler, so if you click the rectangle, it removes that rectangle.": "例えば以下のコードでは四角をクリックした際のハンドラ内で`remove_child`インターフェイスを呼び出しており、クリック時に四角が画面から取り除かれます。",  # noqa
    ##################################################
    '```py\n# runnable\nfrom typing_extensions import TypedDict\n\nimport apysc as ap\n\n\nclass _RectOptions(TypedDict):\n    rectangle: ap.Rectangle\n\n\ndef on_sprite_click(e: ap.MouseEvent[ap.Sprite], options: _RectOptions) -> None:\n    """\n    The handler that the sprite calls when clicked.\n\n    Parameters\n    ----------\n    e : MouseEvent\n        Event instance.\n    options : dict\n        Optional arguments dictionary.\n    """\n    sprite: ap.Sprite = e.this\n    rectangle: ap.Rectangle = options["rectangle"]\n    sprite.remove_child(child=rectangle)\n\n\nap.Stage(\n    background_color=ap.Color("#333"),\n    stage_width=150,\n    stage_height=150,\n    stage_elem_id="stage",\n)\n\nsprite: ap.Sprite = ap.Sprite()\nsprite.graphics.begin_fill(color=ap.Color("#0af"))\nrectangle: ap.Rectangle = sprite.graphics.draw_rect(x=50, y=50, width=50, height=50)\noptions: _RectOptions = {"rectangle": rectangle}\nsprite.click(on_sprite_click, options=options)\n\nap.save_overall_html(dest_dir_path="sprite_basic_usage_of_remove_child/")\n```': '```py\n# runnable\nfrom typing_extensions import TypedDict\n\nimport apysc as ap\n\n\nclass _RectOptions(TypedDict):\n    rectangle: ap.Rectangle\n\n\ndef on_sprite_click(e: ap.MouseEvent[ap.Sprite], options: _RectOptions) -> None:\n    """\n    The handler that the sprite calls when clicked.\n\n    Parameters\n    ----------\n    e : MouseEvent\n        Event instance.\n    options : dict\n        Optional arguments dictionary.\n    """\n    sprite: ap.Sprite = e.this\n    rectangle: ap.Rectangle = options["rectangle"]\n    sprite.remove_child(child=rectangle)\n\n\nap.Stage(\n    background_color=ap.Color("#333"),\n    stage_width=150,\n    stage_height=150,\n    stage_elem_id="stage",\n)\n\nsprite: ap.Sprite = ap.Sprite()\nsprite.graphics.begin_fill(color=ap.Color("#0af"))\nrectangle: ap.Rectangle = sprite.graphics.draw_rect(x=50, y=50, width=50, height=50)\noptions: _RectOptions = {"rectangle": rectangle}\nsprite.click(on_sprite_click, options=options)\n\nap.save_overall_html(dest_dir_path="sprite_basic_usage_of_remove_child/")\n```',  # noqa
    ##################################################
    "## The basic usage of the add_child interface": "## add_child インターフェイスの基本的な使い方",
    ##################################################
    "The `add_child` interface adds a removed child again or adds a child to the other container instance.": "`add_child`インターフェイスは取り除かれた子のインスタンスをもう一度他の親のコンテナーのインスタンスへと追加します。",  # noqa
    ##################################################
    "The following code example removes the rectangle from the first `Sprite` container (be positioned to the left) when you click the rectangle. Also, that click event adds the rectangle to the second `Sprite` container (be positioned to the right).": "以下のコードでは四角をクリックした際に1つ目の左に配置されている`Sprite`の親のコンテナーからその四角を取り除き、そして2つ目の右側に配置してある`Sprite`のインスタンスへと子を追加しています。",  # noqa
    ##################################################
    '```py\n# runnable\nfrom typing_extensions import TypedDict\n\nimport apysc as ap\n\n\nclass _SpriteAndRectOptions(TypedDict):\n    rectangle: ap.Rectangle\n    sprite: ap.Sprite\n\n\ndef on_sprite_click(\n    e: ap.MouseEvent[ap.Sprite], options: _SpriteAndRectOptions\n) -> None:\n    """\n    The handler that the sprite calls when clicked.\n\n    Parameters\n    ----------\n    e : MouseEvent\n        Event instance.\n    options : dict\n        Optional arguments dictionary.\n    """\n    first_sprite: ap.Sprite = e.this\n    rectangle: ap.Rectangle = options["rectangle"]\n    second_sprite: ap.Sprite = options["sprite"]\n    first_sprite.remove_child(child=rectangle)\n    second_sprite.add_child(child=rectangle)\n\n\nap.Stage(\n    background_color=ap.Color("#333"),\n    stage_width=250,\n    stage_height=150,\n    stage_elem_id="stage",\n)\n\nfirst_sprite: ap.Sprite = ap.Sprite()\nfirst_sprite.graphics.begin_fill(color=ap.Color("#0af"))\nfirst_sprite.x = ap.Number(50)\nfirst_sprite.y = ap.Number(50)\nrectangle: ap.Rectangle = first_sprite.graphics.draw_rect(x=0, y=0, width=50, height=50)\n\nsecond_sprite: ap.Sprite = ap.Sprite()\nsecond_sprite.x = ap.Number(150)\nsecond_sprite.y = ap.Number(50)\n\noptions: _SpriteAndRectOptions = {"rectangle": rectangle, "sprite": second_sprite}\nfirst_sprite.click(on_sprite_click, options=options)\n\nap.save_overall_html(dest_dir_path="sprite_basic_usage_of_add_child/")\n```': '```py\n# runnable\nfrom typing_extensions import TypedDict\n\nimport apysc as ap\n\n\nclass _SpriteAndRectOptions(TypedDict):\n    rectangle: ap.Rectangle\n    sprite: ap.Sprite\n\n\ndef on_sprite_click(\n    e: ap.MouseEvent[ap.Sprite], options: _SpriteAndRectOptions\n) -> None:\n    """\n    The handler that the sprite calls when clicked.\n\n    Parameters\n    ----------\n    e : MouseEvent\n        Event instance.\n    options : dict\n        Optional arguments dictionary.\n    """\n    first_sprite: ap.Sprite = e.this\n    rectangle: ap.Rectangle = options["rectangle"]\n    second_sprite: ap.Sprite = options["sprite"]\n    first_sprite.remove_child(child=rectangle)\n    second_sprite.add_child(child=rectangle)\n\n\nap.Stage(\n    background_color=ap.Color("#333"),\n    stage_width=250,\n    stage_height=150,\n    stage_elem_id="stage",\n)\n\nfirst_sprite: ap.Sprite = ap.Sprite()\nfirst_sprite.graphics.begin_fill(color=ap.Color("#0af"))\nfirst_sprite.x = ap.Number(50)\nfirst_sprite.y = ap.Number(50)\nrectangle: ap.Rectangle = first_sprite.graphics.draw_rect(x=0, y=0, width=50, height=50)\n\nsecond_sprite: ap.Sprite = ap.Sprite()\nsecond_sprite.x = ap.Number(150)\nsecond_sprite.y = ap.Number(50)\n\noptions: _SpriteAndRectOptions = {"rectangle": rectangle, "sprite": second_sprite}\nfirst_sprite.click(on_sprite_click, options=options)\n\nap.save_overall_html(dest_dir_path="sprite_basic_usage_of_add_child/")\n```',  # noqa
    ##################################################
    "## See also": "## 関連資料",
    ##################################################
    "- [DisplayObject class parent interfaces](display_object_parent.md)": "- [DisplayObjectクラス parent （親要素属性）のインターフェイス](jp_display_object_parent.md)",  # noqa
    ##################################################
    "- [contains interface](contains.md)": "- [contains インターフェイス](jp_contains.md)",
    ##################################################
    "## add_child API": "## add_child API",
    ##################################################
    '<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>': '<span class="inconspicuous-txt">特記事項: このAPIドキュメントはドキュメントビルド用のスクリプトによって自動で生成・同期されています。そのためもしかしたらこの節の内容は前節までの内容と重複している場合があります。</span>',  # noqa
    ##################################################
    "**[Interface summary]**": "**[インターフェイス概要]**",
    ##################################################
    "Add display object child to this instance.<hr>": "表示オブジェクトの子をこのインスタンスへと追加します。<hr>",  # noqa
    ##################################################
    "**[Parameters]**": "**[引数]**",
    ##################################################
    "- `child`: DisplayObject": "- `child`: DisplayObject",
    ##################################################
    "  - Child instance to add.": "  - 追加する子のインスタンス。",
    ##################################################
    "<hr>": "<hr>",
    ##################################################
    "**[Examples]**": "**[コードサンプル]**",
    ##################################################
    '```py\n>>> import apysc as ap\n>>> stage: ap.Stage = ap.Stage()\n>>> sprite_1: ap.Sprite = ap.Sprite()\n>>> sprite_1.graphics.begin_fill(color=ap.Color("#0af"))\n>>> rectangle: ap.Rectangle = sprite_1.graphics.draw_rect(\n...     x=50, y=50, width=50, height=50\n... )\n>>> sprite_2: ap.Sprite = ap.Sprite()\n>>> sprite_2.add_child(rectangle)\n```': '```py\n>>> import apysc as ap\n>>> stage: ap.Stage = ap.Stage()\n>>> sprite_1: ap.Sprite = ap.Sprite()\n>>> sprite_1.graphics.begin_fill(color=ap.Color("#0af"))\n>>> rectangle: ap.Rectangle = sprite_1.graphics.draw_rect(\n...     x=50, y=50, width=50, height=50\n... )\n>>> sprite_2: ap.Sprite = ap.Sprite()\n>>> sprite_2.add_child(rectangle)\n```',  # noqa
    ##################################################
    "## remove_child API": "## remove_child API",
    ##################################################
    '<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>': '<span class="inconspicuous-txt">特記事項: このAPIドキュメントはドキュメントビルド用のスクリプトによって自動で生成・同期されています。そのためもしかしたらこの節の内容は前節までの内容と重複している場合があります。</span>',  # noqa
    ##################################################
    "**[Interface summary]**": "**[インターフェイス概要]**",
    ##################################################
    "Remove display object child from this instance.<hr>": "このインスタンスから指定された表示オブジェクトの子を取り除きます。<hr>",  # noqa
    ##################################################
    "**[Parameters]**": "**[引数]**",
    ##################################################
    "- `child`: DisplayObject": "- `child`: DisplayObject",
    ##################################################
    "  - Child instance to remove.": "  - 取り除く対象の子のインスタンス。",
    ##################################################
    "<hr>": "<hr>",
    ##################################################
    "**[Examples]**": "**[コードサンプル]**",
    ##################################################
    '```py\n>>> import apysc as ap\n>>> stage: ap.Stage = ap.Stage()\n>>> sprite: ap.Sprite = ap.Sprite()\n>>> sprite.graphics.begin_fill(color=ap.Color("#0af"), alpha=0.5)\n>>> rectangle: ap.Rectangle = sprite.graphics.draw_rect(\n...     x=50, y=50, width=50, height=50\n... )\n>>> sprite.graphics.remove_child(rectangle)\n>>> print(rectangle.parent)\nNone\n```': '```py\n>>> import apysc as ap\n>>> stage: ap.Stage = ap.Stage()\n>>> sprite: ap.Sprite = ap.Sprite()\n>>> sprite.graphics.begin_fill(color=ap.Color("#0af"), alpha=0.5)\n>>> rectangle: ap.Rectangle = sprite.graphics.draw_rect(\n...     x=50, y=50, width=50, height=50\n... )\n>>> sprite.graphics.remove_child(rectangle)\n>>> print(rectangle.parent)\nNone\n```',  # noqa
}
