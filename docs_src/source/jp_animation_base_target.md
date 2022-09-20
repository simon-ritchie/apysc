<span class="inconspicuous-txt">※この翻訳ドキュメントはスクリプトによって出力・同期されています。内容が怪しそうな場合は<a href="https://github.com/simon-ritchie/apysc/issues" target="_blank">GitHubにissue</a>を追加したり[英語の原文](https://simon-ritchie.github.io/apysc/en/animation_base_target.html)の確認をお願いします。</span>

# AnimationBase クラス target 属性のインターフェイス

このページでは`AnimationBase`クラスの`target`属性のインターフェイスについて説明します。

## 属性の概要

`target`属性はアニメーション対象のインスタンス（例: `Sprite`や`Rectangle`などのインスタンス）を返却します。

## 基本的な使い方

`AnimationBase`クラスの各サブクラス（例: `AnimationMove`や`AnimationX`クラスなど）はgetterの`target`属性を持っています。

```py
# runnable
import apysc as ap

ap.Stage(
    stage_width=200, stage_height=150, background_color="#333", stage_elem_id="stage"
)
sprite: ap.Sprite = ap.Sprite()
sprite.graphics.begin_fill(color="#00aaff")
rectangle: ap.Rectangle = sprite.graphics.draw_rect(x=50, y=50, width=50, height=50)
animation_x: ap.AnimationX = rectangle.animation_x(x=100)
assert isinstance(animation_x.target, ap.Rectangle)
```

## ジェネリックの型アノテーションについて

`AnimationBase`クラスとその各サブクラスにはジェネリックの型アノテーションを行うことができます。型アノテーションをした場合`target`属性の型はその型のインスタンスとなります。

以下のコードでは`[ap.Rectangle]`というジェネリックの型アノテーションを行っています。

```py
# runnable
import apysc as ap

ap.Stage(
    stage_width=200, stage_height=150, background_color="#333", stage_elem_id="stage"
)
sprite: ap.Sprite = ap.Sprite()
sprite.graphics.begin_fill(color="#00aaff")
rectangle: ap.Rectangle = sprite.graphics.draw_rect(x=50, y=50, width=50, height=50)
animation_x: ap.AnimationX[ap.Rectangle] = rectangle.animation_x(x=100)
assert isinstance(animation_x.target, ap.Rectangle)
```

イベントハンドラの`AnimationEvent`のインスタンスへジェネリックの型アノテーションを行うことも有益なケースがあります。この型アノテーションも`target`属性（`e.this.target`）の型に影響します。

```py
# runnable
import apysc as ap


def on_animation_complete(e: ap.AnimationEvent[ap.Rectangle], options: dict) -> None:
    """
    The handler the animation calls when its end.

    Parameters
    ----------
    e : ap.AnimationEvent
        Event instance.
    options : dict
        Optional arguments dictionary.
    """
    rectangle: ap.Rectangle = e.this.target
    rectangle.animation_x(x=50).start()


ap.Stage(
    stage_width=200, stage_height=150, background_color="#333", stage_elem_id="stage"
)
sprite: ap.Sprite = ap.Sprite()
sprite.graphics.begin_fill(color="#00aaff")
rectangle: ap.Rectangle = sprite.graphics.draw_rect(x=50, y=50, width=50, height=50)
animation_x: ap.AnimationX = rectangle.animation_x(x=100)
animation_x.animation_complete(on_animation_complete)
```

## target 属性のAPI

<span class="inconspicuous-txt">特記事項: このAPIドキュメントはドキュメントビルド用のスクリプトによって自動で生成・同期されています。そのためもしかしたらこの節の内容は前節までの内容と重複している場合があります。</span>

**[インターフェイス概要]**

アニメーション対象のインスタンスを取得します。<hr>

**[返却値]**

- `target`: VariableNameInterface
  - アニメーション対象のインスタンス。

<hr>

**[コードサンプル]**

```py
>>> import apysc as ap
>>> def on_animation_complete(
...     e: ap.AnimationEvent[ap.Rectangle], options: dict
... ) -> None:
...     rectangle: ap.Rectangle = e.this.target
>>> stage: ap.Stage = ap.Stage()
>>> sprite: ap.Sprite = ap.Sprite()
>>> sprite.graphics.begin_fill(color="#0af")
>>> rectangle: ap.Rectangle = sprite.graphics.draw_rect(
...     x=50, y=50, width=50, height=50
... )
>>> _ = (
...     rectangle.animation_x(
...         x=100,
...     )
...     .animation_complete(on_animation_complete)
...     .start()
... )
```