"""This module is for the translation mapping data of the
following document:

Document file: what_apysc_can_do.md
Language: jp
"""

from typing import Dict

MAPPING: Dict[str, str] = {
    ##################################################
    "# What apysc can do in its current implementation": "# apysc ライブラリが現在の実装でできること",
    ##################################################
    "This page explains the current apysc implementation and functionality summary.": "このページでは apysc ライブパリの現在の実装と機能の概要について説明します。",  # noqa
    ##################################################
    "## Write with the Python and export HTML or use it on the Jupyter": "## Pythonを使って書き、それをHTMLへ出力・もしくはJupyter上で利用する",  # noqa
    ##################################################
    "The apysc library can write the front-end with the Python language and export the HTML or use it on the Jupyter notebook, JupyterLab, and the Google Colaboratory!": "apysc ライブラリではフロントエンドをPythonを使って書くことができ、結果をHTMLに出力したりもしくはJupyter notebookやJupyterLab、Google Colaboratory上などで表示することができます。",  # noqa
    ##################################################
    "See also:": "参考資料:",
    ##################################################
    "- [save_overall_html interface](save_overall_html.md)": "- [save_overall_html インターフェイス](jp_save_overall_html.md)",  # noqa
    ##################################################
    "- [display_on_jupyter interface](display_on_jupyter.md)": "- [display_on_jupyter インターフェイス](jp_display_on_jupyter.md)",  # noqa
    ##################################################
    "- [display_on_colaboratory interface](display_on_colaboratory.md)": "- [display_on_colaboratory インターフェイス](jp_display_on_colaboratory.md)",  # noqa
    ##################################################
    "## Draw the many types of the vector graphics": "## 様々な種類のベクターグラフィックスの描画",
    ##################################################
    "The apysc library can draw many vector graphics types, like the rectangle, circle, line.": "apysc ライブラリでは四角や円、線などの様々な種類のベクターグラフィックスの描画を行うことができます。",  # noqa
    ##################################################
    "<details>\n<summary>Display the code block:</summary>": "<details>\n<summary>コードブロックを表示:</summary>",  # noqa
    ##################################################
    '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    stage_width=650, stage_height=210, background_color="#333", stage_elem_id="stage"\n)\nsprite: ap.Sprite = ap.Sprite()\n\nsprite.graphics.begin_fill(color="#0af")\nsprite.graphics.draw_rect(x=50, y=50, width=50, height=50)\n\nsprite.graphics.draw_round_rect(\n    x=150, y=50, width=50, height=50, ellipse_width=12, ellipse_height=12\n)\n\nsprite.graphics.draw_circle(x=275, y=75, radius=25)\n\nsprite.graphics.draw_ellipse(x=375, y=75, width=50, height=30)\n\nsprite.graphics.draw_polygon(\n    points=[\n        ap.Point2D(x=475, y=50),\n        ap.Point2D(x=450, y=100),\n        ap.Point2D(x=500, y=100),\n    ]\n)\n\nsprite.graphics.begin_fill(color="")\nsprite.graphics.line_style(color="#eee", thickness=3)\nsprite.graphics.move_to(x=550, y=50)\nsprite.graphics.line_to(x=600, y=50)\nsprite.graphics.line_to(x=550, y=100)\nsprite.graphics.line_to(x=600, y=100)\n\nsprite.graphics.draw_line(x_start=50, y_start=130, x_end=600, y_end=130)\nsprite.graphics.draw_dotted_line(\n    x_start=50, y_start=145, x_end=600, y_end=145, dot_size=2\n)\nsprite.graphics.draw_round_dotted_line(\n    x_start=53, y_start=160, x_end=600, y_end=160, round_size=6, space_size=6\n)\n\nap.save_overall_html(dest_dir_path="what_apysc_can_do_draw_vector_graphics/")\n```': '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    stage_width=650, stage_height=210, background_color="#333", stage_elem_id="stage"\n)\nsprite: ap.Sprite = ap.Sprite()\n\nsprite.graphics.begin_fill(color="#0af")\nsprite.graphics.draw_rect(x=50, y=50, width=50, height=50)\n\nsprite.graphics.draw_round_rect(\n    x=150, y=50, width=50, height=50, ellipse_width=12, ellipse_height=12\n)\n\nsprite.graphics.draw_circle(x=275, y=75, radius=25)\n\nsprite.graphics.draw_ellipse(x=375, y=75, width=50, height=30)\n\nsprite.graphics.draw_polygon(\n    points=[\n        ap.Point2D(x=475, y=50),\n        ap.Point2D(x=450, y=100),\n        ap.Point2D(x=500, y=100),\n    ]\n)\n\nsprite.graphics.begin_fill(color="")\nsprite.graphics.line_style(color="#eee", thickness=3)\nsprite.graphics.move_to(x=550, y=50)\nsprite.graphics.line_to(x=600, y=50)\nsprite.graphics.line_to(x=550, y=100)\nsprite.graphics.line_to(x=600, y=100)\n\nsprite.graphics.draw_line(x_start=50, y_start=130, x_end=600, y_end=130)\nsprite.graphics.draw_dotted_line(\n    x_start=50, y_start=145, x_end=600, y_end=145, dot_size=2\n)\nsprite.graphics.draw_round_dotted_line(\n    x_start=53, y_start=160, x_end=600, y_end=160, round_size=6, space_size=6\n)\n\nap.save_overall_html(dest_dir_path="what_apysc_can_do_draw_vector_graphics/")\n```',  # noqa
    ##################################################
    "</details>": "</details>",
    ##################################################
    "See also:": "参考資料:",
    ##################################################
    "- [Graphics class](graphics.md)": "- [Graphics クラス](jp_graphics.md)",
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
    ##################################################
    "## Set each mouse event": "## 各種マウスイベントの設定",
    ##################################################
    "The apysc library supports each mouse event, like the click, mouse down, mouse over, mouse move.": "apysc ライブラリではクリックやマウスダウン、マウスオーバー、マウスムーブなどの各種マウスイベントの設定をサポートしています。",  # noqa
    ##################################################
    "The click event example (please click the following rectangle):": "クリックイベントの例（以下の四角をクリックしてご確認ください）:",  # noqa
    ##################################################
    "<details>\n<summary>Display the code block:</summary>": "<details>\n<summary>コードブロックを表示:</summary>",  # noqa
    ##################################################
    '```py\n# runnable\nimport apysc as ap\n\n\ndef on_click(e: ap.MouseEvent[ap.Rectangle], options: dict) -> None:\n    """\n    The handler that the rectangle calls when clicked.\n\n    Parameters\n    ----------\n    e : ap.MouseEvent\n        Event instance.\n    options : dict\n        Optional arguments dictionary.\n    """\n    color: ap.String = e.this.fill_color\n    condition: ap.Boolean = color == "#00aaff"\n    with ap.If(condition):\n        e.this.fill_color = ap.String("#f0a")\n    with ap.Else():\n        e.this.fill_color = ap.String("#0af")\n\n\nap.Stage(\n    stage_width=150, stage_height=150, background_color="#333", stage_elem_id="stage"\n)\nsprite: ap.Sprite = ap.Sprite()\n\nsprite.graphics.begin_fill(color="#0af")\nrectangle: ap.Rectangle = sprite.graphics.draw_rect(x=50, y=50, width=50, height=50)\nrectangle.click(on_click)\n\nap.save_overall_html(dest_dir_path="what_apysc_can_do_mouse_event_click/")\n```': '```py\n# runnable\nimport apysc as ap\n\n\ndef on_click(e: ap.MouseEvent[ap.Rectangle], options: dict) -> None:\n    """\n    The handler that the rectangle calls when clicked.\n\n    Parameters\n    ----------\n    e : ap.MouseEvent\n        Event instance.\n    options : dict\n        Optional arguments dictionary.\n    """\n    color: ap.String = e.this.fill_color\n    condition: ap.Boolean = color == "#00aaff"\n    with ap.If(condition):\n        e.this.fill_color = ap.String("#f0a")\n    with ap.Else():\n        e.this.fill_color = ap.String("#0af")\n\n\nap.Stage(\n    stage_width=150, stage_height=150, background_color="#333", stage_elem_id="stage"\n)\nsprite: ap.Sprite = ap.Sprite()\n\nsprite.graphics.begin_fill(color="#0af")\nrectangle: ap.Rectangle = sprite.graphics.draw_rect(x=50, y=50, width=50, height=50)\nrectangle.click(on_click)\n\nap.save_overall_html(dest_dir_path="what_apysc_can_do_mouse_event_click/")\n```',  # noqa
    ##################################################
    "</details>": "</details>",
    ##################################################
    "See also:": "参考資料:",
    ##################################################
    "- [Basic mouse event interfaces](mouse_event_basic.md)": "- [基本的なマウスイベントの各インターフェイス](jp_mouse_event_basic.md)",  # noqa
    ##################################################
    "- [click interface](click.md)": "- [click インターフェイス](jp_click.md)",
    ##################################################
    "- [mousedown and mouseup interfaces](mousedown_and_mouseup.md)": "- [mousedown と mouseup のインターフェイス](jp_mousedown_and_mouseup.md)",  # noqa
    ##################################################
    "- [mouseover and mouseout interfaces](mouseover_and_mouseout.md)": "- [mouseover と mouseout のインターフェイス](jp_mouseover_and_mouseout.md)",  # noqa
    ##################################################
    "- [mousemove interface](mousemove.md)": "- [mousemove インターフェイス](jp_mousemove.md)",
    ##################################################
    "## The timer interface and animation": "## タイマーのインターフェイスとアニメーション",
    ##################################################
    "You can use the timer-related interfaces and animate with them.": "タイマーに関係したインターフェイスを利用することができ、それを使ってアニメーションを設定することができます。",  # noqa
    ##################################################
    "<details>\n<summary>Display the code block:</summary>": "<details>\n<summary>コードブロックを表示:</summary>",  # noqa
    ##################################################
    '```py\n# runnable\nfrom typing_extensions import TypedDict\n\nimport apysc as ap\n\n\nclass _Options(TypedDict):\n    rectangle: ap.Rectangle\n    alpha_direction: ap.Int\n\n\ndef on_timer(e: ap.TimerEvent, options: _Options) -> None:\n    """\n    The handler that the timer calls.\n\n    Parameters\n    ----------\n    e : ap.TimerEvent\n        Event instance.\n    options : dict\n        Optional arguments dictionary.\n    """\n    rectangle: ap.Rectangle = options["rectangle"]\n    alpha_direction: ap.Int = options["alpha_direction"]\n    current_alpha: ap.Number = rectangle.fill_alpha\n    condition_1: ap.Boolean = current_alpha < 0.0\n    condition_2: ap.Boolean = current_alpha > 1.0\n    with ap.If(condition_1):\n        alpha_direction.value = 1\n    with ap.Elif(condition_2):\n        alpha_direction.value = -1\n    rectangle.fill_alpha += alpha_direction * 0.03\n    rectangle.rotation_around_center += 1\n\n\nap.Stage(\n    stage_width=150, stage_height=150, background_color="#333", stage_elem_id="stage"\n)\nsprite: ap.Sprite = ap.Sprite()\n\nsprite.graphics.begin_fill(color="#0af")\nalpha_direction: ap.Int = ap.Int(1)\nrectangle: ap.Rectangle = sprite.graphics.draw_rect(x=50, y=50, width=50, height=50)\noptions: _Options = {"rectangle": rectangle, "alpha_direction": alpha_direction}\ntimer: ap.Timer = ap.Timer(on_timer, delay=ap.FPS.FPS_60, options=options)\ntimer.start()\n\nap.save_overall_html(dest_dir_path="what_apysc_can_do_timer_animation/")\n```': '```py\n# runnable\nfrom typing_extensions import TypedDict\n\nimport apysc as ap\n\n\nclass _Options(TypedDict):\n    rectangle: ap.Rectangle\n    alpha_direction: ap.Int\n\n\ndef on_timer(e: ap.TimerEvent, options: _Options) -> None:\n    """\n    The handler that the timer calls.\n\n    Parameters\n    ----------\n    e : ap.TimerEvent\n        Event instance.\n    options : dict\n        Optional arguments dictionary.\n    """\n    rectangle: ap.Rectangle = options["rectangle"]\n    alpha_direction: ap.Int = options["alpha_direction"]\n    current_alpha: ap.Number = rectangle.fill_alpha\n    condition_1: ap.Boolean = current_alpha < 0.0\n    condition_2: ap.Boolean = current_alpha > 1.0\n    with ap.If(condition_1):\n        alpha_direction.value = 1\n    with ap.Elif(condition_2):\n        alpha_direction.value = -1\n    rectangle.fill_alpha += alpha_direction * 0.03\n    rectangle.rotation_around_center += 1\n\n\nap.Stage(\n    stage_width=150, stage_height=150, background_color="#333", stage_elem_id="stage"\n)\nsprite: ap.Sprite = ap.Sprite()\n\nsprite.graphics.begin_fill(color="#0af")\nalpha_direction: ap.Int = ap.Int(1)\nrectangle: ap.Rectangle = sprite.graphics.draw_rect(x=50, y=50, width=50, height=50)\noptions: _Options = {"rectangle": rectangle, "alpha_direction": alpha_direction}\ntimer: ap.Timer = ap.Timer(on_timer, delay=ap.FPS.FPS_60, options=options)\ntimer.start()\n\nap.save_overall_html(dest_dir_path="what_apysc_can_do_timer_animation/")\n```',  # noqa
    ##################################################
    "</details>": "</details>",
    ##################################################
    "See also:": "参考資料:",
    ##################################################
    "- [Timer class](timer.md)": "- [Timer クラス](jp_timer.md)",
    ##################################################
    "- [TimerEvent class](timer_event.md)": "- [TimerEvent クラス](jp_timer_event.md)",
    ##################################################
    "- [Timer class delay setting](timer_delay.md)": "- [Timer クラスの delay 設定](jp_timer_delay.md)",  # noqa
    ##################################################
    "- [FPS enum](fps.md)": "- [FPS の enum](jp_fps.md)",
    ##################################################
    "- [Timer class repeat_count setting](timer_repeat_count.md)": "- [Timer クラスの repeat_count 設定](jp_timer_repeat_count.md)",  # noqa
    ##################################################
    "- [Timer class start and stop interfaces](timer_start_and_stop.md)": "- [Timer クラスの start と stop の各インターフェイス](jp_timer_start_and_stop.md)",  # noqa
    ##################################################
    "- [Timer class timer_complete interface](timer_complete.md)": "- [Timer クラスの timer_complete インターフェイス](jp_timer_complete.md)",  # noqa
    ##################################################
    "- [Timer class reset interface](timer_reset.md)": "- [Timer クラスの reset インターフェイス](jp_timer_reset.md)",  # noqa
    ##################################################
    "## Animate properties with each animation interface": "## アニメーションのインターフェイスによる各属性のアニメーション",  # noqa
    ##################################################
    "You can use each animation (tween) interface and animate with them.": "各アニメーション（Tween）のインターフェイスを使ってアニメーションをさせることができます。",  # noqa
    ##################################################
    "See also:": "参考資料:",
    ##################################################
    "- [Animation interfaces abstract](animation_interfaces_abstract.md)": "- [アニメーションの各インターフェイスの概要](jp_animation_interfaces_abstract.md)",  # noqa
}
