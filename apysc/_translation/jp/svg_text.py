"""This module is for the translation mapping data of the
following document:

Document file: svg_text.md
Language: jp
"""

from typing import Dict

MAPPING: Dict[str, str] = {
    ##################################################
    "# SvgText class": "# SvgText クラス",
    ##################################################
    "This page explains the `SvgText` class.": "このページでは`SvgText`クラスについて説明します。",
    ##################################################
    "## What class is this?": "## クラス概要",
    ##################################################
    "The `SvgText` class creates an SVG text object.": "`SvgText`クラスはSVGテキストのオブジェクトを生成します。",  # noqa
    ##################################################
    "## Basic usage": "## 基本的な使い方",
    ##################################################
    "The `SvgText` class constructor requires the `text` argument.": "`SvgText`クラスのコンストラクタは`text`引数の指定を必要とします。",  # noqa
    ##################################################
    "The constructor also accepts each font's and style's argument, such as the `font_size`, `font_family`, `fill_color`, and `bold`.": "コンストラクタでは`font_size`や`font_family`、`fill_color`、`bold`などのフォントやスタイルなどの引数を指定することもできます。",  # noqa
    ##################################################
    '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    background_color=ap.Color("#333"),\n    stage_width=200,\n    stage_height=50,\n    stage_elem_id="stage",\n)\nsvg_text: ap.SvgText = ap.SvgText(\n    text="Hello, world!",\n    x=20,\n    y=32,\n    fill_color=ap.Color("#aaa"),\n)\nap.save_overall_html(dest_dir_path="svg_text_basic_usage/")\n```': '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    background_color=ap.Color("#333"),\n    stage_width=200,\n    stage_height=50,\n    stage_elem_id="stage",\n)\nsvg_text: ap.SvgText = ap.SvgText(\n    text="Hello, world!",\n    x=20,\n    y=32,\n    fill_color=ap.Color("#aaa"),\n)\nap.save_overall_html(dest_dir_path="svg_text_basic_usage/")\n```',  # noqa
    ##################################################
    "## Note on the baseline of a text's y-coordinate": "## テキストのY座標の基準点に対する特記事項",
    ##################################################
    "The baseline of a text's y-coordinate is the text's bottom position (this is the specification of the SVG text).": "テキストのY座標の基準点はテキストの下部付近の位置となります（これはSVGテキストの仕様となります）。",  # noqa
    ##################################################
    "So if you specify `y=0` as the coordinate, you can see almost nothing of a text's content (barely see the bottom of the comma in the following example).": "そのためもしもY座標に`y=0`を指定した場合、テキストのコンテンツがほとんど見えなくなります（以下の例では辛うじてコンマの一部が確認できます）。",  # noqa
    ##################################################
    '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    background_color=ap.Color("#333"),\n    stage_width=200,\n    stage_height=50,\n    stage_elem_id="stage",\n)\nsvg_text: ap.SvgText = ap.SvgText(\n    text="Hello, world!",\n    x=20,\n    y=0,\n    fill_color=ap.Color("#aaa"),\n)\nap.save_overall_html(dest_dir_path="svg_text_note_on_the_y_baseline/")\n```': '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    background_color=ap.Color("#333"),\n    stage_width=200,\n    stage_height=50,\n    stage_elem_id="stage",\n)\nsvg_text: ap.SvgText = ap.SvgText(\n    text="Hello, world!",\n    x=20,\n    y=0,\n    fill_color=ap.Color("#aaa"),\n)\nap.save_overall_html(dest_dir_path="svg_text_note_on_the_y_baseline/")\n```',  # noqa
    ##################################################
    "## text property interface example": "## text 属性のインターフェイス例",
    ##################################################
    "The `text` property updates or gets the instance's text.": "`text`属性ではインスタンスのテキストの更新もしくは取得を行えます。",  # noqa
    ##################################################
    '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    background_color=ap.Color("#333"),\n    stage_width=200,\n    stage_height=50,\n    stage_elem_id="stage",\n)\nsvg_text: ap.SvgText = ap.SvgText(\n    text="Hello, world!",\n    x=20,\n    y=32,\n    fill_color=ap.Color("#aaa"),\n)\nsvg_text.text = ap.String("Lorem ipsum")\nap.save_overall_html(dest_dir_path="svg_text_text/")\n```': '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    background_color=ap.Color("#333"),\n    stage_width=200,\n    stage_height=50,\n    stage_elem_id="stage",\n)\nsvg_text: ap.SvgText = ap.SvgText(\n    text="Hello, world!",\n    x=20,\n    y=32,\n    fill_color=ap.Color("#aaa"),\n)\nsvg_text.text = ap.String("Lorem ipsum")\nap.save_overall_html(dest_dir_path="svg_text_text/")\n```',  # noqa
    ##################################################
    "## font_size property interface example": "## font_size 属性のインターフェイス例",
    ##################################################
    "The `font_size` property updates or gets the instance's font size.": "`font_size`属性ではインスタンスのフォントサイズの更新もしくは取得を行えます。",  # noqa
    ##################################################
    '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    background_color=ap.Color("#333"),\n    stage_width=200,\n    stage_height=50,\n    stage_elem_id="stage",\n)\nsvg_text: ap.SvgText = ap.SvgText(\n    text="Hello, world!",\n    x=20,\n    y=34,\n    fill_color=ap.Color("#aaa"),\n)\nsvg_text.font_size = ap.Int(24)\nap.save_overall_html(dest_dir_path="svg_text_font_size/")\n```': '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    background_color=ap.Color("#333"),\n    stage_width=200,\n    stage_height=50,\n    stage_elem_id="stage",\n)\nsvg_text: ap.SvgText = ap.SvgText(\n    text="Hello, world!",\n    x=20,\n    y=34,\n    fill_color=ap.Color("#aaa"),\n)\nsvg_text.font_size = ap.Int(24)\nap.save_overall_html(dest_dir_path="svg_text_font_size/")\n```',  # noqa
    ##################################################
    "## font_family property interface example": "## font_family 属性のインターフェイス例",
    ##################################################
    "The `font_family` property updates or gets the instance's font family.": "`font_family`属性ではインスタンスのフォントファミリー（フォントの指定）の更新もしくは取得を行えます。",  # noqa
    ##################################################
    "This property requires an `Array` of each font name `String`.": "この属性は各フォント名の`String`型の文字列を格納した`Array`型の配列を必要とします。",  # noqa
    ##################################################
    '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    background_color=ap.Color("#333"),\n    stage_width=200,\n    stage_height=50,\n    stage_elem_id="stage",\n)\nsvg_text: ap.SvgText = ap.SvgText(\n    text="Hello, world!",\n    x=20,\n    y=32,\n    fill_color=ap.Color("#aaa"),\n)\nsvg_text.font_family = ap.Array([ap.String("Impact"), ap.String("Times New Roman")])\nap.save_overall_html(dest_dir_path="svg_text_font_family/")\n```': '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    background_color=ap.Color("#333"),\n    stage_width=200,\n    stage_height=50,\n    stage_elem_id="stage",\n)\nsvg_text: ap.SvgText = ap.SvgText(\n    text="Hello, world!",\n    x=20,\n    y=32,\n    fill_color=ap.Color("#aaa"),\n)\nsvg_text.font_family = ap.Array([ap.String("Impact"), ap.String("Times New Roman")])\nap.save_overall_html(dest_dir_path="svg_text_font_family/")\n```',  # noqa
    ##################################################
    "## x property interface example": "## x属性のインターフェイス例",
    ##################################################
    "The `x` property updates or gets the instance's x-coordinate:": "`x`属性ではX座標の値の更新もしくは取得を行えます:",  # noqa
    ##################################################
    '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    background_color=ap.Color("#333"),\n    stage_width=200,\n    stage_height=50,\n    stage_elem_id="stage",\n)\nsvg_text: ap.SvgText = ap.SvgText(\n    text="Hello, world!",\n    y=32,\n    fill_color=ap.Color("#aaa"),\n)\nsvg_text.x = ap.Number(50)\nap.save_overall_html(dest_dir_path="svg_text_x/")\n```': '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    background_color=ap.Color("#333"),\n    stage_width=200,\n    stage_height=50,\n    stage_elem_id="stage",\n)\nsvg_text: ap.SvgText = ap.SvgText(\n    text="Hello, world!",\n    y=32,\n    fill_color=ap.Color("#aaa"),\n)\nsvg_text.x = ap.Number(50)\nap.save_overall_html(dest_dir_path="svg_text_x/")\n```',  # noqa
    ##################################################
    "## y property interface example": "## y属性のインターフェイス例",
    ##################################################
    "The `y` property updates or gets the instance's y-coordinate:": "`y`属性ではY座標の値の更新もしくは取得を行えます:",  # noqa
    ##################################################
    '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    background_color=ap.Color("#333"),\n    stage_width=200,\n    stage_height=70,\n    stage_elem_id="stage",\n)\nsvg_text: ap.SvgText = ap.SvgText(\n    text="Hello, world!",\n    x=20,\n    y=32,\n    fill_color=ap.Color("#aaa"),\n)\nsvg_text.y = ap.Number(45)\nap.save_overall_html(dest_dir_path="svg_text_y/")\n```': '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    background_color=ap.Color("#333"),\n    stage_width=200,\n    stage_height=70,\n    stage_elem_id="stage",\n)\nsvg_text: ap.SvgText = ap.SvgText(\n    text="Hello, world!",\n    x=20,\n    y=32,\n    fill_color=ap.Color("#aaa"),\n)\nsvg_text.y = ap.Number(45)\nap.save_overall_html(dest_dir_path="svg_text_y/")\n```',  # noqa
    ##################################################
    "## fill_color property interface example": "## fill_color属性のインターフェイス例",
    ##################################################
    "The `fill_color` property updates or gets the instance's fill color:": "`fill_color`属性は塗りの色の値の更新もしくは取得を行えます:",  # noqa
    ##################################################
    '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    background_color=ap.Color("#333"),\n    stage_width=200,\n    stage_height=50,\n    stage_elem_id="stage",\n)\nsvg_text: ap.SvgText = ap.SvgText(\n    text="Hello, world!",\n    x=20,\n    y=32,\n)\nsvg_text.fill_color = ap.Color("#0af")\nap.save_overall_html(dest_dir_path="svg_text_fill_color/")\n```': '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    background_color=ap.Color("#333"),\n    stage_width=200,\n    stage_height=50,\n    stage_elem_id="stage",\n)\nsvg_text: ap.SvgText = ap.SvgText(\n    text="Hello, world!",\n    x=20,\n    y=32,\n)\nsvg_text.fill_color = ap.Color("#0af")\nap.save_overall_html(dest_dir_path="svg_text_fill_color/")\n```',  # noqa
    ##################################################
    "## fill_alpha property interface example": "## fill_alpha属性のインターフェイス例",
    ##################################################
    "The `fill_alpha` property updates or gets the instance's fill alpha (opacity):": "`fill_alpha`属性は塗りの透明度の値の更新もしくは取得を行えます:",  # noqa
    ##################################################
    '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    background_color=ap.Color("#333"),\n    stage_width=200,\n    stage_height=50,\n    stage_elem_id="stage",\n)\nsvg_text: ap.SvgText = ap.SvgText(\n    text="Hello, world!",\n    x=20,\n    y=32,\n    fill_color=ap.Color("#aaa"),\n)\nsvg_text.fill_alpha = ap.Number(0.3)\nap.save_overall_html(dest_dir_path="svg_text_fill_alpha/")\n```': '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    background_color=ap.Color("#333"),\n    stage_width=200,\n    stage_height=50,\n    stage_elem_id="stage",\n)\nsvg_text: ap.SvgText = ap.SvgText(\n    text="Hello, world!",\n    x=20,\n    y=32,\n    fill_color=ap.Color("#aaa"),\n)\nsvg_text.fill_alpha = ap.Number(0.3)\nap.save_overall_html(dest_dir_path="svg_text_fill_alpha/")\n```',  # noqa
    ##################################################
    "## line_color property interface example": "## line_color属性のインターフェイス例",
    ##################################################
    "The `line_color` property updates or gets the instance's line color:": "`line_color`属性では線の色の値の更新もしくは取得を行えます:",  # noqa
    ##################################################
    '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    background_color=ap.Color("#333"),\n    stage_width=200,\n    stage_height=50,\n    stage_elem_id="stage",\n)\nsvg_text: ap.SvgText = ap.SvgText(\n    text="Hello, world!",\n    x=20,\n    y=34,\n    font_size=24,\n    bold=True,\n    fill_color=ap.COLORLESS,\n    line_thickness=1,\n)\nsvg_text.line_color = ap.Color("#0af")\nap.save_overall_html(dest_dir_path="svg_text_line_color/")\n```': '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    background_color=ap.Color("#333"),\n    stage_width=200,\n    stage_height=50,\n    stage_elem_id="stage",\n)\nsvg_text: ap.SvgText = ap.SvgText(\n    text="Hello, world!",\n    x=20,\n    y=34,\n    font_size=24,\n    bold=True,\n    fill_color=ap.COLORLESS,\n    line_thickness=1,\n)\nsvg_text.line_color = ap.Color("#0af")\nap.save_overall_html(dest_dir_path="svg_text_line_color/")\n```',  # noqa
    ##################################################
    "## line_alpha property interface example": "## line_alpha属性のインターフェイス例",
    ##################################################
    "The `line_alpha` property updates or gets the instance's line alpha (opacity):": "`line_alpha`属性では線の透明度の値の更新もしくは取得を行えます:",  # noqa
    ##################################################
    '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    background_color=ap.Color("#333"),\n    stage_width=200,\n    stage_height=50,\n    stage_elem_id="stage",\n)\nsvg_text: ap.SvgText = ap.SvgText(\n    text="Hello, world!",\n    x=20,\n    y=34,\n    font_size=24,\n    bold=True,\n    fill_color=ap.COLORLESS,\n    line_color=ap.Color("#0af"),\n    line_thickness=1,\n)\nsvg_text.line_alpha = ap.Number(0.3)\nap.save_overall_html(dest_dir_path="svg_text_line_alpha/")\n```': '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    background_color=ap.Color("#333"),\n    stage_width=200,\n    stage_height=50,\n    stage_elem_id="stage",\n)\nsvg_text: ap.SvgText = ap.SvgText(\n    text="Hello, world!",\n    x=20,\n    y=34,\n    font_size=24,\n    bold=True,\n    fill_color=ap.COLORLESS,\n    line_color=ap.Color("#0af"),\n    line_thickness=1,\n)\nsvg_text.line_alpha = ap.Number(0.3)\nap.save_overall_html(dest_dir_path="svg_text_line_alpha/")\n```',  # noqa
    ##################################################
    "## line_thickness property interface example": "## line_thickness属性のインターフェイス例",
    ##################################################
    "The `line_thickness` property updates or gets the instance's line thickness (line width):": "`line_thickness`属性では線の幅の更新もしくは取得を行えます:",  # noqa
    ##################################################
    '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    background_color=ap.Color("#333"),\n    stage_width=200,\n    stage_height=50,\n    stage_elem_id="stage",\n)\nsvg_text: ap.SvgText = ap.SvgText(\n    text="Hello, world!",\n    x=20,\n    y=34,\n    font_size=24,\n    bold=True,\n    fill_color=ap.COLORLESS,\n    line_color=ap.Color("#0af"),\n)\nsvg_text.line_thickness = ap.Int(3)\nap.save_overall_html(dest_dir_path="svg_text_line_thickness/")\n```': '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    background_color=ap.Color("#333"),\n    stage_width=200,\n    stage_height=50,\n    stage_elem_id="stage",\n)\nsvg_text: ap.SvgText = ap.SvgText(\n    text="Hello, world!",\n    x=20,\n    y=34,\n    font_size=24,\n    bold=True,\n    fill_color=ap.COLORLESS,\n    line_color=ap.Color("#0af"),\n)\nsvg_text.line_thickness = ap.Int(3)\nap.save_overall_html(dest_dir_path="svg_text_line_thickness/")\n```',  # noqa
    ##################################################
    "## leading property interface example": "## leading 属性のインターフェイス例",
    ##################################################
    "The `leading` property updates or gets the instance's text leading (line height).": "`leading`属性ではインスタンスの行間の更新もしくは取得を行えます。",  # noqa
    ##################################################
    '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    background_color=ap.Color("#333"),\n    stage_width=500,\n    stage_height=120,\n    stage_elem_id="stage",\n)\nsvg_text: ap.SvgText = ap.SvgText(\n    text="Lorem ipsum dolor sit amet,\nconsectetur adipiscing elit,\n"\n    "sed do eiusmod tempor incididunt",\n    x=20,\n    y=32,\n    fill_color=ap.Color("#aaa"),\n)\nsvg_text.leading = ap.Number(2.0)\n\nap.save_overall_html(dest_dir_path="svg_text_leading/")\n```': '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    background_color=ap.Color("#333"),\n    stage_width=500,\n    stage_height=120,\n    stage_elem_id="stage",\n)\nsvg_text: ap.SvgText = ap.SvgText(\n    text="Lorem ipsum dolor sit amet,\nconsectetur adipiscing elit,\n"\n    "sed do eiusmod tempor incididunt",\n    x=20,\n    y=32,\n    fill_color=ap.Color("#aaa"),\n)\nsvg_text.leading = ap.Number(2.0)\n\nap.save_overall_html(dest_dir_path="svg_text_leading/")\n```',  # noqa
    ##################################################
    "## align property interface example": "## align 属性のインターフェイス例",
    ##################################################
    "The `align` property updates or gets the instance's horizontal text alignment (left, center, or right).": "`align`属性ではインスタンスの水平方向の行揃えの設定（左端、中央、右端）の更新もしくは取得を行えます。",  # noqa
    ##################################################
    "This property requires the `SvgTextAlign` enum.": "この属性は`SvgTextAlign`のenumの値を必要とします。",  # noqa
    ##################################################
    '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    background_color=ap.Color("#333"),\n    stage_width=500,\n    stage_height=100,\n    stage_elem_id="stage",\n)\nsvg_text: ap.SvgText = ap.SvgText(\n    text="Lorem ipsum dolor sit amet,\nconsectetur adipiscing elit,\n"\n    "sed do eiusmod tempor incididunt",\n    x=250,\n    y=32,\n    fill_color=ap.Color("#aaa"),\n)\nsvg_text.align = ap.SvgTextAlign.CENTER\n\nap.save_overall_html(dest_dir_path="svg_text_align/")\n```': '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    background_color=ap.Color("#333"),\n    stage_width=500,\n    stage_height=100,\n    stage_elem_id="stage",\n)\nsvg_text: ap.SvgText = ap.SvgText(\n    text="Lorem ipsum dolor sit amet,\nconsectetur adipiscing elit,\n"\n    "sed do eiusmod tempor incididunt",\n    x=250,\n    y=32,\n    fill_color=ap.Color("#aaa"),\n)\nsvg_text.align = ap.SvgTextAlign.CENTER\n\nap.save_overall_html(dest_dir_path="svg_text_align/")\n```',  # noqa
    ##################################################
    "Note: This property setting changes x coordinate baseline (position of `x=0`), as follows:": "特記事項: この属性はX座標の基準位置（`x=0`の位置）を以下のように変更します:",  # noqa
    ##################################################
    "- SvgTextAlign.CENTER: X coordinate baseline becomes the text's center position.": "- SvgTextAlign.CENTER: X座標の基準位置はテキストの中央位置になります。",  # noqa
    ##################################################
    "- SvgTextAlign.RIGHT: X coordinate baseline becomes the text's right position.": "- SvgTextAlign.RIGHT: X座標の基準位置はテキストの右端の位置になります。",  # noqa
    ##################################################
    '```py\n# runnable\nimport apysc as ap\n\nSTAGE_WIDTH: int = 500\nSTAGE_HEIGHT: int = 120\nap.Stage(\n    background_color=ap.Color("#333"),\n    stage_width=STAGE_WIDTH,\n    stage_height=STAGE_HEIGHT,\n    stage_elem_id="stage",\n)\ncontainer_sprite: ap.Sprite = ap.Sprite()\ncontainer_sprite.x = ap.Number(STAGE_WIDTH / 2)\n\nvertical_x0_line: ap.Line = ap.Line(\n    start_point=ap.Point2D(0, 0),\n    end_point=ap.Point2D(0, STAGE_HEIGHT),\n    line_color=ap.Color("#666"),\n    parent=container_sprite,\n)\nx0_text: ap.SvgText = ap.SvgText(\n    text="Text\'s x=0 position",\n    fill_color=ap.Color("#666"),\n    x=5,\n    y=20,\n    parent=container_sprite,\n)\n\nleft_align_sample_text: ap.SvgText = ap.SvgText(\n    text="Left align sample (default)",\n    x=0,\n    y=52,\n    fill_color=ap.Color("#aaa"),\n    parent=container_sprite,\n)\n\ncenter_align_sample_text: ap.SvgText = ap.SvgText(\n    text="Center align sample",\n    x=0,\n    y=72,\n    fill_color=ap.Color("#aaa"),\n    parent=container_sprite,\n)\ncenter_align_sample_text.align = ap.SvgTextAlign.CENTER\n\nright_align_sample_text: ap.SvgText = ap.SvgText(\n    text="Right align sample",\n    x=0,\n    y=92,\n    fill_color=ap.Color("#aaa"),\n    parent=container_sprite,\n)\nright_align_sample_text.align = ap.SvgTextAlign.RIGHT\n\nap.save_overall_html(dest_dir_path="svg_text_align_note/")\n```': '```py\n# runnable\nimport apysc as ap\n\nSTAGE_WIDTH: int = 500\nSTAGE_HEIGHT: int = 120\nap.Stage(\n    background_color=ap.Color("#333"),\n    stage_width=STAGE_WIDTH,\n    stage_height=STAGE_HEIGHT,\n    stage_elem_id="stage",\n)\ncontainer_sprite: ap.Sprite = ap.Sprite()\ncontainer_sprite.x = ap.Number(STAGE_WIDTH / 2)\n\nvertical_x0_line: ap.Line = ap.Line(\n    start_point=ap.Point2D(0, 0),\n    end_point=ap.Point2D(0, STAGE_HEIGHT),\n    line_color=ap.Color("#666"),\n    parent=container_sprite,\n)\nx0_text: ap.SvgText = ap.SvgText(\n    text="Text\'s x=0 position",\n    fill_color=ap.Color("#666"),\n    x=5,\n    y=20,\n    parent=container_sprite,\n)\n\nleft_align_sample_text: ap.SvgText = ap.SvgText(\n    text="Left align sample (default)",\n    x=0,\n    y=52,\n    fill_color=ap.Color("#aaa"),\n    parent=container_sprite,\n)\n\ncenter_align_sample_text: ap.SvgText = ap.SvgText(\n    text="Center align sample",\n    x=0,\n    y=72,\n    fill_color=ap.Color("#aaa"),\n    parent=container_sprite,\n)\ncenter_align_sample_text.align = ap.SvgTextAlign.CENTER\n\nright_align_sample_text: ap.SvgText = ap.SvgText(\n    text="Right align sample",\n    x=0,\n    y=92,\n    fill_color=ap.Color("#aaa"),\n    parent=container_sprite,\n)\nright_align_sample_text.align = ap.SvgTextAlign.RIGHT\n\nap.save_overall_html(dest_dir_path="svg_text_align_note/")\n```',  # noqa
    ##################################################
    "## bold property interface example": "## bold 属性のインターフェイス例",
    ##################################################
    "The `bold` property updates or gets the instance's `bold` text setting.": "`bold`属性ではインスタンスの太字設定の更新もしくは取得を行えます。",  # noqa
    ##################################################
    '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    background_color=ap.Color("#333"),\n    stage_width=200,\n    stage_height=50,\n    stage_elem_id="stage",\n)\nsvg_text: ap.SvgText = ap.SvgText(\n    text="Bold style sample",\n    x=20,\n    y=32,\n    fill_color=ap.Color("#aaa"),\n)\nsvg_text.bold = ap.Boolean(True)\nap.save_overall_html(dest_dir_path="svg_text_bold/")\n```': '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    background_color=ap.Color("#333"),\n    stage_width=200,\n    stage_height=50,\n    stage_elem_id="stage",\n)\nsvg_text: ap.SvgText = ap.SvgText(\n    text="Bold style sample",\n    x=20,\n    y=32,\n    fill_color=ap.Color("#aaa"),\n)\nsvg_text.bold = ap.Boolean(True)\nap.save_overall_html(dest_dir_path="svg_text_bold/")\n```',  # noqa
    ##################################################
    "## italic property interface example": "## italic 属性のインターフェイス例",
    ##################################################
    "The `italic` property updates or gets the instance's `italic` style setting.": "`italic`属性ではインスタンスの斜体の設定の更新もしくは取得を行えます。",  # noqa
    ##################################################
    '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    background_color=ap.Color("#333"),\n    stage_width=200,\n    stage_height=50,\n    stage_elem_id="stage",\n)\nsvg_text: ap.SvgText = ap.SvgText(\n    text="Italic style sample",\n    x=20,\n    y=32,\n    fill_color=ap.Color("#aaa"),\n)\nsvg_text.italic = ap.Boolean(True)\nap.save_overall_html(dest_dir_path="svg_text_italic/")\n```': '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    background_color=ap.Color("#333"),\n    stage_width=200,\n    stage_height=50,\n    stage_elem_id="stage",\n)\nsvg_text: ap.SvgText = ap.SvgText(\n    text="Italic style sample",\n    x=20,\n    y=32,\n    fill_color=ap.Color("#aaa"),\n)\nsvg_text.italic = ap.Boolean(True)\nap.save_overall_html(dest_dir_path="svg_text_italic/")\n```',  # noqa
    ##################################################
    "## rotation_around_center property interface example": "## rotation_around_center属性のインターフェイス例",  # noqa
    ##################################################
    "The `rotation_around_center` property updates or gets the instance's rotation value (0 to 359) from the center point:": "`rotation_around_center`属性ではインスタンスの中央座標での回転量（0～359）の更新もしくは取得を行えます:",  # noqa
    ##################################################
    '```py\n# runnable\nimport apysc as ap\n\nstage: ap.Stage = ap.Stage(\n    background_color=ap.Color("#333"),\n    stage_width=200,\n    stage_height=50,\n    stage_elem_id="stage",\n)\nsvg_text: ap.SvgText = ap.SvgText(\n    text="Hello, world!",\n    x=100,\n    y=32,\n    fill_color=ap.Color("#aaa"),\n    align=ap.SvgTextAlign.CENTER,\n)\n\n\ndef on_enter_frame(e: ap.EnterFrameEvent, optional: dict) -> None:\n    """\n    The handler to handle a timer event.\n\n    Parameters\n    ----------\n    e : ap.EnterFrameEvent\n        Event instance.\n    optional : dict\n        Optional argument dictionary.\n    """\n    svg_text.rotation_around_center += 1\n\n\nstage.enter_frame(handler=on_enter_frame)\nap.save_overall_html(dest_dir_path="svg_txt_rotation_around_center/")\n```': '```py\n# runnable\nimport apysc as ap\n\nstage: ap.Stage = ap.Stage(\n    background_color=ap.Color("#333"),\n    stage_width=200,\n    stage_height=50,\n    stage_elem_id="stage",\n)\nsvg_text: ap.SvgText = ap.SvgText(\n    text="Hello, world!",\n    x=100,\n    y=32,\n    fill_color=ap.Color("#aaa"),\n    align=ap.SvgTextAlign.CENTER,\n)\n\n\ndef on_enter_frame(e: ap.EnterFrameEvent, optional: dict) -> None:\n    """\n    The handler to handle a timer event.\n\n    Parameters\n    ----------\n    e : ap.EnterFrameEvent\n        Event instance.\n    optional : dict\n        Optional argument dictionary.\n    """\n    svg_text.rotation_around_center += 1\n\n\nstage.enter_frame(handler=on_enter_frame)\nap.save_overall_html(dest_dir_path="svg_txt_rotation_around_center/")\n```',  # noqa
    ##################################################
    "## set_rotation_around_point and get_rotation_around_point methods interface example": "## set_rotation_around_pointとget_rotation_around_pointメソッドのインターフェイス例",  # noqa
    ##################################################
    "The `set_rotation_around_point` method updates the instance's rotation value (0 to 359) from a specified point.": "`set_rotation_around_point`メソッドは指定された座標からのインスタンスの回転量（0～359）を更新します。",  # noqa
    ##################################################
    "Similarly, the `get_rotation_around_point` method gets the instance's rotation value (0 to 359) from a specified point:": "同様に、`get_rotation_around_point`メソッドでは指定された座標のインスタンスの回転量（0～359）を取得します:",  # noqa
    ##################################################
    '```py\n# runnable\nimport apysc as ap\n\nstage: ap.Stage = ap.Stage(\n    background_color=ap.Color("#333"),\n    stage_width=200,\n    stage_height=120,\n    stage_elem_id="stage",\n)\nX: ap.Number = ap.Number(20)\nY: ap.Number = ap.Number(32)\nsvg_text: ap.SvgText = ap.SvgText(\n    text="Hello, world!",\n    x=X,\n    y=Y,\n    fill_color=ap.Color("#aaa"),\n)\n\n\ndef on_enter_frame(e: ap.EnterFrameEvent, optional: dict) -> None:\n    """\n    The handler to handle a timer event.\n\n    Parameters\n    ----------\n    e : ap.EnterFrameEvent\n        Event instance.\n    optional : dict\n        Optional argument dictionary.\n    """\n    rotation: ap.Int = (\n        svg_text.get_rotation_around_point(\n            x=X,\n            y=Y,\n        )\n        + 1\n    )\n    svg_text.set_rotation_around_point(\n        rotation=rotation,\n        x=X,\n        y=Y,\n    )\n\n\nstage.enter_frame(handler=on_enter_frame)\nap.save_overall_html(dest_dir_path="svg_txt_rotation_around_point/")\n```': '```py\n# runnable\nimport apysc as ap\n\nstage: ap.Stage = ap.Stage(\n    background_color=ap.Color("#333"),\n    stage_width=200,\n    stage_height=120,\n    stage_elem_id="stage",\n)\nX: ap.Number = ap.Number(20)\nY: ap.Number = ap.Number(32)\nsvg_text: ap.SvgText = ap.SvgText(\n    text="Hello, world!",\n    x=X,\n    y=Y,\n    fill_color=ap.Color("#aaa"),\n)\n\n\ndef on_enter_frame(e: ap.EnterFrameEvent, optional: dict) -> None:\n    """\n    The handler to handle a timer event.\n\n    Parameters\n    ----------\n    e : ap.EnterFrameEvent\n        Event instance.\n    optional : dict\n        Optional argument dictionary.\n    """\n    rotation: ap.Int = (\n        svg_text.get_rotation_around_point(\n            x=X,\n            y=Y,\n        )\n        + 1\n    )\n    svg_text.set_rotation_around_point(\n        rotation=rotation,\n        x=X,\n        y=Y,\n    )\n\n\nstage.enter_frame(handler=on_enter_frame)\nap.save_overall_html(dest_dir_path="svg_txt_rotation_around_point/")\n```',  # noqa
    ##################################################
    "## Scale-related interfaces note": "## 拡縮関係のインターフェイスに対する特記事項",
    ##################################################
    "The scale-related interfaces are not recommended as the display may become distorted depending on the settings.": "拡縮関係のインターフェイスは設定次第では表示が崩れたりするため利用は非推奨です。",  # noqa
    ##################################################
    "## scale_x_from_center property interface example": "## scale_x_from_center属性のインターフェイス例",  # noqa
    ##################################################
    "The `scale_x_from_center` property updates or gets the instance's scale-x from the center point:": "`scale_x_from_center`属性ではインスタンスの中央座標でのX軸の拡縮値の更新もしくは取得を行えます:",  # noqa
    ##################################################
    '```py\n# runnable\nimport apysc as ap\n\nstage: ap.Stage = ap.Stage(\n    background_color=ap.Color("#333"),\n    stage_width=200,\n    stage_height=50,\n    stage_elem_id="stage",\n)\ndirection: ap.Int = ap.Int(-1)\nsvg_text: ap.SvgText = ap.SvgText(\n    text="Hello, world!",\n    x=20,\n    y=32,\n    fill_color=ap.Color("#aaa"),\n)\n\n\ndef on_enter_frame(e: ap.EnterFrameEvent, optional: dict) -> None:\n    """\n    The handler to handle a timer event.\n\n    Parameters\n    ----------\n    e : ap.EnterFrameEvent\n        Event instance.\n    optional : dict\n        Optional argument dictionary.\n    """\n    scale: ap.Number = svg_text.scale_x_from_center\n    with ap.If(scale > 1):\n        direction.value = -1\n    with ap.If(scale <= 0.3):\n        direction.value = 1\n    scale += direction * 0.005\n    svg_text.scale_x_from_center = scale\n\n\nstage.enter_frame(handler=on_enter_frame)\nap.save_overall_html(dest_dir_path="svg_txt_scale_x_from_center/")\n```': '```py\n# runnable\nimport apysc as ap\n\nstage: ap.Stage = ap.Stage(\n    background_color=ap.Color("#333"),\n    stage_width=200,\n    stage_height=50,\n    stage_elem_id="stage",\n)\ndirection: ap.Int = ap.Int(-1)\nsvg_text: ap.SvgText = ap.SvgText(\n    text="Hello, world!",\n    x=20,\n    y=32,\n    fill_color=ap.Color("#aaa"),\n)\n\n\ndef on_enter_frame(e: ap.EnterFrameEvent, optional: dict) -> None:\n    """\n    The handler to handle a timer event.\n\n    Parameters\n    ----------\n    e : ap.EnterFrameEvent\n        Event instance.\n    optional : dict\n        Optional argument dictionary.\n    """\n    scale: ap.Number = svg_text.scale_x_from_center\n    with ap.If(scale > 1):\n        direction.value = -1\n    with ap.If(scale <= 0.3):\n        direction.value = 1\n    scale += direction * 0.005\n    svg_text.scale_x_from_center = scale\n\n\nstage.enter_frame(handler=on_enter_frame)\nap.save_overall_html(dest_dir_path="svg_txt_scale_x_from_center/")\n```',  # noqa
    ##################################################
    "## set_scale_x_from_point and get_scale_x_from_point methods interface example": "## set_scale_x_from_pointとget_scale_x_from_pointメソッドのインターフェイス例",  # noqa
    ##################################################
    "The `set_scale_x_from_point` method updates the instance's scale-x from a specified point.": "`set_scale_x_from_point`メソッドは指定されたX座標を基準としてX軸の拡縮値を更新します。",  # noqa
    ##################################################
    "Similarly, the `get_scale_x_from_point` method gets the instance's scale-x from a specified point:": "同様に、`get_scale_x_from_point`メソッドでは指定されたX座標を基準としたX軸の拡縮値を取得します:",  # noqa
    ##################################################
    '```py\n# runnable\nimport apysc as ap\n\nstage: ap.Stage = ap.Stage(\n    background_color=ap.Color("#333"),\n    stage_width=200,\n    stage_height=50,\n    stage_elem_id="stage",\n)\nX: ap.Number = ap.Number(20)\ndirection: ap.Int = ap.Int(-1)\nsvg_text: ap.SvgText = ap.SvgText(\n    text="Hello, world!",\n    x=X,\n    y=32,\n    fill_color=ap.Color("#aaa"),\n)\n\n\ndef on_enter_frame(e: ap.EnterFrameEvent, optional: dict) -> None:\n    """\n    The handler to handle a timer event.\n\n    Parameters\n    ----------\n    e : ap.EnterFrameEvent\n        Event instance.\n    optional : dict\n        Optional argument dictionary.\n    """\n    scale: ap.Number = svg_text.get_scale_x_from_point(x=X)\n    with ap.If(scale > 1):\n        direction.value = -1\n    with ap.If(scale <= 0.3):\n        direction.value = 1\n    scale += direction * 0.005\n    svg_text.set_scale_x_from_point(scale_x=scale, x=X)\n\n\nstage.enter_frame(handler=on_enter_frame)\nap.save_overall_html(dest_dir_path="svg_txt_scale_x_from_point/")\n```': '```py\n# runnable\nimport apysc as ap\n\nstage: ap.Stage = ap.Stage(\n    background_color=ap.Color("#333"),\n    stage_width=200,\n    stage_height=50,\n    stage_elem_id="stage",\n)\nX: ap.Number = ap.Number(20)\ndirection: ap.Int = ap.Int(-1)\nsvg_text: ap.SvgText = ap.SvgText(\n    text="Hello, world!",\n    x=X,\n    y=32,\n    fill_color=ap.Color("#aaa"),\n)\n\n\ndef on_enter_frame(e: ap.EnterFrameEvent, optional: dict) -> None:\n    """\n    The handler to handle a timer event.\n\n    Parameters\n    ----------\n    e : ap.EnterFrameEvent\n        Event instance.\n    optional : dict\n        Optional argument dictionary.\n    """\n    scale: ap.Number = svg_text.get_scale_x_from_point(x=X)\n    with ap.If(scale > 1):\n        direction.value = -1\n    with ap.If(scale <= 0.3):\n        direction.value = 1\n    scale += direction * 0.005\n    svg_text.set_scale_x_from_point(scale_x=scale, x=X)\n\n\nstage.enter_frame(handler=on_enter_frame)\nap.save_overall_html(dest_dir_path="svg_txt_scale_x_from_point/")\n```',  # noqa
    ##################################################
    "## flip_x property interface example": "## flip_x属性のインターフェイス例",
    ##################################################
    "The `flip_x` property updates or gets the instance's flip-x (reflecting state) boolean value:": "`flip_x`属性ではインスタンスのX軸の反転状況の真偽値の更新もしくは取得を行えます:",  # noqa
    ##################################################
    '```py\n# runnable\nimport apysc as ap\n\nstage: ap.Stage = ap.Stage(\n    background_color=ap.Color("#333"),\n    stage_width=200,\n    stage_height=50,\n    stage_elem_id="stage",\n)\nsvg_text: ap.SvgText = ap.SvgText(\n    text="Hello, world!",\n    x=20,\n    y=32,\n    fill_color=ap.Color("#aaa"),\n)\n\n\ndef on_timer(e: ap.TimerEvent, options: dict) -> None:\n    """\n    The handler to handle a timer event.\n\n    Parameters\n    ----------\n    e : ap.TimerEvent\n        Event instance.\n    options : dict\n        Optional argument dictionary.\n    """\n    svg_text.flip_x = svg_text.flip_x.not_\n\n\nap.Timer(handler=on_timer, delay=1000).start()\nap.save_overall_html(dest_dir_path="svg_txt_flip_x/")\n```': '```py\n# runnable\nimport apysc as ap\n\nstage: ap.Stage = ap.Stage(\n    background_color=ap.Color("#333"),\n    stage_width=200,\n    stage_height=50,\n    stage_elem_id="stage",\n)\nsvg_text: ap.SvgText = ap.SvgText(\n    text="Hello, world!",\n    x=20,\n    y=32,\n    fill_color=ap.Color("#aaa"),\n)\n\n\ndef on_timer(e: ap.TimerEvent, options: dict) -> None:\n    """\n    The handler to handle a timer event.\n\n    Parameters\n    ----------\n    e : ap.TimerEvent\n        Event instance.\n    options : dict\n        Optional argument dictionary.\n    """\n    svg_text.flip_x = svg_text.flip_x.not_\n\n\nap.Timer(handler=on_timer, delay=1000).start()\nap.save_overall_html(dest_dir_path="svg_txt_flip_x/")\n```',  # noqa
    ##################################################
    "## flip_y property interface example": "## flip_y属性のインターフェイス例",
    ##################################################
    "The `flip_y` property updates or gets the instance's flip-y (reflecting state) boolean value:": "`flip_y`属性ではインスタンスのX軸の反転状況の真偽値の更新もしくは取得を行えます:",  # noqa
    ##################################################
    '```py\n# runnable\nimport apysc as ap\n\nstage: ap.Stage = ap.Stage(\n    background_color=ap.Color("#333"),\n    stage_width=200,\n    stage_height=50,\n    stage_elem_id="stage",\n)\nsvg_text: ap.SvgText = ap.SvgText(\n    text="Hello, world!",\n    x=20,\n    y=32,\n    fill_color=ap.Color("#aaa"),\n)\n\n\ndef on_timer(e: ap.TimerEvent, options: dict) -> None:\n    """\n    The handler to handle a timer event.\n\n    Parameters\n    ----------\n    e : ap.TimerEvent\n        Event instance.\n    options : dict\n        Optional argument dictionary.\n    """\n    svg_text.flip_y = svg_text.flip_y.not_\n\n\nap.Timer(handler=on_timer, delay=1000).start()\nap.save_overall_html(dest_dir_path="svg_txt_flip_y/")\n```': '```py\n# runnable\nimport apysc as ap\n\nstage: ap.Stage = ap.Stage(\n    background_color=ap.Color("#333"),\n    stage_width=200,\n    stage_height=50,\n    stage_elem_id="stage",\n)\nsvg_text: ap.SvgText = ap.SvgText(\n    text="Hello, world!",\n    x=20,\n    y=32,\n    fill_color=ap.Color("#aaa"),\n)\n\n\ndef on_timer(e: ap.TimerEvent, options: dict) -> None:\n    """\n    The handler to handle a timer event.\n\n    Parameters\n    ----------\n    e : ap.TimerEvent\n        Event instance.\n    options : dict\n        Optional argument dictionary.\n    """\n    svg_text.flip_y = svg_text.flip_y.not_\n\n\nap.Timer(handler=on_timer, delay=1000).start()\nap.save_overall_html(dest_dir_path="svg_txt_flip_y/")\n```',  # noqa
    ##################################################
    "## SvgText constructor API": "## SvgText クラスのコンストラクタのAPI",
    ##################################################
    '<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>': '<span class="inconspicuous-txt">特記事項: このAPIドキュメントはドキュメントビルド用のスクリプトによって自動で生成・同期されています。そのためもしかしたらこの節の内容は前節までの内容と重複している場合があります。</span>',  # noqa
    ##################################################
    "**[Interface summary]**": "**[インターフェイス概要]**",
    ##################################################
    "The class for an SVG text.<hr>": "SVGテキストのためのクラスです。<hr>",
    ##################################################
    "**[Parameters]**": "**[引数]**",
    ##################################################
    "- `text`: Union[str, String]": "- `text`: Union[str, String]",
    ##################################################
    "  - A text to use in this class.": "  - このクラスで使用するテキスト。",
    ##################################################
    "- `font_size`: Union[int, Int], optional": "- `font_size`: Union[int, Int], optional",  # noqa
    ##################################################
    "  - A font-size setting.": "  - フォントサイズ設定。",
    ##################################################
    "- `font_family`: Optional[Union[Array[String], List[str]]], optional": "- `font_family`: Optional[Union[Array[String], List[str]]], optional",  # noqa
    ##################################################
    "  - A font-family setting. Each string in an array needs to be a font name (e.g., `Times New Roman`).": "  - フォントファミリー設定。配列内の各文字列には個別のフォント名を指定する必要があります（例: `Times New Roman`）。",  # noqa
    ##################################################
    "- `x`: float or Number, optional": "- `x`: float or Number, optional",
    ##################################################
    "  - X-coordinate to start drawing.": "  - 描画を開始するX座標。",
    ##################################################
    "- `y`: float or Number, optional": "- `y`: float or Number, optional",
    ##################################################
    "  - Y-coordinate to start drawing (please see also the `Notes` section).": "  - 描画を開始するY座標（`特記事項`の節も確認をお願いします）。",  # noqa
    ##################################################
    "- `fill_color`: Color": "- `fill_color`: Color",
    ##################################################
    "  - A fill-color setting.": "  - 塗りの色の設定。",
    ##################################################
    "- `fill_alpha`: float or Number, optional": "- `fill_alpha`: float or Number, optional",  # noqa
    ##################################################
    "  - A fill-alpha setting.": "  - 塗りの透明度の設定。",
    ##################################################
    "- `line_color`: Color, optional": "- `line_color`: Color, optional",
    ##################################################
    "  - A line-color setting.": "  - 線の色の設定。",
    ##################################################
    "- `line_alpha`: float or Number, optional": "- `line_alpha`: float or Number, optional",  # noqa
    ##################################################
    "  - A line-alpha setting.": "  - 線の透明度の設定。",
    ##################################################
    "- `line_thickness`: int or Int, optional": "- `line_thickness`: int or Int, optional",  # noqa
    ##################################################
    "  - A line-thickness (line-width) setting.": "  - 線幅の設定。",
    ##################################################
    "- `leading`: float or Number, optional": "- `leading`: float or Number, optional",
    ##################################################
    "  - A text-leading size.": "  - テキストの行間のサイズ。",
    ##################################################
    "- `align`: SvgTextAlign, default SvgTextAlign.LEFT": "- `align`: SvgTextAlign, default SvgTextAlign.LEFT",  # noqa
    ##################################################
    "  - A text-align setting.": "  - テキストの行揃えの設定。",
    ##################################################
    "- `bold`: Union[bool, Boolean], optional": "- `bold`: Union[bool, Boolean], optional",  # noqa
    ##################################################
    "  - A boolean, whether this text is a bold style or not.": "  - テキストに太字のスタイル設定を行うかどうかの真偽値。",  # noqa
    ##################################################
    "- `italic`: Union[bool, Boolean], optional": "- `italic`: Union[bool, Boolean], optional",  # noqa
    ##################################################
    "  - A boolean, whether a text is an italic style or not (normal).": "  - テキストを斜体表示のスタイル設定を行うかどうかの真偽値。",  # noqa
    ##################################################
    "- `parent`: ChildMixIn or None, optional": "- `parent`: ChildMixIn or None, optional",  # noqa
    ##################################################
    "  - A parent instance to add this instance. If the specified value is None, this interface uses a stage instance.": "  - このインスタンスを追加する親のインスタンス。もしもNoneが指定された場合、このインスタンスはステージのインスタンスへと追加されます。",  # noqa
    ##################################################
    "- `variable_name_suffix`: str, optional": "- `variable_name_suffix`: str, optional",  # noqa
    ##################################################
    "  - A JavaScript variable name suffix string. This setting is sometimes useful for JavaScript debugging.": "  - JavaScript上の変数のサフィックスの設定です。この設定はJavaScriptのデバッグ時に役立つことがあります。",  # noqa
    ##################################################
    "<hr>": "<hr>",
    ##################################################
    "**[Notes]**": "**[特記事項]**",
    ##################################################
    " ・SvgText's y-coordinate zero-position starts at the bottom of a text. So if you set y=0, a text becomes almost invisible.<hr>": " ・SVGTextクラスの座標の0の位置はテキストの下部からスタートします。そのためもしもy=0を指定した場合、テキストはほとんど見えない状態になります。<hr>",  # noqa
    ##################################################
    "**[Examples]**": "**[コードサンプル]**",
    ##################################################
    '```py\n>>> import apysc as ap\n>>> stage: ap.Stage = ap.Stage(\n...     background_color=ap.Color("#333"),\n...     stage_width=200,\n...     stage_height=50,\n...     stage_elem_id="stage",\n... )\n>>> svg_text: ap.SvgText = ap.SvgText(\n...     text="Hello, world!",\n...     font_size=20,\n...     fill_color=ap.Color("#0af"),\n... )\n>>> svg_text.text\nString("Hello, world!")\n\n>>> svg_text.font_size\nInt(20)\n\n>>> svg_text.fill_color\nColor("#00aaff")\n```': '```py\n>>> import apysc as ap\n>>> stage: ap.Stage = ap.Stage(\n...     background_color=ap.Color("#333"),\n...     stage_width=200,\n...     stage_height=50,\n...     stage_elem_id="stage",\n... )\n>>> svg_text: ap.SvgText = ap.SvgText(\n...     text="Hello, world!",\n...     font_size=20,\n...     fill_color=ap.Color("#0af"),\n... )\n>>> svg_text.text\nString("Hello, world!")\n\n>>> svg_text.font_size\nInt(20)\n\n>>> svg_text.fill_color\nColor("#00aaff")\n```',  # noqa
}
