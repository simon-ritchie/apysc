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

datetime_1: ap.DateTime = ap.DateTime(2022, 12, 7)
datetime_2: ap.DateTime = ap.DateTime(2022, 12, 5)
timedelta_: ap.TimeDelta = datetime_1 - datetime_2
```

`TimeDelta`クラスのインスタンスは以下のように`days`属性や`total_seconds`メソッドなどの各インターフェイスを持っています:

```
# runnable
import apysc as ap

datetime_1: ap.DateTime = ap.DateTime(2022, 12, 7)
datetime_2: ap.DateTime = ap.DateTime(2022, 12, 5)
timedelta_: ap.TimeDelta = datetime_1 - datetime_2
days: ap.Int = timedelta_.days
assert days == 2
total_seconds: ap.Number = timedelta_.total_seconds()
assert total_seconds == 60 * 60 * 24 * 2
```