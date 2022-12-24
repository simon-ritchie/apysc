"""This module is for the translation mapping data of the
following document:

Document file: graphics_draw_polygon.md
Language: jp
"""

from typing import Dict

MAPPING: Dict[str, str] = {
    ##################################################
    "# Graphics draw_polygon interface": "# Graphics クラスの draw_polygon インターフェイス",
    ##################################################
    "This page explains the `Graphics` class `draw_polygon` method interface.": "このページでは`Graphics`クラスの`draw_polygon`メソッドのインターフェイスについて説明します。",  # noqa
    ##################################################
    "## What interface is this?": "## インターフェイス概要",
    ##################################################
    "The `draw_polygon` interface draws vector polygon graphics. This interface works slightly similar to the `line_to` and `move_to` interfaces, but the paths do not need to be closed.": "`draw_polygon`インターフェイスは多角形のベクターグラフィックスを描画します。このインターフェイスは`line_to`や`move_to`などのインターフェイスと挙動が少し似ていますが、パスを閉じなくても良いという違いがあります。",  # noqa
    ##################################################
    "## Basic usage": "## 基本的な使い方",
    ##################################################
    "The `draw_polygon` interface has the `points` argument, which determines the polygon vertices coordinates.": "`draw_polygon`インターフェイスは各頂点の座標を決めるための`points`引数を必要とします。",  # noqa
    ##################################################
    '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    background_color="#333", stage_width=250, stage_height=150, stage_elem_id="stage"\n)\n\nsprite: ap.Sprite = ap.Sprite()\n\n# Draw the triangle with the draw_polygon interface.\nsprite.graphics.begin_fill(color="#0af")\nsprite.graphics.draw_polygon(\n    points=ap.Array(\n        [\n            ap.Point2D(x=75, y=50),\n            ap.Point2D(x=50, y=100),\n            ap.Point2D(x=100, y=100),\n        ]\n    )\n)\n\n# Draw the diamond shape with the draw_polygon interface.\nsprite.graphics.draw_polygon(\n    points=ap.Array(\n        [\n            ap.Point2D(x=175, y=50),\n            ap.Point2D(x=150, y=75),\n            ap.Point2D(x=175, y=100),\n            ap.Point2D(x=200, y=75),\n        ]\n    )\n)\n\nap.save_overall_html(dest_dir_path="graphics_draw_polygon_basic_usage/")\n```': '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    background_color="#333", stage_width=250, stage_height=150, stage_elem_id="stage"\n)\n\nsprite: ap.Sprite = ap.Sprite()\n\n# Draw the triangle with the draw_polygon interface.\nsprite.graphics.begin_fill(color="#0af")\nsprite.graphics.draw_polygon(\n    points=ap.Array(\n        [\n            ap.Point2D(x=75, y=50),\n            ap.Point2D(x=50, y=100),\n            ap.Point2D(x=100, y=100),\n        ]\n    )\n)\n\n# Draw the diamond shape with the draw_polygon interface.\nsprite.graphics.draw_polygon(\n    points=ap.Array(\n        [\n            ap.Point2D(x=175, y=50),\n            ap.Point2D(x=150, y=75),\n            ap.Point2D(x=175, y=100),\n            ap.Point2D(x=200, y=75),\n        ]\n    )\n)\n\nap.save_overall_html(dest_dir_path="graphics_draw_polygon_basic_usage/")\n```',  # noqa
    ##################################################
    "## Difference between the line_to and draw_polygon interfaces": "## line_to と draw_polygon の各インターフェイスの違いについて",  # noqa
    ##################################################
    "If you set the fill color, the `draw_polygon` interface becomes slightly similar to the `line_to` (and `move_to`) interfaces. So, for example, the following codes both draw the triangle.": "塗りの色の設定をした場合`draw_polygon`と`line_to`（及び`move_to`）のインターフェイスの挙動は少し近くなります。例えば以下のコード例では各インターフェイスでどちらも三角形が描画しています。",  # noqa
    ##################################################
    "The `draw_polygon` interface draws the left triangle. Similarly, the `move_to` and `line_to` interfaces draw the right one.": "`draw_polygon`インターフェイスでは左側の三角形を描画し、`move_to`と`line_to`のインターフェイスでは右側の三角形を描画しています。",  # noqa
    ##################################################
    '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    background_color="#333", stage_width=250, stage_height=150, stage_elem_id="stage"\n)\n\nsprite: ap.Sprite = ap.Sprite()\nsprite.graphics.begin_fill(color="#0af")\n\n# Draw the triangle with the draw_polygon interface.\nsprite.graphics.draw_polygon(\n    points=ap.Array(\n        [\n            ap.Point2D(x=75, y=50),\n            ap.Point2D(x=50, y=100),\n            ap.Point2D(x=100, y=100),\n        ]\n    )\n)\n\n# Draw the triangle with the move_to and line_to interfaces.\nsprite.graphics.move_to(x=175, y=50)\nsprite.graphics.line_to(x=150, y=100)\nsprite.graphics.line_to(x=200, y=100)\n\nap.save_overall_html(dest_dir_path="graphics_draw_polygon_line_to_difference_1/")\n```': '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    background_color="#333", stage_width=250, stage_height=150, stage_elem_id="stage"\n)\n\nsprite: ap.Sprite = ap.Sprite()\nsprite.graphics.begin_fill(color="#0af")\n\n# Draw the triangle with the draw_polygon interface.\nsprite.graphics.draw_polygon(\n    points=ap.Array(\n        [\n            ap.Point2D(x=75, y=50),\n            ap.Point2D(x=50, y=100),\n            ap.Point2D(x=100, y=100),\n        ]\n    )\n)\n\n# Draw the triangle with the move_to and line_to interfaces.\nsprite.graphics.move_to(x=175, y=50)\nsprite.graphics.line_to(x=150, y=100)\nsprite.graphics.line_to(x=200, y=100)\n\nap.save_overall_html(dest_dir_path="graphics_draw_polygon_line_to_difference_1/")\n```',  # noqa
    ##################################################
    "But there is a difference in whether closing the paths is necessary or not. This difference becomes significant when you set the line style setting. The `line_to` interface does not close the paths from end coordinates to start coordinates.": "一方で、各インターフェイスにはパスを閉じる必要があるかどうかの違いがあります。この違いは線の設定を行った場合には顕著になります。`line_to`のインターフェイスでは終点の座標から始点の座標へはパスが自動では繋がりません。",  # noqa
    ##################################################
    '```py\n# runnable\nimport apysc as ap\n\nstage: ap.Stage = ap.Stage(\n    background_color="#333", stage_width=250, stage_height=150, stage_elem_id="stage"\n)\n\nsprite: ap.Sprite = ap.Sprite()\nsprite.graphics.begin_fill(color="#0af")\n\n# Set the line style to see the difference.\nsprite.graphics.line_style(color="#fff", thickness=3)\n\n# Draw the triangle with the draw_polygon interface.\nsprite.graphics.draw_polygon(\n    points=ap.Array(\n        [\n            ap.Point2D(x=75, y=50),\n            ap.Point2D(x=50, y=100),\n            ap.Point2D(x=100, y=100),\n        ]\n    )\n)\n\n# Draw the triangle with the move_to and line_to interfaces.\nsprite.graphics.move_to(x=175, y=50)\nsprite.graphics.line_to(x=150, y=100)\nsprite.graphics.line_to(x=200, y=100)\n\nap.save_overall_html(dest_dir_path="graphics_draw_polygon_line_to_difference_2/")\n```': '```py\n# runnable\nimport apysc as ap\n\nstage: ap.Stage = ap.Stage(\n    background_color="#333", stage_width=250, stage_height=150, stage_elem_id="stage"\n)\n\nsprite: ap.Sprite = ap.Sprite()\nsprite.graphics.begin_fill(color="#0af")\n\n# Set the line style to see the difference.\nsprite.graphics.line_style(color="#fff", thickness=3)\n\n# Draw the triangle with the draw_polygon interface.\nsprite.graphics.draw_polygon(\n    points=ap.Array(\n        [\n            ap.Point2D(x=75, y=50),\n            ap.Point2D(x=50, y=100),\n            ap.Point2D(x=100, y=100),\n        ]\n    )\n)\n\n# Draw the triangle with the move_to and line_to interfaces.\nsprite.graphics.move_to(x=175, y=50)\nsprite.graphics.line_to(x=150, y=100)\nsprite.graphics.line_to(x=200, y=100)\n\nap.save_overall_html(dest_dir_path="graphics_draw_polygon_line_to_difference_2/")\n```',  # noqa
    ##################################################
    "## Return value": "## 返却値",
    ##################################################
    "The `draw_polygon` interface returns the `Polygon` instance. And that has the basic interface as same as the other type graphics instances. The `Polygon` instance also has the `append_line_point` method interface to append points dynamically.": "`draw_polygon`インターフェイスは`Polygon`クラスのインスタンスを返却します。そのインスタンスは他のグラフィックス系のインスタンスと同様の基本的なインターフェイスを持っています。加えて、`Polygon`クラスは頂点を加えるための`append_line_point`メソッドを持っています。",  # noqa
    ##################################################
    "For instance, the following code appends the point and changes from the triangle to the rectangle.": "例えば以下のコード例では座標の追加を行い三角から四角に変換しています。",  # noqa
    ##################################################
    '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    background_color="#333", stage_width=150, stage_height=150, stage_elem_id="stage"\n)\n\nsprite: ap.Sprite = ap.Sprite()\nsprite.graphics.begin_fill(color="#0af")\n\n# Draw the triangle.\npolygon: ap.Polygon = sprite.graphics.draw_polygon(\n    points=ap.Array(\n        [\n            ap.Point2D(x=75, y=50),\n            ap.Point2D(x=50, y=75),\n            ap.Point2D(x=75, y=100),\n        ]\n    )\n)\n\n# Append the point and change to the rectangle dynamically.\npolygon.append_line_point(x=100, y=75)\n\nap.save_overall_html(dest_dir_path="graphics_draw_polygon_append_line_point/")\n```': '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    background_color="#333", stage_width=150, stage_height=150, stage_elem_id="stage"\n)\n\nsprite: ap.Sprite = ap.Sprite()\nsprite.graphics.begin_fill(color="#0af")\n\n# Draw the triangle.\npolygon: ap.Polygon = sprite.graphics.draw_polygon(\n    points=ap.Array(\n        [\n            ap.Point2D(x=75, y=50),\n            ap.Point2D(x=50, y=75),\n            ap.Point2D(x=75, y=100),\n        ]\n    )\n)\n\n# Append the point and change to the rectangle dynamically.\npolygon.append_line_point(x=100, y=75)\n\nap.save_overall_html(dest_dir_path="graphics_draw_polygon_append_line_point/")\n```',  # noqa
    ##################################################
    "## draw_polygon API": "## draw_polygon API",
    ##################################################
    '<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>': '<span class="inconspicuous-txt">特記事項: このAPIドキュメントはドキュメントビルド用のスクリプトによって自動で生成・同期されています。そのためもしかしたらこの節の内容は前節までの内容と重複している場合があります。</span>',  # noqa
    ##################################################
    "**[Interface summary]**": "**[インターフェイス概要]**",
    ##################################################
    "Draw a polygon vector graphic. This interface is similar to the Polyline class (created by `move_to` or `line_to`). But unlike that, this interface connects the last point and the start point.<hr>": "多角形のベクターグラフィックスを描画します。このインターフェイスはPolylineクラス（`move_to`や`line_to`のインターフェイスで作成されます）に似ていますが、このインターフェイスは始点と終点が連結されるという違いがあります。<hr>",  # noqa
    ##################################################
    "**[Parameters]**": "**[引数]**",
    ##################################################
    "- `points`: list of Point2D or Array.": "- `points`: list of Point2D or Array.",
    ##################################################
    "  - Polygon vertex points.": "  - 多角形の頂点の各座標。",
    ##################################################
    "- `variable_name_suffix`: str, default ''": "- `variable_name_suffix`: str, default ''",  # noqa
    ##################################################
    "  - A JavaScript variable name suffix string. This setting is sometimes useful for JavaScript's debugging.": "  - JavaScript上の変数のサフィックスの設定です。この設定はJavaScriptのデバッグ時に役立つことがあります。",  # noqa
    ##################################################
    "<hr>": "<hr>",
    ##################################################
    "**[Returns]**": "**[返却値]**",
    ##################################################
    "- `polygon`: Polygon": "- `polygon`: Polygon",
    ##################################################
    "  - Created polygon graphics instance.": "  - 作成された多角形のグラフィックスのインスタンス。",
    ##################################################
    "<hr>": "<hr>",
    ##################################################
    "**[Examples]**": "**[コードサンプル]**",
    ##################################################
    "```py\n>>> import apysc as ap\n>>> stage: ap.Stage = ap.Stage()\n>>> sprite: ap.Sprite = ap.Sprite()\n>>> sprite.graphics.begin_fill(color=\"#0af\")\n>>> polygon: ap.Polygon = sprite.graphics.draw_polygon(\n...     points=[\n...         ap.Point2D(x=25, y=0),\n...         ap.Point2D(x=0, y=50),\n...         ap.Point2D(x=50, y=50),\n...     ]\n... )\n>>> polygon.fill_color\nString('#00aaff')\n```": "```py\n>>> import apysc as ap\n>>> stage: ap.Stage = ap.Stage()\n>>> sprite: ap.Sprite = ap.Sprite()\n>>> sprite.graphics.begin_fill(color=\"#0af\")\n>>> polygon: ap.Polygon = sprite.graphics.draw_polygon(\n...     points=[\n...         ap.Point2D(x=25, y=0),\n...         ap.Point2D(x=0, y=50),\n...         ap.Point2D(x=50, y=50),\n...     ]\n... )\n>>> polygon.fill_color\nString('#00aaff')\n```",  # noqa
}
