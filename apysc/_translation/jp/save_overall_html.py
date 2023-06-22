"""This module is for the translation mapping data of the
following document:

Document file: save_overall_html.md
Language: jp
"""

from typing import Dict

MAPPING: Dict[str, str] = {
    ##################################################
    "# save_overall_html interface": "# save_overall_html インターフェイス",
    ##################################################
    "This page explains the `save_overall_html` function interface.": "このページでは`save_overall_html`関数のインターフェイスについて説明します。",  # noqa
    ##################################################
    "## What interface is this?": "## インターフェイス概要",
    ##################################################
    "The `save_overall_html` function interface will export the overall HTML and JavaScript files. At the end of the apysc project, this function's calling is necessary to export the HTML.": "`save_overall_html`関数のインターフェイスはHTMLとJavaScript全体のファイルを出力します。apyscのプロジェクトの最後でHTMLなどを出力するためにこの関数の呼び出しが必要になります。",  # noqa
    ##################################################
    "## Basic usage": "## 基本的な使い方",
    ##################################################
    "The `save_overall_html` function need at least one argument, `dest_dir_path`. This argument determines a directory path to save HTML and JavaScript files.": "`save_overall_html`関数では最低限`dest_dir_path`引数の指定が必要になります。この引数はHTMLとJavaScriptの各ファイルの出力先のディレクトリとなります。",  # noqa
    ##################################################
    "The following code example exports the HTML and JavaScript files, and the exported HTML displays the blank stage (150 px width and height).": "以下のコード例ではHTMLとJavaScriptの各ファイル出力しています。出力したHTMLでは縦横150pxの空のステージのみ表示されるようにしてあります。",  # noqa
    ##################################################
    '```py\n# runnable\nimport apysc as ap\n\nstage: ap.Stage = ap.Stage(\n    background_color="#333", stage_width=150, stage_height=150, stage_elem_id="stage"\n)\n\nap.save_overall_html(dest_dir_path="save_overall_html_interface_basic_usage/")\n```': '```py\n# runnable\nimport apysc as ap\n\nstage: ap.Stage = ap.Stage(\n    background_color="#333", stage_width=150, stage_height=150, stage_elem_id="stage"\n)\n\nap.save_overall_html(dest_dir_path="save_overall_html_interface_basic_usage/")\n```',  # noqa
    ##################################################
    "The preceding code exports the `save_overall_html_interface_basic_usage/index.html` and the other JavaScript library files.": "上記のコードでは`save_overall_html_interface_basic_usage/index.html`のパスにHTMLファイルや他のJavaScriptのライブラリファイルが出力されます。",  # noqa
    ##################################################
    "## Minify the HTML": "## HTMLを最小化する",
    ##################################################
    "The `save_overall_html` function has the `minify` optional argument (default is True). This interface minifies an output HTML if this value is `True`\\. The `False` setting is sometimes helpful for debugging.": "`save_overall_html`関数には`minify`のオプションの引数が存在します（デフォルトではTrueになっています）。この設定はもしTrueになっていきれば出力結果のHTMLを最小化（minify）します。Falseの設定はデバッグ時などに便利な時があります。",  # noqa
    ##################################################
    '```py\nimport apysc as ap\n\nstage: ap.Stage = ap.Stage(\n    background_color="#333", stage_width=150, stage_height=150, stage_elem_id="stage"\n)\n\nap.save_overall_html(dest_dir_path="dest_dir/", minify=False)\n```': '```py\nimport apysc as ap\n\nstage: ap.Stage = ap.Stage(\n    background_color="#333", stage_width=150, stage_height=150, stage_elem_id="stage"\n)\n\nap.save_overall_html(dest_dir_path="dest_dir/", minify=False)\n```',  # noqa
    ##################################################
    "## JavaScript libs directory path setting and skip option": "## JavaScriptのライブラリのディレクトリパスの設定と出力スキップの設定",  # noqa
    ##################################################
    "If you want to adjust the JavaScript library paths, set the `js_lib_dir_path` optional argument. This option overrides the JavaScript library paths in an exported HTML (`index.html`).": "もしもJavaScriptのライブラリパスを調整したい場合、`js_lib_dir_path`のオプションとなる引数で設定することができます。このオプションは出力されたHTML（`index.html`）内のJavaScriptのライブラリのパス指定を上書きします。",  # noqa
    ##################################################
    "This setting is sometimes helpful when you want to export the HTML with specified JavaScript library paths, for instance, the Django library static directory.": "この設定は例えばDjangoのようなライブラリの静的ファイルのディレクトリを指定する形でJavaScriptライブラリのパスを指定してHTMLを出力したい場合などに役立つ時があります。",  # noqa
    ##################################################
    "Also, the `skip_js_lib_exporting` option is helpful when you want to skip the already exported js files. This setting skips the JavaScript library exporting.": "また、`skip_js_lib_exporting`の引数のオプションも既に出力済みのJavaScriptライブラリの出力を省略したい場合に役立ちます。この設定を有効にするとJavaScriptライブラリのファイルは出力されなくなります。",  # noqa
    ##################################################
    '```py\nimport apysc as ap\n\nstage: ap.Stage = ap.Stage(\n    background_color="#333", stage_width=150, stage_height=150, stage_elem_id="stage"\n)\n\nap.save_overall_html(\n    dest_dir_path="dest_dir/", js_lib_dir_path="static/js/", skip_js_lib_exporting=True\n)\n```': '```py\nimport apysc as ap\n\nstage: ap.Stage = ap.Stage(\n    background_color="#333", stage_width=150, stage_height=150, stage_elem_id="stage"\n)\n\nap.save_overall_html(\n    dest_dir_path="dest_dir/", js_lib_dir_path="static/js/", skip_js_lib_exporting=True\n)\n```',  # noqa
    ##################################################
    "Notes: The `js_lib_dir_path` option does not change the js files exporting destination directory currently.": "特記事項: 現在の実装では`js_lib_dir_path`の設定ではJavaScriptファイルの出力先は変更されません。",  # noqa
    ##################################################
    "## Change the HTML file name by the html_file_name option": "## html_file_name オプションを使用してHTMLのファイル名を変更する",  # noqa
    ##################################################
    "If you need to change the output HTML file name, use the `html_file_name` optional argument. This argument changes the HTML file name from `index.html` to any other name.": "出力されるHTMLのファイル名を変更したい場合には`html_file_name`のオプションの引数を指定することで変更することができます。この引数はHTMLのファイル名を`index.html`から任意の他の名前に変更します。",  # noqa
    ##################################################
    '```py\nimport apysc as ap\n\nstage: ap.Stage = ap.Stage(\n    background_color="#333", stage_width=150, stage_height=150, stage_elem_id="stage"\n)\n\nap.save_overall_html(dest_dir_path="dest_dir/", html_file_name="chart.html")\n```': '```py\nimport apysc as ap\n\nstage: ap.Stage = ap.Stage(\n    background_color="#333", stage_width=150, stage_height=150, stage_elem_id="stage"\n)\n\nap.save_overall_html(dest_dir_path="dest_dir/", html_file_name="chart.html")\n```',  # noqa
    ##################################################
    "## Bundle each JavaScript library to the signle HTML file by the embed_js_libs option": "## embed_js_libs オプションでJavaScriptのライブラリを1つのHTMLファイルにまとめる",  # noqa
    ##################################################
    "You can bundle each JavaScript library to the single output HTML file by the `embed_js_libs` optional argument. This option is maybe useful when you need to pass the output file to the other members.": "`embed_js_libs`のオプションの引数を設定することで、出力結果のHTML内に各JavaScriptライブラリの内容を含めてまとめることができます。この設定は他のメンバーにファイルを共有する場合などに1つのファイルのみで扱うことができ便利な時があります。",  # noqa
    ##################################################
    '```py\nimport apysc as ap\n\nstage: ap.Stage = ap.Stage(\n    background_color="#333", stage_width=150, stage_height=150, stage_elem_id="stage"\n)\n\nap.save_overall_html(dest_dir_path="dest_dir/", embed_js_libs=True)\n```': '```py\nimport apysc as ap\n\nstage: ap.Stage = ap.Stage(\n    background_color="#333", stage_width=150, stage_height=150, stage_elem_id="stage"\n)\n\nap.save_overall_html(dest_dir_path="dest_dir/", embed_js_libs=True)\n```',  # noqa
    ##################################################
    "## Change the stdout setting by the verbose option": "## verbose オプションで標準出力の設定を変更する",  # noqa
    ##################################################
    "The `verbose` optional argument changes the exporting stdout behavior. If the specified value is 0, the apysc displays nothing. If 1 or the other values is specified, the apysc displays the stdout.": "`verbose`のオプションの引数はファイル出力時の標準出力の挙動を変更します。もしも0が指定された場合標準出力に何も表示しなくなります。1もしくは他の値を指定すればapyscライブラリは標準出力を表示します。",  # noqa
    ##################################################
    '```py\nimport apysc as ap\n\nstage: ap.Stage = ap.Stage(\n    background_color="#333", stage_width=150, stage_height=150, stage_elem_id="stage"\n)\n\nap.save_overall_html(dest_dir_path="dest_dir/", verbose=0)\n```': '```py\nimport apysc as ap\n\nstage: ap.Stage = ap.Stage(\n    background_color="#333", stage_width=150, stage_height=150, stage_elem_id="stage"\n)\n\nap.save_overall_html(dest_dir_path="dest_dir/", verbose=0)\n```',  # noqa
    ##################################################
    "## save_overall_html API": "## save_overall_html API",
    ##################################################
    '<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>': '<span class="inconspicuous-txt">特記事項: このAPIドキュメントはドキュメントビルド用のスクリプトによって自動で生成・同期されています。そのためもしかしたらこの節の内容は前節までの内容と重複している場合があります。</span>',  # noqa
    ##################################################
    "**[Interface summary]**": "**[インターフェイス概要]**",
    ##################################################
    "Save the overall HTML and js files under the specified directory path.<hr>": "指定されたディレクトリパス以下にHTMLとJavaScriptのファイル全体を出力します。<hr>",  # noqa
    ##################################################
    "**[Parameters]**": "**[引数]**",
    ##################################################
    "- `dest_dir_path`: str": "- `dest_dir_path`: str",
    ##################################################
    "  - Destination directory path to save each HTML and js file.": "  - 各HTMLとJavaScriptファイルの保存先となるディレクトリパス。",  # noqa
    ##################################################
    "- `html_file_name`: str, default 'index.html'": "- `html_file_name`: str, default 'index.html'",  # noqa
    ##################################################
    "  - The output HTML file name.": "  - 出力されるHTMLのファイル名。",
    ##################################################
    "- `minify`: bool, default True": "- `minify`: bool, default True",
    ##################################################
    "  - Boolean value indicates whether minify HTML and js or not. The False setting is helpful when debugging.": "  - HTMLとJavaScriptの内容を最小化（minify）するかどうかの真偽値。Falseの設定はデバッグ時などに便利な時があります。",  # noqa
    ##################################################
    "- `js_lib_dir_path`: str, default './'": "- `js_lib_dir_path`: str, default './'",  # noqa
    ##################################################
    "  - JavaScript libraries directory path. This setting applies to a JavaScript source path in HTML. If not specified, then set the same directory with HTML. This setting is maybe helpful to set js lib directory, such as Django's static (static_collected) directory. This interface recommends setting True value to the `skip_js_lib_exporting` argument if this argument sets.": "  - JavaScriptライブラリのパスの設定。この設定はHTML内のJavaScriptのコードのパスの指定部分に影響します。指定されていない場合にはHTMLと同じディレクトリが設定されます。この設定はDjangoのようなライブラリの静的ファイルのディレクトリを指定する場合などに便利なことがあります。もしこの引数が設定された場合には`skip_js_lib_exporting`の設定も有効にすることが推奨されます。",  # noqa
    ##################################################
    "- `skip_js_lib_exporting`: bool, default False": "- `skip_js_lib_exporting`: bool, default False",  # noqa
    ##################################################
    "  - If True, this interface does not export JavaScript libraries.": "  - Trueが設定された場合、このインターフェイスはJavaScriptの各ライブラリを出力しなくなります。",  # noqa
    ##################################################
    "- `embed_js_libs`: bool, default False": "- `embed_js_libs`: bool, default False",
    ##################################################
    "  - Option to embed the JavaScript libraries script to the output HTML or not. If True, the output HTML becomes enormous, and be only one HTML file. Occasionally, this option is useful when sharing the exported file or using the output file with an iframe tag to avoid the CORS error.": "  - 各JavaScriptライブラリを出力されるHTML内に埋め込むかどうかの設定です。もしTrueが設定された場合、出力されるHTMLは大きくなり、そして1つのHTMLファイルのみ出力されるようになります。この設定は出力されたファイルをiframeタグで使う際にCORSのエラーを回避したい時などに役立つことがあります。",  # noqa
    ##################################################
    "- `verbose`: int, default 1": "- `verbose`: int, default 1",
    ##################################################
    "  - The Logging setting. If 0 is specified, this interface does not display a logging message. If 1 or the other value is specified, this interface displays a message usually.": "  - ロギング（ログ表示）の設定です。0が指定された場合、このインターフェイスはログのメッセージを表示しなくなります。1もしくは他の値を指定した場合、このインターフェイスはログのメッセージを通常通り表示します。",  # noqa
    ##################################################
    "<hr>": "<hr>",
    ##################################################
    "**[Notes]**": "**[特記事項]**",
    ##################################################
    "This interface empties a specified directory before saving.<hr>": "このインターフェイスは指定された出力先のディレクトリを出力前に空にします。<hr>",  # noqa
    ##################################################
    "**[Examples]**": "**[コードサンプル]**",
    ##################################################
    '```py\n>>> import apysc as ap\n>>> stage: ap.Stage = ap.Stage()\n>>> # Do something here...\n>>> ap.save_overall_html(dest_dir_path="tmp/output/")\n```': '```py\n>>> import apysc as ap\n>>> stage: ap.Stage = ap.Stage()\n>>> # Do something here...\n>>> ap.save_overall_html(dest_dir_path="tmp/output/")\n```',  # noqa
}
