"""This module is for the translation mapping data of the
following document:

Document file: line.md
Language: jp
"""

from typing import Dict

MAPPING: Dict[str, str] = {

    '# Line class':
    '# Line クラス',

    'This page explains the `Line` class.':
    'このページでは`Line`クラスについて説明します。',

    '## What class is this?':
    '## クラス概要',

    'The `Line` class creates a straight-line vector graphics object.':
    '`Line`クラスは直線のベクターグラフィックスを生成します。',

    '## Basic usage':
    '## 基本的な使い方',

    'The `Line` class constructor requires the `start_point` and `end_point` arguments.':  # noqa
    '`Line`クラスのコンストラクタでは`start_point`や`end_point`の引数指定を必要とします。',

    'The constructor also accepts each style\'s argument, such as the `line_color`.':  # noqa
    'コンストラクタは`line_color`などのスタイル設定の引数も受け付けます。',

    '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    background_color=\'#333\',\n    stage_width=200,\n    stage_height=100,\n    stage_elem_id=\'stage\')\nline: ap.Line = ap.Line(\n    start_point=ap.Point2D(x=50, y=50),\n    end_point=ap.Point2D(x=150, y=50),\n    line_color=\'#0af\', line_thickness=5)\n\nap.save_overall_html(\n    dest_dir_path=\'line_basic_usage/\')\n```':  # noqa
    '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    background_color=\'#333\',\n    stage_width=200,\n    stage_height=100,\n    stage_elem_id=\'stage\')\nline: ap.Line = ap.Line(\n    start_point=ap.Point2D(x=50, y=50),\n    end_point=ap.Point2D(x=150, y=50),\n    line_color=\'#0af\', line_thickness=5)\n\nap.save_overall_html(\n    dest_dir_path=\'line_basic_usage/\')\n```',  # noqa

    '## Note of the draw_line or other interfaces':
    '## draw_line や他の各インターフェイスの特記事項',

    'You can also create a line instance with the `draw_line` interface (or the other interfaces, such as the `draw_dotted_line`).':  # noqa
    '`draw_line`や`draw_dotted_line`などの他のインターフェイスを使う形でも直線のインスタンスを生成することができます。',  # noqa

    'Please see also:':
    '関連資料:',

    '- [Graphics class draw_line interface](graphics_draw_line.md)':
    '- [Graphics クラスの draw_line (線の描画)のインターフェイス](jp_graphics_draw_line.md)',

    '- [Graphics class draw_dotted_line interface](graphics_draw_dotted_line.md)':  # noqa
    '- [Graphics クラスの draw_dotted_line (点線の描画)のインターフェイス](jp_graphics_draw_dotted_line.md)',  # noqa

    '- [Graphics class draw_dashed_line interface](graphics_draw_dashed_line.md)':  # noqa
    '- [Graphics クラスの draw_dashed_line (破線の描画)のインターフェイス](jp_graphics_draw_dashed_line.md)',  # noqa

    '- [Graphics class draw_round_dotted_line interface](graphics_draw_round_dotted_line.md)':  # noqa
    '- [Graphics クラスの draw_round_dotted_line (点線(丸)の描画)のインターフェイス](jp_graphics_draw_round_dotted_line.md)',  # noqa

    '- [Graphics class draw_dash_dotted_line interface](graphics_draw_dash_dotted_line.md)':  # noqa
    '- [Graphics クラスの draw_dash_dotted_line (一点鎖線の描画)のインターフェイス](jp_graphics_draw_dash_dotted_line.md)',  # noqa

    '## x property interface example':
    '## x属性のインターフェイス例',

    'The `x` property updates or gets the instance\'s x-coordinate:':
    '`x`属性ではX座標の値の更新もしくは取得を行えます:',

    '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    background_color=\'#333\',\n    stage_width=200,\n    stage_height=100,\n    stage_elem_id=\'stage\')\nline: ap.Line = ap.Line(\n    start_point=ap.Point2D(x=50, y=50),\n    end_point=ap.Point2D(x=150, y=50),\n    line_color=\'#0af\', line_thickness=5)\nline.x = ap.Int(100)\n\nap.save_overall_html(\n    dest_dir_path=\'line_x/\')\n```':  # noqa
    '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    background_color=\'#333\',\n    stage_width=200,\n    stage_height=100,\n    stage_elem_id=\'stage\')\nline: ap.Line = ap.Line(\n    start_point=ap.Point2D(x=50, y=50),\n    end_point=ap.Point2D(x=150, y=50),\n    line_color=\'#0af\', line_thickness=5)\nline.x = ap.Int(100)\n\nap.save_overall_html(\n    dest_dir_path=\'line_x/\')\n```',  # noqa

    'Notes: this attribute\'s value becomes the same as the arguments\' minimum point value.':  # noqa
    '特記事項: この属性の値は引数の座標の最小値と同値になります。',

    '## y property interface example':
    '## y属性のインターフェイス例',

    'The `y` property updates or gets the instance\'s y-coordinate:':
    '`y`属性ではY座標の値の更新もしくは取得を行えます:',

    '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    background_color=\'#333\',\n    stage_width=200,\n    stage_height=100,\n    stage_elem_id=\'stage\')\nline: ap.Line = ap.Line(\n    start_point=ap.Point2D(x=50, y=50),\n    end_point=ap.Point2D(x=150, y=50),\n    line_color=\'#0af\', line_thickness=5)\nline.y = ap.Int(80)\n\nap.save_overall_html(\n    dest_dir_path=\'line_y/\')\n```':  # noqa
    '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    background_color=\'#333\',\n    stage_width=200,\n    stage_height=100,\n    stage_elem_id=\'stage\')\nline: ap.Line = ap.Line(\n    start_point=ap.Point2D(x=50, y=50),\n    end_point=ap.Point2D(x=150, y=50),\n    line_color=\'#0af\', line_thickness=5)\nline.y = ap.Int(80)\n\nap.save_overall_html(\n    dest_dir_path=\'line_y/\')\n```',  # noqa

    'Notes: this attribute\'s value becomes the same as the arguments\' minimum point value.':  # noqa
    '特記事項: この属性の値は引数の座標の最小値と同値になります。',

    '## line_color property interface example':
    '## line_color属性のインターフェイス例',

    'The `line_color` property updates or gets the instance\'s line color:':
    '`line_color`属性では線の色の値の更新もしくは取得を行えます:',

    '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    background_color=\'#333\',\n    stage_width=200,\n    stage_height=100,\n    stage_elem_id=\'stage\')\nline: ap.Line = ap.Line(\n    start_point=ap.Point2D(x=50, y=50),\n    end_point=ap.Point2D(x=150, y=50), line_thickness=5)\nline.line_color = ap.String(\'#f0a\')\n\nap.save_overall_html(\n    dest_dir_path=\'line_line_color/\')\n```':  # noqa
    '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    background_color=\'#333\',\n    stage_width=200,\n    stage_height=100,\n    stage_elem_id=\'stage\')\nline: ap.Line = ap.Line(\n    start_point=ap.Point2D(x=50, y=50),\n    end_point=ap.Point2D(x=150, y=50), line_thickness=5)\nline.line_color = ap.String(\'#f0a\')\n\nap.save_overall_html(\n    dest_dir_path=\'line_line_color/\')\n```',  # noqa

    '## line_alpha property interface example':
    '## line_alpha属性のインターフェイス例',

    'The `line_alpha` property updates or gets the instance\'s line alpha (opacity):':  # noqa
    '`line_alpha`属性では線の透明度の値の更新もしくは取得を行えます:',

    '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    background_color=\'#333\',\n    stage_width=200,\n    stage_height=100,\n    stage_elem_id=\'stage\')\nline: ap.Line = ap.Line(\n    start_point=ap.Point2D(x=50, y=50),\n    end_point=ap.Point2D(x=150, y=50),\n    line_color=\'#0af\', line_thickness=5)\nline.line_alpha = ap.Number(0.3)\n\nap.save_overall_html(\n    dest_dir_path=\'line_line_alpha/\')\n```':  # noqa
    '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    background_color=\'#333\',\n    stage_width=200,\n    stage_height=100,\n    stage_elem_id=\'stage\')\nline: ap.Line = ap.Line(\n    start_point=ap.Point2D(x=50, y=50),\n    end_point=ap.Point2D(x=150, y=50),\n    line_color=\'#0af\', line_thickness=5)\nline.line_alpha = ap.Number(0.3)\n\nap.save_overall_html(\n    dest_dir_path=\'line_line_alpha/\')\n```',  # noqa

    '## line_thickness property interface example':
    '## line_thickness属性のインターフェイス例',

    'The `line_thickness` property updates or gets the instance\'s line thickness (line width):':  # noqa
    '`line_thickness`属性では線の幅の更新もしくは取得を行えます:',

    '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    background_color=\'#333\',\n    stage_width=200,\n    stage_height=100,\n    stage_elem_id=\'stage\')\nline: ap.Line = ap.Line(\n    start_point=ap.Point2D(x=50, y=50),\n    end_point=ap.Point2D(x=150, y=50),\n    line_color=\'#0af\')\nline.line_thickness = ap.Int(10)\n\nap.save_overall_html(\n    dest_dir_path=\'line_line_thickness/\')\n```':  # noqa
    '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    background_color=\'#333\',\n    stage_width=200,\n    stage_height=100,\n    stage_elem_id=\'stage\')\nline: ap.Line = ap.Line(\n    start_point=ap.Point2D(x=50, y=50),\n    end_point=ap.Point2D(x=150, y=50),\n    line_color=\'#0af\')\nline.line_thickness = ap.Int(10)\n\nap.save_overall_html(\n    dest_dir_path=\'line_line_thickness/\')\n```',  # noqa

    '## line_dot_setting property interface example':
    '## line_dot_setting属性のインターフェイス例',

    'The `line_dot_setting` property updates or gets the instance\'s line dot-style setting:':  # noqa
    '`line_dot_setting`属性では点線のスタイル設定の更新もしくは取得を行えます:',

    '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    background_color=\'#333\',\n    stage_width=200,\n    stage_height=100,\n    stage_elem_id=\'stage\')\nline: ap.Line = ap.Line(\n    start_point=ap.Point2D(x=50, y=50),\n    end_point=ap.Point2D(x=150, y=50),\n    line_color=\'#0af\', line_thickness=3)\nline.line_dot_setting = ap.LineDotSetting(dot_size=3)\n\nap.save_overall_html(\n    dest_dir_path=\'line_line_dot_setting/\')\n```':  # noqa
    '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    background_color=\'#333\',\n    stage_width=200,\n    stage_height=100,\n    stage_elem_id=\'stage\')\nline: ap.Line = ap.Line(\n    start_point=ap.Point2D(x=50, y=50),\n    end_point=ap.Point2D(x=150, y=50),\n    line_color=\'#0af\', line_thickness=3)\nline.line_dot_setting = ap.LineDotSetting(dot_size=3)\n\nap.save_overall_html(\n    dest_dir_path=\'line_line_dot_setting/\')\n```',  # noqa

    '## line_dash_setting property interface example':
    '## line_dash_setting属性のインターフェイス例',

    'The `line_dash_setting` property updates or gets the instance\'s line dash-style setting:':  # noqa
    '`line_dash_setting`属性では破線のスタイル設定の更新もしくは取得を行えます:',

    '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    background_color=\'#333\',\n    stage_width=200,\n    stage_height=100,\n    stage_elem_id=\'stage\')\nline: ap.Line = ap.Line(\n    start_point=ap.Point2D(x=50, y=50),\n    end_point=ap.Point2D(x=150, y=50),\n    line_color=\'#0af\', line_thickness=3)\nline.line_dash_setting = ap.LineDashSetting(\n    dash_size=6, space_size=2)\n\nap.save_overall_html(\n    dest_dir_path=\'line_line_dash_setting/\')\n```':  # noqa
    '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    background_color=\'#333\',\n    stage_width=200,\n    stage_height=100,\n    stage_elem_id=\'stage\')\nline: ap.Line = ap.Line(\n    start_point=ap.Point2D(x=50, y=50),\n    end_point=ap.Point2D(x=150, y=50),\n    line_color=\'#0af\', line_thickness=3)\nline.line_dash_setting = ap.LineDashSetting(\n    dash_size=6, space_size=2)\n\nap.save_overall_html(\n    dest_dir_path=\'line_line_dash_setting/\')\n```',  # noqa

    '## line_round_dot_setting property interface example':
    '## line_round_dot_setting属性のインターフェイス例',

    'The `line_round_dot_setting` property updates or gets the instance\'s line round dot-style setting:':  # noqa
    '`line_round_dot_setting`属性では丸ドット線のスタイル設定の更新もしくは取得を行えます:',

    '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    background_color=\'#333\',\n    stage_width=200,\n    stage_height=100,\n    stage_elem_id=\'stage\')\nline: ap.Line = ap.Line(\n    start_point=ap.Point2D(x=50, y=50),\n    end_point=ap.Point2D(x=150, y=50),\n    line_color=\'#0af\')\nline.line_round_dot_setting = ap.LineRoundDotSetting(\n    round_size=5, space_size=3)\n\nap.save_overall_html(\n    dest_dir_path=\'line_line_round_dot_setting/\')\n```':  # noqa
    '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    background_color=\'#333\',\n    stage_width=200,\n    stage_height=100,\n    stage_elem_id=\'stage\')\nline: ap.Line = ap.Line(\n    start_point=ap.Point2D(x=50, y=50),\n    end_point=ap.Point2D(x=150, y=50),\n    line_color=\'#0af\')\nline.line_round_dot_setting = ap.LineRoundDotSetting(\n    round_size=5, space_size=3)\n\nap.save_overall_html(\n    dest_dir_path=\'line_line_round_dot_setting/\')\n```',  # noqa

    '## line_dash_dot_setting property interface example':
    '## line_dash_dot_setting属性のインターフェイス例',

    'The `line_dash_dot_setting` property updates or gets the instance\'s dash-dotted line style setting:':  # noqa
    '`line_dash_dot_setting`属性では一点鎖線のスタイル設定の更新もしくは取得を行えます:',

    '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    background_color=\'#333\',\n    stage_width=200,\n    stage_height=100,\n    stage_elem_id=\'stage\')\nline: ap.Line = ap.Line(\n    start_point=ap.Point2D(x=50, y=50),\n    end_point=ap.Point2D(x=150, y=50),\n    line_color=\'#0af\', line_thickness=3)\nline.line_dash_dot_setting = ap.LineDashDotSetting(\n    dot_size=2, dash_size=5, space_size=2)\n\nap.save_overall_html(\n    dest_dir_path=\'line_line_dash_dot_setting/\')\n```':  # noqa
    '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    background_color=\'#333\',\n    stage_width=200,\n    stage_height=100,\n    stage_elem_id=\'stage\')\nline: ap.Line = ap.Line(\n    start_point=ap.Point2D(x=50, y=50),\n    end_point=ap.Point2D(x=150, y=50),\n    line_color=\'#0af\', line_thickness=3)\nline.line_dash_dot_setting = ap.LineDashDotSetting(\n    dot_size=2, dash_size=5, space_size=2)\n\nap.save_overall_html(\n    dest_dir_path=\'line_line_dash_dot_setting/\')\n```',  # noqa

}
