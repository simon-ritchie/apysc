<span class="inconspicuous-txt">※この翻訳ドキュメントはスクリプトによって出力・同期されています。内容が怪しそうな場合は<a href="https://github.com/simon-ritchie/apysc/issues" target="_blank">GitHubにissue</a>を追加したり[英語の原文](https://simon-ritchie.github.io/apysc/en/graphics_base_line_alpha.html)の確認をお願いします。</span>

# GraphicsBase クラスの line_alpha インターフェイス

このページでは`GraphicsBase`クラスの`line_alpha`属性のインターフェイスについて説明します。

## インターフェイス概要

`line_alpha`属性のインターフェイスではインスタンスの線の透明度の更新や取得を行うことができます。

## 基本的な使い方

getterとsetterの両方のインターフェイスの値は`Number`型の0.0～1.0の範囲の値となります。

以下のコード例では0.5の線の透明度を2番目の四角に設定し、0.25の線の透明度を3番目の四角に設定しています:

```py
# runnable
import apysc as ap

ap.Stage(
    stage_width=350, stage_height=150, background_color="#333", stage_elem_id="stage"
)
sprite: ap.Sprite = ap.Sprite()
sprite.graphics.line_style(color="#0af", thickness=5)

rectangle_1: ap.Rectangle = sprite.graphics.draw_rect(x=50, y=50, width=50, height=50)

rectangle_2: ap.Rectangle = sprite.graphics.draw_rect(x=150, y=50, width=50, height=50)
rectangle_2.line_alpha = ap.Number(0.5)

rectangle_3: ap.Rectangle = sprite.graphics.draw_rect(x=250, y=50, width=50, height=50)
rectangle_3.line_alpha = ap.Number(0.25)

ap.save_overall_html(dest_dir_path="./graphics_base_line_alpha_basic_usage/")
```

<iframe src="static/graphics_base_line_alpha_basic_usage/index.html" width="350" height="150"></iframe>

## line_alpha 属性のAPI

<span class="inconspicuous-txt">特記事項: このAPIドキュメントはドキュメントビルド用のスクリプトによって自動で生成・同期されています。そのためもしかしたらこの節の内容は前節までの内容と重複している場合があります。</span>

**[インターフェイス概要]** インスタンスの線の透明度を取得します。<hr>

**[返却値]**

- `line_alpha`: Number
  - 現在の線の透明度（0.0～1.0）。

<hr>

**[コードサンプル]**

```py
>>> import apysc as ap
>>> stage: ap.Stage = ap.Stage()
>>> sprite: ap.Sprite = ap.Sprite()
>>> sprite.graphics.line_style(color="#fff", thickness=5, alpha=1.0)
>>> rectangle: ap.Rectangle = sprite.graphics.draw_rect(
...     x=50, y=50, width=50, height=50
... )
>>> rectangle.line_alpha = ap.Number(0.5)
>>> rectangle.line_alpha
Number(0.5)
```