<span class="inconspicuous-txt">※この翻訳ドキュメントはスクリプトによって出力・同期されています。内容が怪しそうな場合は<a href="https://github.com/simon-ritchie/apysc/issues" target="_blank">GitHubにissue</a>を追加したり[英語の原文](https://simon-ritchie.github.io/apysc/en/graphics_draw_dotted_line.html)の確認をお願いします。</span>

# Graphics クラスの draw_dotted_line インターフェイス

このページでは`Graphics`クラスの`draw_dotted_line`メソッドのインターフェイスについて説明します。

## インターフェイス概要

`draw_dotted_line`インターフェイスはシンプルな点線の直線のグラフィックスを描画します。このインターフェイスは`dot_setting`、`dash_setting`、`round_dot_setting`、`dash_dot_setting`の引数や属性の設定を無視します。

## 基本的な使い方

`draw_dotted_line`インターフェイスは基本的な線の座標の指定として`x_start`、`y_start`、`x_end`、`y_end`の各引数を持ちます。また、点線のサイズとして`dot_size`引数の指定が必要です。

```py
# runnable
import apysc as ap

ap.Stage(
    background_color=ap.Color("#333"),
    stage_width=250,
    stage_height=130,
    stage_elem_id="stage",
)
sprite: ap.Sprite = ap.Sprite()

# Set 2-pixel dot size and draw line.
sprite.graphics.line_style(color=ap.Color("#0af"), thickness=2)
sprite.graphics.draw_dotted_line(
    x_start=50, y_start=50, x_end=200, y_end=50, dot_size=2
)

# Set 5-pixel dot size and draw line.
sprite.graphics.line_style(color=ap.Color("#0af"), thickness=2)
sprite.graphics.draw_dotted_line(
    x_start=50, y_start=80, x_end=200, y_end=80, dot_size=5
)

ap.save_overall_html(dest_dir_path="graphics_draw_dotted_line_basic_usage/")
```

<iframe src="static/graphics_draw_dotted_line_basic_usage/index.html" width="250" height="130"></iframe>

## draw_dotted_line API

<span class="inconspicuous-txt">特記事項: このAPIドキュメントはドキュメントビルド用のスクリプトによって自動で生成・同期されています。そのためもしかしたらこの節の内容は前節までの内容と重複している場合があります。</span>

**[インターフェイスの構造]** `draw_dotted_line(self, *, x_start: Union[float, apysc._type.number.Number], y_start: Union[float, apysc._type.number.Number], x_end: Union[float, apysc._type.number.Number], y_end: Union[float, apysc._type.number.Number], dot_size: Union[int, apysc._type.int.Int], variable_name_suffix: str = '') -> '_line.Line'`<hr>

**[インターフェイス概要]**

点線のベクターグラフィックスを描画します。<hr>

**[引数]**

- `x_start`: float or Number
  - 線の開始位置のX座標。

- `y_start`: float or Number
  - 線の開始位置のY座標。

- `x_end`: float or Number
  - 線の終了位置のX座標。

- `y_end`: float or Number
  - 線の終了位置のY座標。

- `dot_size`: Int or int
  - ドットのサイズ。

- `variable_name_suffix`: str, default ''
  - JavaScript上の変数のサフィックスの設定です。この設定はJavaScriptのデバッグ時に役立つことがあります。

<hr>

**[返却値]**

- `line`: Line
  - 生成された線のグラフィックスのインスタンス。

<hr>

**[特記事項]**

 ・このインターフェイスは`LineDotSetting`を除いた`LineDashSetting`などの線のスタイル設定を無視します。<hr>

**[コードサンプル]**

```py
>>> import apysc as ap
>>> stage: ap.Stage = ap.Stage()
>>> sprite: ap.Sprite = ap.Sprite()
>>> sprite.graphics.line_style(color=ap.Color("#fff"), thickness=5)
>>> line: ap.Line = sprite.graphics.draw_dotted_line(
...     x_start=50, y_start=50, x_end=150, y_end=50, dot_size=5
... )
>>> line.line_color
Color("#ffffff")

>>> line.line_thickness
Int(5)

>>> line.line_dot_setting.dot_size
Int(5)
```