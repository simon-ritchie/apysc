"""This module is for the translation mapping data of the
following document:

Document file: graphics.md
Language: jp
"""

from typing import Dict

MAPPING: Dict[str, str] = {
    ##################################################
    "# Graphics class": "# Graphics クラス",
    ##################################################
    "This page explains the `Graphics` class.": "このページでは`Graphics`クラスについて説明します。",
    ##################################################
    "## What is Graphics?": "## Graphics クラスの概要",
    ##################################################
    "The `Graphics` is the class to handle each vector graphics interface. This interface has the draw rectangle interface, draw line interface, or something else.": "`Graphics`クラスは各ベクターグラフィックスの描画のインターフェイスを扱うクラスです。このインターフェイスには四角の描画や線の描画など様々なインターフェイスが存在します。",  # noqa
    ##################################################
    "The `Sprite` or other `DisplayObject` instances instantiate this class instance.": "`Sprite`クラスなどのインスタンスはこの`Graphics`クラスのインスタンスを内部で生成します。",  # noqa
    ##################################################
    "## Call interfaces from sprite instance": "## Sprite のインスタンスを経由した各インターフェイスの呼び出し",
    ##################################################
    "Sprite (object container) instance has the `graphics` attribute to call each drawing interface with this attribute.": "Sprite のインスタンスは`graphics`属性を持っており、その属性を使用して各描画のインターフェイスを呼び出すことができます。",  # noqa
    ##################################################
    '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    background_color=ap.Color("#333"),\n    stage_width=250,\n    stage_height=180,\n    stage_elem_id="stage",\n)\n\nsprite: ap.Sprite = ap.Sprite()\n\n# Draw the white border and cyan color rectangle.\nsprite.graphics.line_style(color=ap.Color("#fff"), thickness=5)\nsprite.graphics.begin_fill(color=ap.Color("#0af"))\nsprite.graphics.draw_rect(x=50, y=50, width=50, height=50)\n\n# Draw the magenta color polyline.\nsprite.graphics.begin_fill(color=ap.COLORLESS)\nsprite.graphics.line_style(color=ap.Color("#f0a"), thickness=5)\nsprite.graphics.move_to(x=150, y=50)\nsprite.graphics.line_to(x=200, y=50)\nsprite.graphics.line_to(x=150, y=100)\nsprite.graphics.line_to(x=200, y=100)\n\n# Draw the dashed line.\nsprite.graphics.draw_dashed_line(\n    x_start=50, y_start=130, x_end=200, y_end=130, dash_size=10, space_size=5\n)\n\nap.save_overall_html(dest_dir_path="graphics_call_interfaces_from_sprite_instance/")\n```': '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    background_color=ap.Color("#333"),\n    stage_width=250,\n    stage_height=180,\n    stage_elem_id="stage",\n)\n\nsprite: ap.Sprite = ap.Sprite()\n\n# Draw the white border and cyan color rectangle.\nsprite.graphics.line_style(color=ap.Color("#fff"), thickness=5)\nsprite.graphics.begin_fill(color=ap.Color("#0af"))\nsprite.graphics.draw_rect(x=50, y=50, width=50, height=50)\n\n# Draw the magenta color polyline.\nsprite.graphics.begin_fill(color=ap.COLORLESS)\nsprite.graphics.line_style(color=ap.Color("#f0a"), thickness=5)\nsprite.graphics.move_to(x=150, y=50)\nsprite.graphics.line_to(x=200, y=50)\nsprite.graphics.line_to(x=150, y=100)\nsprite.graphics.line_to(x=200, y=100)\n\n# Draw the dashed line.\nsprite.graphics.draw_dashed_line(\n    x_start=50, y_start=130, x_end=200, y_end=130, dash_size=10, space_size=5\n)\n\nap.save_overall_html(dest_dir_path="graphics_call_interfaces_from_sprite_instance/")\n```',  # noqa
    ##################################################
    "## Return values": "## 各返却値について",
    ##################################################
    "Each interface returns created graphic instances (e.g., `Rectangle`\\, `Polyline`\\, and so on). These instances have the basic `DisplayObject` attributes and methods, like x, y, fill_alpha, visible, or something else.": "各インターフェイスは`Rectangle`や`Polyline`クラスなどの生成されたグラフィックスのインスタンスを返却します。これらのインスタンスはxやy、fill_alpha、visibleなどの基本的な`DisplayObject`クラスの各属性やメソッドなどを持っています。",  # noqa
    ##################################################
    "For example, you can set an event and coordinate's updating to these instances, as follows:": "例えば以下のコード例のようにこれらのインスタンスに対してイベントを設定して座標の更新処理などを設定することができます:",  # noqa
    ##################################################
    '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    background_color=ap.Color("#333"),\n    stage_width=200,\n    stage_height=200,\n    stage_elem_id="stage",\n)\n\nsprite: ap.Sprite = ap.Sprite()\n\n\ndef on_rectangle_click(e: ap.MouseEvent[ap.Rectangle], options: dict) -> None:\n    """\n    The handler that the rectangle calls when clicked.\n\n    Parameters\n    ----------\n    e : MouseEvent\n        Event instance.\n    options : dict\n        Optional arguments dictionary.\n    """\n    rectangle: ap.Rectangle = e.this\n\n    # Update the coordinates, fill alpha, and fill color.\n    rectangle.x = ap.Number(100)\n    rectangle.y = ap.Number(100)\n    rectangle.fill_alpha = ap.Number(0.5)\n    rectangle.fill_color = ap.Color("#f0a")\n\n\n# drew_rect interface will return Rectangle instance.\nsprite.graphics.begin_fill(color=ap.Color("#0af"))\nrectangle: ap.Rectangle = sprite.graphics.draw_rect(x=50, y=50, width=50, height=50)\n\n# Bind click event to the rectangle.\nrectangle.click(on_rectangle_click)\n\nap.save_overall_html(dest_dir_path="graphics_return_values/")\n```': '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    background_color=ap.Color("#333"),\n    stage_width=200,\n    stage_height=200,\n    stage_elem_id="stage",\n)\n\nsprite: ap.Sprite = ap.Sprite()\n\n\ndef on_rectangle_click(e: ap.MouseEvent[ap.Rectangle], options: dict) -> None:\n    """\n    The handler that the rectangle calls when clicked.\n\n    Parameters\n    ----------\n    e : MouseEvent\n        Event instance.\n    options : dict\n        Optional arguments dictionary.\n    """\n    rectangle: ap.Rectangle = e.this\n\n    # Update the coordinates, fill alpha, and fill color.\n    rectangle.x = ap.Number(100)\n    rectangle.y = ap.Number(100)\n    rectangle.fill_alpha = ap.Number(0.5)\n    rectangle.fill_color = ap.Color("#f0a")\n\n\n# drew_rect interface will return Rectangle instance.\nsprite.graphics.begin_fill(color=ap.Color("#0af"))\nrectangle: ap.Rectangle = sprite.graphics.draw_rect(x=50, y=50, width=50, height=50)\n\n# Bind click event to the rectangle.\nrectangle.click(on_rectangle_click)\n\nap.save_overall_html(dest_dir_path="graphics_return_values/")\n```',  # noqa
    ##################################################
    "If you click the following rectangle, that rectangle changes x and y coordinates, fill color, and alpha (opacity) values.": "もし以下の四角をクリックすると座標値や塗りの色、透明度などの値が更新されます。",  # noqa
    ##################################################
    "## See also": "## 関連資料",
    ##################################################
    "- [Graphics class begin_fill interface](graphics_begin_fill.md)": "- [Graphics クラスの begin_fill (塗りの設定)のインターフェイス](jp_graphics_begin_fill.md)",  # noqa
    ##################################################
    "- [Graphics class line_style interface](graphics_line_style.md)": "- [Graphics クラスの line_style (線のスタイル設定)のインターフェイス](jp_graphics_line_style.md)",  # noqa
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
}
