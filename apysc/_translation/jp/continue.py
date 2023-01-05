"""This module is for the translation mapping data of the
following document:

Document file: continue.md
Language: jp
"""

from typing import Dict

MAPPING: Dict[str, str] = {
    ##################################################
    "# Continue class": "# Continue クラス",
    ##################################################
    "This page explains the `Continue` class.": "このページでは`Continue`クラスについて説明します。",
    ##################################################
    "Before reading on, maybe it is helpful to read the following page (apysc uses the `Continue` class for the same reason):": "このページを読み進める前に以下のページを確認しておくと役に立つかもしれません（apyscでは`Continue`クラスを同様の利用で使用しています）。",  # noqa
    ##################################################
    "- [Why the apysc library doesn't use the Python built-in data type](why_apysc_doesnt_use_python_builtin_data_type.md)": "- [なぜapyscではPythonのビルトインのデータの型を使用していないのか](jp_why_apysc_doesnt_use_python_builtin_data_type.md)",  # noqa
    ##################################################
    "## What is the Continue class?": "## Continue クラスの概要",
    ##################################################
    "The `with For` block uses the `Continue` class to skip a current loop iteration (in JavaScript). It behaves like the Python built-in `continue` keyword.": "`with For`のブロックではJavaScript上での特定のループをスキップするために`Continue`クラスが使用されます。このインターフェイスはPythonビルトインの`continue`キーワードのように動作します。",  # noqa
    ##################################################
    "## Basic usage": "## 基本的な使い方",
    ##################################################
    "The `Continue` class can only be used in the `with For` (or other loop class) block, as follows:": "`Continue`クラスは以下のコード例のように`with For`（もしくは他のループクラス）のブロックでのみ使用することができます:",  # noqa
    ##################################################
    '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    stage_width=250, stage_height=150, background_color="#333", stage_elem_id="stage"\n)\nsprite: ap.Sprite = ap.Sprite()\n\narr: ap.Array = ap.Array(range(2))\ni: ap.Int\nwith ap.For(arr) as i:\n    condition: ap.Boolean = i == 0\n    with ap.If(condition):\n        sprite.graphics.begin_fill(color="#0af")\n        sprite.graphics.draw_rect(x=50, y=50, width=50, height=50)\n        ap.Continue()\n\n    sprite.graphics.begin_fill(color="#f0a")\n    sprite.graphics.draw_rect(x=150, y=50, width=50, height=50)\n\nap.save_overall_html(dest_dir_path="continue_basic_usage/")\n```': '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    stage_width=250, stage_height=150, background_color="#333", stage_elem_id="stage"\n)\nsprite: ap.Sprite = ap.Sprite()\n\narr: ap.Array = ap.Array(range(2))\ni: ap.Int\nwith ap.For(arr) as i:\n    condition: ap.Boolean = i == 0\n    with ap.If(condition):\n        sprite.graphics.begin_fill(color="#0af")\n        sprite.graphics.draw_rect(x=50, y=50, width=50, height=50)\n        ap.Continue()\n\n    sprite.graphics.begin_fill(color="#f0a")\n    sprite.graphics.draw_rect(x=150, y=50, width=50, height=50)\n\nap.save_overall_html(dest_dir_path="continue_basic_usage/")\n```',  # noqa
    ##################################################
    "If you use the `Continue` class in the out of the `with For` block, then an exception is raised:": "もし`Continue`クラスを`with For`ブロック外で使用した場合はエラーになります:",  # noqa
    ##################################################
    "```py\nimport apysc as ap\n\nap.Continue()\n```": "```py\nimport apysc as ap\n\nap.Continue()\n```",  # noqa
    ##################################################
    "```\nException: The `Continue` class can be instantiated in the with loop statement, for example, after the `with ap.For(...):` statement.\n```": "```\nException: The `Continue` class can be instantiated in the with loop statement, for example, after the `with ap.For(...):` statement.\n```",  # noqa
    ##################################################
    "## Continue API": "## Continue API",
    ##################################################
    '<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>': '<span class="inconspicuous-txt">特記事項: このAPIドキュメントはドキュメントビルド用のスクリプトによって自動で生成・同期されています。そのためもしかしたらこの節の内容は前節までの内容と重複している場合があります。</span>',  # noqa
    ##################################################
    "**[Interface summary]**": "**[インターフェイス概要]**",
    ##################################################
    "The loop continue expression class.<hr>": "ループのcontinueの表現を扱うためのクラスです。<hr>",
    ##################################################
    "**[Notes]**": "**[特記事項]**",
    ##################################################
    "This class can be instantiated in the with loop statement, for example, after the `with ap.For(...):` statement.<hr>": "このクラスはwithステートメントのループ内でのみインスタンス化することができます。例えば`with ap.For(...)ステート内が該当します。`<hr>",  # noqa
    ##################################################
    "**[Examples]**": "**[コードサンプル]**",
    ##################################################
    "```py\n>>> import apysc as ap\n>>> arr: ap.Array = ap.Array(range(3))\n>>> with ap.For(arr) as i:\n...     with ap.If(i == 1):\n...         _ = ap.Continue()\n...\n```": "```py\n>>> import apysc as ap\n>>> arr: ap.Array = ap.Array(range(3))\n>>> with ap.For(arr) as i:\n...     with ap.If(i == 1):\n...         _ = ap.Continue()\n...\n```",  # noqa
}
