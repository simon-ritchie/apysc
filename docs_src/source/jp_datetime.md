<span class="inconspicuous-txt">※この翻訳ドキュメントはスクリプトによって出力・同期されています。内容が怪しそうな場合は<a href="https://github.com/simon-ritchie/apysc/issues" target="_blank">GitHubにissue</a>を追加したり[英語の原文](https://simon-ritchie.github.io/apysc/en/datetime.html)の確認をお願いします。</span>

# DateTime クラス

このページでは`DateTime`クラスについて説明します。

## クラス概要

`DateTime`クラスは日付と時間かんけぽの各インターフェイスを扱うためのクラスです。

## 基本的な使い方

コンストラクタの引数では`year`、`month`、`day`の各引数の指定を必要とします。

```py
# runnable
import apysc as ap

dt: ap.DateTime = ap.DateTime(year=2022, month=12, day=5)
```

また、省略可能な引数として`hour`、`minute`、`second`の引数を指定することもできます。

```py
# runnable
import apysc as ap

dt: ap.DateTime = ap.DateTime(
    year=2022, month=12, day=5, hour=10, minute=30, second=50, millisecond=500
)
```

各値はgetterとsetterのインターフェイスを持っています。

例えば`month`属性であれば以下のように属性経由で値の取得や更新を行うことができます。

```py
# runnable
import apysc as ap

dt: ap.DateTime = ap.DateTime(year=2022, month=12, day=5)
assert dt.month == 12
dt.month = ap.Int(10)
assert dt.month == 10
```

特記事項: `weekday_py`と`weekday_js`属性はgetterのインターフェイスのみ存在します。

他の属性の詳細に関しては以下のを参照してください:

- [DateTime クラスの year 属性](jp_datetime_year.md)
- [DateTime クラスの month 属性](jp_datetime_month.md)

- [DateTime クラスの day 属性](jp_datetime_day.md)
- [DateTime クラスの hour 属性](jp_datetime_hour.md)

- [DateTime クラスの minute 属性](jp_datetime_minute.md)
- [DateTime クラスの second 属性](jp_datetime_second.md)

- [DateTime クラスの millisecond 属性](jp_datetime_millisecond.md)
- [DateTime クラスの weekday_js と weekday_py 属性](jp_datetime_weekday_js_and_weekday_py.md)

また、`DateTime`クラスは`now`のクラスメソッドのような各メソッドのインターフェイスを持っています。

メソッドの各インターフェイスの詳細は以下を参照してください。

- [DateTime クラスの now インターフェイス](jp_datetime_now.md)

## DateTime クラスのコンストラクタのAPI

<span class="inconspicuous-txt">特記事項: このAPIドキュメントはドキュメントビルド用のスクリプトによって自動で生成・同期されています。そのためもしかしたらこの節の内容は前節までの内容と重複している場合があります。</span>

**[インターフェイスの構造]** `__init__(self, year: Union[int, apysc._type.int.Int], month: Union[int, apysc._type.int.Int], day: Union[int, apysc._type.int.Int], *, hour: Union[int, apysc._type.int.Int] = 0, minute: Union[int, apysc._type.int.Int] = 0, second: Union[int, apysc._type.int.Int] = 0, millisecond: Union[int, apysc._type.int.Int] = 0, variable_name_suffix: str = '', skip_init_substitution_expression_appending: bool = False) -> None`<hr>

**[インターフェイス概要]**

日時に絡んだインターフェイスのためのクラスです。<hr>

**[引数]**

- `year`: Union[int, Int]
  - 4桁の数字の年。

- `month`: Union[int, Int]
  - 2桁の月（1～12）。

- `day`: Union[int, Int]
  - 2桁の日（1～31）。

- `hour`: Optional[Union[int, Int]], optional
  - 2桁の時（0～23）。

- `minute`: Optional[Union[int, Int]], optional
  - 2桁の分（0～59）。

- `second`: Optional[Union[int, Int]], optional
  - 2桁の秒（0～59）。

- `millisecond`: Optional[Union[int, Int]], optional
  - ミリ秒（0～999）

- `variable_name_suffix`: str, default ''
  - JavaScript上の変数のサフィックスの設定です。この設定はJavaScriptのデバッグ時に役立つことがあります。

- `skip_init_substitution_expression_appending`: bool, default False
  - 初期値の代入表現の追加をスキップするかどうかの真偽値。`DateTime`クラスでは内部でのみこのオプションを使用します。

<hr>

**[コードサンプル]**

```py
>>> import apysc as ap
>>> datetime_: ap.DateTime = ap.DateTime(
...     year=2022,
...     month=12,
...     day=5,
...     hour=10,
...     minute=30,
...     second=50,
...     millisecond=500,
... )
>>> datetime_.year
Int(2022)

>>> datetime_.month
Int(12)

>>> datetime_.day
Int(5)

>>> datetime_.hour
Int(10)

>>> datetime_.minute
Int(30)

>>> datetime_.millisecond
Int(500)

>>> datetime_.weekday_py
Int(0)

>>> datetime_.weekday_js
Int(1)
```