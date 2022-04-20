"""This module is for the translation mapping data of the
following document:

Document file: mousemove.md
Language: jp
"""

from typing import Dict

MAPPING: Dict[str, str] = {

    '# mousemove interface':
    '# mousemove インターフェイス',

    'This page explains the `mousemove` interface.':
    'このページでは`mousemove`のインターフェイスについて説明します。',

    '## What interface is this?':
    '## インターフェイス概要',

    'The `mousemove` interface binds the mouse moving event handler to any `DisplayObject` instance. If you move the mouse cursor on that instance, the interface calls the registered handler.':  # noqa
    '`mousemove`のインターフェイスは任意の`DisplayObject`のインスタンスへとマウスを動かした時のイベントハンドラの設定を追加します。対象のインスタンス上でマウスカーソルを動かす度に設定されたハンドラが呼ばれます。',  # noqa

    '## See also':
    '## 関連資料',

    'The following page describes the basic mouse event interfaces.':
    '以下のページでは基本的なマウスイベントの各インターフェイスについて説明しています。',

    '- [Basic mouse event interfaces](mouse_event_basic.md)':
    '- [基本的なマウスイベントの各インターフェイス](jp_mouse_event_basic.md)',

    '## Basic usage':
    '## 基本的な使い方',

    'Each `DisplayObject` instance has the `mousemove` method, and you can bind handlers by that.':  # noqa
    '`DisplayObject`の各インスタンスは`mousemove`メソッドを持っており、そのインターフェイスを使ってハンドラを設定することができます。',  # noqa

    'The following example binds the mouse move event handler to the circle. So if you move a mouse cursor on that, the circle follows the cursor position.':  # noqa
    '以下のコード例では円に対してマウスを動かしたときのハンドラを設定しています。対象の円の上でマウスカーソルを動かすと、円の位置はカーソルの位置に更新されます。',  # noqa

    '```py\n# runnable\nimport apysc as ap\n\n\ndef on_mousemove(\n        e: ap.MouseEvent[ap.Circle], options: dict) -> None:\n    """\n    The handler that the circle calls when mousemove.\n\n    Parameters\n    ----------\n    e : MouseEvent\n        Event instance.\n    options : dict\n        Optional arguments dictionary.\n    """\n    circle: ap.Circle = e.this\n    circle.x = e.stage_x\n    circle.y = e.stage_y\n\n\nap.Stage(\n    background_color=\'#333\',\n    stage_width=200,\n    stage_height=200,\n    stage_elem_id=\'stage\')\n\nsprite: ap.Sprite = ap.Sprite()\nsprite.graphics.begin_fill(color=\'#0af\')\ncircle: ap.Circle = sprite.graphics.draw_circle(x=100, y=100, radius=100)\ncircle.mousemove(on_mousemove)\n\nap.save_overall_html(\n    dest_dir_path=\'mousemove_basic_usage/\')\n```':  # noqa
    '```py\n# runnable\nimport apysc as ap\n\n\ndef on_mousemove(\n        e: ap.MouseEvent[ap.Circle], options: dict) -> None:\n    """\n    The handler that the circle calls when mousemove.\n\n    Parameters\n    ----------\n    e : MouseEvent\n        Event instance.\n    options : dict\n        Optional arguments dictionary.\n    """\n    circle: ap.Circle = e.this\n    circle.x = e.stage_x\n    circle.y = e.stage_y\n\n\nap.Stage(\n    background_color=\'#333\',\n    stage_width=200,\n    stage_height=200,\n    stage_elem_id=\'stage\')\n\nsprite: ap.Sprite = ap.Sprite()\nsprite.graphics.begin_fill(color=\'#0af\')\ncircle: ap.Circle = sprite.graphics.draw_circle(x=100, y=100, radius=100)\ncircle.mousemove(on_mousemove)\n\nap.save_overall_html(\n    dest_dir_path=\'mousemove_basic_usage/\')\n```',  # noqa

    '## Unbind interfaces':
    '## 解除用のインターフェイス',

    '`unbind_mousemove` interface can remove the binding of the mouse move event from the `DisplayObject`\\.':  # noqa
    '`unbind_mousemove`インターフェイスでは`DisplayObject`のインスタンスのマウスを動かした時のイベントのハンドラ設定を解除することができます。',  # noqa

    'In the following example, the interface removes the mouse move event handler if you click the circle.':  # noqa
    '以下のコード例では円をクリックした際にマウスを動かしたときのイベントハンドラの設定を解除するようにしています。',

    '```py\n# runnable\nimport apysc as ap\n\n\ndef on_mousemove(\n        e: ap.MouseEvent[ap.Circle], options: dict) -> None:\n    """\n    The handler that the circle calls when mousemove.\n\n    Parameters\n    ----------\n    e : MouseEvent\n        Event instance.\n    options : dict\n        Optional arguments dictionary.\n    """\n    circle: ap.Circle = e.this\n    circle.x = e.stage_x\n    circle.y = e.stage_y\n\n\ndef on_click(e: ap.MouseEvent[ap.Circle], options: dict) -> None:\n    """\n    The handler that the circle calls when clicked.\n\n    Parameters\n    ----------\n    e : MouseEvent\n        Event instance.\n    options : dict\n        Optional arguments dictionary.\n    """\n    circle: ap.Circle = e.this\n    circle.unbind_mousemove(handler=on_mousemove)\n\n\nap.Stage(\n    background_color=\'#333\',\n    stage_width=200,\n    stage_height=200,\n    stage_elem_id=\'stage\')\n\nsprite: ap.Sprite = ap.Sprite()\nsprite.graphics.begin_fill(color=\'#0af\')\ncircle: ap.Circle = sprite.graphics.draw_circle(x=100, y=100, radius=100)\ncircle.mousemove(on_mousemove)\ncircle.click(on_click)\n\nap.save_overall_html(\n    dest_dir_path=\'mousemove_unbind_interface/\')\n```':  # noqa
    '```py\n# runnable\nimport apysc as ap\n\n\ndef on_mousemove(\n        e: ap.MouseEvent[ap.Circle], options: dict) -> None:\n    """\n    The handler that the circle calls when mousemove.\n\n    Parameters\n    ----------\n    e : MouseEvent\n        Event instance.\n    options : dict\n        Optional arguments dictionary.\n    """\n    circle: ap.Circle = e.this\n    circle.x = e.stage_x\n    circle.y = e.stage_y\n\n\ndef on_click(e: ap.MouseEvent[ap.Circle], options: dict) -> None:\n    """\n    The handler that the circle calls when clicked.\n\n    Parameters\n    ----------\n    e : MouseEvent\n        Event instance.\n    options : dict\n        Optional arguments dictionary.\n    """\n    circle: ap.Circle = e.this\n    circle.unbind_mousemove(handler=on_mousemove)\n\n\nap.Stage(\n    background_color=\'#333\',\n    stage_width=200,\n    stage_height=200,\n    stage_elem_id=\'stage\')\n\nsprite: ap.Sprite = ap.Sprite()\nsprite.graphics.begin_fill(color=\'#0af\')\ncircle: ap.Circle = sprite.graphics.draw_circle(x=100, y=100, radius=100)\ncircle.mousemove(on_mousemove)\ncircle.click(on_click)\n\nap.save_overall_html(\n    dest_dir_path=\'mousemove_unbind_interface/\')\n```',  # noqa

    'There are also existing the `unbind_mousemove_all` interface. This interface unbinds all the handlers from the target `DisplayObject` instance.':  # noqa
    'また、`unbind_mousemove_all`のインターフェイスも存在し、このインターフェイスは`DisplayObject`のインスタンスからマウスを動かしたときのイベントのハンドラ設定を全て解除します。',  # noqa

    '## mousemove API':
    '## mousemove API',

    '<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>':  # noqa
    '<span class="inconspicuous-txt">特記事項: このAPIドキュメントはドキュメントビルド用のスクリプトによって自動で生成・同期されています。そのためもしかしたらこの節の内容は前節までの内容と重複している場合があります。</span>',  # noqa

    '**[Interface summary]** Add mouse move event listener setting.<hr>':
    '**[インターフェイス概要]** マウスを動かした時のイベント設定を追加します。<hr>',

    '**[Parameters]**':
    '**[引数]**',

    '- `handler`: _Handler':
    '- `handler`: _Handler',

    '  - Callable that would be called when mousemove on this instance.':
    '  - インスタンス上でマウスを動かした際に呼ばれる関数もしくはメソッド。',

    '- `options`: dict or None, default None':
    '- `options`: dict or None, default None',

    '  - Optional arguments dictionary to be passed to a handler.':
    '  - ハンドラに渡される省略が可能な追加のパラメーターとしての辞書。',

    '<hr>':
    '<hr>',

    '**[Returns]**':
    '**[返却値]**',

    '- `name`: str':
    '- `name`: str',

    '  - Handler\'s name.':
    '  - ハンドラ名。',

    '<hr>':
    '<hr>',

    '**[Examples]**':
    '**[コードサンプル]**',

    '```py\n>>> import apysc as ap\n>>> def on_mousemove(\n...         e: ap.MouseEvent[ap.Rectangle], options: dict) -> None:\n...     stage_x: ap.Int = e.stage_x\n...     ap.trace(\'stage_x:\', stage_x)\n>>> stage: ap.Stage = ap.Stage()\n>>> sprite: ap.Sprite = ap.Sprite()\n>>> sprite.graphics.begin_fill(color=\'#0af\')\n>>> rectangle: ap.Rectangle = sprite.graphics.draw_rect(\n...     x=50, y=50, width=50, height=50)\n>>> _ = rectangle.mousemove(on_mousemove)\n```':  # noqa
    '```py\n>>> import apysc as ap\n>>> def on_mousemove(\n...         e: ap.MouseEvent[ap.Rectangle], options: dict) -> None:\n...     stage_x: ap.Int = e.stage_x\n...     ap.trace(\'stage_x:\', stage_x)\n>>> stage: ap.Stage = ap.Stage()\n>>> sprite: ap.Sprite = ap.Sprite()\n>>> sprite.graphics.begin_fill(color=\'#0af\')\n>>> rectangle: ap.Rectangle = sprite.graphics.draw_rect(\n...     x=50, y=50, width=50, height=50)\n>>> _ = rectangle.mousemove(on_mousemove)\n```',  # noqa

    '<hr>':
    '<hr>',

    '**[References]**':
    '**[関連資料]**',

    '- [About the handler options\' type document](https://simon-ritchie.github.io/apysc/about_handler_options_type.html)':  # noqa
    '- [ハンドラのoptions引数の型について](https://simon-ritchie.github.io/apysc/jp_about_handler_options_type.html)',  # noqa

    '## unbind_mousemove API':
    '## unbind_mousemove API',

    '<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>':  # noqa
    '<span class="inconspicuous-txt">特記事項: このAPIドキュメントはドキュメントビルド用のスクリプトによって自動で生成・同期されています。そのためもしかしたらこの節の内容は前節までの内容と重複している場合があります。</span>',  # noqa

    '**[Interface summary]** Unbind a specified handler\'s mouse move event.<hr>':  # noqa
    '**[インターフェイス概要]** マウスカーソルを動かした際のイベントで指定されたハンドラの設定を解除します。<hr>',

    '**[Parameters]**':
    '**[引数]**',

    '- `handler`: _Handler':
    '- `handler`: _Handler',

    '  - Unbinding target Callable.':
    '  - イベント設定を取り除く対象の関数やメソッドなど。',

    '<hr>':
    '<hr>',

    '**[Examples]**':
    '**[コードサンプル]**',

    '```py\n>>> import apysc as ap\n>>> def on_mousemove(\n...         e: ap.MouseEvent[ap.Rectangle], options: dict) -> None:\n...     stage_x: ap.Int = e.stage_x\n...     ap.trace(\'stage_x:\', stage_x)\n>>> def on_click(\n...         e: ap.MouseEvent[ap.Rectangle], options: dict) -> None:\n...     rectangle: ap.Rectangle = e.this\n...     rectangle.unbind_mousemove(on_mousemove)\n>>> stage: ap.Stage = ap.Stage()\n>>> sprite: ap.Sprite = ap.Sprite()\n>>> sprite.graphics.begin_fill(color=\'#0af\')\n>>> rectangle: ap.Rectangle = sprite.graphics.draw_rect(\n...     x=50, y=50, width=50, height=50)\n>>> _ = rectangle.mousemove(on_mousemove)\n>>> _ = rectangle.click(on_click)\n```':  # noqa
    '```py\n>>> import apysc as ap\n>>> def on_mousemove(\n...         e: ap.MouseEvent[ap.Rectangle], options: dict) -> None:\n...     stage_x: ap.Int = e.stage_x\n...     ap.trace(\'stage_x:\', stage_x)\n>>> def on_click(\n...         e: ap.MouseEvent[ap.Rectangle], options: dict) -> None:\n...     rectangle: ap.Rectangle = e.this\n...     rectangle.unbind_mousemove(on_mousemove)\n>>> stage: ap.Stage = ap.Stage()\n>>> sprite: ap.Sprite = ap.Sprite()\n>>> sprite.graphics.begin_fill(color=\'#0af\')\n>>> rectangle: ap.Rectangle = sprite.graphics.draw_rect(\n...     x=50, y=50, width=50, height=50)\n>>> _ = rectangle.mousemove(on_mousemove)\n>>> _ = rectangle.click(on_click)\n```',  # noqa

    '## unbind_mousemove_all API':
    '## unbind_mousemove_all API',

    '<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>':  # noqa
    '<span class="inconspicuous-txt">特記事項: このAPIドキュメントはドキュメントビルド用のスクリプトによって自動で生成・同期されています。そのためもしかしたらこの節の内容は前節までの内容と重複している場合があります。</span>',  # noqa

    '**[Interface summary]** Unbind all mouse move events.<hr>':
    '**[インターフェイス概要]** マウスカーソルを動かしたときのイベントの全てのハンドラ設定を解除します。<hr>',

    '**[Examples]**':
    '**[コードサンプル]**',

    '```py\n>>> import apysc as ap\n>>> def on_mousemove(\n...         e: ap.MouseEvent[ap.Rectangle], options: dict) -> None:\n...     stage_x: ap.Int = e.stage_x\n...     ap.trace(\'stage_x:\', stage_x)\n>>> def on_click(\n...         e: ap.MouseEvent[ap.Rectangle], options: dict) -> None:\n...     rectangle: ap.Rectangle = e.this\n...     rectangle.unbind_mousemove_all()\n>>> stage: ap.Stage = ap.Stage()\n>>> sprite: ap.Sprite = ap.Sprite()\n>>> sprite.graphics.begin_fill(color=\'#0af\')\n>>> rectangle: ap.Rectangle = sprite.graphics.draw_rect(\n...     x=50, y=50, width=50, height=50)\n>>> _ = rectangle.mousemove(on_mousemove)\n>>> _ = rectangle.click(on_click)\n```':  # noqa
    '```py\n>>> import apysc as ap\n>>> def on_mousemove(\n...         e: ap.MouseEvent[ap.Rectangle], options: dict) -> None:\n...     stage_x: ap.Int = e.stage_x\n...     ap.trace(\'stage_x:\', stage_x)\n>>> def on_click(\n...         e: ap.MouseEvent[ap.Rectangle], options: dict) -> None:\n...     rectangle: ap.Rectangle = e.this\n...     rectangle.unbind_mousemove_all()\n>>> stage: ap.Stage = ap.Stage()\n>>> sprite: ap.Sprite = ap.Sprite()\n>>> sprite.graphics.begin_fill(color=\'#0af\')\n>>> rectangle: ap.Rectangle = sprite.graphics.draw_rect(\n...     x=50, y=50, width=50, height=50)\n>>> _ = rectangle.mousemove(on_mousemove)\n>>> _ = rectangle.click(on_click)\n```',  # noqa

}
