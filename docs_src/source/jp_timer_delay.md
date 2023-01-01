<span class="inconspicuous-txt">※この翻訳ドキュメントはスクリプトによって出力・同期されています。内容が怪しそうな場合は<a href="https://github.com/simon-ritchie/apysc/issues" target="_blank">GitHubにissue</a>を追加したり[英語の原文](https://simon-ritchie.github.io/apysc/en/timer_delay.html)の確認をお願いします。</span>

# Timer クラスの delay 設定

このページでは`Timer`クラスの`delay`引数の設定について説明します。

## 引数の概要

`delay`引数の設定ではタイマーの間隔を設定できます。この設定はミリ秒単位となり、1000の値を指定すれば1秒ごとの間隔になります。

この引数は`int`、`float`、`Int`、`Number`型の値、もしくは`FPS`のenumの値を受け付けます。

## 基本的な使い方

`Timer`クラスのコンストラクタで`deplay`引数のパラメーターを設定することができます。以下のコード例では`timer_1`、`timer_2`、`timer_3`の3つのタイマーを生成し、それぞれdelayの値に`100`、`33.3333333`、`16.6666667`の各値を設定しています。

1番目のタイマー（`delay`の値は100）では1秒間に10回ハンドラの呼び出しを行い、2番目のタイマー（`delay`の値は33.3333333）では1秒間に30回の呼び出しを行い、3番目のタイマー（`delay`の値は16.6666667）では60回の呼び出しを行います。

```py
# runnable
from typing_extensions import TypedDict

import apysc as ap

ap.Stage(
    stage_width=350, stage_height=150, background_color="#333", stage_elem_id="stage"
)
sprite: ap.Sprite = ap.Sprite()

sprite.graphics.begin_fill(color="#0af")
rectangle_1: ap.Rectangle = sprite.graphics.draw_rect(x=50, y=50, width=50, height=50)
rectangle_2: ap.Rectangle = sprite.graphics.draw_rect(x=150, y=50, width=50, height=50)
rectangle_3: ap.Rectangle = sprite.graphics.draw_rect(x=250, y=50, width=50, height=50)


class _RectOptions(TypedDict):
    rectangle: ap.Rectangle


def on_timer(e: ap.TimerEvent, options: _RectOptions) -> None:
    """
    The Handler would be called every timer tick.

    Parameters
    ----------
    e : ap.TimerEvent
        Event instance.
    options : dict
        Optional arguments dictionary.
    """
    rectangle: ap.Rectangle = options["rectangle"]
    rectangle.rotation_around_center += 1


options: _RectOptions = {"rectangle": rectangle_1}
timer_1: ap.Timer = ap.Timer(handler=on_timer, delay=100, options=options)
timer_1.start()

options = {"rectangle": rectangle_2}
timer_2: ap.Timer = ap.Timer(handler=on_timer, delay=33.3333333, options=options)
timer_2.start()

options = {"rectangle": rectangle_3}
timer_3: ap.Timer = ap.Timer(handler=on_timer, delay=16.6666667, options=options)
timer_3.start()

ap.save_overall_html(dest_dir_path="timer_delay_basic_usage/")
```

<iframe src="static/timer_delay_basic_usage/index.html" width="350" height="150"></iframe>

## delay 引数にFPSのenumの値を設定する

`delay`の引数には`FPS`（frames per second / 1秒当たりのフレーム数）のenumの値を指定することもできます。例えば、`FPS.FPS_60`を指定すれば60FPS相当の実行回数（16.6666667ミリ秒ごとの実行）となります。同様に`FPS.FPS_30`を指定すれば30FPS相当（33.3333333ミリ秒ごとの実行）となります。

```py
# runnable
from typing_extensions import TypedDict

import apysc as ap

ap.Stage(
    stage_width=150, stage_height=150, background_color="#333", stage_elem_id="stage"
)
sprite: ap.Sprite = ap.Sprite()
sprite.graphics.begin_fill(color="#0af")
rectangle: ap.Rectangle = sprite.graphics.draw_rect(x=50, y=50, width=50, height=50)


class _RectOptions(TypedDict):
    rectangle: ap.Rectangle


def on_timer(e: ap.TimerEvent, options: _RectOptions) -> None:
    """
    The Handler would be called every timer tick.

    Parameters
    ----------
    e : ap.TimerEvent
        Event instance.
    options : dict
        Optional arguments dictionary.
    """
    rectangle: ap.Rectangle = options["rectangle"]
    rectangle.rotation_around_center += 1


options: _RectOptions = {"rectangle": rectangle}
timer: ap.Timer = ap.Timer(handler=on_timer, delay=ap.FPS.FPS_60, options=options)
timer.start()

ap.save_overall_html(dest_dir_path="timer_delay_fps_enum/")
```

<iframe src="static/timer_delay_fps_enum/index.html" width="150" height="150"></iframe>

## 関連資料

- [FPS の enum](jp_fps.md)

## Timer クラスのコンストラクタのAPI

<span class="inconspicuous-txt">特記事項: このAPIドキュメントはドキュメントビルド用のスクリプトによって自動で生成・同期されています。そのためもしかしたらこの節の内容は前節までの内容と重複している場合があります。</span>

**[インターフェイスの構造]** `__init__(self, handler: Callable[[ForwardRef('TimerEvent'), ~_ConstructorOptions], NoneType], *, delay: Union[int, float, apysc._type.number_value_mixin.NumberValueMixIn, apysc._time.fps.FPS], repeat_count: Union[int, apysc._type.int.Int] = 0, options: Union[~_ConstructorOptions, NoneType] = None) -> None`<hr>

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

- [FPS の enum](https://simon-ritchie.github.io/apysc/jp/jp_fps.html)
- [Timer クラスの repeat_count 設定](https://simon-ritchie.github.io/apysc/jp/jp_timer_repeat_count.html)

- [ハンドラのoptions引数の型について](https://simon-ritchie.github.io/apysc/jp/jp_about_handler_options_type.html)

## delay 属性のAPI

<span class="inconspicuous-txt">特記事項: このAPIドキュメントはドキュメントビルド用のスクリプトによって自動で生成・同期されています。そのためもしかしたらこの節の内容は前節までの内容と重複している場合があります。</span>

**[インターフェイス概要]**

遅延（間隔）値を取得します。<hr>

**[返却値]**

- `delay`: Number
  - ハンドラの実行ごとのミリ秒の間隔値。

<hr>

**[コードサンプル]**

```py
>>> import apysc as ap
>>> def on_timer(e: ap.TimerEvent, options: dict) -> None:
...     pass
>>> timer: ap.Timer = ap.Timer(on_timer, delay=33.3, repeat_count=50)
>>> timer.delay
Number(33.3)
```