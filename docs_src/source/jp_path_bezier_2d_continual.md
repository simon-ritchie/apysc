<span class="inconspicuous-txt">※この翻訳ドキュメントはスクリプトによって出力・同期されています。内容が怪しそうな場合は<a href="https://github.com/simon-ritchie/apysc/issues" target="_blank">GitHubにissue</a>を追加したり[英語の原文](https://simon-ritchie.github.io/apysc/en/path_bezier_2d_continual.html)の確認をお願いします。</span>

# PathBezier2DContinual クラス

このページでは`PathBezier2DContinual`クラスについて説明します。

## クラス概要

PathBezier2DContinual`クラスはパスに連続した2次元のベジェ曲線を設定するためのクラスです。

この設定は線対称な位置の制御点を使うことで滑らかな曲線を描画します。

主にこの設定は`Path`クラスのコンストラクタと`draw_path`メソッドのインターフェイスで使用されます。

## 基本的な使い方

`PathBezier2DContinual`クラスのコンストラクタは`x`と`y`の引数を必要とします。

これらの座標はベジェ曲線の終点座標の指定となります。

`PathBezier2DContinual`クラスは`PathBezier2D`もしくは`PathBezier2DContinual`クラスの直後でのみ使用することができるという制限があります。

```py
# runnable
import apysc as ap

ap.Stage(
    background_color="#333", stage_width=400, stage_height=200, stage_elem_id="stage"
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
        ap.PathBezier2DContinual(
            x=250,
            y=100,
        ),
        ap.PathBezier2DContinual(
            x=350,
            y=100,
        ),
    ],
    line_color="#0af",
    line_thickness=5,
)

ap.save_overall_html(dest_dir_path="path_bezier_2d_continual_basic_usage/")
```

<iframe src="static/path_bezier_2d_continual_basic_usage/index.html" width="400" height="200"></iframe>

## 相対座標設定

コンストラクタの`relative`のオプション引数はその挙動を変更します。

例として、もしその引数にTrueを指定した場合座標は相対座標として設定されます。

デフォルト値はFalseとなっており、この設定では絶対座標として扱われます。

```py
# runnable
import apysc as ap

ap.Stage(
    background_color="#333", stage_width=400, stage_height=200, stage_elem_id="stage"
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
        ap.PathBezier2DContinual(
            x=100,
            y=0,
            relative=True,
        ),
        ap.PathBezier2DContinual(
            x=100,
            y=0,
            relative=True,
        ),
    ],
    line_color="#0af",
    line_thickness=5,
)

ap.save_overall_html(dest_dir_path="path_bezier_2d_continual_relative/")
```

<iframe src="static/path_bezier_2d_continual_relative/index.html" width="400" height="200"></iframe>

## PathBezier2DContinual クラスのコンストラクタのAPI

<span class="inconspicuous-txt">特記事項: このAPIドキュメントはドキュメントビルド用のスクリプトによって自動で生成・同期されています。そのためもしかしたらこの節の内容は前節までの内容と重複している場合があります。</span>

**[インターフェイスの構造]** `__init__(self, x: Union[int, apysc._type.int.Int], y: Union[int, apysc._type.int.Int], *, relative: Union[bool, apysc._type.boolean.Boolean] = False, variable_name_suffix: str = '') -> None`<hr>

**[インターフェイス概要]**

SVGの連続した2次元のベジェ曲線のデータ設定用のクラスです。<hr>

**[引数]**

- `x`: Int or int
  - 終点のX座標。

- `y`: Int or int
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
...         ap.PathBezier2DContinual(x=150, y=50),
...     ]
... )
```

<hr>

**[関連資料]**

- [Path クラス](https://simon-ritchie.github.io/apysc/jp/jp_path.html)
- [Graphics クラスの draw_path インターフェイス](https://simon-ritchie.github.io/apysc/jp/jp_graphics_draw_path.html)

- [PathBezier2D クラス](https://simon-ritchie.github.io/apysc/jp/jp_path_bezier_2d.html)