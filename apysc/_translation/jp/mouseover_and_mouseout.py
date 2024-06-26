"""This module is for the translation mapping data of the
following document:

Document file: mouseover_and_mouseout.md
Language: jp
"""

from typing import Dict

MAPPING: Dict[str, str] = {
    ##################################################
    "# mouseover and mouseout interfaces": "# mouseover と mouseout のインターフェイス",
    ##################################################
    "This page explains the `mouseover` and `mouseout` interfaces.": "このページでは`mouseover`と`mouseout`の各インターフェイスについて説明します。",  # noqa
    ##################################################
    "## What interfaces are these?": "## 各インターフェイスの概要",
    ##################################################
    "The `mouseover` interface binds the event handler. Moreover, this interface calls the handler when a mouse cursor is over on a `DisplayObject` instance. Conversely, the `mouseout` interface also binds and calls the handler when a cursor is out from the `DisplayObject` one.": "`mouseover`インターフェイスはマウスカーソルが対象の`DisplayObject`インスタンス上に乗った時のイベントのハンドラを設定します。逆に`mouseout`インターフェイスはマウスカーソルが対象の`DisplayObject`上から離れた時のイベントのハンドラを設定します。",  # noqa
    ##################################################
    "## See also": "## 関連資料",
    ##################################################
    "The following page describes the basic mouse event interfaces.": "以下のページでは基本的なマウスイベントの各インターフェイスについて説明しています。",  # noqa
    ##################################################
    "- [Basic mouse event interfaces](mouse_event_basic.md)": "- [基本的なマウスイベントの各インターフェイス](jp_mouse_event_basic.md)",  # noqa
    ##################################################
    "## Basic usage of the mouseover and mouseout interfaces": "## mouseover と mouseout の各インターフェイスの基本的な使い方",  # noqa
    ##################################################
    "Each `DisplayObject` instance has the `mouseover` and `mouseout` interfaces, and you can bind handlers by these.": "`DisplayObject`の各インスタンスは`mouseover`と`mouseout`の各インターフェイスを持っており、それらを使ってハンドラを設定することができます。",  # noqa
    ##################################################
    "The following example binds the mouse over and handler and mouse out one to the rectangle. The rectangle color changes when your cursor is over the rectangle. Also, it reverts to the original one when your cursor is outed from the rectangle.": "以下のコード例ではマウスが乗った時と離れた時のイベントのハンドラを四角に対して設定しています。四角にマウスカーソルが乗った時に四角の色が変更され、カーソルが離れた時に色が戻されるように設定してあります。",  # noqa
    ##################################################
    '```py\n# runnable\nimport apysc as ap\n\n\ndef on_mouseover(e: ap.MouseEvent[ap.Rectangle], options: dict) -> None:\n    """\n    The handler that the rectangle calls when mouseover.\n\n    Parameters\n    ----------\n    e : MouseEvent\n        Event instance.\n    options : dict\n        Optional arguments dictionary.\n    """\n    rectangle: ap.Rectangle = e.this\n\n    # Change the rectangle fill color to magenta.\n    rectangle.fill_color = ap.Color("#f0a")\n\n\ndef on_mouseout(e: ap.MouseEvent[ap.Rectangle], options: dict) -> None:\n    """\n    The handler that the rectangle calls when mouseout.\n\n    Parameters\n    ----------\n    e : MouseEvent\n        Event instance.\n    options : dict\n        Optional arguments dictionary.\n    """\n    rectangle: ap.Rectangle = e.this\n\n    # Revert the rectangle fill color.\n    rectangle.fill_color = ap.Color("#0af")\n\n\nap.Stage(\n    background_color=ap.Color("#333"),\n    stage_width=150,\n    stage_height=150,\n    stage_elem_id="stage",\n)\n\nsprite: ap.Sprite = ap.Sprite()\n\nsprite.graphics.begin_fill(color=ap.Color("#0af"))\nrectangle: ap.Rectangle = sprite.graphics.draw_rect(x=50, y=50, width=50, height=50)\n\n# Bind the mouse over and mouse out event handlers to the rectangle.\nrectangle.mouseover(on_mouseover)\nrectangle.mouseout(on_mouseout)\n\nap.save_overall_html(dest_dir_path="mouseover_and_mouseout_basic_usage/")\n```': '```py\n# runnable\nimport apysc as ap\n\n\ndef on_mouseover(e: ap.MouseEvent[ap.Rectangle], options: dict) -> None:\n    """\n    The handler that the rectangle calls when mouseover.\n\n    Parameters\n    ----------\n    e : MouseEvent\n        Event instance.\n    options : dict\n        Optional arguments dictionary.\n    """\n    rectangle: ap.Rectangle = e.this\n\n    # Change the rectangle fill color to magenta.\n    rectangle.fill_color = ap.Color("#f0a")\n\n\ndef on_mouseout(e: ap.MouseEvent[ap.Rectangle], options: dict) -> None:\n    """\n    The handler that the rectangle calls when mouseout.\n\n    Parameters\n    ----------\n    e : MouseEvent\n        Event instance.\n    options : dict\n        Optional arguments dictionary.\n    """\n    rectangle: ap.Rectangle = e.this\n\n    # Revert the rectangle fill color.\n    rectangle.fill_color = ap.Color("#0af")\n\n\nap.Stage(\n    background_color=ap.Color("#333"),\n    stage_width=150,\n    stage_height=150,\n    stage_elem_id="stage",\n)\n\nsprite: ap.Sprite = ap.Sprite()\n\nsprite.graphics.begin_fill(color=ap.Color("#0af"))\nrectangle: ap.Rectangle = sprite.graphics.draw_rect(x=50, y=50, width=50, height=50)\n\n# Bind the mouse over and mouse out event handlers to the rectangle.\nrectangle.mouseover(on_mouseover)\nrectangle.mouseout(on_mouseout)\n\nap.save_overall_html(dest_dir_path="mouseover_and_mouseout_basic_usage/")\n```',  # noqa
    ##################################################
    "## Unbind interfaces": "## 解除用のインターフェイス",
    ##################################################
    "The `unbind_mouseover` and `unbind_mouseout` interfaces unbind each registered handler from the `DisplayObject`\\.": "`unbind_mouseover`と`unbind_mouseout`の各インターフェイスは`DisplayObject`から登録されているハンドラの設定を解除します。",  # noqa
    ##################################################
    "The following example unbind handlers in the `on_mouseover` and `on_mouseout` functions so that the interface calls these handlers only once.": "以下のコード例では`on_mouseover`と`on_mouseout`のハンドラの関数内でハンドラの設定を解除しているためこれらのハンドラは最初の1回のみ呼ばれます。",  # noqa
    ##################################################
    '```py\n# runnable\nimport apysc as ap\n\n\ndef on_mouseover(e: ap.MouseEvent[ap.Rectangle], options: dict) -> None:\n    """\n    The handler that the rectangle calls when mouseover.\n\n    Parameters\n    ----------\n    e : MouseEvent\n        Event instance.\n    options : dict\n        Optional arguments dictionary.\n    """\n    rectangle: ap.Rectangle = e.this\n    rectangle.fill_color = ap.Color("#f0a")\n\n    # Unbind the mouseover handler.\n    rectangle.unbind_mouseover(handler=on_mouseover)\n\n\ndef on_mouseout(e: ap.MouseEvent[ap.Rectangle], options: dict) -> None:\n    """\n    The handler that the rectangle calls when mouseout.\n\n    Parameters\n    ----------\n    e : MouseEvent\n        Event instance.\n    options : dict\n        Optional arguments dictionary.\n    """\n    rectangle: ap.Rectangle = e.this\n    rectangle.fill_color = ap.Color("#0af")\n\n    rectangle.unbind_mouseout(handler=on_mouseout)\n\n\nap.Stage(\n    background_color=ap.Color("#333"),\n    stage_width=150,\n    stage_height=150,\n    stage_elem_id="stage",\n)\n\nsprite: ap.Sprite = ap.Sprite()\n\nsprite.graphics.begin_fill(color=ap.Color("#0af"))\nrectangle: ap.Rectangle = sprite.graphics.draw_rect(x=50, y=50, width=50, height=50)\n\nrectangle.mouseover(on_mouseover)\nrectangle.mouseout(on_mouseout)\n\nap.save_overall_html(dest_dir_path="mouseover_and_mouseout_unbind_interfaces/")\n```': '```py\n# runnable\nimport apysc as ap\n\n\ndef on_mouseover(e: ap.MouseEvent[ap.Rectangle], options: dict) -> None:\n    """\n    The handler that the rectangle calls when mouseover.\n\n    Parameters\n    ----------\n    e : MouseEvent\n        Event instance.\n    options : dict\n        Optional arguments dictionary.\n    """\n    rectangle: ap.Rectangle = e.this\n    rectangle.fill_color = ap.Color("#f0a")\n\n    # Unbind the mouseover handler.\n    rectangle.unbind_mouseover(handler=on_mouseover)\n\n\ndef on_mouseout(e: ap.MouseEvent[ap.Rectangle], options: dict) -> None:\n    """\n    The handler that the rectangle calls when mouseout.\n\n    Parameters\n    ----------\n    e : MouseEvent\n        Event instance.\n    options : dict\n        Optional arguments dictionary.\n    """\n    rectangle: ap.Rectangle = e.this\n    rectangle.fill_color = ap.Color("#0af")\n\n    rectangle.unbind_mouseout(handler=on_mouseout)\n\n\nap.Stage(\n    background_color=ap.Color("#333"),\n    stage_width=150,\n    stage_height=150,\n    stage_elem_id="stage",\n)\n\nsprite: ap.Sprite = ap.Sprite()\n\nsprite.graphics.begin_fill(color=ap.Color("#0af"))\nrectangle: ap.Rectangle = sprite.graphics.draw_rect(x=50, y=50, width=50, height=50)\n\nrectangle.mouseover(on_mouseover)\nrectangle.mouseout(on_mouseout)\n\nap.save_overall_html(dest_dir_path="mouseover_and_mouseout_unbind_interfaces/")\n```',  # noqa
    ##################################################
    "There are also existing the `unbind_mouseover_all` and `unbind_mouseout_all` interfaces. These interfaces unbind all the handlers from the target `DisplayObject` instance.": "`unbind_mouseover_all`と`unbind_mouseout_all`の各インターフェイスも存在します。これらのインターフェイスは対象の`DisplayObject`のインスタンスから対象のイベントのハンドラ設定を全て解除します。",  # noqa
    ##################################################
    "## mouseover API": "## mouseover API",
    ##################################################
    '<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>': '<span class="inconspicuous-txt">特記事項: このAPIドキュメントはドキュメントビルド用のスクリプトによって自動で生成・同期されています。そのためもしかしたらこの節の内容は前節までの内容と重複している場合があります。</span>',  # noqa
    ##################################################
    "**[Interface summary]**": "**[インターフェイス概要]**",
    ##################################################
    "Add mouse over event listener setting.<hr>": "マウスカーソルが乗った時のイベントのハンドラ設定を追加します。<hr>",  # noqa
    ##################################################
    "**[Parameters]**": "**[引数]**",
    ##################################################
    "- `handler`: _Handler": "- `handler`: _Handler",
    ##################################################
    "  - Callable that would be called when mouse over on this instance.": "  - インスタンス上にマウスカーソルが乗った際に呼ばれる関数もしくはメソッド。",  # noqa
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
    '```py\n>>> import apysc as ap\n>>> def on_mouseover(e: ap.MouseEvent[ap.Rectangle], options: dict) -> None:\n...     rectangle: ap.Rectangle = e.this\n...     rectangle.fill_color = ap.Color("#f0a")\n>>> stage: ap.Stage = ap.Stage()\n>>> sprite: ap.Sprite = ap.Sprite()\n>>> sprite.graphics.begin_fill(color=ap.Color("#0af"))\n>>> rectangle: ap.Rectangle = sprite.graphics.draw_rect(\n...     x=50, y=50, width=50, height=50\n... )\n>>> _ = rectangle.mouseout(on_mouseover)\n```': '```py\n>>> import apysc as ap\n>>> def on_mouseover(e: ap.MouseEvent[ap.Rectangle], options: dict) -> None:\n...     rectangle: ap.Rectangle = e.this\n...     rectangle.fill_color = ap.Color("#f0a")\n>>> stage: ap.Stage = ap.Stage()\n>>> sprite: ap.Sprite = ap.Sprite()\n>>> sprite.graphics.begin_fill(color=ap.Color("#0af"))\n>>> rectangle: ap.Rectangle = sprite.graphics.draw_rect(\n...     x=50, y=50, width=50, height=50\n... )\n>>> _ = rectangle.mouseout(on_mouseover)\n```',  # noqa
    ##################################################
    "<hr>": "<hr>",
    ##################################################
    "**[References]**": "**[関連資料]**",
    ##################################################
    "- [About the handler options' type](https://simon-ritchie.github.io/apysc/en/about_handler_options_type.html)": "- [ハンドラのoptions引数の型について](https://simon-ritchie.github.io/apysc/jp/jp_about_handler_options_type.html)",  # noqa
    ##################################################
    "## unbind_mouseover API": "## unbind_mouseover API",
    ##################################################
    '<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>': '<span class="inconspicuous-txt">特記事項: このAPIドキュメントはドキュメントビルド用のスクリプトによって自動で生成・同期されています。そのためもしかしたらこの節の内容は前節までの内容と重複している場合があります。</span>',  # noqa
    ##################################################
    "**[Interface summary]**": "**[インターフェイス概要]**",
    ##################################################
    "Unbind a specified handler's mouseover event.<hr>": "マウスカーソルが乗った際のイベントの指定されたハンドラ設定を解除します。<hr>",  # noqa
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
    '```py\n>>> import apysc as ap\n>>> def on_mouseover(e: ap.MouseEvent[ap.Rectangle], options: dict) -> None:\n...     rectangle: ap.Rectangle = e.this\n...     rectangle.fill_color = ap.Color("#f0a")\n...     rectangle.unbind_mouseover(on_mouseover)\n>>> stage: ap.Stage = ap.Stage()\n>>> sprite: ap.Sprite = ap.Sprite()\n>>> sprite.graphics.begin_fill(color=ap.Color("#0af"))\n>>> rectangle: ap.Rectangle = sprite.graphics.draw_rect(\n...     x=50, y=50, width=50, height=50\n... )\n>>> _ = rectangle.mouseout(on_mouseover)\n```': '```py\n>>> import apysc as ap\n>>> def on_mouseover(e: ap.MouseEvent[ap.Rectangle], options: dict) -> None:\n...     rectangle: ap.Rectangle = e.this\n...     rectangle.fill_color = ap.Color("#f0a")\n...     rectangle.unbind_mouseover(on_mouseover)\n>>> stage: ap.Stage = ap.Stage()\n>>> sprite: ap.Sprite = ap.Sprite()\n>>> sprite.graphics.begin_fill(color=ap.Color("#0af"))\n>>> rectangle: ap.Rectangle = sprite.graphics.draw_rect(\n...     x=50, y=50, width=50, height=50\n... )\n>>> _ = rectangle.mouseout(on_mouseover)\n```',  # noqa
    ##################################################
    "## unbind_mouseover_all API": "## unbind_mouseover_all API",
    ##################################################
    '<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>': '<span class="inconspicuous-txt">特記事項: このAPIドキュメントはドキュメントビルド用のスクリプトによって自動で生成・同期されています。そのためもしかしたらこの節の内容は前節までの内容と重複している場合があります。</span>',  # noqa
    ##################################################
    "**[Interface summary]**": "**[インターフェイス概要]**",
    ##################################################
    "Unbind all mouseover events.<hr>": "マウスカーソルが乗った際のイベントの全てのハンドラ設定を解除します。<hr>",
    ##################################################
    "**[Examples]**": "**[コードサンプル]**",
    ##################################################
    '```py\n>>> import apysc as ap\n>>> def on_mouseover(e: ap.MouseEvent[ap.Rectangle], options: dict) -> None:\n...     rectangle: ap.Rectangle = e.this\n...     rectangle.fill_color = ap.Color("#f0a")\n...     rectangle.unbind_mouseover_all()\n>>> stage: ap.Stage = ap.Stage()\n>>> sprite: ap.Sprite = ap.Sprite()\n>>> sprite.graphics.begin_fill(color=ap.Color("#0af"))\n>>> rectangle: ap.Rectangle = sprite.graphics.draw_rect(\n...     x=50, y=50, width=50, height=50\n... )\n>>> _ = rectangle.mouseout(on_mouseover)\n```': '```py\n>>> import apysc as ap\n>>> def on_mouseover(e: ap.MouseEvent[ap.Rectangle], options: dict) -> None:\n...     rectangle: ap.Rectangle = e.this\n...     rectangle.fill_color = ap.Color("#f0a")\n...     rectangle.unbind_mouseover_all()\n>>> stage: ap.Stage = ap.Stage()\n>>> sprite: ap.Sprite = ap.Sprite()\n>>> sprite.graphics.begin_fill(color=ap.Color("#0af"))\n>>> rectangle: ap.Rectangle = sprite.graphics.draw_rect(\n...     x=50, y=50, width=50, height=50\n... )\n>>> _ = rectangle.mouseout(on_mouseover)\n```',  # noqa
    ##################################################
    "## mouseout API": "## mouseout API",
    ##################################################
    '<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>': '<span class="inconspicuous-txt">特記事項: このAPIドキュメントはドキュメントビルド用のスクリプトによって自動で生成・同期されています。そのためもしかしたらこの節の内容は前節までの内容と重複している場合があります。</span>',  # noqa
    ##################################################
    "**[Interface summary]**": "**[インターフェイス概要]**",
    ##################################################
    "Add mouse out event listener setting.<hr>": "マウスカーソルがインスタンス上から離れた際のイベントのハンドラを設定します。<hr>",  # noqa
    ##################################################
    "**[Parameters]**": "**[引数]**",
    ##################################################
    "- `handler`: _Handler": "- `handler`: _Handler",
    ##################################################
    "  - Callable that would be called when mouse out on this instance.": "  - インスタンス上からマウスカーソルが離れた際のイベントの対象のハンドラ設定を解除します。",  # noqa
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
    '```py\n>>> import apysc as ap\n>>> def on_mouseout(e: ap.MouseEvent[ap.Rectangle], options: dict) -> None:\n...     rectangle: ap.Rectangle = e.this\n...     rectangle.fill_color = ap.Color("#f0a")\n>>> stage: ap.Stage = ap.Stage()\n>>> sprite: ap.Sprite = ap.Sprite()\n>>> sprite.graphics.begin_fill(color=ap.Color("#0af"))\n>>> rectangle: ap.Rectangle = sprite.graphics.draw_rect(\n...     x=50, y=50, width=50, height=50\n... )\n>>> _ = rectangle.mouseout(on_mouseout)\n```': '```py\n>>> import apysc as ap\n>>> def on_mouseout(e: ap.MouseEvent[ap.Rectangle], options: dict) -> None:\n...     rectangle: ap.Rectangle = e.this\n...     rectangle.fill_color = ap.Color("#f0a")\n>>> stage: ap.Stage = ap.Stage()\n>>> sprite: ap.Sprite = ap.Sprite()\n>>> sprite.graphics.begin_fill(color=ap.Color("#0af"))\n>>> rectangle: ap.Rectangle = sprite.graphics.draw_rect(\n...     x=50, y=50, width=50, height=50\n... )\n>>> _ = rectangle.mouseout(on_mouseout)\n```',  # noqa
    ##################################################
    "<hr>": "<hr>",
    ##################################################
    "**[References]**": "**[関連資料]**",
    ##################################################
    "- [About the handler options' type](https://simon-ritchie.github.io/apysc/en/about_handler_options_type.html)": "- [ハンドラのoptions引数の型について](https://simon-ritchie.github.io/apysc/jp/jp_about_handler_options_type.html)",  # noqa
    ##################################################
    "## unbind_mouseout API": "## unbind_mouseout API",
    ##################################################
    '<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>': '<span class="inconspicuous-txt">特記事項: このAPIドキュメントはドキュメントビルド用のスクリプトによって自動で生成・同期されています。そのためもしかしたらこの節の内容は前節までの内容と重複している場合があります。</span>',  # noqa
    ##################################################
    "**[Interface summary]**": "**[インターフェイス概要]**",
    ##################################################
    "Unbind a specified handler's mouse-out event.<hr>": "インスタンス上からマウスカーソルが離れた際のイベントの対象のハンドラ設定を解除します。<hr>",  # noqa
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
    '```py\n>>> import apysc as ap\n>>> def on_mouseout(e: ap.MouseEvent[ap.Rectangle], options: dict) -> None:\n...     rectangle: ap.Rectangle = e.this\n...     rectangle.fill_color = ap.Color("#f0a")\n...     rectangle.unbind_mouseout(on_mouseout)\n>>> stage: ap.Stage = ap.Stage()\n>>> sprite: ap.Sprite = ap.Sprite()\n>>> sprite.graphics.begin_fill(color=ap.Color("#0af"))\n>>> rectangle: ap.Rectangle = sprite.graphics.draw_rect(\n...     x=50, y=50, width=50, height=50\n... )\n>>> _ = rectangle.mouseout(on_mouseout)\n```': '```py\n>>> import apysc as ap\n>>> def on_mouseout(e: ap.MouseEvent[ap.Rectangle], options: dict) -> None:\n...     rectangle: ap.Rectangle = e.this\n...     rectangle.fill_color = ap.Color("#f0a")\n...     rectangle.unbind_mouseout(on_mouseout)\n>>> stage: ap.Stage = ap.Stage()\n>>> sprite: ap.Sprite = ap.Sprite()\n>>> sprite.graphics.begin_fill(color=ap.Color("#0af"))\n>>> rectangle: ap.Rectangle = sprite.graphics.draw_rect(\n...     x=50, y=50, width=50, height=50\n... )\n>>> _ = rectangle.mouseout(on_mouseout)\n```',  # noqa
    ##################################################
    "## unbind_mouseout_all API": "## unbind_mouseout_all API",
    ##################################################
    '<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>': '<span class="inconspicuous-txt">特記事項: このAPIドキュメントはドキュメントビルド用のスクリプトによって自動で生成・同期されています。そのためもしかしたらこの節の内容は前節までの内容と重複している場合があります。</span>',  # noqa
    ##################################################
    "**[Interface summary]**": "**[インターフェイス概要]**",
    ##################################################
    "Unbind all mouse out events.<hr>": "インスタンス上からマウスカーソルが離れた際のイベントのハンドラ設定を全て解除します。<hr>",  # noqa
    ##################################################
    "**[Examples]**": "**[コードサンプル]**",
    ##################################################
    '```py\n>>> import apysc as ap\n>>> def on_mouseout(e: ap.MouseEvent[ap.Rectangle], options: dict) -> None:\n...     rectangle: ap.Rectangle = e.this\n...     rectangle.fill_color = ap.Color("#f0a")\n...     rectangle.unbind_mouseout_all()\n>>> stage: ap.Stage = ap.Stage()\n>>> sprite: ap.Sprite = ap.Sprite()\n>>> sprite.graphics.begin_fill(color=ap.Color("#0af"))\n>>> rectangle: ap.Rectangle = sprite.graphics.draw_rect(\n...     x=50, y=50, width=50, height=50\n... )\n>>> _ = rectangle.mouseout(on_mouseout)\n```': '```py\n>>> import apysc as ap\n>>> def on_mouseout(e: ap.MouseEvent[ap.Rectangle], options: dict) -> None:\n...     rectangle: ap.Rectangle = e.this\n...     rectangle.fill_color = ap.Color("#f0a")\n...     rectangle.unbind_mouseout_all()\n>>> stage: ap.Stage = ap.Stage()\n>>> sprite: ap.Sprite = ap.Sprite()\n>>> sprite.graphics.begin_fill(color=ap.Color("#0af"))\n>>> rectangle: ap.Rectangle = sprite.graphics.draw_rect(\n...     x=50, y=50, width=50, height=50\n... )\n>>> _ = rectangle.mouseout(on_mouseout)\n```',  # noqa
}
