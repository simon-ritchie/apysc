<span class="inconspicuous-txt">※この翻訳ドキュメントはスクリプトによって出力・同期されています。内容が怪しそうな場合は<a href="https://github.com/simon-ritchie/apysc/issues" target="_blank">GitHubにissue</a>を追加したり[英語の原文](https://simon-ritchie.github.io/apysc/en/display_object_parent.html)の確認をお願いします。</span>

# DisplayObject クラスの parent インターフェイス

このページでは`DisplayObject`クラスの`parent`関係のインターフェイス（`parent`属性と`remove_from_parent`メソッド）について説明します。

## 各インターフェイスの概要

`parent`属性はgetterのみのインターフェイスとなります。この属性値は`Stage`のインスタンスもしくは`Sprite`などのコンテナのインスタンスとなります。

```py
# runnable
import apysc as ap

ap.Stage(
    background_color="#333", stage_width=150, stage_height=200, stage_elem_id="stage"
)

sprite: ap.Sprite = ap.Sprite()
rectangle: ap.Rectangle = sprite.graphics.draw_rect(x=50, y=50, width=50, height=50)

assert isinstance(sprite.parent, ap.Stage)
assert isinstance(sprite.graphics.parent, ap.Sprite)
assert isinstance(rectangle.parent, ap.Graphics)
```

`remove_from_parent`インターフェイスは自身のインスタンスを親のインスタンスから取り除き、画面上に表示されない状態にします。

## remove_from_parent インターフェイスの基本的な使い方

`remove_from_parent`メソッドのインターフェイス（引数を必要としません）は自身のインスタンスを親のインスタンスから取り除きます。取り除かれたインスタンスは他の親（コンテナ）のインスタンスへと追加されるまで画面に表示されません。

```py
# runnable
import apysc as ap

ap.Stage(
    background_color="#333", stage_width=150, stage_height=150, stage_elem_id="stage"
)

sprite: ap.Sprite = ap.Sprite()
rectangle: ap.Rectangle = sprite.graphics.draw_rect(x=50, y=50, width=50, height=50)

# Remove the rectangle from the parent, and nothing displays
# on the stage.
rectangle.remove_from_parent()

ap.save_overall_html(dest_dir_path="display_object_remove_from_parent_basic_usage/")
```

<iframe src="static/display_object_remove_from_parent_basic_usage/index.html" width="150" height="150"></iframe>

## 関連資料

- [add_child （子の追加）と remove_child （子の削除）のインターフェイス](jp_add_child_and_remove_child.md)

## parent API

<span class="inconspicuous-txt">特記事項: このAPIドキュメントはドキュメントビルド用のスクリプトによって自動で生成・同期されています。そのためもしかしたらこの節の内容は前節までの内容と重複している場合があります。</span>

**[インターフェイス概要]** `add_child`や`remove_child`などのインターフェイスを持っている親のインスタンスを取得します。<hr>

**[返却値]**

- `parent`: any parent instance (ChildInterface) or None
  - `add_child`や`remove_child`などのインターフェイスを持っている親のインスタンス。もしこのインスタンスが親を持っていない（画面に追加されていない）場合、このインターフェイスはNoneを返却します。

<hr>

**[コードサンプル]**

```py
>>> import apysc as ap
>>> stage: ap.Stage = ap.Stage()
>>> sprite_1: ap.Sprite = ap.Sprite()
>>> sprite_1.graphics.begin_fill(color="#0af")
>>> rectangle: ap.Rectangle = sprite_1.graphics.draw_rect(
...     x=50, y=50, width=50, height=50
... )
>>> sprite_2: ap.Sprite = ap.Sprite()
>>> sprite_2.add_child(rectangle)
>>> rectangle.parent == sprite_2
True
```

## remove_from_parent API

<span class="inconspicuous-txt">特記事項: このAPIドキュメントはドキュメントビルド用のスクリプトによって自動で生成・同期されています。そのためもしかしたらこの節の内容は前節までの内容と重複している場合があります。</span>

**[インターフェイスの構造]** `remove_from_parent(self) -> None`<hr>

**[インターフェイス概要]** このインスタンスを親のインスタンスから取り除きます。.<hr>

**[エラー発生条件]**

- ValueError: もしも親のインスタンスがNoneの場合（親の無い状態の場合）。