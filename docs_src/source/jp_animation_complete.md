<span class="inconspicuous-txt">※この翻訳ドキュメントはスクリプトによって出力・同期されています。内容が怪しそうな場合は<a href="https://github.com/simon-ritchie/apysc/issues" target="_blank">GitHubにissue</a>を追加したり[英語の原文](../en/animation_complete.html)の確認をお願いします。</span>

# AnimationBase クラス animation_complete インターフェイス

このページでは`AnimationBase`クラスの`animation_complete`メソッドのインターフェイスについて説明します。

## インターフェイス概要

`animation_complete`メソッドはアニメーションが終了したときのハンドラを設定します。

ハンドラの引数には第一引数にイベントのインスタンス（`ap.AnimationEvent`）、第二引数にはオプションのパラメーターとなる辞書が必要になります。

## 基本的な使い方

`animation_complete`メソッドは第一引数にハンドラが必要となり、第二引数にはオプションのパラメーターの辞書を設定することができます。

以下のコード例ではX座標のアニメーション終了時用に`animation_complete`メソッドを読んでハンドラを設定しています。そのハンドラ内ではX座標をリセットするための別のアニメーションを開始しています。

```py
# runnable
import apysc as ap

DURATION: int = 1000


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
        x=50, duration=DURATION)
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
    x=100, duration=1000)
animation_x.animation_complete(on_animation_complete_1)
animation_x.start()

ap.save_overall_html(
    dest_dir_path='./animation_complete_basic_usage/')
```

<iframe src="static/animation_complete_basic_usage/index.html" width="200" height="150"></iframe>

## 他のインターフェイスを呼び出す際の特記事項

`animation_complete`メソッドはアニメーション開始前にのみ設定することができます。`start`メソッド呼び出し後に`animation_complete`メソッドを呼び出すとエラーになります。

```py
import apysc as ap


def on_animation_complete(
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
    ap.trace('Animation complete!')


ap.Stage(
    stage_width=200, stage_height=200, background_color='#333',
    stage_elem_id='stage')
sprite: ap.Sprite = ap.Sprite()
sprite.graphics.begin_fill(color='#0af')
rectangle: ap.Rectangle = sprite.graphics.draw_rect(
    x=50, y=50, width=50, height=50)

animation_move: ap.AnimationMove = rectangle.animation_move(
    x=100, y=100, duration=1000)
animation_move.start()
animation_move.animation_complete(on_animation_complete)
```

```
Exception: This interface can not be called after the animation is started.
```

`start`メソッド呼び出し前に`animation_complete`メソッドを呼び出すことで正常に動作します:

```py
# runnable
import apysc as ap


def on_animation_complete(
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
    ap.trace('Animation complete!')


ap.Stage(
    stage_width=200, stage_height=200, background_color='#333',
    stage_elem_id='stage')
sprite: ap.Sprite = ap.Sprite()
sprite.graphics.begin_fill(color='#0af')
rectangle: ap.Rectangle = sprite.graphics.draw_rect(
    x=50, y=50, width=50, height=50)

animation_move: ap.AnimationMove = rectangle.animation_move(
    x=100, y=100, duration=1000)
animation_move.animation_complete(on_animation_complete)
animation_move.start()
```

## animation_complete API

<span class="inconspicuous-txt">特記事項: このAPIドキュメントはドキュメントビルド用のスクリプトによって自動で生成・同期されています。そのためもしかしたらこの節の内容は前節までの内容と重複している場合があります。</span>

**[インターフェイスの構造]** `animation_complete(self, handler:Callable[[_ForwardRef('animation_event.AnimationEvent'), ~_O], NoneType], *, options:Union[~_O, NoneType]=None) -> 'AnimationBase'`<hr>

**[インターフェイス概要]** アニメーション終了時のイベントリスナーの設定を追加します。<hr>

**[引数]**

- `handler`: _Handler
  - アニメーション終了時に実行される関数もしくはメソッド。

- `options`: dict or None, default None
  - ハンドラに渡される省略が可能な追加のパラメーターとしての辞書。

<hr>

**[返却値]**

- `self`: AnimatonBase
  - このインスタンス。

<hr>

**[エラー発生条件]**

- Exception: もしアニメーション開始後にこのインターフェイスを呼び出している場合。

<hr>

**[特記事項]**

このインターフェイスはアニメーション開始前にのみ利用することができます。<hr>

**[コードサンプル]**

```py
>>> import apysc as ap
>>> def on_animation_complete(
...         e: ap.AnimationEvent[ap.Rectangle],
...         options: dict) -> None:
...     ap.trace('Animation completed!')
>>> stage: ap.Stage = ap.Stage()
>>> sprite: ap.Sprite = ap.Sprite()
>>> sprite.graphics.begin_fill(color='#0af')
>>> rectangle: ap.Rectangle = sprite.graphics.draw_rect(
...     x=50, y=50, width=50, height=50)
>>> _ = rectangle.animation_x(
...     x=100,
... ).animation_complete(on_animation_complete).start()
```

<hr>

**[関連資料]**

- [ハンドラのoptions引数の型について](https://simon-ritchie.github.io/apysc/jp_about_handler_options_type.html)