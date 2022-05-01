<span class="inconspicuous-txt">※この翻訳ドキュメントはスクリプトによって出力・同期されています。内容が怪しそうな場合は<a href="https://github.com/simon-ritchie/apysc/issues" target="_blank">GitHubにissue</a>を追加したり[英語の原文](https://simon-ritchie.github.io/apysc/en/array_slice.html)の確認をお願いします。</span>

# Array クラスの slice インターフェイス

このページでは`Array`クラスの`slice`メソッドのインターフェイスについて説明します。

## インターフェイス概要

`slice`メソッドのインターフェイスは指定されたインデックスの範囲の配列の値を抽出し新しい配列を返却します。

## 基本的な使い方

`slice`メソッドは`start`と`end`の各引数（Pythonビルトインの`int`もしくはapyscの`Int`の整数）を必要とし、返却値として新しい配列を返します。

例として`start`引数に1を指定し`end`引数に3を指定した場合、このメソッドはPythonビルトインの`[1:3]`という指定によるスライスと同じように動作します。

元々の配列の値は変更されません。

```py
# runnable
import apysc as ap

arr: ap.Array[int] = ap.Array([1, 2, 3, 4])
sliced_arr: ap.Array[int] = arr.slice(start=1, end=3)
assert sliced_arr == [2, 3]
assert arr == [1, 2, 3, 4]
```

## slice API

<span class="inconspicuous-txt">特記事項: このAPIドキュメントはドキュメントビルド用のスクリプトによって自動で生成・同期されています。そのためもしかしたらこの節の内容は前節までの内容と重複している場合があります。</span>

**[インターフェイスの構造]** `slice(self, *, start:Union[int, apysc._type.int.Int, NoneType]=None, end:Union[int, apysc._type.int.Int, NoneType]=None) -> 'Array'`<hr>

**[インターフェイス概要]** 与えられた開始と終了のインデックスに応じて配列をスライスします。<hr>

**[引数]**

- `start`: Int or int or None, default None
  - スライス範囲の開始インデックス。

- `end`: Int or int or None, default None
  - スライス範囲の終了インデックス（結果の配列のこのインデックスの値を含みません）。

<hr>

**[返却値]**

- `sliced_arr`: Array
  - スライスされた配列。

<hr>

**[コードサンプル]**

```py
>>> import apysc as ap
>>> arr: ap.Array = ap.Array([1, 2, 3, 4])
>>> arr.slice(start=1, end=3)
Array([2, 3])

>>> arr.slice(start=1)
Array([2, 3, 4])

>>> arr.slice(end=2)
Array([1, 2])
```