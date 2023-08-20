"""This module is for the translation mapping data of the
following document:

Document file: color.md
Language: jp
"""

from typing import Dict

MAPPING: Dict[str, str] = {
    ##################################################
    "# Color class": "# Color クラス",
    ##################################################
    "This page explains the `Color` class.": "このページでは`Color`クラスについて説明します。",
    ##################################################
    "## What class is this?": "## クラス概要",
    ##################################################
    "The `Color` class handles color settings.": "`Color`クラスの色の設定を扱います。",
    ##################################################
    "Color settings, such as the `fill_color` or `line_color` arguments or properties, require its value.": "色の設定、例えば`fill_color`や`line_color`などの引数や属性はこの値を必要とします。",  # noqa
    ##################################################
    "## Basic usage": "## 基本的な使い方",
    ##################################################
    "The constructor of the `Color` class requires a hexadecimal color code string, for example, `#00aaff`.": "`Color`クラスのコンストラクタでは例えば`#00aaff`などの16進数のカラーコードを必要とします。",  # noqa
    ##################################################
    "```py\n# runnable\nimport apysc as ap\n\nstage: ap.Stage = ap.Stage(\n    stage_width=250,\n    stage_height=150,\n    background_color=ap.Color(\"#333\"),\n    stage_elem_id=\"stage\",\n)\n\nleft_rectangle: ap.Rectangle = ap.Rectangle(\n    x=50,\n    y=50,\n    width=50,\n    height=50,\n    fill_color=ap.Color(\"#00aaff\"),\n)\n\nright_rectangle: ap.Rectangle = ap.Rectangle(\n    x=150,\n    y=50,\n    width=50,\n    height=50,\n    line_color=ap.Color(\"#ffffff\"),\n    line_thickness=3,\n)\n\nap.save_overall_html(dest_dir_path=\"./color_basic_usage/\")\n```": "```py\n# runnable\nimport apysc as ap\n\nstage: ap.Stage = ap.Stage(\n    stage_width=250,\n    stage_height=150,\n    background_color=ap.Color(\"#333\"),\n    stage_elem_id=\"stage\",\n)\n\nleft_rectangle: ap.Rectangle = ap.Rectangle(\n    x=50,\n    y=50,\n    width=50,\n    height=50,\n    fill_color=ap.Color(\"#00aaff\"),\n)\n\nright_rectangle: ap.Rectangle = ap.Rectangle(\n    x=150,\n    y=50,\n    width=50,\n    height=50,\n    line_color=ap.Color(\"#ffffff\"),\n    line_thickness=3,\n)\n\nap.save_overall_html(dest_dir_path=\"./color_basic_usage/\")\n```",  # noqa
    ##################################################
    "## Acceptable hexadecimal color codes": "## 受け付けられる16進数のカラーコード",
    ##################################################
    "Color code is acceptable like the following list:": "以下のようなカラーコードが受け付けられます:",
    ##################################################
    "- Six characters, e.g., `#00aaff`.": "- `#00aaff`などの6文字による指定。",
    ##################################################
    "- Three characters, e.g., `#0af` (this becomes `#00aaff`).": "- `#0af`などの3文字による指定（これは`#00aaff`と同じ値として扱われます）。",  # noqa
    ##################################################
    "- A single character, e.g., `#5` (this becomes `#000005`).": "- `#5`などの1文字による指定（これは`000005`と同じ値として扱われます）。",  # noqa
    ##################################################
    "- A skipped `#` symbol string, e.g., `0af` (this becomes `#00aaff`).": "- `0af`などの`#`記号を省略した指定（これは`#00aaff`と同じ値として扱われます）。",  # noqa
    ##################################################
    "- The `COLORLESS` constant (this setting clears a color setting).": "- `COLORLESS`定数（この設定は色の設定を削除します）。",  # noqa
    ##################################################
    "## Color constructor API": "## Color クラスのコンストラクタのAPI",
    ##################################################
    "<span class=\"inconspicuous-txt\">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>": "<span class=\"inconspicuous-txt\">特記事項: このAPIドキュメントはドキュメントビルド用のスクリプトによって自動で生成・同期されています。そのためもしかしたらこの節の内容は前節までの内容と重複している場合があります。</span>",  # noqa
    ##################################################
    "**[Interface summary]**": "**[インターフェイス概要]**",
    ##################################################
    "The color class implementation.<hr>": "色のクラスの実装です。<hr>",
    ##################################################
    "**[Parameters]**": "**[引数]**",
    ##################################################
    "- `value`: str or String": "- `value`: str or String",
    ##################################################
    "  - A hexadecimal color code string (e.g., \'#000000\').": "  - 16進数の色の文字列（例 : \'#000000\'）。",  # noqa
    ##################################################
    "- `variable_name_suffix`: str, default \'\'": "- `variable_name_suffix`: str, default \'\'",  # noqa
    ##################################################
    "  - A JavaScript variable name suffix string. This setting is sometimes useful for JavaScript debugging.": "  - JavaScript上の変数のサフィックスの設定です。この設定はJavaScriptのデバッグ時に役立つことがあります。",  # noqa
}
