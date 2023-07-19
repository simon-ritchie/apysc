"""This module is for the translation mapping data of the
following document:

Document file: mousedown_and_mouseup.md
Language: jp
"""

from typing import Dict

MAPPING: Dict[str, str] = {
    ##################################################
    "# mousedown and mouseup interfaces": "# mousedown と mouseup のインターフェイス",
    ##################################################
    "This page explains the `mousedown` and `mouseup` interfaces.": "このページでは`mousedown`や`mouseup`の各インターフェイスについて説明します。",  # noqa
    ##################################################
    "## What interfaces are these?": "## 各インターフェイスの概要",
    ##################################################
    "The `mousedown` interface binds the event handler that the interface calls when a user mouse downed on a `DisplayObject` instance. Conversely, the `mouseup` interface binds the event handler that the interface calls when a user mouse upped on a `DisplayObject` one.": "`mousedown`インターフェイスは`DisplayObject`のインスタンス上でマウスを押した時のイベントのハンドラを設定するためのインターフェイスです。逆に`mouseup`インターフェイスはマウスから指を離した（押している状態を解除した）時のイベントのハンドラを設定するためのインターフェイスです。",  # noqa
    ##################################################
    "## See also": "## 関連資料",
    ##################################################
    "The following page describes the basic mouse event interfaces:": "以下のページでは基本的なマウスイベントのインターフェイスについて説明しています:",  # noqa
    ##################################################
    "- [Basic mouse event interfaces](mouse_event_basic.md)": "- [基本的なマウスイベントの各インターフェイス](jp_mouse_event_basic.md)",  # noqa
    ##################################################
    "## Basic usage of the mousedown and mouseup interfaces": "## mousedown と mouseup のインターフェイスの基本的な使い方",  # noqa
    ##################################################
    "Each `DisplayObject` instance has the `mousedown` and `mouseup` method interfaces, and you can bind handlers by these.": "`DisplayObject`の各インスタンスは`mousedown`と`mouseup`のメソッドのインターフェイスを持っており、それらを使ってハンドラを設定することができます。",  # noqa
    ##################################################
    "The following example binds the mouse down handler and mouse upped one to the rectangle. The handler changes the rectangle color when the mouse downs and reverts to the original one when the mouse upped.": "以下のコード例では四角に対してマウスを押した時と離した時のハンドラをそれぞれ設定しています。ハンドラではマウスを押した時に四角の色を変更し、マウスを離した時に元の色に戻しています。",  # noqa
    ##################################################
    '```py\n# runnable\nimport apysc as ap\n\n\ndef on_mousedown(e: ap.MouseEvent[ap.Rectangle], options: dict) -> None:\n    """\n    The handler that the rectangle calls when mousedown.\n\n    Parameters\n    ----------\n    e : MouseEvent\n        Event instance.\n    options : dict\n        Optional arguments dictionary.\n    """\n    rectangle: ap.Rectangle = e.this\n    rectangle.fill_color = ap.String("#f0a")\n\n\ndef on_mouseup(e: ap.MouseEvent[ap.Rectangle], options: dict) -> None:\n    """\n    The handler that the rectangle calls when mouseup.\n\n    Parameters\n    ----------\n    e : MouseEvent\n        Event instance.\n    options : dict\n        Optional arguments dictionary.\n    """\n    rectangle: ap.Rectangle = e.this\n    rectangle.fill_color = ap.String("#0af")\n\n\nap.Stage(\n    background_color="#333", stage_width=150, stage_height=150, stage_elem_id="stage"\n)\n\nsprite: ap.Sprite = ap.Sprite()\nsprite.graphics.begin_fill(color="#0af")\nrectangle: ap.Rectangle = sprite.graphics.draw_rect(x=50, y=50, width=50, height=50)\n\n# Bind each handler to the rectangle.\nrectangle.mousedown(on_mousedown)\nrectangle.mouseup(on_mouseup)\n\nap.save_overall_html(dest_dir_path="mousedown_and_mouseup_basic_usage/")\n```': '```py\n# runnable\nimport apysc as ap\n\n\ndef on_mousedown(e: ap.MouseEvent[ap.Rectangle], options: dict) -> None:\n    """\n    The handler that the rectangle calls when mousedown.\n\n    Parameters\n    ----------\n    e : MouseEvent\n        Event instance.\n    options : dict\n        Optional arguments dictionary.\n    """\n    rectangle: ap.Rectangle = e.this\n    rectangle.fill_color = ap.String("#f0a")\n\n\ndef on_mouseup(e: ap.MouseEvent[ap.Rectangle], options: dict) -> None:\n    """\n    The handler that the rectangle calls when mouseup.\n\n    Parameters\n    ----------\n    e : MouseEvent\n        Event instance.\n    options : dict\n        Optional arguments dictionary.\n    """\n    rectangle: ap.Rectangle = e.this\n    rectangle.fill_color = ap.String("#0af")\n\n\nap.Stage(\n    background_color="#333", stage_width=150, stage_height=150, stage_elem_id="stage"\n)\n\nsprite: ap.Sprite = ap.Sprite()\nsprite.graphics.begin_fill(color="#0af")\nrectangle: ap.Rectangle = sprite.graphics.draw_rect(x=50, y=50, width=50, height=50)\n\n# Bind each handler to the rectangle.\nrectangle.mousedown(on_mousedown)\nrectangle.mouseup(on_mouseup)\n\nap.save_overall_html(dest_dir_path="mousedown_and_mouseup_basic_usage/")\n```',  # noqa
    ##################################################
    "## Unbind interfaces": "## 解除用のインターフェイス",
    ##################################################
    "The `unbind_mousedown` and `unbind_mouseup` interfaces unbind each registered handler from the `DisplayObject`\\.": "`unbind_mousedown`と`unbind_mouseup`は`DisplayObject`のインスタンスから設定されているハンドラの設定を解除します。",  # noqa
    ##################################################
    "The following example unbinds handlers in the `on_mousedown` and `on_mouseup` functions so that the rectangle calls these handlers only once.": "以下のコード例では`on_mousedown`と`on_mouseup`の各ハンドラ内でハンドラの設定を解除しているためハンドラの処理は1回のみ実行されます。",  # noqa
    ##################################################
    '```py\n# runnable\nimport apysc as ap\n\n\ndef on_mousedown(e: ap.MouseEvent[ap.Rectangle], options: dict) -> None:\n    """\n    The handler that the rectangle calls when mousedown.\n\n    Parameters\n    ----------\n    e : MouseEvent\n        Event instance.\n    options : dict\n        Optional arguments dictionary.\n    """\n    rectangle: ap.Rectangle = e.this\n    rectangle.unbind_mousedown(handler=on_mousedown)\n    rectangle.fill_color = ap.String("#f0a")\n\n\ndef on_mouseup(e: ap.MouseEvent[ap.Rectangle], options: dict) -> None:\n    """\n    The handler that the rectangle calls when mouseup.\n\n    Parameters\n    ----------\n    e : MouseEvent\n        Event instance.\n    options : dict\n        Optional arguments dictionary.\n    """\n    rectangle: ap.Rectangle = e.this\n    rectangle.unbind_mouseup(handler=on_mouseup)\n    rectangle.fill_color = ap.String("#0af")\n\n\nap.Stage(\n    background_color="#333", stage_width=150, stage_height=150, stage_elem_id="stage"\n)\n\nsprite: ap.Sprite = ap.Sprite()\nsprite.graphics.begin_fill(color="#0af")\nrectangle: ap.Rectangle = sprite.graphics.draw_rect(x=50, y=50, width=50, height=50)\n\nrectangle.mousedown(on_mousedown)\nrectangle.mouseup(on_mouseup)\n\nap.save_overall_html(dest_dir_path="mousedown_and_mouseup_unbind_interfaces/")\n```': '```py\n# runnable\nimport apysc as ap\n\n\ndef on_mousedown(e: ap.MouseEvent[ap.Rectangle], options: dict) -> None:\n    """\n    The handler that the rectangle calls when mousedown.\n\n    Parameters\n    ----------\n    e : MouseEvent\n        Event instance.\n    options : dict\n        Optional arguments dictionary.\n    """\n    rectangle: ap.Rectangle = e.this\n    rectangle.unbind_mousedown(handler=on_mousedown)\n    rectangle.fill_color = ap.String("#f0a")\n\n\ndef on_mouseup(e: ap.MouseEvent[ap.Rectangle], options: dict) -> None:\n    """\n    The handler that the rectangle calls when mouseup.\n\n    Parameters\n    ----------\n    e : MouseEvent\n        Event instance.\n    options : dict\n        Optional arguments dictionary.\n    """\n    rectangle: ap.Rectangle = e.this\n    rectangle.unbind_mouseup(handler=on_mouseup)\n    rectangle.fill_color = ap.String("#0af")\n\n\nap.Stage(\n    background_color="#333", stage_width=150, stage_height=150, stage_elem_id="stage"\n)\n\nsprite: ap.Sprite = ap.Sprite()\nsprite.graphics.begin_fill(color="#0af")\nrectangle: ap.Rectangle = sprite.graphics.draw_rect(x=50, y=50, width=50, height=50)\n\nrectangle.mousedown(on_mousedown)\nrectangle.mouseup(on_mouseup)\n\nap.save_overall_html(dest_dir_path="mousedown_and_mouseup_unbind_interfaces/")\n```',  # noqa
    ##################################################
    "There are also existing the `unbind_mousedown_all` and `unbind_mouseup_all` interfaces. These interfaces unbind all the handlers from the target `DisplayObject` instance.": "また、`unbind_mousedown_all`や`unbind_mouseup_all`などのインターフェイスも存在します。これらのインターフェイスは`DisplayObject`のインスタンスから該当のイベントのハンドラ設定を全て取り除きます。",  # noqa
    ##################################################
    "## mousedown API": "## mousedown API",
    ##################################################
    '<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>': '<span class="inconspicuous-txt">特記事項: このAPIドキュメントはドキュメントビルド用のスクリプトによって自動で生成・同期されています。そのためもしかしたらこの節の内容は前節までの内容と重複している場合があります。</span>',  # noqa
    ##################################################
    "**[Interface summary]**": "**[インターフェイス概要]**",
    ##################################################
    "Add mouse down event listener setting.<hr>": "マウスのボタンを押した時のイベント設定を追加します。<hr>",
    ##################################################
    "**[Parameters]**": "**[引数]**",
    ##################################################
    "- `handler`: _Handler": "- `handler`: _Handler",
    ##################################################
    "  - Callable that would be called when mouse down on this instance.": "  - インスタンス上でマウスのボタンを押した時に呼ばれる関数もしくはメソッド。",  # noqa
    ##################################################
    "- `options`: dict or None, default None": "- `options`: dict or None, default None",  # noqa
    ##################################################
    "  - Optional arguments dictionary to be passed to a handler.": "  - ハンドラに渡される省略が可能な追加のパラメーターとしての辞書。",  # noqa
    ##################################################
    "<hr>": "<hr>",
    ##################################################
    "**[Returns]**": "**[返却値]**",
    ##################################################
    "- `name`: str": "- `name`: str",
    ##################################################
    "  - Handler's name.": "  - ハンドラ名。",
    ##################################################
    "<hr>": "<hr>",
    ##################################################
    "**[Examples]**": "**[コードサンプル]**",
    ##################################################
    '```py\n>>> import apysc as ap\n>>> def on_mousedown(e: ap.MouseEvent[ap.Rectangle], options: dict) -> None:\n...     rectangle: ap.Rectangle = e.this\n...     rectangle.fill_color = ap.String("#f0a")\n>>> stage: ap.Stage = ap.Stage()\n>>> sprite: ap.Sprite = ap.Sprite()\n>>> sprite.graphics.begin_fill(color="#0af")\n>>> rectangle: ap.Rectangle = sprite.graphics.draw_rect(\n...     x=50, y=50, width=50, height=50\n... )\n>>> _ = rectangle.mousedown(on_mousedown)\n```': '```py\n>>> import apysc as ap\n>>> def on_mousedown(e: ap.MouseEvent[ap.Rectangle], options: dict) -> None:\n...     rectangle: ap.Rectangle = e.this\n...     rectangle.fill_color = ap.String("#f0a")\n>>> stage: ap.Stage = ap.Stage()\n>>> sprite: ap.Sprite = ap.Sprite()\n>>> sprite.graphics.begin_fill(color="#0af")\n>>> rectangle: ap.Rectangle = sprite.graphics.draw_rect(\n...     x=50, y=50, width=50, height=50\n... )\n>>> _ = rectangle.mousedown(on_mousedown)\n```',  # noqa
    ##################################################
    "<hr>": "<hr>",
    ##################################################
    "**[References]**": "**[関連資料]**",
    ##################################################
    "- [About the handler options' type](https://simon-ritchie.github.io/apysc/en/about_handler_options_type.html)": "- [ハンドラのoptions引数の型について](https://simon-ritchie.github.io/apysc/jp/jp_about_handler_options_type.html)",  # noqa
    ##################################################
    "## unbind_mousedown API": "## unbind_mousedown API",
    ##################################################
    '<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>': '<span class="inconspicuous-txt">特記事項: このAPIドキュメントはドキュメントビルド用のスクリプトによって自動で生成・同期されています。そのためもしかしたらこの節の内容は前節までの内容と重複している場合があります。</span>',  # noqa
    ##################################################
    "**[Interface summary]**": "**[インターフェイス概要]**",
    ##################################################
    "Unbind a specified handler's mouse down event.<hr>": "マウスのボタンを押した際のイベントの指定されたハンドラ設定を解除します。<hr>",  # noqa
    ##################################################
    "**[Parameters]**": "**[引数]**",
    ##################################################
    "- `handler`: _Handler": "- `handler`: _Handler",
    ##################################################
    "  - Unbinding target Callable.": "  - イベント設定を取り除く対象の関数やメソッドなど。",
    ##################################################
    "<hr>": "<hr>",
    ##################################################
    "**[Examples]**": "**[コードサンプル]**",
    ##################################################
    '```py\n>>> import apysc as ap\n>>> def on_mousedown(e: ap.MouseEvent[ap.Rectangle], options: dict) -> None:\n...     rectangle: ap.Rectangle = e.this\n...     rectangle.fill_color = ap.String("#f0a")\n...     rectangle.unbind_mousedown(on_mousedown)\n>>> stage: ap.Stage = ap.Stage()\n>>> sprite: ap.Sprite = ap.Sprite()\n>>> sprite.graphics.begin_fill(color="#0af")\n>>> rectangle: ap.Rectangle = sprite.graphics.draw_rect(\n...     x=50, y=50, width=50, height=50\n... )\n>>> _ = rectangle.mousedown(on_mousedown)\n```': '```py\n>>> import apysc as ap\n>>> def on_mousedown(e: ap.MouseEvent[ap.Rectangle], options: dict) -> None:\n...     rectangle: ap.Rectangle = e.this\n...     rectangle.fill_color = ap.String("#f0a")\n...     rectangle.unbind_mousedown(on_mousedown)\n>>> stage: ap.Stage = ap.Stage()\n>>> sprite: ap.Sprite = ap.Sprite()\n>>> sprite.graphics.begin_fill(color="#0af")\n>>> rectangle: ap.Rectangle = sprite.graphics.draw_rect(\n...     x=50, y=50, width=50, height=50\n... )\n>>> _ = rectangle.mousedown(on_mousedown)\n```',  # noqa
    ##################################################
    "## unbind_mousedown_all API": "## unbind_mousedown_all API",
    ##################################################
    '<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>': '<span class="inconspicuous-txt">特記事項: このAPIドキュメントはドキュメントビルド用のスクリプトによって自動で生成・同期されています。そのためもしかしたらこの節の内容は前節までの内容と重複している場合があります。</span>',  # noqa
    ##################################################
    "**[Interface summary]**": "**[インターフェイス概要]**",
    ##################################################
    "Unbind all mouse down events.<hr>": "マウスのボタンを押した時のイベントの全てのハンドラ設定を解除します。<hr>",
    ##################################################
    "**[Examples]**": "**[コードサンプル]**",
    ##################################################
    '```py\n>>> import apysc as ap\n>>> def on_mousedown(e: ap.MouseEvent[ap.Rectangle], options: dict) -> None:\n...     rectangle: ap.Rectangle = e.this\n...     rectangle.fill_color = ap.String("#f0a")\n...     rectangle.unbind_mousedown_all()\n>>> stage: ap.Stage = ap.Stage()\n>>> sprite: ap.Sprite = ap.Sprite()\n>>> sprite.graphics.begin_fill(color="#0af")\n>>> rectangle: ap.Rectangle = sprite.graphics.draw_rect(\n...     x=50, y=50, width=50, height=50\n... )\n>>> _ = rectangle.mousedown(on_mousedown)\n```': '```py\n>>> import apysc as ap\n>>> def on_mousedown(e: ap.MouseEvent[ap.Rectangle], options: dict) -> None:\n...     rectangle: ap.Rectangle = e.this\n...     rectangle.fill_color = ap.String("#f0a")\n...     rectangle.unbind_mousedown_all()\n>>> stage: ap.Stage = ap.Stage()\n>>> sprite: ap.Sprite = ap.Sprite()\n>>> sprite.graphics.begin_fill(color="#0af")\n>>> rectangle: ap.Rectangle = sprite.graphics.draw_rect(\n...     x=50, y=50, width=50, height=50\n... )\n>>> _ = rectangle.mousedown(on_mousedown)\n```',  # noqa
    ##################################################
    "## mouseup API": "## mouseup API",
    ##################################################
    '<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>': '<span class="inconspicuous-txt">特記事項: このAPIドキュメントはドキュメントビルド用のスクリプトによって自動で生成・同期されています。そのためもしかしたらこの節の内容は前節までの内容と重複している場合があります。</span>',  # noqa
    ##################################################
    "**[Interface summary]**": "**[インターフェイス概要]**",
    ##################################################
    "Add mouse up event listener setting.<hr>": "マウスのボタンを離した時のイベント設定を追加します。<hr>",
    ##################################################
    "**[Parameters]**": "**[引数]**",
    ##################################################
    "- `handler`: _Handler": "- `handler`: _Handler",
    ##################################################
    "  - Callable that would be called when mouse-up on this instance.": "  - インスタンス上でマウスのボタンを離した時に呼ばれる関数もしくはメソッド。",  # noqa
    ##################################################
    "- `options`: dict or None, default None": "- `options`: dict or None, default None",  # noqa
    ##################################################
    "  - Optional arguments dictionary to be passed to a handler.": "  - ハンドラに渡される省略が可能な追加のパラメーターとしての辞書。",  # noqa
    ##################################################
    "<hr>": "<hr>",
    ##################################################
    "**[Returns]**": "**[返却値]**",
    ##################################################
    "- `name`: str": "- `name`: str",
    ##################################################
    "  - Handler's name.": "  - ハンドラ名。",
    ##################################################
    "<hr>": "<hr>",
    ##################################################
    "**[Examples]**": "**[コードサンプル]**",
    ##################################################
    '```py\n>>> import apysc as ap\n>>> def on_mouseup(e: ap.MouseEvent[ap.Rectangle], options: dict) -> None:\n...     rectangle: ap.Rectangle = e.this\n...     rectangle.fill_color = ap.String("#f0a")\n>>> stage: ap.Stage = ap.Stage()\n>>> sprite: ap.Sprite = ap.Sprite()\n>>> sprite.graphics.begin_fill(color="#0af")\n>>> rectangle: ap.Rectangle = sprite.graphics.draw_rect(\n...     x=50, y=50, width=50, height=50\n... )\n>>> _ = rectangle.mouseup(on_mouseup)\n```': '```py\n>>> import apysc as ap\n>>> def on_mouseup(e: ap.MouseEvent[ap.Rectangle], options: dict) -> None:\n...     rectangle: ap.Rectangle = e.this\n...     rectangle.fill_color = ap.String("#f0a")\n>>> stage: ap.Stage = ap.Stage()\n>>> sprite: ap.Sprite = ap.Sprite()\n>>> sprite.graphics.begin_fill(color="#0af")\n>>> rectangle: ap.Rectangle = sprite.graphics.draw_rect(\n...     x=50, y=50, width=50, height=50\n... )\n>>> _ = rectangle.mouseup(on_mouseup)\n```',  # noqa
    ##################################################
    "<hr>": "<hr>",
    ##################################################
    "**[References]**": "**[関連資料]**",
    ##################################################
    "- [About the handler options' type](https://simon-ritchie.github.io/apysc/en/about_handler_options_type.html)": "- [ハンドラのoptions引数の型について](https://simon-ritchie.github.io/apysc/jp/jp_about_handler_options_type.html)",  # noqa
    ##################################################
    "## unbind_mouseup API": "## unbind_mouseup API",
    ##################################################
    '<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>': '<span class="inconspicuous-txt">特記事項: このAPIドキュメントはドキュメントビルド用のスクリプトによって自動で生成・同期されています。そのためもしかしたらこの節の内容は前節までの内容と重複している場合があります。</span>',  # noqa
    ##################################################
    "**[Interface summary]**": "**[インターフェイス概要]**",
    ##################################################
    "Unbind a specified handler's mouse-up event.<hr>": "マウスのボタンを離した際のイベントの指定されたハンドラ設定を解除します。<hr>",  # noqa
    ##################################################
    "**[Parameters]**": "**[引数]**",
    ##################################################
    "- `handler`: _Handler": "- `handler`: _Handler",
    ##################################################
    "  - Unbinding target Callable.": "  - イベント設定を取り除く対象の関数やメソッドなど。",
    ##################################################
    "<hr>": "<hr>",
    ##################################################
    "**[Examples]**": "**[コードサンプル]**",
    ##################################################
    '```py\n>>> import apysc as ap\n>>> def on_mouseup(e: ap.MouseEvent[ap.Rectangle], options: dict) -> None:\n...     rectangle: ap.Rectangle = e.this\n...     rectangle.fill_color = ap.String("#f0a")\n...     rectangle.unbind_mouseup(on_mouseup)\n>>> stage: ap.Stage = ap.Stage()\n>>> sprite: ap.Sprite = ap.Sprite()\n>>> sprite.graphics.begin_fill(color="#0af")\n>>> rectangle: ap.Rectangle = sprite.graphics.draw_rect(\n...     x=50, y=50, width=50, height=50\n... )\n>>> _ = rectangle.mouseup(on_mouseup)\n```': '```py\n>>> import apysc as ap\n>>> def on_mouseup(e: ap.MouseEvent[ap.Rectangle], options: dict) -> None:\n...     rectangle: ap.Rectangle = e.this\n...     rectangle.fill_color = ap.String("#f0a")\n...     rectangle.unbind_mouseup(on_mouseup)\n>>> stage: ap.Stage = ap.Stage()\n>>> sprite: ap.Sprite = ap.Sprite()\n>>> sprite.graphics.begin_fill(color="#0af")\n>>> rectangle: ap.Rectangle = sprite.graphics.draw_rect(\n...     x=50, y=50, width=50, height=50\n... )\n>>> _ = rectangle.mouseup(on_mouseup)\n```',  # noqa
    ##################################################
    "## unbind_mouseup_all API": "## unbind_mouseup_all API",
    ##################################################
    '<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>': '<span class="inconspicuous-txt">特記事項: このAPIドキュメントはドキュメントビルド用のスクリプトによって自動で生成・同期されています。そのためもしかしたらこの節の内容は前節までの内容と重複している場合があります。</span>',  # noqa
    ##################################################
    "**[Interface summary]**": "**[インターフェイス概要]**",
    ##################################################
    "Unbind all mouse up events.<hr>": "マウスのボタンを離したとぎのイベントの全てのハンドラ設定を解除します。<hr>",
    ##################################################
    "**[Examples]**": "**[コードサンプル]**",
    ##################################################
    '```py\n>>> import apysc as ap\n>>> def on_mouseup(e: ap.MouseEvent[ap.Rectangle], options: dict) -> None:\n...     rectangle: ap.Rectangle = e.this\n...     rectangle.fill_color = ap.String("#f0a")\n...     rectangle.unbind_mouseup_all()\n>>> stage: ap.Stage = ap.Stage()\n>>> sprite: ap.Sprite = ap.Sprite()\n>>> sprite.graphics.begin_fill(color="#0af")\n>>> rectangle: ap.Rectangle = sprite.graphics.draw_rect(\n...     x=50, y=50, width=50, height=50\n... )\n>>> _ = rectangle.mouseup(on_mouseup)\n```': '```py\n>>> import apysc as ap\n>>> def on_mouseup(e: ap.MouseEvent[ap.Rectangle], options: dict) -> None:\n...     rectangle: ap.Rectangle = e.this\n...     rectangle.fill_color = ap.String("#f0a")\n...     rectangle.unbind_mouseup_all()\n>>> stage: ap.Stage = ap.Stage()\n>>> sprite: ap.Sprite = ap.Sprite()\n>>> sprite.graphics.begin_fill(color="#0af")\n>>> rectangle: ap.Rectangle = sprite.graphics.draw_rect(\n...     x=50, y=50, width=50, height=50\n... )\n>>> _ = rectangle.mouseup(on_mouseup)\n```',  # noqa
}
