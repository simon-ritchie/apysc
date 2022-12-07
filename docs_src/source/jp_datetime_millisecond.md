<span class="inconspicuous-txt">※この翻訳ドキュメントはスクリプトによって出力・同期されています。内容が怪しそうな場合は<a href="https://github.com/simon-ritchie/apysc/issues" target="_blank">GitHubにissue</a>を追加したり[英語の原文](https://simon-ritchie.github.io/apysc/en/datetime_millisecond.html)の確認をお願いします。</span>

# DateTime クラスの millisecond 属性

このページでは`DateTime`クラスの`millisecond`属性のインターフェイスについて説明します。

## インターフェイス概要

`millisecond`属性ではミリ秒の値の取得もしくは設定を行うことができます。

## 基本的な使い方

`DateTime`クラスのインスタンスがその属性のインターフェイスを持っています。

そのインタ費フェイスのgetterでは`Int`型のミリ秒の値を返却します。

```py
# runnable
import apysc as ap

datetime_: ap.DateTime = ap.DateTime(year=2022, month=12, day=5, millisecond=500)
millisecond: ap.Int = datetime_.millisecond
assert millisecond == 500
```

また、setter側のインターフェイスでは同様に`Int`型の値を受け付けます。

```py
# runnable
import apysc as ap

datetime_: ap.DateTime = ap.DateTime(year=2022, month=12, day=5, millisecond=500)
datetime_.millisecond = ap.Int(300)
assert datetime_.millisecond == 300
```

## millisecond 属性のAPI

<span class="inconspicuous-txt">特記事項: このAPIドキュメントはドキュメントビルド用のスクリプトによって自動で生成・同期されています。そのためもしかしたらこの節の内容は前節までの内容と重複している場合があります。</span>

**[インターフェイス概要]**

現在のミリ秒の値を取得します。<hr>

**[返却値]**

- `millisecond`: Int
  - 現在のミリ秒の値。

<hr>

**[コードサンプル]**

```py
>>> import apysc as ap
>>> datetime_: ap.DateTime = ap.DateTime(
...     year=2022, month=12, day=1, millisecond=500
... )
>>> datetime_.millisecond
Int(500)

>>> datetime_.millisecond = ap.Int(300)
>>> datetime_.millisecond
Int(300)
```