"""This module is for the translation mapping data of the
following document:

Document file: string_zfill.md
Language: jp
"""

from typing import Dict

MAPPING: Dict[str, str] = {
    ##################################################
    "# String class zfill method": "# String クラスの zfill メソッド",
    ##################################################
    "This page explains the `String` class `zfill` method.": "このページでは`String`クラスの`zfill`メソッドについて説明します。",  # noqa
    ##################################################
    "## What method is this?": "## メソッド概要",
    ##################################################
    "The `zfill` method returns a zero-filled string with the specified widgth (number of total characters).": "`zfill`メソッドは指定された文字数でゼロ埋めされた文字列を返却します。",  # noqa
    ##################################################
    "## Basic usage": "## 基本的な使い方",
    ##################################################
    "The `zfill` method required the `width` argument (`int` or `ap.Int` type).": "`zfill`メソッドは`width`引数を必要とします（`int`もしくは`ap.Int`型となります）。",  # noqa
    ##################################################
    "It determines the number of total characters.": "その設定によって合計の文字数が決定します。",
    ##################################################
    "A return value becomes copied `ap.String` value.": "返却値はコピーされた`ap.String`型の値となります。",  # noqa
    ##################################################
    '```py\n# runnable\n\nimport apysc as ap\n\nap.Stage(\n    stage_width=0,\n    stage_height=0,\n    background_color=ap.Color("#333"),\n    stage_elem_id="stage",\n)\n\nstring: ap.String = ap.String(value="1")\nstring = string.zfill(width=1)\nap.assert_equal(string, "1")\n\nstring = string.zfill(width=3)\nap.assert_equal(string, "001")\n\nstring = string.zfill(width=5)\nap.assert_equal(string, "00001")\n\nap.save_overall_html(dest_dir_path="string_zfill_basic_usage/")\n```': '```py\n# runnable\n\nimport apysc as ap\n\nap.Stage(\n    stage_width=0,\n    stage_height=0,\n    background_color=ap.Color("#333"),\n    stage_elem_id="stage",\n)\n\nstring: ap.String = ap.String(value="1")\nstring = string.zfill(width=1)\nap.assert_equal(string, "1")\n\nstring = string.zfill(width=3)\nap.assert_equal(string, "001")\n\nstring = string.zfill(width=5)\nap.assert_equal(string, "00001")\n\nap.save_overall_html(dest_dir_path="string_zfill_basic_usage/")\n```',  # noqa
    ##################################################
    "## zfill method API": "## zfill メソッドのAPI",
    ##################################################
    '<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>': '<span class="inconspicuous-txt">特記事項: このAPIドキュメントはドキュメントビルド用のスクリプトによって自動で生成・同期されています。そのためもしかしたらこの節の内容は前節までの内容と重複している場合があります。</span>',  # noqa
    ##################################################
    "**[Interface summary]**": "**[インターフェイス概要]**",
    ##################################################
    "Return a copy of the string left filled with 0.<hr>": "文字列の左側を0で埋めた文字列を返却します。<hr>",  # noqa
    ##################################################
    "**[Parameters]**": "**[引数]**",
    ##################################################
    '- `width`: Union[int, "Int"]': '- `width`: Union[int, "Int"]',
    ##################################################
    "  - A width (length) of the string.": "  - 文字列の幅（長さ）。",
    ##################################################
    "<hr>": "<hr>",
    ##################################################
    "**[Returns]**": "**[返却値]**",
    ##################################################
    "- `result`: String": "- `result`: String",
    ##################################################
    "  - A result string.": "  - 結果の文字列。",
    ##################################################
    "<hr>": "<hr>",
    ##################################################
    "**[Examples]**": "**[コードサンプル]**",
    ##################################################
    '```py\n>>> import apysc as ap\n>>> _: ap.Stage = ap.Stage()\n>>> string: ap.String = ap.String("1")\n>>> string = string.zfill(width=1)\n>>> string\nString("1")\n\n>>> string = string.zfill(width=3)\n>>> string\nString("001")\n\n>>> string = string.zfill(width=5)\n>>> string\nString("00001")\n```': '```py\n>>> import apysc as ap\n>>> _: ap.Stage = ap.Stage()\n>>> string: ap.String = ap.String("1")\n>>> string = string.zfill(width=1)\n>>> string\nString("1")\n\n>>> string = string.zfill(width=3)\n>>> string\nString("001")\n\n>>> string = string.zfill(width=5)\n>>> string\nString("00001")\n```',  # noqa
}
