<span class="inconspicuous-txt">※この翻訳ドキュメントはスクリプトによって出力・同期されています。内容が怪しそうな場合は<a href="https://github.com/simon-ritchie/apysc/issues" target="_blank">GitHubにissue</a>を追加したり[英語の原文](https://simon-ritchie.github.io/apysc/en/graphics_draw_round_rect.html)の確認をお願いします。</span>

# Graphics クラスの draw_round_rect インターフェイス

このページでは`Graphics`クラスの`draw_round_rect`メソッドのインターフェイスについて説明します。

## インターフェイス概要

`draw_round_rect`インターフェイスは角丸の四角のベクターグラフィックスを描画します。

## 基本的な使い方

`draw_round_rect`インターフェイスは`x`、`y`、`width`、`height`などの各引数を持っています。`x`と`y`引数は四角の座標を設定し、`width`と`height`は四角のサイズを決定します。

このインターフェイスはさらに角丸のサイズを設定するための`ellipse_width`と`ellipse_height`の引数を持っています。

```py
# runnable
import apysc as ap

ap.Stage(
    background_color='#333',
    stage_width=350,
    stage_height=150,
    stage_elem_id='stage')

sprite: ap.Sprite = ap.Sprite()
sprite.graphics.begin_fill(color='#0af')

# Set 10-pixel ellipse size and draw the rectangle.
sprite.graphics.draw_round_rect(
    x=50, y=50, width=50, height=50, ellipse_width=10, ellipse_height=10)

# Set 20-pixel ellipse size and draw the rectangle.
sprite.graphics.draw_round_rect(
    x=150, y=50, width=50, height=50, ellipse_width=20, ellipse_height=20)

# Set 5-pixel ellipse width and 20-pixel ellipse height and
# draw the rectangle.
sprite.graphics.draw_round_rect(
    x=250, y=50, width=50, height=50, ellipse_width=5, ellipse_height=20)

ap.save_overall_html(
    dest_dir_path='graphics_draw_round_rect_basic_usage/')
```

<iframe src="static/graphics_draw_round_rect_basic_usage/index.html" width="350" height="150"></iframe>

## 返却値

`draw_round_rect`インターフェイスは`draw_rect`インターフェイスと同様に`Rectangle`クラスのインスタンスを返却します。

`Rectangle`クラスのインスタンスは四角の角丸のサイズを変更するための`ellipse_width`と`ellipse_height`属性を持っています。

```py
# runnable
import apysc as ap

ap.Stage(
    background_color='#333',
    stage_width=150,
    stage_height=150,
    stage_elem_id='stage')

sprite: ap.Sprite = ap.Sprite()
sprite.graphics.begin_fill(color='#0af')

rectangle: ap.Rectangle = sprite.graphics.draw_round_rect(
    x=50, y=50, width=50, height=50, ellipse_width=10, ellipse_height=10)

# You can update the ellipse_width and ellipse_height
# attributes dynamically.
rectangle.ellipse_width = ap.Int(20)

ap.save_overall_html(
    dest_dir_path='graphics_draw_round_rect_return_value/')
```

<iframe src="static/graphics_draw_round_rect_return_value/index.html" width="150" height="150"></iframe>

## draw_round_rect API

<span class="inconspicuous-txt">特記事項: このAPIドキュメントはドキュメントビルド用のスクリプトによって自動で生成・同期されています。そのためもしかしたらこの節の内容は前節までの内容と重複している場合があります。</span>

**[インターフェイスの構造]** `draw_round_rect(self, *, x: Union[int, apysc._type.int.Int], y: Union[int, apysc._type.int.Int], width: Union[int, apysc._type.int.Int], height: Union[int, apysc._type.int.Int], ellipse_width: Union[int, apysc._type.int.Int], ellipse_height: Union[int, apysc._type.int.Int]) -> apysc._display.rectangle.Rectangle`<hr>

**[インターフェイス概要]** 角丸四角のベクターグラフィックスを描画します。<hr>

**[引数]**

- `x`: Int or int
  - 描画を開始するX座標。

- `y`: Int or int
  - 描画を開始するY座標。

- `width`: Int or int
  - 四角の幅。

- `height`: Int or int
  - 四角の高さ。

- `ellipse_width`: Int or int
  - 四角の角丸の幅。

- `ellipse_height`: Int or int
  - 四角の角丸の高さ。

<hr>

**[返却値]**

- `rectangle`: Rectangle
  - 生成された四角。

<hr>

**[コードサンプル]**

```py
>>> import apysc as ap
>>> stage: ap.Stage = ap.Stage()
>>> sprite: ap.Sprite = ap.Sprite()
>>> sprite.graphics.begin_fill(color='#0af')
>>> round_rect: ap.Rectangle = sprite.graphics.draw_round_rect(
...     x=50, y=50, width=50, height=50,
...     ellipse_width=10, ellipse_height=15)
>>> round_rect.ellipse_width
Int(10)

>>> round_rect.ellipse_height
Int(15)
```