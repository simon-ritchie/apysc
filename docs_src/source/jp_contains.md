<span class="inconspicuous-txt">※この翻訳ドキュメントはスクリプトによって出力・同期されています。内容が怪しそうな場合は<a href="https://github.com/simon-ritchie/apysc/issues" target="_blank">GitHubにissue</a>を追加したり[英語の原文](https://simon-ritchie.github.io/apysc/en/contains.html)の確認をお願いします。</span>

# contains インターフェイス

このページでは`Graphics`や`Sprite`、`Stage`などのコンテナとしての各クラスが持つ`contains`メソッドのインターフェイスについて説明します。

## インターフェイス概要

`contains`インターフェイスは引数に指定された子のインスタンスを対象のコンテナが持つかどうかの真偽値（`Boolean`）を返却します。

## 基本的な使い方

以下のコード例では最初の四角が`Sprite`のコンテナーの子かどうかをチェックしています。もしその子を含んでいればその子を取り除き、ブラウザのコンソール上にログを表示しています（ログの表示にはF12キーを押してください）。

```py
# runnable
from typing_extensions import TypedDict

import apysc as ap


class _RectOptions(TypedDict):
    rectangle: ap.Rectangle


def on_sprite_click(e: ap.MouseEvent[ap.Sprite], options: _RectOptions) -> None:
    """
    The handler that the sprite calls when clicked.

    Parameters
    ----------
    e : MouseEvent
        Event instance.
    options : dict
        Optional arguments dictionary.
    """
    sprite: ap.Sprite = e.this
    rectangle_1: ap.Rectangle = options["rectangle"]
    condition: ap.Boolean = sprite.graphics.contains(child=rectangle_1)
    with ap.If(condition):
        sprite.remove_child(child=rectangle_1)
        ap.trace("Removed the rectangle!")


ap.Stage(
    background_color=ap.Color("#333"),
    stage_width=250,
    stage_height=150,
    stage_elem_id="stage",
)

sprite: ap.Sprite = ap.Sprite()
sprite.graphics.begin_fill(color=ap.Color("#0af"))
rectangle_1: ap.Rectangle = sprite.graphics.draw_rect(x=50, y=50, width=50, height=50)
sprite.graphics.draw_rect(x=150, y=50, width=50, height=50)
options: _RectOptions = {"rectangle": rectangle_1}
sprite.click(on_sprite_click, options=options)

ap.save_overall_html(dest_dir_path="sprite_contains_basic_usage/")
```

<iframe src="static/sprite_contains_basic_usage/index.html" width="250" height="150"></iframe>

## 関連資料

- [add_child （子の追加）と remove_child （子の削除）のインターフェイス](jp_add_child_and_remove_child.md)

## contains API

<span class="inconspicuous-txt">特記事項: このAPIドキュメントはドキュメントビルド用のスクリプトによって自動で生成・同期されています。そのためもしかしたらこの節の内容は前節までの内容と重複している場合があります。</span>

**[インターフェイスの構造]** `contains(self, child: apysc._display.display_object.DisplayObject) -> apysc._type.boolean.Boolean`<hr>

**[インターフェイス概要]**

指定された子のインスタンスを持っているかどうかの真偽値を取得します。<hr>

**[引数]**

- `child`: DisplayObject
  - チェック対象の子のインスタンス。

<hr>

**[返却値]**

- `result`: Boolean
  - このインスタンスが指定された子を持つ場合Trueが設定されます。

<hr>

**[コードサンプル]**

```py
>>> import apysc as ap
>>> stage: ap.Stage = ap.Stage()
>>> sprite: ap.Sprite = ap.Sprite()
>>> sprite.graphics.begin_fill(color=ap.Color("#0af"), alpha=0.5)
>>> rectangle: ap.Rectangle = sprite.graphics.draw_rect(
...     x=50, y=50, width=50, height=50
... )
>>> sprite.graphics.contains(rectangle)
Boolean(True)

>>> rectangle.remove_from_parent()
>>> sprite.graphics.contains(rectangle)
Boolean(False)
```