<span class="inconspicuous-txt">※この翻訳ドキュメントはスクリプトによって出力・同期されています。内容が怪しそうな場合は<a href="https://github.com/simon-ritchie/apysc/issues" target="_blank">GitHubにissue</a>を追加したり[英語の原文](https://simon-ritchie.github.io/apysc/en/bind_and_trigger_custom_event.html)の確認をお願いします。</span>

# カスタムイベントの登録とイベントの発生（発火）制御

このページでは`bind_custom_event`と`trigger_custom_event`の各インターフェイスについて説明します。

## 各インターフェイスの概要

`bind_custom_event`インターフェイスは対象のインスタンスに独自のイベントを登録し、`trigger_custom_event`インターフェイスは任意の箇所でカスタムイベントの発生（発火）の制御を行います。

## 基本的な使い方

`bind_custom_event`インターフェイスは`custom_event_type`と`handler`、`e`、そして`options`引数を持っています（`options`引数は省略可です）。

`custom_event_type`引数は独自のイベントの種類の文字列です。この引数の文字列は`trigger_custom_event`インターフェイスでの指定時でも同じ値を設定する必要があります。

`e`引数はイベントのインスタンスです。場合によっては`MouseEvent`クラスや`TimerEvent`クラスなどの`Event`クラスのサブクラスを指定します。

以下のコード例では四角をクリックした際に回転させるようにしています。もし回転量が90度に達した場合、`rotate_90_degrees`の独自のイベントが発生し`on_rotate_90_degrees`関数のハンドラが実行されます。対象のハンドラ内では2つ目の四角を`visible`属性を有効化する形で表示しています。

```py
# runnable
from typing_extensions import TypedDict

import apysc as ap

# Custom event type name.
ROTATE_90_DEGREES: str = "rotate_90_degrees"


class _RectOptions(TypedDict):
    rectangle: ap.Rectangle


def on_rectangle_click(e: ap.MouseEvent[ap.Rectangle], options: dict) -> None:
    """
    The handler that the rectangle calls when clicked.

    Parameters
    ----------
    e : ap.MouseEvent
        Event instance.
    options : dict
        Optional arguments dictionary.
    """
    e.this.unbind_click(on_rectangle_click)
    options_: _RectOptions = {"rectangle": e.this}
    timer: ap.Timer = ap.Timer(
        on_timer, delay=ap.FPS.FPS_60, repeat_count=90, options=options_
    )
    timer.timer_complete(on_timer_complete, options=options_)
    timer.start()


def on_timer(e: ap.TimerEvent, options: _RectOptions) -> None:
    """
    The handler that the timer calls.

    Parameters
    ----------
    e : ap.TimerEvent
        Event instance.
    options : dict
        Optional arguments dictionary.
    """
    rectangle: ap.Rectangle = options["rectangle"]
    rectangle.rotation_around_center += 1


def on_timer_complete(e: ap.TimerEvent, options: _RectOptions) -> None:
    """
    The handler that timer calls when its end.

    Parameters
    ----------
    e : ap.TimerEvent
        Event instance.
    options : dict
        Optional arguments dictionary.
    """
    rectangle: ap.Rectangle = options["rectangle"]
    rectangle.trigger_custom_event(custom_event_type=ROTATE_90_DEGREES)


def on_rotate_90_degrees(e: ap.Event, options: _RectOptions) -> None:
    """
    The handler that the rectangle rates 90 degrees (custom event).

    Parameters
    ----------
    e : ap.Event
        Event instance.
    options : dict
        Optional arguments dictionary.
    """
    rectangle: ap.Rectangle = options["rectangle"]
    rectangle.visible = ap.Boolean(True)


ap.Stage(
    stage_width=250,
    stage_height=150,
    background_color=ap.Color("#333"),
    stage_elem_id="stage",
)
sprite: ap.Sprite = ap.Sprite()
sprite.graphics.begin_fill(color=ap.Color("#0af"))

rectangle_1: ap.Rectangle = sprite.graphics.draw_rect(x=50, y=50, width=50, height=50)
rectangle_1.click(on_rectangle_click)
rectangle_2: ap.Rectangle = sprite.graphics.draw_rect(x=150, y=50, width=50, height=50)
rectangle_2.visible = ap.Boolean(False)

e: ap.Event = ap.Event(this=rectangle_1)
rectangle_1.bind_custom_event(
    custom_event_type=ROTATE_90_DEGREES,
    handler=on_rotate_90_degrees,
    e=e,
    options={"rectangle": rectangle_2},
)

ap.save_overall_html(dest_dir_path="bind_and_trigger_custom_event_basic_usage/")
```

<iframe src="static/bind_and_trigger_custom_event_basic_usage/index.html" width="250" height="150"></iframe>

## カスタムイベントの設定の解除

`unbind_custom_event`メソッドのインターフェイスは単体のカスタムイベントの解除を行います。

同様に、`unbind_custom_event_all`メソッドのインターフェイスは全てのカスタムイベントの解除を行います。

## bind_custom_event API

<span class="inconspicuous-txt">特記事項: このAPIドキュメントはドキュメントビルド用のスクリプトによって自動で生成・同期されています。そのためもしかしたらこの節の内容は前節までの内容と重複している場合があります。</span>

**[インターフェイスの構造]** `bind_custom_event(self, *, custom_event_type: Union[apysc._event.custom_event_type.CustomEventType, str], handler: Callable[[Any, Any], NoneType], e: apysc._event.event.Event, options: Union[Any, NoneType] = None, in_handler_head_expression: str = '') -> str`<hr>

**[インターフェイス概要]**

カスタムイベントのリスナー設定を追加します。<hr>

**[引数]**

- `custom_event_type`: CustomEventType or str
  - 対象の独自のイベントの種別値としての文字列。

- `handler`: _Handler
  - 対象のイベントが発生（発火）される時に実行されるハンドラ。

- `e`: Event
  - イベントのインスタンス。

- `options`: dict or None, default None
  - ハンドラに渡される省略が可能な追加のパラメーターとしての辞書。

- `in_handler_head_expression`: str, default ""
  - 省略可能なハンドラ内の先頭に加える（JavaScriptの）表現の文字列。

<hr>

**[返却値]**

- `name`: str
  - ハンドラ名。

<hr>

**[コードサンプル]**

```py
>>> import apysc as ap
>>> def on_custom_event(e: ap.Event[ap.Rectangle], options: dict) -> None:
...     rectangle: ap.Rectangle = e.this
...     rectangle.fill_color = ap.Color("#f0a")
>>> stage: ap.Stage = ap.Stage()
>>> sprite: ap.Sprite = ap.Sprite()
>>> sprite.graphics.begin_fill(color=ap.Color("#0af"))
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

<hr>

**[関連資料]**

- [ハンドラのoptions引数の型について](https://simon-ritchie.github.io/apysc/jp/jp_about_handler_options_type.html)

## trigger_custom_event API

<span class="inconspicuous-txt">特記事項: このAPIドキュメントはドキュメントビルド用のスクリプトによって自動で生成・同期されています。そのためもしかしたらこの節の内容は前節までの内容と重複している場合があります。</span>

**[インターフェイスの構造]** `trigger_custom_event(self, *, custom_event_type: Union[apysc._event.custom_event_type.CustomEventType, str]) -> None`<hr>

**[インターフェイス概要]**

カスタムイベントのトリガー設定を追加します。<hr>

**[引数]**

- `custom_event_type`: CustomEventType or str
  - 対象の独自のイベントの種別値としての文字列。

<hr>

**[コードサンプル]**

```py
>>> import apysc as ap
>>> def on_custom_event(e: ap.Event[ap.Rectangle], options: dict) -> None:
...     rectangle: ap.Rectangle = e.this
...     rectangle.fill_color = ap.Color("#f0a")
>>> stage: ap.Stage = ap.Stage()
>>> sprite: ap.Sprite = ap.Sprite()
>>> sprite.graphics.begin_fill(color=ap.Color("#0af"))
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

## unbind_custom_event のAPI

<span class="inconspicuous-txt">特記事項: このAPIドキュメントはドキュメントビルド用のスクリプトによって自動で生成・同期されています。そのためもしかしたらこの節の内容は前節までの内容と重複している場合があります。</span>

**[インターフェイスの構造]** `unbind_custom_event(self, *, custom_event_type: Union[apysc._event.custom_event_type.CustomEventType, str], handler: Callable[[Any, Any], NoneType]) -> str`<hr>

**[インターフェイス概要]**

単体のカスタムイベントのリスナー設定を解除します。<hr>

**[引数]**

- `custom_event_type`: CustomEventType or str
  - 対象の独自のイベントの種別値としての文字列。

- `handler`: _Handler
  - カスタムイベントが発火された際に呼ばれるハンドラ。

<hr>

**[返却値]**

- `name`: str
  - ハンドラ名。

<hr>

**[コードサンプル]**

```py
>>> import apysc as ap
>>> def on_custom_event(e: ap.Event[ap.Rectangle], options: dict) -> None:
...     rectangle: ap.Rectangle = e.this
...     rectangle.fill_color = ap.Color("#f0a")
...     rectangle.unbind_custom_event(
...         custom_event_type="my_custom_event", handler=on_custom_event
...     )
>>> stage: ap.Stage = ap.Stage()
>>> sprite: ap.Sprite = ap.Sprite()
>>> sprite.graphics.begin_fill(color=ap.Color("#0af"))
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

## unbind_custom_event_all のAPI

<span class="inconspicuous-txt">特記事項: このAPIドキュメントはドキュメントビルド用のスクリプトによって自動で生成・同期されています。そのためもしかしたらこの節の内容は前節までの内容と重複している場合があります。</span>

**[インターフェイスの構造]** `unbind_custom_event_all(self, *, custom_event_type: Union[apysc._event.custom_event_type.CustomEventType, str]) -> None`<hr>

**[インターフェイス概要]**

カスタムイベントのリスナー設定を一通り解除します。<hr>

**[引数]**

- `custom_event_type`: CustomEventType or str
  - 対象の独自のイベントの種別値としての文字列。

<hr>

**[コードサンプル]**

```py
>>> import apysc as ap
>>> def on_custom_event(e: ap.Event[ap.Rectangle], options: dict) -> None:
...     rectangle: ap.Rectangle = e.this
...     rectangle.fill_color = ap.Color("#f0a")
...     rectangle.unbind_custom_event_all(custom_event_type="my_custom_event")
>>> stage: ap.Stage = ap.Stage()
>>> sprite: ap.Sprite = ap.Sprite()
>>> sprite.graphics.begin_fill(color=ap.Color("#0af"))
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