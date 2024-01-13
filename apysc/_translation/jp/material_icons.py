"""This module is for the translation mapping data of the
following document:

Document file: material_icons.md
Language: jp
"""

from typing import Dict

MAPPING: Dict[str, str] = {
    ##################################################
    "# Material icons": "# マテリアルデザインアイコン",
    ##################################################
    "This page explains the material icon-related implementations of apysc.": "このページではapyscでのマテリアルデザインのアイコンに関係した実装について説明します。",  # noqa
    ##################################################
    "## Implementation overview": "## 実装の概要",
    ##################################################
    "Each material icon class name becomes the `Material<icon_name>Icon`, for instance, `MaterialSearchIcon` or `MaterialAccountCircleIcon`.": "各マテリアルデザインのアイコンのクラス名は例えば`MaterialSearchIcon`や`MaterialAccountCircleIcon`といったように`Material<アイコン名>Icon`という形式になります。",  # noqa
    ##################################################
    "You can use these icon classes similar to the other graphics classes, such as the `Rectangle` or `Circle`.": "これらのアイコンのクラスは`Rectangle`や`Circle`などの他のグラフィックス用の各クラスと同様に使用することができます。",  # noqa
    ##################################################
    "## Basic usage": "## 基本的な使い方",
    ##################################################
    '```py\n# runnable\nimport apysc as ap\n\nMARGIN: int = 20\nICON_SIZE: int = 24\nICON_NUM: int = 3\nstage: ap.Stage = ap.Stage(\n    background_color=ap.Color("#333"),\n    stage_width=MARGIN * 2 + ICON_SIZE * ICON_NUM + MARGIN * 2,\n    stage_height=MARGIN + ICON_SIZE + MARGIN,\n    stage_elem_id="stage",\n)\n\nsearch_icon: ap.MaterialSearchIcon = ap.MaterialSearchIcon(\n    fill_color=ap.Colors.GRAY_AAAAAA,\n    x=MARGIN,\n    y=MARGIN,\n    width=ICON_SIZE,\n    height=ICON_SIZE,\n)\ninfo_icon: ap.MaterialInfoIcon = ap.MaterialInfoIcon(\n    fill_color=ap.Colors.CYAN_00FFFF,\n    x=MARGIN + ICON_SIZE + MARGIN,\n    y=MARGIN,\n    width=ICON_SIZE,\n    height=ICON_SIZE,\n)\nhome_icon: ap.MaterialHomeIcon = ap.MaterialHomeIcon(\n    fill_color=ap.Colors.MAGENTA_FF00FF,\n    x=MARGIN + (ICON_SIZE + MARGIN) * 2,\n    y=MARGIN,\n    width=ICON_SIZE,\n    height=ICON_SIZE,\n)\n\nap.save_overall_html(dest_dir_path="./material_icons_basic_usage/")\n```': '```py\n# runnable\nimport apysc as ap\n\nMARGIN: int = 20\nICON_SIZE: int = 24\nICON_NUM: int = 3\nstage: ap.Stage = ap.Stage(\n    background_color=ap.Color("#333"),\n    stage_width=MARGIN * 2 + ICON_SIZE * ICON_NUM + MARGIN * 2,\n    stage_height=MARGIN + ICON_SIZE + MARGIN,\n    stage_elem_id="stage",\n)\n\nsearch_icon: ap.MaterialSearchIcon = ap.MaterialSearchIcon(\n    fill_color=ap.Colors.GRAY_AAAAAA,\n    x=MARGIN,\n    y=MARGIN,\n    width=ICON_SIZE,\n    height=ICON_SIZE,\n)\ninfo_icon: ap.MaterialInfoIcon = ap.MaterialInfoIcon(\n    fill_color=ap.Colors.CYAN_00FFFF,\n    x=MARGIN + ICON_SIZE + MARGIN,\n    y=MARGIN,\n    width=ICON_SIZE,\n    height=ICON_SIZE,\n)\nhome_icon: ap.MaterialHomeIcon = ap.MaterialHomeIcon(\n    fill_color=ap.Colors.MAGENTA_FF00FF,\n    x=MARGIN + (ICON_SIZE + MARGIN) * 2,\n    y=MARGIN,\n    width=ICON_SIZE,\n    height=ICON_SIZE,\n)\n\nap.save_overall_html(dest_dir_path="./material_icons_basic_usage/")\n```',  # noqa
    ##################################################
    "## Each material icon constructor API": "## 各マテリアルアイコンのコンストラクタのAPI",
    ##################################################
    '<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>': '<span class="inconspicuous-txt">特記事項: このAPIドキュメントはドキュメントビルド用のスクリプトによって自動で生成・同期されています。そのためもしかしたらこの節の内容は前節までの内容と重複している場合があります。</span>',  # noqa
    ##################################################
    "**[Interface summary]**": "**[インターフェイス概要]**",
    ##################################################
    "Create a material icon.<hr>": "マテリアルデザインのアイコンを作成します。<hr>",
    ##################################################
    "**[Parameters]**": "**[引数]**",
    ##################################################
    "- `fill_color`: Color": "- `fill_color`: Color",
    ##################################################
    "  - An icon fill-color.": "  - アイコンの塗りの色。",
    ##################################################
    "- `fill_alpha`: Union[float, Number], optional": "- `fill_alpha`: Union[float, Number], optional",  # noqa
    ##################################################
    "  - An icon fill-alpha (opacity).": "  - アイコンの塗りの透明度。",
    ##################################################
    "- `x`: Union[float, Number], optional": "- `x`: Union[float, Number], optional",
    ##################################################
    "  - An icon x-coordinate.": "  - アイコンのX座標。",
    ##################################################
    "- `y`: Union[float, Number], optional": "- `y`: Union[float, Number], optional",
    ##################################################
    "  - An icon y-coordinate.": "  - アイコンのY座標。",
    ##################################################
    "- `width`: Union[int, Int], optional": "- `width`: Union[int, Int], optional",
    ##################################################
    "  - An icon width.": "  - アイコンの幅。",
    ##################################################
    "- `height`: Union[int, Int], optional": "- `height`: Union[int, Int], optional",
    ##################################################
    "  - An icon height.": "  - アイコンの高さ。",
    ##################################################
    "- `parent`: ChildMixIn or None, default None": "- `parent`: ChildMixIn or None, default None",  # noqa
    ##################################################
    "  - A parent instance to add this instance. If the specified value is None, this interface uses a stage instance.": "  - このインスタンスを追加する親のインスタンス。もしもNoneが指定された場合、このインスタンスはステージのインスタンスへと追加されます。",  # noqa
    ##################################################
    "- `variable_name_suffix`: str, optional": "- `variable_name_suffix`: str, optional",  # noqa
    ##################################################
    "  - A JavaScript variable name suffix string. This setting is sometimes useful for JavaScript debugging.": "  - JavaScript上の変数のサフィックスの設定です。この設定はJavaScriptのデバッグ時に役立つことがあります。",  # noqa
    ##################################################
    "<hr>": "<hr>",
    ##################################################
    "**[References]**": "**[関連資料]**",
    ##################################################
    "- [Material icons](https://fonts.google.com/icons?selected=Material+Icons:search:)": "- [Material icons](https://fonts.google.com/icons?selected=Material+Icons:search:)",  # noqa
    ##################################################
    "- [APACHE LICENSE, VERSION 2.0](https://www.apache.org/licenses/LICENSE-2.0.html)": "- [APACHE LICENSE, VERSION 2.0](https://www.apache.org/licenses/jp_LICENSE-2.0.html)",  # noqa
}
