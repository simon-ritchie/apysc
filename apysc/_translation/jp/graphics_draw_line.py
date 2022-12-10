"""This module is for the translation mapping data of the
following document:

Document file: graphics_draw_line.md
Language: jp
"""

from typing import Dict

MAPPING: Dict[str, str] = {
    ##################################################
    "# Graphics draw_line interface": "# Graphics クラスの draw_line インターフェイス",
    ##################################################
    "This page explains the `Graphics` class `draw_line` method interface.": "このページでは`Graphics`クラスの`draw_line`メソッドのインターフェイスについて説明します。",  # noqa
    ##################################################
    "## What interface is this?": "## インターフェイス概要",
    ##################################################
    "`draw_line` interface will draw the simple straight line graphics. This interface will ignore `dot_setting`, `dash_setting`, `round_dot_setting`, and `dash_dot_setting`.": "`draw_line`インターフェイスはシンプルな直線のグラフィックスを描画します。このインターフェイスは`dot_setting`、`dash_setting`、`round_dot_setting`、`dash_dot_setting`などの引数や属性の設定を無視します。",  # noqa
    ##################################################
    "## Basic usage": "## 基本的な使い方",
    ##################################################
    "`draw_line` inteface has `x_start` (line x-start coordinate), `y_start` (line y-start coordinate), `x_end` (line x-end coordinate), and `y_end` (line y-end coordinate) arguments.": "`draw_line`インターフェイスは`x_start`（線の開始位置のX座標）、`y_start`（線の開始位置のY座標）、`x_end`（線の終了位置のX座標）、`y_end`（線の終了位置のY座標）の各引数を必要とします。",  # noqa
    ##################################################
    '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    background_color="#333", stage_width=200, stage_height=100, stage_elem_id="stage"\n)\nsprite: ap.Sprite = ap.Sprite()\n\nsprite.graphics.line_style(color="#0af", thickness=5)\nsprite.graphics.draw_line(x_start=50, y_start=50, x_end=150, y_end=50)\n\nap.save_overall_html(dest_dir_path="graphics_draw_line_basic_usage/")\n```': '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    background_color="#333", stage_width=200, stage_height=100, stage_elem_id="stage"\n)\nsprite: ap.Sprite = ap.Sprite()\n\nsprite.graphics.line_style(color="#0af", thickness=5)\nsprite.graphics.draw_line(x_start=50, y_start=50, x_end=150, y_end=50)\n\nap.save_overall_html(dest_dir_path="graphics_draw_line_basic_usage/")\n```',  # noqa
    ##################################################
    "## Ignored line style settings": "## 無視される線のスタイル設定",
    ##################################################
    "This interface will ignore `dot_setting`, `dash_setting`, `round_dot_setting`, and `dash_dot_setting` for simplicity. If you need to draw these styled lines, then use `draw_dotted_line`, `draw_dashed_line`, `draw_round_dotted_line`, or `draw_dash_dotted_line` interfaces instead of the `draw_line` interface.": "このインターフェイスはインターフェイスのシンプルさのために`dot_setting`、`dash_setting`、`round_dot_setting`、`dash_dot_setting`の各設定を無視します。もしもこれらのスタイル設定が必要な場合には`draw_line`インターフェイスの代わりに`draw_dotted_line`、`draw_dashed_line`、`draw_round_dotted_line`、`draw_dash_dotted_line`などのインターフェイスを仕様してください。",  # noqa
    ##################################################
    '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    background_color="#333", stage_width=200, stage_height=100, stage_elem_id="stage"\n)\nsprite: ap.Sprite = ap.Sprite()\n\n# dot_setting will be ignored, and the result line will not be dotted.\nsprite.graphics.line_style(\n    color="#0af", thickness=5, dot_setting=ap.LineDotSetting(dot_size=5)\n)\nsprite.graphics.draw_line(x_start=50, y_start=50, x_end=150, y_end=50)\n\nap.save_overall_html(dest_dir_path="graphics_draw_line_ignored_dot_setting/")\n```': '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    background_color="#333", stage_width=200, stage_height=100, stage_elem_id="stage"\n)\nsprite: ap.Sprite = ap.Sprite()\n\n# dot_setting will be ignored, and the result line will not be dotted.\nsprite.graphics.line_style(\n    color="#0af", thickness=5, dot_setting=ap.LineDotSetting(dot_size=5)\n)\nsprite.graphics.draw_line(x_start=50, y_start=50, x_end=150, y_end=50)\n\nap.save_overall_html(dest_dir_path="graphics_draw_line_ignored_dot_setting/")\n```',  # noqa
    ##################################################
    "## Line class instance": "## Line クラスのインスタンス",
    ##################################################
    "`draw_line` interface returns the `Line` instance. You can update each setting or bind events to that instance. `draw_dotted_line`, `draw_dashed_line`, `draw_round_dotted_line`\n, and `draw_dash_dotted_line` will also return the same type instance.": "`draw_line`インターフェイスは`Line`クラスのインスタンスを返却します。そのインスタンスの各種設定を変更したりイベントを登録したり等を行うことができます。`draw_dotted_line`、`draw_dashed_line`、`draw_round_dotted_line`、`draw_dash_dotted_line`などのインターフェイスも同じく`Line`クラスのインスタンスを返却します。",  # noqa
    ##################################################
    '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    background_color="#333", stage_width=200, stage_height=100, stage_elem_id="stage"\n)\nsprite: ap.Sprite = ap.Sprite()\n\nsprite.graphics.line_style(color="#0af", thickness=5)\nline: ap.Line = sprite.graphics.draw_line(x_start=50, y_start=50, x_end=150, y_end=50)\n\n# Update the line color from cyan to magenta.\nline.line_color = ap.String("#f0a")\n\nap.save_overall_html(dest_dir_path="graphics_draw_line_line_instance/")\n```': '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    background_color="#333", stage_width=200, stage_height=100, stage_elem_id="stage"\n)\nsprite: ap.Sprite = ap.Sprite()\n\nsprite.graphics.line_style(color="#0af", thickness=5)\nline: ap.Line = sprite.graphics.draw_line(x_start=50, y_start=50, x_end=150, y_end=50)\n\n# Update the line color from cyan to magenta.\nline.line_color = ap.String("#f0a")\n\nap.save_overall_html(dest_dir_path="graphics_draw_line_line_instance/")\n```',  # noqa
    ##################################################
    "## draw_line API": "## draw_line API",
    ##################################################
    '<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>': '<span class="inconspicuous-txt">特記事項: このAPIドキュメントはドキュメントビルド用のスクリプトによって自動で生成・同期されています。そのためもしかしたらこの節の内容は前節までの内容と重複している場合があります。</span>',  # noqa
    ##################################################
    "**[Interface summary]**": "**[インターフェイス概要]**",
    ##################################################
    "Draw a normal line vector graphic.<hr>": "通常の直線のベクターグラフィックスを描画します。<hr>",
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
    " ・This interface ignores line settings, like the `LineDotSetting`, `LineDashSetting`.<hr>": " ・このインターフェイスは`LineDotSetting`や`LineDashSetting`などの設定を無視します。<hr>",  # noqa
    ##################################################
    "**[Examples]**": "**[コードサンプル]**",
    ##################################################
    "```py\n>>> import apysc as ap\n>>> stage: ap.Stage = ap.Stage()\n>>> sprite: ap.Sprite = ap.Sprite()\n>>> sprite.graphics.line_style(color=\"#fff\", thickness=5)\n>>> line: ap.Line = sprite.graphics.draw_line(\n...     x_start=50, y_start=50, x_end=150, y_end=50\n... )\n>>> line.line_color\nString('#ffffff')\n\n>>> line.line_thickness\nInt(5)\n```": "```py\n>>> import apysc as ap\n>>> stage: ap.Stage = ap.Stage()\n>>> sprite: ap.Sprite = ap.Sprite()\n>>> sprite.graphics.line_style(color=\"#fff\", thickness=5)\n>>> line: ap.Line = sprite.graphics.draw_line(\n...     x_start=50, y_start=50, x_end=150, y_end=50\n... )\n>>> line.line_color\nString('#ffffff')\n\n>>> line.line_thickness\nInt(5)\n```",  # noqa
}
