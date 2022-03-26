"""This module is for the translation mapping data of the
following document:

Document file: mousedown_and_mouseup.md
Language: jp
"""

from typing import Dict

MAPPING: Dict[str, str] = {

    '# Mousedown and mouseup interfaces':
    '',

    'This page explains the `mousedown` and `mouseup` interfaces.':
    '',

    '## What interfaces are these?':
    '## 各インターフェイスの概要',

    'The `mousedown` interface binds the event handler that the interface calls when a user mouse downed on a `DisplayObject` instance. Conversely, the `mouseup` interface binds the event handler that the interface calls when a user mouse upped on a `DisplayObject` one.':  # noqa
    '',

    '## See also':
    '## 関連資料',

    'The following page describes the basic mouse event interfaces:':
    '',

    '- [Basic mouse event interfaces](mouse_event_basic.md)':
    '- [基本的なマウスイベントの各インターフェイス](jp_mouse_event_basic.md)',

    '## Basic usage of the mousedown and mouseup interfaces':
    '',

    'Each `DisplayObject` instance has the `mousedown` and `mouseup` method interfaces, and you can bind handlers by these.':  # noqa
    '',

    'The following example binds the mouse down handler and mouse upped one to the rectangle. The handler changes the rectangle color when the mouse downs and reverts to the original one when the mouse upped.':  # noqa
    '',

    '```py\n# runnable\nimport apysc as ap\n\n\ndef on_mousedown(\n        e: ap.MouseEvent[ap.Rectangle], options: dict) -> None:\n    """\n    The handler that the rectangle calls when mousedown.\n\n    Parameters\n    ----------\n    e : MouseEvent\n        Event instance.\n    options : dict\n        Optional arguments dictionary.\n    """\n    rectangle: ap.Rectangle = e.this\n    rectangle.fill_color = ap.String(\'#f0a\')\n\n\ndef on_mouseup(\n        e: ap.MouseEvent[ap.Rectangle], options: dict) -> None:\n    """\n    The handler that the rectangle calls when mouseup.\n\n    Parameters\n    ----------\n    e : MouseEvent\n        Event instance.\n    options : dict\n        Optional arguments dictionary.\n    """\n    rectangle: ap.Rectangle = e.this\n    rectangle.fill_color = ap.String(\'#0af\')\n\n\nap.Stage(\n    background_color=\'#333\',\n    stage_width=150,\n    stage_height=150,\n    stage_elem_id=\'stage\')\n\nsprite: ap.Sprite = ap.Sprite()\nsprite.graphics.begin_fill(color=\'#0af\')\nrectangle: ap.Rectangle = sprite.graphics.draw_rect(\n    x=50, y=50, width=50, height=50)\n\n# Bind each handler to the rectangle.\nrectangle.mousedown(on_mousedown)\nrectangle.mouseup(on_mouseup)\n\nap.save_overall_html(\n    dest_dir_path=\'mousedown_and_mouseup_basic_usage/\')\n```':  # noqa
    '```py\n# runnable\nimport apysc as ap\n\n\ndef on_mousedown(\n        e: ap.MouseEvent[ap.Rectangle], options: dict) -> None:\n    """\n    The handler that the rectangle calls when mousedown.\n\n    Parameters\n    ----------\n    e : MouseEvent\n        Event instance.\n    options : dict\n        Optional arguments dictionary.\n    """\n    rectangle: ap.Rectangle = e.this\n    rectangle.fill_color = ap.String(\'#f0a\')\n\n\ndef on_mouseup(\n        e: ap.MouseEvent[ap.Rectangle], options: dict) -> None:\n    """\n    The handler that the rectangle calls when mouseup.\n\n    Parameters\n    ----------\n    e : MouseEvent\n        Event instance.\n    options : dict\n        Optional arguments dictionary.\n    """\n    rectangle: ap.Rectangle = e.this\n    rectangle.fill_color = ap.String(\'#0af\')\n\n\nap.Stage(\n    background_color=\'#333\',\n    stage_width=150,\n    stage_height=150,\n    stage_elem_id=\'stage\')\n\nsprite: ap.Sprite = ap.Sprite()\nsprite.graphics.begin_fill(color=\'#0af\')\nrectangle: ap.Rectangle = sprite.graphics.draw_rect(\n    x=50, y=50, width=50, height=50)\n\n# Bind each handler to the rectangle.\nrectangle.mousedown(on_mousedown)\nrectangle.mouseup(on_mouseup)\n\nap.save_overall_html(\n    dest_dir_path=\'mousedown_and_mouseup_basic_usage/\')\n```',  # noqa

    '## Unbind interfaces':
    '',

    'The `unbind_mousedown` and `unbind_mouseup` interfaces unbind each registered handler from the `DisplayObject`\\.':  # noqa
    '',

    'The following example unbinds handlers in the `on_mousedown` and `on_mouseup` functions so that the rectangle calls these handlers only once.':  # noqa
    '',

    '```py\n# runnable\nimport apysc as ap\n\n\ndef on_mousedown(\n        e: ap.MouseEvent[ap.Rectangle], options: dict) -> None:\n    """\n    The handler that the rectangle calls when mousedown.\n\n    Parameters\n    ----------\n    e : MouseEvent\n        Event instance.\n    options : dict\n        Optional arguments dictionary.\n    """\n    rectangle: ap.Rectangle = e.this\n    rectangle.unbind_mousedown(handler=on_mousedown)\n    rectangle.fill_color = ap.String(\'#f0a\')\n\n\ndef on_mouseup(\n        e: ap.MouseEvent[ap.Rectangle], options: dict) -> None:\n    """\n    The handler that the rectangle calls when mouseup.\n\n    Parameters\n    ----------\n    e : MouseEvent\n        Event instance.\n    options : dict\n        Optional arguments dictionary.\n    """\n    rectangle: ap.Rectangle = e.this\n    rectangle.unbind_mouseup(handler=on_mouseup)\n    rectangle.fill_color = ap.String(\'#0af\')\n\n\nap.Stage(\n    background_color=\'#333\',\n    stage_width=150,\n    stage_height=150,\n    stage_elem_id=\'stage\')\n\nsprite: ap.Sprite = ap.Sprite()\nsprite.graphics.begin_fill(color=\'#0af\')\nrectangle: ap.Rectangle = sprite.graphics.draw_rect(\n    x=50, y=50, width=50, height=50)\n\nrectangle.mousedown(on_mousedown)\nrectangle.mouseup(on_mouseup)\n\nap.save_overall_html(\n    dest_dir_path=\'mousedown_and_mouseup_unbind_interfaces/\')\n```':  # noqa
    '```py\n# runnable\nimport apysc as ap\n\n\ndef on_mousedown(\n        e: ap.MouseEvent[ap.Rectangle], options: dict) -> None:\n    """\n    The handler that the rectangle calls when mousedown.\n\n    Parameters\n    ----------\n    e : MouseEvent\n        Event instance.\n    options : dict\n        Optional arguments dictionary.\n    """\n    rectangle: ap.Rectangle = e.this\n    rectangle.unbind_mousedown(handler=on_mousedown)\n    rectangle.fill_color = ap.String(\'#f0a\')\n\n\ndef on_mouseup(\n        e: ap.MouseEvent[ap.Rectangle], options: dict) -> None:\n    """\n    The handler that the rectangle calls when mouseup.\n\n    Parameters\n    ----------\n    e : MouseEvent\n        Event instance.\n    options : dict\n        Optional arguments dictionary.\n    """\n    rectangle: ap.Rectangle = e.this\n    rectangle.unbind_mouseup(handler=on_mouseup)\n    rectangle.fill_color = ap.String(\'#0af\')\n\n\nap.Stage(\n    background_color=\'#333\',\n    stage_width=150,\n    stage_height=150,\n    stage_elem_id=\'stage\')\n\nsprite: ap.Sprite = ap.Sprite()\nsprite.graphics.begin_fill(color=\'#0af\')\nrectangle: ap.Rectangle = sprite.graphics.draw_rect(\n    x=50, y=50, width=50, height=50)\n\nrectangle.mousedown(on_mousedown)\nrectangle.mouseup(on_mouseup)\n\nap.save_overall_html(\n    dest_dir_path=\'mousedown_and_mouseup_unbind_interfaces/\')\n```',  # noqa

    'There are also existing the `unbind_mousedown_all` and `unbind_mouseup_all` interfaces. These interfaces unbind all the handlers from the target `DisplayObject` instance.':  # noqa
    '',

    '## mousedown API':
    '',

    '<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>':  # noqa
    '<span class="inconspicuous-txt">特記事項: このAPIドキュメントはドキュメントビルド用のスクリプトによって自動で生成・同期されています。そのためもしかしたらこの節の内容は前節までの内容と重複している場合があります。</span>',  # noqa

    '**[Interface summary]** Add mouse down event listener setting.<hr>':
    '',

    '**[Parameters]**':
    '**[引数]**',

    '- `handler`: _Handler':
    '- `handler`: _Handler',

    '  - Callable that would be called when mouse down on this instance.':
    '',

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

    '```py\n>>> import apysc as ap\n>>> def on_mousedown(\n...         e: ap.MouseEvent[ap.Rectangle], options: dict) -> None:\n...     rectangle: ap.Rectangle = e.this\n...     rectangle.fill_color = ap.String(\'#f0a\')\n>>> stage: ap.Stage = ap.Stage()\n>>> sprite: ap.Sprite = ap.Sprite()\n>>> sprite.graphics.begin_fill(color=\'#0af\')\n>>> rectangle: ap.Rectangle = sprite.graphics.draw_rect(\n...     x=50, y=50, width=50, height=50)\n>>> _ = rectangle.mousedown(on_mousedown)\n```':  # noqa
    '```py\n>>> import apysc as ap\n>>> def on_mousedown(\n...         e: ap.MouseEvent[ap.Rectangle], options: dict) -> None:\n...     rectangle: ap.Rectangle = e.this\n...     rectangle.fill_color = ap.String(\'#f0a\')\n>>> stage: ap.Stage = ap.Stage()\n>>> sprite: ap.Sprite = ap.Sprite()\n>>> sprite.graphics.begin_fill(color=\'#0af\')\n>>> rectangle: ap.Rectangle = sprite.graphics.draw_rect(\n...     x=50, y=50, width=50, height=50)\n>>> _ = rectangle.mousedown(on_mousedown)\n```',  # noqa

    '<hr>':
    '<hr>',

    '**[References]**':
    '**[関連資料]**',

    '- [About the handler options\' type document](https://simon-ritchie.github.io/apysc/about_handler_options_type.html)':  # noqa
    '- [ハンドラのoptions引数の型について](https://simon-ritchie.github.io/apysc/jp_about_handler_options_type.html)',  # noqa

    '## unbind_mousedown API':
    '',

    '<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>':  # noqa
    '<span class="inconspicuous-txt">特記事項: このAPIドキュメントはドキュメントビルド用のスクリプトによって自動で生成・同期されています。そのためもしかしたらこの節の内容は前節までの内容と重複している場合があります。</span>',  # noqa

    '**[Interface summary]** Unbind a specified handler\'s mouse down event.<hr>':  # noqa
    '',

    '**[Parameters]**':
    '**[引数]**',

    '- `handler`: _Handler':
    '- `handler`: _Handler',

    '  - Unbinding target Callable.':
    '  - 指定された関数やメソッドのハンドラの設定を解除します。',

    '<hr>':
    '<hr>',

    '**[Examples]**':
    '**[コードサンプル]**',

    '```py\n>>> import apysc as ap\n>>> def on_mousedown(\n...         e: ap.MouseEvent[ap.Rectangle], options: dict) -> None:\n...     rectangle: ap.Rectangle = e.this\n...     rectangle.fill_color = ap.String(\'#f0a\')\n...     rectangle.unbind_mousedown(on_mousedown)\n>>> stage: ap.Stage = ap.Stage()\n>>> sprite: ap.Sprite = ap.Sprite()\n>>> sprite.graphics.begin_fill(color=\'#0af\')\n>>> rectangle: ap.Rectangle = sprite.graphics.draw_rect(\n...     x=50, y=50, width=50, height=50)\n>>> _ = rectangle.mousedown(on_mousedown)\n```':  # noqa
    '```py\n>>> import apysc as ap\n>>> def on_mousedown(\n...         e: ap.MouseEvent[ap.Rectangle], options: dict) -> None:\n...     rectangle: ap.Rectangle = e.this\n...     rectangle.fill_color = ap.String(\'#f0a\')\n...     rectangle.unbind_mousedown(on_mousedown)\n>>> stage: ap.Stage = ap.Stage()\n>>> sprite: ap.Sprite = ap.Sprite()\n>>> sprite.graphics.begin_fill(color=\'#0af\')\n>>> rectangle: ap.Rectangle = sprite.graphics.draw_rect(\n...     x=50, y=50, width=50, height=50)\n>>> _ = rectangle.mousedown(on_mousedown)\n```',  # noqa

    '## unbind_mousedown_all API':
    '',

    '<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>':  # noqa
    '<span class="inconspicuous-txt">特記事項: このAPIドキュメントはドキュメントビルド用のスクリプトによって自動で生成・同期されています。そのためもしかしたらこの節の内容は前節までの内容と重複している場合があります。</span>',  # noqa

    '**[Interface summary]** Unbind all mouse down events.<hr>':
    '',

    '**[Examples]**':
    '**[コードサンプル]**',

    '```py\n>>> import apysc as ap\n>>> def on_mousedown(\n...         e: ap.MouseEvent[ap.Rectangle], options: dict) -> None:\n...     rectangle: ap.Rectangle = e.this\n...     rectangle.fill_color = ap.String(\'#f0a\')\n...     rectangle.unbind_mousedown_all()\n>>> stage: ap.Stage = ap.Stage()\n>>> sprite: ap.Sprite = ap.Sprite()\n>>> sprite.graphics.begin_fill(color=\'#0af\')\n>>> rectangle: ap.Rectangle = sprite.graphics.draw_rect(\n...     x=50, y=50, width=50, height=50)\n>>> _ = rectangle.mousedown(on_mousedown)\n```':  # noqa
    '```py\n>>> import apysc as ap\n>>> def on_mousedown(\n...         e: ap.MouseEvent[ap.Rectangle], options: dict) -> None:\n...     rectangle: ap.Rectangle = e.this\n...     rectangle.fill_color = ap.String(\'#f0a\')\n...     rectangle.unbind_mousedown_all()\n>>> stage: ap.Stage = ap.Stage()\n>>> sprite: ap.Sprite = ap.Sprite()\n>>> sprite.graphics.begin_fill(color=\'#0af\')\n>>> rectangle: ap.Rectangle = sprite.graphics.draw_rect(\n...     x=50, y=50, width=50, height=50)\n>>> _ = rectangle.mousedown(on_mousedown)\n```',  # noqa

    '## mouseup API':
    '',

    '<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>':  # noqa
    '<span class="inconspicuous-txt">特記事項: このAPIドキュメントはドキュメントビルド用のスクリプトによって自動で生成・同期されています。そのためもしかしたらこの節の内容は前節までの内容と重複している場合があります。</span>',  # noqa

    '**[Interface summary]** Add mouse up event listener setting.<hr>':
    '',

    '**[Parameters]**':
    '**[引数]**',

    '- `handler`: _Handler':
    '- `handler`: _Handler',

    '  - Callable that would be called when mouse-up on this instance.':
    '',

    '- `options`: dict or None, default None':
    '- `options`: dict or None, default None',

    '  - Optional arguments dictionary to be passed to a handler':
    '',

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

    '```py\n>>> import apysc as ap\n>>> def on_mouseup(\n...         e: ap.MouseEvent[ap.Rectangle], options: dict) -> None:\n...     rectangle: ap.Rectangle = e.this\n...     rectangle.fill_color = ap.String(\'#f0a\')\n>>> stage: ap.Stage = ap.Stage()\n>>> sprite: ap.Sprite = ap.Sprite()\n>>> sprite.graphics.begin_fill(color=\'#0af\')\n>>> rectangle: ap.Rectangle = sprite.graphics.draw_rect(\n...     x=50, y=50, width=50, height=50)\n>>> _ = rectangle.mouseup(on_mouseup)\n```':  # noqa
    '```py\n>>> import apysc as ap\n>>> def on_mouseup(\n...         e: ap.MouseEvent[ap.Rectangle], options: dict) -> None:\n...     rectangle: ap.Rectangle = e.this\n...     rectangle.fill_color = ap.String(\'#f0a\')\n>>> stage: ap.Stage = ap.Stage()\n>>> sprite: ap.Sprite = ap.Sprite()\n>>> sprite.graphics.begin_fill(color=\'#0af\')\n>>> rectangle: ap.Rectangle = sprite.graphics.draw_rect(\n...     x=50, y=50, width=50, height=50)\n>>> _ = rectangle.mouseup(on_mouseup)\n```',  # noqa

    '<hr>':
    '<hr>',

    '**[References]**':
    '**[関連資料]**',

    '- [About the handler options\' type document](https://simon-ritchie.github.io/apysc/about_handler_options_type.html)':  # noqa
    '- [ハンドラのoptions引数の型について](https://simon-ritchie.github.io/apysc/jp_about_handler_options_type.html)',  # noqa

    '## unbind_mouseup API':
    '',

    '<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>':  # noqa
    '<span class="inconspicuous-txt">特記事項: このAPIドキュメントはドキュメントビルド用のスクリプトによって自動で生成・同期されています。そのためもしかしたらこの節の内容は前節までの内容と重複している場合があります。</span>',  # noqa

    '**[Interface summary]** Unbind a specified handler\'s mouse-up event.<hr>':  # noqa
    '',

    '**[Parameters]**':
    '**[引数]**',

    '- `handler`: _Handler':
    '- `handler`: _Handler',

    '  - Unbinding target Callable.':
    '  - 指定された関数やメソッドのハンドラの設定を解除します。',

    '<hr>':
    '<hr>',

    '**[Examples]**':
    '**[コードサンプル]**',

    '```py\n>>> import apysc as ap\n>>> def on_mouseup(\n...         e: ap.MouseEvent[ap.Rectangle], options: dict) -> None:\n...     rectangle: ap.Rectangle = e.this\n...     rectangle.fill_color = ap.String(\'#f0a\')\n...     rectangle.unbind_mouseup(on_mouseup)\n>>> stage: ap.Stage = ap.Stage()\n>>> sprite: ap.Sprite = ap.Sprite()\n>>> sprite.graphics.begin_fill(color=\'#0af\')\n>>> rectangle: ap.Rectangle = sprite.graphics.draw_rect(\n...     x=50, y=50, width=50, height=50)\n>>> _ = rectangle.mouseup(on_mouseup)\n```':  # noqa
    '```py\n>>> import apysc as ap\n>>> def on_mouseup(\n...         e: ap.MouseEvent[ap.Rectangle], options: dict) -> None:\n...     rectangle: ap.Rectangle = e.this\n...     rectangle.fill_color = ap.String(\'#f0a\')\n...     rectangle.unbind_mouseup(on_mouseup)\n>>> stage: ap.Stage = ap.Stage()\n>>> sprite: ap.Sprite = ap.Sprite()\n>>> sprite.graphics.begin_fill(color=\'#0af\')\n>>> rectangle: ap.Rectangle = sprite.graphics.draw_rect(\n...     x=50, y=50, width=50, height=50)\n>>> _ = rectangle.mouseup(on_mouseup)\n```',  # noqa

    '## unbind_mouseup_all API':
    '',

    '<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>':  # noqa
    '<span class="inconspicuous-txt">特記事項: このAPIドキュメントはドキュメントビルド用のスクリプトによって自動で生成・同期されています。そのためもしかしたらこの節の内容は前節までの内容と重複している場合があります。</span>',  # noqa

    '**[Interface summary]** Unbind all mouse up events.<hr>':
    '',

    '**[Examples]**':
    '**[コードサンプル]**',

    '```py\n>>> import apysc as ap\n>>> def on_mouseup(\n...         e: ap.MouseEvent[ap.Rectangle], options: dict) -> None:\n...     rectangle: ap.Rectangle = e.this\n...     rectangle.fill_color = ap.String(\'#f0a\')\n...     rectangle.unbind_mouseup_all()\n>>> stage: ap.Stage = ap.Stage()\n>>> sprite: ap.Sprite = ap.Sprite()\n>>> sprite.graphics.begin_fill(color=\'#0af\')\n>>> rectangle: ap.Rectangle = sprite.graphics.draw_rect(\n...     x=50, y=50, width=50, height=50)\n>>> _ = rectangle.mouseup(on_mouseup)\n```':  # noqa
    '```py\n>>> import apysc as ap\n>>> def on_mouseup(\n...         e: ap.MouseEvent[ap.Rectangle], options: dict) -> None:\n...     rectangle: ap.Rectangle = e.this\n...     rectangle.fill_color = ap.String(\'#f0a\')\n...     rectangle.unbind_mouseup_all()\n>>> stage: ap.Stage = ap.Stage()\n>>> sprite: ap.Sprite = ap.Sprite()\n>>> sprite.graphics.begin_fill(color=\'#0af\')\n>>> rectangle: ap.Rectangle = sprite.graphics.draw_rect(\n...     x=50, y=50, width=50, height=50)\n>>> _ = rectangle.mouseup(on_mouseup)\n```',  # noqa

}
