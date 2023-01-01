<span class="inconspicuous-txt">※この翻訳ドキュメントはスクリプトによって出力・同期されています。内容が怪しそうな場合は<a href="https://github.com/simon-ritchie/apysc/issues" target="_blank">GitHubにissue</a>を追加したり[英語の原文](https://simon-ritchie.github.io/apysc/en/mousedown_and_mouseup.html)の確認をお願いします。</span>

# mousedown と mouseup のインターフェイス

このページでは`mousedown`や`mouseup`の各インターフェイスについて説明します。

## 各インターフェイスの概要

`mousedown`インターフェイスは`DisplayObject`のインスタンス上でマウスを押した時のイベントのハンドラを設定するためのインターフェイスです。逆に`mouseup`インターフェイスはマウスから指を離した（押している状態を解除した）時のイベントのハンドラを設定するためのインターフェイスです。

## 関連資料

以下のページでは基本的なマウスイベントのインターフェイスについて説明しています:

- [基本的なマウスイベントの各インターフェイス](jp_mouse_event_basic.md)

## mousedown と mouseup のインターフェイスの基本的な使い方

`DisplayObject`の各インスタンスは`mousedown`と`mouseup`のメソッドのインターフェイスを持っており、それらを使ってハンドラを設定することができます。

以下のコード例では四角に対してマウスを押した時と離した時のハンドラをそれぞれ設定しています。ハンドラではマウスを押した時に四角の色を変更し、マウスを離した時に元の色に戻しています。

```py
# runnable
import apysc as ap


def on_mousedown(e: ap.MouseEvent[ap.Rectangle], options: dict) -> None:
    """
    The handler that the rectangle calls when mousedown.

    Parameters
    ----------
    e : MouseEvent
        Event instance.
    options : dict
        Optional arguments dictionary.
    """
    rectangle: ap.Rectangle = e.this
    rectangle.fill_color = ap.String("#f0a")


def on_mouseup(e: ap.MouseEvent[ap.Rectangle], options: dict) -> None:
    """
    The handler that the rectangle calls when mouseup.

    Parameters
    ----------
    e : MouseEvent
        Event instance.
    options : dict
        Optional arguments dictionary.
    """
    rectangle: ap.Rectangle = e.this
    rectangle.fill_color = ap.String("#0af")


ap.Stage(
    background_color="#333", stage_width=150, stage_height=150, stage_elem_id="stage"
)

sprite: ap.Sprite = ap.Sprite()
sprite.graphics.begin_fill(color="#0af")
rectangle: ap.Rectangle = sprite.graphics.draw_rect(x=50, y=50, width=50, height=50)

# Bind each handler to the rectangle.
rectangle.mousedown(on_mousedown)
rectangle.mouseup(on_mouseup)

ap.save_overall_html(dest_dir_path="mousedown_and_mouseup_basic_usage/")
```

<iframe src="static/mousedown_and_mouseup_basic_usage/index.html" width="150" height="150"></iframe>

## 解除用のインターフェイス

`unbind_mousedown`と`unbind_mouseup`は`DisplayObject`のインスタンスから設定されているハンドラの設定を解除します。

以下のコード例では`on_mousedown`と`on_mouseup`の各ハンドラ内でハンドラの設定を解除しているためハンドラの処理は1回のみ実行されます。

```py
# runnable
import apysc as ap


def on_mousedown(e: ap.MouseEvent[ap.Rectangle], options: dict) -> None:
    """
    The handler that the rectangle calls when mousedown.

    Parameters
    ----------
    e : MouseEvent
        Event instance.
    options : dict
        Optional arguments dictionary.
    """
    rectangle: ap.Rectangle = e.this
    rectangle.unbind_mousedown(handler=on_mousedown)
    rectangle.fill_color = ap.String("#f0a")


def on_mouseup(e: ap.MouseEvent[ap.Rectangle], options: dict) -> None:
    """
    The handler that the rectangle calls when mouseup.

    Parameters
    ----------
    e : MouseEvent
        Event instance.
    options : dict
        Optional arguments dictionary.
    """
    rectangle: ap.Rectangle = e.this
    rectangle.unbind_mouseup(handler=on_mouseup)
    rectangle.fill_color = ap.String("#0af")


ap.Stage(
    background_color="#333", stage_width=150, stage_height=150, stage_elem_id="stage"
)

sprite: ap.Sprite = ap.Sprite()
sprite.graphics.begin_fill(color="#0af")
rectangle: ap.Rectangle = sprite.graphics.draw_rect(x=50, y=50, width=50, height=50)

rectangle.mousedown(on_mousedown)
rectangle.mouseup(on_mouseup)

ap.save_overall_html(dest_dir_path="mousedown_and_mouseup_unbind_interfaces/")
```

<iframe src="static/mousedown_and_mouseup_unbind_interfaces/index.html" width="150" height="150"></iframe>

また、`unbind_mousedown_all`や`unbind_mouseup_all`などのインターフェイスも存在します。これらのインターフェイスは`DisplayObject`のインスタンスから該当のイベントのハンドラ設定を全て取り除きます。

## mousedown API

<span class="inconspicuous-txt">特記事項: このAPIドキュメントはドキュメントビルド用のスクリプトによって自動で生成・同期されています。そのためもしかしたらこの節の内容は前節までの内容と重複している場合があります。</span>

**[インターフェイスの構造]** `mousedown(self, handler: Callable[[apysc._event.mouse_event.MouseEvent, ~_Options], NoneType], *, options: Union[~_Options, NoneType] = None) -> str`<hr>

**[インターフェイス概要]**

マウスのボタンを押した時のイベント設定を追加します。<hr>

**[引数]**

- `handler`: _Handler
  - インスタンス上でマウスのボタンを押した時に呼ばれる関数もしくはメソッド。

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
>>> def on_mousedown(e: ap.MouseEvent[ap.Rectangle], options: dict) -> None:
...     rectangle: ap.Rectangle = e.this
...     rectangle.fill_color = ap.String("#f0a")
>>> stage: ap.Stage = ap.Stage()
>>> sprite: ap.Sprite = ap.Sprite()
>>> sprite.graphics.begin_fill(color="#0af")
>>> rectangle: ap.Rectangle = sprite.graphics.draw_rect(
...     x=50, y=50, width=50, height=50
... )
>>> _ = rectangle.mousedown(on_mousedown)
```

<hr>

**[関連資料]**

- [ハンドラのoptions引数の型について](https://simon-ritchie.github.io/apysc/jp/jp_about_handler_options_type.html)

## unbind_mousedown API

<span class="inconspicuous-txt">特記事項: このAPIドキュメントはドキュメントビルド用のスクリプトによって自動で生成・同期されています。そのためもしかしたらこの節の内容は前節までの内容と重複している場合があります。</span>

**[インターフェイスの構造]** `unbind_mousedown(self, handler: Callable[[apysc._event.mouse_event.MouseEvent, ~_Options], NoneType]) -> None`<hr>

**[インターフェイス概要]**

マウスのボタンを押した際のイベントの指定されたハンドラ設定を解除します。<hr>

**[引数]**

- `handler`: _Handler
  - イベント設定を取り除く対象の関数やメソッドなど。

<hr>

**[コードサンプル]**

```py
>>> import apysc as ap
>>> def on_mousedown(e: ap.MouseEvent[ap.Rectangle], options: dict) -> None:
...     rectangle: ap.Rectangle = e.this
...     rectangle.fill_color = ap.String("#f0a")
...     rectangle.unbind_mousedown(on_mousedown)
>>> stage: ap.Stage = ap.Stage()
>>> sprite: ap.Sprite = ap.Sprite()
>>> sprite.graphics.begin_fill(color="#0af")
>>> rectangle: ap.Rectangle = sprite.graphics.draw_rect(
...     x=50, y=50, width=50, height=50
... )
>>> _ = rectangle.mousedown(on_mousedown)
```

## unbind_mousedown_all API

<span class="inconspicuous-txt">特記事項: このAPIドキュメントはドキュメントビルド用のスクリプトによって自動で生成・同期されています。そのためもしかしたらこの節の内容は前節までの内容と重複している場合があります。</span>

**[インターフェイスの構造]** `unbind_mousedown_all(self) -> None`<hr>

**[インターフェイス概要]**

マウスのボタンを押した時のイベントの全てのハンドラ設定を解除します。<hr>

**[コードサンプル]**

```py
>>> import apysc as ap
>>> def on_mousedown(e: ap.MouseEvent[ap.Rectangle], options: dict) -> None:
...     rectangle: ap.Rectangle = e.this
...     rectangle.fill_color = ap.String("#f0a")
...     rectangle.unbind_mousedown_all()
>>> stage: ap.Stage = ap.Stage()
>>> sprite: ap.Sprite = ap.Sprite()
>>> sprite.graphics.begin_fill(color="#0af")
>>> rectangle: ap.Rectangle = sprite.graphics.draw_rect(
...     x=50, y=50, width=50, height=50
... )
>>> _ = rectangle.mousedown(on_mousedown)
```

## mouseup API

<span class="inconspicuous-txt">特記事項: このAPIドキュメントはドキュメントビルド用のスクリプトによって自動で生成・同期されています。そのためもしかしたらこの節の内容は前節までの内容と重複している場合があります。</span>

**[インターフェイスの構造]** `mouseup(self, handler: Callable[[apysc._event.mouse_event.MouseEvent, ~_Options], NoneType], *, options: Union[~_Options, NoneType] = None) -> str`<hr>

**[インターフェイス概要]**

マウスのボタンを離した時のイベント設定を追加します。<hr>

**[引数]**

- `handler`: _Handler
  - インスタンス上でマウスのボタンを離した時に呼ばれる関数もしくはメソッド。

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
>>> def on_mouseup(e: ap.MouseEvent[ap.Rectangle], options: dict) -> None:
...     rectangle: ap.Rectangle = e.this
...     rectangle.fill_color = ap.String("#f0a")
>>> stage: ap.Stage = ap.Stage()
>>> sprite: ap.Sprite = ap.Sprite()
>>> sprite.graphics.begin_fill(color="#0af")
>>> rectangle: ap.Rectangle = sprite.graphics.draw_rect(
...     x=50, y=50, width=50, height=50
... )
>>> _ = rectangle.mouseup(on_mouseup)
```

<hr>

**[関連資料]**

- [ハンドラのoptions引数の型について](https://simon-ritchie.github.io/apysc/jp/jp_about_handler_options_type.html)

## unbind_mouseup API

<span class="inconspicuous-txt">特記事項: このAPIドキュメントはドキュメントビルド用のスクリプトによって自動で生成・同期されています。そのためもしかしたらこの節の内容は前節までの内容と重複している場合があります。</span>

**[インターフェイスの構造]** `unbind_mouseup(self, handler: Callable[[apysc._event.mouse_event.MouseEvent, ~_Options], NoneType]) -> None`<hr>

**[インターフェイス概要]**

マウスのボタンを離した際のイベントの指定されたハンドラ設定を解除します。<hr>

**[引数]**

- `handler`: _Handler
  - イベント設定を取り除く対象の関数やメソッドなど。

<hr>

**[コードサンプル]**

```py
>>> import apysc as ap
>>> def on_mouseup(e: ap.MouseEvent[ap.Rectangle], options: dict) -> None:
...     rectangle: ap.Rectangle = e.this
...     rectangle.fill_color = ap.String("#f0a")
...     rectangle.unbind_mouseup(on_mouseup)
>>> stage: ap.Stage = ap.Stage()
>>> sprite: ap.Sprite = ap.Sprite()
>>> sprite.graphics.begin_fill(color="#0af")
>>> rectangle: ap.Rectangle = sprite.graphics.draw_rect(
...     x=50, y=50, width=50, height=50
... )
>>> _ = rectangle.mouseup(on_mouseup)
```

## unbind_mouseup_all API

<span class="inconspicuous-txt">特記事項: このAPIドキュメントはドキュメントビルド用のスクリプトによって自動で生成・同期されています。そのためもしかしたらこの節の内容は前節までの内容と重複している場合があります。</span>

**[インターフェイスの構造]** `unbind_mouseup_all(self) -> None`<hr>

**[インターフェイス概要]**

マウスのボタンを離したとぎのイベントの全てのハンドラ設定を解除します。<hr>

**[コードサンプル]**

```py
>>> import apysc as ap
>>> def on_mouseup(e: ap.MouseEvent[ap.Rectangle], options: dict) -> None:
...     rectangle: ap.Rectangle = e.this
...     rectangle.fill_color = ap.String("#f0a")
...     rectangle.unbind_mouseup_all()
>>> stage: ap.Stage = ap.Stage()
>>> sprite: ap.Sprite = ap.Sprite()
>>> sprite.graphics.begin_fill(color="#0af")
>>> rectangle: ap.Rectangle = sprite.graphics.draw_rect(
...     x=50, y=50, width=50, height=50
... )
>>> _ = rectangle.mouseup(on_mouseup)
```