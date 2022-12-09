<span class="inconspicuous-txt">※この翻訳ドキュメントはスクリプトによって出力・同期されています。内容が怪しそうな場合は<a href="https://github.com/simon-ritchie/apysc/issues" target="_blank">GitHubにissue</a>を追加したり[英語の原文](https://simon-ritchie.github.io/apysc/en/datetime_day.html)の確認をお願いします。</span>

# DateTime クラスの day 属性

このページでは`DateTime`クラスの`day`属性のインターフェイスについて説明します。

## インターフェイス概要

`day`属性では日の値の取得もしくは設定を行うことができます。

## 基本的な使い方

`DateTime`クラスのインスタンスがその属性のインターフェイスを持っています。

そのインターフェイスのgetterでは`Int`型の日の値を返却します。

```py
# runnable
import apysc as ap

datetime_: ap.DateTime = ap.DateTime(year=2022, month=12, day=5)
day: ap.Int = datetime_.day
assert day == 5
```

また、setterのインターフェイスでは同様に`Int`型の値を受け付けます。

1～31の整数を受け付けることができます。

```py
# runnable
import apysc as ap

datetime_: ap.DateTime = ap.DateTime(year=2022, month=12, day=5)
datetime_.day = ap.Int(10)
assert datetime_.day == 10
```

## day 属性のAPI

<span class="inconspicuous-txt">特記事項: このAPIドキュメントはドキュメントビルド用のスクリプトによって自動で生成・同期されています。そのためもしかしたらこの節の内容は前節までの内容と重複している場合があります。</span>

**[インターフェイス概要]**

現在の日の値を取得します。<hr>

**[返却値]**

- `day`: Int
  - 現在の日の値。

<hr>

**[コードサンプル]**

```py
>>> import apysc as ap
>>> datetime_: ap.DateTime = ap.DateTime(year=2022, month=12, day=1)
>>> datetime_.day
Int(1)

>>> datetime_.day = ap.Int(2)
>>> datetime_.day
Int(2)
```