<span class="inconspicuous-txt">※この翻訳ドキュメントはスクリプトによって出力・同期されています。内容が怪しそうな場合は<a href="https://github.com/simon-ritchie/apysc/issues" target="_blank">GitHubにissue</a>を追加したり[英語の原文](https://simon-ritchie.github.io/apysc/en/animation_delay.html)の確認をお願いします。</span>

# 各アニメーションのインターフェイスのdelayの設定

このページでは各アニメーションのインターフェイスの`delay`の設定について説明します。

## 設定概要

`delay`の設定はアニメーション開始前の遅延時間を値を設定することができます。たとえば`delay`の引数に3000を指定すればアニメーションは3秒後に開始します。

`animation_move`や`animation_x`などの各アニメーションのインターフェイスはこの`delay`引数を持っています。

## 基本的な使い方

以下の例では各X座標のアニメーション間で2秒の遅延設定(delay)を行っています。2秒間停止してからアニメーションが開始します。

```py
# runnable
import apysc as ap

DURATION: int = 3000
DELAY: int = 2000
EASING: ap.Easing = ap.Easing.EASE_OUT_QUINT


def on_animation_complete_1(e: ap.AnimationEvent[ap.Rectangle], options: dict) -> None:
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
        x=50, duration=DURATION, delay=DELAY, easing=EASING
    )
    animation_x.animation_complete(on_animation_complete_2)
    animation_x.start()


def on_animation_complete_2(e: ap.AnimationEvent[ap.Rectangle], options: dict) -> None:
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
        x=300, duration=DURATION, delay=DELAY, easing=EASING
    )
    animation_x.animation_complete(on_animation_complete_1)
    animation_x.start()


ap.Stage(
    stage_width=400, stage_height=150, background_color="#333", stage_elem_id="stage"
)
sprite: ap.Sprite = ap.Sprite()
sprite.graphics.begin_fill(color="#0af")
rectangle: ap.Rectangle = sprite.graphics.draw_rect(x=50, y=50, width=50, height=50)

animation_x: ap.AnimationX = rectangle.animation_x(
    x=300, duration=DURATION, delay=DELAY, easing=EASING
)
animation_x.animation_complete(on_animation_complete_1)
animation_x.start()

ap.save_overall_html(dest_dir_path="./animation_delay_basic_usage/")
```

<iframe src="static/animation_delay_basic_usage/index.html" width="400" height="150"></iframe>