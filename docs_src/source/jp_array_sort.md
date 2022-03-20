<span class="inconspicuous-txt">※この翻訳ドキュメントはスクリプトによって出力・同期されています。内容が怪しそうな場合は<a href="https://github.com/simon-ritchie/apysc/issues" target="_blank">GitHubにissue</a>を追加したり[英語の原文](array_sort.md)の確認をお願いします。</span>

# Array クラスの sort インターフェイス

このページでは`Array`クラスの`sort`メソッドのインターフェイスについて説明します。

## インターフェイス概要

`sort`メソッドのインターフェイスは配列の値をソートします（デフォルトでは昇順となります）。

## 基本的な使い方

`sort`は昇順でソートする場合引数を必要とせず、配列の値は直接更新されます（返却値は設定されません）。

```py
# runnable
import apysc as ap

arr: ap.Array[int] = ap.Array([5, 1, 3])
arr.sort()
assert arr == [1, 3, 5]
```

もし`ascending`引数に`False`を指定した場合、結果は降順となります。

```py
# runnable
import apysc as ap

arr: ap.Array[int] = ap.Array([5, 1, 3])
arr.sort(ascending=False)
assert arr == [5, 3, 1]
```

## 関連資料

- [Array クラスの reverse インターフェイス](jp_array_reverse.md)

## sort API

<span class="inconspicuous-txt">特記事項: このAPIドキュメントはドキュメントビルド用のスクリプトによって自動で生成・同期されています。そのためもしかしたらこの節の内容は前節までの内容と重複している場合があります。</span>

**[インターフェイスの構造]** `sort(self, *, ascending:bool=True) -> None`<hr>

**[インターフェイス概要]** この配列の値を直接更新する形でソートを行います。<hr>

**[引数]**

- `ascending`: bool, default True
  - 昇順でソートを行うかどうかの指定です。もしFalseが指定された場合、このインターフェイスは降順で値をソートします。

<hr>

**[コードサンプル]**

```py
>>> import apysc as ap
>>> arr: ap.Array = ap.Array([3, 5, 1, 4, 2])
>>> arr.sort()
>>> arr
Array([1, 2, 3, 4, 5])

>>> arr.sort(ascending=False)
>>> arr
Array([5, 4, 3, 2, 1])
```