"""This module is for the translation mapping data of the
following document:

Document file: graphics_draw_triangle.md
Language: jp
"""

from typing import Dict

MAPPING: Dict[str, str] = {
    ##################################################
    "# Graphics draw_triangle interface": "# Graphics クラスの draw_triangle インターフェイス",
    ##################################################
    "This page explains the `Graphics` class `draw_triangle` method interface.": "このページでは`Graphics`クラスの`draw_triangle`メソッドのインターフェイスについて説明します。",  # noqa
    ##################################################
    "## What interface is this?": "## インターフェイス概要",
    ##################################################
    "The `draw_triangle` interface draws vector triangle graphics.": "`draw_triangle`インターフェイスは三角形のベクターグラフィックスを描画します。",  # noqa
    ##################################################
    "## Basic usage": "## 基本的な使い方",
    ##################################################
    "The `draw_triangle` interface requires the `x1`, `y1`, `x2`, `y2`, `x3`, and `y3` arguments.": "`draw_triangle`インターフェイスは`x1`, `y1`, `x2`, `y2`, `x3`, `y3`の各引数の指定を必要とします。",  # noqa
    ##################################################
    "The `x1` and `y1` arguments are the first vertex coordinate of a triangle.": "`x1`と`y1`の引数は三角形の1つ目の頂点の座標となります。",  # noqa
    ##################################################
    "The `x2` and `y2` are the second vertex coordinate, and the `x3` and `y3` are the third.": "`x2`と`y2`は2つ目の頂点の座標となり、`x3`と`y3`は3つ目の頂点の座標となりま。",  # noqa
    ##################################################
    '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    stage_width=150, stage_height=150, background_color="#333", stage_elem_id="stage"\n)\nsprite: ap.Sprite = ap.Sprite()\nsprite.graphics.begin_fill(color="#0af")\ntriangle: ap.Triangle = sprite.graphics.draw_triangle(\n    x1=75,\n    y1=50,\n    x2=50,\n    y2=100,\n    x3=100,\n    y3=100,\n)\n\nap.save_overall_html(dest_dir_path="./graphics_draw_triangle_basic_usage/")\n```': '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    stage_width=150, stage_height=150, background_color="#333", stage_elem_id="stage"\n)\nsprite: ap.Sprite = ap.Sprite()\nsprite.graphics.begin_fill(color="#0af")\ntriangle: ap.Triangle = sprite.graphics.draw_triangle(\n    x1=75,\n    y1=50,\n    x2=50,\n    y2=100,\n    x3=100,\n    y3=100,\n)\n\nap.save_overall_html(dest_dir_path="./graphics_draw_triangle_basic_usage/")\n```',  # noqa
    ##################################################
    "## Triangle instance": "## Triangle インスタンス",
    ##################################################
    "The `draw_triangle` interface returns a `Triangle` instance.": "`draw_triangle`インターフェイスは`Triangle`クラスのインスタンスを返却します。",  # noqa
    ##################################################
    "You can update each setting or bind events.": "そのインスタンスを使って各種設定を更新したりイベントの設定などを行うことができます。",  # noqa
    ##################################################
    "For instance, the following example sets the mouse event to the `Triangle` instance and updates the x-coordinate in the `on_click` handler:": "例えば、以下の例では`Triangle`のインスタンスにマウスイベントを設定し、`on_click`のハンドラ内でX座標の更新を行っています:",  # noqa
    ##################################################
    '```py\n# runnable\nimport apysc as ap\n\n\ndef on_click(e: ap.MouseEvent[ap.Triangle], options: dict) -> None:\n    """\n    The handler for the click event.\n\n    Parameters\n    ----------\n    e : ap.MouseEvent[ap.Rectangle]\n        Event instance.\n    options : dict\n        Optional arguments dictionary.\n    """\n    triangle: ap.Triangle = e.this\n    triangle.x += 2\n\n\nap.Stage(\n    stage_width=150, stage_height=150, background_color="#333", stage_elem_id="stage"\n)\nsprite: ap.Sprite = ap.Sprite()\nsprite.graphics.begin_fill(color="#0af")\ntriangle: ap.Triangle = sprite.graphics.draw_triangle(\n    x1=75,\n    y1=50,\n    x2=50,\n    y2=100,\n    x3=100,\n    y3=100,\n)\ntriangle.click(handler=on_click)\n\nap.save_overall_html(dest_dir_path="./graphics_draw_triangle_triangle_instance/")\n```': '```py\n# runnable\nimport apysc as ap\n\n\ndef on_click(e: ap.MouseEvent[ap.Triangle], options: dict) -> None:\n    """\n    The handler for the click event.\n\n    Parameters\n    ----------\n    e : ap.MouseEvent[ap.Rectangle]\n        Event instance.\n    options : dict\n        Optional arguments dictionary.\n    """\n    triangle: ap.Triangle = e.this\n    triangle.x += 2\n\n\nap.Stage(\n    stage_width=150, stage_height=150, background_color="#333", stage_elem_id="stage"\n)\nsprite: ap.Sprite = ap.Sprite()\nsprite.graphics.begin_fill(color="#0af")\ntriangle: ap.Triangle = sprite.graphics.draw_triangle(\n    x1=75,\n    y1=50,\n    x2=50,\n    y2=100,\n    x3=100,\n    y3=100,\n)\ntriangle.click(handler=on_click)\n\nap.save_overall_html(dest_dir_path="./graphics_draw_triangle_triangle_instance/")\n```',  # noqa
    ##################################################
    "## draw_triangle API": "## draw_triangle のAPI",
    ##################################################
    '<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>': '<span class="inconspicuous-txt">特記事項: このAPIドキュメントはドキュメントビルド用のスクリプトによって自動で生成・同期されています。そのためもしかしたらこの節の内容は前節までの内容と重複している場合があります。</span>',  # noqa
    ##################################################
    "**[Interface summary]**": "**[インターフェイス概要]**",
    ##################################################
    "Draw a triangle vector graphic.<hr>": "三角形のベクターグラフィックスを描画します。<hr>",
    ##################################################
    "**[Parameters]**": "**[引数]**",
    ##################################################
    "- `x1`: Union[float, Number]": "- `x1`: Union[float, Number]",
    ##################################################
    "  - First vertex's x coordinate.": "  - 1つ目の頂点のX座標。",
    ##################################################
    "- `y1`: Union[float, Number]": "- `y1`: Union[float, Number]",
    ##################################################
    "  - First vertex's y coordinate.": "  - 1つ目の頂点のY座標。",
    ##################################################
    "- `x2`: Union[float, Number]": "- `x2`: Union[float, Number]",
    ##################################################
    "  - Second vertex's x coordinate.": "  - 2つ目の頂点のX座標。",
    ##################################################
    "- `y2`: Union[float, Number]": "- `y2`: Union[float, Number]",
    ##################################################
    "  - Second vertex's y coordinate.": "  - 2つ目の頂点のY座標。",
    ##################################################
    "- `x3`: Union[float, Number]": "- `x3`: Union[float, Number]",
    ##################################################
    "  - Third vertex's x coordinate.": "  - 3つ目の頂点のX座標。",
    ##################################################
    "- `y3`: Union[float, Number]": "- `y3`: Union[float, Number]",
    ##################################################
    "  - Third vertex's y coordinate.": "  - 3つ目の頂点のY座標。",
    ##################################################
    "- `variable_name_suffix`: str, optional": "- `variable_name_suffix`: str, optional",  # noqa
    ##################################################
    "  - A JavaScript variable name suffix string. This setting is sometimes useful for JavaScript debugging.": "  - JavaScript上の変数のサフィックスの設定です。この設定はJavaScriptのデバッグ時に役立つことがあります。",  # noqa
    ##################################################
    "<hr>": "<hr>",
    ##################################################
    "**[Returns]**": "**[返却値]**",
    ##################################################
    "- `triangle`: Triangle": "- `triangle`: Triangle",
    ##################################################
    "  - Created triangle graphics instance.": "  - 生成された三角形のグラフィックスのインスタンス。",
    ##################################################
    "<hr>": "<hr>",
    ##################################################
    "**[Examples]**": "**[コードサンプル]**",
    ##################################################
    '```py\n>>> import apysc as ap\n>>> _ = ap.Stage()\n>>> sprite: ap.Sprite = ap.Sprite()\n>>> sprite.graphics.begin_fill(color="#0af", alpha=0.7)\n>>> sprite.graphics.line_style(color="#fff", thickness=5, alpha=0.5)\n>>> triangle: ap.Triangle = sprite.graphics.draw_triangle(\n...     x1=75,\n...     y1=50,\n...     x2=25,\n...     y2=100,\n...     x3=100,\n...     y3=100,\n... )\n>>> triangle.x1\nNumber(75.0)\n\n>>> triangle.y1 = ap.Number(30)\n>>> triangle.y1\nNumber(30.0)\n\n>>> triangle.fill_color\nString(\'#00aaff\')\n```': '```py\n>>> import apysc as ap\n>>> _ = ap.Stage()\n>>> sprite: ap.Sprite = ap.Sprite()\n>>> sprite.graphics.begin_fill(color="#0af", alpha=0.7)\n>>> sprite.graphics.line_style(color="#fff", thickness=5, alpha=0.5)\n>>> triangle: ap.Triangle = sprite.graphics.draw_triangle(\n...     x1=75,\n...     y1=50,\n...     x2=25,\n...     y2=100,\n...     x3=100,\n...     y3=100,\n... )\n>>> triangle.x1\nNumber(75.0)\n\n>>> triangle.y1 = ap.Number(30)\n>>> triangle.y1\nNumber(30.0)\n\n>>> triangle.fill_color\nString(\'#00aaff\')\n```',  # noqa
    ##################################################
    "<hr>": "<hr>",
    ##################################################
    "**[References]**": "**[関連資料]**",
    ##################################################
    "- [Triangle class](https://simon-ritchie.github.io/apysc/en/triangle.html)": "- [Triangle クラス](https://simon-ritchie.github.io/apysc/jp/jp_triangle.html)",  # noqa
}
