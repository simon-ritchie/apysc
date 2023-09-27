<span class="inconspicuous-txt">※この翻訳ドキュメントはスクリプトによって出力・同期されています。内容が怪しそうな場合は<a href="https://github.com/simon-ritchie/apysc/issues" target="_blank">GitHubにissue</a>を追加したり[英語の原文](https://simon-ritchie.github.io/apysc/en/path_bezier_3d.html)の確認をお願いします。</span>

# PathBezier3D クラス

このページでは`PathBezier3D`クラスについて説明します。

## クラス概要

`PathBezier3D`クラスはパス上に3次のベジェ曲線を設定するためのクラスです。

このクラスは2つの制御点を持ちます（比較対象として、2次のベジェ曲線では1つの制御点のみを持ちます）。

主にこの設定は`Path`クラスのコンストラクタと`draw_path`メソッドのインターフェイスで使用されます。

## 基本的な使い方

`PathBezier3D`クラスのコンストラクタでは`control_x1`、`control_y1`、`control_x2`、`control_y2`、`dest_x`、`dest_y`の各引数の指定が必要です。

`control_x1`と`control_y1`はベジェ曲線の最初の制御点の位置を決定するための座標指定です。

同様に、`control_x2`と`control_y2`はベジェ曲線の2番目の制御点の位置を決定するための座標指定です。

`dest_x`と`dest_y`はベジェ曲線の終点座標の指定となります。

```py
# runnable
import apysc as ap

ap.Stage(
    background_color=ap.Color("#333"),
    stage_width=250,
    stage_height=270,
    stage_elem_id="stage",
)

path: ap.Path = ap.Path(
    path_data_list=[
        ap.PathMoveTo(x=50, y=200),
        ap.PathBezier3D(
            control_x1=50,
            control_y1=25,
            control_x2=200,
            control_y2=25,
            dest_x=200,
            dest_y=200,
        ),
    ],
    line_color=ap.Color("#0af"),
    line_thickness=5,
)

ap.save_overall_html(dest_dir_path="path_bezier_3d_basic_usage_1/")
```

<iframe src="static/path_bezier_3d_basic_usage_1/index.html" width="250" height="270"></iframe>

以下のコード例では、シアン色の円はベジェ曲線の最初の制御点を示しています。

マゼンタの円ではベジェ曲線の2つ目の制御点を示しています。

また、黄色の円ではベジェ曲線の終点座標を示しています。

```py
# runnable
import apysc as ap

ap.Stage(
    background_color=ap.Color("#333"),
    stage_width=250,
    stage_height=270,
    stage_elem_id="stage",
)

CONTROL_X1: float = 50
CONTROL_Y1: float = 25
CONTROL_X2: float = 200
CONTROL_Y2: float = 25
DEST_X: float = 200
DEST_Y: float = 200

path: ap.Path = ap.Path(
    path_data_list=[
        ap.PathMoveTo(x=50, y=200),
        ap.PathBezier3D(
            control_x1=CONTROL_X1,
            control_y1=CONTROL_Y1,
            control_x2=CONTROL_X2,
            control_y2=CONTROL_Y2,
            dest_x=DEST_X,
            dest_y=DEST_Y,
        ),
    ],
    line_color=ap.Color("#fff"),
    line_thickness=5,
)

RADIUS: int = 10
cyan_circle: ap.Circle = ap.Circle(
    x=CONTROL_X1,
    y=CONTROL_Y1,
    radius=RADIUS,
    fill_color=ap.Color("#0af"),
)

magenta_circle: ap.Circle = ap.Circle(
    x=CONTROL_X2,
    y=CONTROL_Y2,
    radius=RADIUS,
    fill_color=ap.Color("#f0a"),
)

yellow_circle: ap.Circle = ap.Circle(
    x=DEST_X,
    y=DEST_Y,
    radius=RADIUS,
    fill_color=ap.Color("#ff0"),
)

ap.save_overall_html(dest_dir_path="path_bezier_3d_basic_usage_2/")
```

<iframe src="static/path_bezier_3d_basic_usage_2/index.html" width="250" height="270"></iframe>

## 相対座標設定

コンストラクタの`relative`のオプション引数はその挙動を変更します。

例として、もしその引数にTrueを指定した場合座標は相対座標として設定されます。

デフォルト値はFalseとなっており、この設定では絶対座標として扱われます。

基準点は開始位置の座標となります。最初の制御点や2つ目の制御点ではありません。

以下のコード例ではrelativeの設定をしてベジェ曲線を描画しています。

```py
# runnable
import apysc as ap

ap.Stage(
    background_color=ap.Color("#333"),
    stage_width=250,
    stage_height=270,
    stage_elem_id="stage",
)

path: ap.Path = ap.Path(
    path_data_list=[
        ap.PathMoveTo(x=50, y=200),
        ap.PathBezier3D(
            control_x1=0,
            control_y1=-175,
            control_x2=150,
            control_y2=-175,
            dest_x=150,
            dest_y=0,
            relative=True,
        ),
    ],
    line_color=ap.Color("#0af"),
    line_thickness=5,
)

ap.save_overall_html(dest_dir_path="path_bezier_3d_relative/")
```

<iframe src="static/path_bezier_3d_relative/index.html" width="250" height="270"></iframe>

## PathBezier3D クラスのコンストラクタのAPI

<span class="inconspicuous-txt">特記事項: このAPIドキュメントはドキュメントビルド用のスクリプトによって自動で生成・同期されています。そのためもしかしたらこの節の内容は前節までの内容と重複している場合があります。</span>

**[インターフェイスの構造]** `__init__(self, control_x1: Union[float, apysc._type.number.Number], control_y1: Union[float, apysc._type.number.Number], control_x2: Union[float, apysc._type.number.Number], control_y2: Union[float, apysc._type.number.Number], dest_x: Union[float, apysc._type.number.Number], dest_y: Union[float, apysc._type.number.Number], *, relative: Union[bool, apysc._type.boolean.Boolean] = False, variable_name_suffix: str = '') -> None`<hr>

**[インターフェイス概要]**

SVGの3次のベジェ曲線（C）のパスデータのためのクラスです。<hr>

**[引数]**

- `control_x1`: float or Number
  - ベジェ曲線の最初の制御点のX座標。

- `control_y1`: float or Number
  - ベジェ曲線の最初の制御点のY座標。

- `control_x2`: float or Number
  - ベジェ曲線の2つ目の制御点のX座標。

- `control_y2`: float or Number
  - ベジェ曲線の2つ目の制御点のY座標。

- `dest_x`: float or Number
  - 終点のX座標。

- `dest_y`: float or Number
  - 終点のY座標。

- `relative`: bool or Boolean, default False
  - パスの座標が相対座標として扱うかもしくは絶対座標として扱うかどうかの真偽値。

- `variable_name_suffix`: str, default ""
  - JavaScript上の変数のサフィックスの設定です。この設定はJavaScriptのデバッグ時に役立つことがあります。

<hr>

**[コードサンプル]**

```py
>>> import apysc as ap
>>> stage: ap.Stage = ap.Stage()
>>> sprite: ap.Sprite = ap.Sprite()
>>> sprite.graphics.line_style(color=ap.Color("#fff"), thickness=3)
>>> path: ap.Path = sprite.graphics.draw_path(
...     path_data_list=[
...         ap.PathMoveTo(x=0, y=50),
...         ap.PathBezier3D(
...             control_x1=0,
...             control_y1=0,
...             control_x2=50,
...             control_y2=0,
...             dest_x=50,
...             dest_y=50,
...         ),
...         ap.PathBezier3DContinual(
...             control_x=100, control_y=100, dest_x=100, dest_y=50
...         ),
...     ]
... )
```

<hr>

**[関連資料]**

- [Path クラス](https://simon-ritchie.github.io/apysc/jp/jp_path.html)
- [Graphics クラスの draw_path インターフェイス](https://simon-ritchie.github.io/apysc/jp/jp_graphics_draw_path.html)

- [PathBezier3DContinual クラス](https://simon-ritchie.github.io/apysc/jp/jp_path_bezier_3d_continual.html)