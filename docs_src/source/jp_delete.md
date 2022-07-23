<span class="inconspicuous-txt">※この翻訳ドキュメントはスクリプトによって出力・同期されています。内容が怪しそうな場合は<a href="https://github.com/simon-ritchie/apysc/issues" target="_blank">GitHubにissue</a>を追加したり[英語の原文](https://simon-ritchie.github.io/apysc/en/delete.html)の確認をお願いします。</span>

# delete インターフェイス

このページでは`delete`関数のインターフェイスについて説明します。

## インターフェイス概要

`delete`関数は任意のインスタンスの削除を行います。削除された対象は`undefined`のオブジェクトになります。

もし対象のインスタンスが`DisplayObject`のインスタンスであれば、このインターフェイスはそのインスタンスをステージから取り除きます。

例えば`Sprite`や`Rectangle`などのインスタンスであればこのインターフェイスはそれらのインスタンスを取り除きます。

## 基本的な使い方

`delete`関数の引数へは任意のapyscのインスタンスを指定することができます。

```py
# runnable
import apysc as ap

int_val: ap.Int = ap.Int(10)
ap.delete(int_val)
```

もし指定されたインスタンスが`DisplayObject`のインスタンスであれば、`delete`関数はそのインスタンスをステージから取り除きます。

また、削除されたインスタンスはundefinedのオブジェクトになります。

```py
# runnable
import apysc as ap


def on_click(e: ap.MouseEvent[ap.Sprite], options: dict) -> None:
    """
    The click event handler that a sprite calls.

    Parameters
    ----------
    e : ap.MouseEvent[ap.Sprite]
        Event instance.
    options : dict
        Optional arguments dictionary.
    """
    sprite: ap.Sprite = e.this
    ap.delete(sprite)
    ap.assert_undefined(sprite)


ap.Stage(
    stage_width=150, stage_height=150, background_color="#333", stage_elem_id="stage"
)
sprite: ap.Sprite = ap.Sprite()
sprite.graphics.begin_fill(color="#0af")
sprite.graphics.draw_rect(x=50, y=50, width=50, height=50)
sprite.click(on_click)

ap.save_overall_html(dest_dir_path="delete_basic_usage/")
```

もし以下の四角をクリックすると、`delete`関数は対象のインスタンスをステージから取り除きます。

<iframe src="static/delete_basic_usage/index.html" width="150" height="150"></iframe>