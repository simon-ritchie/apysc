"""This module is for the translation mapping data of the
following document:

Document file: polygon.md
Language: jp
"""

from typing import Dict

MAPPING: Dict[str, str] = {

    '# Polygon class':
    '# Polygon クラス',

    'This page explains the `Polygon` class.':
    'このページでは`Polygon`クラスについて説明します。',

    '## What class is this?':
    '## クラス概要',

    'The `Polygon` class creates a polygon vector graphics object.':
    '`Polygon`クラスは多角形のベクターグラフィックスを生成します。',

    '## Basic usage':
    '## 基本的な使い方',

    'The `Polygon` class constructor requires the `points` list argument.':
    '`Polygon`クラスのコンストラクタでは`points`のリストの引数の指定が必要となります。',

    'The constructor also accepts each style\'s argument, such as the `fill_color`.':  # noqa
    'コンストラクタでは他の`fill_color`などのスタイル設定の各引数も受け付けます。',

    '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    background_color=\'#333\',\n    stage_width=150,\n    stage_height=150,\n    stage_elem_id=\'stage\')\npolygon: ap.Polygon = ap.Polygon(\n    points=[\n        ap.Point2D(x=75, y=50),\n        ap.Point2D(x=50, y=100),\n        ap.Point2D(x=100, y=100),\n    ],\n    fill_color=\'#0af\')\n\nap.save_overall_html(\n    dest_dir_path=\'polygon_basic_usage/\')\n```':  # noqa
    '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    background_color=\'#333\',\n    stage_width=150,\n    stage_height=150,\n    stage_elem_id=\'stage\')\npolygon: ap.Polygon = ap.Polygon(\n    points=[\n        ap.Point2D(x=75, y=50),\n        ap.Point2D(x=50, y=100),\n        ap.Point2D(x=100, y=100),\n    ],\n    fill_color=\'#0af\')\n\nap.save_overall_html(\n    dest_dir_path=\'polygon_basic_usage/\')\n```',  # noqa

    '## Note of the draw_polygon interface':
    '## draw_polygon インターフェイスにおける特記事項',

    'You can also create a polygon instance with the `draw_polygon` interface.':  # noqa
    '`draw_polygon`インターフェイスを使う形でも多角形のインスタンスを生成することができます。',

    'Please see also:':
    '関連資料:',

    '- [Graphics class draw_polygon interface](graphics_draw_polygon.md)':
    '- [Graphics クラスの draw_polygon (多角形描画)のインターフェイス](jp_graphics_draw_polygon.md)',  # noqa

    '## x property interface example':
    '## x属性のインターフェイス例',

    'The `x` property updates or gets the instance\'s x-coordinate:':
    '`x`属性ではX座標の値の更新もしくは取得を行えます:',

    '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    background_color=\'#333\',\n    stage_width=150,\n    stage_height=150,\n    stage_elem_id=\'stage\')\npolygon: ap.Polygon = ap.Polygon(\n    points=[\n        ap.Point2D(x=75, y=50),\n        ap.Point2D(x=50, y=100),\n        ap.Point2D(x=100, y=100),\n    ],\n    fill_color=\'#0af\')\npolygon.x = ap.Int(100)\n\nap.save_overall_html(\n    dest_dir_path=\'polygon_x/\')\n```':  # noqa
    '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    background_color=\'#333\',\n    stage_width=150,\n    stage_height=150,\n    stage_elem_id=\'stage\')\npolygon: ap.Polygon = ap.Polygon(\n    points=[\n        ap.Point2D(x=75, y=50),\n        ap.Point2D(x=50, y=100),\n        ap.Point2D(x=100, y=100),\n    ],\n    fill_color=\'#0af\')\npolygon.x = ap.Int(100)\n\nap.save_overall_html(\n    dest_dir_path=\'polygon_x/\')\n```',  # noqa

    'Notes: this attribute\'s value becomes the same as the arguments\' minimum point value.':  # noqa
    '特記事項: この属性の値は引数の座標の最小値と同値になります。',

    '## y property interface example':
    '## y属性のインターフェイス例',

    'The `y` property updates or gets the instance\'s y-coordinate:':
    '`y`属性ではY座標の値の更新もしくは取得を行えます:',

    '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    background_color=\'#333\',\n    stage_width=150,\n    stage_height=150,\n    stage_elem_id=\'stage\')\npolygon: ap.Polygon = ap.Polygon(\n    points=[\n        ap.Point2D(x=75, y=50),\n        ap.Point2D(x=50, y=100),\n        ap.Point2D(x=100, y=100),\n    ],\n    fill_color=\'#0af\')\npolygon.y = ap.Int(100)\n\nap.save_overall_html(\n    dest_dir_path=\'polygon_y/\')\n```':  # noqa
    '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    background_color=\'#333\',\n    stage_width=150,\n    stage_height=150,\n    stage_elem_id=\'stage\')\npolygon: ap.Polygon = ap.Polygon(\n    points=[\n        ap.Point2D(x=75, y=50),\n        ap.Point2D(x=50, y=100),\n        ap.Point2D(x=100, y=100),\n    ],\n    fill_color=\'#0af\')\npolygon.y = ap.Int(100)\n\nap.save_overall_html(\n    dest_dir_path=\'polygon_y/\')\n```',  # noqa

    'Notes: this attribute\'s value becomes the same as the arguments\' minimum point value.':  # noqa
    '特記事項: この属性の値は引数の座標の最小値と同値になります。',

    '## fill_color property interface example':
    '## fill_color属性のインターフェイス例',

    'The `fill_color` property updates or gets the instance\'s fill color:':
    '`fill_color`属性は塗りの色の値の更新もしくは取得を行えます:',

    '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    background_color=\'#333\',\n    stage_width=150,\n    stage_height=150,\n    stage_elem_id=\'stage\')\npolygon: ap.Polygon = ap.Polygon(\n    points=[\n        ap.Point2D(x=75, y=50),\n        ap.Point2D(x=50, y=100),\n        ap.Point2D(x=100, y=100),\n    ])\npolygon.fill_color = ap.String(\'#f0a\')\n\nap.save_overall_html(\n    dest_dir_path=\'polygon_fill_color/\')\n```':  # noqa
    '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    background_color=\'#333\',\n    stage_width=150,\n    stage_height=150,\n    stage_elem_id=\'stage\')\npolygon: ap.Polygon = ap.Polygon(\n    points=[\n        ap.Point2D(x=75, y=50),\n        ap.Point2D(x=50, y=100),\n        ap.Point2D(x=100, y=100),\n    ])\npolygon.fill_color = ap.String(\'#f0a\')\n\nap.save_overall_html(\n    dest_dir_path=\'polygon_fill_color/\')\n```',  # noqa

    '## fill_alpha property interface example':
    '## fill_alpha属性のインターフェイス例',

    'The `fill_alpha` property updates or gets the instance\'s fill alpha (opacity):':  # noqa
    '`fill_alpha`属性は塗りの透明度の値の更新もしくは取得を行えます:',

    '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    background_color=\'#333\',\n    stage_width=150,\n    stage_height=150,\n    stage_elem_id=\'stage\')\npolygon: ap.Polygon = ap.Polygon(\n    points=[\n        ap.Point2D(x=75, y=50),\n        ap.Point2D(x=50, y=100),\n        ap.Point2D(x=100, y=100),\n    ],\n    fill_color=\'#0af\')\npolygon.fill_alpha = ap.Number(0.3)\n\nap.save_overall_html(\n    dest_dir_path=\'polygon_fill_alpha/\')\n```':  # noqa
    '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    background_color=\'#333\',\n    stage_width=150,\n    stage_height=150,\n    stage_elem_id=\'stage\')\npolygon: ap.Polygon = ap.Polygon(\n    points=[\n        ap.Point2D(x=75, y=50),\n        ap.Point2D(x=50, y=100),\n        ap.Point2D(x=100, y=100),\n    ],\n    fill_color=\'#0af\')\npolygon.fill_alpha = ap.Number(0.3)\n\nap.save_overall_html(\n    dest_dir_path=\'polygon_fill_alpha/\')\n```',  # noqa

    '## line_color property interface example':
    '## line_color属性のインターフェイス例',

    'The `line_color` property updates or gets the instance\'s line color:':
    '`line_color`属性では線の色の値の更新もしくは取得を行えます:',

    '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    background_color=\'#333\',\n    stage_width=150,\n    stage_height=150,\n    stage_elem_id=\'stage\')\npolygon: ap.Polygon = ap.Polygon(\n    points=[\n        ap.Point2D(x=75, y=50),\n        ap.Point2D(x=50, y=100),\n        ap.Point2D(x=100, y=100),\n    ],\n    line_thickness=5)\npolygon.line_color = ap.String(\'#0af\')\n\nap.save_overall_html(\n    dest_dir_path=\'polygon_line_color/\')\n```':  # noqa
    '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    background_color=\'#333\',\n    stage_width=150,\n    stage_height=150,\n    stage_elem_id=\'stage\')\npolygon: ap.Polygon = ap.Polygon(\n    points=[\n        ap.Point2D(x=75, y=50),\n        ap.Point2D(x=50, y=100),\n        ap.Point2D(x=100, y=100),\n    ],\n    line_thickness=5)\npolygon.line_color = ap.String(\'#0af\')\n\nap.save_overall_html(\n    dest_dir_path=\'polygon_line_color/\')\n```',  # noqa

    '## line_alpha property interface example':
    '## line_alpha属性のインターフェイス例',

    'The `line_alpha` property updates or gets the instance\'s line alpha (opacity):':  # noqa
    '`line_alpha`属性では線の透明度の値の更新もしくは取得を行えます:',

    '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    background_color=\'#333\',\n    stage_width=150,\n    stage_height=150,\n    stage_elem_id=\'stage\')\npolygon: ap.Polygon = ap.Polygon(\n    points=[\n        ap.Point2D(x=75, y=50),\n        ap.Point2D(x=50, y=100),\n        ap.Point2D(x=100, y=100),\n    ],\n    line_color=\'#0af\',\n    line_thickness=5)\npolygon.line_alpha = ap.Number(0.3)\n\nap.save_overall_html(\n    dest_dir_path=\'polygon_line_alpha/\')\n```':  # noqa
    '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    background_color=\'#333\',\n    stage_width=150,\n    stage_height=150,\n    stage_elem_id=\'stage\')\npolygon: ap.Polygon = ap.Polygon(\n    points=[\n        ap.Point2D(x=75, y=50),\n        ap.Point2D(x=50, y=100),\n        ap.Point2D(x=100, y=100),\n    ],\n    line_color=\'#0af\',\n    line_thickness=5)\npolygon.line_alpha = ap.Number(0.3)\n\nap.save_overall_html(\n    dest_dir_path=\'polygon_line_alpha/\')\n```',  # noqa

    '## line_thickness property interface example':
    '## line_thickness属性のインターフェイス例',

    'The `line_thickness` property updates or gets the instance\'s line thickness (line width):':  # noqa
    '`line_thickness`属性では線の幅の更新もしくは取得を行えます:',

    '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    background_color=\'#333\',\n    stage_width=150,\n    stage_height=150,\n    stage_elem_id=\'stage\')\npolygon: ap.Polygon = ap.Polygon(\n    points=[\n        ap.Point2D(x=75, y=50),\n        ap.Point2D(x=50, y=100),\n        ap.Point2D(x=100, y=100),\n    ],\n    line_color=\'#0af\')\npolygon.line_thickness = ap.Int(8)\n\nap.save_overall_html(\n    dest_dir_path=\'polygon_line_thickness/\')\n```':  # noqa
    '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    background_color=\'#333\',\n    stage_width=150,\n    stage_height=150,\n    stage_elem_id=\'stage\')\npolygon: ap.Polygon = ap.Polygon(\n    points=[\n        ap.Point2D(x=75, y=50),\n        ap.Point2D(x=50, y=100),\n        ap.Point2D(x=100, y=100),\n    ],\n    line_color=\'#0af\')\npolygon.line_thickness = ap.Int(8)\n\nap.save_overall_html(\n    dest_dir_path=\'polygon_line_thickness/\')\n```',  # noqa

    '## line_dot_setting property interface example':
    '## line_dot_setting属性のインターフェイス例',

    'The `line_dot_setting` property updates or gets the instance\'s line dot-style setting:':  # noqa
    '`line_dot_setting`属性では点線のスタイル設定の更新もしくは取得を行えます:',

    '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    background_color=\'#333\',\n    stage_width=150,\n    stage_height=150,\n    stage_elem_id=\'stage\')\npolygon: ap.Polygon = ap.Polygon(\n    points=[\n        ap.Point2D(x=75, y=50),\n        ap.Point2D(x=50, y=100),\n        ap.Point2D(x=100, y=100),\n    ],\n    line_color=\'#0af\',\n    line_thickness=2)\npolygon.line_dot_setting = ap.LineDotSetting(dot_size=2)\n\nap.save_overall_html(\n    dest_dir_path=\'polygon_line_dot_setting/\')\n```':  # noqa
    '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    background_color=\'#333\',\n    stage_width=150,\n    stage_height=150,\n    stage_elem_id=\'stage\')\npolygon: ap.Polygon = ap.Polygon(\n    points=[\n        ap.Point2D(x=75, y=50),\n        ap.Point2D(x=50, y=100),\n        ap.Point2D(x=100, y=100),\n    ],\n    line_color=\'#0af\',\n    line_thickness=2)\npolygon.line_dot_setting = ap.LineDotSetting(dot_size=2)\n\nap.save_overall_html(\n    dest_dir_path=\'polygon_line_dot_setting/\')\n```',  # noqa

    '## line_dash_setting property interface example':
    '## line_dash_setting属性のインターフェイス例',

    'The `line_dash_setting` property updates or gets the instance\'s line dash-style setting:':  # noqa
    '`line_dash_setting`属性では破線のスタイル設定の更新もしくは取得を行えます:',

    '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    background_color=\'#333\',\n    stage_width=150,\n    stage_height=150,\n    stage_elem_id=\'stage\')\npolygon: ap.Polygon = ap.Polygon(\n    points=[\n        ap.Point2D(x=75, y=50),\n        ap.Point2D(x=50, y=100),\n        ap.Point2D(x=100, y=100),\n    ],\n    line_color=\'#0af\',\n    line_thickness=2)\npolygon.line_dash_setting = ap.LineDashSetting(\n    dash_size=5, space_size=2)\n\nap.save_overall_html(\n    dest_dir_path=\'polygon_line_dash_setting/\')\n```':  # noqa
    '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    background_color=\'#333\',\n    stage_width=150,\n    stage_height=150,\n    stage_elem_id=\'stage\')\npolygon: ap.Polygon = ap.Polygon(\n    points=[\n        ap.Point2D(x=75, y=50),\n        ap.Point2D(x=50, y=100),\n        ap.Point2D(x=100, y=100),\n    ],\n    line_color=\'#0af\',\n    line_thickness=2)\npolygon.line_dash_setting = ap.LineDashSetting(\n    dash_size=5, space_size=2)\n\nap.save_overall_html(\n    dest_dir_path=\'polygon_line_dash_setting/\')\n```',  # noqa

    '## line_round_dot_setting property interface example':
    '## line_round_dot_setting属性のインターフェイス例',

    'The `line_round_dot_setting` property updates or gets the instance\'s line round dot-style setting:':  # noqa
    '`line_round_dot_setting`属性では丸ドット線のスタイル設定の更新もしくは取得を行えます:',

    '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    background_color=\'#333\',\n    stage_width=150,\n    stage_height=150,\n    stage_elem_id=\'stage\')\npolygon: ap.Polygon = ap.Polygon(\n    points=[\n        ap.Point2D(x=75, y=50),\n        ap.Point2D(x=50, y=100),\n        ap.Point2D(x=100, y=100),\n    ],\n    line_color=\'#0af\')\npolygon.line_round_dot_setting = ap.LineRoundDotSetting(\n    round_size=4, space_size=3)\n\nap.save_overall_html(\n    dest_dir_path=\'polygon_line_round_dot_setting/\')\n```':  # noqa
    '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    background_color=\'#333\',\n    stage_width=150,\n    stage_height=150,\n    stage_elem_id=\'stage\')\npolygon: ap.Polygon = ap.Polygon(\n    points=[\n        ap.Point2D(x=75, y=50),\n        ap.Point2D(x=50, y=100),\n        ap.Point2D(x=100, y=100),\n    ],\n    line_color=\'#0af\')\npolygon.line_round_dot_setting = ap.LineRoundDotSetting(\n    round_size=4, space_size=3)\n\nap.save_overall_html(\n    dest_dir_path=\'polygon_line_round_dot_setting/\')\n```',  # noqa

    '## line_dash_dot_setting property interface example':
    '## line_dash_dot_setting属性のインターフェイス例',

    'The `line_dash_dot_setting` property updates or gets the instance\'s dash-dotted line style setting:':  # noqa
    '`line_dash_dot_setting`属性では一点鎖線のスタイル設定の更新もしくは取得を行えます:',

    '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    background_color=\'#333\',\n    stage_width=150,\n    stage_height=150,\n    stage_elem_id=\'stage\')\npolygon: ap.Polygon = ap.Polygon(\n    points=[\n        ap.Point2D(x=75, y=50),\n        ap.Point2D(x=50, y=100),\n        ap.Point2D(x=100, y=100),\n    ],\n    line_color=\'#0af\')\npolygon.line_dash_dot_setting = ap.LineDashDotSetting(\n    dot_size=2, dash_size=5, space_size=2)\n\nap.save_overall_html(\n    dest_dir_path=\'polygon_line_dash_dot_setting/\')\n```':  # noqa
    '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    background_color=\'#333\',\n    stage_width=150,\n    stage_height=150,\n    stage_elem_id=\'stage\')\npolygon: ap.Polygon = ap.Polygon(\n    points=[\n        ap.Point2D(x=75, y=50),\n        ap.Point2D(x=50, y=100),\n        ap.Point2D(x=100, y=100),\n    ],\n    line_color=\'#0af\')\npolygon.line_dash_dot_setting = ap.LineDashDotSetting(\n    dot_size=2, dash_size=5, space_size=2)\n\nap.save_overall_html(\n    dest_dir_path=\'polygon_line_dash_dot_setting/\')\n```',  # noqa

}
