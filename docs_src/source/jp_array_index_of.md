<span class="inconspicuous-txt">※この翻訳ドキュメントはスクリプトによって出力・同期されています。内容が怪しそうな場合は<a href="https://github.com/simon-ritchie/apysc/issues" target="_blank">GitHubにissue</a>を追加したり[英語の原文](https://simon-ritchie.github.io/apysc/en/array_index_of.html)の確認をお願いします。</span>

# Array クラスの index_of インターフェイス

このページでは`Array`クラスの`index_of`メソッドのインターフェイスについて説明します。

## インターフェイス概要

`index_of`メソッドは指定された値の配列内でのインデックスを返却します。

## 基本的な使い方

`index_of`メソッドは`value`引数の指定を必要とし、値が配列内で見つかった場合にはそのインデックスを返却します。

```py
# runnable
import apysc as ap

arr: ap.Array[int] = ap.Array([1, 3, 5])
index: ap.Int = arr.index_of(value=3)
assert index == 1
```

もしも配列内で値が見つからなかった場合インデックスは`-1`となります。

```py
# runnable
import apysc as ap

arr: ap.Array[int] = ap.Array([1, 3, 5])
index: ap.Int = arr.index_of(value=2)
assert index == -1
```

## index_of API

<span class="inconspicuous-txt">特記事項: このAPIドキュメントはドキュメントビルド用のスクリプトによって自動で生成・同期されています。そのためもしかしたらこの節の内容は前節までの内容と重複している場合があります。</span>

**[インターフェイスの構造]** `index_of(self, value:~T) -> apysc._type.int.Int`<hr>

**[インターフェイス概要]** 指定された値を検索し、その値のインデックスを返却します。<hr>

**[引数]**

- `value`: *
  - 検索対象の任意の値。

<hr>

**[返却値]**

- `index`: Int
  - 値が見つかった位置のインデックス。もし配列が対象の値を含んでいない場合は-1となります。

<hr>

**[コードサンプル]**

```py
>>> import apysc as ap
>>> arr: ap.Array = ap.Array([1, 3, 5])
>>> arr.index_of(3)
Int(1)
```