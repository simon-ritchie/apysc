<span class="inconspicuous-txt">※この翻訳ドキュメントはスクリプトによって出力・同期されています。内容が怪しそうな場合は<a href="https://github.com/simon-ritchie/apysc/issues" target="_blank">GitHubにissue</a>を追加したり[英語の原文](https://simon-ritchie.github.io/apysc/en/array_insert_and_insert_at.html)の確認をお願いします。</span>

# Array クラスの insert と insert_at のインターフェイス

このページでは`Array`クラスの`insert`と`insert_at`メソッドの各インターフェイスについて説明します。

## 各インターフェイスの概要

`insert`と`insert_at`メソッドの各インターフェイスは任意の値を配列の指定されたインデックスへと追加します。それぞれの員スターフェイスは同じ挙動をします（`insert`メソッドは`insert_at`メソッドのエイリアスとなっています）。

## 基本的な使い方

`insert`と`insert_at`メソッドは`index`と`value`の同じ引数を持っています。`index`引数はPythonビルトインの`int`とapyscの`Int`クラスの値を受け付けます。

```py
# runnable
import apysc as ap

arr: ap.Array[int] = ap.Array([1, 4])
arr.insert(index=1, value=2)
assert arr == [1, 2, 4]

index: ap.Int = ap.Int(2)
arr.insert_at(index=index, value=3)
assert arr == [1, 2, 3, 4]
```

## insert API

<span class="inconspicuous-txt">特記事項: このAPIドキュメントはドキュメントビルド用のスクリプトによって自動で生成・同期されています。そのためもしかしたらこの節の内容は前節までの内容と重複している場合があります。</span>

**[インターフェイスの構造]** `insert(self, index: Union[int, apysc._type.int.Int], value: ~T) -> None`<hr>

**[インターフェイス概要]**

この配列の指定されたインデックスの位置へ値を挿入します。このインターフェイスは`insert_at`メソッドと同じ挙動をします。<hr>

**[引数]**

- `index`: Int or int
  - 値を追加するインデックス。

- `value`: *
  - 追加対象の任意の値。

<hr>

**[コードサンプル]**

```py
>>> import apysc as ap
>>> arr: ap.Array = ap.Array([1, 3])
>>> arr.insert(index=1, value=2)
>>> arr
Array([1, 2, 3])
```

## insert_at API

<span class="inconspicuous-txt">特記事項: このAPIドキュメントはドキュメントビルド用のスクリプトによって自動で生成・同期されています。そのためもしかしたらこの節の内容は前節までの内容と重複している場合があります。</span>

**[インターフェイスの構造]** `insert_at(self, *, index: Union[int, apysc._type.int.Int], value: ~T) -> None`<hr>

**[インターフェイス概要]**

この配列の指定されたインデックスの位置へ値を挿入します。このインターフェイスは`insert`メソッドと同じ挙動をします。<hr>

**[引数]**

- `index`: Int or int
  - 値を追加するインデックス。

- `value`: *
  - 追加対象の任意の値。

<hr>

**[コードサンプル]**

```py
>>> import apysc as ap
>>> arr: ap.Array = ap.Array([1, 3])
>>> arr.insert_at(index=1, value=2)
>>> arr
Array([1, 2, 3])
```