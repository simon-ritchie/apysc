"""This module is for the translation mapping data of the
following document:

Document file: graphics_move_to_and_line_to.md
Language: jp
"""

from typing import Dict

MAPPING: Dict[str, str] = {
    ##################################################
    "# Graphics move_to and line_to interfaces": "# Graphics クラスの move_to と line_to インターフェイス",  # noqa
    ##################################################
    "This page explains the `Graphics` class `move_to` and `line_to` method interfaces.": "このページでは`Graphics`クラスの`move_to`と`line_to`メソッドの各インターフェイスについて説明します。",  # noqa
    ##################################################
    "## What interfaces are they?": "## 各インターフェイスの概要",
    ##################################################
    "The `move_to` interface sets the line start point. The `line_to` draws the line from a current point to a destination point. Sequentially, if you call the `line_to` interface, the line becomes polyline.": "`move_to`インターフェイスは線の描画の開始位置を設定します。`line_to`インターフェイスは現在の位置から終点位置に向けて線を描画します。連続して`line_to`を呼び出すと対象の線は折れ線になります。",  # noqa
    ##################################################
    "If you call the `move_to` interface after the calling of `line_to`\\, it creates a new line instance.": "もしも`line_to`インターフェイスを呼んだ後に`move_to`インターフェイスを呼んだ場合には新しい線のインスタンスが生成されます。",  # noqa
    ##################################################
    "## Basic usage": "## 基本的な使い方",
    ##################################################
    "The `move_to` and `line_to` interfaces have x and y arguments.": "`move_to`と`line_to`インターフェイスは共にxとyの引数を必要とします。",  # noqa
    ##################################################
    '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    background_color="#333", stage_width=300, stage_height=100, stage_elem_id="stage"\n)\nsprite: ap.Sprite = ap.Sprite()\n\nsprite.graphics.line_style(color="#0af", thickness=5)\n\n# Move to x=50, y=50 point (no drawing).\nsprite.graphics.move_to(x=50, y=50)\n\n# Draw the line from the current point (50, 50) to the\n# destination point (250, 50).\nsprite.graphics.line_to(x=250, y=50)\n\nap.save_overall_html(dest_dir_path="graphics_move_to_and_line_to_basic_usage/")\n```': '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    background_color="#333", stage_width=300, stage_height=100, stage_elem_id="stage"\n)\nsprite: ap.Sprite = ap.Sprite()\n\nsprite.graphics.line_style(color="#0af", thickness=5)\n\n# Move to x=50, y=50 point (no drawing).\nsprite.graphics.move_to(x=50, y=50)\n\n# Draw the line from the current point (50, 50) to the\n# destination point (250, 50).\nsprite.graphics.line_to(x=250, y=50)\n\nap.save_overall_html(dest_dir_path="graphics_move_to_and_line_to_basic_usage/")\n```',  # noqa
    ##################################################
    "## Sequential calling of the line_to interface": "## line_to インターフェイスの連続した呼び出し",
    ##################################################
    "Sequentially, if you call the `line_to` interface, the result line becomes the polyline.": "`line_to`インターフェイスを連続して呼び出した場合、結果の線は折れ線になります。",  # noqa
    ##################################################
    '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    background_color="#333", stage_width=200, stage_height=200, stage_elem_id="stage"\n)\nsprite: ap.Sprite = ap.Sprite()\n\nsprite.graphics.line_style(color="#0af", thickness=5)\n\n# Move to x=50, y=50 point (no drawing).\nsprite.graphics.move_to(x=50, y=50)\n\n# Draw the line from the current point (50, 50) to the\n# destination point (150, 50).\nsprite.graphics.line_to(x=150, y=50)\n\n# Draw the line from the current point (250, 50) to the\n# destination point (50, 150). This calling changes the line\n# to the polyline.\nsprite.graphics.line_to(x=50, y=150)\n\n# Finally the polyline becomes Z shape by drawing to\n# destination point (150, 150).\nsprite.graphics.line_to(x=150, y=150)\n\nap.save_overall_html(dest_dir_path="graphics_move_to_and_line_to_sequential_calling/")\n```': '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    background_color="#333", stage_width=200, stage_height=200, stage_elem_id="stage"\n)\nsprite: ap.Sprite = ap.Sprite()\n\nsprite.graphics.line_style(color="#0af", thickness=5)\n\n# Move to x=50, y=50 point (no drawing).\nsprite.graphics.move_to(x=50, y=50)\n\n# Draw the line from the current point (50, 50) to the\n# destination point (150, 50).\nsprite.graphics.line_to(x=150, y=50)\n\n# Draw the line from the current point (250, 50) to the\n# destination point (50, 150). This calling changes the line\n# to the polyline.\nsprite.graphics.line_to(x=50, y=150)\n\n# Finally the polyline becomes Z shape by drawing to\n# destination point (150, 150).\nsprite.graphics.line_to(x=150, y=150)\n\nap.save_overall_html(dest_dir_path="graphics_move_to_and_line_to_sequential_calling/")\n```',  # noqa
    ##################################################
    "## move_to interface calling after line_to interface calling": "## line_to インターフェイスを呼び出した後の move_to インターフェイスの呼び出し",  # noqa
    ##################################################
    "If you call the `move_to` interface after calling the `line_to` interface, it creates a new line instance.": "`line_to`インターフェイスを呼び出した後に`move_to`を呼び出した場合新しい線のインスタンスが生成されます。",  # noqa
    ##################################################
    '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    background_color="#333", stage_width=250, stage_height=150, stage_elem_id="stage"\n)\nsprite: ap.Sprite = ap.Sprite()\n\nsprite.graphics.line_style(color="#0af", thickness=5)\n\n# First move_to interface calling.\nsprite.graphics.move_to(x=50, y=50)\nsprite.graphics.line_to(x=100, y=50)\nsprite.graphics.line_to(x=50, y=100)\nsprite.graphics.line_to(x=100, y=100)\n\n# Second move_to interface calling. This will create a new\n# polyline instance.\nsprite.graphics.move_to(x=150, y=50)\nsprite.graphics.line_to(x=200, y=50)\nsprite.graphics.line_to(x=150, y=100)\nsprite.graphics.line_to(x=200, y=100)\n\nap.save_overall_html(\n    dest_dir_path="graphics_move_to_and_line_to_multi_move_to_calling/"\n)\n```': '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    background_color="#333", stage_width=250, stage_height=150, stage_elem_id="stage"\n)\nsprite: ap.Sprite = ap.Sprite()\n\nsprite.graphics.line_style(color="#0af", thickness=5)\n\n# First move_to interface calling.\nsprite.graphics.move_to(x=50, y=50)\nsprite.graphics.line_to(x=100, y=50)\nsprite.graphics.line_to(x=50, y=100)\nsprite.graphics.line_to(x=100, y=100)\n\n# Second move_to interface calling. This will create a new\n# polyline instance.\nsprite.graphics.move_to(x=150, y=50)\nsprite.graphics.line_to(x=200, y=50)\nsprite.graphics.line_to(x=150, y=100)\nsprite.graphics.line_to(x=200, y=100)\n\nap.save_overall_html(\n    dest_dir_path="graphics_move_to_and_line_to_multi_move_to_calling/"\n)\n```',  # noqa
    ##################################################
    "## Polyline instance": "## Polyline インスタンス",
    ##################################################
    "`move_to` and `line_to` interfaces will return `Polyline` instance. You can update each setting or bind events to that instance.": "`move_to`や`line_to`インターフェイスは`Polyline`クラスのインスタンスを返却します。そのインスタンスを使って各設定を更新したりイベントを設定したりすることができます。",  # noqa
    ##################################################
    "For instance, the following script sets the mouse event to `Polyline`\\, updates the line color, and sets dot style in the handler (`on_line_click`).": "例えば以下のコード例では`Polyline`のインスタンスにマウスイベントを設定し、`on_line_click`ハンドラ内で線の色の更新と点線のスタイルを設定しています。",  # noqa
    ##################################################
    '```py\n# runnable\nimport apysc as ap\n\n\ndef on_line_click(e: ap.MouseEvent[ap.Polyline], options: dict) -> None:\n    """\n    The handler that the line instance calls when clicked.\n\n    Parameters\n    ----------\n    e : MouseEvent\n        The event instance.\n    options : dict\n        Optional arguments.\n    """\n    polyline: ap.Polyline = e.this\n    polyline.line_color = ap.String("#f0a")\n    polyline.line_dot_setting = ap.LineDotSetting(dot_size=5)\n\n\nap.Stage(\n    background_color="#333", stage_width=200, stage_height=100, stage_elem_id="stage"\n)\nsprite: ap.Sprite = ap.Sprite()\n\nsprite.graphics.line_style(color="#0af", thickness=30)\npolyline: ap.Polyline = sprite.graphics.move_to(x=50, y=50)\nsprite.graphics.line_to(x=150, y=50)\npolyline.click(on_line_click)\n\nap.save_overall_html(dest_dir_path="graphics_move_to_and_line_to_polyline/")\n```': '```py\n# runnable\nimport apysc as ap\n\n\ndef on_line_click(e: ap.MouseEvent[ap.Polyline], options: dict) -> None:\n    """\n    The handler that the line instance calls when clicked.\n\n    Parameters\n    ----------\n    e : MouseEvent\n        The event instance.\n    options : dict\n        Optional arguments.\n    """\n    polyline: ap.Polyline = e.this\n    polyline.line_color = ap.String("#f0a")\n    polyline.line_dot_setting = ap.LineDotSetting(dot_size=5)\n\n\nap.Stage(\n    background_color="#333", stage_width=200, stage_height=100, stage_elem_id="stage"\n)\nsprite: ap.Sprite = ap.Sprite()\n\nsprite.graphics.line_style(color="#0af", thickness=30)\npolyline: ap.Polyline = sprite.graphics.move_to(x=50, y=50)\nsprite.graphics.line_to(x=150, y=50)\npolyline.click(on_line_click)\n\nap.save_overall_html(dest_dir_path="graphics_move_to_and_line_to_polyline/")\n```',  # noqa
    ##################################################
    "If you click the following line, line style will be updated:": "もし以下の四角をクリックし0た場合、線のスタイルは更新されます:",  # noqa
    ##################################################
    "## move_to API": "## move_to API",
    ##################################################
    '<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>': '<span class="inconspicuous-txt">特記事項: このAPIドキュメントはドキュメントビルド用のスクリプトによって自動で生成・同期されています。そのためもしかしたらこの節の内容は前節までの内容と重複している場合があります。</span>',  # noqa
    ##################################################
    "**[Interface summary]**": "**[インターフェイス概要]**",
    ##################################################
    "Move a line position to a specified point.<hr>": "指定された座標に線の描画位置を移動させます。<hr>",
    ##################################################
    "**[Parameters]**": "**[引数]**",
    ##################################################
    "- `x`: Int or int": "- `x`: Int or int",
    ##################################################
    "  - X destination point to move.": "  - 移動先となるX座標。",
    ##################################################
    "- `y`: Int or int": "- `y`: Int or int",
    ##################################################
    "  - Y destination point to move.": "  - 移動先となるY座標。",
    ##################################################
    "- `variable_name_suffix`: str, default ''": "- `variable_name_suffix`: str, default ''",  # noqa
    ##################################################
    "  - A JavaScript variable name suffix string. This setting is sometimes useful for JavaScript's debugging.": "  - JavaScript上の変数のサフィックスの設定です。この設定はJavaScriptのデバッグ時に役立つことがあります。",  # noqa
    ##################################################
    "<hr>": "<hr>",
    ##################################################
    "**[Returns]**": "**[返却値]**",
    ##################################################
    "- `line`: Polyline": "- `line`: Polyline",
    ##################################################
    "  - Line graphics instance.": "  - 線のグラフィックスのインスタンス。",
    ##################################################
    "<hr>": "<hr>",
    ##################################################
    "**[Examples]**": "**[コードサンプル]**",
    ##################################################
    "```py\n>>> import apysc as ap\n>>> stage: ap.Stage = ap.Stage()\n>>> sprite: ap.Sprite = ap.Sprite()\n>>> sprite.graphics.line_style(color=\"#fff\", thickness=5)\n>>> line_1: ap.Polyline = sprite.graphics.move_to(x=50, y=50)\n>>> line_2: ap.Polyline = sprite.graphics.line_to(x=150, y=50)\n>>> line_1 == line_2\nTrue\n\n>>> line_1.line_color\nString('#ffffff')\n\n>>> line_1.line_thickness\nInt(5)\n```": "```py\n>>> import apysc as ap\n>>> stage: ap.Stage = ap.Stage()\n>>> sprite: ap.Sprite = ap.Sprite()\n>>> sprite.graphics.line_style(color=\"#fff\", thickness=5)\n>>> line_1: ap.Polyline = sprite.graphics.move_to(x=50, y=50)\n>>> line_2: ap.Polyline = sprite.graphics.line_to(x=150, y=50)\n>>> line_1 == line_2\nTrue\n\n>>> line_1.line_color\nString('#ffffff')\n\n>>> line_1.line_thickness\nInt(5)\n```",  # noqa
    ##################################################
    "## line_to API": "## line_to API",
    ##################################################
    '<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>': '<span class="inconspicuous-txt">特記事項: このAPIドキュメントはドキュメントビルド用のスクリプトによって自動で生成・同期されています。そのためもしかしたらこの節の内容は前節までの内容と重複している場合があります。</span>',  # noqa
    ##################################################
    "**[Interface summary]**": "**[インターフェイス概要]**",
    ##################################################
    "Draw a line from previous point to specified point (initial point is x = 0, y = 0).<hr>": "直前の位置の座標から指定された座標に向けて線を描画します（初期位置はx=0, y=0になります）。<hr>",  # noqa
    ##################################################
    "**[Parameters]**": "**[引数]**",
    ##################################################
    "- `x`: Int or int": "- `x`: Int or int",
    ##################################################
    "  - X destination point to draw a line.": "  - 線の描画先となる終点のX座標。",
    ##################################################
    "- `y`: Int or int": "- `y`: Int or int",
    ##################################################
    "  - Y destination point to draw a line.": "  - 線の描画先となる終点のY座標。",
    ##################################################
    "- `variable_name_suffix`: str, default ''": "- `variable_name_suffix`: str, default ''",  # noqa
    ##################################################
    "  - A JavaScript variable name suffix string. This setting is sometimes useful for JavaScript's debugging.": "  - JavaScript上の変数のサフィックスの設定です。この設定はJavaScriptのデバッグ時に役立つことがあります。",  # noqa
    ##################################################
    "<hr>": "<hr>",
    ##################################################
    "**[Returns]**": "**[返却値]**",
    ##################################################
    "- `line`: Polyline": "- `line`: Polyline",
    ##################################################
    "  - Line graphics instance.": "  - 線のグラフィックスのインスタンス。",
    ##################################################
    "<hr>": "<hr>",
    ##################################################
    "**[Examples]**": "**[コードサンプル]**",
    ##################################################
    "```py\n>>> import apysc as ap\n>>> stage: ap.Stage = ap.Stage()\n>>> sprite: ap.Sprite = ap.Sprite()\n>>> sprite.graphics.line_style(color=\"#fff\", thickness=5)\n>>> line_1: ap.Polyline = sprite.graphics.move_to(x=50, y=50)\n>>> line_2: ap.Polyline = sprite.graphics.line_to(x=150, y=50)\n>>> line_3: ap.Polyline = sprite.graphics.line_to(x=50, y=150)\n>>> line_1 == line_2 == line_3\nTrue\n\n>>> line_1.line_color\nString('#ffffff')\n\n>>> line_1.line_thickness\nInt(5)\n```": "```py\n>>> import apysc as ap\n>>> stage: ap.Stage = ap.Stage()\n>>> sprite: ap.Sprite = ap.Sprite()\n>>> sprite.graphics.line_style(color=\"#fff\", thickness=5)\n>>> line_1: ap.Polyline = sprite.graphics.move_to(x=50, y=50)\n>>> line_2: ap.Polyline = sprite.graphics.line_to(x=150, y=50)\n>>> line_3: ap.Polyline = sprite.graphics.line_to(x=50, y=150)\n>>> line_1 == line_2 == line_3\nTrue\n\n>>> line_1.line_color\nString('#ffffff')\n\n>>> line_1.line_thickness\nInt(5)\n```",  # noqa
}
