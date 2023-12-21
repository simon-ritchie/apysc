"""This module is for the translation mapping data of the
following document:

Document file: draw_interfaces_abstract.md
Language: jp
"""

from typing import Dict

MAPPING: Dict[str, str] = {
    ##################################################
    "# Draw interfaces abstract": "# 描画の各インターフェイスの概要",
    ##################################################
    "This page would explain the drawing interfaces abstract.": "このページでは描画の各インターフェイスについて説明します。",  # noqa
    ##################################################
    "## What apysc can do in its drawing interfaces": "## apyscの描画の各インターフェイスでできること",
    ##################################################
    "- You can set the fill-color, fill-alpha (opacity), line-color, line-alpha, line-thickness values and draw each SVG graphic with these.": "- これらのインターフェイスを使って塗りの色、塗りの透明度、線の色、線の透明度、線幅などを設定することができます。",  # noqa
    ##################################################
    "- Supported graphics: The rectangle, circle, ellipse, polygon, line, polyline, and path.": "- 四角や丸、楕円、多角形、線、折れ線、パスなどの描画をサポートしています。",  # noqa
    ##################################################
    "## Fill settings": "## 塗りの設定",
    ##################################################
    "The `begin_fill` interface sets the fill-color and fill-alpha (opacity).": "`begin_fill`のインターフェイスは塗りの色と塗りの透明度を設定します。",  # noqa
    ##################################################
    '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    background_color=ap.Color("#333"),\n    stage_width=150,\n    stage_height=150,\n    stage_elem_id="stage",\n)\nsprite: ap.Sprite = ap.Sprite()\nsprite.graphics.begin_fill(color=ap.Color("#0af"), alpha=0.5)\nsprite.graphics.draw_rect(x=50, y=50, width=50, height=50)\n\nap.save_overall_html(dest_dir_path="draw_interfaces_abstract_begin_fill/")\n```': '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    background_color=ap.Color("#333"),\n    stage_width=150,\n    stage_height=150,\n    stage_elem_id="stage",\n)\nsprite: ap.Sprite = ap.Sprite()\nsprite.graphics.begin_fill(color=ap.Color("#0af"), alpha=0.5)\nsprite.graphics.draw_rect(x=50, y=50, width=50, height=50)\n\nap.save_overall_html(dest_dir_path="draw_interfaces_abstract_begin_fill/")\n```',  # noqa
    ##################################################
    "For more details, please see:": "詳細は以下をご確認ください:",
    ##################################################
    "- [Graphics class begin_fill interface](graphics_begin_fill.md).": "- [Graphics クラスの begin_fill (塗りの設定)のインターフェイス](jp_graphics_begin_fill.md)",  # noqa
    ##################################################
    "## Line style settings": "## 線のスタイル設定",
    ##################################################
    "The `line_style` interface sets the line-color, line-alpha (opacity), line-thickness.": "`line_style`インターフェイスは線の色と線の透明度、線幅などを設定することができます。",  # noqa
    ##################################################
    '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    background_color=ap.Color("#333"),\n    stage_width=200,\n    stage_height=100,\n    stage_elem_id="stage",\n)\nsprite: ap.Sprite = ap.Sprite()\nsprite.graphics.line_style(color=ap.Color("#fff"), thickness=5, alpha=0.5)\nsprite.graphics.draw_line(x_start=50, y_start=50, x_end=150, y_end=50)\n\nap.save_overall_html(dest_dir_path="draw_interfaces_abstract_line_style/")\n```': '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    background_color=ap.Color("#333"),\n    stage_width=200,\n    stage_height=100,\n    stage_elem_id="stage",\n)\nsprite: ap.Sprite = ap.Sprite()\nsprite.graphics.line_style(color=ap.Color("#fff"), thickness=5, alpha=0.5)\nsprite.graphics.draw_line(x_start=50, y_start=50, x_end=150, y_end=50)\n\nap.save_overall_html(dest_dir_path="draw_interfaces_abstract_line_style/")\n```',  # noqa
    ##################################################
    "For more details, please see:": "詳細は以下をご確認ください:",
    ##################################################
    "- [Graphics class line_style interface](graphics_line_style.md).": "- [Graphics クラスの line_style (線のスタイル設定)のインターフェイス](jp_graphics_line_style.md)",  # noqa
    ##################################################
    "## Each drawing interface": "## 描画の各インターフェイス",
    ##################################################
    "Each drawing interface has the `draw_` prefix draw SVG graphics (e.g., draw_rect, draw_circle).": "各描画のインターフェイスは`draw_`のプレフィックスを持っており、SVGのグラフィックを描画します（例 : draw_rect や draw_circle など）。",  # noqa
    ##################################################
    '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    background_color=ap.Color("#333"),\n    stage_width=250,\n    stage_height=150,\n    stage_elem_id="stage",\n)\nsprite: ap.Sprite = ap.Sprite()\nsprite.graphics.begin_fill(color=ap.Color("#0af"))\nsprite.graphics.draw_rect(x=50, y=50, width=50, height=50)\nsprite.graphics.draw_circle(x=175, y=75, radius=25)\n\nap.save_overall_html(dest_dir_path="draw_interfaces_abstract_each_drawing_interface/")\n```': '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    background_color=ap.Color("#333"),\n    stage_width=250,\n    stage_height=150,\n    stage_elem_id="stage",\n)\nsprite: ap.Sprite = ap.Sprite()\nsprite.graphics.begin_fill(color=ap.Color("#0af"))\nsprite.graphics.draw_rect(x=50, y=50, width=50, height=50)\nsprite.graphics.draw_circle(x=175, y=75, radius=25)\n\nap.save_overall_html(dest_dir_path="draw_interfaces_abstract_each_drawing_interface/")\n```',  # noqa
    ##################################################
    "For more details, please see the following:": "詳細については以下をご確認ください:",
    ##################################################
    "- [Graphics class draw_rect interface](graphics_draw_rect.md)": "- [Graphics クラスの draw_rect (四角の描画)のインターフェイス](jp_graphics_draw_rect.md)",  # noqa
    ##################################################
    "- [Graphics class draw_round_rect interface](graphics_draw_round_rect.md)": "- [Graphics クラスの draw_round_rect (角丸の四角の描画)のインターフェイス](jp_graphics_draw_round_rect.md)",  # noqa
    ##################################################
    "- [Graphics class draw_circle interface](graphics_draw_circle.md)": "- [Graphics クラスの draw_circle (円の描画)のインターフェイス](jp_graphics_draw_circle.md)",  # noqa
    ##################################################
    "- [Graphics class draw_ellipse interface](graphics_draw_ellipse.md)": "- [Graphics クラスの draw_ellipse (楕円描画) のインターフェイス](jp_graphics_draw_ellipse.md)",  # noqa
    ##################################################
    "- [Graphics class move_to and line_to interfaces](graphics_move_to_and_line_to.md)": "- [Graphics クラスの move_to (線の描画位置の変更)と line_to (指定座標への線の描画)のインターフェイス](jp_graphics_move_to_and_line_to.md)",  # noqa
    ##################################################
    "- [Graphics class draw_line interface](graphics_draw_line.md)": "- [Graphics クラスの draw_line (線の描画)のインターフェイス](jp_graphics_draw_line.md)",  # noqa
    ##################################################
    "- [Graphics class draw_dotted_line interface](graphics_draw_dotted_line.md)": "- [Graphics クラスの draw_dotted_line (点線の描画)のインターフェイス](jp_graphics_draw_dotted_line.md)",  # noqa
    ##################################################
    "- [Graphics class draw_dashed_line interface](graphics_draw_dashed_line.md)": "- [Graphics クラスの draw_dashed_line (破線の描画)のインターフェイス](jp_graphics_draw_dashed_line.md)",  # noqa
    ##################################################
    "- [Graphics class draw_round_dotted_line interface](graphics_draw_round_dotted_line.md)": "- [Graphics クラスの draw_round_dotted_line (点線(丸)の描画)のインターフェイス](jp_graphics_draw_round_dotted_line.md)",  # noqa
    ##################################################
    "- [Graphics class draw_dash_dotted_line interface](graphics_draw_dash_dotted_line.md)": "- [Graphics クラスの draw_dash_dotted_line (一点鎖線の描画)のインターフェイス](jp_graphics_draw_dash_dotted_line.md)",  # noqa
    ##################################################
    "- [Graphics class draw_polygon interface](graphics_draw_polygon.md)": "- [Graphics クラスの draw_polygon (多角形描画)のインターフェイス](jp_graphics_draw_polygon.md)",  # noqa
    ##################################################
    "## See also": "## 関連資料",
    ##################################################
    "- [Graphics class](graphics.md)": "- [Graphics クラス](jp_graphics.md)",
    ##################################################
    "- [GraphicsBase class fill_color interface](graphics_base_fill_color.md)": "- [GraphicsBase クラスの fill_color (塗り設定)のインターフェイス](jp_graphics_base_fill_color.md)",  # noqa
    ##################################################
    "- [GraphicsBase class fill_alpha interface](graphics_base_fill_alpha.md)": "- [GraphicsBase クラスの fill_alpha (塗りの透明度設定)のインターフェイス](jp_graphics_base_fill_alpha.md)",  # noqa
    ##################################################
    "- [GraphicsBase class line_color interface](graphics_base_line_color.md)": "- [GraphicsBase クラスの line_color (線の色設定)のインターフェイス](jp_graphics_base_line_color.md)",  # noqa
    ##################################################
    "- [GraphicsBase class line_alpha interface](graphics_base_line_alpha.md)": "- [GraphicsBase クラスの line_color (線の透明度設定)のインターフェイス](jp_graphics_base_line_alpha.md)",  # noqa
    ##################################################
    "- [GraphicsBase class line_thickness interface](graphics_base_line_thickness.md)": "- [GraphicsBase クラスの line_color (線幅設定)のインターフェイス](jp_graphics_base_line_thickness.md)",  # noqa
    ##################################################
    "- [GraphicsBase class line_dot_setting interface](graphics_base_line_dot_setting.md)": "- [GraphicsBase クラスの line_dot_setting (点線設定)のインターフェイス](jp_graphics_base_line_dot_setting.md)",  # noqa
    ##################################################
    "- [GraphicsBase class line_dash_setting interface](graphics_base_line_dash_setting.md)": "- [GraphicsBase クラスの line_dash_setting (破線設定)のインターフェイス](jp_graphics_base_line_dash_setting.md)",  # noqa
    ##################################################
    "- [GraphicsBase class line_round_dot_setting interface](graphics_base_line_round_dot_setting.md)": "- [GraphicsBase クラスの line_round_dot_setting (点線(丸)設定)のインターフェイス](jp_graphics_base_line_round_dot_setting.md)",  # noqa
    ##################################################
    "- [GraphicsBase class line_dash_dot_setting interface](graphics_base_line_dash_dot_setting.md)": "- [GraphicsBase クラスの line_dash_dot_setting (一点鎖線設定)のインターフェイス](jp_graphics_base_line_dash_dot_setting.md)",  # noqa
}
