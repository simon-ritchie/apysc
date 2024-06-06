"""This module is for the translation mapping data of the
following document:

Document file: color_from_rgb.md
Language: jp
"""

from typing import Dict

MAPPING: Dict[str, str] = {
    ##################################################
    "# Color class from_rgb class method": "# Color クラスの from_rgb クラスメソッド",
    ##################################################
    "This pace explains the `Color` class `from_rgb` class method.": "このページでは`Color`クラスの`from_rgb`クラスメソッドについて説明します。",  # noqa
    ##################################################
    "## What class method is this?": "## クラスメソッド概要",
    ##################################################
    "The `from_rgb` class method creates a new color instance from red, green and blue integer (0 to 255, 8bit unsigned integer range).": "`from_rgs`クラスメソッドは赤緑青の3色の指定から新たな色のインスタンスを作成します（0～255の8bitの正の整数の範囲を受け付けます）。",  # noqa
    ##################################################
    "## Basic usage": "## 基本的な使い方",
    ##################################################
    "The `from_rgb` class method requires the `red`, `green`, and `blue` arguments (`int` or `ap.Int` type value).": "`from_rgb`クラスメソッドは`red`、`green`、`blue`の各引数を必要とします（`int`もしくは`ap.Int`型の値）。",  # noqa
    ##################################################
    "Its class method returns a new color instance.": "このクラスメソッドは新たな色のインスタンスを返します。",
    ##################################################
    '```py\n# runnable\n\nimport apysc as ap\n\nap.Stage(\n    stage_width=350,\n    stage_height=150,\n    background_color=ap.Color("#333"),\n    stage_elem_id="stage",\n)\n\nblack_color: ap.Color = ap.Color.from_rgb(red=0, green=0, blue=0)\nblack_rectangle: ap.Rectangle = ap.Rectangle(\n    x=50,\n    y=50,\n    width=50,\n    height=50,\n    fill_color=black_color,\n)\n\nwhite_color: ap.Color = ap.Color.from_rgb(red=255, green=255, blue=255)\nwhite_rectangle: ap.Rectangle = ap.Rectangle(\n    x=150,\n    y=50,\n    width=50,\n    height=50,\n    fill_color=white_color,\n)\n\ncyan_color: ap.Color = ap.Color.from_rgb(red=0, green=128, blue=255)\ncyan_rectangle: ap.Rectangle = ap.Rectangle(\n    x=250,\n    y=50,\n    width=50,\n    height=50,\n    fill_color=cyan_color,\n)\n\nap.save_overall_html(dest_dir_path="color_from_rgb_basic_usage/")\n```': '```py\n# runnable\n\nimport apysc as ap\n\nap.Stage(\n    stage_width=350,\n    stage_height=150,\n    background_color=ap.Color("#333"),\n    stage_elem_id="stage",\n)\n\nblack_color: ap.Color = ap.Color.from_rgb(red=0, green=0, blue=0)\nblack_rectangle: ap.Rectangle = ap.Rectangle(\n    x=50,\n    y=50,\n    width=50,\n    height=50,\n    fill_color=black_color,\n)\n\nwhite_color: ap.Color = ap.Color.from_rgb(red=255, green=255, blue=255)\nwhite_rectangle: ap.Rectangle = ap.Rectangle(\n    x=150,\n    y=50,\n    width=50,\n    height=50,\n    fill_color=white_color,\n)\n\ncyan_color: ap.Color = ap.Color.from_rgb(red=0, green=128, blue=255)\ncyan_rectangle: ap.Rectangle = ap.Rectangle(\n    x=250,\n    y=50,\n    width=50,\n    height=50,\n    fill_color=cyan_color,\n)\n\nap.save_overall_html(dest_dir_path="color_from_rgb_basic_usage/")\n```',  # noqa
    ##################################################
    "## from_rgb class method API": "## from_rgb クラスメソッドのAPI",
    ##################################################
    '<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>': '<span class="inconspicuous-txt">特記事項: このAPIドキュメントはドキュメントビルド用のスクリプトによって自動で生成・同期されています。そのためもしかしたらこの節の内容は前節までの内容と重複している場合があります。</span>',  # noqa
    ##################################################
    "**[Interface summary]**": "**[インターフェイス概要]**",
    ##################################################
    "Create a color instance from RGB (red, green, and blue) values.<hr>": "RGB（赤、緑、青）の値から色のインスタンスを生成します。<hr>",  # noqa
    ##################################################
    "**[Parameters]**": "**[引数]**",
    ##################################################
    "- `red`: Union[int, Int]": "- `red`: Union[int, Int]",
    ##################################################
    "  - A red color value (0 to 255).": "  - 赤色の値（0～255）。",
    ##################################################
    "- `green`: Union[int, Int]": "- `green`: Union[int, Int]",
    ##################################################
    "  - A green color value (0 to 255).": "  - 緑色の値（0～255）。",
    ##################################################
    "- `blue`: Union[int, Int]": "- `blue`: Union[int, Int]",
    ##################################################
    "  - A blue color value (0 to 255).": "  - 青色の値（0～255）。",
    ##################################################
    '- `variable_name_suffix`: str, default ""': '- `variable_name_suffix`: str, default ""',  # noqa
    ##################################################
    "  - A JavaScript variable name suffix string. This setting is sometimes useful for JavaScript debugging.": "  - JavaScript上の変数のサフィックスの設定です。この設定はJavaScriptのデバッグ時に役立つことがあります。",  # noqa
    ##################################################
    "<hr>": "<hr>",
    ##################################################
    "**[Returns]**": "**[返却値]**",
    ##################################################
    "- `color`: Color": "- `color`: Color",
    ##################################################
    "  - A created color instance.": "  - 作成された色のインスタンス。",
    ##################################################
    "<hr>": "<hr>",
    ##################################################
    "**[Examples]**": "**[コードサンプル]**",
    ##################################################
    '```py\n>>> import apysc as ap\n>>> color: ap.Color = ap.Color.from_rgb(red=0, green=255, blue=0)\n>>> color\nColor("#00FF00")\n```': '```py\n>>> import apysc as ap\n>>> color: ap.Color = ap.Color.from_rgb(red=0, green=255, blue=0)\n>>> color\nColor("#00FF00")\n```',  # noqa
    ##################################################
    "<hr>": "<hr>",
    ##################################################
    "**[References]**": "**[関連資料]**",
    ##################################################
    "- [Color class](https://simon-ritchie.github.io/apysc/en/color.html)": "- [Color クラス](https://simon-ritchie.github.io/apysc/jp/jp_color.html)",  # noqa
}
