<span class="inconspicuous-txt">※この翻訳ドキュメントはスクリプトによって出力・同期されています。内容が怪しそうな場合は<a href="https://github.com/simon-ritchie/apysc/issues" target="_blank">GitHubにissue</a>を追加したり[英語の原文](https://simon-ritchie.github.io/apysc/en/animation_reverse.html)の確認をお願いします。</span>

# animation_reverse インターフェイス

このページでは`animation_reverse`メソッドのインターフェイスについて説明します。

## インターフェイス概要

`animation_reverse`インターフェイスは動いているアニメーションの再生を反転（逆再生）します。

このインターフェイスは`animation_x`や`animation_move`などのアニメーション関係のインターフェイスを持つクラスのインスタンス上に存在します。

## 基本的な使い方

以下の例ではX座標のアニメーションを設定し、1秒ごとの間隔で`animation_reverse`インターフェイスを使ってアニメーションを反転（逆作成）しています。

```py
# runnable
from typing_extensions import TypedDict

import apysc as ap


class _RectOptions(TypedDict):
    rectangle: ap.Rectangle


def on_timer_1(e: ap.TimerEvent, options: _RectOptions) -> None:
    """
    The event handler that timer calls after the 3 seconds.

    Parameters
    ----------
    e : ap.TimerEvent
        Event instance.
    options : dict
        Optional arguments dictionary.
    """
    ap.Timer(on_timer_2, delay=1000, options=options).start()


def on_timer_2(e: ap.TimerEvent, options: _RectOptions) -> None:
    """
    The event handler that timer calls every second.

    Parameters
    ----------
    e : ap.TimerEvent
        Event instance.
    options : dict
        Optional arguments dictionary.
    """
    rectangle: ap.Rectangle = options["rectangle"]
    rectangle.animation_reverse()


ap.Stage(
    stage_width=500, stage_height=150, background_color="#333", stage_elem_id="stage"
)
sprite: ap.Sprite = ap.Sprite()
sprite.graphics.begin_fill(color="#0af")

rectangle: ap.Rectangle = sprite.graphics.draw_rect(x=50, y=50, width=50, height=50)
rectangle.animation_x(x=400, duration=5000).start()
options: _RectOptions = {"rectangle": rectangle}
ap.Timer(on_timer_1, delay=3000, repeat_count=1, options=options).start()

ap.save_overall_html(dest_dir_path="animation_reverse_basic_usage/")
```

<iframe src="static/animation_reverse_basic_usage/index.html" width="500" height="150"></iframe>

## インターフェイスの特記事項

このインターフェイスはアニメーションが動いている間のみ使用することができます。以下のコード例のようにアニメーションが終了している状態で呼び出しても何も発生せずアニメーションが終了した状態のままとなります:

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
    rectangle: ap.Rectangle = options["rectangle"]

    # Nothing happens since the animation has already been completed.
    rectangle.animation_reverse()


ap.Stage(
    stage_width=500, stage_height=150, background_color="#333", stage_elem_id="stage"
)
sprite: ap.Sprite = ap.Sprite()
sprite.graphics.begin_fill(color="#0af")

rectangle: ap.Rectangle = sprite.graphics.draw_rect(x=50, y=50, width=50, height=50)
rectangle.animation_x(x=400, duration=1000).start()

options: _RectOptions = {"rectangle": rectangle}
ap.Timer(on_timer, delay=1500, repeat_count=1, options=options).start()

ap.save_overall_html(dest_dir_path="animation_reverse_notes/")
```

<iframe src="static/animation_reverse_notes/index.html" width="500" height="150"></iframe>

## animation_reverse API

<span class="inconspicuous-txt">特記事項: このAPIドキュメントはドキュメントビルド用のスクリプトによって自動で生成・同期されています。そのためもしかしたらこの節の内容は前節までの内容と重複している場合があります。</span>

**[インターフェイスの構造]** `animation_reverse(self) -> None`<hr>

**[インターフェイス概要]** 動いている全てのアニメーションを反転（逆再生）します。<hr>

**[特記事項]**

複数回このインターフェイスを呼び出した際などに、アニメーションの最初もしくは最後に到達しアニメーションが停止した場合、その後にこのインターフェイスを呼び出しても反転（逆再生）はされずに停止したままとなります。そのためアニメーション時間と同じ時間のタイマーなどで反転の指定した場合などは正常に動作しません。<hr>

**[コードサンプル]**

```py
>>> from typing_extensions import TypedDict
>>> import apysc as ap
>>> class RectOptions(TypedDict):
...     rectangle: ap.Rectangle
>>> def on_timer(
...         e: ap.TimerEvent,
...         options: RectOptions) -> None:
...     rectangle: ap.Rectangle = options['rectangle']
...     rectangle.animation_reverse()
>>> stage: ap.Stage = ap.Stage()
>>> sprite: ap.Sprite = ap.Sprite()
>>> sprite.graphics.begin_fill(color='#0af')
>>> rectangle: ap.Rectangle = sprite.graphics.draw_rect(
...     x=50, y=50, width=50, height=50)
>>> _ = rectangle.animation_x(
...     x=100,
...     duration=1500,
...     easing=ap.Easing.EASE_OUT_QUINT,
... ).start()
>>> options: RectOptions = {'rectangle': rectangle}
>>> ap.Timer(on_timer, delay=750, options=options).start()
```