<span class="inconspicuous-txt">※この翻訳ドキュメントはスクリプトによって出力・同期されています。内容が怪しそうな場合は<a href="https://github.com/simon-ritchie/apysc/issues" target="_blank">GitHubにissue</a>を追加したり[英語の原文](click.md)の確認をお願いします。</span>

# click インターフェイス

このページでは`click`インターフェイスについて説明します。

## インターフェイス概要

`click`インターフェイスは`Sprite`や`Rectangle`クラスなどの任意の`DisplayObject`のサブクラスのインスタンスにクリックイベントを設定します。これらのインターフェイスで登録されたハンドラは対象のインスタンスをクリックした際に呼ばれます。

逆に`unbind_click`インターフェイスは対象の`DisplayObject`のインスタンスからクリックイベントの登録を解除します。

## 関連資料

以下のページでは基本的なマウスイベントのインターフェイスについて説明しています。

- [基本的なマウスイベントの各インターフェイス](jp_mouse_event_basic.md)

## click インターフェイスの基本的な使い方

`DisplayObject`のサブクラスの各インスタンスは`click`メソッドを持っており、そのインターフェイスを使ってイベントのハンドラを登録することができます。

以下のコード例では四角に対してクリックのイベントハンドラを設定しています。

```py
# runnable
import apysc as ap

ap.Stage(
    background_color='#333',
    stage_width=150,
    stage_height=150,
    stage_elem_id='stage')

sprite: ap.Sprite = ap.Sprite()
sprite.graphics.begin_fill(color='#0af')


def on_click(
        e: ap.MouseEvent[ap.Rectangle], options: dict) -> None:
    """
    The handler that the rectangle calls when clicked.

    Parameters
    ----------
    e : MouseEvent
        Event instance.
    options : dict
        Optional arguments.
    """
    rectangle: ap.Rectangle = e.this
    rectangle.fill_color = ap.String('#f0a')


rectangle: ap.Rectangle = sprite.graphics.draw_rect(
    x=50, y=50, width=50, height=50)
rectangle.click(handler=on_click)

ap.save_overall_html(
    dest_dir_path='click_basic_usage_of_the_click_interface/')
```

もしも以下の四角をクリックすると四角の色はマゼンタに切り替わります。

<iframe src="static/click_basic_usage_of_the_click_interface/index.html" width="150" height="150"></iframe>

## unbind_click インターフェイスの基本的な使い方

`unbind_click`インターフェイスは`DisplayObject`のサブクラスのインスタンスから登録済みのクリックイベントの設定を取り除きます。

以下のコード例では`unbind_click`メソッドでクリックイベントを取り除いているため四角をクリックしても何も発生しません。

```py
# runnable
import apysc as ap

ap.Stage(
    background_color='#333',
    stage_width=150,
    stage_height=150,
    stage_elem_id='stage')

sprite: ap.Sprite = ap.Sprite()
sprite.graphics.begin_fill(color='#0af')


def on_click(
        e: ap.MouseEvent[ap.Rectangle], options: dict) -> None:
    """
    The handler that the rectangle calls when clicked.

    Parameters
    ----------
    e : MouseEvent
        Event instance.
    options : dict
        Optional arguments.
    """
    rectangle: ap.Rectangle = e.this
    rectangle.fill_color = ap.String('#f0a')


rectangle: ap.Rectangle = sprite.graphics.draw_rect(
    x=50, y=50, width=50, height=50)
rectangle.click(handler=on_click)
rectangle.unbind_click(handler=on_click)

ap.save_overall_html(
    dest_dir_path='click_basic_usage_of_the_unbind_click_interface/')
```

<iframe src="static/click_basic_usage_of_the_unbind_click_interface/index.html" width="150" height="150"></iframe>

## 全てのクリックのイベントハンドラを解除する

`unbind_click_all`インターフェイスは`DisplayObject`のサブクラスのインスタンスから全ての登録されているクリックイベントのハンドラを解除します。

以下のコード例では`unbind_click_all`メソッドで全てのクリックイベントの設定を取り除いており、四角をクリックしても何も起きません。

```py
# runnable
import apysc as ap

ap.Stage(
    background_color='#333',
    stage_width=150,
    stage_height=150,
    stage_elem_id='stage')

sprite: ap.Sprite = ap.Sprite()
sprite.graphics.begin_fill(color='#0af')


def on_click(
        e: ap.MouseEvent[ap.Rectangle], options: dict) -> None:
    """
    The handler that the rectangle calls when clicked.

    Parameters
    ----------
    e : MouseEvent
        Event instance.
    options : dict
        Optional arguments.
    """
    rectangle: ap.Rectangle = e.this
    rectangle.fill_color = ap.String('#f0a')


rectangle: ap.Rectangle = sprite.graphics.draw_rect(
    x=50, y=50, width=50, height=50)
rectangle.click(handler=on_click)
rectangle.unbind_click_all()

ap.save_overall_html(
    dest_dir_path='click_unbind_all_the_click_event_handlers/')
```

<iframe src="static/click_unbind_all_the_click_event_handlers/index.html" width="150" height="150"></iframe>

## click API

<span class="inconspicuous-txt">特記事項: このAPIドキュメントはドキュメントビルド用のスクリプトによって自動で生成・同期されています。そのためもしかしたらこの節の内容は前節までの内容と重複している場合があります。</span>

**[インターフェイスの構造]** `click(self, handler:Callable[[apysc._event.mouse_event.MouseEvent, ~_O], NoneType], *, options:Union[~_O, NoneType]=None) -> str`<hr>

**[インターフェイス概要]** クリックイベント用の設定を追加します。<hr>

**[引数]**

- `handler`: _Handler
  - このインスタンスをクリックした際に呼ばれるハンドラ。

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
>>> def on_click(
...         e: ap.MouseEvent[ap.Rectangle], options: dict) -> None:
...     rectangle: ap.Rectangle = e.this
...     rectangle.x += 10
>>> stage: ap.Stage = ap.Stage()
>>> sprite: ap.Sprite = ap.Sprite()
>>> sprite.graphics.begin_fill(color='#0af')
>>> rectangle: ap.Rectangle = sprite.graphics.draw_rect(
...     x=50, y=50, width=50, height=50)
>>> _ = rectangle.click(on_click)
```

<hr>

**[関連資料]**

- [ハンドラのoptions引数の型について](https://simon-ritchie.github.io/apysc/jp_about_handler_options_type.html)

## unbind_click API

<span class="inconspicuous-txt">特記事項: このAPIドキュメントはドキュメントビルド用のスクリプトによって自動で生成・同期されています。そのためもしかしたらこの節の内容は前節までの内容と重複している場合があります。</span>

**[インターフェイスの構造]** `unbind_click(self, handler:Callable[[apysc._event.mouse_event.MouseEvent, ~_O], NoneType]) -> None`<hr>

**[インターフェイス概要]** 指定されたクリックイベントのハンドラの設定を取り除きます。<hr>

**[引数]**

- `handler`: _Handler
  - 指定された関数やメソッドのハンドラの設定を解除します。

<hr>

**[コードサンプル]**

```py
>>> import apysc as ap
>>> def on_click(
...         e: ap.MouseEvent[ap.Rectangle], options: dict) -> None:
...     rectangle: ap.Rectangle = e.this
...     rectangle.fill_color = ap.String('#f0a')
...     rectangle.unbind_click(on_click)
>>> stage: ap.Stage = ap.Stage()
>>> sprite: ap.Sprite = ap.Sprite()
>>> sprite.graphics.begin_fill(color='#0af')
>>> rectangle: ap.Rectangle = sprite.graphics.draw_rect(
...     x=50, y=50, width=50, height=50)
>>> _ = rectangle.click(on_click)
```

## unbind_click_all API

<span class="inconspicuous-txt">特記事項: このAPIドキュメントはドキュメントビルド用のスクリプトによって自動で生成・同期されています。そのためもしかしたらこの節の内容は前節までの内容と重複している場合があります。</span>

**[インターフェイスの構造]** `unbind_click_all(self) -> None`<hr>

**[インターフェイス概要]** 全てのクリックイベントの設定を解除します。<hr>

**[コードサンプル]**

```py
>>> import apysc as ap
>>> def on_click(
...         e: ap.MouseEvent[ap.Rectangle], options: dict) -> None:
...     rectangle: ap.Rectangle = e.this
...     rectangle.fill_color = ap.String('#f0a')
...     rectangle.unbind_click_all()
>>> stage: ap.Stage = ap.Stage()
>>> sprite: ap.Sprite = ap.Sprite()
>>> sprite.graphics.begin_fill(color='#0af')
>>> rectangle: ap.Rectangle = sprite.graphics.draw_rect(
...     x=50, y=50, width=50, height=50)
>>> _ = rectangle.click(on_click)
```