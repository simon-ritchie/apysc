"""This module is for the translation mapping data of the
following document:

Document file: svg_text_span.md
Language: jp
"""

from typing import Dict

MAPPING: Dict[str, str] = {
    ##################################################
    "# SvgTextSpan class": "# SvgTextSpan クラス",
    ##################################################
    "This page explains the `SvgTextSpan` class.": "このページでは`SvgTextSpan`クラスについて説明します。",
    ##################################################
    "## What interface is this?": "## インターフェイス概要",
    ##################################################
    "The `SvgTextSpan` is the class for an SVG text-span (the child class of `SvgText`).": "`SvgTextSpan`は`SvgText`の子となるテキスト要素を作成するためのクラスです。",  # noqa
    ##################################################
    "You can create an `SvgText` instance with multiple `SvgTextSpan` class instances and set different text styles.": "複数の`SvgTextSpan`クラスのインスタンスを使ってそれぞれに異なるテキストのスタイルを設定した状態の`SvgText`のインスタンスを作成することができます。",  # noqa
    ##################################################
    "## Basic usage": "## 基本的な使い方",
    ##################################################
    "The `SvgTextSpan` class constructor requires the `text` argument.": "`SvgTextSpan`クラスのコンストラクタには`text`引数を必要とします。",  # noqa
    ##################################################
    "The constructor also accepts each font's and style's argument, such as the `font_size`, `font_family`, `fill_color`, and `bold`.": "コンストラクタでは`font_size`や`font_family`、`fill_color`、`bold`などの各スタイル設定の引数を受け付けます。",  # noqa
    ##################################################
    "If you skip the style settings' arguments, these settings become the parent SvgText's styles.": "もしもそれらのスタイル設定の引数指定を省略した場合、親のSVGTextのインスタンスのスタイルが反映されます。",  # noqa
    ##################################################
    "You can use `SvgTextSpan` instances to create an `SvgText` instance with the `create_with_svg_text_spans` class method.": "また、複数の`SvgTextSpan`のインスタンスを使って`SvgText`のインスタンスの作成するには`create_with_svg_text_spans`のクラスメソッドを使うことで対応ができます。",  # noqa
    ##################################################
    '```py\n# runnable\nimport apysc as ap\n\nstage: ap.Stage = ap.Stage(\n    background_color=ap.Color("#333"),\n    stage_width=200,\n    stage_height=50,\n    stage_elem_id="stage",\n)\nsvg_text: ap.SvgText = ap.SvgText.create_with_svg_text_spans(\n    text_spans=[\n        ap.SvgTextSpan(text="Lorem "),\n        ap.SvgTextSpan(text="ipsum ", font_size=20, fill_color=ap.Color("#0af")),\n        ap.SvgTextSpan(text="dolor ", font_size=12),\n    ],\n    fill_color=ap.Color("#aaa"),\n    font_size=16,\n    x=20,\n    y=32,\n)\n\nap.save_overall_html(dest_dir_path="svg_txt_span_basic_usage/")\n```': '```py\n# runnable\nimport apysc as ap\n\nstage: ap.Stage = ap.Stage(\n    background_color=ap.Color("#333"),\n    stage_width=200,\n    stage_height=50,\n    stage_elem_id="stage",\n)\nsvg_text: ap.SvgText = ap.SvgText.create_with_svg_text_spans(\n    text_spans=[\n        ap.SvgTextSpan(text="Lorem "),\n        ap.SvgTextSpan(text="ipsum ", font_size=20, fill_color=ap.Color("#0af")),\n        ap.SvgTextSpan(text="dolor ", font_size=12),\n    ],\n    fill_color=ap.Color("#aaa"),\n    font_size=16,\n    x=20,\n    y=32,\n)\n\nap.save_overall_html(dest_dir_path="svg_txt_span_basic_usage/")\n```',  # noqa
    ##################################################
    "## Notes of the line breaking": "## 改行に対する特記事項",
    ##################################################
    "The `SvgTextSpan` class ignores line breaks.": "`SvgTextSpan`クラスは改行設定を無視します。",
    ##################################################
    "For instance, the following example's text contains a line break (`\n`), but the text line becomes a single line.": "例えば、以下の例では改行用の文字列（`\n`）を含んでいますがテキストの行は単一行になっています。",  # noqa
    ##################################################
    '```py\n# runnable\nimport apysc as ap\n\nstage: ap.Stage = ap.Stage(\n    background_color=ap.Color("#333"),\n    stage_width=200,\n    stage_height=50,\n    stage_elem_id="stage",\n)\nsvg_text: ap.SvgText = ap.SvgText.create_with_svg_text_spans(\n    text_spans=[\n        ap.SvgTextSpan(text="Lorem \n"),\n        ap.SvgTextSpan(text="ipsum \n"),\n        ap.SvgTextSpan(text="dolor"),\n    ],\n    x=20,\n    y=32,\n    fill_color=ap.Color("#aaa"),\n)\n\nap.save_overall_html(dest_dir_path="svg_txt_span_notes_of_the_line_break/")\n```': '```py\n# runnable\nimport apysc as ap\n\nstage: ap.Stage = ap.Stage(\n    background_color=ap.Color("#333"),\n    stage_width=200,\n    stage_height=50,\n    stage_elem_id="stage",\n)\nsvg_text: ap.SvgText = ap.SvgText.create_with_svg_text_spans(\n    text_spans=[\n        ap.SvgTextSpan(text="Lorem \n"),\n        ap.SvgTextSpan(text="ipsum \n"),\n        ap.SvgTextSpan(text="dolor"),\n    ],\n    x=20,\n    y=32,\n    fill_color=ap.Color("#aaa"),\n)\n\nap.save_overall_html(dest_dir_path="svg_txt_span_notes_of_the_line_break/")\n```',  # noqa
    ##################################################
    "If you want to add a line break, please use the `SvgText` class (not the `SvgTextSpan`) or create multiple `SvgText` instances.": "もしも改行を加えたい場合には`SvgTextSpan`クラスではなく`SvgText`クラスを使用するか、もしくは複数のインスタンスを作成して対応をお願いします。",  # noqa
    ##################################################
    "## text property interface example": "## text 属性のインターフェイス例",
    ##################################################
    "The `text` property updates or gets the instance's text.": "`text`属性ではインスタンスのテキストの更新もしくは取得を行えます。",  # noqa
    ##################################################
    '```py\n# runnable\nimport apysc as ap\n\nstage: ap.Stage = ap.Stage(\n    background_color=ap.Color("#333"),\n    stage_width=200,\n    stage_height=50,\n    stage_elem_id="stage",\n)\ntext_span_1: ap.SvgTextSpan = ap.SvgTextSpan(text="Lorem ")\ntext_span_2: ap.SvgTextSpan = ap.SvgTextSpan(text="ipsum")\ntext_span_2.text = ap.String("dolor")\n\nsvg_text: ap.SvgText = ap.SvgText.create_with_svg_text_spans(\n    text_spans=[text_span_1, text_span_2],\n    font_size=16,\n    x=20,\n    y=32,\n    fill_color=ap.Color("#aaa"),\n)\n\nap.save_overall_html(dest_dir_path="svg_txt_span_text/")\n```': '```py\n# runnable\nimport apysc as ap\n\nstage: ap.Stage = ap.Stage(\n    background_color=ap.Color("#333"),\n    stage_width=200,\n    stage_height=50,\n    stage_elem_id="stage",\n)\ntext_span_1: ap.SvgTextSpan = ap.SvgTextSpan(text="Lorem ")\ntext_span_2: ap.SvgTextSpan = ap.SvgTextSpan(text="ipsum")\ntext_span_2.text = ap.String("dolor")\n\nsvg_text: ap.SvgText = ap.SvgText.create_with_svg_text_spans(\n    text_spans=[text_span_1, text_span_2],\n    font_size=16,\n    x=20,\n    y=32,\n    fill_color=ap.Color("#aaa"),\n)\n\nap.save_overall_html(dest_dir_path="svg_txt_span_text/")\n```',  # noqa
    ##################################################
    "## font_size property interface example": "## font_size 属性のインターフェイス例",
    ##################################################
    "The `font_size` property updates or gets the instance's font size.": "`font_size`属性ではインスタンスのフォントサイズの更新もしくは取得を行えます。",  # noqa
    ##################################################
    '```py\n# runnable\nimport apysc as ap\n\nstage: ap.Stage = ap.Stage(\n    background_color=ap.Color("#333"),\n    stage_width=200,\n    stage_height=50,\n    stage_elem_id="stage",\n)\ntext_span_1: ap.SvgTextSpan = ap.SvgTextSpan(text="Lorem ")\ntext_span_2: ap.SvgTextSpan = ap.SvgTextSpan(text="ipsum")\ntext_span_2.font_size = ap.Int(25)\n\nsvg_text: ap.SvgText = ap.SvgText.create_with_svg_text_spans(\n    text_spans=[text_span_1, text_span_2],\n    font_size=16,\n    x=20,\n    y=32,\n    fill_color=ap.Color("#aaa"),\n)\n\nap.save_overall_html(dest_dir_path="svg_txt_span_font_size/")\n```': '```py\n# runnable\nimport apysc as ap\n\nstage: ap.Stage = ap.Stage(\n    background_color=ap.Color("#333"),\n    stage_width=200,\n    stage_height=50,\n    stage_elem_id="stage",\n)\ntext_span_1: ap.SvgTextSpan = ap.SvgTextSpan(text="Lorem ")\ntext_span_2: ap.SvgTextSpan = ap.SvgTextSpan(text="ipsum")\ntext_span_2.font_size = ap.Int(25)\n\nsvg_text: ap.SvgText = ap.SvgText.create_with_svg_text_spans(\n    text_spans=[text_span_1, text_span_2],\n    font_size=16,\n    x=20,\n    y=32,\n    fill_color=ap.Color("#aaa"),\n)\n\nap.save_overall_html(dest_dir_path="svg_txt_span_font_size/")\n```',  # noqa
    ##################################################
    "## font_family property interface example": "## font_family 属性のインターフェイス例",
    ##################################################
    "The `font_family` property updates or gets the instance's font family.": "`font_family`属性ではインスタンスのフォントファミリー（フォントの指定）の更新もしくは取得を行えます。",  # noqa
    ##################################################
    "This property requires an `Array` of each font name `String`.": "この属性は各フォント名の`String`型の文字列を格納した`Array`型の配列を必要とします。",  # noqa
    ##################################################
    '```py\n# runnable\nimport apysc as ap\n\nstage: ap.Stage = ap.Stage(\n    background_color=ap.Color("#333"),\n    stage_width=200,\n    stage_height=50,\n    stage_elem_id="stage",\n)\ntext_span_1: ap.SvgTextSpan = ap.SvgTextSpan(text="Lorem ")\ntext_span_2: ap.SvgTextSpan = ap.SvgTextSpan(text="ipsum")\ntext_span_2.font_family = ap.Array([ap.String("Impact"), ap.String("Arial")])\n\nsvg_text: ap.SvgText = ap.SvgText.create_with_svg_text_spans(\n    text_spans=[text_span_1, text_span_2],\n    font_size=16,\n    x=20,\n    y=32,\n    fill_color=ap.Color("#aaa"),\n)\n\nap.save_overall_html(dest_dir_path="svg_txt_span_font_family/")\n```': '```py\n# runnable\nimport apysc as ap\n\nstage: ap.Stage = ap.Stage(\n    background_color=ap.Color("#333"),\n    stage_width=200,\n    stage_height=50,\n    stage_elem_id="stage",\n)\ntext_span_1: ap.SvgTextSpan = ap.SvgTextSpan(text="Lorem ")\ntext_span_2: ap.SvgTextSpan = ap.SvgTextSpan(text="ipsum")\ntext_span_2.font_family = ap.Array([ap.String("Impact"), ap.String("Arial")])\n\nsvg_text: ap.SvgText = ap.SvgText.create_with_svg_text_spans(\n    text_spans=[text_span_1, text_span_2],\n    font_size=16,\n    x=20,\n    y=32,\n    fill_color=ap.Color("#aaa"),\n)\n\nap.save_overall_html(dest_dir_path="svg_txt_span_font_family/")\n```',  # noqa
    ##################################################
    "## fill_color property interface example": "## fill_color属性のインターフェイス例",
    ##################################################
    "The `fill_color` property updates or gets the instance's fill color:": "`fill_color`属性は塗りの色の値の更新もしくは取得を行えます:",  # noqa
    ##################################################
    '```py\n# runnable\nimport apysc as ap\n\nstage: ap.Stage = ap.Stage(\n    background_color=ap.Color("#333"),\n    stage_width=200,\n    stage_height=50,\n    stage_elem_id="stage",\n)\ntext_span_1: ap.SvgTextSpan = ap.SvgTextSpan(text="Lorem ")\ntext_span_2: ap.SvgTextSpan = ap.SvgTextSpan(text="ipsum")\ntext_span_2.fill_color = ap.Color("#0af")\n\nsvg_text: ap.SvgText = ap.SvgText.create_with_svg_text_spans(\n    text_spans=[text_span_1, text_span_2],\n    font_size=16,\n    x=20,\n    y=32,\n    fill_color=ap.Color("#aaa"),\n)\n\nap.save_overall_html(dest_dir_path="svg_txt_span_fill_color/")\n```': '```py\n# runnable\nimport apysc as ap\n\nstage: ap.Stage = ap.Stage(\n    background_color=ap.Color("#333"),\n    stage_width=200,\n    stage_height=50,\n    stage_elem_id="stage",\n)\ntext_span_1: ap.SvgTextSpan = ap.SvgTextSpan(text="Lorem ")\ntext_span_2: ap.SvgTextSpan = ap.SvgTextSpan(text="ipsum")\ntext_span_2.fill_color = ap.Color("#0af")\n\nsvg_text: ap.SvgText = ap.SvgText.create_with_svg_text_spans(\n    text_spans=[text_span_1, text_span_2],\n    font_size=16,\n    x=20,\n    y=32,\n    fill_color=ap.Color("#aaa"),\n)\n\nap.save_overall_html(dest_dir_path="svg_txt_span_fill_color/")\n```',  # noqa
    ##################################################
    "## fill_alpha property interface example": "## fill_alpha属性のインターフェイス例",
    ##################################################
    "The `fill_alpha` property updates or gets the instance's fill alpha (opacity):": "`fill_alpha`属性は塗りの透明度の値の更新もしくは取得を行えます:",  # noqa
    ##################################################
    '```py\n# runnable\nimport apysc as ap\n\nstage: ap.Stage = ap.Stage(\n    background_color=ap.Color("#333"),\n    stage_width=200,\n    stage_height=50,\n    stage_elem_id="stage",\n)\ntext_span_1: ap.SvgTextSpan = ap.SvgTextSpan(text="Lorem ")\ntext_span_2: ap.SvgTextSpan = ap.SvgTextSpan(text="ipsum")\ntext_span_2.fill_alpha = ap.Number(0.3)\n\nsvg_text: ap.SvgText = ap.SvgText.create_with_svg_text_spans(\n    text_spans=[text_span_1, text_span_2],\n    font_size=16,\n    x=20,\n    y=32,\n    fill_color=ap.Color("#aaa"),\n)\n\nap.save_overall_html(dest_dir_path="svg_txt_span_fill_alpha/")\n```': '```py\n# runnable\nimport apysc as ap\n\nstage: ap.Stage = ap.Stage(\n    background_color=ap.Color("#333"),\n    stage_width=200,\n    stage_height=50,\n    stage_elem_id="stage",\n)\ntext_span_1: ap.SvgTextSpan = ap.SvgTextSpan(text="Lorem ")\ntext_span_2: ap.SvgTextSpan = ap.SvgTextSpan(text="ipsum")\ntext_span_2.fill_alpha = ap.Number(0.3)\n\nsvg_text: ap.SvgText = ap.SvgText.create_with_svg_text_spans(\n    text_spans=[text_span_1, text_span_2],\n    font_size=16,\n    x=20,\n    y=32,\n    fill_color=ap.Color("#aaa"),\n)\n\nap.save_overall_html(dest_dir_path="svg_txt_span_fill_alpha/")\n```',  # noqa
    ##################################################
    "## line_color property interface example": "## line_color属性のインターフェイス例",
    ##################################################
    "The `line_color` property updates or gets the instance's line color:": "`line_color`属性では線の色の値の更新もしくは取得を行えます:",  # noqa
    ##################################################
    '```py\n# runnable\nimport apysc as ap\n\nstage: ap.Stage = ap.Stage(\n    background_color=ap.Color("#333"),\n    stage_width=200,\n    stage_height=50,\n    stage_elem_id="stage",\n)\ntext_span_1: ap.SvgTextSpan = ap.SvgTextSpan(\n    text="Lorem ", line_thickness=1, font_size=20, bold=True\n)\ntext_span_1.line_color = ap.Color("#aaa")\ntext_span_2: ap.SvgTextSpan = ap.SvgTextSpan(\n    text="ipsum", line_thickness=1, font_size=20, bold=True\n)\ntext_span_2.line_color = ap.Color("#0af")\n\nsvg_text: ap.SvgText = ap.SvgText.create_with_svg_text_spans(\n    text_spans=[text_span_1, text_span_2],\n    font_size=16,\n    x=20,\n    y=32,\n    fill_color=ap.COLORLESS,\n)\n\nap.save_overall_html(dest_dir_path="svg_txt_span_line_color/")\n```': '```py\n# runnable\nimport apysc as ap\n\nstage: ap.Stage = ap.Stage(\n    background_color=ap.Color("#333"),\n    stage_width=200,\n    stage_height=50,\n    stage_elem_id="stage",\n)\ntext_span_1: ap.SvgTextSpan = ap.SvgTextSpan(\n    text="Lorem ", line_thickness=1, font_size=20, bold=True\n)\ntext_span_1.line_color = ap.Color("#aaa")\ntext_span_2: ap.SvgTextSpan = ap.SvgTextSpan(\n    text="ipsum", line_thickness=1, font_size=20, bold=True\n)\ntext_span_2.line_color = ap.Color("#0af")\n\nsvg_text: ap.SvgText = ap.SvgText.create_with_svg_text_spans(\n    text_spans=[text_span_1, text_span_2],\n    font_size=16,\n    x=20,\n    y=32,\n    fill_color=ap.COLORLESS,\n)\n\nap.save_overall_html(dest_dir_path="svg_txt_span_line_color/")\n```',  # noqa
    ##################################################
    "## line_alpha property interface example": "## line_alpha属性のインターフェイス例",
    ##################################################
    "The `line_alpha` property updates or gets the instance's line alpha (opacity):": "`line_alpha`属性では線の透明度の値の更新もしくは取得を行えます:",  # noqa
    ##################################################
    '```py\n# runnable\nimport apysc as ap\n\nstage: ap.Stage = ap.Stage(\n    background_color=ap.Color("#333"),\n    stage_width=200,\n    stage_height=50,\n    stage_elem_id="stage",\n)\ntext_span_1: ap.SvgTextSpan = ap.SvgTextSpan(\n    text="Lorem ",\n    line_color=ap.Color("#0af"),\n    line_thickness=1,\n    font_size=20,\n    bold=True,\n)\ntext_span_2: ap.SvgTextSpan = ap.SvgTextSpan(\n    text="ipsum",\n    line_color=ap.Color("#0af"),\n    line_thickness=1,\n    font_size=20,\n    bold=True,\n)\ntext_span_2.line_alpha = ap.Number(0.3)\n\nsvg_text: ap.SvgText = ap.SvgText.create_with_svg_text_spans(\n    text_spans=[text_span_1, text_span_2],\n    font_size=16,\n    x=20,\n    y=32,\n    fill_color=ap.COLORLESS,\n)\n\nap.save_overall_html(dest_dir_path="svg_txt_span_line_alpha/")\n```': '```py\n# runnable\nimport apysc as ap\n\nstage: ap.Stage = ap.Stage(\n    background_color=ap.Color("#333"),\n    stage_width=200,\n    stage_height=50,\n    stage_elem_id="stage",\n)\ntext_span_1: ap.SvgTextSpan = ap.SvgTextSpan(\n    text="Lorem ",\n    line_color=ap.Color("#0af"),\n    line_thickness=1,\n    font_size=20,\n    bold=True,\n)\ntext_span_2: ap.SvgTextSpan = ap.SvgTextSpan(\n    text="ipsum",\n    line_color=ap.Color("#0af"),\n    line_thickness=1,\n    font_size=20,\n    bold=True,\n)\ntext_span_2.line_alpha = ap.Number(0.3)\n\nsvg_text: ap.SvgText = ap.SvgText.create_with_svg_text_spans(\n    text_spans=[text_span_1, text_span_2],\n    font_size=16,\n    x=20,\n    y=32,\n    fill_color=ap.COLORLESS,\n)\n\nap.save_overall_html(dest_dir_path="svg_txt_span_line_alpha/")\n```',  # noqa
    ##################################################
    "## line_thickness property interface example": "## line_thickness属性のインターフェイス例",
    ##################################################
    "The `line_thickness` property updates or gets the instance's line thickness (line width):": "`line_thickness`属性では線の幅の更新もしくは取得を行えます:",  # noqa
    ##################################################
    '```py\n# runnable\nimport apysc as ap\n\nstage: ap.Stage = ap.Stage(\n    background_color=ap.Color("#333"),\n    stage_width=200,\n    stage_height=50,\n    stage_elem_id="stage",\n)\ntext_span_1: ap.SvgTextSpan = ap.SvgTextSpan(\n    text="Lorem ",\n    line_color=ap.Color("#0af"),\n    font_size=20,\n    bold=True,\n)\ntext_span_2: ap.SvgTextSpan = ap.SvgTextSpan(\n    text="ipsum",\n    line_color=ap.Color("#0af"),\n    font_size=20,\n    bold=True,\n)\ntext_span_1.line_thickness = ap.Int(3)\ntext_span_2.line_thickness = ap.Int(3)\n\nsvg_text: ap.SvgText = ap.SvgText.create_with_svg_text_spans(\n    text_spans=[text_span_1, text_span_2],\n    font_size=16,\n    x=20,\n    y=32,\n    fill_color=ap.COLORLESS,\n)\n\nap.save_overall_html(dest_dir_path="svg_txt_span_line_thickness/")\n```': '```py\n# runnable\nimport apysc as ap\n\nstage: ap.Stage = ap.Stage(\n    background_color=ap.Color("#333"),\n    stage_width=200,\n    stage_height=50,\n    stage_elem_id="stage",\n)\ntext_span_1: ap.SvgTextSpan = ap.SvgTextSpan(\n    text="Lorem ",\n    line_color=ap.Color("#0af"),\n    font_size=20,\n    bold=True,\n)\ntext_span_2: ap.SvgTextSpan = ap.SvgTextSpan(\n    text="ipsum",\n    line_color=ap.Color("#0af"),\n    font_size=20,\n    bold=True,\n)\ntext_span_1.line_thickness = ap.Int(3)\ntext_span_2.line_thickness = ap.Int(3)\n\nsvg_text: ap.SvgText = ap.SvgText.create_with_svg_text_spans(\n    text_spans=[text_span_1, text_span_2],\n    font_size=16,\n    x=20,\n    y=32,\n    fill_color=ap.COLORLESS,\n)\n\nap.save_overall_html(dest_dir_path="svg_txt_span_line_thickness/")\n```',  # noqa
    ##################################################
    "## bold property interface example": "## bold 属性のインターフェイス例",
    ##################################################
    "The `bold` property updates or gets the instance's `bold` text setting.": "`bold`属性ではインスタンスの太字設定の更新もしくは取得を行えます。",  # noqa
    ##################################################
    '```py\n# runnable\nimport apysc as ap\n\nstage: ap.Stage = ap.Stage(\n    background_color=ap.Color("#333"),\n    stage_width=200,\n    stage_height=50,\n    stage_elem_id="stage",\n)\ntext_span_1: ap.SvgTextSpan = ap.SvgTextSpan(text="Lorem ")\ntext_span_2: ap.SvgTextSpan = ap.SvgTextSpan(text="ipsum")\ntext_span_2.bold = ap.Boolean(True)\n\nsvg_text: ap.SvgText = ap.SvgText.create_with_svg_text_spans(\n    text_spans=[text_span_1, text_span_2],\n    font_size=16,\n    x=20,\n    y=32,\n    fill_color=ap.Color("#aaa"),\n)\n\nap.save_overall_html(dest_dir_path="svg_txt_span_bold/")\n```': '```py\n# runnable\nimport apysc as ap\n\nstage: ap.Stage = ap.Stage(\n    background_color=ap.Color("#333"),\n    stage_width=200,\n    stage_height=50,\n    stage_elem_id="stage",\n)\ntext_span_1: ap.SvgTextSpan = ap.SvgTextSpan(text="Lorem ")\ntext_span_2: ap.SvgTextSpan = ap.SvgTextSpan(text="ipsum")\ntext_span_2.bold = ap.Boolean(True)\n\nsvg_text: ap.SvgText = ap.SvgText.create_with_svg_text_spans(\n    text_spans=[text_span_1, text_span_2],\n    font_size=16,\n    x=20,\n    y=32,\n    fill_color=ap.Color("#aaa"),\n)\n\nap.save_overall_html(dest_dir_path="svg_txt_span_bold/")\n```',  # noqa
    ##################################################
    "## italic property interface example": "## italic 属性のインターフェイス例",
    ##################################################
    "The `italic` property updates or gets the instance's `italic` style setting.": "`italic`属性ではインスタンスの斜体の設定の更新もしくは取得を行えます。",  # noqa
    ##################################################
    '```py\n# runnable\nimport apysc as ap\n\nstage: ap.Stage = ap.Stage(\n    background_color=ap.Color("#333"),\n    stage_width=200,\n    stage_height=50,\n    stage_elem_id="stage",\n)\ntext_span_1: ap.SvgTextSpan = ap.SvgTextSpan(text="Lorem ")\ntext_span_2: ap.SvgTextSpan = ap.SvgTextSpan(text="ipsum")\ntext_span_2.italic = ap.Boolean(True)\n\nsvg_text: ap.SvgText = ap.SvgText.create_with_svg_text_spans(\n    text_spans=[text_span_1, text_span_2],\n    font_size=16,\n    x=20,\n    y=32,\n    fill_color=ap.Color("#aaa"),\n)\n\nap.save_overall_html(dest_dir_path="svg_txt_span_italic/")\n```': '```py\n# runnable\nimport apysc as ap\n\nstage: ap.Stage = ap.Stage(\n    background_color=ap.Color("#333"),\n    stage_width=200,\n    stage_height=50,\n    stage_elem_id="stage",\n)\ntext_span_1: ap.SvgTextSpan = ap.SvgTextSpan(text="Lorem ")\ntext_span_2: ap.SvgTextSpan = ap.SvgTextSpan(text="ipsum")\ntext_span_2.italic = ap.Boolean(True)\n\nsvg_text: ap.SvgText = ap.SvgText.create_with_svg_text_spans(\n    text_spans=[text_span_1, text_span_2],\n    font_size=16,\n    x=20,\n    y=32,\n    fill_color=ap.Color("#aaa"),\n)\n\nap.save_overall_html(dest_dir_path="svg_txt_span_italic/")\n```',  # noqa
    ##################################################
    "## delta_x property interface example": "## delta_x 属性のインターフェイス例",
    ##################################################
    "The `delta_x` property updates or gets the instance's delta-x (x-coordinate adjustment).": "`delta_x`属性ではインスタンスのX座標の調整値の更新もしくは取得を行えます。",  # noqa
    ##################################################
    '```py\n# runnable\nimport apysc as ap\n\nstage: ap.Stage = ap.Stage(\n    background_color=ap.Color("#333"),\n    stage_width=200,\n    stage_height=50,\n    stage_elem_id="stage",\n)\ntext_span_1: ap.SvgTextSpan = ap.SvgTextSpan(text="Lorem ")\ntext_span_2: ap.SvgTextSpan = ap.SvgTextSpan(text="ipsum")\ntext_span_2.delta_x = ap.Number(-20)\n\nsvg_text: ap.SvgText = ap.SvgText.create_with_svg_text_spans(\n    text_spans=[text_span_1, text_span_2],\n    font_size=16,\n    x=20,\n    y=32,\n    fill_color=ap.Color("#aaa"),\n)\n\nap.save_overall_html(dest_dir_path="svg_txt_span_delta_x/")\n```': '```py\n# runnable\nimport apysc as ap\n\nstage: ap.Stage = ap.Stage(\n    background_color=ap.Color("#333"),\n    stage_width=200,\n    stage_height=50,\n    stage_elem_id="stage",\n)\ntext_span_1: ap.SvgTextSpan = ap.SvgTextSpan(text="Lorem ")\ntext_span_2: ap.SvgTextSpan = ap.SvgTextSpan(text="ipsum")\ntext_span_2.delta_x = ap.Number(-20)\n\nsvg_text: ap.SvgText = ap.SvgText.create_with_svg_text_spans(\n    text_spans=[text_span_1, text_span_2],\n    font_size=16,\n    x=20,\n    y=32,\n    fill_color=ap.Color("#aaa"),\n)\n\nap.save_overall_html(dest_dir_path="svg_txt_span_delta_x/")\n```',  # noqa
    ##################################################
    "## delta_y property interface example": "## delta_y 属性のインターフェイス例",
    ##################################################
    "The `delta_y` property updates or gets the instance's delta-y (y-coordinate adjustment).": "`delta_y`属性ではインスタンスのY座標の調整値の更新もくしは取得を行えます。",  # noqa
    ##################################################
    "Note: This setting inherits a y-coordinate from the previous `SvgTextSpan` instance.": "特記事項: この設定は直前の`SvgTextSpan`インスタンスの設定を引き継ぎます。",  # noqa
    ##################################################
    '```py\n# runnable\nimport apysc as ap\n\nstage: ap.Stage = ap.Stage(\n    background_color=ap.Color("#333"),\n    stage_width=200,\n    stage_height=80,\n    stage_elem_id="stage",\n)\ntext_span_1: ap.SvgTextSpan = ap.SvgTextSpan(text="Lorem ")\ntext_span_2: ap.SvgTextSpan = ap.SvgTextSpan(text="ipsum ")\ntext_span_3: ap.SvgTextSpan = ap.SvgTextSpan(text="dolar")\n\ntext_span_2.delta_y = ap.Number(10)\ntext_span_3.delta_y = ap.Number(10)\n\nsvg_text: ap.SvgText = ap.SvgText.create_with_svg_text_spans(\n    text_spans=[text_span_1, text_span_2],\n    font_size=16,\n    x=20,\n    y=32,\n    fill_color=ap.Color("#aaa"),\n)\n\nap.save_overall_html(dest_dir_path="svg_txt_span_delta_y/")\n```': '```py\n# runnable\nimport apysc as ap\n\nstage: ap.Stage = ap.Stage(\n    background_color=ap.Color("#333"),\n    stage_width=200,\n    stage_height=80,\n    stage_elem_id="stage",\n)\ntext_span_1: ap.SvgTextSpan = ap.SvgTextSpan(text="Lorem ")\ntext_span_2: ap.SvgTextSpan = ap.SvgTextSpan(text="ipsum ")\ntext_span_3: ap.SvgTextSpan = ap.SvgTextSpan(text="dolar")\n\ntext_span_2.delta_y = ap.Number(10)\ntext_span_3.delta_y = ap.Number(10)\n\nsvg_text: ap.SvgText = ap.SvgText.create_with_svg_text_spans(\n    text_spans=[text_span_1, text_span_2],\n    font_size=16,\n    x=20,\n    y=32,\n    fill_color=ap.Color("#aaa"),\n)\n\nap.save_overall_html(dest_dir_path="svg_txt_span_delta_y/")\n```',  # noqa
    ##################################################
    "## SvgTextSpan constructor API": "## SvgTextSpan クラスのコンストラクタのAPI",
    ##################################################
    '<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>': '<span class="inconspicuous-txt">特記事項: このAPIドキュメントはドキュメントビルド用のスクリプトによって自動で生成・同期されています。そのためもしかしたらこの節の内容は前節までの内容と重複している場合があります。</span>',  # noqa
    ##################################################
    "**[Interface summary]**": "**[インターフェイス概要]**",
    ##################################################
    "The class for an SVG text-span (the child class of `SvgText`).<hr>": "`SvgText`の子となるSVGのtext-span要素のためのクラスです。<hr>",  # noqa
    ##################################################
    "**[Parameters]**": "**[引数]**",
    ##################################################
    "- `text`: Union[str, String]": "- `text`: Union[str, String]",
    ##################################################
    "  - A text to use in this class.": "  - このクラスで使用するテキスト。",
    ##################################################
    "- `font_size`: Optional[Union[int, Int]], optional": "- `font_size`: Optional[Union[int, Int]], optional",  # noqa
    ##################################################
    "  - A font-size setting.": "  - フォントサイズ設定。",
    ##################################################
    "- `font_family`: Optional[Union[Array[String], List[str]]], optional": "- `font_family`: Optional[Union[Array[String], List[str]]], optional",  # noqa
    ##################################################
    "  - A font-family setting. Each string in an array needs to be a font name (e.g., `Times New Roman`).": "  - フォントファミリー設定。配列内の各文字列には個別のフォント名を指定する必要があります（例: `Times New Roman`）。",  # noqa
    ##################################################
    "- `fill_color`: Optional[Color], optional": "- `fill_color`: Optional[Color], optional",  # noqa
    ##################################################
    "  - A fill-color setting.": "  - 塗りの色の設定。",
    ##################################################
    "- `fill_alpha`: Optional[Union[float, Number]], optional": "- `fill_alpha`: Optional[Union[float, Number]], optional",  # noqa
    ##################################################
    "  - A fill-alpha setting.": "  - 塗りの透明度の設定。",
    ##################################################
    "- `line_color`: Optional[Color], optional": "- `line_color`: Optional[Color], optional",  # noqa
    ##################################################
    "  - A line-color setting.": "  - 線の色の設定。",
    ##################################################
    "- `line_alpha`: Optional[Union[float, Number]], optional": "- `line_alpha`: Optional[Union[float, Number]], optional",  # noqa
    ##################################################
    "  - A line-alpha setting.": "  - 線の透明度の設定。",
    ##################################################
    "- `line_thickness`: Optional[Union[int, Int]], optional": "- `line_thickness`: Optional[Union[int, Int]], optional",  # noqa
    ##################################################
    "  - A line-thickness (line-width) to set.": "  - 設定の線幅。",
    ##################################################
    "- `bold`: Optional[Union[bool, Boolean]], optional": "- `bold`: Optional[Union[bool, Boolean]], optional",  # noqa
    ##################################################
    "  - A boolean, whether this text is a bold style or not.": "  - テキストに太字のスタイル設定を行うかどうかの真偽値。",  # noqa
    ##################################################
    "- `italic`: Optional[Union[bool, Boolean]], optional": "- `italic`: Optional[Union[bool, Boolean]], optional",  # noqa
    ##################################################
    "  - A boolean, whether a text is an italic style or not (normal).": "  - テキストを斜体表示のスタイル設定を行うかどうかの真偽値。",  # noqa
    ##################################################
    "- `delta_x`: Union[float, Number], optional": "- `delta_x`: Union[float, Number], optional",  # noqa
    ##################################################
    "  - A coordinate delta-x setting. Notes: This setting also changes a coordinate of subsequent `SvgTextSpan`'s instance.": "  - X座標の調整値の設定。特記事項 : この設定は後に続く`SvgTextSpan`のインスタンスの座標も変更します。",  # noqa
    ##################################################
    "- `delta_y`: Union[float, Number], optional": "- `delta_y`: Union[float, Number], optional",  # noqa
    ##################################################
    "  - A coordinate delta-y setting. Notes: This setting also changes a coordinate of subsequent `SvgTextSpan`'s instance.": "  - Y座標の調整値の設定。特記事項 : この設定は後に続く`SvgTextSpan`のインスタンスの座標も更新します。",  # noqa
    ##################################################
    "- `variable_name_suffix`: str, optional": "- `variable_name_suffix`: str, optional",  # noqa
    ##################################################
    "  - A JavaScript variable name suffix string. This setting is sometimes useful for JavaScript debugging.": "  - JavaScript上の変数のサフィックスの設定です。この設定はJavaScriptのデバッグ時に役立つことがあります。",  # noqa
    ##################################################
    "<hr>": "<hr>",
    ##################################################
    "**[Notes]**": "**[特記事項]**",
    ##################################################
    " ・If style settings are `None`, its styles inherit parent style settings.<hr>": " ・もしも各種スタイル設定に`None`が指定された場合、そのスタイルは親のスタイル設定を引き継ぎます。<hr>",  # noqa
    ##################################################
    "**[Examples]**": "**[コードサンプル]**",
    ##################################################
    '```py\n>>> import apysc as ap\n>>> stage: ap.Stage = ap.Stage(\n...     background_color=ap.Color("#333"), stage_width=200, stage_height=50\n... )\n>>> svg_text: ap.SvgText = ap.SvgText.create_with_svg_text_spans(\n...     text_spans=[\n...         ap.SvgTextSpan(text="Hello, "),\n...         ap.SvgTextSpan(text="Hello, ", font_size=14),\n...     ],\n...     font_size=20,\n...     fill_color=ap.Color("#0af"),\n... )\n```': '```py\n>>> import apysc as ap\n>>> stage: ap.Stage = ap.Stage(\n...     background_color=ap.Color("#333"), stage_width=200, stage_height=50\n... )\n>>> svg_text: ap.SvgText = ap.SvgText.create_with_svg_text_spans(\n...     text_spans=[\n...         ap.SvgTextSpan(text="Hello, "),\n...         ap.SvgTextSpan(text="Hello, ", font_size=14),\n...     ],\n...     font_size=20,\n...     fill_color=ap.Color("#0af"),\n... )\n```',  # noqa
    ##################################################
    "<hr>": "<hr>",
    ##################################################
    "**[References]**": "**[関連資料]**",
    ##################################################
    "- [SvgText class](https://simon-ritchie.github.io/apysc/en/svg_text.html)": "- [SvgText クラス](https://simon-ritchie.github.io/apysc/jp/jp_svg_text.html)",  # noqa
    ##################################################
    "## SvgText create_with_svg_text_spans class method API": "## SvgText クラスの create_with_svg_text_spans クラスメソッドのAPI",  # noqa
    ##################################################
    '<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>': '<span class="inconspicuous-txt">特記事項: このAPIドキュメントはドキュメントビルド用のスクリプトによって自動で生成・同期されています。そのためもしかしたらこの節の内容は前節までの内容と重複している場合があります。</span>',  # noqa
    ##################################################
    "**[Interface summary]**": "**[インターフェイス概要]**",
    ##################################################
    "Create an `SvgText` instance with specified text spans.<hr>": "指定された各text spanのインスタンスを使用して`SvgText`のインスタンスを生成します。<hr>",  # noqa
    ##################################################
    "**[Parameters]**": "**[引数]**",
    ##################################################
    "- `text_spans`: Union[List[SvgTextSpan], Array[SvgTextSpan]]": "- `text_spans`: Union[List[SvgTextSpan], Array[SvgTextSpan]]",  # noqa
    ##################################################
    "  - Text spans.": "  - 各text span。",
    ##################################################
    "- `font_size`: Union[int, Int], optional": "- `font_size`: Union[int, Int], optional",  # noqa
    ##################################################
    "  - A font-size setting for an overall text.": "  - テキスト全体に設定するフォントサイズの設定。",
    ##################################################
    "- `font_family`: Optional[Union[Array[String], List[str]]], optional": "- `font_family`: Optional[Union[Array[String], List[str]]], optional",  # noqa
    ##################################################
    "  - A font-family setting for an overall text. Each string in an array needs to be a font name (e.g., `Times New Roman`).": "  - テキスト全体に設定するフォント設定。配列内の各文字列はフォント名を指定する必要があります（例 : `Times New Roman`）。",  # noqa
    ##################################################
    "- `x`: Union[float, Number], optional": "- `x`: Union[float, Number], optional",
    ##################################################
    "  - X-coordinate to start drawing.": "  - 描画を開始するX座標。",
    ##################################################
    "- `y`: Union[float, Number], optional": "- `y`: Union[float, Number], optional",
    ##################################################
    "  - Y-coordinate to start drawing (please see also the `Notes` section).": "  - 描画を開始するY座標（`特記事項`の節も確認をお願いします）。",  # noqa
    ##################################################
    "- `fill_color`: Color, optional": "- `fill_color`: Color, optional",
    ##################################################
    "  - A fill-color setting for an overall text.": "  - テキスト全体に設定する塗りの色。",
    ##################################################
    "- `fill_alpha`: float or Number, optional": "- `fill_alpha`: float or Number, optional",  # noqa
    ##################################################
    "  - A fill-alpha setting for an overall text.": "  - テキスト全体に設定する塗りの透明度。",
    ##################################################
    "- `line_color`: Color, optional": "- `line_color`: Color, optional",
    ##################################################
    "  - A line-color setting for an overall text.": "  - テキスト全体に設定する線の色。",
    ##################################################
    "- `line_alpha`: float or Number, optional": "- `line_alpha`: float or Number, optional",  # noqa
    ##################################################
    "  - A line-alpha setting for an overall text.": "  - テキスト全体に設定する線の透明度。",
    ##################################################
    "- `line_thickness`: int or Int, optional": "- `line_thickness`: int or Int, optional",  # noqa
    ##################################################
    "  - A line-thickness (line-width) setting for an overall text.": "  - テキスト全体に設定する線幅。",  # noqa
    ##################################################
    "- `leading`: float or Number, optional": "- `leading`: float or Number, optional",
    ##################################################
    "  - A text-leading size for an overall text.": "  - テキスト全体に設定する行間設定。",
    ##################################################
    "- `align`: SvgTextAlign, optional": "- `align`: SvgTextAlign, optional",
    ##################################################
    "  - A text-align setting for an overall text.": "  - テキスト全体に設定する行揃え設定。",
    ##################################################
    "- `bold`: Union[bool, Boolean], optional": "- `bold`: Union[bool, Boolean], optional",  # noqa
    ##################################################
    "  - A boolean, whether this text is a bold style or not.": "  - テキストに太字のスタイル設定を行うかどうかの真偽値。",  # noqa
    ##################################################
    "- `italic`: Union[bool, Boolean], optional": "- `italic`: Union[bool, Boolean], optional",  # noqa
    ##################################################
    "  - A boolean, whether a text is an italic style or not (normal).": "  - テキストを斜体表示のスタイル設定を行うかどうかの真偽値。",  # noqa
    ##################################################
    "- `parent`: Optional[ChildMixIn], optional": "- `parent`: Optional[ChildMixIn], optional",  # noqa
    ##################################################
    "  - A parent instance to add this instance. If the specified value is None, this interface uses a stage instance.": "  - このインスタンスを追加する親のインスタンス。もしもNoneが指定された場合、このインスタンスはステージのインスタンスへと追加されます。",  # noqa
    ##################################################
    "- `variable_name_suffix`: str, optional": "- `variable_name_suffix`: str, optional",  # noqa
    ##################################################
    "  - A JavaScript variable name suffix string. This setting is sometimes useful for JavaScript debugging.": "  - JavaScript上の変数のサフィックスの設定です。この設定はJavaScriptのデバッグ時に役立つことがあります。",  # noqa
    ##################################################
    "<hr>": "<hr>",
    ##################################################
    "**[Returns]**": "**[返却値]**",
    ##################################################
    "- `svg_text`: SvgText": "- `svg_text`: SvgText",
    ##################################################
    "  - A created `SvgText` instance.": "  - 生成された`SvgText`のインスタンス。",
    ##################################################
    "<hr>": "<hr>",
    ##################################################
    "**[Notes]**": "**[特記事項]**",
    ##################################################
    " ・SvgText's y-coordinate zero-position starts at the bottom of a text. So if you set y=0, a text becomes almost invisible.<hr>": " ・SVGTextクラスの座標の0の位置はテキストの下部からスタートします。そのためもしもy=0を指定した場合、テキストはほとんど見えない状態になります。<hr>",  # noqa
    ##################################################
    "**[Examples]**": "**[コードサンプル]**",
    ##################################################
    '```py\n>>> import apysc as ap\n>>> stage: ap.Stage = ap.Stage(\n...     background_color=ap.Color("#333"),\n...     stage_width=200,\n...     stage_height=50,\n... )\n>>> svg_text: ap.SvgText = ap.SvgText.create_with_svg_text_spans(\n...     text_spans=[\n...         ap.SvgTextSpan(text="Hello, "),\n...         ap.SvgTextSpan(text="Hello, ", font_size=14),\n...     ],\n...     font_size=20,\n...     fill_color=ap.Color("#0af"),\n... )\n```': '```py\n>>> import apysc as ap\n>>> stage: ap.Stage = ap.Stage(\n...     background_color=ap.Color("#333"),\n...     stage_width=200,\n...     stage_height=50,\n... )\n>>> svg_text: ap.SvgText = ap.SvgText.create_with_svg_text_spans(\n...     text_spans=[\n...         ap.SvgTextSpan(text="Hello, "),\n...         ap.SvgTextSpan(text="Hello, ", font_size=14),\n...     ],\n...     font_size=20,\n...     fill_color=ap.Color("#0af"),\n... )\n```',  # noqa
    ##################################################
    "<hr>": "<hr>",
    ##################################################
    "**[References]**": "**[関連資料]**",
    ##################################################
    "- [SvgText class](https://simon-ritchie.github.io/apysc/en/svg_text.html)": "- [SvgText クラス](https://simon-ritchie.github.io/apysc/jp/jp_svg_text.html)",  # noqa
}
