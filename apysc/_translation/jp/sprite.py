"""This module is for the translation mapping data of the
following document:

Document file: sprite.md
Language: jp
"""

from typing import Dict

MAPPING: Dict[str, str] = {
    ##################################################
    "# Sprite class": "# Spriteクラス",
    ##################################################
    "This page explains the `Sprite` class.": "このページでは、`Sprite`クラスについて説明します。",
    ##################################################
    "## What is the Sprite?": "## Spriteとは？",
    ##################################################
    "The `Sprite` class is the container of each `DisplayObject` instance. It also has the `Graphics` class interfaces and can draw each vector graphic.": "`Sprite`クラスは、各`DisplayObject`インスタンスのコンテナです。また、`Graphics`クラスのインタフェースを持ち、各ベクターグラフィックを描画することができます。",  # noqa
    ##################################################
    "## Note for the automated addition": "## インスタンスの自動追加に関する注意点",
    ##################################################
    "The `Sprite` instance is automated added to the stage (no need to call `add_child` or other related interfaces). However, suppose you want to add to the other instance. In that case, you need to call the `add_child` method manually.": "`Sprite`のインスタンスは自動的にステージに追加されます（`add_child`などの関連インタフェースを呼び出す必要はありません）。一方で、もし他のインスタンスに`Sprite`のインスタンスを追加したいと場合、手動で `add_child` メソッドを呼び出す必要があります。",  # noqa
    ##################################################
    "## graphics attribute interfaces": "## graphics属性のインタフェース",
    ##################################################
    "The `Sprite` instance has the `graphics` attribute, and you can draw each vector graphic with it. For example, the following code draws the cyan color rectangle.": "`Sprite`クラスのインスタンスは`graphics`属性を持っており、それを使って各ベクターグラフィックを描画することができます。例えば以下のコードでは水色の四角を描画します。",  # noqa
    ##################################################
    '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    background_color="#333", stage_width=150, stage_height=150, stage_elem_id="stage"\n)\n\nsprite: ap.Sprite = ap.Sprite()\nsprite.graphics.begin_fill(color="#0af")\nsprite.graphics.draw_rect(x=50, y=50, width=50, height=50)\n\nap.save_overall_html(dest_dir_path="sprite_graphics_attribute/")\n```': '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    background_color="#333", stage_width=150, stage_height=150, stage_elem_id="stage"\n)\n\nsprite: ap.Sprite = ap.Sprite()\nsprite.graphics.begin_fill(color="#0af")\nsprite.graphics.draw_rect(x=50, y=50, width=50, height=50)\n\nap.save_overall_html(dest_dir_path="sprite_graphics_attribute/")\n```',  # noqa
    ##################################################
    "For more details, please see the `Graphics` related documents, for example:": "詳細は以下の`Graphics`クラスの関連ドキュメントをご覧ください。",  # noqa
    ##################################################
    "- [Graphics class](graphics.md)": "- [Graphics クラス](jp_graphics.md)",
    ##################################################
    "- [Graphics begin_fill interface](graphics_begin_fill.md)": "- [Graphics クラス begin_fill （塗り設定）のインターフェイス](jp_graphics_begin_fill.md)",  # noqa
    ##################################################
    "- [Graphics line_style interface](graphics_line_style.md)": "- [Graphics クラス line_style （線設定）のインターフェイス](jp_graphics_line_style.md)",  # noqa
    ##################################################
    "- [Graphics draw_rect interface](graphics_draw_rect.md)": "- [Graphics クラス draw_rect （四角描画）のインターフェイス](jp_graphics_draw_rect.md)",  # noqa
    ##################################################
    "- [Graphics draw_circle interface](graphics_draw_circle.md)": "- [Graphics クラス draw_circle （円描画）のインターフェイス](jp_graphics_draw_circle.md)",  # noqa
    ##################################################
    "## Move DisplayObject instances simultaneously": "## DisplayObjectの複数のインスタンスの移動について",  # noqa
    ##################################################
    "The `Sprite` class is a container, and if you move that coordinates, it changes children's coordinates simultaneously. For example, the following code changes the sprite y-coordinate when clicking the rectangle.": "`Sprite`クラスはコンテナであり、その座標を移動させると同時に子のインスタンスの座標も変更されます。例えば以下のコードでは四角をクリックするとSpriteのy座標が変化します（子の各四角形が一通り移動します）。",  # noqa
    ##################################################
    '```py\n# runnable\nimport apysc as ap\n\n\ndef on_sprite_click(e: ap.MouseEvent[ap.Sprite], options: dict) -> None:\n    """\n    The handler that the sprite calls when clicked.\n\n    Parameters\n    ----------\n    e : MouseEvent\n        Event instance.\n    options : dict\n        Optional arguments dictionary.\n    """\n    sprite: ap.Sprite = e.this\n    sprite.y += 50\n\n\nap.Stage(\n    background_color="#333", stage_width=250, stage_height=250, stage_elem_id="stage"\n)\n\nsprite: ap.Sprite = ap.Sprite()\nsprite.graphics.begin_fill(color="#0af")\nsprite.graphics.draw_rect(x=50, y=50, width=50, height=50)\nsprite.graphics.draw_rect(x=150, y=50, width=50, height=50)\nsprite.click(on_sprite_click)\n\nap.save_overall_html(dest_dir_path="sprite_move_instances_simultaneously/")\n```': '```py\n# runnable\nimport apysc as ap\n\n\ndef on_sprite_click(e: ap.MouseEvent[ap.Sprite], options: dict) -> None:\n    """\n    The handler that the sprite calls when clicked.\n\n    Parameters\n    ----------\n    e : MouseEvent\n        Event instance.\n    options : dict\n        Optional arguments dictionary.\n    """\n    sprite: ap.Sprite = e.this\n    sprite.y += 50\n\n\nap.Stage(\n    background_color="#333", stage_width=250, stage_height=250, stage_elem_id="stage"\n)\n\nsprite: ap.Sprite = ap.Sprite()\nsprite.graphics.begin_fill(color="#0af")\nsprite.graphics.draw_rect(x=50, y=50, width=50, height=50)\nsprite.graphics.draw_rect(x=150, y=50, width=50, height=50)\nsprite.click(on_sprite_click)\n\nap.save_overall_html(dest_dir_path="sprite_move_instances_simultaneously/")\n```',  # noqa
    ##################################################
    "The subsequent pages explain the other interfaces, such as the `add_child` interface.": "以降のページでは`add_child`のインターフェースなど、Spriteクラスの他のインターフェースについて説明していきます。",  # noqa
    ##################################################
    "## See also": "## 関連資料",
    ##################################################
    "- [add_child and remove_child interfaces](add_child_and_remove_child.md)": "- [add_child （子の追加）と remove_child （子の削除）のインターフェイス](jp_add_child_and_remove_child.md)",  # noqa
    ##################################################
    "- [contains interface](contains.md)": "- [contains インターフェイス](jp_contains.md)",
    ##################################################
    "- [num_children interface](num_children.md)": "- [num_children （子の件数属性）のインターフェイス](jp_num_children.md)",  # noqa
    ##################################################
    "- [get_child_at interface](get_child_at.md)": "- [get_child_at （特定位置の子の取得処理）のインターフェイス](jp_get_child_at.md)",  # noqa
    ##################################################
    "## Sprite class constructor API": "## SpriteクラスのコンストラクタAPI",
    ##################################################
    '<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>': '<span class="inconspicuous-txt">特記事項: このAPIドキュメントはドキュメントビルド用のスクリプトによって自動で生成・同期されています。そのためもしかしたらこの節の内容は前節までの内容と重複している場合があります。</span>',  # noqa
    ##################################################
    "**[Interface summary]**": "**[インターフェイス概要]**",
    ##################################################
    "Create a basic display object that can be a parent.<hr>": "親になることの出来る基本的な表示用のオブジェクトを作成します。<hr>",  # noqa
    ##################################################
    "**[Parameters]**": "**[引数]**",
    ##################################################
    "- `variable_name`: str, default '": "- `variable_name`: str, default '",
    ##################################################
    "  - Variable name of this instance. A js expression uses this setting. It is unnecessary to specify any string except when instantiating the `Sprite` subclass.": "  - このインスタンスの（JavaScript上などで使われる）変数名の設定値。apyscの内部実装で`Sprite`クラスのサブクラスをインスタンス化する時以外は設定は不要です。",  # noqa
    ##################################################
    "- `variable_name_suffix`: str, default ''": "- `variable_name_suffix`: str, default ''",  # noqa
    ##################################################
    "  - A JavaScript variable name suffix string. This setting is sometimes useful for JavaScript debugging.": "  - JavaScript上の変数のサフィックスの設定です。この設定はJavaScriptのデバッグ時に役立つことがあります。",  # noqa
    ##################################################
    "<hr>": "<hr>",
    ##################################################
    "**[Examples]**": "**[コードサンプル]**",
    ##################################################
    '```py\n>>> import apysc as ap\n>>> stage: ap.Stage = ap.Stage()\n>>> sprite_1: ap.Sprite = ap.Sprite()\n>>> # Create the sprite child rectangle\n>>> sprite_1.graphics.begin_fill(color="#0af")\n>>> rect: ap.Rectangle = sprite_1.graphics.draw_rect(\n...     x=50, y=50, width=50, height=50\n... )\n>>> sprite_1.graphics.contains(rect)\nBoolean(True)\n\n>>> # Move the created rectangle to the other sprite\n>>> sprite_2: ap.Sprite = ap.Sprite()\n>>> sprite_2.add_child(rect)\n>>> sprite_1.graphics.contains(rect)\nBoolean(False)\n\n>>> sprite_2.contains(rect)\nBoolean(True)\n\n>>> # Move the sprite container\n>>> sprite_2.x = ap.Number(50)\n>>> sprite_2.x\nNumber(50.0)\n```': '```py\n>>> import apysc as ap\n>>> stage: ap.Stage = ap.Stage()\n>>> sprite_1: ap.Sprite = ap.Sprite()\n>>> # Create the sprite child rectangle\n>>> sprite_1.graphics.begin_fill(color="#0af")\n>>> rect: ap.Rectangle = sprite_1.graphics.draw_rect(\n...     x=50, y=50, width=50, height=50\n... )\n>>> sprite_1.graphics.contains(rect)\nBoolean(True)\n\n>>> # Move the created rectangle to the other sprite\n>>> sprite_2: ap.Sprite = ap.Sprite()\n>>> sprite_2.add_child(rect)\n>>> sprite_1.graphics.contains(rect)\nBoolean(False)\n\n>>> sprite_2.contains(rect)\nBoolean(True)\n\n>>> # Move the sprite container\n>>> sprite_2.x = ap.Number(50)\n>>> sprite_2.x\nNumber(50.0)\n```',  # noqa
}
