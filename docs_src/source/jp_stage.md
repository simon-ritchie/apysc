<span class="inconspicuous-txt">※この翻訳ドキュメントはスクリプトによって出力・同期されています。内容が怪しそうな場合は<a href="https://github.com/simon-ritchie/apysc/issues" target="_blank">GitHubにissue</a>を追加したり[英語の原文](https://simon-ritchie.github.io/apysc/en/stage.html)の確認をお願いします。</span>

# Stage クラス

このページでは`Stage`クラスについて説明します。

## Stage クラスの概要

`Stage`クラスはapyscにおける描画エリア全体を扱うインスタンスを作成し、各要素を格納します。

apyscのプロジェクトの最初で`Stage`のインスタンスを作成する必要があります（この時点で内部でデータやファイルの古いものの削除などが実行されます）。

## ステージの作成

ステージの作成は以下のコード例のようにシンプルです:

```py
# runnable
import apysc as ap

stage: ap.Stage = ap.Stage()
```

## ステージの背景色設定

`Stage`クラスは`background_color`のオプションの引数を持っており、この引数でステージの背景色を変更することができます。

```py
# runnable
import apysc as ap

stage: ap.Stage = ap.Stage(background_color="#333", stage_elem_id="stage")

ap.save_overall_html(dest_dir_path="stage_background_color/")
```

このコードは以下のように黒背景のステージのHTMLを生成します:

<iframe src="static/stage_background_color/index.html" width="300" height="185"></iframe>

## ステージのサイズ設定

`Stage`クラスはステージの幅を設定する`stage_width`引数とステージの高さを設定する`stage_height`引数を持っています。これらの設定はステージのサイズを変更します。

```py
# runnable
import apysc as ap

stage: ap.Stage = ap.Stage(
    stage_width=500, stage_height=50, background_color="#333", stage_elem_id="stage"
)

ap.save_overall_html(dest_dir_path="stage_size/")
```

上記のコードは以下のように横長のステージを作成します:

<iframe src="static/stage_size/index.html" width="500", height="50"></iframe>

## ステージの要素のID設定

ステージの要素のID（HTMLのID）は`stage_elem_id`引数で設定することができます。もしもこの設定を指定しない場合、apyscはステージ生成時のタイムスタンプや乱数などをベースとした一意なIDを生成します（例 : `stage_12345...`）。

```py
# runnable
import apysc as ap

stage: ap.Stage = ap.Stage(background_color="#333", stage_elem_id="line_chart_1")
```

このオプションはapyscの各プロジェクトで複数回出力などを行う際のIDの識別やバージョン管理などの面で便利です。

## Stage クラスのコンストラクタのAPI

<span class="inconspicuous-txt">特記事項: このAPIドキュメントはドキュメントビルド用のスクリプトによって自動で生成・同期されています。そのためもしかしたらこの節の内容は前節までの内容と重複している場合があります。</span>

**[インターフェイスの構造]** `__init__(self, *, stage_width: int = 300, stage_height: int = 185, background_color: str = '#ffffff', add_to: str = 'body', stage_elem_id: Union[str, NoneType] = None, variable_name_suffix: str = '') -> None`<hr>

**[インターフェイス概要]** ステージ（描画領域全体）のインスタンスを生成します。<hr>

**[引数]**

- `stage_width`: int, default 300
  - ステージの幅。

- `stage_height`: int, default 185
  - ステージの高さ。

- `background_color`: str, default '#ffffff'
  - 16進数の背景色の文字列。

- `add_to`: str, default 'body'
  - ステージの要素を追加先となる要素の指定。一意のタグ（例 : 'body'）やIDのセレクタ（例 : '#any-unique-elem'）を受け付けることができます。

- `stage_elem_id`: str or None, optional
  - ステージのHTML要素に設定されるIDの属性（例 : 'line-graph'）。もしNoneが設定されている場合、乱数などを使った数値を使った値が設定されます。

- `variable_name_suffix`: str, default ''
  - JavaScript上の変数のサフィックスの設定です。この設定はJavaScriptのデバッグ時に役立つことがあります。

<hr>

**[コードサンプル]**

```py
>>> import apysc as ap
>>> stage: ap.Stage = ap.Stage(
...     stage_width=500,
...     stage_height=300,
...     background_color="#333",
...     stage_elem_id="sales_chart",
... )
```

## stage_elem_id 属性のAPI

<span class="inconspicuous-txt">特記事項: このAPIドキュメントはドキュメントビルド用のスクリプトによって自動で生成・同期されています。そのためもしかしたらこの節の内容は前節までの内容と重複している場合があります。</span>

**[インターフェイス概要]** ステージのHTML要素のIDを取得します。<hr>

**[返却値]**

- `stage_elem_id`: str
  - ステージのHTML要素のID（ID用の#の記号などは含まれません。例 : 'line-graph'）。

<hr>

**[コードサンプル]**

```py
>>> import apysc as ap
>>> stage: ap.Stage = ap.Stage(
...     stage_width=500,
...     stage_height=300,
...     background_color="#333",
...     stage_elem_id="sales_chart",
... )
>>> stage.stage_elem_id
'sales_chart'
```

## add_child API

<span class="inconspicuous-txt">特記事項: このAPIドキュメントはドキュメントビルド用のスクリプトによって自動で生成・同期されています。そのためもしかしたらこの節の内容は前節までの内容と重複している場合があります。</span>

**[インターフェイスの構造]** `add_child(self, child: apysc._display.display_object.DisplayObject) -> None`<hr>

**[インターフェイス概要]** 表示オブジェクトの子をこのインスタンスへと追加します。<hr>

**[引数]**

- `child`: DisplayObject
  - 追加する子のインスタンス。

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
```

<hr>

**[関連資料]**

- [add_child （子の追加）と remove_child （子の削除）のインターフェイス](https://simon-ritchie.github.io/apysc/jp/jp_add_child_and_remove_child.html)

## remove_child API

<span class="inconspicuous-txt">特記事項: このAPIドキュメントはドキュメントビルド用のスクリプトによって自動で生成・同期されています。そのためもしかしたらこの節の内容は前節までの内容と重複している場合があります。</span>

**[インターフェイスの構造]** `remove_child(self, child: apysc._display.display_object.DisplayObject) -> None`<hr>

**[インターフェイス概要]** このインスタンスから指定された表示オブジェクトの子を取り除きます。<hr>

**[引数]**

- `child`: DisplayObject
  - 取り除く対象の子のインスタンス。

<hr>

**[コードサンプル]**

```py
>>> import apysc as ap
>>> stage: ap.Stage = ap.Stage()
>>> sprite: ap.Sprite = ap.Sprite()
>>> sprite.graphics.begin_fill(color="#0af", alpha=0.5)
>>> rectangle: ap.Rectangle = sprite.graphics.draw_rect(
...     x=50, y=50, width=50, height=50
... )
>>> sprite.graphics.remove_child(rectangle)
>>> print(rectangle.parent)
None
```

<hr>

**[関連資料]**

- [add_child （子の追加）と remove_child （子の削除）のインターフェイス](https://simon-ritchie.github.io/apysc/jp/jp_add_child_and_remove_child.html)

## contains API

<span class="inconspicuous-txt">特記事項: このAPIドキュメントはドキュメントビルド用のスクリプトによって自動で生成・同期されています。そのためもしかしたらこの節の内容は前節までの内容と重複している場合があります。</span>

**[インターフェイスの構造]** `contains(self, child: apysc._display.display_object.DisplayObject) -> apysc._type.boolean.Boolean`<hr>

**[インターフェイス概要]** 指定された子のインスタンスを持っているかどうかの真偽値を取得します。<hr>

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
>>> sprite.graphics.begin_fill(color="#0af", alpha=0.5)
>>> rectangle: ap.Rectangle = sprite.graphics.draw_rect(
...     x=50, y=50, width=50, height=50
... )
>>> sprite.graphics.contains(rectangle)
Boolean(True)

>>> rectangle.remove_from_parent()
>>> sprite.graphics.contains(rectangle)
Boolean(False)
```

<hr>

**[関連資料]**

- [contains インターフェイス](https://simon-ritchie.github.io/apysc/jp/jp_contains.html)

## num_children property API

<span class="inconspicuous-txt">特記事項: このAPIドキュメントはドキュメントビルド用のスクリプトによって自動で生成・同期されています。そのためもしかしたらこの節の内容は前節までの内容と重複している場合があります。</span>

**[インターフェイス概要]** 現在の子の数を取得します。<hr>

**[返却値]**

- `num_children`: int
  - 現在の子の数。

<hr>

**[コードサンプル]**

```py
>>> import apysc as ap
>>> stage: ap.Stage = ap.Stage()
>>> sprite: ap.Sprite = ap.Sprite()
>>> sprite.graphics.begin_fill(color="#0af", alpha=0.5)
>>> rectangle_1: ap.Rectangle = sprite.graphics.draw_rect(
...     x=50, y=50, width=50, height=50
... )
>>> rectangle_2: ap.Rectangle = sprite.graphics.draw_rect(
...     x=150, y=50, width=50, height=50
... )
>>> sprite.graphics.num_children
Int(2)
```

<hr>

**[関連資料]**

- [num_children （子の件数属性）のインターフェイス](https://simon-ritchie.github.io/apysc/jp/jp_num_children.html)

## get_child_at API

<span class="inconspicuous-txt">特記事項: このAPIドキュメントはドキュメントビルド用のスクリプトによって自動で生成・同期されています。そのためもしかしたらこの節の内容は前節までの内容と重複している場合があります。</span>

**[インターフェイスの構造]** `get_child_at(self, index: Union[int, apysc._type.int.Int]) -> apysc._display.display_object.DisplayObject`<hr>

**[インターフェイス概要]** 指定されたインデックス位置の子を取得します。<hr>

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
>>> sprite.graphics.begin_fill(color="#0af", alpha=0.5)
>>> rectangle_1: ap.Rectangle = sprite.graphics.draw_rect(
...     x=50, y=50, width=50, height=50
... )
>>> rectangle_2: ap.Rectangle = sprite.graphics.draw_rect(
...     x=150, y=50, width=50, height=50
... )
>>> child_at_index_1: ap.DisplayObject = sprite.graphics.get_child_at(1)
>>> child_at_index_1 == rectangle_2
True
```

<hr>

**[関連資料]**

- [get_child_at （特定位置の子の取得処理）のインターフェイス](https://simon-ritchie.github.io/apysc/jp/jp_get_child_at.html)