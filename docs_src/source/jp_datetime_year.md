<span class="inconspicuous-txt">※この翻訳ドキュメントはスクリプトによって出力・同期されています。内容が怪しそうな場合は<a href="https://github.com/simon-ritchie/apysc/issues" target="_blank">GitHubにissue</a>を追加したり[英語の原文](https://simon-ritchie.github.io/apysc/en/datetime_year.html)の確認をお願いします。</span>

# DateTime クラスの year 属性

このページでは`DateTime`クラスの`year`属性について説明します。

## インターフェイス概要

`year`属性は年の値の取得もしくは設定を行うことができます。

## 基本的な使い方

`DateTime`クラスのインスタンスがその属性のインターフェイスを持っています。

そのgetterインターフェイスは`Int`型の年の値を返却します。

```py
# runnable
import apysc as ap

ap.Stage()
datetime_: ap.DateTime = ap.DateTime(year=2022, month=12, day=1)
year: ap.Int = datetime_.year
assert year == 2022
```

また、`year`属性のsetterインターフェイスも同様に`Int`型の年の値を受け付けます。

4桁の数字を受け付けることができます（例 : 2023）。

```py
# runnable
import apysc as ap

ap.Stage()
datetime_: ap.DateTime = ap.DateTime(year=2022, month=12, day=1)
datetime_.year = ap.Int(2023)
assert datetime_.year == 2023
```

## year 属性のAPI

<span class="inconspicuous-txt">特記事項: このAPIドキュメントはドキュメントビルド用のスクリプトによって自動で生成・同期されています。そのためもしかしたらこの節の内容は前節までの内容と重複している場合があります。</span>

**[インターフェイス概要]**

現在の年の値を取得します。<hr>

**[返却値]**

- `year`: Int
  - 現在の年の値。

<hr>

**[コードサンプル]**

```py
>>> import apysc as ap
>>> _ = ap.Stage()
>>> datetime_: ap.DateTime = ap.DateTime(year=2022, month=12, day=1)
>>> datetime_.year
Int(2022)

>>> datetime_.year = ap.Int(2023)
>>> datetime_.year
Int(2023)
```