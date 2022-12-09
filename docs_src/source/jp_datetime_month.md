<span class="inconspicuous-txt">※この翻訳ドキュメントはスクリプトによって出力・同期されています。内容が怪しそうな場合は<a href="https://github.com/simon-ritchie/apysc/issues" target="_blank">GitHubにissue</a>を追加したり[英語の原文](https://simon-ritchie.github.io/apysc/en/datetime_month.html)の確認をお願いします。</span>

# DateTime クラスの month 属性

このページでは`DateTime`クラスの`month`属性のインターフェイスについて説明します。

## インターフェイス概要

`month`属性では月の値の取得もしくは設定を行うことができます。

## 基本的な使い方

`DateTime`クラスのインスタンスがその属性のインターフェイスを持っています。

そのgetterのインターフェイスは`Int`型の月の値を返却します。

```py
# runnable
import apysc as ap

datetime_: ap.DateTime = ap.DateTime(year=2022, month=12, day=1)
assert datetime_.month == 12
```

また、setter側のインターフェイスでは同様に`Int`型の月の値を受け付けます。

1～12の範囲の整数を受け付けることができます。

```py
# runnable
import apysc as ap

datetime_: ap.DateTime = ap.DateTime(year=2022, month=12, day=1)
datetime_.month = ap.Int(1)
assert datetime_.month == 1
```

## month 属性のAPI

<span class="inconspicuous-txt">特記事項: このAPIドキュメントはドキュメントビルド用のスクリプトによって自動で生成・同期されています。そのためもしかしたらこの節の内容は前節までの内容と重複している場合があります。</span>

**[インターフェイス概要]**

現在の月の値を取得します。<hr>

**[返却値]**

- `month`: Int
  - 現在の月の値。

<hr>

**[コードサンプル]**

```py
>>> import apysc as ap
>>> datetime_: ap.DateTime = ap.DateTime(year=2022, month=12, day=1)
>>> datetime_.month
Int(12)

>>> datetime_.month = ap.Int(1)
>>> datetime_.month
Int(1)
```