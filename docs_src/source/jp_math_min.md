<span class="inconspicuous-txt">※この翻訳ドキュメントはスクリプトによって出力・同期されています。内容が怪しそうな場合は<a href="https://github.com/simon-ritchie/apysc/issues" target="_blank">GitHubにissue</a>を追加したり[英語の原文](https://simon-ritchie.github.io/apysc/en/math_min.html)の確認をお願いします。</span>

# Math クラスの min インターフェイス

このページでは`Math`クラスの`min`のクラスメソッドのインターフェイスについて説明します。

## インターフェイス概要

`min`のクラスメソッドのインターフェイスでは指定された数値の配列の中の最小値を返却します。

## 基本的な使い方

`min`インターフェイスは`Array`クラスの値の引数（`values`）を必要とします。

このインターフェイスは`Number`型の値を返却します。

特記事項: `Array`内の各値の型に関わらず、このインターフェイスは`Number`型の値を返却します。

```py
# runnable
import apysc as ap

arr: ap.Array = ap.Array([9, 10, ap.Int(8), ap.Number(9.5), 11])
min_value: ap.Number = ap.Math.min(values=arr)
assert min_value == 8
```

## Math.min のAPI

<span class="inconspicuous-txt">特記事項: このAPIドキュメントはドキュメントビルド用のスクリプトによって自動で生成・同期されています。そのためもしかしたらこの節の内容は前節までの内容と重複している場合があります。</span>

**[インターフェイスの構造]** `min(values: apysc._type.array.Array) -> apysc._type.number.Number`<hr>

**[インターフェイス概要]**

指定された配列の各値の中から最小値の数値を取得します。<hr>

**[引数]**

- `values`: Array[Union[Int, Number, int, float]]
  - 数値を格納した配列。

<hr>

**[返却値]**

- `min_value`: Number
  - 配列の中で最小の数値。

<hr>

**[コードサンプル]**

```py
>>> import apysc as ap
>>> arr: ap.Array = ap.Array([10, 9.5, ap.Int(8), ap.Number(8.5)])
>>> min_value: ap.Number = ap.Math.min(values=arr)
>>> min_value
Number(8.0)
```