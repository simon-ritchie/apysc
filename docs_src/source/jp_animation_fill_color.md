<span class="inconspicuous-txt">※この翻訳ドキュメントはスクリプトによって出力・同期されています。内容が怪しそうな場合は<a href="https://github.com/simon-ritchie/apysc/issues" target="_blank">GitHubにissue</a>を追加したり[英語の原文](animation_fill_color.md)の確認をお願いします。</span>

# animation_fill_color インターフェイス

このページでは`animation_fill_color`メソッドのインターフェイスについて説明します。

## インターフェイス概要

`animation_fill_color`メソッドのインターフェイスは`ap.AnimationFillColor`クラスのインスタンスを生成します。そのインスタンスを使って塗りのアニメーションを行うことができます。

このインターフェイスは`Rectangle`や`Circle`クラスなどの`GraphicsBase`クラスの各サブクラスに存在します。

## 使い方例

以下のコード例では`animation_fill_color`メソッドを使って塗りの色をシアン（`#0af`）からマゼンタ（`#f0a`）へとアニメーションさせています。

```py
# runnable
import apysc as ap

DURATION: int = 1000


def on_animation_complete_1(
        e: ap.AnimationEvent[ap.Rectangle], options: dict) -> None:
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
    rectangle.animation_fill_color(
        fill_color='#0af', duration=DURATION,
    ).animation_complete(on_animation_complete_2).start()


def on_animation_complete_2(
        e: ap.AnimationEvent[ap.Rectangle], options: dict) -> None:
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
    rectangle.animation_fill_color(
        fill_color='#f0a', duration=DURATION,
    ).animation_complete(on_animation_complete_1).start()


ap.Stage(
    stage_width=150, stage_height=150,
    background_color='#333', stage_elem_id='stage')
sprite: ap.Sprite = ap.Sprite()
sprite.graphics.begin_fill(color='#0af')
rectangle: ap.Rectangle = sprite.graphics.draw_rect(
    x=50, y=50, width=50, height=50)
rectangle.animation_fill_color(
    fill_color='#f0a', duration=DURATION,
).animation_complete(on_animation_complete_1).start()

ap.save_overall_html(
    dest_dir_path='./animation_fill_color_basic_usage/')
```

<iframe src="static/animation_fill_color_basic_usage/index.html" width="150" height="150"></iframe>

## animation_fill_color API

<span class="inconspicuous-txt">特記事項: このAPIドキュメントはドキュメントビルド用のスクリプトによって自動で生成・同期されています。そのためもしかしたらこの節の内容は前節までの内容と重複している場合があります。</span>

**[インターフェイスの構造]** `animation_fill_color(self, fill_color:~StrOrString, *, duration:Union[int, apysc._type.int.Int]=3000, delay:Union[int, apysc._type.int.Int]=0, easing:apysc._animation.easing.Easing=<Easing.LINEAR: 'function(x) {return x;}'>) -> apysc._animation.animation_fill_color.AnimationFillColor`<hr>

**[インターフェイス概要]** 塗りの色のアニメーションの設定を行います。.<hr>

**[引数]**

- `fill_color`: str or String
  - アニメーションの最終的な塗りの色（16進数の色の文字列）。

- `duration`: Int or int, default 3000
  - アニメーション完了までのミリ秒。

- `delay`: Int or int, default 0
  - アニメーション開始までの遅延時間のミリ秒。

- `easing`: Easing, default Easing.LINEAR
  - イージング設定。

<hr>

**[返却値]**

- `animation_fill_color`: AnimationFillColor
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
>>> _ = rectangle.animation_fill_color(
...     fill_color='#f0a',
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