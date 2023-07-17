<span class="inconspicuous-txt">※この翻訳ドキュメントはスクリプトによって出力・同期されています。内容が怪しそうな場合は<a href="https://github.com/simon-ritchie/apysc/issues" target="_blank">GitHubにissue</a>を追加したり[英語の原文](https://simon-ritchie.github.io/apysc/en/datetime_set_month_end.html)の確認をお願いします。</span>

# DateTime クラスの set_month_end インターフェイス

このページでは`DateTime`クラスの`set_month_end`メソッドのインターフェイスについて説明します。

## インターフェイス概要

`set_month_end`メソッドのインターフェイスでは現在の月の月末の日付を設定します。

例えば、もし現在の日付が2022-12-05であればこのメソッドによって2022-12-31が設定されます。

## 基本的な使い方

このメソッドでは引数を必要としません。

```py
# runnable
import apysc as ap

ap.Stage()
datetime_: ap.DateTime = ap.DateTime(year=2022, month=12, day=5)
datetime_.set_month_end()
assert datetime_.day == 31
```