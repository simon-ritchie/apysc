<span class="inconspicuous-txt">※この翻訳ドキュメントはスクリプトによって出力・同期されています。内容が怪しそうな場合は<a href="https://github.com/simon-ritchie/apysc/issues" target="_blank">GitHubにissue</a>を追加したり[英語の原文](https://simon-ritchie.github.io/apysc/en/mouse_event_basic.html)の確認をお願いします。</span>

# 基本的なマウスイベントの各インターフェイス

このページでは`this`属性などのマウスイベントの基本的な各インターフェイスについて説明します。

## 基本的なイベント登録処理の使い方

各マウスイベント設定のインターフェイスは`handler`と`options`引数を受け付けます。`handler`引数はイベントが発行された際に使用される関数などのオブジェクトです。

`options`引数はハンドラへ渡される追加の任意の辞書のパラメーターです。この引数は省略できます。

例えば`click`のイベントを以下のコードのように設定することができます:

```py
# runnable
from typing_extensions import TypedDict

import apysc as ap

ap.Stage(
    background_color="#333", stage_width=150, stage_height=150, stage_elem_id="stage"
)

sprite: ap.Sprite = ap.Sprite()
sprite.graphics.begin_fill(color="#0af")


class _ColorOptions(TypedDict):
    color: str


def on_rectangle_click(e: ap.MouseEvent, options: _ColorOptions) -> None:
    """
    The handler that the rectangle calls when clicked.

    Parameters
    ----------
    e : MouseEvent
        Event instance.
    options : dict
        Optional arguments.
    """
    # Change the clicked rectangle color to the passed color.
    rectangle: ap.Rectangle = e.this
    color: ap.String = ap.String(options["color"])
    rectangle.fill_color = color


rectangle: ap.Rectangle = sprite.graphics.draw_rect(x=50, y=50, width=50, height=50)
options: _ColorOptions = {"color": "#f0a"}
rectangle.click(handler=on_rectangle_click, options=options)

ap.save_overall_html(dest_dir_path="mouse_event_basic_basic_binding_usage/")
```

四角をクリックした場合、ハンドラは四角の色をパラメーターに渡された色に変更します。

<iframe src="static/mouse_event_basic_basic_binding_usage/index.html" width="150" height="150"></iframe>

`DisplayObject`の各インスタンスには`click`や`mousedown`、`mouseup`、`mouseover`、`mouseout`、`mousemove`などの様々なイベント設定用のインターフェイスがそっ歳します。

## 基本的なイベント解除処理の使い方

`DisplayObject`の各インスタンスは`unbind_click`や`unbind_mousedown`などの`unbind_<event_name>`という名前の形式のインターフェイスを持っています。

これらのインターフェイスではイベントハンドラの設定単体を解除することができます。

例えば以下のコード例ではクリックイベントを解除しているため、ハンドラの関数は呼ばれなくなります。

```py
# runnable
from typing_extensions import TypedDict

import apysc as ap

ap.Stage(
    background_color="#333", stage_width=150, stage_height=150, stage_elem_id="stage"
)

sprite: ap.Sprite = ap.Sprite()
sprite.graphics.begin_fill(color="#0af")


class _ColorOptions(TypedDict):
    color: str


def on_rectangle_click(e: ap.MouseEvent, options: _ColorOptions) -> None:
    """
    The handler that the rectangle calls when clicked.

    Parameters
    ----------
    e : MouseEvent
        Event instance.
    options : dict
        Optional arguments.
    """
    # Change the clicked rectangle color to the passed color.
    rectangle: ap.Rectangle = e.this
    color: ap.String = ap.String(options["color"])
    rectangle.fill_color = color


rectangle: ap.Rectangle = sprite.graphics.draw_rect(x=50, y=50, width=50, height=50)
options: _ColorOptions = {"color": "#f0a"}
rectangle.click(handler=on_rectangle_click, options=options)

rectangle.unbind_click(handler=on_rectangle_click)

ap.save_overall_html(dest_dir_path="mouse_event_basic_basic_unbinding_usage/")
```

以下の四角をクリックしてみても何も起こらないことが確認できます。

<iframe src="static/mouse_event_basic_basic_unbinding_usage/index.html" width="150" height="150"></iframe>

## 全てのイベントハンドラの設定を解除する

特定のイベントの設定を一括で解除するのが役立つ時があります。イベントが設定できる各インスタンスは`unbind_click_all`などの`unbind_<event_name>_all`という名前の形式のインターフェイスを持っており、それを使ってインスタンスから一通りのイベントのハンドラ設定を解除することができます。

以下のコード例では`unbind_click_all`メソッドを呼んで全てのクリックイベントのハンドラ設定を解除しています。

```py
# runnable
from typing_extensions import TypedDict

import apysc as ap

ap.Stage(
    background_color="#333", stage_width=150, stage_height=150, stage_elem_id="stage"
)

sprite: ap.Sprite = ap.Sprite()
sprite.graphics.begin_fill(color="#0af")


class _ColorOptions(TypedDict):
    color: str


def change_color_on_rectangle_click(e: ap.MouseEvent, options: _ColorOptions) -> None:
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
    color: ap.String = ap.String(options["color"])
    rectangle.fill_color = color


def change_x_on_rectangle_click(e: ap.MouseEvent, options: dict) -> None:
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
    rectangle.x += 50


rectangle: ap.Rectangle = sprite.graphics.draw_rect(x=50, y=50, width=50, height=50)
options: _ColorOptions = {"color": "#f0a"}
rectangle.click(handler=change_color_on_rectangle_click, options=options)
rectangle.click(handler=change_x_on_rectangle_click)

rectangle.unbind_click_all()

ap.save_overall_html(dest_dir_path="mouse_event_basic_unbind_all_event_handlers/")
```

四角をクリックしてみても色の変化やX座標の更新などが発生しないことを確認できます。

<iframe src="static/mouse_event_basic_unbind_all_event_handlers/index.html" width="150" height="150"></iframe>

## ハンドラの引数の名前と型

ハンドラの関数（もしくはメソッド）の第一引数は`MouseEvent`型の引数が必要になります。

また、第二引数には`options`という名前の辞書の引数が必要になります。イベント設定時にこのoptionsパラメーターの指定を省略した場合にはこの引数の値は空の辞書（`{}`）になります。

## MouseEvent クラスの this 属性

`MouseEvent`クラスのインスタンスはイベント登録対象のインスタンスとなる`this`属性を持っています。例えばクリックイベントを四角のインスタンスに設定した場合、`this`属性はその四角のインスタンスになります。

## MouseEvent クラスのジェネリック型の設定

もしもハンドラを特定の型のインスタンスのみで使うことが分かっている場合、`MouseEvent`の型アノテーションでジェネリックの型の指定を行うことができます（例: `MouseEvent[Rectangle]`）。

この設定は`this`属性の型の決定に使われ、`mypy`や`Pylance`などの型チェックのライブラリを使っている場合役立つことがあります。

```py
# runnable
import apysc as ap

ap.Stage(
    background_color="#333", stage_width=200, stage_height=150, stage_elem_id="stage"
)

sprite: ap.Sprite = ap.Sprite()
sprite.graphics.begin_fill(color="#0af")


def on_rectangle_mousedown(e: ap.MouseEvent[ap.Rectangle], options: dict) -> None:
    """
    The handler that the rectangle calls when mousedown.

    Parameters
    ----------
    e : MouseEvent
        Event instance.
    options : dict
        Optional arguments.
    """
    rectangle = e.this
    rectangle.x += 50


rectangle: ap.Rectangle = sprite.graphics.draw_rect(x=50, y=50, width=50, height=50)
rectangle.mousedown(handler=on_rectangle_mousedown)
```

## MouseEvent クラスの stage_x と stage_y 属性

MouseEventクラスのインスタンスは`stage_x`や`stage_y`の各属性のインターフェイスを持っています。これらの属性はステージの左上の位置を基準とした絶対座標となります。

```py
# runnable
import apysc as ap

ap.Stage(
    background_color="#333", stage_width=150, stage_height=200, stage_elem_id="stage"
)

sprite: ap.Sprite = ap.Sprite()
sprite.graphics.begin_fill(color="#0af")


def on_mousemove(e: ap.MouseEvent[ap.Rectangle], options: dict) -> None:
    """
    The handler that the rectangle calls when mousemove.

    Parameters
    ----------
    e : MouseEvent
        Event instance.
    options : dict
        Optional arguments.
    """
    ap.trace("stage_x:", e.stage_x, "stage_y:", e.stage_y)


rectangle: ap.Rectangle = sprite.graphics.draw_rect(x=50, y=100, width=50, height=50)
rectangle.mousemove(handler=on_mousemove)

ap.save_overall_html(dest_dir_path="mouse_event_basic_stage_x_and_stage_y")
```

F12を押してChromeなどのDevToolsを開き、以下の四角の上でマウスカーソルを動かすと`stage_x`や`stage_y`の座標値を家訓することができます。前述のコードでは四角を`(50, 100)`の位置に設定しているため、`stage_x`の値は50～100の範囲の値となり、`stage_y`の値は100～150の範囲の値となります。

<iframe src="static/mouse_event_basic_stage_x_and_stage_y/index.html" width="150" height="200"></iframe>

## MouseEvent クラスの local_x と local_y 属性

MouseEventのインスタンスは`local_x`と`local_y`という属性も持っています。これらの属性はイベントが登録されたインスタンスを基準とした相対座標となります。

以下のコード例ではlocal_xとlocal_yの座標が四角の範囲の座標になっていることを確認できます。四角のサイズが50pxなため、`local_x`と`local_y`の値は両方とも0～50の範囲になります。

```py
# runnable
import apysc as ap

ap.Stage(
    background_color="#333", stage_width=150, stage_height=150, stage_elem_id="stage"
)

sprite: ap.Sprite = ap.Sprite()
sprite.graphics.begin_fill(color="#0af")


def on_mousemove(e: ap.MouseEvent[ap.Rectangle], options: dict) -> None:
    """
    The handler that the rectangle calls when mousemove.

    Parameters
    ----------
    e : MouseEvent
        Event instance.
    options : dict
        Optional arguments.
    """
    ap.trace("local_x:", e.local_x, "local_y:", e.local_y)


rectangle: ap.Rectangle = sprite.graphics.draw_rect(x=50, y=50, width=50, height=50)
rectangle.mousemove(handler=on_mousemove)

ap.save_overall_html(dest_dir_path="mouse_event_basic_local_x_and_local_y")
```

F12を押してChromeなどのDevToolsを開き、以下の四角の上でマウスカーソルを動かしてみて出力結果を確認してみてください。

<iframe src="static/mouse_event_basic_local_x_and_local_y/index.html" width="150" height="150"></iframe>

## 関連資料

- [click インターフェイス](jp_click.md)
- [mousedown と mouseup のインターフェイス](jp_mousedown_and_mouseup.md)

- [mouseover と mouseout のインターフェイス](jp_mouseover_and_mouseout.md)
- [mousemove インターフェイス](jp_mousemove.md)

## stage_x 属性のAPI

<span class="inconspicuous-txt">特記事項: このAPIドキュメントはドキュメントビルド用のスクリプトによって自動で生成・同期されています。そのためもしかしたらこの節の内容は前節までの内容と重複している場合があります。</span>

**[インターフェイス概要]**

ステージ基準のX座標を取得します。<hr>

**[返却値]**

- `x`: Int
  - X座標。

<hr>

**[コードサンプル]**

```py
>>> import apysc as ap
>>> def on_mousedown(e: ap.MouseEvent[ap.Rectangle], options: dict) -> None:
...     stage_x: ap.Int = e.stage_x
...     # Do something here with the coordinate.
>>> stage: ap.Stage = ap.Stage()
>>> sprite: ap.Sprite = ap.Sprite()
>>> sprite.graphics.begin_fill(color="#0af")
>>> rectangle: ap.Rectangle = sprite.graphics.draw_rect(
...     x=50, y=50, width=50, height=50
... )
>>> _ = rectangle.mousedown(on_mousedown)
```

## stage_y 属性のAPI

<span class="inconspicuous-txt">特記事項: このAPIドキュメントはドキュメントビルド用のスクリプトによって自動で生成・同期されています。そのためもしかしたらこの節の内容は前節までの内容と重複している場合があります。</span>

**[インターフェイス概要]**

ステージ基準のY座標を取得します。<hr>

**[返却値]**

- `y`: Int
  - Y座標。

<hr>

**[コードサンプル]**

```py
>>> import apysc as ap
>>> def on_mousedown(e: ap.MouseEvent[ap.Rectangle], options: dict) -> None:
...     stage_y: ap.Int = e.stage_y
...     # Do something here with the coordinate.
>>> stage: ap.Stage = ap.Stage()
>>> sprite: ap.Sprite = ap.Sprite()
>>> sprite.graphics.begin_fill(color="#0af")
>>> rectangle: ap.Rectangle = sprite.graphics.draw_rect(
...     x=50, y=50, width=50, height=50
... )
>>> _ = rectangle.mousedown(on_mousedown)
```

## local_x 属性のAPI

<span class="inconspicuous-txt">特記事項: このAPIドキュメントはドキュメントビルド用のスクリプトによって自動で生成・同期されています。そのためもしかしたらこの節の内容は前節までの内容と重複している場合があります。</span>

**[インターフェイス概要]**

イベントが設定されているインスタンス内の相対座標のX座標を取得します。例えばSpriteのインスタンスをクリックした場合にはSpriteの左上の位置を基準とした座標になります。<hr>

**[返却値]**

- `x`: Int
  - X座標。

<hr>

**[コードサンプル]**

```py
>>> import apysc as ap
>>> def on_mousedown(e: ap.MouseEvent[ap.Rectangle], options: dict) -> None:
...     local_x: ap.Int = e.local_x
...     # Do something here with the coordinate.
>>> stage: ap.Stage = ap.Stage()
>>> sprite: ap.Sprite = ap.Sprite()
>>> sprite.graphics.begin_fill(color="#0af")
>>> rectangle: ap.Rectangle = sprite.graphics.draw_rect(
...     x=50, y=50, width=50, height=50
... )
>>> _ = rectangle.mousedown(on_mousedown)
```

## local_y 属性のAPI

<span class="inconspicuous-txt">特記事項: このAPIドキュメントはドキュメントビルド用のスクリプトによって自動で生成・同期されています。そのためもしかしたらこの節の内容は前節までの内容と重複している場合があります。</span>

**[インターフェイス概要]**

イベントが設定されているインスタンスないの相対座標のY座標を取得します。例えばSpriteのインスタンスをクリックした場合にはSpriteの左上の位置を基準とした座標になります。<hr>

**[返却値]**

- `y`: Int
  - Y座標。

<hr>

**[コードサンプル]**

```py
>>> import apysc as ap
>>> def on_mousedown(e: ap.MouseEvent[ap.Rectangle], options: dict) -> None:
...     local_y: ap.Int = e.local_y
...     # Do something here with the coordinate.
>>> stage: ap.Stage = ap.Stage()
>>> sprite: ap.Sprite = ap.Sprite()
>>> sprite.graphics.begin_fill(color="#0af")
>>> rectangle: ap.Rectangle = sprite.graphics.draw_rect(
...     x=50, y=50, width=50, height=50
... )
>>> _ = rectangle.mousedown(on_mousedown)
```

## this 属性のAPI

<span class="inconspicuous-txt">特記事項: このAPIドキュメントはドキュメントビルド用のスクリプトによって自動で生成・同期されています。そのためもしかしたらこの節の内容は前節までの内容と重複している場合があります。</span>

**[インターフェイス概要]**

このイベントが設定されているインスタンスを取得します。<hr>

**[返却値]**

- `this`: VariableNameMixIn
  - このイベントが設定されているインスタンス。

<hr>

**[コードサンプル]**

```py
>>> import apysc as ap
>>> def on_custom_event(e: ap.Event[ap.Rectangle], options: dict) -> None:
...     rectangle: ap.Rectangle = e.this
...     rectangle.fill_color = ap.String("#f0a")
>>> stage: ap.Stage = ap.Stage()
>>> sprite: ap.Sprite = ap.Sprite()
>>> sprite.graphics.begin_fill(color="#0af")
>>> rectangle: ap.Rectangle = sprite.graphics.draw_rect(
...     x=50, y=50, width=50, height=50
... )
>>> e: ap.Event = ap.Event(this=rectangle)
>>> _ = rectangle.bind_custom_event(
...     custom_event_type="my_custom_event", handler=on_custom_event, e=e
... )
>>> # Do something here and then trigger the custom event
>>> rectangle.trigger_custom_event(custom_event_type="my_custom_event")
```