<span class="inconspicuous-txt">※この翻訳ドキュメントはスクリプトによって出力・同期されています。内容が怪しそうな場合は<a href="https://github.com/simon-ritchie/apysc/issues" target="_blank">GitHubにissue</a>を追加したり[英語の原文](https://simon-ritchie.github.io/apysc/en/mouse_event_abstract.html)の確認をお願いします。</span>

# MouseEvent の各インターフェイスの概要

このページでは MouseEvent クラスの各インターフェイスの概要について説明します。

## これらの各インターフェイスでapyscが出来ること

- クリックやマウスダウン、マウスオーバーなどの`MouseEvent`の各ハンドラをグラフィックスのインスタンスへ設定することができます。
- ハンドラの引数へ任意のパラメーターを渡すことができます。

## クリックイベントの例

マウスイベントを設定するにはまずはハンドラ用の関数（もしくはメソッド）の定義が必要になります（例: `on_click`）。

これらのハンドラは click のインターフェイスで登録することができます。

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
    rectangle: ap.Rectangle = e.this
    with ap.If(rectangle.fill_color == "#00aaff"):
        rectangle.fill_color = ap.String("#f0a")
        ap.Return()

    with ap.If(rectangle.fill_color == "#ff00aa"):
        rectangle.fill_color = ap.String("#0af")
        ap.Return()


ap.Stage(
    background_color="#333", stage_width=150, stage_height=150, stage_elem_id="stage"
)
sprite: ap.Sprite = ap.Sprite()
sprite.graphics.begin_fill(color="#0af")
rectangle: ap.Rectangle = sprite.graphics.draw_rect(x=50, y=50, width=50, height=50)
rectangle.click(on_click)

ap.save_overall_html(dest_dir_path="mouse_event_abstract_click/")
```

<iframe src="static/mouse_event_abstract_click/index.html" width="150" height="150"></iframe>

## 関連資料

他にもマウスダウンやマウスオーバー、マウスムーブなど様々なイベント設定用のインターフェイスが存在します。詳細は以下をご確認ください:

- [基本的なマウスイベントの各インターフェイス](jp_mouse_event_basic.md)
- [click インターフェイス](jp_click.md)

- [dblclick インターフェイス](jp_dblclick.md)
- [mousedown と mouseup のインターフェイス](jp_mousedown_and_mouseup.md)

- [mouseover と mouseout のインターフェイス](jp_mouseover_and_mouseout.md)
- [mousemove インターフェイス](jp_mousemove.md)