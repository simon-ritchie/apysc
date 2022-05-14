<span class="inconspicuous-txt">※この翻訳ドキュメントはスクリプトによって出力・同期されています。内容が怪しそうな場合は<a href="https://github.com/simon-ritchie/apysc/issues" target="_blank">GitHubにissue</a>を追加したり[英語の原文](https://simon-ritchie.github.io/apysc/en/point2d.html)の確認をお願いします。</span>

# Point2D クラス

このページでは`Point2D`クラスについて説明します。

## Point2D クラスの概要

`Point2D`クラスは2次元の座標値を扱うためのインターフェイスのクラスで、X座標とY座標を扱います。このクラスは`Polygon`クラスなどの一部のクラスで使用され、各頂点座標の設定用に参照されます。

## 基本的な使い方

`Point2D`クラスのコンストラクタでは`x`と`y`の各引数が必要になります。各引数はPythonのビルトインの`int`の値かもしくはapyscの`Int`の値を受け付けます。

```py
# runnable
import apysc as ap

point_1: ap.Point2D = ap.Point2D(x=10, y=20)

x: ap.Int = ap.Int(10)
y: ap.Int = ap.Int(20)
point_2: ap.Point2D = ap.Point2D(x=x, y=y)
```

## XとY座標のgetterのインターフェイス

`Point2D`クラスの`x`と`y`の属性は以下のコード例のように`Int`型の値を返却します:

```py
# runnable
import apysc as ap

point: ap.Point2D = ap.Point2D(x=10, y=20)
assert point.x == 10
assert point.y == 20
```

## XとY座標のsetterのインターフェイス

`x`と`y`属性は以下のコード例のように`Int`型の値を使って値を更新することができます:

```py
# runnable
import apysc as ap

point: ap.Point2D = ap.Point2D(x=10, y=20)
point.x = ap.Int(30)
assert point.x == 30
```

## draw_polygon インターフェイスにおける使用例

`draw_polygon`インターフェイスは`Point2D`の値のリストの引数を必要とします。そのためこの節ではその描画のインターフェイスによる`Point2D`クラスを使ったコード例を載せています。

以下のコード例では3点の座標を指定することによって三角形のベクターグラフィックスを描画しています。

```py
# runnable
import apysc as ap

ap.Stage(
    stage_width=150, stage_height=150, background_color='#333',
    stage_elem_id='stage')
sprite: ap.Sprite = ap.Sprite()
sprite.graphics.begin_fill(color='#0af')

sprite.graphics.draw_polygon(
    points=[
        ap.Point2D(x=75, y=50),
        ap.Point2D(x=50, y=100),
        ap.Point2D(x=100, y=100),
    ])

ap.save_overall_html(
    dest_dir_path='point2d_basic_usage/')
```

<iframe src="static/point2d_basic_usage/index.html" width="150" height="150"></iframe>

## Point2D クラスのコンストラクタのAPI

<span class="inconspicuous-txt">特記事項: このAPIドキュメントはドキュメントビルド用のスクリプトによって自動で生成・同期されています。そのためもしかしたらこの節の内容は前節までの内容と重複している場合があります。</span>

**[インターフェイスの構造]** `__init__(self, x: Union[int, apysc._type.int.Int], y: Union[int, apysc._type.int.Int]) -> None`<hr>

**[インターフェイス概要]** 2次元の座標値を扱うクラスです。<hr>

**[引数]**

- `x`: int or Int
  - X座標。

- `y`: int or Int
  - Y座標。

<hr>

**[コードサンプル]**

```py
>>> import apysc as ap
>>> stage: ap.Stage = ap.Stage()
>>> sprite: ap.Sprite = ap.Sprite()
>>> sprite.graphics.begin_fill(color='#0af')
>>> polygon: ap.Polygon = sprite.graphics.draw_polygon(
...     points=[
...         ap.Point2D(x=0, y=0),
...         ap.Point2D(x=0, y=50),
...         ap.Point2D(x=50, y=25),
...     ])
```

## x属性のAPI

<span class="inconspicuous-txt">特記事項: このAPIドキュメントはドキュメントビルド用のスクリプトによって自動で生成・同期されています。そのためもしかしたらこの節の内容は前節までの内容と重複している場合があります。</span>

**[インターフェイス概要]** X座標の属性のインターフェイスです。<hr>

**[返却値]**

- `x`: Int
  - X座標。

<hr>

**[コードサンプル]**

```py
>>> import apysc as ap
>>> point: ap.Point2D = ap.Point2D(x=50, y=100)
>>> point.x = ap.Int(150)
>>> point.x
Int(150)
```

## y属性のAPI

<span class="inconspicuous-txt">特記事項: このAPIドキュメントはドキュメントビルド用のスクリプトによって自動で生成・同期されています。そのためもしかしたらこの節の内容は前節までの内容と重複している場合があります。</span>

**[インターフェイス概要]** Y座標の属性のインターフェイスです。<hr>

**[返却値]**

- `y`: Int
  - Y座標。

<hr>

**[コードサンプル]**

```py
>>> import apysc as ap
>>> point: ap.Point2D = ap.Point2D(x=50, y=100)
>>> point.y = ap.Int(150)
>>> point.y
Int(150)
```