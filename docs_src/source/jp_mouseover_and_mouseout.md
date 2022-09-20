<span class="inconspicuous-txt">※この翻訳ドキュメントはスクリプトによって出力・同期されています。内容が怪しそうな場合は<a href="https://github.com/simon-ritchie/apysc/issues" target="_blank">GitHubにissue</a>を追加したり[英語の原文](https://simon-ritchie.github.io/apysc/en/mouseover_and_mouseout.html)の確認をお願いします。</span>

# mouseover と mouseout のインターフェイス

このページでは`mouseover`と`mouseout`の各インターフェイスについて説明します。

## 各インターフェイスの概要

`mouseover`インターフェイスはマウスカーソルが対象の`DisplayObject`インスタンス上に乗った時のイベントのハンドラを設定します。逆に`mouseout`インターフェイスはマウスカーソルが対象の`DisplayObject`上から離れた時のイベントのハンドラを設定します。

## 関連資料

以下のページでは基本的なマウスイベントの各インターフェイスについて説明しています。

- [基本的なマウスイベントの各インターフェイス](jp_mouse_event_basic.md)

## mouseover と mouseout の各インターフェイスの基本的な使い方

`DisplayObject`の各インスタンスは`mouseover`と`mouseout`の各インターフェイスを持っており、それらを使ってハンドラを設定することができます。

以下のコード例ではマウスが乗った時と離れた時のイベントのハンドラを四角に対して設定しています。四角にマウスカーソルが乗った時に四角の色が変更され、カーソルが離れた時に色が戻されるように設定してあります。

```py
# runnable
import apysc as ap


def on_mouseover(e: ap.MouseEvent[ap.Rectangle], options: dict) -> None:
    """
    The handler that the rectangle calls when mouseover.

    Parameters
    ----------
    e : MouseEvent
        Event instance.
    options : dict
        Optional arguments dictionary.
    """
    rectangle: ap.Rectangle = e.this

    # Change the rectangle fill color to magenta.
    rectangle.fill_color = ap.String("#f0a")


def on_mouseout(e: ap.MouseEvent[ap.Rectangle], options: dict) -> None:
    """
    The handler that the rectangle calls when mouseout.

    Parameters
    ----------
    e : MouseEvent
        Event instance.
    options : dict
        Optional arguments dictionary.
    """
    rectangle: ap.Rectangle = e.this

    # Revert the rectangle fill color.
    rectangle.fill_color = ap.String("#0af")


ap.Stage(
    background_color="#333", stage_width=150, stage_height=150, stage_elem_id="stage"
)

sprite: ap.Sprite = ap.Sprite()

sprite.graphics.begin_fill(color="#0af")
rectangle: ap.Rectangle = sprite.graphics.draw_rect(x=50, y=50, width=50, height=50)

# Bind the mouse over and mouse out event handlers to the rectangle.
rectangle.mouseover(on_mouseover)
rectangle.mouseout(on_mouseout)

ap.save_overall_html(dest_dir_path="mouseover_and_mouseout_basic_usage/")
```

<iframe src="static/mouseover_and_mouseout_basic_usage/index.html" width="150" height="150"></iframe>

## 解除用のインターフェイス

`unbind_mouseover`と`unbind_mouseout`の各インターフェイスは`DisplayObject`から登録されているハンドラの設定を解除します。

以下のコード例では`on_mouseover`と`on_mouseout`のハンドラの関数内でハンドラの設定を解除しているためこれらのハンドラは最初の1回のみ呼ばれます。

```py
# runnable
import apysc as ap


def on_mouseover(e: ap.MouseEvent[ap.Rectangle], options: dict) -> None:
    """
    The handler that the rectangle calls when mouseover.

    Parameters
    ----------
    e : MouseEvent
        Event instance.
    options : dict
        Optional arguments dictionary.
    """
    rectangle: ap.Rectangle = e.this
    rectangle.fill_color = ap.String("#f0a")

    # Unbind the mouseover handler.
    rectangle.unbind_mouseover(handler=on_mouseover)


def on_mouseout(e: ap.MouseEvent[ap.Rectangle], options: dict) -> None:
    """
    The handler that the rectangle calls when mouseout.

    Parameters
    ----------
    e : MouseEvent
        Event instance.
    options : dict
        Optional arguments dictionary.
    """
    rectangle: ap.Rectangle = e.this
    rectangle.fill_color = ap.String("#0af")

    rectangle.unbind_mouseout(handler=on_mouseout)


ap.Stage(
    background_color="#333", stage_width=150, stage_height=150, stage_elem_id="stage"
)

sprite: ap.Sprite = ap.Sprite()

sprite.graphics.begin_fill(color="#0af")
rectangle: ap.Rectangle = sprite.graphics.draw_rect(x=50, y=50, width=50, height=50)

rectangle.mouseover(on_mouseover)
rectangle.mouseout(on_mouseout)

ap.save_overall_html(dest_dir_path="mouseover_and_mouseout_unbind_interfaces/")
```

<iframe src="static/mouseover_and_mouseout_unbind_interfaces/index.html" width="150" height="150"></iframe>

`unbind_mouseover_all`と`unbind_mouseout_all`の各インターフェイスも存在します。これらのインターフェイスは対象の`DisplayObject`のインスタンスから対象のイベントのハンドラ設定を全て解除します。

## mouseover API

<span class="inconspicuous-txt">特記事項: このAPIドキュメントはドキュメントビルド用のスクリプトによって自動で生成・同期されています。そのためもしかしたらこの節の内容は前節までの内容と重複している場合があります。</span>

**[インターフェイスの構造]** `mouseover(self, handler: Callable[[apysc._event.mouse_event.MouseEvent, ~_O], NoneType], *, options: Union[~_O, NoneType] = None) -> str`<hr>

**[インターフェイス概要]**

マウスカーソルが乗った時のイベントのハンドラ設定を追加します。<hr>

**[引数]**

- `handler`: _Handler
  - インスタンス上にマウスカーソルが乗った際に呼ばれる関数もしくはメソッド。

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
>>> def on_mouseover(e: ap.MouseEvent[ap.Rectangle], options: dict) -> None:
...     rectangle: ap.Rectangle = e.this
...     rectangle.fill_color = ap.String("#f0a")
>>> stage: ap.Stage = ap.Stage()
>>> sprite: ap.Sprite = ap.Sprite()
>>> sprite.graphics.begin_fill(color="#0af")
>>> rectangle: ap.Rectangle = sprite.graphics.draw_rect(
...     x=50, y=50, width=50, height=50
... )
>>> _ = rectangle.mouseout(on_mouseover)
```

<hr>

**[関連資料]**

- [ハンドラのoptions引数の型について](https://simon-ritchie.github.io/apysc/jp/jp_about_handler_options_type.html)

## unbind_mouseover API

<span class="inconspicuous-txt">特記事項: このAPIドキュメントはドキュメントビルド用のスクリプトによって自動で生成・同期されています。そのためもしかしたらこの節の内容は前節までの内容と重複している場合があります。</span>

**[インターフェイスの構造]** `unbind_mouseover(self, handler: Callable[[apysc._event.mouse_event.MouseEvent, ~_O], NoneType]) -> None`<hr>

**[インターフェイス概要]**

マウスカーソルが乗った際のイベントの指定されたハンドラ設定を解除します。<hr>

**[引数]**

- `handler`: _Handler
  - イベント設定を取り除く対象の関数やメソッドなど。

<hr>

**[コードサンプル]**

```py
>>> import apysc as ap
>>> def on_mouseover(e: ap.MouseEvent[ap.Rectangle], options: dict) -> None:
...     rectangle: ap.Rectangle = e.this
...     rectangle.fill_color = ap.String("#f0a")
...     rectangle.unbind_mouseover(on_mouseover)
>>> stage: ap.Stage = ap.Stage()
>>> sprite: ap.Sprite = ap.Sprite()
>>> sprite.graphics.begin_fill(color="#0af")
>>> rectangle: ap.Rectangle = sprite.graphics.draw_rect(
...     x=50, y=50, width=50, height=50
... )
>>> _ = rectangle.mouseout(on_mouseover)
```

## unbind_mouseover_all API

<span class="inconspicuous-txt">特記事項: このAPIドキュメントはドキュメントビルド用のスクリプトによって自動で生成・同期されています。そのためもしかしたらこの節の内容は前節までの内容と重複している場合があります。</span>

**[インターフェイスの構造]** `unbind_mouseover_all(self) -> None`<hr>

**[インターフェイス概要]**

マウスカーソルが乗った際のイベントの全てのハンドラ設定を解除します。<hr>

**[コードサンプル]**

```py
>>> import apysc as ap
>>> def on_mouseover(e: ap.MouseEvent[ap.Rectangle], options: dict) -> None:
...     rectangle: ap.Rectangle = e.this
...     rectangle.fill_color = ap.String("#f0a")
...     rectangle.unbind_mouseover_all()
>>> stage: ap.Stage = ap.Stage()
>>> sprite: ap.Sprite = ap.Sprite()
>>> sprite.graphics.begin_fill(color="#0af")
>>> rectangle: ap.Rectangle = sprite.graphics.draw_rect(
...     x=50, y=50, width=50, height=50
... )
>>> _ = rectangle.mouseout(on_mouseover)
```

## mouseout API

<span class="inconspicuous-txt">特記事項: このAPIドキュメントはドキュメントビルド用のスクリプトによって自動で生成・同期されています。そのためもしかしたらこの節の内容は前節までの内容と重複している場合があります。</span>

**[インターフェイスの構造]** `mouseout(self, handler: Callable[[apysc._event.mouse_event.MouseEvent, ~_O], NoneType], *, options: Union[~_O, NoneType] = None) -> str`<hr>

**[インターフェイス概要]**

マウスカーソルがインスタンス上から離れた際のイベントのハンドラを設定します。<hr>

**[引数]**

- `handler`: _Handler
  - インスタンス上からマウスカーソルが離れた際のイベントの対象のハンドラ設定を解除します。

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
>>> def on_mouseout(e: ap.MouseEvent[ap.Rectangle], options: dict) -> None:
...     rectangle: ap.Rectangle = e.this
...     rectangle.fill_color = ap.String("#f0a")
>>> stage: ap.Stage = ap.Stage()
>>> sprite: ap.Sprite = ap.Sprite()
>>> sprite.graphics.begin_fill(color="#0af")
>>> rectangle: ap.Rectangle = sprite.graphics.draw_rect(
...     x=50, y=50, width=50, height=50
... )
>>> _ = rectangle.mouseout(on_mouseout)
```

<hr>

**[関連資料]**

- [ハンドラのoptions引数の型について](https://simon-ritchie.github.io/apysc/jp/jp_about_handler_options_type.html)

## unbind_mouseout API

<span class="inconspicuous-txt">特記事項: このAPIドキュメントはドキュメントビルド用のスクリプトによって自動で生成・同期されています。そのためもしかしたらこの節の内容は前節までの内容と重複している場合があります。</span>

**[インターフェイスの構造]** `unbind_mouseout(self, handler: Callable[[apysc._event.mouse_event.MouseEvent, ~_O], NoneType]) -> None`<hr>

**[インターフェイス概要]**

インスタンス上からマウスカーソルが離れた際のイベントの対象のハンドラ設定を解除します。<hr>

**[引数]**

- `handler`: _Handler
  - イベント設定を取り除く対象の関数やメソッドなど。

<hr>

**[コードサンプル]**

```py
>>> import apysc as ap
>>> def on_mouseout(e: ap.MouseEvent[ap.Rectangle], options: dict) -> None:
...     rectangle: ap.Rectangle = e.this
...     rectangle.fill_color = ap.String("#f0a")
...     rectangle.unbind_mouseout(on_mouseout)
>>> stage: ap.Stage = ap.Stage()
>>> sprite: ap.Sprite = ap.Sprite()
>>> sprite.graphics.begin_fill(color="#0af")
>>> rectangle: ap.Rectangle = sprite.graphics.draw_rect(
...     x=50, y=50, width=50, height=50
... )
>>> _ = rectangle.mouseout(on_mouseout)
```

## unbind_mouseout_all API

<span class="inconspicuous-txt">特記事項: このAPIドキュメントはドキュメントビルド用のスクリプトによって自動で生成・同期されています。そのためもしかしたらこの節の内容は前節までの内容と重複している場合があります。</span>

**[インターフェイスの構造]** `unbind_mouseout_all(self) -> None`<hr>

**[インターフェイス概要]**

インスタンス上からマウスカーソルが離れた際のイベントのハンドラ設定を全て解除します。<hr>

**[コードサンプル]**

```py
>>> import apysc as ap
>>> def on_mouseout(e: ap.MouseEvent[ap.Rectangle], options: dict) -> None:
...     rectangle: ap.Rectangle = e.this
...     rectangle.fill_color = ap.String("#f0a")
...     rectangle.unbind_mouseout_all()
>>> stage: ap.Stage = ap.Stage()
>>> sprite: ap.Sprite = ap.Sprite()
>>> sprite.graphics.begin_fill(color="#0af")
>>> rectangle: ap.Rectangle = sprite.graphics.draw_rect(
...     x=50, y=50, width=50, height=50
... )
>>> _ = rectangle.mouseout(on_mouseout)
```