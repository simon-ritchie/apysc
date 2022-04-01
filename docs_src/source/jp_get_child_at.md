<span class="inconspicuous-txt">※この翻訳ドキュメントはスクリプトによって出力・同期されています。内容が怪しそうな場合は<a href="https://github.com/simon-ritchie/apysc/issues" target="_blank">GitHubにissue</a>を追加したり[英語の原文](get_child_at.md)の確認をお願いします。</span>

# get_child_at インターフェイス

このページでは`Graphisc`や`Sprite`、`Stage`などのコンテナーのクラスの`get_child_at`メソッドのインターフェイスについて説明します。

## インターフェイス概要

`get_child_at`インターフェイスは指定されたインデックスの位置の子のインスタンス（`DisplkayObject`クラスのインスタンス）を返却します。

## 基本的な使い方

以下のコード例ではSpriteのコンテナーへと四角を追加しています。`Sprite`のクラスは`Graphics`のインスタンスを子としてコンストラクタで追加するため、最初の子は`Graphics`のインスタンスとなり、2番目の子は`add_child`メソッドで追加された`Rectangle`の四角のインスタンスとなります。

```py
# runnable
import apysc as ap

ap.Stage(
    background_color='#333',
    stage_width=450,
    stage_height=150,
    stage_elem_id='stage')

sprite: ap.Sprite = ap.Sprite()
sprite.graphics.begin_fill(color='#0af')
rectangle_1: ap.Rectangle = sprite.graphics.draw_rect(
    x=50, y=50, width=50, height=50)
sprite.add_child(rectangle_1)

first_child: ap.DisplayObject = sprite.get_child_at(index=0)
assert isinstance(first_child, ap.Graphics)

second_child: ap.DisplayObject = sprite.get_child_at(index=1)
assert isinstance(second_child, ap.Rectangle)
```

## get_child_at API

<span class="inconspicuous-txt">特記事項: このAPIドキュメントはドキュメントビルド用のスクリプトによって自動で生成・同期されています。そのためもしかしたらこの節の内容は前節までの内容と重複している場合があります。</span>

**[インターフェイスの構造]** `get_child_at(self, index:Union[int, apysc._type.int.Int]) -> apysc._display.display_object.DisplayObject`<hr>

**[インターフェイス概要]** 指定されたインデックスの子のインスタンスを取得します。<hr>

**[引数]**

- `index`: int or Int
  - 対象の子のインデックス（0からスタートします）。

<hr>

**[返却値]**

- `child`: DisplayObject
  - 対象の子のインスタンス。

<hr>

**[コードサンプル]**

```py
>>> import apysc as ap
>>> stage: ap.Stage = ap.Stage()
>>> sprite: ap.Sprite = ap.Sprite()
>>> sprite.graphics.begin_fill(color='#0af', alpha=0.5)
>>> rectangle_1: ap.Rectangle = sprite.graphics.draw_rect(
...     x=50, y=50, width=50, height=50)
>>> rectangle_2: ap.Rectangle = sprite.graphics.draw_rect(
...     x=150, y=50, width=50, height=50)
>>> child_at_index_1: ap.DisplayObject = (
...     sprite.graphics.get_child_at(1))
>>> child_at_index_1 == rectangle_2
True
```