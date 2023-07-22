"""This module is for the translation mapping data of the
following document:

Document file: quick_start.md
Language: jp
"""

from typing import Dict

MAPPING: Dict[str, str] = {
    ##################################################
    "# Quick start guide": "# クイックスタートガイド",
    ##################################################
    "This page explains the first step of the apysc library journey.": "このページではapyscのライブラリの最初の一歩としての諸々について説明します。",  # noqa
    ##################################################
    "## Installing": "## インストール",
    ##################################################
    "To use apysc library Python 3.7 or the later version is required.": "apyscのライブラリを使うにはPython3.7もしくはそれ以降のPythonバージョンが必要です。",  # noqa
    ##################################################
    "You can use the pip command to install apysc.": "apyscはpipのコマンドを使ってインストールすることができます。",  # noqa
    ##################################################
    "```\n$ pip install apysc\n```": "```\n$ pip install apysc\n```",
    ##################################################
    "## Create stage and export HTML": "## Stageのインスタンスを作成し、HTMLを出力する",
    ##################################################
    "`Stage` instance is apysc's space for displaying each graphic. You can set arguments of `stage_width` for width setting, `stage_height` for height setting, and `background_color` for background.": "`Stage`のインスタンスはapyscの各グラフィックスを表示する領域となるインスタンスです。幅の設定としての`stage_width`引数、高さの設定としての`stage_height`引数、そして背景色としての`background_color`引数を設定することができます。",  # noqa
    ##################################################
    '```py\n# runnable\nimport apysc as ap\n\nstage = ap.Stage(stage_width=300, stage_height=180, background_color="#333")\n```': '```py\n# runnable\nimport apysc as ap\n\nstage = ap.Stage(stage_width=300, stage_height=180, background_color="#333")\n```',  # noqa
    ##################################################
    "Then you can export each HTML and js file by the `save_overall_html` function (in this case, that code displays only the black background stage).": "さらに、結果のHTMLとJavaScriptのファイルを`save_overall_html`関数によって保存することができます（このケースではまだ黒い背景のステージが表示されるだけです）。",  # noqa
    ##################################################
    '```py\n# runnable\nimport apysc as ap\n\nstage: ap.Stage = ap.Stage(\n    stage_width=300, stage_height=180, background_color="#333", stage_elem_id="stage"\n)\nap.save_overall_html(dest_dir_path="quick_start_stage_creation/")\n```': '```py\n# runnable\nimport apysc as ap\n\nstage: ap.Stage = ap.Stage(\n    stage_width=300, stage_height=180, background_color="#333", stage_elem_id="stage"\n)\nap.save_overall_html(dest_dir_path="quick_start_stage_creation/")\n```',  # noqa
    ##################################################
    "This code will create each HTML and js files to `dest_dir_path`. You can confirm an exported result by opening `index.html` (`quick_start_stage_creation/index.html`), as follows:": "このコードでは`dest_dir_path`引数に指定されたディレクトリに結果のHTMLとJavaScriptの各ファイルを生成します。以下のコード例では`index.html`のファイル（`quick_start_stage_creation/index.html`）を開くことで出力結果を確認することができます。",  # noqa
    ##################################################
    "## Add sprite container and vector graphics": "## Spriteのコンテナとベクターグラフィックスを追加する",
    ##################################################
    "The `Sprite` class is the container object of each display object, and it can make vector graphics with the `graphics` property.": "`Sprite`クラスは各表示オブジェクトのコンテナとなるクラスであり、`graphics`属性を使ってベクターグラフィックスを生成することもできます。",  # noqa
    ##################################################
    '```py\n# runnable\nimport apysc as ap\n\nstage: ap.Stage = ap.Stage(\n    stage_width=250, stage_height=150, background_color="#333", stage_elem_id="stage"\n)\nsprite: ap.Sprite = ap.Sprite()\n\n# Draw polyline vector graphics.\nsprite.graphics.line_style(color="#fff", thickness=3)\nsprite.graphics.move_to(x=50, y=50)\nsprite.graphics.line_to(x=100, y=50)\nsprite.graphics.line_to(x=50, y=100)\nsprite.graphics.line_to(x=100, y=100)\n\n# Draw rectangle vector graphic.\nsprite.graphics.begin_fill(color="#0af")\nsprite.graphics.draw_rect(x=150, y=50, width=50, height=50)\n\nap.save_overall_html(dest_dir_path="quick_start_sprite_graphics/")\n```': '```py\n# runnable\nimport apysc as ap\n\nstage: ap.Stage = ap.Stage(\n    stage_width=250, stage_height=150, background_color="#333", stage_elem_id="stage"\n)\nsprite: ap.Sprite = ap.Sprite()\n\n# Draw polyline vector graphics.\nsprite.graphics.line_style(color="#fff", thickness=3)\nsprite.graphics.move_to(x=50, y=50)\nsprite.graphics.line_to(x=100, y=50)\nsprite.graphics.line_to(x=50, y=100)\nsprite.graphics.line_to(x=100, y=100)\n\n# Draw rectangle vector graphic.\nsprite.graphics.begin_fill(color="#0af")\nsprite.graphics.draw_rect(x=150, y=50, width=50, height=50)\n\nap.save_overall_html(dest_dir_path="quick_start_sprite_graphics/")\n```',  # noqa
    ##################################################
    "Please see each interface documentation page for more details of `Sprite` and `Graphics`\\.": "`Sprite`や`Graphics`クラスの詳細については各インターフェイスのドキュメントをご確認ください。",  # noqa
    ##################################################
    "## See also": "## 関連資料",
    ##################################################
    "- [Sprite class](sprite.md)": "- [Sprite クラス](jp_sprite.md)",
    ##################################################
    "- [Draw interfaces abstract](draw_interfaces_abstract.md)": "- [描画の各インターフェイスの概要](jp_draw_interfaces_abstract.md)",  # noqa
}
