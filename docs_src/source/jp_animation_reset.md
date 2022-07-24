<span class="inconspicuous-txt">※この翻訳ドキュメントはスクリプトによって出力・同期されています。内容が怪しそうな場合は<a href="https://github.com/simon-ritchie/apysc/issues" target="_blank">GitHubにissue</a>を追加したり[英語の原文](https://simon-ritchie.github.io/apysc/en/animation_reset.html)の確認をお願いします。</span>

# animation_reset インターフェイス

このページでは`animation_reset`メソッドのインターフェイスについて説明します。

## インターフェイス概要

`animation_reset`インターフェイスは全てのアニメーションのリセットと停止を行います。

このインターフェイスは`animation_x`や`animation_move`などのアニメーション関係のインターフェイスを持つクラスのインスタンス上に存在します。

## 基本的な使い方

以下のコード例では四角にクリックイベントを設定し、四角をクリックした際にX座標にアニメーションがスタートするようにしてあります。アニメーションがスタートしてから1秒経過した時点で`animation_reset`インターフェイスによってX座標のリセットが実行されています。

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
    e : ap.Rectangle
        Event instance.
    options : dict
        Optional arguments dictionary.
    """
    e.this.animation_x(x=500, duration=3000).start()
    options_: _RectOptions = {"rectangle": e.this}
    timer: ap.Timer = ap.Timer(on_timer, delay=1000, repeat_count=1, options=options_)
    timer.start()


def on_timer(e: ap.TimerEvent, options: _RectOptions) -> None:
    """
    The handler that the timer calls.

    Parameters
    ----------
    e : ap.TimerEvent
        Event instance.
    options : _RectOptions
        Optional arguments dictionary.
    """
    options["rectangle"].animation_reset()


ap.Stage(
    stage_width=600, stage_height=150, background_color="#333", stage_elem_id="stage"
)
sprite: ap.Sprite = ap.Sprite()
sprite.graphics.begin_fill(color="#00aaff")
rectangle: ap.Rectangle = sprite.graphics.draw_rect(x=50, y=50, width=50, height=50)
rectangle.click(on_click)

ap.save_overall_html(dest_dir_path="./animation_reset_basic_usage/")
```

<iframe src="static/animation_reset_basic_usage/index.html" width="600" height=150></iframe>

## animation_reset API

<span class="inconspicuous-txt">特記事項: このAPIドキュメントはドキュメントビルド用のスクリプトによって自動で生成・同期されています。そのためもしかしたらこの節の内容は前節までの内容と重複している場合があります。</span>

**[インターフェイスの構造]** `animation_reset(self) -> None`<hr>

**[インターフェイス概要]** 全てのアニメーションのリセットと停止を行います。<hr>

**[コードサンプル]**

```py
>>> from typing_extensions import TypedDict
>>> import apysc as ap
>>> class RectOptions(TypedDict):
...     rectangle: ap.Rectangle
...
>>> def on_timer(e: ap.TimerEvent, options: RectOptions) -> None:
...     rectangle: ap.Rectangle = options["rectangle"]
...     rectangle.animation_reset()
>>> stage: ap.Stage = ap.Stage()
>>> sprite: ap.Sprite = ap.Sprite()
>>> sprite.graphics.begin_fill(color="#0af")
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