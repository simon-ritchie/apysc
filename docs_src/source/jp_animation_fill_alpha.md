<span class="inconspicuous-txt">※この翻訳ドキュメントはスクリプトによって出力・同期されています。内容が怪しそうな場合は<a href="https://github.com/simon-ritchie/apysc/issues" target="_blank">GitHubにissue</a>を追加したり[英語の原文](https://simon-ritchie.github.io/apysc/en/animation_fill_alpha.html)の確認をお願いします。</span>

# animation_fill_alpha インターフェイス

このページでは`animation_fill_alpha`メソッドのインターフェイスについて説明します。

## インターフェイス概要

`animation_fill_alpha`メソッドのインターフェイスでは`AnimationBase`のサブクラスであり且つアニメーション設定を扱う`ap.AnimationFillAlpha`クラスのインスタンスを生成します。そのインスタンスを使って塗りの透明度のアニメーションを設定することができます。

このインターフェイスは`Rectangle`や`Circle`クラスなどの`GraphicsBase`のサブクラスで存在します。

## 基本的な使い方

以下の例では1.0～0.0の塗りの透明度のアニメーションを`animation_fill_alpha`メソッドで設定しています。

```py
# runnable
import apysc as ap

DURATION: int = 1000


def on_animation_complete_1(e: ap.AnimationEvent[ap.Rectangle], options: dict) -> None:
    """
    The handler that animation calls when its end.

    Parameters
    ----------
    e : AnimationEvent
        Event instance.
    options : dict
        Optional arguments dictionary.
    """
    rectangle: ap.Rectangle = e.this.target
    rectangle.animation_fill_alpha(
        alpha=1.0,
        duration=DURATION,
    ).animation_complete(on_animation_complete_2).start()


def on_animation_complete_2(e: ap.AnimationEvent[ap.Rectangle], options: dict) -> None:
    """
    The handler that animation calls when its end.

    Parameters
    ----------
    e : AnimationEvent
        Event instance.
    options : dict
        Optional arguments dictionary.
    """
    rectangle: ap.Rectangle = e.this.target
    rectangle.animation_fill_alpha(
        alpha=0.0,
        duration=DURATION,
    ).animation_complete(on_animation_complete_1).start()


ap.Stage(
    stage_width=150,
    stage_height=150,
    background_color=ap.Color("#333"),
    stage_elem_id="stage",
)
sprite: ap.Sprite = ap.Sprite()
sprite.graphics.begin_fill(color=ap.Color("#00aaff"))
rectangle: ap.Rectangle = sprite.graphics.draw_rect(x=50, y=50, width=50, height=50)
rectangle.animation_fill_alpha(
    alpha=0.0,
    duration=DURATION,
).animation_complete(on_animation_complete_1).start()

ap.save_overall_html(dest_dir_path="./animation_fill_alpha_basic_usage/")
```

<iframe src="static/animation_fill_alpha_basic_usage/index.html" width="150" height="150"></iframe>

## animation_fill_alpha API

<span class="inconspicuous-txt">特記事項: このAPIドキュメントはドキュメントビルド用のスクリプトによって自動で生成・同期されています。そのためもしかしたらこの節の内容は前節までの内容と重複している場合があります。</span>

**[インターフェイスの構造]** `animation_fill_alpha(self, *, alpha: Union[float, apysc._type.number.Number], duration: Union[int, apysc._type.int.Int] = 3000, delay: Union[int, apysc._type.int.Int] = 0, easing: apysc._animation.easing.Easing = <Easing.LINEAR: 'function(x) {return x;}'>) -> apysc._animation.animation_fill_alpha.AnimationFillAlpha`<hr>

**[インターフェイス概要]**

塗りの透明度のアニメーション設定を行います。<hr>

**[引数]**

- `alpha`: Number or float
  - 透明度のアニメーションの最終値。

- `duration`: Int or int, default 3000
  - アニメーション完了までのミリ秒。

- `delay`: Int or int, default 0
  - アニメーション開始までの遅延時間のミリ秒。

- `easing`: Easing, default Easing.LINEAR
  - イージング設定。

<hr>

**[返却値]**

- `animation_fill_alpha`: AnimationFillAlpha
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
>>> circle: ap.Circle = sprite.graphics.draw_circle(x=100, y=100, radius=50)
>>> _ = circle.animation_y(
...     y=100,
...     duration=1500,
...     easing=ap.Easing.EASE_OUT_QUINT,
... ).start()
```

<hr>

**[関連資料]**

- [各アニメーションインターフェイスの duration （アニメーション時間）設定](https://simon-ritchie.github.io/apysc/jp/jp_animation_duration.html)
- [各アニメーションインターフェイスの返却値](https://simon-ritchie.github.io/apysc/jp/jp_animation_return_value.html)

- [連続したアニメーション設定](https://simon-ritchie.github.io/apysc/jp/jp_sequential_animation.html)
- [animation_parallel インターフェイス](https://simon-ritchie.github.io/apysc/jp/jp_animation_parallel.html)

- [イージングのenum](https://simon-ritchie.github.io/apysc/jp/jp_easing_enum.html)