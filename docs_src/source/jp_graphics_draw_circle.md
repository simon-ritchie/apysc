<span class="inconspicuous-txt">※この翻訳ドキュメントはスクリプトによって出力・同期されています。内容が怪しそうな場合は<a href="https://github.com/simon-ritchie/apysc/issues" target="_blank">GitHubにissue</a>を追加したり[英語の原文](https://simon-ritchie.github.io/apysc/en/graphics_draw_circle.html)の確認をお願いします。</span>

# Graphics クラスの draw_circle インターフェイス

このページでは`Graphics`クラスの`draw_circle`メソッドのインターフェイスについて説明します。

## インターフェイス概要

`draw_circle`インターフェイスはベクターグラフィックスの円を描画します。

## 基本的な使い方

`draw_circle`インターフェイスは`x`と`y`、そして`radius`引数を持っています。

`x`と`y`引数は円の中央座標となります。`radius`引数は円の半径となります、幅と高さは`radius`引数の2倍の値になります。

```py
# runnable
import apysc as ap

ap.Stage(
    background_color="#333", stage_width=350, stage_height=200, stage_elem_id="stage"
)

sprite: ap.Sprite = ap.Sprite()

# Set the cyan color and draw the circle.
sprite.graphics.begin_fill(color="#0af")
sprite.graphics.draw_circle(x=100, y=100, radius=50)

# Set the dotted-line style and draw the circle.
sprite.graphics.begin_fill(color="")
sprite.graphics.line_style(
    color="#fff", thickness=3, dot_setting=ap.LineDotSetting(dot_size=3)
)
sprite.graphics.draw_circle(x=250, y=100, radius=50)

# Draw the inner circle.
sprite.graphics.draw_circle(x=250, y=100, radius=25)

ap.save_overall_html(dest_dir_path="graphics_draw_circle_basic_usage/")
```

<iframe src="static/graphics_draw_circle_basic_usage/index.html" width="350" height="200"></iframe>

## 返却値

`draw_circle`インターフェイスの返却値は`Circle`クラスのインスタンスとなります。

このインスタンスは`radius`属性や他の基本的な各インターフェイスを持っており生成後に値を更新することができます。

```py
# runnable
import apysc as ap

ap.Stage(
    background_color="#333", stage_width=400, stage_height=400, stage_elem_id="stage"
)

sprite: ap.Sprite = ap.Sprite()

# Draw the small radius circle.
sprite.graphics.begin_fill(color="#0af")
circle: ap.Circle = sprite.graphics.draw_circle(x=200, y=200, radius=25)

# Update circle radius to become the bigger one.
circle.radius = ap.Int(100)

ap.save_overall_html(dest_dir_path="graphics_draw_circle_return_value/")
```

<iframe src="static/graphics_draw_circle_return_value/index.html" width="400" height="400"></iframe>

## draw_circle API

<span class="inconspicuous-txt">特記事項: このAPIドキュメントはドキュメントビルド用のスクリプトによって自動で生成・同期されています。そのためもしかしたらこの節の内容は前節までの内容と重複している場合があります。</span>

**[インターフェイスの構造]** `draw_circle(self, *, x: Union[float, apysc._type.number.Number], y: Union[float, apysc._type.number.Number], radius: Union[int, apysc._type.int.Int], variable_name_suffix: str = '') -> '_circle.Circle'`<hr>

**[インターフェイス概要]**

円のベクターグラフィックスを描画します。<hr>

**[引数]**

- `x`: float or Number
  - 円の中心のX座標。

- `y`: float or Number
  - 円の中心のY座標。

- `radius`: Int or int
  - 円の半径。

- `variable_name_suffix`: str, default ''
  - JavaScript上の変数のサフィックスの設定です。この設定はJavaScriptのデバッグ時に役立つことがあります。

<hr>

**[返却値]**

- `circle`: Circle
  - 生成された円のグラフィックスのインスタンス。

<hr>

**[コードサンプル]**

```py
>>> import apysc as ap
>>> stage: ap.Stage = ap.Stage()
>>> sprite: ap.Sprite = ap.Sprite()
>>> sprite.graphics.begin_fill(color="#0af")
>>> circle: ap.Circle = sprite.graphics.draw_circle(x=100, y=100, radius=50)
>>> circle.x
Number(100.0)

>>> circle.y
Number(100.0)

>>> circle.radius
Int(50)

>>> circle.fill_color
String('#00aaff')
```