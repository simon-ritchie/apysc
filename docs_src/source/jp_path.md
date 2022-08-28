<span class="inconspicuous-txt">※この翻訳ドキュメントはスクリプトによって出力・同期されています。内容が怪しそうな場合は<a href="https://github.com/simon-ritchie/apysc/issues" target="_blank">GitHubにissue</a>を追加したり[英語の原文](https://simon-ritchie.github.io/apysc/en/path.html)の確認をお願いします。</span>

# Path クラス

このページでは`Path`クラスについて説明します。

## クラス概要

`Path`クラスはパスのベクターグラフィックスのオブジェクトを生成します。

## 基本的な使い方

`Path`

コンストラクタは`fill_color`や`line_color`などのスタイル設定用の引数も受け付けます。

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
    line_color="0af",
    line_thickness=5,
)

ap.save_overall_html(dest_dir_path="path_basic_usage/")
```

<iframe src="static/path_basic_usage/index.html" width="200" height="100"></iframe>