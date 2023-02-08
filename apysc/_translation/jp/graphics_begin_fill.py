"""This module is for the translation mapping data of the
following document:

Document file: graphics_begin_fill.md
Language: jp
"""

from typing import Dict

MAPPING: Dict[str, str] = {
    ##################################################
    "# Graphics begin_fill interface": "# Graphics クラスの begin_fill インターフェイス",
    ##################################################
    "This page explains the `Graphics` class `begin_fill` method interface.": "このページでは`Graphics`クラスの`begin_fill`メソッドのインターフェイスについて説明します。",  # noqa
    ##################################################
    "## What interface is this?": "## インターフェイス概要",
    ##################################################
    "`begin_fill` interface would set the fill color and fill alpha settings. This setting would be maintained until it is called again or called the `clear` method.": "`begin_fill`インターフェイスは塗りの色と塗りの透明度を設定します。この設定は再度`begin_fill`のインターフェイスを呼び出すか、もしくは`clear`メソッドを呼ぶまで保持されます。",  # noqa
    ##################################################
    "## Basic usage": "## 基本的な使い方",
    ##################################################
    "Draw vector graphics interfaces (e.g., `draw_rect`) would use these fill settings when creating, so the `begin_fill` method needs to be called before calling each drawing interface.": "ベクターグラフィックスの描画系の各インターフェイス（例 : `draw_rect`など）はグラフィックス生成時にこの塗りの設定を参照します。そのため描画系のインターフェイスを実行する前にこの`begin_fill`のインターフェイスを呼び出しておく必要があります。",  # noqa
    ##################################################
    '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    background_color="#333", stage_width=350, stage_height=150, stage_elem_id="stage"\n)\nsprite: ap.Sprite = ap.Sprite()\n\n# Set blue fill color and draw the first rectangle.\nsprite.graphics.begin_fill(color="#0af")\nsprite.graphics.draw_rect(x=50, y=50, width=50, height=50)\n\n# Draw the second rectangle (fill color setting will be maintained).\nsprite.graphics.draw_rect(x=150, y=50, width=50, height=50)\n\n# Set the other fill color and draw the third rectangle.\nsprite.graphics.begin_fill(color="#f0a")\nsprite.graphics.draw_rect(x=250, y=50, width=50, height=50)\n\nap.save_overall_html(dest_dir_path="graphics_begin_fill_basic_usage/")\n```': '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    background_color="#333", stage_width=350, stage_height=150, stage_elem_id="stage"\n)\nsprite: ap.Sprite = ap.Sprite()\n\n# Set blue fill color and draw the first rectangle.\nsprite.graphics.begin_fill(color="#0af")\nsprite.graphics.draw_rect(x=50, y=50, width=50, height=50)\n\n# Draw the second rectangle (fill color setting will be maintained).\nsprite.graphics.draw_rect(x=150, y=50, width=50, height=50)\n\n# Set the other fill color and draw the third rectangle.\nsprite.graphics.begin_fill(color="#f0a")\nsprite.graphics.draw_rect(x=250, y=50, width=50, height=50)\n\nap.save_overall_html(dest_dir_path="graphics_begin_fill_basic_usage/")\n```',  # noqa
    ##################################################
    "## Fill color setting": "## 塗りの色の設定",
    ##################################################
    "The `color` argument sets the fill color, and the `begin_fill` interface requires this argument.": "`color`引数は塗りの色を設定します。`begin_fill`インターフェイスではこの引数は必須になっています。",  # noqa
    ##################################################
    '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    background_color="#333", stage_width=150, stage_height=150, stage_elem_id="stage"\n)\nsprite: ap.Sprite = ap.Sprite()\n\n# Set a cyan fill color and draw the rectangle.\nsprite.graphics.begin_fill(color="#0af")\nsprite.graphics.draw_rect(x=50, y=50, width=50, height=50)\n\nap.save_overall_html(dest_dir_path="graphics_begin_fill_fill_color/")\n```': '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    background_color="#333", stage_width=150, stage_height=150, stage_elem_id="stage"\n)\nsprite: ap.Sprite = ap.Sprite()\n\n# Set a cyan fill color and draw the rectangle.\nsprite.graphics.begin_fill(color="#0af")\nsprite.graphics.draw_rect(x=50, y=50, width=50, height=50)\n\nap.save_overall_html(dest_dir_path="graphics_begin_fill_fill_color/")\n```',  # noqa
    ##################################################
    "If you want to clear fill color, specify a blank string to this argument.": "もしも塗りの色の設定を削除したい場合、空の文字列をこの引数に指定してください。",  # noqa
    ##################################################
    "For example, since the following code clears fill color settings, a rectangle graphic becomes invisible.": "以下のコード例では塗りの色の設定を削除しているため、四角のグラフィックは見えなくなります。",  # noqa
    ##################################################
    '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    background_color="#333", stage_width=150, stage_height=150, stage_elem_id="stage"\n)\nsprite: ap.Sprite = ap.Sprite()\n\nsprite.graphics.begin_fill(color="#0af")\n\n# Clear fill color by specifying blank string.\nsprite.graphics.begin_fill(color="")\n\n# Since fill color is not set, the rectangle is invisible.\nsprite.graphics.draw_rect(x=50, y=50, width=50, height=50)\n\nap.save_overall_html(dest_dir_path="graphics_begin_fill_color_setting_clear/")\n```': '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    background_color="#333", stage_width=150, stage_height=150, stage_elem_id="stage"\n)\nsprite: ap.Sprite = ap.Sprite()\n\nsprite.graphics.begin_fill(color="#0af")\n\n# Clear fill color by specifying blank string.\nsprite.graphics.begin_fill(color="")\n\n# Since fill color is not set, the rectangle is invisible.\nsprite.graphics.draw_rect(x=50, y=50, width=50, height=50)\n\nap.save_overall_html(dest_dir_path="graphics_begin_fill_color_setting_clear/")\n```',  # noqa
    ##################################################
    "Color code is acceptable like the following list:": "カラーコードは以下の形の指定を受け付けています。",
    ##################################################
    "- Six characters, e.g., `#00aaff`.": "- `#00aaff`などの6文字による指定。",
    ##################################################
    "- Three characters, e.g., `#0af` (this becomes `#00aaff`).": "- `#0af`などの3文字による指定（これは`#00aaff`と同じ値として扱われます）。",  # noqa
    ##################################################
    "- Single character, e.g., `#5` (this becomes `#000005`).": "- `#5`などの1文字による指定（これは`000005`と同じ値として扱われます）。",  # noqa
    ##################################################
    "- Skipped `#` symbol, e.g., `0af` (this becomes `#00aaff`).": "- `0af`などの`#`記号を省略した指定（これは`#00aaff`と同じ値として扱われます）。",  # noqa
    ##################################################
    "- Blank string, e.g., `''` (this setting clears the fill color setting).": "- ``などの空文字（この指定は塗りの色の設定を削除します）。",  # noqa
    ##################################################
    '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    background_color="#333", stage_width=450, stage_height=150, stage_elem_id="stage"\n)\nsprite: ap.Sprite = ap.Sprite()\n\n# Six characters fill color setting (a cyan color).\nsprite.graphics.begin_fill(color="#00aaff")\nsprite.graphics.draw_rect(x=50, y=50, width=50, height=50)\n\n# Three characters fill color setting (a magenta color).\nsprite.graphics.begin_fill(color="#f0a")\nsprite.graphics.draw_rect(x=150, y=50, width=50, height=50)\n\n# Single characters fill color setting (a black color).\nsprite.graphics.begin_fill(color="#0")\nsprite.graphics.draw_rect(x=250, y=50, width=50, height=50)\n\n# Fill color that Skipped `#` symbol is also acceptable.\nsprite.graphics.begin_fill(color="999")\nsprite.graphics.draw_rect(x=350, y=50, width=50, height=50)\n\nap.save_overall_html(dest_dir_path="graphics_begin_fill_acceptable_color_settings/")\n```': '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    background_color="#333", stage_width=450, stage_height=150, stage_elem_id="stage"\n)\nsprite: ap.Sprite = ap.Sprite()\n\n# Six characters fill color setting (a cyan color).\nsprite.graphics.begin_fill(color="#00aaff")\nsprite.graphics.draw_rect(x=50, y=50, width=50, height=50)\n\n# Three characters fill color setting (a magenta color).\nsprite.graphics.begin_fill(color="#f0a")\nsprite.graphics.draw_rect(x=150, y=50, width=50, height=50)\n\n# Single characters fill color setting (a black color).\nsprite.graphics.begin_fill(color="#0")\nsprite.graphics.draw_rect(x=250, y=50, width=50, height=50)\n\n# Fill color that Skipped `#` symbol is also acceptable.\nsprite.graphics.begin_fill(color="999")\nsprite.graphics.draw_rect(x=350, y=50, width=50, height=50)\n\nap.save_overall_html(dest_dir_path="graphics_begin_fill_acceptable_color_settings/")\n```',  # noqa
    ##################################################
    "## Fill color alpha (opacity) setting": "## 塗りの色の透明度の設定",
    ##################################################
    "Fill color alpha (opacity) can be set by the `alpha` argument. It can accept 0.0 (transparent) to 1.0 (opaque).": "塗りの透明度は`alpha`引数で設定できます。0.0（透明）～1.0（不透明）の範囲の値を受け付けます。",  # noqa
    ##################################################
    '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    background_color="#333", stage_width=200, stage_height=200, stage_elem_id="stage"\n)\nsprite: ap.Sprite = ap.Sprite()\n\nsprite.graphics.begin_fill(color="#00aaff", alpha=0.2)\nsprite.graphics.draw_rect(x=50, y=75, width=50, height=50)\nsprite.graphics.draw_rect(x=75, y=50, width=50, height=50)\nsprite.graphics.draw_rect(x=75, y=75, width=50, height=50)\nsprite.graphics.draw_rect(x=75, y=100, width=50, height=50)\nsprite.graphics.draw_rect(x=100, y=75, width=50, height=50)\n\nap.save_overall_html(dest_dir_path="graphics_begin_fill_alpha_setting/")\n```': '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    background_color="#333", stage_width=200, stage_height=200, stage_elem_id="stage"\n)\nsprite: ap.Sprite = ap.Sprite()\n\nsprite.graphics.begin_fill(color="#00aaff", alpha=0.2)\nsprite.graphics.draw_rect(x=50, y=75, width=50, height=50)\nsprite.graphics.draw_rect(x=75, y=50, width=50, height=50)\nsprite.graphics.draw_rect(x=75, y=75, width=50, height=50)\nsprite.graphics.draw_rect(x=75, y=100, width=50, height=50)\nsprite.graphics.draw_rect(x=100, y=75, width=50, height=50)\n\nap.save_overall_html(dest_dir_path="graphics_begin_fill_alpha_setting/")\n```',  # noqa
    ##################################################
    "## begin_fill API": "## begin_fill API",
    ##################################################
    '<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>': '<span class="inconspicuous-txt">特記事項: このAPIドキュメントはドキュメントビルド用のスクリプトによって自動で生成・同期されています。そのためもしかしたらこの節の内容は前節までの内容と重複している場合があります。</span>',  # noqa
    ##################################################
    "**[Interface summary]**": "**[インターフェイス概要]**",
    ##################################################
    "Set single color value for fill.<hr>": "塗りのための単一の色の設定を行います。<hr>",
    ##################################################
    "**[Parameters]**": "**[引数]**",
    ##################################################
    "- `color`: str or String": "- `color`: str or String",
    ##################################################
    "  - Hexadecimal color string. e.g., '#00aaff'": "  - '#00aaff'などの16進数の色の文字列。",
    ##################################################
    "- `alpha`: float or Number, default 1.0": "- `alpha`: float or Number, default 1.0",  # noqa
    ##################################################
    "  - Color opacity (0.0 to 1.0).": "  - 塗りの透明度（0.0～1.0）。",
    ##################################################
    "<hr>": "<hr>",
    ##################################################
    "**[Examples]**": "**[コードサンプル]**",
    ##################################################
    "```py\n>>> import apysc as ap\n>>> stage: ap.Stage = ap.Stage()\n>>> sprite: ap.Sprite = ap.Sprite()\n>>> sprite.graphics.begin_fill(color=\"#0af\")\n>>> rectangle: ap.Rectangle = sprite.graphics.draw_rect(\n...     x=50, y=50, width=50, height=50\n... )\n>>> rectangle.fill_color\nString('#00aaff')\n```": "```py\n>>> import apysc as ap\n>>> stage: ap.Stage = ap.Stage()\n>>> sprite: ap.Sprite = ap.Sprite()\n>>> sprite.graphics.begin_fill(color=\"#0af\")\n>>> rectangle: ap.Rectangle = sprite.graphics.draw_rect(\n...     x=50, y=50, width=50, height=50\n... )\n>>> rectangle.fill_color\nString('#00aaff')\n```",  # noqa
    ##################################################
    "## fill_color property API": "## fill_color 属性のAPI",
    ##################################################
    '<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>': '<span class="inconspicuous-txt">特記事項: このAPIドキュメントはドキュメントビルド用のスクリプトによって自動で生成・同期されています。そのためもしかしたらこの節の内容は前節までの内容と重複している場合があります。</span>',  # noqa
    ##################################################
    "**[Interface summary]**": "**[インターフェイス概要]**",
    ##################################################
    "Get current fill color.<hr>": "現在の塗りの色を取得します。<hr>",
    ##################################################
    "**[Returns]**": "**[返却値]**",
    ##################################################
    "- `fill_color`: String": "- `fill_color`: String",
    ##################################################
    "  - Current fill color (hexadecimal string, e.g., '#00aaff'). If not be set, this interface returns a blank string.": "  - 現在の塗りの色（`'#00aaff'`などの16進数の文字列）。もしも設定されていない場合空文字が返却されます。",  # noqa
    ##################################################
    "<hr>": "<hr>",
    ##################################################
    "**[Examples]**": "**[コードサンプル]**",
    ##################################################
    "```py\n>>> import apysc as ap\n>>> stage: ap.Stage = ap.Stage()\n>>> sprite: ap.Sprite = ap.Sprite()\n>>> sprite.graphics.begin_fill(color=\"#0af\")\n>>> rectangle: ap.Rectangle = sprite.graphics.draw_rect(\n...     x=50, y=50, width=50, height=50\n... )\n>>> rectangle.fill_color\nString('#00aaff')\n```": "```py\n>>> import apysc as ap\n>>> stage: ap.Stage = ap.Stage()\n>>> sprite: ap.Sprite = ap.Sprite()\n>>> sprite.graphics.begin_fill(color=\"#0af\")\n>>> rectangle: ap.Rectangle = sprite.graphics.draw_rect(\n...     x=50, y=50, width=50, height=50\n... )\n>>> rectangle.fill_color\nString('#00aaff')\n```",  # noqa
    ##################################################
    "## fill_alpha property API": "## fill_alpha 属性のAPI",
    ##################################################
    '<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>': '<span class="inconspicuous-txt">特記事項: このAPIドキュメントはドキュメントビルド用のスクリプトによって自動で生成・同期されています。そのためもしかしたらこの節の内容は前節までの内容と重複している場合があります。</span>',  # noqa
    ##################################################
    "**[Interface summary]**": "**[インターフェイス概要]**",
    ##################################################
    "Get current fill color opacity.<hr>": "現在の塗りの透明度を取得します。<hr>",
    ##################################################
    "**[Returns]**": "**[返却値]**",
    ##################################################
    "- `fill_alpha`: Number": "- `fill_alpha`: Number",
    ##################################################
    "  - Current fill color opacity (0.0 to 1.0). If not be set, 1.0 will be returned.": "  - 現在の塗りの透明度（0.0～1.0）。もし設定されていない場合1.0の値が返却されます。",  # noqa
    ##################################################
    "<hr>": "<hr>",
    ##################################################
    "**[Examples]**": "**[コードサンプル]**",
    ##################################################
    '```py\n>>> import apysc as ap\n>>> stage: ap.Stage = ap.Stage()\n>>> sprite: ap.Sprite = ap.Sprite()\n>>> sprite.graphics.begin_fill(color="#0af", alpha=0.5)\n>>> rectangle: ap.Rectangle = sprite.graphics.draw_rect(\n...     x=50, y=50, width=50, height=50\n... )\n>>> rectangle.fill_alpha\nNumber(0.5)\n```': '```py\n>>> import apysc as ap\n>>> stage: ap.Stage = ap.Stage()\n>>> sprite: ap.Sprite = ap.Sprite()\n>>> sprite.graphics.begin_fill(color="#0af", alpha=0.5)\n>>> rectangle: ap.Rectangle = sprite.graphics.draw_rect(\n...     x=50, y=50, width=50, height=50\n... )\n>>> rectangle.fill_alpha\nNumber(0.5)\n```',  # noqa
}
