"""This module is for the translation mapping data of the
following document:

Document file: graphics_draw_round_rect.md
Language: jp
"""

from typing import Dict

MAPPING: Dict[str, str] = {
    ##################################################
    "# Graphics draw_round_rect interface": "# Graphics クラスの draw_round_rect インターフェイス",
    ##################################################
    "This page explains the `Graphics` class `draw_round_rect` method interface.": "このページでは`Graphics`クラスの`draw_round_rect`メソッドのインターフェイスについて説明します。",  # noqa
    ##################################################
    "## What interface is this?": "## インターフェイス概要",
    ##################################################
    "`draw_round_rect` interface draws vector rounded rectangle graphics.": "`draw_round_rect`インターフェイスは角丸の四角のベクターグラフィックスを描画します。",  # noqa
    ##################################################
    "## Basic usage": "## 基本的な使い方",
    ##################################################
    "`draw_round_rect` interface has `x`, `y`, `width`, and `height` arguments. `x` and `y` are rectangle coordinates settings, and `width` and `height` will determine rectangle size.": "`draw_round_rect`インターフェイスは`x`、`y`、`width`、`height`などの各引数を持っています。`x`と`y`引数は四角の座標を設定し、`width`と`height`は四角のサイズを決定します。",  # noqa
    ##################################################
    "This interface also has `ellipse_width` and `ellipse_height` arguments to set the round size to the rectangle corners.": "このインターフェイスはさらに角丸のサイズを設定するための`ellipse_width`と`ellipse_height`の引数を持っています。",  # noqa
    ##################################################
    '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    background_color="#333", stage_width=350, stage_height=150, stage_elem_id="stage"\n)\n\nsprite: ap.Sprite = ap.Sprite()\nsprite.graphics.begin_fill(color="#0af")\n\n# Set 10-pixel ellipse size and draw the rectangle.\nsprite.graphics.draw_round_rect(\n    x=50, y=50, width=50, height=50, ellipse_width=10, ellipse_height=10\n)\n\n# Set 20-pixel ellipse size and draw the rectangle.\nsprite.graphics.draw_round_rect(\n    x=150, y=50, width=50, height=50, ellipse_width=20, ellipse_height=20\n)\n\n# Set 5-pixel ellipse width and 20-pixel ellipse height and\n# draw the rectangle.\nsprite.graphics.draw_round_rect(\n    x=250, y=50, width=50, height=50, ellipse_width=5, ellipse_height=20\n)\n\nap.save_overall_html(dest_dir_path="graphics_draw_round_rect_basic_usage/")\n```': '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    background_color="#333", stage_width=350, stage_height=150, stage_elem_id="stage"\n)\n\nsprite: ap.Sprite = ap.Sprite()\nsprite.graphics.begin_fill(color="#0af")\n\n# Set 10-pixel ellipse size and draw the rectangle.\nsprite.graphics.draw_round_rect(\n    x=50, y=50, width=50, height=50, ellipse_width=10, ellipse_height=10\n)\n\n# Set 20-pixel ellipse size and draw the rectangle.\nsprite.graphics.draw_round_rect(\n    x=150, y=50, width=50, height=50, ellipse_width=20, ellipse_height=20\n)\n\n# Set 5-pixel ellipse width and 20-pixel ellipse height and\n# draw the rectangle.\nsprite.graphics.draw_round_rect(\n    x=250, y=50, width=50, height=50, ellipse_width=5, ellipse_height=20\n)\n\nap.save_overall_html(dest_dir_path="graphics_draw_round_rect_basic_usage/")\n```',  # noqa
    ##################################################
    "## Return value": "## 返却値",
    ##################################################
    "`draw_round_rect` interface will return the `Rectangle` instance, same as the `draw_rect` interface.": "`draw_round_rect`インターフェイスは`draw_rect`インターフェイスと同様に`Rectangle`クラスのインスタンスを返却します。",  # noqa
    ##################################################
    "The `Rectangle` instance has the `ellipse_width` attribute and `ellipse_height` to change the rectangle round size.": "`Rectangle`クラスのインスタンスは四角の角丸のサイズを変更するための`ellipse_width`と`ellipse_height`属性を持っています。",  # noqa
    ##################################################
    '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    background_color="#333", stage_width=150, stage_height=150, stage_elem_id="stage"\n)\n\nsprite: ap.Sprite = ap.Sprite()\nsprite.graphics.begin_fill(color="#0af")\n\nrectangle: ap.Rectangle = sprite.graphics.draw_round_rect(\n    x=50, y=50, width=50, height=50, ellipse_width=10, ellipse_height=10\n)\n\n# You can update the ellipse_width and ellipse_height\n# attributes dynamically.\nrectangle.ellipse_width = ap.Int(20)\n\nap.save_overall_html(dest_dir_path="graphics_draw_round_rect_return_value/")\n```': '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    background_color="#333", stage_width=150, stage_height=150, stage_elem_id="stage"\n)\n\nsprite: ap.Sprite = ap.Sprite()\nsprite.graphics.begin_fill(color="#0af")\n\nrectangle: ap.Rectangle = sprite.graphics.draw_round_rect(\n    x=50, y=50, width=50, height=50, ellipse_width=10, ellipse_height=10\n)\n\n# You can update the ellipse_width and ellipse_height\n# attributes dynamically.\nrectangle.ellipse_width = ap.Int(20)\n\nap.save_overall_html(dest_dir_path="graphics_draw_round_rect_return_value/")\n```',  # noqa
    ##################################################
    "## draw_round_rect API": "## draw_round_rect API",
    ##################################################
    '<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>': '<span class="inconspicuous-txt">特記事項: このAPIドキュメントはドキュメントビルド用のスクリプトによって自動で生成・同期されています。そのためもしかしたらこの節の内容は前節までの内容と重複している場合があります。</span>',  # noqa
    ##################################################
    "**[Interface summary]**": "**[インターフェイス概要]**",
    ##################################################
    "Draw a rounded rectangle vector graphics.<hr>": "角丸四角のベクターグラフィックスを描画します。<hr>",
    ##################################################
    "**[Parameters]**": "**[引数]**",
    ##################################################
    "- `x`: Int or int": "- `x`: Int or int",
    ##################################################
    "  - X-coordinate to start drawing.": "  - 描画を開始するX座標。",
    ##################################################
    "- `y`: Int or int": "- `y`: Int or int",
    ##################################################
    "  - Y-coordinate to start drawing.": "  - 描画を開始するY座標。",
    ##################################################
    "- `width`: Int or int": "- `width`: Int or int",
    ##################################################
    "  - Rectangle width.": "  - 四角の幅。",
    ##################################################
    "- `height`: Int or int": "- `height`: Int or int",
    ##################################################
    "  - Rectangle height.": "  - 四角の高さ。",
    ##################################################
    "- `ellipse_width`: Int or int": "- `ellipse_width`: Int or int",
    ##################################################
    "  - Ellipse width of the rectangle corner.": "  - 四角の角丸の幅。",
    ##################################################
    "- `ellipse_height`: Int or int": "- `ellipse_height`: Int or int",
    ##################################################
    "  - Ellipse height of the rectangle corner.": "  - 四角の角丸の高さ。",
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
    '```py\n>>> import apysc as ap\n>>> stage: ap.Stage = ap.Stage()\n>>> sprite: ap.Sprite = ap.Sprite()\n>>> sprite.graphics.begin_fill(color="#0af")\n>>> round_rect: ap.Rectangle = sprite.graphics.draw_round_rect(\n...     x=50, y=50, width=50, height=50, ellipse_width=10, ellipse_height=15\n... )\n>>> round_rect.ellipse_width\nInt(10)\n\n>>> round_rect.ellipse_height\nInt(15)\n```': '```py\n>>> import apysc as ap\n>>> stage: ap.Stage = ap.Stage()\n>>> sprite: ap.Sprite = ap.Sprite()\n>>> sprite.graphics.begin_fill(color="#0af")\n>>> round_rect: ap.Rectangle = sprite.graphics.draw_round_rect(\n...     x=50, y=50, width=50, height=50, ellipse_width=10, ellipse_height=15\n... )\n>>> round_rect.ellipse_width\nInt(10)\n\n>>> round_rect.ellipse_height\nInt(15)\n```',  # noqa
}
