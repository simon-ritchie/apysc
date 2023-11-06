"""This module is for the translation mapping data of the
following document:

Document file: rectangle_geom.md
Language: jp
"""

from typing import Dict

MAPPING: Dict[str, str] = {
    ##################################################
    "# RectangleGeom class": "# RectangleGeom クラス",
    ##################################################
    "This page explains the `RectangleGeom` class.": "このページでは`RectangleGeom`クラスについて説明します。",  # noqa
    ##################################################
    "## What class is this?": "## クラス概要",
    ##################################################
    "The `RectangleGeom` class has the rectangle's geometry interfaces, such as the `left_x`, `center_x`, `right_x`, `top_y`, `center_y`, `bottom_y`, `width`, and `height`.": "`RectangleGeom`クラスは`lext_x`や`center_x`、`right_x`、`top_y`、`center_y`、`bottom_y`、`width`、`height`といった四角の幾何学（座標やサイズなど）の各インターフェイスを持ちます。",  # noqa
    ##################################################
    "## Basic usage": "## 基本的な使い方",
    ##################################################
    "In most cases, the apysc initializes the `RectangleGeom` class internally.": "多くのケースでは、apyscが内部で`RectangleGeom`クラスを初期化します。",  # noqa
    ##################################################
    "For instance, the `get_bounds` method returns a `RectangleGeom` instance; and sets its instance's rectangle geometry data (bounding box).": "例えば、`get_bounds`メソッドは`RectangleGeom`インスタンスを返却し、且つそのインスタンスに四角の幾何学のデータ（バウンディングボックス）を設定します。",  # noqa
    ##################################################
    '```py\n# runnable\nimport apysc as ap\n\nstage: ap.Stage = ap.Stage(\n    background_color=ap.Color("#333"),\n    stage_width=300,\n    stage_height=200,\n    stage_elem_id="stage",\n)\nrectangle: ap.Rectangle = ap.Rectangle(\n    x=50,\n    y=50,\n    width=200,\n    height=75,\n    fill_color=ap.Color("#0af"),\n)\nbounding_box: ap.RectangleGeom = rectangle.get_bounds()\ntext_1: ap.SvgText = ap.SvgText(\n    text=(\n        ap.String("Left x: ")\n        + bounding_box.left_x.to_string()\n        + ap.String(" width: ")\n        + bounding_box.width.to_string()\n    ),\n    x=50,\n    y=150,\n    fill_color=ap.Color("#aaa"),\n)\nap.save_overall_html(dest_dir_path="rectangle_geom_basic_usage/")\n```': '```py\n# runnable\nimport apysc as ap\n\nstage: ap.Stage = ap.Stage(\n    background_color=ap.Color("#333"),\n    stage_width=300,\n    stage_height=200,\n    stage_elem_id="stage",\n)\nrectangle: ap.Rectangle = ap.Rectangle(\n    x=50,\n    y=50,\n    width=200,\n    height=75,\n    fill_color=ap.Color("#0af"),\n)\nbounding_box: ap.RectangleGeom = rectangle.get_bounds()\ntext_1: ap.SvgText = ap.SvgText(\n    text=(\n        ap.String("Left x: ")\n        + bounding_box.left_x.to_string()\n        + ap.String(" width: ")\n        + bounding_box.width.to_string()\n    ),\n    x=50,\n    y=150,\n    fill_color=ap.Color("#aaa"),\n)\nap.save_overall_html(dest_dir_path="rectangle_geom_basic_usage/")\n```',  # noqa
    ##################################################
    "## Each attribute point": "## 各属性の座標",
    ##################################################
    "The following example shows each attribute point:": "以下の例では各属性の座標を表示しています:",
    ##################################################
    '```py\n# runnable\nimport apysc as ap\n\nstage: ap.Stage = ap.Stage(\n    background_color=ap.Color("#333"),\n    stage_width=600,\n    stage_height=440,\n    stage_elem_id="stage",\n)\ncircle: ap.Circle = ap.Circle(\n    x=250,\n    y=220,\n    radius=150,\n    fill_color=ap.Color("#0af"),\n)\nbounding_box: ap.RectangleGeom = circle.get_bounds()\n\nLINE_COLOR: ap.Color = ap.Color("#aaa")\nbox_rectangle: ap.Rectangle = ap.Rectangle(\n    x=bounding_box.left_x,\n    y=bounding_box.top_y,\n    width=bounding_box.width,\n    height=bounding_box.height,\n    line_color=LINE_COLOR,\n)\n\nPOINT_RADIUS: int = 10\nfill_color: ap.Color = ap.Color("#fd63c3")\nleft_x_and_top_y_circle: ap.Circle = ap.Circle(\n    x=bounding_box.left_x,\n    y=bounding_box.top_y,\n    radius=POINT_RADIUS,\n    fill_color=fill_color,\n)\nleft_x_and_top_y_text: ap.SvgText = ap.SvgText(\n    text="left_x and top_y",\n    x=bounding_box.left_x,\n    y=bounding_box.top_y - 15,\n    fill_color=fill_color,\n)\n\nfill_color = ap.Color("#ae59e3")\nright_x_and_top_y_circle: ap.Circle = ap.Circle(\n    x=bounding_box.right_x,\n    y=bounding_box.top_y,\n    radius=POINT_RADIUS,\n    fill_color=fill_color,\n)\nright_x_and_top_y_text: ap.SvgText = ap.SvgText(\n    text="right_x and top_y",\n    x=bounding_box.right_x,\n    y=bounding_box.top_y - 15,\n    fill_color=fill_color,\n)\n\nfill_color = ap.Color("#726efa")\nleft_x_and_bottom_y_circle: ap.Circle = ap.Circle(\n    x=bounding_box.left_x,\n    y=bounding_box.bottom_y,\n    radius=POINT_RADIUS,\n    fill_color=fill_color,\n)\nleft_x_and_bottom_y_text: ap.SvgText = ap.SvgText(\n    text="left_x and bottom_y",\n    x=bounding_box.left_x,\n    y=bounding_box.bottom_y + 31,\n    fill_color=fill_color,\n)\n\nfill_color = ap.Color("#6eaee6")\nright_x_and_bottom_y_circle: ap.Circle = ap.Circle(\n    x=bounding_box.right_x,\n    y=bounding_box.bottom_y,\n    radius=POINT_RADIUS,\n    fill_color=fill_color,\n)\nright_x_and_bottom_y_text: ap.SvgText = ap.SvgText(\n    text="right_x and bottom_y",\n    x=bounding_box.right_x,\n    y=bounding_box.bottom_y + 31,\n    fill_color=fill_color,\n)\n\nfill_color = ap.Color("#ffffff")\ncenter_x_and_center_y_circle: ap.Circle = ap.Circle(\n    x=bounding_box.center_x,\n    y=bounding_box.center_y,\n    radius=POINT_RADIUS,\n    fill_color=fill_color,\n)\ncenter_x_and_center_y_text: ap.SvgText = ap.SvgText(\n    text="center_x and center_y",\n    x=bounding_box.center_x + 25,\n    y=bounding_box.center_y + 5,\n    fill_color=fill_color,\n)\n\nap.save_overall_html(dest_dir_path="rectangle_geom_each_attribute_point/")\n```': '```py\n# runnable\nimport apysc as ap\n\nstage: ap.Stage = ap.Stage(\n    background_color=ap.Color("#333"),\n    stage_width=600,\n    stage_height=440,\n    stage_elem_id="stage",\n)\ncircle: ap.Circle = ap.Circle(\n    x=250,\n    y=220,\n    radius=150,\n    fill_color=ap.Color("#0af"),\n)\nbounding_box: ap.RectangleGeom = circle.get_bounds()\n\nLINE_COLOR: ap.Color = ap.Color("#aaa")\nbox_rectangle: ap.Rectangle = ap.Rectangle(\n    x=bounding_box.left_x,\n    y=bounding_box.top_y,\n    width=bounding_box.width,\n    height=bounding_box.height,\n    line_color=LINE_COLOR,\n)\n\nPOINT_RADIUS: int = 10\nfill_color: ap.Color = ap.Color("#fd63c3")\nleft_x_and_top_y_circle: ap.Circle = ap.Circle(\n    x=bounding_box.left_x,\n    y=bounding_box.top_y,\n    radius=POINT_RADIUS,\n    fill_color=fill_color,\n)\nleft_x_and_top_y_text: ap.SvgText = ap.SvgText(\n    text="left_x and top_y",\n    x=bounding_box.left_x,\n    y=bounding_box.top_y - 15,\n    fill_color=fill_color,\n)\n\nfill_color = ap.Color("#ae59e3")\nright_x_and_top_y_circle: ap.Circle = ap.Circle(\n    x=bounding_box.right_x,\n    y=bounding_box.top_y,\n    radius=POINT_RADIUS,\n    fill_color=fill_color,\n)\nright_x_and_top_y_text: ap.SvgText = ap.SvgText(\n    text="right_x and top_y",\n    x=bounding_box.right_x,\n    y=bounding_box.top_y - 15,\n    fill_color=fill_color,\n)\n\nfill_color = ap.Color("#726efa")\nleft_x_and_bottom_y_circle: ap.Circle = ap.Circle(\n    x=bounding_box.left_x,\n    y=bounding_box.bottom_y,\n    radius=POINT_RADIUS,\n    fill_color=fill_color,\n)\nleft_x_and_bottom_y_text: ap.SvgText = ap.SvgText(\n    text="left_x and bottom_y",\n    x=bounding_box.left_x,\n    y=bounding_box.bottom_y + 31,\n    fill_color=fill_color,\n)\n\nfill_color = ap.Color("#6eaee6")\nright_x_and_bottom_y_circle: ap.Circle = ap.Circle(\n    x=bounding_box.right_x,\n    y=bounding_box.bottom_y,\n    radius=POINT_RADIUS,\n    fill_color=fill_color,\n)\nright_x_and_bottom_y_text: ap.SvgText = ap.SvgText(\n    text="right_x and bottom_y",\n    x=bounding_box.right_x,\n    y=bounding_box.bottom_y + 31,\n    fill_color=fill_color,\n)\n\nfill_color = ap.Color("#ffffff")\ncenter_x_and_center_y_circle: ap.Circle = ap.Circle(\n    x=bounding_box.center_x,\n    y=bounding_box.center_y,\n    radius=POINT_RADIUS,\n    fill_color=fill_color,\n)\ncenter_x_and_center_y_text: ap.SvgText = ap.SvgText(\n    text="center_x and center_y",\n    x=bounding_box.center_x + 25,\n    y=bounding_box.center_y + 5,\n    fill_color=fill_color,\n)\n\nap.save_overall_html(dest_dir_path="rectangle_geom_each_attribute_point/")\n```',  # noqa
    ##################################################
    "## RectangleGeom constructor API": "## RectangleGeom クラスのコンストラクタのAPI",
    ##################################################
    '<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>': '<span class="inconspicuous-txt">特記事項: このAPIドキュメントはドキュメントビルド用のスクリプトによって自動で生成・同期されています。そのためもしかしたらこの節の内容は前節までの内容と重複している場合があります。</span>',  # noqa
    ##################################################
    "**[Interface summary]**": "**[インターフェイス概要]**",
    ##################################################
    "The rectangle's geometry class.<hr>": "四角の幾何学情報を扱うためのクラスです。<hr>",
    ##################################################
    "**[Parameters]**": "**[引数]**",
    ##################################################
    "- `left_x`: Number": "- `left_x`: Number",
    ##################################################
    "  - The rectangle left x coordinate.": "  - 四角の左端のX座標。",
    ##################################################
    "- `center_x`: Number": "- `center_x`: Number",
    ##################################################
    "  - The rectangle center x coordinate.": "  - 四角の中央のX座標。",
    ##################################################
    "- `right_x`: Number": "- `right_x`: Number",
    ##################################################
    "  - The rectangle right x coordinate.": "  - 四角の右端のX座標。",
    ##################################################
    "- `top_y`: Number": "- `top_y`: Number",
    ##################################################
    "  - The rectangle top y coordinate.": "  - 四角の上端のY座標。",
    ##################################################
    "- `center_y`: Number": "- `center_y`: Number",
    ##################################################
    "  - The rectangle center y coordinate.": "  - 四角の中央のY座標。",
    ##################################################
    "- `bottom_y`: Number": "- `bottom_y`: Number",
    ##################################################
    "  - The rectangle bottom y coordinate.": "  - 四角の下端のY座標。",
    ##################################################
    "- `width`: Int": "- `width`: Int",
    ##################################################
    "  - The rectangle width.": "  - 四角の幅。",
    ##################################################
    "- `height`: Int": "- `height`: Int",
    ##################################################
    "  - The Rectangle height.": "  - 四角の高さ。",
    ##################################################
    "## RectangleGeom left_x property API": "## RectangleGeom クラスの left_x 属性のAPI",
    ##################################################
    '<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>': '<span class="inconspicuous-txt">特記事項: このAPIドキュメントはドキュメントビルド用のスクリプトによって自動で生成・同期されています。そのためもしかしたらこの節の内容は前節までの内容と重複している場合があります。</span>',  # noqa
    ##################################################
    "**[Interface summary]**": "**[インターフェイス概要]**",
    ##################################################
    "Get the rectangle left x coordinate.<hr>": "四角の左端のX座標を取得します。<hr>",
    ##################################################
    "**[Returns]**": "**[返却値]**",
    ##################################################
    "- `left_x`: Number": "- `left_x`: Number",
    ##################################################
    "  - The rectangle left x coordinate.": "  - 四角の左端のX座標。",
    ##################################################
    "## RectangleGeom center_x property API": "## RectangleGeom クラスの center_x 属性のAPI",
    ##################################################
    '<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>': '<span class="inconspicuous-txt">特記事項: このAPIドキュメントはドキュメントビルド用のスクリプトによって自動で生成・同期されています。そのためもしかしたらこの節の内容は前節までの内容と重複している場合があります。</span>',  # noqa
    ##################################################
    "**[Interface summary]**": "**[インターフェイス概要]**",
    ##################################################
    "Get the rectangle center x coordinate.<hr>": "四角の中央のX座標を取得します。<hr>",
    ##################################################
    "**[Returns]**": "**[返却値]**",
    ##################################################
    "- `center_x`: Number": "- `center_x`: Number",
    ##################################################
    "  - The rectangle center x coordinate.": "  - 四角の中央のX座標。",
    ##################################################
    "## RectangleGeom right_x property API": "## RectangleGeom クラスの right_x 属性のAPI",
    ##################################################
    '<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>': '<span class="inconspicuous-txt">特記事項: このAPIドキュメントはドキュメントビルド用のスクリプトによって自動で生成・同期されています。そのためもしかしたらこの節の内容は前節までの内容と重複している場合があります。</span>',  # noqa
    ##################################################
    "**[Interface summary]**": "**[インターフェイス概要]**",
    ##################################################
    "Get the rectangle right x coordinate.<hr>": "四角の右端のX座標を取得します。<hr>",
    ##################################################
    "**[Returns]**": "**[返却値]**",
    ##################################################
    "- `right_x`: Number": "- `right_x`: Number",
    ##################################################
    "  - The rectangle right x coordinate.": "  - 四角の右端のX座標。",
    ##################################################
    "## RectangleGeom top_y property API": "## RectangleGeom クラスの top_y 属性のAPI",
    ##################################################
    '<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>': '<span class="inconspicuous-txt">特記事項: このAPIドキュメントはドキュメントビルド用のスクリプトによって自動で生成・同期されています。そのためもしかしたらこの節の内容は前節までの内容と重複している場合があります。</span>',  # noqa
    ##################################################
    "**[Interface summary]**": "**[インターフェイス概要]**",
    ##################################################
    "Get the rectangle top y coordinate.<hr>": "四角の上端のY座標を取得します。<hr>",
    ##################################################
    "**[Returns]**": "**[返却値]**",
    ##################################################
    "- `top_y`: Number": "- `top_y`: Number",
    ##################################################
    "  - The rectangle top y coordinate.": "  - 四角の上端のY座標。",
    ##################################################
    "## RectangleGeom center_y property API": "## RectangleGeom クラスの center_y 属性のAPI",
    ##################################################
    '<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>': '<span class="inconspicuous-txt">特記事項: このAPIドキュメントはドキュメントビルド用のスクリプトによって自動で生成・同期されています。そのためもしかしたらこの節の内容は前節までの内容と重複している場合があります。</span>',  # noqa
    ##################################################
    "**[Interface summary]**": "**[インターフェイス概要]**",
    ##################################################
    "Get the rectangle center y coordinate.<hr>": "四角の中央のY座標を取得します。<hr>",
    ##################################################
    "**[Returns]**": "**[返却値]**",
    ##################################################
    "- `center_y`: Number": "- `center_y`: Number",
    ##################################################
    "  - The rectangle center y coordinate.": "  - 四角の中央のY座標。",
    ##################################################
    "## RectangleGeom bottom_y property API": "## RectangleGeom クラスの bottom_y 属性のAPI",
    ##################################################
    '<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>': '<span class="inconspicuous-txt">特記事項: このAPIドキュメントはドキュメントビルド用のスクリプトによって自動で生成・同期されています。そのためもしかしたらこの節の内容は前節までの内容と重複している場合があります。</span>',  # noqa
    ##################################################
    "**[Interface summary]**": "**[インターフェイス概要]**",
    ##################################################
    "Get the rectangle bottom y coordinate.<hr>": "四角の下端のY座標を取得します。<hr>",
    ##################################################
    "**[Returns]**": "**[返却値]**",
    ##################################################
    "- `bottom_y`: Number": "- `bottom_y`: Number",
    ##################################################
    "  - The rectangle bottom y coordinate.": "  - 四角の下端のY座標。",
    ##################################################
    "## RectangleGeom width property API": "## RectangleGeom クラスの width 属性のAPI",
    ##################################################
    '<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>': '<span class="inconspicuous-txt">特記事項: このAPIドキュメントはドキュメントビルド用のスクリプトによって自動で生成・同期されています。そのためもしかしたらこの節の内容は前節までの内容と重複している場合があります。</span>',  # noqa
    ##################################################
    "**[Interface summary]**": "**[インターフェイス概要]**",
    ##################################################
    "Get the rectangle geometry width.<hr>": "四角の幅の値を取得します。<hr>",
    ##################################################
    "**[Returns]**": "**[返却値]**",
    ##################################################
    "- `width`: Int": "- `width`: Int",
    ##################################################
    "  - The rectangle geometry width.": "  - 四角の幅の値。",
    ##################################################
    "## RectangleGeom height property API": "## RectangleGeom の height 属性のAPI",
    ##################################################
    '<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>': '<span class="inconspicuous-txt">特記事項: このAPIドキュメントはドキュメントビルド用のスクリプトによって自動で生成・同期されています。そのためもしかしたらこの節の内容は前節までの内容と重複している場合があります。</span>',  # noqa
    ##################################################
    "**[Interface summary]**": "**[インターフェイス概要]**",
    ##################################################
    "Get the rectangle geometry height.<hr>": "四角の高さの値を取得します。<hr>",
    ##################################################
    "**[Returns]**": "**[返却値]**",
    ##################################################
    "- `height`: Int": "- `height`: Int",
    ##################################################
    "  - The rectangle geometry height.": "  - 四角の高さの値。",
    ##################################################
    "## get_bounds method API": "## get_bounds メソッドのAPI",
    ##################################################
    '<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>': '<span class="inconspicuous-txt">特記事項: このAPIドキュメントはドキュメントビルド用のスクリプトによって自動で生成・同期されています。そのためもしかしたらこの節の内容は前節までの内容と重複している場合があります。</span>',  # noqa
    ##################################################
    "**[Interface summary]**": "**[インターフェイス概要]**",
    ##################################################
    "Get an instance's bounding-box geometry data.<hr>": "インスタンスのバウンディングボックスの幾何データを取得します。<hr>",  # noqa
    ##################################################
    "**[Returns]**": "**[返却値]**",
    ##################################################
    "- `bounding_box`: RectangleGeom": "- `bounding_box`: RectangleGeom",
    ##################################################
    "  - An instance's bounding-box geometry data.": "  - インスタンスのバウンディングボックスの幾何データ。",
    ##################################################
    "<hr>": "<hr>",
    ##################################################
    "**[Examples]**": "**[コードサンプル]**",
    ##################################################
    '```py\n>>> import apysc as ap\n>>> stage: ap.Stage = ap.Stage(\n...     background_color=ap.Color("#333"), stage_width=250, stage_height=350\n... )\n>>> rectangle: ap.Rectangle = ap.Rectangle(\n...     x=50,\n...     y=100,\n...     width=150,\n...     height=200,\n...     fill_color=ap.Color("#0af"),\n... )\n>>> bounding_box: ap.RectangleGeom = rectangle.get_bounds()\n```': '```py\n>>> import apysc as ap\n>>> stage: ap.Stage = ap.Stage(\n...     background_color=ap.Color("#333"), stage_width=250, stage_height=350\n... )\n>>> rectangle: ap.Rectangle = ap.Rectangle(\n...     x=50,\n...     y=100,\n...     width=150,\n...     height=200,\n...     fill_color=ap.Color("#0af"),\n... )\n>>> bounding_box: ap.RectangleGeom = rectangle.get_bounds()\n```',  # noqa
    ##################################################
    "<hr>": "<hr>",
    ##################################################
    "**[References]**": "**[関連資料]**",
    ##################################################
    "- [get_bounds interface](https://simon-ritchie.github.io/apysc/en/get_bounds.md)": "- [get_bounds インターフェイス](https://simon-ritchie.github.io/apysc/jp/jp_get_bounds.md)",  # noqa
}
