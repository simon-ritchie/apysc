<span class="inconspicuous-txt">※この翻訳ドキュメントはスクリプトによって出力・同期されています。内容が怪しそうな場合は<a href="https://github.com/simon-ritchie/apysc/issues" target="_blank">GitHubにissue</a>を追加したり[英語の原文](https://simon-ritchie.github.io/apysc/en/graphics_draw_dashed_line.html)の確認をお願いします。</span>

# Graphics クラスの draw_dashed_line インターフェイス

このページでは`Graphics`クラスの`draw_dashed_line`メソッドのインターフェイスについて説明します。

## インターフェイス概要

`draw_dashed_line`インターフェイスはシンプルな破線の直線のグラフィックスを描画します。このインターフェイスは`dot_setting`や`dash_setting`、`round_dot_setting`、`dash_dot_setting`の引数や属性の設定を無視します。

## 基本的な使い方

`draw_dashed_line`インターフェイスは基本的な線の座標の指定として`x_start`、`y_start`、`x_end`、`y_end`の各引数を持ちます。加えて、破線のサイズとしての`dash_size`引数と破線間のスペースのサイズとしての`space_size`引数の指定が必要です。

```py
# runnable
import apysc as ap

ap.Stage(
    background_color='#333',
    stage_width=250,
    stage_height=130,
    stage_elem_id='stage')
sprite: ap.Sprite = ap.Sprite()

# Set 5-pixel dash setting and draw the line.
sprite.graphics.line_style(
    color='#0af', thickness=2)
sprite.graphics.draw_dashed_line(
    x_start=50, y_start=50, x_end=200, y_end=50,
    dash_size=5, space_size=2)

# Set 10-pixel dash setting and draw the line.
sprite.graphics.draw_dashed_line(
    x_start=50, y_start=80, x_end=200, y_end=80,
    dash_size=10, space_size=2)

ap.save_overall_html(
    dest_dir_path='graphics_draw_dashed_line_basic_usage/')
```

<iframe src="static/graphics_draw_dashed_line_basic_usage/index.html" width="250" height=130></iframe>

## draw_dashed_line API

<span class="inconspicuous-txt">特記事項: このAPIドキュメントはドキュメントビルド用のスクリプトによって自動で生成・同期されています。そのためもしかしたらこの節の内容は前節までの内容と重複している場合があります。</span>

**[インターフェイスの構造]** `draw_dashed_line(self, x_start: Union[int, apysc._type.int.Int], y_start: Union[int, apysc._type.int.Int], x_end: Union[int, apysc._type.int.Int], y_end: Union[int, apysc._type.int.Int], dash_size: Union[int, apysc._type.int.Int], space_size: Union[int, apysc._type.int.Int]) -> '_line.Line'`<hr>

**[インターフェイス概要]** 破線のベクターグラフィックスを描画します。<hr>

**[引数]**

- `x_start`: Int or int
  - 線の開始位置のX座標。

- `y_start`: Int or int
  - 線の開始位置のY座標。

- `x_end`: Int or int
  - 線の終了位置のX座標。

- `y_end`: Int or int
  - 線の終了位置のY座標。

- `dash_size`: Int or int
  - 破線部分のサイズ。

- `space_size`: Int or int
  - 破線間の空白スペースのサイズ。

<hr>

**[返却値]**

- `line`: Line
  - 生成された線のグラフィックスのインスタンス。

<hr>

**[特記事項]**

 ・このインターフェイスは`LineDashSetting`を除いた`LineDotSetting`などの線のスタイル設定を無視します。<hr>

**[コードサンプル]**

```py
>>> import apysc as ap
>>> stage: ap.Stage = ap.Stage()
>>> sprite: ap.Sprite = ap.Sprite()
>>> sprite.graphics.line_style(color='#fff', thickness=5)
>>> line: ap.Line = sprite.graphics.draw_dashed_line(
...     x_start=50, y_start=50, x_end=150, y_end=50,
...     dash_size=5, space_size=2)
>>> line.line_color
String('#ffffff')

>>> line.line_dash_setting.dash_size
Int(5)

>>> line.line_dash_setting.space_size
Int(2)
```