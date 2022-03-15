<span class="inconspicuous-txt">※この翻訳ドキュメントはスクリプトによって出力・同期されています。内容が怪しそうな場合は<a href="https://github.com/simon-ritchie/apysc/issues" target="_blank">GitHubにissue</a>を追加したり[英語の原文](animation_parallel.md)の確認をお願いします。</span>

# animation_parallel インターフェイス

このページでは`animation_parallel`のインターフェイスについて説明します。

## インターフェイス概要

`animation_parallel`メソッドのインターフェイスは`AnimationParallel`クラスのインスタンスを生成します。このインスタンスを使うことで複数のアニメーションの同時実行の設定を行うことができます。

このインターフェイスは`Sprite`や`Rectangle`などの`DisplayObject`の各サブクラスに存在します。

## 使い方例

`animation_parallel`メソッドを使ってこのインターフェイスを使用することができます。`animations`引数の値は各アニメーションの設定値の指定を必要としません。

以下のコード例ではX座標、塗りの透明度、塗りの色、そして線の幅に対するアニメーションを同時に実行しています。

```py
# runnable
import apysc as ap

ap.Stage(
    stage_width=400, stage_height=150, background_color='#333',
    stage_elem_id='stage')
sprite: ap.Sprite = ap.Sprite()
sprite.graphics.begin_fill(color='#0af')
sprite.graphics.line_style(color='#fff', thickness=3)

rectangle: ap.Rectangle = sprite.graphics.draw_rect(
    x=50, y=50, width=50, height=50)
rectangle.animation_parallel(
    animations=[
        rectangle.animation_x(x=300),
        rectangle.animation_fill_color(fill_color='#f0a'),
        rectangle.animation_fill_alpha(alpha=0.3),
        rectangle.animation_line_thickness(thickness=7),
    ],
    duration=3000, delay=3000, easing=ap.Easing.EASE_OUT_QUINT,
).start()

ap.save_overall_html(
    dest_dir_path='animation_parallel_basic_usage/')
```

<iframe src="static/animation_parallel_basic_usage/index.html" width="400" height="150"></iframe>

## 各アニメーションのduration、delay、easingの設定についての特記事項

各アニメーションごとの`duration`や`delay`、`easing`の引数設定は`animation_parallel`メソッド側の値が使用されるため設定できません。もし何らかの値を設定した場合にはエラーとなります。

```py
...
rectangle.animation_parallel(
    animations=[
        rectangle.animation_x(x=300, duration=1000),
    ],
    duration=3000, delay=2000, easing=ap.Easing.EASE_OUT_QUINT,
)
...
```

```
ValueError: There is an animation target that is changed duration setting: 1000
The duration setting of animation in the `animations` argument can not be changed.
Target animation type: <class 'apysc._animation.animation_x.AnimationX'>
```

## animation_parallel API

<span class="inconspicuous-txt">特記事項: このAPIドキュメントはドキュメントビルド用のスクリプトによって自動で生成・同期されています。そのためもしかしたらこの節の内容は前節までの内容と重複している場合があります。</span>

**[インターフェイスの構造]** `animation_parallel(self, animations:List[apysc._animation.animation_base.AnimationBase], *, duration:Union[int, apysc._type.int.Int]=3000, delay:Union[int, apysc._type.int.Int]=0, easing:apysc._animation.easing.Easing=<Easing.LINEAR: 'function(x) {return x;}'>) -> apysc._animation.animation_parallel.AnimationParallel`<hr>

**[インターフェイス概要]** アニメーションの並列実行設定を行います。<hr>

**[引数]**

- `animations`: list of AnimationBase
  - 対象の各アニメーションの設定。

- `duration`: Int or int, default 3000
  - アニメーション完了までのミリ秒。

- `delay`: Int or int, default 0
  - アニメーション開始までの遅延時間のミリ秒。

- `easing`: Easing, default Easing.LINEAR
  - イージング設定。

<hr>

**[返却値]**

- `animation_parallel`: AnimationParallel
  - 生成されたアニメーションのインスタンス。

<hr>

**[エラー発生条件]**

- ValueError: <br> ・もし各アニメーションの対象のインスタンスがこのインスタンスでは無い場合。<br> ・もし`animations`引数の各アニメーションのderationやdelay、easingの設定が変更去れている場合。

<hr>

**[特記事項]**

 ・アニメーションを開始するには返却されたインスタンスの`start`メソッドを呼び出す必要があります。 <br> ・`animations`引数の値には`AnimationParallel`クラスのインスタンスを含めることはできません。 <br> ・このインターフェイスは`animations`引数内の値のduration, delay, easingの各引数の設定を無視します（代わりにこのインターフェイス自身のそれらの引数の設定を利用してください）。<hr>

**[コードサンプル]**

```py
>>> import apysc as ap
>>> stage: ap.Stage = ap.Stage()
>>> sprite: ap.Sprite = ap.Sprite()
>>> sprite.graphics.begin_fill(color='#0af')
>>> rectangle: ap.Rectangle = sprite.graphics.draw_rect(
...     x=50, y=50, width=50, height=50)
>>> _ = rectangle.animation_parallel(
...     animations=[
...         rectangle.animation_x(x=100),
...         rectangle.animation_fill_color(fill_color='#f0a'),
...         rectangle.animation_fill_alpha(alpha=0.5),
...     ],
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

- [イージングのenum](https://simon-ritchie.github.io/apysc/jp_easing_enum.html)