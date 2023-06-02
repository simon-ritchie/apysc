"""This module is for the translation mapping data of the
following document:

Document file: display_on_colaboratory.md
Language: jp
"""

from typing import Dict

MAPPING: Dict[str, str] = {
    ##################################################
    "# display_on_colaboratory interface": "# display_on_colaboratory インターフェイス",
    ##################################################
    "This page will explain the `display_on_colaboratory` function interface.": "このページでは`display_on_colaboratory`関数のインターフェイスについて説明します。",  # noqa
    ##################################################
    "## What interface is this?": "## インターフェイス概要",
    ##################################################
    "The `display_on_colaboratory` interface displays the apysc HTML on the Google Colaboratory.": "`display_on_colaboratory`インターフェイスはapyscのHTMLをGoogle Colaboratory上で表示します。",  # noqa
    ##################################################
    "## Requirements": "## 必要とされるインストールなどの対応",
    ##################################################
    "You need to install apysc on the Google Colaboratory before going on. The `!` symbol and pip command on the Google Colaboratory installs this library:": "利用するには事前にGoogle Colaboratory上でapyscをインストールする必要があります。`!`の記号とpip五万度でGoogle Colaboratory上にこのライブラリをインストールすることができます。",  # noqa
    ##################################################
    "```\n!pip install apysc\n```": "```\n!pip install apysc\n```",
    ##################################################
    "## Basic usage": "## 基本的な使い方",
    ##################################################
    "You can use the `display_on_colaboratory` interface to display an output HTML instead of the `save_overall_html` function.": "`save_overall_html`関数の代わりに`display_on_colaboratory`関数のインターフェイスを使うことで出力結果のHTMLを表示することができます。",  # noqa
    ##################################################
    "This interface requires the `html_file_name` argument to be unique if you need to output multiple HTML. Otherwise, it overwrites the HTML file:": "このインターフェイスは複数の出力出力ファイルをユニークにするための`html_file_name`引数によるファイル名の指定が必要になります。ユニークに設定しないとHTMLファイルが上書きされてしまいます。",  # noqa
    ##################################################
    '```py\nimport apysc as ap\n\nap.Stage(stage_width=250, stage_height=150, background_color="#333")\nsprite = ap.Sprite()\nsprite.graphics.begin_fill(color="#0af")\nsprite.graphics.draw_rect(x=50, y=50, width=50, height=50)\n\nsprite.graphics.begin_fill(color="#f0a")\nsprite.graphics.draw_rect(x=150, y=50, width=50, height=50)\n\nap.display_on_colaboratory(html_file_name="jupyter_test_1.html")\n```': '```py\nimport apysc as ap\n\nap.Stage(stage_width=250, stage_height=150, background_color="#333")\nsprite = ap.Sprite()\nsprite.graphics.begin_fill(color="#0af")\nsprite.graphics.draw_rect(x=50, y=50, width=50, height=50)\n\nsprite.graphics.begin_fill(color="#f0a")\nsprite.graphics.draw_rect(x=150, y=50, width=50, height=50)\n\nap.display_on_colaboratory(html_file_name="jupyter_test_1.html")\n```',  # noqa
    ##################################################
    "![](_static/colaboratory_interface.png)": "![](_static/colaboratory_interface.png)",  # noqa
    ##################################################
    "## display_on_colaboratory API": "## display_on_colaboratory API",
    ##################################################
    '<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>': '<span class="inconspicuous-txt">特記事項: このAPIドキュメントはドキュメントビルド用のスクリプトによって自動で生成・同期されています。そのためもしかしたらこの節の内容は前節までの内容と重複している場合があります。</span>',  # noqa
    ##################################################
    "**[Interface summary]**": "**[インターフェイス概要]**",
    ##################################################
    "Save the overall HTML and display it on Google Colaboratory.<hr>": "HTML全体を保存し結果をGoogle Colaboratory上で表示します。<hr>",  # noqa
    ##################################################
    "**[Parameters]**": "**[引数]**",
    ##################################################
    "- `html_file_name`: str, default 'index.html'": "- `html_file_name`: str, default 'index.html'",  # noqa
    ##################################################
    "  - The output HTML file name.": "  - 出力されるHTMLのファイル名。",
    ##################################################
    "- `minify`: bool, default True": "- `minify`: bool, default True",
    ##################################################
    "  - Boolean value whether minify a HTML or not. False setting is useful when debugging.": "  - HTMLを最小化（minify）するかどうかの真偽値。Falseの設定はデバッグ時などに役に立つことがあります。",  # noqa
}
