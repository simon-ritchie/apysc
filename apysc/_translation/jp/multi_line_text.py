"""This module is for the translation mapping data of the
following document:

Document file: multi_line_text.md
Language: jp
"""

from typing import Dict

MAPPING: Dict[str, str] = {
    ##################################################
    "# MultiLineText class": "# MultiLineText クラス",
    ##################################################
    "This page explains the `MultiLineText` class.": "このページでは`MultiLineText`クラスについて説明します。",  # noqa
    ##################################################
    "## What class is this?": "## クラス概要",
    ##################################################
    "The `MultiLineText` class creates a multi-line text instance.": "`MultiLineText`クラスは複数行のテキストのインスタンスを生成します。",  # noqa
    ##################################################
    "This text instance wraps at a certain width.": "このテキストのインスタンスは一定の幅で折り返します。",
    ##################################################
    "## Basic usage": "## 基本的な使い方",
    ##################################################
    "The `MultiLineText` class requires the `text` argument.": "`MultiLineText`クラスは`text`引数を必要とします。",  # noqa
    ##################################################
    "The constructor also accepts each style setting, such as the `width`, `fill_color`, `bold`, and `text_align`.": "コンストラクタでは`width`、`fill_color`、`bold`、`text_align`などのスタイル設定も同様に受け付けます。",  # noqa
    ##################################################
    '```py\n# runnable\nimport apysc as ap\n\nstage: ap.Stage = ap.Stage(\n    background_color=ap.Color("#333"),\n    stage_width=300,\n    stage_height=200,\n    stage_elem_id="stage",\n)\n\nmulti_line_text: ap.MultiLineText = ap.MultiLineText(\n    text="Lorem ipsum dolor sit amet, consectetur adipiscing elit, "\n    "sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. "\n    "Ut enim ad minim veniam",\n    width=250,\n    font_size=16,\n    fill_color=ap.Colors.CYAN_00AAFF,\n    x=25,\n    y=25,\n)\nap.save_overall_html(dest_dir_path="multi_line_text_basic_usage/")\n```': '```py\n# runnable\nimport apysc as ap\n\nstage: ap.Stage = ap.Stage(\n    background_color=ap.Color("#333"),\n    stage_width=300,\n    stage_height=200,\n    stage_elem_id="stage",\n)\n\nmulti_line_text: ap.MultiLineText = ap.MultiLineText(\n    text="Lorem ipsum dolor sit amet, consectetur adipiscing elit, "\n    "sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. "\n    "Ut enim ad minim veniam",\n    width=250,\n    font_size=16,\n    fill_color=ap.Colors.CYAN_00AAFF,\n    x=25,\n    y=25,\n)\nap.save_overall_html(dest_dir_path="multi_line_text_basic_usage/")\n```',  # noqa
    ##################################################
    "## MultiLineText constructor API": "## MultiLineText クラスのコンストラクタのAPI",
    ##################################################
    '<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>': '<span class="inconspicuous-txt">特記事項: このAPIドキュメントはドキュメントビルド用のスクリプトによって自動で生成・同期されています。そのためもしかしたらこの節の内容は前節までの内容と重複している場合があります。</span>',  # noqa
    ##################################################
    "**[Interface summary]**": "**[インターフェイス概要]**",
    ##################################################
    "The class implementation for a multiline text element.<hr>": "複数行のテキスト要素のクラスの実装。<hr>",  # noqa
    ##################################################
    "**[Parameters]**": "**[引数]**",
    ##################################################
    "- `text`: Union[str, String]": "- `text`: Union[str, String]",
    ##################################################
    "  - Text to display. An HTML tag is available.": "  - 表示対象のテキスト。HTMLタグが利用可能です。",
    ##################################################
    "- `x`: Union[float, Number], default 0": "- `x`: Union[float, Number], default 0",
    ##################################################
    "  - X-coordinate.": "  - X座標。",
    ##################################################
    "- `y`: Union[float, Number], default 0": "- `y`: Union[float, Number], default 0",
    ##################################################
    "  - Y-coordinate.": "  - Y座標。",
    ##################################################
    "- `width`: Union[int, Int], default 200": "- `width`: Union[int, Int], default 200",  # noqa
    ##################################################
    "  - Width of the text to wrap.": "  - 折り返し位置となるテキストの幅。",
    ##################################################
    "- `font_size`: Union[int, Int], default 16": "- `font_size`: Union[int, Int], default 16",  # noqa
    ##################################################
    "  - Font size.": "  - フォントサイズ。",
    ##################################################
    "- `fill_color`: Color, default Colors.GRAY_666666": "- `fill_color`: Color, default Colors.GRAY_666666",  # noqa
    ##################################################
    "  - Text color.": "  - テキストの色。",
    ##################################################
    "- `fill_alpha`: Union[float, Number], default 1.0": "- `fill_alpha`: Union[float, Number], default 1.0",  # noqa
    ##################################################
    "  - Text alpha (opacity). The minimum value is 0.0 (transparent), and the maximum value is 1.0 (solid).": "  - テキストの透明度。最小値は0.0（透明）、最大値は1.0（不透明）になります。",  # noqa
    ##################################################
    "- `bold`: Union[bool, Boolean], default False": "- `bold`: Union[bool, Boolean], default False",  # noqa
    ##################################################
    "  - Whether to display the text in bold.": "  - テキストを太字で表示するか否か。",
    ##################################################
    "- `italic`: Union[bool, Boolean], default False": "- `italic`: Union[bool, Boolean], default False",  # noqa
    ##################################################
    "  - Whether to display the text in italic.": "  - テキストを斜体で表示するか否か。",
    ##################################################
    "- `text_align`: CssTextAlign, default `CssTextAlign.LEFT`": "- `text_align`: CssTextAlign, default `CssTextAlign.LEFT`",  # noqa
    ##################################################
    "  - Text align setting.": "  - テキストの行揃えの設定。",
    ##################################################
    "- `text_align_last`: CssTextAlignLast, default `CssTextAlignLast.AUTO`": "- `text_align_last`: CssTextAlignLast, default `CssTextAlignLast.AUTO`",  # noqa
    ##################################################
    "  - Last line's text-align setting.": "  - 最終行の行揃えの設定。",
    ##################################################
    "- `underline`: Union[bool, Boolean], default False": "- `underline`: Union[bool, Boolean], default False",  # noqa
    ##################################################
    "  - Whether to display the text's underline.": "  - テキストの下線を表示するか否か。",
    ##################################################
    "- `line_height`: Union[float, Number], default 1.5": "- `line_height`: Union[float, Number], default 1.5",  # noqa
    ##################################################
    "  - A line-height (text-leading) setting.": "  - 行の高さ（テキストの行間）の設定。",
    ##################################################
    "- `parent`: ChildMixIn or None, default None": "- `parent`: ChildMixIn or None, default None",  # noqa
    ##################################################
    "  - A parent instance to add this instance. If the specified value is None, this interface uses a stage instance.": "  - このインスタンスを追加する親のインスタンス。もしもNoneが指定された場合、このインスタンスはステージのインスタンスへと追加されます。",  # noqa
    ##################################################
    '- `variable_name_suffix`: str, default ""': '- `variable_name_suffix`: str, default ""',  # noqa
    ##################################################
    "  - A JavaScript variable name suffix string. This setting is sometimes useful for JavaScript debugging.": "  - JavaScript上の変数のサフィックスの設定です。この設定はJavaScriptのデバッグ時に役立つことがあります。",  # noqa
    ##################################################
    "<hr>": "<hr>",
    ##################################################
    "**[Examples]**": "**[コードサンプル]**",
    ##################################################
    '```py\n>>> import apysc as ap\n>>> stage: ap.Stage = ap.Stage(\n...     background_color=ap.Color("#333"),\n...     stage_width=300,\n...     stage_height=100,\n...     stage_elem_id="stage",\n... )\n>>> multi_line_text: ap.MultiLineText = ap.MultiLineText(\n...     text="Lorem ipsum dolor sit amet, consectetur adipiscing elit, "\n...     "sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. "\n...     "Ut enim ad minim veniam",\n...     width=300,\n...     font_size=16,\n...     fill_color=ap.Color("#00aaff"),\n...     x=20,\n...     y=20,\n... )\n>>> multi_line_text.fill_color\nColor("#00aaff")\n```': '```py\n>>> import apysc as ap\n>>> stage: ap.Stage = ap.Stage(\n...     background_color=ap.Color("#333"),\n...     stage_width=300,\n...     stage_height=100,\n...     stage_elem_id="stage",\n... )\n>>> multi_line_text: ap.MultiLineText = ap.MultiLineText(\n...     text="Lorem ipsum dolor sit amet, consectetur adipiscing elit, "\n...     "sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. "\n...     "Ut enim ad minim veniam",\n...     width=300,\n...     font_size=16,\n...     fill_color=ap.Color("#00aaff"),\n...     x=20,\n...     y=20,\n... )\n>>> multi_line_text.fill_color\nColor("#00aaff")\n```',  # noqa
    ##################################################
    "<hr>": "<hr>",
    ##################################################
    "**[References]**": "**[関連資料]**",
    ##################################################
    "- [Text fill_color property](https://simon-ritchie.github.io/apysc/en/text_fill_color.html)": "- [テキストの fill_color 属性](https://simon-ritchie.github.io/apysc/jp/jp_text_fill_color.html)",  # noqa
    ##################################################
    "- [Text fill_alpha property](https://simon-ritchie.github.io/apysc/en/text_fill_alpha.html)": "- [テキストの fill_alpha 属性](https://simon-ritchie.github.io/apysc/jp/jp_text_fill_alpha.html)",  # noqa
    ##################################################
    "- [Text bold property](https://simon-ritchie.github.io/apysc/en/text_bold.html)": "- [テキストの bold 属性](https://simon-ritchie.github.io/apysc/jp/jp_text_bold.html)",  # noqa
    ##################################################
    "- [Text italic property](https://simon-ritchie.github.io/apysc/en/text_italic.html)": "- [テキストの italic 属性](https://simon-ritchie.github.io/apysc/jp/jp_text_italic.html)",  # noqa
    ##################################################
    "- [text_align property](https://simon-ritchie.github.io/apysc/en/text_align.html)": "- [text_align 属性](https://simon-ritchie.github.io/apysc/jp/jp_text_align.html)",  # noqa
    ##################################################
    "- [text_align_last property](https://simon-ritchie.github.io/apysc/en/text_align_last.html)": "- [text_align_last 属性](https://simon-ritchie.github.io/apysc/jp/jp_text_align_last.html)",  # noqa
    ##################################################
    "- [Text font_size property](https://simon-ritchie.github.io/apysc/en/text_font_size.html)": "- [テキストの font_size 属性](https://simon-ritchie.github.io/apysc/jp/jp_text_font_size.html)",  # noqa
    ##################################################
    "- [Text line_height property](https://simon-ritchie.github.io/apysc/en/text_line_height.html)": "- [テキストの line_height 属性](https://simon-ritchie.github.io/apysc/jp/jp_text_line_height.html)",  # noqa
}
