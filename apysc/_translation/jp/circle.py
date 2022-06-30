"""This module is for the translation mapping data of the
following document:

Document file: circle.md
Language: jp
"""

from typing import Dict

MAPPING: Dict[str, str] = {

    '# Circle class':
    '# Circle クラス',

    'This page explains the `Circle` class.':
    'このページでは`Circle`クラスについて説明します。',

    '## What class is this?':
    '## クラス概要',

    'The `Circle` class creates a circle vector graphics object.':
    '`Circle`クラスは円のベクターグラフィックスを生成します。',

    '## Basic usage':
    '## 基本的な使い方',

    'The `Circle` class constructor requires the `x` (center-x), `y` (center-y), and `radius` arguments.':  # noqa
    '`Circle`クラスのコンストラクタでは`x`（円の中央のX座標）、`y`（円の中央のY座標）、そして半径としての`radius`引数が必要となります。',  # noqa

    'The constructor also accepts each style\'s argument, such as the `fill_color`.':  # noqa
    'コンストラクタでは他の`fill_color`などのスタイル設定の各引数も受け付けます。',

    '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    background_color=\'#333\',\n    stage_width=150,\n    stage_height=150,\n    stage_elem_id=\'stage\')\ncircle: ap.Circle = ap.Circle(\n    x=75, y=75, radius=50, fill_color=\'#0af\')\n\nap.save_overall_html(\n    dest_dir_path=\'circle_basic_usage/\')\n```':  # noqa
    '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    background_color=\'#333\',\n    stage_width=150,\n    stage_height=150,\n    stage_elem_id=\'stage\')\ncircle: ap.Circle = ap.Circle(\n    x=75, y=75, radius=50, fill_color=\'#0af\')\n\nap.save_overall_html(\n    dest_dir_path=\'circle_basic_usage/\')\n```',  # noqa

    '## Note of the draw_circle interface':
    '## draw_circle インターフェイスに対する特記事項',

    'You can also create a circle instance with the `draw_circle` interface.':  # noqa
    '`draw_circle`インターフェイスを使って円を作成することもできます。',

    'Please see also:':
    '関連資料:',

    '- [Graphics class draw_circle interface](graphics_draw_circle.md)':
    '- [Graphics クラスの draw_circle (円の描画)のインターフェイス](jp_graphics_draw_circle.md)',  # noqa

    '## x property interface example':
    '## x属性のインターフェイス例',

    'The `x` property updates or gets the instance\'s x-coordinate:':
    '`x`属性ではX座標の値の更新もしくは取得を行えます:',

    '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    background_color=\'#333\',\n    stage_width=200,\n    stage_height=150,\n    stage_elem_id=\'stage\')\ncircle: ap.Circle = ap.Circle(\n    x=0, y=75, radius=50, fill_color=\'#0af\')\ncircle.x = ap.Int(100)\n\nap.save_overall_html(\n    dest_dir_path=\'circle_x/\')\n```':  # noqa
    '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    background_color=\'#333\',\n    stage_width=200,\n    stage_height=150,\n    stage_elem_id=\'stage\')\ncircle: ap.Circle = ap.Circle(\n    x=0, y=75, radius=50, fill_color=\'#0af\')\ncircle.x = ap.Int(100)\n\nap.save_overall_html(\n    dest_dir_path=\'circle_x/\')\n```',  # noqa

    '## y property interface example':
    '## y属性のインターフェイス例',

    'The `y` property updates or gets the instance\'s y-coordinate:':
    '`y`属性ではY座標の値の更新もしくは取得を行えます:',

    '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    background_color=\'#333\',\n    stage_width=150,\n    stage_height=200,\n    stage_elem_id=\'stage\')\ncircle: ap.Circle = ap.Circle(\n    x=75, y=0, radius=50, fill_color=\'#0af\')\ncircle.y = ap.Int(100)\n\nap.save_overall_html(\n    dest_dir_path=\'circle_y/\')\n```':  # noqa
    '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    background_color=\'#333\',\n    stage_width=150,\n    stage_height=200,\n    stage_elem_id=\'stage\')\ncircle: ap.Circle = ap.Circle(\n    x=75, y=0, radius=50, fill_color=\'#0af\')\ncircle.y = ap.Int(100)\n\nap.save_overall_html(\n    dest_dir_path=\'circle_y/\')\n```',  # noqa

    '## radius property interface example':
    '## radius属性のインターフェイス例',

    'The `radius` property updates or gets the instance\'s radius:':
    '`radius`属性では円の半径の値の更新もしくは取得を行えます:',

    '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    background_color=\'#333\',\n    stage_width=150,\n    stage_height=150,\n    stage_elem_id=\'stage\')\ncircle: ap.Circle = ap.Circle(\n    x=75, y=75, radius=0, fill_color=\'#0af\')\ncircle.radius = ap.Int(30)\n\nap.save_overall_html(\n    dest_dir_path=\'circle_radius/\')\n```':  # noqa
    '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    background_color=\'#333\',\n    stage_width=150,\n    stage_height=150,\n    stage_elem_id=\'stage\')\ncircle: ap.Circle = ap.Circle(\n    x=75, y=75, radius=0, fill_color=\'#0af\')\ncircle.radius = ap.Int(30)\n\nap.save_overall_html(\n    dest_dir_path=\'circle_radius/\')\n```',  # noqa

    '## fill_color property interface example':
    '## fill_color属性のインターフェイス例',

    'The `fill_color` property updates or gets the instance\'s fill color:':
    '`fill_color`属性は塗りの色の値の更新もしくは取得を行えます:',

    '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    background_color=\'#333\',\n    stage_width=150,\n    stage_height=150,\n    stage_elem_id=\'stage\')\ncircle: ap.Circle = ap.Circle(x=75, y=75, radius=50)\ncircle.fill_color = ap.String(\'#f0a\')\n\nap.save_overall_html(\n    dest_dir_path=\'circle_fill_color/\')\n```':  # noqa
    '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    background_color=\'#333\',\n    stage_width=150,\n    stage_height=150,\n    stage_elem_id=\'stage\')\ncircle: ap.Circle = ap.Circle(x=75, y=75, radius=50)\ncircle.fill_color = ap.String(\'#f0a\')\n\nap.save_overall_html(\n    dest_dir_path=\'circle_fill_color/\')\n```',  # noqa

    '## fill_alpha property interface example':
    '## fill_alpha属性のインターフェイス例',

    'The `fill_alpha` property updates or gets the instance\'s fill alpha (opacity):':  # noqa
    '`fill_alpha`属性は塗りの透明度の値の更新もしくは取得を行えます:',

    '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    background_color=\'#333\',\n    stage_width=150,\n    stage_height=150,\n    stage_elem_id=\'stage\')\ncircle: ap.Circle = ap.Circle(\n    x=75, y=75, radius=50, fill_color=\'#0af\')\ncircle.fill_alpha = ap.Number(0.3)\n\nap.save_overall_html(\n    dest_dir_path=\'circle_fill_alpha/\')\n```':  # noqa
    '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    background_color=\'#333\',\n    stage_width=150,\n    stage_height=150,\n    stage_elem_id=\'stage\')\ncircle: ap.Circle = ap.Circle(\n    x=75, y=75, radius=50, fill_color=\'#0af\')\ncircle.fill_alpha = ap.Number(0.3)\n\nap.save_overall_html(\n    dest_dir_path=\'circle_fill_alpha/\')\n```',  # noqa

    '## line_color property interface example':
    '## line_color属性のインターフェイス例',

    'The `line_color` property updates or gets the instance\'s line color:':
    '`line_color`属性では線の色の値の更新もしくは取得を行えます:',

    '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    background_color=\'#333\',\n    stage_width=150,\n    stage_height=150,\n    stage_elem_id=\'stage\')\ncircle: ap.Circle = ap.Circle(\n    x=75, y=75, radius=50, line_thickness=5)\ncircle.line_color = ap.String(\'#f0a\')\n\nap.save_overall_html(\n    dest_dir_path=\'circle_line_color/\')\n```':  # noqa
    '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    background_color=\'#333\',\n    stage_width=150,\n    stage_height=150,\n    stage_elem_id=\'stage\')\ncircle: ap.Circle = ap.Circle(\n    x=75, y=75, radius=50, line_thickness=5)\ncircle.line_color = ap.String(\'#f0a\')\n\nap.save_overall_html(\n    dest_dir_path=\'circle_line_color/\')\n```',  # noqa

    '## line_alpha property interface example':
    '## line_alpha属性のインターフェイス例',

    'The `line_alpha` property updates or gets the instance\'s line alpha (opacity):':  # noqa
    '`line_alpha`属性では線の透明度の値の更新もしくは取得を行えます:',

    '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    background_color=\'#333\',\n    stage_width=150,\n    stage_height=150,\n    stage_elem_id=\'stage\')\ncircle: ap.Circle = ap.Circle(\n    x=75, y=75, radius=50, line_color=\'0af\', line_thickness=5)\ncircle.line_alpha = ap.Number(0.3)\n\nap.save_overall_html(\n    dest_dir_path=\'circle_line_alpha/\')\n```':  # noqa
    '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    background_color=\'#333\',\n    stage_width=150,\n    stage_height=150,\n    stage_elem_id=\'stage\')\ncircle: ap.Circle = ap.Circle(\n    x=75, y=75, radius=50, line_color=\'0af\', line_thickness=5)\ncircle.line_alpha = ap.Number(0.3)\n\nap.save_overall_html(\n    dest_dir_path=\'circle_line_alpha/\')\n```',  # noqa

    '## line_thickness property interface example':
    '## line_thickness属性のインターフェイス例',

    'The `line_thickness` property updates or gets the instance\'s line thickness (line width):':  # noqa
    '`line_thickness`属性では線の幅の更新もしくは取得を行えます:',

    '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    background_color=\'#333\',\n    stage_width=150,\n    stage_height=150,\n    stage_elem_id=\'stage\')\ncircle: ap.Circle = ap.Circle(\n    x=75, y=75, radius=50, line_color=\'0af\')\ncircle.line_thickness = ap.Int(8)\n\nap.save_overall_html(\n    dest_dir_path=\'circle_line_thickness/\')\n```':  # noqa
    '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    background_color=\'#333\',\n    stage_width=150,\n    stage_height=150,\n    stage_elem_id=\'stage\')\ncircle: ap.Circle = ap.Circle(\n    x=75, y=75, radius=50, line_color=\'0af\')\ncircle.line_thickness = ap.Int(8)\n\nap.save_overall_html(\n    dest_dir_path=\'circle_line_thickness/\')\n```',  # noqa

    '## line_dot_setting property interface example':
    '## line_dot_setting属性のインターフェイス例',

    'The `line_dot_setting` property updates or gets the instance\'s line dot-style setting:':  # noqa
    '`line_dot_setting`属性では点線のスタイル設定の更新もしくは取得を行えます:',

    '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    background_color=\'#333\',\n    stage_width=150,\n    stage_height=150,\n    stage_elem_id=\'stage\')\ncircle: ap.Circle = ap.Circle(\n    x=75, y=75, radius=50, line_color=\'0af\', line_thickness=3)\ncircle.line_dot_setting = ap.LineDotSetting(dot_size=3)\n\nap.save_overall_html(\n    dest_dir_path=\'circle_line_dot_setting/\')\n```':  # noqa
    '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    background_color=\'#333\',\n    stage_width=150,\n    stage_height=150,\n    stage_elem_id=\'stage\')\ncircle: ap.Circle = ap.Circle(\n    x=75, y=75, radius=50, line_color=\'0af\', line_thickness=3)\ncircle.line_dot_setting = ap.LineDotSetting(dot_size=3)\n\nap.save_overall_html(\n    dest_dir_path=\'circle_line_dot_setting/\')\n```',  # noqa

    '## line_dash_setting property interface example':
    '## line_dash_setting属性のインターフェイス例',

    'The `line_dash_setting` property updates or gets the instance\'s line dash-style setting:':  # noqa
    '`line_dash_setting`属性では破線のスタイル設定の更新もしくは取得を行えます:',

    '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    background_color=\'#333\',\n    stage_width=150,\n    stage_height=150,\n    stage_elem_id=\'stage\')\ncircle: ap.Circle = ap.Circle(\n    x=75, y=75, radius=50, line_color=\'0af\', line_thickness=3)\ncircle.line_dash_setting = ap.LineDashSetting(\n    dash_size=5, space_size=2)\n\nap.save_overall_html(\n    dest_dir_path=\'circle_line_dash_setting/\')\n```':  # noqa
    '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    background_color=\'#333\',\n    stage_width=150,\n    stage_height=150,\n    stage_elem_id=\'stage\')\ncircle: ap.Circle = ap.Circle(\n    x=75, y=75, radius=50, line_color=\'0af\', line_thickness=3)\ncircle.line_dash_setting = ap.LineDashSetting(\n    dash_size=5, space_size=2)\n\nap.save_overall_html(\n    dest_dir_path=\'circle_line_dash_setting/\')\n```',  # noqa

    '## line_round_dot_setting property interface example':
    '## line_round_dot_setting属性のインターフェイス例',

    'The `line_round_dot_setting` property updates or gets the instance\'s line round dot-style setting:':  # noqa
    '`line_round_dot_setting`属性では丸ドット線のスタイル設定の更新もしくは取得を行えます:',

    '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    background_color=\'#333\',\n    stage_width=150,\n    stage_height=150,\n    stage_elem_id=\'stage\')\ncircle: ap.Circle = ap.Circle(\n    x=75, y=75, radius=50, line_color=\'0af\')\ncircle.line_round_dot_setting = ap.LineRoundDotSetting(\n    round_size=5, space_size=3)\n\nap.save_overall_html(\n    dest_dir_path=\'circle_line_round_dot_setting/\')\n```':  # noqa
    '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    background_color=\'#333\',\n    stage_width=150,\n    stage_height=150,\n    stage_elem_id=\'stage\')\ncircle: ap.Circle = ap.Circle(\n    x=75, y=75, radius=50, line_color=\'0af\')\ncircle.line_round_dot_setting = ap.LineRoundDotSetting(\n    round_size=5, space_size=3)\n\nap.save_overall_html(\n    dest_dir_path=\'circle_line_round_dot_setting/\')\n```',  # noqa

    '## line_dash_dot_setting property interface example':
    '## line_dash_dot_setting属性のインターフェイス例',

    'The `line_dash_dot_setting` property updates or gets the instance\'s dash-dotted line style setting:':  # noqa
    '`line_dash_dot_setting`属性では一点鎖線のスタイル設定の更新もしくは取得を行えます:',

    '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    background_color=\'#333\',\n    stage_width=150,\n    stage_height=150,\n    stage_elem_id=\'stage\')\ncircle: ap.Circle = ap.Circle(\n    x=75, y=75, radius=50, line_color=\'0af\', line_thickness=3)\ncircle.line_dash_dot_setting = ap.LineDashDotSetting(\n    dot_size=3, dash_size=6, space_size=3)\n\nap.save_overall_html(\n    dest_dir_path=\'circle_line_dash_dot_setting/\')\n```':  # noqa
    '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    background_color=\'#333\',\n    stage_width=150,\n    stage_height=150,\n    stage_elem_id=\'stage\')\ncircle: ap.Circle = ap.Circle(\n    x=75, y=75, radius=50, line_color=\'0af\', line_thickness=3)\ncircle.line_dash_dot_setting = ap.LineDashDotSetting(\n    dot_size=3, dash_size=6, space_size=3)\n\nap.save_overall_html(\n    dest_dir_path=\'circle_line_dash_dot_setting/\')\n```',  # noqa

}
