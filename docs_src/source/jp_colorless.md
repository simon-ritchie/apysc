<span class="inconspicuous-txt">※この翻訳ドキュメントはスクリプトによって出力・同期されています。内容が怪しそうな場合は<a href="https://github.com/simon-ritchie/apysc/issues" target="_blank">GitHubにissue</a>を追加したり[英語の原文](https://simon-ritchie.github.io/apysc/en/colorless.html)の確認をお願いします。</span>

# COLORLESS 定数

このページでは `COLORLESS` 定数について説明します。

## 定数の概要

`COLORLESS`定数は無色の指定用の設定です。

もし各色関係の引数や属性にこの定数を設定した場合、`apysc`ライブラリではその色の指定箇所で色を削除します。

## 基本的な使い方

`COLORLESS`定数は`Color`クラスのサブクラスです。

そのため、色関係の引数や属性にこの定数を指定することができます。

以下の例では`fill_color`と`line_color`引数の各値に`COLORLESS`定数が指定されているため`apysc`ライブラリでは色を表示しません:

```py
# runnable
import apysc as ap

_ = ap.Stage(
    stage_width=150,
    stage_height=150,
    background_color=ap.Color("#333"),
    stage_elem_id="stage",
)
_ = ap.Rectangle(
    x=50,
    y=50,
    width=50,
    height=50,
    fill_color=ap.COLORLESS,
    line_color=ap.COLORLESS,
    line_thickness=3,
)

ap.save_overall_html(dest_dir_path="./colorless_basic_usage/")
```

<iframe src="static/colorless_basic_usage/index.html" width="150" height="150"></iframe>