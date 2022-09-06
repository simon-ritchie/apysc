<span class="inconspicuous-txt">※この翻訳ドキュメントはスクリプトによって出力・同期されています。内容が怪しそうな場合は<a href="https://github.com/simon-ritchie/apysc/issues" target="_blank">GitHubにissue</a>を追加したり[英語の原文](https://simon-ritchie.github.io/apysc/en/path_close.html)の確認をお願いします。</span>

# PathClose クラス

このページでは`PathClose`クラスについて説明します。

## クラス概要

`PathClose`クラスはパスを閉じる設定のためのクラスです。

もしもパスの始点と終点が繋がっていない場合、この設定はこれらの座標を接続します。

主にこの設定は`Path`クラスのコンストラクタと`draw_path`メソッドのインターフェイスで使用されます。

## 基本的な使い方

`PathClose`クラスのコンストラクタは引数を必要としません。

`Path`クラスのコンストラクタもしくは`draw_path`メソッドのインターフェイスの`path_data_list`引数でそのインスタンスが必要とされます。

以下のコード例では、左側のパスのグラフィックスは`Close`クラスの設定を使用していません。

逆に右側のパスのグラフィックスでは`Close`クラスの設定を使用しており、始点と終点の座標が接続されています:

```py
# runnable
import apysc as ap

ap.Stage(
    background_color="#333", stage_width=250, stage_height=150, stage_elem_id="stage"
)
left_path: ap.Path = ap.Path(
    path_data_list=[
        ap.PathMoveTo(x=75, y=50),
        ap.PathLineTo(x=50, y=100),
        ap.PathLineTo(x=100, y=100),
    ],
    line_color="#0af",
    line_thickness=5,
)

right_path: ap.Path = ap.Path(
    path_data_list=[
        ap.PathMoveTo(x=175, y=50),
        ap.PathLineTo(x=150, y=100),
        ap.PathLineTo(x=200, y=100),
        ap.PathClose(),
    ],
    line_color="#0af",
    line_thickness=5,
)

ap.save_overall_html(dest_dir_path="path_close_basic_usage/")
```

<iframe src="static/path_close_basic_usage/index.html" width="250" height="150"></iframe>

## PathClose クラスのコンストラクタのAPI

<span class="inconspicuous-txt">特記事項: このAPIドキュメントはドキュメントビルド用のスクリプトによって自動で生成・同期されています。そのためもしかしたらこの節の内容は前節までの内容と重複している場合があります。</span>

**[インターフェイスの構造]** `__init__(self) -> None`<hr>

**[インターフェイス概要]** SVGのパスを閉じる指定（Z）のためのデータのクラスです。<hr>

**[コードサンプル]**

```py
>>> import apysc as ap
>>> stage: ap.Stage = ap.Stage()
>>> sprite: ap.Sprite = ap.Sprite()
>>> sprite.graphics.line_style(color="#fff", thickness=3)
>>> path: ap.Path = sprite.graphics.draw_path(
...     path_data_list=[
...         ap.PathMoveTo(x=0, y=00),
...         ap.PathLineTo(x=50, y=0),
...         ap.PathLineTo(x=50, y=50),
...         ap.PathClose(),
...     ]
... )
```

<hr>

**[関連資料]**

- [Path クラス](https://simon-ritchie.github.io/apysc/en/jp_path.html)
- [Graphics クラスの draw_path インターフェイス](https://simon-ritchie.github.io/apysc/en/jp_graphics_draw_path.html)