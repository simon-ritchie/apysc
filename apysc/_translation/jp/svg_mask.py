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
    "3. Set a mask instance to the target `DisplayObject`'s `svg_mask` property.": "マスクのインスタンスを対象の`DisplayObject`の`svg_mask`属性に設定します。",  # noqa
}
