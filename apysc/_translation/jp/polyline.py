"""This module is for the translation mapping data of the
following document:

Document file: polyline.md
Language: jp
"""

from typing import Dict

MAPPING: Dict[str, str] = {
    ##################################################
    "# Polyline class": "# Polyline クラス",
    ##################################################
    "This page explains the `Polyline` class.": "このページでは`Polyline`クラスについて説明します。",
    ##################################################
    "## What class is this?": "## クラス概要",
    ##################################################
    "The `Polyline` class creates a polyline vector graphics object.": "`Polyline`クラスは折れ線のベクターグラフィックスを生成します。",  # noqa
    ##################################################
    "## Basic usage": "## 基本的な使い方",
    ##################################################
    "The `Polyline` class constructor requires the `points` list argument.": "`Polyline`クラスはコンストラクタに`points`のリストの引数を必要とします。",  # noqa
    ##################################################
    "The constructor also accepts each style's argument, such as the `line_color`.": "コンストラクタは`line_color`などのスタイル設定の引数も受け付けます。",  # noqa
    ##################################################
    '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    background_color="#333", stage_width=200, stage_height=150, stage_elem_id="stage"\n)\npolyline: ap.Polyline = ap.Polyline(\n    points=[\n        ap.Point2D(x=50, y=50),\n        ap.Point2D(x=100, y=50),\n        ap.Point2D(x=100, y=100),\n        ap.Point2D(x=150, y=100),\n    ],\n    line_color="#0af",\n    line_thickness=3,\n)\n\nap.save_overall_html(dest_dir_path="polyline_basic_usage/")\n```': '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    background_color="#333", stage_width=200, stage_height=150, stage_elem_id="stage"\n)\npolyline: ap.Polyline = ap.Polyline(\n    points=[\n        ap.Point2D(x=50, y=50),\n        ap.Point2D(x=100, y=50),\n        ap.Point2D(x=100, y=100),\n        ap.Point2D(x=150, y=100),\n    ],\n    line_color="#0af",\n    line_thickness=3,\n)\n\nap.save_overall_html(dest_dir_path="polyline_basic_usage/")\n```',  # noqa
    ##################################################
    "## Note of the move_to and line_to interfaces": "## move_to と line_to インターフェイスの特記事項",  # noqa
    ##################################################
    "You can also create a polyline instance with the `move_to` and `line_to` interfaces.": "`move_to`と`line_to`の各インターフェイスを使う形でも折れ線のインスタンスを生成することができます。",  # noqa
    ##################################################
    "Please see also:": "関連資料:",
    ##################################################
    "- [Graphics class move_to and line_to interfaces](graphics_move_to_and_line_to.md)": "- [Graphics クラスの move_to (線の描画位置の変更)と line_to (指定座標への線の描画)のインターフェイス](jp_graphics_move_to_and_line_to.md)",  # noqa
    ##################################################
    "## x property interface example": "## x属性のインターフェイス例",
    ##################################################
    "The `x` property updates or gets the instance's x-coordinate:": "`x`属性ではX座標の値の更新もしくは取得を行えます:",  # noqa
    ##################################################
    '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    background_color="#333", stage_width=200, stage_height=150, stage_elem_id="stage"\n)\npolyline: ap.Polyline = ap.Polyline(\n    points=[\n        ap.Point2D(x=50, y=50),\n        ap.Point2D(x=100, y=50),\n        ap.Point2D(x=100, y=100),\n        ap.Point2D(x=150, y=100),\n    ],\n    line_color="#0af",\n    line_thickness=3,\n)\npolyline.x = ap.Number(100)\n\nap.save_overall_html(dest_dir_path="polyline_x/")\n```': '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    background_color="#333", stage_width=200, stage_height=150, stage_elem_id="stage"\n)\npolyline: ap.Polyline = ap.Polyline(\n    points=[\n        ap.Point2D(x=50, y=50),\n        ap.Point2D(x=100, y=50),\n        ap.Point2D(x=100, y=100),\n        ap.Point2D(x=150, y=100),\n    ],\n    line_color="#0af",\n    line_thickness=3,\n)\npolyline.x = ap.Number(100)\n\nap.save_overall_html(dest_dir_path="polyline_x/")\n```',  # noqa
    ##################################################
    "Notes: This attribute's value becomes the same as the arguments' minimum point value.": "特記事項: この属性の値は引数の座標の最小値と同値になります。",  # noqa
    ##################################################
    "## y property interface example": "## y属性のインターフェイス例",
    ##################################################
    "The `y` property updates or gets the instance's y-coordinate:": "`y`属性ではY座標の値の更新もしくは取得を行えます:",  # noqa
    ##################################################
    '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    background_color="#333", stage_width=200, stage_height=150, stage_elem_id="stage"\n)\npolyline: ap.Polyline = ap.Polyline(\n    points=[\n        ap.Point2D(x=50, y=50),\n        ap.Point2D(x=100, y=50),\n        ap.Point2D(x=100, y=100),\n        ap.Point2D(x=150, y=100),\n    ],\n    line_color="#0af",\n    line_thickness=3,\n)\npolyline.y = ap.Number(100)\n\nap.save_overall_html(dest_dir_path="polyline_y/")\n```': '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    background_color="#333", stage_width=200, stage_height=150, stage_elem_id="stage"\n)\npolyline: ap.Polyline = ap.Polyline(\n    points=[\n        ap.Point2D(x=50, y=50),\n        ap.Point2D(x=100, y=50),\n        ap.Point2D(x=100, y=100),\n        ap.Point2D(x=150, y=100),\n    ],\n    line_color="#0af",\n    line_thickness=3,\n)\npolyline.y = ap.Number(100)\n\nap.save_overall_html(dest_dir_path="polyline_y/")\n```',  # noqa
    ##################################################
    "Notes: This attribute's value becomes the same as the arguments' minimum point value.": "特記事項: この属性の値は引数の座標の最小値と同値になります。",  # noqa
    ##################################################
    "## fill_color property interface example": "## fill_color属性のインターフェイス例",
    ##################################################
    "The `fill_color` property updates or gets the instance's fill color:": "`fill_color`属性は塗りの色の値の更新もしくは取得を行えます:",  # noqa
    ##################################################
    '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    background_color="#333", stage_width=200, stage_height=150, stage_elem_id="stage"\n)\npolyline: ap.Polyline = ap.Polyline(\n    points=[\n        ap.Point2D(x=50, y=50),\n        ap.Point2D(x=100, y=50),\n        ap.Point2D(x=100, y=100),\n        ap.Point2D(x=150, y=100),\n    ],\n    line_color="#fff",\n    line_thickness=3,\n)\npolyline.fill_color = ap.String("#0af")\n\nap.save_overall_html(dest_dir_path="polyline_fill_color/")\n```': '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    background_color="#333", stage_width=200, stage_height=150, stage_elem_id="stage"\n)\npolyline: ap.Polyline = ap.Polyline(\n    points=[\n        ap.Point2D(x=50, y=50),\n        ap.Point2D(x=100, y=50),\n        ap.Point2D(x=100, y=100),\n        ap.Point2D(x=150, y=100),\n    ],\n    line_color="#fff",\n    line_thickness=3,\n)\npolyline.fill_color = ap.String("#0af")\n\nap.save_overall_html(dest_dir_path="polyline_fill_color/")\n```',  # noqa
    ##################################################
    "## fill_alpha property interface example": "## fill_alpha属性のインターフェイス例",
    ##################################################
    "The `fill_alpha` property updates or gets the instance's fill alpha (opacity):": "`fill_alpha`属性は塗りの透明度の値の更新もしくは取得を行えます:",  # noqa
    ##################################################
    '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    background_color="#333", stage_width=200, stage_height=150, stage_elem_id="stage"\n)\npolyline: ap.Polyline = ap.Polyline(\n    points=[\n        ap.Point2D(x=50, y=50),\n        ap.Point2D(x=100, y=50),\n        ap.Point2D(x=100, y=100),\n        ap.Point2D(x=150, y=100),\n    ],\n    fill_color="#0af",\n    line_color="#fff",\n    line_thickness=3,\n)\npolyline.fill_alpha = ap.Number(0.3)\n\nap.save_overall_html(dest_dir_path="polyline_fill_alpha/")\n```': '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    background_color="#333", stage_width=200, stage_height=150, stage_elem_id="stage"\n)\npolyline: ap.Polyline = ap.Polyline(\n    points=[\n        ap.Point2D(x=50, y=50),\n        ap.Point2D(x=100, y=50),\n        ap.Point2D(x=100, y=100),\n        ap.Point2D(x=150, y=100),\n    ],\n    fill_color="#0af",\n    line_color="#fff",\n    line_thickness=3,\n)\npolyline.fill_alpha = ap.Number(0.3)\n\nap.save_overall_html(dest_dir_path="polyline_fill_alpha/")\n```',  # noqa
    ##################################################
    "## line_color property interface example": "## line_color属性のインターフェイス例",
    ##################################################
    "The `line_color` property updates or gets the instance's line color:": "`line_color`属性では線の色の値の更新もしくは取得を行えます:",  # noqa
    ##################################################
    '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    background_color="#333", stage_width=200, stage_height=150, stage_elem_id="stage"\n)\npolyline: ap.Polyline = ap.Polyline(\n    points=[\n        ap.Point2D(x=50, y=50),\n        ap.Point2D(x=100, y=50),\n        ap.Point2D(x=100, y=100),\n        ap.Point2D(x=150, y=100),\n    ],\n    line_thickness=3,\n)\npolyline.line_color = ap.String("#0af")\n\nap.save_overall_html(dest_dir_path="polyline_line_color/")\n```': '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    background_color="#333", stage_width=200, stage_height=150, stage_elem_id="stage"\n)\npolyline: ap.Polyline = ap.Polyline(\n    points=[\n        ap.Point2D(x=50, y=50),\n        ap.Point2D(x=100, y=50),\n        ap.Point2D(x=100, y=100),\n        ap.Point2D(x=150, y=100),\n    ],\n    line_thickness=3,\n)\npolyline.line_color = ap.String("#0af")\n\nap.save_overall_html(dest_dir_path="polyline_line_color/")\n```',  # noqa
    ##################################################
    "## line_alpha property interface example": "## line_alpha属性のインターフェイス例",
    ##################################################
    "The `line_alpha` property updates or gets the instance's line alpha (opacity):": "`line_alpha`属性では線の透明度の値の更新もしくは取得を行えます:",  # noqa
    ##################################################
    '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    background_color="#333", stage_width=200, stage_height=150, stage_elem_id="stage"\n)\npolyline: ap.Polyline = ap.Polyline(\n    points=[\n        ap.Point2D(x=50, y=50),\n        ap.Point2D(x=100, y=50),\n        ap.Point2D(x=100, y=100),\n        ap.Point2D(x=150, y=100),\n    ],\n    line_color="#0af",\n    line_thickness=3,\n)\npolyline.line_alpha = ap.Number(0.3)\n\nap.save_overall_html(dest_dir_path="polyline_line_alpha/")\n```': '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    background_color="#333", stage_width=200, stage_height=150, stage_elem_id="stage"\n)\npolyline: ap.Polyline = ap.Polyline(\n    points=[\n        ap.Point2D(x=50, y=50),\n        ap.Point2D(x=100, y=50),\n        ap.Point2D(x=100, y=100),\n        ap.Point2D(x=150, y=100),\n    ],\n    line_color="#0af",\n    line_thickness=3,\n)\npolyline.line_alpha = ap.Number(0.3)\n\nap.save_overall_html(dest_dir_path="polyline_line_alpha/")\n```',  # noqa
    ##################################################
    "## line_thickness property interface example": "## line_thickness属性のインターフェイス例",
    ##################################################
    "The `line_thickness` property updates or gets the instance's line thickness (line width):": "`line_thickness`属性では線の幅の更新もしくは取得を行えます:",  # noqa
    ##################################################
    '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    background_color="#333", stage_width=200, stage_height=150, stage_elem_id="stage"\n)\npolyline: ap.Polyline = ap.Polyline(\n    points=[\n        ap.Point2D(x=50, y=50),\n        ap.Point2D(x=100, y=50),\n        ap.Point2D(x=100, y=100),\n        ap.Point2D(x=150, y=100),\n    ],\n    line_color="#0af",\n)\npolyline.line_thickness = ap.Int(6)\n\nap.save_overall_html(dest_dir_path="polyline_line_thickness/")\n```': '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    background_color="#333", stage_width=200, stage_height=150, stage_elem_id="stage"\n)\npolyline: ap.Polyline = ap.Polyline(\n    points=[\n        ap.Point2D(x=50, y=50),\n        ap.Point2D(x=100, y=50),\n        ap.Point2D(x=100, y=100),\n        ap.Point2D(x=150, y=100),\n    ],\n    line_color="#0af",\n)\npolyline.line_thickness = ap.Int(6)\n\nap.save_overall_html(dest_dir_path="polyline_line_thickness/")\n```',  # noqa
    ##################################################
    "## line_dot_setting property interface example": "## line_dot_setting属性のインターフェイス例",  # noqa
    ##################################################
    "The `line_dot_setting` property updates or gets the instance's line dot-style setting:": "`line_dot_setting`属性では点線のスタイル設定の更新もしくは取得を行えます:",  # noqa
    ##################################################
    '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    background_color="#333", stage_width=200, stage_height=150, stage_elem_id="stage"\n)\npolyline: ap.Polyline = ap.Polyline(\n    points=[\n        ap.Point2D(x=50, y=50),\n        ap.Point2D(x=100, y=50),\n        ap.Point2D(x=100, y=100),\n        ap.Point2D(x=150, y=100),\n    ],\n    line_color="#0af",\n    line_thickness=3,\n)\npolyline.line_dot_setting = ap.LineDotSetting(dot_size=3)\n\nap.save_overall_html(dest_dir_path="polyline_line_dot_setting/")\n```': '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    background_color="#333", stage_width=200, stage_height=150, stage_elem_id="stage"\n)\npolyline: ap.Polyline = ap.Polyline(\n    points=[\n        ap.Point2D(x=50, y=50),\n        ap.Point2D(x=100, y=50),\n        ap.Point2D(x=100, y=100),\n        ap.Point2D(x=150, y=100),\n    ],\n    line_color="#0af",\n    line_thickness=3,\n)\npolyline.line_dot_setting = ap.LineDotSetting(dot_size=3)\n\nap.save_overall_html(dest_dir_path="polyline_line_dot_setting/")\n```',  # noqa
    ##################################################
    "## line_dash_setting property interface example": "## line_dash_setting属性のインターフェイス例",  # noqa
    ##################################################
    "The `line_dash_setting` property updates or gets the instance's line dash-style setting:": "`line_dash_setting`属性では破線のスタイル設定の更新もしくは取得を行えます:",  # noqa
    ##################################################
    '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    background_color="#333", stage_width=200, stage_height=150, stage_elem_id="stage"\n)\npolyline: ap.Polyline = ap.Polyline(\n    points=[\n        ap.Point2D(x=50, y=50),\n        ap.Point2D(x=100, y=50),\n        ap.Point2D(x=100, y=100),\n        ap.Point2D(x=150, y=100),\n    ],\n    line_color="#0af",\n    line_thickness=3,\n)\npolyline.line_dash_setting = ap.LineDashSetting(dash_size=5, space_size=2)\n\nap.save_overall_html(dest_dir_path="polyline_line_dash_setting/")\n```': '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    background_color="#333", stage_width=200, stage_height=150, stage_elem_id="stage"\n)\npolyline: ap.Polyline = ap.Polyline(\n    points=[\n        ap.Point2D(x=50, y=50),\n        ap.Point2D(x=100, y=50),\n        ap.Point2D(x=100, y=100),\n        ap.Point2D(x=150, y=100),\n    ],\n    line_color="#0af",\n    line_thickness=3,\n)\npolyline.line_dash_setting = ap.LineDashSetting(dash_size=5, space_size=2)\n\nap.save_overall_html(dest_dir_path="polyline_line_dash_setting/")\n```',  # noqa
    ##################################################
    "## line_round_dot_setting property interface example": "## line_round_dot_setting属性のインターフェイス例",  # noqa
    ##################################################
    "The `line_round_dot_setting` property updates or gets the instance's line-round dot-style setting:": "`line_round_dot_setting`属性では丸ドット線のスタイル設定の更新もしくは取得を行えます:",  # noqa
    ##################################################
    '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    background_color="#333", stage_width=200, stage_height=150, stage_elem_id="stage"\n)\npolyline: ap.Polyline = ap.Polyline(\n    points=[\n        ap.Point2D(x=50, y=50),\n        ap.Point2D(x=100, y=50),\n        ap.Point2D(x=100, y=100),\n        ap.Point2D(x=150, y=100),\n    ],\n    line_color="#0af",\n)\npolyline.line_round_dot_setting = ap.LineRoundDotSetting(round_size=6, space_size=3)\n\nap.save_overall_html(dest_dir_path="polyline_line_round_dot_setting/")\n```': '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    background_color="#333", stage_width=200, stage_height=150, stage_elem_id="stage"\n)\npolyline: ap.Polyline = ap.Polyline(\n    points=[\n        ap.Point2D(x=50, y=50),\n        ap.Point2D(x=100, y=50),\n        ap.Point2D(x=100, y=100),\n        ap.Point2D(x=150, y=100),\n    ],\n    line_color="#0af",\n)\npolyline.line_round_dot_setting = ap.LineRoundDotSetting(round_size=6, space_size=3)\n\nap.save_overall_html(dest_dir_path="polyline_line_round_dot_setting/")\n```',  # noqa
    ##################################################
    "## line_dash_dot_setting property interface example": "## line_dash_dot_setting属性のインターフェイス例",  # noqa
    ##################################################
    "The `line_dash_dot_setting` property updates or gets the instance's dash-dotted line style setting:": "`line_dash_dot_setting`属性では一点鎖線のスタイル設定の更新もしくは取得を行えます:",  # noqa
    ##################################################
    '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    background_color="#333", stage_width=200, stage_height=150, stage_elem_id="stage"\n)\npolyline: ap.Polyline = ap.Polyline(\n    points=[\n        ap.Point2D(x=50, y=50),\n        ap.Point2D(x=100, y=50),\n        ap.Point2D(x=100, y=100),\n        ap.Point2D(x=150, y=100),\n    ],\n    line_color="#0af",\n    line_thickness=3,\n)\npolyline.line_dash_dot_setting = ap.LineDashDotSetting(\n    dot_size=2, dash_size=5, space_size=2\n)\n\nap.save_overall_html(dest_dir_path="polyline_line_dash_dot_setting/")\n```': '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    background_color="#333", stage_width=200, stage_height=150, stage_elem_id="stage"\n)\npolyline: ap.Polyline = ap.Polyline(\n    points=[\n        ap.Point2D(x=50, y=50),\n        ap.Point2D(x=100, y=50),\n        ap.Point2D(x=100, y=100),\n        ap.Point2D(x=150, y=100),\n    ],\n    line_color="#0af",\n    line_thickness=3,\n)\npolyline.line_dash_dot_setting = ap.LineDashDotSetting(\n    dot_size=2, dash_size=5, space_size=2\n)\n\nap.save_overall_html(dest_dir_path="polyline_line_dash_dot_setting/")\n```',  # noqa
    ##################################################
    "## rotation_around_center property interface example": "## rotation_around_center属性のインターフェイス例",  # noqa
    ##################################################
    "The `rotation_around_center` property updates or gets the instance's rotation value (0 to 359) from the center point:": "`rotation_around_center`属性ではインスタンスの中央座標での回転量（0～359）の更新もしくは取得を行えます:",  # noqa
    ##################################################
    '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    background_color="#333", stage_width=200, stage_height=150, stage_elem_id="stage"\n)\npolyline: ap.Polyline = ap.Polyline(\n    points=[\n        ap.Point2D(x=50, y=50),\n        ap.Point2D(x=100, y=50),\n        ap.Point2D(x=100, y=100),\n        ap.Point2D(x=150, y=100),\n    ],\n    line_color="#0af",\n    line_thickness=3,\n)\n\n\ndef on_timer(e: ap.TimerEvent, options: dict) -> None:\n    """\n    The timer event handler.\n\n    Parameters\n    ----------\n    e : ap.TimerEvent\n        Event instance.\n    options : dict\n        Optional arguments dictionary.\n    """\n    polyline.rotation_around_center += 1\n\n\nap.Timer(on_timer, delay=ap.FPS.FPS_60).start()\nap.save_overall_html(dest_dir_path="polyline_rotation_around_center/")\n```': '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    background_color="#333", stage_width=200, stage_height=150, stage_elem_id="stage"\n)\npolyline: ap.Polyline = ap.Polyline(\n    points=[\n        ap.Point2D(x=50, y=50),\n        ap.Point2D(x=100, y=50),\n        ap.Point2D(x=100, y=100),\n        ap.Point2D(x=150, y=100),\n    ],\n    line_color="#0af",\n    line_thickness=3,\n)\n\n\ndef on_timer(e: ap.TimerEvent, options: dict) -> None:\n    """\n    The timer event handler.\n\n    Parameters\n    ----------\n    e : ap.TimerEvent\n        Event instance.\n    options : dict\n        Optional arguments dictionary.\n    """\n    polyline.rotation_around_center += 1\n\n\nap.Timer(on_timer, delay=ap.FPS.FPS_60).start()\nap.save_overall_html(dest_dir_path="polyline_rotation_around_center/")\n```',  # noqa
    ##################################################
    "## set_rotation_around_point and get_rotation_around_point methods interfaces example": "## set_rotation_around_pointとget_rotation_around_pointメソッドのインターフェイス例",  # noqa
    ##################################################
    "The `set_rotation_around_point` method updates the instance's rotation value (0 to 359) from a specified point.": "`set_rotation_around_point`メソッドは指定された座標からのインスタンスの回転量（0～359）を更新します。",  # noqa
    ##################################################
    "Similarly, the `get_rotation_around_point` method gets the instance's rotation value (0 to 359) from a specified point:": "同様に、`get_rotation_around_point`メソッドでは指定された座標のインスタンスの回転量（0～359）を取得します:",  # noqa
    ##################################################
    '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    background_color="#333", stage_width=200, stage_height=150, stage_elem_id="stage"\n)\npolyline: ap.Polyline = ap.Polyline(\n    points=[\n        ap.Point2D(x=50, y=50),\n        ap.Point2D(x=100, y=50),\n        ap.Point2D(x=100, y=100),\n        ap.Point2D(x=150, y=100),\n    ],\n    line_color="#0af",\n    line_thickness=3,\n)\nx: ap.Int = ap.Int(150)\ny: ap.Int = ap.Int(100)\n\n\ndef on_timer(e: ap.TimerEvent, options: dict) -> None:\n    """\n    The timer event handler.\n\n    Parameters\n    ----------\n    e : ap.TimerEvent\n        Event instance.\n    options : dict\n        Optional arguments dictionary.\n    """\n    rotation: ap.Int = polyline.get_rotation_around_point(x=x, y=y)\n    rotation += 1\n    polyline.set_rotation_around_point(rotation=rotation, x=x, y=y)\n\n\nap.Timer(on_timer, delay=ap.FPS.FPS_60).start()\nap.save_overall_html(dest_dir_path="polyline_set_rotation_around_point/")\n```': '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    background_color="#333", stage_width=200, stage_height=150, stage_elem_id="stage"\n)\npolyline: ap.Polyline = ap.Polyline(\n    points=[\n        ap.Point2D(x=50, y=50),\n        ap.Point2D(x=100, y=50),\n        ap.Point2D(x=100, y=100),\n        ap.Point2D(x=150, y=100),\n    ],\n    line_color="#0af",\n    line_thickness=3,\n)\nx: ap.Int = ap.Int(150)\ny: ap.Int = ap.Int(100)\n\n\ndef on_timer(e: ap.TimerEvent, options: dict) -> None:\n    """\n    The timer event handler.\n\n    Parameters\n    ----------\n    e : ap.TimerEvent\n        Event instance.\n    options : dict\n        Optional arguments dictionary.\n    """\n    rotation: ap.Int = polyline.get_rotation_around_point(x=x, y=y)\n    rotation += 1\n    polyline.set_rotation_around_point(rotation=rotation, x=x, y=y)\n\n\nap.Timer(on_timer, delay=ap.FPS.FPS_60).start()\nap.save_overall_html(dest_dir_path="polyline_set_rotation_around_point/")\n```',  # noqa
    ##################################################
    "## scale_x_from_center property interface example": "## scale_x_from_center属性のインターフェイス例",  # noqa
    ##################################################
    "The `scale_x_from_center` property updates or gets the instance's scale-x from the center point:": "`scale_x_from_center`属性ではインスタンスの中央座標でのX軸の拡縮値の更新もしくは取得を行えます:",  # noqa
    ##################################################
    '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    background_color="#333", stage_width=200, stage_height=150, stage_elem_id="stage"\n)\npolyline: ap.Polyline = ap.Polyline(\n    points=[\n        ap.Point2D(x=50, y=50),\n        ap.Point2D(x=100, y=50),\n        ap.Point2D(x=100, y=100),\n        ap.Point2D(x=150, y=100),\n    ],\n    line_color="#0af",\n    line_thickness=3,\n)\ndirection: ap.Int = ap.Int(-1)\n\n\ndef on_timer(e: ap.TimerEvent, options: dict) -> None:\n    """\n    The timer event handler.\n\n    Parameters\n    ----------\n    e : ap.TimerEvent\n        Event instance.\n    options : dict\n        Optional arguments dictionary.\n    """\n    with ap.If(polyline.scale_x_from_center <= 0.001):\n        direction.value = 1\n    with ap.If(polyline.scale_x_from_center >= 2.0):\n        direction.value = -1\n    polyline.scale_x_from_center += direction * 0.005\n\n\nap.Timer(on_timer, delay=ap.FPS.FPS_60).start()\nap.save_overall_html(dest_dir_path="polyline_scale_x_from_center/")\n```': '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    background_color="#333", stage_width=200, stage_height=150, stage_elem_id="stage"\n)\npolyline: ap.Polyline = ap.Polyline(\n    points=[\n        ap.Point2D(x=50, y=50),\n        ap.Point2D(x=100, y=50),\n        ap.Point2D(x=100, y=100),\n        ap.Point2D(x=150, y=100),\n    ],\n    line_color="#0af",\n    line_thickness=3,\n)\ndirection: ap.Int = ap.Int(-1)\n\n\ndef on_timer(e: ap.TimerEvent, options: dict) -> None:\n    """\n    The timer event handler.\n\n    Parameters\n    ----------\n    e : ap.TimerEvent\n        Event instance.\n    options : dict\n        Optional arguments dictionary.\n    """\n    with ap.If(polyline.scale_x_from_center <= 0.001):\n        direction.value = 1\n    with ap.If(polyline.scale_x_from_center >= 2.0):\n        direction.value = -1\n    polyline.scale_x_from_center += direction * 0.005\n\n\nap.Timer(on_timer, delay=ap.FPS.FPS_60).start()\nap.save_overall_html(dest_dir_path="polyline_scale_x_from_center/")\n```',  # noqa
    ##################################################
    "## scale_y_from_center property interface example": "## scale_y_from_center属性のインターフェイス例",  # noqa
    ##################################################
    "The `scale_y_from_center` property updates or gets the instance's scale-y from the center point:": "`scale_y_from_center`属性ではインスタンスの中央座標でのX軸の拡縮値の更新もしくは取得を行えます:",  # noqa
    ##################################################
    '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    background_color="#333", stage_width=200, stage_height=150, stage_elem_id="stage"\n)\npolyline: ap.Polyline = ap.Polyline(\n    points=[\n        ap.Point2D(x=50, y=50),\n        ap.Point2D(x=100, y=50),\n        ap.Point2D(x=100, y=100),\n        ap.Point2D(x=150, y=100),\n    ],\n    line_color="#0af",\n    line_thickness=3,\n)\ndirection: ap.Int = ap.Int(-1)\n\n\ndef on_timer(e: ap.TimerEvent, options: dict) -> None:\n    """\n    The timer event handler.\n\n    Parameters\n    ----------\n    e : ap.TimerEvent\n        Event instance.\n    options : dict\n        Optional arguments dictionary.\n    """\n    with ap.If(polyline.scale_y_from_center <= 0.001):\n        direction.value = 1\n    with ap.If(polyline.scale_y_from_center >= 2.0):\n        direction.value = -1\n    polyline.scale_y_from_center += direction * 0.005\n\n\nap.Timer(on_timer, delay=ap.FPS.FPS_60).start()\nap.save_overall_html(dest_dir_path="polyline_scale_y_from_center/")\n```': '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    background_color="#333", stage_width=200, stage_height=150, stage_elem_id="stage"\n)\npolyline: ap.Polyline = ap.Polyline(\n    points=[\n        ap.Point2D(x=50, y=50),\n        ap.Point2D(x=100, y=50),\n        ap.Point2D(x=100, y=100),\n        ap.Point2D(x=150, y=100),\n    ],\n    line_color="#0af",\n    line_thickness=3,\n)\ndirection: ap.Int = ap.Int(-1)\n\n\ndef on_timer(e: ap.TimerEvent, options: dict) -> None:\n    """\n    The timer event handler.\n\n    Parameters\n    ----------\n    e : ap.TimerEvent\n        Event instance.\n    options : dict\n        Optional arguments dictionary.\n    """\n    with ap.If(polyline.scale_y_from_center <= 0.001):\n        direction.value = 1\n    with ap.If(polyline.scale_y_from_center >= 2.0):\n        direction.value = -1\n    polyline.scale_y_from_center += direction * 0.005\n\n\nap.Timer(on_timer, delay=ap.FPS.FPS_60).start()\nap.save_overall_html(dest_dir_path="polyline_scale_y_from_center/")\n```',  # noqa
    ##################################################
    "## set_scale_x_from_point and get_scale_x_from_point methods interfaces example": "## set_scale_x_from_pointとget_scale_x_from_pointメソッドのインターフェイス例",  # noqa
    ##################################################
    "The `set_scale_x_from_point` method updates the instance's scale-x from a specified point.": "`set_scale_x_from_point`メソッドは指定されたX座標を基準としてX軸の拡縮値を更新します。",  # noqa
    ##################################################
    "Similarly, the `get_scale_x_from_point` method gets the instance's scale-x from a specified point:": "同様に、`get_scale_x_from_point`メソッドでは指定されたX座標を基準としたX軸の拡縮値を取得します:",  # noqa
    ##################################################
    '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    background_color="#333", stage_width=200, stage_height=150, stage_elem_id="stage"\n)\npolyline: ap.Polyline = ap.Polyline(\n    points=[\n        ap.Point2D(x=50, y=50),\n        ap.Point2D(x=100, y=50),\n        ap.Point2D(x=100, y=100),\n        ap.Point2D(x=150, y=100),\n    ],\n    line_color="#0af",\n    line_thickness=3,\n)\ndirection: ap.Int = ap.Int(-1)\nx: ap.Int = ap.Int(150)\n\n\ndef on_timer(e: ap.TimerEvent, options: dict) -> None:\n    """\n    The timer event handler.\n\n    Parameters\n    ----------\n    e : ap.TimerEvent\n        Event instance.\n    options : dict\n        Optional arguments dictionary.\n    """\n    scale: ap.Number = polyline.get_scale_x_from_point(x=x)\n    with ap.If(scale <= 0.001):\n        direction.value = 1\n    with ap.If(scale >= 2.0):\n        direction.value = -1\n    scale += direction * 0.005\n    polyline.set_scale_x_from_point(scale_x=scale, x=x)\n\n\nap.Timer(on_timer, delay=ap.FPS.FPS_60).start()\nap.save_overall_html(dest_dir_path="polyline_scale_x_from_point/")\n```': '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    background_color="#333", stage_width=200, stage_height=150, stage_elem_id="stage"\n)\npolyline: ap.Polyline = ap.Polyline(\n    points=[\n        ap.Point2D(x=50, y=50),\n        ap.Point2D(x=100, y=50),\n        ap.Point2D(x=100, y=100),\n        ap.Point2D(x=150, y=100),\n    ],\n    line_color="#0af",\n    line_thickness=3,\n)\ndirection: ap.Int = ap.Int(-1)\nx: ap.Int = ap.Int(150)\n\n\ndef on_timer(e: ap.TimerEvent, options: dict) -> None:\n    """\n    The timer event handler.\n\n    Parameters\n    ----------\n    e : ap.TimerEvent\n        Event instance.\n    options : dict\n        Optional arguments dictionary.\n    """\n    scale: ap.Number = polyline.get_scale_x_from_point(x=x)\n    with ap.If(scale <= 0.001):\n        direction.value = 1\n    with ap.If(scale >= 2.0):\n        direction.value = -1\n    scale += direction * 0.005\n    polyline.set_scale_x_from_point(scale_x=scale, x=x)\n\n\nap.Timer(on_timer, delay=ap.FPS.FPS_60).start()\nap.save_overall_html(dest_dir_path="polyline_scale_x_from_point/")\n```',  # noqa
    ##################################################
    "## set_scale_y_from_point and get_scale_y_from_point methods interfaces example": "## set_scale_y_from_pointとget_scale_y_from_pointメソッドのインターフェイス例",  # noqa
    ##################################################
    "The `set_scale_y_from_point` method updates the instance's scale-y from a specified point.": "`set_scale_y_from_point`メソッドは指定されたY座標を基準としてY軸の拡縮値を更新します。",  # noqa
    ##################################################
    "Similarly, the `get_scale_y_from_point` method gets the instance's scale-y from a specified point:": "同様に、`get_scale_y_from_point`メソッドでは指定されたY座標を基準としたY軸の拡縮値を取得します。",  # noqa
    ##################################################
    '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    background_color="#333", stage_width=200, stage_height=150, stage_elem_id="stage"\n)\npolyline: ap.Polyline = ap.Polyline(\n    points=[\n        ap.Point2D(x=50, y=50),\n        ap.Point2D(x=100, y=50),\n        ap.Point2D(x=100, y=100),\n        ap.Point2D(x=150, y=100),\n    ],\n    line_color="#0af",\n    line_thickness=3,\n)\ndirection: ap.Int = ap.Int(-1)\ny: ap.Int = ap.Int(100)\n\n\ndef on_timer(e: ap.TimerEvent, options: dict) -> None:\n    """\n    The timer event handler.\n\n    Parameters\n    ----------\n    e : ap.TimerEvent\n        Event instance.\n    options : dict\n        Optional arguments dictionary.\n    """\n    scale: ap.Number = polyline.get_scale_y_from_point(y=y)\n    with ap.If(scale <= 0.001):\n        direction.value = 1\n    with ap.If(scale >= 2.0):\n        direction.value = -1\n    scale += direction * 0.005\n    polyline.set_scale_y_from_point(scale_y=scale, y=y)\n\n\nap.Timer(on_timer, delay=ap.FPS.FPS_60).start()\nap.save_overall_html(dest_dir_path="polyline_scale_y_from_point/")\n```': '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    background_color="#333", stage_width=200, stage_height=150, stage_elem_id="stage"\n)\npolyline: ap.Polyline = ap.Polyline(\n    points=[\n        ap.Point2D(x=50, y=50),\n        ap.Point2D(x=100, y=50),\n        ap.Point2D(x=100, y=100),\n        ap.Point2D(x=150, y=100),\n    ],\n    line_color="#0af",\n    line_thickness=3,\n)\ndirection: ap.Int = ap.Int(-1)\ny: ap.Int = ap.Int(100)\n\n\ndef on_timer(e: ap.TimerEvent, options: dict) -> None:\n    """\n    The timer event handler.\n\n    Parameters\n    ----------\n    e : ap.TimerEvent\n        Event instance.\n    options : dict\n        Optional arguments dictionary.\n    """\n    scale: ap.Number = polyline.get_scale_y_from_point(y=y)\n    with ap.If(scale <= 0.001):\n        direction.value = 1\n    with ap.If(scale >= 2.0):\n        direction.value = -1\n    scale += direction * 0.005\n    polyline.set_scale_y_from_point(scale_y=scale, y=y)\n\n\nap.Timer(on_timer, delay=ap.FPS.FPS_60).start()\nap.save_overall_html(dest_dir_path="polyline_scale_y_from_point/")\n```',  # noqa
    ##################################################
    "## flip_x property interface example": "## flip_x属性のインターフェイス例",
    ##################################################
    "The `flip_x` property updates or gets the instance's flip-x (reflecting state) boolean value:": "`flip_x`属性ではインスタンスのX軸の反転状況の真偽値の更新もしくは取得を行えます:",  # noqa
    ##################################################
    '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    background_color="#333", stage_width=150, stage_height=150, stage_elem_id="stage"\n)\npolyline: ap.Polyline = ap.Polyline(\n    points=[\n        ap.Point2D(x=50, y=50),\n        ap.Point2D(x=100, y=50),\n        ap.Point2D(x=50, y=100),\n    ],\n    line_color="#0af",\n    line_thickness=3,\n)\n\n\ndef on_timer(e: ap.TimerEvent, options: dict) -> None:\n    """\n    The timer event handler.\n\n    Parameters\n    ----------\n    e : ap.TimerEvent\n        Event instance.\n    options : dict\n        Optional arguments dictionary.\n    """\n    polyline.flip_x = polyline.flip_x.not_\n\n\nap.Timer(on_timer, delay=1000).start()\nap.save_overall_html(dest_dir_path="polyline_flip_x/")\n```': '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    background_color="#333", stage_width=150, stage_height=150, stage_elem_id="stage"\n)\npolyline: ap.Polyline = ap.Polyline(\n    points=[\n        ap.Point2D(x=50, y=50),\n        ap.Point2D(x=100, y=50),\n        ap.Point2D(x=50, y=100),\n    ],\n    line_color="#0af",\n    line_thickness=3,\n)\n\n\ndef on_timer(e: ap.TimerEvent, options: dict) -> None:\n    """\n    The timer event handler.\n\n    Parameters\n    ----------\n    e : ap.TimerEvent\n        Event instance.\n    options : dict\n        Optional arguments dictionary.\n    """\n    polyline.flip_x = polyline.flip_x.not_\n\n\nap.Timer(on_timer, delay=1000).start()\nap.save_overall_html(dest_dir_path="polyline_flip_x/")\n```',  # noqa
    ##################################################
    "## flip_y property interface example": "## flip_y属性のインターフェイス例",
    ##################################################
    "The `flip_y` property updates or gets the instance's flip-y (reflecting state) boolean value:": "`flip_y`属性ではインスタンスのX軸の反転状況の真偽値の更新もしくは取得を行えます:",  # noqa
    ##################################################
    '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    background_color="#333", stage_width=150, stage_height=150, stage_elem_id="stage"\n)\npolyline: ap.Polyline = ap.Polyline(\n    points=[\n        ap.Point2D(x=50, y=50),\n        ap.Point2D(x=100, y=50),\n        ap.Point2D(x=50, y=100),\n    ],\n    line_color="#0af",\n    line_thickness=3,\n)\n\n\ndef on_timer(e: ap.TimerEvent, options: dict) -> None:\n    """\n    The timer event handler.\n\n    Parameters\n    ----------\n    e : ap.TimerEvent\n        Event instance.\n    options : dict\n        Optional arguments dictionary.\n    """\n    polyline.flip_y = polyline.flip_y.not_\n\n\nap.Timer(on_timer, delay=1000).start()\nap.save_overall_html(dest_dir_path="polyline_flip_y/")\n```': '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    background_color="#333", stage_width=150, stage_height=150, stage_elem_id="stage"\n)\npolyline: ap.Polyline = ap.Polyline(\n    points=[\n        ap.Point2D(x=50, y=50),\n        ap.Point2D(x=100, y=50),\n        ap.Point2D(x=50, y=100),\n    ],\n    line_color="#0af",\n    line_thickness=3,\n)\n\n\ndef on_timer(e: ap.TimerEvent, options: dict) -> None:\n    """\n    The timer event handler.\n\n    Parameters\n    ----------\n    e : ap.TimerEvent\n        Event instance.\n    options : dict\n        Optional arguments dictionary.\n    """\n    polyline.flip_y = polyline.flip_y.not_\n\n\nap.Timer(on_timer, delay=1000).start()\nap.save_overall_html(dest_dir_path="polyline_flip_y/")\n```',  # noqa
    ##################################################
    "## skew_x property interface example": "## skew_x属性のインターフェイス例",
    ##################################################
    "The `skew_x` property updates or gets the instance's skew-x (distortion) value:": "`skew_x`属性ではインスタンスのX軸の歪みの値の更新もしくは取得を行えます:",  # noqa
    ##################################################
    '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    background_color="#333", stage_width=150, stage_height=150, stage_elem_id="stage"\n)\npolyline: ap.Polyline = ap.Polyline(\n    points=[\n        ap.Point2D(x=50, y=50),\n        ap.Point2D(x=100, y=50),\n        ap.Point2D(x=50, y=100),\n    ],\n    line_color="#0af",\n    line_thickness=3,\n)\n\n\ndef on_timer(e: ap.TimerEvent, options: dict) -> None:\n    """\n    The timer event handler.\n\n    Parameters\n    ----------\n    e : ap.TimerEvent\n        Event instance.\n    options : dict\n        Optional arguments dictionary.\n    """\n    polyline.skew_x += 1\n\n\nap.Timer(on_timer, delay=ap.FPS.FPS_60).start()\nap.save_overall_html(dest_dir_path="polyline_skew_x/")\n```': '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    background_color="#333", stage_width=150, stage_height=150, stage_elem_id="stage"\n)\npolyline: ap.Polyline = ap.Polyline(\n    points=[\n        ap.Point2D(x=50, y=50),\n        ap.Point2D(x=100, y=50),\n        ap.Point2D(x=50, y=100),\n    ],\n    line_color="#0af",\n    line_thickness=3,\n)\n\n\ndef on_timer(e: ap.TimerEvent, options: dict) -> None:\n    """\n    The timer event handler.\n\n    Parameters\n    ----------\n    e : ap.TimerEvent\n        Event instance.\n    options : dict\n        Optional arguments dictionary.\n    """\n    polyline.skew_x += 1\n\n\nap.Timer(on_timer, delay=ap.FPS.FPS_60).start()\nap.save_overall_html(dest_dir_path="polyline_skew_x/")\n```',  # noqa
    ##################################################
    "## skew_y property interface example": "## skew_y属性のインターフェイス例",
    ##################################################
    "The `skew_y` property updates or gets the instance's skew-y (distortion) value:": "`skew_y`属性ではインスタンスのY軸の歪みの値の更新もしくは取得を行えます:",  # noqa
    ##################################################
    '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    background_color="#333", stage_width=150, stage_height=150, stage_elem_id="stage"\n)\npolyline: ap.Polyline = ap.Polyline(\n    points=[\n        ap.Point2D(x=50, y=50),\n        ap.Point2D(x=100, y=50),\n        ap.Point2D(x=50, y=100),\n    ],\n    line_color="#0af",\n    line_thickness=3,\n)\n\n\ndef on_timer(e: ap.TimerEvent, options: dict) -> None:\n    """\n    The timer event handler.\n\n    Parameters\n    ----------\n    e : ap.TimerEvent\n        Event instance.\n    options : dict\n        Optional arguments dictionary.\n    """\n    polyline.skew_y += 1\n\n\nap.Timer(on_timer, delay=ap.FPS.FPS_60).start()\nap.save_overall_html(dest_dir_path="polyline_skew_y/")\n```': '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    background_color="#333", stage_width=150, stage_height=150, stage_elem_id="stage"\n)\npolyline: ap.Polyline = ap.Polyline(\n    points=[\n        ap.Point2D(x=50, y=50),\n        ap.Point2D(x=100, y=50),\n        ap.Point2D(x=50, y=100),\n    ],\n    line_color="#0af",\n    line_thickness=3,\n)\n\n\ndef on_timer(e: ap.TimerEvent, options: dict) -> None:\n    """\n    The timer event handler.\n\n    Parameters\n    ----------\n    e : ap.TimerEvent\n        Event instance.\n    options : dict\n        Optional arguments dictionary.\n    """\n    polyline.skew_y += 1\n\n\nap.Timer(on_timer, delay=ap.FPS.FPS_60).start()\nap.save_overall_html(dest_dir_path="polyline_skew_y/")\n```',  # noqa
    ##################################################
    "## Polyline class constructor API": "## Polyline クラスのコンストラクタのAPI",
    ##################################################
    '<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>': '<span class="inconspicuous-txt">特記事項: このAPIドキュメントはドキュメントビルド用のスクリプトによって自動で生成・同期されています。そのためもしかしたらこの節の内容は前節までの内容と重複している場合があります。</span>',  # noqa
    ##################################################
    "**[Interface summary]**": "**[インターフェイス概要]**",
    ##################################################
    "Create a polyline vector graphic.<hr>": "折れ線のベクターグラフィックスを生成します。<hr>",
    ##################################################
    "**[Parameters]**": "**[引数]**",
    ##################################################
    "- `points`: Array of Point2D or list of Point2D": "- `points`: Array of Point2D or list of Point2D",  # noqa
    ##################################################
    "  - List of line points.": "  - 線の座標のリスト。",
    ##################################################
    "- `fill_color`: str or String, default ''": "- `fill_color`: str or String, default ''",  # noqa
    ##################################################
    "  - A fill-color to set.": "  - 設定する塗りの色。",
    ##################################################
    "- `fill_alpha`: float or Number, default 1.0": "- `fill_alpha`: float or Number, default 1.0",  # noqa
    ##################################################
    "  - A fill-alpha to set.": "  - 設定する塗りの透明度。",
    ##################################################
    "- `line_color`: str or String, default ''": "- `line_color`: str or String, default ''",  # noqa
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
    "  - A parent instance to add this instance. If a specified value is None, this interface uses a stage instance.": "  - このインスタンスを追加する親のインスタンス。もしもNoneが指定された場合、このインスタンスはステージのインスタンスへと追加されます。",  # noqa
    ##################################################
    "- `variable_name_suffix`: str, default ''": "- `variable_name_suffix`: str, default ''",  # noqa
    ##################################################
    "  - A JavaScript variable name suffix string. This setting is sometimes useful for JavaScript debugging.": "  - JavaScript上の変数のサフィックスの設定です。この設定はJavaScriptのデバッグ時に役立つことがあります。",  # noqa
    ##################################################
    "<hr>": "<hr>",
    ##################################################
    "**[Examples]**": "**[コードサンプル]**",
    ##################################################
    "```py\n>>> import apysc as ap\n>>> stage: ap.Stage = ap.Stage()\n>>> polyline: ap.Polyline = ap.Polyline(\n...     points=[\n...         ap.Point2D(x=50, y=50),\n...         ap.Point2D(x=100, y=100),\n...         ap.Point2D(x=150, y=50),\n...     ],\n...     line_color=\"#ffffff\",\n...     line_thickness=3,\n... )\n>>> polyline.line_color\nString('#ffffff')\n\n>>> polyline.line_thickness\nInt(3)\n```": "```py\n>>> import apysc as ap\n>>> stage: ap.Stage = ap.Stage()\n>>> polyline: ap.Polyline = ap.Polyline(\n...     points=[\n...         ap.Point2D(x=50, y=50),\n...         ap.Point2D(x=100, y=100),\n...         ap.Point2D(x=150, y=50),\n...     ],\n...     line_color=\"#ffffff\",\n...     line_thickness=3,\n... )\n>>> polyline.line_color\nString('#ffffff')\n\n>>> polyline.line_thickness\nInt(3)\n```",  # noqa
}
