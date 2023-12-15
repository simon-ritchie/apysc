"""This module is for the translation mapping data of the
following document:

Document file: triangle.md
Language: jp
"""

from typing import Dict

MAPPING: Dict[str, str] = {
    ##################################################
    "# Triangle class": "# Triangle クラス",
    ##################################################
    "This page explains the `Triangle` class.": "このページでは`Triangle`クラスについて説明します。",
    ##################################################
    "## What class is this?": "## クラス概要",
    ##################################################
    "The `Triangle` class creates a triangle vector graphics object.": "`Triangle`クラスは三角形のベクターグラフィックスのオブジェクトを生成します。",  # noqa
    ##################################################
    "## Basic usage": "## 基本的な使い方",
    ##################################################
    "The `Triangle` class constructor requires the `x1`, `y1`, `x2`, `y2`, `x3`, and `y3` arguments.": "`Triangle`クラスのコンストラクタでは`x1`、`y1`、`x2`、`y2`、`x3`、`y3`の各引数の指定を必要とします。",  # noqa
    ##################################################
    "The `x1` and `y1` arguments are the first vertex's coordinates.": "`x1`と`y1`引数は1つ目の頂点の座標となります。",  # noqa
    ##################################################
    "Similarly, the `x2` and `y2` are the second vertex's coordinates, and the `x3` and `y3` are the third.": "同様に、`x2`と`y2`引数は2つ目の頂点の座標となり、`x3`と`y3`は3つ目の頂点の座標となります。",  # noqa
    ##################################################
    "The constructor also accepts each style's argument, such as the `fill_color`.": "コンストラクタでは他の`fill_color`などのスタイル設定の各引数も受け付けます。",  # noqa
    ##################################################
    '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    background_color=ap.Color("#333"),\n    stage_width=150,\n    stage_height=150,\n    stage_elem_id="stage",\n)\ntriangle: ap.Triangle = ap.Triangle(\n    x1=75,\n    y1=50,\n    x2=50,\n    y2=100,\n    x3=100,\n    y3=100,\n    fill_color=ap.Color("#0af"),\n)\n\nap.save_overall_html(dest_dir_path="triangle_basic_usage/")\n```': '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    background_color=ap.Color("#333"),\n    stage_width=150,\n    stage_height=150,\n    stage_elem_id="stage",\n)\ntriangle: ap.Triangle = ap.Triangle(\n    x1=75,\n    y1=50,\n    x2=50,\n    y2=100,\n    x3=100,\n    y3=100,\n    fill_color=ap.Color("#0af"),\n)\n\nap.save_overall_html(dest_dir_path="triangle_basic_usage/")\n```',  # noqa
    ##################################################
    "## Note of the draw_triangle interface": "## draw_triangle インターフェイスの特記事項",
    ##################################################
    "you can also create a triangle instance with the `draw_triangle` interface.": "`draw_triangle`インターフェイスを使うことでも三角形のインスタンスを生成することができます。",  # noqa
    ##################################################
    "For more details, please see the following:": "詳細については以下をご確認ください:",
    ##################################################
    "- [Graphics draw_triangle interface](graphics_draw_triangle.md)": "- [Graphics クラスの draw_triangle インターフェイス](jp_graphics_draw_triangle.md)",  # noqa
    ##################################################
    "## x property interface example": "## x属性のインターフェイス例",
    ##################################################
    "The `x` property updates or gets the instance's x-coordinate:": "`x`属性ではX座標の値の更新もしくは取得を行えます:",  # noqa
    ##################################################
    '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    background_color=ap.Color("#333"),\n    stage_width=150,\n    stage_height=150,\n    stage_elem_id="stage",\n)\ntriangle: ap.Triangle = ap.Triangle(\n    x1=75,\n    y1=50,\n    x2=50,\n    y2=100,\n    x3=100,\n    y3=100,\n    fill_color=ap.Color("#0af"),\n)\ntriangle.x = ap.Number(100)\n\nap.save_overall_html(dest_dir_path="triangle_x/")\n```': '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    background_color=ap.Color("#333"),\n    stage_width=150,\n    stage_height=150,\n    stage_elem_id="stage",\n)\ntriangle: ap.Triangle = ap.Triangle(\n    x1=75,\n    y1=50,\n    x2=50,\n    y2=100,\n    x3=100,\n    y3=100,\n    fill_color=ap.Color("#0af"),\n)\ntriangle.x = ap.Number(100)\n\nap.save_overall_html(dest_dir_path="triangle_x/")\n```',  # noqa
    ##################################################
    "## y property interface example": "## y属性のインターフェイス例",
    ##################################################
    "The `y` property updates or gets the instance's y-coordinate:": "`y`属性ではY座標の値の更新もしくは取得を行えます:",  # noqa
    ##################################################
    '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    background_color=ap.Color("#333"),\n    stage_width=150,\n    stage_height=150,\n    stage_elem_id="stage",\n)\ntriangle: ap.Triangle = ap.Triangle(\n    x1=75,\n    y1=50,\n    x2=50,\n    y2=100,\n    x3=100,\n    y3=100,\n    fill_color=ap.Color("#0af"),\n)\ntriangle.y = ap.Number(100)\n\nap.save_overall_html(dest_dir_path="triangle_y/")\n```': '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    background_color=ap.Color("#333"),\n    stage_width=150,\n    stage_height=150,\n    stage_elem_id="stage",\n)\ntriangle: ap.Triangle = ap.Triangle(\n    x1=75,\n    y1=50,\n    x2=50,\n    y2=100,\n    x3=100,\n    y3=100,\n    fill_color=ap.Color("#0af"),\n)\ntriangle.y = ap.Number(100)\n\nap.save_overall_html(dest_dir_path="triangle_y/")\n```',  # noqa
    ##################################################
    "## x1 property interface example": "## x1属性のインターフェイス例",
    ##################################################
    "The `x1` property updates or gets the instance's first vertex x-coordinate:": "`x1`属性では1つ目の頂点のX座標の更新もしくは取得を行えます:",  # noqa
    ##################################################
    '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    background_color=ap.Color("#333"),\n    stage_width=150,\n    stage_height=150,\n    stage_elem_id="stage",\n)\ntriangle: ap.Triangle = ap.Triangle(\n    x1=75,\n    y1=50,\n    x2=50,\n    y2=100,\n    x3=100,\n    y3=100,\n    fill_color=ap.Color("#0af"),\n)\ntriangle.x1 = ap.Number(100)\n\nap.save_overall_html(dest_dir_path="triangle_x1/")\n```': '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    background_color=ap.Color("#333"),\n    stage_width=150,\n    stage_height=150,\n    stage_elem_id="stage",\n)\ntriangle: ap.Triangle = ap.Triangle(\n    x1=75,\n    y1=50,\n    x2=50,\n    y2=100,\n    x3=100,\n    y3=100,\n    fill_color=ap.Color("#0af"),\n)\ntriangle.x1 = ap.Number(100)\n\nap.save_overall_html(dest_dir_path="triangle_x1/")\n```',  # noqa
    ##################################################
    "## y1 property interface example": "## y1属性のインターフェイス例",
    ##################################################
    "The `y1` property updates or gets the instance's first vertex y-coordinate:": "`y1`属性では1つ目の頂点のY座標の更新もしくは取得を行えます:",  # noqa
    ##################################################
    '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    background_color=ap.Color("#333"),\n    stage_width=150,\n    stage_height=150,\n    stage_elem_id="stage",\n)\ntriangle: ap.Triangle = ap.Triangle(\n    x1=75,\n    y1=50,\n    x2=50,\n    y2=100,\n    x3=100,\n    y3=100,\n    fill_color=ap.Color("#0af"),\n)\ntriangle.y1 = ap.Number(0)\n\nap.save_overall_html(dest_dir_path="triangle_y1/")\n```': '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    background_color=ap.Color("#333"),\n    stage_width=150,\n    stage_height=150,\n    stage_elem_id="stage",\n)\ntriangle: ap.Triangle = ap.Triangle(\n    x1=75,\n    y1=50,\n    x2=50,\n    y2=100,\n    x3=100,\n    y3=100,\n    fill_color=ap.Color("#0af"),\n)\ntriangle.y1 = ap.Number(0)\n\nap.save_overall_html(dest_dir_path="triangle_y1/")\n```',  # noqa
    ##################################################
    "## x2 property interface example": "## x2属性のインターフェイス例",
    ##################################################
    "The `x2` property updates or gets the instance's second vertex x-coordinate:": "`x2`属性では2つ目の頂点のX座標の更新もしくは取得を行えます:",  # noqa
    ##################################################
    '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    background_color=ap.Color("#333"),\n    stage_width=150,\n    stage_height=150,\n    stage_elem_id="stage",\n)\ntriangle: ap.Triangle = ap.Triangle(\n    x1=75,\n    y1=50,\n    x2=50,\n    y2=100,\n    x3=100,\n    y3=100,\n    fill_color=ap.Color("#0af"),\n)\ntriangle.x2 = ap.Number(75)\n\nap.save_overall_html(dest_dir_path="triangle_x2/")\n```': '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    background_color=ap.Color("#333"),\n    stage_width=150,\n    stage_height=150,\n    stage_elem_id="stage",\n)\ntriangle: ap.Triangle = ap.Triangle(\n    x1=75,\n    y1=50,\n    x2=50,\n    y2=100,\n    x3=100,\n    y3=100,\n    fill_color=ap.Color("#0af"),\n)\ntriangle.x2 = ap.Number(75)\n\nap.save_overall_html(dest_dir_path="triangle_x2/")\n```',  # noqa
    ##################################################
    "## y2 property interface example": "## y2属性のインターフェイス例",
    ##################################################
    "The `y2` property updates or gets the instance's second vertex y-coordinate:": "`y2`属性では2つ目の頂点のY座標の更新もしくは取得を行えます:",  # noqa
    ##################################################
    '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    background_color=ap.Color("#333"),\n    stage_width=150,\n    stage_height=150,\n    stage_elem_id="stage",\n)\ntriangle: ap.Triangle = ap.Triangle(\n    x1=75,\n    y1=50,\n    x2=50,\n    y2=100,\n    x3=100,\n    y3=100,\n    fill_color=ap.Color("#0af"),\n)\ntriangle.y2 = ap.Number(75)\n\nap.save_overall_html(dest_dir_path="triangle_y2/")\n```': '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    background_color=ap.Color("#333"),\n    stage_width=150,\n    stage_height=150,\n    stage_elem_id="stage",\n)\ntriangle: ap.Triangle = ap.Triangle(\n    x1=75,\n    y1=50,\n    x2=50,\n    y2=100,\n    x3=100,\n    y3=100,\n    fill_color=ap.Color("#0af"),\n)\ntriangle.y2 = ap.Number(75)\n\nap.save_overall_html(dest_dir_path="triangle_y2/")\n```',  # noqa
    ##################################################
    "## x3 property interface example": "## x3属性のインターフェイス例",
    ##################################################
    "The `x3` property updates or gets the instance's third vertex x-coordinate:": "`x3`属性では3つ目のX座標の更新もしくは取得を行えます:",  # noqa
    ##################################################
    '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    background_color=ap.Color("#333"),\n    stage_width=150,\n    stage_height=150,\n    stage_elem_id="stage",\n)\ntriangle: ap.Triangle = ap.Triangle(\n    x1=75,\n    y1=50,\n    x2=50,\n    y2=100,\n    x3=100,\n    y3=100,\n    fill_color=ap.Color("#0af"),\n)\ntriangle.x3 = ap.Number(75)\n\nap.save_overall_html(dest_dir_path="triangle_x3/")\n```': '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    background_color=ap.Color("#333"),\n    stage_width=150,\n    stage_height=150,\n    stage_elem_id="stage",\n)\ntriangle: ap.Triangle = ap.Triangle(\n    x1=75,\n    y1=50,\n    x2=50,\n    y2=100,\n    x3=100,\n    y3=100,\n    fill_color=ap.Color("#0af"),\n)\ntriangle.x3 = ap.Number(75)\n\nap.save_overall_html(dest_dir_path="triangle_x3/")\n```',  # noqa
    ##################################################
    "## y3 property interface example": "## y3属性のインターフェイス例",
    ##################################################
    "The `y3` property updates or gets the instance's third vertex y-coordinate:": "`y3`属性では3つ目のY座標の更新もしくは取得を行えます:",  # noqa
    ##################################################
    '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    background_color=ap.Color("#333"),\n    stage_width=150,\n    stage_height=150,\n    stage_elem_id="stage",\n)\ntriangle: ap.Triangle = ap.Triangle(\n    x1=75,\n    y1=50,\n    x2=50,\n    y2=100,\n    x3=100,\n    y3=100,\n    fill_color=ap.Color("#0af"),\n)\ntriangle.y3 = ap.Number(75)\n\nap.save_overall_html(dest_dir_path="triangle_y3/")\n```': '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    background_color=ap.Color("#333"),\n    stage_width=150,\n    stage_height=150,\n    stage_elem_id="stage",\n)\ntriangle: ap.Triangle = ap.Triangle(\n    x1=75,\n    y1=50,\n    x2=50,\n    y2=100,\n    x3=100,\n    y3=100,\n    fill_color=ap.Color("#0af"),\n)\ntriangle.y3 = ap.Number(75)\n\nap.save_overall_html(dest_dir_path="triangle_y3/")\n```',  # noqa
    ##################################################
    "## fill_color property interface example": "## fill_color属性のインターフェイス例",
    ##################################################
    "The `fill_color` property updates or gets the instance's fill color:": "`fill_color`属性は塗りの色の値の更新もしくは取得を行えます:",  # noqa
    ##################################################
    '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    background_color=ap.Color("#333"),\n    stage_width=150,\n    stage_height=150,\n    stage_elem_id="stage",\n)\ntriangle: ap.Triangle = ap.Triangle(\n    x1=75,\n    y1=50,\n    x2=50,\n    y2=100,\n    x3=100,\n    y3=100,\n    fill_color=ap.Color("#0af"),\n)\ntriangle.fill_color = ap.Color("#f0a")\n\nap.save_overall_html(dest_dir_path="triangle_fill_color/")\n```': '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    background_color=ap.Color("#333"),\n    stage_width=150,\n    stage_height=150,\n    stage_elem_id="stage",\n)\ntriangle: ap.Triangle = ap.Triangle(\n    x1=75,\n    y1=50,\n    x2=50,\n    y2=100,\n    x3=100,\n    y3=100,\n    fill_color=ap.Color("#0af"),\n)\ntriangle.fill_color = ap.Color("#f0a")\n\nap.save_overall_html(dest_dir_path="triangle_fill_color/")\n```',  # noqa
    ##################################################
    "## fill_alpha property interface example": "## fill_alpha属性のインターフェイス例",
    ##################################################
    "The `fill_alpha` property updates or gets the instance's fill alpha (opacity):": "`fill_alpha`属性は塗りの透明度の値の更新もしくは取得を行えます:",  # noqa
    ##################################################
    '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    background_color=ap.Color("#333"),\n    stage_width=150,\n    stage_height=150,\n    stage_elem_id="stage",\n)\ntriangle: ap.Triangle = ap.Triangle(\n    x1=75,\n    y1=50,\n    x2=50,\n    y2=100,\n    x3=100,\n    y3=100,\n    fill_color=ap.Color("#0af"),\n)\ntriangle.fill_alpha = ap.Number(0.3)\n\nap.save_overall_html(dest_dir_path="triangle_fill_alpha/")\n```': '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    background_color=ap.Color("#333"),\n    stage_width=150,\n    stage_height=150,\n    stage_elem_id="stage",\n)\ntriangle: ap.Triangle = ap.Triangle(\n    x1=75,\n    y1=50,\n    x2=50,\n    y2=100,\n    x3=100,\n    y3=100,\n    fill_color=ap.Color("#0af"),\n)\ntriangle.fill_alpha = ap.Number(0.3)\n\nap.save_overall_html(dest_dir_path="triangle_fill_alpha/")\n```',  # noqa
    ##################################################
    "## line_color property interface example": "## line_color属性のインターフェイス例",
    ##################################################
    "The `line_color` property updates or gets the instance's line color:": "`line_color`属性では線の色の値の更新もしくは取得を行えます:",  # noqa
    ##################################################
    '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    background_color=ap.Color("#333"),\n    stage_width=150,\n    stage_height=150,\n    stage_elem_id="stage",\n)\ntriangle: ap.Triangle = ap.Triangle(\n    x1=75,\n    y1=50,\n    x2=50,\n    y2=100,\n    x3=100,\n    y3=100,\n    fill_color=ap.Color("#0af"),\n    line_thickness=3,\n)\ntriangle.line_color = ap.Color("#fff")\n\nap.save_overall_html(dest_dir_path="triangle_line_color/")\n```': '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    background_color=ap.Color("#333"),\n    stage_width=150,\n    stage_height=150,\n    stage_elem_id="stage",\n)\ntriangle: ap.Triangle = ap.Triangle(\n    x1=75,\n    y1=50,\n    x2=50,\n    y2=100,\n    x3=100,\n    y3=100,\n    fill_color=ap.Color("#0af"),\n    line_thickness=3,\n)\ntriangle.line_color = ap.Color("#fff")\n\nap.save_overall_html(dest_dir_path="triangle_line_color/")\n```',  # noqa
    ##################################################
    "## line_alpha property interface example": "## line_alpha属性のインターフェイス例",
    ##################################################
    "The `line_alpha` property updates or gets the instance's line alpha (opacity):": "`line_alpha`属性では線の透明度の値の更新もしくは取得を行えます:",  # noqa
    ##################################################
    '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    background_color=ap.Color("#333"),\n    stage_width=150,\n    stage_height=150,\n    stage_elem_id="stage",\n)\ntriangle: ap.Triangle = ap.Triangle(\n    x1=75,\n    y1=50,\n    x2=50,\n    y2=100,\n    x3=100,\n    y3=100,\n    line_color=ap.Color("#0af"),\n    line_thickness=3,\n)\ntriangle.line_alpha = ap.Number(0.3)\n\nap.save_overall_html(dest_dir_path="triangle_line_alpha/")\n```': '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    background_color=ap.Color("#333"),\n    stage_width=150,\n    stage_height=150,\n    stage_elem_id="stage",\n)\ntriangle: ap.Triangle = ap.Triangle(\n    x1=75,\n    y1=50,\n    x2=50,\n    y2=100,\n    x3=100,\n    y3=100,\n    line_color=ap.Color("#0af"),\n    line_thickness=3,\n)\ntriangle.line_alpha = ap.Number(0.3)\n\nap.save_overall_html(dest_dir_path="triangle_line_alpha/")\n```',  # noqa
    ##################################################
    "## line_thickness property interface example": "## line_thickness属性のインターフェイス例",
    ##################################################
    "The `line_thickness` property updates or gets the instance's line thickness (line width):": "`line_thickness`属性では線の幅の更新もしくは取得を行えます:",  # noqa
    ##################################################
    '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    background_color=ap.Color("#333"),\n    stage_width=150,\n    stage_height=150,\n    stage_elem_id="stage",\n)\ntriangle: ap.Triangle = ap.Triangle(\n    x1=75,\n    y1=50,\n    x2=50,\n    y2=100,\n    x3=100,\n    y3=100,\n    line_color=ap.Color("#0af"),\n    line_thickness=1,\n)\ntriangle.line_thickness = ap.Int(5)\n\nap.save_overall_html(dest_dir_path="triangle_line_thickness/")\n```': '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    background_color=ap.Color("#333"),\n    stage_width=150,\n    stage_height=150,\n    stage_elem_id="stage",\n)\ntriangle: ap.Triangle = ap.Triangle(\n    x1=75,\n    y1=50,\n    x2=50,\n    y2=100,\n    x3=100,\n    y3=100,\n    line_color=ap.Color("#0af"),\n    line_thickness=1,\n)\ntriangle.line_thickness = ap.Int(5)\n\nap.save_overall_html(dest_dir_path="triangle_line_thickness/")\n```',  # noqa
    ##################################################
    "## line_dot_setting property interface example": "## line_dot_setting属性のインターフェイス例",  # noqa
    ##################################################
    "The `line_dot_setting` property updates or gets the instance's line dot-style setting:": "`line_dot_setting`属性では点線のスタイル設定の更新もしくは取得を行えます:",  # noqa
    ##################################################
    '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    background_color=ap.Color("#333"),\n    stage_width=150,\n    stage_height=150,\n    stage_elem_id="stage",\n)\ntriangle: ap.Triangle = ap.Triangle(\n    x1=75,\n    y1=50,\n    x2=50,\n    y2=100,\n    x3=100,\n    y3=100,\n    line_color=ap.Color("#0af"),\n    line_thickness=5,\n)\ntriangle.line_dot_setting = ap.LineDotSetting(dot_size=3)\n\nap.save_overall_html(dest_dir_path="triangle_line_dot_setting/")\n```': '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    background_color=ap.Color("#333"),\n    stage_width=150,\n    stage_height=150,\n    stage_elem_id="stage",\n)\ntriangle: ap.Triangle = ap.Triangle(\n    x1=75,\n    y1=50,\n    x2=50,\n    y2=100,\n    x3=100,\n    y3=100,\n    line_color=ap.Color("#0af"),\n    line_thickness=5,\n)\ntriangle.line_dot_setting = ap.LineDotSetting(dot_size=3)\n\nap.save_overall_html(dest_dir_path="triangle_line_dot_setting/")\n```',  # noqa
    ##################################################
    "## line_dash_setting property interface example": "## line_dash_setting属性のインターフェイス例",  # noqa
    ##################################################
    "The `line_dash_setting` property updates or gets the instance's line dash-style setting:": "`line_dash_setting`属性では破線のスタイル設定の更新もしくは取得を行えます:",  # noqa
    ##################################################
    '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    background_color=ap.Color("#333"),\n    stage_width=150,\n    stage_height=150,\n    stage_elem_id="stage",\n)\ntriangle: ap.Triangle = ap.Triangle(\n    x1=75,\n    y1=50,\n    x2=50,\n    y2=100,\n    x3=100,\n    y3=100,\n    line_color=ap.Color("#0af"),\n    line_thickness=5,\n)\ntriangle.line_dash_setting = ap.LineDashSetting(dash_size=7, space_size=2)\n\nap.save_overall_html(dest_dir_path="triangle_line_dash_setting/")\n```': '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    background_color=ap.Color("#333"),\n    stage_width=150,\n    stage_height=150,\n    stage_elem_id="stage",\n)\ntriangle: ap.Triangle = ap.Triangle(\n    x1=75,\n    y1=50,\n    x2=50,\n    y2=100,\n    x3=100,\n    y3=100,\n    line_color=ap.Color("#0af"),\n    line_thickness=5,\n)\ntriangle.line_dash_setting = ap.LineDashSetting(dash_size=7, space_size=2)\n\nap.save_overall_html(dest_dir_path="triangle_line_dash_setting/")\n```',  # noqa
    ##################################################
    "## line_round_dot_setting property interface example": "## line_round_dot_setting属性のインターフェイス例",  # noqa
    ##################################################
    "The `line_round_dot_setting` property updates or gets the instance's line-round dot-style setting:": "`line_round_dot_setting`属性では丸ドット線のスタイル設定の更新もしくは取得を行えます:",  # noqa
    ##################################################
    '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    background_color=ap.Color("#333"),\n    stage_width=150,\n    stage_height=150,\n    stage_elem_id="stage",\n)\ntriangle: ap.Triangle = ap.Triangle(\n    x1=75,\n    y1=50,\n    x2=50,\n    y2=100,\n    x3=100,\n    y3=100,\n    line_color=ap.Color("#0af"),\n)\ntriangle.line_round_dot_setting = ap.LineRoundDotSetting(round_size=6, space_size=3)\n\nap.save_overall_html(dest_dir_path="triangle_line_round_dot_setting/")\n```': '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    background_color=ap.Color("#333"),\n    stage_width=150,\n    stage_height=150,\n    stage_elem_id="stage",\n)\ntriangle: ap.Triangle = ap.Triangle(\n    x1=75,\n    y1=50,\n    x2=50,\n    y2=100,\n    x3=100,\n    y3=100,\n    line_color=ap.Color("#0af"),\n)\ntriangle.line_round_dot_setting = ap.LineRoundDotSetting(round_size=6, space_size=3)\n\nap.save_overall_html(dest_dir_path="triangle_line_round_dot_setting/")\n```',  # noqa
    ##################################################
    "## line_dash_dot_setting property interface example": "## line_dash_dot_setting属性のインターフェイス例",  # noqa
    ##################################################
    "The `line_dash_dot_setting` property updates or gets the instance's dash-dotted line style setting:": "`line_dash_dot_setting`属性では一点鎖線のスタイル設定の更新もしくは取得を行えます:",  # noqa
    ##################################################
    '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    background_color=ap.Color("#333"),\n    stage_width=150,\n    stage_height=150,\n    stage_elem_id="stage",\n)\ntriangle: ap.Triangle = ap.Triangle(\n    x1=75,\n    y1=50,\n    x2=50,\n    y2=100,\n    x3=100,\n    y3=100,\n    line_color=ap.Color("#0af"),\n    line_thickness=3,\n)\ntriangle.line_dash_dot_setting = ap.LineDashDotSetting(\n    dot_size=3, dash_size=6, space_size=3\n)\n\nap.save_overall_html(dest_dir_path="triangle_line_dash_dot_setting/")\n```': '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    background_color=ap.Color("#333"),\n    stage_width=150,\n    stage_height=150,\n    stage_elem_id="stage",\n)\ntriangle: ap.Triangle = ap.Triangle(\n    x1=75,\n    y1=50,\n    x2=50,\n    y2=100,\n    x3=100,\n    y3=100,\n    line_color=ap.Color("#0af"),\n    line_thickness=3,\n)\ntriangle.line_dash_dot_setting = ap.LineDashDotSetting(\n    dot_size=3, dash_size=6, space_size=3\n)\n\nap.save_overall_html(dest_dir_path="triangle_line_dash_dot_setting/")\n```',  # noqa
    ##################################################
    "## rotation_around_center property interface example": "## rotation_around_center属性のインターフェイス例",  # noqa
    ##################################################
    "The `rotation_around_center` property updates or gets the instance's rotation value (0 to 359) from the center point:": "`rotation_around_center`属性ではインスタンスの中央座標での回転量（0～359）の更新もしくは取得を行えます:",  # noqa
    ##################################################
    '```py\n# runnable\nimport apysc as ap\n\nstage: ap.Stage = ap.Stage(\n    background_color=ap.Color("#333"),\n    stage_width=150,\n    stage_height=150,\n    stage_elem_id="stage",\n)\ntriangle: ap.Triangle = ap.Triangle(\n    x1=75,\n    y1=50,\n    x2=50,\n    y2=100,\n    x3=100,\n    y3=100,\n    fill_color=ap.Color("#0af"),\n)\n\n\ndef on_enter_frame(e: ap.EnterFrameEvent[ap.Triangle], options: dict) -> None:\n    """\n    The enter-frame event handler.\n\n    Parameters\n    ----------\n    e : ap.EnterFrameEvent[ap.Triangle]\n        Event instance.\n    options : dict\n        Optional arguments dictionary.\n    """\n    triangle.rotation_around_center += 1\n\n\nstage.enter_frame(handler=on_enter_frame)\nap.save_overall_html(dest_dir_path="triangle_rotation_around_center/")\n```': '```py\n# runnable\nimport apysc as ap\n\nstage: ap.Stage = ap.Stage(\n    background_color=ap.Color("#333"),\n    stage_width=150,\n    stage_height=150,\n    stage_elem_id="stage",\n)\ntriangle: ap.Triangle = ap.Triangle(\n    x1=75,\n    y1=50,\n    x2=50,\n    y2=100,\n    x3=100,\n    y3=100,\n    fill_color=ap.Color("#0af"),\n)\n\n\ndef on_enter_frame(e: ap.EnterFrameEvent[ap.Triangle], options: dict) -> None:\n    """\n    The enter-frame event handler.\n\n    Parameters\n    ----------\n    e : ap.EnterFrameEvent[ap.Triangle]\n        Event instance.\n    options : dict\n        Optional arguments dictionary.\n    """\n    triangle.rotation_around_center += 1\n\n\nstage.enter_frame(handler=on_enter_frame)\nap.save_overall_html(dest_dir_path="triangle_rotation_around_center/")\n```',  # noqa
    ##################################################
    "## set_rotation_around_point and get_rotation_around_point methods interface example": "## set_rotation_around_pointとget_rotation_around_pointメソッドのインターフェイス例",  # noqa
    ##################################################
    "The `set_rotation_around_point` method updates the instance's rotation value (0 to 359) from a specified point.": "`set_rotation_around_point`メソッドは指定された座標からのインスタンスの回転量（0～359）を更新します。",  # noqa
    ##################################################
    "Similarly, the `get_rotation_around_point` method gets the instance's rotation value (0 to 359) from a specified point:": "同様に、`get_rotation_around_point`メソッドでは指定された座標のインスタンスの回転量（0～359）を取得します:",  # noqa
    ##################################################
    '```py\n# runnable\nimport apysc as ap\n\nstage: ap.Stage = ap.Stage(\n    background_color=ap.Color("#333"),\n    stage_width=150,\n    stage_height=150,\n    stage_elem_id="stage",\n)\nROTATION_X: ap.Int = ap.Int(100)\nROTATION_Y: ap.Int = ap.Int(100)\ntriangle: ap.Triangle = ap.Triangle(\n    x1=75,\n    y1=50,\n    x2=50,\n    y2=100,\n    x3=ROTATION_X,\n    y3=ROTATION_Y,\n    fill_color=ap.Color("#0af"),\n)\n\n\ndef on_enter_frame(e: ap.EnterFrameEvent[ap.Triangle], options: dict) -> None:\n    """\n    The enter-frame event handler.\n\n    Parameters\n    ----------\n    e : ap.EnterFrameEvent[ap.Triangle]\n        Event instance.\n    options : dict\n        Optional arguments dictionary.\n    """\n    rotation: ap.Int = triangle.get_rotation_around_point(x=ROTATION_X, y=ROTATION_Y)\n    triangle.set_rotation_around_point(\n        rotation=rotation + 1, x=ROTATION_X, y=ROTATION_Y\n    )\n\n\nstage.enter_frame(handler=on_enter_frame)\nap.save_overall_html(dest_dir_path="triangle_set_rotation_around_point/")\n```': '```py\n# runnable\nimport apysc as ap\n\nstage: ap.Stage = ap.Stage(\n    background_color=ap.Color("#333"),\n    stage_width=150,\n    stage_height=150,\n    stage_elem_id="stage",\n)\nROTATION_X: ap.Int = ap.Int(100)\nROTATION_Y: ap.Int = ap.Int(100)\ntriangle: ap.Triangle = ap.Triangle(\n    x1=75,\n    y1=50,\n    x2=50,\n    y2=100,\n    x3=ROTATION_X,\n    y3=ROTATION_Y,\n    fill_color=ap.Color("#0af"),\n)\n\n\ndef on_enter_frame(e: ap.EnterFrameEvent[ap.Triangle], options: dict) -> None:\n    """\n    The enter-frame event handler.\n\n    Parameters\n    ----------\n    e : ap.EnterFrameEvent[ap.Triangle]\n        Event instance.\n    options : dict\n        Optional arguments dictionary.\n    """\n    rotation: ap.Int = triangle.get_rotation_around_point(x=ROTATION_X, y=ROTATION_Y)\n    triangle.set_rotation_around_point(\n        rotation=rotation + 1, x=ROTATION_X, y=ROTATION_Y\n    )\n\n\nstage.enter_frame(handler=on_enter_frame)\nap.save_overall_html(dest_dir_path="triangle_set_rotation_around_point/")\n```',  # noqa
    ##################################################
    "## scale_x_from_center property interface example": "## scale_x_from_center属性のインターフェイス例",  # noqa
    ##################################################
    "The `scale_x_from_center` property updates or gets the instance's scale-x from the center point:": "`scale_x_from_center`属性ではインスタンスの中央座標でのX軸の拡縮値の更新もしくは取得を行えます:",  # noqa
    ##################################################
    '```py\n# runnable\nimport apysc as ap\n\nstage: ap.Stage = ap.Stage(\n    background_color=ap.Color("#333"),\n    stage_width=150,\n    stage_height=150,\n    stage_elem_id="stage",\n)\ntriangle: ap.Triangle = ap.Triangle(\n    x1=75,\n    y1=50,\n    x2=50,\n    y2=100,\n    x3=100,\n    y3=100,\n    fill_color=ap.Color("#0af"),\n)\ndirection: ap.Int = ap.Int(1)\n\n\ndef on_enter_frame(e: ap.EnterFrameEvent[ap.Triangle], options: dict) -> None:\n    """\n    The enter-frame event handler.\n\n    Parameters\n    ----------\n    e : ap.EnterFrameEvent[ap.Triangle]\n        Event instance.\n    options : dict\n        Optional arguments dictionary.\n    """\n    with ap.If(triangle.scale_x_from_center <= 0.001):\n        direction.value = 1\n    with ap.If(triangle.scale_x_from_center >= 2.0):\n        direction.value = -1\n    triangle.scale_x_from_center += direction * 0.005\n\n\nstage.enter_frame(handler=on_enter_frame)\nap.save_overall_html(dest_dir_path="triangle_scale_x_from_center/")\n```': '```py\n# runnable\nimport apysc as ap\n\nstage: ap.Stage = ap.Stage(\n    background_color=ap.Color("#333"),\n    stage_width=150,\n    stage_height=150,\n    stage_elem_id="stage",\n)\ntriangle: ap.Triangle = ap.Triangle(\n    x1=75,\n    y1=50,\n    x2=50,\n    y2=100,\n    x3=100,\n    y3=100,\n    fill_color=ap.Color("#0af"),\n)\ndirection: ap.Int = ap.Int(1)\n\n\ndef on_enter_frame(e: ap.EnterFrameEvent[ap.Triangle], options: dict) -> None:\n    """\n    The enter-frame event handler.\n\n    Parameters\n    ----------\n    e : ap.EnterFrameEvent[ap.Triangle]\n        Event instance.\n    options : dict\n        Optional arguments dictionary.\n    """\n    with ap.If(triangle.scale_x_from_center <= 0.001):\n        direction.value = 1\n    with ap.If(triangle.scale_x_from_center >= 2.0):\n        direction.value = -1\n    triangle.scale_x_from_center += direction * 0.005\n\n\nstage.enter_frame(handler=on_enter_frame)\nap.save_overall_html(dest_dir_path="triangle_scale_x_from_center/")\n```',  # noqa
    ##################################################
    "## scale_y_from_center property interface example": "## scale_y_from_center属性のインターフェイス例",  # noqa
    ##################################################
    "The `scale_y_from_center` property updates or gets the instance's scale-y from the center point:": "`scale_y_from_center`属性ではインスタンスの中央座標でのX軸の拡縮値の更新もしくは取得を行えます:",  # noqa
    ##################################################
    '```py\n# runnable\nimport apysc as ap\n\nstage: ap.Stage = ap.Stage(\n    background_color=ap.Color("#333"),\n    stage_width=150,\n    stage_height=150,\n    stage_elem_id="stage",\n)\ntriangle: ap.Triangle = ap.Triangle(\n    x1=75,\n    y1=50,\n    x2=50,\n    y2=100,\n    x3=100,\n    y3=100,\n    fill_color=ap.Color("#0af"),\n)\ndirection: ap.Int = ap.Int(1)\n\n\ndef on_enter_frame(e: ap.EnterFrameEvent[ap.Triangle], options: dict) -> None:\n    """\n    The enter-frame event handler.\n\n    Parameters\n    ----------\n    e : ap.EnterFrameEvent[ap.Triangle]\n        Event instance.\n    options : dict\n        Optional arguments dictionary.\n    """\n    with ap.If(triangle.scale_y_from_center <= 0.001):\n        direction.value = 1\n    with ap.If(triangle.scale_y_from_center >= 2.0):\n        direction.value = -1\n    triangle.scale_y_from_center += direction * 0.005\n\n\nstage.enter_frame(handler=on_enter_frame)\nap.save_overall_html(dest_dir_path="triangle_scale_y_from_center/")\n```': '```py\n# runnable\nimport apysc as ap\n\nstage: ap.Stage = ap.Stage(\n    background_color=ap.Color("#333"),\n    stage_width=150,\n    stage_height=150,\n    stage_elem_id="stage",\n)\ntriangle: ap.Triangle = ap.Triangle(\n    x1=75,\n    y1=50,\n    x2=50,\n    y2=100,\n    x3=100,\n    y3=100,\n    fill_color=ap.Color("#0af"),\n)\ndirection: ap.Int = ap.Int(1)\n\n\ndef on_enter_frame(e: ap.EnterFrameEvent[ap.Triangle], options: dict) -> None:\n    """\n    The enter-frame event handler.\n\n    Parameters\n    ----------\n    e : ap.EnterFrameEvent[ap.Triangle]\n        Event instance.\n    options : dict\n        Optional arguments dictionary.\n    """\n    with ap.If(triangle.scale_y_from_center <= 0.001):\n        direction.value = 1\n    with ap.If(triangle.scale_y_from_center >= 2.0):\n        direction.value = -1\n    triangle.scale_y_from_center += direction * 0.005\n\n\nstage.enter_frame(handler=on_enter_frame)\nap.save_overall_html(dest_dir_path="triangle_scale_y_from_center/")\n```',  # noqa
    ##################################################
    "## set_scale_x_from_point and get_scale_x_from_point methods interface example": "## set_scale_x_from_pointとget_scale_x_from_pointメソッドのインターフェイス例",  # noqa
    ##################################################
    '```py\n# runnable\nimport apysc as ap\n\nstage: ap.Stage = ap.Stage(\n    background_color=ap.Color("#333"),\n    stage_width=150,\n    stage_height=150,\n    stage_elem_id="stage",\n)\nSCALE_COORDINATE_X: ap.Int = ap.Int(100)\ntriangle: ap.Triangle = ap.Triangle(\n    x1=75,\n    y1=50,\n    x2=50,\n    y2=100,\n    x3=SCALE_COORDINATE_X,\n    y3=100,\n    fill_color=ap.Color("#0af"),\n)\ndirection: ap.Int = ap.Int(1)\n\n\ndef on_enter_frame(e: ap.EnterFrameEvent[ap.Triangle], options: dict) -> None:\n    """\n    The enter-frame event handler.\n\n    Parameters\n    ----------\n    e : ap.EnterFrameEvent[ap.Triangle]\n        Event instance.\n    options : dict\n        Optional arguments dictionary.\n    """\n    scale: ap.Number = triangle.get_scale_x_from_point(x=SCALE_COORDINATE_X)\n    scale += direction * 0.005\n    with ap.If(scale <= 0.001):\n        direction.value = 1\n    with ap.If(scale >= 2.0):\n        direction.value = -1\n    triangle.set_scale_x_from_point(scale_x=scale, x=SCALE_COORDINATE_X)\n\n\nstage.enter_frame(handler=on_enter_frame)\nap.save_overall_html(dest_dir_path="triangle_set_scale_x_from_point/")\n```': '```py\n# runnable\nimport apysc as ap\n\nstage: ap.Stage = ap.Stage(\n    background_color=ap.Color("#333"),\n    stage_width=150,\n    stage_height=150,\n    stage_elem_id="stage",\n)\nSCALE_COORDINATE_X: ap.Int = ap.Int(100)\ntriangle: ap.Triangle = ap.Triangle(\n    x1=75,\n    y1=50,\n    x2=50,\n    y2=100,\n    x3=SCALE_COORDINATE_X,\n    y3=100,\n    fill_color=ap.Color("#0af"),\n)\ndirection: ap.Int = ap.Int(1)\n\n\ndef on_enter_frame(e: ap.EnterFrameEvent[ap.Triangle], options: dict) -> None:\n    """\n    The enter-frame event handler.\n\n    Parameters\n    ----------\n    e : ap.EnterFrameEvent[ap.Triangle]\n        Event instance.\n    options : dict\n        Optional arguments dictionary.\n    """\n    scale: ap.Number = triangle.get_scale_x_from_point(x=SCALE_COORDINATE_X)\n    scale += direction * 0.005\n    with ap.If(scale <= 0.001):\n        direction.value = 1\n    with ap.If(scale >= 2.0):\n        direction.value = -1\n    triangle.set_scale_x_from_point(scale_x=scale, x=SCALE_COORDINATE_X)\n\n\nstage.enter_frame(handler=on_enter_frame)\nap.save_overall_html(dest_dir_path="triangle_set_scale_x_from_point/")\n```',  # noqa
    ##################################################
    "## set_scale_y_from_point and get_scale_y_from_point methods interface example": "## set_scale_y_from_pointとget_scale_y_from_pointメソッドのインターフェイス例",  # noqa
    ##################################################
    "The `set_scale_y_from_point` method updates the instance's scale-y from a specified point.": "`set_scale_y_from_point`メソッドは指定されたY座標を基準としてY軸の拡縮値を更新します。",  # noqa
    ##################################################
    "Similarly, the `get_scale_y_from_point` method gets the instance's scale-y from a specified point:": "同様に、`get_scale_y_from_point`メソッドでは指定されたY座標を基準としたY軸の拡縮値を取得します。",  # noqa
    ##################################################
    '```py\n# runnable\nimport apysc as ap\n\nstage: ap.Stage = ap.Stage(\n    background_color=ap.Color("#333"),\n    stage_width=150,\n    stage_height=150,\n    stage_elem_id="stage",\n)\nSCALE_COORDINATE_Y: ap.Int = ap.Int(100)\ntriangle: ap.Triangle = ap.Triangle(\n    x1=75,\n    y1=50,\n    x2=50,\n    y2=100,\n    x3=100,\n    y3=SCALE_COORDINATE_Y,\n    fill_color=ap.Color("#0af"),\n)\ndirection: ap.Int = ap.Int(1)\n\n\ndef on_enter_frame(e: ap.EnterFrameEvent[ap.Triangle], options: dict) -> None:\n    """\n    The enter-frame event handler.\n\n    Parameters\n    ----------\n    e : ap.EnterFrameEvent[ap.Triangle]\n        Event instance.\n    options : dict\n        Optional arguments dictionary.\n    """\n    scale: ap.Number = triangle.get_scale_y_from_point(y=SCALE_COORDINATE_Y)\n    scale += direction * 0.005\n    with ap.If(scale <= 0.001):\n        direction.value = 1\n    with ap.If(scale >= 2.0):\n        direction.value = -1\n    triangle.set_scale_y_from_point(scale_y=scale, y=SCALE_COORDINATE_Y)\n\n\nstage.enter_frame(handler=on_enter_frame)\nap.save_overall_html(dest_dir_path="triangle_set_scale_y_from_point/")\n```': '```py\n# runnable\nimport apysc as ap\n\nstage: ap.Stage = ap.Stage(\n    background_color=ap.Color("#333"),\n    stage_width=150,\n    stage_height=150,\n    stage_elem_id="stage",\n)\nSCALE_COORDINATE_Y: ap.Int = ap.Int(100)\ntriangle: ap.Triangle = ap.Triangle(\n    x1=75,\n    y1=50,\n    x2=50,\n    y2=100,\n    x3=100,\n    y3=SCALE_COORDINATE_Y,\n    fill_color=ap.Color("#0af"),\n)\ndirection: ap.Int = ap.Int(1)\n\n\ndef on_enter_frame(e: ap.EnterFrameEvent[ap.Triangle], options: dict) -> None:\n    """\n    The enter-frame event handler.\n\n    Parameters\n    ----------\n    e : ap.EnterFrameEvent[ap.Triangle]\n        Event instance.\n    options : dict\n        Optional arguments dictionary.\n    """\n    scale: ap.Number = triangle.get_scale_y_from_point(y=SCALE_COORDINATE_Y)\n    scale += direction * 0.005\n    with ap.If(scale <= 0.001):\n        direction.value = 1\n    with ap.If(scale >= 2.0):\n        direction.value = -1\n    triangle.set_scale_y_from_point(scale_y=scale, y=SCALE_COORDINATE_Y)\n\n\nstage.enter_frame(handler=on_enter_frame)\nap.save_overall_html(dest_dir_path="triangle_set_scale_y_from_point/")\n```',  # noqa
    ##################################################
    "## flip_x property interface example": "## flip_x属性のインターフェイス例",
    ##################################################
    "The `flip_x` property updates or gets the instance's flip-x (reflecting state) boolean value:": "`flip_x`属性ではインスタンスのX軸の反転状況の真偽値の更新もしくは取得を行えます:",  # noqa
    ##################################################
    '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    background_color=ap.Color("#333"),\n    stage_width=150,\n    stage_height=150,\n    stage_elem_id="stage",\n)\ntriangle: ap.Triangle = ap.Triangle(\n    x1=50,\n    y1=50,\n    x2=50,\n    y2=100,\n    x3=100,\n    y3=100,\n    fill_color=ap.Color("#0af"),\n)\n\n\ndef on_timer(e: ap.TimerEvent, options: dict) -> None:\n    """\n    The timer event handler.\n\n    Parameters\n    ----------\n    e : ap.TimerEvent\n        Event instance.\n    options : dict\n        Optional arguments dictionary.\n    """\n    triangle.flip_x = triangle.flip_x.not_\n\n\nap.Timer(handler=on_timer, delay=1000).start()\nap.save_overall_html(dest_dir_path="triangle_flip_x/")\n```': '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    background_color=ap.Color("#333"),\n    stage_width=150,\n    stage_height=150,\n    stage_elem_id="stage",\n)\ntriangle: ap.Triangle = ap.Triangle(\n    x1=50,\n    y1=50,\n    x2=50,\n    y2=100,\n    x3=100,\n    y3=100,\n    fill_color=ap.Color("#0af"),\n)\n\n\ndef on_timer(e: ap.TimerEvent, options: dict) -> None:\n    """\n    The timer event handler.\n\n    Parameters\n    ----------\n    e : ap.TimerEvent\n        Event instance.\n    options : dict\n        Optional arguments dictionary.\n    """\n    triangle.flip_x = triangle.flip_x.not_\n\n\nap.Timer(handler=on_timer, delay=1000).start()\nap.save_overall_html(dest_dir_path="triangle_flip_x/")\n```',  # noqa
    ##################################################
    "## flip_y property interface example": "## flip_y属性のインターフェイス例",
    ##################################################
    "The `flip_y` property updates or gets the instance's flip-y (reflecting state) boolean value:": "`flip_y`属性ではインスタンスのX軸の反転状況の真偽値の更新もしくは取得を行えます:",  # noqa
    ##################################################
    '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    background_color=ap.Color("#333"),\n    stage_width=150,\n    stage_height=150,\n    stage_elem_id="stage",\n)\ntriangle: ap.Triangle = ap.Triangle(\n    x1=75,\n    y1=50,\n    x2=50,\n    y2=100,\n    x3=100,\n    y3=100,\n    fill_color=ap.Color("#0af"),\n)\n\n\ndef on_timer(e: ap.TimerEvent, options: dict) -> None:\n    """\n    The timer event handler.\n\n    Parameters\n    ----------\n    e : ap.TimerEvent\n        Event instance.\n    options : dict\n        Optional arguments dictionary.\n    """\n    triangle.flip_y = triangle.flip_y.not_\n\n\nap.Timer(handler=on_timer, delay=1000).start()\nap.save_overall_html(dest_dir_path="triangle_flip_y/")\n```': '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    background_color=ap.Color("#333"),\n    stage_width=150,\n    stage_height=150,\n    stage_elem_id="stage",\n)\ntriangle: ap.Triangle = ap.Triangle(\n    x1=75,\n    y1=50,\n    x2=50,\n    y2=100,\n    x3=100,\n    y3=100,\n    fill_color=ap.Color("#0af"),\n)\n\n\ndef on_timer(e: ap.TimerEvent, options: dict) -> None:\n    """\n    The timer event handler.\n\n    Parameters\n    ----------\n    e : ap.TimerEvent\n        Event instance.\n    options : dict\n        Optional arguments dictionary.\n    """\n    triangle.flip_y = triangle.flip_y.not_\n\n\nap.Timer(handler=on_timer, delay=1000).start()\nap.save_overall_html(dest_dir_path="triangle_flip_y/")\n```',  # noqa
    ##################################################
    "## skew_x property interface example": "## skew_x属性のインターフェイス例",
    ##################################################
    "The `skew_x` property updates or gets the instance's skew-x (distortion) value:": "`skew_x`属性ではインスタンスのX軸の歪みの値の更新もしくは取得を行えます:",  # noqa
    ##################################################
    '```py\n# runnable\nimport apysc as ap\n\nstage: ap.Stage = ap.Stage(\n    background_color=ap.Color("#333"),\n    stage_width=150,\n    stage_height=150,\n    stage_elem_id="stage",\n)\ntriangle: ap.Triangle = ap.Triangle(\n    x1=75,\n    y1=50,\n    x2=50,\n    y2=100,\n    x3=100,\n    y3=100,\n    fill_color=ap.Color("#0af"),\n)\n\n\ndef on_enter_frame(e: ap.EnterFrameEvent[ap.Triangle], options: dict) -> None:\n    """\n    The enter-frame event handler.\n\n    Parameters\n    ----------\n    e : ap.EnterFrameEvent[ap.Triangle]\n        Event instance.\n    options : dict\n        Optional arguments dictionary.\n    """\n    triangle.skew_x += 1\n\n\nstage.enter_frame(handler=on_enter_frame)\nap.save_overall_html(dest_dir_path="triangle_skew_x/")\n```': '```py\n# runnable\nimport apysc as ap\n\nstage: ap.Stage = ap.Stage(\n    background_color=ap.Color("#333"),\n    stage_width=150,\n    stage_height=150,\n    stage_elem_id="stage",\n)\ntriangle: ap.Triangle = ap.Triangle(\n    x1=75,\n    y1=50,\n    x2=50,\n    y2=100,\n    x3=100,\n    y3=100,\n    fill_color=ap.Color("#0af"),\n)\n\n\ndef on_enter_frame(e: ap.EnterFrameEvent[ap.Triangle], options: dict) -> None:\n    """\n    The enter-frame event handler.\n\n    Parameters\n    ----------\n    e : ap.EnterFrameEvent[ap.Triangle]\n        Event instance.\n    options : dict\n        Optional arguments dictionary.\n    """\n    triangle.skew_x += 1\n\n\nstage.enter_frame(handler=on_enter_frame)\nap.save_overall_html(dest_dir_path="triangle_skew_x/")\n```',  # noqa
    ##################################################
    "## skew_y property interface example": "## skew_y属性のインターフェイス例",
    ##################################################
    "The `skew_y` property updates or gets the instance's skew-y (distortion) value:": "`skew_y`属性ではインスタンスのY軸の歪みの値の更新もしくは取得を行えます:",  # noqa
    ##################################################
    '```py\n# runnable\nimport apysc as ap\n\nstage: ap.Stage = ap.Stage(\n    background_color=ap.Color("#333"),\n    stage_width=150,\n    stage_height=150,\n    stage_elem_id="stage",\n)\ntriangle: ap.Triangle = ap.Triangle(\n    x1=75,\n    y1=50,\n    x2=50,\n    y2=100,\n    x3=100,\n    y3=100,\n    fill_color=ap.Color("#0af"),\n)\n\n\ndef on_enter_frame(e: ap.EnterFrameEvent[ap.Triangle], options: dict) -> None:\n    """\n    The enter-frame event handler.\n\n    Parameters\n    ----------\n    e : ap.EnterFrameEvent[ap.Triangle]\n        Event instance.\n    options : dict\n        Optional arguments dictionary.\n    """\n    triangle.skew_y += 1\n\n\nstage.enter_frame(handler=on_enter_frame)\nap.save_overall_html(dest_dir_path="triangle_skew_y/")\n```': '```py\n# runnable\nimport apysc as ap\n\nstage: ap.Stage = ap.Stage(\n    background_color=ap.Color("#333"),\n    stage_width=150,\n    stage_height=150,\n    stage_elem_id="stage",\n)\ntriangle: ap.Triangle = ap.Triangle(\n    x1=75,\n    y1=50,\n    x2=50,\n    y2=100,\n    x3=100,\n    y3=100,\n    fill_color=ap.Color("#0af"),\n)\n\n\ndef on_enter_frame(e: ap.EnterFrameEvent[ap.Triangle], options: dict) -> None:\n    """\n    The enter-frame event handler.\n\n    Parameters\n    ----------\n    e : ap.EnterFrameEvent[ap.Triangle]\n        Event instance.\n    options : dict\n        Optional arguments dictionary.\n    """\n    triangle.skew_y += 1\n\n\nstage.enter_frame(handler=on_enter_frame)\nap.save_overall_html(dest_dir_path="triangle_skew_y/")\n```',  # noqa
    ##################################################
    "## Triangle class constructor API": "## Triangle クラスのコンストラクタのAPI",
    ##################################################
    '<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>': '<span class="inconspicuous-txt">特記事項: このAPIドキュメントはドキュメントビルド用のスクリプトによって自動で生成・同期されています。そのためもしかしたらこの節の内容は前節までの内容と重複している場合があります。</span>',  # noqa
    ##################################################
    "**[Interface summary]**": "**[インターフェイス概要]**",
    ##################################################
    "Create a triangle vector graphics instance.<hr>": "三角形のベクターグラフィックスのインスタンスを生成します。<hr>",  # noqa
    ##################################################
    "**[Parameters]**": "**[引数]**",
    ##################################################
    "- `x1`: Union[float, Number]": "- `x1`: Union[float, Number]",
    ##################################################
    "  - First vertex's x coordinate.": "  - 1つ目の頂点のX座標。",
    ##################################################
    "- `y1`: Union[float, Number]": "- `y1`: Union[float, Number]",
    ##################################################
    "  - First vertex's y coordinate.": "  - 1つ目の頂点のY座標。",
    ##################################################
    "- `x2`: Union[float, Number]": "- `x2`: Union[float, Number]",
    ##################################################
    "  - Second vertex's x coordinate.": "  - 2つ目の頂点のX座標。",
    ##################################################
    "- `y2`: Union[float, Number]": "- `y2`: Union[float, Number]",
    ##################################################
    "  - Second vertex's y coordinate.": "  - 2つ目の頂点のY座標。",
    ##################################################
    "- `x3`: Union[float, Number]": "- `x3`: Union[float, Number]",
    ##################################################
    "  - Third vertex's x coordinate.": "  - 3つ目の頂点のX座標。",
    ##################################################
    "- `y3`: Union[float, Number]": "- `y3`: Union[float, Number]",
    ##################################################
    "  - Third vertex's y coordinate.": "  - 3つ目の頂点のY座標。",
    ##################################################
    "- `fill_color`: Color, default COLORLESS": "- `fill_color`: Color, default COLORLESS",  # noqa
    ##################################################
    "  - A fill-color to set.": "  - 設定する塗りの色。",
    ##################################################
    "- `fill_alpha`: float or Number, default 1.0": "- `fill_alpha`: float or Number, default 1.0",  # noqa
    ##################################################
    "  - A fill-alpha to set.": "  - 設定する塗りの透明度。",
    ##################################################
    "- `line_color`: Color, default COLORLESS": "- `line_color`: Color, default COLORLESS",  # noqa
    ##################################################
    "  - A line-color to set.": "  - 設定する線の色。",
    ##################################################
    "- `line_alpha`: float or Number, default 1.0": "- `line_alpha`: float or Number, default 1.0",  # noqa
    ##################################################
    "  - A line-alpha to set.": "  - 設定する線の透明度。",
    ##################################################
    "- `line_thickness`: int or Int, default 1": "- `line_thickness`: int or Int, default 1",  # noqa
    ##################################################
    "  - A line-thickness (line-width) to set.": "  - 設定の線幅。",
    ##################################################
    "- `line_cap`: String or LineCaps or None, default None": "- `line_cap`: String or LineCaps or None, default None",  # noqa
    ##################################################
    "  - A line-cap setting to set.": "  - 設定する線の端のスタイル設定。",
    ##################################################
    "- `line_joints`: String or LineJoints or None, default None": "- `line_joints`: String or LineJoints or None, default None",  # noqa
    ##################################################
    "  - A line-joints setting to set.": "  - 設定する線の連結部分のスタイル設定。",
    ##################################################
    "- `line_dot_setting`: LineDotSetting or None, default None": "- `line_dot_setting`: LineDotSetting or None, default None",  # noqa
    ##################################################
    "  - A dot setting to set.": "  - 設定する点線のスタイル設定。",
    ##################################################
    "- `line_dash_setting`: LineDashSetting or None, default None": "- `line_dash_setting`: LineDashSetting or None, default None",  # noqa
    ##################################################
    "  - A dash setting to set.": "  - 設定する破線のスタイル設定。",
    ##################################################
    "- `line_round_dot_setting`: LineRoundDotSetting or None, default None": "- `line_round_dot_setting`: LineRoundDotSetting or None, default None",  # noqa
    ##################################################
    "  - A round-dot setting to set.": "  - 設定する丸ドットのスタイル設定。",
    ##################################################
    "- `line_dash_dot_setting`: LineDashDotSetting or None, default None": "- `line_dash_dot_setting`: LineDashDotSetting or None, default None",  # noqa
    ##################################################
    "  - A dash-dot (1-dot chain) setting to set.": "  - 設定する一点鎖線のスタイル設定。",
    ##################################################
    "- `parent`: ChildMixIn or None, default None": "- `parent`: ChildMixIn or None, default None",  # noqa
    ##################################################
    "  - A parent instance to add this instance. If the specified value is None, this interface uses a stage instance.": "  - このインスタンスを追加する親のインスタンス。もしもNoneが指定された場合、このインスタンスはステージのインスタンスへと追加されます。",  # noqa
    ##################################################
    '- `variable_name_suffix`: str, default ""': '- `variable_name_suffix`: str, default ""',  # noqa
    ##################################################
    "  - A JavaScript variable name suffix string. This setting is sometimes useful for JavaScript debugging.": "  - JavaScript上の変数のサフィックスの設定です。この設定はJavaScriptのデバッグ時に役立つことがあります。",  # noqa
    ##################################################
    "<hr>": "<hr>",
    ##################################################
    "**[Examples]**": "**[コードサンプル]**",
    ##################################################
    '```py\n>>> import apysc as ap\n>>> _ = ap.Stage()\n>>> triangle: ap.Triangle = ap.Triangle(\n...     x1=75,\n...     y1=50,\n...     x2=50,\n...     y2=100,\n...     x3=100,\n...     y3=100,\n...     fill_color=ap.Color("#0af"),\n...     line_color=ap.Color("#fff"),\n...     line_thickness=3,\n... )\n>>> triangle.x2\nNumber(50.0)\n\n>>> triangle.y1 = ap.Number(30.0)\n>>> triangle.y1\nNumber(30.0)\n```': '```py\n>>> import apysc as ap\n>>> _ = ap.Stage()\n>>> triangle: ap.Triangle = ap.Triangle(\n...     x1=75,\n...     y1=50,\n...     x2=50,\n...     y2=100,\n...     x3=100,\n...     y3=100,\n...     fill_color=ap.Color("#0af"),\n...     line_color=ap.Color("#fff"),\n...     line_thickness=3,\n... )\n>>> triangle.x2\nNumber(50.0)\n\n>>> triangle.y1 = ap.Number(30.0)\n>>> triangle.y1\nNumber(30.0)\n```',  # noqa
    ##################################################
    "## x1 property API": "## x1 属性のAPI",
    ##################################################
    '<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>': '<span class="inconspicuous-txt">特記事項: このAPIドキュメントはドキュメントビルド用のスクリプトによって自動で生成・同期されています。そのためもしかしたらこの節の内容は前節までの内容と重複している場合があります。</span>',  # noqa
    ##################################################
    "**[Interface summary]**": "**[インターフェイス概要]**",
    ##################################################
    "Get a first x-coordinate.<hr>": "1つ目のX座標を取得します。<hr>",
    ##################################################
    "**[Returns]**": "**[返却値]**",
    ##################################################
    "- `x1`: Number": "- `x1`: Number",
    ##################################################
    "  - A first x-coordinate.": "  - 1つ目のX座標。",
    ##################################################
    "## y1 property API": "## y1 属性のAPI",
    ##################################################
    '<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>': '<span class="inconspicuous-txt">特記事項: このAPIドキュメントはドキュメントビルド用のスクリプトによって自動で生成・同期されています。そのためもしかしたらこの節の内容は前節までの内容と重複している場合があります。</span>',  # noqa
    ##################################################
    "**[Interface summary]**": "**[インターフェイス概要]**",
    ##################################################
    "Get a first y-coordinate.<hr>": "1つ目のY座標を取得します。<hr>",
    ##################################################
    "**[Returns]**": "**[返却値]**",
    ##################################################
    "- `y1`: Number": "- `y1`: Number",
    ##################################################
    "  - A first y-coordinate.": "  - 1つ目のY座標。",
    ##################################################
    "## x2 property API": "## x2 属性のAPI",
    ##################################################
    '<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>': '<span class="inconspicuous-txt">特記事項: このAPIドキュメントはドキュメントビルド用のスクリプトによって自動で生成・同期されています。そのためもしかしたらこの節の内容は前節までの内容と重複している場合があります。</span>',  # noqa
    ##################################################
    "**[Interface summary]**": "**[インターフェイス概要]**",
    ##################################################
    "Get a second x-coordinate.<hr>": "Get a second x-coordinate.<hr>",
    ##################################################
    "**[Returns]**": "**[返却値]**",
    ##################################################
    "- `x2`: Number": "- `x2`: Number",
    ##################################################
    "  - A second x-coordinate.": "  - 2つ目のX座標。",
    ##################################################
    "## y2 property API": "## y2 属性のAPI",
    ##################################################
    '<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>': '<span class="inconspicuous-txt">特記事項: このAPIドキュメントはドキュメントビルド用のスクリプトによって自動で生成・同期されています。そのためもしかしたらこの節の内容は前節までの内容と重複している場合があります。</span>',  # noqa
    ##################################################
    "**[Interface summary]**": "**[インターフェイス概要]**",
    ##################################################
    "Get a second y-coordinate.<hr>": "2つ目のY座標を取得します。<hr>",
    ##################################################
    "**[Returns]**": "**[返却値]**",
    ##################################################
    "- `y2`: Number": "- `y2`: Number",
    ##################################################
    "  - A second y-coordinate.": "  - 2つ目のY座標。",
    ##################################################
    "## x3 property API": "## x3 属性のAPI",
    ##################################################
    '<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>': '<span class="inconspicuous-txt">特記事項: このAPIドキュメントはドキュメントビルド用のスクリプトによって自動で生成・同期されています。そのためもしかしたらこの節の内容は前節までの内容と重複している場合があります。</span>',  # noqa
    ##################################################
    "**[Interface summary]**": "**[インターフェイス概要]**",
    ##################################################
    "Get a third x-coordinate.<hr>": "3つ目のX座標を取得します。<hr>",
    ##################################################
    "**[Returns]**": "**[返却値]**",
    ##################################################
    "- `x3`: Number": "- `x3`: Number",
    ##################################################
    "  - A third x-coordinate.": "  - 3つ目のX座標。",
    ##################################################
    "## y3 property API": "## y3 属性のAPI",
    ##################################################
    '<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>': '<span class="inconspicuous-txt">特記事項: このAPIドキュメントはドキュメントビルド用のスクリプトによって自動で生成・同期されています。そのためもしかしたらこの節の内容は前節までの内容と重複している場合があります。</span>',  # noqa
    ##################################################
    "**[Interface summary]**": "**[インターフェイス概要]**",
    ##################################################
    "Get a third y-coordinate.<hr>": "3つ目のY座標を取得します。<hr>",
    ##################################################
    "**[Returns]**": "**[返却値]**",
    ##################################################
    "- `y3`: Number": "- `y3`: Number",
    ##################################################
    "  - A third y-coordinate.": "  - 3つ目のY座標。",
}
