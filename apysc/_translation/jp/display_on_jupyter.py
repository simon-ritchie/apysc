"""This module is for the translation mapping data of the
following document:

Document file: display_on_jupyter.md
Language: jp
"""

from typing import Dict

MAPPING: Dict[str, str] = {
    ##################################################
    "# display_on_jupyter interface": "# display_on_jupyter インターフェイス",
    ##################################################
    "This page explains the `display_on_jupyter` function interface.": "このページでは`display_on_jupyter`関数のインターフェイスについて説明します。",  # noqa
    ##################################################
    "## What interface is this?": "## インターフェイス概要",
    ##################################################
    "The `display_on_jupyter` interface displays the apysc HTML on the Jupyter.": "`display_on_jupyter`関数はapyscによって生成されたHTMLをJupyter上で表示します。",  # noqa
    ##################################################
    "## Requirements": "## 必要とされるインストールなどの対応",
    ##################################################
    "This interface requires the Jupyter library. Therefore, if you haven't installed Jupyter, you need to install it before going on (e.g., `pip install notebook`).": "このインターフェイスはJupyterのライブラリの事前のインストールが必要です。もしインストールされていなければ`pip install notebook`などのコマンドでインストールしておく必要があります。",  # noqa
    ##################################################
    "For more information, please see:": "詳細は以下をご確認ください:",
    ##################################################
    "- [Installing the Jupyter Software](https://jupyter.org/install)": "- [Installing the Jupyter Software](https://jupyter.org/install)",  # noqa
    ##################################################
    "Also, this interface uses the `IPython.display.IFrame` interface. If you encountered that interface error, please update the Jupyter version.": "また、このインターフェイスは`IPython.display.IFrame`のインターフェイスを使用しています。もしも該当のインターフェイス関係でエラーが発生した場合Jupyterのアップデートをお試しください。",  # noqa
    ##################################################
    "## Notes": "## 特記事項",
    ##################################################
    "- Jupyter on the VS Code is not supported currently (since the VS code restriction).": "- VS Code上のJupyterは現在サポートされていません（VS Code上の制限に起因するため将来サポートするかどうかは未定です）。",  # noqa
    ##################################################
    "- Jupyter notebook and JupyterLab are supported.": "- Jupyter notebook 及び JupyterLabはサポートしています。",  # noqa
    ##################################################
    "## Basic usage": "## 基本的な使い方",
    ##################################################
    "You can use the `display_on_jupyter` interface to display an output HTML instead of the `save_overall_html` function.": "出力結果のHTMLをJupyter上で表示するために`save_overall_html`関数の代わりに`display_on_jupyter`を使用することができます。",  # noqa
    ##################################################
    "This interface requires the `html_file_name` argument to be unique if you need to output multiple HTML. Otherwise, this interface overwrites the HTML file:": "このインターフェイスは複数のHTMLファイルを保存する際にファイル名が被らないようにするために`html_file_name`引数にユニークなファイル名の指定が必要です。この値にユニークな値を指定しない場合HTMLが上書きされてしまいます。",  # noqa
    ##################################################
    '```py\nimport apysc as ap\n\nap.Stage(\n    stage_width=250,\n    stage_height=150,\n    background_color=ap.Color("#333"),\n)\nsprite = ap.Sprite()\nsprite.graphics.begin_fill(color=ap.Color("#0af"))\nsprite.graphics.draw_rect(x=50, y=50, width=50, height=50)\n\nsprite.graphics.begin_fill(color=ap.Color("#f0a"))\nsprite.graphics.draw_rect(x=150, y=50, width=50, height=50)\n\nap.display_on_jupyter(html_file_name="jupyter_sample_1.html")\n```': '```py\nimport apysc as ap\n\nap.Stage(\n    stage_width=250,\n    stage_height=150,\n    background_color=ap.Color("#333"),\n)\nsprite = ap.Sprite()\nsprite.graphics.begin_fill(color=ap.Color("#0af"))\nsprite.graphics.draw_rect(x=50, y=50, width=50, height=50)\n\nsprite.graphics.begin_fill(color=ap.Color("#f0a"))\nsprite.graphics.draw_rect(x=150, y=50, width=50, height=50)\n\nap.display_on_jupyter(html_file_name="jupyter_sample_1.html")\n```',  # noqa
    ##################################################
    "![](_static/jupyter_notebook_interface.png)": "![](_static/jupyter_notebook_interface.png)",  # noqa
    ##################################################
    "Also, this interface can use on the JupyterLab:": "このインターフェイスはJupyterLabもサポートしています:",  # noqa
    ##################################################
    "![](_static/jupyterlab_interface.png)": "![](_static/jupyterlab_interface.png)",
    ##################################################
    "## display_on_jupyter API": "## display_on_jupyter API",
    ##################################################
    '<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>': '<span class="inconspicuous-txt">特記事項: このAPIドキュメントはドキュメントビルド用のスクリプトによって自動で生成・同期されています。そのためもしかしたらこの節の内容は前節までの内容と重複している場合があります。</span>',  # noqa
    ##################################################
    "**[Interface summary]**": "**[インターフェイス概要]**",
    ##################################################
    "Save the overall HTML and display it on the Jupyter.<hr>": "HTML全体を保存し結果をJupyter上で表示します。<hr>",  # noqa
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
    ##################################################
    "<hr>": "<hr>",
    ##################################################
    "**[Notes]**": "**[特記事項]**",
    ##################################################
    "Currently, this interface does not support Jupyter on the VS Code. This interface requires the Jupyter library (e.g., `notebook` package).": "現在このインターフェイスはVS Code上のJupyterをサポートしていません。また、このインターフェイスは事前のJupyterのライブラリのインストールが必要です（例 : `notebook`パッケージなど）。",  # noqa
}
