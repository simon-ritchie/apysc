<span class="inconspicuous-txt">※この翻訳ドキュメントはスクリプトによって出力・同期されています。内容が怪しそうな場合は<a href="https://github.com/simon-ritchie/apysc/issues" target="_blank">GitHubにissue</a>を追加したり[英語の原文](https://simon-ritchie.github.io/apysc/en/graphics_base_fill_alpha.html)の確認をお願いします。</span>

# GraphicsBase クラスの fill_alpha インターフェイス

このページでは`GraphicsBase`クラスの`fill_alpha`属性のインターフェイスについて説明します。

## インターフェイス概要

`fill_alpha`属性のインターフェイスではインスタンスの塗りの透明度更新や取得を行うことができます。

## 基本的な使い方

属性のgetterとsetterのインターフェイスの値は`Number`型の値となります（0.0～1.0）。

以下のコード例では2つ目の四角に0.5の透明度を、そして3つ目の四角に0.25の透明度を設定しています:

```py
# runnable
import apysc as ap

ap.Stage(
    stage_width=350, stage_height=150, background_color="#333", stage_elem_id="stage"
)
sprite: ap.Sprite = ap.Sprite()
sprite.graphics.begin_fill(color="#0af")

rectangle_1: ap.Rectangle = sprite.graphics.draw_rect(x=50, y=50, width=50, height=50)

rectangle_2: ap.Rectangle = sprite.graphics.draw_rect(x=150, y=50, width=50, height=50)
rectangle_2.fill_alpha = ap.Number(0.5)

rectangle_3: ap.Rectangle = sprite.graphics.draw_rect(x=250, y=50, width=50, height=50)
rectangle_3.fill_alpha = ap.Number(0.25)

ap.save_overall_html(dest_dir_path="./graphics_base_fill_alpha_basic_usage/")
```

<iframe src="static/graphics_base_fill_alpha_basic_usage/index.html" width="350" height="150"></iframe>

## fill_alpha 属性のAPI

<span class="inconspicuous-txt">特記事項: このAPIドキュメントはドキュメントビルド用のスクリプトによって自動で生成・同期されています。そのためもしかしたらこの節の内容は前節までの内容と重複している場合があります。</span>

**[インターフェイス概要]** このインスタンスの塗りの透明度を取得します。<hr>

**[返却値]**

- `fill_alpha`: Number
  - 現在の塗りの透明度（0.0～1.0）。

<hr>

**[コードサンプル]**

```py
>>> import apysc as ap
>>> stage: ap.Stage = ap.Stage()
>>> sprite: ap.Sprite = ap.Sprite()
>>> sprite.graphics.begin_fill(color="#0af")
>>> rectangle: ap.Rectangle = sprite.graphics.draw_rect(
...     x=50, y=50, width=50, height=50
... )
>>> rectangle.fill_alpha = ap.Number(0.5)
>>> rectangle.fill_alpha
Number(0.5)
```