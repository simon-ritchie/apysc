<span class="inconspicuous-txt">※この翻訳ドキュメントはスクリプトによって出力・同期されています。内容が怪しそうな場合は<a href="https://github.com/simon-ritchie/apysc/issues" target="_blank">GitHubにissue</a>を追加したり[英語の原文](https://simon-ritchie.github.io/apysc/en/datetime_hour.html)の確認をお願いします。</span>

# DateTime クラスの hour 属性

このページでは`DateTime`クラスの`hour`属性のインターフェイスについて説明します。

## インターフェイス概要

`hour`属性では時間の値の取得もしくは設定を行うことができます。

## 基本的な使い方

`DateTime`クラスのインスタンスがその属性のインターフェイスを持っています。

そのインターフェイスのgetterでは`Int`型の時間の値を返却します。

```py
# runnable
import apysc as ap

datetime_: ap.DateTime = ap.DateTime(year=2022, month=12, day=5, hour=10)
hour: ap.Int = datetime_.hour
assert hour == 10
```

また、setterのインターフェイスでは同様に`Int`型の値を受け付けます。

```py
# runnable
import apysc as ap

datetime_: ap.DateTime = ap.DateTime(year=2022, month=12, day=5, hour=10)
datetime_.hour = ap.Int(15)
assert datetime_.hour == 15
```

## hour 属性のAPI

<span class="inconspicuous-txt">特記事項: このAPIドキュメントはドキュメントビルド用のスクリプトによって自動で生成・同期されています。そのためもしかしたらこの節の内容は前節までの内容と重複している場合があります。</span>

**[インターフェイス概要]**

現在の時間の値を取得します。<hr>

**[返却値]**

- `hour`: Int
  - 現在の時間の値。

<hr>

**[コードサンプル]**

```py
>>> import apysc as ap
>>> datetime_: ap.DateTime = ap.DateTime(year=2022, month=12, day=1, hour=5)
>>> datetime_.hour
Int(5)

>>> datetime_.hour = ap.Int(10)
>>> datetime_.hour
Int(10)
```