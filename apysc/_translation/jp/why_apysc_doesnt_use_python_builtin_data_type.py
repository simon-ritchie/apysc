"""This module is for the translation mapping data of the
following document:

Document file: why_apysc_doesnt_use_python_builtin_data_type.md
Language: jp
"""

from typing import Dict

MAPPING: Dict[str, str] = {
    ##################################################
    "# Why the apysc library doesn't use the Python built-in data type": "# 何故 apysc ライブラリではPythonのビルトインのデータ型を使用していないのか",  # noqa
    ##################################################
    "This page explains why the apysc library doesn't use the Python built-in data type, such as `int`\\, `float`\\, `bool`\\, `list`\\. And why the apysc library uses the apysc data type like the `Int`\\, `Number`\\, `Array` instead.": "このページでは apysc ライブラリが何故`int`や`float`、`bool`、`list`などのPythonビルトインのデータ型を使用していないのかについて説明します。また、何故それらの代わりに`Int`や`Number`、`Array`などのデータの型を使用しているのかについても説明します。",  # noqa
    ##################################################
    "## apysc needs to convert Python to JavaScript and track variables change": "## apysc ではPythonをJavaScriptへと変換する必要があり、変数の変化を追う必要があります",  # noqa
    ##################################################
    "The apysc library needs to track variable creation and update to convert the Python code to JavaScript. For this reason, apysc using the original data types, such as `Int`\\, `Number` (`Float`), `String`\\, `Boolean`\\, `Array`\\, and `Dictionary`.": "apysc ライブラリではPythonのコードをJavaScriptへと変換するために変数の生成や更新などの処理を内部で追う必要があります。この理由から、 apysc では`Int`や`Number`（`Float`）、`String`、`Boolean`、`Array`、`Dictionary`などの独自の型を設けてそちらを使用しています。",  # noqa
    ##################################################
    "Occasionally, these are unnecessary to create HTML. Still, these types become essential when you use the asynchronous function, such as the event handler.": "場合によってはHTMLの生成処理でこれらの型の利用が不要な場合もありますが、イベントハンドラなどの非同期な処理を使う場合などには利用が必要になってきます。",  # noqa
    ##################################################
    "The apysc library automatically sets each variable's names and uses them when exporting the HTML and JavaScript files. It also tracks variables creation and updating and applies them to the exported JavaScript.": "apysc ライブラリではそれらの型の内部で自動的に変数名を割り振り、HTMLやJavaScriptのファイルを出力する際にそれらの変数名を使用します。また、変数の生成や更新などの内容も出力されるJavaScriptのコードに反映されます。",  # noqa
    ##################################################
    "Using the Python built-in data type, these variables' values become fixed (the apysc doesn't apply asynchronous function's changes).": "もしPythonビルトインの型を使った場合、これらの値JavaScript上では固定値で設定されます（apysc上では非同期の関数などでの変数の変更が反映されなくなります）。",  # noqa
}
