<span class="inconspicuous-txt">※この翻訳ドキュメントはスクリプトによって出力・同期されています。内容が怪しそうな場合は<a href="https://github.com/simon-ritchie/apysc/issues" target="_blank">GitHubにissue</a>を追加したり[英語の原文](https://simon-ritchie.github.io/apysc/en/math_max.html)の確認をお願いします。</span>

# Math クラスの max インターフェイス

このページでは`Math`クラスの`max`クラスメソッドのインターフェイスについて説明します。

## インターフェイス概要

`max`クラスメソッドのインターフェイスは指定された数値を格納した配列の中での最大値を返却します。

## 基本的な使い方

`max`インターフェイスでは`Array`型の値の引数（`values`）が必要になります。

このインターフェイスは`Number`型の値を返却します。

特記事項: `Array`内の各値の型に関わらず、このインターフェイスは`Number`型の値を返却します。

```py
# runnable
import apysc as ap

ap.Stage()
arr: ap.Array = ap.Array([9, 10, ap.Int(8), ap.Number(9.5), 11])
max_value: ap.Number = ap.Math.max(values=arr)
assert max_value == 11
```

## Math.max のAPI

<span class="inconspicuous-txt">特記事項: このAPIドキュメントはドキュメントビルド用のスクリプトによって自動で生成・同期されています。そのためもしかしたらこの節の内容は前節までの内容と重複している場合があります。</span>

**[インターフェイスの構造]** `max(values: apysc._type.array.Array) -> apysc._type.number.Number`<hr>

**[インターフェイス概要]**

指定された配列の値の中から最大値の数値を取得します。<hr>

**[引数]**

- `values`: Array[Union[Int, Number, int, float]]
  - 数値を格納した配列。

<hr>

**[返却値]**

- `max_value`: Number
  - 配列の中の数値の最大値。

<hr>

**[コードサンプル]**

```py
>>> import apysc as ap
>>> _ = ap.Stage()
>>> arr: ap.Array = ap.Array([10, 9.5, ap.Int(8), ap.Number(8.5)])
>>> max_value: ap.Number = ap.Math.max(values=arr)
>>> max_value
Number(10.0)
```