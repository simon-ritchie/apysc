<span class="inconspicuous-txt">※この翻訳ドキュメントはスクリプトによって出力・同期されています。内容が怪しそうな場合は<a href="https://github.com/simon-ritchie/apysc/issues" target="_blank">GitHubにissue</a>を追加したり[英語の原文](https://simon-ritchie.github.io/apysc/en/path_vertical.html)の確認をお願いします。</span>

# PathVertical クラス

このページでは`PathVertical`クラスについて説明します。

## クラス概要

`PathVertical`クラスはパス上に新しい垂直の直線の設定を追加するためのクラスです。

この設定はもし垂直方向の線の描画のみが必要で水平方向の座標設定が不要な場合にコードの記述をシンプルにします。

主にこの設定は`Path`クラスのコンストラクタと`draw_path`メソッドのインターフェイスで使用されます。

## 基本的な使い方

`PathVertical`クラスのコンストラクタでは`y`の引数指定のみ必要とします。

`Path`クラスのコンストラクタもしくは`draw_path`メソッドのインターフェイスの`path_data_list`引数でそのインスタンスが必要とされます。

以下のコード例ではy=50の座標からy=150の座標に向けて垂直の直線を描画しています:

```py
# runnable
import apysc as ap

ap.Stage(
    background_color="#333", stage_width=100, stage_height=200, stage_elem_id="stage"
)
path: ap.Path = ap.Path(
    path_data_list=[
        ap.PathMoveTo(x=50, y=50),
        ap.PathVertical(y=150),
    ],
    line_color="#0af",
    line_thickness=5,
)

ap.save_overall_html(dest_dir_path="path_vertical_basic_usage/")
```

<iframe src="static/path_vertical_basic_usage/index.html" width="100" height="200"></iframe>

## 相対座標設定

コンストラクタの`relative`のオプション引数はその挙動を変更します。

例として、もしその引数にTrueを指定した場合座標は相対座標として設定されます。

デフォルト値はFalseとなっており、この設定では絶対座標として扱われます。

以下のコード例ではrelativeの設定をして現在の座標から垂直方向に50px下の位置に直線を描画しています:

```py
# runnable
import apysc as ap

ap.Stage(
    background_color="#333", stage_width=100, stage_height=150, stage_elem_id="stage"
)
path: ap.Path = ap.Path(
    path_data_list=[
        ap.PathMoveTo(x=50, y=50),
        ap.PathVertical(y=50, relative=True),
    ],
    line_color="#0af",
    line_thickness=5,
)

ap.save_overall_html(dest_dir_path="path_vertical_relative/")
```

<iframe src="static/path_vertical_relative/index.html" width="100" height="150"></iframe>

## PathVertical クラスのコンストラクタのAPI

<span class="inconspicuous-txt">特記事項: このAPIドキュメントはドキュメントビルド用のスクリプトによって自動で生成・同期されています。そのためもしかしたらこの節の内容は前節までの内容と重複している場合があります。</span>

**[インターフェイスの構造]** `__init__(self, y: Union[int, apysc._type.int.Int], *, relative: Union[bool, apysc._type.boolean.Boolean] = False, variable_name_suffix: str = '') -> None`<hr>

**[インターフェイス概要]** SVGの垂直方向の直線(V)の描画設定用のデータのクラスです。<hr>

**[引数]**

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
...         ap.PathVertical(y=100),
...     ]
... )
```

<hr>

**[関連資料]**

- [Path クラス](https://simon-ritchie.github.io/apysc/en/jp_path.html)
- [Graphics クラスの draw_path インターフェイス](https://simon-ritchie.github.io/apysc/en/jp_graphics_draw_path.html)