<span class="inconspicuous-txt">※この翻訳ドキュメントはスクリプトによって出力・同期されています。内容が怪しそうな場合は<a href="https://github.com/simon-ritchie/apysc/issues" target="_blank">GitHubにissue</a>を追加したり[英語の原文](https://simon-ritchie.github.io/apysc/en/get_bounds.html)の確認をお願いします。</span>

# get_bounds インターフェイス

このページでは`get_bounds`メソッドのインターフェイスについて説明します。

## インターフェイス概要

`get_bounds`メソッドはインスタンスのバウンディングボックスのデータ（座標やサイズなどの幾何データ）を返却します。

## 基本的な使い方

`get_bounds`メソッドでは`RectangleGeom`クラスのインスタンスを返却します。

このメソッドは省略可能な`target_coordinate_space_object`引数を受け付けます。

もしこの引数が指定された場合、返却値の基準となる座標は指定された引数の`DisplayObject`からの相対座標となります。

この設定は親の`DisplayObject`の座標などの相対座標を取得したい場合などに役に立つことがあります。

もしこの引数の指定を省略した場合、座標は`Stage`を基準とした座標となります（実質的に絶対座標となります）。

引数の指定を省略した場合の例 :

```py
# runnable
import apysc as ap

stage: ap.Stage = ap.Stage(
    background_color=ap.Color("#333"),
    stage_width=500,
    stage_height=440,
    stage_elem_id="stage",
)
circle: ap.Circle = ap.Circle(
    x=250,
    y=220,
    radius=150,
    fill_color=ap.Color("#0af"),
)
bounding_box: ap.RectangleGeom = circle.get_bounds()

box_rectangle: ap.Rectangle = ap.Rectangle(
    x=bounding_box.left_x,
    y=bounding_box.top_y,
    width=bounding_box.width,
    height=bounding_box.height,
    line_color=ap.Color("#aaa"),
)

fill_color: ap.Color = ap.Color("#fd63c3")
left_x_and_top_y_circle: ap.Circle = ap.Circle(
    x=bounding_box.left_x,
    y=bounding_box.top_y,
    radius=10,
    fill_color=fill_color,
)
left_x_and_top_y_text: ap.SvgText = ap.SvgText(
    text="left_x and top_y",
    x=bounding_box.left_x,
    y=bounding_box.top_y - 15,
    fill_color=fill_color,
)

ap.save_overall_html(dest_dir_path="get_bounds_basic_usage_1/")
```

<iframe src="static/get_bounds_basic_usage_1/index.html" width="500" height="440"></iframe>

`target_coordinate_space_object`引数を指定した場合の例 :

```py
# runnable
import apysc as ap

stage: ap.Stage = ap.Stage(
    background_color=ap.Color("#333"),
    stage_width=500,
    stage_height=440,
    stage_elem_id="stage",
)
sprite: ap.Sprite = ap.Sprite()
sprite.x = ap.Number(250)
sprite.y = ap.Number(220)
circle: ap.Circle = ap.Circle(
    x=0,
    y=0,
    radius=150,
    fill_color=ap.Color("#0af"),
    parent=sprite,
)
bounding_box: ap.RectangleGeom = circle.get_bounds(
    target_coordinate_space_object=sprite,
)

box_rectangle: ap.Rectangle = ap.Rectangle(
    x=bounding_box.left_x,
    y=bounding_box.top_y,
    width=bounding_box.width,
    height=bounding_box.height,
    line_color=ap.Color("#aaa"),
    parent=sprite,
)

ap.save_overall_html(dest_dir_path="get_bounds_basic_usage_2/")
```

<iframe src="static/get_bounds_basic_usage_2/index.html" width="500" height="440"></iframe>

## get_bounds メソッドのAPI

<span class="inconspicuous-txt">特記事項: このAPIドキュメントはドキュメントビルド用のスクリプトによって自動で生成・同期されています。そのためもしかしたらこの節の内容は前節までの内容と重複している場合があります。</span>

**[インターフェイスの構造]** `get_bounds(self, target_coordinate_space_object: Union[apysc._display.display_object.DisplayObject, NoneType] = None) -> apysc._geom.rectangle_geom.RectangleGeom`<hr>

**[インターフェイス概要]**

インスタンスのバウンディングボックスの幾何データを取得します。<hr>

**[返却値]**

- `bounding_box`: RectangleGeom
  - インスタンスのバウンディングボックスの幾何データ。

- `target_coordinate_space_object`: DisplayObject or None, default None
  - 座標の基準となるオブジェクト。もしNoneが指定された場合、このメソッドはステージを基準としたバウンディングボックスのデータを返却します。もし`DisplayObject`のインスタンスが指定された場合、ごのメソッドは指定されたオブジェクトの座標を基準としたバウンディングボックスのデータを返却します。

<hr>

**[コードサンプル]**

```py
>>> import apysc as ap
>>> stage: ap.Stage = ap.Stage(
...     background_color=ap.Color("#333"), stage_width=250, stage_height=350
... )
>>> rectangle: ap.Rectangle = ap.Rectangle(
...     x=50,
...     y=100,
...     width=150,
...     height=200,
...     fill_color=ap.Color("#0af"),
... )
>>> bounding_box: ap.RectangleGeom = rectangle.get_bounds()
```

<hr>

**[関連資料]**

- [RectangleGeom クラス](https://simon-ritchie.github.io/apysc/jp/jp_rectangle_geom.html)