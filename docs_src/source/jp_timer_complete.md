<span class="inconspicuous-txt">※この翻訳ドキュメントはスクリプトによって出力・同期されています。内容が怪しそうな場合は<a href="https://github.com/simon-ritchie/apysc/issues" target="_blank">GitHubにissue</a>を追加したり[英語の原文](https://simon-ritchie.github.io/apysc/en/timer_complete.html)の確認をお願いします。</span>

# Timer クラスの timer_complete インターフェイス

このページでは`Timer`クラスの`timer_complete`メソッドのインターフェイスについて説明します。

## インターフェイス概要

`timer_complete`メソッドのインターフェイスはタイマーが終了（完了）した際に呼ばれるハンドラを設定します。例えば`repeat_count`の引数に100を設定した場合そのハンドラはタイマーのカウントが100回に到達したタイミングで呼ばれます。

## 基本的な使い方

`timer_complete`メソッドは他のイベント設定のインターフェイスと同様に関数やメソッドのハンドラとしての`handler`の引数とハンドラに渡すオプションのパラメーターとしての`options`引数の辞書を受け付けます。

以下のコード例では四角をクリックした際に1つ目の左側の四角に対する回転設定用のタイマーを開始しています。1つ目のタイマーが終了したタイミングで2つ目のタイマーを開始しています:

```py
# runnable
from typing_extensions import TypedDict

import apysc as ap


class _RectsOptions(TypedDict):
    rectangle_1: ap.Rectangle
    rectangle_2: ap.Rectangle


class _RectOptions(TypedDict):
    rectangle: ap.Rectangle


def on_click(e: ap.MouseEvent[ap.Sprite], options: _RectsOptions) -> None:
    """
    The handler that a rectangle calls when clicked.

    Parameters
    ----------
    e : ap.MouseEvent
        Event instance.
    options : dict
        Optional arguments dictionary.
    """
    e.this.unbind_click(on_click)
    rectangle_1: ap.Rectangle = options["rectangle_1"]
    rectangle_2: ap.Rectangle = options["rectangle_2"]
    options_: _RectOptions = {"rectangle": rectangle_1}
    timer_1: ap.Timer = ap.Timer(
        handler=on_timer, delay=ap.FPS.FPS_60, repeat_count=90, options=options_
    )
    options_ = {"rectangle": rectangle_2}
    timer_1.timer_complete(handler=on_timer_1_complete, options=options_)
    timer_1.start()


def on_timer(e: ap.TimerEvent, options: _RectOptions) -> None:
    """
    The handler that a timer calls.

    Parameters
    ----------
    e : ap.TimerEvent
        Event instance.
    options : dict
        Optional arguments dictionary.
    """
    rectangle: ap.Rectangle = options["rectangle"]
    rectangle.rotation_around_center += 1


def on_timer_1_complete(e: ap.TimerEvent, options: _RectOptions) -> None:
    """
    The handler that the first time calls when completed.

    Parameters
    ----------
    e : ap.TimerEvent
        Event instance.
    options : dict
        Optional arguments dictionary.
    """
    rectangle_2: ap.Rectangle = options["rectangle"]
    options_: _RectOptions = {"rectangle": rectangle_2}
    timer_2: ap.Timer = ap.Timer(
        handler=on_timer, delay=ap.FPS.FPS_60, repeat_count=90, options=options_
    )
    timer_2.start()


ap.Stage(
    stage_width=250, stage_height=150, background_color="#333", stage_elem_id="stage"
)
sprite: ap.Sprite = ap.Sprite()
sprite.graphics.begin_fill(color="#0af")

rectangle_1: ap.Rectangle = sprite.graphics.draw_rect(x=50, y=50, width=50, height=50)
rectangle_2: ap.Rectangle = sprite.graphics.draw_rect(x=150, y=50, width=50, height=50)
options: _RectsOptions = {"rectangle_1": rectangle_1, "rectangle_2": rectangle_2}
sprite.click(handler=on_click, options=options)

ap.save_overall_html(dest_dir_path="timer_complete_basic_usage/")
```

<iframe src="static/timer_complete_basic_usage/index.html" width="250" height="150"></iframe>

## timer_complete API

<span class="inconspicuous-txt">特記事項: このAPIドキュメントはドキュメントビルド用のスクリプトによって自動で生成・同期されています。そのためもしかしたらこの節の内容は前節までの内容と重複している場合があります。</span>

**[インターフェイスの構造]** `timer_complete(self, handler: Callable[[ForwardRef('timer_event.TimerEvent'), ~_O2], NoneType], *, options: Union[~_O2, NoneType] = None) -> str`<hr>

**[インターフェイス概要]** タイマー終了時のイベントハンドラの設定を追加します。<hr>

**[引数]**

- `handler`: _Handler
  - タイマー終了時に呼ばれる関数もしくはメソッド。

- `options`: dict or None, default None
  - ハンドラに渡される省略が可能な追加のパラメーターとしての辞書。

<hr>

**[返却値]**

- `name`: str
  - ハンドラ名。

<hr>

**[コードサンプル]**

```py
>>> from typing_extensions import TypedDict
>>> import apysc as ap
>>> class RectOptions(TypedDict):
...     rectangle: ap.Rectangle
...
>>> def on_timer(e: ap.TimerEvent, options: RectOptions) -> None:
...     rectangle: ap.Rectangle = options["rectangle"]
...     rectangle.x += 1
>>> def on_timer_complete(e: ap.TimerEvent, options: RectOptions) -> None:
...     ap.trace("Timer completed!")
>>> stage: ap.Stage = ap.Stage()
>>> sprite: ap.Sprite = ap.Sprite()
>>> sprite.graphics.begin_fill(color="#0af")
>>> rectangle: ap.Rectangle = sprite.graphics.draw_rect(
...     x=50, y=50, width=50, height=50
... )
>>> options: RectOptions = {"rectangle": rectangle}
>>> timer: ap.Timer = ap.Timer(on_timer, delay=33.3, options=options)
>>> _ = timer.timer_complete(on_timer_complete)
>>> timer.start()
```

<hr>

**[関連資料]**

- [ハンドラのoptions引数の型について](https://simon-ritchie.github.io/apysc/en/jp_about_handler_options_type.html)