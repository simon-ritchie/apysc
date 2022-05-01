<span class="inconspicuous-txt">※この翻訳ドキュメントはスクリプトによって出力・同期されています。内容が怪しそうな場合は<a href="https://github.com/simon-ritchie/apysc/issues" target="_blank">GitHubにissue</a>を追加したり[英語の原文](https://simon-ritchie.github.io/apysc/en/animation_return_value.html)の確認をお願いします。</span>

# 各アニメーションのインターフェイスの返却値

このページでは`animation_move`などの各アニメーションのインターフェイスの返却値について説明します。

## 各インターフェイスはAnimationBaseのサブクラスのインスタンスを返却します

各アニメーション関係のインターフェイスは`AnimationBase`のサブクラスのインスタンスを返却します。例えば`animation_move`インターフェイスであれば`AnimationMove`クラスのインスタンスを返却し、`animation_x`であれば`AnimationX`クラスのインスタンスを返却します。

`AnimationBase`クラスはアニメーションの開始用の`start`メソッドやアニメーション終了時のイベント登録用の`animation_complete`メソッドなどの基本的な共通のアニメーション関係のインターフェイスを持っています。

## 基本的な使い方

返却された各値のクラスはapyscのパッケージに含まれています（例: `ap.AnimationMove`など）。そのためそれらを使用して型アノテーションを行うことができます。

以下のコード例では`animation_x`メソッドを使用しており、返却値として`AnimationX`クラスのインスタンスを受け取っています。加えて`AnimationX`クラスのインスタンスを参照してアニメーション完了時のイベントを設定したりアニメーションを開始したり等を行っています。

```py
# runnable
import apysc as ap

DURATION: int = 1000


def on_animation_complete_1(
        e: ap.AnimationEvent[ap.Rectangle],
        options: dict) -> None:
    """
    The handler that the animation calls when its end.

    Parameters
    ----------
    e : ap.AnimationEvent
        Event instance.
    options : dict
        Optional arguments dictionary.
    """
    rectangle: ap.Rectangle = e.this.target
    animation_x: ap.AnimationX = rectangle.animation_x(
        x=50, duration=DURATION)
    animation_x.animation_complete(on_animation_complete_2)
    animation_x.start()


def on_animation_complete_2(
        e: ap.AnimationEvent[ap.Rectangle],
        options: dict) -> None:
    """
    The handler that the animation calls when its end.

    Parameters
    ----------
    e : ap.AnimationEvent
        Event instance.
    options : dict
        Optional arguments dictionary.
    """
    rectangle: ap.Rectangle = e.this.target
    animation_x: ap.AnimationX = rectangle.animation_x(
        x=100, duration=DURATION)
    animation_x.animation_complete(on_animation_complete_1)
    animation_x.start()


ap.Stage(
    stage_width=200, stage_height=150, background_color='#333',
    stage_elem_id='stage')
sprite: ap.Sprite = ap.Sprite()
sprite.graphics.begin_fill(color='#0af')
rectangle: ap.Rectangle = sprite.graphics.draw_rect(
    x=50, y=50, width=50, height=50)
animation_x: ap.AnimationX = rectangle.animation_x(
    x=100, duration=DURATION)
animation_x.animation_complete(on_animation_complete_1)
animation_x.start()

ap.save_overall_html(
    dest_dir_path='./animation_return_value_basic_usage/')
```

<iframe src="static/animation_return_value_basic_usage/index.html" width="200" height="150"></iframe>