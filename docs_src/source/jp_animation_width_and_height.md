<span class="inconspicuous-txt">※この翻訳ドキュメントはスクリプトによって出力・同期されています。内容が怪しそうな場合は<a href="https://github.com/simon-ritchie/apysc/issues" target="_blank">GitHubにissue</a>を追加したり[英語の原文](https://simon-ritchie.github.io/apysc/en/animation_width_and_height.html)の確認をお願いします。</span>

# animation_width と animation_height のインターフェイス

このページでは`animation_width`と`animation_height`メソッドの各インターフェイスについて説明します。

## 各インターフェイスの概要

`animation_width`インターフェイスは`AnimationWidth`クラスのインスタンスを生成します。そのインスタンスを使って幅のアニメーションを設定することができます。

同様に`animation_height`メソッドのインターフェイスは`AnimationHeight`クラスのインスタンスを生成します。そのインスタンスを使って高さのアニメーションを設定することができます。

これらの各インターフェイスは`Rectangle`クラスなどの`DisplayObject`の各サブクラス上に存在します。

## 基本的な使い方

以下のコード例では`animation_width`メソッドを使って幅（50から100）のアニメーションを設定しています。

```py
# runnable
import apysc as ap

DURATION: int = 1000
EASING: ap.Easing = ap.Easing.EASE_OUT_QUINT


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
    animation_width: ap.AnimationWidth = rectangle.animation_width(
        width=50, duration=DURATION, easing=EASING
    )
    animation_width.animation_complete(on_animation_complete_2)
    animation_width.start()


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
    animation_width: ap.AnimationWidth = rectangle.animation_width(
        width=100, duration=DURATION, easing=EASING
    )
    animation_width.animation_complete(on_animation_complete_1)
    animation_width.start()


ap.Stage(
    stage_width=200,
    stage_height=150,
    background_color=ap.Color("#333"),
    stage_elem_id="stage",
)
sprite: ap.Sprite = ap.Sprite()
sprite.graphics.begin_fill(color=ap.Color("#00aaff"))
rectangle: ap.Rectangle = sprite.graphics.draw_rect(x=50, y=50, width=50, height=50)
animation_width: ap.AnimationWidth = rectangle.animation_width(
    width=100, duration=DURATION, easing=EASING
)
animation_width.animation_complete(on_animation_complete_1)
animation_width.start()

ap.save_overall_html(dest_dir_path="./animation_width_basic_usage/")
```

<iframe src="static/animation_width_basic_usage/index.html" width="200" height="150"></iframe>

同様に以下のコード例では`animation_height`メソッドを使って高さのアニメーションを設定しています。

```py
# runnable
import apysc as ap

DURATION: int = 1000
EASING: ap.Easing = ap.Easing.EASE_OUT_QUINT


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
    animation_height: ap.AnimationHeight = rectangle.animation_height(
        height=50, duration=DURATION, easing=EASING
    )
    animation_height.animation_complete(on_animation_complete_2)
    animation_height.start()


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
    animation_height: ap.AnimationHeight = rectangle.animation_height(
        height=100, duration=DURATION, easing=EASING
    )
    animation_height.animation_complete(on_animation_complete_1)
    animation_height.start()


ap.Stage(
    stage_width=150,
    stage_height=200,
    background_color=ap.Color("#333"),
    stage_elem_id="stage",
)
sprite: ap.Sprite = ap.Sprite()
sprite.graphics.begin_fill(color=ap.Color("#00aaff"))
rectangle: ap.Rectangle = sprite.graphics.draw_rect(x=50, y=50, width=50, height=50)
animation_height: ap.AnimationHeight = rectangle.animation_height(
    height=100, duration=DURATION, easing=EASING
)
animation_height.animation_complete(on_animation_complete_1)
animation_height.start()

ap.save_overall_html(dest_dir_path="./animation_height_basic_usage/")
```

<iframe src="static/animation_height_basic_usage/index.html" width="150" height="200"></iframe>

## Ellipse のインスタンスにおける特記事項

楕円のインスタンス（`Ellipse`クラス）の`animation_width`と`animation_height`の各インターフェイスは内部実行が異なる都合で`AnimationWidth`クラスなどの代わりに`以下のコード例のようにAnimationWidthForEllipse`クラスと`AnimationHeightForEllipse`クラスのインスタンスを返却します:

```py
# runnable
import apysc as ap

ap.Stage(
    stage_width=150,
    stage_height=200,
    background_color=ap.Color("#333"),
    stage_elem_id="stage",
)
sprite: ap.Sprite = ap.Sprite()
sprite.graphics.begin_fill(color=ap.Color("#00aaff"))
ellipse: ap.Ellipse = sprite.graphics.draw_ellipse(x=100, y=100, width=100, height=100)
animation_width: ap.AnimationWidthForEllipse = ellipse.animation_width(
    width=200, duration=1000
)
animation_width.start()
```

## animation_width API

<span class="inconspicuous-txt">特記事項: このAPIドキュメントはドキュメントビルド用のスクリプトによって自動で生成・同期されています。そのためもしかしたらこの節の内容は前節までの内容と重複している場合があります。</span>

**[インターフェイスの構造]** `animation_width(self, *, width: Union[int, apysc._type.int.Int], duration: Union[int, apysc._type.int.Int] = 3000, delay: Union[int, apysc._type.int.Int] = 0, easing: apysc._animation.easing.Easing = <Easing.LINEAR: 'function(x) {return x;}'>) -> apysc._animation.animation_width.AnimationWidth`<hr>

**[インターフェイス概要]**

幅のアニメーションを設定します。<hr>

**[引数]**

- `width`: Int or int
  - 幅のアニメーションの最終値。

- `duration`: Int or int, default 3000
  - アニメーション完了までのミリ秒。

- `delay`: Int or int, default 0
  - アニメーション開始までの遅延時間のミリ秒。

- `easing`: Easing, default Easing.LINEAR
  - イージング設定。

<hr>

**[返却値]**

- `animation_width`: AnimationWidth
  - 生成されたアニメーションのインスタンス。

<hr>

**[特記事項]**

アニメーションを開始するには返却されたインスタンスの`start`メソッドを呼び出す必要があります。<hr>

**[コードサンプル]**

```py
>>> import apysc as ap
>>> stage: ap.Stage = ap.Stage()
>>> sprite: ap.Sprite = ap.Sprite()
>>> sprite.graphics.begin_fill(color=ap.Color("#0af"))
>>> rectangle: ap.Rectangle = sprite.graphics.draw_rect(
...     x=50, y=50, width=50, height=50
... )
>>> _ = rectangle.animation_width(
...     width=100,
...     duration=1500,
...     easing=ap.Easing.EASE_OUT_QUINT,
... ).start()
```

<hr>

**[関連資料]**

- [各アニメーションインターフェイスの duration （アニメーション時間）設定](https://simon-ritchie.github.io/apysc/jp/jp_animation_duration.html)
- [各アニメーションインターフェイスの delay （遅延時間）設定](https://simon-ritchie.github.io/apysc/jp/jp_animation_delay.html)

- [各アニメーションインターフェイスの返却値](https://simon-ritchie.github.io/apysc/jp/jp_animation_return_value.html)
- [連続したアニメーション設定](https://simon-ritchie.github.io/apysc/jp/jp_sequential_animation.html)

- [animation_parallel インターフェイス](https://simon-ritchie.github.io/apysc/jp/jp_animation_parallel.html)
- [イージングのenum](https://simon-ritchie.github.io/apysc/jp/jp_easing_enum.html)

## animation_height API

<span class="inconspicuous-txt">特記事項: このAPIドキュメントはドキュメントビルド用のスクリプトによって自動で生成・同期されています。そのためもしかしたらこの節の内容は前節までの内容と重複している場合があります。</span>

**[インターフェイスの構造]** `animation_height(self, *, height: Union[int, apysc._type.int.Int], duration: Union[int, apysc._type.int.Int] = 3000, delay: Union[int, apysc._type.int.Int] = 0, easing: apysc._animation.easing.Easing = <Easing.LINEAR: 'function(x) {return x;}'>) -> apysc._animation.animation_height.AnimationHeight`<hr>

**[インターフェイス概要]**

高さのアニメーションを設定します。<hr>

**[引数]**

- `height`: Int or int
  - 高さのアニメーションの最終値。

- `duration`: Int or int, default 3000
  - アニメーション完了までのミリ秒。

- `delay`: Int or int, default 0
  - アニメーション開始までの遅延時間のミリ秒。

- `easing`: Easing, default Easing.LINEAR
  - イージング設定。

<hr>

**[返却値]**

- `animation_height`: AnimationHeight
  - 生成されたアニメーションのインスタンス。

<hr>

**[特記事項]**

アニメーションを開始するには返却されたインスタンスの`start`メソッドを呼び出す必要があります。<hr>

**[コードサンプル]**

```py
>>> import apysc as ap
>>> stage: ap.Stage = ap.Stage()
>>> sprite: ap.Sprite = ap.Sprite()
>>> sprite.graphics.begin_fill(color=ap.Color("#0af"))
>>> rectangle: ap.Rectangle = sprite.graphics.draw_rect(
...     x=50, y=50, width=50, height=50
... )
>>> _ = rectangle.animation_height(
...     height=100,
...     duration=1500,
...     easing=ap.Easing.EASE_OUT_QUINT,
... ).start()
```

<hr>

**[関連資料]**

- [各アニメーションインターフェイスの duration （アニメーション時間）設定](https://simon-ritchie.github.io/apysc/jp/jp_animation_duration.html)
- [各アニメーションインターフェイスの delay （遅延時間）設定](https://simon-ritchie.github.io/apysc/jp/jp_animation_delay.html)

- [各アニメーションインターフェイスの返却値](https://simon-ritchie.github.io/apysc/jp/jp_animation_return_value.html)
- [連続したアニメーション設定](https://simon-ritchie.github.io/apysc/jp/jp_sequential_animation.html)

- [animation_parallel インターフェイス](https://simon-ritchie.github.io/apysc/jp/jp_animation_parallel.html)
- [イージングのenum](https://simon-ritchie.github.io/apysc/jp/jp_easing_enum.html)