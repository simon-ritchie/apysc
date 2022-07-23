<span class="inconspicuous-txt">※この翻訳ドキュメントはスクリプトによって出力・同期されています。内容が怪しそうな場合は<a href="https://github.com/simon-ritchie/apysc/issues" target="_blank">GitHubにissue</a>を追加したり[英語の原文](https://simon-ritchie.github.io/apysc/en/timer_reset.html)の確認をお願いします。</span>

# Timer クラスの reset インターフェイス

このページでは`Timer`クラスの`reset`メソッドのインターフェイスについて説明します。

## インターフェイス概要

`reset`メソッドのインターフェイスはタイマーのカウントをリセットしそしてタイマーを停止します。

## 基本的な使い方

`reset`メソッドは引数を必要としません。

以下のコード例では1つ目のタイマーで四角を90度回転させています（`repeat_count=90`）。回転処理が終わったら2つ目のタイマーをリセットさせてからスタートさせています。スタート後に1秒経過したら1つ目のタイマーをリセットしてから再度スタートさせています。

```py
# runnable
from typing_extensions import TypedDict

import apysc as ap

ap.Stage(
    stage_width=150, stage_height=150, background_color="#333", stage_elem_id="stage"
)
sprite: ap.Sprite = ap.Sprite()
sprite.graphics.begin_fill(color="#0af")
rectangle: ap.Rectangle = sprite.graphics.draw_rect(x=50, y=50, width=50, height=50)


class _RectOptions(TypedDict):
    rectangle: ap.Rectangle


class _TimerOptions(TypedDict):
    timer: ap.Timer


def on_first_timer(e: ap.TimerEvent, options: _RectOptions) -> None:
    """
    The handler that the first-timer calls.

    Parameters
    ----------
    e : ap.TimerEvent
        Event instance.
    options : dict
        Optional arguments dictionary.
    """
    rectangle: ap.Rectangle = options["rectangle"]
    rectangle.rotation_around_center += 1


def on_first_timer_complete(e: ap.TimerEvent, options: _TimerOptions) -> None:
    """
    The handler that the first-timer calls when completed.

    Parameters
    ----------
    e : ap.TimerEvent
        Event instance.
    options : dict
        Optional arguments dictionary.
    """
    timer_2: ap.Timer = options["timer"]
    timer_2.reset()
    timer_2.start()


def on_second_timer(e: ap.TimerEvent, options: _TimerOptions) -> None:
    """
    The handler that the second timer calls.

    Parameters
    ----------
    e : ap.TimerEvent
        Event instance.
    options : dict
        Optional arguments dictionary.
    """
    timer_1: ap.Timer = options["timer"]
    timer_1.reset()
    timer_1.start()


options_1: _RectOptions = {"rectangle": rectangle}
timer_1: ap.Timer = ap.Timer(
    handler=on_first_timer, delay=ap.FPS.FPS_60, repeat_count=90, options=options_1
)

options_2: _TimerOptions = {"timer": timer_1}
timer_2: ap.Timer = ap.Timer(
    handler=on_second_timer, delay=1000, repeat_count=1, options=options_2
)
options_2 = {"timer": timer_2}
timer_1.timer_complete(on_first_timer_complete, options=options_2)
timer_1.start()

ap.save_overall_html(dest_dir_path="timer_reset_basic_usage/")
```

<iframe src="static/timer_reset_basic_usage/index.html" width="150" height="150"></iframe>

## reset API

<span class="inconspicuous-txt">特記事項: このAPIドキュメントはドキュメントビルド用のスクリプトによって自動で生成・同期されています。そのためもしかしたらこの節の内容は前節までの内容と重複している場合があります。</span>

**[インターフェイスの構造]** `reset(self) -> None`<hr>

**[インターフェイス概要]** タイマーのカウントをリセットし、そしてタイマーの停止を行います。<hr>

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
...         timer.reset()
>>> stage: ap.Stage = ap.Stage()
>>> sprite: ap.Sprite = ap.Sprite()
>>> sprite.graphics.begin_fill(color='#0af')
>>> rectangle: ap.Rectangle = sprite.graphics.draw_rect(
...     x=50, y=50, width=50, height=50)
>>> options: RectOptions = {'rectangle': rectangle}
>>> _ = ap.Timer(
...     on_timer, delay=33.3, options=options).start()
```