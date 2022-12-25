"""This module is for the translation mapping data of the
following document:

Document file: event_prevent_default_and_stop_propagation.md
Language: jp
"""

from typing import Dict

MAPPING: Dict[str, str] = {
    ##################################################
    "# Event class prevent_default and stop_propagation interfaces": "# Event クラスの prevent_default と stop_propagation のインターフェイス",  # noqa
    ##################################################
    "This page explains the `Event` class `prevent_default` and `stop_propagation` method interfaces.": "このページでは`Event`クラスの`prevent_default`と`stop_propagation`メソッドの各インターフェイスについて説明します。",  # noqa
    ##################################################
    "## What interfaces are these?": "## 各インターフェイスの概要",
    ##################################################
    "The `prevent_default` method interface appends the calling expression of the JavaScript `preventDefault` method. This interface prevents the browser's default behavior of any event.": "`prevent_default`メソッドのインターフェイスはJavaScriptの`preventDefault`メソッドに該当するコード表現を加えます。このインターフェイスはイベントにおけるブラウザのデフォルトの挙動を無効化します。",  # noqa
    ##################################################
    "The `stop_propagation` method interface stops an event's propagation; for example, the triggered child event does not propagate to a parent event (it ignores the parent event).": "`stop_propagation`メソッドのインターフェイスはイベントの伝搬を停止します。例えば、このインスタンス上で実行（発火）されたイベントは親のインスタンスへは伝搬しなくなります（親のイベントは無視されるようになります）。",  # noqa
    ##################################################
    "## Basic usage of the prevent_default interface": "## prevent_default インターフェイスの基本的な使い方",  # noqa
    ##################################################
    "The `Event`'s subclass instance has the `prevent_default` method (note: there is a subclass that does not have this interface). The `prevent_default` method requires no arguments, as follows:": "`Event`のサブクラスのインスタンスは`prevent_default`メソッドを持っています（注: このインターフェイスを持っていないサブクラスも存在します）。`prevent_default`メソッドは特に引数を必要としません。",  # noqa
    ##################################################
    '```py\n# runnable\nimport apysc as ap\n\n\ndef on_click(e: ap.MouseEvent[ap.Rectangle], options: dict) -> None:\n    """\n    The handler that the rectangle calls when clicked.\n\n    Parameters\n    ----------\n    e : ap.MouseEvent\n        Event instance.\n    options : dict\n        Optional arguments dictionary.\n    """\n    e.prevent_default()\n\n\nap.Stage(\n    stage_width=150, stage_height=150, background_color="#333", stage_elem_id="stage"\n)\nsprite: ap.Sprite = ap.Sprite()\nsprite.graphics.begin_fill(color="#0af")\nrectangle: ap.Rectangle = sprite.graphics.draw_rect(x=50, y=50, width=50, height=50)\nrectangle.click(on_click)\n\nap.save_overall_html(dest_dir_path="event_prevent_default_basic_usage/")\n```': '```py\n# runnable\nimport apysc as ap\n\n\ndef on_click(e: ap.MouseEvent[ap.Rectangle], options: dict) -> None:\n    """\n    The handler that the rectangle calls when clicked.\n\n    Parameters\n    ----------\n    e : ap.MouseEvent\n        Event instance.\n    options : dict\n        Optional arguments dictionary.\n    """\n    e.prevent_default()\n\n\nap.Stage(\n    stage_width=150, stage_height=150, background_color="#333", stage_elem_id="stage"\n)\nsprite: ap.Sprite = ap.Sprite()\nsprite.graphics.begin_fill(color="#0af")\nrectangle: ap.Rectangle = sprite.graphics.draw_rect(x=50, y=50, width=50, height=50)\nrectangle.click(on_click)\n\nap.save_overall_html(dest_dir_path="event_prevent_default_basic_usage/")\n```',  # noqa
    ##################################################
    "## Basic usage of the stop_propagation interface": "## stop_propagation インターフェイスの基本的な使い方",  # noqa
    ##################################################
    "The `Event`'s subclass instance has the `stop_propagation` method (note: there is a subclass that does not have this method). The `stop_propagation` method, like the `prevent_default` one, requires no arguments.": "`Event`のサブクラスのインスタンスは`stop_propagation`メソッドを持っています（注: このメソッドを持っていないサブクラスも存在します）。`stop_propagation`メソッドは`prevent_default`メソッドと同様に引数を必要としません。",  # noqa
    ##################################################
    "The following example binds the click event to the sprite and rectangle instances. The rectangle (child) click handler calls the `stop_propagation` method, so the sprite (parent) doesn't call the click handler:": "以下のコード例ではクリックイベントをSpriteの親のインスタンスと四角の子のインスタンスにそれぞれ設定しています。四角の子のインスタンスのクリックのハンドラでは`stop_propagation`メソッドを読んでいるため、親のSpriteのハンドラは呼ばれません（イベントが伝搬しません）。",  # noqa
    ##################################################
    '```py\n# runnable\nimport apysc as ap\n\n\ndef on_rectangle_click(e: ap.MouseEvent[ap.Rectangle], options: dict) -> None:\n    """\n    The handler that the rectangle calls when clicked.\n\n    Parameters\n    ----------\n    e : ap.MouseEvent\n        Event instance.\n    options : dict\n        Optional arguments dictionary.\n    """\n    e.stop_propagation()\n    ap.trace("The rectangle is clicked!")\n\n\ndef on_sprite_click(e: ap.MouseEvent[ap.Sprite], options: dict) -> None:\n    """\n    The handler that the sprite calls when clicked.\n\n    Parameters\n    ----------\n    e : ap.MouseEvent\n        Event instance.\n    options : dict\n        Optional arguments dictionary.\n    """\n    ap.trace("The sprite is clicked!")\n\n\nap.Stage(\n    stage_width=150, stage_height=150, background_color="#333", stage_elem_id="stage"\n)\nsprite: ap.Sprite = ap.Sprite()\nsprite.click(on_sprite_click)\nsprite.graphics.begin_fill(color="#0af")\nrectangle: ap.Rectangle = sprite.graphics.draw_rect(x=50, y=50, width=50, height=50)\nrectangle.click(on_rectangle_click)\n\nap.save_overall_html(dest_dir_path="event_stop_propagation_basic_usage/")\n```': '```py\n# runnable\nimport apysc as ap\n\n\ndef on_rectangle_click(e: ap.MouseEvent[ap.Rectangle], options: dict) -> None:\n    """\n    The handler that the rectangle calls when clicked.\n\n    Parameters\n    ----------\n    e : ap.MouseEvent\n        Event instance.\n    options : dict\n        Optional arguments dictionary.\n    """\n    e.stop_propagation()\n    ap.trace("The rectangle is clicked!")\n\n\ndef on_sprite_click(e: ap.MouseEvent[ap.Sprite], options: dict) -> None:\n    """\n    The handler that the sprite calls when clicked.\n\n    Parameters\n    ----------\n    e : ap.MouseEvent\n        Event instance.\n    options : dict\n        Optional arguments dictionary.\n    """\n    ap.trace("The sprite is clicked!")\n\n\nap.Stage(\n    stage_width=150, stage_height=150, background_color="#333", stage_elem_id="stage"\n)\nsprite: ap.Sprite = ap.Sprite()\nsprite.click(on_sprite_click)\nsprite.graphics.begin_fill(color="#0af")\nrectangle: ap.Rectangle = sprite.graphics.draw_rect(x=50, y=50, width=50, height=50)\nrectangle.click(on_rectangle_click)\n\nap.save_overall_html(dest_dir_path="event_stop_propagation_basic_usage/")\n```',  # noqa
    ##################################################
    "If you click the following rectangle, the only message of `The rectangle is clicked!` is displayed browser console (please press the F12 key). Also, the sprite console message is not displayed.": "もし以下の四角をクリックした場合、ブラウザのコンソールには`The rectangle is clicked!`というメッセージのみが表示され、Sprite関係のメッセージは表示されません。",  # noqa
    ##################################################
    "## prevent_default API": "## prevent_default API",
    ##################################################
    '<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>': '<span class="inconspicuous-txt">特記事項: このAPIドキュメントはドキュメントビルド用のスクリプトによって自動で生成・同期されています。そのためもしかしたらこの節の内容は前節までの内容と重複している場合があります。</span>',  # noqa
    ##################################################
    "**[Interface summary]**": "**[インターフェイス概要]**",
    ##################################################
    "Prevent event's default behavior.<hr>": "イベントのデフォルトの挙動を無効化します。<hr>",
    ##################################################
    "**[Examples]**": "**[コードサンプル]**",
    ##################################################
    '```py\n>>> import apysc as ap\n>>> def on_click(e: ap.MouseEvent[ap.Rectangle], options: dict) -> None:\n...     e.prevent_default()\n...     rectangle: ap.Rectangle = e.this\n...     rectangle.fill_color = ap.String("#f0a")\n...     rectangle.unbind_mouseup_all()\n>>> stage: ap.Stage = ap.Stage()\n>>> sprite: ap.Sprite = ap.Sprite()\n>>> sprite.graphics.begin_fill(color="#0af")\n>>> rectangle: ap.Rectangle = sprite.graphics.draw_rect(\n...     x=50, y=50, width=50, height=50\n... )\n>>> _ = rectangle.click(on_click)\n```': '```py\n>>> import apysc as ap\n>>> def on_click(e: ap.MouseEvent[ap.Rectangle], options: dict) -> None:\n...     e.prevent_default()\n...     rectangle: ap.Rectangle = e.this\n...     rectangle.fill_color = ap.String("#f0a")\n...     rectangle.unbind_mouseup_all()\n>>> stage: ap.Stage = ap.Stage()\n>>> sprite: ap.Sprite = ap.Sprite()\n>>> sprite.graphics.begin_fill(color="#0af")\n>>> rectangle: ap.Rectangle = sprite.graphics.draw_rect(\n...     x=50, y=50, width=50, height=50\n... )\n>>> _ = rectangle.click(on_click)\n```',  # noqa
    ##################################################
    "## stop_propagation API": "## stop_propagation API",
    ##################################################
    '<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>': '<span class="inconspicuous-txt">特記事項: このAPIドキュメントはドキュメントビルド用のスクリプトによって自動で生成・同期されています。そのためもしかしたらこの節の内容は前節までの内容と重複している場合があります。</span>',  # noqa
    ##################################################
    "**[Interface summary]**": "**[インターフェイス概要]**",
    ##################################################
    "Stop an event propagation.<hr>": "イベントの伝搬を停止させます。<hr>",
    ##################################################
    "**[Examples]**": "**[コードサンプル]**",
    ##################################################
    '```py\n>>> import apysc as ap\n>>> def on_click(e: ap.MouseEvent, options: dict) -> None:\n...     e.stop_propagation()\n...     ap.trace("Clicked!")\n>>> stage: ap.Stage = ap.Stage()\n>>> sprite: ap.Sprite = ap.Sprite()\n>>> sprite.graphics.begin_fill(color="#0af")\n>>> rectangle: ap.Rectangle = sprite.graphics.draw_rect(\n...     x=50, y=50, width=50, height=50\n... )\n>>> _ = sprite.click(on_click)\n>>> _ = rectangle.click(on_click)\n```': '```py\n>>> import apysc as ap\n>>> def on_click(e: ap.MouseEvent, options: dict) -> None:\n...     e.stop_propagation()\n...     ap.trace("Clicked!")\n>>> stage: ap.Stage = ap.Stage()\n>>> sprite: ap.Sprite = ap.Sprite()\n>>> sprite.graphics.begin_fill(color="#0af")\n>>> rectangle: ap.Rectangle = sprite.graphics.draw_rect(\n...     x=50, y=50, width=50, height=50\n... )\n>>> _ = sprite.click(on_click)\n>>> _ = rectangle.click(on_click)\n```',  # noqa
}
