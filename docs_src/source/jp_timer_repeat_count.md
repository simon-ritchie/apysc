<span class="inconspicuous-txt">※この翻訳ドキュメントはスクリプトによって出力・同期されています。内容が怪しそうな場合は<a href="https://github.com/simon-ritchie/apysc/issues" target="_blank">GitHubにissue</a>を追加したり[英語の原文](https://simon-ritchie.github.io/apysc/en/timer_repeat_count.html)の確認をお願いします。</span>

# Timer クラスの repeat_count 設定

このページでは`Timer`クラスの`repeat_count`引数の設定について説明します。

## 引数の概要

`repeat_count`引数の設定ではハンドラが呼ばれる最大数を設定できます。例えば、もし10を指定した場合タイマーは10回ハンドラを呼び出した後に停止します。

## 基本的な使い方

`Timer`クラスのコンストラクタにて`repeat_count`引数のパラメーターを設定することができます。以下のコード例では四角をクリックした際に`repeat_count`の値が100のタイマーを設定しています。

もしタイマーがハンドラ内で四角を100回分動かした場合（100px分右に動いた場合）タイマーは停止します。

```py
# runnable
from typing_extensions import TypedDict

import apysc as ap


class _RectOptions(TypedDict):
    rectangle: ap.Rectangle


def on_rectangle_click(e: ap.MouseEvent[ap.Rectangle], options: dict) -> None:
    """
    The handler that a rectangle calls when clicked.

    Parameters
    ----------
    e : ap.MouseEvent
        Event instance.
    options : dict
        Optional arguments dictionary.
    """
    options_: _RectOptions = {"rectangle": e.this}
    timer: ap.Timer = ap.Timer(
        handler=on_timer, delay=16, repeat_count=100, options=options_
    )
    timer.start()
    e.this.unbind_click(handler=on_rectangle_click)


def on_timer(e: ap.TimerEvent, options: _RectOptions) -> None:
    """
    The handler that a timer calls.

    Parameters
    ----------
    e : ap.TimerEvent
        Event instance.
    options : dict
        Optional arguments dictionary.
    """
    rectangle: ap.Rectangle = options["rectangle"]
    rectangle.x += 1


ap.Stage(
    stage_width=250, stage_height=150, background_color="#333", stage_elem_id="stage"
)
sprite: ap.Sprite = ap.Sprite()
sprite.graphics.begin_fill(color="#0af")
rectangle: ap.Rectangle = sprite.graphics.draw_rect(x=50, y=50, width=50, height=50)
rectangle.click(on_rectangle_click)

ap.save_overall_html(dest_dir_path="timer_repeat_count_basic_usage/")
```

<iframe src="static/timer_repeat_count_basic_usage/index.html" width="250" height="150"></iframe>

## Timer クラスのコンストラクタのAPI

<span class="inconspicuous-txt">特記事項: このAPIドキュメントはドキュメントビルド用のスクリプトによって自動で生成・同期されています。そのためもしかしたらこの節の内容は前節までの内容と重複している場合があります。</span>

**[インターフェイスの構造]** `__init__(self, handler: Callable[[ForwardRef('timer_event.TimerEvent'), ~_O1], NoneType], *, delay: Union[int, float, apysc._type.number_value_interface.NumberValueInterface, apysc._time.fps.FPS], repeat_count: Union[int, apysc._type.int.Int] = 0, options: Union[~_O1, NoneType] = None) -> None`<hr>

**[インターフェイス概要]**

一定間隔ごとにハンドラの関数を実行するためのタイマーのクラスです。<hr>

**[引数]**

- `handler`: _Handler
  - 一定間隔ごとに呼ばれる関数もしくはメソッドのハンドラ。

- `delay`: Int or int or Number or float or FPS
  - ハンドラの実行間隔となるミリ秒もしくはFPSのenumの値。もし`FPS`の値が指定された場合、FPSに応じて計算されたミリ秒が設定されます（例えば、もし`FPS_60`が指定されていれば`delay`の値は16.6666667ミリ秒相当になります。）。

- `repeat_count`: Int or int
  - ハンドラの実行回数の上限値。ハンドラの実行回数がこの値に到達した場合タイマーは停止します。もし0が指定された場合にはタイマーは停止しなくなります。

- `options`: dict or None, default None
  - ハンドラの関数もしくはメソッドへ渡すオプションとしての各パラメーターを格納した辞書。

<hr>

**[コードサンプル]**

```py
>>> from typing_extensions import TypedDict
>>> import apysc as ap
>>> class RectOptions(TypedDict):
...     rectangle: ap.Rectangle
...
>>> def on_timer(e: ap.TimerEvent, options: RectOptions) -> None:
...     rectangle: ap.Rectangle = options["rectangle"]
...     rectangle.x += 1
>>> stage: ap.Stage = ap.Stage()
>>> sprite: ap.Sprite = ap.Sprite()
>>> sprite.graphics.begin_fill(color="#0af")
>>> rectangle: ap.Rectangle = sprite.graphics.draw_rect(
...     x=50, y=50, width=50, height=50
... )
>>> options: RectOptions = {"rectangle": rectangle}
>>> _ = ap.Timer(on_timer, delay=ap.FPS.FPS_60, options=options).start()
```

<hr>

**[関連資料]**

- [Timer クラス](https://simon-ritchie.github.io/apysc/jp/jp_timer.html)
- [TimerEvent クラス](https://simon-ritchie.github.io/apysc/jp/jp_timer_event.html)

- [Timer クラスの delay 設定](https://simon-ritchie.github.io/apysc/jp/jp_timer_delay.html)
- [FPS の enum](https://simon-ritchie.github.io/apysc/jp/jp_fps.html)

- [ハンドラのoptions引数の型について](https://simon-ritchie.github.io/apysc/jp/jp_about_handler_options_type.html)

## repeat_count 属性のAPI

<span class="inconspicuous-txt">特記事項: このAPIドキュメントはドキュメントビルド用のスクリプトによって自動で生成・同期されています。そのためもしかしたらこの節の内容は前節までの内容と重複している場合があります。</span>

**[インターフェイス概要]**

ハンドラが呼ばれる最大数を取得します。<hr>

**[返却値]**

- `repeat_count`: Int
  - ハンドラの呼び出しの上限回数。もし0が指定された場合、タイマーはずっと実行され続けます（ハンドラを呼び続けます）。

<hr>

**[コードサンプル]**

```py
>>> import apysc as ap
>>> def on_timer(e: ap.TimerEvent, options: dict) -> None:
...     pass
>>> timer: ap.Timer = ap.Timer(on_timer, delay=33.3, repeat_count=50)
>>> timer.repeat_count
Int(50)
```