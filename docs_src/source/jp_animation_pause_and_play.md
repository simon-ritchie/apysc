<span class="inconspicuous-txt">※この翻訳ドキュメントはスクリプトによって出力・同期されています。内容が怪しそうな場合は<a href="https://github.com/simon-ritchie/apysc/issues" target="_blank">GitHubにissue</a>を追加したり[英語の原文](https://simon-ritchie.github.io/apysc/en/animation_pause_and_play.html)の確認をお願いします。</span>

# animation_pause と animation_play インターフェイス

このページでは`animation_pause`と`animation_play`のメソッドの各インターフェイスについて説明します。

## 各インターフェイス概要

`animation_pause`インターフェイスは対象のインスタンスで動いている全てのアニメーションを停止します。`animation_play`インターフェイスは停止しているアニメーションを再開します。

これらのインターフェイスは`animation_x`や`animation_move`などのアニメーション関係のインターフェイスを持つクラスのインスタンス上に存在します。

## 基本的な使い方

以下のコード例ではX座標のアニメーションをスタートし、その1秒後にアニメーションを停止しています。加えて、停止してからさらに500ミリ秒経過した時点でアニメーションを再開しています。

```py
# runnable
from typing_extensions import TypedDict

import apysc as ap


class _RectOptions(TypedDict):
    rectangle: ap.Rectangle


def on_timer_1(e: ap.TimerEvent, options: _RectOptions) -> None:
    """
    The handler that the timer calls.

    Parameters
    ----------
    e : ap.TimerEvent
        Event instance.
    options : _RectOptions
        Optional arguments dictionary.
    """
    options["rectangle"].animation_pause()
    timer: ap.Timer = ap.Timer(on_timer_2, delay=500, options=options, repeat_count=1)
    timer.start()


def on_timer_2(e: ap.TimerEvent, options: _RectOptions) -> None:
    """
    The handler that the timer calls.

    Parameters
    ----------
    e : ap.TimerEvent
        Event instance.
    options : _RectOptions
        Optional arguments dictionary.
    """
    options["rectangle"].animation_play()


ap.Stage(
    stage_width=600,
    stage_height=150,
    background_color=ap.Color("#333"),
    stage_elem_id="stage",
)
sprite: ap.Sprite = ap.Sprite()
sprite.graphics.begin_fill(color=ap.Color("#00aaff"))
rectangle: ap.Rectangle = sprite.graphics.draw_rect(x=50, y=50, width=50, height=50)
rectangle.animation_x(x=500, duration=15_000).start()

options: _RectOptions = {"rectangle": rectangle}
timer: ap.Timer = ap.Timer(on_timer_1, delay=1000, options=options)
timer.start()

ap.save_overall_html(dest_dir_path="./animation_pause_basic_usage/")
```

<iframe src="static/animation_pause_basic_usage/index.html" width="600" height="150"></iframe>

## animation_pause API

<span class="inconspicuous-txt">特記事項: このAPIドキュメントはドキュメントビルド用のスクリプトによって自動で生成・同期されています。そのためもしかしたらこの節の内容は前節までの内容と重複している場合があります。</span>

**[インターフェイスの構造]** `animation_pause(self) -> None`<hr>

**[インターフェイス概要]**

全てのアニメーションを停止します。<hr>

**[コードサンプル]**

```py
>>> from typing_extensions import TypedDict
>>> import apysc as ap
>>> class RectOptions(TypedDict):
...     rectangle: ap.Rectangle
...
>>> def on_timer(e: ap.TimerEvent, options: RectOptions) -> None:
...     rectangle: ap.Rectangle = options["rectangle"]
...     rectangle.animation_pause()
>>> stage: ap.Stage = ap.Stage()
>>> sprite: ap.Sprite = ap.Sprite()
>>> sprite.graphics.begin_fill(color=ap.Color("#0af"))
>>> rectangle: ap.Rectangle = sprite.graphics.draw_rect(
...     x=50, y=50, width=50, height=50
... )
>>> _ = rectangle.animation_x(
...     x=100,
...     duration=1500,
...     easing=ap.Easing.EASE_OUT_QUINT,
... ).start()
>>> options: RectOptions = {"rectangle": rectangle}
>>> ap.Timer(on_timer, delay=750, options=options).start()
```

## animation_play API

<span class="inconspicuous-txt">特記事項: このAPIドキュメントはドキュメントビルド用のスクリプトによって自動で生成・同期されています。そのためもしかしたらこの節の内容は前節までの内容と重複している場合があります。</span>

**[インターフェイスの構造]** `animation_play(self) -> None`<hr>

**[インターフェイス概要]**

停止している全てのアニメーションを再開します。<hr>

**[コードサンプル]**

```py
>>> from typing_extensions import TypedDict
>>> import apysc as ap
>>> class RectOptions(TypedDict):
...     rectangle: ap.Rectangle
...
>>> def on_timer_1(e: ap.TimerEvent, options: RectOptions) -> None:
...     rectangle: ap.Rectangle = options["rectangle"]
...     rectangle.animation_pause()
>>> def on_timer_2(e: ap.TimerEvent, options: RectOptions) -> None:
...     rectangle: ap.Rectangle = options["rectangle"]
...     rectangle.animation_play()
>>> stage: ap.Stage = ap.Stage()
>>> sprite: ap.Sprite = ap.Sprite()
>>> sprite.graphics.begin_fill(color=ap.Color("#0af"))
>>> rectangle: ap.Rectangle = sprite.graphics.draw_rect(
...     x=50, y=50, width=50, height=50
... )
>>> _ = rectangle.animation_x(
...     x=100,
...     duration=1500,
...     easing=ap.Easing.EASE_OUT_QUINT,
... ).start()
>>> options: RectOptions = {"rectangle": rectangle}
>>> ap.Timer(on_timer_1, delay=500, options=options).start()
>>> ap.Timer(on_timer_2, delay=1000, options=options).start()
```