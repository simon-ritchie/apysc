<span class="inconspicuous-txt">※この翻訳ドキュメントはスクリプトによって出力・同期されています。内容が怪しそうな場合は<a href="https://github.com/simon-ritchie/apysc/issues" target="_blank">GitHubにissue</a>を追加したり[英語の原文](https://simon-ritchie.github.io/apysc/en/graphics_clear.html)の確認をお願いします。</span>

# Graphics クラスの clear インターフェイス

このページでは`Graphics`クラスの`clear`メソッドのインターフェイスについて説明します。

## インターフェイス概要

`clear`メソッドは全ての描画済みグラフィックスを取り除き、塗りと線の設定をリセットします。

## 基本的な使い方

`clear`メソッドは引数の指定を必要としません。

以下の例では四角をクリックした際にハンドラ内で`clear`メソッドが呼ばれます:

```py
# runnable
import apysc as ap


def on_click(e: ap.MouseEvent[ap.Sprite], options: dict) -> None:
    """
    The click event handler.

    Parameters
    ----------
    e : ap.MouseEvent[ap.Sprite]
        Event instance.
    options : dict
        Optional arguments dictionary.
    """
    sprite: ap.Sprite = e.this
    ap.assert_equal(sprite.graphics.fill_color, '#00aaff')
    sprite.graphics.clear()
    ap.assert_equal(sprite.graphics.fill_color, '')


ap.Stage(
    stage_width=250, stage_height=150, background_color='#333',
    stage_elem_id='stage')
sprite: ap.Sprite = ap.Sprite()
sprite.graphics.begin_fill(color='#0af')
sprite.graphics.draw_rect(x=50, y=50, width=50, height=50)
sprite.graphics.draw_rect(x=150, y=50, width=50, height=50)
sprite.click(on_click)

ap.save_overall_html(
    dest_dir_path='graphics_clear_basic_usage/')
```

<iframe src="static/graphics_clear_basic_usage/index.html" width="250" height="150"></iframe>