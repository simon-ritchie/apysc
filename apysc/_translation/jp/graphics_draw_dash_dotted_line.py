"""This module is for the translation mapping data of the
following document:

Document file: graphics_draw_dash_dotted_line.md
Language: jp
"""

from typing import Dict

MAPPING: Dict[str, str] = {
    ##################################################
    "# Graphics draw_dash_dotted_line interface": "# Graphics クラスの draw_dash_dotted_line インターフェイス",  # noqa
    ##################################################
    "This page explains the `Graphics` class `draw_dash_dotted_line` method interface.": "このページでは`Graphics`クラスの`draw_dash_dotted_line`メソッドのインターフェイスについて説明します。",  # noqa
    ##################################################
    "## What interface is this?": "## インターフェイス概要",
    ##################################################
    "`draw_dash_dotted_line` interface draws the simple straight dash-dotted-line (also called 1-dot chain line or long dashed short dashed line) graphics.": "`draw_dash_dotted_line`インターフェイスはシンプルな一点鎖線の直線を描画します。",  # noqa
    ##################################################
    "This interface will ignore `dot_setting`, `dash_setting`, `round_dot_setting`, and `dash_dot_setting`.": "このインターフェイスは`dot_setting`や`dash_setting`、`round_dot_setting`、`dash_dot_setting`の引数や属性設定を無視します。",  # noqa
    ##################################################
    "## Basic usage": "## 基本的な使い方",
    ##################################################
    "`draw_dash_dotted_line` interface has basic coordinates arguments of `x_start`, `y_start`, `x_end` and `y_end`. That also has `dot_size` (the short dash size), `dash_size` (the long dash size), and `space_size` (the space size between each dash) arguments to determine line style.": "`draw_dash_dotted_line`インターフェイスは基本的な座標指定の引数として`x_start`、`y_start`、`x_end`、`y_end`の引数を持っています。加えて、短い点線部分のサイズとしての`dot_size`引数、長い破線部分のサイズとしての`dash_size`引数、そしてそれぞれの点線と破線の間のスペースとして`space_size`の引数が必要になります。",  # noqa
    ##################################################
    '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    background_color=ap.Color("#333"),\n    stage_width=250,\n    stage_height=130,\n    stage_elem_id="stage",\n)\nsprite: ap.Sprite = ap.Sprite()\n\n# Set 2-pixel dot size and 6-pixel dash size and draw the line.\nsprite.graphics.line_style(color=ap.Color("#0af"), thickness=5)\nsprite.graphics.draw_dash_dotted_line(\n    x_start=50, y_start=50, x_end=200, y_end=50, dot_size=2, dash_size=6, space_size=5\n)\n\n# Set 5-pixel dot size and 10-pixel dash size and draw the line.\nsprite.graphics.draw_dash_dotted_line(\n    x_start=50, y_start=80, x_end=200, y_end=80, dot_size=5, dash_size=10, space_size=5\n)\n\nap.save_overall_html(dest_dir_path="graphics_draw_dash_dotted_line_basic_usage/")\n```': '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    background_color=ap.Color("#333"),\n    stage_width=250,\n    stage_height=130,\n    stage_elem_id="stage",\n)\nsprite: ap.Sprite = ap.Sprite()\n\n# Set 2-pixel dot size and 6-pixel dash size and draw the line.\nsprite.graphics.line_style(color=ap.Color("#0af"), thickness=5)\nsprite.graphics.draw_dash_dotted_line(\n    x_start=50, y_start=50, x_end=200, y_end=50, dot_size=2, dash_size=6, space_size=5\n)\n\n# Set 5-pixel dot size and 10-pixel dash size and draw the line.\nsprite.graphics.draw_dash_dotted_line(\n    x_start=50, y_start=80, x_end=200, y_end=80, dot_size=5, dash_size=10, space_size=5\n)\n\nap.save_overall_html(dest_dir_path="graphics_draw_dash_dotted_line_basic_usage/")\n```',  # noqa
    ##################################################
    "## draw_dash_dotted_line API": "## draw_dash_dotted_line API",
    ##################################################
    '<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>': '<span class="inconspicuous-txt">特記事項: このAPIドキュメントはドキュメントビルド用のスクリプトによって自動で生成・同期されています。そのためもしかしたらこの節の内容は前節までの内容と重複している場合があります。</span>',  # noqa
    ##################################################
    "**[Interface summary]**": "**[インターフェイス概要]**",
    ##################################################
    "Draw a dash-dotted (1-dot chain) line vector graphics.<hr>": "一点鎖線のベクターグラフィックスの線を描画します。<hr>",  # noqa
    ##################################################
    "**[Parameters]**": "**[引数]**",
    ##################################################
    "- `x_start`: float or Number": "- `x_start`: float or Number",
    ##################################################
    "  - Line start x-coordinate.": "  - 線の開始位置のX座標。",
    ##################################################
    "- `y_start`: float or Number": "- `y_start`: float or Number",
    ##################################################
    "  - Line start y-coordinate.": "  - 線の開始位置のY座標。",
    ##################################################
    "- `x_end`: float or Number": "- `x_end`: float or Number",
    ##################################################
    "  - Line end x-coordinate.": "  - 線の終了位置のX座標。",
    ##################################################
    "- `y_end`: float or Number": "- `y_end`: float or Number",
    ##################################################
    "  - Line end y-coordinate.": "  - 線の終了位置のY座標。",
    ##################################################
    "- `dot_size`: Int or int": "- `dot_size`: Int or int",
    ##################################################
    "  - Dot size.": "  - ドットのサイズ。",
    ##################################################
    "- `dash_size`: Int or int": "- `dash_size`: Int or int",
    ##################################################
    "  - Dash size.": "  - 破線部分のサイズ。",
    ##################################################
    "- `space_size`: Int or int": "- `space_size`: Int or int",
    ##################################################
    "  - Blank space size between dots and dashes.": "  - ドット（点線）や破線間の空白スペースのサイズ。",
    ##################################################
    '- `variable_name_suffix`: str, default ""': '- `variable_name_suffix`: str, default ""',  # noqa
    ##################################################
    "  - A JavaScript variable name suffix string. This setting is sometimes useful for JavaScript debugging.": "  - JavaScript上の変数のサフィックスの設定です。この設定はJavaScriptのデバッグ時に役立つことがあります。",  # noqa
    ##################################################
    "<hr>": "<hr>",
    ##################################################
    "**[Returns]**": "**[返却値]**",
    ##################################################
    "- `line`: Line": "- `line`: Line",
    ##################################################
    "  - Created line graphics instance.": "  - 生成された線のグラフィックスのインスタンス。",
    ##################################################
    "<hr>": "<hr>",
    ##################################################
    "**[Examples]**": "**[コードサンプル]**",
    ##################################################
    '```py\n>>> import apysc as ap\n>>> stage: ap.Stage = ap.Stage()\n>>> sprite: ap.Sprite = ap.Sprite()\n>>> sprite.graphics.line_style(color=ap.Color("#fff"), thickness=5)\n>>> line: ap.Line = sprite.graphics.draw_dash_dotted_line(\n...     x_start=50,\n...     y_start=50,\n...     x_end=150,\n...     y_end=50,\n...     dot_size=2,\n...     dash_size=5,\n...     space_size=3,\n... )\n>>> line.line_color\nColor("#ffffff")\n\n>>> line.line_dash_dot_setting.dot_size\nInt(2)\n\n>>> line.line_dash_dot_setting.dash_size\nInt(5)\n\n>>> line.line_dash_dot_setting.space_size\nInt(3)\n```': '```py\n>>> import apysc as ap\n>>> stage: ap.Stage = ap.Stage()\n>>> sprite: ap.Sprite = ap.Sprite()\n>>> sprite.graphics.line_style(color=ap.Color("#fff"), thickness=5)\n>>> line: ap.Line = sprite.graphics.draw_dash_dotted_line(\n...     x_start=50,\n...     y_start=50,\n...     x_end=150,\n...     y_end=50,\n...     dot_size=2,\n...     dash_size=5,\n...     space_size=3,\n... )\n>>> line.line_color\nColor("#ffffff")\n\n>>> line.line_dash_dot_setting.dot_size\nInt(2)\n\n>>> line.line_dash_dot_setting.dash_size\nInt(5)\n\n>>> line.line_dash_dot_setting.space_size\nInt(3)\n```',  # noqa
}
