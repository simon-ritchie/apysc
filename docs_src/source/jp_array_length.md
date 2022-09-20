<span class="inconspicuous-txt">※この翻訳ドキュメントはスクリプトによって出力・同期されています。内容が怪しそうな場合は<a href="https://github.com/simon-ritchie/apysc/issues" target="_blank">GitHubにissue</a>を追加したり[英語の原文](https://simon-ritchie.github.io/apysc/en/array_length.html)の確認をお願いします。</span>

# Array クラスの length インターフェイス

このページでは`Array`クラスの`length`属性のインターフェイスについて説明します。

## インターフェイス概要

`length`属性のインターフェイスは配列の値の長さ（件数）を返却します。

## 基本的な使い方

`length`属性はgetterのインターフェイスのみを持ちます。返却値はapyscの`Int`クラスの整数値となります。

```py
# runnable
import apysc as ap

arr: ap.Array[int] = ap.Array([1, 2, 3, 4])
length: ap.Int = arr.length
assert length == 4
```

## len()関数における特記事項

`Array`クラスはPythonビルトインの`len()`関数をサポートしておらず、もし使用した場合にはエラーとなります。代わりに`length`属性を使用してください。

```py
import apysc as ap

arr: ap.Array[int] = ap.Array([1, 2, 3, 4])
len(arr)
```

```
Exception: Array instance can't apply len function. Please use length property instead.
```

## length属性のAPI

<span class="inconspicuous-txt">特記事項: このAPIドキュメントはドキュメントビルド用のスクリプトによって自動で生成・同期されています。そのためもしかしたらこの節の内容は前節までの内容と重複している場合があります。</span>

**[インターフェイス概要]**

この配列の長さ（値の数）を取得します。<hr>

**[返却値]**

- `length`: Int
  - この配列の長さ（値の件数）。

<hr>

**[コードサンプル]**

```py
>>> import apysc as ap
>>> arr: ap.Array = ap.Array([1, 2, 3])
>>> arr.length
Int(3)
```