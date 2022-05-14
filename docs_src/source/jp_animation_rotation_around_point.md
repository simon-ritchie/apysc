<span class="inconspicuous-txt">※この翻訳ドキュメントはスクリプトによって出力・同期されています。内容が怪しそうな場合は<a href="https://github.com/simon-ritchie/apysc/issues" target="_blank">GitHubにissue</a>を追加したり[英語の原文](https://simon-ritchie.github.io/apysc/en/animation_rotation_around_point.html)の確認をお願いします。</span>

# animation_rotation_around_point インターフェイス

このページでは`animation_rotation_around_point`メソッドのインターフェイスについて説明します。

## インターフェイス概要

`animation_rotation_around_point`メソッドのインターフェイスは`ap.AnimationRotationAroundPoint`クラスのインスタンスを生成します。そのインスタンスを使って任意の座標を基準とした回転のアニメーションを設定することができます。

このインターフェイスは`Rectangle`や`Circle`クラスなどの`GraphicsBase`のサブクラスで存在します。

## 基本的な使い方

`animation_rotation_around_point`メソッドは回転角度のrotation、回転の基準座標となるxとyの各引数を必要とします。

以下のコード例ではx=100, y=100の座標（四角の右下の位置）を基準に0度から90度の回転のアニメーションを設定しています。

```py
# runnable
import apysc as ap

DURATION: int = 1000


def on_animation_complete_1(
        e: ap.AnimationEvent[ap.Rectangle], options: dict) -> None:
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
    rectangle.animation_rotation_around_point(
        rotation_around_point=0,
        x=100,
        y=100,
        duration=1000,
        easing=ap.Easing.EASE_OUT_QUINT,
    ).animation_complete(on_animation_complete_2).start()


def on_animation_complete_2(
        e: ap.AnimationEvent[ap.Rectangle], options: dict) -> None:
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
    rectangle.animation_rotation_around_point(
        rotation_around_point=90,
        x=100,
        y=100,
        duration=1000,
        easing=ap.Easing.EASE_OUT_QUINT,
    ).animation_complete(on_animation_complete_1).start()


ap.Stage(
    stage_width=150, stage_height=150,
    background_color='#333', stage_elem_id='stage')
sprite: ap.Sprite = ap.Sprite()
sprite.graphics.begin_fill(color='#0af')
rectangle: ap.Rectangle = sprite.graphics.draw_rect(
    x=50, y=50, width=50, height=50)
rectangle.animation_rotation_around_point(
    rotation_around_point=90,
    x=100,
    y=100,
    duration=1000,
    easing=ap.Easing.EASE_OUT_QUINT,
).animation_complete(on_animation_complete_1).start()

ap.save_overall_html(
    dest_dir_path='./animation_rotation_around_point_basic_usage/')
```

<iframe src="static/animation_rotation_around_point_basic_usage/index.html" width="150" height="150"></iframe>

## animation_rotation_around_point API

<span class="inconspicuous-txt">特記事項: このAPIドキュメントはドキュメントビルド用のスクリプトによって自動で生成・同期されています。そのためもしかしたらこの節の内容は前節までの内容と重複している場合があります。</span>

**[インターフェイスの構造]** `animation_rotation_around_point(self, rotation_around_point: Union[int, apysc._type.int.Int], x: Union[int, apysc._type.int.Int], y: Union[int, apysc._type.int.Int], *, duration: Union[int, apysc._type.int.Int] = 3000, delay: Union[int, apysc._type.int.Int] = 0, easing: apysc._animation.easing.Easing = <Easing.LINEAR: 'function(x) {return x;}'>) -> apysc._animation.animation_rotation_around_point.AnimationRotationAroundPoint`<hr>

**[インターフェイス概要]** 指定された座標を基準とした回転のアニメーションを設定します。<hr>

**[引数]**

- `rotation_around_point`: Int or int
  - 回転のアニメーションの回転量の最終値。

- `x`: Int or int
  - X座標。

- `y`: Int or int
  - Y座標。

- `duration`: Int or int, default 3000
  - アニメーション完了までのミリ秒。

- `delay`: Int or int, default 0
  - アニメーション開始までの遅延時間のミリ秒。

- `easing`: Easing, default Easing.LINEAR
  - イージング設定。

<hr>

**[返却値]**

- `animation_rotation_around_point`: AnimationRotationAroundPoint
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
>>> _ = rectangle.animation_rotation_around_point(
...     rotation_around_point=90,
...     x=ap.Int(100),
...     y=ap.Int(100),
...     duration=1500,
...     easing=ap.Easing.EASE_OUT_QUINT,
... ).start()
```

<hr>

**[関連資料]**

- [各アニメーションインターフェイスの duration （アニメーション時間）設定](https://simon-ritchie.github.io/apysc/jp_animation_duration.html)
- [各アニメーションインターフェイスの delay （遅延時間）設定](https://simon-ritchie.github.io/apysc/jp_animation_delay.html)

- [各アニメーションインターフェイスの返却値](https://simon-ritchie.github.io/apysc/jp_animation_return_value.html)
- [連続したアニメーション設定](https://simon-ritchie.github.io/apysc/jp_sequential_animation.html)

- [animation_parallel （並列アニメーション設定）のインターフェイス](https://simon-ritchie.github.io/apysc/jp_animation_parallel.html)
- [イージングのenum](https://simon-ritchie.github.io/apysc/jp_easing_enum.html)