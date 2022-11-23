"""This module is for the translation mapping data of the
following document:

Document file: graphics_draw_round_dotted_line.md
Language: jp
"""

from typing import Dict

MAPPING: Dict[str, str] = {
    ##################################################
    "# Graphics draw_round_dotted_line interface": "# Graphics クラスの draw_round_dotted_line インターフェイス",  # noqa
    ##################################################
    "This page explains the `Graphics` class `draw_round_dotted_line` method interface.": "このページでは`Graphics`クラスの`draw_round_dotted_line`メソッドのインターフェイスについて説明します。",  # noqa
    ##################################################
    "## What interface is this?": "## インターフェイス概要",
    ##################################################
    "`draw_round_dotted_line` interface draws the simple straight round dotted-line graphics. This interface ignores `dot_setting`\\, `dash_setting`\\, `round_dot_setting`\\, `dash_dot_setting`\\, and `cap` settings (this interface is using round cap setting so cap setting will also be ignored).": "`draw_round_dotted_line`インターフェイスはシンプルな丸ドットの直線のグラフィックスを描画します。このインターフェイスは`dot_setting`、`dash_setting`、`round_dot_setting`、`dash_dot_setting`、`cap`の各設定を無視します（このインターフェイスでは丸の`cap`設定を内部で使っているため`cap`設定は無視されます）。",  # noqa
    ##################################################
    "## Basic usage": "## 基本的な使い方",
    ##################################################
    "`draw_round_dotted_line` interface has basic coordinates arguments of `x_start`, `y_start`, `x_end` and `y_end`. That also has `round_size` and `space_size` arguments to determine the round style (line round size and the space size between each round).": "`draw_round_dotted_line`インターフェイスは基本的な座標指定の引数として`x_start`、`y_start`、`x_end`、`y_end`の引数を持っています。それらに加えて丸のサイズの`round_size`と丸の間のスペースを決定する`space_size`引数の指定が必要になります。",  # noqa
    ##################################################
    '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    background_color="#333", stage_width=250, stage_height=130, stage_elem_id="stage"\n)\nsprite: ap.Sprite = ap.Sprite()\n\n# Set 5-pixel round size and draw the line.\nsprite.graphics.line_style(color="#0af")\nsprite.graphics.draw_round_dotted_line(\n    x_start=50, y_start=50, x_end=200, y_end=50, round_size=5, space_size=5\n)\n\n# Set 10-pixel round size and draw the line.\nsprite.graphics.draw_round_dotted_line(\n    x_start=50, y_start=80, x_end=200, y_end=80, round_size=10, space_size=5\n)\n\nap.save_overall_html(dest_dir_path="graphics_draw_round_dotted_line_basic_usage/")\n```': '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    background_color="#333", stage_width=250, stage_height=130, stage_elem_id="stage"\n)\nsprite: ap.Sprite = ap.Sprite()\n\n# Set 5-pixel round size and draw the line.\nsprite.graphics.line_style(color="#0af")\nsprite.graphics.draw_round_dotted_line(\n    x_start=50, y_start=50, x_end=200, y_end=50, round_size=5, space_size=5\n)\n\n# Set 10-pixel round size and draw the line.\nsprite.graphics.draw_round_dotted_line(\n    x_start=50, y_start=80, x_end=200, y_end=80, round_size=10, space_size=5\n)\n\nap.save_overall_html(dest_dir_path="graphics_draw_round_dotted_line_basic_usage/")\n```',  # noqa
    ##################################################
    "## Notes": "## 特記事項",
    ##################################################
    "Since this interface uses the round cap setting, the line length becomes longer by the size of the cap.": "このインターフェイスは丸のcap（線の端のスタイル）設定を使用しているため、線の長さはcapのサイズに応じて大きくなります。",  # noqa
    ##################################################
    "If you want to align the left line position with other lines, subtract half-round size from the `x_start` argument.": "もしも線の左端を他の線と合わせたい場合には丸のサイズの半分を`x_start`の引数から減算してください。",  # noqa
    ##################################################
    '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    background_color="#333", stage_width=270, stage_height=130, stage_elem_id="stage"\n)\nsprite: ap.Sprite = ap.Sprite()\n\n# Set 5-pixel round size and draw the line.\nsprite.graphics.line_style(color="#0af")\nsprite.graphics.draw_round_dotted_line(\n    x_start=50, y_start=50, x_end=220, y_end=50, round_size=10, space_size=5\n)\n\n# Set 45-pixel (50 - half-round size) to x_start argument\n# and draw the normal line.\nsprite.graphics.draw_line(x_start=45, y_start=80, x_end=225, y_end=80)\n\nap.save_overall_html(dest_dir_path="graphics_draw_round_dotted_line_notes/")\n```': '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    background_color="#333", stage_width=270, stage_height=130, stage_elem_id="stage"\n)\nsprite: ap.Sprite = ap.Sprite()\n\n# Set 5-pixel round size and draw the line.\nsprite.graphics.line_style(color="#0af")\nsprite.graphics.draw_round_dotted_line(\n    x_start=50, y_start=50, x_end=220, y_end=50, round_size=10, space_size=5\n)\n\n# Set 45-pixel (50 - half-round size) to x_start argument\n# and draw the normal line.\nsprite.graphics.draw_line(x_start=45, y_start=80, x_end=225, y_end=80)\n\nap.save_overall_html(dest_dir_path="graphics_draw_round_dotted_line_notes/")\n```',  # noqa
    ##################################################
    "## draw_round_dotted_line API": "## draw_round_dotted_line API",
    ##################################################
    '<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>': '<span class="inconspicuous-txt">特記事項: このAPIドキュメントはドキュメントビルド用のスクリプトによって自動で生成・同期されています。そのためもしかしたらこの節の内容は前節までの内容と重複している場合があります。</span>',  # noqa
    ##################################################
    "**[Interface summary]**": "**[インターフェイス概要]**",
    ##################################################
    "Draw a round-dotted line vector graphics.<hr>": "丸ドットの直線のベクターグラフィックスを描画します。<hr>",
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
    "- `round_size`: Int or int": "- `round_size`: Int or int",
    ##################################################
    "  - Dot round size.": "  - 丸ドットのサイズ。",
    ##################################################
    "- `space_size`: Int or int": "- `space_size`: Int or int",
    ##################################################
    "  - Blank space size between dots.": "  - ドット間の空白のスペースのサイズ。",
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
    "This interface ignores line settings, like the `LineDotSetting`, except `LineRoundDotSetting`.<hr>": "このインターフェイスは`LineRoundDotSetting`を除いて`LineDotSetting`などの設定を無視します。<hr>",  # noqa
    ##################################################
    "**[Examples]**": "**[コードサンプル]**",
    ##################################################
    "```py\n>>> import apysc as ap\n>>> stage: ap.Stage = ap.Stage()\n>>> sprite: ap.Sprite = ap.Sprite()\n>>> sprite.graphics.line_style(color=\"#fff\", thickness=5)\n>>> line: ap.Line = sprite.graphics.draw_round_dotted_line(\n...     x_start=50, y_start=50, x_end=150, y_end=50, round_size=6, space_size=3\n... )\n>>> line.line_color\nString('#ffffff')\n\n>>> line.line_round_dot_setting.round_size\nInt(6)\n\n>>> line.line_round_dot_setting.space_size\nInt(3)\n```": "```py\n>>> import apysc as ap\n>>> stage: ap.Stage = ap.Stage()\n>>> sprite: ap.Sprite = ap.Sprite()\n>>> sprite.graphics.line_style(color=\"#fff\", thickness=5)\n>>> line: ap.Line = sprite.graphics.draw_round_dotted_line(\n...     x_start=50, y_start=50, x_end=150, y_end=50, round_size=6, space_size=3\n... )\n>>> line.line_color\nString('#ffffff')\n\n>>> line.line_round_dot_setting.round_size\nInt(6)\n\n>>> line.line_round_dot_setting.space_size\nInt(3)\n```",  # noqa
}
