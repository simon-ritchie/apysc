<span class="inconspicuous-txt">※この翻訳ドキュメントはスクリプトによって出力・同期されています。内容が怪しそうな場合は<a href="https://github.com/simon-ritchie/apysc/issues" target="_blank">GitHubにissue</a>を追加したり[英語の原文](https://simon-ritchie.github.io/apysc/en/timer_event.html)の確認をお願いします。</span>

# TimerEvent クラス

このページでは`TimerEvent`クラスについて説明します。

## クラス概要

`TimerEvent`クラスは`Timer`クラスのコンストラクタや`timer_complete`などのインターフェイスで登録されるタイマー関係のイベントのハンドラに渡されるイベントのクラスです。

## 基本的な使い方

タイマー関係の各イベントハンドラの第一引数は`TimerEvent`クラスのインスタンスとなります。

```py
# runnable
from typing_extensions import TypedDict

import apysc as ap


class _RectOptions(TypedDict):
    rectangle: ap.Rectangle


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
    rectangle: ap.Rectangle = options['rectangle']
    rectangle.rotation_around_center += 1


def on_timer_complete(e: ap.TimerEvent, options: dict) -> None:
    """
    The handler that the timer calls when completed.

    Parameters
    ----------
    e : ap.TimerEvent
        Event instance.
    options : dict
        Optional arguments dictionary.
    """
    ap.trace('Timer complete!')


ap.Stage(
    stage_width=150, stage_height=150, background_color='#333',
    stage_elem_id='stage')
sprite: ap.Sprite = ap.Sprite()
sprite.graphics.begin_fill(color='#0af')
rectangle: ap.Rectangle = sprite.graphics.draw_rect(
    x=50, y=50, width=50, height=50)

options: _RectOptions = {'rectangle': rectangle}
timer: ap.Timer = ap.Timer(
    handler=on_timer, delay=33.3, options=options)
timer.start()
timer.timer_complete(handler=on_timer_complete)

ap.save_overall_html(
    dest_dir_path='timer_event_basic_usage/')
```

<iframe src="static/timer_event_basic_usage/index.html" width="150" height="150"></iframe>

## this 属性

`TimerEvent`のインスタンスの`this`属性は対象の`Timer`クラスのインスタンスとなり、ぞれを参照してタイマー関係の各インターフェイスを使用することができます。

```py
# runnable
from typing_extensions import TypedDict

import apysc as ap


class _RectOptions(TypedDict):
    rectangle: ap.Rectangle


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
    rectangle: ap.Rectangle = options['rectangle']
    rectangle.rotation_around_center += 1
    ap.trace('Current timer count: ', e.this.current_count)


ap.Stage(
    stage_width=150, stage_height=150, background_color='#333',
    stage_elem_id='stage')
sprite: ap.Sprite = ap.Sprite()
sprite.graphics.begin_fill(color='#0af')
rectangle: ap.Rectangle = sprite.graphics.draw_rect(
    x=50, y=50, width=50, height=50)

options: _RectOptions = {'rectangle': rectangle}
timer: ap.Timer = ap.Timer(
    handler=on_timer, delay=16.6, options=options)
timer.start()

ap.save_overall_html(
    dest_dir_path='timer_event_this_attribute/')
```

<iframe src="static/timer_event_this_attribute/index.html" width="150" height="150"></iframe>

## TimerEvent クラスのコンストラクタのAPI

<span class="inconspicuous-txt">特記事項: このAPIドキュメントはドキュメントビルド用のスクリプトによって自動で生成・同期されています。そのためもしかしたらこの節の内容は前節までの内容と重複している場合があります。</span>

**[インターフェイスの構造]** `__init__(self, this:'timer.Timer') -> None`<hr>

**[インターフェイス概要]** タイマー関係のイベントのクラスです。<hr>

**[引数]**

- `this`: Timer
  - 対象のタイマーのインスタンス。

<hr>

**[コードサンプル]**

```py
>>> from typing_extensions import TypedDict
>>> import apysc as ap
>>> class RectOptions(TypedDict):
...     rectangle: ap.Rectangle
>>> def on_timer(e: ap.TimerEvent, options: RectOptions) -> None:
...     rectangle: ap.Rectangle = options['rectangle']
...     rectangle.x += 1
>>> stage: ap.Stage = ap.Stage()
>>> sprite: ap.Sprite = ap.Sprite()
>>> sprite.graphics.begin_fill(color='#0af')
>>> rectangle: ap.Rectangle = sprite.graphics.draw_rect(
...     x=50, y=50, width=50, height=50)
>>> options: RectOptions = {'rectangle': rectangle}
>>> ap.Timer(
...     on_timer, delay=ap.FPS.FPS_60, options=options,
... ).start()
```

## this 属性のAPI

<span class="inconspicuous-txt">特記事項: このAPIドキュメントはドキュメントビルド用のスクリプトによって自動で生成・同期されています。そのためもしかしたらこの節の内容は前節までの内容と重複している場合があります。</span>

**[インターフェイス概要]** このイベントのハンドラが設定されている対象のタイマーのインスタンス。<hr>

**[返却値]**

- `this`: TImer
  - このイベントのハンドラが設定されているインスタンス。

<hr>

**[コードサンプル]**

```py
>>> from typing_extensions import TypedDict
>>> import apysc as ap
>>> class RectOptions(TypedDict):
...     rectangle: ap.Rectangle
>>> def on_timer(e: ap.TimerEvent, options: RectOptions) -> None:
...     rectangle: ap.Rectangle = options['rectangle']
...     rectangle.x += 1
...     with ap.If(rectangle.x >= 100):
...         timer: ap.Timer = e.this
...         timer.stop()
>>> stage: ap.Stage = ap.Stage()
>>> sprite: ap.Sprite = ap.Sprite()
>>> sprite.graphics.begin_fill(color='#0af')
>>> rectangle: ap.Rectangle = sprite.graphics.draw_rect(
...     x=50, y=50, width=50, height=50)
>>> options: RectOptions = {'rectangle': rectangle}
>>> ap.Timer(
...     on_timer, delay=ap.FPS.FPS_60, options=options,
... ).start()
```