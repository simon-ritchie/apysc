"""This module is for the translation mapping data of the
following document:

Document file: ellipse.md
Language: jp
"""

from typing import Dict

MAPPING: Dict[str, str] = {

    '# Ellipse class':
    '# Ellipse クラス',

    'This page explains the `Ellipse` class.':
    'このページでは`Ellipse`クラスについて説明します。',

    '## What class is this?':
    '## クラス概要',

    'The `Ellipse` class creates an ellipse vector graphics object.':
    '`Ellipse`クラスは楕円のベクターグラフィックスのオブジェクトを生成します。',

    '## Basic usage':
    '## 基本的な使い方',

    'The `Ellipse` class constructor requires the `x` (center-x), `y` (center-y), `width`, and `height` arguments.':  # noqa
    '`Ellipse`クラスのコンストラクタでは`x`（楕円の中央のX座標）、`y`（楕円の中央のY座標）、`width`、`height`の各引数の指定が必要です。',  # noqa

    'The constructor also accepts each style\'s argument, such as the `fill_color`.':  # noqa
    'コンストラクタでは他の`fill_color`などのスタイル設定の各引数も受け付けます。',

    '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    background_color=\'#333\',\n    stage_width=150,\n    stage_height=150,\n    stage_elem_id=\'stage\')\nellipse: ap.Ellipse = ap.Ellipse(\n    x=75, y=75, width=100, height=75, fill_color=\'#0af\')\n\nap.save_overall_html(\n    dest_dir_path=\'ellipse_basic_usage/\')\n```':  # noqa
    '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    background_color=\'#333\',\n    stage_width=150,\n    stage_height=150,\n    stage_elem_id=\'stage\')\nellipse: ap.Ellipse = ap.Ellipse(\n    x=75, y=75, width=100, height=75, fill_color=\'#0af\')\n\nap.save_overall_html(\n    dest_dir_path=\'ellipse_basic_usage/\')\n```',  # noqa

    '## Note of the draw_ellipse interface':
    '## draw_ellipse インターフェイスについての特記事項',

    'You can also create an ellipse instance with the `draw_ellipse` interface.':  # noqa
    '`draw_ellipse`を使う形でも楕円のインスタンスを生成することができます。',

    'Please see also:':
    '関連資料:',

    '- [Graphics class draw_ellipse interface](graphics_draw_ellipse.md)':
    '- [Graphics クラスの draw_ellipse (楕円描画) のインターフェイス](jp_graphics_draw_ellipse.md)',  # noqa

    '## x property interface example':
    '## x属性のインターフェイス例',

    'The `x` property updates or gets the instance\'s x-coordinate:':
    '`x`属性ではX座標の値の更新もしくは取得を行えます:',

    '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    background_color=\'#333\',\n    stage_width=150,\n    stage_height=150,\n    stage_elem_id=\'stage\')\nellipse: ap.Ellipse = ap.Ellipse(\n    x=0, y=75, width=100, height=75, fill_color=\'#0af\')\nellipse.x = ap.Int(100)\n\nap.save_overall_html(\n    dest_dir_path=\'ellipse_x/\')\n```':  # noqa
    '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    background_color=\'#333\',\n    stage_width=150,\n    stage_height=150,\n    stage_elem_id=\'stage\')\nellipse: ap.Ellipse = ap.Ellipse(\n    x=0, y=75, width=100, height=75, fill_color=\'#0af\')\nellipse.x = ap.Int(100)\n\nap.save_overall_html(\n    dest_dir_path=\'ellipse_x/\')\n```',  # noqa

    '## y property interface example':
    '## y属性のインターフェイス例',

    'The `y` property updates or gets the instance\'s y-coordinate:':
    '`y`属性ではY座標の値の更新もしくは取得を行えます:',

    '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    background_color=\'#333\',\n    stage_width=150,\n    stage_height=150,\n    stage_elem_id=\'stage\')\nellipse: ap.Ellipse = ap.Ellipse(\n    x=75, y=0, width=100, height=50, fill_color=\'#0af\')\nellipse.y = ap.Int(125)\n\nap.save_overall_html(\n    dest_dir_path=\'ellipse_y/\')\n```':  # noqa
    '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    background_color=\'#333\',\n    stage_width=150,\n    stage_height=150,\n    stage_elem_id=\'stage\')\nellipse: ap.Ellipse = ap.Ellipse(\n    x=75, y=0, width=100, height=50, fill_color=\'#0af\')\nellipse.y = ap.Int(125)\n\nap.save_overall_html(\n    dest_dir_path=\'ellipse_y/\')\n```',  # noqa

    '## width property interface example':
    '## width属性のインターフェイス例',

    'The `width` property updates or gets the instance\'s width:':
    '`width`属性では幅の値の更新もしくは取得を行えます:',

    '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    background_color=\'#333\',\n    stage_width=150,\n    stage_height=150,\n    stage_elem_id=\'stage\')\nellipse: ap.Ellipse = ap.Ellipse(\n    x=75, y=75, width=0, height=75, fill_color=\'#0af\')\nellipse.width = ap.Int(125)\n\nap.save_overall_html(\n    dest_dir_path=\'ellipse_width/\')\n```':  # noqa
    '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    background_color=\'#333\',\n    stage_width=150,\n    stage_height=150,\n    stage_elem_id=\'stage\')\nellipse: ap.Ellipse = ap.Ellipse(\n    x=75, y=75, width=0, height=75, fill_color=\'#0af\')\nellipse.width = ap.Int(125)\n\nap.save_overall_html(\n    dest_dir_path=\'ellipse_width/\')\n```',  # noqa

    '## height property interface example':
    '## height属性のインターフェイス例',

    'The `height` property updates or gets the instance\'s height:':
    '`height`属性では高さの値の更新もしくは取得を行えます:',

    '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    background_color=\'#333\',\n    stage_width=150,\n    stage_height=150,\n    stage_elem_id=\'stage\')\nellipse: ap.Ellipse = ap.Ellipse(\n    x=75, y=75, width=75, height=0, fill_color=\'#0af\')\nellipse.height = ap.Int(125)\n\nap.save_overall_html(\n    dest_dir_path=\'ellipse_height/\')\n```':  # noqa
    '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    background_color=\'#333\',\n    stage_width=150,\n    stage_height=150,\n    stage_elem_id=\'stage\')\nellipse: ap.Ellipse = ap.Ellipse(\n    x=75, y=75, width=75, height=0, fill_color=\'#0af\')\nellipse.height = ap.Int(125)\n\nap.save_overall_html(\n    dest_dir_path=\'ellipse_height/\')\n```',  # noqa

    '## fill_color property interface example':
    '## fill_color属性のインターフェイス例',

    'The `fill_color` property updates or gets the instance\'s fill color:':
    '`fill_color`属性は塗りの色の値の更新もしくは取得を行えます:',

    '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    background_color=\'#333\',\n    stage_width=150,\n    stage_height=150,\n    stage_elem_id=\'stage\')\nellipse: ap.Ellipse = ap.Ellipse(\n    x=75, y=75, width=100, height=75)\nellipse.fill_color = ap.String(\'#f0a\')\n\nap.save_overall_html(\n    dest_dir_path=\'ellipse_fill_color/\')\n```':  # noqa
    '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    background_color=\'#333\',\n    stage_width=150,\n    stage_height=150,\n    stage_elem_id=\'stage\')\nellipse: ap.Ellipse = ap.Ellipse(\n    x=75, y=75, width=100, height=75)\nellipse.fill_color = ap.String(\'#f0a\')\n\nap.save_overall_html(\n    dest_dir_path=\'ellipse_fill_color/\')\n```',  # noqa

    '## fill_alpha property interface example':
    '## fill_alpha属性のインターフェイス例',

    'The `fill_alpha` property updates or gets the instance\'s fill alpha (opacity):':  # noqa
    '`fill_alpha`属性は塗りの透明度の値の更新もしくは取得を行えます:',

    '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    background_color=\'#333\',\n    stage_width=150,\n    stage_height=150,\n    stage_elem_id=\'stage\')\nellipse: ap.Ellipse = ap.Ellipse(\n    x=75, y=75, width=100, height=75, fill_color=\'#0af\')\nellipse.fill_alpha = ap.Number(0.3)\n\nap.save_overall_html(\n    dest_dir_path=\'ellipse_fill_alpha/\')\n```':  # noqa
    '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    background_color=\'#333\',\n    stage_width=150,\n    stage_height=150,\n    stage_elem_id=\'stage\')\nellipse: ap.Ellipse = ap.Ellipse(\n    x=75, y=75, width=100, height=75, fill_color=\'#0af\')\nellipse.fill_alpha = ap.Number(0.3)\n\nap.save_overall_html(\n    dest_dir_path=\'ellipse_fill_alpha/\')\n```',  # noqa

    '## line_color property interface example':
    '## line_color属性のインターフェイス例',

    'The `line_color` property updates or gets the instance\'s line color:':
    '`line_color`属性では線の色の値の更新もしくは取得を行えます:',

    '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    background_color=\'#333\',\n    stage_width=150,\n    stage_height=150,\n    stage_elem_id=\'stage\')\nellipse: ap.Ellipse = ap.Ellipse(\n    x=75, y=75, width=100, height=75, line_thickness=5)\nellipse.line_color = ap.String(\'#0af\')\n\nap.save_overall_html(\n    dest_dir_path=\'ellipse_line_color/\')\n```':  # noqa
    '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    background_color=\'#333\',\n    stage_width=150,\n    stage_height=150,\n    stage_elem_id=\'stage\')\nellipse: ap.Ellipse = ap.Ellipse(\n    x=75, y=75, width=100, height=75, line_thickness=5)\nellipse.line_color = ap.String(\'#0af\')\n\nap.save_overall_html(\n    dest_dir_path=\'ellipse_line_color/\')\n```',  # noqa

    '## line_alpha property interface example':
    '## line_alpha属性のインターフェイス例',

    'The `line_alpha` property updates or gets the instance\'s line alpha (opacity):':  # noqa
    '`line_alpha`属性では線の透明度の値の更新もしくは取得を行えます:',

    '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    background_color=\'#333\',\n    stage_width=150,\n    stage_height=150,\n    stage_elem_id=\'stage\')\nellipse: ap.Ellipse = ap.Ellipse(\n    x=75, y=75, width=100, height=75,\n    line_color=\'0af\', line_thickness=5)\nellipse.line_alpha = ap.Number(0.3)\n\nap.save_overall_html(\n    dest_dir_path=\'ellipse_line_alpha/\')\n```':  # noqa
    '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    background_color=\'#333\',\n    stage_width=150,\n    stage_height=150,\n    stage_elem_id=\'stage\')\nellipse: ap.Ellipse = ap.Ellipse(\n    x=75, y=75, width=100, height=75,\n    line_color=\'0af\', line_thickness=5)\nellipse.line_alpha = ap.Number(0.3)\n\nap.save_overall_html(\n    dest_dir_path=\'ellipse_line_alpha/\')\n```',  # noqa

    '## line_thickness property interface example':
    '## line_thickness属性のインターフェイス例',

    'The `line_thickness` property updates or gets the instance\'s line thickness (line width):':  # noqa
    '`line_thickness`属性では線の幅の更新もしくは取得を行えます:',

    '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    background_color=\'#333\',\n    stage_width=150,\n    stage_height=150,\n    stage_elem_id=\'stage\')\nellipse: ap.Ellipse = ap.Ellipse(\n    x=75, y=75, width=100, height=75, line_color=\'0af\')\nellipse.line_thickness = ap.Int(8)\n\nap.save_overall_html(\n    dest_dir_path=\'ellipse_line_thickness/\')\n```':  # noqa
    '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    background_color=\'#333\',\n    stage_width=150,\n    stage_height=150,\n    stage_elem_id=\'stage\')\nellipse: ap.Ellipse = ap.Ellipse(\n    x=75, y=75, width=100, height=75, line_color=\'0af\')\nellipse.line_thickness = ap.Int(8)\n\nap.save_overall_html(\n    dest_dir_path=\'ellipse_line_thickness/\')\n```',  # noqa

    '## line_dot_setting property interface example':
    '## line_dot_setting属性のインターフェイス例',

    'The `line_dot_setting` property updates or gets the instance\'s line dot-style setting:':  # noqa
    '`line_dot_setting`属性では点線のスタイル設定の更新もしくは取得を行えます:',

    '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    background_color=\'#333\',\n    stage_width=150,\n    stage_height=150,\n    stage_elem_id=\'stage\')\nellipse: ap.Ellipse = ap.Ellipse(\n    x=75, y=75, width=100, height=75,\n    line_color=\'0af\', line_thickness=2)\nellipse.line_dot_setting = ap.LineDotSetting(dot_size=2)\n\nap.save_overall_html(\n    dest_dir_path=\'ellipse_line_dot_setting/\')\n```':  # noqa
    '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    background_color=\'#333\',\n    stage_width=150,\n    stage_height=150,\n    stage_elem_id=\'stage\')\nellipse: ap.Ellipse = ap.Ellipse(\n    x=75, y=75, width=100, height=75,\n    line_color=\'0af\', line_thickness=2)\nellipse.line_dot_setting = ap.LineDotSetting(dot_size=2)\n\nap.save_overall_html(\n    dest_dir_path=\'ellipse_line_dot_setting/\')\n```',  # noqa

    '## line_dash_setting property interface example':
    '## line_dash_setting属性のインターフェイス例',

    'The `line_dash_setting` property updates or gets the instance\'s line dash-style setting:':  # noqa
    '`line_dash_setting`属性では破線のスタイル設定の更新もしくは取得を行えます:',

    '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    background_color=\'#333\',\n    stage_width=150,\n    stage_height=150,\n    stage_elem_id=\'stage\')\nellipse: ap.Ellipse = ap.Ellipse(\n    x=75, y=75, width=100, height=75,\n    line_color=\'0af\', line_thickness=2)\nellipse.line_dash_setting = ap.LineDashSetting(\n    dash_size=6, space_size=2)\n\nap.save_overall_html(\n    dest_dir_path=\'ellipse_line_dash_setting/\')\n```':  # noqa
    '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    background_color=\'#333\',\n    stage_width=150,\n    stage_height=150,\n    stage_elem_id=\'stage\')\nellipse: ap.Ellipse = ap.Ellipse(\n    x=75, y=75, width=100, height=75,\n    line_color=\'0af\', line_thickness=2)\nellipse.line_dash_setting = ap.LineDashSetting(\n    dash_size=6, space_size=2)\n\nap.save_overall_html(\n    dest_dir_path=\'ellipse_line_dash_setting/\')\n```',  # noqa

    '## line_round_dot_setting property interface example':
    '## line_round_dot_setting属性のインターフェイス例',

    'The `line_round_dot_setting` property updates or gets the instance\'s line round dot-style setting:':  # noqa
    '`line_round_dot_setting`属性では丸ドット線のスタイル設定の更新もしくは取得を行えます:',

    '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    background_color=\'#333\',\n    stage_width=150,\n    stage_height=150,\n    stage_elem_id=\'stage\')\nellipse: ap.Ellipse = ap.Ellipse(\n    x=75, y=75, width=100, height=75, line_color=\'0af\')\nellipse.line_round_dot_setting = ap.LineRoundDotSetting(\n    round_size=5, space_size=2)\n\nap.save_overall_html(\n    dest_dir_path=\'ellipse_line_round_dot_setting/\')\n```':  # noqa
    '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    background_color=\'#333\',\n    stage_width=150,\n    stage_height=150,\n    stage_elem_id=\'stage\')\nellipse: ap.Ellipse = ap.Ellipse(\n    x=75, y=75, width=100, height=75, line_color=\'0af\')\nellipse.line_round_dot_setting = ap.LineRoundDotSetting(\n    round_size=5, space_size=2)\n\nap.save_overall_html(\n    dest_dir_path=\'ellipse_line_round_dot_setting/\')\n```',  # noqa

    '## line_dash_dot_setting property interface example':
    '## line_dash_dot_setting属性のインターフェイス例',

    'The `line_dash_dot_setting` property updates or gets the instance\'s dash-dotted line style setting:':  # noqa
    '`line_dash_dot_setting`属性では一点鎖線のスタイル設定の更新もしくは取得を行えます:',

    '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    background_color=\'#333\',\n    stage_width=150,\n    stage_height=150,\n    stage_elem_id=\'stage\')\nellipse: ap.Ellipse = ap.Ellipse(\n    x=75, y=75, width=100, height=75,\n    line_color=\'0af\', line_thickness=2)\nellipse.line_dash_dot_setting = ap.LineDashDotSetting(\n    dot_size=3, dash_size=6, space_size=3)\n\nap.save_overall_html(\n    dest_dir_path=\'ellipse_line_dash_dot_setting/\')\n```':  # noqa
    '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    background_color=\'#333\',\n    stage_width=150,\n    stage_height=150,\n    stage_elem_id=\'stage\')\nellipse: ap.Ellipse = ap.Ellipse(\n    x=75, y=75, width=100, height=75,\n    line_color=\'0af\', line_thickness=2)\nellipse.line_dash_dot_setting = ap.LineDashDotSetting(\n    dot_size=3, dash_size=6, space_size=3)\n\nap.save_overall_html(\n    dest_dir_path=\'ellipse_line_dash_dot_setting/\')\n```',  # noqa

    '## Ellipse class constructor API':
    '## Ellipse クラスのコンストラクタのAPI',

    '<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>':  # noqa
    '<span class="inconspicuous-txt">特記事項: このAPIドキュメントはドキュメントビルド用のスクリプトによって自動で生成・同期されています。そのためもしかしたらこの節の内容は前節までの内容と重複している場合があります。</span>',  # noqa

    '**[Interface summary]** Create an ellipse vector graphic.<hr>':
    '**[インターフェイス概要]** 楕円のベクターグラフィックスを生成します。<hr>',

    '**[Parameters]**':
    '**[引数]**',

    '- `x`: Int or int':
    '- `x`: Int or int',

    '  - X-coordinate of the ellipse center.':
    '  - 楕円の中央のX座標。',

    '- `y`: Int or int':
    '- `y`: Int or int',

    '  - Y-coordinate of the ellipse center.':
    '  - 楕円の中央のY座標。',

    '- `width`: Int or int':
    '- `width`: Int or int',

    '  - Ellipse width.':
    '  - 楕円の幅。',

    '- `height`: Int or int':
    '- `height`: Int or int',

    '  - Ellipse height.':
    '  - 楕円の高さ。',

    '- `fill_color`: str or String, default \'\'':
    '- `fill_color`: str or String, default \'\'',

    '  - A fill-color to set.':
    '  - 設定する塗りの色。',

    '- `fill_alpha`: float or Number, default 1.0':
    '- `fill_alpha`: float or Number, default 1.0',

    '  - A fill-alpha to set.':
    '  - 設定する塗りの透明度。',

    '- `line_color`: str or String, default \'\'':
    '- `line_color`: str or String, default \'\'',

    '  - A line-color to set.':
    '  - 設定する線の色。',

    '- `line_alpha`: float or Number, default 1.0':
    '- `line_alpha`: float or Number, default 1.0',

    '  - A line-alpha to set.':
    '  - 設定する線の透明度。',

    '- `line_thickness`: int or Int, default 1':
    '- `line_thickness`: int or Int, default 1',

    '  - A line-thickness (line-width) to set.':
    '  - 設定の線幅。',

    '- `line_cap`: String or LineCaps or None, default None':
    '- `line_cap`: String or LineCaps or None, default None',

    '  - A line-cap setting to set.':
    '  - 設定する線の端のスタイル設定。',

    '- `line_joints`: String or LineJoints or None, default None':
    '- `line_joints`: String or LineJoints or None, default None',

    '  - A line-joints setting to set.':
    '  - 設定する線の連結部分のスタイル設定。',

    '- `line_dot_setting`: LineDotSetting or None, default None':
    '- `line_dot_setting`: LineDotSetting or None, default None',

    '  - A dot setting to set.':
    '  - 設定する点線のスタイル設定。',

    '- `line_dash_setting`: LineDashSetting or None, default None':
    '- `line_dash_setting`: LineDashSetting or None, default None',

    '  - A dash setting to set.':
    '  - 設定する破線のスタイル設定。',

    '- `line_round_dot_setting`: LineRoundDotSetting or None, default None':
    '- `line_round_dot_setting`: LineRoundDotSetting or None, default None',

    '  - A round-dot setting to set.':
    '  - 設定する丸ドットのスタイル設定。',

    '- `line_dash_dot_setting`: LineDashDotSetting or None, default None':
    '- `line_dash_dot_setting`: LineDashDotSetting or None, default None',

    '  - A dash dot (1-dot chain) setting to set.':
    '  - 設定する一点鎖線のスタイル設定。',

    '- `parent`: ChildInterface or None, default None':
    '- `parent`: ChildInterface or None, default None',

    '  - A parent instance to add this instance. If a specified value is None, this interface uses a stage instance.':  # noqa
    '  - このインスタンスを追加する親のインスタンス。もしもNoneが指定された場合、このインスタンスはステージのインスタンスへと追加されます。',  # noqa

    '<hr>':
    '<hr>',

    '**[Examples]**':
    '**[コードサンプル]**',

    '```py\n>>> import apysc as ap\n>>> stage: ap.Stage = ap.Stage()\n>>> ellipse: ap.Ellipse = ap.Ellipse(\n...    x=100, y=100, width=100, height=50, fill_color=\'#00aaff\')\n>>> ellipse.x\nInt(100)\n\n>>> ellipse.y\nInt(100)\n\n>>> ellipse.width\nInt(100)\n\n>>> ellipse.height\nInt(50)\n\n>>> ellipse.fill_color\nString(\'#00aaff\')\n```':  # noqa
    '```py\n>>> import apysc as ap\n>>> stage: ap.Stage = ap.Stage()\n>>> ellipse: ap.Ellipse = ap.Ellipse(\n...    x=100, y=100, width=100, height=50, fill_color=\'#00aaff\')\n>>> ellipse.x\nInt(100)\n\n>>> ellipse.y\nInt(100)\n\n>>> ellipse.width\nInt(100)\n\n>>> ellipse.height\nInt(50)\n\n>>> ellipse.fill_color\nString(\'#00aaff\')\n```',  # noqa

}
