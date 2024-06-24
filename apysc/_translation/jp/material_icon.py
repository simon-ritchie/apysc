"""This module is for the translation mapping data of the
following document:

Document file: material_icon.md
Language: jp
"""

from typing import Dict

MAPPING: Dict[str, str] = {
    ##################################################
    "# Material icon": "# マテリアルアイコン",
    ##################################################
    "This page explains the material icon's apysc implementations.": "このページではapyscにおけるマテリアルアイコンの実装について説明します。",  # noqa
    ##################################################
    "## Basic usage": "## 基本的な使い方",
    ##################################################
    "Each material icon exists in the root package (e.g., `ap.MaterialTimelineIcon`).": "各マテリアルアイコンは一番上のパッケージパスに存在します（例 : `ap.MaterialTimelineIcon`）。",  # noqa
    ##################################################
    "Also, each material icon name has the prefix of `Material` and suffix of `Icon`.": "また、各マテリアルアイコンの名前は`Material`というプレフィックスと`Icon`というサフィックスを共通で持ちます。",  # noqa
    ##################################################
    "All material icons' constructor has the coordinates and style settings arguments, such as the `x`, `y`, `size`, `fill_color`, and `fill_alpha`.": "全てのマテリアルアイコンのコンストラクタは`x`や`y`、`size`、`fill_color`、`fill_alpha`などの座標やスタイルの設定の引数を持ちます。",  # noqa
    ##################################################
    '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    background_color=ap.Color("#333"),\n    stage_width=168,\n    stage_height=72,\n    stage_elem_id="stage",\n)\nSIZE: int = 24\n\nap.MaterialHomeIcon(\n    x=24,\n    y=24,\n    size=SIZE,\n    fill_color=ap.Colors.CYAN_00AAFF,\n)\nap.MaterialBuildIcon(\n    x=24 * 3,\n    y=24,\n    size=SIZE,\n    fill_color=ap.Colors.CYAN_00AAFF,\n)\nap.MaterialCheckCircleIcon(\n    x=24 * 5,\n    y=24,\n    size=SIZE,\n    fill_color=ap.Colors.CYAN_00AAFF,\n)\n\nap.save_overall_html(dest_dir_path="material_icon_basic_usage_1/")\n```': '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    background_color=ap.Color("#333"),\n    stage_width=168,\n    stage_height=72,\n    stage_elem_id="stage",\n)\nSIZE: int = 24\n\nap.MaterialHomeIcon(\n    x=24,\n    y=24,\n    size=SIZE,\n    fill_color=ap.Colors.CYAN_00AAFF,\n)\nap.MaterialBuildIcon(\n    x=24 * 3,\n    y=24,\n    size=SIZE,\n    fill_color=ap.Colors.CYAN_00AAFF,\n)\nap.MaterialCheckCircleIcon(\n    x=24 * 5,\n    y=24,\n    size=SIZE,\n    fill_color=ap.Colors.CYAN_00AAFF,\n)\n\nap.save_overall_html(dest_dir_path="material_icon_basic_usage_1/")\n```',  # noqa
    ##################################################
    "You can also set coordinates or styles with an instance's attributes as follows:": "以下のようにインスタンスの属性を用いて座標やスタイルを設定することもできます:",  # noqa
    ##################################################
    '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    background_color=ap.Color("#333"),\n    stage_width=168,\n    stage_height=72,\n    stage_elem_id="stage",\n)\nSIZE: int = 24\n\nhome_icon: ap.MaterialHomeIcon = ap.MaterialHomeIcon(size=SIZE)\nhome_icon.x = ap.Number(24)\nhome_icon.y = ap.Number(24)\nhome_icon.fill_color = ap.Colors.CYAN_00AAFF\n\nbuild_icon: ap.MaterialBuildIcon = ap.MaterialBuildIcon(size=SIZE)\nbuild_icon.x = ap.Number(24 * 3)\nbuild_icon.y = ap.Number(24)\nbuild_icon.fill_color = ap.Colors.CYAN_00AAFF\n\ncheck_circle_icon: ap.MaterialCheckCircleIcon = ap.MaterialCheckCircleIcon(\n    size=SIZE,\n)\ncheck_circle_icon.x = ap.Number(24 * 5)\ncheck_circle_icon.y = ap.Number(24)\ncheck_circle_icon.fill_color = ap.Colors.CYAN_00AAFF\n\nap.save_overall_html(dest_dir_path="material_icon_basic_usage_2/")\n```': '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    background_color=ap.Color("#333"),\n    stage_width=168,\n    stage_height=72,\n    stage_elem_id="stage",\n)\nSIZE: int = 24\n\nhome_icon: ap.MaterialHomeIcon = ap.MaterialHomeIcon(size=SIZE)\nhome_icon.x = ap.Number(24)\nhome_icon.y = ap.Number(24)\nhome_icon.fill_color = ap.Colors.CYAN_00AAFF\n\nbuild_icon: ap.MaterialBuildIcon = ap.MaterialBuildIcon(size=SIZE)\nbuild_icon.x = ap.Number(24 * 3)\nbuild_icon.y = ap.Number(24)\nbuild_icon.fill_color = ap.Colors.CYAN_00AAFF\n\ncheck_circle_icon: ap.MaterialCheckCircleIcon = ap.MaterialCheckCircleIcon(\n    size=SIZE,\n)\ncheck_circle_icon.x = ap.Number(24 * 5)\ncheck_circle_icon.y = ap.Number(24)\ncheck_circle_icon.fill_color = ap.Colors.CYAN_00AAFF\n\nap.save_overall_html(dest_dir_path="material_icon_basic_usage_2/")\n```',  # noqa
    ##################################################
    "## Material icon's license": "## マテリアルアイコンのライセンス",
    ##################################################
    "The apysc library uses material icons licensed under the APACHE LICENSE, VERSION 2.0.": "apyscライブラリはAPACHE LICENSE, VERSION 2.0のライセンスのマテリアルアイコンを使用しています。",  # noqa
    ##################################################
    "- [Material Symbols & Icons](https://fonts.google.com/icons?icon.size=24&icon.color=%23e8eaed)": "- [Material Symbols & Icons](https://fonts.google.com/icons?icon.size=24&icon.color=%23e8eaed)",  # noqa
    ##################################################
    "- [material-design-icons (GitHub)](https://github.com/google/material-design-icons)": "- [material-design-icons (GitHub)](https://github.com/google/material-design-icons)",  # noqa
    ##################################################
    "- [APACHE LICENSE, VERSION 2.0](https://www.apache.org/licenses/LICENSE-2.0.html)": "- [APACHE LICENSE, VERSION 2.0](https://www.apache.org/licenses/jp_LICENSE-2.0.html)",  # noqa
    ##################################################
    "## Each material icon constructor API": "## 各マテリアルアイコンのコンストラクタのAPI",
    ##################################################
    '<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>': '<span class="inconspicuous-txt">特記事項: このAPIドキュメントはドキュメントビルド用のスクリプトによって自動で生成・同期されています。そのためもしかしたらこの節の内容は前節までの内容と重複している場合があります。</span>',  # noqa
    ##################################################
    "**[Interface summary]**": "**[インターフェイス概要]**",
    ##################################################
    "The class implementation for the SVG icon's class.<hr>": "SVGアイコンのためのクラスの実装。<hr>",  # noqa
    ##################################################
    "**[Parameters]**": "**[引数]**",
    ##################################################
    "- `x`: Union[float, Number], optional": "- `x`: Union[float, Number], optional",
    ##################################################
    "  - X-coordinate of the icon.": "  - アイコンのX座標。",
    ##################################################
    "- `y`: Union[float, Number], optional": "- `y`: Union[float, Number], optional",
    ##################################################
    "  - Y-coordinate of the icon.": "  - アイコンのY座標。",
    ##################################################
    "- `size`: Union[int, Int], optional": "- `size`: Union[int, Int], optional",
    ##################################################
    "  - Size of the icon.": "  - アイコンのY座標。",
    ##################################################
    "- `fill_color`: Color, optional": "- `fill_color`: Color, optional",
    ##################################################
    "  - Fill-color of the icon.": "  - アイコンの塗りの色。",
    ##################################################
    "- `fill_alpha`: Union[float, Number], optional": "- `fill_alpha`: Union[float, Number], optional",  # noqa
    ##################################################
    "  - Fill-alpha of the icon.": "  - アイコンの塗りの透明度。",
    ##################################################
    "- `parent`: Optional[ChildMixIn], optional": "- `parent`: Optional[ChildMixIn], optional",  # noqa
    ##################################################
    "  - A parent instance to add this instance. If the specified value is None, this interface uses a stage instance.": "  - このインスタンスを追加する親のインスタンス。もしもNoneが指定された場合、このインスタンスはステージのインスタンスへと追加されます。",  # noqa
    ##################################################
    "- `variable_name_suffix`: str, optional": "- `variable_name_suffix`: str, optional",  # noqa
    ##################################################
    "  - A JavaScript variable name suffix string. This setting is sometimes useful for JavaScript debugging.": "  - JavaScript上の変数のサフィックスの設定です。この設定はJavaScriptのデバッグ時に役立つことがあります。",  # noqa
}
