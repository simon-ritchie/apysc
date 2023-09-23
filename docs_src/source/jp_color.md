<span class="inconspicuous-txt">※この翻訳ドキュメントはスクリプトによって出力・同期されています。内容が怪しそうな場合は<a href="https://github.com/simon-ritchie/apysc/issues" target="_blank">GitHubにissue</a>を追加したり[英語の原文](https://simon-ritchie.github.io/apysc/en/color.html)の確認をお願いします。</span>

# Color クラス

このページでは`Color`クラスについて説明します。

## クラス概要

`Color`クラスの色の設定を扱います。

色の設定、例えば`fill_color`や`line_color`などの引数や属性はこの値を必要とします。

## 基本的な使い方

`Color`クラスのコンストラクタでは例えば`#00aaff`などの16進数のカラーコードを必要とします。

```py
# runnable
import apysc as ap

stage: ap.Stage = ap.Stage(
    stage_width=250,
    stage_height=150,
    background_color=ap.Color("#333"),
    stage_elem_id="stage",
)

left_rectangle: ap.Rectangle = ap.Rectangle(
    x=50,
    y=50,
    width=50,
    height=50,
    fill_color=ap.Color("#00aaff"),
)

right_rectangle: ap.Rectangle = ap.Rectangle(
    x=150,
    y=50,
    width=50,
    height=50,
    line_color=ap.Color("#ffffff"),
    line_thickness=3,
)

ap.save_overall_html(dest_dir_path="./color_basic_usage/")
```

<iframe src="static/color_basic_usage/index.html" width="250" height="150"></iframe>

## 受け付けられる16進数のカラーコード

以下のようなカラーコードが受け付けられます:

- `#00aaff`などの6文字による指定。
- `#0af`などの3文字による指定（これは`#00aaff`と同じ値として扱われます）。

- `#5`などの1文字による指定（これは`000005`と同じ値として扱われます）。
- `0af`などの`#`記号を省略した指定（これは`#00aaff`と同じ値として扱われます）。

- `COLORLESS`定数（この設定は色の設定を削除します）。

## Color クラスのコンストラクタのAPI

<span class="inconspicuous-txt">特記事項: このAPIドキュメントはドキュメントビルド用のスクリプトによって自動で生成・同期されています。そのためもしかしたらこの節の内容は前節までの内容と重複している場合があります。</span>

**[インターフェイスの構造]** `__init__(self, value: ~_StrOrString, *, variable_name_suffix: str = '') -> None`<hr>

**[インターフェイス概要]**

色のクラスの実装です。<hr>

**[引数]**

- `value`: str or String
  - 16進数の色の文字列（例 : '#000000'）。

- `variable_name_suffix`: str, default ''
  - JavaScript上の変数のサフィックスの設定です。この設定はJavaScriptのデバッグ時に役立つことがあります。

<hr>

**[コードサンプル]**

```py
>>> import apysc as ap
>>> color: ap.Color = ap.Color("#0af")
>>> color
Color("#00aaff")

>>> color = ap.Color("#ffffff")
>>> color
Color("#ffffff")
```

<hr>

**[関連資料]**

- [Colors クラス](https://simon-ritchie.github.io/apysc/jp/jp_colors.html)
- [MaterialDesignColors クラス](https://simon-ritchie.github.io/apysc/jp/jp_material_design_colors.html)

- [COLORLESS 定数](https://simon-ritchie.github.io/apysc/jp/jp_colorless.html)