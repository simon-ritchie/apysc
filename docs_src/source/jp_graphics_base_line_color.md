<span class="inconspicuous-txt">※この翻訳ドキュメントはスクリプトによって出力・同期されています。内容が怪しそうな場合は<a href="https://github.com/simon-ritchie/apysc/issues" target="_blank">GitHubにissue</a>を追加したり[英語の原文](https://simon-ritchie.github.io/apysc/en/graphics_base_line_color.html)の確認をお願いします。</span>

# GraphicsBase クラスの line_color インターフェイス

このページでは`GraphicsBase`クラスの`line_color`属性のインターフェイスについて説明します。

## インターフェイス概要

`line_color`属性のインターフェイスではインスタンスの線の色の更新や取得を行うことができます。

## 基本的な使い方

getterとsetterのインターフェイスで扱う値は`Color`型の値となります。

以下のコード例では四角をクリックした際に線の色をシアンからマゼンタに変更しています:

```py
# runnable
import apysc as ap


def on_click(e: ap.MouseEvent[ap.Rectangle], options: dict) -> None:
    """
    The handler that the rectangle calls when clicked.

    Parameters
    ----------
    e : MouseEvent
        Event instance.
    options : dict
        Optional arguments dictionary.
    """
    rectangle: ap.Rectangle = e.this
    line_color: ap.Color = rectangle.line_color
    with ap.If(line_color == ap.Color("#00aaff")):
        rectangle.line_color = ap.Color("#f0a")
    with ap.Else():
        rectangle.line_color = ap.Color("#0af")


ap.Stage(
    stage_width=150,
    stage_height=150,
    background_color=ap.Color("#333"),
    stage_elem_id="stage",
)
sprite: ap.Sprite = ap.Sprite()
sprite.graphics.begin_fill(color=ap.Color("#0"), alpha=0.0)
sprite.graphics.line_style(color=ap.Color("#0af"), thickness=5)

rectangle: ap.Rectangle = sprite.graphics.draw_rect(x=50, y=50, width=50, height=50)
rectangle.click(on_click)

ap.save_overall_html(dest_dir_path="./graphics_base_line_color_basic_usage/")
```

<iframe src="static/graphics_base_line_color_basic_usage/index.html" width="150" height="150"></iframe>

## line_color 属性のAPI

<span class="inconspicuous-txt">特記事項: このAPIドキュメントはドキュメントビルド用のスクリプトによって自動で生成・同期されています。そのためもしかしたらこの節の内容は前節までの内容と重複している場合があります。</span>

**[インターフェイス概要]**

インスタンスの線の色を取得します。<hr>

**[返却値]**

- `line_color`: Color
  - '#00aaff'などの16進数の線の色。もし設定されていない場合は`COLORLESS`の定数が返却されます。

<hr>

**[コードサンプル]**

```py
>>> import apysc as ap
>>> _ = ap.Stage(
...     stage_width=150,
...     stage_height=150,
...     background_color=ap.Color("#333"),
...     stage_elem_id="stage",
... )
>>> rectangle: ap.Rectangle = ap.Rectangle(
...     x=50,
...     y=50,
...     width=50,
...     height=50,
...     line_color=ap.Color("#0af"),
...     line_thickness=2,
... )
>>> rectangle.line_color
Color("#00aaff")

>>> rectangle.line_color = ap.Color("#ff00aa")
>>> rectangle.line_color
Color("#ff00aa")
```