<span class="inconspicuous-txt">※この翻訳ドキュメントはスクリプトによって出力・同期されています。内容が怪しそうな場合は<a href="https://github.com/simon-ritchie/apysc/issues" target="_blank">GitHubにissue</a>を追加したり[英語の原文](../en/array_remove_and_remove_at.html)の確認をお願いします。</span>

# Array クラスの remove と remove_at のインターフェイス

このページでは`Array`クラスの`remove`と`remove_at`メソッドの各インターフェイスについて説明します。

## 各インターフェイスの概要

`remove`メソッドは配列から指定された値を取り除き、`remove_at`メソッドは配列から指定されたインデックスの値を取り除きます。

## 基本的な使い方

`remove`メソッドは以下のコード例のように取り除く対象の値を第一引数に必要とします。

```py
# runnable
import apysc as ap

arr: ap.Array[int] = ap.Array([1, 2, 3])
arr.remove(value=2)
assert arr == [1, 3]
```

`remove_at`メソッドは以下のコード例のように配列のインデックスの整数（Pythonビルトインの`int`もしくはapyscの`Int`）を第一引数に必要とします。

```py
# runnable
import apysc as ap

arr: ap.Array[int] = ap.Array([1, 2, 3])
arr.remove_at(index=1)
assert arr == [1, 3]
```

## remove API

<span class="inconspicuous-txt">特記事項: このAPIドキュメントはドキュメントビルド用のスクリプトによって自動で生成・同期されています。そのためもしかしたらこの節の内容は前節までの内容と重複している場合があります。</span>

**[インターフェイスの構造]** `remove(self, value:~T) -> None`<hr>

**[インターフェイス概要]** 指定された値をこの配列から取り除きます。<hr>

**[引数]**

- `value`: Any
  - 取り除く対象の値。

<hr>

**[コードサンプル]**

```py
>>> import apysc as ap
>>> arr: ap.Array = ap.Array([1, 3, 5])
>>> arr.remove(3)
>>> arr
Array([1, 5])
```

## remove_at API

<span class="inconspicuous-txt">特記事項: このAPIドキュメントはドキュメントビルド用のスクリプトによって自動で生成・同期されています。そのためもしかしたらこの節の内容は前節までの内容と重複している場合があります。</span>

**[インターフェイスの構造]** `remove_at(self, index:Union[int, apysc._type.int.Int]) -> None`<hr>

**[インターフェイス概要]** 指定されたインデックスの位置の値を配列から取り除きます。<hr>

**[引数]**

- `index`: Int or int
  - 取り除く値のインデックス。

<hr>

**[コードサンプル]**

```py
>>> import apysc as ap
>>> arr: ap.Array = ap.Array([1, 2, 3])
>>> arr.remove_at(1)
>>> arr
Array([1, 3])
```