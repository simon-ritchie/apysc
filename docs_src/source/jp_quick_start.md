<span class="inconspicuous-txt">※この翻訳ドキュメントはスクリプトによって出力・同期されています。内容が怪しそうな場合は<a href="https://github.com/simon-ritchie/apysc/issues" target="_blank">GitHubにissue</a>を追加したり[英語の原文](../en/quick_start.html)の確認をお願いします。</span>

# クイックスタートガイド

このページではapyscのライブラリの最初の一歩としての諸々について説明します。

## インストール

apyscのライブラリを使うにはPython3.6もしくはそれ以降のPythonバージョンが必要です。

apyscはpipのコマンドを使ってインストールすることができます。

```
$ pip install apysc
```

## Stageのインスタンスを作成し、HTMLを出力する

`Stage`のインスタンスはapyscの各グラフィックスを表示する領域となるインスタンスです。幅の設定としての`stage_width`引数、高さの設定としての`stage_height`引数、そして背景色としての`background_color`引数を設定することができます。

```py
# runnable
import apysc as ap

stage = ap.Stage(stage_width=300, stage_height=180, background_color='#333')
```

さらに、結果のHTMLとJavaScriptのファイルを`save_overall_html`関数によって保存することができます（このケースではまだ黒い背景のステージが表示されるだけです）。

```py
# runnable
import apysc as ap

stage: ap.Stage = ap.Stage(
    stage_width=300, stage_height=180, background_color='#333',
    stage_elem_id='stage')
ap.save_overall_html(
    dest_dir_path='quick_start_stage_creation/')
```

このコードでは`dest_dir_path`引数に指定されたディレクトリに結果のHTMLとJavaScriptの各ファイルを生成します。以下のコード例では`index.html`のファイル（`quick_start_stage_creation/index.html`）を開くことで出力結果を確認することができます。

<iframe src="static/quick_start_stage_creation/index.html" width="300" height="180"></iframe>

## Spriteのコンテナとベクターグラフィックスを追加する

`Sprite`クラスは各表示オブジェクトのコンテナとなるクラスであり、`graphics`属性を使ってベクターグラフィックスを生成することもできます。

```py
# runnable
import apysc as ap

stage: ap.Stage = ap.Stage(
    stage_width=250, stage_height=150, background_color='#333',
    stage_elem_id='stage')
sprite: ap.Sprite = ap.Sprite()

# Draw polyline vector graphics.
sprite.graphics.line_style(color='#fff', thickness=3)
sprite.graphics.move_to(x=50, y=50)
sprite.graphics.line_to(x=100, y=50)
sprite.graphics.line_to(x=50, y=100)
sprite.graphics.line_to(x=100, y=100)

# Draw rectangle vector graphic.
sprite.graphics.begin_fill(color='#0af')
sprite.graphics.draw_rect(x=150, y=50, width=50, height=50)

ap.save_overall_html(
    dest_dir_path='quick_start_sprite_graphics/')
```

<iframe src="static/quick_start_sprite_graphics/index.html" width="250" height="150"></iframe>

`Sprite`や`Graphics`クラスの詳細については各インターフェイスのドキュメントをご確認ください。

## 関連資料

- [Sprite クラス](jp_sprite.md)
- [描画の各インターフェイスの概要](jp_draw_interfaces_abstract.md)