<span class="inconspicuous-txt">※この翻訳ドキュメントはスクリプトによって出力・同期されています。内容が怪しそうな場合は<a href="https://github.com/simon-ritchie/apysc/issues" target="_blank">GitHubにissue</a>を追加したり[英語の原文](https://simon-ritchie.github.io/apysc/en/graphics_line_thickness.html)の確認をお願いします。</span>

# Graphics クラスの line_thickness インターフェイス

このページでは`Graphics`クラスの`line_thickness`属性のインターフェイスについて説明します。

## インターフェイス概要

`line_thickness`属性のインターフェイスではインスタンスの線幅の値の更新や取得が行えます。

## 基本的な使い方

getterもしくはsetterの各インターフェイスの値は`Int`型の値になります。

以下のコード例では1つ目の四角に5pxの線幅を設定しており、2つ目の四角には10pxの線幅を設定しています:

```py
# runnable
import apysc as ap

ap.Stage(
    stage_width=250, stage_height=150, background_color='#333',
    stage_elem_id='stage')
sprite: ap.Sprite = ap.Sprite()
sprite.graphics.line_style(color='#0af', thickness=1)

rectangle_1: ap.Rectangle = sprite.graphics.draw_rect(
    x=50, y=50, width=50, height=50)
rectangle_1.line_thickness = ap.Int(5)

rectangle_2: ap.Rectangle = sprite.graphics.draw_rect(
    x=150, y=50, width=50, height=50)
rectangle_2.line_thickness = ap.Int(10)

ap.save_overall_html(
    dest_dir_path='./graphics_line_thickness_basic_usage/')
```

<iframe src="static/graphics_line_thickness_basic_usage/index.html" width="250" height="150"></iframe>

## line_thickness 属性のAPI

<span class="inconspicuous-txt">特記事項: このAPIドキュメントはドキュメントビルド用のスクリプトによって自動で生成・同期されています。そのためもしかしたらこの節の内容は前節までの内容と重複している場合があります。</span>

**[インターフェイス概要]** このインスタンスの線幅を取得します。<hr>

**[返却値]**

- `line_thickness`: Int
  - 現在の線幅。

<hr>

**[コードサンプル]**

```py
>>> import apysc as ap
>>> stage: ap.Stage = ap.Stage()
>>> sprite: ap.Sprite = ap.Sprite()
>>> sprite.graphics.line_style(
...     color='#fff', thickness=5)
>>> line: ap.Line = sprite.graphics.draw_line(
...     x_start=50, y_start=50, x_end=150, y_end=50)
>>> line.line_thickness
Int(5)
```