"""This module is for the translation mapping data of the
following document:

Document file: trace.md
Language: jp
"""

from typing import Dict

MAPPING: Dict[str, str] = {
    ##################################################
    "# trace interface": "# trace インターフェイス",
    ##################################################
    "This page explains the `trace` function interface.": "このページでは`trace`関数のインターフェイスについて説明します。",  # noqa
    ##################################################
    "## What interface is this?": "## インターフェイス概要",
    ##################################################
    "The `trace` function interface displays any message on the browser console. This interface behaves like the JavaScript `console.log` function.": "`trace`関数のインターフェイスは任意のメッセージをブラウザのコンソール上に表示します。このインターフェイスはJavaScriptの`console.log`の関数と同じような挙動をします。",  # noqa
    ##################################################
    "Also, this interface displays Python's file name, caller information, and line number.": "また、このインターフェイスはPythonのファイル名、呼び出し元の情報、行番号などの情報も表示します。",  # noqa
    ##################################################
    "## Note for the print alias": "## print関数のエイリアスに対する特記事項",
    ##################################################
    "The `ap.print` function is the alias of the `trace` function. Therefore, It behaves the same as the `trace` function.": "`ap.print`関数は`trace`関数のエイリアスとなります。そのため、その関数は`trace`関数と同じように動作します。",  # noqa
    ##################################################
    "## Basic usage": "## 基本的な使い方",
    ##################################################
    "The `trace` function can accept any number of arguments and various value types.": "`trace`関数は任意の数の引数を受け付け、そして様々な型の値を指定することができます。",  # noqa
    ##################################################
    "The following example draws the rectangle. Then, the handler displays the message on the browser console when you click it(please press the F12 key).": "伊賀のコード例では四角を描画し、四角をクリックした際にブラウザのコンソール上にメッセージを表示するようにしています（F12キーを押してコンソールを開いてご確認ください）。",  # noqa
    ##################################################
    '```py\n# runnable\nimport apysc as ap\n\n\ndef on_rectangle_click(e: ap.MouseEvent[ap.Rectangle], options: dict) -> None:\n    """\n    The handler that the rectangle calls when clicked.\n\n    Parameters\n    ----------\n    e : MouseEvent\n        Event instance.\n    options : dict\n        Optional arguments dictionary.\n    """\n    ap.trace("Hello apysc!", "Rectangle width:", e.this.width)\n\n\nap.Stage(\n    stage_width=150, stage_height=150, background_color="#333", stage_elem_id="stage"\n)\nsprite: ap.Sprite = ap.Sprite()\nsprite.graphics.begin_fill(color="#0af")\nrectangle: ap.Rectangle = sprite.graphics.draw_rect(x=50, y=50, width=50, height=50)\nrectangle.click(on_rectangle_click)\n\nap.save_overall_html(dest_dir_path="trace_basic_usage/")\n```': '```py\n# runnable\nimport apysc as ap\n\n\ndef on_rectangle_click(e: ap.MouseEvent[ap.Rectangle], options: dict) -> None:\n    """\n    The handler that the rectangle calls when clicked.\n\n    Parameters\n    ----------\n    e : MouseEvent\n        Event instance.\n    options : dict\n        Optional arguments dictionary.\n    """\n    ap.trace("Hello apysc!", "Rectangle width:", e.this.width)\n\n\nap.Stage(\n    stage_width=150, stage_height=150, background_color="#333", stage_elem_id="stage"\n)\nsprite: ap.Sprite = ap.Sprite()\nsprite.graphics.begin_fill(color="#0af")\nrectangle: ap.Rectangle = sprite.graphics.draw_rect(x=50, y=50, width=50, height=50)\nrectangle.click(on_rectangle_click)\n\nap.save_overall_html(dest_dir_path="trace_basic_usage/")\n```',  # noqa
    ##################################################
    "## trace API": "## trace API",
    ##################################################
    '<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>': '<span class="inconspicuous-txt">特記事項: このAPIドキュメントはドキュメントビルド用のスクリプトによって自動で生成・同期されています。そのためもしかしたらこの節の内容は前節までの内容と重複している場合があります。</span>',  # noqa
    ##################################################
    "**[Interface summary]**": "**[インターフェイス概要]**",
    ##################################################
    "Display arguments information to console. This function saves a JavaScript `console.log` expression.<hr>": "引数に指定された値の情報をコンソールへ表示します。この関数はJavaScriptの`console.log`に該当するコードを保存します。<hr>",  # noqa
    ##################################################
    "**[Parameters]**": "**[引数]**",
    ##################################################
    "- `*args`: list": "- `*args`: list",
    ##################################################
    "  - Any arguments to display to console.": "  - コンソール上に表示する任意の引数の値。",
    ##################################################
    "<hr>": "<hr>",
    ##################################################
    "**[Notes]**": "**[特記事項]**",
    ##################################################
    "The `ap.print` function is the alias of the `trace` function.<hr>": "`ap.print`関数は`trace`関数のエイリアスとなります。<hr>",  # noqa
    ##################################################
    "**[Examples]**": "**[コードサンプル]**",
    ##################################################
    '```py\n>>> import apysc as ap\n>>> int_val: ap.Int = ap.Int(10)\n>>> ap.trace("Int value is:", int_val)\n```': '```py\n>>> import apysc as ap\n>>> int_val: ap.Int = ap.Int(10)\n>>> ap.trace("Int value is:", int_val)\n```',  # noqa
}
