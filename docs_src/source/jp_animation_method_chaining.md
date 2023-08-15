<span class="inconspicuous-txt">※この翻訳ドキュメントはスクリプトによって出力・同期されています。内容が怪しそうな場合は<a href="https://github.com/simon-ritchie/apysc/issues" target="_blank">GitHubにissue</a>を追加したり[英語の原文](https://simon-ritchie.github.io/apysc/en/animation_method_chaining.html)の確認をお願いします。</span>

# AnimationBase クラスのインターフェイスのメソッドチェーン

このページでは各アニメーションのインターフェイスのメソッドチェーンについて説明します。

## AnimationBaseクラスに関係した各インターフェイスは自身のインスタンスを返却します

`animation_x`や`start`、`animation_complete`メソッドなどの`AnimationBase`クラスに絡んだ各インターフェイスは自身のインスタンスを返却します。それを利用して以下のコード例のようにメソッドチェーンを利用することができます（`animation_x`、`animation_complete`、`start`の各インターフェイスで利用しています）。

```py
# runnable
import apysc as ap


def on_animation_complete(e: ap.AnimationEvent[ap.Rectangle], options: dict) -> None:
    """
    The handler that the animation calls when its end.

    Parameters
    ----------
    e : AnimationEvent
        Event instance.
    options : dict
        Optional arguments dictionary.
    """
    ap.trace("Animation is completed!")


ap.Stage(
    stage_width=200,
    stage_height=150,
    background_color=ap.Color("#333"),
    stage_elem_id="stage",
)
sprite: ap.Sprite = ap.Sprite()
sprite.graphics.begin_fill(color=ap.Color("#00aaff"))
rectangle: ap.Rectangle = sprite.graphics.draw_rect(x=50, y=50, width=50, height=50)
rectangle.animation_x(
    x=100,
    duration=1000,
).animation_complete(on_animation_complete).start()

ap.save_overall_html(dest_dir_path="./animation_method_chaining_basic_usage_1/")
```

<iframe src="static/animation_method_chaining_basic_usage_1/index.html" width="200" height=150></iframe>

これらのメソッドチェーンの記述はコードの記述をシンプルにしたい際に役立つことがあります。

もしD3.jsなどでのJavaScriptでの記述に近い形でメソッドチェーンを使いたい場合には以下のコード例のように行末にバックスラッシュを記述することで設定することができます:

```py
# runnable
import apysc as ap


def on_animation_complete(e: ap.AnimationEvent[ap.Rectangle], options: dict) -> None:
    """
    The handler that the animation calls when its end.

    Parameters
    ----------
    e : AnimationEvent
        Event instance.
    options : dict
        Optional arguments dictionary.
    """
    ap.trace("Animation is completed!")


ap.Stage(
    stage_width=200,
    stage_height=150,
    background_color=ap.Color("#333"),
    stage_elem_id="stage",
)
sprite: ap.Sprite = ap.Sprite()
sprite.graphics.begin_fill(color=ap.Color("#00aaff"))
rectangle: ap.Rectangle = sprite.graphics.draw_rect(x=50, y=50, width=50, height=50)
rectangle.animation_x(x=100, duration=1000).animation_complete(
    on_animation_complete
).start()

ap.save_overall_html(dest_dir_path="./animation_method_chaining_basic_usage_2/")
```

<iframe src="static/animation_method_chaining_basic_usage_2/index.html" width="200" height=150></iframe>