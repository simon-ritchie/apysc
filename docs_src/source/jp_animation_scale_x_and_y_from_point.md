<span class="inconspicuous-txt">※この翻訳ドキュメントはスクリプトによって出力・同期されています。内容が怪しそうな場合は<a href="https://github.com/simon-ritchie/apysc/issues" target="_blank">GitHubにissue</a>を追加したり[英語の原文](https://simon-ritchie.github.io/apysc/en/animation_scale_x_and_y_from_point.html)の確認をお願いします。</span>

# animation_scale_x_from_point と animation_scale_y_from_point のインターフェイス

このページでは`animation_scale_x_from_point`と`animation_scale_y_from_point`の各メソッドのインターフェイスについて説明します。

## 各インターフェイスの概要

`animation_scale_x_from_point`メソッドのインターフェイスは`ap.AnimationScaleXFromPoint`クラスのインスタンスを生成します。そのインスタンスを使って指定座標を基準としたX軸の拡縮のアニメーションを設定することができます。

同じように`animation_scale_y_from_point`メソッドのインターフェイスでは`ap.AnimationScaleYFromPoint`クラスのインスタンスを生成します。そのインスタンスを使ってY軸の拡縮のアニメーションを設定することができます。

これらのインターフェイスは`scale_x_from_center`や`scale_y_from_center`などのインターフェイスを持つ`Rectangle`や`Circle`などの`GraphicsBase`の各サブクラス上に存在します。

## 基本的な使い方

以下のコード例ではX軸の拡縮（1.0から2.0）を左側の四角へ、そしてY軸の拡縮を右側の四角へとそれぞれ`animation_scale_x_from_point`と`animation_scale_y_from_point`のメソッドを使って設定しています。

これらの設定は左側の四角では左端（x=50）の座標で、右側の四角では下端（y=100）の位置を基準に拡縮の設定を行っています。

```py
# runnable
from enum import Enum

from typing_extensions import TypedDict

import apysc as ap

DURATION: int = 1000
EASING: ap.Easing = ap.Easing.EASE_OUT_QUINT
LEFT_RECTANGLE_X: int = 50
RIGHT_RECTANGLE_Y: int = 100
SCALE_1: float = 1.0
SCALE_2: float = 2.0


class Direction(Enum):
    X = 1
    Y = 2


class Options(TypedDict):
    direction: Direction


def on_animation_complete_1(
        e: ap.AnimationEvent[ap.Rectangle], options: Options) -> None:
    """
    The handler that the animation calls when its end.

    Parameters
    ----------
    e : AnimationEvent
        Event instance.
    options : dict
        Optional arguments dictionary.
    """
    rectangle: ap.Rectangle = e.this.target
    if options['direction'] == Direction.X:
        rectangle.animation_scale_x_from_point(
            scale_x_from_point=SCALE_1,
            x=LEFT_RECTANGLE_X,
            duration=DURATION,
            easing=EASING,
        ).animation_complete(
            on_animation_complete_2,
            options=options,
        ).start()
    elif options['direction'] == Direction.Y:
        rectangle.animation_scale_y_from_point(
            scale_y_from_point=SCALE_1,
            y=RIGHT_RECTANGLE_Y,
            duration=DURATION,
            easing=EASING,
        ).animation_complete(
            on_animation_complete_2,
            options=options,
        ).start()


def on_animation_complete_2(
        e: ap.AnimationEvent[ap.Rectangle], options: Options) -> None:
    """
    The handler that the animation calls when its end.

    Parameters
    ----------
    e : AnimationEvent
        Event instance.
    options : dict
        Optional arguments dictionary.
    """
    rectangle: ap.Rectangle = e.this.target
    if options['direction'] == Direction.X:
        rectangle.animation_scale_x_from_point(
            scale_x_from_point=SCALE_2,
            x=LEFT_RECTANGLE_X,
            duration=DURATION,
            easing=EASING,
        ).animation_complete(
            on_animation_complete_1,
            options=options,
        ).start()
    elif options['direction'] == Direction.Y:
        rectangle.animation_scale_y_from_point(
            scale_y_from_point=SCALE_2,
            y=RIGHT_RECTANGLE_Y,
            duration=DURATION,
            easing=EASING,
        ).animation_complete(
            on_animation_complete_1,
            options=options,
        ).start()


ap.Stage(
    stage_width=250, stage_height=150,
    background_color='#333', stage_elem_id='stage')
sprite: ap.Sprite = ap.Sprite()
sprite.graphics.begin_fill(color='#0af')
left_rectangle: ap.Rectangle = sprite.graphics.draw_rect(
    x=50, y=50, width=50, height=50)
right_rectangle: ap.Rectangle = sprite.graphics.draw_rect(
    x=150, y=50, width=50, height=50)

options: Options = {'direction': Direction.X}
left_rectangle.animation_scale_x_from_point(
    scale_x_from_point=SCALE_2,
    x=LEFT_RECTANGLE_X,
    duration=DURATION,
    easing=EASING,
).animation_complete(
    on_animation_complete_1,
    options=options,
).start()

options = {'direction': Direction.Y}
right_rectangle.animation_scale_y_from_point(
    scale_y_from_point=SCALE_2,
    y=RIGHT_RECTANGLE_Y,
    duration=DURATION,
    easing=EASING,
).animation_complete(
    on_animation_complete_1,
    options=options,
).start()

ap.save_overall_html(
    dest_dir_path='./animation_scale_x_and_y_from_point_basic_usage/')
```

<iframe src="static/animation_scale_x_and_y_from_point_basic_usage/index.html" width="250" height="150"></iframe>