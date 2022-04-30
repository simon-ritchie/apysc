<span class="inconspicuous-txt">※この翻訳ドキュメントはスクリプトによって出力・同期されています。内容が怪しそうな場合は<a href="https://github.com/simon-ritchie/apysc/issues" target="_blank">GitHubにissue</a>を追加したり[英語の原文](../en/graphics_fill_color.html)の確認をお願いします。</span>

# Graphics クラスの fill_color インターフェイス

このページでは`Graphics`クラスの`fill_color`属性の居たーフェイスについて説明します。

## インターフェイス概要

`fill_color`属性のインターフェイスでは塗りの色の値を更新したり取得したりすることができます。

## 基本的な使い方

getterのインターフェイスは`String`型の16進数のカラーコードの文字列になります。setterのインターフェイスも`String`型の16進数のカラーコードの指定が必要になります。

以下のコード例では四角をクリックした際に塗りの色をシアンからマゼンタに変更するようにしています:

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
    fill_color: ap.String = rectangle.fill_color
    with ap.If(fill_color == '#00aaff'):
        rectangle.fill_color = ap.String('#f0a')
    with ap.Else():
        rectangle.fill_color = ap.String('#0af')


ap.Stage(
    stage_width=150, stage_height=150, background_color='#333',
    stage_elem_id='stage')
sprite: ap.Sprite = ap.Sprite()
sprite.graphics.begin_fill(color='#0af')
rectangle: ap.Rectangle = sprite.graphics.draw_rect(
    x=50, y=50, width=50, height=50)
rectangle.click(on_click)

ap.save_overall_html(
    dest_dir_path='./graphics_fill_color_basic_usage/')
```

<iframe src="static/graphics_fill_color_basic_usage/index.html" width="150" height="150"></iframe>

## fill_color 属性のAPI

<span class="inconspicuous-txt">特記事項: このAPIドキュメントはドキュメントビルド用のスクリプトによって自動で生成・同期されています。そのためもしかしたらこの節の内容は前節までの内容と重複している場合があります。</span>

**[インターフェイス概要]** インスタンスの塗りの色を取得します。<hr>

**[返却値]**

- `fill_color`: String
  - 現在の塗りの色（`'#00aaff'`などの16進数の文字列）。もしも設定されていない場合空文字が返却されます。

<hr>

**[コードサンプル]**

```py
>>> import apysc as ap
>>> stage: ap.Stage = ap.Stage()
>>> sprite: ap.Sprite = ap.Sprite()
>>> sprite.graphics.begin_fill(color='#0af')
>>> rectangle: ap.Rectangle = sprite.graphics.draw_rect(
...     x=50, y=50, width=50, height=50)
>>> rectangle.fill_color = ap.String('#f0a')
>>> rectangle.fill_color
String('#ff00aa')
```