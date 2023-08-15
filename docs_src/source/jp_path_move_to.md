<span class="inconspicuous-txt">※この翻訳ドキュメントはスクリプトによって出力・同期されています。内容が怪しそうな場合は<a href="https://github.com/simon-ritchie/apysc/issues" target="_blank">GitHubにissue</a>を追加したり[英語の原文](https://simon-ritchie.github.io/apysc/en/path_move_to.html)の確認をお願いします。</span>

# PathMoveTo クラス

このページでは`PathMoveTo`クラスについて説明します。

## クラス概要

`PathMoveTo`クラスはパスに新しい座標設定を追加するためのクラスです。

この設定は座標設定のみを行い、新しいベクターグラフィックスの追加などは行いません。

主にこの設定は`Path`クラスのコンストラクタと`draw_path`メソッドのインターフェイスで使用されます。

## 基本的な使い方

`PathMoveTo`クラスのコンストラクタは`x`と`y`の引数指定を必要とします。

`Path`クラスのコンストラクタもしくは`draw_path`メソッドのインターフェイスの`path_data_list`引数でそのインスタンスが必要とされます。

以下のコード例では`PathMoveTo`のインスタンスを使ってx=50, y=50の座標位置を設定した後にx=150, y=50の位置へ線を描画しています:

```py
# runnable
import apysc as ap

ap.Stage(
    background_color=ap.Color("#333"),
    stage_width=200,
    stage_height=100,
    stage_elem_id="stage",
)
path: ap.Path = ap.Path(
    path_data_list=[
        ap.PathMoveTo(x=50, y=50),
        ap.PathLineTo(x=150, y=50),
    ],
    line_color=ap.Color("#0af"),
    line_thickness=5,
)

ap.save_overall_html(dest_dir_path="path_move_to_basic_usage/")
```

<iframe src="static/path_move_to_basic_usage/index.html" width="200" height="100"></iframe>

## 相対座標設定

コンストラクタの`relative`のオプション引数はその挙動を変更します。

例として、もしその引数にTrueを指定した場合座標は相対座標として設定されます。

デフォルト値はFalseとなっており、この設定では絶対座標として扱われます。

以下のコード例ではrelativeの設定を行っており、相対的に50px下の位置に移動させています:

```py
# runnable
import apysc as ap

ap.Stage(
    background_color=ap.Color("#333"),
    stage_width=200,
    stage_height=200,
    stage_elem_id="stage",
)
path: ap.Path = ap.Path(
    path_data_list=[
        ap.PathMoveTo(x=50, y=50),
        ap.PathLineTo(x=150, y=50),
        ap.PathMoveTo(x=0, y=50, relative=True),
        ap.PathLineTo(x=0, y=50, relative=True),
    ],
    line_color=ap.Color("#0af"),
    line_thickness=5,
)

ap.save_overall_html(dest_dir_path="path_move_to_relative/")
```

<iframe src="static/path_move_to_relative/index.html" width="200" height="200"></iframe>

## PathMoveTo クラスのコンストラクタのAPI

<span class="inconspicuous-txt">特記事項: このAPIドキュメントはドキュメントビルド用のスクリプトによって自動で生成・同期されています。そのためもしかしたらこの節の内容は前節までの内容と重複している場合があります。</span>

**[インターフェイスの構造]** `__init__(self, x: Union[float, apysc._type.number.Number], y: Union[float, apysc._type.number.Number], *, relative: Union[bool, apysc._type.boolean.Boolean] = False, variable_name_suffix: str = '') -> None`<hr>

**[インターフェイス概要]**

SVGの特定座標への移動（M）のためのパスデータのクラスです。<hr>

**[引数]**

- `x`: float or Number
  - 終点のX座標。

- `y`: float or Number
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
>>> sprite.graphics.line_style(color=ap.Color("#fff"), thickness=3)
>>> path: ap.Path = sprite.graphics.draw_path(
...     path_data_list=[
...         ap.PathMoveTo(x=0, y=50),
...         ap.PathLineTo(x=50, y=50),
...     ]
... )
```

<hr>

**[関連資料]**

- [Path クラス](https://simon-ritchie.github.io/apysc/jp/jp_path.html)
- [Graphics クラスの draw_path インターフェイス](https://simon-ritchie.github.io/apysc/jp/jp_graphics_draw_path.html)