<span class="inconspicuous-txt">※この翻訳ドキュメントはスクリプトによって出力・同期されています。内容が怪しそうな場合は<a href="https://github.com/simon-ritchie/apysc/issues" target="_blank">GitHubにissue</a>を追加したり[英語の原文](https://simon-ritchie.github.io/apysc/en/math_trunc.html)の確認をお願いします。</span>

# Math クラスの trunc インターフェイス

このページでは`Math`クラスの`trunc`クラスメソッドのインターフェイスについて説明します。

## インターフェイス概要

`trunc`クラスメソッドのインターフェイスは指定された値の小数点以下の値を切り捨てて整数の値を返却します。

## 基本的な使い方

`trunc`インターフェイスは`Int`、`Number`、`String`、もしくは`Boolean`のいずれかの型の値の引数を必要とします。

もしも引数の値が`Number`もしくは`String`型の値であればこのインターフェイスは小数点以下の値を切り捨てて`Int`型に変換した状態で返却します。

もしも引数の値が`Boolean`の型の値であれば、このインターフェイスは0もしくは1の`Int`型の値を返却します。

```py
# runnable
import apysc as ap

result_int: ap.Int = ap.Math.trunc(value=ap.Int(10))
assert result_int == 10

result_int = ap.Math.trunc(value=ap.Number(8.5))
assert result_int == 8

result_int = ap.Math.trunc(value=ap.String("7.6"))
assert result_int == 7

result_int = ap.Math.trunc(value=ap.Boolean(True))
assert result_int == 1
```

## Math.trunc のAPI

<span class="inconspicuous-txt">特記事項: このAPIドキュメントはドキュメントビルド用のスクリプトによって自動で生成・同期されています。そのためもしかしたらこの節の内容は前節までの内容と重複している場合があります。</span>

**[インターフェイスの構造]** `trunc(value: Union[apysc._type.int.Int, apysc._type.number.Number, apysc._type.string.String, apysc._type.boolean.Boolean]) -> apysc._type.int.Int`<hr>

**[インターフェイス概要]**

指定された値から小数点以下の値を切り落とします。<hr>

**[引数]**

- `value`: Union[Int, Number, String, Boolean]
  - 小数点以下を切り捨てる対象の値。もし指定された値が`Number`、`String`、もしくは`Boolean`型の値の場合、変逆値は`Int`型の値となります。

<hr>

**[返却値]**

- `result`: Int
  - 切り捨て処理と`Int`型への変換が反映された値。

<hr>

**[コードサンプル]**

```py
>>> import apysc as ap
>>> result_int: ap.Int = ap.Math.trunc(value=ap.Int(10))
>>> result_int
Int(10)

>>> result_int = ap.Math.trunc(value=ap.Number(8.5))
>>> result_int
Int(8)

>>> result_int = ap.Math.trunc(value=ap.String("7.6"))
>>> result_int
Int(7)

>>> result_int = ap.Math.trunc(value=ap.Boolean(True))
>>> result_int
Int(1)

>>> result_int = ap.Math.trunc(value=ap.Boolean(False))
>>> result_int
Int(0)
```