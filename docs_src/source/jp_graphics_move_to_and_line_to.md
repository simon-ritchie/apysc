<span class="inconspicuous-txt">※この翻訳ドキュメントはスクリプトによって出力・同期されています。内容が怪しそうな場合は<a href="https://github.com/simon-ritchie/apysc/issues" target="_blank">GitHubにissue</a>を追加したり[英語の原文](https://simon-ritchie.github.io/apysc/en/graphics_move_to_and_line_to.html)の確認をお願いします。</span>

# Graphics クラスの move_to と line_to インターフェイス

このページでは`Graphics`クラスの`move_to`と`line_to`メソッドの各インターフェイスについて説明します。

## 各インターフェイスの概要

`move_to`インターフェイスは線の描画の開始位置を設定します。`line_to`インターフェイスは現在の位置から終点位置に向けて線を描画します。連続して`line_to`を呼び出すと対象の線は折れ線になります。

もしも`line_to`インターフェイスを呼んだ後に`move_to`インターフェイスを呼んだ場合には新しい線のインスタンスが生成されます。

## 基本的な使い方

`move_to`と`line_to`インターフェイスは共にxとyの引数を必要とします。

```py
# runnable
import apysc as ap

ap.Stage(
    background_color=ap.Color("#333"),
    stage_width=300,
    stage_height=100,
    stage_elem_id="stage",
)
sprite: ap.Sprite = ap.Sprite()

sprite.graphics.line_style(color=ap.Color("#0af"), thickness=5)

# Move to x=50, y=50 point (no drawing).
sprite.graphics.move_to(x=50, y=50)

# Draw the line from the current point (50, 50) to the
# destination point (250, 50).
sprite.graphics.line_to(x=250, y=50)

ap.save_overall_html(dest_dir_path="graphics_move_to_and_line_to_basic_usage/")
```

<iframe src="static/graphics_move_to_and_line_to_basic_usage/index.html" width="300" height="100"></iframe>

## line_to インターフェイスの連続した呼び出し

`line_to`インターフェイスを連続して呼び出した場合、結果の線は折れ線になります。

```py
# runnable
import apysc as ap

ap.Stage(
    background_color=ap.Color("#333"),
    stage_width=200,
    stage_height=200,
    stage_elem_id="stage",
)
sprite: ap.Sprite = ap.Sprite()

sprite.graphics.line_style(color=ap.Color("#0af"), thickness=5)

# Move to x=50, y=50 point (no drawing).
sprite.graphics.move_to(x=50, y=50)

# Draw the line from the current point (50, 50) to the
# destination point (150, 50).
sprite.graphics.line_to(x=150, y=50)

# Draw the line from the current point (250, 50) to the
# destination point (50, 150). This calling changes the line
# to the polyline.
sprite.graphics.line_to(x=50, y=150)

# Finally the polyline becomes Z shape by drawing to
# destination point (150, 150).
sprite.graphics.line_to(x=150, y=150)

ap.save_overall_html(dest_dir_path="graphics_move_to_and_line_to_sequential_calling/")
```

<iframe src="static/graphics_move_to_and_line_to_sequential_calling/index.html" width="200" height="200"></iframe>

## line_to インターフェイスを呼び出した後の move_to インターフェイスの呼び出し

`line_to`インターフェイスを呼び出した後に`move_to`を呼び出した場合新しい線のインスタンスが生成されます。

```py
# runnable
import apysc as ap

ap.Stage(
    background_color=ap.Color("#333"),
    stage_width=250,
    stage_height=150,
    stage_elem_id="stage",
)
sprite: ap.Sprite = ap.Sprite()

sprite.graphics.line_style(color=ap.Color("#0af"), thickness=5)

# First move_to interface calling.
sprite.graphics.move_to(x=50, y=50)
sprite.graphics.line_to(x=100, y=50)
sprite.graphics.line_to(x=50, y=100)
sprite.graphics.line_to(x=100, y=100)

# Second move_to interface calling. This will create a new
# polyline instance.
sprite.graphics.move_to(x=150, y=50)
sprite.graphics.line_to(x=200, y=50)
sprite.graphics.line_to(x=150, y=100)
sprite.graphics.line_to(x=200, y=100)

ap.save_overall_html(
    dest_dir_path="graphics_move_to_and_line_to_multi_move_to_calling/"
)
```

<iframe src="static/graphics_move_to_and_line_to_multi_move_to_calling/index.html" width="250" height="150"></iframe>

## Polyline インスタンス

`move_to`や`line_to`インターフェイスは`Polyline`クラスのインスタンスを返却します。そのインスタンスを使って各設定を更新したりイベントを設定したりすることができます。

例えば以下のコード例では`Polyline`のインスタンスにマウスイベントを設定し、`on_line_click`ハンドラ内で線の色の更新と点線のスタイルを設定しています。

```py
# runnable
import apysc as ap


def on_line_click(e: ap.MouseEvent[ap.Polyline], options: dict) -> None:
    """
    The handler that the line instance calls when clicked.

    Parameters
    ----------
    e : MouseEvent
        The event instance.
    options : dict
        Optional arguments.
    """
    polyline: ap.Polyline = e.this
    polyline.line_color = ap.Color("#f0a")
    polyline.line_dot_setting = ap.LineDotSetting(dot_size=5)


ap.Stage(
    background_color=ap.Color("#333"),
    stage_width=200,
    stage_height=100,
    stage_elem_id="stage",
)
sprite: ap.Sprite = ap.Sprite()

sprite.graphics.line_style(color=ap.Color("#0af"), thickness=30)
polyline: ap.Polyline = sprite.graphics.move_to(x=50, y=50)
sprite.graphics.line_to(x=150, y=50)
polyline.click(on_line_click)

ap.save_overall_html(dest_dir_path="graphics_move_to_and_line_to_polyline/")
```

もし以下の四角をクリックし0た場合、線のスタイルは更新されます:

<iframe src="static/graphics_move_to_and_line_to_polyline/index.html" width="200" height="100"></iframe>

## move_to API

<span class="inconspicuous-txt">特記事項: このAPIドキュメントはドキュメントビルド用のスクリプトによって自動で生成・同期されています。そのためもしかしたらこの節の内容は前節までの内容と重複している場合があります。</span>

**[インターフェイスの構造]** `move_to(self, *, x: Union[float, apysc._type.number.Number], y: Union[float, apysc._type.number.Number], variable_name_suffix: str = '') -> '_polyline.Polyline'`<hr>

**[インターフェイス概要]**

指定された座標に線の描画位置を移動させます。<hr>

**[引数]**

- `x`: float or Number
  - 移動先となるX座標。

- `y`: float or Number
  - 移動先となるY座標。

- `variable_name_suffix`: str, default ""
  - JavaScript上の変数のサフィックスの設定です。この設定はJavaScriptのデバッグ時に役立つことがあります。

<hr>

**[返却値]**

- `line`: Polyline
  - 線のグラフィックスのインスタンス。

<hr>

**[コードサンプル]**

```py
>>> import apysc as ap
>>> stage: ap.Stage = ap.Stage()
>>> sprite: ap.Sprite = ap.Sprite()
>>> sprite.graphics.line_style(color=ap.Color("#fff"), thickness=5)
>>> line_1: ap.Polyline = sprite.graphics.move_to(x=50, y=50)
>>> line_2: ap.Polyline = sprite.graphics.line_to(x=150, y=50)
>>> line_1 == line_2
True

>>> line_1.line_color
Color("#ffffff")

>>> line_1.line_thickness
Int(5)
```

## line_to API

<span class="inconspicuous-txt">特記事項: このAPIドキュメントはドキュメントビルド用のスクリプトによって自動で生成・同期されています。そのためもしかしたらこの節の内容は前節までの内容と重複している場合があります。</span>

**[インターフェイスの構造]** `line_to(self, *, x: Union[float, apysc._type.number.Number], y: Union[float, apysc._type.number.Number], variable_name_suffix: str = '') -> '_polyline.Polyline'`<hr>

**[インターフェイス概要]**

直前の位置の座標から指定された座標に向けて線を描画します（初期位置はx=0, y=0になります）。<hr>

**[引数]**

- `x`: float or Number
  - 線の描画先となる終点のX座標。

- `y`: float or Number
  - 線の描画先となる終点のY座標。

- `variable_name_suffix`: str, default ""
  - JavaScript上の変数のサフィックスの設定です。この設定はJavaScriptのデバッグ時に役立つことがあります。

<hr>

**[返却値]**

- `line`: Polyline
  - 線のグラフィックスのインスタンス。

<hr>

**[コードサンプル]**

```py
>>> import apysc as ap
>>> stage: ap.Stage = ap.Stage()
>>> sprite: ap.Sprite = ap.Sprite()
>>> sprite.graphics.line_style(color=ap.Color("#fff"), thickness=5)
>>> line_1: ap.Polyline = sprite.graphics.move_to(x=50, y=50)
>>> line_2: ap.Polyline = sprite.graphics.line_to(x=150, y=50)
>>> line_3: ap.Polyline = sprite.graphics.line_to(x=50, y=150)
>>> line_1 == line_2 == line_3
True

>>> line_1.line_color
Color("#ffffff")

>>> line_1.line_thickness
Int(5)
```