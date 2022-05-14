<span class="inconspicuous-txt">※この翻訳ドキュメントはスクリプトによって出力・同期されています。内容が怪しそうな場合は<a href="https://github.com/simon-ritchie/apysc/issues" target="_blank">GitHubにissue</a>を追加したり[英語の原文](https://simon-ritchie.github.io/apysc/en/timer.html)の確認をお願いします。</span>

# Timer クラス

このページでは`Timer`クラスについて説明します。

## Timer クラスの概要

`Timer`クラスは一定間隔で処理を実行するためのタイマーの処理を扱います。任意の間隔を設定してハンドラの呼び出し設定を追加することができます。

## 基本的な使い方

`Timer`クラスはコンストラクタでハンドラとしての`handler`引数とタイマー実行間隔のミリ秒としての`delay`引数の指定を必要とします。そして`start`メソッドを呼び出すとタイマーがスタートします。タイマーは`TimerEvent`クラスのインスタンスとオプションとして指定できる追加のパラメーターの引数をハンドラへ渡します。

以下のコード例では四角（`Sprite`）をクリックした際に`Timer`クラスを使用した設定を行っています:

```py
# runnable
from typing_extensions import TypedDict

import apysc as ap


class _RectOptions(TypedDict):
    rectangle: ap.Rectangle


def on_sprite_click(
        e: ap.MouseEvent[ap.Sprite], options: _RectOptions) -> None:
    """
    The Handler that the rectangle calls when clicked.

    Parameters
    ----------
    e : MouseEvent
        Event instance.
    options : dict
        Optional arguments dictionary.
    """
    e.this.unbind_click_all()
    timer: ap.Timer = ap.Timer(on_timer, delay=16.6, options=options)
    timer.start()


def on_timer(e: ap.TimerEvent, options: _RectOptions) -> None:
    """
    The Handler a timer calls.

    Parameters
    ----------
    e : TimerEvent
        Event instance.
    options : dict
        Optional arguments dictionary.
    """
    rectangle: ap.Rectangle = options['rectangle']
    rectangle.x += 1


ap.Stage(
    stage_width=350, stage_height=150, background_color='#333',
    stage_elem_id='stage')
sprite: ap.Sprite = ap.Sprite()
sprite.graphics.begin_fill(color='#0af')
rectangle: ap.Rectangle = sprite.graphics.draw_rect(
    x=50, y=50, width=50, height=50)
options: _RectOptions = {'rectangle': rectangle}
sprite.click(on_sprite_click, options=options)

ap.save_overall_html(
    dest_dir_path='timer_basic_usage/')
```

四角をクリックするとタイマーがスタートし、タイマーのハンドラは四角のX座標を加算していきます。

<iframe src="static/timer_basic_usage/index.html" width="350" height="150"></iframe>

## 関連資料

- [TimerEvent クラス](jp_timer_event.md)
- [Timer クラスの delay 設定](jp_timer_delay.md)

- [FPS の enum](jp_fps.md)
- [Timer クラスの repeat_count 設定](jp_timer_repeat_count.md)

- [Timer クラスの start と stop の各インターフェイス](jp_timer_start_and_stop.md)
- [Timer クラスの timer_complete インターフェイス](jp_timer_complete.md)

- [Timer クラスの reset インターフェイス](jp_timer_reset.md)

## Timer クラスのコンストラクタのAPI

<span class="inconspicuous-txt">特記事項: このAPIドキュメントはドキュメントビルド用のスクリプトによって自動で生成・同期されています。そのためもしかしたらこの節の内容は前節までの内容と重複している場合があります。</span>

**[インターフェイスの構造]** `__init__(self, handler: Callable[[ForwardRef('timer_event.TimerEvent'), ~_O1], NoneType], delay: Union[int, float, apysc._type.number_value_interface.NumberValueInterface, apysc._time.fps.FPS], *, repeat_count: Union[int, apysc._type.int.Int] = 0, options: Union[~_O1, NoneType] = None) -> None`<hr>

**[インターフェイス概要]** 一定間隔ごとにハンドラの関数を実行するためのタイマーのクラスです。<hr>

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
>>> def on_timer(e: ap.TimerEvent, options: RectOptions) -> None:
...     rectangle: ap.Rectangle = options['rectangle']
...     rectangle.x += 1
>>> stage: ap.Stage = ap.Stage()
>>> sprite: ap.Sprite = ap.Sprite()
>>> sprite.graphics.begin_fill(color='#0af')
>>> rectangle: ap.Rectangle = sprite.graphics.draw_rect(
...     x=50, y=50, width=50, height=50)
>>> options: RectOptions = {'rectangle': rectangle}
>>> _ = ap.Timer(
...     on_timer, delay=ap.FPS.FPS_60, options=options).start()
```

<hr>

**[関連資料]**

- [TimerEvent クラス](https://simon-ritchie.github.io/apysc/jp_timer_event.html)
- [Timer クラスの delay 設定](https://simon-ritchie.github.io/apysc/jp_timer_delay.html)

- [FPS の enum](https://simon-ritchie.github.io/apysc/jp_fps.html)
- [Timer クラスの repeat_count 設定](https://simon-ritchie.github.io/apysc/jp_timer_repeat_count.html)

- [ハンドラのoptions引数の型について](https://simon-ritchie.github.io/apysc/jp_about_handler_options_type.html)