"""This module is for the translation mapping data of the
following document:

Document file: svg_mask.md
Language: jp
"""

from typing import Dict

MAPPING: Dict[str, str] = {
    ##################################################
    "# SvgMask class and its related interfaces": "# SvgMask クラスと関連インターフェース",
    ##################################################
    "This page explains the `SvgMask` class and related interfaces, such as the `add_svg_masking_object` method and `svg_mask` property.": "このページでは`SvgMask`クラスとそれに関連した`add_svg_masking_object`メソッドや`svg_mask`属性などのインターフェイスについて説明します。",  # noqa
    ##################################################
    "## What class is this?": "## クラス概要",
    ##################################################
    "The `SvgMask` handles SVG graphics mask settings.": "`SvgMask`クラスはSVGグラフィックのマスク設定を扱います。",  # noqa
    ##################################################
    "You can set another SVG `DisplayObject` as a mask for an SVG `DisplayObject` (e.g., `Rectangle`) to display only the overlapping area.": "重なりあった領域のみを表示する形でSVGの`DisplayObject`（例 : `Rectangle`）に別のSVGの`DisplayObject`を設定することができます。",  # noqa
    ##################################################
    "## Basic usage": "## 基本的な使い方",
    ##################################################
    "You can apply the mask setting in the following steps:": "以下のステップでマスク設定を適用することができます。",  # noqa
    ##################################################
    "1. Create an `SvgMask` instance.": "1. `SvgMask`インスタンスを作成します。",
    ##################################################
    "2. Add a `DisplayObject` to the created `SvgMask` instance with the `add_svg_masking_object` method.": "2. `add_svg_masking_object`メソッドを使って作成した`SvgMask`のインスタンスに`DisplayObject`を追加します。",  # noqa
    ##################################################
    "3. Set a mask instance to the target `DisplayObject`'s `svg_mask` property.": "3. マスクのインスタンスを対象の`DisplayObject`の`svg_mask`属性に設定します。",  # noqa
    ##################################################
    '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    background_color=ap.Color("#333"),\n    stage_width=150,\n    stage_height=150,\n    stage_elem_id="stage",\n)\n\n# 1. Create an `SvgMask` instance.\nmask: ap.SvgMask = ap.SvgMask()\ncircle: ap.Circle = ap.Circle(x=100, y=100, radius=50)\n\n# 2. Add a `DisplayObject` to the created `SvgMask` instance.\nmask.add_svg_masking_object(masking_object=circle)\nrectangle: ap.Rectangle = ap.Rectangle(\n    x=0, y=0, width=100, height=100, fill_color=ap.Colors.CYAN_00AAFF\n)\n\n# 3. Set a mask instance to the target `DisplayObject`\'s `svg_mask` property.\nrectangle.svg_mask = mask\n\nap.save_overall_html(dest_dir_path="svg_mask_basic_usage/")\n```': '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    background_color=ap.Color("#333"),\n    stage_width=150,\n    stage_height=150,\n    stage_elem_id="stage",\n)\n\n# 1. Create an `SvgMask` instance.\nmask: ap.SvgMask = ap.SvgMask()\ncircle: ap.Circle = ap.Circle(x=100, y=100, radius=50)\n\n# 2. Add a `DisplayObject` to the created `SvgMask` instance.\nmask.add_svg_masking_object(masking_object=circle)\nrectangle: ap.Rectangle = ap.Rectangle(\n    x=0, y=0, width=100, height=100, fill_color=ap.Colors.CYAN_00AAFF\n)\n\n# 3. Set a mask instance to the target `DisplayObject`\'s `svg_mask` property.\nrectangle.svg_mask = mask\n\nap.save_overall_html(dest_dir_path="svg_mask_basic_usage/")\n```',  # noqa
    ##################################################
    "## Case when you want to synchronize the coordinates of DisplayObject and mask": "## DisplayObjectとマスクの座標を同期させたい場合のケース",  # noqa
    ##################################################
    "Both the `DisplayObject` to set the mask and the `DisplayObject` for the mask have separate coordinates.": "マスクを設定する対象の`DisplayObject`とマスク用の`DisplayObject`はそれぞれ分離された座標値を持っています。",  # noqa
    ##################################################
    "If you want to change the coordinates of each `DisplayObject` by the same amount, it is convenient to use the `Sprite` container.": "もし両方の`DisplayObject`の座標を同じ量だけ変更したい場合には`Sprite`のコンテナーを使用すると便利です。",  # noqa
    ##################################################
    "By changing only the coordinates of a `Sprite` container, you can change the coordinates of a `DisplayObject` while maintaining the coordinates of the mask.": "`Sprite`のコンテナーの座標のみを変更することで、マスクの座標を維持したまま`DisplayObject`の座標を変更することができます。",  # noqa
    ##################################################
    "Notes: You do not need to add `DisplayObject` to the `Sprite` container for the masking.": "特記事項 : マスク処理用の`DisplayObject`は`Sprite`のコンテナーへと追加する必要はありません。",  # noqa
    ##################################################
    '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    background_color=ap.Color("#333"),\n    stage_width=400,\n    stage_height=300,\n    stage_elem_id="stage",\n)\nmask: ap.SvgMask = ap.SvgMask()\ncircle: ap.Circle = ap.Circle(x=150, y=100, radius=100)\nmask.add_svg_masking_object(masking_object=circle)\nrectangle: ap.Rectangle = ap.Rectangle(\n    x=50, y=50, width=100, height=100, fill_color=ap.Colors.CYAN_00AAFF\n)\nrectangle.svg_mask = mask\n\nsprite: ap.Sprite = ap.Sprite()\n# Notes: You do not need to add the circle for masking.\nsprite.add_child(rectangle)\nsprite.x = ap.Number(100)\nsprite.y = ap.Number(50)\n\nap.save_overall_html(dest_dir_path="svg_mask_sprite_container_example/")\n```': '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    background_color=ap.Color("#333"),\n    stage_width=400,\n    stage_height=300,\n    stage_elem_id="stage",\n)\nmask: ap.SvgMask = ap.SvgMask()\ncircle: ap.Circle = ap.Circle(x=150, y=100, radius=100)\nmask.add_svg_masking_object(masking_object=circle)\nrectangle: ap.Rectangle = ap.Rectangle(\n    x=50, y=50, width=100, height=100, fill_color=ap.Colors.CYAN_00AAFF\n)\nrectangle.svg_mask = mask\n\nsprite: ap.Sprite = ap.Sprite()\n# Notes: You do not need to add the circle for masking.\nsprite.add_child(rectangle)\nsprite.x = ap.Number(100)\nsprite.y = ap.Number(50)\n\nap.save_overall_html(dest_dir_path="svg_mask_sprite_container_example/")\n```',  # noqa
    ##################################################
    "## SvgMask constructor API": "## SvgMask クラスのコンストラクタのAPI",
    ##################################################
    '<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>': '<span class="inconspicuous-txt">特記事項: このAPIドキュメントはドキュメントビルド用のスクリプトによって自動で生成・同期されています。そのためもしかしたらこの節の内容は前節までの内容と重複している場合があります。</span>',  # noqa
    ##################################################
    "**[Interface summary]**": "**[インターフェイス概要]**",
    ##################################################
    "The class for the SVG masking.<hr>": "SVGのマスク処理のためのクラスです。<hr>",
    ##################################################
    "**[Parameters]**": "**[引数]**",
    ##################################################
    '- `variable_name_suffix`: str, default ""': '- `variable_name_suffix`: str, default ""',  # noqa
    ##################################################
    "  - A JavaScript variable name suffix string. This setting is sometimes useful for JavaScript debugging.": "  - JavaScript上の変数のサフィックスの設定です。この設定はJavaScriptのデバッグ時に役立つことがあります。",  # noqa
    ##################################################
    "<hr>": "<hr>",
    ##################################################
    "**[Examples]**": "**[コードサンプル]**",
    ##################################################
    "```py\n>>> import apysc as ap\n>>> _ = ap.Stage()\n>>> mask: ap.SvgMask = ap.SvgMask()\n>>> circle: ap.Circle = ap.Circle(\n...     x=50, y=50, radius=50, fill_color=ap.Colors.CYAN_00AAFF\n... )\n>>> mask.add_svg_masking_object(masking_object=circle)\n>>> rectangle: ap.Rectangle = ap.Rectangle(\n...     x=0, y=0, width=100, height=100, fill_color=ap.Colors.CYAN_00AAFF\n... )\n>>> rectangle.svg_mask = mask\n```": "```py\n>>> import apysc as ap\n>>> _ = ap.Stage()\n>>> mask: ap.SvgMask = ap.SvgMask()\n>>> circle: ap.Circle = ap.Circle(\n...     x=50, y=50, radius=50, fill_color=ap.Colors.CYAN_00AAFF\n... )\n>>> mask.add_svg_masking_object(masking_object=circle)\n>>> rectangle: ap.Rectangle = ap.Rectangle(\n...     x=0, y=0, width=100, height=100, fill_color=ap.Colors.CYAN_00AAFF\n... )\n>>> rectangle.svg_mask = mask\n```",  # noqa
    ##################################################
    "## SvgMask add_svg_masking_object method API": "## SvgMask クラスの add_svg_masking_object メソッドのAPI",  # noqa
    ##################################################
    '<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>': '<span class="inconspicuous-txt">特記事項: このAPIドキュメントはドキュメントビルド用のスクリプトによって自動で生成・同期されています。そのためもしかしたらこの節の内容は前節までの内容と重複している場合があります。</span>',  # noqa
    ##################################################
    "**[Interface summary]**": "**[インターフェイス概要]**",
    ##################################################
    "Add an SVG masking object to this mask. This instance uses its masking object to mask other SVG graphics objects. It is possible to add multiple masking objects to a mask.<hr>": "このマスクにマスク処理用のSVGのオブジェクトを追加します。このインスタンスは他のSVGのグラフィックスオブジェクトをマスクするためにそのオブジェクトを使用します。マスクへ複数のマスク処理用のオブジェクトを追加することができます。<hr>",  # noqa
    ##################################################
    "**[Parameters]**": "**[引数]**",
    ##################################################
    "- `masking_object`: GraphicsBase": "- `masking_object`: GraphicsBase",
    ##################################################
    "  - The masking object to add.": "  - 追加するマスク処理用のオブジェクト。",
    ##################################################
    "<hr>": "<hr>",
    ##################################################
    "**[Examples]**": "**[コードサンプル]**",
    ##################################################
    "```py\n>>> import apysc as ap\n>>> _ = ap.Stage()\n>>> mask: ap.SvgMask = ap.SvgMask()\n>>> circle: ap.Circle = ap.Circle(\n...     x=50, y=50, radius=50, fill_color=ap.Colors.CYAN_00AAFF\n... )\n>>> mask.add_svg_masking_object(masking_object=circle)\n>>> rectangle: ap.Rectangle = ap.Rectangle(\n...     x=0, y=0, width=100, height=100, fill_color=ap.Colors.CYAN_00AAFF\n... )\n>>> rectangle.svg_mask = mask\n```": "```py\n>>> import apysc as ap\n>>> _ = ap.Stage()\n>>> mask: ap.SvgMask = ap.SvgMask()\n>>> circle: ap.Circle = ap.Circle(\n...     x=50, y=50, radius=50, fill_color=ap.Colors.CYAN_00AAFF\n... )\n>>> mask.add_svg_masking_object(masking_object=circle)\n>>> rectangle: ap.Rectangle = ap.Rectangle(\n...     x=0, y=0, width=100, height=100, fill_color=ap.Colors.CYAN_00AAFF\n... )\n>>> rectangle.svg_mask = mask\n```",  # noqa
    ##################################################
    "## svg_mask property API": "## svg_mask 属性のAPI",
    ##################################################
    '<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>': '<span class="inconspicuous-txt">特記事項: このAPIドキュメントはドキュメントビルド用のスクリプトによって自動で生成・同期されています。そのためもしかしたらこの節の内容は前節までの内容と重複している場合があります。</span>',  # noqa
    ##################################################
    "**[Interface summary]**": "**[インターフェイス概要]**",
    ##################################################
    "Get an SVG mask setting. If the mask is not set, this property becomes `None`.<hr>": "SVGのマスク設定を取得します。もしマスク設定がされていなければ、この属性の値はNoneとなります。<hr>",  # noqa
    ##################################################
    "**[Returns]**": "**[返却値]**",
    ##################################################
    "- `mask`: Optional[SvgMask]": "- `mask`: Optional[SvgMask]",
    ##################################################
    "  - A mask setting.": "  - マスク設定。",
    ##################################################
    "<hr>": "<hr>",
    ##################################################
    "**[Examples]**": "**[コードサンプル]**",
    ##################################################
    "```py\n>>> import apysc as ap\n>>> _ = ap.Stage()\n>>> mask: ap.SvgMask = ap.SvgMask()\n>>> circle: ap.Circle = ap.Circle(\n...     x=50, y=50, radius=50, fill_color=ap.Colors.CYAN_00AAFF\n... )\n>>> mask.add_svg_masking_object(masking_object=circle)\n>>> rectangle: ap.Rectangle = ap.Rectangle(\n...     x=0, y=0, width=100, height=100, fill_color=ap.Colors.CYAN_00AAFF\n... )\n>>> rectangle.svg_mask = mask\n>>> assert rectangle.svg_mask == mask\n```": "```py\n>>> import apysc as ap\n>>> _ = ap.Stage()\n>>> mask: ap.SvgMask = ap.SvgMask()\n>>> circle: ap.Circle = ap.Circle(\n...     x=50, y=50, radius=50, fill_color=ap.Colors.CYAN_00AAFF\n... )\n>>> mask.add_svg_masking_object(masking_object=circle)\n>>> rectangle: ap.Rectangle = ap.Rectangle(\n...     x=0, y=0, width=100, height=100, fill_color=ap.Colors.CYAN_00AAFF\n... )\n>>> rectangle.svg_mask = mask\n>>> assert rectangle.svg_mask == mask\n```",  # noqa
}
