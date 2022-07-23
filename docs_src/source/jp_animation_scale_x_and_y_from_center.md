<span class="inconspicuous-txt">※この翻訳ドキュメントはスクリプトによって出力・同期されています。内容が怪しそうな場合は<a href="https://github.com/simon-ritchie/apysc/issues" target="_blank">GitHubにissue</a>を追加したり[英語の原文](https://simon-ritchie.github.io/apysc/en/animation_scale_x_and_y_from_center.html)の確認をお願いします。</span>

# animation_scale_x_from_center と animation_scale_y_from_center のインターフェイス

このページでは`animation_scale_x_from_center`と`animation_scale_y_from_center`メソッドの各インターフェイスについて説明します。

## 各インターフェイスの概要

`animation_scale_x_from_center`メソッドのインターフェイスは`ap.AnimationScaleXFromCenter`クラスのインスタンスを生成します。そのインスタンスを使って中央座標を基準としたX軸方向の拡縮のアニメーションを設定することができます。

同様に`animation_scale_y_from_center`メソッドのインターフェイスでは`ap.AnimationScaleYFromCenter`クラスのインスタンスを生成します。そのインスタンスを使ってY軸方向の拡縮のアニメーションを設定することができます。

これらのインターフェイスは`scale_x_from_center`や`scale_y_from_center`などのインターフェイスを持つ`Rectangle`や`Circle`などの`GraphicsBase`のサブクラス上に存在します。

## 基本的な使い方

以下のコード例ではX軸方向の拡縮（1.0から2.0）のアニメーションを`animation_scale_x_from_center`メソッドを使って左側の四角に設定しています。同様にY軸方向の拡縮のアニメーションを右側の四角に設定しています。

```py
# runnable
from enum import Enum

from typing_extensions import TypedDict

import apysc as ap

DURATION: int = 1000
EASING: ap.Easing = ap.Easing.EASE_OUT_QUINT


class Direction(Enum):
    X = 1
    Y = 2


class Options(TypedDict):
    direction: Direction


def on_animation_complete_1(
    e: ap.AnimationEvent[ap.Rectangle], options: Options
) -> None:
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
    SCALE: float = 1.0
    if options["direction"] == Direction.X:
        rectangle.animation_scale_x_from_center(
            scale_x_from_center=SCALE,
            duration=DURATION,
            easing=EASING,
        ).animation_complete(
            on_animation_complete_2,
            options=options,
        ).start()
    elif options["direction"] == Direction.Y:
        rectangle.animation_scale_y_from_center(
            scale_y_from_center=SCALE,
            duration=DURATION,
            easing=EASING,
        ).animation_complete(
            on_animation_complete_2,
            options=options,
        ).start()


def on_animation_complete_2(
    e: ap.AnimationEvent[ap.Rectangle], options: Options
) -> None:
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
    SCALE: float = 2.0
    if options["direction"] == Direction.X:
        rectangle.animation_scale_x_from_center(
            scale_x_from_center=SCALE,
            duration=DURATION,
            easing=EASING,
        ).animation_complete(
            on_animation_complete_1,
            options=options,
        ).start()
    elif options["direction"] == Direction.Y:
        rectangle.animation_scale_y_from_center(
            scale_y_from_center=SCALE,
            duration=DURATION,
            easing=EASING,
        ).animation_complete(
            on_animation_complete_1,
            options=options,
        ).start()


ap.Stage(
    stage_width=250, stage_height=150, background_color="#333", stage_elem_id="stage"
)
sprite: ap.Sprite = ap.Sprite()
sprite.graphics.begin_fill(color="#0af")
left_rectangle: ap.Rectangle = sprite.graphics.draw_rect(
    x=50, y=50, width=50, height=50
)
right_rectangle: ap.Rectangle = sprite.graphics.draw_rect(
    x=150, y=50, width=50, height=50
)

options: Options = {"direction": Direction.X}
left_rectangle.animation_scale_x_from_center(
    scale_x_from_center=2.0,
    duration=DURATION,
    easing=EASING,
).animation_complete(
    on_animation_complete_1,
    options=options,
).start()

options = {"direction": Direction.Y}
right_rectangle.animation_scale_y_from_center(
    scale_y_from_center=2.0,
    duration=DURATION,
    easing=EASING,
).animation_complete(
    on_animation_complete_1,
    options=options,
).start()

ap.save_overall_html(dest_dir_path="./animation_scale_x_and_y_from_center_basic_usage/")
```

<iframe src="static/animation_scale_x_and_y_from_center_basic_usage/index.html" width="250" height="150"></iframe>

## animation_scale_x_from_center API

<span class="inconspicuous-txt">特記事項: このAPIドキュメントはドキュメントビルド用のスクリプトによって自動で生成・同期されています。そのためもしかしたらこの節の内容は前節までの内容と重複している場合があります。</span>

**[インターフェイスの構造]** `animation_scale_x_from_center(self, *, scale_x_from_center: Union[float, apysc._type.number.Number], duration: Union[int, apysc._type.int.Int] = 3000, delay: Union[int, apysc._type.int.Int] = 0, easing: apysc._animation.easing.Easing = <Easing.LINEAR: 'function(x) {return x;}'>) -> apysc._animation.animation_scale_x_from_center.AnimationScaleXFromCenter`<hr>

**[インターフェイス概要]** 中央座標を基準としたX軸の拡縮アニメーションを設定します。<hr>

**[引数]**

- `scale_x_from_center`: Number or float
  - X軸の拡縮のアニメーションの最終値。

- `duration`: Int or int, default 3000
  - アニメーション完了までのミリ秒。

- `delay`: Int or int, default 0
  - アニメーション開始までの遅延時間のミリ秒。

- `easing`: Easing, default Easing.LINEAR
  - イージング設定。

<hr>

**[返却値]**

- `animation_scale_x_from_center`: AnimationScaleXFromCenter
  - 生成されたアニメーションのインスタンス。

<hr>

**[特記事項]**

アニメーションを開始するには返却されたインスタンスの`start`メソッドを呼び出す必要があります。<hr>

**[コードサンプル]**

```py
>>> import apysc as ap
>>> stage: ap.Stage = ap.Stage()
>>> sprite: ap.Sprite = ap.Sprite()
>>> sprite.graphics.begin_fill(color='#0af')
>>> rectangle: ap.Rectangle = sprite.graphics.draw_rect(
...     x=50, y=50, width=50, height=50)
>>> _ = rectangle.animation_scale_x_from_center(
...     scale_x_from_center=0.5,
...     duration=1500,
...     easing=ap.Easing.EASE_OUT_QUINT,
... ).start()
```

<hr>

**[関連資料]**

- [各アニメーションインターフェイスの duration （アニメーション時間）設定](https://simon-ritchie.github.io/apysc/en/jp_animation_duration.html)
- [各アニメーションインターフェイスの delay （遅延時間）設定](https://simon-ritchie.github.io/apysc/en/jp_animation_delay.html)

- [各アニメーションインターフェイスの返却値](https://simon-ritchie.github.io/apysc/en/jp_animation_return_value.html)
- [連続したアニメーション設定](https://simon-ritchie.github.io/apysc/en/jp_sequential_animation.html)

- [animation_parallel （並列アニメーション設定）のインターフェイス](https://simon-ritchie.github.io/apysc/en/jp_animation_parallel.html)
- [イージングのenum](https://simon-ritchie.github.io/apysc/en/jp_easing_enum.html)

## animation_scale_y_from_center API

<span class="inconspicuous-txt">特記事項: このAPIドキュメントはドキュメントビルド用のスクリプトによって自動で生成・同期されています。そのためもしかしたらこの節の内容は前節までの内容と重複している場合があります。</span>

**[インターフェイスの構造]** `animation_scale_y_from_center(self, *, scale_y_from_center: Union[float, apysc._type.number.Number], duration: Union[int, apysc._type.int.Int] = 3000, delay: Union[int, apysc._type.int.Int] = 0, easing: apysc._animation.easing.Easing = <Easing.LINEAR: 'function(x) {return x;}'>) -> apysc._animation.animation_scale_y_from_center.AnimationScaleYFromCenter`<hr>

**[インターフェイス概要]** 中央座標を基準としたY軸の拡縮アニメーションを設定します。<hr>

**[引数]**

- `scale_y_from_center`: Number or float
  - Y軸の拡縮のアニメーションの最終値。

- `duration`: Int or int, default 3000
  - アニメーション完了までのミリ秒。

- `delay`: Int or int, default 0
  - アニメーション開始までの遅延時間のミリ秒。

- `easing`: Easing, default Easing.LINEAR
  - イージング設定。

<hr>

**[返却値]**

- `animation_scale_y_from_center`: AnimationScaleYFromCenter
  - 生成されたアニメーションのインスタンス。

<hr>

**[特記事項]**

アニメーションを開始するには返却されたインスタンスの`start`メソッドを呼び出す必要があります。<hr>

**[コードサンプル]**

```py
>>> import apysc as ap
>>> stage: ap.Stage = ap.Stage()
>>> sprite: ap.Sprite = ap.Sprite()
>>> sprite.graphics.begin_fill(color='#0af')
>>> rectangle: ap.Rectangle = sprite.graphics.draw_rect(
...     x=50, y=50, width=50, height=50)
>>> _ = rectangle.animation_scale_y_from_center(
...     scale_y_from_center=0.5,
...     duration=1500,
...     easing=ap.Easing.EASE_OUT_QUINT,
... ).start()
```

<hr>

**[関連資料]**

- [各アニメーションインターフェイスの duration （アニメーション時間）設定](https://simon-ritchie.github.io/apysc/en/jp_animation_duration.html)
- [各アニメーションインターフェイスの delay （遅延時間）設定](https://simon-ritchie.github.io/apysc/en/jp_animation_delay.html)

- [各アニメーションインターフェイスの返却値](https://simon-ritchie.github.io/apysc/en/jp_animation_return_value.html)
- [連続したアニメーション設定](https://simon-ritchie.github.io/apysc/en/jp_sequential_animation.html)

- [animation_parallel （並列アニメーション設定）のインターフェイス](https://simon-ritchie.github.io/apysc/en/jp_animation_parallel.html)
- [イージングのenum](https://simon-ritchie.github.io/apysc/en/jp_easing_enum.html)