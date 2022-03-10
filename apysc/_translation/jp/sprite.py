"""This module is for the translation mapping data of the
following document:

Document file: sprite.md
Language: jp
"""

from typing import Dict

MAPPING: Dict[str, str] = {

    '# Sprite (English document)':
    '# Sprite (日本語ドキュメント)',

    'This page explains the `Sprite` class.':
    'このページでは、`Sprite`クラスについて説明します。',

    '## What is the Sprite?':
    '## Spriteとは？',

    'The `Sprite` class is the container of each `DisplayObject` instance. It also has the `Graphics` class interfaces and can draw each vector graphic.':  # noqa
    '`Sprite`クラスは、各`DisplayObject`インスタンスのコンテナです。また、`Graphics`クラスのインタフェースを持ち、各ベクターグラフィックを描画することができます。',  # noqa

    '## Note for the automated addition':
    '## インスタンスの自動追加に関する注意点',

    'The `Sprite` instance is automated added to the stage (no need to call `add_child` or other related interfaces). However, suppose you want to add to the other instance. In that case, you need to call the `add_child` method manually.':  # noqa
    '`Sprite`のインスタンスは自動的にステージに追加されます（`add_child`などの関連インタフェースを呼び出す必要はありません）。一方で、もし他のインスタンスに`Sprite`のインスタンスを追加したいと場合、手動で `add_child` メソッドを呼び出す必要があります。',  # noqa

    '## graphics attribute interfaces':
    '## graphics属性のインタフェース',

    'The `Sprite` instance has the `graphics` attribute, and you can draw each vector graphic with it. For example, the following code draws the cyan color rectangle.':  # noqa
    '`Sprite`クラスのインスタンスは`graphics`属性を持っており、それを使って各ベクターグラフィックを描画することができます。例えば以下のコードでは水色の四角を描画します。',  # noqa

    '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    background_color=\'#333\',\n    stage_width=150,\n    stage_height=150,\n    stage_elem_id=\'stage\')\n\nsprite: ap.Sprite = ap.Sprite()\nsprite.graphics.begin_fill(color=\'#0af\')\nsprite.graphics.draw_rect(x=50, y=50, width=50, height=50)\n\nap.save_overall_html(\n    dest_dir_path=\'sprite_graphics_attribute/\')\n```':  # noqa
    '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    background_color=\'#333\',\n    stage_width=150,\n    stage_height=150,\n    stage_elem_id=\'stage\')\n\nsprite: ap.Sprite = ap.Sprite()\nsprite.graphics.begin_fill(color=\'#0af\')\nsprite.graphics.draw_rect(x=50, y=50, width=50, height=50)\n\nap.save_overall_html(\n    dest_dir_path=\'sprite_graphics_attribute/\')\n```',  # noqa

    'For more details, please see the `Graphics` related documents, for example:':  # noqa
    '詳細は以下の`Graphics`クラスの関連ドキュメントをご覧ください。',

    '- [Graphics class](graphics.md)\n- [Graphics begin_fill interface](graphics_begin_fill.md)\n- [Graphics line_style interface](graphics_line_style.md)\n- [Graphics draw_rect interface](graphics_draw_rect.md)\n- [Graphics draw_circle interface](graphics_draw_circle.md)':  # noqa
    '- [Graphicsクラス](jp_graphics.md)\n\n- [Graphicsクラス begin_fill インターフェイス](jp_graphics_begin_fill.md)\n\n- [Graphicsクラス line_style インターフェイス](jp_graphics_line_style.md)\n\n- [Graphicsクラス draw_rect インターフェイス](jp_graphics_draw_rect.md)\n\n- [Graphicsクラス draw_circle インターフェイス](jp_graphics_draw_circle.md)',  # noqa

    '## Move DisplayObject instances simultaneously':
    '## DisplayObjectの複数のインスタンスの移動について',

    'The `Sprite` class is a container, and if you move that coordinates, it changes children\'s coordinates simultaneously. For example, the following code changes the sprite y-coordinate when clicking the rectangle.':  # noqa
    '`Sprite`クラスはコンテナであり、その座標を移動させると同時に子のインスタンスの座標も変更されます。例えば以下のコードでは四角をクリックするとSpriteのy座標が変化します（子の各四角形が一通り移動します）。',  # noqa

    '```py\n# runnable\nimport apysc as ap\n\n\ndef on_sprite_click(\n        e: ap.MouseEvent[ap.Sprite], options: dict) -> None:\n    """\n    The handler that the sprite calls when clicked.\n\n    Parameters\n    ----------\n    e : MouseEvent\n        Event instance.\n    options : dict\n        Optional arguments dictionary.\n    """\n    sprite: ap.Sprite = e.this\n    sprite.y += 50\n\n\nap.Stage(\n    background_color=\'#333\',\n    stage_width=250,\n    stage_height=250,\n    stage_elem_id=\'stage\')\n\nsprite: ap.Sprite = ap.Sprite()\nsprite.graphics.begin_fill(color=\'#0af\')\nsprite.graphics.draw_rect(x=50, y=50, width=50, height=50)\nsprite.graphics.draw_rect(x=150, y=50, width=50, height=50)\nsprite.click(on_sprite_click)\n\nap.save_overall_html(\n    dest_dir_path=\'sprite_move_instances_simultaneously/\')\n```':  # noqa
    '```py\n# runnable\nimport apysc as ap\n\n\ndef on_sprite_click(\n        e: ap.MouseEvent[ap.Sprite], options: dict) -> None:\n    """\n    The handler that the sprite calls when clicked.\n\n    Parameters\n    ----------\n    e : MouseEvent\n        Event instance.\n    options : dict\n        Optional arguments dictionary.\n    """\n    sprite: ap.Sprite = e.this\n    sprite.y += 50\n\n\nap.Stage(\n    background_color=\'#333\',\n    stage_width=250,\n    stage_height=250,\n    stage_elem_id=\'stage\')\n\nsprite: ap.Sprite = ap.Sprite()\nsprite.graphics.begin_fill(color=\'#0af\')\nsprite.graphics.draw_rect(x=50, y=50, width=50, height=50)\nsprite.graphics.draw_rect(x=150, y=50, width=50, height=50)\nsprite.click(on_sprite_click)\n\nap.save_overall_html(\n    dest_dir_path=\'sprite_move_instances_simultaneously/\')\n```',  # noqa

    'The subsequent pages explain the other interfaces, such as the `add_child` interface.':  # noqa
    '以降のページでは`add_child`のインターフェースなど、Spriteクラスの他のインターフェースについて説明していきます。',

    '## See also':
    '## 関連資料',

    '- [add_child and remove_child interfaces](add_child_and_remove_child.md)\n- [contains interface](contains.md)\n- [num_children interface](num_children.md)\n- [get_child_at interface](get_child_at.md)':  # noqa
    '- [add_child と remove_child インターフェイス](jp_add_child_and_remove_child.md)\n\n- [contains インターフェイス](jp_contains.md)\n\n- [num_children インターフェイス](jp_num_children.md)\n\n- [get_child_at インターフェイス](jp_get_child_at.md)',  # noqa

    '## Sprite class constructor API':
    '## SpriteクラスのコンストラクタAPI',

    '<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>':  # noqa
    '<span class="inconspicuous-txt">特記事項: このAPIドキュメントはドキュメントビルド用のスクリプトによって自動で生成・同期されています。そのためもしかしたらこの節の内容は前節までの内容と重複している場合があります。</span>',  # noqa

    '**[Interface summary]** Create a basic display object that can be a parent.<hr>':  # noqa
    '**[インターフェイス概要]** 子を持つことのできる基本的な表示要素用のオブジェクトを生成します。',

    '**[Parameters]**':
    '**[引数]**',

    '- `variable_name`: str or None, default None\n  - Variable name of this instance. A js expression uses this setting. It is unnecessary to specify any string except when instantiating the `Sprite` subclass.':  # noqa
    '- `variable_name`: str or None, default None\n  - このインスタンスのJavaScriptで使用するための変数名です。Spriteクラスのサブクラスを使う場合を除いてこの引数の指定は不要です。',  # noqa

    '**[Examples]**':
    '**[コードサンプル]**',

    '```py\n>>> import apysc as ap\n>>> stage: ap.Stage = ap.Stage()\n>>> sprite_1: ap.Sprite = ap.Sprite()\n>>> # Create the sprite child rectangle\n>>> sprite_1.graphics.begin_fill(color=\'#0af\')\n>>> rect: ap.Rectangle = sprite_1.graphics.draw_rect(\n...     x=50, y=50, width=50, height=50)\n>>> sprite_1.graphics.contains(rect)\nBoolean(True)\n\n>>> # Move the created rectangle to the other sprite\n>>> sprite_2: ap.Sprite = ap.Sprite()\n>>> sprite_2.add_child(rect)\n>>> sprite_1.graphics.contains(rect)\nBoolean(False)\n\n>>> sprite_2.contains(rect)\nBoolean(True)\n\n>>> # Move the sprite container\n>>> sprite_2.x = ap.Int(50)\n>>> sprite_2.x\nInt(50)\n```':  # noqa
    '```py\n>>> import apysc as ap\n>>> stage: ap.Stage = ap.Stage()\n>>> sprite_1: ap.Sprite = ap.Sprite()\n>>> # Create the sprite child rectangle\n>>> sprite_1.graphics.begin_fill(color=\'#0af\')\n>>> rect: ap.Rectangle = sprite_1.graphics.draw_rect(\n...     x=50, y=50, width=50, height=50)\n>>> sprite_1.graphics.contains(rect)\nBoolean(True)\n\n>>> # Move the created rectangle to the other sprite\n>>> sprite_2: ap.Sprite = ap.Sprite()\n>>> sprite_2.add_child(rect)\n>>> sprite_1.graphics.contains(rect)\nBoolean(False)\n\n>>> sprite_2.contains(rect)\nBoolean(True)\n\n>>> # Move the sprite container\n>>> sprite_2.x = ap.Int(50)\n>>> sprite_2.x\nInt(50)\n```',  # noqa

}
