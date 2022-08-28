<span class="inconspicuous-txt">※この翻訳ドキュメントはスクリプトによって出力・同期されています。内容が怪しそうな場合は<a href="https://github.com/simon-ritchie/apysc/issues" target="_blank">GitHubにissue</a>を追加したり[英語の原文](https://simon-ritchie.github.io/apysc/en/path_line_to.html)の確認をお願いします。</span>

# PathLineTo クラス

このページでは`PathLineTo`クラスについて説明します。

## クラス概要

`PathLineTo`クラスは現在設定されている座標位置から新たな線のパスを描画します。

主にこの設定は`Path`クラスのコンストラクタと`draw_path`メソッドのインターフェイスで使用されます。

## 基本的な使い方

`PathLineTo`クラスのコンストラクタでは`x`と`y`の引数指定が必要となります。

`Path`クラスのコンストラクタもしくは`draw_path`メソッドのインターフェイスの`path_data_list`引数でそのインスタンスが必要とされます。

以下のコード例ではx=50, y=50の位置からx=150, y=50の位置に向けて`PathLineTo`のインスタンスを設定して線の描画設定を行っています:

```py
# runnable
import apysc as ap

ap.Stage(
    background_color="#333", stage_width=200, stage_height=100, stage_elem_id="stage"
)
path: ap.Path = ap.Path(
    path_data_list=[
        ap.PathMoveTo(x=50, y=50),
        ap.PathLineTo(x=150, y=50),
    ],
    line_color="#0af",
    line_thickness=5,
)

ap.save_overall_html(dest_dir_path="path_line_to_basic_usage/")
```

<iframe src="static/path_line_to_basic_usage/index.html" width="200" height="100"></iframe>

## 相対座標設定

コンストラクタの`relative`のオプション引数はその挙動を変更します。

例として、もしその引数にTrueを指定した場合座標は相対座標として設定されます。

デフォルト値はFalseとなっており、この設定では絶対座標として扱われます。

以下のコード例ではrelativeの設定を行い、現在の位置から50px下の位置に向けて線の描画を行っています:

```py
# runnable
import apysc as ap

ap.Stage(
    background_color="#333", stage_width=100, stage_height=150, stage_elem_id="stage"
)
path: ap.Path = ap.Path(
    path_data_list=[
        ap.PathMoveTo(x=50, y=50),
        ap.PathLineTo(x=0, y=50, relative=True),
    ],
    line_color="#0af",
    line_thickness=5,
)

ap.save_overall_html(dest_dir_path="path_line_to_relative/")
```

<iframe src="static/path_line_to_relative/index.html" width="100" height="150"></iframe>