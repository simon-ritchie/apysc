"""This module is for the translation mapping data of the
following document:

Document file: graphics_line_dash_dot_setting.md
Language: jp
"""

from typing import Dict

MAPPING: Dict[str, str] = {

    '# Graphics line_dash_dot_setting interface':
    '# Graphics クラスの line_dash_dot_setting インターフェイス',

    'This page explains the `Graphics` class `line_dash_dot_setting` property interface.':  # noqa
    'このページでは`Graphics`クラスの`line_dash_dot_setting`属性のインターフェイスについて説明します。',

    '## What interface is this?':
    '## インターフェイス概要',

    'The `line_dash_dot_setting` property interface updates or get the instance\'s current line dash-dot setting.':  # noqa
    '`line_dash_dot_setting`属性のインターフェイスでは現在の一点鎖線のスタイル設定の更新もしくは取得を行えます。',

    '## Basic usage':
    '## 基本的な使い方',

    'The getter or setter interface value becomes (or requires) the `LineDashDotSetting` instance value.':  # noqa
    'getterやsetterのインターフェイスの値は`LineDashDotSetting`インスタンスの値となります。',

    'The following example sets the 10-pixel dash and 3-pixel dot to the line:':  # noqa
    '以下のコード例では10pxの破線と3pxの点線の一点鎖線を設定しています。',

    '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    stage_width=250, stage_height=100, background_color=\'#333\',\n    stage_elem_id=\'stage\')\nsprite: ap.Sprite = ap.Sprite()\nsprite.graphics.line_style(color=\'#0af\', thickness=5)\n\nline: ap.Line = sprite.graphics.draw_line(\n    x_start=50, y_start=50, x_end=200, y_end=50)\nline.line_dash_dot_setting = ap.LineDashDotSetting(\n    dot_size=10, dash_size=3, space_size=3)\n\nap.save_overall_html(\n    dest_dir_path=\'./graphics_line_dash_dot_setting_basic_usage/\')\n```':  # noqa
    '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    stage_width=250, stage_height=100, background_color=\'#333\',\n    stage_elem_id=\'stage\')\nsprite: ap.Sprite = ap.Sprite()\nsprite.graphics.line_style(color=\'#0af\', thickness=5)\n\nline: ap.Line = sprite.graphics.draw_line(\n    x_start=50, y_start=50, x_end=200, y_end=50)\nline.line_dash_dot_setting = ap.LineDashDotSetting(\n    dot_size=10, dash_size=3, space_size=3)\n\nap.save_overall_html(\n    dest_dir_path=\'./graphics_line_dash_dot_setting_basic_usage/\')\n```',  # noqa

    '## line_dash_dot_setting API':
    '## line_dash_dot_setting API',

    '<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>':  # noqa
    '<span class="inconspicuous-txt">特記事項: このAPIドキュメントはドキュメントビルド用のスクリプトによって自動で生成・同期されています。そのためもしかしたらこの節の内容は前節までの内容と重複している場合があります。</span>',  # noqa

    '**[Interface summary]** Get current dash dot (1-dot chain) setting.<hr>':  # noqa
    '**[インターフェイス概要]** 現在の一点鎖線のスタイル設定を取得します。<hr>',

    '**[Returns]**':
    '**[返却値]**',

    '- `line_dash_dot_setting`: LineDashDotSetting or None':
    '- `line_dash_dot_setting`: LineDashDotSetting or None',

    '  - Dash dot (1-dot chain) setting.':
    '  - 一点鎖線の設定。',

    '<hr>':
    '<hr>',

    '**[Examples]**':
    '**[コードサンプル]**',

    '```py\n>>> import apysc as ap\n>>> stage: ap.Stage = ap.Stage()\n>>> sprite: ap.Sprite = ap.Sprite()\n>>> sprite.graphics.line_style(color=\'#fff\', thickness=10)\n>>> line: ap.Line = sprite.graphics.draw_line(\n...     x_start=50, y_start=50, x_end=150, y_end=50)\n>>> line.line_dash_dot_setting = ap.LineDashDotSetting(\n...     dot_size=2, dash_size=5, space_size=3)\n>>> line.line_dash_dot_setting.dot_size\nInt(2)\n\n>>> line.line_dash_dot_setting.dash_size\nInt(5)\n\n>>> line.line_dash_dot_setting.space_size\nInt(3)\n```':  # noqa
    '```py\n>>> import apysc as ap\n>>> stage: ap.Stage = ap.Stage()\n>>> sprite: ap.Sprite = ap.Sprite()\n>>> sprite.graphics.line_style(color=\'#fff\', thickness=10)\n>>> line: ap.Line = sprite.graphics.draw_line(\n...     x_start=50, y_start=50, x_end=150, y_end=50)\n>>> line.line_dash_dot_setting = ap.LineDashDotSetting(\n...     dot_size=2, dash_size=5, space_size=3)\n>>> line.line_dash_dot_setting.dot_size\nInt(2)\n\n>>> line.line_dash_dot_setting.dash_size\nInt(5)\n\n>>> line.line_dash_dot_setting.space_size\nInt(3)\n```',  # noqa

}
