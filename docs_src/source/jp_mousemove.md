<span class="inconspicuous-txt">※この翻訳ドキュメントはスクリプトによって出力・同期されています。内容が怪しそうな場合は<a href="https://github.com/simon-ritchie/apysc/issues" target="_blank">GitHubにissue</a>を追加したり[英語の原文](https://simon-ritchie.github.io/apysc/en/mousemove.html)の確認をお願いします。</span>

# mousemove インターフェイス

このページでは`mousemove`のインターフェイスについて説明します。

## インターフェイス概要

`mousemove`のインターフェイスは任意の`DisplayObject`のインスタンスへとマウスを動かした時のイベントハンドラの設定を追加します。対象のインスタンス上でマウスカーソルを動かす度に設定されたハンドラが呼ばれます。

## 関連資料

以下のページでは基本的なマウスイベントの各インターフェイスについて説明しています。

- [基本的なマウスイベントの各インターフェイス](jp_mouse_event_basic.md)

## 基本的な使い方

`DisplayObject`の各インスタンスは`mousemove`メソッドを持っており、そのインターフェイスを使ってハンドラを設定することができます。

以下のコード例では円に対してマウスを動かしたときのハンドラを設定しています。対象の円の上でマウスカーソルを動かすと、円の位置はカーソルの位置に更新されます。

```py
# runnable
import apysc as ap


def on_mousemove(e: ap.MouseEvent[ap.Circle], options: dict) -> None:
    """
    The handler that the circle calls when mousemove.

    Parameters
    ----------
    e : MouseEvent
        Event instance.
    options : dict
        Optional arguments dictionary.
    """
    circle: ap.Circle = e.this
    circle.x = e.stage_x
    circle.y = e.stage_y


ap.Stage(
    background_color="#333", stage_width=200, stage_height=200, stage_elem_id="stage"
)

sprite: ap.Sprite = ap.Sprite()
sprite.graphics.begin_fill(color="#0af")
circle: ap.Circle = sprite.graphics.draw_circle(x=100, y=100, radius=100)
circle.mousemove(on_mousemove)

ap.save_overall_html(dest_dir_path="mousemove_basic_usage/")
```

<iframe src="static/mousemove_basic_usage/index.html" width="200" height="200"></iframe>

## 解除用のインターフェイス

`unbind_mousemove`インターフェイスでは`DisplayObject`のインスタンスのマウスを動かした時のイベントのハンドラ設定を解除することができます。

以下のコード例では円をクリックした際にマウスを動かしたときのイベントハンドラの設定を解除するようにしています。

```py
# runnable
import apysc as ap


def on_mousemove(e: ap.MouseEvent[ap.Circle], options: dict) -> None:
    """
    The handler that the circle calls when mousemove.

    Parameters
    ----------
    e : MouseEvent
        Event instance.
    options : dict
        Optional arguments dictionary.
    """
    circle: ap.Circle = e.this
    circle.x = e.stage_x
    circle.y = e.stage_y


def on_click(e: ap.MouseEvent[ap.Circle], options: dict) -> None:
    """
    The handler that the circle calls when clicked.

    Parameters
    ----------
    e : MouseEvent
        Event instance.
    options : dict
        Optional arguments dictionary.
    """
    circle: ap.Circle = e.this
    circle.unbind_mousemove(handler=on_mousemove)


ap.Stage(
    background_color="#333", stage_width=200, stage_height=200, stage_elem_id="stage"
)

sprite: ap.Sprite = ap.Sprite()
sprite.graphics.begin_fill(color="#0af")
circle: ap.Circle = sprite.graphics.draw_circle(x=100, y=100, radius=100)
circle.mousemove(on_mousemove)
circle.click(on_click)

ap.save_overall_html(dest_dir_path="mousemove_unbind_interface/")
```

<iframe src="static/mousemove_unbind_interface/index.html" width="200" height="200"></iframe>

また、`unbind_mousemove_all`のインターフェイスも存在し、このインターフェイスは`DisplayObject`のインスタンスからマウスを動かしたときのイベントのハンドラ設定を全て解除します。

## mousemove API

<span class="inconspicuous-txt">特記事項: このAPIドキュメントはドキュメントビルド用のスクリプトによって自動で生成・同期されています。そのためもしかしたらこの節の内容は前節までの内容と重複している場合があります。</span>

**[インターフェイスの構造]** `mousemove(self, handler: Callable[[apysc._event.mouse_event.MouseEvent, ~_O], NoneType], *, options: Union[~_O, NoneType] = None) -> str`<hr>

**[インターフェイス概要]** マウスを動かした時のイベント設定を追加します。<hr>

**[引数]**

- `handler`: _Handler
  - インスタンス上でマウスを動かした際に呼ばれる関数もしくはメソッド。

- `options`: dict or None, default None
  - ハンドラに渡される省略が可能な追加のパラメーターとしての辞書。

<hr>

**[返却値]**

- `name`: str
  - ハンドラ名。

<hr>

**[コードサンプル]**

```py
>>> import apysc as ap
>>> def on_mousemove(e: ap.MouseEvent[ap.Rectangle], options: dict) -> None:
...     stage_x: ap.Int = e.stage_x
...     ap.trace("stage_x:", stage_x)
>>> stage: ap.Stage = ap.Stage()
>>> sprite: ap.Sprite = ap.Sprite()
>>> sprite.graphics.begin_fill(color="#0af")
>>> rectangle: ap.Rectangle = sprite.graphics.draw_rect(
...     x=50, y=50, width=50, height=50
... )
>>> _ = rectangle.mousemove(on_mousemove)
```

<hr>

**[関連資料]**

- [ハンドラのoptions引数の型について](https://simon-ritchie.github.io/apysc/en/jp_about_handler_options_type.html)

## unbind_mousemove API

<span class="inconspicuous-txt">特記事項: このAPIドキュメントはドキュメントビルド用のスクリプトによって自動で生成・同期されています。そのためもしかしたらこの節の内容は前節までの内容と重複している場合があります。</span>

**[インターフェイスの構造]** `unbind_mousemove(self, handler: Callable[[apysc._event.mouse_event.MouseEvent, ~_O], NoneType]) -> None`<hr>

**[インターフェイス概要]** マウスカーソルを動かした際のイベントで指定されたハンドラの設定を解除します。<hr>

**[引数]**

- `handler`: _Handler
  - イベント設定を取り除く対象の関数やメソッドなど。

<hr>

**[コードサンプル]**

```py
>>> import apysc as ap
>>> def on_mousemove(e: ap.MouseEvent[ap.Rectangle], options: dict) -> None:
...     stage_x: ap.Int = e.stage_x
...     ap.trace("stage_x:", stage_x)
>>> def on_click(e: ap.MouseEvent[ap.Rectangle], options: dict) -> None:
...     rectangle: ap.Rectangle = e.this
...     rectangle.unbind_mousemove(on_mousemove)
>>> stage: ap.Stage = ap.Stage()
>>> sprite: ap.Sprite = ap.Sprite()
>>> sprite.graphics.begin_fill(color="#0af")
>>> rectangle: ap.Rectangle = sprite.graphics.draw_rect(
...     x=50, y=50, width=50, height=50
... )
>>> _ = rectangle.mousemove(on_mousemove)
>>> _ = rectangle.click(on_click)
```

## unbind_mousemove_all API

<span class="inconspicuous-txt">特記事項: このAPIドキュメントはドキュメントビルド用のスクリプトによって自動で生成・同期されています。そのためもしかしたらこの節の内容は前節までの内容と重複している場合があります。</span>

**[インターフェイスの構造]** `unbind_mousemove_all(self) -> None`<hr>

**[インターフェイス概要]** マウスカーソルを動かしたときのイベントの全てのハンドラ設定を解除します。<hr>

**[コードサンプル]**

```py
>>> import apysc as ap
>>> def on_mousemove(e: ap.MouseEvent[ap.Rectangle], options: dict) -> None:
...     stage_x: ap.Int = e.stage_x
...     ap.trace("stage_x:", stage_x)
>>> def on_click(e: ap.MouseEvent[ap.Rectangle], options: dict) -> None:
...     rectangle: ap.Rectangle = e.this
...     rectangle.unbind_mousemove_all()
>>> stage: ap.Stage = ap.Stage()
>>> sprite: ap.Sprite = ap.Sprite()
>>> sprite.graphics.begin_fill(color="#0af")
>>> rectangle: ap.Rectangle = sprite.graphics.draw_rect(
...     x=50, y=50, width=50, height=50
... )
>>> _ = rectangle.mousemove(on_mousemove)
>>> _ = rectangle.click(on_click)
```