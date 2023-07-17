<span class="inconspicuous-txt">※この翻訳ドキュメントはスクリプトによって出力・同期されています。内容が怪しそうな場合は<a href="https://github.com/simon-ritchie/apysc/issues" target="_blank">GitHubにissue</a>を追加したり[英語の原文](https://simon-ritchie.github.io/apysc/en/timedelta.html)の確認をお願いします。</span>

# TimeDelta クラス

このページでは`TimeDelta`クラスについて説明します。

## クラス概要

`TimeDelta`クラスは2つの`DateTime`クラスのインスタンス間の時間差を扱います。

## 基本的な使い方

2つの`DateTime`クラスのインスタンス間の減算はこのクラスのインスタンスを返却します。

```py
# runnable
import apysc as ap

ap.Stage()
datetime_1: ap.DateTime = ap.DateTime(2022, 12, 7)
datetime_2: ap.DateTime = ap.DateTime(2022, 12, 5)
timedelta_: ap.TimeDelta = datetime_1 - datetime_2
```

`TimeDelta`クラスのインスタンスは以下のように`days`属性や`total_seconds`メソッドなどの各インターフェイスを持っています:

```py
# runnable
import apysc as ap

ap.Stage()
datetime_1: ap.DateTime = ap.DateTime(2022, 12, 7)
datetime_2: ap.DateTime = ap.DateTime(2022, 12, 5)
timedelta_: ap.TimeDelta = datetime_1 - datetime_2
days: ap.Int = timedelta_.days
assert days == 2
total_seconds: ap.Number = timedelta_.total_seconds()
assert total_seconds == 60 * 60 * 24 * 2
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
>>> _ = ap.Stage()
>>> datetime_1: ap.DateTime = ap.DateTime(2022, 12, 7)
>>> datetime_2: ap.DateTime = ap.DateTime(2022, 12, 5)
>>> timedelta_: ap.TimeDelta = datetime_1 - datetime_2
>>> timedelta_.days
Int(2)
```

<hr>

**[関連資料]**

- [TimeDelta クラスの days インターフェイス](https://simon-ritchie.github.io/apysc/jp/jp_timedelta_days.html)

## total_seconds メソッドのAPI

<span class="inconspicuous-txt">特記事項: このAPIドキュメントはドキュメントビルド用のスクリプトによって自動で生成・同期されています。そのためもしかしたらこの節の内容は前節までの内容と重複している場合があります。</span>

**[インターフェイスの構造]** `total_seconds(self) -> apysc._type.number.Number`<hr>

**[インターフェイス概要]**

時間の間隔値の合計秒数を取得します。<hr>

**[返却値]**

- `total_seconds`: Number
  - 時間の間隔値の合計秒数。

<hr>

**[コードサンプル]**

```py
>>> import apysc as ap
>>> _ = ap.Stage()
>>> datetime_1: ap.DateTime = ap.DateTime(2022, 12, 7)
>>> datetime_2: ap.DateTime = ap.DateTime(2022, 12, 6)
>>> timedelta_: ap.TimeDelta = datetime_1 - datetime_2
>>> timedelta_.total_seconds()
Number(86400.0)
```

<hr>

**[関連資料]**

- [TimeDelta クラスの total_seconds インターフェイス](https://simon-ritchie.github.io/apysc/jp/jp_timedelta_total_seconds.html)