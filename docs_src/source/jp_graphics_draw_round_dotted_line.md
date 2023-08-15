<span class="inconspicuous-txt">※この翻訳ドキュメントはスクリプトによって出力・同期されています。内容が怪しそうな場合は<a href="https://github.com/simon-ritchie/apysc/issues" target="_blank">GitHubにissue</a>を追加したり[英語の原文](https://simon-ritchie.github.io/apysc/en/graphics_draw_round_dotted_line.html)の確認をお願いします。</span>

# Graphics クラスの draw_round_dotted_line インターフェイス

このページでは`Graphics`クラスの`draw_round_dotted_line`メソッドのインターフェイスについて説明します。

## インターフェイス概要

`draw_round_dotted_line`インターフェイスはシンプルな丸ドットの直線のグラフィックスを描画します。このインターフェイスは`dot_setting`、`dash_setting`、`round_dot_setting`、`dash_dot_setting`、`cap`の各設定を無視します（このインターフェイスでは丸の`cap`設定を内部で使っているため`cap`設定は無視されます）。

## 基本的な使い方

`draw_round_dotted_line`インターフェイスは基本的な座標指定の引数として`x_start`、`y_start`、`x_end`、`y_end`の引数を持っています。それらに加えて丸のサイズの`round_size`と丸の間のスペースを決定する`space_size`引数の指定が必要になります。

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

# Set 5-pixel round size and draw the line.
sprite.graphics.line_style(color=ap.Color("#0af"))
sprite.graphics.draw_round_dotted_line(
    x_start=50, y_start=50, x_end=200, y_end=50, round_size=5, space_size=5
)

# Set 10-pixel round size and draw the line.
sprite.graphics.draw_round_dotted_line(
    x_start=50, y_start=80, x_end=200, y_end=80, round_size=10, space_size=5
)

ap.save_overall_html(dest_dir_path="graphics_draw_round_dotted_line_basic_usage/")
```

<iframe src="static/graphics_draw_round_dotted_line_basic_usage/index.html" width="250" height="130"></iframe>

## 特記事項

このインターフェイスは丸のcap（線の端のスタイル）設定を使用しているため、線の長さはcapのサイズに応じて大きくなります。

もしも線の左端を他の線と合わせたい場合には丸のサイズの半分を`x_start`の引数から減算してください。

```py
# runnable
import apysc as ap

ap.Stage(
    background_color=ap.Color("#333"),
    stage_width=270,
    stage_height=130,
    stage_elem_id="stage",
)
sprite: ap.Sprite = ap.Sprite()

# Set 5-pixel round size and draw the line.
sprite.graphics.line_style(color=ap.Color("#0af"))
sprite.graphics.draw_round_dotted_line(
    x_start=50, y_start=50, x_end=220, y_end=50, round_size=10, space_size=5
)

# Set 45-pixel (50 - half-round size) to x_start argument
# and draw the normal line.
sprite.graphics.draw_line(x_start=45, y_start=80, x_end=225, y_end=80)

ap.save_overall_html(dest_dir_path="graphics_draw_round_dotted_line_notes/")
```

<iframe src="static/graphics_draw_round_dotted_line_notes/index.html" width="270" height="130"></iframe>

## draw_round_dotted_line API

<span class="inconspicuous-txt">特記事項: このAPIドキュメントはドキュメントビルド用のスクリプトによって自動で生成・同期されています。そのためもしかしたらこの節の内容は前節までの内容と重複している場合があります。</span>

**[インターフェイスの構造]** `draw_round_dotted_line(self, *, x_start: Union[float, apysc._type.number.Number], y_start: Union[float, apysc._type.number.Number], x_end: Union[float, apysc._type.number.Number], y_end: Union[float, apysc._type.number.Number], round_size: Union[int, apysc._type.int.Int], space_size: Union[int, apysc._type.int.Int], variable_name_suffix: str = '') -> '_line.Line'`<hr>

**[インターフェイス概要]**

丸ドットの直線のベクターグラフィックスを描画します。<hr>

**[引数]**

- `x_start`: float or Number
  - 線の開始位置のX座標。

- `y_start`: float or Number
  - 線の開始位置のY座標。

- `x_end`: float or Number
  - 線の終了位置のX座標。

- `y_end`: float or Number
  - 線の終了位置のY座標。

- `round_size`: Int or int
  - 丸ドットのサイズ。

- `space_size`: Int or int
  - ドット間の空白のスペースのサイズ。

- `variable_name_suffix`: str, default ''
  - JavaScript上の変数のサフィックスの設定です。この設定はJavaScriptのデバッグ時に役立つことがあります。

<hr>

**[返却値]**

- `line`: Line
  - 生成された線のグラフィックスのインスタンス。

<hr>

**[特記事項]**

このインターフェイスは`LineRoundDotSetting`を除いて`LineDotSetting`などの設定を無視します。<hr>

**[コードサンプル]**

```py
>>> import apysc as ap
>>> stage: ap.Stage = ap.Stage()
>>> sprite: ap.Sprite = ap.Sprite()
>>> sprite.graphics.line_style(color=ap.Color("#fff"), thickness=5)
>>> line: ap.Line = sprite.graphics.draw_round_dotted_line(
...     x_start=50, y_start=50, x_end=150, y_end=50, round_size=6, space_size=3
... )
>>> line.line_color
Color("#ffffff")

>>> line.line_round_dot_setting.round_size
Int(6)

>>> line.line_round_dot_setting.space_size
Int(3)
```