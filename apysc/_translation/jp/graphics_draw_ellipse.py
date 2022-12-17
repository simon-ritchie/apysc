"""This module is for the translation mapping data of the
following document:

Document file: graphics_draw_ellipse.md
Language: jp
"""

from typing import Dict

MAPPING: Dict[str, str] = {
    ##################################################
    "# Graphics draw_ellipse interface": "# Graphics クラスの draw_ellipse インターフェイス",
    ##################################################
    "This page explains the `Graphics` class `draw_ellipse` method interface.": "このページでは`Graphics`クラスの`draw_ellipse`メソッドのインターフェイスについて説明します。",  # noqa
    ##################################################
    "## What interface is this?": "## インターフェイス概要",
    ##################################################
    "The `draw_ellipse` interface draws the vector ellipse graphics.": "`draw_ellipse`インターフェイスは楕円のベクターグラフィックスを描画します。",  # noqa
    ##################################################
    "## Basic usage": "## 基本的な使い方",
    ##################################################
    "The `draw_ellipse` interface has the `x`\\, `y`\\, `width`\\, and `height` arguments. The `x` and `y` arguments are the ellipse center coordinates. The `width` and `height` arguments are the ellipse size. These sizes are twice the size of the radius.": "`draw_ellipse`インターフェイスは`x`、`y`、`width`、`height`の各インターフェイスを持っています。`x`と`y`の引数は楕円の中央座標となります。`width`と`height`は楕円の幅と高さを決定します。これらのサイズは半径の倍の値（直径）で指定する必要があります。",  # noqa
    ##################################################
    '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    background_color="#333", stage_width=325, stage_height=200, stage_elem_id="stage"\n)\n\nsprite: ap.Sprite = ap.Sprite()\n\n# Set the cyan fill color and draw the ellipse.\nsprite.graphics.begin_fill(color="#0af")\nsprite.graphics.draw_ellipse(x=125, y=100, width=150, height=100)\n\n# Set the only dotted-line style and draw the ellipse.\nsprite.graphics.begin_fill(color="")\nsprite.graphics.line_style(\n    color="#fff", thickness=3, dot_setting=ap.LineDotSetting(dot_size=3)\n)\nsprite.graphics.draw_ellipse(x=200, y=100, width=150, height=100)\n\nap.save_overall_html(dest_dir_path="graphics_draw_ellipse_basic_usage/")\n```': '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    background_color="#333", stage_width=325, stage_height=200, stage_elem_id="stage"\n)\n\nsprite: ap.Sprite = ap.Sprite()\n\n# Set the cyan fill color and draw the ellipse.\nsprite.graphics.begin_fill(color="#0af")\nsprite.graphics.draw_ellipse(x=125, y=100, width=150, height=100)\n\n# Set the only dotted-line style and draw the ellipse.\nsprite.graphics.begin_fill(color="")\nsprite.graphics.line_style(\n    color="#fff", thickness=3, dot_setting=ap.LineDotSetting(dot_size=3)\n)\nsprite.graphics.draw_ellipse(x=200, y=100, width=150, height=100)\n\nap.save_overall_html(dest_dir_path="graphics_draw_ellipse_basic_usage/")\n```',  # noqa
    ##################################################
    "## Return value": "## 返却値",
    ##################################################
    "The return value of the `draw_ellipse` interface is the instance of the `Ellipse` class.": "`draw_ellipse`インターフェイスの返却値は`Ellipse`クラスのインスタンスとなります。",  # noqa
    ##################################################
    "It has the basic interfaces (like the `x` or the `width` attributes) similar to the other graphics classes.": "このクラスのインスタンスは他のグラフィックス系のクラスと同様に`x`や`y`、`width`などの基本的なインターフェイスを持っています。",  # noqa
    ##################################################
    "The following code example binds the click event handler. If you click the ellipse, the width and height become wider.": "以下のコード例ではクリックのイベントハンドラを設定しており、楕円をクリックするたびに幅と高さが大きくなるようにしています。",  # noqa
    ##################################################
    '```py\n# runnable\nimport apysc as ap\n\n\ndef on_ellipse_click(e: ap.MouseEvent[ap.Ellipse], options: dict) -> None:\n    """\n    The handler that the ellipse calls when clicked.\n\n    Parameters\n    ----------\n    e : MouseEvent\n        Event instance.\n    options : dict\n        Optional arguments dictionary.\n    """\n    ellipse: ap.Ellipse = e.this\n    ellipse.width += 15\n    ellipse.height += 10\n\n\nap.Stage(\n    background_color="#333", stage_width=250, stage_height=200, stage_elem_id="stage"\n)\n\nsprite: ap.Sprite = ap.Sprite()\n\nsprite.graphics.begin_fill(color="#0af")\nellipse: ap.Ellipse = sprite.graphics.draw_ellipse(x=125, y=100, width=150, height=100)\nellipse.click(on_ellipse_click)\n\nap.save_overall_html(dest_dir_path="graphics_draw_ellipse_return_value/")\n```': '```py\n# runnable\nimport apysc as ap\n\n\ndef on_ellipse_click(e: ap.MouseEvent[ap.Ellipse], options: dict) -> None:\n    """\n    The handler that the ellipse calls when clicked.\n\n    Parameters\n    ----------\n    e : MouseEvent\n        Event instance.\n    options : dict\n        Optional arguments dictionary.\n    """\n    ellipse: ap.Ellipse = e.this\n    ellipse.width += 15\n    ellipse.height += 10\n\n\nap.Stage(\n    background_color="#333", stage_width=250, stage_height=200, stage_elem_id="stage"\n)\n\nsprite: ap.Sprite = ap.Sprite()\n\nsprite.graphics.begin_fill(color="#0af")\nellipse: ap.Ellipse = sprite.graphics.draw_ellipse(x=125, y=100, width=150, height=100)\nellipse.click(on_ellipse_click)\n\nap.save_overall_html(dest_dir_path="graphics_draw_ellipse_return_value/")\n```',  # noqa
    ##################################################
    "## draw_ellipse API": "## draw_ellipse API",
    ##################################################
    '<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>': '<span class="inconspicuous-txt">特記事項: このAPIドキュメントはドキュメントビルド用のスクリプトによって自動で生成・同期されています。そのためもしかしたらこの節の内容は前節までの内容と重複している場合があります。</span>',  # noqa
    ##################################################
    "**[Interface summary]**": "**[インターフェイス概要]**",
    ##################################################
    "Draw an ellipse vector graphic.<hr>": "楕円のベクターグラフィックスを描画します。<hr>",
    ##################################################
    "**[Parameters]**": "**[引数]**",
    ##################################################
    "- `x`: Int or int": "- `x`: Int or int",
    ##################################################
    "  - X-coordinate of the ellipse center.": "  - 楕円の中央のX座標。",
    ##################################################
    "- `y`: Int or int": "- `y`: Int or int",
    ##################################################
    "  - Y-coordinate of the ellipse center.": "  - 楕円の中央のY座標。",
    ##################################################
    "- `width`: Int or int": "- `width`: Int or int",
    ##################################################
    "  - Ellipse width.": "  - 楕円の幅。",
    ##################################################
    "- `height`: Int or int": "- `height`: Int or int",
    ##################################################
    "  - Ellipse height.": "  - 楕円の高さ。",
    ##################################################
    "- `variable_name_suffix`: str, default ''": "- `variable_name_suffix`: str, default ''",  # noqa
    ##################################################
    "  - A JavaScript variable name suffix string. This setting is sometimes useful for JavaScript's debugging.": "  - JavaScript上の変数のサフィックスの設定です。この設定はJavaScriptのデバッグ時に役立つことがあります。",  # noqa
    ##################################################
    "<hr>": "<hr>",
    ##################################################
    "**[Returns]**": "**[返却値]**",
    ##################################################
    "- `ellipse`: Ellipse": "- `ellipse`: Ellipse",
    ##################################################
    "  - Created ellipse graphics instance.": "  - 作成された楕円のグラフィックスのインスタンス。",
    ##################################################
    "<hr>": "<hr>",
    ##################################################
    "**[Examples]**": "**[コードサンプル]**",
    ##################################################
    "```py\n>>> import apysc as ap\n>>> stage: ap.Stage = ap.Stage()\n>>> sprite: ap.Sprite = ap.Sprite()\n>>> sprite.graphics.begin_fill(color=\"#0af\")\n>>> ellipse: ap.Ellipse = sprite.graphics.draw_ellipse(\n...     x=100, y=100, width=100, height=50\n... )\n>>> ellipse.x\nInt(100)\n\n>>> ellipse.y\nInt(100)\n\n>>> ellipse.width\nInt(100)\n\n>>> ellipse.height\nInt(50)\n\n>>> ellipse.fill_color\nString('#00aaff')\n```": "```py\n>>> import apysc as ap\n>>> stage: ap.Stage = ap.Stage()\n>>> sprite: ap.Sprite = ap.Sprite()\n>>> sprite.graphics.begin_fill(color=\"#0af\")\n>>> ellipse: ap.Ellipse = sprite.graphics.draw_ellipse(\n...     x=100, y=100, width=100, height=50\n... )\n>>> ellipse.x\nInt(100)\n\n>>> ellipse.y\nInt(100)\n\n>>> ellipse.width\nInt(100)\n\n>>> ellipse.height\nInt(50)\n\n>>> ellipse.fill_color\nString('#00aaff')\n```",  # noqa
}
