<span class="inconspicuous-txt">※この翻訳ドキュメントはスクリプトによって出力・同期されています。内容が怪しそうな場合は<a href="https://github.com/simon-ritchie/apysc/issues" target="_blank">GitHubにissue</a>を追加したり[英語の原文](https://simon-ritchie.github.io/apysc/en/color_from_rgb.html)の確認をお願いします。</span>

# Color クラスの from_rgb クラスメソッド

このページでは`Color`クラスの`from_rgb`クラスメソッドについて説明します。

## クラスメソッド概要

`from_rgs`クラスメソッドは赤緑青の3色の指定から新たな色のインスタンスを作成します（0～255の8bitの正の整数の範囲を受け付けます）。

## 基本的な使い方

`from_rgb`クラスメソッドは`red`、`green`、`blue`の各引数を必要とします（`int`もしくは`ap.Int`型の値）。

このクラスメソッドは新たな色のインスタンスを返します。

```py
# runnable

import apysc as ap

ap.Stage(
    stage_width=350,
    stage_height=150,
    background_color=ap.Color("#333"),
    stage_elem_id="stage",
)

black_color: ap.Color = ap.Color.from_rgb(red=0, green=0, blue=0)
black_rectangle: ap.Rectangle = ap.Rectangle(
    x=50,
    y=50,
    width=50,
    height=50,
    fill_color=black_color,
)

white_color: ap.Color = ap.Color.from_rgb(red=255, green=255, blue=255)
white_rectangle: ap.Rectangle = ap.Rectangle(
    x=150,
    y=50,
    width=50,
    height=50,
    fill_color=white_color,
)

cyan_color: ap.Color = ap.Color.from_rgb(red=0, green=128, blue=255)
cyan_rectangle: ap.Rectangle = ap.Rectangle(
    x=250,
    y=50,
    width=50,
    height=50,
    fill_color=cyan_color,
)

ap.save_overall_html(dest_dir_path="color_from_rgb_basic_usage/")
```

<iframe src="static/color_from_rgb_basic_usage/index.html" width="350" height="150"></iframe>

## from_rgb クラスメソッドのAPI

<span class="inconspicuous-txt">特記事項: このAPIドキュメントはドキュメントビルド用のスクリプトによって自動で生成・同期されています。そのためもしかしたらこの節の内容は前節までの内容と重複している場合があります。</span>

**[インターフェイスの構造]** `from_rgb(*, red: Union[int, apysc._type.int.Int], green: Union[int, apysc._type.int.Int], blue: Union[int, apysc._type.int.Int], variable_name_suffix: str = '') -> 'Color'`<hr>

**[インターフェイス概要]**

RGB（赤、緑、青）の値から色のインスタンスを生成します。<hr>

**[引数]**

- `red`: Union[int, Int]
  - 赤色の値（0～255）。

- `green`: Union[int, Int]
  - 緑色の値（0～255）。

- `blue`: Union[int, Int]
  - 青色の値（0～255）。

- `variable_name_suffix`: str, default ''
  - JavaScript上の変数のサフィックスの設定です。この設定はJavaScriptのデバッグ時に役立つことがあります。

<hr>

**[返却値]**

- `color`: Color
  - 作成された色のインスタンス。

<hr>

**[コードサンプル]**

```py
>>> import apysc as ap
>>> color: ap.Color = ap.Color.from_rgb(red=0, green=255, blue=0)
>>> color
Color("#00FF00")
```