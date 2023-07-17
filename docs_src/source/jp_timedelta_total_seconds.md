<span class="inconspicuous-txt">※この翻訳ドキュメントはスクリプトによって出力・同期されています。内容が怪しそうな場合は<a href="https://github.com/simon-ritchie/apysc/issues" target="_blank">GitHubにissue</a>を追加したり[英語の原文](https://simon-ritchie.github.io/apysc/en/timedelta_total_seconds.html)の確認をお願いします。</span>

# TimeDelta クラスの total_seconds インターフェイス

このページでは`TimeDelta`クラスの`total_seconds`メソッドのインターフェイスについて説明します。

## インターフェイス概要

`total_seconds`メソッドは2つの`DateTime`クラスのインスタンス間の合計秒数を返却します。

## 基本的な使い方

`total_seconds`メソッドはapyscの`Number`型の値を返却します。

もしもいずれかの`DateTime`のインスタンスが`millisecond`属性の値を持っていた場合このインターフェイスは小数点数も含んだ値を設定します。

```py
# runnable
import apysc as ap

ap.Stage()
datetime_1: ap.DateTime = ap.DateTime(2022, 12, 7, millisecond=100)
datetime_2: ap.DateTime = ap.DateTime(2022, 12, 5)
timedelta_: ap.TimeDelta = datetime_1 - datetime_2
total_seconds: ap.Number = timedelta_.total_seconds()
assert total_seconds == 60 * 60 * 24 * 2 + 0.1
```

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

- [TimeDelta クラス](https://simon-ritchie.github.io/apysc/jp/jp_timedelta.html)