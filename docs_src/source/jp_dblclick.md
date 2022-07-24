<span class="inconspicuous-txt">※この翻訳ドキュメントはスクリプトによって出力・同期されています。内容が怪しそうな場合は<a href="https://github.com/simon-ritchie/apysc/issues" target="_blank">GitHubにissue</a>を追加したり[英語の原文](https://simon-ritchie.github.io/apysc/en/dblclick.html)の確認をお願いします。</span>

# dblclick インターフェイス

このページでは`dblclick` (double-click)のインターフェイスについて説明します。

## インターフェイス概要

`dblclick`インターフェイスは`Sprite`や`Rectangle`などの任意の`DisplayObject`のサブクラスのインスタンスへダブルクリック時のイベントを設定します。もし登録したインスタンス上でダブルクリックした場合、登録されているハンドラの関数などが呼び出されます。

## 関連資料

以下のページでは基本的なマウスイベントの各インターフェイスについて説明しています。

- [基本的なマウスイベントの各インターフェイス](jp_mouse_event_basic.md)

## dblclick インターフェイスの基本的な使い方

`DisplayObject`のサブクラスの各インスタンスは`dblclick`メソッドを持っており、それを使ってハンドラを登録することができます。

以下のコード例では四角に対してダブルクリック時のハンドラを登録しています。対象の四角のインスタンスをダブルクリックすると四角の色はシアンからマゼンタに変化します。

```py
# runnable
import apysc as ap


def on_double_click(e: ap.MouseEvent[ap.Rectangle], options: dict) -> None:
    """
    The handler that the rectangle calls when double-clicked.

    Parameters
    ----------
    e : ap.MouseEvent
        Event instance.
    options : dict
        Optional arguments dictionary.
    """
    rectangle: ap.Rectangle = e.this
    rectangle.fill_color = ap.String("#f0a")


ap.Stage(
    stage_width=150, stage_height=150, background_color="#333", stage_elem_id="stage"
)
sprite: ap.Sprite = ap.Sprite()
sprite.graphics.begin_fill(color="#0af")
rectangle: ap.Rectangle = sprite.graphics.draw_rect(x=50, y=50, width=50, height=50)
rectangle.dblclick(on_double_click)

ap.save_overall_html(dest_dir_path="./dblclick_basic_usage/")
```

<iframe src="static/dblclick_basic_usage/index.html" width="150" height="150"></iframe>

## unbind_dblclick の各インターフェイスの基本的な使い方

`unbind_dblclick`インターフェイスは`DisplayObject`のサブクラスの任意のインスタンスからダブルクリックイベントのハンドラの設定を取り除きます。また、`unbind_dblclick_all`インターフェイスは対象のインスタンスに設定されているダブルクリックのハンドラ設定を全て取り除きます。

以下のコード例では`unbind_dblclick`メソッドでダブルクリックのイベント設定を取り除いているため、四角をダブルクリックしても何も起きません。

```py
# runnable
import apysc as ap


def on_double_click(e: ap.MouseEvent[ap.Rectangle], options: dict) -> None:
    """
    The handler that the rectangle calls when double-clicked.

    Parameters
    ----------
    e : ap.MouseEvent
        Event instance.
    options : dict
        Optional arguments dictionary.
    """
    rectangle: ap.Rectangle = e.this
    rectangle.fill_color = ap.String("#f0a")


ap.Stage(
    stage_width=150, stage_height=150, background_color="#333", stage_elem_id="stage"
)
sprite: ap.Sprite = ap.Sprite()
sprite.graphics.begin_fill(color="#0af")
rectangle: ap.Rectangle = sprite.graphics.draw_rect(x=50, y=50, width=50, height=50)
rectangle.dblclick(on_double_click)
rectangle.unbind_dblclick(on_double_click)

ap.save_overall_html(dest_dir_path="./unbind_dblclick_basic_usage/")
```

<iframe src="static/unbind_dblclick_basic_usage/index.html" width="150" height="150"></iframe>

## dblclick API

<span class="inconspicuous-txt">特記事項: このAPIドキュメントはドキュメントビルド用のスクリプトによって自動で生成・同期されています。そのためもしかしたらこの節の内容は前節までの内容と重複している場合があります。</span>

**[インターフェイスの構造]** `dblclick(self, handler: Callable[[apysc._event.mouse_event.MouseEvent, ~_O], NoneType], *, options: Union[~_O, NoneType] = None) -> str`<hr>

**[インターフェイス概要]** ダブルクリック時のイベント設定を追加します。<hr>

**[引数]**

- `handler`: _Handler
  - このインスタンスをダブルクリックした際に呼ばれる関数やメソッドのハンドラ。

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
>>> def on_double_click(e: ap.MouseEvent[ap.Rectangle], options: dict) -> None:
...     rectangle: ap.Rectangle = e.this
...     rectangle.fill_color = ap.String("#f0a")
>>> stage: ap.Stage = ap.Stage()
>>> sprite: ap.Sprite = ap.Sprite()
>>> sprite.graphics.begin_fill(color="#0af")
>>> rectangle: ap.Rectangle = sprite.graphics.draw_rect(
...     x=50, y=50, width=50, height=50
... )
>>> _ = rectangle.dblclick(on_double_click)
```

<hr>

**[関連資料]**

- [ハンドラのoptions引数の型について](https://simon-ritchie.github.io/apysc/en/jp_about_handler_options_type.html)

## unbind_dblclick API

<span class="inconspicuous-txt">特記事項: このAPIドキュメントはドキュメントビルド用のスクリプトによって自動で生成・同期されています。そのためもしかしたらこの節の内容は前節までの内容と重複している場合があります。</span>

**[インターフェイスの構造]** `unbind_dblclick(self, handler: Callable[[apysc._event.mouse_event.MouseEvent, ~_O], NoneType]) -> None`<hr>

**[インターフェイス概要]** 指定されたハンドラのダブルクリック時のイベント設定を取り除きます。<hr>

**[引数]**

- `handler`: _Handler
  - イベント設定を取り除く対象の関数やメソッドなど。

<hr>

**[コードサンプル]**

```py
>>> import apysc as ap
>>> def on_double_click(e: ap.MouseEvent[ap.Rectangle], options: dict) -> None:
...     rectangle: ap.Rectangle = e.this
...     rectangle.fill_color = ap.String("#f0a")
...     rectangle.unbind_dblclick(on_double_click)
>>> stage: ap.Stage = ap.Stage()
>>> sprite: ap.Sprite = ap.Sprite()
>>> sprite.graphics.begin_fill(color="#0af")
>>> rectangle: ap.Rectangle = sprite.graphics.draw_rect(
...     x=50, y=50, width=50, height=50
... )
>>> _ = rectangle.dblclick(on_double_click)
```

## unbind_dblclick_all API

<span class="inconspicuous-txt">特記事項: このAPIドキュメントはドキュメントビルド用のスクリプトによって自動で生成・同期されています。そのためもしかしたらこの節の内容は前節までの内容と重複している場合があります。</span>

**[インターフェイスの構造]** `unbind_dblclick_all(self) -> None`<hr>

**[インターフェイス概要]** 全てのダブルクリック時のイベント設定を取り除きます。<hr>

**[コードサンプル]**

```py
>>> import apysc as ap
>>> def on_double_click(e: ap.MouseEvent[ap.Rectangle], options: dict) -> None:
...     rectangle: ap.Rectangle = e.this
...     rectangle.fill_color = ap.String("#f0a")
...     rectangle.unbind_dblclick_all()
>>> stage: ap.Stage = ap.Stage()
>>> sprite: ap.Sprite = ap.Sprite()
>>> sprite.graphics.begin_fill(color="#0af")
>>> rectangle: ap.Rectangle = sprite.graphics.draw_rect(
...     x=50, y=50, width=50, height=50
... )
>>> _ = rectangle.dblclick(on_double_click)
```