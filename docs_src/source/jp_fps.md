<span class="inconspicuous-txt">※この翻訳ドキュメントはスクリプトによって出力・同期されています。内容が怪しそうな場合は<a href="https://github.com/simon-ritchie/apysc/issues" target="_blank">GitHubにissue</a>を追加したり[英語の原文](https://simon-ritchie.github.io/apysc/en/fps.html)の確認をお願いします。</span>

# FPS の enum

このページでは`FPS`のenumのクラスについて説明します。

## クラス概要

`FPS`のenumのクラスは各FPS（frames per second）の定義です。タイマーが実行間隔を決めるために主にこのenumを使用しています。

## 基本的な使い方

FPSのenumの定義は5間隔（15, 20, 25, 30等）で存在します。`Timer`クラスの`delay`引数は`FPS`のenumの値を受け付けることができます。例えば`FPS.FPS_60`の値を`delay`引数に指定した場合、タイマーの間隔は約`16.6666667`ミリ秒ごととなります。同じように`FPS.FPS_30`を指定すると`33.3333333`ミリ秒ごとの間隔となります。

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


ap.Stage(
    stage_width=350, stage_height=150, background_color='#333',
    stage_elem_id='stage')
sprite: ap.Sprite = ap.Sprite()
sprite.graphics.begin_fill(color='#0af')

rectangle_1: ap.Rectangle = sprite.graphics.draw_rect(
    x=50, y=50, width=50, height=50)
options: _RectOptions = {'rectangle': rectangle_1}
timer_1: ap.Timer = ap.Timer(
    handler=on_timer, delay=ap.FPS.FPS_10, options=options)
timer_1.start()

rectangle_2: ap.Rectangle = sprite.graphics.draw_rect(
    x=150, y=50, width=50, height=50)
options = {'rectangle': rectangle_2}
timer_2: ap.Timer = ap.Timer(
    handler=on_timer, delay=ap.FPS.FPS_30, options=options)
timer_2.start()

rectangle_3: ap.Rectangle = sprite.graphics.draw_rect(
    x=250, y=50, width=50, height=50)
options = {'rectangle': rectangle_3}
timer_3: ap.Timer = ap.Timer(
    handler=on_timer, delay=ap.FPS.FPS_60, options=options)
timer_3.start()

ap.save_overall_html(
    dest_dir_path='fps_basic_usage/')
```

<iframe src="static/fps_basic_usage/index.html" width="350" height="150"></iframe>

## 関連資料

- [Timer クラスの delay 設定](jp_timer_delay.md)