"""This module is for the translation mapping data of the
following document:

Document file: circle.md
Language: jp
"""

from typing import Dict

MAPPING: Dict[str, str] = {
    ##################################################
    "# Circle class": "# Circle クラス",
    ##################################################
    "This page explains the `Circle` class.": "このページでは`Circle`クラスについて説明します。",
    ##################################################
    "## What class is this?": "## クラス概要",
    ##################################################
    "The `Circle` class creates a circle vector graphics object.": "`Circle`クラスは円のベクターグラフィックスを生成します。",  # noqa
    ##################################################
    "## Basic usage": "## 基本的な使い方",
    ##################################################
    "The `Circle` class constructor requires the `x` (center x), `y` (center y), and `radius` arguments.": "`Circle`クラスのコンストラクタでは`x`（円の中央のX座標）、`y`（円の中央のY座標）、そして半径としての`radius`引数が必要となります。",  # noqa
    ##################################################
    "The constructor also accepts each style's argument, such as the `fill_color`.": "コンストラクタでは他の`fill_color`などのスタイル設定の各引数も受け付けます。",  # noqa
    ##################################################
    '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    background_color=ap.Color("#333"),\n    stage_width=150,\n    stage_height=150,\n    stage_elem_id="stage",\n)\ncircle: ap.Circle = ap.Circle(\n    x=75,\n    y=75,\n    radius=50,\n    fill_color=ap.Color("#0af"),\n)\n\nap.save_overall_html(dest_dir_path="circle_basic_usage/")\n```': '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    background_color=ap.Color("#333"),\n    stage_width=150,\n    stage_height=150,\n    stage_elem_id="stage",\n)\ncircle: ap.Circle = ap.Circle(\n    x=75,\n    y=75,\n    radius=50,\n    fill_color=ap.Color("#0af"),\n)\n\nap.save_overall_html(dest_dir_path="circle_basic_usage/")\n```',  # noqa
    ##################################################
    "## Note of the draw_circle interface": "## draw_circle インターフェイスに対する特記事項",
    ##################################################
    "You can also create a circle instance with the `draw_circle` interface.": "`draw_circle`インターフェイスを使って円を作成することもできます。",  # noqa
    ##################################################
    "Please see also:": "関連資料:",
    ##################################################
    "- [Graphics class draw_circle interface](graphics_draw_circle.md)": "- [Graphics クラスの draw_circle (円の描画)のインターフェイス](jp_graphics_draw_circle.md)",  # noqa
    ##################################################
    "## x property interface example": "## x属性のインターフェイス例",
    ##################################################
    "The `x` property updates or gets the instance's x-coordinate:": "`x`属性ではX座標の値の更新もしくは取得を行えます:",  # noqa
    ##################################################
    '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    background_color=ap.Color("#333"),\n    stage_width=200,\n    stage_height=150,\n    stage_elem_id="stage",\n)\ncircle: ap.Circle = ap.Circle(\n    x=0,\n    y=75,\n    radius=50,\n    fill_color=ap.Color("#0af"),\n)\ncircle.x = ap.Number(100)\n\nap.save_overall_html(dest_dir_path="circle_x/")\n```': '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    background_color=ap.Color("#333"),\n    stage_width=200,\n    stage_height=150,\n    stage_elem_id="stage",\n)\ncircle: ap.Circle = ap.Circle(\n    x=0,\n    y=75,\n    radius=50,\n    fill_color=ap.Color("#0af"),\n)\ncircle.x = ap.Number(100)\n\nap.save_overall_html(dest_dir_path="circle_x/")\n```',  # noqa
    ##################################################
    "## y property interface example": "## y属性のインターフェイス例",
    ##################################################
    "The `y` property updates or gets the instance's y-coordinate:": "`y`属性ではY座標の値の更新もしくは取得を行えます:",  # noqa
    ##################################################
    '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    background_color=ap.Color("#333"),\n    stage_width=150,\n    stage_height=200,\n    stage_elem_id="stage",\n)\ncircle: ap.Circle = ap.Circle(\n    x=75,\n    y=0,\n    radius=50,\n    fill_color=ap.Color("#0af"),\n)\ncircle.y = ap.Number(100)\n\nap.save_overall_html(dest_dir_path="circle_y/")\n```': '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    background_color=ap.Color("#333"),\n    stage_width=150,\n    stage_height=200,\n    stage_elem_id="stage",\n)\ncircle: ap.Circle = ap.Circle(\n    x=75,\n    y=0,\n    radius=50,\n    fill_color=ap.Color("#0af"),\n)\ncircle.y = ap.Number(100)\n\nap.save_overall_html(dest_dir_path="circle_y/")\n```',  # noqa
    ##################################################
    "## radius property interface example": "## radius属性のインターフェイス例",
    ##################################################
    "The `radius` property updates or gets the instance's radius:": "`radius`属性では円の半径の値の更新もしくは取得を行えます:",  # noqa
    ##################################################
    '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    background_color=ap.Color("#333"),\n    stage_width=150,\n    stage_height=150,\n    stage_elem_id="stage",\n)\ncircle: ap.Circle = ap.Circle(\n    x=75,\n    y=75,\n    radius=0,\n    fill_color=ap.Color("#0af"),\n)\ncircle.radius = ap.Int(30)\n\nap.save_overall_html(dest_dir_path="circle_radius/")\n```': '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    background_color=ap.Color("#333"),\n    stage_width=150,\n    stage_height=150,\n    stage_elem_id="stage",\n)\ncircle: ap.Circle = ap.Circle(\n    x=75,\n    y=75,\n    radius=0,\n    fill_color=ap.Color("#0af"),\n)\ncircle.radius = ap.Int(30)\n\nap.save_overall_html(dest_dir_path="circle_radius/")\n```',  # noqa
    ##################################################
    "## fill_color property interface example": "## fill_color属性のインターフェイス例",
    ##################################################
    "The `fill_color` property updates or gets the instance's fill color:": "`fill_color`属性は塗りの色の値の更新もしくは取得を行えます:",  # noqa
    ##################################################
    '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    background_color=ap.Color("#333"),\n    stage_width=150,\n    stage_height=150,\n    stage_elem_id="stage",\n)\ncircle: ap.Circle = ap.Circle(x=75, y=75, radius=50)\ncircle.fill_color = ap.Color("#f0a")\n\nap.save_overall_html(dest_dir_path="circle_fill_color/")\n```': '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    background_color=ap.Color("#333"),\n    stage_width=150,\n    stage_height=150,\n    stage_elem_id="stage",\n)\ncircle: ap.Circle = ap.Circle(x=75, y=75, radius=50)\ncircle.fill_color = ap.Color("#f0a")\n\nap.save_overall_html(dest_dir_path="circle_fill_color/")\n```',  # noqa
    ##################################################
    "## fill_alpha property interface example": "## fill_alpha属性のインターフェイス例",
    ##################################################
    "The `fill_alpha` property updates or gets the instance's fill alpha (opacity):": "`fill_alpha`属性は塗りの透明度の値の更新もしくは取得を行えます:",  # noqa
    ##################################################
    '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    background_color=ap.Color("#333"),\n    stage_width=150,\n    stage_height=150,\n    stage_elem_id="stage",\n)\ncircle: ap.Circle = ap.Circle(\n    x=75,\n    y=75,\n    radius=50,\n    fill_color=ap.Color("#0af"),\n)\ncircle.fill_alpha = ap.Number(0.3)\n\nap.save_overall_html(dest_dir_path="circle_fill_alpha/")\n```': '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    background_color=ap.Color("#333"),\n    stage_width=150,\n    stage_height=150,\n    stage_elem_id="stage",\n)\ncircle: ap.Circle = ap.Circle(\n    x=75,\n    y=75,\n    radius=50,\n    fill_color=ap.Color("#0af"),\n)\ncircle.fill_alpha = ap.Number(0.3)\n\nap.save_overall_html(dest_dir_path="circle_fill_alpha/")\n```',  # noqa
    ##################################################
    "## line_color property interface example": "## line_color属性のインターフェイス例",
    ##################################################
    "The `line_color` property updates or gets the instance's line color:": "`line_color`属性では線の色の値の更新もしくは取得を行えます:",  # noqa
    ##################################################
    '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    background_color=ap.Color("#333"),\n    stage_width=150,\n    stage_height=150,\n    stage_elem_id="stage",\n)\ncircle: ap.Circle = ap.Circle(x=75, y=75, radius=50, line_thickness=5)\ncircle.line_color = ap.Color("#f0a")\n\nap.save_overall_html(dest_dir_path="circle_line_color/")\n```': '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    background_color=ap.Color("#333"),\n    stage_width=150,\n    stage_height=150,\n    stage_elem_id="stage",\n)\ncircle: ap.Circle = ap.Circle(x=75, y=75, radius=50, line_thickness=5)\ncircle.line_color = ap.Color("#f0a")\n\nap.save_overall_html(dest_dir_path="circle_line_color/")\n```',  # noqa
    ##################################################
    "## line_alpha property interface example": "## line_alpha属性のインターフェイス例",
    ##################################################
    "The `line_alpha` property updates or gets the instance's line alpha (opacity):": "`line_alpha`属性では線の透明度の値の更新もしくは取得を行えます:",  # noqa
    ##################################################
    '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    background_color=ap.Color("#333"),\n    stage_width=150,\n    stage_height=150,\n    stage_elem_id="stage",\n)\ncircle: ap.Circle = ap.Circle(\n    x=75,\n    y=75,\n    radius=50,\n    line_color=ap.Color("0af"),\n    line_thickness=5,\n)\ncircle.line_alpha = ap.Number(0.3)\n\nap.save_overall_html(dest_dir_path="circle_line_alpha/")\n```': '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    background_color=ap.Color("#333"),\n    stage_width=150,\n    stage_height=150,\n    stage_elem_id="stage",\n)\ncircle: ap.Circle = ap.Circle(\n    x=75,\n    y=75,\n    radius=50,\n    line_color=ap.Color("0af"),\n    line_thickness=5,\n)\ncircle.line_alpha = ap.Number(0.3)\n\nap.save_overall_html(dest_dir_path="circle_line_alpha/")\n```',  # noqa
    ##################################################
    "## line_thickness property interface example": "## line_thickness属性のインターフェイス例",
    ##################################################
    "The `line_thickness` property updates or gets the instance's line thickness (line width):": "`line_thickness`属性では線の幅の更新もしくは取得を行えます:",  # noqa
    ##################################################
    '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    background_color=ap.Color("#333"),\n    stage_width=150,\n    stage_height=150,\n    stage_elem_id="stage",\n)\ncircle: ap.Circle = ap.Circle(\n    x=75,\n    y=75,\n    radius=50,\n    line_color=ap.Color("0af"),\n)\ncircle.line_thickness = ap.Int(8)\n\nap.save_overall_html(dest_dir_path="circle_line_thickness/")\n```': '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    background_color=ap.Color("#333"),\n    stage_width=150,\n    stage_height=150,\n    stage_elem_id="stage",\n)\ncircle: ap.Circle = ap.Circle(\n    x=75,\n    y=75,\n    radius=50,\n    line_color=ap.Color("0af"),\n)\ncircle.line_thickness = ap.Int(8)\n\nap.save_overall_html(dest_dir_path="circle_line_thickness/")\n```',  # noqa
    ##################################################
    "## line_dot_setting property interface example": "## line_dot_setting属性のインターフェイス例",  # noqa
    ##################################################
    "The `line_dot_setting` property updates or gets the instance's line dot-style setting:": "`line_dot_setting`属性では点線のスタイル設定の更新もしくは取得を行えます:",  # noqa
    ##################################################
    '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    background_color=ap.Color("#333"),\n    stage_width=150,\n    stage_height=150,\n    stage_elem_id="stage",\n)\ncircle: ap.Circle = ap.Circle(\n    x=75,\n    y=75,\n    radius=50,\n    line_color=ap.Color("0af"),\n    line_thickness=3,\n)\ncircle.line_dot_setting = ap.LineDotSetting(dot_size=3)\n\nap.save_overall_html(dest_dir_path="circle_line_dot_setting/")\n```': '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    background_color=ap.Color("#333"),\n    stage_width=150,\n    stage_height=150,\n    stage_elem_id="stage",\n)\ncircle: ap.Circle = ap.Circle(\n    x=75,\n    y=75,\n    radius=50,\n    line_color=ap.Color("0af"),\n    line_thickness=3,\n)\ncircle.line_dot_setting = ap.LineDotSetting(dot_size=3)\n\nap.save_overall_html(dest_dir_path="circle_line_dot_setting/")\n```',  # noqa
    ##################################################
    "## line_dash_setting property interface example": "## line_dash_setting属性のインターフェイス例",  # noqa
    ##################################################
    "The `line_dash_setting` property updates or gets the instance's line dash-style setting:": "`line_dash_setting`属性では破線のスタイル設定の更新もしくは取得を行えます:",  # noqa
    ##################################################
    '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    background_color=ap.Color("#333"),\n    stage_width=150,\n    stage_height=150,\n    stage_elem_id="stage",\n)\ncircle: ap.Circle = ap.Circle(\n    x=75,\n    y=75,\n    radius=50,\n    line_color=ap.Color("0af"),\n    line_thickness=3,\n)\ncircle.line_dash_setting = ap.LineDashSetting(dash_size=5, space_size=2)\n\nap.save_overall_html(dest_dir_path="circle_line_dash_setting/")\n```': '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    background_color=ap.Color("#333"),\n    stage_width=150,\n    stage_height=150,\n    stage_elem_id="stage",\n)\ncircle: ap.Circle = ap.Circle(\n    x=75,\n    y=75,\n    radius=50,\n    line_color=ap.Color("0af"),\n    line_thickness=3,\n)\ncircle.line_dash_setting = ap.LineDashSetting(dash_size=5, space_size=2)\n\nap.save_overall_html(dest_dir_path="circle_line_dash_setting/")\n```',  # noqa
    ##################################################
    "## line_round_dot_setting property interface example": "## line_round_dot_setting属性のインターフェイス例",  # noqa
    ##################################################
    "The `line_round_dot_setting` property updates or gets the instance's line-round dot-style setting:": "`line_round_dot_setting`属性では丸ドット線のスタイル設定の更新もしくは取得を行えます:",  # noqa
    ##################################################
    '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    background_color=ap.Color("#333"),\n    stage_width=150,\n    stage_height=150,\n    stage_elem_id="stage",\n)\ncircle: ap.Circle = ap.Circle(\n    x=75,\n    y=75,\n    radius=50,\n    line_color=ap.Color("0af"),\n)\ncircle.line_round_dot_setting = ap.LineRoundDotSetting(round_size=5, space_size=3)\n\nap.save_overall_html(dest_dir_path="circle_line_round_dot_setting/")\n```': '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    background_color=ap.Color("#333"),\n    stage_width=150,\n    stage_height=150,\n    stage_elem_id="stage",\n)\ncircle: ap.Circle = ap.Circle(\n    x=75,\n    y=75,\n    radius=50,\n    line_color=ap.Color("0af"),\n)\ncircle.line_round_dot_setting = ap.LineRoundDotSetting(round_size=5, space_size=3)\n\nap.save_overall_html(dest_dir_path="circle_line_round_dot_setting/")\n```',  # noqa
    ##################################################
    "## line_dash_dot_setting property interface example": "## line_dash_dot_setting属性のインターフェイス例",  # noqa
    ##################################################
    "The `line_dash_dot_setting` property updates or gets the instance's dash-dotted line style setting:": "`line_dash_dot_setting`属性では一点鎖線のスタイル設定の更新もしくは取得を行えます:",  # noqa
    ##################################################
    '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    background_color=ap.Color("#333"),\n    stage_width=150,\n    stage_height=150,\n    stage_elem_id="stage",\n)\ncircle: ap.Circle = ap.Circle(\n    x=75,\n    y=75,\n    radius=50,\n    line_color=ap.Color("0af"),\n    line_thickness=3,\n)\ncircle.line_dash_dot_setting = ap.LineDashDotSetting(\n    dot_size=3, dash_size=6, space_size=3\n)\n\nap.save_overall_html(dest_dir_path="circle_line_dash_dot_setting/")\n```': '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    background_color=ap.Color("#333"),\n    stage_width=150,\n    stage_height=150,\n    stage_elem_id="stage",\n)\ncircle: ap.Circle = ap.Circle(\n    x=75,\n    y=75,\n    radius=50,\n    line_color=ap.Color("0af"),\n    line_thickness=3,\n)\ncircle.line_dash_dot_setting = ap.LineDashDotSetting(\n    dot_size=3, dash_size=6, space_size=3\n)\n\nap.save_overall_html(dest_dir_path="circle_line_dash_dot_setting/")\n```',  # noqa
    ##################################################
    "## rotation_around_center property interface example": "## rotation_around_center属性のインターフェイス例",  # noqa
    ##################################################
    "The `rotation_around_center` property updates or gets the instance's rotation value (0 to 359) from the center point:": "`rotation_around_center`属性ではインスタンスの中央座標での回転量（0～359）の更新もしくは取得を行えます:",  # noqa
    ##################################################
    '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    background_color=ap.Color("#333"),\n    stage_width=150,\n    stage_height=150,\n    stage_elem_id="stage",\n)\ncircle: ap.Circle = ap.Circle(\n    x=75,\n    y=75,\n    radius=50,\n    fill_color=ap.Color("#0af"),\n)\ncircle.scale_x_from_center = ap.Number(0.5)\n\n\ndef on_timer(e: ap.TimerEvent, options: dict) -> None:\n    """\n    The timer event handler.\n\n    Parameters\n    ----------\n    e : ap.TimerEvent\n        Event instance.\n    options : dict\n        Optional arguments dictionary.\n    """\n    circle.rotation_around_center += 1\n\n\nap.Timer(on_timer, delay=ap.FPS.FPS_60).start()\nap.save_overall_html(dest_dir_path="circle_rotation_around_center/")\n```': '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    background_color=ap.Color("#333"),\n    stage_width=150,\n    stage_height=150,\n    stage_elem_id="stage",\n)\ncircle: ap.Circle = ap.Circle(\n    x=75,\n    y=75,\n    radius=50,\n    fill_color=ap.Color("#0af"),\n)\ncircle.scale_x_from_center = ap.Number(0.5)\n\n\ndef on_timer(e: ap.TimerEvent, options: dict) -> None:\n    """\n    The timer event handler.\n\n    Parameters\n    ----------\n    e : ap.TimerEvent\n        Event instance.\n    options : dict\n        Optional arguments dictionary.\n    """\n    circle.rotation_around_center += 1\n\n\nap.Timer(on_timer, delay=ap.FPS.FPS_60).start()\nap.save_overall_html(dest_dir_path="circle_rotation_around_center/")\n```',  # noqa
    ##################################################
    "## set_rotation_around_point and get_rotation_around_point methods interface example": "## set_rotation_around_pointとget_rotation_around_pointメソッドのインターフェイス例",  # noqa
    ##################################################
    "The `set_rotation_around_point` method updates the instance's rotation value (0 to 359) from a specified point.": "`set_rotation_around_point`メソッドは指定された座標からのインスタンスの回転量（0～359）を更新します。",  # noqa
    ##################################################
    "Similarly, the `get_rotation_around_point` method gets the instance's rotation value (0 to 359) from a specified point:": "同様に、`get_rotation_around_point`メソッドでは指定された座標のインスタンスの回転量（0～359）を取得します:",  # noqa
    ##################################################
    '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    background_color=ap.Color("#333"),\n    stage_width=150,\n    stage_height=150,\n    stage_elem_id="stage",\n)\ncircle: ap.Circle = ap.Circle(\n    x=75,\n    y=75,\n    radius=50,\n    fill_color=ap.Color("#0af"),\n)\ncircle.scale_x_from_center = ap.Number(0.5)\nx: ap.Int = ap.Int(100)\ny: ap.Int = ap.Int(100)\n\n\ndef on_timer(e: ap.TimerEvent, options: dict) -> None:\n    """\n    The timer event handler.\n\n    Parameters\n    ----------\n    e : ap.TimerEvent\n        Event instance.\n    options : dict\n        Optional arguments dictionary.\n    """\n    rotation: ap.Int = circle.get_rotation_around_point(x=x, y=y)\n    rotation += 1\n    circle.set_rotation_around_point(rotation=rotation, x=x, y=y)\n\n\nap.Timer(on_timer, delay=ap.FPS.FPS_60).start()\nap.save_overall_html(dest_dir_path="circle_set_rotation_around_point/")\n```': '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    background_color=ap.Color("#333"),\n    stage_width=150,\n    stage_height=150,\n    stage_elem_id="stage",\n)\ncircle: ap.Circle = ap.Circle(\n    x=75,\n    y=75,\n    radius=50,\n    fill_color=ap.Color("#0af"),\n)\ncircle.scale_x_from_center = ap.Number(0.5)\nx: ap.Int = ap.Int(100)\ny: ap.Int = ap.Int(100)\n\n\ndef on_timer(e: ap.TimerEvent, options: dict) -> None:\n    """\n    The timer event handler.\n\n    Parameters\n    ----------\n    e : ap.TimerEvent\n        Event instance.\n    options : dict\n        Optional arguments dictionary.\n    """\n    rotation: ap.Int = circle.get_rotation_around_point(x=x, y=y)\n    rotation += 1\n    circle.set_rotation_around_point(rotation=rotation, x=x, y=y)\n\n\nap.Timer(on_timer, delay=ap.FPS.FPS_60).start()\nap.save_overall_html(dest_dir_path="circle_set_rotation_around_point/")\n```',  # noqa
    ##################################################
    "## scale_x_from_center property interface example": "## scale_x_from_center属性のインターフェイス例",  # noqa
    ##################################################
    "The `scale_x_from_center` property updates or gets the instance's scale-x from the center point:": "`scale_x_from_center`属性ではインスタンスの中央座標でのX軸の拡縮値の更新もしくは取得を行えます:",  # noqa
    ##################################################
    '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    background_color=ap.Color("#333"),\n    stage_width=150,\n    stage_height=150,\n    stage_elem_id="stage",\n)\ncircle: ap.Circle = ap.Circle(\n    x=75,\n    y=75,\n    radius=50,\n    fill_color=ap.Color("#0af"),\n)\ndirection: ap.Int = ap.Int(-1)\n\n\ndef on_timer(e: ap.TimerEvent, options: dict) -> None:\n    """\n    The timer event handler.\n\n    Parameters\n    ----------\n    e : ap.TimerEvent\n        Event instance.\n    options : dict\n        Optional arguments dictionary.\n    """\n    with ap.If(circle.scale_x_from_center <= 0.001):\n        direction.value = 1\n    with ap.If(circle.scale_x_from_center >= 2.0):\n        direction.value = -1\n    circle.scale_x_from_center += direction * 0.005\n\n\nap.Timer(on_timer, delay=ap.FPS.FPS_60).start()\nap.save_overall_html(dest_dir_path="circle_scale_x_from_center/")\n```': '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    background_color=ap.Color("#333"),\n    stage_width=150,\n    stage_height=150,\n    stage_elem_id="stage",\n)\ncircle: ap.Circle = ap.Circle(\n    x=75,\n    y=75,\n    radius=50,\n    fill_color=ap.Color("#0af"),\n)\ndirection: ap.Int = ap.Int(-1)\n\n\ndef on_timer(e: ap.TimerEvent, options: dict) -> None:\n    """\n    The timer event handler.\n\n    Parameters\n    ----------\n    e : ap.TimerEvent\n        Event instance.\n    options : dict\n        Optional arguments dictionary.\n    """\n    with ap.If(circle.scale_x_from_center <= 0.001):\n        direction.value = 1\n    with ap.If(circle.scale_x_from_center >= 2.0):\n        direction.value = -1\n    circle.scale_x_from_center += direction * 0.005\n\n\nap.Timer(on_timer, delay=ap.FPS.FPS_60).start()\nap.save_overall_html(dest_dir_path="circle_scale_x_from_center/")\n```',  # noqa
    ##################################################
    "## scale_y_from_center property interface example": "## scale_y_from_center属性のインターフェイス例",  # noqa
    ##################################################
    "The `scale_y_from_center` property updates or gets the instance's scale-y from the center point:": "`scale_y_from_center`属性ではインスタンスの中央座標でのX軸の拡縮値の更新もしくは取得を行えます:",  # noqa
    ##################################################
    '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    background_color=ap.Color("#333"),\n    stage_width=150,\n    stage_height=150,\n    stage_elem_id="stage",\n)\ncircle: ap.Circle = ap.Circle(\n    x=75,\n    y=75,\n    radius=50,\n    fill_color=ap.Color("#0af"),\n)\ndirection: ap.Int = ap.Int(-1)\n\n\ndef on_timer(e: ap.TimerEvent, options: dict) -> None:\n    """\n    The timer event handler.\n\n    Parameters\n    ----------\n    e : ap.TimerEvent\n        Event instance.\n    options : dict\n        Optional arguments dictionary.\n    """\n    with ap.If(circle.scale_y_from_center <= 0.001):\n        direction.value = 1\n    with ap.If(circle.scale_y_from_center >= 2.0):\n        direction.value = -1\n    circle.scale_y_from_center += direction * 0.005\n\n\nap.Timer(on_timer, delay=ap.FPS.FPS_60).start()\nap.save_overall_html(dest_dir_path="circle_scale_y_from_center/")\n```': '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    background_color=ap.Color("#333"),\n    stage_width=150,\n    stage_height=150,\n    stage_elem_id="stage",\n)\ncircle: ap.Circle = ap.Circle(\n    x=75,\n    y=75,\n    radius=50,\n    fill_color=ap.Color("#0af"),\n)\ndirection: ap.Int = ap.Int(-1)\n\n\ndef on_timer(e: ap.TimerEvent, options: dict) -> None:\n    """\n    The timer event handler.\n\n    Parameters\n    ----------\n    e : ap.TimerEvent\n        Event instance.\n    options : dict\n        Optional arguments dictionary.\n    """\n    with ap.If(circle.scale_y_from_center <= 0.001):\n        direction.value = 1\n    with ap.If(circle.scale_y_from_center >= 2.0):\n        direction.value = -1\n    circle.scale_y_from_center += direction * 0.005\n\n\nap.Timer(on_timer, delay=ap.FPS.FPS_60).start()\nap.save_overall_html(dest_dir_path="circle_scale_y_from_center/")\n```',  # noqa
    ##################################################
    "## set_scale_x_from_point and get_scale_x_from_point methods interface example": "## set_scale_x_from_pointとget_scale_x_from_pointメソッドのインターフェイス例",  # noqa
    ##################################################
    "The `set_scale_x_from_point` method updates the instance's scale-x from a specified point.": "`set_scale_x_from_point`メソッドは指定されたX座標を基準としてX軸の拡縮値を更新します。",  # noqa
    ##################################################
    "Similarly, the `get_scale_x_from_point` method gets the instance's scale-x from a specified point:": "同様に、`get_scale_x_from_point`メソッドでは指定されたX座標を基準としたX軸の拡縮値を取得します:",  # noqa
    ##################################################
    '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    background_color=ap.Color("#333"),\n    stage_width=150,\n    stage_height=150,\n    stage_elem_id="stage",\n)\ncircle: ap.Circle = ap.Circle(\n    x=75,\n    y=75,\n    radius=50,\n    fill_color=ap.Color("#0af"),\n)\ndirection: ap.Int = ap.Int(-1)\nx: ap.Int = ap.Int(125)\n\n\ndef on_timer(e: ap.TimerEvent, options: dict) -> None:\n    """\n    The timer event handler.\n\n    Parameters\n    ----------\n    e : ap.TimerEvent\n        Event instance.\n    options : dict\n        Optional arguments dictionary.\n    """\n    scale: ap.Number = circle.get_scale_x_from_point(x=x)\n    with ap.If(scale <= 0.001):\n        direction.value = 1\n    with ap.If(scale >= 2.0):\n        direction.value = -1\n    scale += direction * 0.005\n    circle.set_scale_x_from_point(scale_x=scale, x=x)\n\n\nap.Timer(on_timer, delay=ap.FPS.FPS_60).start()\nap.save_overall_html(dest_dir_path="circle_scale_x_from_point/")\n```': '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    background_color=ap.Color("#333"),\n    stage_width=150,\n    stage_height=150,\n    stage_elem_id="stage",\n)\ncircle: ap.Circle = ap.Circle(\n    x=75,\n    y=75,\n    radius=50,\n    fill_color=ap.Color("#0af"),\n)\ndirection: ap.Int = ap.Int(-1)\nx: ap.Int = ap.Int(125)\n\n\ndef on_timer(e: ap.TimerEvent, options: dict) -> None:\n    """\n    The timer event handler.\n\n    Parameters\n    ----------\n    e : ap.TimerEvent\n        Event instance.\n    options : dict\n        Optional arguments dictionary.\n    """\n    scale: ap.Number = circle.get_scale_x_from_point(x=x)\n    with ap.If(scale <= 0.001):\n        direction.value = 1\n    with ap.If(scale >= 2.0):\n        direction.value = -1\n    scale += direction * 0.005\n    circle.set_scale_x_from_point(scale_x=scale, x=x)\n\n\nap.Timer(on_timer, delay=ap.FPS.FPS_60).start()\nap.save_overall_html(dest_dir_path="circle_scale_x_from_point/")\n```',  # noqa
    ##################################################
    "## set_scale_y_from_point and get_scale_y_from_point methods interface example": "## set_scale_y_from_pointとget_scale_y_from_pointメソッドのインターフェイス例",  # noqa
    ##################################################
    "The `set_scale_y_from_point` method updates the instance's scale-y from a specified point.": "`set_scale_y_from_point`メソッドは指定されたY座標を基準としてY軸の拡縮値を更新します。",  # noqa
    ##################################################
    "Similarly, the `get_scale_y_from_point` method gets the instance's scale-y from a specified point:": "同様に、`get_scale_y_from_point`メソッドでは指定されたY座標を基準としたY軸の拡縮値を取得します。",  # noqa
    ##################################################
    '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    background_color=ap.Color("#333"),\n    stage_width=150,\n    stage_height=150,\n    stage_elem_id="stage",\n)\ncircle: ap.Circle = ap.Circle(\n    x=75,\n    y=75,\n    radius=50,\n    fill_color=ap.Color("#0af"),\n)\ndirection: ap.Int = ap.Int(-1)\ny: ap.Int = ap.Int(125)\n\n\ndef on_timer(e: ap.TimerEvent, options: dict) -> None:\n    """\n    The timer event handler.\n\n    Parameters\n    ----------\n    e : ap.TimerEvent\n        Event instance.\n    options : dict\n        Optional arguments dictionary.\n    """\n    scale: ap.Number = circle.get_scale_y_from_point(y=y)\n    with ap.If(scale <= 0.001):\n        direction.value = 1\n    with ap.If(scale >= 2.0):\n        direction.value = -1\n    scale += direction * 0.005\n    circle.set_scale_y_from_point(scale_y=scale, y=y)\n\n\nap.Timer(on_timer, delay=ap.FPS.FPS_60).start()\nap.save_overall_html(dest_dir_path="circle_scale_y_from_point/")\n```': '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    background_color=ap.Color("#333"),\n    stage_width=150,\n    stage_height=150,\n    stage_elem_id="stage",\n)\ncircle: ap.Circle = ap.Circle(\n    x=75,\n    y=75,\n    radius=50,\n    fill_color=ap.Color("#0af"),\n)\ndirection: ap.Int = ap.Int(-1)\ny: ap.Int = ap.Int(125)\n\n\ndef on_timer(e: ap.TimerEvent, options: dict) -> None:\n    """\n    The timer event handler.\n\n    Parameters\n    ----------\n    e : ap.TimerEvent\n        Event instance.\n    options : dict\n        Optional arguments dictionary.\n    """\n    scale: ap.Number = circle.get_scale_y_from_point(y=y)\n    with ap.If(scale <= 0.001):\n        direction.value = 1\n    with ap.If(scale >= 2.0):\n        direction.value = -1\n    scale += direction * 0.005\n    circle.set_scale_y_from_point(scale_y=scale, y=y)\n\n\nap.Timer(on_timer, delay=ap.FPS.FPS_60).start()\nap.save_overall_html(dest_dir_path="circle_scale_y_from_point/")\n```',  # noqa
    ##################################################
    "## flip_x property interface example": "## flip_x属性のインターフェイス例",
    ##################################################
    "The `flip_x` property updates or gets the instance's flip-x (reflecting state) boolean value:": "`flip_x`属性ではインスタンスのX軸の反転状況の真偽値の更新もしくは取得を行えます:",  # noqa
    ##################################################
    '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    background_color=ap.Color("#333"),\n    stage_width=150,\n    stage_height=150,\n    stage_elem_id="stage",\n)\ncircle: ap.Circle = ap.Circle(\n    x=75,\n    y=75,\n    radius=50,\n    fill_color=ap.Color("#0af"),\n)\ncircle.scale_x_from_center = ap.Number(0.5)\ncircle.rotation_around_center = ap.Int(30)\n\n\ndef on_timer(e: ap.TimerEvent, options: dict) -> None:\n    """\n    The timer event handler.\n\n    Parameters\n    ----------\n    e : ap.TimerEvent\n        Event instance.\n    options : dict\n        Optional arguments dictionary.\n    """\n    circle.flip_x = circle.flip_x.not_\n\n\nap.Timer(on_timer, delay=1000).start()\nap.save_overall_html(dest_dir_path="circle_flip_x/")\n```': '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    background_color=ap.Color("#333"),\n    stage_width=150,\n    stage_height=150,\n    stage_elem_id="stage",\n)\ncircle: ap.Circle = ap.Circle(\n    x=75,\n    y=75,\n    radius=50,\n    fill_color=ap.Color("#0af"),\n)\ncircle.scale_x_from_center = ap.Number(0.5)\ncircle.rotation_around_center = ap.Int(30)\n\n\ndef on_timer(e: ap.TimerEvent, options: dict) -> None:\n    """\n    The timer event handler.\n\n    Parameters\n    ----------\n    e : ap.TimerEvent\n        Event instance.\n    options : dict\n        Optional arguments dictionary.\n    """\n    circle.flip_x = circle.flip_x.not_\n\n\nap.Timer(on_timer, delay=1000).start()\nap.save_overall_html(dest_dir_path="circle_flip_x/")\n```',  # noqa
    ##################################################
    "Notes: Depending on the shape of the instance, this may be difficult to tell the difference between the x and y axes interfaces.": "特記事項: インスタンスの形状によってはこのインターフェイスはX軸とY軸の各インターフェイスで違いが分かりづらいケースが発生します。",  # noqa
    ##################################################
    "## flip_y property interface example": "## flip_y属性のインターフェイス例",
    ##################################################
    "The `flip_y` property updates or gets the instance's flip-y (reflecting state) boolean value:": "`flip_y`属性ではインスタンスのX軸の反転状況の真偽値の更新もしくは取得を行えます:",  # noqa
    ##################################################
    '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    background_color=ap.Color("#333"),\n    stage_width=150,\n    stage_height=150,\n    stage_elem_id="stage",\n)\ncircle: ap.Circle = ap.Circle(\n    x=75,\n    y=75,\n    radius=50,\n    fill_color=ap.Color("#0af"),\n)\ncircle.scale_x_from_center = ap.Number(0.5)\ncircle.rotation_around_center = ap.Int(30)\n\n\ndef on_timer(e: ap.TimerEvent, options: dict) -> None:\n    """\n    The timer event handler.\n\n    Parameters\n    ----------\n    e : ap.TimerEvent\n        Event instance.\n    options : dict\n        Optional arguments dictionary.\n    """\n    circle.flip_y = circle.flip_y.not_\n\n\nap.Timer(on_timer, delay=1000).start()\nap.save_overall_html(dest_dir_path="circle_flip_y/")\n```': '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    background_color=ap.Color("#333"),\n    stage_width=150,\n    stage_height=150,\n    stage_elem_id="stage",\n)\ncircle: ap.Circle = ap.Circle(\n    x=75,\n    y=75,\n    radius=50,\n    fill_color=ap.Color("#0af"),\n)\ncircle.scale_x_from_center = ap.Number(0.5)\ncircle.rotation_around_center = ap.Int(30)\n\n\ndef on_timer(e: ap.TimerEvent, options: dict) -> None:\n    """\n    The timer event handler.\n\n    Parameters\n    ----------\n    e : ap.TimerEvent\n        Event instance.\n    options : dict\n        Optional arguments dictionary.\n    """\n    circle.flip_y = circle.flip_y.not_\n\n\nap.Timer(on_timer, delay=1000).start()\nap.save_overall_html(dest_dir_path="circle_flip_y/")\n```',  # noqa
    ##################################################
    "Notes: Depending on the shape of the instance, this may be difficult to tell the difference between the x and y axes interfaces.": "特記事項: インスタンスの形状によってはこのインターフェイスはX軸とY軸の各インターフェイスで違いが分かりづらいケースが発生します。",  # noqa
    ##################################################
    "## skew_x property interface example": "## skew_x属性のインターフェイス例",
    ##################################################
    "The `skew_x` property updates or gets the instance's skew-x (distortion) value:": "`skew_x`属性ではインスタンスのX軸の歪みの値の更新もしくは取得を行えます:",  # noqa
    ##################################################
    '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    background_color=ap.Color("#333"),\n    stage_width=150,\n    stage_height=150,\n    stage_elem_id="stage",\n)\ncircle: ap.Circle = ap.Circle(\n    x=75,\n    y=75,\n    radius=50,\n    fill_color=ap.Color("#0af"),\n)\n\n\ndef on_timer(e: ap.TimerEvent, options: dict) -> None:\n    """\n    The timer event handler.\n\n    Parameters\n    ----------\n    e : ap.TimerEvent\n        Event instance.\n    options : dict\n        Optional arguments dictionary.\n    """\n    circle.skew_x += 1\n\n\nap.Timer(on_timer, delay=ap.FPS.FPS_60).start()\nap.save_overall_html(dest_dir_path="circle_skew_x/")\n```': '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    background_color=ap.Color("#333"),\n    stage_width=150,\n    stage_height=150,\n    stage_elem_id="stage",\n)\ncircle: ap.Circle = ap.Circle(\n    x=75,\n    y=75,\n    radius=50,\n    fill_color=ap.Color("#0af"),\n)\n\n\ndef on_timer(e: ap.TimerEvent, options: dict) -> None:\n    """\n    The timer event handler.\n\n    Parameters\n    ----------\n    e : ap.TimerEvent\n        Event instance.\n    options : dict\n        Optional arguments dictionary.\n    """\n    circle.skew_x += 1\n\n\nap.Timer(on_timer, delay=ap.FPS.FPS_60).start()\nap.save_overall_html(dest_dir_path="circle_skew_x/")\n```',  # noqa
    ##################################################
    "Notes: Depending on the shape of the instance, this may be difficult to tell the difference between the x and y axes interfaces.": "特記事項: インスタンスの形状によってはこのインターフェイスはX軸とY軸の各インターフェイスで違いが分かりづらいケースが発生します。",  # noqa
    ##################################################
    "## skew_y property interface example": "## skew_y属性のインターフェイス例",
    ##################################################
    "The `skew_y` property updates or gets the instance's skew-y (distortion) value:": "`skew_y`属性ではインスタンスのY軸の歪みの値の更新もしくは取得を行えます:",  # noqa
    ##################################################
    '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    background_color=ap.Color("#333"),\n    stage_width=150,\n    stage_height=150,\n    stage_elem_id="stage",\n)\ncircle: ap.Circle = ap.Circle(\n    x=75,\n    y=75,\n    radius=50,\n    fill_color=ap.Color("#0af"),\n)\n\n\ndef on_timer(e: ap.TimerEvent, options: dict) -> None:\n    """\n    The timer event handler.\n\n    Parameters\n    ----------\n    e : ap.TimerEvent\n        Event instance.\n    options : dict\n        Optional arguments dictionary.\n    """\n    circle.skew_y += 1\n\n\nap.Timer(on_timer, delay=ap.FPS.FPS_60).start()\nap.save_overall_html(dest_dir_path="circle_skew_y/")\n```': '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    background_color=ap.Color("#333"),\n    stage_width=150,\n    stage_height=150,\n    stage_elem_id="stage",\n)\ncircle: ap.Circle = ap.Circle(\n    x=75,\n    y=75,\n    radius=50,\n    fill_color=ap.Color("#0af"),\n)\n\n\ndef on_timer(e: ap.TimerEvent, options: dict) -> None:\n    """\n    The timer event handler.\n\n    Parameters\n    ----------\n    e : ap.TimerEvent\n        Event instance.\n    options : dict\n        Optional arguments dictionary.\n    """\n    circle.skew_y += 1\n\n\nap.Timer(on_timer, delay=ap.FPS.FPS_60).start()\nap.save_overall_html(dest_dir_path="circle_skew_y/")\n```',  # noqa
    ##################################################
    "Notes: Depending on the shape of the instance, this may be difficult to tell the difference between the x and y axes interfaces.": "特記事項: インスタンスの形状によってはこのインターフェイスはX軸とY軸の各インターフェイスで違いが分かりづらいケースが発生します。",  # noqa
    ##################################################
    "## Circle class constructor API": "## Circle クラスのコンストラクタのAPI",
    ##################################################
    '<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>': '<span class="inconspicuous-txt">特記事項: このAPIドキュメントはドキュメントビルド用のスクリプトによって自動で生成・同期されています。そのためもしかしたらこの節の内容は前節までの内容と重複している場合があります。</span>',  # noqa
    ##################################################
    "**[Interface summary]**": "**[インターフェイス概要]**",
    ##################################################
    "Create a circle vector graphic.<hr>": "円のベクターグラフィックスを生成します。<hr>",
    ##################################################
    "**[Parameters]**": "**[引数]**",
    ##################################################
    "- `x`: float or Number": "- `x`: float or Number",
    ##################################################
    "  - X-coordinate of the circle center.": "  - 円の中心のX座標。",
    ##################################################
    "- `y`: float or Number": "- `y`: float or Number",
    ##################################################
    "  - Y-coordinate of the circle center.": "  - 円の中心のY座標。",
    ##################################################
    "- `radius`: Int or int": "- `radius`: Int or int",
    ##################################################
    "  - Circle radius.": "  - 円の半径。",
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
    '```py\n>>> import apysc as ap\n>>> stage: ap.Stage = ap.Stage()\n>>> circle: ap.Circle = ap.Circle(\n...     x=100, y=100, radius=50, fill_color=ap.Color("#00aaff")\n... )\n>>> circle.x\nNumber(100.0)\n\n>>> circle.y\nNumber(100.0)\n\n>>> circle.radius\nInt(50)\n\n>>> circle.fill_color\nColor("#00aaff")\n\n>>> circle = ap.Circle(\n...     x=100,\n...     y=100,\n...     radius=50,\n...     line_color=ap.Color("#ffffff"),\n...     line_thickness=3,\n...     line_dot_setting=ap.LineDotSetting(dot_size=10),\n... )\n>>> circle.line_color\nColor("#ffffff")\n\n>>> circle.line_thickness\nInt(3)\n```': '```py\n>>> import apysc as ap\n>>> stage: ap.Stage = ap.Stage()\n>>> circle: ap.Circle = ap.Circle(\n...     x=100, y=100, radius=50, fill_color=ap.Color("#00aaff")\n... )\n>>> circle.x\nNumber(100.0)\n\n>>> circle.y\nNumber(100.0)\n\n>>> circle.radius\nInt(50)\n\n>>> circle.fill_color\nColor("#00aaff")\n\n>>> circle = ap.Circle(\n...     x=100,\n...     y=100,\n...     radius=50,\n...     line_color=ap.Color("#ffffff"),\n...     line_thickness=3,\n...     line_dot_setting=ap.LineDotSetting(dot_size=10),\n... )\n>>> circle.line_color\nColor("#ffffff")\n\n>>> circle.line_thickness\nInt(3)\n```',  # noqa
}
