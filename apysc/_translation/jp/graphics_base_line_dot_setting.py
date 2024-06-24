"""This module is for the translation mapping data of the
following document:

Document file: graphics_base_line_dot_setting.md
Language: jp
"""

from typing import Dict

MAPPING: Dict[str, str] = {
    ##################################################
    "# GraphicsBase line_dot_setting interface": "# GraphicsBase クラスの line_dot_setting インターフェイス",  # noqa
    ##################################################
    "This page explains the `GraphicsBase` class `line_dot_setting` property interface.": "このページでは`GraphicsBase`クラスの`line_dot_setting`属性のインターフェイスについて説明します。",  # noqa
    ##################################################
    "## What interface is this?": "## インターフェイス概要",
    ##################################################
    "The `line_dot_setting` property interface updates or gets the instance's current line dot setting.": "`line_dot_setting`属性のインターフェイスはインスタンスの線のドット設定の更新もしくは取得を行います。",  # noqa
    ##################################################
    "## Basic usage": "## 基本的な使い方",
    ##################################################
    "The getter or setter interface value becomes (or requires) the `LineDotSetting` instance value.": "getterやsetterのインターフェイスの値は`LineDotSetting`クラスのインスタンスの値となります。",  # noqa
    ##################################################
    "The following example sets the 5-pixel dot to the line:": "以下のコード例では5pxの点線の設定を線に行っています:",  # noqa
    ##################################################
    '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    stage_width=250,\n    stage_height=100,\n    background_color=ap.Color("#333"),\n    stage_elem_id="stage",\n)\nsprite: ap.Sprite = ap.Sprite()\nsprite.graphics.line_style(color=ap.Color("#0af"), thickness=5)\n\nline: ap.Line = sprite.graphics.draw_line(x_start=50, y_start=50, x_end=200, y_end=50)\nline.line_dot_setting = ap.LineDotSetting(dot_size=5)\n\nap.save_overall_html(dest_dir_path="./graphics_base_line_dot_setting_basic_usage/")\n```': '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    stage_width=250,\n    stage_height=100,\n    background_color=ap.Color("#333"),\n    stage_elem_id="stage",\n)\nsprite: ap.Sprite = ap.Sprite()\nsprite.graphics.line_style(color=ap.Color("#0af"), thickness=5)\n\nline: ap.Line = sprite.graphics.draw_line(x_start=50, y_start=50, x_end=200, y_end=50)\nline.line_dot_setting = ap.LineDotSetting(dot_size=5)\n\nap.save_overall_html(dest_dir_path="./graphics_base_line_dot_setting_basic_usage/")\n```',  # noqa
    ##################################################
    "## Delete setting": "## 設定の削除",
    ##################################################
    "The `delete_line_dot_setting` interface deletes this line setting.": "`delete_line_dot_setting`インターフェイスはこの線の設定を削除します。",  # noqa
    ##################################################
    "In the following example, if you click the rectangle, the handler deletes the line setting:": "以下の例では四角をクリックするとハンドラ内の処理で線の設定を削除しています:",  # noqa
    ##################################################
    '```py\n# runnable\nimport apysc as ap\n\n\ndef on_click(e: ap.MouseEvent[ap.Rectangle], options: dict) -> None:\n    """\n    The handler for the click event.\n\n    Parameters\n    ----------\n    e : ap.MouseEvent[ap.Rectangle]\n        Event instance.\n    options : dict\n        Optional argument dictionary.\n    """\n    rectangle: ap.Rectangle = e.this\n    rectangle.delete_line_dot_setting()\n\n\nap.Stage(\n    stage_width=150,\n    stage_height=150,\n    background_color=ap.Color("#333"),\n    stage_elem_id="stage",\n)\nrectangle: ap.Rectangle = ap.Rectangle(\n    x=50,\n    y=50,\n    width=50,\n    height=50,\n    fill_color=ap.Color("#666"),\n    line_color=ap.Color("#fff"),\n    line_thickness=3,\n    line_dot_setting=ap.LineDotSetting(dot_size=3),\n)\nrectangle.click(handler=on_click)\nap.save_overall_html(dest_dir_path="./graphics_base_line_dot_setting_delete_setting/")\n```': '```py\n# runnable\nimport apysc as ap\n\n\ndef on_click(e: ap.MouseEvent[ap.Rectangle], options: dict) -> None:\n    """\n    The handler for the click event.\n\n    Parameters\n    ----------\n    e : ap.MouseEvent[ap.Rectangle]\n        Event instance.\n    options : dict\n        Optional argument dictionary.\n    """\n    rectangle: ap.Rectangle = e.this\n    rectangle.delete_line_dot_setting()\n\n\nap.Stage(\n    stage_width=150,\n    stage_height=150,\n    background_color=ap.Color("#333"),\n    stage_elem_id="stage",\n)\nrectangle: ap.Rectangle = ap.Rectangle(\n    x=50,\n    y=50,\n    width=50,\n    height=50,\n    fill_color=ap.Color("#666"),\n    line_color=ap.Color("#fff"),\n    line_thickness=3,\n    line_dot_setting=ap.LineDotSetting(dot_size=3),\n)\nrectangle.click(handler=on_click)\nap.save_overall_html(dest_dir_path="./graphics_base_line_dot_setting_delete_setting/")\n```',  # noqa
    ##################################################
    "## See also": "## 関連資料",
    ##################################################
    "- [Graphics class line_style interface](graphics_line_style.md)": "- [Graphics クラスの line_style (線のスタイル設定)のインターフェイス](jp_graphics_line_style.md)",  # noqa
    ##################################################
    "## line_dot_setting property API": "## line_dot_setting 属性のAPI",
    ##################################################
    '<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>': '<span class="inconspicuous-txt">特記事項: このAPIドキュメントはドキュメントビルド用のスクリプトによって自動で生成・同期されています。そのためもしかしたらこの節の内容は前節までの内容と重複している場合があります。</span>',  # noqa
    ##################################################
    "**[Interface summary]**": "**[インターフェイス概要]**",
    ##################################################
    "Get this instance's line dot setting.<hr>": "このインスタンスの線の点線のスタイル設定を取得します。<hr>",
    ##################################################
    "**[Returns]**": "**[返却値]**",
    ##################################################
    "- `line_dot_setting`: LineDotSetting or None": "- `line_dot_setting`: LineDotSetting or None",  # noqa
    ##################################################
    "  - Lien dot setting.": "  - 線の点線のスタイル設定。",
    ##################################################
    "<hr>": "<hr>",
    ##################################################
    "**[Examples]**": "**[コードサンプル]**",
    ##################################################
    '```py\n>>> import apysc as ap\n>>> stage: ap.Stage = ap.Stage()\n>>> sprite: ap.Sprite = ap.Sprite()\n>>> sprite.graphics.line_style(color=ap.Color("#fff"), thickness=10)\n>>> line: ap.Line = sprite.graphics.draw_line(\n...     x_start=50, y_start=50, x_end=150, y_end=50\n... )\n>>> line.line_dot_setting = ap.LineDotSetting(dot_size=5)\n>>> line.line_dot_setting.dot_size\nInt(5)\n```': '```py\n>>> import apysc as ap\n>>> stage: ap.Stage = ap.Stage()\n>>> sprite: ap.Sprite = ap.Sprite()\n>>> sprite.graphics.line_style(color=ap.Color("#fff"), thickness=10)\n>>> line: ap.Line = sprite.graphics.draw_line(\n...     x_start=50, y_start=50, x_end=150, y_end=50\n... )\n>>> line.line_dot_setting = ap.LineDotSetting(dot_size=5)\n>>> line.line_dot_setting.dot_size\nInt(5)\n```',  # noqa
    ##################################################
    "## delete_line_dot_setting API": "## delete_line_dot_setting のAPI",
    ##################################################
    '<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>': '<span class="inconspicuous-txt">特記事項: このAPIドキュメントはドキュメントビルド用のスクリプトによって自動で生成・同期されています。そのためもしかしたらこの節の内容は前節までの内容と重複している場合があります。</span>',  # noqa
    ##################################################
    "**[Interface summary]**": "**[インターフェイス概要]**",
    ##################################################
    "Delete a current line dot setting.": "現在の点線の設定を削除します。",
}
