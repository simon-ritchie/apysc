"""This module is for the translation mapping data of the
following document:

Document file: return.md
Language: jp
"""

from typing import Dict

MAPPING: Dict[str, str] = {
    ##################################################
    "# Return class": "# Return クラス",
    ##################################################
    "This page explains the `Return` class.": "このページでは`Return`クラスについて説明します。",
    ##################################################
    "Before reading on, maybe it is helpful to read the following page (the apysc uses the `Return` class for the same reason of each apysc data type):": "このページを読み進める前に以下のページを確認しておくと役に立つかもしれません（apyscライブラリでは`Return`クラスを各データクラスと同じような理由で使用しています）。",  # noqa
    ##################################################
    "- [Why the apysc library doesn't use the Python built-in data type](why_apysc_doesnt_use_python_builtin_data_type.md)": "- [なぜapyscではPythonのビルトインのデータの型を使用していないのか](jp_why_apysc_doesnt_use_python_builtin_data_type.md)",  # noqa
    ##################################################
    "## What is the Return class?": "## Return クラスの概要",
    ##################################################
    "The `Return` class behaves to append the `return;` JavaScript code. Therefore, this class can be used only in an event handler (function or method) scope.": "`Return`クラスはJavaScriptの`return;`のコードのように振る舞います。従って、このクラスはイベントハンドラの関数もしくはメソッド内のスコープでのみ使用することができます。",  # noqa
    ##################################################
    "## Basic usage": "## 基本的な使い方",
    ##################################################
    "The `Return` class constructor accepts no arguments. You can use this interface with the branch condition, for example, the `ap.If` class.": "`Return`クラスのコンストラクタは引数を必要としません。このクラスは`ap.If`などの条件分岐の記述内などで使うことができます。",  # noqa
    ##################################################
    "The following example changes the rectangle fill color when you click it. Each `ap.If` branch instantiate `Return` class, so the code applies the changing of fill color one by one:": "以下のコード例では四角をクリックするたびに塗りの色を変更しています。各`ap.If`での分岐内では`Return`クラスを使用しているため、1回のクリックでは1回の色変更のみ行われます:",  # noqa
    ##################################################
    '```py\n# runnable\nimport apysc as ap\n\n\ndef on_click(e: ap.MouseEvent[ap.Rectangle], options: dict) -> None:\n    """\n    The handler that the rectangle calls when clicked.\n\n    Parameters\n    ----------\n    e : ap.MouseEvent\n        Event instance.\n    options : dict\n        Optional arguments dictionary.\n    """\n    rectangle: ap.Rectangle = e.this\n    fill_color: ap.Color = rectangle.fill_color\n    with ap.If(fill_color == ap.Color("#00aaff")):\n        rectangle.fill_color = ap.Color("#ff00aa")\n        ap.Return()\n    with ap.If(fill_color == ap.Color("#ff00aa")):\n        rectangle.fill_color = ap.Color("#00ffaa")\n        ap.Return()\n    with ap.If(fill_color == ap.Color("#00ffaa")):\n        rectangle.fill_color = ap.Color("#00aaff")\n        ap.Return()\n\n\nap.Stage(\n    stage_width=150,\n    stage_height=150,\n    background_color=ap.Color("#333"),\n    stage_elem_id="stage",\n)\nsprite: ap.Sprite = ap.Sprite()\nsprite.graphics.begin_fill(color=ap.Color("#00aaff"))\nrectangle: ap.Rectangle = sprite.graphics.draw_rect(x=50, y=50, width=50, height=50)\nrectangle.click(on_click)\n\nap.save_overall_html(dest_dir_path="return_basic_usage/")\n```': '```py\n# runnable\nimport apysc as ap\n\n\ndef on_click(e: ap.MouseEvent[ap.Rectangle], options: dict) -> None:\n    """\n    The handler that the rectangle calls when clicked.\n\n    Parameters\n    ----------\n    e : ap.MouseEvent\n        Event instance.\n    options : dict\n        Optional arguments dictionary.\n    """\n    rectangle: ap.Rectangle = e.this\n    fill_color: ap.Color = rectangle.fill_color\n    with ap.If(fill_color == ap.Color("#00aaff")):\n        rectangle.fill_color = ap.Color("#ff00aa")\n        ap.Return()\n    with ap.If(fill_color == ap.Color("#ff00aa")):\n        rectangle.fill_color = ap.Color("#00ffaa")\n        ap.Return()\n    with ap.If(fill_color == ap.Color("#00ffaa")):\n        rectangle.fill_color = ap.Color("#00aaff")\n        ap.Return()\n\n\nap.Stage(\n    stage_width=150,\n    stage_height=150,\n    background_color=ap.Color("#333"),\n    stage_elem_id="stage",\n)\nsprite: ap.Sprite = ap.Sprite()\nsprite.graphics.begin_fill(color=ap.Color("#00aaff"))\nrectangle: ap.Rectangle = sprite.graphics.draw_rect(x=50, y=50, width=50, height=50)\nrectangle.click(on_click)\n\nap.save_overall_html(dest_dir_path="return_basic_usage/")\n```',  # noqa
    ##################################################
    "## Return API": "## Return API",
    ##################################################
    '<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>': '<span class="inconspicuous-txt">特記事項: このAPIドキュメントはドキュメントビルド用のスクリプトによって自動で生成・同期されています。そのためもしかしたらこの節の内容は前節までの内容と重複している場合があります。</span>',  # noqa
    ##################################################
    "**[Interface summary]**": "**[インターフェイス概要]**",
    ##################################################
    "Class for the return expression.<hr>": "return のコード表現のためのクラスです。<hr>",
    ##################################################
    "**[Notes]**": "**[特記事項]**",
    ##################################################
    "This class can be instantiated only in an event handler scope.<hr>": "このクラスはイベントハンドラのスコープ内でのみインスタンス化することができます。<hr>",  # noqa
    ##################################################
    "**[Examples]**": "**[コードサンプル]**",
    ##################################################
    "```py\n>>> import apysc as ap\n>>> def on_timer(e: ap.TimerEvent, options: dict) -> None:\n...     '''\n...     The handler that the timer calls.\n...\n```": "```py\n>>> import apysc as ap\n>>> def on_timer(e: ap.TimerEvent, options: dict) -> None:\n...     '''\n...     The handler that the timer calls.\n...\n```",  # noqa
}
