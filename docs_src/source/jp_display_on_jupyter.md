<span class="inconspicuous-txt">※この翻訳ドキュメントはスクリプトによって出力・同期されています。内容が怪しそうな場合は<a href="https://github.com/simon-ritchie/apysc/issues" target="_blank">GitHubにissue</a>を追加したり[英語の原文](https://simon-ritchie.github.io/apysc/en/display_on_jupyter.html)の確認をお願いします。</span>

# display_on_jupyter インターフェイス

このページでは`display_on_jupyter`関数のインターフェイスについて説明します。

## インターフェイス概要

`display_on_jupyter`関数はapyscによって生成されたHTMLをJupyter上で表示します。

## 必要とされるインストールなどの対応

このインターフェイスはJupyterのライブラリの事前のインストールが必要です。もしインストールされていなければ`pip install notebook`などのコマンドでインストールしておく必要があります。

詳細は以下をご確認ください:

- [Installing the Jupyter Software](https://jupyter.org/install)

また、このインターフェイスは`IPython.display.IFrame`のインターフェイスを使用しています。もしも該当のインターフェイス関係でエラーが発生した場合Jupyterのアップデートをお試しください。

## 特記事項

- VS Code上のJupyterは現在サポートされていません（VS Code上の制限に起因するため将来サポートするかどうかは未定です）。
- Jupyter notebook 及び JupyterLabはサポートしています。

## 基本的な使い方

出力結果のHTMLをJupyter上で表示するために`save_overall_html`関数の代わりに`display_on_jupyter`を使用することができます。

このインターフェイスは複数のHTMLファイルを保存する際にファイル名が被らないようにするために`html_file_name`引数にユニークなファイル名の指定が必要です。この値にユニークな値を指定しない場合HTMLが上書きされてしまいます。

```py
import apysc as ap

ap.Stage(
    stage_width=250,
    stage_height=150,
    background_color=ap.Color("#333"),
)
sprite = ap.Sprite()
sprite.graphics.begin_fill(color=ap.Color("#0af"))
sprite.graphics.draw_rect(x=50, y=50, width=50, height=50)

sprite.graphics.begin_fill(color=ap.Color("#f0a"))
sprite.graphics.draw_rect(x=150, y=50, width=50, height=50)

ap.display_on_jupyter(html_file_name="jupyter_sample_1.html")
```

![](_static/jupyter_notebook_interface.png)

このインターフェイスはJupyterLabもサポートしています:

![](_static/jupyterlab_interface.png)

## display_on_jupyter API

<span class="inconspicuous-txt">特記事項: このAPIドキュメントはドキュメントビルド用のスクリプトによって自動で生成・同期されています。そのためもしかしたらこの節の内容は前節までの内容と重複している場合があります。</span>

**[インターフェイスの構造]** `display_on_jupyter(html_file_name: str, *, minify: bool = True) -> None`<hr>

**[インターフェイス概要]**

HTML全体を保存し結果をJupyter上で表示します。<hr>

**[引数]**

- `html_file_name`: str, default 'index.html'
  - 出力されるHTMLのファイル名。

- `minify`: bool, default True
  - HTMLを最小化（minify）するかどうかの真偽値。Falseの設定はデバッグ時などに役に立つことがあります。

<hr>

**[特記事項]**

現在このインターフェイスはVS Code上のJupyterをサポートしていません。また、このインターフェイスは事前のJupyterのライブラリのインストールが必要です（例 : `notebook`パッケージなど）。