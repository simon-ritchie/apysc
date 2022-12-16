"""This module is for the translation mapping data of the
following document:

Document file: graphics_draw_dotted_line.md
Language: jp
"""

from typing import Dict

MAPPING: Dict[str, str] = {
    ##################################################
    "# Graphics draw_dotted_line interface": "# Graphics クラスの draw_dotted_line インターフェイス",  # noqa
    ##################################################
    "This page explains the `Graphics` class `draw_dotted_line` method interface.": "このページでは`Graphics`クラスの`draw_dotted_line`メソッドのインターフェイスについて説明します。",  # noqa
    ##################################################
    "## What interface is this?": "## インターフェイス概要",
    ##################################################
    "`draw_dotted_line` interface will draw the simple straight dotted-line graphics. This interface will ignore `dot_setting`, `dash_setting`, `round_dot_setting`, and `dash_dot_setting`.": "`draw_dotted_line`インターフェイスはシンプルな点線の直線のグラフィックスを描画します。このインターフェイスは`dot_setting`、`dash_setting`、`round_dot_setting`、`dash_dot_setting`の引数や属性の設定を無視します。",  # noqa
    ##################################################
    "## Basic usage": "## 基本的な使い方",
    ##################################################
    "`draw_dotted_line` interface has basic coordinates arguments of `x_start`, `y_start`, `x_end` and `y_end`. That also has `dot_size` argument and it will set line dot size.": "`draw_dotted_line`インターフェイスは基本的な線の座標の指定として`x_start`、`y_start`、`x_end`、`y_end`の各引数を持ちます。また、点線のサイズとして`dot_size`引数の指定が必要です。",  # noqa
    ##################################################
    '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    background_color="#333", stage_width=250, stage_height=130, stage_elem_id="stage"\n)\nsprite: ap.Sprite = ap.Sprite()\n\n# Set 2-pixel dot size and draw line.\nsprite.graphics.line_style(color="#0af", thickness=2)\nsprite.graphics.draw_dotted_line(\n    x_start=50, y_start=50, x_end=200, y_end=50, dot_size=2\n)\n\n# Set 5-pixel dot size and draw line.\nsprite.graphics.line_style(color="#0af", thickness=2)\nsprite.graphics.draw_dotted_line(\n    x_start=50, y_start=80, x_end=200, y_end=80, dot_size=5\n)\n\nap.save_overall_html(dest_dir_path="graphics_draw_dotted_line_basic_usage/")\n```': '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    background_color="#333", stage_width=250, stage_height=130, stage_elem_id="stage"\n)\nsprite: ap.Sprite = ap.Sprite()\n\n# Set 2-pixel dot size and draw line.\nsprite.graphics.line_style(color="#0af", thickness=2)\nsprite.graphics.draw_dotted_line(\n    x_start=50, y_start=50, x_end=200, y_end=50, dot_size=2\n)\n\n# Set 5-pixel dot size and draw line.\nsprite.graphics.line_style(color="#0af", thickness=2)\nsprite.graphics.draw_dotted_line(\n    x_start=50, y_start=80, x_end=200, y_end=80, dot_size=5\n)\n\nap.save_overall_html(dest_dir_path="graphics_draw_dotted_line_basic_usage/")\n```',  # noqa
    ##################################################
    "## draw_dotted_line API": "## draw_dotted_line API",
    ##################################################
    '<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>': '<span class="inconspicuous-txt">特記事項: このAPIドキュメントはドキュメントビルド用のスクリプトによって自動で生成・同期されています。そのためもしかしたらこの節の内容は前節までの内容と重複している場合があります。</span>',  # noqa
    ##################################################
    "**[Interface summary]**": "**[インターフェイス概要]**",
    ##################################################
    "Draw a dotted line vector graphics.<hr>": "点線のベクターグラフィックスを描画します。<hr>",
    ##################################################
    "**[Parameters]**": "**[引数]**",
    ##################################################
    "- `x_start`: Int or int": "- `x_start`: Int or int",
    ##################################################
    "  - Line start x-coordinate.": "  - 線の開始位置のX座標。",
    ##################################################
    "- `y_start`: Int or int": "- `y_start`: Int or int",
    ##################################################
    "  - Line start y-coordinate.": "  - 線の開始位置のY座標。",
    ##################################################
    "- `x_end`: Int or int": "- `x_end`: Int or int",
    ##################################################
    "  - Line end x-coordinate.": "  - 線の終了位置のX座標。",
    ##################################################
    "- `y_end`: Int or int": "- `y_end`: Int or int",
    ##################################################
    "  - Line end y-coordinate.": "  - 線の終了位置のY座標。",
    ##################################################
    "- `dot_size`: Int or int": "- `dot_size`: Int or int",
    ##################################################
    "  - Dot size.": "  - ドットのサイズ。",
    ##################################################
    "- `variable_name_suffix`: str, default ''": "- `variable_name_suffix`: str, default ''",  # noqa
    ##################################################
    "  - A JavaScript variable name suffix string. This setting is sometimes useful for JavaScript's debugging.": "  - JavaScript上の変数のサフィックスの設定です。この設定はJavaScriptのデバッグ時に役立つことがあります。",  # noqa
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
    " ・This interface ignores line settings, like the `LineDashSetting`, except `LineDotSetting`.<hr>": " ・このインターフェイスは`LineDotSetting`を除いた`LineDashSetting`などの線のスタイル設定を無視します。<hr>",  # noqa
    ##################################################
    "**[Examples]**": "**[コードサンプル]**",
    ##################################################
    "```py\n>>> import apysc as ap\n>>> stage: ap.Stage = ap.Stage()\n>>> sprite: ap.Sprite = ap.Sprite()\n>>> sprite.graphics.line_style(color=\"#fff\", thickness=5)\n>>> line: ap.Line = sprite.graphics.draw_dotted_line(\n...     x_start=50, y_start=50, x_end=150, y_end=50, dot_size=5\n... )\n>>> line.line_color\nString('#ffffff')\n\n>>> line.line_thickness\nInt(5)\n\n>>> line.line_dot_setting.dot_size\nInt(5)\n```": "```py\n>>> import apysc as ap\n>>> stage: ap.Stage = ap.Stage()\n>>> sprite: ap.Sprite = ap.Sprite()\n>>> sprite.graphics.line_style(color=\"#fff\", thickness=5)\n>>> line: ap.Line = sprite.graphics.draw_dotted_line(\n...     x_start=50, y_start=50, x_end=150, y_end=50, dot_size=5\n... )\n>>> line.line_color\nString('#ffffff')\n\n>>> line.line_thickness\nInt(5)\n\n>>> line.line_dot_setting.dot_size\nInt(5)\n```",  # noqa
}
