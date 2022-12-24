"""This module is for the translation mapping data of the
following document:

Document file: graphics_draw_rect.md
Language: jp
"""

from typing import Dict

MAPPING: Dict[str, str] = {
    ##################################################
    "# Graphics draw_rect interface": "# Graphics クラスの draw_rect インターフェイス",
    ##################################################
    "This page explains the `Graphics` class `draw_rect` method interface.": "このページでは`Graphics`クラスの`draw_rect`メソッドのインターフェイスについて説明します。",  # noqa
    ##################################################
    "## What interface is this?": "## インターフェイス概要",
    ##################################################
    "`draw_rect` interface draws vector rectangle graphics.": "`draw_rect`インターフェイスは四角のベクターグラフィックスを描画します。",  # noqa
    ##################################################
    "## Basic usage": "## 基本的な使い方",
    ##################################################
    "`draw_rect` interface has `x`, `y`, `width`, and `height` arguments. `x` and `y` are rectangle coordinates settings, and `width` and `height` will determine rectangle size.": "`draw_rect`インターフェイスは`x`、`y`、`width`、`height`の各引数を持っています。`x`と`y`は四角の座標を設定し、`width`と`height`は四角のサイズを決定します。",  # noqa
    ##################################################
    '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    background_color="#333", stage_width=200, stage_height=150, stage_elem_id="stage"\n)\nsprite: ap.Sprite = ap.Sprite()\nsprite.graphics.begin_fill(color="#0af")\nsprite.graphics.draw_rect(x=50, y=50, width=100, height=50)\n\nap.save_overall_html(dest_dir_path="graphics_draw_rect_basic_usage/")\n```': '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    background_color="#333", stage_width=200, stage_height=150, stage_elem_id="stage"\n)\nsprite: ap.Sprite = ap.Sprite()\nsprite.graphics.begin_fill(color="#0af")\nsprite.graphics.draw_rect(x=50, y=50, width=100, height=50)\n\nap.save_overall_html(dest_dir_path="graphics_draw_rect_basic_usage/")\n```',  # noqa
    ##################################################
    "The previous script draws horizontal rectangle graphics.": "前述のコードでは横長の四角を描画しています。",  # noqa
    ##################################################
    "Notes: `begin_fill` call (fill color setting) is necessary before `draw_rect` interface call. If you skip it, it displays nothing on stage.": "特記事項: `draw_rect`のインターフェイスを呼ぶ前に`begin_fill`メソッド（塗りの設定のインターフェイス）を呼んでおく必要があります。もし`begin_fill`の呼び出しがされていない場合画面上に四角が表示されません。",  # noqa
    ##################################################
    '```py\n# runnable\nimport apysc as ap\n\nstage: ap.Stage = ap.Stage(\n    background_color="#333", stage_width=200, stage_height=150, stage_elem_id="stage"\n)\nsprite: ap.Sprite = ap.Sprite()\nsprite.graphics.draw_rect(x=50, y=50, width=100, height=50)\n\nap.save_overall_html(dest_dir_path="graphics_draw_rect_basic_usage_skipped_begin_fill/")\n```': '```py\n# runnable\nimport apysc as ap\n\nstage: ap.Stage = ap.Stage(\n    background_color="#333", stage_width=200, stage_height=150, stage_elem_id="stage"\n)\nsprite: ap.Sprite = ap.Sprite()\nsprite.graphics.draw_rect(x=50, y=50, width=100, height=50)\n\nap.save_overall_html(dest_dir_path="graphics_draw_rect_basic_usage_skipped_begin_fill/")\n```',  # noqa
    ##################################################
    "## Rectangle instance": "## Rectangle インスタンス",
    ##################################################
    "`draw_rect` interface will return `Rectangle` instance. You can update each setting or bind events.": "`draw_rect`インターフェイスは`Rectangle`クラスのインスタンスを変逆します。そのインスタンスに対して各属性の更新やイベントハンドラの登録などを行うことができます。",  # noqa
    ##################################################
    "For instance, the following script sets the mouse event to `Rectangle` and updates the x position in the handler (`on_click`).": "例えば以下のコードでは`Rectangle`のインスタンスに対してクリックのマウスイベントを登録し、`on_click`のハンドラ内でX座標を更新しています。",  # noqa
    ##################################################
    '```py\n# runnable\nimport apysc as ap\n\n\ndef on_click(e: ap.MouseEvent[ap.Rectangle], options: dict) -> None:\n    """\n    The handler that the rectangle calls when clicked.\n\n    Parameters\n    ----------\n    e : MouseEvent\n        Created event instance.\n    options : dict\n        Optional arguments.\n    """\n    rectangle: ap.Rectangle = e.this\n    rectangle.x = ap.Int(100)\n\n\nap.Stage(\n    background_color="#333", stage_width=200, stage_height=150, stage_elem_id="stage"\n)\nsprite: ap.Sprite = ap.Sprite()\n\nsprite.graphics.begin_fill(color="#0af")\nrectangle: ap.Rectangle = sprite.graphics.draw_rect(x=50, y=50, width=50, height=50)\nrectangle.click(on_click)\n\nap.save_overall_html(dest_dir_path="graphics_draw_rect_rectangle/")\n```': '```py\n# runnable\nimport apysc as ap\n\n\ndef on_click(e: ap.MouseEvent[ap.Rectangle], options: dict) -> None:\n    """\n    The handler that the rectangle calls when clicked.\n\n    Parameters\n    ----------\n    e : MouseEvent\n        Created event instance.\n    options : dict\n        Optional arguments.\n    """\n    rectangle: ap.Rectangle = e.this\n    rectangle.x = ap.Int(100)\n\n\nap.Stage(\n    background_color="#333", stage_width=200, stage_height=150, stage_elem_id="stage"\n)\nsprite: ap.Sprite = ap.Sprite()\n\nsprite.graphics.begin_fill(color="#0af")\nrectangle: ap.Rectangle = sprite.graphics.draw_rect(x=50, y=50, width=50, height=50)\nrectangle.click(on_click)\n\nap.save_overall_html(dest_dir_path="graphics_draw_rect_rectangle/")\n```',  # noqa
    ##################################################
    "If you click rectangle, the handler changes the x position to 100.": "四角をクリックしてみると、ハンドラはX座標を100pxの位置に変更します。",  # noqa
    ##################################################
    "## draw_rect API": "## draw_rect API",
    ##################################################
    '<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>': '<span class="inconspicuous-txt">特記事項: このAPIドキュメントはドキュメントビルド用のスクリプトによって自動で生成・同期されています。そのためもしかしたらこの節の内容は前節までの内容と重複している場合があります。</span>',  # noqa
    ##################################################
    "**[Interface summary]**": "**[インターフェイス概要]**",
    ##################################################
    "Draw a rectangle vector graphics.<hr>": "ベクターグラフィックスの四角を描画します。<hr>",
    ##################################################
    "**[Parameters]**": "**[引数]**",
    ##################################################
    "- `x`: Int or int": "- `x`: Int or int",
    ##################################################
    "  - X position to start drawing.": "  - 描画を開始する位置のX座標。",
    ##################################################
    "- `y`: Int or int": "- `y`: Int or int",
    ##################################################
    "  - Y position to start drawing.": "  - 描画を開始する位置のY座標。",
    ##################################################
    "- `width`: Int or int": "- `width`: Int or int",
    ##################################################
    "  - Rectangle width.": "  - 四角の幅。",
    ##################################################
    "- `height`: Int or int": "- `height`: Int or int",
    ##################################################
    "  - Rectangle height.": "  - 四角の高さ。",
    ##################################################
    "- `variable_name_suffix`: str, default ''": "- `variable_name_suffix`: str, default ''",  # noqa
    ##################################################
    "  - A JavaScript variable name suffix string. This setting is sometimes useful for JavaScript's debugging.": "  - JavaScript上の変数のサフィックスの設定です。この設定はJavaScriptのデバッグ時に役立つことがあります。",  # noqa
    ##################################################
    "<hr>": "<hr>",
    ##################################################
    "**[Returns]**": "**[返却値]**",
    ##################################################
    "- `rectangle`: Rectangle": "- `rectangle`: Rectangle",
    ##################################################
    "  - Created rectangle.": "  - 生成された四角。",
    ##################################################
    "<hr>": "<hr>",
    ##################################################
    "**[Examples]**": "**[コードサンプル]**",
    ##################################################
    "```py\n>>> import apysc as ap\n>>> stage: ap.Stage = ap.Stage()\n>>> sprite: ap.Sprite = ap.Sprite()\n>>> sprite.graphics.begin_fill(color=\"#0af\")\n>>> rectangle: ap.Rectangle = sprite.graphics.draw_rect(\n...     x=50, y=50, width=50, height=50\n... )\n>>> rectangle.x\nInt(50)\n\n>>> rectangle.width\nInt(50)\n\n>>> rectangle.fill_color\nString('#00aaff')\n```": "```py\n>>> import apysc as ap\n>>> stage: ap.Stage = ap.Stage()\n>>> sprite: ap.Sprite = ap.Sprite()\n>>> sprite.graphics.begin_fill(color=\"#0af\")\n>>> rectangle: ap.Rectangle = sprite.graphics.draw_rect(\n...     x=50, y=50, width=50, height=50\n... )\n>>> rectangle.x\nInt(50)\n\n>>> rectangle.width\nInt(50)\n\n>>> rectangle.fill_color\nString('#00aaff')\n```",  # noqa
}
