"""This module is for the translation mapping data of the
following document:

Document file: graphics_line_style.md
Language: jp
"""

from typing import Dict

MAPPING: Dict[str, str] = {
    ##################################################
    "# Graphics line_style interface": "# Graphics クラスの line_style インターフェイス",
    ##################################################
    "This page explains the `Graphics` class `line_style` method interface.": "このページでは`Graphics`クラスの`line_style`メソッドのインターフェイスについて説明します。",  # noqa
    ##################################################
    "## What interface is this?": "## インターフェイス概要",
    ##################################################
    "The `line_style` interface sets each line style, such as the line color, line alpha, line thickness, line dot setting. This interface maintains these settings until it is called again or called the `clear` method (similar to the `begin_fill` interface).": "`line_style`インターフェイスは線の色や線の透明度、線幅、点線などの線の各スタイルの設定を行います。このインターフェイスは再度インターフェイスを実行したり`clear`メソッドなどを呼ぶまでスタイル設定を保持し続けます（`begin_fill`インターフェイスと同じような挙動をします）。",  # noqa
    ##################################################
    "## Basic usage": "## 基本的な使い方",
    ##################################################
    "Draw vector graphics interfaces (e.g., the `draw_rect` or `line_to`) use these line settings when creating. Therefore, calling the `line_style` method is necessary before calling each drawing interface.": "`draw_rect`や`line_to`などのベクターグラフィックスの描画系の各インターフェイスはこのインターフェイスのスタイル設定を各グラフィックスインスタンス作成時に参照します。従って線の設定が必要な場合には各描画系のインターフェイスを呼ぶ前にこのインターフェイスで設定を行っておく必要があります。",  # noqa
    ##################################################
    '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    background_color="#333", stage_width=200, stage_height=162, stage_elem_id="stage"\n)\nsprite: ap.Sprite = ap.Sprite()\n\n# Draw a white line with 3px line thickness.\nsprite.graphics.line_style(color="#ccc", thickness=8)\nsprite.graphics.move_to(x=50, y=50)\nsprite.graphics.line_to(x=150, y=50)\n\n# Line style setting will be maintained.\nsprite.graphics.move_to(x=50, y=80)\nsprite.graphics.line_to(x=150, y=80)\n\n# Change line color and thickness.\nsprite.graphics.line_style(color="#0af", thickness=3)\nsprite.graphics.move_to(x=50, y=110)\nsprite.graphics.line_to(x=150, y=110)\n\nap.save_overall_html(dest_dir_path="graphics_line_style_basics/")\n```': '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    background_color="#333", stage_width=200, stage_height=162, stage_elem_id="stage"\n)\nsprite: ap.Sprite = ap.Sprite()\n\n# Draw a white line with 3px line thickness.\nsprite.graphics.line_style(color="#ccc", thickness=8)\nsprite.graphics.move_to(x=50, y=50)\nsprite.graphics.line_to(x=150, y=50)\n\n# Line style setting will be maintained.\nsprite.graphics.move_to(x=50, y=80)\nsprite.graphics.line_to(x=150, y=80)\n\n# Change line color and thickness.\nsprite.graphics.line_style(color="#0af", thickness=3)\nsprite.graphics.move_to(x=50, y=110)\nsprite.graphics.line_to(x=150, y=110)\n\nap.save_overall_html(dest_dir_path="graphics_line_style_basics/")\n```',  # noqa
    ##################################################
    "## Line-color setting": "## 線の色の設定",
    ##################################################
    "The required `color` argument sets the line color.": "指定が必須な`color`引数は線の色を設定します。",
    ##################################################
    '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    background_color="#333", stage_width=200, stage_height=102, stage_elem_id="stage"\n)\nsprite: ap.Sprite = ap.Sprite()\n\n# Set a cyan line color and draw the line.\nsprite.graphics.line_style(color="#0af", thickness=4)\nsprite.graphics.draw_line(x_start=50, x_end=150, y_start=50, y_end=50)\n\nap.save_overall_html(dest_dir_path="graphics_line_style_line_color/")\n```': '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    background_color="#333", stage_width=200, stage_height=102, stage_elem_id="stage"\n)\nsprite: ap.Sprite = ap.Sprite()\n\n# Set a cyan line color and draw the line.\nsprite.graphics.line_style(color="#0af", thickness=4)\nsprite.graphics.draw_line(x_start=50, x_end=150, y_start=50, y_end=50)\n\nap.save_overall_html(dest_dir_path="graphics_line_style_line_color/")\n```',  # noqa
    ##################################################
    "If you want to clear line color, specify a blank string to this argument.": "もしも線の色設定を削除したい場合にはこの引数に空文字を指定してください。",  # noqa
    ##################################################
    "For example, the result line graphic becomes invisible since the following code clears the line color setting.": "例えば以下のコード例では線の色設定を削除しているので線は見えなくなっています。",  # noqa
    ##################################################
    '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    background_color="#333", stage_width=200, stage_height=102, stage_elem_id="stage"\n)\nsprite: ap.Sprite = ap.Sprite()\n\n# Set a cyan line color.\nsprite.graphics.line_style(color="#0af", thickness=4)\n\n# Clear the line color by specifying a blank string.\nsprite.graphics.line_style(color="", thickness=4)\nsprite.graphics.draw_line(x_start=50, x_end=150, y_start=50, y_end=50)\n\nap.save_overall_html(dest_dir_path="graphics_line_style_clear_line_color/")\n```': '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    background_color="#333", stage_width=200, stage_height=102, stage_elem_id="stage"\n)\nsprite: ap.Sprite = ap.Sprite()\n\n# Set a cyan line color.\nsprite.graphics.line_style(color="#0af", thickness=4)\n\n# Clear the line color by specifying a blank string.\nsprite.graphics.line_style(color="", thickness=4)\nsprite.graphics.draw_line(x_start=50, x_end=150, y_start=50, y_end=50)\n\nap.save_overall_html(dest_dir_path="graphics_line_style_clear_line_color/")\n```',  # noqa
    ##################################################
    "Color code is acceptable like the following list (same as `begin_fill` interface `color` argument):": "以下のリストようなのカラーコードの文字列を指定することができます（`begin_fill`インターフェイスの`color`引数と同じ挙動になります）。",  # noqa
    ##################################################
    "- Six characters, e.g., `#00aaff`.": "- `#00aaff`などの6文字による指定。",
    ##################################################
    "- Three characters, e.g., `#0af` (this becomes `#00aaff`).": "- `#0af`などの3文字による指定（これは`#00aaff`と同じ値として扱われます）。",  # noqa
    ##################################################
    "- Single character, e.g., `#5` (this becomes `#000005`).": "- `#5`などの1文字による指定（これは`000005`と同じ値として扱われます）。",  # noqa
    ##################################################
    "- Skipped `#` symbol, e.g., `0af` (this becomes `#00aaff`).": "- `0af`などの`#`記号を省略した指定（これは`#00aaff`と同じ値として扱われます）。",  # noqa
    ##################################################
    "- Blank string, e.g., `''` (this clears line color setting).": "- `''`などの空文字の指定（これは線の色の削除指定として扱われます）。`",  # noqa
    ##################################################
    '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    background_color="#333", stage_width=200, stage_height=162, stage_elem_id="stage"\n)\nsprite: ap.Sprite = ap.Sprite()\n\n# The six characters line color setting (a cyan color).\nsprite.graphics.line_style(color="#00aaff", thickness=4)\nsprite.graphics.draw_line(x_start=50, x_end=150, y_start=50, y_end=50)\n\n# The three characters line color setting (a magenta color).\nsprite.graphics.line_style(color="#f0a", thickness=4)\nsprite.graphics.draw_line(x_start=50, x_end=150, y_start=80, y_end=80)\n\n# The one character line color setting (a black color).\nsprite.graphics.line_style(color="#5", thickness=4)\nsprite.graphics.draw_line(x_start=50, x_end=150, y_start=110, y_end=110)\n\nap.save_overall_html(dest_dir_path="graphics_line_style_line_color_color_code/")\n```': '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    background_color="#333", stage_width=200, stage_height=162, stage_elem_id="stage"\n)\nsprite: ap.Sprite = ap.Sprite()\n\n# The six characters line color setting (a cyan color).\nsprite.graphics.line_style(color="#00aaff", thickness=4)\nsprite.graphics.draw_line(x_start=50, x_end=150, y_start=50, y_end=50)\n\n# The three characters line color setting (a magenta color).\nsprite.graphics.line_style(color="#f0a", thickness=4)\nsprite.graphics.draw_line(x_start=50, x_end=150, y_start=80, y_end=80)\n\n# The one character line color setting (a black color).\nsprite.graphics.line_style(color="#5", thickness=4)\nsprite.graphics.draw_line(x_start=50, x_end=150, y_start=110, y_end=110)\n\nap.save_overall_html(dest_dir_path="graphics_line_style_line_color_color_code/")\n```',  # noqa
    ##################################################
    "## Line thickness setting": "## 線幅の設定",
    ##################################################
    "The `thickness` argument sets the line thickness. It can accept greater than or equal to 1.": "`thickness`引数は線の幅を設定します。1以上の値を受け付けることができます。",  # noqa
    ##################################################
    '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    background_color="#333", stage_width=200, stage_height=165, stage_elem_id="stage"\n)\nsprite: ap.Sprite = ap.Sprite()\n\n# Set 1-pixel line thickness.\nsprite.graphics.line_style(color="#0af", thickness=1)\nsprite.graphics.draw_line(x_start=50, x_end=150, y_start=50, y_end=50)\n\n# Set 4-pixel line thickness.\nsprite.graphics.line_style(color="#0af", thickness=4)\nsprite.graphics.draw_line(x_start=50, x_end=150, y_start=80, y_end=80)\n\n# Set 10-pixel line thickness.\nsprite.graphics.line_style(color="#0af", thickness=10)\nsprite.graphics.draw_line(x_start=50, x_end=150, y_start=110, y_end=110)\n\nap.save_overall_html(dest_dir_path="graphics_line_style_thickness/")\n```': '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    background_color="#333", stage_width=200, stage_height=165, stage_elem_id="stage"\n)\nsprite: ap.Sprite = ap.Sprite()\n\n# Set 1-pixel line thickness.\nsprite.graphics.line_style(color="#0af", thickness=1)\nsprite.graphics.draw_line(x_start=50, x_end=150, y_start=50, y_end=50)\n\n# Set 4-pixel line thickness.\nsprite.graphics.line_style(color="#0af", thickness=4)\nsprite.graphics.draw_line(x_start=50, x_end=150, y_start=80, y_end=80)\n\n# Set 10-pixel line thickness.\nsprite.graphics.line_style(color="#0af", thickness=10)\nsprite.graphics.draw_line(x_start=50, x_end=150, y_start=110, y_end=110)\n\nap.save_overall_html(dest_dir_path="graphics_line_style_thickness/")\n```',  # noqa
    ##################################################
    "## Line alpha (opacity) setting": "## 線の透明度の設定",
    ##################################################
    "A line alpha (opacity) can be set by the `alpha` argument. It can accept 0.0 (transparent) to 1.0 (opaque).": "`alpha`引数で線の透明度を設定することができます。0.0（透明）～1.0（不透明）の範囲の値を受け付けることができます。",  # noqa
    ##################################################
    '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    background_color="#333", stage_width=150, stage_height=150, stage_elem_id="stage"\n)\nsprite: ap.Sprite = ap.Sprite()\n\n# Draw the cyan line from upper-left to lower-right.\nsprite.graphics.line_style(color="#0af", thickness=15, alpha=0.3)\nsprite.graphics.draw_line(x_start=50, x_end=100, y_start=50, y_end=100)\n\n# Draw the magenta line from upper-right to lower-left.\nsprite.graphics.line_style(color="#f0a", thickness=15, alpha=0.3)\nsprite.graphics.draw_line(x_start=100, x_end=50, y_start=50, y_end=100)\n\nap.save_overall_html(dest_dir_path="graphics_line_style_alpha/")\n```': '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    background_color="#333", stage_width=150, stage_height=150, stage_elem_id="stage"\n)\nsprite: ap.Sprite = ap.Sprite()\n\n# Draw the cyan line from upper-left to lower-right.\nsprite.graphics.line_style(color="#0af", thickness=15, alpha=0.3)\nsprite.graphics.draw_line(x_start=50, x_end=100, y_start=50, y_end=100)\n\n# Draw the magenta line from upper-right to lower-left.\nsprite.graphics.line_style(color="#f0a", thickness=15, alpha=0.3)\nsprite.graphics.draw_line(x_start=100, x_end=50, y_start=50, y_end=100)\n\nap.save_overall_html(dest_dir_path="graphics_line_style_alpha/")\n```',  # noqa
    ##################################################
    "## Line cap setting": "## 線端の設定",
    ##################################################
    "Line cap setting changes line edge style. The `cap` argument sets this style setting, and `LineCaps` enum values are acceptable.": "線の端のスタイルは`cap`引数で設定することができます。`LineCaps`クラスのenumの値を受け付けます。",  # noqa
    ##################################################
    "There are three `LineCaps` options, as follows:": "以下のように`LineCaps`のオプションは3種類存在します:",  # noqa
    ##################################################
    "- BUTT: This is the default value, and it sets no cap.": "- BUTT: デフォルト値であり、端にはなにも設定されません。",  # noqa
    ##################################################
    "- ROUND: This changes the line edge to the rounded one.": "- ROUND: 線の端のスタイルを丸くします。",  # noqa
    ##################################################
    "- SQUARE: This is similar to BUTT, but it increases the line length by the squared edge.": "- SQUARE: 線の端のスタイルを四角くします。これはBUTTと似た表示になりますが、設定される四角の分だけ線が長くなります。",  # noqa
    ##################################################
    '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    background_color="#333", stage_width=200, stage_height=180, stage_elem_id="stage"\n)\nsprite: ap.Sprite = ap.Sprite()\n\n# BUTT caps setting (default).\nsprite.graphics.line_style(color="#0af", thickness=20, cap=ap.LineCaps.BUTT)\nsprite.graphics.draw_line(x_start=50, x_end=150, y_start=50, y_end=50)\n\n# ROUND caps setting.\nsprite.graphics.line_style(color="#0af", thickness=20, cap=ap.LineCaps.ROUND)\nsprite.graphics.draw_line(x_start=50, x_end=150, y_start=90, y_end=90)\n\n# SQUARE caps setting (same line length setting as BUTT line,\n# but this will be longer for the caps).\nsprite.graphics.line_style(color="#0af", thickness=20, cap=ap.LineCaps.SQUARE)\nsprite.graphics.draw_line(x_start=50, x_end=150, y_start=130, y_end=130)\n\nap.save_overall_html(dest_dir_path="graphics_line_style_caps/")\n```': '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    background_color="#333", stage_width=200, stage_height=180, stage_elem_id="stage"\n)\nsprite: ap.Sprite = ap.Sprite()\n\n# BUTT caps setting (default).\nsprite.graphics.line_style(color="#0af", thickness=20, cap=ap.LineCaps.BUTT)\nsprite.graphics.draw_line(x_start=50, x_end=150, y_start=50, y_end=50)\n\n# ROUND caps setting.\nsprite.graphics.line_style(color="#0af", thickness=20, cap=ap.LineCaps.ROUND)\nsprite.graphics.draw_line(x_start=50, x_end=150, y_start=90, y_end=90)\n\n# SQUARE caps setting (same line length setting as BUTT line,\n# but this will be longer for the caps).\nsprite.graphics.line_style(color="#0af", thickness=20, cap=ap.LineCaps.SQUARE)\nsprite.graphics.draw_line(x_start=50, x_end=150, y_start=130, y_end=130)\n\nap.save_overall_html(dest_dir_path="graphics_line_style_caps/")\n```',  # noqa
    ##################################################
    "## Line joints setting": "## 線の繋ぎ目の設定",
    ##################################################
    "Line joints setting changes the line vertices style. The `joints` argument sets this style, and `LineJoints` enum values are acceptable. The `Polyline` class (`move_to` and `line_to` interfaces) mainly uses this argument.": "`joints`引数では線の繋ぎ目（頂点部分）のスタイルを変更します。この引数には`LineJoints`のenumの各値を受け付けます。主に`move_to`や`line_to`などのインターフェイスで生成される`Polyline`クラスのインスタンスでこの引数は使用されます。",  # noqa
    ##################################################
    "There are three LineJoints enum values, as follows:": "以下のようにLineJointsのenumには3つの値が存在します:",  # noqa
    ##################################################
    "- MITER: This setting sets the style like a picture frame vertices. This setting is the default style setting.": "- MITER: この設定は頂点が（尖った形での）額縁のような形のスタイルが設定されます。この設定がデフォルトのスタイルとなります。",  # noqa
    ##################################################
    "- ROUND: This setting sets the rounded vertices style.": "- ROUND: この設定は丸い頂点のスタイルを設定します。",  # noqa
    ##################################################
    "- BEVEL: This setting sets a beveled vertices style.": "- BEVEL: この設定は射角（ベベル）の頂点のスタイルを設定します。",  # noqa
    ##################################################
    '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    background_color="#333", stage_width=350, stage_height=150, stage_elem_id="stage"\n)\nsprite: ap.Sprite = ap.Sprite()\n\n# Set MITER joints setting and draw the polyline.\nsprite.graphics.line_style(color="#0af", thickness=10, joints=ap.LineJoints.MITER)\nsprite.graphics.move_to(x=50, y=100)\nsprite.graphics.line_to(x=75, y=50)\nsprite.graphics.line_to(x=100, y=100)\n\n# Set ROUND joints setting and draw the polyline.\nsprite.graphics.line_style(color="#0af", thickness=10, joints=ap.LineJoints.ROUND)\nsprite.graphics.move_to(x=150, y=100)\nsprite.graphics.line_to(x=175, y=50)\nsprite.graphics.line_to(x=200, y=100)\n\n# Set BEVEL joints setting and draw the polyline.\nsprite.graphics.line_style(color="#0af", thickness=10, joints=ap.LineJoints.BEVEL)\nsprite.graphics.move_to(x=250, y=100)\nsprite.graphics.line_to(x=275, y=50)\nsprite.graphics.line_to(x=300, y=100)\n\nap.save_overall_html(dest_dir_path="graphics_line_style_joints/")\n```': '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    background_color="#333", stage_width=350, stage_height=150, stage_elem_id="stage"\n)\nsprite: ap.Sprite = ap.Sprite()\n\n# Set MITER joints setting and draw the polyline.\nsprite.graphics.line_style(color="#0af", thickness=10, joints=ap.LineJoints.MITER)\nsprite.graphics.move_to(x=50, y=100)\nsprite.graphics.line_to(x=75, y=50)\nsprite.graphics.line_to(x=100, y=100)\n\n# Set ROUND joints setting and draw the polyline.\nsprite.graphics.line_style(color="#0af", thickness=10, joints=ap.LineJoints.ROUND)\nsprite.graphics.move_to(x=150, y=100)\nsprite.graphics.line_to(x=175, y=50)\nsprite.graphics.line_to(x=200, y=100)\n\n# Set BEVEL joints setting and draw the polyline.\nsprite.graphics.line_style(color="#0af", thickness=10, joints=ap.LineJoints.BEVEL)\nsprite.graphics.move_to(x=250, y=100)\nsprite.graphics.line_to(x=275, y=50)\nsprite.graphics.line_to(x=300, y=100)\n\nap.save_overall_html(dest_dir_path="graphics_line_style_joints/")\n```',  # noqa
    ##################################################
    "## Line dot setting": "## 線の点線設定",
    ##################################################
    "Line dot setting changes the line to dotted line. The `dot_setting` argument (`LineDotSetting` value) sets this setting. It can change dot size by the `dot_size` argument (greater than or equal to 1 value is acceptable).": "`dot_setting`引数は線を点線へと変更する設定です。この引数は`LineDotSetting`クラスの設定を受け付けます。点線のサイズは`dot_size`引数で変更することができます（1以上の値を受け付けます）。",  # noqa
    ##################################################
    '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    background_color="#333", stage_width=300, stage_height=160, stage_elem_id="stage"\n)\nsprite: ap.Sprite = ap.Sprite()\n\n# Set the line dot settings with 2-pixel dot size and draw the dotted line.\nsprite.graphics.line_style(\n    color="#0af", thickness=5, dot_setting=ap.LineDotSetting(dot_size=2)\n)\nsprite.graphics.move_to(x=50, y=50)\nsprite.graphics.line_to(x=250, y=50)\n\n# Set the line dot settings with 5-pixel dot size and draw the dotted line.\nsprite.graphics.line_style(\n    color="#0af", thickness=5, dot_setting=ap.LineDotSetting(dot_size=5)\n)\nsprite.graphics.move_to(x=50, y=80)\nsprite.graphics.line_to(x=250, y=80)\n\n# Set the line dot settings with 10-pixel dot size and draw the dotted line.\nsprite.graphics.line_style(\n    color="#0af", thickness=5, dot_setting=ap.LineDotSetting(dot_size=10)\n)\nsprite.graphics.move_to(x=50, y=110)\nsprite.graphics.line_to(x=250, y=110)\n\nap.save_overall_html(dest_dir_path="graphics_line_style_line_dot_setting/")\n```': '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    background_color="#333", stage_width=300, stage_height=160, stage_elem_id="stage"\n)\nsprite: ap.Sprite = ap.Sprite()\n\n# Set the line dot settings with 2-pixel dot size and draw the dotted line.\nsprite.graphics.line_style(\n    color="#0af", thickness=5, dot_setting=ap.LineDotSetting(dot_size=2)\n)\nsprite.graphics.move_to(x=50, y=50)\nsprite.graphics.line_to(x=250, y=50)\n\n# Set the line dot settings with 5-pixel dot size and draw the dotted line.\nsprite.graphics.line_style(\n    color="#0af", thickness=5, dot_setting=ap.LineDotSetting(dot_size=5)\n)\nsprite.graphics.move_to(x=50, y=80)\nsprite.graphics.line_to(x=250, y=80)\n\n# Set the line dot settings with 10-pixel dot size and draw the dotted line.\nsprite.graphics.line_style(\n    color="#0af", thickness=5, dot_setting=ap.LineDotSetting(dot_size=10)\n)\nsprite.graphics.move_to(x=50, y=110)\nsprite.graphics.line_to(x=250, y=110)\n\nap.save_overall_html(dest_dir_path="graphics_line_style_line_dot_setting/")\n```',  # noqa
    ##################################################
    "This setting (or the other similar settings) also changes the `Rectangle` or other graphics classes.": "この設定や類似の設定は線のグラフィックスだけでなく`Rectangle`など他のグラフィックスクラスの表示も変更します。",  # noqa
    ##################################################
    '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    background_color="#333", stage_width=250, stage_height=150, stage_elem_id="stage"\n)\nsprite: ap.Sprite = ap.Sprite()\n\n# Set the line dot setting with 2-pixel dot size and draw the rectangle.\n# Fill color setting is skipped.\nsprite.graphics.line_style(\n    color="#0af", thickness=5, dot_setting=ap.LineDotSetting(dot_size=2)\n)\nsprite.graphics.draw_rect(x=50, y=50, width=50, height=50)\n\n# Draw the rectangle with the dotted line setting and the fill color.\nsprite.graphics.begin_fill(color="#038")\nsprite.graphics.draw_rect(x=150, y=50, width=50, height=50)\n\nap.save_overall_html(dest_dir_path="graphics_line_style_line_dot_setting_rectangle/")\n```': '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    background_color="#333", stage_width=250, stage_height=150, stage_elem_id="stage"\n)\nsprite: ap.Sprite = ap.Sprite()\n\n# Set the line dot setting with 2-pixel dot size and draw the rectangle.\n# Fill color setting is skipped.\nsprite.graphics.line_style(\n    color="#0af", thickness=5, dot_setting=ap.LineDotSetting(dot_size=2)\n)\nsprite.graphics.draw_rect(x=50, y=50, width=50, height=50)\n\n# Draw the rectangle with the dotted line setting and the fill color.\nsprite.graphics.begin_fill(color="#038")\nsprite.graphics.draw_rect(x=150, y=50, width=50, height=50)\n\nap.save_overall_html(dest_dir_path="graphics_line_style_line_dot_setting_rectangle/")\n```',  # noqa
    ##################################################
    "Notes: This setting will be ignored by `draw_line`, `draw_dotted_line`, `draw_dashed_line`, `draw_round_dotted_line`, and `draw_dash_dotted_line` interfaces.": "特記事項: この設定は`draw_line`、`draw_dotted_line`、`draw_dashed_line`、`draw_round_dotted_line`、`draw_dash_dotted_line`の各インターフェイスで無視されます。",  # noqa
    ##################################################
    "## Line dash setting": "## 線の破線設定",
    ##################################################
    "Line dash setting changes the line to the dashed line. The `dash_setting` argument (`LineDashSetting` value) sets this setting. It can change dash size and space size by the `dash_size` and `space_size` arguments.": "`dash_setting`引数は線の破線のスタイル設定を変更します。ごの引数は`LineDashSetting`クラスの設定を受け付けます。この設定では破線のサイズを`dash_size`引数で、空白のスペースのサイズを`space_size`引数で変更することができます。",  # noqa
    ##################################################
    '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    background_color="#333", stage_width=300, stage_height=130, stage_elem_id="stage"\n)\nsprite: ap.Sprite = ap.Sprite()\n\n# Set 10-pixel dash size and 3-pixel space size and draw the line.\nsprite.graphics.line_style(\n    color="#0af",\n    thickness=3,\n    dash_setting=ap.LineDashSetting(dash_size=10, space_size=3),\n)\nsprite.graphics.move_to(x=50, y=50)\nsprite.graphics.line_to(x=250, y=50)\n\n# Set 15-pixel dash size and 5-pixel space size and draw the line.\nsprite.graphics.line_style(\n    color="#0af",\n    thickness=3,\n    dash_setting=ap.LineDashSetting(dash_size=15, space_size=5),\n)\nsprite.graphics.move_to(x=50, y=80)\nsprite.graphics.line_to(x=250, y=80)\n\nap.save_overall_html(dest_dir_path="graphics_line_style_line_dash_setting/")\n```': '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    background_color="#333", stage_width=300, stage_height=130, stage_elem_id="stage"\n)\nsprite: ap.Sprite = ap.Sprite()\n\n# Set 10-pixel dash size and 3-pixel space size and draw the line.\nsprite.graphics.line_style(\n    color="#0af",\n    thickness=3,\n    dash_setting=ap.LineDashSetting(dash_size=10, space_size=3),\n)\nsprite.graphics.move_to(x=50, y=50)\nsprite.graphics.line_to(x=250, y=50)\n\n# Set 15-pixel dash size and 5-pixel space size and draw the line.\nsprite.graphics.line_style(\n    color="#0af",\n    thickness=3,\n    dash_setting=ap.LineDashSetting(dash_size=15, space_size=5),\n)\nsprite.graphics.move_to(x=50, y=80)\nsprite.graphics.line_to(x=250, y=80)\n\nap.save_overall_html(dest_dir_path="graphics_line_style_line_dash_setting/")\n```',  # noqa
    ##################################################
    "Notes: This setting will be ignored by `draw_line`, `draw_dotted_line`, `draw_dashed_line`, `draw_round_dotted_line`, and `draw_dash_dotted_line` interfaces.": "特記事項: この設定は`draw_line`、`draw_dotted_line`、`draw_dashed_line`、`draw_round_dotted_line`、`draw_dash_dotted_line`の各インターフェイスで無視されます。",  # noqa
    ##################################################
    "## Line round dot setting": "## 線の丸ドット設定",
    ##################################################
    "Line round dot setting changes the line to the round dotted line. The `round_dot_setting` argument (`LineRoundDotSetting` value) sets this setting. It can change round size and space size by the `round_size` and `space_size` arguments.": "`round_dot_setting`引数は線の丸ドットのスタイルを設定します。この引数は`LineRoundDotSetting`クラスの値を受け付けます。この設定では円のサイズを`round_size`、円の間のスペースのサイズを`space_size`引数で変更することができます。",  # noqa
    ##################################################
    '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    background_color="#333", stage_width=300, stage_height=130, stage_elem_id="stage"\n)\nsprite: ap.Sprite = ap.Sprite()\n\n# Set 5-pixel round size and draw the line.\nsprite.graphics.line_style(\n    color="#0af",\n    thickness=5,\n    round_dot_setting=ap.LineRoundDotSetting(round_size=5, space_size=5),\n)\nsprite.graphics.move_to(x=50, y=50)\nsprite.graphics.line_to(x=250, y=50)\n\n# Set 10-pixel round size and draw the line.\nsprite.graphics.line_style(\n    color="#0af",\n    thickness=5,\n    round_dot_setting=ap.LineRoundDotSetting(round_size=10, space_size=5),\n)\nsprite.graphics.move_to(x=50, y=80)\nsprite.graphics.line_to(x=250, y=80)\n\nap.save_overall_html(dest_dir_path="graphics_line_style_line_round_dot_setting/")\n```': '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    background_color="#333", stage_width=300, stage_height=130, stage_elem_id="stage"\n)\nsprite: ap.Sprite = ap.Sprite()\n\n# Set 5-pixel round size and draw the line.\nsprite.graphics.line_style(\n    color="#0af",\n    thickness=5,\n    round_dot_setting=ap.LineRoundDotSetting(round_size=5, space_size=5),\n)\nsprite.graphics.move_to(x=50, y=50)\nsprite.graphics.line_to(x=250, y=50)\n\n# Set 10-pixel round size and draw the line.\nsprite.graphics.line_style(\n    color="#0af",\n    thickness=5,\n    round_dot_setting=ap.LineRoundDotSetting(round_size=10, space_size=5),\n)\nsprite.graphics.move_to(x=50, y=80)\nsprite.graphics.line_to(x=250, y=80)\n\nap.save_overall_html(dest_dir_path="graphics_line_style_line_round_dot_setting/")\n```',  # noqa
    ##################################################
    "Notes: Since this setting uses the `cap` setting internally, this setting ignores the `cap` setting, increasing the line length by the capsize.": "特記事項: この設定は内部で`cap`設定の値を使用しているため、この設定では`cap`引数の設定が無視されます。また、丸のサイズに応じた分だけ線の長さが長くなります。",  # noqa
    ##################################################
    "Notes: This setting will be ignored by `draw_line`, `draw_dotted_line`, `draw_dashed_line`, `draw_round_dotted_line`, and `draw_dash_dotted_line` interfaces.": "特記事項: この設定は`draw_line`、`draw_dotted_line`、`draw_dashed_line`、`draw_round_dotted_line`、`draw_dash_dotted_line`の各インターフェイスで無視されます。",  # noqa
    ##################################################
    "## Line dash-dot setting": "## 線の一点鎖線の設定",
    ##################################################
    "Line dash-dot setting changes the line to the dash-dotted line (also called long dashed short dashed line or one-dot chain line). The `dash_dot_setting` arguments set this setting and it accepts a `LineDashDotSetting` instance. This argument accepts the `dot_size` (short dashed size), `dash_size` (long dashed size), and `space_size` arguments.": "`dash_dot_setting`引数は線に一点鎖線のスタイルを設定します。この引数は`LineDashDotSetting`クラスのインスタンスを受け付けます。この設定は短い点線のサイズを`dot_size`、長い破線のサイズを`dash_size`、そして空白のスペースのサイズを`space_size`引数で設定できます。",  # noqa
    ##################################################
    '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    background_color="#333", stage_width=300, stage_height=130, stage_elem_id="stage"\n)\nsprite: ap.Sprite = ap.Sprite()\n\n# Set 3-pixel dot size and 10-pixel dash size and draw the line.\nsprite.graphics.line_style(\n    color="#0af",\n    thickness=3,\n    dash_dot_setting=ap.LineDashDotSetting(dot_size=3, dash_size=10, space_size=3),\n)\nsprite.graphics.move_to(x=50, y=50)\nsprite.graphics.line_to(x=250, y=50)\n\n# Set 5-pixel dot size and 15-pixel dash size and draw the line.\nsprite.graphics.line_style(\n    color="#0af",\n    thickness=3,\n    dash_dot_setting=ap.LineDashDotSetting(dot_size=5, dash_size=15, space_size=3),\n)\nsprite.graphics.move_to(x=50, y=80)\nsprite.graphics.line_to(x=250, y=80)\n\nap.save_overall_html(dest_dir_path="graphics_line_style_line_dash_dot_setting/")\n```': '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    background_color="#333", stage_width=300, stage_height=130, stage_elem_id="stage"\n)\nsprite: ap.Sprite = ap.Sprite()\n\n# Set 3-pixel dot size and 10-pixel dash size and draw the line.\nsprite.graphics.line_style(\n    color="#0af",\n    thickness=3,\n    dash_dot_setting=ap.LineDashDotSetting(dot_size=3, dash_size=10, space_size=3),\n)\nsprite.graphics.move_to(x=50, y=50)\nsprite.graphics.line_to(x=250, y=50)\n\n# Set 5-pixel dot size and 15-pixel dash size and draw the line.\nsprite.graphics.line_style(\n    color="#0af",\n    thickness=3,\n    dash_dot_setting=ap.LineDashDotSetting(dot_size=5, dash_size=15, space_size=3),\n)\nsprite.graphics.move_to(x=50, y=80)\nsprite.graphics.line_to(x=250, y=80)\n\nap.save_overall_html(dest_dir_path="graphics_line_style_line_dash_dot_setting/")\n```',  # noqa
    ##################################################
    "Notes: This setting will be ignored by `draw_line`, `draw_dotted_line`, `draw_dashed_line`, `draw_round_dotted_line`, and `draw_dash_dotted_line` interfaces.": "特記事項: この設定は`draw_line`、`draw_dotted_line`、`draw_dashed_line`、`draw_round_dotted_line`、`draw_dash_dotted_line`の各インターフェイスで無視されます。",  # noqa
    ##################################################
    "## line_style API": "## line_style API",
    ##################################################
    '<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>': '<span class="inconspicuous-txt">特記事項: このAPIドキュメントはドキュメントビルド用のスクリプトによって自動で生成・同期されています。そのためもしかしたらこの節の内容は前節までの内容と重複している場合があります。</span>',  # noqa
    ##################################################
    "**[Interface summary]**": "**[インターフェイス概要]**",
    ##################################################
    "Set line style values.<hr>": "線のスタイルを設定します。<hr>",
    ##################################################
    "**[Parameters]**": "**[引数]**",
    ##################################################
    "- `color`: String or str": "- `color`: String or str",
    ##################################################
    "  - Hexadecimal color string. e.g., '#00aaff'": "  - '#00aaff'などの16進数の色の文字列。",
    ##################################################
    "- `thickness`: Int or int, default 1": "- `thickness`: Int or int, default 1",
    ##################################################
    "  - Line thickness (minimum value is 1).": "  - 線の幅（1以上の値を受け付けます）。",
    ##################################################
    "- `alpha`: float or Number, default 1.0": "- `alpha`: float or Number, default 1.0",  # noqa
    ##################################################
    "  - Line color opacity (0.0 to 1.0).": "  - 線色の透明度（0.0～1.0）。",
    ##################################################
    "- `cap`: LineCaps or None, default None": "- `cap`: LineCaps or None, default None",  # noqa
    ##################################################
    "  - Line cap (edge style) setting. The not line-related graphics (e.g., Rectangle ignores this, conversely used by Polyline) ignore this setting.": "  - 線の端のスタイル設定。線に関係しないRectangleクラスなどのグラフィックスインスタンスはこの設定を無視します。逆にPolylineクラスなどの線に関係したインスタンスではこの設定を使用します。",  # noqa
    ##################################################
    "- `joints`: LineJoints or None, default None": "- `joints`: LineJoints or None, default None",  # noqa
    ##################################################
    "  - Line vertices (joints) style setting. The not polyline-related graphics (e.g., Rectangle ignores this, conversely used by Polyline) ignore this setting.": "  - 線の頂点（接合部）のスタイル設定。折れ線線に関係しないRectangleなどのグラフィックスインスタンスはこの設定を無視します。逆にPolylineクラスなどの折れ線関係のクラスではこの設定を使用します。",  # noqa
    ##################################################
    "- `dot_setting`: LineDotSetting or None, default None": "- `dot_setting`: LineDotSetting or None, default None",  # noqa
    ##################################################
    "  - Dot setting. If this is specified, it makes a line dotted.": "  - 点線の設定。もしもこの引数が指定された場合、線は点線になります。",  # noqa
    ##################################################
    "- `dash_setting`: LineDashSetting or None, default None": "- `dash_setting`: LineDashSetting or None, default None",  # noqa
    ##################################################
    "  - Dash setting. If this is specified, it makes a line dashed.": "  - 破線の設定。もしこの引数が指定された場合、線は破線になります。",  # noqa
    ##################################################
    "- `round_dot_setting`: LineRoundDotSetting or None, default None": "- `round_dot_setting`: LineRoundDotSetting or None, default None",  # noqa
    ##################################################
    "  - Round dot setting. If this is specified, it makes a line round dotted. Notes: since this style uses a cap setting, it overrides cap and line thickness settings. And it increases the amount of line size. If you want to adjust to the same width of a normal line when using move_to and line_to interfaces, add half-round size to start x-coordinate and subtract from end e-coordinate. e.g., `this.move_to(x + round_size / 2, y)`, `this.line_to(x - round_size / 2, y)`": "  - 丸ドットの設定。もしこの引数が指定された場合、線は丸ドットになります。特記事項: ごの設定は内部でcapの設定を使用しているため、cap（線の端のスタイル設定）と線幅の設定を上書きします。また、cap設定を使用している都合、線の長さも長くなります。move_toやline_toなどのインターフェイスを使った通常の線の長さと合わせたい場合には丸の半分のサイズを線の開始位置のX座標へ加算し、さらに丸の半分のサイズを線の終了位置のX座標から減算してください（Y座標も同様です）。例: `this.move_to(x + round_size / 2, y)`、`this.line_to(x - round_size / 2, y)`",  # noqa
    ##################################################
    "- `dash_dot_setting`: LineDashDotSetting or None, default None": "- `dash_dot_setting`: LineDashDotSetting or None, default None",  # noqa
    ##################################################
    "  - Dash dot (1-dot chain) setting. If this is specified, it makes a line 1-dot chained.": "  - 一点鎖線のスタイル設定。もしこの引数が指定された場合、線の一点鎖線になります。",  # noqa
    ##################################################
    "<hr>": "<hr>",
    ##################################################
    "**[Examples]**": "**[コードサンプル]**",
    ##################################################
    "```py\n>>> import apysc as ap\n>>> stage: ap.Stage = ap.Stage()\n>>> sprite: ap.Sprite = ap.Sprite()\n>>> sprite.graphics.line_style(\n...     color=\"#fff\", thickness=5, alpha=0.5, cap=ap.LineCaps.ROUND\n... )\n>>> line: ap.Line = sprite.graphics.draw_line(\n...     x_start=50, y_start=50, x_end=150, y_end=50\n... )\n>>> line.line_color\nString('#ffffff')\n\n>>> line.line_thickness\nInt(5)\n\n>>> line.line_alpha\nNumber(0.5)\n\n>>> line.line_cap\nString('round')\n```": "```py\n>>> import apysc as ap\n>>> stage: ap.Stage = ap.Stage()\n>>> sprite: ap.Sprite = ap.Sprite()\n>>> sprite.graphics.line_style(\n...     color=\"#fff\", thickness=5, alpha=0.5, cap=ap.LineCaps.ROUND\n... )\n>>> line: ap.Line = sprite.graphics.draw_line(\n...     x_start=50, y_start=50, x_end=150, y_end=50\n... )\n>>> line.line_color\nString('#ffffff')\n\n>>> line.line_thickness\nInt(5)\n\n>>> line.line_alpha\nNumber(0.5)\n\n>>> line.line_cap\nString('round')\n```",  # noqa
    ##################################################
    "## line_color property API": "## line_color 属性のAPI",
    ##################################################
    '<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>': '<span class="inconspicuous-txt">特記事項: このAPIドキュメントはドキュメントビルド用のスクリプトによって自動で生成・同期されています。そのためもしかしたらこの節の内容は前節までの内容と重複している場合があります。</span>',  # noqa
    ##################################################
    "**[Interface summary]**": "**[インターフェイス概要]**",
    ##################################################
    "Get current line color.<hr>": "現在の線の色を取得します。<hr>",
    ##################################################
    "**[Returns]**": "**[返却値]**",
    ##################################################
    "- `line_color`: String": "- `line_color`: String",
    ##################################################
    "  - Current line color (hexadecimal string, e.g., '#00aaff'). If not be set, this interface returns a blank string.": "  - '#00aaff'などの16進数の線の色。もし設定されていない場合はこの空文字となります。",  # noqa
    ##################################################
    "<hr>": "<hr>",
    ##################################################
    "**[Examples]**": "**[コードサンプル]**",
    ##################################################
    "```py\n>>> import apysc as ap\n>>> stage: ap.Stage = ap.Stage()\n>>> sprite: ap.Sprite = ap.Sprite()\n>>> sprite.graphics.line_style(\n...     color=\"#fff\", thickness=5, alpha=0.5, cap=ap.LineCaps.ROUND\n... )\n>>> sprite.graphics.line_color\nString('#ffffff')\n```": "```py\n>>> import apysc as ap\n>>> stage: ap.Stage = ap.Stage()\n>>> sprite: ap.Sprite = ap.Sprite()\n>>> sprite.graphics.line_style(\n...     color=\"#fff\", thickness=5, alpha=0.5, cap=ap.LineCaps.ROUND\n... )\n>>> sprite.graphics.line_color\nString('#ffffff')\n```",  # noqa
    ##################################################
    "## line_thickness property API": "## line_thickness 属性のAPI",
    ##################################################
    '<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>': '<span class="inconspicuous-txt">特記事項: このAPIドキュメントはドキュメントビルド用のスクリプトによって自動で生成・同期されています。そのためもしかしたらこの節の内容は前節までの内容と重複している場合があります。</span>',  # noqa
    ##################################################
    "**[Interface summary]**": "**[インターフェイス概要]**",
    ##################################################
    "Get current line thickness.<hr>": "現在の線の線幅を取得します。<hr>",
    ##################################################
    "**[Returns]**": "**[返却値]**",
    ##################################################
    "- `line_thickness`: Int": "- `line_thickness`: Int",
    ##################################################
    "  - Current line thickness.": "  - 現在の線幅。",
    ##################################################
    "<hr>": "<hr>",
    ##################################################
    "**[Examples]**": "**[コードサンプル]**",
    ##################################################
    '```py\n>>> import apysc as ap\n>>> stage: ap.Stage = ap.Stage()\n>>> sprite: ap.Sprite = ap.Sprite()\n>>> sprite.graphics.line_style(color="#fff", thickness=5, alpha=0.5)\n>>> sprite.graphics.line_thickness\nInt(5)\n```': '```py\n>>> import apysc as ap\n>>> stage: ap.Stage = ap.Stage()\n>>> sprite: ap.Sprite = ap.Sprite()\n>>> sprite.graphics.line_style(color="#fff", thickness=5, alpha=0.5)\n>>> sprite.graphics.line_thickness\nInt(5)\n```',  # noqa
    ##################################################
    "## line_alpha property API": "## line_alpha 属性のAPI",
    ##################################################
    '<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>': '<span class="inconspicuous-txt">特記事項: このAPIドキュメントはドキュメントビルド用のスクリプトによって自動で生成・同期されています。そのためもしかしたらこの節の内容は前節までの内容と重複している場合があります。</span>',  # noqa
    ##################################################
    "**[Interface summary]**": "**[インターフェイス概要]**",
    ##################################################
    "Get current line color opacity.<hr>": "現在の線の透明度を取得します。<hr>",
    ##################################################
    "**[Returns]**": "**[返却値]**",
    ##################################################
    "- `line_alpha`: Number": "- `line_alpha`: Number",
    ##################################################
    "  - Current line opacity (0.0 to 1.0).": "  - 現在の線の透明度（0.0～1.0）。",
    ##################################################
    "<hr>": "<hr>",
    ##################################################
    "**[Examples]**": "**[コードサンプル]**",
    ##################################################
    '```py\n>>> import apysc as ap\n>>> stage: ap.Stage = ap.Stage()\n>>> sprite: ap.Sprite = ap.Sprite()\n>>> sprite.graphics.line_style(\n...     color="#fff", thickness=5, alpha=0.5, cap=ap.LineCaps.ROUND\n... )\n>>> sprite.graphics.line_alpha\nNumber(0.5)\n```': '```py\n>>> import apysc as ap\n>>> stage: ap.Stage = ap.Stage()\n>>> sprite: ap.Sprite = ap.Sprite()\n>>> sprite.graphics.line_style(\n...     color="#fff", thickness=5, alpha=0.5, cap=ap.LineCaps.ROUND\n... )\n>>> sprite.graphics.line_alpha\nNumber(0.5)\n```',  # noqa
    ##################################################
    "## line_cap property API": "## line_cap 属性のAPI",
    ##################################################
    '<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>': '<span class="inconspicuous-txt">特記事項: このAPIドキュメントはドキュメントビルド用のスクリプトによって自動で生成・同期されています。そのためもしかしたらこの節の内容は前節までの内容と重複している場合があります。</span>',  # noqa
    ##################################################
    "**[Interface summary]**": "**[インターフェイス概要]**",
    ##################################################
    "Get current line cap (edge) style setting.<hr>": "現在の線の端のスタイル設定。<hr>",
    ##################################################
    "**[Returns]**": "**[返却値]**",
    ##################################################
    "- `line_cap`: String": "- `line_cap`: String",
    ##################################################
    "  - Current line cap (edge) style setting.": "  - 現在の線の端のスタイル設定。",
    ##################################################
    "<hr>": "<hr>",
    ##################################################
    "**[Examples]**": "**[コードサンプル]**",
    ##################################################
    "```py\n>>> import apysc as ap\n>>> stage: ap.Stage = ap.Stage()\n>>> sprite: ap.Sprite = ap.Sprite()\n>>> sprite.graphics.line_style(\n...     color=\"#fff\", thickness=5, alpha=0.5, cap=ap.LineCaps.ROUND\n... )\n>>> sprite.graphics.line_cap\nString('round')\n```": "```py\n>>> import apysc as ap\n>>> stage: ap.Stage = ap.Stage()\n>>> sprite: ap.Sprite = ap.Sprite()\n>>> sprite.graphics.line_style(\n...     color=\"#fff\", thickness=5, alpha=0.5, cap=ap.LineCaps.ROUND\n... )\n>>> sprite.graphics.line_cap\nString('round')\n```",  # noqa
    ##################################################
    "## line_joints property API": "## line_joints 属性のAPI",
    ##################################################
    '<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>': '<span class="inconspicuous-txt">特記事項: このAPIドキュメントはドキュメントビルド用のスクリプトによって自動で生成・同期されています。そのためもしかしたらこの節の内容は前節までの内容と重複している場合があります。</span>',  # noqa
    ##################################################
    "**[Interface summary]**": "**[インターフェイス概要]**",
    ##################################################
    "Get current line joints (vertices) style setting.<hr>": "現在の線の接合部（頂点）のスタイル設定を取得します。<hr>",  # noqa
    ##################################################
    "**[Returns]**": "**[返却値]**",
    ##################################################
    "- `line_joints`: String": "- `line_joints`: String",
    ##################################################
    "  - Current line joints (vertices) style setting.": "  - 現在の線の接合部（頂点）のスタイル設定。",
    ##################################################
    "<hr>": "<hr>",
    ##################################################
    "**[Examples]**": "**[コードサンプル]**",
    ##################################################
    "```py\n>>> import apysc as ap\n>>> stage: ap.Stage = ap.Stage()\n>>> sprite: ap.Sprite = ap.Sprite()\n>>> sprite.graphics.line_style(\n...     color=\"#fff\", thickness=5, joints=ap.LineJoints.ROUND\n... )\n>>> sprite.graphics.line_joints\nString('round')\n```": "```py\n>>> import apysc as ap\n>>> stage: ap.Stage = ap.Stage()\n>>> sprite: ap.Sprite = ap.Sprite()\n>>> sprite.graphics.line_style(\n...     color=\"#fff\", thickness=5, joints=ap.LineJoints.ROUND\n... )\n>>> sprite.graphics.line_joints\nString('round')\n```",  # noqa
    ##################################################
    "## line_dot_setting property API": "## line_dot_setting 属性のAPI",
    ##################################################
    '<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>': '<span class="inconspicuous-txt">特記事項: このAPIドキュメントはドキュメントビルド用のスクリプトによって自動で生成・同期されています。そのためもしかしたらこの節の内容は前節までの内容と重複している場合があります。</span>',  # noqa
    ##################################################
    "**[Interface summary]**": "**[インターフェイス概要]**",
    ##################################################
    "Get current line dot setting.<hr>": "現在の線の点線設定を取得します。<hr>",
    ##################################################
    "**[Returns]**": "**[返却値]**",
    ##################################################
    "- `line_dot_setting`: LineDotSetting or None": "- `line_dot_setting`: LineDotSetting or None",  # noqa
    ##################################################
    "  - Current line dot setting.": "  - 現在の点線設定。",
    ##################################################
    "<hr>": "<hr>",
    ##################################################
    "**[Examples]**": "**[コードサンプル]**",
    ##################################################
    '```py\n>>> import apysc as ap\n>>> stage: ap.Stage = ap.Stage()\n>>> sprite: ap.Sprite = ap.Sprite()\n>>> sprite.graphics.line_style(\n...     color="#fff", thickness=5, dot_setting=ap.LineDotSetting(dot_size=5)\n... )\n>>> sprite.graphics.line_dot_setting.dot_size\nInt(5)\n```': '```py\n>>> import apysc as ap\n>>> stage: ap.Stage = ap.Stage()\n>>> sprite: ap.Sprite = ap.Sprite()\n>>> sprite.graphics.line_style(\n...     color="#fff", thickness=5, dot_setting=ap.LineDotSetting(dot_size=5)\n... )\n>>> sprite.graphics.line_dot_setting.dot_size\nInt(5)\n```',  # noqa
    ##################################################
    "## line_dash_setting property API": "## line_dash_setting 属性のAPI",
    ##################################################
    '<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>': '<span class="inconspicuous-txt">特記事項: このAPIドキュメントはドキュメントビルド用のスクリプトによって自動で生成・同期されています。そのためもしかしたらこの節の内容は前節までの内容と重複している場合があります。</span>',  # noqa
    ##################################################
    "**[Interface summary]**": "**[インターフェイス概要]**",
    ##################################################
    "Get current line dash setting.<hr>": "現在の線の破線のスタイル設定を取得します。<hr>",
    ##################################################
    "**[Returns]**": "**[返却値]**",
    ##################################################
    "- `line_dash_setting`: LineDashSetting or None": "- `line_dash_setting`: LineDashSetting or None",  # noqa
    ##################################################
    "  - Current line dash setting.": "  - 現在の破線設定。",
    ##################################################
    "<hr>": "<hr>",
    ##################################################
    "**[Examples]**": "**[コードサンプル]**",
    ##################################################
    '```py\n>>> import apysc as ap\n>>> stage: ap.Stage = ap.Stage()\n>>> sprite: ap.Sprite = ap.Sprite()\n>>> sprite.graphics.line_style(\n...     color="#fff",\n...     thickness=5,\n...     dash_setting=ap.LineDashSetting(dash_size=10, space_size=5),\n... )\n>>> sprite.graphics.line_dash_setting.dash_size\nInt(10)\n\n>>> sprite.graphics.line_dash_setting.space_size\nInt(5)\n```': '```py\n>>> import apysc as ap\n>>> stage: ap.Stage = ap.Stage()\n>>> sprite: ap.Sprite = ap.Sprite()\n>>> sprite.graphics.line_style(\n...     color="#fff",\n...     thickness=5,\n...     dash_setting=ap.LineDashSetting(dash_size=10, space_size=5),\n... )\n>>> sprite.graphics.line_dash_setting.dash_size\nInt(10)\n\n>>> sprite.graphics.line_dash_setting.space_size\nInt(5)\n```',  # noqa
    ##################################################
    "## line_round_dot_setting property API": "## line_round_dot_setting 属性のAPI",
    ##################################################
    '<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>': '<span class="inconspicuous-txt">特記事項: このAPIドキュメントはドキュメントビルド用のスクリプトによって自動で生成・同期されています。そのためもしかしたらこの節の内容は前節までの内容と重複している場合があります。</span>',  # noqa
    ##################################################
    "**[Interface summary]**": "**[インターフェイス概要]**",
    ##################################################
    "Get current line round dot setting.<hr>": "現在の線の丸ドットのスタイル設定を取得します。<hr>",
    ##################################################
    "**[Returns]**": "**[返却値]**",
    ##################################################
    "- `line_round_dot_setting`: LineRoundDotSetting or None": "- `line_round_dot_setting`: LineRoundDotSetting or None",  # noqa
    ##################################################
    "  - Current line round dot setting.": "  - 現在の線の丸ドットのスタイル設定。",
    ##################################################
    "<hr>": "<hr>",
    ##################################################
    "**[Examples]**": "**[コードサンプル]**",
    ##################################################
    '```py\n>>> import apysc as ap\n>>> stage: ap.Stage = ap.Stage()\n>>> sprite: ap.Sprite = ap.Sprite()\n>>> sprite.graphics.line_style(\n...     color="#fff",\n...     thickness=5,\n...     round_dot_setting=ap.LineRoundDotSetting(round_size=6, space_size=3),\n... )\n>>> sprite.graphics.line_round_dot_setting.round_size\nInt(6)\n\n>>> sprite.graphics.line_round_dot_setting.space_size\nInt(3)\n```': '```py\n>>> import apysc as ap\n>>> stage: ap.Stage = ap.Stage()\n>>> sprite: ap.Sprite = ap.Sprite()\n>>> sprite.graphics.line_style(\n...     color="#fff",\n...     thickness=5,\n...     round_dot_setting=ap.LineRoundDotSetting(round_size=6, space_size=3),\n... )\n>>> sprite.graphics.line_round_dot_setting.round_size\nInt(6)\n\n>>> sprite.graphics.line_round_dot_setting.space_size\nInt(3)\n```',  # noqa
    ##################################################
    "## line_dash_dot_setting property API": "## line_dash_dot_setting 属性のAPI",
    ##################################################
    '<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>': '<span class="inconspicuous-txt">特記事項: このAPIドキュメントはドキュメントビルド用のスクリプトによって自動で生成・同期されています。そのためもしかしたらこの節の内容は前節までの内容と重複している場合があります。</span>',  # noqa
    ##################################################
    "**[Interface summary]**": "**[インターフェイス概要]**",
    ##################################################
    "Get current line dash dot setting.<hr>": "現在の線の一点鎖線のスタイル設定を取得します。<hr>",
    ##################################################
    "**[Returns]**": "**[返却値]**",
    ##################################################
    "- `line_dash_dot_setting`: LineDashDotSetting or None": "- `line_dash_dot_setting`: LineDashDotSetting or None",  # noqa
    ##################################################
    "  - Current line dash dot setting.": "  - 現在の一点鎖線のスタイル設定。",
    ##################################################
    "<hr>": "<hr>",
    ##################################################
    "**[Examples]**": "**[コードサンプル]**",
    ##################################################
    '```py\n>>> import apysc as ap\n>>> stage: ap.Stage = ap.Stage()\n>>> sprite: ap.Sprite = ap.Sprite()\n>>> sprite.graphics.line_style(\n...     color="#fff",\n...     thickness=5,\n...     dash_dot_setting=ap.LineDashDotSetting(\n...         dot_size=2, dash_size=5, space_size=3\n...     ),\n... )\n>>> sprite.graphics.line_dash_dot_setting.dot_size\nInt(2)\n\n>>> sprite.graphics.line_dash_dot_setting.dash_size\nInt(5)\n\n>>> sprite.graphics.line_dash_dot_setting.space_size\nInt(3)\n```': '```py\n>>> import apysc as ap\n>>> stage: ap.Stage = ap.Stage()\n>>> sprite: ap.Sprite = ap.Sprite()\n>>> sprite.graphics.line_style(\n...     color="#fff",\n...     thickness=5,\n...     dash_dot_setting=ap.LineDashDotSetting(\n...         dot_size=2, dash_size=5, space_size=3\n...     ),\n... )\n>>> sprite.graphics.line_dash_dot_setting.dot_size\nInt(2)\n\n>>> sprite.graphics.line_dash_dot_setting.dash_size\nInt(5)\n\n>>> sprite.graphics.line_dash_dot_setting.space_size\nInt(3)\n```',  # noqa
}
