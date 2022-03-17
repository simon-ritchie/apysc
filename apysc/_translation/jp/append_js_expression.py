"""This module is for the translation mapping data of the
following document:

Document file: append_js_expression.md
Language: jp
"""

from typing import Dict

MAPPING: Dict[str, str] = {

    '# append_js_expression interface':
    '# append_js_expression インターフェイス',

    'This page explains the `append_js_expression` function interface.':
    'このページでは`append_js_expression`関数のインターフェイスについて説明します。',

    '## What interface is this?':
    '## インターフェイス概要',

    'The `append_js_expression` function interface appends any JavaScript to the exported HTML at any position. This interface may be helpful if you need to use the apysc not supported interfaces or irregular JavaScript implementation, like the Django template tags or parameters (e.g., `{% if ... %}`).':  # noqa
    '`append_js_expression`関数は出力先のHTMLの任意の場所にJavaScriptのコードを追加します。このインターフェイスはapyscがサポートしていない特殊な処理などを追加する際などに役に立つことがあります（Djangoなどのライブラリでテンプレートタグなどを独自の出力したい場合など）。',  # noqa

    '## Basic usage':
    '## 基本的な使い方',

    'The `append_js_expression` function requires JavaScript string at the argument.':  # noqa
    '`append_js_expression`関数は引数にJavaScriptのコードの文字列が必要とします。',

    'The following example appends the `console.log` JavaScript calling at the rectangle click handler:':  # noqa
    '以下のコード例では四角をクリックした際のハンドラ内で`console.log`のJavaScriptの関数呼び出しのコードを追加しています。',  # noqa

    '```py\n# runnable\nimport apysc as ap\n\n\ndef on_click(\n        e: ap.MouseEvent[ap.Rectangle], options: dict) -> None:\n    """\n    The handler that the animation calls when its end.\n\n    Parameters\n    ----------\n    e : ap.MouseEvent\n        Event instance.\n    options : dict\n        Optional arguments dictionary.\n    """\n    ap.append_js_expression(\n        expression=\'console.log("The rectangle is clicked!");\')\n\n\nap.Stage(\n    stage_width=150, stage_height=150, background_color=\'#333\',\n    stage_elem_id=\'stage\')\nsprite: ap.Sprite = ap.Sprite()\nsprite.graphics.begin_fill(color=\'#0af\')\nrectangle: ap.Rectangle = sprite.graphics.draw_rect(\n    x=50, y=50, width=50, height=50)\nrectangle.click(on_click)\n\nap.save_overall_html(\n    dest_dir_path=\'append_js_expression_basic_usage/\')\n```':  # noqa
    '```py\n# runnable\nimport apysc as ap\n\n\ndef on_click(\n        e: ap.MouseEvent[ap.Rectangle], options: dict) -> None:\n    """\n    The handler that the animation calls when its end.\n\n    Parameters\n    ----------\n    e : ap.MouseEvent\n        Event instance.\n    options : dict\n        Optional arguments dictionary.\n    """\n    ap.append_js_expression(\n        expression=\'console.log("The rectangle is clicked!");\')\n\n\nap.Stage(\n    stage_width=150, stage_height=150, background_color=\'#333\',\n    stage_elem_id=\'stage\')\nsprite: ap.Sprite = ap.Sprite()\nsprite.graphics.begin_fill(color=\'#0af\')\nrectangle: ap.Rectangle = sprite.graphics.draw_rect(\n    x=50, y=50, width=50, height=50)\nrectangle.click(on_click)\n\nap.save_overall_html(\n    dest_dir_path=\'append_js_expression_basic_usage/\')\n```',  # noqa

    'If you click the following rectangle, the handler displays the `The rectangle is clicked!` message on the browser console (please press the F12 key).':  # noqa
    '四角をクリックすると`The rectangle is clicked!`というメッセージがブラウザのコンソールに表示されます（F12キーを押して確認してください）。',  # noqa

    '## append_js_expression API':
    '## append_js_expression API',

    '<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>':  # noqa
    '<span class="inconspicuous-txt">特記事項: このAPIドキュメントはドキュメントビルド用のスクリプトによって自動で生成・同期されています。そのためもしかしたらこの節の内容は前節までの内容と重複している場合があります。</span>',  # noqa

    '**[Interface summary]** Append js expression.<hr>':
    '**[インターフェイス概要]** JavaScriptのコード表現の記述を結果のHTMLへ追加します。<hr>',

    '**[Parameters]**':
    '**[引数]**',

    '- `expression`: str':
    '- `expression`: str',

    '  - JavaScript Expression string.':
    '  - 追加対象のJavaScriptのコードの文字列。',

    '<hr>':
    '<hr>',

    '**[Examples]**':
    '**[コードサンプル]**',

    '```py\n>>> import apysc as ap\n>>> ap.append_js_expression(expression=\'console.log("Hello!")\')\n```':  # noqa
    '```py\n>>> import apysc as ap\n>>> ap.append_js_expression(expression=\'console.log("Hello!")\')\n```',  # noqa

}
