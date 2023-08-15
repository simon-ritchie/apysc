<span class="inconspicuous-txt">※この翻訳ドキュメントはスクリプトによって出力・同期されています。内容が怪しそうな場合は<a href="https://github.com/simon-ritchie/apysc/issues" target="_blank">GitHubにissue</a>を追加したり[英語の原文](https://simon-ritchie.github.io/apysc/en/graphics_draw_rect.html)の確認をお願いします。</span>

# Graphics クラスの draw_rect インターフェイス

このページでは`Graphics`クラスの`draw_rect`メソッドのインターフェイスについて説明します。

## インターフェイス概要

`draw_rect`インターフェイスは四角のベクターグラフィックスを描画します。

## 基本的な使い方

`draw_rect`インターフェイスは`x`、`y`、`width`、`height`の各引数を持っています。`x`と`y`は四角の座標を設定し、`width`と`height`は四角のサイズを決定します。

```py
# runnable
import apysc as ap

ap.Stage(
    background_color=ap.Color("#333"),
    stage_width=200,
    stage_height=150,
    stage_elem_id="stage",
)
sprite: ap.Sprite = ap.Sprite()
sprite.graphics.begin_fill(color=ap.Color("#0af"))
sprite.graphics.draw_rect(x=50, y=50, width=100, height=50)

ap.save_overall_html(dest_dir_path="graphics_draw_rect_basic_usage/")
```

前述のコードでは横長の四角を描画しています。

<iframe src="static/graphics_draw_rect_basic_usage/index.html" width="200" height="150"></iframe>

特記事項: `draw_rect`のインターフェイスを呼ぶ前に`begin_fill`メソッド（塗りの設定のインターフェイス）を呼んでおく必要があります。もし`begin_fill`の呼び出しがされていない場合画面上に四角が表示されません。

```py
# runnable
import apysc as ap

stage: ap.Stage = ap.Stage(
    background_color=ap.Color("#333"),
    stage_width=200,
    stage_height=150,
    stage_elem_id="stage",
)
sprite: ap.Sprite = ap.Sprite()
sprite.graphics.draw_rect(x=50, y=50, width=100, height=50)

ap.save_overall_html(dest_dir_path="graphics_draw_rect_basic_usage_skipped_begin_fill/")
```

<iframe src="static/graphics_draw_rect_basic_usage_skipped_begin_fill/index.html" width="200" height="150"></iframe>

## Rectangle インスタンス

`draw_rect`インターフェイスは`Rectangle`クラスのインスタンスを変逆します。そのインスタンスに対して各属性の更新やイベントハンドラの登録などを行うことができます。

例えば以下のコードでは`Rectangle`のインスタンスに対してクリックのマウスイベントを登録し、`on_click`のハンドラ内でX座標を更新しています。

```py
# runnable
import apysc as ap


def on_click(e: ap.MouseEvent[ap.Rectangle], options: dict) -> None:
    """
    The handler that the rectangle calls when clicked.

    Parameters
    ----------
    e : MouseEvent
        Created event instance.
    options : dict
        Optional arguments.
    """
    rectangle: ap.Rectangle = e.this
    rectangle.x = ap.Int(100)


ap.Stage(
    background_color=ap.Color("#333"),
    stage_width=200,
    stage_height=150,
    stage_elem_id="stage",
)
sprite: ap.Sprite = ap.Sprite()

sprite.graphics.begin_fill(color=ap.Color("#0af"))
rectangle: ap.Rectangle = sprite.graphics.draw_rect(x=50, y=50, width=50, height=50)
rectangle.click(on_click)

ap.save_overall_html(dest_dir_path="graphics_draw_rect_rectangle/")
```

四角をクリックしてみると、ハンドラはX座標を100pxの位置に変更します。

<iframe src="static/graphics_draw_rect_rectangle/index.html" width="200" height="150"></iframe>

## draw_rect API

<span class="inconspicuous-txt">特記事項: このAPIドキュメントはドキュメントビルド用のスクリプトによって自動で生成・同期されています。そのためもしかしたらこの節の内容は前節までの内容と重複している場合があります。</span>

**[インターフェイスの構造]** `draw_rect(self, *, x: Union[float, apysc._type.number.Number], y: Union[float, apysc._type.number.Number], width: Union[int, apysc._type.int.Int], height: Union[int, apysc._type.int.Int], variable_name_suffix: str = '') -> apysc._display.rectangle.Rectangle`<hr>

**[インターフェイス概要]**

ベクターグラフィックスの四角を描画します。<hr>

**[引数]**

- `x`: float or Number
  - 描画を開始する位置のX座標。

- `y`: float or Number
  - 描画を開始する位置のY座標。

- `width`: Int or int
  - 四角の幅。

- `height`: Int or int
  - 四角の高さ。

- `variable_name_suffix`: str, default ''
  - JavaScript上の変数のサフィックスの設定です。この設定はJavaScriptのデバッグ時に役立つことがあります。

<hr>

**[返却値]**

- `rectangle`: Rectangle
  - 生成された四角。

<hr>

**[コードサンプル]**

```py
>>> import apysc as ap
>>> stage: ap.Stage = ap.Stage()
>>> sprite: ap.Sprite = ap.Sprite()
>>> sprite.graphics.begin_fill(color=ap.Color("#0af"))
>>> rectangle: ap.Rectangle = sprite.graphics.draw_rect(
...     x=50, y=50, width=50, height=50
... )
>>> rectangle.x
Number(50.0)

>>> rectangle.width
Int(50)

>>> rectangle.fill_color
Color("#00aaff")
```