<span class="inconspicuous-txt">※この翻訳ドキュメントはスクリプトによって出力・同期されています。内容が怪しそうな場合は<a href="https://github.com/simon-ritchie/apysc/issues" target="_blank">GitHubにissue</a>を追加したり[英語の原文](https://simon-ritchie.github.io/apysc/en/event_prevent_default_and_stop_propagation.html)の確認をお願いします。</span>

# Event クラスの prevent_default と stop_propagation のインターフェイス

このページでは`Event`クラスの`prevent_default`と`stop_propagation`メソッドの各インターフェイスについて説明します。

## 各インターフェイスの概要

`prevent_default`メソッドのインターフェイスはJavaScriptの`preventDefault`メソッドに該当するコード表現を加えます。このインターフェイスはイベントにおけるブラウザのデフォルトの挙動を無効化します。

`stop_propagation`メソッドのインターフェイスはイベントの伝搬を停止します。例えば、このインスタンス上で実行（発火）されたイベントは親のインスタンスへは伝搬しなくなります（親のイベントは無視されるようになります）。

## prevent_default インターフェイスの基本的な使い方

`Event`のサブクラスのインスタンスは`prevent_default`メソッドを持っています（注: このインターフェイスを持っていないサブクラスも存在します）。`prevent_default`メソッドは特に引数を必要としません。

```py
# runnable
import apysc as ap


def on_click(e: ap.MouseEvent[ap.Rectangle], options: dict) -> None:
    """
    The handler that the rectangle calls when clicked.

    Parameters
    ----------
    e : ap.MouseEvent
        Event instance.
    options : dict
        Optional arguments dictionary.
    """
    e.prevent_default()


ap.Stage(
    stage_width=150, stage_height=150, background_color="#333", stage_elem_id="stage"
)
sprite: ap.Sprite = ap.Sprite()
sprite.graphics.begin_fill(color="#0af")
rectangle: ap.Rectangle = sprite.graphics.draw_rect(x=50, y=50, width=50, height=50)
rectangle.click(on_click)

ap.save_overall_html(dest_dir_path="event_prevent_default_basic_usage/")
```

## stop_propagation インターフェイスの基本的な使い方

`Event`のサブクラスのインスタンスは`stop_propagation`メソッドを持っています（注: このメソッドを持っていないサブクラスも存在します）。`stop_propagation`メソッドは`prevent_default`メソッドと同様に引数を必要としません。

以下のコード例ではクリックイベントをSpriteの親のインスタンスと四角の子のインスタンスにそれぞれ設定しています。四角の子のインスタンスのクリックのハンドラでは`stop_propagation`メソッドを読んでいるため、親のSpriteのハンドラは呼ばれません（イベントが伝搬しません）。

```py
# runnable
import apysc as ap


def on_rectangle_click(e: ap.MouseEvent[ap.Rectangle], options: dict) -> None:
    """
    The handler that the rectangle calls when clicked.

    Parameters
    ----------
    e : ap.MouseEvent
        Event instance.
    options : dict
        Optional arguments dictionary.
    """
    e.stop_propagation()
    ap.trace("The rectangle is clicked!")


def on_sprite_click(e: ap.MouseEvent[ap.Sprite], options: dict) -> None:
    """
    The handler that the sprite calls when clicked.

    Parameters
    ----------
    e : ap.MouseEvent
        Event instance.
    options : dict
        Optional arguments dictionary.
    """
    ap.trace("The sprite is clicked!")


ap.Stage(
    stage_width=150, stage_height=150, background_color="#333", stage_elem_id="stage"
)
sprite: ap.Sprite = ap.Sprite()
sprite.click(on_sprite_click)
sprite.graphics.begin_fill(color="#0af")
rectangle: ap.Rectangle = sprite.graphics.draw_rect(x=50, y=50, width=50, height=50)
rectangle.click(on_rectangle_click)

ap.save_overall_html(dest_dir_path="event_stop_propagation_basic_usage/")
```

もし以下の四角をクリックした場合、ブラウザのコンソールには`The rectangle is clicked!`というメッセージのみが表示され、Sprite関係のメッセージは表示されません。

<iframe src="static/event_stop_propagation_basic_usage/index.html" width="150" height="150"></iframe>

## prevent_default API

<span class="inconspicuous-txt">特記事項: このAPIドキュメントはドキュメントビルド用のスクリプトによって自動で生成・同期されています。そのためもしかしたらこの節の内容は前節までの内容と重複している場合があります。</span>

**[インターフェイスの構造]** `prevent_default(self) -> None`<hr>

**[インターフェイス概要]** イベントのデフォルトの挙動を無効化します。<hr>

**[コードサンプル]**

```py
>>> import apysc as ap
>>> def on_click(e: ap.MouseEvent[ap.Rectangle], options: dict) -> None:
...     e.prevent_default()
...     rectangle: ap.Rectangle = e.this
...     rectangle.fill_color = ap.String("#f0a")
...     rectangle.unbind_mouseup_all()
>>> stage: ap.Stage = ap.Stage()
>>> sprite: ap.Sprite = ap.Sprite()
>>> sprite.graphics.begin_fill(color="#0af")
>>> rectangle: ap.Rectangle = sprite.graphics.draw_rect(
...     x=50, y=50, width=50, height=50
... )
>>> _ = rectangle.click(on_click)
```

## stop_propagation API

<span class="inconspicuous-txt">特記事項: このAPIドキュメントはドキュメントビルド用のスクリプトによって自動で生成・同期されています。そのためもしかしたらこの節の内容は前節までの内容と重複している場合があります。</span>

**[インターフェイスの構造]** `stop_propagation(self) -> None`<hr>

**[インターフェイス概要]** イベントの伝搬を停止するように設定します。<hr>

**[コードサンプル]**

```py
>>> import apysc as ap
>>> def on_click(e: ap.MouseEvent, options: dict) -> None:
...     e.stop_propagation()
...     ap.trace("Clicked!")
>>> stage: ap.Stage = ap.Stage()
>>> sprite: ap.Sprite = ap.Sprite()
>>> sprite.graphics.begin_fill(color="#0af")
>>> rectangle: ap.Rectangle = sprite.graphics.draw_rect(
...     x=50, y=50, width=50, height=50
... )
>>> _ = sprite.click(on_click)
>>> _ = rectangle.click(on_click)
```