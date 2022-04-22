<span class="inconspicuous-txt">※この翻訳ドキュメントはスクリプトによって出力・同期されています。内容が怪しそうな場合は<a href="https://github.com/simon-ritchie/apysc/issues" target="_blank">GitHubにissue</a>を追加したり[英語の原文](save_overall_html.md)の確認をお願いします。</span>

# save_overall_html インターフェイス

このページでは`save_overall_html`関数のインターフェイスについて説明します。

## インターフェイス概要

`save_overall_html`関数のインターフェイスはHTMLとJavaScript全体のファイルを出力します。apyscのプロジェクトの最後でHTMLなどを出力するためにこの関数の呼び出しが必要になります。

## 基本的な使い方

`save_overall_html`関数では最低限`dest_dir_path`引数の指定が必要になります。この引数はHTMLとJavaScriptの各ファイルの出力先のディレクトリとなります。

以下のコード例ではHTMLとJavaScriptの各ファイル出力しています。出力したHTMLでは縦横150pxの空のステージのみ表示されるようにしてあります。

```py
# runnable
import apysc as ap

stage: ap.Stage = ap.Stage(
    background_color='#333',
    stage_width=150,
    stage_height=150,
    stage_elem_id='stage')

ap.save_overall_html(
    dest_dir_path='save_overall_html_interface_basic_usage/')
```

上記のコードでは`save_overall_html_interface_basic_usage/index.html`のパスにHTMLファイルや他のJavaScriptのライブラリファイルが出力されます。

<iframe src="static/save_overall_html_interface_basic_usage/index.html" width="150" height="150"></iframe>

## HTMLを最小化する

`save_overall_html`関数には`minify`のオプションの引数が存在します（デフォルトではTrueになっています）。この設定はもしTrueになっていきれば出力結果のHTMLを最小化（minify）します。Falseの設定はデバッグ時などに便利な時があります。

```py
import apysc as ap

stage: ap.Stage = ap.Stage(
    background_color='#333',
    stage_width=150,
    stage_height=150,
    stage_elem_id='stage')

ap.save_overall_html(
    dest_dir_path='dest_dir/',
    minify=False)
```

## JavaScriptのライブラリのディレクトリパスの設定と出力スキップの設定

もしもJavaScriptのライブラリパスを調整したい場合、`js_lib_dir_path`のオプションとなる引数で設定することができます。このオプションは出力されたHTML（`index.html`）内のJavaScriptのライブラリのパス指定を上書きします。

この設定は例えばDjangoのようなライブラリの静的ファイルのディレクトリを指定する形でJavaScriptライブラリのパスを指定してHTMLを出力したい場合などに役立つ時があります。

また、`skip_js_lib_exporting`の引数のオプションも既に出力済みのJavaScriptライブラリの出力を省略したい場合に役立ちます。この設定を有効にするとJavaScriptライブラリのファイルは出力されなくなります。

```py
import apysc as ap

stage: ap.Stage = ap.Stage(
    background_color='#333',
    stage_width=150,
    stage_height=150,
    stage_elem_id='stage')

ap.save_overall_html(
    dest_dir_path='dest_dir/',
    js_lib_dir_path='static/js/',
    skip_js_lib_exporting=True)
```

特記事項: 現在の実装では`js_lib_dir_path`の設定ではJavaScriptファイルの出力先は変更されません。

## html_file_name オプションを使用してHTMLのファイル名を変更する

出力されるHTMLのファイル名を変更したい場合には`html_file_name`のオプションの引数を指定することで変更することができます。この引数はHTMLのファイル名を`index.html`から任意の他の名前に変更します。

```py
import apysc as ap

stage: ap.Stage = ap.Stage(
    background_color='#333',
    stage_width=150,
    stage_height=150,
    stage_elem_id='stage')

ap.save_overall_html(
    dest_dir_path='dest_dir/',
    html_file_name='chart.html')
```

## embed_js_libs オプションでJavaScriptのライブラリを1つのHTMLファイルにまとめる

`embed_js_libs`のオプションの引数を設定することで、出力結果のHTML内に各JavaScriptライブラリの内容を含めてまとめることができます。この設定は他のメンバーにファイルを共有する場合などに1つのファイルのみで扱うことができ便利な時があります。

```py
import apysc as ap

stage: ap.Stage = ap.Stage(
    background_color='#333',
    stage_width=150,
    stage_height=150,
    stage_elem_id='stage')

ap.save_overall_html(
    dest_dir_path='dest_dir/',
    embed_js_libs=True)
```

## verbose オプションで標準出力の設定を変更する

`verbose`のオプションの引数はファイル出力時の標準出力の挙動を変更します。もしも0が指定された場合標準出力に何も表示しなくなります。1もしくは他の値を指定すればapyscライブラリは標準出力を表示します。

```py
import apysc as ap

stage: ap.Stage = ap.Stage(
    background_color='#333',
    stage_width=150,
    stage_height=150,
    stage_elem_id='stage')

ap.save_overall_html(
    dest_dir_path='dest_dir/',
    verbose=0)
```

## save_overall_html API

<span class="inconspicuous-txt">特記事項: このAPIドキュメントはドキュメントビルド用のスクリプトによって自動で生成・同期されています。そのためもしかしたらこの節の内容は前節までの内容と重複している場合があります。</span>

**[インターフェイスの構造]** `save_overall_html(dest_dir_path:str, *, html_file_name:str='index.html', minify:bool=True, js_lib_dir_path:str='./', skip_js_lib_exporting:bool=False, embed_js_libs:bool=False, verbose:int=1) -> None`<hr>

**[インターフェイス概要]** 指定されたディレクトリパス以下にHTMLとJavaScriptのファイル全体を出力します。<hr>

**[引数]**

- `dest_dir_path`: str
  - 各HTMLとJavaScriptファイルの保存先となるディレクトリパス。

- `html_file_name`: str, default 'index.html'
  - 出力されるHTMLのファイル名。

- `minify`: bool, default True
  - HTMLとJavaScriptの内容を最小化（minify）するかどうかの真偽値。Falseの設定はデバッグ時などに便利な時があります。

- `js_lib_dir_path`: str, default './'
  - JavaScriptライブラリのパスの設定。この設定はHTML内のJavaScriptのコードのパスの指定部分に影響します。指定されていない場合にはHTMLと同じディレクトリが設定されます。この設定はDjangoのようなライブラリの静的ファイルのディレクトリを指定する場合などに便利なことがあります。もしこの引数が設定された場合には`skip_js_lib_exporting`の設定も有効にすることが推奨されます。

- `skip_js_lib_exporting`: bool, default False
  - Trueが設定された場合、このインターフェイスはJavaScriptの各ライブラリを出力しなくなります。

- `embed_js_libs`: bool, default False
  - 各JavaScriptライブラリを出力されるHTML内に埋め込むかどうかの設定です。もしTrueが設定された場合、出力されるHTMLは大きくなり、そして1つのHTMLファイルのみ出力されるようになります。この設定は出力されたファイルをiframeタグで使う際にCORSのエラーを回避したい時などに役立つことがあります。

- `verbose`: int, default 1
  - ロギング（ログ表示）の設定です。0が指定された場合、このインターフェイスはログのメッセージを表示しなくなります。1もしくは他の値を指定した場合、このインターフェイスはログのメッセージを通常通り表示します。

<hr>

**[特記事項]**

このインターフェイスは指定された出力先のディレクトリを出力前に空にします。<hr>

**[コードサンプル]**

```py
>>> import apysc as ap
>>> stage: ap.Stage = ap.Stage()
>>> # Do something here...
>>> ap.save_overall_html(dest_dir_path='tmp/output/')
```