"""This module is for the translation mapping data of the
following document:

Document file: trace.md
Language: jp
"""

from typing import Dict

MAPPING: Dict[str, str] = {
    ##################################################
    "# trace interface":
    "# trace インターフェイス",
    ##################################################
    "This page explains the `trace` function interface.":
    "このページでは`trace`関数のインターフェイスについて説明します。",
    ##################################################
    "## What interface is this?":
    "## インターフェイス概要",
    ##################################################
    "The `trace` function interface displays any message on the browser console. This interface behaves like the JavaScript `console.log` function.":  # noqa
    "`trace`関数のインターフェイスは任意のメッセージをブラウザのコンソール上に表示します。このインターフェイスはJavaScriptの`console.log`の関数と同じような挙動をします。",  # noqa
    ##################################################
    "## Basic usage":
    "## 基本的な使い方",
    ##################################################
    "The `trace` function can accept any number of arguments and various value types.":  # noqa
    "`trace`関数は任意の数の引数を受け付け、そして様々な型の値を指定することができます。",
    ##################################################
    "The following example draws the rectangle. Then, the handler displays the message on the browser console when you click it(please press the F12 key).":  # noqa
    "伊賀のコード例では四角を描画し、四角をクリックした際にブラウザのコンソール上にメッセージを表示するようにしています（F12キーを押してコンソールを開いてご確認ください）。",  # noqa
    ##################################################
    "```py\n# runnable\nimport apysc as ap\n\n\ndef on_rectangle_click(\n        e: ap.MouseEvent[ap.Rectangle], options: dict) -> None:\n    \"\"\"\n    The handler that the rectangle calls when clicked.\n\n    Parameters\n    ----------\n    e : MouseEvent\n        Event instance.\n    options : dict\n        Optional arguments dictionary.\n    \"\"\"\n    ap.trace(\'Hello apysc!\', \'Rectangle width:\', e.this.width)\n\n\nap.Stage(\n    stage_width=150, stage_height=150, background_color=\'#333\',\n    stage_elem_id=\'stage\')\nsprite: ap.Sprite = ap.Sprite()\nsprite.graphics.begin_fill(color=\'#0af\')\nrectangle: ap.Rectangle = sprite.graphics.draw_rect(\n    x=50, y=50, width=50, height=50)\nrectangle.click(on_rectangle_click)\n\nap.save_overall_html(\n    dest_dir_path=\'trace_basic_usage/\')\n```":  # noqa
    "```py\n# runnable\nimport apysc as ap\n\n\ndef on_rectangle_click(\n        e: ap.MouseEvent[ap.Rectangle], options: dict) -> None:\n    \"\"\"\n    The handler that the rectangle calls when clicked.\n\n    Parameters\n    ----------\n    e : MouseEvent\n        Event instance.\n    options : dict\n        Optional arguments dictionary.\n    \"\"\"\n    ap.trace(\'Hello apysc!\', \'Rectangle width:\', e.this.width)\n\n\nap.Stage(\n    stage_width=150, stage_height=150, background_color=\'#333\',\n    stage_elem_id=\'stage\')\nsprite: ap.Sprite = ap.Sprite()\nsprite.graphics.begin_fill(color=\'#0af\')\nrectangle: ap.Rectangle = sprite.graphics.draw_rect(\n    x=50, y=50, width=50, height=50)\nrectangle.click(on_rectangle_click)\n\nap.save_overall_html(\n    dest_dir_path=\'trace_basic_usage/\')\n```",  # noqa
    ##################################################
    "## trace API":
    "## trace API",
    ##################################################
    "<span class=\"inconspicuous-txt\">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>":  # noqa
    "<span class=\"inconspicuous-txt\">特記事項: このAPIドキュメントはドキュメントビルド用のスクリプトによって自動で生成・同期されています。そのためもしかしたらこの節の内容は前節までの内容と重複している場合があります。</span>",  # noqa
    ##################################################
    "**[Interface summary]** Display arguments information to console. This function saves a JavaScript `console.log` expression.<hr>":  # noqa
    "**[インターフェイス概要]** 引数に指定された値の情報をコンソールへ表示します。この関数はJavaScriptの`console.log`に該当するコードを保存します。<hr>",  # noqa
    ##################################################
    "**[Parameters]**":
    "**[引数]**",
    ##################################################
    "- `*args`: list":
    "- `*args`: list",
    ##################################################
    "  - Any arguments to display to console.":
    "  - コンソール上に表示する任意の引数の値。",
    ##################################################
    "<hr>":
    "<hr>",
    ##################################################
    "**[Examples]**":
    "**[コードサンプル]**",
    ##################################################
    "```py\n>>> import apysc as ap\n>>> int_val: ap.Int = ap.Int(10)\n>>> ap.trace(\'Int value is:\', int_val)\n```":  # noqa
    "```py\n>>> import apysc as ap\n>>> int_val: ap.Int = ap.Int(10)\n>>> ap.trace(\'Int value is:\', int_val)\n```",  # noqa
}
