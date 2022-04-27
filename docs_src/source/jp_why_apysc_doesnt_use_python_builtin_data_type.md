<span class="inconspicuous-txt">※この翻訳ドキュメントはスクリプトによって出力・同期されています。内容が怪しそうな場合は<a href="https://github.com/simon-ritchie/apysc/issues" target="_blank">GitHubにissue</a>を追加したり[英語の原文](why_apysc_doesnt_use_python_builtin_data_type.md)の確認をお願いします。</span>

# 何故 apysc ライブラリではPythonのビルトインのデータ型を使用していないのか

このページでは apysc ライブラリが何故`int`や`float`、`bool`、`list`などのPythonビルトインのデータ型を使用していないのかについて説明します。また、何故それらの代わりに`Int`や`Number`、`Array`などのデータの型を使用しているのかについても説明します。

## apysc ではPythonをJavaScriptへと変換する必要があり、変数の変化を追う必要があります

apysc ライブラリではPythonのコードをJavaScriptへと変換するために変数の生成や更新などの処理を内部で追う必要があります。この理由から、 apysc では`Int`や`Number`（`Float`）、`String`、`Boolean`、`Array`、`Dictionary`などの独自の型を設けてそちらを使用しています。

場合によってはHTMLの生成処理でこれらの型の利用が不要な場合もありますが、イベントハンドラなどの非同期な処理を使う場合などには利用が必要になってきます。

apysc ライブラリではそれらの型の内部で自動的に変数名を割り振り、HTMLやJavaScriptのファイルを出力する際にそれらの変数名を使用します。また、変数の生成や更新などの内容も出力されるJavaScriptのコードに反映されます。

もしPythonビルトインの型を使った場合、これらの値JavaScript上では固定値で設定されます（apysc上では非同期の関数などでの変数の変更が反映されなくなります）。