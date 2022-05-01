<span class="inconspicuous-txt">※この翻訳ドキュメントはスクリプトによって出力・同期されています。内容が怪しそうな場合は<a href="https://github.com/simon-ritchie/apysc/issues" target="_blank">GitHubにissue</a>を追加したり[英語の原文](https://simon-ritchie.github.io/apysc/en/int_and_number.html)の確認をお願いします。</span>

# Int と Number クラス

このページでは`Int`と`Number`の各クラスについて説明します。

事前に以下のページを確認しておくと読み進める上で役に立つかもしれません:

- [なぜapyscではPythonのビルトインのデータの型を使用していないのか](jp_why_apysc_doesnt_use_python_builtin_data_type.md)

## Int クラス

`Int`クラスはapyscの整数の型となります。このクラスは以下のコード例のようにコンストラクタに数値の値を受け付けます:

```py
# runnable
import apysc as ap

int_1: ap.Int = ap.Int(10)
assert int_1 == 10
```

```py
# runnable
import apysc as ap

int_1: ap.Int = ap.Int(10)
int_2: ap.Int = ap.Int(int_1)
```

```py
# runnable
import apysc as ap

int_1: ap.Int = ap.Int(10)
int_2: ap.Int = ap.Int(int_1)
int_2 += 15
assert int_2 == 25
```

もしコンストラクタの引数に浮動小数点数を指定した場合には`Int`クラスはその値の浮動小数点数を切り捨てます:

```py
# runnable
import apysc as ap

int_1: ap.Int = ap.Int(10.5)
assert int_1 == 10
```

## Number クラス

`Number`クラスはapyscの浮動小数点数の型です。このクラスは`Int`クラスと同様にコンストラクタの引数に数値を受け付けます。

```py
# runnable
import apysc as ap

number_1: ap.Number = ap.Number(10.5)
assert number_1 == 10.5

number_2: ap.Number = ap.Number(number_1)
number_2 += 10.5
assert number_2 == 21
```

## Floatクラスのエイリアスの特記事項

`Float`クラスは`Number`クラスのエイリアス。です。このエイリアスは`Number`クラスと同様に動作します。Python開発者の方はもしかしたら`Number`クラスよりもこちらのエイリアスの方が慣れ親しんでいて自然に感じられるかもしれません。一方でJavaScriptなどの開発者の方は`Float`よりも`Number`の方が自然に思えるかもしれません。

```py
# runnable
import apysc as ap

assert ap.Number == ap.Float
assert ap.Number(10.5) == ap.Float(10.5)
```

## Int と Number クラスの基本的なインターフェイス

`Int`と`Number`の各クラスは同じ各インターフェイスを持っています。詳細に関しては以下をご確認ください:

- [Int と Number クラスの基本的な各計算の制御](jp_int_and_number_arithmetic_operations.md)
- [Int と Number クラスの基本的な各比較の制御](jp_int_and_number_comparison_operations.md)

- [基本的なデータクラスの共通の value インターフェイス](jp_fundamental_data_classes_value_interface.md)

## Int クラスのコンストラクタのAPI

<span class="inconspicuous-txt">特記事項: このAPIドキュメントはドキュメントビルド用のスクリプトによって自動で生成・同期されています。そのためもしかしたらこの節の内容は前節までの内容と重複している場合があります。</span>

**[インターフェイスの構造]** `__init__(self, value:Union[int, float, apysc._type.number_value_interface.NumberValueInterface]) -> None`<hr>

**[インターフェイス概要]** apyscライブラリ上の整数のためのクラスです。<hr>

**[引数]**

- `value`: int or float or Int or Number
  - 整数の初期値。もしも`float`や`Number`の値が指定された場合このクラスは値を整数へと変換します。

<hr>

**[コードサンプル]**

```py
>>> import apysc as ap
>>> int_val: ap.Int = ap.Int(10)
>>> int_val
Int(10)

>>> int_val == 10
Boolean(True)

>>> int_val == ap.Int(10)
Boolean(True)

>>> int_val >= 10
Boolean(True)

>>> int_val += 10
>>> int_val
Int(20)

>>> int_val = ap.Int(10.5)
>>> int_val
Int(10)
```

<hr>

**[関連資料]**

- [Int と Number クラスの共通の各計算制御](https://simon-ritchie.github.io/apysc/jp_int_and_number_arithmetic_operations.html)
- [Int と Number クラスの共通の各比較制御](https://simon-ritchie.github.io/apysc/jp_int_and_number_comparison_operations.html)

## Number クラスのコンストラクタのAPI

<span class="inconspicuous-txt">特記事項: このAPIドキュメントはドキュメントビルド用のスクリプトによって自動で生成・同期されています。そのためもしかしたらこの節の内容は前節までの内容と重複している場合があります。</span>

**[インターフェイスの構造]** `__init__(self, value:Union[int, float, apysc._type.number_value_interface.NumberValueInterface]) -> None`<hr>

**[インターフェイス概要]** apyscライブラリ用の浮動小数点数のクラスです。<hr>

**[引数]**

- `value`: int or float or Int or Number
  - 浮動小数点数の初期値。もしもintやIntなどの型の値が指定された場合このクラスは値を浮動小数点数へ変換します。

<hr>

**[特記事項]**

`Float`クラスはNumberクラスのエイリアスであり、このエイリアスはNumberクラスと同様に動作します。<hr>

**[コードサンプル]**

```py
>>> import apysc as ap
>>> number: ap.Number = ap.Number(10.5)
>>> number
Number(10.5)

>>> number == 10.5
Boolean(True)

>>> number == ap.Number(10.5)
Boolean(True)

>>> number >= 10.5
Boolean(True)

>>> number += 10.3
>>> number
Number(20.8)
```

<hr>

**[関連資料]**

- [Int と Number クラスの共通の各計算制御](https://simon-ritchie.github.io/apysc/jp_int_and_number_arithmetic_operations.html)
- [Int と Number クラスの共通の各比較制御](https://simon-ritchie.github.io/apysc/jp_int_and_number_comparison_operations.html)

## value 属性のAPI

<span class="inconspicuous-txt">特記事項: このAPIドキュメントはドキュメントビルド用のスクリプトによって自動で生成・同期されています。そのためもしかしたらこの節の内容は前節までの内容と重複している場合があります。</span>

**[インターフェイス概要]** 現在の数値を取得します。<hr>

**[返却値]**

- `value`: int or float
  - 現在の数値。

<hr>

**[コードサンプル]**

```py
>>> import apysc as ap
>>> int_val: ap.Int = ap.Int(10)
>>> int_val.value
10

>>> int_val.value = 20
>>> int_val.value
20

>>> int_val.value = ap.Int(30)
>>> int_val.value
30
```

<hr>

**[関連資料]**

- [apyscの基本的なデータクラスの value インターフェイス](https://simon-ritchie.github.io/apysc/jp_fundamental_data_classes_value_interface.html)