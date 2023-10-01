"""This module is for the translation mapping data of the
following document:

Document file: graphics_draw_dashed_line.md
Language: jp
"""

from typing import Dict

MAPPING: Dict[str, str] = {
    ##################################################
    "# Graphics draw_dashed_line interface": "# Graphics クラスの draw_dashed_line インターフェイス",  # noqa
    ##################################################
    "This page explains the `Graphics` class `draw_dashed_line` method interface.": "このページでは`Graphics`クラスの`draw_dashed_line`メソッドのインターフェイスについて説明します。",  # noqa
    ##################################################
    "## What interface is this?": "## インターフェイス概要",
    ##################################################
    "`draw_dashed_line` interface will draw the simple straight dashed-line graphics. This interface will ignore `dot_setting`, `dash_setting`, `round_dot_setting`, and `dash_dot_setting`.": "`draw_dashed_line`インターフェイスはシンプルな破線の直線のグラフィックスを描画します。このインターフェイスは`dot_setting`や`dash_setting`、`round_dot_setting`、`dash_dot_setting`の引数や属性の設定を無視します。",  # noqa
    ##################################################
    "## Basic usage": "## 基本的な使い方",
    ##################################################
    "`draw_dashed_line` interface has basic coordinates arguments of `x_start`, `y_start`, `x_end` and `y_end`. That also has `dash_size` and `space_size` arguments to determine dash style (line dash size and the space size between each dash).": "`draw_dashed_line`インターフェイスは基本的な線の座標の指定として`x_start`、`y_start`、`x_end`、`y_end`の各引数を持ちます。加えて、破線のサイズとしての`dash_size`引数と破線間のスペースのサイズとしての`space_size`引数の指定が必要です。",  # noqa
    ##################################################
    '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    background_color=ap.Color("#333"),\n    stage_width=250,\n    stage_height=130,\n    stage_elem_id="stage",\n)\nsprite: ap.Sprite = ap.Sprite()\n\n# Set 5-pixel dash setting and draw the line.\nsprite.graphics.line_style(color=ap.Color("#0af"), thickness=2)\nsprite.graphics.draw_dashed_line(\n    x_start=50, y_start=50, x_end=200, y_end=50, dash_size=5, space_size=2\n)\n\n# Set 10-pixel dash setting and draw the line.\nsprite.graphics.draw_dashed_line(\n    x_start=50, y_start=80, x_end=200, y_end=80, dash_size=10, space_size=2\n)\n\nap.save_overall_html(dest_dir_path="graphics_draw_dashed_line_basic_usage/")\n```': '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    background_color=ap.Color("#333"),\n    stage_width=250,\n    stage_height=130,\n    stage_elem_id="stage",\n)\nsprite: ap.Sprite = ap.Sprite()\n\n# Set 5-pixel dash setting and draw the line.\nsprite.graphics.line_style(color=ap.Color("#0af"), thickness=2)\nsprite.graphics.draw_dashed_line(\n    x_start=50, y_start=50, x_end=200, y_end=50, dash_size=5, space_size=2\n)\n\n# Set 10-pixel dash setting and draw the line.\nsprite.graphics.draw_dashed_line(\n    x_start=50, y_start=80, x_end=200, y_end=80, dash_size=10, space_size=2\n)\n\nap.save_overall_html(dest_dir_path="graphics_draw_dashed_line_basic_usage/")\n```',  # noqa
    ##################################################
    "## draw_dashed_line API": "## draw_dashed_line API",
    ##################################################
    '<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>': '<span class="inconspicuous-txt">特記事項: このAPIドキュメントはドキュメントビルド用のスクリプトによって自動で生成・同期されています。そのためもしかしたらこの節の内容は前節までの内容と重複している場合があります。</span>',  # noqa
    ##################################################
    "**[Interface summary]**": "**[インターフェイス概要]**",
    ##################################################
    "Draw a dashed line vector graphics.<hr>": "破線のベクターグラフィックスを描画します。<hr>",
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
    "- `dash_size`: Int or int": "- `dash_size`: Int or int",
    ##################################################
    "  - Dash size.": "  - 破線部分のサイズ。",
    ##################################################
    "- `space_size`: Int or int": "- `space_size`: Int or int",
    ##################################################
    "  - Blank space size between dashes.": "  - 破線間の空白スペースのサイズ。",
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
    "**[Notes]**": "**[特記事項]**",
    ##################################################
    " ・This interface ignores line settings, like the `LineDotSetting`, except `LineDashSetting`.<hr>": " ・このインターフェイスは`LineDashSetting`を除いた`LineDotSetting`などの線のスタイル設定を無視します。<hr>",  # noqa
    ##################################################
    "**[Examples]**": "**[コードサンプル]**",
    ##################################################
    '```py\n>>> import apysc as ap\n>>> stage: ap.Stage = ap.Stage()\n>>> sprite: ap.Sprite = ap.Sprite()\n>>> sprite.graphics.line_style(color=ap.Color("#fff"), thickness=5)\n>>> line: ap.Line = sprite.graphics.draw_dashed_line(\n...     x_start=50, y_start=50, x_end=150, y_end=50, dash_size=5, space_size=2\n... )\n>>> line.line_color\nColor("#ffffff")\n\n>>> line.line_dash_setting.dash_size\nInt(5)\n\n>>> line.line_dash_setting.space_size\nInt(2)\n```': '```py\n>>> import apysc as ap\n>>> stage: ap.Stage = ap.Stage()\n>>> sprite: ap.Sprite = ap.Sprite()\n>>> sprite.graphics.line_style(color=ap.Color("#fff"), thickness=5)\n>>> line: ap.Line = sprite.graphics.draw_dashed_line(\n...     x_start=50, y_start=50, x_end=150, y_end=50, dash_size=5, space_size=2\n... )\n>>> line.line_color\nColor("#ffffff")\n\n>>> line.line_dash_setting.dash_size\nInt(5)\n\n>>> line.line_dash_setting.space_size\nInt(2)\n```',  # noqa
}
