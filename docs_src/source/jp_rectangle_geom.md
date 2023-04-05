<span class="inconspicuous-txt">※この翻訳ドキュメントはスクリプトによって出力・同期されています。内容が怪しそうな場合は<a href="https://github.com/simon-ritchie/apysc/issues" target="_blank">GitHubにissue</a>を追加したり[英語の原文](https://simon-ritchie.github.io/apysc/en/rectangle_geom.html)の確認をお願いします。</span>

# RectangleGeom クラス

このページでは`RectangleGeom`クラスについて説明します。

## クラス概要

`RectangleGeom`クラスは`lext_x`や`center_x`、`right_x`、`top_y`、`center_y`、`bottom_y`、`width`、`height`といった四角の幾何学（座標やサイズなど）の各インターフェイスを持ちます。

## 基本的な使い方

多くのケースでは、apyscが内部で`RectangleGeom`クラスを初期化します。

例えば、`get_bounds`メソッドは`RectangleGeom`インスタンスを返却し、且つそのインスタンスに四角の幾何学のデータ（バウンディングボックス）を設定します。

```py
# runnable
import apysc as ap

stage: ap.Stage = ap.Stage(background_color="#333", stage_width=300, stage_height=200)
rectangle: ap.Rectangle = ap.Rectangle(
    x=50,
    y=50,
    width=200,
    height=75,
    fill_color="#0af",
)
bounding_box: ap.RectangleGeom = rectangle.get_bounds()
text_1: ap.SVGText = ap.SVGText(
    text=(
        ap.String("Left x: ")
        + bounding_box.left_x.to_string()
        + ap.String(" width: ")
        + bounding_box.width.to_string()
    ),
    x=50,
    y=150,
    fill_color="#aaa",
)
ap.save_overall_html(dest_dir_path="rectangle_geom_basic_usage/")
```

<iframe src="static/rectangle_geom_basic_usage/index.html" width="300" height="200"></iframe>

## 各属性の座標

以下の例では各属性の座標を表示しています:

```py
# runnable
import apysc as ap

stage: ap.Stage = ap.Stage(background_color="#333", stage_width=600, stage_height=440)
circle: ap.Circle = ap.Circle(
    x=250,
    y=220,
    radius=150,
    fill_color="#0af",
)
bounding_box: ap.RectangleGeom = circle.get_bounds()

LINE_COLOR: str = "#aaa"
box_rectangle: ap.Rectangle = ap.Rectangle(
    x=bounding_box.left_x,
    y=bounding_box.top_y,
    width=bounding_box.width,
    height=bounding_box.height,
    line_color=LINE_COLOR,
)

POINT_RADIUS: int = 10
fill_color: str = "#fd63c3"
left_x_and_top_y_circle: ap.Circle = ap.Circle(
    x=bounding_box.left_x,
    y=bounding_box.top_y,
    radius=POINT_RADIUS,
    fill_color=fill_color,
)
left_x_and_top_y_text: ap.SVGText = ap.SVGText(
    text="left_x and top_y",
    x=bounding_box.left_x,
    y=bounding_box.top_y - 15,
    fill_color=fill_color,
)

fill_color = "#ae59e3"
right_x_and_top_y_circle: ap.Circle = ap.Circle(
    x=bounding_box.right_x,
    y=bounding_box.top_y,
    radius=POINT_RADIUS,
    fill_color=fill_color,
)
right_x_and_top_y_text: ap.SVGText = ap.SVGText(
    text="right_x and top_y",
    x=bounding_box.right_x,
    y=bounding_box.top_y - 15,
    fill_color=fill_color,
)

fill_color = "#726efa"
left_x_and_bottom_y_circle: ap.Circle = ap.Circle(
    x=bounding_box.left_x,
    y=bounding_box.bottom_y,
    radius=POINT_RADIUS,
    fill_color=fill_color,
)
left_x_and_bottom_y_text: ap.SVGText = ap.SVGText(
    text="left_x and bottom_y",
    x=bounding_box.left_x,
    y=bounding_box.bottom_y + 31,
    fill_color=fill_color,
)

fill_color = "#6eaee6"
right_x_and_bottom_y_circle: ap.Circle = ap.Circle(
    x=bounding_box.right_x,
    y=bounding_box.bottom_y,
    radius=POINT_RADIUS,
    fill_color=fill_color,
)
right_x_and_bottom_y_text: ap.SVGText = ap.SVGText(
    text="right_x and bottom_y",
    x=bounding_box.right_x,
    y=bounding_box.bottom_y + 31,
    fill_color=fill_color,
)

fill_color = "#ffffff"
center_x_and_center_y_circle: ap.Circle = ap.Circle(
    x=bounding_box.center_x,
    y=bounding_box.center_y,
    radius=POINT_RADIUS,
    fill_color=fill_color,
)
center_x_and_center_y_text: ap.SVGText = ap.SVGText(
    text="center_x and center_y",
    x=bounding_box.center_x + 25,
    y=bounding_box.center_y + 5,
    fill_color=fill_color,
)

ap.save_overall_html(dest_dir_path="rectangle_geom_each_attribute_point/")
```

<iframe src="static/rectangle_geom_each_attribute_point/index.html" width="600" height="440"></iframe>

## RectangleGeom クラスのコンストラクタのAPI

<span class="inconspicuous-txt">特記事項: このAPIドキュメントはドキュメントビルド用のスクリプトによって自動で生成・同期されています。そのためもしかしたらこの節の内容は前節までの内容と重複している場合があります。</span>

**[インターフェイスの構造]** `__init__(self, *, left_x: apysc._type.number.Number, center_x: apysc._type.number.Number, right_x: apysc._type.number.Number, top_y: apysc._type.number.Number, center_y: apysc._type.number.Number, bottom_y: apysc._type.number.Number, width: apysc._type.int.Int, height: apysc._type.int.Int)`<hr>

**[インターフェイス概要]**

四角の幾何学情報を扱うためのクラスです。<hr>

**[引数]**

- `left_x`: Number
  - 四角の左端のX座標。

- `center_x`: Number
  - 四角の中央のX座標。

- `right_x`: Number
  - 四角の右端のX座標。

- `top_y`: Number
  - 四角の上端のY座標。

- `center_y`: Number
  - 四角の中央のY座標。

- `bottom_y`: Number
  - 四角の下端のY座標。

- `width`: Int
  - 四角の幅。

- `height`: Int
  - 四角の高さ。

## RectangleGeom クラスの left_x 属性のAPI

<span class="inconspicuous-txt">特記事項: このAPIドキュメントはドキュメントビルド用のスクリプトによって自動で生成・同期されています。そのためもしかしたらこの節の内容は前節までの内容と重複している場合があります。</span>

**[インターフェイス概要]**

四角の左端のX座標を取得します。<hr>

**[返却値]**

- `left_x`: Number
  - 四角の左端のX座標。

## RectangleGeom クラスの center_x 属性のAPI

<span class="inconspicuous-txt">特記事項: このAPIドキュメントはドキュメントビルド用のスクリプトによって自動で生成・同期されています。そのためもしかしたらこの節の内容は前節までの内容と重複している場合があります。</span>

**[インターフェイス概要]**

四角の中央のX座標を取得します。<hr>

**[返却値]**

- `center_x`: Number
  - 四角の中央のX座標。

## RectangleGeom クラスの right_x 属性のAPI

<span class="inconspicuous-txt">特記事項: このAPIドキュメントはドキュメントビルド用のスクリプトによって自動で生成・同期されています。そのためもしかしたらこの節の内容は前節までの内容と重複している場合があります。</span>

**[インターフェイス概要]**

四角の右端のX座標を取得します。<hr>

**[返却値]**

- `right_x`: Number
  - 四角の右端のX座標。

## RectangleGeom クラスの top_y 属性のAPI

<span class="inconspicuous-txt">特記事項: このAPIドキュメントはドキュメントビルド用のスクリプトによって自動で生成・同期されています。そのためもしかしたらこの節の内容は前節までの内容と重複している場合があります。</span>

**[インターフェイス概要]**

四角の上端のY座標を取得します。<hr>

**[返却値]**

- `top_y`: Number
  - 四角の上端のY座標。

## RectangleGeom クラスの center_y 属性のAPI

<span class="inconspicuous-txt">特記事項: このAPIドキュメントはドキュメントビルド用のスクリプトによって自動で生成・同期されています。そのためもしかしたらこの節の内容は前節までの内容と重複している場合があります。</span>

**[インターフェイス概要]**

四角の中央のY座標を取得します。<hr>

**[返却値]**

- `center_y`: Number
  - 四角の中央のY座標。

## RectangleGeom クラスの bottom_y 属性のAPI

<span class="inconspicuous-txt">特記事項: このAPIドキュメントはドキュメントビルド用のスクリプトによって自動で生成・同期されています。そのためもしかしたらこの節の内容は前節までの内容と重複している場合があります。</span>

**[インターフェイス概要]**

四角の下端のY座標を取得します。<hr>

**[返却値]**

- `bottom_y`: Number
  - 四角の下端のY座標。

## RectangleGeom クラスの width 属性のAPI

<span class="inconspicuous-txt">特記事項: このAPIドキュメントはドキュメントビルド用のスクリプトによって自動で生成・同期されています。そのためもしかしたらこの節の内容は前節までの内容と重複している場合があります。</span>

**[インターフェイス概要]**

四角の幅の値を取得します。<hr>

**[返却値]**

- `width`: Int
  - 四角の幅の値。

## RectangleGeom の height 属性のAPI

<span class="inconspicuous-txt">特記事項: このAPIドキュメントはドキュメントビルド用のスクリプトによって自動で生成・同期されています。そのためもしかしたらこの節の内容は前節までの内容と重複している場合があります。</span>

**[インターフェイス概要]**

四角の高さの値を取得します。<hr>

**[返却値]**

- `height`: Int
  - 四角の高さの値。

## get_bounds メソッドのAPI

<span class="inconspicuous-txt">特記事項: このAPIドキュメントはドキュメントビルド用のスクリプトによって自動で生成・同期されています。そのためもしかしたらこの節の内容は前節までの内容と重複している場合があります。</span>

**[インターフェイスの構造]** `get_bounds(self) -> apysc._geom.rectangle_geom.RectangleGeom`<hr>

**[インターフェイス概要]**

インスタンスのバウンディングボックスの幾何データを取得します。<hr>

**[返却値]**

- `bounding_box`: RectangleGeom
  - インスタンスのバウンディングボックスの幾何データ。