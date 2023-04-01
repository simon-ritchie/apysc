"""This module is for the translation mapping data of the
following document:

Document file: for.md
Language: jp
"""

from typing import Dict

MAPPING: Dict[str, str] = {
    ##################################################
    "# For class": "# For クラス",
    ##################################################
    "This page explains the `For` class.": "このページでは`For`クラスについて説明します。",
    ##################################################
    "Before reading on, maybe it is helpful to read the following page (the apysc uses the `For` class for the same reason for each data type):": "このページを読み進める前に以下のページを事前に確認しておくと役に立つかもしれません（apyscでは`For`クラスを各データ型のクラスと同じ理由で使用しています）。",  # noqa
    ##################################################
    "- [Why the apysc library doesn't use the Python built-in data type](why_apysc_doesnt_use_python_builtin_data_type.md)": "- [なぜapyscではPythonのビルトインのデータの型を使用していないのか](jp_why_apysc_doesnt_use_python_builtin_data_type.md)",  # noqa
    ##################################################
    "## What is the For class?": "## For クラスの概要",
    ##################################################
    "The `For` class is the apysc for loop class. It behaves like the Python built-in `for` keyword.": "`For`クラスはapyscのループ制御用のクラスです。このクラスはPythonのビルトインの`for`のキーワードのように動作します。",  # noqa
    ##################################################
    "## Basic usage": "## 基本的な使い方",
    ##################################################
    "The `For` class requires using the `with` statement. The `as` keyword value becomes the `Int` type index (an `i` variable)  or `String` type key.": "`For`クラスは`with`ステートメントと一緒に使用する必要があります。`as`のキーワードの値は`Int`型のインデックス（`i`の変数）もしくは`String`型のキーになります。",  # noqa
    ##################################################
    "The following example draws the three rectangles in the `with For` block:": "以下のコード例では3つの四角を`with For`のブロック内で描画しています:",  # noqa
    ##################################################
    '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    stage_width=350, stage_height=150, background_color="#333", stage_elem_id="stage"\n)\nsprite: ap.Sprite = ap.Sprite()\nsprite.graphics.begin_fill(color="#0af")\n\narr: ap.Array[int] = ap.Array(range(3))\ni: ap.Int\nwith ap.For(arr) as i:\n    sprite.graphics.draw_rect(x=i * 100 + 50, y=50, width=50, height=50)\n\nap.save_overall_html(dest_dir_path="for_basic_usage/")\n```': '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    stage_width=350, stage_height=150, background_color="#333", stage_elem_id="stage"\n)\nsprite: ap.Sprite = ap.Sprite()\nsprite.graphics.begin_fill(color="#0af")\n\narr: ap.Array[int] = ap.Array(range(3))\ni: ap.Int\nwith ap.For(arr) as i:\n    sprite.graphics.draw_rect(x=i * 100 + 50, y=50, width=50, height=50)\n\nap.save_overall_html(dest_dir_path="for_basic_usage/")\n```',  # noqa
    ##################################################
    "The `For` class constructor's first argument accepts an `Array` or `Dictionary` value. If you pass a `Dictionary` value, the `as` keyword value becomes a `String` value, not `Int`\\.": "`For`クラスの第一引数は`Array`もしくは`Dictionary`クラスの値を受け付けます。もしも`Dictionary`の値を指定した場合、`as`のキーワードの値は`Int`の代わりに`String`の値になります。",  # noqa
    ##################################################
    '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    stage_width=250, stage_height=150, background_color="#333", stage_elem_id="stage"\n)\nsprite: ap.Sprite = ap.Sprite()\n\ndict_val: ap.Dictionary = ap.Dictionary(\n    {"magenta": ap.String("#f0a"), "cyan": ap.String("#0af")}\n)\nkey: ap.String\nwith ap.For(dict_val) as key:\n    color: ap.String = dict_val[key]\n    sprite.graphics.begin_fill(color=color)\n    condition_1: ap.Boolean = key == "magenta"\n    condition_2: ap.Boolean = key == "cyan"\n    with ap.If(condition_1):\n        sprite.graphics.draw_rect(x=50, y=50, width=50, height=50)\n    with ap.Elif(condition_2):\n        sprite.graphics.draw_rect(x=150, y=50, width=50, height=50)\n\nap.save_overall_html(dest_dir_path="for_basic_usage_with_dict/")\n```': '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    stage_width=250, stage_height=150, background_color="#333", stage_elem_id="stage"\n)\nsprite: ap.Sprite = ap.Sprite()\n\ndict_val: ap.Dictionary = ap.Dictionary(\n    {"magenta": ap.String("#f0a"), "cyan": ap.String("#0af")}\n)\nkey: ap.String\nwith ap.For(dict_val) as key:\n    color: ap.String = dict_val[key]\n    sprite.graphics.begin_fill(color=color)\n    condition_1: ap.Boolean = key == "magenta"\n    condition_2: ap.Boolean = key == "cyan"\n    with ap.If(condition_1):\n        sprite.graphics.draw_rect(x=50, y=50, width=50, height=50)\n    with ap.Elif(condition_2):\n        sprite.graphics.draw_rect(x=150, y=50, width=50, height=50)\n\nap.save_overall_html(dest_dir_path="for_basic_usage_with_dict/")\n```',  # noqa
    ##################################################
    "## See also": "## 関連資料",
    ##################################################
    "- [Each branch instruction class's scope variables reverting setting](branch_instruction_variables_reverting_setting.md)": "- [分岐条件の各クラスのスコープ内変数の復元設定](jp_branch_instruction_variables_reverting_setting.md)",  # noqa
    ##################################################
    "  - Notes: the `For` class also has the same arguments and behaves in the same way.": "  - 特記事項: `For`クラスは同じ各引数を持っており、同じように動作します。",  # noqa
    ##################################################
    "## For API": "## For API",
    ##################################################
    '<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>': '<span class="inconspicuous-txt">特記事項: このAPIドキュメントはドキュメントビルド用のスクリプトによって自動で生成・同期されています。そのためもしかしたらこの節の内容は前節までの内容と重複している場合があります。</span>',  # noqa
    ##################################################
    "**[Interface summary]**": "**[インターフェイス概要]**",
    ##################################################
    "A class to append for the (loop) expression.<hr>": "ループのfor文の表現を追加するためのクラスです。<hr>",  # noqa
    ##################################################
    "**[Parameters]**": "**[引数]**",
    ##################################################
    "- `arr_or_dict`: Array or Dictionary": "- `arr_or_dict`: Array or Dictionary",
    ##################################################
    "  - Array or Dictionary instance to iterate.": "  - ループで使用するためのArray もしくは Dictionary クラスのインスタンス。",  # noqa
    ##################################################
    "- `locals_`: dict or None, default None": "- `locals_`: dict or None, default None",  # noqa
    ##################################################
    "  - Current scope's local variables. Set locals() value to this argument. If specified, this interface reverts all local scope VariableNameMixIn variables (like Int, Sprite) at the end of a `For` scope. This setting is useful when you don't want to update each variable by implementing the `For` scope.": "  - 現在のスコープのローカル変数。設定する場合にはlocals()関数の値をこの引数に指定してください。もし設定された場合にはこのいんたーふぇいろは`For`クラスによるスコープの終わりにVariableNameMixInを継承した各変数（IntやSpriteなど）の値を元の状態に復元します。この設定はもしも変数の値を`For`のスコープ内で更新したくない場合などに便利な時があります。",  # noqa
    ##################################################
    "- `globals_`: dict or None, default None": "- `globals_`: dict or None, default None",  # noqa
    ##################################################
    "  - Current scope's global variables. Set globals() value to this argument. This setting works the same way as the locals_ argument.": "  - 現在のスコープの各グローバル変数。設定する場合にはglobal()関数の値をこの引数に指定してください。この設定はlocals_引数と同じように動作します。",  # noqa
    ##################################################
    "<hr>": "<hr>",
    ##################################################
    "**[Examples]**": "**[コードサンプル]**",
    ##################################################
    '```py\n>>> import apysc as ap\n>>> arr: ap.Array = ap.Array(range(3))\n>>> with ap.For(arr) as i:\n...     ap.trace("Loop index is:", i)\n...\n```': '```py\n>>> import apysc as ap\n>>> arr: ap.Array = ap.Array(range(3))\n>>> with ap.For(arr) as i:\n...     ap.trace("Loop index is:", i)\n...\n```',  # noqa
}
