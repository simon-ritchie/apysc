"""This module is for the translation mapping data of the
following document:

Document file: graphics_base_rotation_around_center.md
Language: jp
"""

from typing import Dict

MAPPING: Dict[str, str] = {
    ##################################################
    "# GraphicsBase rotation_around_center interface": "# GraphicsBase クラスの rotation_around_center インターフェイス",  # noqa
    ##################################################
    "This page explains the `GraphicsBase` class (base class of each graphic, such as the `Rectangle`) `rotation_around_center` property interface.": "このページでは`GraphicsBase`クラス（`Rectangle`などのグラフィックのクラスの基底クラス）の`rotation_around_center`属性のインターフェイスについて説明します。",  # noqa
    ##################################################
    "## What interface is this?": "## インターフェイス概要",
    ##################################################
    "The `rotation_around_center` property interface can set the rotation angle to its instance (rotation value around its center point).": "`rotation_around_center`属性のインターフェイスではインスタンスの中央座標を基準とした回転角度の設定を行うことができます。",  # noqa
    ##################################################
    "## Basic usage": "## 基本的な使い方",
    ##################################################
    "The `rotation_around_center` interface accepts the `int` or `Int` value.": "`rotation_around_center`インターフェイスは`int`もしくは`Int`の値を受け付けます。",  # noqa
    ##################################################
    '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    background_color="#333", stage_width=150, stage_height=150, stage_elem_id="stage"\n)\nsprite: ap.Sprite = ap.Sprite()\n\n# Set the cyan fill color and draw the rectangle.\nsprite.graphics.begin_fill(color="#0af", alpha=0.5)\ncyan_rect: ap.Rectangle = sprite.graphics.draw_rect(x=50, y=50, width=50, height=50)\ncyan_rect.rotation_around_center = ap.Int(30)\n\n# Set the magenta fill color and draw the rectangle.\nsprite.graphics.begin_fill(color="#f0a", alpha=0.5)\nmagenta_rect: ap.Rectangle = sprite.graphics.draw_rect(x=50, y=50, width=50, height=50)\n# Append the rotation angle with the incremental addition (the result\n# rotation will be 60 degrees).\nmagenta_rect.rotation_around_center += ap.Int(30)\nmagenta_rect.rotation_around_center += ap.Int(30)\n\nap.save_overall_html(dest_dir_path="graphics_base_rotation_around_center_basic_usage/")\n```': '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    background_color="#333", stage_width=150, stage_height=150, stage_elem_id="stage"\n)\nsprite: ap.Sprite = ap.Sprite()\n\n# Set the cyan fill color and draw the rectangle.\nsprite.graphics.begin_fill(color="#0af", alpha=0.5)\ncyan_rect: ap.Rectangle = sprite.graphics.draw_rect(x=50, y=50, width=50, height=50)\ncyan_rect.rotation_around_center = ap.Int(30)\n\n# Set the magenta fill color and draw the rectangle.\nsprite.graphics.begin_fill(color="#f0a", alpha=0.5)\nmagenta_rect: ap.Rectangle = sprite.graphics.draw_rect(x=50, y=50, width=50, height=50)\n# Append the rotation angle with the incremental addition (the result\n# rotation will be 60 degrees).\nmagenta_rect.rotation_around_center += ap.Int(30)\nmagenta_rect.rotation_around_center += ap.Int(30)\n\nap.save_overall_html(dest_dir_path="graphics_base_rotation_around_center_basic_usage/")\n```',  # noqa
    ##################################################
    "## Notes": "## 特記事項",
    ##################################################
    "This interface supports only the graphics instances currently. The container instances, such as the `Sprite` instance, are not supported (due to the HTML (SVG) specification).": "このインターフェイスは現在グラフィック系のクラスでのみサポートしており、`Sprite`などのコンテナーのインスタンスでは現在サポートしていません（HTMLのSVGの仕様に依存しています）。",  # noqa
    ##################################################
    "## rotation_around_center property API": "## rotation_around_center 属性のAPI",
    ##################################################
    '<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>': '<span class="inconspicuous-txt">特記事項: このAPIドキュメントはドキュメントビルド用のスクリプトによって自動で生成・同期されています。そのためもしかしたらこの節の内容は前節までの内容と重複している場合があります。</span>',  # noqa
    ##################################################
    "**[Interface summary]**": "**[インターフェイス概要]**",
    ##################################################
    "Get a rotation value around the center of this instance.<hr>": "インスタンスの中央座標を基準とした回転量を取得します。<hr>",  # noqa
    ##################################################
    "**[Returns]**": "**[返却値]**",
    ##################################################
    "- `rotation_around_center`: Int": "- `rotation_around_center`: Int",
    ##################################################
    "  - Rotation value around the center of this instance.": "  - このインスタンスの中央座標を基準とした回転量。",  # noqa
    ##################################################
    "<hr>": "<hr>",
    ##################################################
    "**[Examples]**": "**[コードサンプル]**",
    ##################################################
    '```py\n>>> import apysc as ap\n>>> stage: ap.Stage = ap.Stage()\n>>> sprite: ap.Sprite = ap.Sprite()\n>>> sprite.graphics.begin_fill(color="#0af")\n>>> rectangle: ap.Rectangle = sprite.graphics.draw_rect(\n...     x=50, y=50, width=50, height=50\n... )\n>>> rectangle.rotation_around_center = ap.Int(45)\n>>> rectangle.rotation_around_center\nInt(45)\n```': '```py\n>>> import apysc as ap\n>>> stage: ap.Stage = ap.Stage()\n>>> sprite: ap.Sprite = ap.Sprite()\n>>> sprite.graphics.begin_fill(color="#0af")\n>>> rectangle: ap.Rectangle = sprite.graphics.draw_rect(\n...     x=50, y=50, width=50, height=50\n... )\n>>> rectangle.rotation_around_center = ap.Int(45)\n>>> rectangle.rotation_around_center\nInt(45)\n```',  # noqa
}
