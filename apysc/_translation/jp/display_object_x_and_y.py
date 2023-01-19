"""This module is for the translation mapping data of the
following document:

Document file: display_object_x_and_y.md
Language: jp
"""

from typing import Dict

MAPPING: Dict[str, str] = {
    ##################################################
    "# DisplayObject x and y interfaces": "# DisplayObject クラスの x と y のインターフェイス",
    ##################################################
    "This page explains the `DisplayObject` class x and y property interfaces.": "このページでは`DisplayObject`クラスのxとy属性のインターフェイスについて説明します。",  # noqa
    ##################################################
    "## What interfaces are these?": "## 各インターフェイスの概要",
    ##################################################
    "The x and y properties change the `DisplayObject` instance 2-dimensional coordinates.": "xとy属性は`DisplayObject`のインスタンスの2次元の座標位置を変更します。",  # noqa
    ##################################################
    "## Basic usage": "## 基本的な使い方",
    ##################################################
    "Each `DisplayObject` instance has the x and y properties and can get/set the value with it.": "`DisplayObject`の各インスタンスはxとy属性を持っており、それを参照して座標値の取得と更新を行うことができます。",  # noqa
    ##################################################
    '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    background_color="#333", stage_width=150, stage_height=150, stage_elem_id="stage"\n)\n\nsprite: ap.Sprite = ap.Sprite()\nsprite.graphics.begin_fill(color="#0af")\nrectangle: ap.Rectangle = sprite.graphics.draw_rect(x=0, y=0, width=50, height=50)\n\n# Update the x and y coordinates from 0 to 50.\nrectangle.x = ap.Int(50)\nrectangle.y = ap.Int(50)\n\nap.save_overall_html(dest_dir_path="display_object_x_and_y_basic_usage/")\n```': '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    background_color="#333", stage_width=150, stage_height=150, stage_elem_id="stage"\n)\n\nsprite: ap.Sprite = ap.Sprite()\nsprite.graphics.begin_fill(color="#0af")\nrectangle: ap.Rectangle = sprite.graphics.draw_rect(x=0, y=0, width=50, height=50)\n\n# Update the x and y coordinates from 0 to 50.\nrectangle.x = ap.Int(50)\nrectangle.y = ap.Int(50)\n\nap.save_overall_html(dest_dir_path="display_object_x_and_y_basic_usage/")\n```',  # noqa
    ##################################################
    "## Augmented assignment": "## 累算代入演算",
    ##################################################
    "The x and y properties support the Augmented assignments, like the `+=`\\, `-=`\\, `/=`\\, and `*=` operators.": "xとy属性は`+=`や`-=`、`/=`、`*=`の累算代入演算をサポートしています。",  # noqa
    ##################################################
    "The following example appends 10-pixel to the y-coordinate when you click the rectangle.": "以下のコード例では四角をクリックする度に10pxずつY座標を加算しています。",  # noqa
    ##################################################
    '```py\n# runnable\nimport apysc as ap\n\n\ndef on_click(e: ap.MouseEvent[ap.Rectangle], options: dict) -> None:\n    """\n    The handler that the rectangle calls when clicked.\n\n    Parameters\n    ----------\n    e : MouseEvent\n        Event instance.\n    options : dict\n        Optional arguments dictionary.\n    """\n    rectangle: ap.Rectangle = e.this\n    rectangle.y += 10\n\n\nap.Stage(\n    background_color="#333", stage_width=150, stage_height=150, stage_elem_id="stage"\n)\n\nsprite: ap.Sprite = ap.Sprite()\nsprite.graphics.begin_fill(color="#0af")\nrectangle: ap.Rectangle = sprite.graphics.draw_rect(x=50, y=50, width=50, height=50)\nrectangle.click(on_click)\n\nap.save_overall_html(dest_dir_path="display_object_x_and_y_augmented_assignment/")\n```': '```py\n# runnable\nimport apysc as ap\n\n\ndef on_click(e: ap.MouseEvent[ap.Rectangle], options: dict) -> None:\n    """\n    The handler that the rectangle calls when clicked.\n\n    Parameters\n    ----------\n    e : MouseEvent\n        Event instance.\n    options : dict\n        Optional arguments dictionary.\n    """\n    rectangle: ap.Rectangle = e.this\n    rectangle.y += 10\n\n\nap.Stage(\n    background_color="#333", stage_width=150, stage_height=150, stage_elem_id="stage"\n)\n\nsprite: ap.Sprite = ap.Sprite()\nsprite.graphics.begin_fill(color="#0af")\nrectangle: ap.Rectangle = sprite.graphics.draw_rect(x=50, y=50, width=50, height=50)\nrectangle.click(on_click)\n\nap.save_overall_html(dest_dir_path="display_object_x_and_y_augmented_assignment/")\n```',  # noqa
    ##################################################
    "## x property API": "## x属性のAPI",
    ##################################################
    '<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>': '<span class="inconspicuous-txt">特記事項: このAPIドキュメントはドキュメントビルド用のスクリプトによって自動で生成・同期されています。そのためもしかしたらこの節の内容は前節までの内容と重複している場合があります。</span>',  # noqa
    ##################################################
    "**[Interface summary]**": "**[インターフェイス概要]**",
    ##################################################
    "Get an x-coordinate.<hr>": "X座標を取得します。<hr>",
    ##################################################
    "**[Returns]**": "**[返却値]**",
    ##################################################
    "- `x`: Int": "- `x`: Int",
    ##################################################
    "  - X-coordinate.": "  - X座標。",
    ##################################################
    "<hr>": "<hr>",
    ##################################################
    "**[Examples]**": "**[コードサンプル]**",
    ##################################################
    '```py\n>>> import apysc as ap\n>>> stage: ap.Stage = ap.Stage()\n>>> sprite: ap.Sprite = ap.Sprite()\n>>> sprite.graphics.begin_fill(color="#0af")\n>>> rectangle: ap.Rectangle = sprite.graphics.draw_rect(\n...     x=50, y=50, width=50, height=50\n... )\n>>> rectangle.x = ap.Int(100)\n>>> rectangle.x\nInt(100)\n```': '```py\n>>> import apysc as ap\n>>> stage: ap.Stage = ap.Stage()\n>>> sprite: ap.Sprite = ap.Sprite()\n>>> sprite.graphics.begin_fill(color="#0af")\n>>> rectangle: ap.Rectangle = sprite.graphics.draw_rect(\n...     x=50, y=50, width=50, height=50\n... )\n>>> rectangle.x = ap.Int(100)\n>>> rectangle.x\nInt(100)\n```',  # noqa
    ##################################################
    "## y property API": "## y属性のAPI",
    ##################################################
    '<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>': '<span class="inconspicuous-txt">特記事項: このAPIドキュメントはドキュメントビルド用のスクリプトによって自動で生成・同期されています。そのためもしかしたらこの節の内容は前節までの内容と重複している場合があります。</span>',  # noqa
    ##################################################
    "**[Interface summary]**": "**[インターフェイス概要]**",
    ##################################################
    "Get a y-coordinate.<hr>": "Y座標を取得します。<hr>",
    ##################################################
    "**[Returns]**": "**[返却値]**",
    ##################################################
    "- `y`: Int": "- `y`: Int",
    ##################################################
    "  - Y-coordinate.": "  - Y座標。",
    ##################################################
    "<hr>": "<hr>",
    ##################################################
    "**[Examples]**": "**[コードサンプル]**",
    ##################################################
    '```py\n>>> import apysc as ap\n>>> stage: ap.Stage = ap.Stage()\n>>> sprite: ap.Sprite = ap.Sprite()\n>>> sprite.graphics.begin_fill(color="#0af")\n>>> rectangle: ap.Rectangle = sprite.graphics.draw_rect(\n...     x=50, y=50, width=50, height=50\n... )\n>>> rectangle.y = ap.Int(100)\n>>> rectangle.y\nInt(100)\n```': '```py\n>>> import apysc as ap\n>>> stage: ap.Stage = ap.Stage()\n>>> sprite: ap.Sprite = ap.Sprite()\n>>> sprite.graphics.begin_fill(color="#0af")\n>>> rectangle: ap.Rectangle = sprite.graphics.draw_rect(\n...     x=50, y=50, width=50, height=50\n... )\n>>> rectangle.y = ap.Int(100)\n>>> rectangle.y\nInt(100)\n```',  # noqa
}
