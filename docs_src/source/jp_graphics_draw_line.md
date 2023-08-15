<span class="inconspicuous-txt">※この翻訳ドキュメントはスクリプトによって出力・同期されています。内容が怪しそうな場合は<a href="https://github.com/simon-ritchie/apysc/issues" target="_blank">GitHubにissue</a>を追加したり[英語の原文](https://simon-ritchie.github.io/apysc/en/graphics_draw_line.html)の確認をお願いします。</span>

# Graphics クラスの draw_line インターフェイス

このページでは`Graphics`クラスの`draw_line`メソッドのインターフェイスについて説明します。

## インターフェイス概要

`draw_line`インターフェイスはシンプルな直線のグラフィックスを描画します。このインターフェイスは`dot_setting`、`dash_setting`、`round_dot_setting`、`dash_dot_setting`などの引数や属性の設定を無視します。

## 基本的な使い方

`draw_line`インターフェイスは`x_start`（線の開始位置のX座標）、`y_start`（線の開始位置のY座標）、`x_end`（線の終了位置のX座標）、`y_end`（線の終了位置のY座標）の各引数を必要とします。

```py
# runnable
import apysc as ap

ap.Stage(
    background_color=ap.Color("#333"),
    stage_width=200,
    stage_height=100,
    stage_elem_id="stage",
)
sprite: ap.Sprite = ap.Sprite()

sprite.graphics.line_style(color=ap.Color("#0af"), thickness=5)
sprite.graphics.draw_line(x_start=50, y_start=50, x_end=150, y_end=50)

ap.save_overall_html(dest_dir_path="graphics_draw_line_basic_usage/")
```

<iframe src="static/graphics_draw_line_basic_usage/index.html" width="200" height=100></iframe>

## 無視される線のスタイル設定

このインターフェイスはインターフェイスのシンプルさのために`dot_setting`、`dash_setting`、`round_dot_setting`、`dash_dot_setting`の各設定を無視します。もしもこれらのスタイル設定が必要な場合には`draw_line`インターフェイスの代わりに`draw_dotted_line`、`draw_dashed_line`、`draw_round_dotted_line`、`draw_dash_dotted_line`などのインターフェイスを仕様してください。

```py
# runnable
import apysc as ap

ap.Stage(
    background_color=ap.Color("#333"),
    stage_width=200,
    stage_height=100,
    stage_elem_id="stage",
)
sprite: ap.Sprite = ap.Sprite()

# dot_setting will be ignored, and the result line will not be dotted.
sprite.graphics.line_style(
    color=ap.Color("#0af"),
    thickness=5,
    dot_setting=ap.LineDotSetting(dot_size=5),
)
sprite.graphics.draw_line(x_start=50, y_start=50, x_end=150, y_end=50)

ap.save_overall_html(dest_dir_path="graphics_draw_line_ignored_dot_setting/")
```

<iframe src="static/graphics_draw_line_ignored_dot_setting/index.html" width="200" height=100></iframe>

## Line クラスのインスタンス

`draw_line`インターフェイスは`Line`クラスのインスタンスを返却します。そのインスタンスの各種設定を変更したりイベントを登録したり等を行うことができます。`draw_dotted_line`、`draw_dashed_line`、`draw_round_dotted_line`、`draw_dash_dotted_line`などのインターフェイスも同じく`Line`クラスのインスタンスを返却します。

```py
# runnable
import apysc as ap

ap.Stage(
    background_color=ap.Color("#333"),
    stage_width=200,
    stage_height=100,
    stage_elem_id="stage",
)
sprite: ap.Sprite = ap.Sprite()

sprite.graphics.line_style(color=ap.Color("#0af"), thickness=5)
line: ap.Line = sprite.graphics.draw_line(x_start=50, y_start=50, x_end=150, y_end=50)

# Update the line color from cyan to magenta.
line.line_color = ap.Color("#f0a")

ap.save_overall_html(dest_dir_path="graphics_draw_line_line_instance/")
```

<iframe src="static/graphics_draw_line_line_instance/index.html" width="200" height=100></iframe>

## draw_line API

<span class="inconspicuous-txt">特記事項: このAPIドキュメントはドキュメントビルド用のスクリプトによって自動で生成・同期されています。そのためもしかしたらこの節の内容は前節までの内容と重複している場合があります。</span>

**[インターフェイスの構造]** `draw_line(self, *, x_start: Union[float, apysc._type.number.Number], y_start: Union[float, apysc._type.number.Number], x_end: Union[float, apysc._type.number.Number], y_end: Union[float, apysc._type.number.Number], variable_name_suffix: str = '') -> '_line.Line'`<hr>

**[インターフェイス概要]**

通常の直線のベクターグラフィックスを描画します。<hr>

**[引数]**

- `x_start`: float or Number
  - 線の開始位置のX座標。

- `y_start`: float or Number
  - 線の開始位置のY座標。

- `x_end`: float or Number
  - 線の終了位置のX座標。

- `y_end`: float or Number
  - 線の終了位置のY座標。

- `variable_name_suffix`: str, default ''
  - JavaScript上の変数のサフィックスの設定です。この設定はJavaScriptのデバッグ時に役立つことがあります。

<hr>

**[返却値]**

- `line`: Line
  - 生成された線のグラフィックスのインスタンス。

<hr>

**[特記事項]**

 ・このインターフェイスは`LineDotSetting`や`LineDashSetting`などの設定を無視します。<hr>

**[コードサンプル]**

```py
>>> import apysc as ap
>>> stage: ap.Stage = ap.Stage()
>>> sprite: ap.Sprite = ap.Sprite()
>>> sprite.graphics.line_style(color=ap.Color("#fff"), thickness=5)
>>> line: ap.Line = sprite.graphics.draw_line(
...     x_start=50, y_start=50, x_end=150, y_end=50
... )
>>> line.line_color
Color("#ffffff")

>>> line.line_thickness
Int(5)
```