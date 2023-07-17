<span class="inconspicuous-txt">※この翻訳ドキュメントはスクリプトによって出力・同期されています。内容が怪しそうな場合は<a href="https://github.com/simon-ritchie/apysc/issues" target="_blank">GitHubにissue</a>を追加したり[英語の原文](https://simon-ritchie.github.io/apysc/en/datetime_weekday_js_and_weekday_py.html)の確認をお願いします。</span>

# DateTime クラスの weekday_js と weekday_py 属性

このページでは`DateTime`クラスの`weekday_js`と`weekday_py`属性の各インターフェイスについて説明します。

## 各インターフェイス概要

`weekday_js`属性はJavaScriptの曜日の値（日曜が0となり、土曜が6となります）を取得します。

似たような形で、`weekday_py`属性はPythonの曜日の値（月曜が0となり、日曜が6となります）を取得します。

これらのインターフェイスはgetterのインターフェイスのみ存在します（setterのインターフェイスは存在しません）。

## 基本的な使い方

`DateTime`クラスのインスタンスがこれらの各属性のインターフェイスを持っています。

これらのgetterのインターフェイスは`Int`型の曜日の値を返却します。

```py
# runnable
import apysc as ap

ap.Stage()

# 2022-12-11 is Sunday.
datetime_: ap.DateTime = ap.DateTime(year=2022, month=12, day=11)
weekday_js: ap.Int = datetime_.weekday_js
assert weekday_js == 0

weekday_py: ap.Int = datetime_.weekday_py
assert weekday_py == 6
```

## weekday_js 属性のAPI

<span class="inconspicuous-txt">特記事項: このAPIドキュメントはドキュメントビルド用のスクリプトによって自動で生成・同期されています。そのためもしかしたらこの節の内容は前節までの内容と重複している場合があります。</span>

**[インターフェイス概要]**

現在の曜日の値を取得します。このインターフェイスは以下のようにJavaScriptの曜日の値をベースとした値を設定します。<br> ・0 -> 日曜 <br> ・1 -> 月曜 <br> ・2 -> 火曜 <br> ・3 -> 水曜 <br> ・4 -> 木曜 <br> ・5 -> 金曜 <br> ・6 -> 土曜<hr>

**[返却値]**

- `weekday`: Int
  - 現在の曜日の値。

<hr>

**[コードサンプル]**

```py
>>> import apysc as ap
>>> _ = ap.Stage()
>>> datetime_: ap.DateTime = ap.DateTime(year=2022, month=12, day=4)
>>> datetime_.weekday_js  # Sunday
Int(0)

>>> datetime_ = ap.DateTime(year=2022, month=12, day=10)
>>> datetime_.weekday_js  # Saturday
Int(6)
```

## weekday_py 属性のAPI

<span class="inconspicuous-txt">特記事項: このAPIドキュメントはドキュメントビルド用のスクリプトによって自動で生成・同期されています。そのためもしかしたらこの節の内容は前節までの内容と重複している場合があります。</span>

**[インターフェイス概要]**

現在の曜日の値を取得します。このインターフェイスは以下のようにPythonの曜日の値をベースとした値を設定します。<br> ・0 -> 月曜 <br> ・1 -> 火曜 <br> ・2 -> 水曜 <br> ・3 -> 木曜 <br> ・4 -> 金曜 <br> ・5 -> 土曜 <br> ・6 -> 日曜<hr>

**[返却値]**

- `weekday`: Int
  - 現在の曜日の値。

<hr>

**[コードサンプル]**

```py
>>> import apysc as ap
>>> _ = ap.Stage()
>>> datetime_: ap.DateTime = ap.DateTime(year=2022, month=12, day=5)
>>> datetime_.weekday_py  # Monday
Int(0)

>>> datetime_: ap.DateTime = ap.DateTime(year=2022, month=12, day=4)
>>> datetime_.weekday_py  # Sunday
Int(6)
```