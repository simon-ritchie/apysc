<span class="inconspicuous-txt">※この翻訳ドキュメントはスクリプトによって出力・同期されています。内容が怪しそうな場合は<a href="https://github.com/simon-ritchie/apysc/issues" target="_blank">GitHubにissue</a>を追加したり[英語の原文](../en/animation_duration.html)の確認をお願いします。</span>

# 各アニメーションのインターフェイスのduration設定

このページでは各アニメーションのインターフェイスの`duration`設定について説明します。

## 設定概要

`duration`設定はアニメーションの開始から終了までにかける時間を設定します。単位はミリ秒です。例えば`duration`引数に3000を指定したらアニメーションが完了するまで3秒必要とする設定になります。

`animation_move`などの各アニメーションのインターフェイスはこの`duration`引数を持っています。

## 基本的な使い方

以下の例ではX座標のアニメーションで`duration`の設定に3秒を設定しています。

```py
# runnable
import apysc as ap

DURATION: int = 3000
EASING: ap.Easing = ap.Easing.EASE_OUT_QUINT


def on_animation_complete_1(
        e: ap.AnimationEvent[ap.Rectangle],
        options: dict) -> None:
    """
    The handler that animation calls when its end.

    Parameters
    ----------
    e : ap.AnimationEvent
        Event instance.
    options : dict
        Optional arguments dictionary.
    """
    rectangle: ap.Rectangle = e.this.target
    animation_x: ap.AnimationX = rectangle.animation_x(
        x=50, duration=DURATION, easing=EASING)
    animation_x.animation_complete(on_animation_complete_2)
    animation_x.start()


def on_animation_complete_2(
        e: ap.AnimationEvent[ap.Rectangle], options: dict) -> None:
    """
    The handler that animation calls when its end.

    Parameters
    ----------
    e : ap.AnimationEvent
        Event instance.
    options : dict
        Optional arguments dictionary.
    """
    rectangle: ap.Rectangle = e.this.target
    animation_x: ap.AnimationX = rectangle.animation_x(
        x=400, duration=DURATION, easing=EASING)
    animation_x.animation_complete(on_animation_complete_1)
    animation_x.start()


ap.Stage(
    stage_width=500, stage_height=150, background_color='#333',
    stage_elem_id='stage')
sprite: ap.Sprite = ap.Sprite()
sprite.graphics.begin_fill(color='#0af')
rectangle: ap.Rectangle = sprite.graphics.draw_rect(
    x=50, y=50, width=50, height=50)

animation_x: ap.AnimationX = rectangle.animation_x(
    x=400, duration=DURATION, easing=EASING)
animation_x.animation_complete(on_animation_complete_1)
animation_x.start()

ap.save_overall_html(
    dest_dir_path='./animation_duration_basic_usage/')
```

<iframe src="static/animation_duration_basic_usage/index.html" width="500" height="150"></iframe>