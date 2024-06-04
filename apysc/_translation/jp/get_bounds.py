"""This module is for the translation mapping data of the
following document:

Document file: get_bounds.md
Language: jp
"""

from typing import Dict

MAPPING: Dict[str, str] = {
    ##################################################
    "# get_bounds interface": "# get_bounds インターフェイス",
    ##################################################
    "This page explains the `get_bounds` method interface.": "このページでは`get_bounds`メソッドのインターフェイスについて説明します。",  # noqa
    ##################################################
    "## What interface is this?": "## インターフェイス概要",
    ##################################################
    "The `get_bounds` method returns an instance's bounding box (geometry data, such as the coordinates or size).": "`get_bounds`メソッドはインスタンスのバウンディングボックスのデータ（座標やサイズなどの幾何データ）を返却します。",  # noqa
    ##################################################
    "## Basic usage": "## 基本的な使い方",
    ##################################################
    "The `get_bounds` method returns a `RectangleGeom` instance.": "`get_bounds`メソッドでは`RectangleGeom`クラスのインスタンスを返却します。",  # noqa
    ##################################################
    "It does not require any arguments.": "このインターフェイスでは引数を必要としません。",
    ##################################################
    "Coordinates baseline becomes the stage's x=0 and y=0.": "座標の基準座標はステージのx=0とy=0の位置となります。",  # noqa
    ##################################################
    '```py\n# runnable\nimport apysc as ap\n\nstage: ap.Stage = ap.Stage(\n    background_color=ap.Color("#333"),\n    stage_width=500,\n    stage_height=440,\n    stage_elem_id="stage",\n)\ncircle: ap.Circle = ap.Circle(\n    x=250,\n    y=220,\n    radius=150,\n    fill_color=ap.Color("#0af"),\n)\nbounding_box: ap.RectangleGeom = circle.get_bounds()\n\nbox_rectangle: ap.Rectangle = ap.Rectangle(\n    x=bounding_box.left_x,\n    y=bounding_box.top_y,\n    width=bounding_box.width,\n    height=bounding_box.height,\n    line_color=ap.Color("#aaa"),\n)\n\nfill_color: ap.Color = ap.Color("#fd63c3")\nleft_x_and_top_y_circle: ap.Circle = ap.Circle(\n    x=bounding_box.left_x,\n    y=bounding_box.top_y,\n    radius=10,\n    fill_color=fill_color,\n)\nleft_x_and_top_y_text: ap.SvgText = ap.SvgText(\n    text="left_x and top_y",\n    x=bounding_box.left_x,\n    y=bounding_box.top_y - 15,\n    fill_color=fill_color,\n)\n\nap.save_overall_html(dest_dir_path="get_bounds_basic_usage/")\n```': '```py\n# runnable\nimport apysc as ap\n\nstage: ap.Stage = ap.Stage(\n    background_color=ap.Color("#333"),\n    stage_width=500,\n    stage_height=440,\n    stage_elem_id="stage",\n)\ncircle: ap.Circle = ap.Circle(\n    x=250,\n    y=220,\n    radius=150,\n    fill_color=ap.Color("#0af"),\n)\nbounding_box: ap.RectangleGeom = circle.get_bounds()\n\nbox_rectangle: ap.Rectangle = ap.Rectangle(\n    x=bounding_box.left_x,\n    y=bounding_box.top_y,\n    width=bounding_box.width,\n    height=bounding_box.height,\n    line_color=ap.Color("#aaa"),\n)\n\nfill_color: ap.Color = ap.Color("#fd63c3")\nleft_x_and_top_y_circle: ap.Circle = ap.Circle(\n    x=bounding_box.left_x,\n    y=bounding_box.top_y,\n    radius=10,\n    fill_color=fill_color,\n)\nleft_x_and_top_y_text: ap.SvgText = ap.SvgText(\n    text="left_x and top_y",\n    x=bounding_box.left_x,\n    y=bounding_box.top_y - 15,\n    fill_color=fill_color,\n)\n\nap.save_overall_html(dest_dir_path="get_bounds_basic_usage/")\n```',  # noqa
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
    "- [RectangleGeom class](https://simon-ritchie.github.io/apysc/en/rectangle_geom.html)": "- [RectangleGeom クラス](https://simon-ritchie.github.io/apysc/jp/jp_rectangle_geom.html)",  # noqa
}
