"""This module is for the translation mapping data of the
following document:

Document file: rectangle.md
Language: jp
"""

from typing import Dict

MAPPING: Dict[str, str] = {

    '# Rectangle class':
    '# Rectangle クラス',

    'This page explains the `Rectangle` class.':
    'このページでは`Rectangle`クラスについて説明します。',

    '## What class is this?':
    '## クラス概要',

    'The `Rectangle` class creates a rectangle vector graphics object.':
    '`Rectangle`クラスは四角のベクターグラフィックスを生成します。',

    '## Basic usage':
    '## 基本的な使い方',

    'The `Rectangle` class constructor requires the `x`, `y`, `width`, and `height` arguments.':  # noqa
    '`Rectangle`クラスのコンストラクタでは`x`、`y`、`width`、`height`の引数指定が必要になります。',

    'The constructor also accepts each style\'s argument, such as the `fill_color`.':  # noqa
    'コンストラクタでは他にも`fill_color`などのスタイル設定の引数を受け付けます。',

    '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    background_color=\'#333\',\n    stage_width=200,\n    stage_height=150,\n    stage_elem_id=\'stage\')\nrectangle: ap.Rectangle = ap.Rectangle(\n    x=50, y=50, width=100, height=50,\n    fill_color=\'#0af\')\n\nap.save_overall_html(\n    dest_dir_path=\'rectangle_basic_usage/\')\n```':  # noqa
    '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    background_color=\'#333\',\n    stage_width=200,\n    stage_height=150,\n    stage_elem_id=\'stage\')\nrectangle: ap.Rectangle = ap.Rectangle(\n    x=50, y=50, width=100, height=50,\n    fill_color=\'#0af\')\n\nap.save_overall_html(\n    dest_dir_path=\'rectangle_basic_usage/\')\n```',  # noqa

    '## Note of the draw_rect interface':
    '## draw_rect インターフェイスに対する特記事項',

    'You can also create a rectangle instance with the `draw_rect` interface.':  # noqa
    '`draw_rect`インターフェイスを使っても四角のインスタンスを生成することができます。',

    'Please see also:':
    '関連資料:',

    '- [Graphics class draw_rect interface](graphics_draw_rect.md)':
    '- [Graphics クラスの draw_rect (四角の描画)のインターフェイス](jp_graphics_draw_rect.md)',  # noqa

    '## x property interface example':
    '## x属性のインターフェイス例',

    'The `x` property updates or gets the instance\'s x-coordinate:':
    '`x`属性ではX座標の値の更新もしくは取得を行えます:',

    '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    background_color=\'#333\',\n    stage_width=200,\n    stage_height=150,\n    stage_elem_id=\'stage\')\nrectangle: ap.Rectangle = ap.Rectangle(\n    x=0, y=50, width=50, height=50,\n    fill_color=\'#0af\')\nrectangle.x = ap.Int(100)\n\nap.save_overall_html(\n    dest_dir_path=\'rectangle_x/\')\n```':  # noqa
    '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    background_color=\'#333\',\n    stage_width=200,\n    stage_height=150,\n    stage_elem_id=\'stage\')\nrectangle: ap.Rectangle = ap.Rectangle(\n    x=0, y=50, width=50, height=50,\n    fill_color=\'#0af\')\nrectangle.x = ap.Int(100)\n\nap.save_overall_html(\n    dest_dir_path=\'rectangle_x/\')\n```',  # noqa

    '## y property interface example':
    '## y属性のインターフェイス例',

    'The `y` property updates or gets the instance\'s y-coordinate:':
    '`y`属性ではY座標の値の更新もしくは取得を行えます:',

    '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    background_color=\'#333\',\n    stage_width=150,\n    stage_height=200,\n    stage_elem_id=\'stage\')\nrectangle: ap.Rectangle = ap.Rectangle(\n    x=50, y=0, width=50, height=50,\n    fill_color=\'#0af\')\nrectangle.y = ap.Int(100)\n\nap.save_overall_html(\n    dest_dir_path=\'rectangle_y/\')\n```':  # noqa
    '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    background_color=\'#333\',\n    stage_width=150,\n    stage_height=200,\n    stage_elem_id=\'stage\')\nrectangle: ap.Rectangle = ap.Rectangle(\n    x=50, y=0, width=50, height=50,\n    fill_color=\'#0af\')\nrectangle.y = ap.Int(100)\n\nap.save_overall_html(\n    dest_dir_path=\'rectangle_y/\')\n```',  # noqa

    '## width property interface example':
    '## width属性のインターフェイス例',

    'The `width` property updates or gets the instance\'s width:':
    '`width`属性では幅の値の更新もしくは取得を行えます:',

    '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    background_color=\'#333\',\n    stage_width=200,\n    stage_height=150,\n    stage_elem_id=\'stage\')\nrectangle: ap.Rectangle = ap.Rectangle(\n    x=50, y=50, width=50, height=50,\n    fill_color=\'#0af\')\nrectangle.width = ap.Int(100)\n\nap.save_overall_html(\n    dest_dir_path=\'rectangle_width/\')\n```':  # noqa
    '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    background_color=\'#333\',\n    stage_width=200,\n    stage_height=150,\n    stage_elem_id=\'stage\')\nrectangle: ap.Rectangle = ap.Rectangle(\n    x=50, y=50, width=50, height=50,\n    fill_color=\'#0af\')\nrectangle.width = ap.Int(100)\n\nap.save_overall_html(\n    dest_dir_path=\'rectangle_width/\')\n```',  # noqa

    '## height property interface example':
    '## height属性のインターフェイス例',

    'The `height` property updates or gets the instance\'s height:':
    '`height`属性では高さの値の更新もしくは取得を行えます:',

    '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    background_color=\'#333\',\n    stage_width=150,\n    stage_height=200,\n    stage_elem_id=\'stage\')\nrectangle: ap.Rectangle = ap.Rectangle(\n    x=50, y=50, width=50, height=50,\n    fill_color=\'#0af\')\nrectangle.height = ap.Int(100)\n\nap.save_overall_html(\n    dest_dir_path=\'rectangle_height/\')\n```':  # noqa
    '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    background_color=\'#333\',\n    stage_width=150,\n    stage_height=200,\n    stage_elem_id=\'stage\')\nrectangle: ap.Rectangle = ap.Rectangle(\n    x=50, y=50, width=50, height=50,\n    fill_color=\'#0af\')\nrectangle.height = ap.Int(100)\n\nap.save_overall_html(\n    dest_dir_path=\'rectangle_height/\')\n```',  # noqa

    '## ellipse_width property interface example':
    '## ellipse_width属性のインターフェイス例',

    'The `ellipse_width` property updates or gets the instance\'s ellipse width:':  # noqa
    '`ellipse_width`属性では四角の角丸の幅の値の更新もしくは取得を行えます:',

    '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    background_color=\'#333\',\n    stage_width=150,\n    stage_height=150,\n    stage_elem_id=\'stage\')\nrectangle: ap.Rectangle = ap.Rectangle(\n    x=50, y=50, width=50, height=50,\n    fill_color=\'#0af\')\nrectangle.ellipse_width = ap.Int(30)\nrectangle.ellipse_height = ap.Int(15)\n\nap.save_overall_html(\n    dest_dir_path=\'rectangle_ellipse_width/\')\n```':  # noqa
    '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    background_color=\'#333\',\n    stage_width=150,\n    stage_height=150,\n    stage_elem_id=\'stage\')\nrectangle: ap.Rectangle = ap.Rectangle(\n    x=50, y=50, width=50, height=50,\n    fill_color=\'#0af\')\nrectangle.ellipse_width = ap.Int(30)\nrectangle.ellipse_height = ap.Int(15)\n\nap.save_overall_html(\n    dest_dir_path=\'rectangle_ellipse_width/\')\n```',  # noqa

    '## ellipse_height property interface example':
    '## ellipse_height属性のインターフェイス例',

    'The `ellipse_height` property updates or gets the instance\'s ellipse height:':  # noqa
    '`ellipse_height`属性では四角の角丸の高さの値の更新もしくは取得を行えます:',

    '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    background_color=\'#333\',\n    stage_width=150,\n    stage_height=150,\n    stage_elem_id=\'stage\')\nrectangle: ap.Rectangle = ap.Rectangle(\n    x=50, y=50, width=50, height=50,\n    fill_color=\'#0af\')\nrectangle.ellipse_width = ap.Int(15)\nrectangle.ellipse_height = ap.Int(30)\n\nap.save_overall_html(\n    dest_dir_path=\'rectangle_ellipse_height/\')\n```':  # noqa
    '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    background_color=\'#333\',\n    stage_width=150,\n    stage_height=150,\n    stage_elem_id=\'stage\')\nrectangle: ap.Rectangle = ap.Rectangle(\n    x=50, y=50, width=50, height=50,\n    fill_color=\'#0af\')\nrectangle.ellipse_width = ap.Int(15)\nrectangle.ellipse_height = ap.Int(30)\n\nap.save_overall_html(\n    dest_dir_path=\'rectangle_ellipse_height/\')\n```',  # noqa

    '## fill_color property interface example':
    '## fill_color属性のインターフェイス例',

    'The `fill_color` property updates or gets the instance\'s fill color:':
    '`fill_color`属性は塗りの色の値の更新もしくは取得を行えます:',

    '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    background_color=\'#333\',\n    stage_width=150,\n    stage_height=150,\n    stage_elem_id=\'stage\')\nrectangle: ap.Rectangle = ap.Rectangle(\n    x=50, y=50, width=50, height=50,\n    fill_color=\'#0af\')\nrectangle.fill_color = ap.String(\'#f0a\')\n\nap.save_overall_html(\n    dest_dir_path=\'rectangle_fill_color/\')\n```':  # noqa
    '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    background_color=\'#333\',\n    stage_width=150,\n    stage_height=150,\n    stage_elem_id=\'stage\')\nrectangle: ap.Rectangle = ap.Rectangle(\n    x=50, y=50, width=50, height=50,\n    fill_color=\'#0af\')\nrectangle.fill_color = ap.String(\'#f0a\')\n\nap.save_overall_html(\n    dest_dir_path=\'rectangle_fill_color/\')\n```',  # noqa

    '## fill_alpha property interface example':
    '## fill_alpha属性のインターフェイス例',

    'The `fill_alpha` property updates or gets the instance\'s fill alpha (opacity):':  # noqa
    '`fill_alpha`属性は塗りの透明度の値の更新もしくは取得を行えます:',

    '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    background_color=\'#333\',\n    stage_width=150,\n    stage_height=150,\n    stage_elem_id=\'stage\')\nrectangle: ap.Rectangle = ap.Rectangle(\n    x=50, y=50, width=50, height=50,\n    fill_color=\'#0af\')\nrectangle.fill_alpha = ap.Number(0.3)\n\nap.save_overall_html(\n    dest_dir_path=\'rectangle_fill_alpha/\')\n```':  # noqa
    '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    background_color=\'#333\',\n    stage_width=150,\n    stage_height=150,\n    stage_elem_id=\'stage\')\nrectangle: ap.Rectangle = ap.Rectangle(\n    x=50, y=50, width=50, height=50,\n    fill_color=\'#0af\')\nrectangle.fill_alpha = ap.Number(0.3)\n\nap.save_overall_html(\n    dest_dir_path=\'rectangle_fill_alpha/\')\n```',  # noqa

    '## line_color property interface example':
    '## line_color属性のインターフェイス例',

    'The `line_color` property updates or gets the instance\'s line color:':
    '`line_color`属性では線の色の値の更新もしくは取得を行えます:',

    '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    background_color=\'#333\',\n    stage_width=150,\n    stage_height=150,\n    stage_elem_id=\'stage\')\nrectangle: ap.Rectangle = ap.Rectangle(\n    x=50, y=50, width=50, height=50, line_thickness=5)\nrectangle.line_color = ap.String(\'#0af\')\n\nap.save_overall_html(\n    dest_dir_path=\'rectangle_line_color/\')\n```':  # noqa
    '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    background_color=\'#333\',\n    stage_width=150,\n    stage_height=150,\n    stage_elem_id=\'stage\')\nrectangle: ap.Rectangle = ap.Rectangle(\n    x=50, y=50, width=50, height=50, line_thickness=5)\nrectangle.line_color = ap.String(\'#0af\')\n\nap.save_overall_html(\n    dest_dir_path=\'rectangle_line_color/\')\n```',  # noqa

    '## line_alpha property interface example':
    '## line_alpha属性のインターフェイス例',

    'The `line_alpha` property updates or gets the instance\'s line alpha (opacity):':  # noqa
    '`line_alpha`属性では線の透明度の値の更新もしくは取得を行えます:',

    '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    background_color=\'#333\',\n    stage_width=150,\n    stage_height=150,\n    stage_elem_id=\'stage\')\nrectangle: ap.Rectangle = ap.Rectangle(\n    x=50, y=50, width=50, height=50,\n    line_color=\'#0af\', line_thickness=5)\nrectangle.line_alpha = ap.Number(0.3)\n\nap.save_overall_html(\n    dest_dir_path=\'rectangle_line_alpha/\')\n```':  # noqa
    '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    background_color=\'#333\',\n    stage_width=150,\n    stage_height=150,\n    stage_elem_id=\'stage\')\nrectangle: ap.Rectangle = ap.Rectangle(\n    x=50, y=50, width=50, height=50,\n    line_color=\'#0af\', line_thickness=5)\nrectangle.line_alpha = ap.Number(0.3)\n\nap.save_overall_html(\n    dest_dir_path=\'rectangle_line_alpha/\')\n```',  # noqa

    '## line_thickness property interface example':
    '## line_thickness属性のインターフェイス例',

    'The `line_thickness` property updates or gets the instance\'s line thickness (line width):':  # noqa
    '`line_thickness`属性では線の幅の更新もしくは取得を行えます:',

    '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    background_color=\'#333\',\n    stage_width=150,\n    stage_height=150,\n    stage_elem_id=\'stage\')\nrectangle: ap.Rectangle = ap.Rectangle(\n    x=50, y=50, width=50, height=50, line_color=\'#0af\')\nrectangle.line_thickness = ap.Int(10)\n\nap.save_overall_html(\n    dest_dir_path=\'rectangle_line_thickness/\')\n```':  # noqa
    '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    background_color=\'#333\',\n    stage_width=150,\n    stage_height=150,\n    stage_elem_id=\'stage\')\nrectangle: ap.Rectangle = ap.Rectangle(\n    x=50, y=50, width=50, height=50, line_color=\'#0af\')\nrectangle.line_thickness = ap.Int(10)\n\nap.save_overall_html(\n    dest_dir_path=\'rectangle_line_thickness/\')\n```',  # noqa

    '## line_dot_setting property interface example':
    '## line_dot_setting属性のインターフェイス例',

    'The `line_dot_setting` property updates or gets the instance\'s line dot-style setting:':  # noqa
    '`line_dot_setting`属性では点線のスタイル設定の更新もしくは取得を行えます:',

    '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    background_color=\'#333\',\n    stage_width=150,\n    stage_height=150,\n    stage_elem_id=\'stage\')\nrectangle: ap.Rectangle = ap.Rectangle(\n    x=50, y=50, width=50, height=50,\n    line_color=\'#0af\', line_thickness=5)\nrectangle.line_dot_setting = ap.LineDotSetting(dot_size=3)\n\nap.save_overall_html(\n    dest_dir_path=\'rectangle_line_dot_setting/\')\n```':  # noqa
    '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    background_color=\'#333\',\n    stage_width=150,\n    stage_height=150,\n    stage_elem_id=\'stage\')\nrectangle: ap.Rectangle = ap.Rectangle(\n    x=50, y=50, width=50, height=50,\n    line_color=\'#0af\', line_thickness=5)\nrectangle.line_dot_setting = ap.LineDotSetting(dot_size=3)\n\nap.save_overall_html(\n    dest_dir_path=\'rectangle_line_dot_setting/\')\n```',  # noqa

    '## line_dash_setting property interface example':
    '## line_dash_setting属性のインターフェイス例',

    'The `line_dash_setting` property updates or gets the instance\'s line dash-style setting:':  # noqa
    '`line_dash_setting`属性では破線のスタイル設定の更新もしくは取得を行えます:',

    '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    background_color=\'#333\',\n    stage_width=150,\n    stage_height=150,\n    stage_elem_id=\'stage\')\nrectangle: ap.Rectangle = ap.Rectangle(\n    x=50, y=50, width=50, height=50,\n    line_color=\'#0af\', line_thickness=2)\nrectangle.line_dash_setting = ap.LineDashSetting(\n    dash_size=7, space_size=2)\n\nap.save_overall_html(\n    dest_dir_path=\'rectangle_line_dash_setting/\')\n```':  # noqa
    '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    background_color=\'#333\',\n    stage_width=150,\n    stage_height=150,\n    stage_elem_id=\'stage\')\nrectangle: ap.Rectangle = ap.Rectangle(\n    x=50, y=50, width=50, height=50,\n    line_color=\'#0af\', line_thickness=2)\nrectangle.line_dash_setting = ap.LineDashSetting(\n    dash_size=7, space_size=2)\n\nap.save_overall_html(\n    dest_dir_path=\'rectangle_line_dash_setting/\')\n```',  # noqa

    '## line_round_dot_setting property interface example':
    '## line_round_dot_setting属性のインターフェイス例',

    'The `line_round_dot_setting` property updates or gets the instance\'s line round dot-style setting:':  # noqa
    '`line_round_dot_setting`属性では丸ドット線のスタイル設定の更新もしくは取得を行えます:',

    '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    background_color=\'#333\',\n    stage_width=150,\n    stage_height=150,\n    stage_elem_id=\'stage\')\nrectangle: ap.Rectangle = ap.Rectangle(\n    x=50, y=50, width=50, height=50,\n    line_color=\'#0af\')\nrectangle.line_round_dot_setting = ap.LineRoundDotSetting(\n    round_size=6, space_size=3)\n\nap.save_overall_html(\n    dest_dir_path=\'rectangle_line_round_dot_setting/\')\n```':  # noqa
    '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    background_color=\'#333\',\n    stage_width=150,\n    stage_height=150,\n    stage_elem_id=\'stage\')\nrectangle: ap.Rectangle = ap.Rectangle(\n    x=50, y=50, width=50, height=50,\n    line_color=\'#0af\')\nrectangle.line_round_dot_setting = ap.LineRoundDotSetting(\n    round_size=6, space_size=3)\n\nap.save_overall_html(\n    dest_dir_path=\'rectangle_line_round_dot_setting/\')\n```',  # noqa

    '## line_dash_dot_setting property interface example':
    '## line_dash_dot_setting属性のインターフェイス例',

    'The `line_dash_dot_setting` property updates or gets the instance\'s dash-dotted line style setting:':  # noqa
    '`line_dash_dot_setting`属性では一点鎖線のスタイル設定の更新もしくは取得を行えます:',

    '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    background_color=\'#333\',\n    stage_width=150,\n    stage_height=150,\n    stage_elem_id=\'stage\')\nrectangle: ap.Rectangle = ap.Rectangle(\n    x=50, y=50, width=50, height=50,\n    line_color=\'#0af\', line_thickness=3)\nrectangle.line_dash_dot_setting = ap.LineDashDotSetting(\n    dot_size=3, dash_size=7, space_size=3)\n\nap.save_overall_html(\n    dest_dir_path=\'rectangle_line_dash_dot_setting/\')\n```':  # noqa
    '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    background_color=\'#333\',\n    stage_width=150,\n    stage_height=150,\n    stage_elem_id=\'stage\')\nrectangle: ap.Rectangle = ap.Rectangle(\n    x=50, y=50, width=50, height=50,\n    line_color=\'#0af\', line_thickness=3)\nrectangle.line_dash_dot_setting = ap.LineDashDotSetting(\n    dot_size=3, dash_size=7, space_size=3)\n\nap.save_overall_html(\n    dest_dir_path=\'rectangle_line_dash_dot_setting/\')\n```',  # noqa

}
