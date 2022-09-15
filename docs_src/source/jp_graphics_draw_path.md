<span class="inconspicuous-txt">※この翻訳ドキュメントはスクリプトによって出力・同期されています。内容が怪しそうな場合は<a href="https://github.com/simon-ritchie/apysc/issues" target="_blank">GitHubにissue</a>を追加したり[英語の原文](https://simon-ritchie.github.io/apysc/en/graphics_draw_path.html)の確認をお願いします。</span>

# Graphics クラスの draw_path インターフェイス

このページでは`Graphics`クラスの`draw_path`インターフェイスについて説明します。

## インターフェイス概要

`draw_path`インターフェイスはベクターグラフィックスのパスを描画します。

## 基本的な使い方

`draw_path`インターフェイスは`path_data_list`引数の指定を必要とします。

`path_data_list`引数は`PathLineTo`や`PathBezier2D`などのパスデータの配列となります。

```py
# runnable
import apysc as ap

ap.Stage(
    background_color="#333", stage_width=300, stage_height=150, stage_elem_id="stage"
)
sprite: ap.Sprite = ap.Sprite()
sprite.graphics.line_style(color="#0af", thickness=5)
path: ap.Path = sprite.graphics.draw_path(
    path_data_list=[
        ap.PathMoveTo(x=50, y=100),
        ap.PathLineTo(x=100, y=100),
        ap.PathLineTo(x=150, y=50),
        ap.PathBezier2D(
            control_x=200,
            control_y=100,
            dest_x=250,
            dest_y=50,
        ),
    ],
)

ap.save_overall_html(dest_dir_path="graphics_draw_path_basic_usage/")
```

<iframe src="static/graphics_draw_path_basic_usage/index.html" width="300" height="150"></iframe>

## 関連資料

- [Path クラス](jp_path.md)
- [PathMoveTo クラス](jp_path_move_to.md)

- [PathLineTo クラス](jp_path_line_to.md)
- [PathHorizontal クラス](jp_path_horizontal.md)

- [PathVertical クラス](jp_path_vertical.md)
- [PathClose クラス](jp_path_close.md)

- [PathBezier2D クラス](jp_path_bezier_2d.md)
- [PathBezier2DContinual クラス](jp_path_bezier_3d.md)

- [PathBezier3DContinual クラス](jp_path_bezier_3d_continual.md)

## draw_path API

<span class="inconspicuous-txt">特記事項: このAPIドキュメントはドキュメントビルド用のスクリプトによって自動で生成・同期されています。そのためもしかしたらこの節の内容は前節までの内容と重複している場合があります。</span>

**[インターフェイスの構造]** `draw_path(self, *, path_data_list: List[apysc._geom.path_data_base.PathDataBase], variable_name_suffix: str = '') -> '_path.Path'`<hr>

**[インターフェイス概要]** パスのベクターグラフィックスを描画します。<hr>

**[引数]**

- `path_data_list`: list of PathDataBase
  - ap.PathData.MoveToなどの対象のパスデータの設定のリスト。

- `variable_name_suffix`: str, default ''
  - JavaScript上の変数のサフィックスの設定です。この設定はJavaScriptのデバッグ時に役立つことがあります。

<hr>

**[返却値]**

- `path`: Path
  - 作成されたパスのグラフィックスのインスタンス。

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
- [PathMoveTo クラス](https://simon-ritchie.github.io/apysc/jp/jp_path_move_to.html)

- [PathLineTo クラス](https://simon-ritchie.github.io/apysc/jp/jp_path_line_to.html)
- [PathHorizontal クラス](https://simon-ritchie.github.io/apysc/jp/jp_path_horizontal.html)

- [PathVertical クラス](https://simon-ritchie.github.io/apysc/jp/jp_path_vertical.html)
- [PathClose クラス](https://simon-ritchie.github.io/apysc/jp/jp_path_close.html)

- [PathBezier2D クラス](https://simon-ritchie.github.io/apysc/jp/jp_path_bezier_2d.html)
- [PathBezier2DContinual クラス](https://simon-ritchie.github.io/apysc/jp/jp_path_bezier_2d_continual.html)

- [PathBezier3D クラス](https://simon-ritchie.github.io/apysc/jp/jp_path_bezier_3d.html)
- [PathBezier3DContinual クラス](https://simon-ritchie.github.io/apysc/jp/jp_path_bezier_3d_continual.html)