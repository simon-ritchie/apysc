"""This module is for the translation mapping data of the
following document:

Document file: click.md
Language: jp
"""

from typing import Dict

MAPPING: Dict[str, str] = {

    '# click interface':
    '# click インターフェイス',

    'This page explains the `click` interface.':
    'このページでは`click`インターフェイスについて説明します。',

    '## What interface is this?':
    '## インターフェイス概要',

    'The `click` interface binds the click event to any `DisplayObject` instance (e.g., `Sprite`\\, `Rectangle`\\, and so on). These interfaces call the registered handler function if you mouse down on that instance and mouse up.':  # noqa
    '`click`インターフェイスは`Sprite`や`Rectangle`クラスなどの任意の`DisplayObject`のサブクラスのインスタンスにクリックイベントを設定します。これらのインターフェイスで登録されたハンドラは対象のインスタンスをクリックした際に呼ばれます。',  # noqa

    'Conversely, the `unbind_click` interface unbinds the click event from the `DisplayObject` instance.':  # noqa
    '逆に`unbind_click`インターフェイスは対象の`DisplayObject`のインスタンスからクリックイベントの登録を解除します。',  # noqa

    '## See also':
    '## 関連資料',

    'The following page describes basic mouse event interfaces.':
    '以下のページでは基本的なマウスイベントのインターフェイスについて説明しています。',

    '- [Basic mouse event interfaces](mouse_event_basic.md)':
    '- [基本的なマウスイベントの各インターフェイス](jp_mouse_event_basic.md)',

    '## Basic usage of the click interface':
    '## click インターフェイスの基本的な使い方',

    'Each `DisplayObject` instance has the `click` method, and you can bind handlers by that.':  # noqa
    '`DisplayObject`のサブクラスの各インスタンスは`click`メソッドを持っており、そのインターフェイスを使ってイベントのハンドラを登録することができます。',  # noqa

    'The following example binds the click event handler to the rectangle.':
    '以下のコード例では四角に対してクリックのイベントハンドラを設定しています。',

    '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    background_color=\'#333\',\n    stage_width=150,\n    stage_height=150,\n    stage_elem_id=\'stage\')\n\nsprite: ap.Sprite = ap.Sprite()\nsprite.graphics.begin_fill(color=\'#0af\')\n\n\ndef on_click(\n        e: ap.MouseEvent[ap.Rectangle], options: dict) -> None:\n    """\n    The handler that the rectangle calls when clicked.\n\n    Parameters\n    ----------\n    e : MouseEvent\n        Event instance.\n    options : dict\n        Optional arguments.\n    """\n    rectangle: ap.Rectangle = e.this\n    rectangle.fill_color = ap.String(\'#f0a\')\n\n\nrectangle: ap.Rectangle = sprite.graphics.draw_rect(\n    x=50, y=50, width=50, height=50)\nrectangle.click(handler=on_click)\n\nap.save_overall_html(\n    dest_dir_path=\'click_basic_usage_of_the_click_interface/\')\n```':  # noqa
    '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    background_color=\'#333\',\n    stage_width=150,\n    stage_height=150,\n    stage_elem_id=\'stage\')\n\nsprite: ap.Sprite = ap.Sprite()\nsprite.graphics.begin_fill(color=\'#0af\')\n\n\ndef on_click(\n        e: ap.MouseEvent[ap.Rectangle], options: dict) -> None:\n    """\n    The handler that the rectangle calls when clicked.\n\n    Parameters\n    ----------\n    e : MouseEvent\n        Event instance.\n    options : dict\n        Optional arguments.\n    """\n    rectangle: ap.Rectangle = e.this\n    rectangle.fill_color = ap.String(\'#f0a\')\n\n\nrectangle: ap.Rectangle = sprite.graphics.draw_rect(\n    x=50, y=50, width=50, height=50)\nrectangle.click(handler=on_click)\n\nap.save_overall_html(\n    dest_dir_path=\'click_basic_usage_of_the_click_interface/\')\n```',  # noqa

    'If you click the following rectangle, the rectangle color becomes the magenta color.':  # noqa
    'もしも以下の四角をクリックすると四角の色はマゼンタに切り替わります。',

    '## Basic usage of the unbind_click interface':
    '## unbind_click インターフェイスの基本的な使い方',

    'The `unbind_click` interface can remove the binded click event from a `DisplayObject` instance.':  # noqa
    '`unbind_click`インターフェイスは`DisplayObject`のサブクラスのインスタンスから登録済みのクリックイベントの設定を取り除きます。',  # noqa

    'The following example removes the click event by the `unbind_click` method, and nothing happens if you click the rectangle.':  # noqa
    '以下のコード例では`unbind_click`メソッドでクリックイベントを取り除いているため四角をクリックしても何も発生しません。',

    '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    background_color=\'#333\',\n    stage_width=150,\n    stage_height=150,\n    stage_elem_id=\'stage\')\n\nsprite: ap.Sprite = ap.Sprite()\nsprite.graphics.begin_fill(color=\'#0af\')\n\n\ndef on_click(\n        e: ap.MouseEvent[ap.Rectangle], options: dict) -> None:\n    """\n    The handler that the rectangle calls when clicked.\n\n    Parameters\n    ----------\n    e : MouseEvent\n        Event instance.\n    options : dict\n        Optional arguments.\n    """\n    rectangle: ap.Rectangle = e.this\n    rectangle.fill_color = ap.String(\'#f0a\')\n\n\nrectangle: ap.Rectangle = sprite.graphics.draw_rect(\n    x=50, y=50, width=50, height=50)\nrectangle.click(handler=on_click)\nrectangle.unbind_click(handler=on_click)\n\nap.save_overall_html(\n    dest_dir_path=\'click_basic_usage_of_the_unbind_click_interface/\')\n```':  # noqa
    '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    background_color=\'#333\',\n    stage_width=150,\n    stage_height=150,\n    stage_elem_id=\'stage\')\n\nsprite: ap.Sprite = ap.Sprite()\nsprite.graphics.begin_fill(color=\'#0af\')\n\n\ndef on_click(\n        e: ap.MouseEvent[ap.Rectangle], options: dict) -> None:\n    """\n    The handler that the rectangle calls when clicked.\n\n    Parameters\n    ----------\n    e : MouseEvent\n        Event instance.\n    options : dict\n        Optional arguments.\n    """\n    rectangle: ap.Rectangle = e.this\n    rectangle.fill_color = ap.String(\'#f0a\')\n\n\nrectangle: ap.Rectangle = sprite.graphics.draw_rect(\n    x=50, y=50, width=50, height=50)\nrectangle.click(handler=on_click)\nrectangle.unbind_click(handler=on_click)\n\nap.save_overall_html(\n    dest_dir_path=\'click_basic_usage_of_the_unbind_click_interface/\')\n```',  # noqa

    '## Unbind all the click event handlers':
    '## 全てのクリックのイベントハンドラを解除する',

    '`unbind_click_all` interface can unbind all the click event handlers from the `DisplayObject` instance.':  # noqa
    '`unbind_click_all`インターフェイスは`DisplayObject`のサブクラスのインスタンスから全ての登録されているクリックイベントのハンドラを解除します。',  # noqa

    'The following example removes all the click events by the `unbind_click_all` method (if you click the rectangle, nothing happens).':  # noqa
    '以下のコード例では`unbind_click_all`メソッドで全てのクリックイベントの設定を取り除いており、四角をクリックしても何も起きません。',  # noqa

    '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    background_color=\'#333\',\n    stage_width=150,\n    stage_height=150,\n    stage_elem_id=\'stage\')\n\nsprite: ap.Sprite = ap.Sprite()\nsprite.graphics.begin_fill(color=\'#0af\')\n\n\ndef on_click(\n        e: ap.MouseEvent[ap.Rectangle], options: dict) -> None:\n    """\n    The handler that the rectangle calls when clicked.\n\n    Parameters\n    ----------\n    e : MouseEvent\n        Event instance.\n    options : dict\n        Optional arguments.\n    """\n    rectangle: ap.Rectangle = e.this\n    rectangle.fill_color = ap.String(\'#f0a\')\n\n\nrectangle: ap.Rectangle = sprite.graphics.draw_rect(\n    x=50, y=50, width=50, height=50)\nrectangle.click(handler=on_click)\nrectangle.unbind_click_all()\n\nap.save_overall_html(\n    dest_dir_path=\'click_unbind_all_the_click_event_handlers/\')\n```':  # noqa
    '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    background_color=\'#333\',\n    stage_width=150,\n    stage_height=150,\n    stage_elem_id=\'stage\')\n\nsprite: ap.Sprite = ap.Sprite()\nsprite.graphics.begin_fill(color=\'#0af\')\n\n\ndef on_click(\n        e: ap.MouseEvent[ap.Rectangle], options: dict) -> None:\n    """\n    The handler that the rectangle calls when clicked.\n\n    Parameters\n    ----------\n    e : MouseEvent\n        Event instance.\n    options : dict\n        Optional arguments.\n    """\n    rectangle: ap.Rectangle = e.this\n    rectangle.fill_color = ap.String(\'#f0a\')\n\n\nrectangle: ap.Rectangle = sprite.graphics.draw_rect(\n    x=50, y=50, width=50, height=50)\nrectangle.click(handler=on_click)\nrectangle.unbind_click_all()\n\nap.save_overall_html(\n    dest_dir_path=\'click_unbind_all_the_click_event_handlers/\')\n```',  # noqa

    '## click API':
    '## click API',

    '<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>':  # noqa
    '<span class="inconspicuous-txt">特記事項: このAPIドキュメントはドキュメントビルド用のスクリプトによって自動で生成・同期されています。そのためもしかしたらこの節の内容は前節までの内容と重複している場合があります。</span>',  # noqa

    '**[Interface summary]** Add a click event listener setting.<hr>':
    '**[インターフェイス概要]** クリックイベント用の設定を追加します。<hr>',

    '**[Parameters]**':
    '**[引数]**',

    '- `handler`: _Handler':
    '- `handler`: _Handler',

    '  - A callable would be called when clicking this instance.':
    '  - このインスタンスをクリックした際に呼ばれるハンドラ。',

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

    '```py\n>>> import apysc as ap\n>>> def on_click(\n...         e: ap.MouseEvent[ap.Rectangle], options: dict) -> None:\n...     rectangle: ap.Rectangle = e.this\n...     rectangle.x += 10\n>>> stage: ap.Stage = ap.Stage()\n>>> sprite: ap.Sprite = ap.Sprite()\n>>> sprite.graphics.begin_fill(color=\'#0af\')\n>>> rectangle: ap.Rectangle = sprite.graphics.draw_rect(\n...     x=50, y=50, width=50, height=50)\n>>> _ = rectangle.click(on_click)\n```':  # noqa
    '```py\n>>> import apysc as ap\n>>> def on_click(\n...         e: ap.MouseEvent[ap.Rectangle], options: dict) -> None:\n...     rectangle: ap.Rectangle = e.this\n...     rectangle.x += 10\n>>> stage: ap.Stage = ap.Stage()\n>>> sprite: ap.Sprite = ap.Sprite()\n>>> sprite.graphics.begin_fill(color=\'#0af\')\n>>> rectangle: ap.Rectangle = sprite.graphics.draw_rect(\n...     x=50, y=50, width=50, height=50)\n>>> _ = rectangle.click(on_click)\n```',  # noqa

    '<hr>':
    '<hr>',

    '**[References]**':
    '**[関連資料]**',

    '- [About the handler options\' type document](https://simon-ritchie.github.io/apysc/about_handler_options_type.html)':  # noqa
    '- [ハンドラのoptions引数の型について](https://simon-ritchie.github.io/apysc/jp_about_handler_options_type.html)',  # noqa

    '## unbind_click API':
    '## unbind_click API',

    '<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>':  # noqa
    '<span class="inconspicuous-txt">特記事項: このAPIドキュメントはドキュメントビルド用のスクリプトによって自動で生成・同期されています。そのためもしかしたらこの節の内容は前節までの内容と重複している場合があります。</span>',  # noqa

    '**[Interface summary]** Unbind specified handler\'s click event.<hr>':
    '**[インターフェイス概要]** 指定されたクリックイベントのハンドラの設定を取り除きます。<hr>',

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

    '```py\n>>> import apysc as ap\n>>> def on_click(\n...         e: ap.MouseEvent[ap.Rectangle], options: dict) -> None:\n...     rectangle: ap.Rectangle = e.this\n...     rectangle.fill_color = ap.String(\'#f0a\')\n...     rectangle.unbind_click(on_click)\n>>> stage: ap.Stage = ap.Stage()\n>>> sprite: ap.Sprite = ap.Sprite()\n>>> sprite.graphics.begin_fill(color=\'#0af\')\n>>> rectangle: ap.Rectangle = sprite.graphics.draw_rect(\n...     x=50, y=50, width=50, height=50)\n>>> _ = rectangle.click(on_click)\n```':  # noqa
    '```py\n>>> import apysc as ap\n>>> def on_click(\n...         e: ap.MouseEvent[ap.Rectangle], options: dict) -> None:\n...     rectangle: ap.Rectangle = e.this\n...     rectangle.fill_color = ap.String(\'#f0a\')\n...     rectangle.unbind_click(on_click)\n>>> stage: ap.Stage = ap.Stage()\n>>> sprite: ap.Sprite = ap.Sprite()\n>>> sprite.graphics.begin_fill(color=\'#0af\')\n>>> rectangle: ap.Rectangle = sprite.graphics.draw_rect(\n...     x=50, y=50, width=50, height=50)\n>>> _ = rectangle.click(on_click)\n```',  # noqa

    '## unbind_click_all API':
    '## unbind_click_all API',

    '<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>':  # noqa
    '<span class="inconspicuous-txt">特記事項: このAPIドキュメントはドキュメントビルド用のスクリプトによって自動で生成・同期されています。そのためもしかしたらこの節の内容は前節までの内容と重複している場合があります。</span>',  # noqa

    '**[Interface summary]** Unbind all click events.<hr>':
    '**[インターフェイス概要]** 全てのクリックイベントの設定を解除します。<hr>',

    '**[Examples]**':
    '**[コードサンプル]**',

    '```py\n>>> import apysc as ap\n>>> def on_click(\n...         e: ap.MouseEvent[ap.Rectangle], options: dict) -> None:\n...     rectangle: ap.Rectangle = e.this\n...     rectangle.fill_color = ap.String(\'#f0a\')\n...     rectangle.unbind_click_all()\n>>> stage: ap.Stage = ap.Stage()\n>>> sprite: ap.Sprite = ap.Sprite()\n>>> sprite.graphics.begin_fill(color=\'#0af\')\n>>> rectangle: ap.Rectangle = sprite.graphics.draw_rect(\n...     x=50, y=50, width=50, height=50)\n>>> _ = rectangle.click(on_click)\n```':  # noqa
    '```py\n>>> import apysc as ap\n>>> def on_click(\n...         e: ap.MouseEvent[ap.Rectangle], options: dict) -> None:\n...     rectangle: ap.Rectangle = e.this\n...     rectangle.fill_color = ap.String(\'#f0a\')\n...     rectangle.unbind_click_all()\n>>> stage: ap.Stage = ap.Stage()\n>>> sprite: ap.Sprite = ap.Sprite()\n>>> sprite.graphics.begin_fill(color=\'#0af\')\n>>> rectangle: ap.Rectangle = sprite.graphics.draw_rect(\n...     x=50, y=50, width=50, height=50)\n>>> _ = rectangle.click(on_click)\n```',  # noqa

}
