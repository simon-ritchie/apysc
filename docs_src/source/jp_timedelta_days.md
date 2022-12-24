<span class="inconspicuous-txt">※この翻訳ドキュメントはスクリプトによって出力・同期されています。内容が怪しそうな場合は<a href="https://github.com/simon-ritchie/apysc/issues" target="_blank">GitHubにissue</a>を追加したり[英語の原文](https://simon-ritchie.github.io/apysc/en/timedelta_days.html)の確認をお願いします。</span>

# TimeDelta クラスの days 属性

このページでは`TimeDelta`クラスの`days`属性のインターフェイスについて説明します。

## インターフェイス概要

`days`属性は2つの`DateTime`クラスのインスタンス間の日数値を返却します。

## 基本的な使い方

`days`属性の値の型はapyscの`Int`型となり、且つその値の小数点数は切り捨てられます。

```py
# runnable
import apysc as ap

datetime_1: ap.DateTime = ap.DateTime(2022, 12, 7)
datetime_2: ap.DateTime = ap.DateTime(2022, 12, 5)
timedelta_: ap.TimeDelta = datetime_1 - datetime_2
days: ap.Int = timedelta_.days
assert days == 2

datetime_3: ap.DateTime = ap.DateTime(2022, 12, 7)
datetime_4: ap.DateTime = ap.DateTime(2022, 12, 5, hour=10)
timedelta_ = datetime_3 - datetime_4
days = timedelta_.days
assert days == 1
```

## days 属性のAPI

<span class="inconspicuous-txt">特記事項: このAPIドキュメントはドキュメントビルド用のスクリプトによって自動で生成・同期されています。そのためもしかしたらこの節の内容は前節までの内容と重複している場合があります。</span>

**[インターフェイス概要]**

時間の間隔値の日数を取得します。<hr>

**[返却値]**

- `days`: Int
  - 日数値。小数点数の分は無視されます。

<hr>

**[コードサンプル]**

```py
>>> import apysc as ap
>>> datetime_1: ap.DateTime = ap.DateTime(2022, 12, 7)
>>> datetime_2: ap.DateTime = ap.DateTime(2022, 12, 5)
>>> timedelta_: ap.TimeDelta = datetime_1 - datetime_2
>>> timedelta_.days
Int(2)
```