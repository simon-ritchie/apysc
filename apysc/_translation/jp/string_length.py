"""This module is for the translation mapping data of the
following document:

Document file: string_length.md
Language: jp
"""

from typing import Dict

MAPPING: Dict[str, str] = {
    ##################################################
    "# String class length property": "# String クラスの length 属性",
    ##################################################
    "This page explains the `String` class `length` property.": "このページでは`String`クラスの`length`属性について説明します。",  # noqa
    ##################################################
    "## What property is this?": "## 属性の概要",
    ##################################################
    "The `length` property returns the number of characters.": "`length`属性は文字数を返却します。",
    ##################################################
    "For example, the `ABCDEF` string returns 6, and the `あいうえお` string returns 5.": "例えば`ABCDEF`という文字列では6が返却され、`あいうえお`という文字列では5が返却されます。",  # noqa
    ##################################################
    "## Basic usage": "## 基本的な使い方",
    ##################################################
    "The `length` property returns an `Int` value as follows:": "`length`属性では以下のように`Int`の値を返却します。",  # noqa
    ##################################################
    '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    stage_width=0,\n    stage_height=0,\n    background_color=ap.Color("#333"),\n    stage_elem_id="stage",\n)\n\nstring: ap.String = ap.String("ABCDEF")\nlength: ap.Int = string.length\nap.assert_equal(length, 6)\n\nap.save_overall_html(dest_dir_path="string_length_basic_usage_1/")\n```': '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    stage_width=0,\n    stage_height=0,\n    background_color=ap.Color("#333"),\n    stage_elem_id="stage",\n)\n\nstring: ap.String = ap.String("ABCDEF")\nlength: ap.Int = string.length\nap.assert_equal(length, 6)\n\nap.save_overall_html(dest_dir_path="string_length_basic_usage_1/")\n```',  # noqa
    ##################################################
    "## Notes of the emoji": "## 絵文字に関する特記事項",
    ##################################################
    "This property returns an unexpected characters length when the string is an emoji character: since this property counts Unicode code points.": "この属性はUnicodeのコードポイント数をカウントしているため、絵文字を対象とした場合に想定外の文字列を返却することがあります。",  # noqa
    ##################################################
    "Most of the emoji characters behave as expected length, as follows:": "大半の絵文字は以下のように想定通りの文字数として振る舞います。",  # noqa
    ##################################################
    '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    stage_width=0,\n    stage_height=0,\n    background_color=ap.Color("#333"),\n    stage_elem_id="stage",\n)\nstring: ap.String = ap.String("🎉")\nap.assert_equal(string.length, 1)\n\nstring = ap.String("🥳🌟🍻")\nap.assert_equal(string.length, 3)\n\nap.save_overall_html(dest_dir_path="string_length_notes_1/")\n```': '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    stage_width=0,\n    stage_height=0,\n    background_color=ap.Color("#333"),\n    stage_elem_id="stage",\n)\nstring: ap.String = ap.String("🎉")\nap.assert_equal(string.length, 1)\n\nstring = ap.String("🥳🌟🍻")\nap.assert_equal(string.length, 3)\n\nap.save_overall_html(dest_dir_path="string_length_notes_1/")\n```',  # noqa
    ##################################################
    "However, in some emojis that have multiple code points, this property returns an unexpected length of characters (this behavior is the same as the Python):": "しかしながら複数のコードポイントを持つ絵文字に関してはこの属性は想定外の文字数を返却します（これはPythonと同じような挙動をします）:",  # noqa
    ##################################################
    '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    stage_width=0,\n    stage_height=0,\n    background_color=ap.Color("#333"),\n    stage_elem_id="stage",\n)\n\nassert len("👨‍👩‍👦") == 5\n\nstring: ap.String = ap.String("👨‍👩‍👦")\nap.assert_equal(string.length, 5)\n\nap.save_overall_html(dest_dir_path="string_length_notes_2/")\n```': '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    stage_width=0,\n    stage_height=0,\n    background_color=ap.Color("#333"),\n    stage_elem_id="stage",\n)\n\nassert len("👨‍👩‍👦") == 5\n\nstring: ap.String = ap.String("👨‍👩‍👦")\nap.assert_equal(string.length, 5)\n\nap.save_overall_html(dest_dir_path="string_length_notes_2/")\n```',  # noqa
    ##################################################
    "## length property API": "## length 属性のAPI",
    ##################################################
    '<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>': '<span class="inconspicuous-txt">特記事項: このAPIドキュメントはドキュメントビルド用のスクリプトによって自動で生成・同期されています。そのためもしかしたらこの節の内容は前節までの内容と重複している場合があります。</span>',  # noqa
    ##################################################
    "**[Interface summary]**": "**[インターフェイス概要]**",
    ##################################################
    "Get a character length (number).<hr>": "文字の長さ（文字数）を取得します。<hr>",
    ##################################################
    "**[Returns]**": "**[返却値]**",
    ##################################################
    "- `characters_length`: Int": "- `characters_length`: Int",
    ##################################################
    "  - A character length (number).": "  - 文字の長さ（文字数）。",
    ##################################################
    "<hr>": "<hr>",
    ##################################################
    "**[Examples]**": "**[コードサンプル]**",
    ##################################################
    '```py\n>>> import apysc as ap\n>>> _ = ap.Stage()\n>>> string: ap.String = ap.String("Hello")\n>>> string.length\nInt(5)\n```': '```py\n>>> import apysc as ap\n>>> _ = ap.Stage()\n>>> string: ap.String = ap.String("Hello")\n>>> string.length\nInt(5)\n```',  # noqa
}
