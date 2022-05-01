<span class="inconspicuous-txt">※この翻訳ドキュメントはスクリプトによって出力・同期されています。内容が怪しそうな場合は<a href="https://github.com/simon-ritchie/apysc/issues" target="_blank">GitHubにissue</a>を追加したり[英語の原文](https://simon-ritchie.github.io/apysc/en/timer_start_and_stop.html)の確認をお願いします。</span>

# Timer クラスの start と stop のインターフェイス

このページでTimerクラスの`start`と`stop`メソッドの各インターフェイスについて説明します。

## 各インターフェイスの概要

`start`メソッドのインターフェイスはタイマーをスタートさせます。逆に`stop`メソッドのインターフェイスはタイマーを停止させます。

## 基本的な使い方

`start`と`stop`の各メソッドは引数を必要としません。以下のコード例では四角をクリックした際にタイマーをスタートさせ、タイマーのカウントが100に達した時点でタイマーを停止させています。

```py
# runnable
from typing_extensions import TypedDict

import apysc as ap


class _RectOptions(TypedDict):
    rectangle: ap.Rectangle


def on_rectangle_click(
        e: ap.MouseEvent[ap.Rectangle], options: dict) -> None:
    """
    The handler that a rectangle calls when clicked.

    Parameters
    ----------
    e : ap.MouseEvent
        Event instance.
    options : dict
        Optional arguments dictionary.
    """
    options_: _RectOptions = {'rectangle': e.this}
    timer: ap.Timer = ap.Timer(
        handler=on_timer, delay=16, repeat_count=100,
        options=options_)
    timer.start()
    e.this.unbind_click(handler=on_rectangle_click)


def on_timer(e: ap.TimerEvent, options: _RectOptions) -> None:
    """
    The handler what a timer calls.

    Parameters
    ----------
    e : ap.TimerEvent
        Event instance.
    options : dict
        Optional arguments dictionary.
    """
    rectangle: ap.Rectangle = options['rectangle']
    rectangle.x += 1
    timer: ap.Timer = e.this
    condition: ap.Boolean = timer.current_count == 100
    with ap.If(condition):
        timer.stop()


ap.Stage(
    stage_width=250, stage_height=150, background_color='#333',
    stage_elem_id='stage')
sprite: ap.Sprite = ap.Sprite()
sprite.graphics.begin_fill(color='#0af')
rectangle: ap.Rectangle = sprite.graphics.draw_rect(
    x=50, y=50, width=50, height=50)
rectangle.click(on_rectangle_click)

ap.save_overall_html(
    dest_dir_path='timer_start_and_stop_basic_usage/')
```

<iframe src="static/timer_start_and_stop_basic_usage/index.html" width="250" height="150"></iframe>

## start API

<span class="inconspicuous-txt">特記事項: このAPIドキュメントはドキュメントビルド用のスクリプトによって自動で生成・同期されています。そのためもしかしたらこの節の内容は前節までの内容と重複している場合があります。</span>

**[インターフェイスの構造]** `start(self) -> None`<hr>

**[インターフェイス概要]** タイマーを開始します。<hr>

**[コードサンプル]**

```py
>>> import apysc as ap
>>> def on_timer(e: ap.TimerEvent, options: dict) -> None:
...     pass
>>> _ = ap.Timer(
...     on_timer, delay=33.3, repeat_count=50).start()
```

## stop API

<span class="inconspicuous-txt">特記事項: このAPIドキュメントはドキュメントビルド用のスクリプトによって自動で生成・同期されています。そのためもしかしたらこの節の内容は前節までの内容と重複している場合があります。</span>

**[インターフェイスの構造]** `stop(self) -> None`<hr>

**[インターフェイス概要]** タイマーを停止します。<hr>

**[コードサンプル]**

```py
>>> from typing_extensions import TypedDict
>>> import apysc as ap
>>> class RectOptions(TypedDict):
...     rectangle: ap.Rectangle
>>> def on_timer(e: ap.TimerEvent, options: RectOptions) -> None:
...     rectangle: ap.Rectangle = options['rectangle']
...     rectangle.x += 1
...     with ap.If(rectangle.x > 100):
...         timer: ap.Timer = e.this
...         timer.stop()
>>> stage: ap.Stage = ap.Stage()
>>> sprite: ap.Sprite = ap.Sprite()
>>> sprite.graphics.begin_fill(color='#0af')
>>> rectangle: ap.Rectangle = sprite.graphics.draw_rect(
...     x=50, y=50, width=50, height=50)
>>> options: RectOptions = {'rectangle': rectangle}
>>> _ = ap.Timer(
...     on_timer, delay=33.3, options=options).start()
```