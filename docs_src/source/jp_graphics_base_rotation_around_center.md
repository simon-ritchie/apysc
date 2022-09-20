<span class="inconspicuous-txt">※この翻訳ドキュメントはスクリプトによって出力・同期されています。内容が怪しそうな場合は<a href="https://github.com/simon-ritchie/apysc/issues" target="_blank">GitHubにissue</a>を追加したり[英語の原文](https://simon-ritchie.github.io/apysc/en/graphics_base_rotation_around_center.html)の確認をお願いします。</span>

# GraphicsBase クラスの rotation_around_center インターフェイス

このページでは`GraphicsBase`クラス（`Rectangle`などのグラフィックのクラスの基底クラス）の`rotation_around_center`属性のインターフェイスについて説明します。

## インターフェイス概要

`rotation_around_center`属性のインターフェイスではインスタンスの中央座標を基準とした回転角度の設定を行うことができます。

## 基本的な使い方

`rotation_around_center`インターフェイスは`int`もしくは`Int`の値を受け付けます。

```py
# runnable
import apysc as ap

ap.Stage(
    background_color="#333", stage_width=150, stage_height=150, stage_elem_id="stage"
)
sprite: ap.Sprite = ap.Sprite()

# Set the cyan fill color and draw the rectangle.
sprite.graphics.begin_fill(color="#0af", alpha=0.5)
cyan_rect: ap.Rectangle = sprite.graphics.draw_rect(x=50, y=50, width=50, height=50)
cyan_rect.rotation_around_center = ap.Int(30)

# Set the magenta fill color and draw the rectangle.
sprite.graphics.begin_fill(color="#f0a", alpha=0.5)
magenta_rect: ap.Rectangle = sprite.graphics.draw_rect(x=50, y=50, width=50, height=50)
# Append the rotation angle with the incremental addition (the result
# rotation will be 60 degrees).
magenta_rect.rotation_around_center += ap.Int(30)
magenta_rect.rotation_around_center += ap.Int(30)

ap.save_overall_html(dest_dir_path="graphics_base_rotation_around_center_basic_usage/")
```

<iframe src="static/graphics_base_rotation_around_center_basic_usage/index.html" width="150" height="150"></iframe>

## 特記事項

このインターフェイスは現在グラフィック系のクラスでのみサポートしており、`Sprite`などのコンテナーのインスタンスでは現在サポートしていません（HTMLのSVGの仕様に依存しています）。

## rotation_around_center 属性のAPI

<span class="inconspicuous-txt">特記事項: このAPIドキュメントはドキュメントビルド用のスクリプトによって自動で生成・同期されています。そのためもしかしたらこの節の内容は前節までの内容と重複している場合があります。</span>

**[インターフェイス概要]**

インスタンスの中央座標を基準とした回転量を取得します。<hr>

**[返却値]**

- `rotation_around_center`: Int
  - このインスタンスの中央座標を基準とした回転量。

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
>>> rectangle.rotation_around_center = ap.Int(45)
>>> rectangle.rotation_around_center
Int(45)
```