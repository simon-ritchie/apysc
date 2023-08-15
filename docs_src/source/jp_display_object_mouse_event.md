<span class="inconspicuous-txt">※この翻訳ドキュメントはスクリプトによって出力・同期されています。内容が怪しそうな場合は<a href="https://github.com/simon-ritchie/apysc/issues" target="_blank">GitHubにissue</a>を追加したり[英語の原文](https://simon-ritchie.github.io/apysc/en/display_object_mouse_event.html)の確認をお願いします。</span>

# DisplayObject クラスのマウスイベント設定の各インターフェイス

このページでは`DisplayObject`クラスのマウスイベントの登録の各インターフェイスについて説明します。

## 各インターフェイスの概要

各`DisplayObject`のインスタンスはクリックやマウスオーバーなどのマウスイベント登録用の各インターフェイスを持っています。

これらのインターフェイスは`DisplayObject`にマウスイベントを設定でき、例えばクリック時に実行したい関数などを登録することができます。

## 基本的な使い方

`click`や`mouseover`などの各インターフェイスで任意のイベントハンドラ（Callableオブジェクト）を登録することができます。

以下のコード例ではクリックのイベントハンドラを設定しており、四角をクリックすると色が変わるようにしています。

```py
# runnable
import apysc as ap


def on_click(e: ap.MouseEvent[ap.Rectangle], options: dict) -> None:
    """
    The handler that the rectangle calls when clicked.

    Parameters
    ----------
    e : MouseEvent
        Event instance.
    options : dict
        Optional arguments dictionary.
    """
    rectangle: ap.Rectangle = e.this
    rectangle.fill_color = ap.Color("#f0a")


ap.Stage(
    background_color=ap.Color("#333"),
    stage_width=150,
    stage_height=150,
    stage_elem_id="stage",
)

sprite: ap.Sprite = ap.Sprite()
sprite.graphics.begin_fill(color=ap.Color("#0af"))
rectangle: ap.Rectangle = sprite.graphics.draw_rect(x=50, y=50, width=50, height=50)
rectangle.click(on_click)

ap.save_overall_html(dest_dir_path="display_object_mouse_event_basic_usage/")
```

<iframe src="static/display_object_mouse_event_basic_usage/index.html" width="150" height="150"></iframe>

## 関連資料

詳細については以下の各ページをご確認ください:

- [基本的なマウスイベントの各インターフェイス](jp_mouse_event_basic.md)
- [click インターフェイス](jp_click.md)

- [mousedown と mouseup のインターフェイス](jp_mousedown_and_mouseup.md)
- [mouseover と mouseout のインターフェイス](jp_mouseover_and_mouseout.md)

- [mousemove インターフェイス](jp_mousemove.md)