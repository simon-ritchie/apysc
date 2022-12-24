<span class="inconspicuous-txt">※この翻訳ドキュメントはスクリプトによって出力・同期されています。内容が怪しそうな場合は<a href="https://github.com/simon-ritchie/apysc/issues" target="_blank">GitHubにissue</a>を追加したり[英語の原文](https://simon-ritchie.github.io/apysc/en/path_bezier_3d_continual.html)の確認をお願いします。</span>

# PathBezier3DContinual クラス

このページでは`PathBezier3DContinual`クラスについて説明しるます。

## クラス概要

`PathBezier3DContinual`クラスはパス上に連続した3次ベジェ曲線を設定するためのクラスです。

この設定は制御点に線対称位置を使用することで滑らかな曲線を描画します。

主にこの設定は`Path`クラスのコンストラクタと`draw_path`メソッドのインターフェイスで使用されます。

## 基本的な使い方

`PathBezier3DContinual`クラスのコンストラクタでは`control_x`、`control_y`、`dest_x`、`dest_y`の各引数の指定が必要になります。

`control_x`と`control_y`はベジェ曲線の2つ目の制御点の位置となります。

ベジェ曲線の2つ目の制御点の線対称の位置は`PathBezier3DContinual`クラスの1つ目の制御点の位置として設定されます。

そのため`PathBezier3DContinual`クラスのコンストラクタには1つ目の制御点の位置の指定の引数は存在しません。

`dest_x`と`dest_y`引数はベジェ曲線の終点位置の指定となります。

`PathBezier3DContinual`クラスには`PathBezier3D`や`PathBezier3DContinual`クラスの直後でのみ使用できるという制限が存在します。

```py
# runnable
import apysc as ap

ap.Stage(
    background_color="#333", stage_width=400, stage_height=420, stage_elem_id="stage"
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
        ap.PathBezier3DContinual(
            control_x=350,
            control_y=375,
            dest_x=350,
            dest_y=200,
        ),
    ],
    line_color="#0af",
    line_thickness=5,
)

ap.save_overall_html(dest_dir_path="path_bezier_3d_continual_basic_usage_1/")
```

<iframe src="static/path_bezier_3d_continual_basic_usage_1/index.html" width="400" height="420"></iframe>

以下のコード例ではシアンの円は制御点（`control_x`と`control_y`）の位置を示し、マゼンタの円では終点の位置（`dest_x`と`dest_y`）を示します。

```py
# runnable
import apysc as ap

ap.Stage(
    background_color="#333", stage_width=400, stage_height=420, stage_elem_id="stage"
)

CONTROL_X: int = 350
CONTROL_Y: int = 375
DEST_X: int = 350
DEST_Y: int = 200

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
        ap.PathBezier3DContinual(
            control_x=CONTROL_X,
            control_y=CONTROL_Y,
            dest_x=DEST_X,
            dest_y=DEST_Y,
        ),
    ],
    line_color="#fff",
    line_thickness=5,
)

RADIUS: int = 10

cyan_circle: ap.Circle = ap.Circle(
    x=CONTROL_X,
    y=CONTROL_Y,
    radius=RADIUS,
    fill_color="#0af",
)

magenta_circle: ap.Circle = ap.Circle(
    x=DEST_X,
    y=DEST_Y,
    radius=RADIUS,
    fill_color="#f0a",
)

ap.save_overall_html(dest_dir_path="path_bezier_3d_continual_basic_usage_2/")
```

<iframe src="static/path_bezier_3d_continual_basic_usage_2/index.html" width="400" height="420"></iframe>

## 相対座標設定

コンストラクタの`relative`のオプション引数はその挙動を変更します。

例として、もしその引数にTrueを指定した場合座標は相対座標として設定されます。

デフォルト値はFalseとなっており、この設定では絶対座標として扱われます。

基準となる位置は制御点などではなく始点の位置となります。

```py
# runnable
import apysc as ap

ap.Stage(
    background_color="#333", stage_width=400, stage_height=420, stage_elem_id="stage"
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
        ap.PathBezier3DContinual(
            control_x=150,
            control_y=175,
            dest_x=150,
            dest_y=0,
            relative=True,
        ),
    ],
    line_color="#0af",
    line_thickness=5,
)

ap.save_overall_html(dest_dir_path="path_bezier_3d_continual_relative/")
```

<iframe src="static/path_bezier_3d_continual_relative/index.html" width="400" height="420"></iframe>

## PathBezier3DContinual クラスのコンストラクタのAPI

<span class="inconspicuous-txt">特記事項: このAPIドキュメントはドキュメントビルド用のスクリプトによって自動で生成・同期されています。そのためもしかしたらこの節の内容は前節までの内容と重複している場合があります。</span>

**[インターフェイスの構造]** `__init__(self, control_x: Union[int, apysc._type.int.Int], control_y: Union[int, apysc._type.int.Int], dest_x: Union[int, apysc._type.int.Int], dest_y: Union[int, apysc._type.int.Int], *, relative: Union[bool, apysc._type.boolean.Boolean] = False, variable_name_suffix: str = '') -> None`<hr>

**[インターフェイス概要]**

SVGの連続した3次ベジェ曲線（S）のためのパスデータのクラスです。<hr>

**[引数]**

- `control_x`: Int or int
  - ベジェ曲線の制御点のX座標。

- `control_y`: Int or int
  - ベジェ曲線の制御点のY座標。

- `dest_x`: Int or int
  - 終点のX座標。

- `dest_y`: Int or int
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

- [PathBezier3D クラス](https://simon-ritchie.github.io/apysc/jp/jp_path_bezier_3d.html)