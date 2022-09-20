<span class="inconspicuous-txt">※この翻訳ドキュメントはスクリプトによって出力・同期されています。内容が怪しそうな場合は<a href="https://github.com/simon-ritchie/apysc/issues" target="_blank">GitHubにissue</a>を追加したり[英語の原文](https://simon-ritchie.github.io/apysc/en/animation_event.html)の確認をお願いします。</span>

# AnimationEvent クラス

このページでは`AnimationEvent`クラスについて説明します。

## クラス概要

アニメーション終了時のイベントなどの各アニメーション関連のイベントで`AnimationEvent`クラスは使用されます。各アニメーションのインターフェイスはイベントのハンドラへこのイベントのインスタンスを渡します。

## 基本的な使い方

以下の例ではアニメーション完了時のイベントのハンドラへ`e: ap.AnimationEvent`という指定で`AnimationEvent`のインスタンスの引数を設定しています。

```py
# runnable
import apysc as ap


def on_animation_complete(e: ap.AnimationEvent, options: dict) -> None:
    """
    The handler that animation calls when its end.

    Parameters
    ----------
    e : ap.AnimationEvent
        Event instance.
    options : dict
        Optional arguments dictionary.
    """
    ap.trace("Animation is completed!")


ap.Stage(
    stage_width=200, stage_height=150, background_color="#333", stage_elem_id="stage"
)
sprite: ap.Sprite = ap.Sprite()
sprite.graphics.begin_fill(color="#00aaff")
rectangle: ap.Rectangle = sprite.graphics.draw_rect(x=50, y=50, width=50, height=50)
animation_x: ap.AnimationX = rectangle.animation_x(x=100)
animation_x.animation_complete(on_animation_complete)
animation_x.start()
```

## this属性

`AnimationEvent`のインスタンスの`this`属性は`AnimationMove`や`AnimationX`等の`AnimationEvent`クラスのサブクラスになります。

この属性の型は呼んだアニメーションのインターフェイスによって変動します。例えば`animation_x`のインターフェイスであれば`this`属性の型は`AnimationX`クラスのインスタンスとなります。

```py
# runnable
import apysc as ap


def on_animation_complete(e: ap.AnimationEvent, options: dict) -> None:
    """
    The handler that animation calls when its end.

    Parameters
    ----------
    e : ap.AnimationEvent
        Event instance.
    options : dict
        Optional arguments dictionary.
    """
    assert isinstance(e.this, ap.AnimationX)


ap.Stage(
    stage_width=200, stage_height=150, background_color="#333", stage_elem_id="stage"
)
sprite: ap.Sprite = ap.Sprite()
sprite.graphics.begin_fill(color="#00aaff")
rectangle: ap.Rectangle = sprite.graphics.draw_rect(x=50, y=50, width=50, height=50)
animation_x: ap.AnimationX = rectangle.animation_x(x=100)
animation_x.animation_complete(on_animation_complete)
animation_x.start()
```

## ジェネリックの型アノテーション

`AnimationEvent`クラスはジェネリックの型アノテーションを行うことができます。もし型アノテーションをした場合にはアニメーション対象の値となる`target`属性は（`DisplayObject`などの）型アノテーションを行った型のインスタンスになります。

以下のコードでは`AnimationEvent`の値に`Rectangle`のジェネリックの型アノテーションを行っており、mypyやPylanceなどでの型チェックのライブラリやエディタなどでの恩恵を受けることができます。

```py
# runnable
import apysc as ap


def on_animation_complete(e: ap.AnimationEvent[ap.Rectangle], options: dict) -> None:
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
    rectangle.animation_x(x=50).start()


ap.Stage(
    stage_width=200, stage_height=150, background_color="#333", stage_elem_id="stage"
)
sprite: ap.Sprite = ap.Sprite()
sprite.graphics.begin_fill(color="#00aaff")
rectangle: ap.Rectangle = sprite.graphics.draw_rect(x=50, y=50, width=50, height=50)
animation_x: ap.AnimationX = rectangle.animation_x(x=100)
animation_x.animation_complete(on_animation_complete)
animation_x.start()
```

## AnimationEvent クラスのコンストラクタのAPI

<span class="inconspicuous-txt">特記事項: このAPIドキュメントはドキュメントビルド用のスクリプトによって自動で生成・同期されています。そのためもしかしたらこの節の内容は前節までの内容と重複している場合があります。</span>

**[インターフェイスの構造]** `__init__(self, *, this: 'animation_base.AnimationBase[_T]') -> None`<hr>

**[インターフェイス概要]**

アニメーションイベント用のクラスです。<hr>

**[引数]**

- `this`: AnimationBase
  - アニメーションの設定を扱うインスタンス。

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
>>> _ = rectangle.animation_x(x=100).animation_complete(on_animation_complete)
```

## this 属性のAPI

<span class="inconspicuous-txt">特記事項: このAPIドキュメントはドキュメントビルド用のスクリプトによって自動で生成・同期されています。そのためもしかしたらこの節の内容は前節までの内容と重複している場合があります。</span>

**[インターフェイス概要]**

このイベントのリスナーとしてのアニメーション設定のインスタンスを取得します。<hr>

**[返却値]**

- `this`: AnimationBase
  - このイベントのハンドラが設定されているインスタンス。

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
>>> _ = rectangle.animation_x(x=100).animation_complete(on_animation_complete)
```