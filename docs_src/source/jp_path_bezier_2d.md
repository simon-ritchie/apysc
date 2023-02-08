<span class="inconspicuous-txt">※この翻訳ドキュメントはスクリプトによって出力・同期されています。内容が怪しそうな場合は<a href="https://github.com/simon-ritchie/apysc/issues" target="_blank">GitHubにissue</a>を追加したり[英語の原文](https://simon-ritchie.github.io/apysc/en/path_bezier_2d.html)の確認をお願いします。</span>

# PathBezier2D クラス

このページでは`PathBezier2D`クラスについて説明します。

## クラス概要

`PathBezier2D`クラスはパスへ2次のベジェ曲線を設定するためのクラスです。

主にこの設定は`Path`クラスのコンストラクタと`draw_path`メソッドのインターフェイスで使用されます。

## 基本的な使い方

`PathBezier2D`クラスのコンストラクタでは`control_x`、`control_y`、`dest_x`、`dest_y`の各パラメーターが必要になります。

`control_x`と`control_y`はベジェ曲線の制御点の座標となります。

`dest_x`と`dest_y`はベジェ曲線の終点座標の指定となります。

```py
# runnable
import apysc as ap

ap.Stage(
    background_color="#333", stage_width=200, stage_height=150, stage_elem_id="stage"
)
path: ap.Path = ap.Path(
    path_data_list=[
        ap.PathMoveTo(x=50, y=100),
        ap.PathBezier2D(
            control_x=100,
            control_y=25,
            dest_x=150,
            dest_y=100,
        ),
    ],
    line_color="#0af",
    line_thickness=5,
)

ap.save_overall_html(dest_dir_path="path_bezier_2d_basic_usage_1/")
```

<iframe src="static/path_bezier_2d_basic_usage_1/index.html" width="200" height="150"></iframe>

以下のコード例ではマゼンタ色の円で制御点の座標を示しています。

同様に、シアンの色では終点座標を示しています。

```py
# runnable
import apysc as ap

ap.Stage(
    background_color="#333", stage_width=200, stage_height=150, stage_elem_id="stage"
)

CONTROL_X: float = 100
CONTROL_Y: float = 25
DEST_X: float = 150
DEST_Y: float = 100
path: ap.Path = ap.Path(
    path_data_list=[
        ap.PathMoveTo(x=50, y=100),
        ap.PathBezier2D(
            control_x=CONTROL_X,
            control_y=CONTROL_Y,
            dest_x=DEST_X,
            dest_y=DEST_Y,
        ),
    ],
    line_color="#fff",
    line_thickness=5,
)

RADIUS: int = 5
magenta_circle: ap.Circle = ap.Circle(
    x=CONTROL_X,
    y=CONTROL_Y,
    radius=RADIUS,
    fill_color="#f0a",
)
cyan_circle: ap.Circle = ap.Circle(
    x=DEST_X,
    y=DEST_Y,
    radius=RADIUS,
    fill_color="#0af",
)

ap.save_overall_html(dest_dir_path="path_bezier_2d_basic_usage_2/")
```

<iframe src="static/path_bezier_2d_basic_usage_2/index.html" width="200" height="150"></iframe>

## 相対座標設定

コンストラクタの`relative`のオプション引数はその挙動を変更します。

例として、もしその引数にTrueを指定した場合座標は相対座標として設定されます。

デフォルト値はFalseとなっており、この設定では絶対座標として扱われます。

基準となる座標は制御点などではなく開始点となります。

以下のコード例ではrelativeの設定を行いつつベジェ曲線を描画しています。

`relative`の設定を使用しているため`control_y`のパラメーターは負の値となり、`dest_y`のパラメーターは0になっています:

```py
# runnable
import apysc as ap

ap.Stage(
    background_color="#333", stage_width=200, stage_height=150, stage_elem_id="stage"
)

path: ap.Path = ap.Path(
    path_data_list=[
        ap.PathMoveTo(x=50, y=100),
        ap.PathBezier2D(
            control_x=50, control_y=-75, dest_x=100, dest_y=0, relative=True
        ),
    ],
    line_color="#0af",
    line_thickness=5,
)

ap.save_overall_html(dest_dir_path="path_bezier_2d_relative/")
```

<iframe src="static/path_bezier_2d_relative/index.html" width="200" height="150"></iframe>

## PathBezier2D クラスのコンストラクタのAPI

<span class="inconspicuous-txt">特記事項: このAPIドキュメントはドキュメントビルド用のスクリプトによって自動で生成・同期されています。そのためもしかしたらこの節の内容は前節までの内容と重複している場合があります。</span>

**[インターフェイスの構造]** `__init__(self, control_x: Union[float, apysc._type.number.Number], control_y: Union[float, apysc._type.number.Number], dest_x: Union[float, apysc._type.number.Number], dest_y: Union[float, apysc._type.number.Number], *, relative: Union[bool, apysc._type.boolean.Boolean] = False, variable_name_suffix: str = '') -> None`<hr>

**[インターフェイス概要]**

SVGの2次のベジェ曲線（Q）のデータを設定するためのクラスです。<hr>

**[引数]**

- `control_x`: float or Number
  - ベジェ曲線の制御点のX座標。

- `control_y`: float or Number
  - ベジェ曲線の制御点のY座標。

- `dest_x`: float or Number
  - 終点のX座標。

- `dest_y`: float or Number
  - 終点のY座標。

- `relative`: bool or Boolean, default False
  - パスの座標が相対座標として扱うかもしくは絶対座標として扱うかどうかの真偽値。

- `variable_name_suffix`: str, default ''
  - JavaScript上の変数のサフィックスの設定です。この設定はJavaScriptのデバッグ時に役立つことがあります。

<hr>

**[コードサンプル]**

```py
>>> import apysc as ap
>>> stage: ap.Stage = ap.Stage()
>>> sprite: ap.Sprite = ap.Sprite()
>>> sprite.graphics.line_style(color="#fff", thickness=3)
>>> path: ap.Path = sprite.graphics.draw_path(
...     path_data_list=[
...         ap.PathMoveTo(x=0, y=50),
...         ap.PathBezier2D(control_x=50, control_y=0, dest_x=100, dest_y=50),
...     ]
... )
```

<hr>

**[関連資料]**

- [Path クラス](https://simon-ritchie.github.io/apysc/jp/jp_path.html)
- [Graphics クラスの draw_path インターフェイス](https://simon-ritchie.github.io/apysc/jp/jp_graphics_draw_path.html)

- [PathBezier2DContinual クラス](https://simon-ritchie.github.io/apysc/jp/jp_path_bezier_2d_continual.html)