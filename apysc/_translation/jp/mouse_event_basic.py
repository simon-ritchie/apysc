"""This module is for the translation mapping data of the
following document:

Document file: mouse_event_basic.md
Language: jp
"""

from typing import Dict

MAPPING: Dict[str, str] = {
    ##################################################
    "# Basic mouse event interfaces": "# 基本的なマウスイベントの各インターフェイス",
    ##################################################
    "This page explains the basic mouse event interfaces, like the `this` attribute.": "このページでは`this`属性などのマウスイベントの基本的な各インターフェイスについて説明します。",  # noqa
    ##################################################
    "## Basic binding usage": "## 基本的なイベント登録処理の使い方",
    ##################################################
    "Each mouse event binding interface accepts `handler` and `options` arguments. The `handler` argument is each interface's callable object when event dispatching.": "各マウスイベント設定のインターフェイスは`handler`と`options`引数を受け付けます。`handler`引数はイベントが発行された際に使用される関数などのオブジェクトです。",  # noqa
    ##################################################
    "The `options` argument is an optional parameter dictionary to be passed to the handler. You can skip this argument.": "`options`引数はハンドラへ渡される追加の任意の辞書のパラメーターです。この引数は省略できます。",  # noqa
    ##################################################
    "For instance, you can set the `click` event as follows:": "例えば`click`のイベントを以下のコードのように設定することができます:",  # noqa
    ##################################################
    '```py\n# runnable\nfrom typing_extensions import TypedDict\n\nimport apysc as ap\n\nap.Stage(\n    background_color=ap.Color("#333"),\n    stage_width=150,\n    stage_height=150,\n    stage_elem_id="stage",\n)\n\nsprite: ap.Sprite = ap.Sprite()\nsprite.graphics.begin_fill(color=ap.Color("#0af"))\n\n\nclass _ColorOptions(TypedDict):\n    color: str\n\n\ndef on_rectangle_click(e: ap.MouseEvent, options: _ColorOptions) -> None:\n    """\n    The handler that the rectangle calls when clicked.\n\n    Parameters\n    ----------\n    e : MouseEvent\n        Event instance.\n    options : dict\n        Optional arguments.\n    """\n    # Change the clicked rectangle color to the passed color.\n    rectangle: ap.Rectangle = e.this\n    color: ap.Color = ap.Color(options["color"])\n    rectangle.fill_color = color\n\n\nrectangle: ap.Rectangle = sprite.graphics.draw_rect(x=50, y=50, width=50, height=50)\noptions: _ColorOptions = {"color": "#f0a"}\nrectangle.click(handler=on_rectangle_click, options=options)\n\nap.save_overall_html(dest_dir_path="mouse_event_basic_basic_binding_usage/")\n```': '```py\n# runnable\nfrom typing_extensions import TypedDict\n\nimport apysc as ap\n\nap.Stage(\n    background_color=ap.Color("#333"),\n    stage_width=150,\n    stage_height=150,\n    stage_elem_id="stage",\n)\n\nsprite: ap.Sprite = ap.Sprite()\nsprite.graphics.begin_fill(color=ap.Color("#0af"))\n\n\nclass _ColorOptions(TypedDict):\n    color: str\n\n\ndef on_rectangle_click(e: ap.MouseEvent, options: _ColorOptions) -> None:\n    """\n    The handler that the rectangle calls when clicked.\n\n    Parameters\n    ----------\n    e : MouseEvent\n        Event instance.\n    options : dict\n        Optional arguments.\n    """\n    # Change the clicked rectangle color to the passed color.\n    rectangle: ap.Rectangle = e.this\n    color: ap.Color = ap.Color(options["color"])\n    rectangle.fill_color = color\n\n\nrectangle: ap.Rectangle = sprite.graphics.draw_rect(x=50, y=50, width=50, height=50)\noptions: _ColorOptions = {"color": "#f0a"}\nrectangle.click(handler=on_rectangle_click, options=options)\n\nap.save_overall_html(dest_dir_path="mouse_event_basic_basic_binding_usage/")\n```',  # noqa
    ##################################################
    "If you click the rectangle, the handler changes the rectangle color to the specified options color.": "四角をクリックした場合、ハンドラは四角の色をパラメーターに渡された色に変更します。",  # noqa
    ##################################################
    "There are many mouse events binding interfaces, such as the `click`\\, `mousedown`\\, `mouseup`\\, `mouseover`\\, `mouseout`\\, and `mousemove` that the `DisplayObject` instance has.": "`DisplayObject`の各インスタンスには`click`や`mousedown`、`mouseup`、`mouseover`、`mouseout`、`mousemove`などの様々なイベント設定用のインターフェイスがそっ歳します。",  # noqa
    ##################################################
    "## Basic unbinding usage": "## 基本的なイベント解除処理の使い方",
    ##################################################
    "Each `DisplayObject` instance has the `unbind_<event_name>` interfaces, for example, `unbind_click` or `unbind_mousedown` or something else.": "`DisplayObject`の各インスタンスは`unbind_click`や`unbind_mousedown`などの`unbind_<event_name>`という名前の形式のインターフェイスを持っています。",  # noqa
    ##################################################
    "These interfaces can unbind the single handler setting (remove binding setting).": "これらのインターフェイスではイベントハンドラの設定単体を解除することができます。",  # noqa
    ##################################################
    "For example, the following code unbinds the click event, so the interface doesn't call the handler function.": "例えば以下のコード例ではクリックイベントを解除しているため、ハンドラの関数は呼ばれなくなります。",  # noqa
    ##################################################
    '```py\n# runnable\nfrom typing_extensions import TypedDict\n\nimport apysc as ap\n\nap.Stage(\n    background_color=ap.Color("#333"),\n    stage_width=150,\n    stage_height=150,\n    stage_elem_id="stage",\n)\n\nsprite: ap.Sprite = ap.Sprite()\nsprite.graphics.begin_fill(color=ap.Color("#0af"))\n\n\nclass _ColorOptions(TypedDict):\n    color: str\n\n\ndef on_rectangle_click(e: ap.MouseEvent, options: _ColorOptions) -> None:\n    """\n    The handler that the rectangle calls when clicked.\n\n    Parameters\n    ----------\n    e : MouseEvent\n        Event instance.\n    options : dict\n        Optional arguments.\n    """\n    # Change the clicked rectangle color to the passed color.\n    rectangle: ap.Rectangle = e.this\n    color: ap.Color = ap.Color(options["color"])\n    rectangle.fill_color = color\n\n\nrectangle: ap.Rectangle = sprite.graphics.draw_rect(x=50, y=50, width=50, height=50)\noptions: _ColorOptions = {"color": "#f0a"}\nrectangle.click(handler=on_rectangle_click, options=options)\n\nrectangle.unbind_click(handler=on_rectangle_click)\n\nap.save_overall_html(dest_dir_path="mouse_event_basic_basic_unbinding_usage/")\n```': '```py\n# runnable\nfrom typing_extensions import TypedDict\n\nimport apysc as ap\n\nap.Stage(\n    background_color=ap.Color("#333"),\n    stage_width=150,\n    stage_height=150,\n    stage_elem_id="stage",\n)\n\nsprite: ap.Sprite = ap.Sprite()\nsprite.graphics.begin_fill(color=ap.Color("#0af"))\n\n\nclass _ColorOptions(TypedDict):\n    color: str\n\n\ndef on_rectangle_click(e: ap.MouseEvent, options: _ColorOptions) -> None:\n    """\n    The handler that the rectangle calls when clicked.\n\n    Parameters\n    ----------\n    e : MouseEvent\n        Event instance.\n    options : dict\n        Optional arguments.\n    """\n    # Change the clicked rectangle color to the passed color.\n    rectangle: ap.Rectangle = e.this\n    color: ap.Color = ap.Color(options["color"])\n    rectangle.fill_color = color\n\n\nrectangle: ap.Rectangle = sprite.graphics.draw_rect(x=50, y=50, width=50, height=50)\noptions: _ColorOptions = {"color": "#f0a"}\nrectangle.click(handler=on_rectangle_click, options=options)\n\nrectangle.unbind_click(handler=on_rectangle_click)\n\nap.save_overall_html(dest_dir_path="mouse_event_basic_basic_unbinding_usage/")\n```',  # noqa
    ##################################################
    "When you click the following rectangle, nothing happens.": "以下の四角をクリックしてみても何も起こらないことが確認できます。",  # noqa
    ##################################################
    "## Unbind all event handlers": "## 全てのイベントハンドラの設定を解除する",
    ##################################################
    "Sometimes, it is helpful to unbind specific all the events at once. For example, each event interface has the `unbind_<event_name>_all` method (e.g., `unbind_click_all`). It can unbind all event handlers from that instance.": "特定のイベントの設定を一括で解除するのが役立つ時があります。イベントが設定できる各インスタンスは`unbind_click_all`などの`unbind_<event_name>_all`という名前の形式のインターフェイスを持っており、それを使ってインスタンスから一通りのイベントのハンドラ設定を解除することができます。",  # noqa
    ##################################################
    "The following code calls the `unbind_click_all` method and removes all handler settings.": "以下のコード例では`unbind_click_all`メソッドを呼んで全てのクリックイベントのハンドラ設定を解除しています。",  # noqa
    ##################################################
    '```py\n# runnable\nfrom typing_extensions import TypedDict\n\nimport apysc as ap\n\nap.Stage(\n    background_color=ap.Color("#333"),\n    stage_width=150,\n    stage_height=150,\n    stage_elem_id="stage",\n)\n\nsprite: ap.Sprite = ap.Sprite()\nsprite.graphics.begin_fill(color=ap.Color("#0af"))\n\n\nclass _ColorOptions(TypedDict):\n    color: str\n\n\ndef change_color_on_rectangle_click(e: ap.MouseEvent, options: _ColorOptions) -> None:\n    """\n    The handler that the rectangle calls when clicked.\n\n    Parameters\n    ----------\n    e : MouseEvent\n        Event instance.\n    options : dict\n        Optional arguments.\n    """\n    rectangle: ap.Rectangle = e.this\n    color: ap.Color = ap.Color(options["color"])\n    rectangle.fill_color = color\n\n\ndef change_x_on_rectangle_click(e: ap.MouseEvent, options: dict) -> None:\n    """\n    The handler that the rectangle calls when clicked.\n\n    Parameters\n    ----------\n    e : MouseEvent\n        Event instance.\n    options : dict\n        Optional arguments.\n    """\n    rectangle: ap.Rectangle = e.this\n    rectangle.x += 50\n\n\nrectangle: ap.Rectangle = sprite.graphics.draw_rect(x=50, y=50, width=50, height=50)\noptions: _ColorOptions = {"color": "#f0a"}\nrectangle.click(handler=change_color_on_rectangle_click, options=options)\nrectangle.click(handler=change_x_on_rectangle_click)\n\nrectangle.unbind_click_all()\n\nap.save_overall_html(dest_dir_path="mouse_event_basic_unbind_all_event_handlers/")\n```': '```py\n# runnable\nfrom typing_extensions import TypedDict\n\nimport apysc as ap\n\nap.Stage(\n    background_color=ap.Color("#333"),\n    stage_width=150,\n    stage_height=150,\n    stage_elem_id="stage",\n)\n\nsprite: ap.Sprite = ap.Sprite()\nsprite.graphics.begin_fill(color=ap.Color("#0af"))\n\n\nclass _ColorOptions(TypedDict):\n    color: str\n\n\ndef change_color_on_rectangle_click(e: ap.MouseEvent, options: _ColorOptions) -> None:\n    """\n    The handler that the rectangle calls when clicked.\n\n    Parameters\n    ----------\n    e : MouseEvent\n        Event instance.\n    options : dict\n        Optional arguments.\n    """\n    rectangle: ap.Rectangle = e.this\n    color: ap.Color = ap.Color(options["color"])\n    rectangle.fill_color = color\n\n\ndef change_x_on_rectangle_click(e: ap.MouseEvent, options: dict) -> None:\n    """\n    The handler that the rectangle calls when clicked.\n\n    Parameters\n    ----------\n    e : MouseEvent\n        Event instance.\n    options : dict\n        Optional arguments.\n    """\n    rectangle: ap.Rectangle = e.this\n    rectangle.x += 50\n\n\nrectangle: ap.Rectangle = sprite.graphics.draw_rect(x=50, y=50, width=50, height=50)\noptions: _ColorOptions = {"color": "#f0a"}\nrectangle.click(handler=change_color_on_rectangle_click, options=options)\nrectangle.click(handler=change_x_on_rectangle_click)\n\nrectangle.unbind_click_all()\n\nap.save_overall_html(dest_dir_path="mouse_event_basic_unbind_all_event_handlers/")\n```',  # noqa
    ##################################################
    "Nothing happens when clicking the rectangle (no color change and no x-coordinate change).": "四角をクリックしてみても色の変化やX座標の更新などが発生しないことを確認できます。",  # noqa
    ##################################################
    "## Handler argument names and types": "## ハンドラの引数の名前と型",
    ##################################################
    "Handler function (or method) first argument requires the type of the `MouseEvent`\\.": "ハンドラの関数（もしくはメソッド）の第一引数は`MouseEvent`型の引数が必要になります。",  # noqa
    ##################################################
    "Also, a second argument name is required to be `options`\\. This argument type becomes `dict`\\. If you skip options argument specification at binding the event, then this argument becomes a blank dictionary (`{}`).": "また、第二引数には`options`という名前の辞書の引数が必要になります。イベント設定時にこのoptionsパラメーターの指定を省略した場合にはこの引数の値は空の辞書（`{}`）になります。",  # noqa
    ##################################################
    "## MouseEvent this attribute": "## MouseEvent クラスの this 属性",
    ##################################################
    "The `MouseEvent` instance has the `this` attribute, which becomes an event target instance. So, if you bind the click event to the rectangle instance, the `this` attribute becomes that rectangle instance.": "`MouseEvent`クラスのインスタンスはイベント登録対象のインスタンスとなる`this`属性を持っています。例えばクリックイベントを四角のインスタンスに設定した場合、`this`属性はその四角のインスタンスになります。",  # noqa
    ##################################################
    "## MouseEvent generic type settings": "## MouseEvent クラスのジェネリック型の設定",
    ##################################################
    "Suppose you know that you only use one of the handlers by an instance of a particular type. In that case, you can set generic type settings to the `MouseEvent` type annotation (e.g., `MouseEvent[Rectangle]`).": "もしもハンドラを特定の型のインスタンスのみで使うことが分かっている場合、`MouseEvent`の型アノテーションでジェネリックの型の指定を行うことができます（例: `MouseEvent[Rectangle]`）。",  # noqa
    ##################################################
    "This setting is helpful to determine the `this` attribute type, and the type-checking library, such as the `mypy` or `Pylance`\\, checks the instance type.": "この設定は`this`属性の型の決定に使われ、`mypy`や`Pylance`などの型チェックのライブラリを使っている場合役立つことがあります。",  # noqa
    ##################################################
    '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    background_color=ap.Color("#333"),\n    stage_width=200,\n    stage_height=150,\n    stage_elem_id="stage",\n)\n\nsprite: ap.Sprite = ap.Sprite()\nsprite.graphics.begin_fill(color=ap.Color("#0af"))\n\n\ndef on_rectangle_mousedown(e: ap.MouseEvent[ap.Rectangle], options: dict) -> None:\n    """\n    The handler that the rectangle calls when mousedown.\n\n    Parameters\n    ----------\n    e : MouseEvent\n        Event instance.\n    options : dict\n        Optional arguments.\n    """\n    rectangle = e.this\n    rectangle.x += 50\n\n\nrectangle: ap.Rectangle = sprite.graphics.draw_rect(x=50, y=50, width=50, height=50)\nrectangle.mousedown(handler=on_rectangle_mousedown)\n```': '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    background_color=ap.Color("#333"),\n    stage_width=200,\n    stage_height=150,\n    stage_elem_id="stage",\n)\n\nsprite: ap.Sprite = ap.Sprite()\nsprite.graphics.begin_fill(color=ap.Color("#0af"))\n\n\ndef on_rectangle_mousedown(e: ap.MouseEvent[ap.Rectangle], options: dict) -> None:\n    """\n    The handler that the rectangle calls when mousedown.\n\n    Parameters\n    ----------\n    e : MouseEvent\n        Event instance.\n    options : dict\n        Optional arguments.\n    """\n    rectangle = e.this\n    rectangle.x += 50\n\n\nrectangle: ap.Rectangle = sprite.graphics.draw_rect(x=50, y=50, width=50, height=50)\nrectangle.mousedown(handler=on_rectangle_mousedown)\n```',  # noqa
    ##################################################
    "## MouseEvent stage_x and stage_y attributes": "## MouseEvent クラスの stage_x と stage_y 属性",  # noqa
    ##################################################
    "MouseEvent instance has the `stage_x` and `stage_y` attributes. These attributes are absolute coordinates from the upper-left position of the stage.": "MouseEventクラスのインスタンスは`stage_x`や`stage_y`の各属性のインターフェイスを持っています。これらの属性はステージの左上の位置を基準とした絶対座標となります。",  # noqa
    ##################################################
    '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    background_color=ap.Color("#333"),\n    stage_width=150,\n    stage_height=200,\n    stage_elem_id="stage",\n)\n\nsprite: ap.Sprite = ap.Sprite()\nsprite.graphics.begin_fill(color=ap.Color("#0af"))\n\n\ndef on_mousemove(e: ap.MouseEvent[ap.Rectangle], options: dict) -> None:\n    """\n    The handler that the rectangle calls when mousemove.\n\n    Parameters\n    ----------\n    e : MouseEvent\n        Event instance.\n    options : dict\n        Optional arguments.\n    """\n    ap.trace("stage_x:", e.stage_x, "stage_y:", e.stage_y)\n\n\nrectangle: ap.Rectangle = sprite.graphics.draw_rect(x=50, y=100, width=50, height=50)\nrectangle.mousemove(handler=on_mousemove)\n\nap.save_overall_html(dest_dir_path="mouse_event_basic_stage_x_and_stage_y")\n```': '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    background_color=ap.Color("#333"),\n    stage_width=150,\n    stage_height=200,\n    stage_elem_id="stage",\n)\n\nsprite: ap.Sprite = ap.Sprite()\nsprite.graphics.begin_fill(color=ap.Color("#0af"))\n\n\ndef on_mousemove(e: ap.MouseEvent[ap.Rectangle], options: dict) -> None:\n    """\n    The handler that the rectangle calls when mousemove.\n\n    Parameters\n    ----------\n    e : MouseEvent\n        Event instance.\n    options : dict\n        Optional arguments.\n    """\n    ap.trace("stage_x:", e.stage_x, "stage_y:", e.stage_y)\n\n\nrectangle: ap.Rectangle = sprite.graphics.draw_rect(x=50, y=100, width=50, height=50)\nrectangle.mousemove(handler=on_mousemove)\n\nap.save_overall_html(dest_dir_path="mouse_event_basic_stage_x_and_stage_y")\n```',  # noqa
    ##################################################
    "If you open the DevTools console on Chrome (press F12) and move the mouse cursor on the following rectangle, you can check the `stage_x` and `stage_y` coordinates. The previous code positions the rectangle at `(50, 100)`, so the `stage_x` becomes the range of 50 to 100, and `stage_y` becomes 100 to 150.": "F12を押してChromeなどのDevToolsを開き、以下の四角の上でマウスカーソルを動かすと`stage_x`や`stage_y`の座標値を家訓することができます。前述のコードでは四角を`(50, 100)`の位置に設定しているため、`stage_x`の値は50～100の範囲の値となり、`stage_y`の値は100～150の範囲の値となります。",  # noqa
    ##################################################
    "## MouseEvent local_x and local_y attributes": "## MouseEvent クラスの local_x と local_y 属性",  # noqa
    ##################################################
    "MouseEvent instance also has `local_x` and `local_y` attributes. These attributes are the local coordinates from the event registered instance position.": "MouseEventのインスタンスは`local_x`と`local_y`という属性も持っています。これらの属性はイベントが登録されたインスタンスを基準とした相対座標となります。",  # noqa
    ##################################################
    "The following example shows that local_x and local_y become the coordinates in the rectangle area. Both of the `local_x` and `local_y` become a range of 0 to 50 because the rectangle size is 50-pixel.": "以下のコード例ではlocal_xとlocal_yの座標が四角の範囲の座標になっていることを確認できます。四角のサイズが50pxなため、`local_x`と`local_y`の値は両方とも0～50の範囲になります。",  # noqa
    ##################################################
    '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    background_color=ap.Color("#333"),\n    stage_width=150,\n    stage_height=150,\n    stage_elem_id="stage",\n)\n\nsprite: ap.Sprite = ap.Sprite()\nsprite.graphics.begin_fill(color=ap.Color("#0af"))\n\n\ndef on_mousemove(e: ap.MouseEvent[ap.Rectangle], options: dict) -> None:\n    """\n    The handler that the rectangle calls when mousemove.\n\n    Parameters\n    ----------\n    e : MouseEvent\n        Event instance.\n    options : dict\n        Optional arguments.\n    """\n    ap.trace("local_x:", e.local_x, "local_y:", e.local_y)\n\n\nrectangle: ap.Rectangle = sprite.graphics.draw_rect(x=50, y=50, width=50, height=50)\nrectangle.mousemove(handler=on_mousemove)\n\nap.save_overall_html(dest_dir_path="mouse_event_basic_local_x_and_local_y")\n```': '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    background_color=ap.Color("#333"),\n    stage_width=150,\n    stage_height=150,\n    stage_elem_id="stage",\n)\n\nsprite: ap.Sprite = ap.Sprite()\nsprite.graphics.begin_fill(color=ap.Color("#0af"))\n\n\ndef on_mousemove(e: ap.MouseEvent[ap.Rectangle], options: dict) -> None:\n    """\n    The handler that the rectangle calls when mousemove.\n\n    Parameters\n    ----------\n    e : MouseEvent\n        Event instance.\n    options : dict\n        Optional arguments.\n    """\n    ap.trace("local_x:", e.local_x, "local_y:", e.local_y)\n\n\nrectangle: ap.Rectangle = sprite.graphics.draw_rect(x=50, y=50, width=50, height=50)\nrectangle.mousemove(handler=on_mousemove)\n\nap.save_overall_html(dest_dir_path="mouse_event_basic_local_x_and_local_y")\n```',  # noqa
    ##################################################
    "Please check on Chrome DevTools (press F12) and move the mouse cursor on the following rectangle.": "F12を押してChromeなどのDevToolsを開き、以下の四角の上でマウスカーソルを動かしてみて出力結果を確認してみてください。",  # noqa
    ##################################################
    "## See also": "## 関連資料",
    ##################################################
    "- [click interface](click.md)": "- [click インターフェイス](jp_click.md)",
    ##################################################
    "- [mousedown and mouseup interfaces](mousedown_and_mouseup.md)": "- [mousedown と mouseup のインターフェイス](jp_mousedown_and_mouseup.md)",  # noqa
    ##################################################
    "- [mouseover and mouseout interfaces](mouseover_and_mouseout.md)": "- [mouseover と mouseout のインターフェイス](jp_mouseover_and_mouseout.md)",  # noqa
    ##################################################
    "- [mousemove interface](mousemove.md)": "- [mousemove インターフェイス](jp_mousemove.md)",
    ##################################################
    "## stage_x property API": "## stage_x 属性のAPI",
    ##################################################
    '<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>': '<span class="inconspicuous-txt">特記事項: このAPIドキュメントはドキュメントビルド用のスクリプトによって自動で生成・同期されています。そのためもしかしたらこの節の内容は前節までの内容と重複している場合があります。</span>',  # noqa
    ##################################################
    "**[Interface summary]**": "**[インターフェイス概要]**",
    ##################################################
    "Get the x-coordinate of the stage reference.<hr>": "ステージ基準のX座標を取得します。<hr>",
    ##################################################
    "**[Returns]**": "**[返却値]**",
    ##################################################
    "- `x`: Number": "- `x`: Number",
    ##################################################
    "  - x-coordinate.": "  - X座標。",
    ##################################################
    "<hr>": "<hr>",
    ##################################################
    "**[Examples]**": "**[コードサンプル]**",
    ##################################################
    '```py\n>>> import apysc as ap\n>>> def on_mousedown(e: ap.MouseEvent[ap.Rectangle], options: dict) -> None:\n...     stage_x: ap.Int = e.stage_x\n...     # Do something here with the coordinate.\n>>> stage: ap.Stage = ap.Stage()\n>>> sprite: ap.Sprite = ap.Sprite()\n>>> sprite.graphics.begin_fill(color=ap.Color("#0af"))\n>>> rectangle: ap.Rectangle = sprite.graphics.draw_rect(\n...     x=50, y=50, width=50, height=50\n... )\n>>> _ = rectangle.mousedown(on_mousedown)\n```': '```py\n>>> import apysc as ap\n>>> def on_mousedown(e: ap.MouseEvent[ap.Rectangle], options: dict) -> None:\n...     stage_x: ap.Int = e.stage_x\n...     # Do something here with the coordinate.\n>>> stage: ap.Stage = ap.Stage()\n>>> sprite: ap.Sprite = ap.Sprite()\n>>> sprite.graphics.begin_fill(color=ap.Color("#0af"))\n>>> rectangle: ap.Rectangle = sprite.graphics.draw_rect(\n...     x=50, y=50, width=50, height=50\n... )\n>>> _ = rectangle.mousedown(on_mousedown)\n```',  # noqa
    ##################################################
    "## stage_y property API": "## stage_y 属性のAPI",
    ##################################################
    '<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>': '<span class="inconspicuous-txt">特記事項: このAPIドキュメントはドキュメントビルド用のスクリプトによって自動で生成・同期されています。そのためもしかしたらこの節の内容は前節までの内容と重複している場合があります。</span>',  # noqa
    ##################################################
    "**[Interface summary]**": "**[インターフェイス概要]**",
    ##################################################
    "Get the y-coordinate of the stage reference.<hr>": "ステージ基準のY座標を取得します。<hr>",
    ##################################################
    "**[Returns]**": "**[返却値]**",
    ##################################################
    "- `y`: Number": "- `y`: Number",
    ##################################################
    "  - y-coordinate.": "  - Y座標。",
    ##################################################
    "<hr>": "<hr>",
    ##################################################
    "**[Examples]**": "**[コードサンプル]**",
    ##################################################
    '```py\n>>> import apysc as ap\n>>> def on_mousedown(e: ap.MouseEvent[ap.Rectangle], options: dict) -> None:\n...     stage_y: ap.Number = e.stage_y\n...     # Do something here with the coordinate.\n>>> stage: ap.Stage = ap.Stage()\n>>> sprite: ap.Sprite = ap.Sprite()\n>>> sprite.graphics.begin_fill(color=ap.Color("#0af"))\n>>> rectangle: ap.Rectangle = sprite.graphics.draw_rect(\n...     x=50, y=50, width=50, height=50\n... )\n>>> _ = rectangle.mousedown(on_mousedown)\n```': '```py\n>>> import apysc as ap\n>>> def on_mousedown(e: ap.MouseEvent[ap.Rectangle], options: dict) -> None:\n...     stage_y: ap.Number = e.stage_y\n...     # Do something here with the coordinate.\n>>> stage: ap.Stage = ap.Stage()\n>>> sprite: ap.Sprite = ap.Sprite()\n>>> sprite.graphics.begin_fill(color=ap.Color("#0af"))\n>>> rectangle: ap.Rectangle = sprite.graphics.draw_rect(\n...     x=50, y=50, width=50, height=50\n... )\n>>> _ = rectangle.mousedown(on_mousedown)\n```',  # noqa
    ##################################################
    "## local_x property API": "## local_x 属性のAPI",
    ##################################################
    '<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>': '<span class="inconspicuous-txt">特記事項: このAPIドキュメントはドキュメントビルド用のスクリプトによって自動で生成・同期されています。そのためもしかしたらこの節の内容は前節までの内容と重複している場合があります。</span>',  # noqa
    ##################################################
    "**[Interface summary]**": "**[インターフェイス概要]**",
    ##################################################
    "Get a local x-coordinate event listening instance. For example, this value becomes x-coordinate from Sprite's left-end position by clicking a Sprite instance.<hr>": "イベントが設定されているインスタンス内の相対座標のX座標を取得します。例えばSpriteのインスタンスをクリックした場合にはSpriteの左上の位置を基準とした座標になります。<hr>",  # noqa
    ##################################################
    "**[Returns]**": "**[返却値]**",
    ##################################################
    "- `x`: Number": "- `x`: Number",
    ##################################################
    "  - x-coordinate.": "  - X座標。",
    ##################################################
    "<hr>": "<hr>",
    ##################################################
    "**[Examples]**": "**[コードサンプル]**",
    ##################################################
    '```py\n>>> import apysc as ap\n>>> def on_mousedown(e: ap.MouseEvent[ap.Rectangle], options: dict) -> None:\n...     local_x: ap.Number = e.local_x\n...     # Do something here with the coordinate.\n>>> stage: ap.Stage = ap.Stage()\n>>> sprite: ap.Sprite = ap.Sprite()\n>>> sprite.graphics.begin_fill(color=ap.Color("#0af"))\n>>> rectangle: ap.Rectangle = sprite.graphics.draw_rect(\n...     x=50, y=50, width=50, height=50\n... )\n>>> _ = rectangle.mousedown(on_mousedown)\n```': '```py\n>>> import apysc as ap\n>>> def on_mousedown(e: ap.MouseEvent[ap.Rectangle], options: dict) -> None:\n...     local_x: ap.Number = e.local_x\n...     # Do something here with the coordinate.\n>>> stage: ap.Stage = ap.Stage()\n>>> sprite: ap.Sprite = ap.Sprite()\n>>> sprite.graphics.begin_fill(color=ap.Color("#0af"))\n>>> rectangle: ap.Rectangle = sprite.graphics.draw_rect(\n...     x=50, y=50, width=50, height=50\n... )\n>>> _ = rectangle.mousedown(on_mousedown)\n```',  # noqa
    ##################################################
    "## local_y property API": "## local_y 属性のAPI",
    ##################################################
    '<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>': '<span class="inconspicuous-txt">特記事項: このAPIドキュメントはドキュメントビルド用のスクリプトによって自動で生成・同期されています。そのためもしかしたらこの節の内容は前節までの内容と重複している場合があります。</span>',  # noqa
    ##################################################
    "**[Interface summary]**": "**[インターフェイス概要]**",
    ##################################################
    "Get the local y-coordinate of the event listening instance. For example, this value becomes y-coordinate from Sprite's top-end position by clicking a Sprite instance.<hr>": "イベントが設定されているインスタンスないの相対座標のY座標を取得します。例えばSpriteのインスタンスをクリックした場合にはSpriteの左上の位置を基準とした座標になります。<hr>",  # noqa
    ##################################################
    "**[Returns]**": "**[返却値]**",
    ##################################################
    "- `y`: Number": "- `y`: Number",
    ##################################################
    "  - y-coordinate.": "  - Y座標。",
    ##################################################
    "<hr>": "<hr>",
    ##################################################
    "**[Examples]**": "**[コードサンプル]**",
    ##################################################
    '```py\n>>> import apysc as ap\n>>> def on_mousedown(e: ap.MouseEvent[ap.Rectangle], options: dict) -> None:\n...     local_y: ap.Number = e.local_y\n...     # Do something here with the coordinate.\n>>> stage: ap.Stage = ap.Stage()\n>>> sprite: ap.Sprite = ap.Sprite()\n>>> sprite.graphics.begin_fill(color=ap.Color("#0af"))\n>>> rectangle: ap.Rectangle = sprite.graphics.draw_rect(\n...     x=50, y=50, width=50, height=50\n... )\n>>> _ = rectangle.mousedown(on_mousedown)\n```': '```py\n>>> import apysc as ap\n>>> def on_mousedown(e: ap.MouseEvent[ap.Rectangle], options: dict) -> None:\n...     local_y: ap.Number = e.local_y\n...     # Do something here with the coordinate.\n>>> stage: ap.Stage = ap.Stage()\n>>> sprite: ap.Sprite = ap.Sprite()\n>>> sprite.graphics.begin_fill(color=ap.Color("#0af"))\n>>> rectangle: ap.Rectangle = sprite.graphics.draw_rect(\n...     x=50, y=50, width=50, height=50\n... )\n>>> _ = rectangle.mousedown(on_mousedown)\n```',  # noqa
    ##################################################
    "## this property API": "## this 属性のAPI",
    ##################################################
    '<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>': '<span class="inconspicuous-txt">特記事項: このAPIドキュメントはドキュメントビルド用のスクリプトによって自動で生成・同期されています。そのためもしかしたらこの節の内容は前節までの内容と重複している場合があります。</span>',  # noqa
    ##################################################
    "**[Interface summary]**": "**[インターフェイス概要]**",
    ##################################################
    "Get an instance of listening to this event.<hr>": "このイベントが設定されているインスタンスを取得します。<hr>",  # noqa
    ##################################################
    "**[Returns]**": "**[返却値]**",
    ##################################################
    "- `this`: VariableNameMixIn": "- `this`: VariableNameMixIn",
    ##################################################
    "  - Instance that listening this event.": "  - このイベントが設定されているインスタンス。",
    ##################################################
    "<hr>": "<hr>",
    ##################################################
    "**[Examples]**": "**[コードサンプル]**",
    ##################################################
    '```py\n>>> import apysc as ap\n>>> def on_custom_event(e: ap.Event[ap.Rectangle], options: dict) -> None:\n...     rectangle: ap.Rectangle = e.this\n...     rectangle.fill_color = ap.Color("#f0a")\n>>> stage: ap.Stage = ap.Stage()\n>>> sprite: ap.Sprite = ap.Sprite()\n>>> sprite.graphics.begin_fill(color=ap.Color("#0af"))\n>>> rectangle: ap.Rectangle = sprite.graphics.draw_rect(\n...     x=50, y=50, width=50, height=50\n... )\n>>> e: ap.Event = ap.Event(this=rectangle)\n>>> _ = rectangle.bind_custom_event(\n...     custom_event_type="my_custom_event", handler=on_custom_event, e=e\n... )\n>>> # Do something here and then trigger the custom event\n>>> rectangle.trigger_custom_event(custom_event_type="my_custom_event")\n```': '```py\n>>> import apysc as ap\n>>> def on_custom_event(e: ap.Event[ap.Rectangle], options: dict) -> None:\n...     rectangle: ap.Rectangle = e.this\n...     rectangle.fill_color = ap.Color("#f0a")\n>>> stage: ap.Stage = ap.Stage()\n>>> sprite: ap.Sprite = ap.Sprite()\n>>> sprite.graphics.begin_fill(color=ap.Color("#0af"))\n>>> rectangle: ap.Rectangle = sprite.graphics.draw_rect(\n...     x=50, y=50, width=50, height=50\n... )\n>>> e: ap.Event = ap.Event(this=rectangle)\n>>> _ = rectangle.bind_custom_event(\n...     custom_event_type="my_custom_event", handler=on_custom_event, e=e\n... )\n>>> # Do something here and then trigger the custom event\n>>> rectangle.trigger_custom_event(custom_event_type="my_custom_event")\n```',  # noqa
}
