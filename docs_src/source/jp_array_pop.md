<span class="inconspicuous-txt">※この翻訳ドキュメントはスクリプトによって出力・同期されています。内容が怪しそうな場合は<a href="https://github.com/simon-ritchie/apysc/issues" target="_blank">GitHubにissue</a>を追加したり[英語の原文](../en/array_pop.html)の確認をお願いします。</span>

# Array クラスの pop インターフェイス

このページでは`Array`クラスの`pop`メソッドのインターフェイスについて説明します。

## インターフェイス概要

`pop`メソッドは配列内の最後の値を配列から取り除き、そしてその取り除いた値を返却します。

## 基本的な使い方

`pop`メソッドには必要な引数は無く、以下のコード例のように配列の最後の値を返却します:

```py
# runnable
import apysc as ap

arr: ap.Array[int] = ap.Array([1, 2, 3])
last_value: int = arr.pop()
assert last_value == 3
```

## pop API

<span class="inconspicuous-txt">特記事項: このAPIドキュメントはドキュメントビルド用のスクリプトによって自動で生成・同期されています。そのためもしかしたらこの節の内容は前節までの内容と重複している場合があります。</span>

**[インターフェイスの構造]** `pop(self) -> ~T`<hr>

**[インターフェイス概要]** 配列の最後の値を配列から取り除き、その値を返却します。<hr>

**[返却値]**

- `value`: *
  - 取り除かれた値。

<hr>

**[コードサンプル]**

```py
>>> import apysc as ap
>>> arr: ap.Array = ap.Array([1, 2, 3])
>>> popped_val: int = arr.pop()
>>> popped_val
3

>>> arr
Array([1, 2])
```