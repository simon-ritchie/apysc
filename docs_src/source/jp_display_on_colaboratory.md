<span class="inconspicuous-txt">※この翻訳ドキュメントはスクリプトによって出力・同期されています。内容が怪しそうな場合は<a href="https://github.com/simon-ritchie/apysc/issues" target="_blank">GitHubにissue</a>を追加したり[英語の原文](https://simon-ritchie.github.io/apysc/en/display_on_colaboratory.html)の確認をお願いします。</span>

# display_on_colaboratory インターフェイス

このページでは`display_on_colaboratory`関数のインターフェイスについて説明します。

## インターフェイス概要

`display_on_colaboratory`インターフェイスはapyscのHTMLをGoogle Colaboratory上で表示します。

## 必要とされるインストールなどの対応

利用するには事前にGoogle Colaboratory上でapyscをインストールする必要があります。`!`の記号とpip五万度でGoogle Colaboratory上にこのライブラリをインストールすることができます。

```
!pip install apysc
```

## 基本的な使い方

`save_overall_html`関数の代わりに`display_on_colaboratory`関数のインターフェイスを使うことで出力結果のHTMLを表示することができます。

このインターフェイスは複数の出力出力ファイルをユニークにするための`html_file_name`引数によるファイル名の指定が必要になります。ユニークに設定しないとHTMLファイルが上書きされてしまいます。

```py
import apysc as ap

ap.Stage(stage_width=250, stage_height=150, background_color="#333")
sprite = ap.Sprite()
sprite.graphics.begin_fill(color="#0af")
sprite.graphics.draw_rect(x=50, y=50, width=50, height=50)

sprite.graphics.begin_fill(color="#f0a")
sprite.graphics.draw_rect(x=150, y=50, width=50, height=50)

ap.display_on_colaboratory(html_file_name="jupyter_test_1.html")
```

![](_static/colaboratory_interface.png)

## display_on_colaboratory API

<span class="inconspicuous-txt">特記事項: このAPIドキュメントはドキュメントビルド用のスクリプトによって自動で生成・同期されています。そのためもしかしたらこの節の内容は前節までの内容と重複している場合があります。</span>

**[インターフェイスの構造]** `display_on_colaboratory(html_file_name: str, *, minify: bool = True) -> None`<hr>

**[インターフェイス概要]** HTML全体を保存しGoogle Colaboratory上で表示します。<hr>

**[引数]**

- `html_file_name`: str, default 'index.html'
  - 出力されるHTMLのファイル名。

- `minify`: bool, default True
  - HTMLを最小化（minify）するかどうかの真偽値。Falseの設定はデバッグ時などに役に立つことがあります。