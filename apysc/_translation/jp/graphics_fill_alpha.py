"""This module is for the translation mapping data of the
following document:

Document file: graphics_fill_alpha.md
Language: jp
"""

from typing import Dict

MAPPING: Dict[str, str] = {

    '# Graphics fill_alpha interface':
    '# Graphics クラスの fill_alpha インターフェイス',

    'This page explains the `Graphics` class `fill_alpha` property interface.':  # noqa
    'このページでは`Graphics`クラスの`fill_alpha`属性のインターフェイスについて説明します。',

    '## What interface is this?':
    '## インターフェイス概要',

    'The `fill_alpha` property interface updates or get the instance\'s fill alpha (opacity).':  # noqa
    '`fill_alpha`属性のインターフェイスではインスタンスの塗りの透明度更新や取得を行うことができます。',

    '## Basic usage':
    '## 基本的な使い方',

    'The getter or setter interface value becomes (or require) the `Number` value (0.0 to 1.0).':  # noqa
    '属性のgetterとsetterのインターフェイスの値は`Number`型の値となります（0.0～1.0）。',

    'The following example sets the 0.5 fill alpha to the second rectangle and 0.25 to the third rectangle:':  # noqa
    '以下のコード例では2つ目の四角に0.5の透明度を、そして3つ目の四角に0.25の透明度を設定しています:',

    '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    stage_width=350, stage_height=150, background_color=\'#333\',\n    stage_elem_id=\'stage\')\nsprite: ap.Sprite = ap.Sprite()\nsprite.graphics.begin_fill(color=\'#0af\')\n\nrectangle_1: ap.Rectangle = sprite.graphics.draw_rect(\n    x=50, y=50, width=50, height=50)\n\nrectangle_2: ap.Rectangle = sprite.graphics.draw_rect(\n    x=150, y=50, width=50, height=50)\nrectangle_2.fill_alpha = ap.Number(0.5)\n\nrectangle_3: ap.Rectangle = sprite.graphics.draw_rect(\n    x=250, y=50, width=50, height=50)\nrectangle_3.fill_alpha = ap.Number(0.25)\n\nap.save_overall_html(\n    dest_dir_path=\'./graphics_fill_alpha_basic_usage/\')\n```':  # noqa
    '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    stage_width=350, stage_height=150, background_color=\'#333\',\n    stage_elem_id=\'stage\')\nsprite: ap.Sprite = ap.Sprite()\nsprite.graphics.begin_fill(color=\'#0af\')\n\nrectangle_1: ap.Rectangle = sprite.graphics.draw_rect(\n    x=50, y=50, width=50, height=50)\n\nrectangle_2: ap.Rectangle = sprite.graphics.draw_rect(\n    x=150, y=50, width=50, height=50)\nrectangle_2.fill_alpha = ap.Number(0.5)\n\nrectangle_3: ap.Rectangle = sprite.graphics.draw_rect(\n    x=250, y=50, width=50, height=50)\nrectangle_3.fill_alpha = ap.Number(0.25)\n\nap.save_overall_html(\n    dest_dir_path=\'./graphics_fill_alpha_basic_usage/\')\n```',  # noqa

    '## fill_alpha property API':
    '## fill_alpha 属性のAPI',

    '<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>':  # noqa
    '<span class="inconspicuous-txt">特記事項: このAPIドキュメントはドキュメントビルド用のスクリプトによって自動で生成・同期されています。そのためもしかしたらこの節の内容は前節までの内容と重複している場合があります。</span>',  # noqa

    '**[Interface summary]** Get this instance\'s fill opacity.<hr>':
    '**[インターフェイス概要]** このインスタンスの塗りの透明度を取得します。<hr>',

    '**[Returns]**':
    '**[返却値]**',

    '- `fill_alpha`: Number':
    '- `fill_alpha`: Number',

    '  - Current fill opacity (0.0 to 1.0).':
    '  - 現在の塗りの透明度（0.0～1.0）。',

    '<hr>':
    '<hr>',

    '**[Examples]**':
    '**[コードサンプル]**',

    '```py\n>>> import apysc as ap\n>>> stage: ap.Stage = ap.Stage()\n>>> sprite: ap.Sprite = ap.Sprite()\n>>> sprite.graphics.begin_fill(color=\'#0af\')\n>>> rectangle: ap.Rectangle = sprite.graphics.draw_rect(\n...     x=50, y=50, width=50, height=50)\n>>> rectangle.fill_alpha = ap.Number(0.5)\n>>> rectangle.fill_alpha\nNumber(0.5)\n```':  # noqa
    '```py\n>>> import apysc as ap\n>>> stage: ap.Stage = ap.Stage()\n>>> sprite: ap.Sprite = ap.Sprite()\n>>> sprite.graphics.begin_fill(color=\'#0af\')\n>>> rectangle: ap.Rectangle = sprite.graphics.draw_rect(\n...     x=50, y=50, width=50, height=50)\n>>> rectangle.fill_alpha = ap.Number(0.5)\n>>> rectangle.fill_alpha\nNumber(0.5)\n```',  # noqa

}
