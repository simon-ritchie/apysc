<span class="inconspicuous-txt">※この翻訳ドキュメントはスクリプトによって出力・同期されています。内容が怪しそうな場合は<a href="https://github.com/simon-ritchie/apysc/issues" target="_blank">GitHubにissue</a>を追加したり[英語の原文](https://simon-ritchie.github.io/apysc/en/animation_finish.html)の確認をお願いします。</span>

# animation_finish インターフェイス

このページでは`animation_finish`メソッドのインターフェイスについて説明します。

## インターフェイス概要

`animation_finish`インターフェイスでは実行されている全てのアニメーションにアニメーションの各属性の最終値を設定しアニメーションを終了させます。

このインターフェイスは`animation_x`や`animation_move`などのアニメーション関係のインターフェイスを持つクラスのインスタンス上に存在します。

## 基本的な使い方

以下のコード例では四角にクリックイベントを設定しています。四角をクリックするとX座標のアニメーションが開始するようになっています。アニメーション開始後に2秒経過したらアニメーションは終了し、最終値の座標が設定されます。

```py
# runnable
from typing_extensions import TypedDict

import apysc as ap


class _RectOptions(TypedDict):
    rectangle: ap.Rectangle


def on_click(e: ap.MouseEvent[ap.Rectangle], options: dict) -> None:
    """
    The handler that the rectangle calls when clicked.

    Parameters
    ----------
    e : ap.MouseEvent
        Event instance.
    options : dict
        Optional arguments dictionary.
    """
    rectangle: ap.Rectangle = e.this
    rectangle.animation_x(
        x=300, duration=5000,
    ).start()

    options_: _RectOptions = {'rectangle': rectangle}
    ap.Timer(
        on_timer, delay=2000, repeat_count=1, options=options_,
    ).start()


def on_timer(e: ap.TimerEvent, options: _RectOptions) -> None:
    """
    The handler that the timer calls when its ends.

    Parameters
    ----------
    e : ap.TimerEvent
        Event instance.
    options : dict
        Optional arguments dictionary.
    """
    rectangle: ap.Rectangle = options['rectangle']
    rectangle.animation_finish()


ap.Stage(
    stage_width=400, stage_height=150, background_color='#333',
    stage_elem_id='stage')
sprite: ap.Sprite = ap.Sprite()
sprite.graphics.begin_fill(color='#0af')

rectangle: ap.Rectangle = sprite.graphics.draw_rect(
    x=50, y=50, width=50, height=50)
rectangle.click(on_click)

ap.save_overall_html(
    dest_dir_path='animation_finish_basic_usage/')
```

<iframe src="static/animation_finish_basic_usage/index.html" width="400" height="150"></iframe>

## animation_finish API

<span class="inconspicuous-txt">特記事項: このAPIドキュメントはドキュメントビルド用のスクリプトによって自動で生成・同期されています。そのためもしかしたらこの節の内容は前節までの内容と重複している場合があります。</span>

**[インターフェイスの構造]** `animation_finish(self) -> None`<hr>

**[インターフェイス概要]** 全てのアニメーションを終了し各属性にアニメーションの最終値の値を設定します。<hr>

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
...     rectangle.animation_finish()
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