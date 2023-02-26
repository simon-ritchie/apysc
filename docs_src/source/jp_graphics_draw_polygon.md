<span class="inconspicuous-txt">※この翻訳ドキュメントはスクリプトによって出力・同期されています。内容が怪しそうな場合は<a href="https://github.com/simon-ritchie/apysc/issues" target="_blank">GitHubにissue</a>を追加したり[英語の原文](https://simon-ritchie.github.io/apysc/en/graphics_draw_polygon.html)の確認をお願いします。</span>

# Graphics クラスの draw_polygon インターフェイス

このページでは`Graphics`クラスの`draw_polygon`メソッドのインターフェイスについて説明します。

## インターフェイス概要

`draw_polygon`インターフェイスは多角形のベクターグラフィックスを描画します。このインターフェイスは`line_to`や`move_to`などのインターフェイスと挙動が少し似ていますが、パスを閉じなくても良いという違いがあります。

## 基本的な使い方

`draw_polygon`インターフェイスは各頂点の座標を決めるための`points`引数を必要とします。

```py
# runnable
import apysc as ap

ap.Stage(
    background_color="#333", stage_width=250, stage_height=150, stage_elem_id="stage"
)

sprite: ap.Sprite = ap.Sprite()

# Draw the triangle with the draw_polygon interface.
sprite.graphics.begin_fill(color="#0af")
sprite.graphics.draw_polygon(
    points=ap.Array(
        [
            ap.Point2D(x=75, y=50),
            ap.Point2D(x=50, y=100),
            ap.Point2D(x=100, y=100),
        ]
    )
)

# Draw the diamond shape with the draw_polygon interface.
sprite.graphics.draw_polygon(
    points=ap.Array(
        [
            ap.Point2D(x=175, y=50),
            ap.Point2D(x=150, y=75),
            ap.Point2D(x=175, y=100),
            ap.Point2D(x=200, y=75),
        ]
    )
)

ap.save_overall_html(dest_dir_path="graphics_draw_polygon_basic_usage/")
```

<iframe src="static/graphics_draw_polygon_basic_usage/index.html" width="250" height="150"></iframe>

## line_to と draw_polygon の各インターフェイスの違いについて

塗りの色の設定をした場合`draw_polygon`と`line_to`（及び`move_to`）のインターフェイスの挙動は少し近くなります。例えば以下のコード例では各インターフェイスでどちらも三角形が描画しています。

`draw_polygon`インターフェイスでは左側の三角形を描画し、`move_to`と`line_to`のインターフェイスでは右側の三角形を描画しています。

```py
# runnable
import apysc as ap

ap.Stage(
    background_color="#333", stage_width=250, stage_height=150, stage_elem_id="stage"
)

sprite: ap.Sprite = ap.Sprite()
sprite.graphics.begin_fill(color="#0af")

# Draw the triangle with the draw_polygon interface.
sprite.graphics.draw_polygon(
    points=ap.Array(
        [
            ap.Point2D(x=75, y=50),
            ap.Point2D(x=50, y=100),
            ap.Point2D(x=100, y=100),
        ]
    )
)

# Draw the triangle with the move_to and line_to interfaces.
sprite.graphics.move_to(x=175, y=50)
sprite.graphics.line_to(x=150, y=100)
sprite.graphics.line_to(x=200, y=100)

ap.save_overall_html(dest_dir_path="graphics_draw_polygon_line_to_difference_1/")
```

<iframe src="static/graphics_draw_polygon_line_to_difference_1/index.html" width="250" height="150"></iframe>

一方で、各インターフェイスにはパスを閉じる必要があるかどうかの違いがあります。この違いは線の設定を行った場合には顕著になります。`line_to`のインターフェイスでは終点の座標から始点の座標へはパスが自動では繋がりません。

```py
# runnable
import apysc as ap

stage: ap.Stage = ap.Stage(
    background_color="#333", stage_width=250, stage_height=150, stage_elem_id="stage"
)

sprite: ap.Sprite = ap.Sprite()
sprite.graphics.begin_fill(color="#0af")

# Set the line style to see the difference.
sprite.graphics.line_style(color="#fff", thickness=3)

# Draw the triangle with the draw_polygon interface.
sprite.graphics.draw_polygon(
    points=ap.Array(
        [
            ap.Point2D(x=75, y=50),
            ap.Point2D(x=50, y=100),
            ap.Point2D(x=100, y=100),
        ]
    )
)

# Draw the triangle with the move_to and line_to interfaces.
sprite.graphics.move_to(x=175, y=50)
sprite.graphics.line_to(x=150, y=100)
sprite.graphics.line_to(x=200, y=100)

ap.save_overall_html(dest_dir_path="graphics_draw_polygon_line_to_difference_2/")
```

<iframe src="static/graphics_draw_polygon_line_to_difference_2/index.html" width="250" height="150"></iframe>

## 返却値

`draw_polygon`インターフェイスは`Polygon`クラスのインスタンスを返却します。そのインスタンスは他のグラフィックス系のインスタンスと同様の基本的なインターフェイスを持っています。加えて、`Polygon`クラスは頂点を加えるための`append_line_point`メソッドを持っています。

例えば以下のコード例では座標の追加を行い三角から四角に変換しています。

```py
# runnable
import apysc as ap

ap.Stage(
    background_color="#333", stage_width=150, stage_height=150, stage_elem_id="stage"
)

sprite: ap.Sprite = ap.Sprite()
sprite.graphics.begin_fill(color="#0af")

# Draw the triangle.
polygon: ap.Polygon = sprite.graphics.draw_polygon(
    points=ap.Array(
        [
            ap.Point2D(x=75, y=50),
            ap.Point2D(x=50, y=75),
            ap.Point2D(x=75, y=100),
        ]
    )
)

# Append the point and change to the rectangle dynamically.
polygon.append_line_point(x=100, y=75)

ap.save_overall_html(dest_dir_path="graphics_draw_polygon_append_line_point/")
```

<iframe src="static/graphics_draw_polygon_append_line_point/index.html" width="150" height="150"></iframe>

## draw_polygon API

<span class="inconspicuous-txt">特記事項: このAPIドキュメントはドキュメントビルド用のスクリプトによって自動で生成・同期されています。そのためもしかしたらこの節の内容は前節までの内容と重複している場合があります。</span>

**[インターフェイスの構造]** `draw_polygon(self, *, points: Union[List[apysc._geom.point2d.Point2D], apysc._type.array.Array[apysc._geom.point2d.Point2D]], variable_name_suffix: str = '') -> '_polyg.Polygon'`<hr>

**[インターフェイス概要]**

多角形のベクターグラフィックスを描画します。このインターフェイスはPolylineクラス（`move_to`や`line_to`のインターフェイスで作成されます）に似ていますが、このインターフェイスは始点と終点が連結されるという違いがあります。<hr>

**[引数]**

- `points`: list of Point2D or Array.
  - 多角形の頂点の各座標。

- `variable_name_suffix`: str, default ''
  - JavaScript上の変数のサフィックスの設定です。この設定はJavaScriptのデバッグ時に役立つことがあります。

<hr>

**[返却値]**

- `polygon`: Polygon
  - 作成された多角形のグラフィックスのインスタンス。

<hr>

**[コードサンプル]**

```py
>>> import apysc as ap
>>> stage: ap.Stage = ap.Stage()
>>> sprite: ap.Sprite = ap.Sprite()
>>> sprite.graphics.begin_fill(color="#0af")
>>> polygon: ap.Polygon = sprite.graphics.draw_polygon(
...     points=[
...         ap.Point2D(x=25, y=0),
...         ap.Point2D(x=0, y=50),
...         ap.Point2D(x=50, y=50),
...     ]
... )
>>> polygon.fill_color
String("#00aaff")
```