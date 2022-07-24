<span class="inconspicuous-txt">※この翻訳ドキュメントはスクリプトによって出力・同期されています。内容が怪しそうな場合は<a href="https://github.com/simon-ritchie/apysc/issues" target="_blank">GitHubにissue</a>を追加したり[英語の原文](https://simon-ritchie.github.io/apysc/en/animation_x.html)の確認をお願いします。</span>

# animation_x インターフェイス

このページでは`animation_x`メソッドのインターフェイスについて説明します。

## インターフェイス概要

`animation_x`メソッドのインターフェイスは`AnimationX`のインスタンスを生成します。そのインスタンスを使ってX座標のアニメーションを設定することができます。

このインターフェイスは`Sprite`や`Rectangle`などの`DisplayObject`の各サブクラスに存在します。

## 基本的な使い方

以下の例では`animation_x`メソッドを使ってX座標（50から100）のアニメーションを設定しています。

```py
# runnable
import apysc as ap

EASING: ap.Easing = ap.Easing.EASE_OUT_QUINT
DURATION: int = 1000


def on_animation_complete_1(e: ap.AnimationEvent[ap.Rectangle], options: dict) -> None:
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
        x=50, duration=DURATION, easing=EASING
    )
    animation_x.animation_complete(on_animation_complete_2)
    animation_x.start()


def on_animation_complete_2(e: ap.AnimationEvent[ap.Rectangle], options: dict) -> None:
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
        x=100, duration=DURATION, easing=EASING
    )
    animation_x.animation_complete(on_animation_complete_1)
    animation_x.start()


ap.Stage(
    stage_width=200, stage_height=150, background_color="#333", stage_elem_id="stage"
)
sprite: ap.Sprite = ap.Sprite()
sprite.graphics.begin_fill(color="#00aaff")
rectangle: ap.Rectangle = sprite.graphics.draw_rect(x=50, y=50, width=50, height=50)
animation_x: ap.AnimationX = rectangle.animation_x(
    x=100, duration=DURATION, easing=EASING
)
animation_x.animation_complete(on_animation_complete_1)
animation_x.start()

ap.save_overall_html(dest_dir_path="./animation_x_basic_usage/")
```

<iframe src="static/animation_x_basic_usage/index.html" width="200" height="150"></iframe>

## Circle と Ellipse の各クラスの特記事項

内部実装が異なるため`Circle`と`Ellipse`の各クラスの`animation_x`インターフェイスは`AnimationX`の代わりに`AnimationCx`クラス（center-x）のインスタンスを返却します。

```py
# runnable
import apysc as ap

ap.Stage(
    stage_width=200, stage_height=150, background_color="#333", stage_elem_id="stage"
)
sprite: ap.Sprite = ap.Sprite()
sprite.graphics.begin_fill(color="#00aaff")
circle: ap.Circle = sprite.graphics.draw_circle(x=100, y=100, radius=50)
animation_cx: ap.AnimationCx = circle.animation_x(
    x=100, duration=1000, easing=ap.Easing.EASE_OUT_QUINT
)
```

## animation_x API

<span class="inconspicuous-txt">特記事項: このAPIドキュメントはドキュメントビルド用のスクリプトによって自動で生成・同期されています。そのためもしかしたらこの節の内容は前節までの内容と重複している場合があります。</span>

**[インターフェイスの構造]** `animation_x(self, *, x: Union[int, apysc._type.int.Int], duration: Union[int, apysc._type.int.Int] = 3000, delay: Union[int, apysc._type.int.Int] = 0, easing: apysc._animation.easing.Easing = <Easing.LINEAR: 'function(x) {return x;}'>) -> apysc._animation.animation_x.AnimationX`<hr>

**[インターフェイス概要]** X座標のアニメーションを設定します。<hr>

**[引数]**

- `x`: Int or int
  - 最終的なX座標。

- `duration`: Int or int, default 3000
  - アニメーション完了までのミリ秒。

- `delay`: Int or int, default 0
  - アニメーション開始までの遅延時間のミリ秒。

- `easing`: Easing, default Easing.LINEAR
  - イージング設定。

<hr>

**[返却値]**

- `animation_x`: AnimationX
  - 生成されたアニメーションのインスタンス。

<hr>

**[特記事項]**

アニメーションを開始するには返却されたインスタンスの`start`メソッドを呼び出す必要があります。<hr>

**[コードサンプル]**

```py
>>> import apysc as ap
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
```

<hr>

**[関連資料]**

- [各アニメーションインターフェイスの duration （アニメーション時間）設定](https://simon-ritchie.github.io/apysc/en/jp_animation_duration.html)
- [各アニメーションインターフェイスの delay （遅延時間）設定](https://simon-ritchie.github.io/apysc/en/jp_animation_delay.html)

- [各アニメーションインターフェイスの返却値](https://simon-ritchie.github.io/apysc/en/jp_animation_return_value.html)
- [連続したアニメーション設定](https://simon-ritchie.github.io/apysc/en/jp_sequential_animation.html)

- [animation_parallel （並列アニメーション設定）のインターフェイス](https://simon-ritchie.github.io/apysc/en/jp_animation_parallel.html)
- [イージングのenum](https://simon-ritchie.github.io/apysc/en/jp_easing_enum.html)