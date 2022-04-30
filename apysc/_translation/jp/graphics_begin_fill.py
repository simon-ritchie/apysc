"""This module is for the translation mapping data of the
following document:

Document file: graphics_begin_fill.md
Language: jp
"""

from typing import Dict

MAPPING: Dict[str, str] = {

    '# Graphics begin_fill interface':
    '# Graphics クラスの begin_fill インターフェイス',

    'This page explains the `Graphics` class `begin_fill` method interface.':  # noqa
    'このページでは`Graphics`クラスの`begin_fill`メソッドのインターフェイスについて説明します。',

    '## What interface is this?':
    '## インターフェイス概要',

    '`begin_fill` interface would set the fill color and fill alpha settings. This setting would be maintained until it is called again or called the `clear` method.':  # noqa
    '`begin_fill`インターフェイスは塗りの色と塗りの透明度を設定します。この設定は再度`begin_fill`のインターフェイスを呼び出すか、もしくは`clear`メソッドを呼ぶまで保持されます。',  # noqa

    '## Basic usage':
    '## 基本的な使い方',

    'Draw vector graphics interfaces (e.g., `draw_rect`) would use these fill settings when creating, so the `begin_fill` method needs to be called before calling each drawing interface.':  # noqa
    'ベクターグラフィックスの描画系の各インターフェイス（例 : `draw_rect`など）はグラフィックス生成時にこの塗りの設定を参照します。そのため描画系のインターフェイスを実行する前にこの`begin_fill`のインターフェイスを呼び出しておく必要があります。',  # noqa

    '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    background_color=\'#333\',\n    stage_width=350,\n    stage_height=150,\n    stage_elem_id=\'stage\')\nsprite: ap.Sprite = ap.Sprite()\n\n# Set blue fill color and draw the first rectangle.\nsprite.graphics.begin_fill(color=\'#0af\')\nsprite.graphics.draw_rect(\n    x=50, y=50, width=50, height=50)\n\n# Draw the second rectangle (fill color setting will be maintained).\nsprite.graphics.draw_rect(\n    x=150, y=50, width=50, height=50)\n\n# Set the other fill color and draw the third rectangle.\nsprite.graphics.begin_fill(color=\'#f0a\')\nsprite.graphics.draw_rect(\n    x=250, y=50, width=50, height=50)\n\nap.save_overall_html(\n    dest_dir_path=\'graphics_begin_fill_basic_usage/\')\n```':  # noqa
    '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    background_color=\'#333\',\n    stage_width=350,\n    stage_height=150,\n    stage_elem_id=\'stage\')\nsprite: ap.Sprite = ap.Sprite()\n\n# Set blue fill color and draw the first rectangle.\nsprite.graphics.begin_fill(color=\'#0af\')\nsprite.graphics.draw_rect(\n    x=50, y=50, width=50, height=50)\n\n# Draw the second rectangle (fill color setting will be maintained).\nsprite.graphics.draw_rect(\n    x=150, y=50, width=50, height=50)\n\n# Set the other fill color and draw the third rectangle.\nsprite.graphics.begin_fill(color=\'#f0a\')\nsprite.graphics.draw_rect(\n    x=250, y=50, width=50, height=50)\n\nap.save_overall_html(\n    dest_dir_path=\'graphics_begin_fill_basic_usage/\')\n```',  # noqa

    '## Fill color setting':
    '## 塗りの色の設定',

    'The `color` argument sets the fill color, and the `begin_fill` interface requires this argument.':  # noqa
    '`color`引数は塗りの色を設定します。`begin_fill`インターフェイスではこの引数は必須になっています。',

    '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    background_color=\'#333\',\n    stage_width=150,\n    stage_height=150,\n    stage_elem_id=\'stage\')\nsprite: ap.Sprite = ap.Sprite()\n\n# Set a cyan fill color and draw the rectangle.\nsprite.graphics.begin_fill(color=\'#0af\')\nsprite.graphics.draw_rect(x=50, y=50, width=50, height=50)\n\nap.save_overall_html(\n    dest_dir_path=\'graphics_begin_fill_fill_color/\')\n```':  # noqa
    '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    background_color=\'#333\',\n    stage_width=150,\n    stage_height=150,\n    stage_elem_id=\'stage\')\nsprite: ap.Sprite = ap.Sprite()\n\n# Set a cyan fill color and draw the rectangle.\nsprite.graphics.begin_fill(color=\'#0af\')\nsprite.graphics.draw_rect(x=50, y=50, width=50, height=50)\n\nap.save_overall_html(\n    dest_dir_path=\'graphics_begin_fill_fill_color/\')\n```',  # noqa

    'If you want to clear fill color, specify a blank string to this argument.':  # noqa
    'もしも塗りの色の設定を削除したい場合、空の文字列をこの引数に指定してください。',

    'For example, since the following code clears fill color settings, a rectangle graphic becomes invisible.':  # noqa
    '以下のコード例では塗りの色の設定を削除しているため、四角のグラフィックは見えなくなります。',

    '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    background_color=\'#333\',\n    stage_width=150,\n    stage_height=150,\n    stage_elem_id=\'stage\')\nsprite: ap.Sprite = ap.Sprite()\n\nsprite.graphics.begin_fill(color=\'#0af\')\n\n# Clear fill color by specifying blank string.\nsprite.graphics.begin_fill(color=\'\')\n\n# Since fill color is not set, the rectangle is invisible.\nsprite.graphics.draw_rect(\n    x=50, y=50, width=50, height=50)\n\nap.save_overall_html(\n    dest_dir_path=\'graphics_begin_fill_color_setting_clear/\')\n```':  # noqa
    '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    background_color=\'#333\',\n    stage_width=150,\n    stage_height=150,\n    stage_elem_id=\'stage\')\nsprite: ap.Sprite = ap.Sprite()\n\nsprite.graphics.begin_fill(color=\'#0af\')\n\n# Clear fill color by specifying blank string.\nsprite.graphics.begin_fill(color=\'\')\n\n# Since fill color is not set, the rectangle is invisible.\nsprite.graphics.draw_rect(\n    x=50, y=50, width=50, height=50)\n\nap.save_overall_html(\n    dest_dir_path=\'graphics_begin_fill_color_setting_clear/\')\n```',  # noqa

    'Color code is acceptable like the following list:':
    'カラーコードは以下の形の指定を受け付けています。',

    '- Six characters, e.g., `#00aaff`.':
    '- `#00aaff`などの6文字による指定。',

    '- Three characters, e.g., `#0af` (this becomes `#00aaff`).':
    '- `#0af`などの3文字による指定（これは`#00aaff`と同じ値として扱われます）。',

    '- Single character, e.g., `#5` (this becomes `#000005`).':
    '- `#5`などの1文字による指定（これは`000005`と同じ値として扱われます）。',

    '- Skipped `#` symbol, e.g., `0af` (this becomes `#00aaff`).':
    '- `0af`などの`#`記号を省略した指定（これは`#00aaff`と同じ値として扱われます）。',

    '- Blank string, e.g., `\'\'` (this setting clears the fill color setting).':  # noqa
    '- ``などの空文字（この指定は塗りの色の設定を削除します）。',

    '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    background_color=\'#333\',\n    stage_width=450,\n    stage_height=150,\n    stage_elem_id=\'stage\')\nsprite: ap.Sprite = ap.Sprite()\n\n# Six characters fill color setting (a cyan color).\nsprite.graphics.begin_fill(color=\'#00aaff\')\nsprite.graphics.draw_rect(\n    x=50, y=50, width=50, height=50)\n\n# Three characters fill color setting (a magenta color).\nsprite.graphics.begin_fill(color=\'#f0a\')\nsprite.graphics.draw_rect(\n    x=150, y=50, width=50, height=50)\n\n# Single characters fill color setting (a black color).\nsprite.graphics.begin_fill(color=\'#0\')\nsprite.graphics.draw_rect(\n    x=250, y=50, width=50, height=50)\n\n# Fill color that Skipped `#` symbol is also acceptable.\nsprite.graphics.begin_fill(color=\'999\')\nsprite.graphics.draw_rect(\n    x=350, y=50, width=50, height=50)\n\nap.save_overall_html(\n    dest_dir_path=\'graphics_begin_fill_acceptable_color_settings/\')\n```':  # noqa
    '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    background_color=\'#333\',\n    stage_width=450,\n    stage_height=150,\n    stage_elem_id=\'stage\')\nsprite: ap.Sprite = ap.Sprite()\n\n# Six characters fill color setting (a cyan color).\nsprite.graphics.begin_fill(color=\'#00aaff\')\nsprite.graphics.draw_rect(\n    x=50, y=50, width=50, height=50)\n\n# Three characters fill color setting (a magenta color).\nsprite.graphics.begin_fill(color=\'#f0a\')\nsprite.graphics.draw_rect(\n    x=150, y=50, width=50, height=50)\n\n# Single characters fill color setting (a black color).\nsprite.graphics.begin_fill(color=\'#0\')\nsprite.graphics.draw_rect(\n    x=250, y=50, width=50, height=50)\n\n# Fill color that Skipped `#` symbol is also acceptable.\nsprite.graphics.begin_fill(color=\'999\')\nsprite.graphics.draw_rect(\n    x=350, y=50, width=50, height=50)\n\nap.save_overall_html(\n    dest_dir_path=\'graphics_begin_fill_acceptable_color_settings/\')\n```',  # noqa

    '## Fill color alpha (opacity) setting':
    '## 塗りの色の透明度の設定',

    'Fill color alpha (opacity) can be set by the `alpha` argument. It can accept 0.0 (transparent) to 1.0 (opaque).':  # noqa
    '塗りの透明度は`alpha`引数で設定できます。0.0（透明）～1.0（不透明）の範囲の値を受け付けます。',

    '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    background_color=\'#333\',\n    stage_width=200,\n    stage_height=200,\n    stage_elem_id=\'stage\')\nsprite: ap.Sprite = ap.Sprite()\n\nsprite.graphics.begin_fill(color=\'#00aaff\', alpha=0.2)\nsprite.graphics.draw_rect(\n    x=50, y=75, width=50, height=50)\nsprite.graphics.draw_rect(\n    x=75, y=50, width=50, height=50)\nsprite.graphics.draw_rect(\n    x=75, y=75, width=50, height=50)\nsprite.graphics.draw_rect(\n    x=75, y=100, width=50, height=50)\nsprite.graphics.draw_rect(\n    x=100, y=75, width=50, height=50)\n\nap.save_overall_html(\n    dest_dir_path=\'graphics_begin_fill_alpha_setting/\')\n```':  # noqa
    '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    background_color=\'#333\',\n    stage_width=200,\n    stage_height=200,\n    stage_elem_id=\'stage\')\nsprite: ap.Sprite = ap.Sprite()\n\nsprite.graphics.begin_fill(color=\'#00aaff\', alpha=0.2)\nsprite.graphics.draw_rect(\n    x=50, y=75, width=50, height=50)\nsprite.graphics.draw_rect(\n    x=75, y=50, width=50, height=50)\nsprite.graphics.draw_rect(\n    x=75, y=75, width=50, height=50)\nsprite.graphics.draw_rect(\n    x=75, y=100, width=50, height=50)\nsprite.graphics.draw_rect(\n    x=100, y=75, width=50, height=50)\n\nap.save_overall_html(\n    dest_dir_path=\'graphics_begin_fill_alpha_setting/\')\n```',  # noqa

    '## begin_fill API':
    '## begin_fill API',

    '<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>':  # noqa
    '<span class="inconspicuous-txt">特記事項: このAPIドキュメントはドキュメントビルド用のスクリプトによって自動で生成・同期されています。そのためもしかしたらこの節の内容は前節までの内容と重複している場合があります。</span>',  # noqa

    '**[Interface summary]** Set single color value for fill.<hr>':
    '**[インターフェイス概要]** 塗りのための単一の色の設定を行います。<hr>',

    '**[Parameters]**':
    '**[引数]**',

    '- `color`: str or String':
    '- `color`: str or String',

    '  - Hexadecimal color string. e.g., \'#00aaff\'':
    '  - \'#00aaff\'などの16進数の色の文字列。',

    '- `alpha`: float or Number, default 1.0':
    '- `alpha`: float or Number, default 1.0',

    '  - Color opacity (0.0 to 1.0).':
    '  - 塗りの透明度（0.0～1.0）。',

    '<hr>':
    '<hr>',

    '**[Examples]**':
    '**[コードサンプル]**',

    '```py\n>>> import apysc as ap\n>>> stage: ap.Stage = ap.Stage()\n>>> sprite: ap.Sprite = ap.Sprite()\n>>> sprite.graphics.begin_fill(color=\'#0af\')\n>>> rectangle: ap.Rectangle = sprite.graphics.draw_rect(\n...     x=50, y=50, width=50, height=50)\n>>> rectangle.fill_color\nString(\'#00aaff\')\n```':  # noqa
    '```py\n>>> import apysc as ap\n>>> stage: ap.Stage = ap.Stage()\n>>> sprite: ap.Sprite = ap.Sprite()\n>>> sprite.graphics.begin_fill(color=\'#0af\')\n>>> rectangle: ap.Rectangle = sprite.graphics.draw_rect(\n...     x=50, y=50, width=50, height=50)\n>>> rectangle.fill_color\nString(\'#00aaff\')\n```',  # noqa

    '## fill_color property API':
    '## fill_color 属性のAPI',

    '<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>':  # noqa
    '<span class="inconspicuous-txt">特記事項: このAPIドキュメントはドキュメントビルド用のスクリプトによって自動で生成・同期されています。そのためもしかしたらこの節の内容は前節までの内容と重複している場合があります。</span>',  # noqa

    '**[Interface summary]** Get current fill color.<hr>':
    '**[インターフェイス概要]** 現在の塗りの色を取得します。<hr>',

    '**[Returns]**':
    '**[返却値]**',

    '- `fill_color`: String':
    '- `fill_color`: String',

    '  - Current fill color (hexadecimal string, e.g., \'#00aaff\'). If not be set, this interface returns a blank string.':  # noqa
    '  - 現在の塗りの色（`\'#00aaff\'`などの16進数の文字列）。もしも設定されていない場合空文字が返却されます。',

    '<hr>':
    '<hr>',

    '**[Examples]**':
    '**[コードサンプル]**',

    '```py\n>>> import apysc as ap\n>>> stage: ap.Stage = ap.Stage()\n>>> sprite: ap.Sprite = ap.Sprite()\n>>> sprite.graphics.begin_fill(color=\'#0af\')\n>>> rectangle: ap.Rectangle = sprite.graphics.draw_rect(\n...     x=50, y=50, width=50, height=50)\n>>> rectangle.fill_color\nString(\'#00aaff\')\n```':  # noqa
    '```py\n>>> import apysc as ap\n>>> stage: ap.Stage = ap.Stage()\n>>> sprite: ap.Sprite = ap.Sprite()\n>>> sprite.graphics.begin_fill(color=\'#0af\')\n>>> rectangle: ap.Rectangle = sprite.graphics.draw_rect(\n...     x=50, y=50, width=50, height=50)\n>>> rectangle.fill_color\nString(\'#00aaff\')\n```',  # noqa

    '## fill_alpha property API':
    '## fill_alpha 属性のAPI',

    '<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>':  # noqa
    '<span class="inconspicuous-txt">特記事項: このAPIドキュメントはドキュメントビルド用のスクリプトによって自動で生成・同期されています。そのためもしかしたらこの節の内容は前節までの内容と重複している場合があります。</span>',  # noqa

    '**[Interface summary]** Get current fill color opacity.<hr>':
    '**[インターフェイス概要]** 現在の塗りの透明度を取得します。<hr>',

    '**[Returns]**':
    '**[返却値]**',

    '- `fill_alpha`: Number':
    '- `fill_alpha`: Number',

    '  - Current fill color opacity (0.0 to 1.0). If not be set, 1.0 will be returned.':  # noqa
    '  - 現在の塗りの透明度（0.0～1.0）。もし設定されていない場合1.0の値が返却されます。',

    '<hr>':
    '<hr>',

    '**[Examples]**':
    '**[コードサンプル]**',

    '```py\n>>> import apysc as ap\n>>> stage: ap.Stage = ap.Stage()\n>>> sprite: ap.Sprite = ap.Sprite()\n>>> sprite.graphics.begin_fill(color=\'#0af\', alpha=0.5)\n>>> rectangle: ap.Rectangle = sprite.graphics.draw_rect(\n...     x=50, y=50, width=50, height=50)\n>>> rectangle.fill_alpha\nNumber(0.5)\n```':  # noqa
    '```py\n>>> import apysc as ap\n>>> stage: ap.Stage = ap.Stage()\n>>> sprite: ap.Sprite = ap.Sprite()\n>>> sprite.graphics.begin_fill(color=\'#0af\', alpha=0.5)\n>>> rectangle: ap.Rectangle = sprite.graphics.draw_rect(\n...     x=50, y=50, width=50, height=50)\n>>> rectangle.fill_alpha\nNumber(0.5)\n```',  # noqa

}
