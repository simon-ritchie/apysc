<span class="inconspicuous-txt">※この翻訳ドキュメントはスクリプトによって出力・同期されています。内容が怪しそうな場合は<a href="https://github.com/simon-ritchie/apysc/issues" target="_blank">GitHubにissue</a>を追加したり[英語の原文](https://simon-ritchie.github.io/apysc/en/remove_children.html)の確認をお願いします。</span>

# remove_children インターフェイス

このページではコンテナの各クラスの`remove_children`メソッドのインターフェイスについて説明します。

## インターフェイス概要

`remove_children`メソッドはコンテナのインスタンスから全ての子のインスタンスを取り除きます。

## 基本的な使い方

`remove_children`メソッドは引数の指定を必要としません。

以下の例では、いずれかの四角をクリックした場合`remove_children`メソッドが呼ばれ全ての子が取り除かれます:

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
    sprite.remove_children()


ap.Stage(
    stage_width=250,
    stage_height=150,
    background_color=ap.Color("#333"),
    stage_elem_id="stage",
)
sprite: ap.Sprite = ap.Sprite()
sprite.graphics.begin_fill(color=ap.Color("#0af"))
sprite.graphics.draw_rect(x=50, y=50, width=50, height=50)
sprite.graphics.draw_rect(x=150, y=50, width=50, height=50)
sprite.click(on_click)

ap.save_overall_html(dest_dir_path="remove_children_basic_usage/")
```

<iframe src="static/remove_children_basic_usage/index.html" width="250" height="150"></iframe>

## remove_children のAPI

<span class="inconspicuous-txt">特記事項: このAPIドキュメントはドキュメントビルド用のスクリプトによって自動で生成・同期されています。そのためもしかしたらこの節の内容は前節までの内容と重複している場合があります。</span>

**[インターフェイスの構造]** `remove_children(self) -> None`<hr>

**[インターフェイス概要]**

このインスタンスから全ての子要素を取り除きます。<hr>

**[コードサンプル]**

```py
>>> import apysc as ap
>>> sprite: ap.Sprite = ap.Sprite()
>>> rectangle_1: ap.Rectangle = ap.Rectangle(
...     x=50, y=50, width=50, height=50, fill_color=ap.Color("#0af")
... )
>>> rectangle_2: ap.Rectangle = ap.Rectangle(
...     x=150, y=50, width=50, height=50, fill_color=ap.Color("#0af")
... )
>>> sprite.add_child(child=rectangle_1)
>>> sprite.add_child(child=rectangle_2)
>>> sprite.remove_children()
>>> sprite.num_children
Int(0)
```