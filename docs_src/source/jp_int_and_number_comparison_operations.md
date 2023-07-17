<span class="inconspicuous-txt">※この翻訳ドキュメントはスクリプトによって出力・同期されています。内容が怪しそうな場合は<a href="https://github.com/simon-ritchie/apysc/issues" target="_blank">GitHubにissue</a>を追加したり[英語の原文](https://simon-ritchie.github.io/apysc/en/int_and_number_comparison_operations.html)の確認をお願いします。</span>

# Int と Number クラスの基本的な比較制御

このページでは`Int`や`Number`クラスの`>=`や`<`などの基本的な比較制御について説明します。

## 共通の挙動

各比較制御はPythonのビルトインの`bool`の値ではなく`Boolean`の値を返却します。

```py
# runnable
import apysc as ap

ap.Stage()
int_1: ap.Int = ap.Int(10)
result: ap.Boolean = int_1 == 10
assert isinstance(result, ap.Boolean)
```

`Int`や`Number`の値をPythonビルトインの`int`や`float`などの値と比較することもできます:

```py
# runnable
import apysc as ap

ap.Stage()
int_1: ap.Int = ap.Int(20)
result: ap.Boolean = int_1 == 20
assert result
```

```py
# runnable
import apysc as ap

ap.Stage()
number_1: ap.Number = ap.Number(10.5)
result: ap.Boolean = number_1 == 10.5
assert result
```

同様に`Int`と`Int`間、`Number`と`Number`間、`Int`と`Number`間の比較などもサポートしています:

```py
# runnable
import apysc as ap

ap.Stage()
int_1: ap.Int = ap.Int(10)
int_2: ap.Int = ap.Int(10)
result: ap.Boolean = int_1 == int_2
assert result
```

```py
# runnable
import apysc as ap

ap.Stage()
number_1: ap.Number = ap.Number(10.5)
number_2: ap.Number = ap.Number(10.5)
result: ap.Boolean = number_1 == number_2
assert result
```

```py
# runnable
import apysc as ap

ap.Stage()
int_1: ap.Int = ap.Int(10)
number_1: ap.Number = ap.Number(10)
result: ap.Boolean = int_1 == number_1
assert result
```

## 等値条件の比較のオペレーター

`==`のオペレーターを使って等値条件の比較を行うことができます。

```py
# runnable
import apysc as ap

ap.Stage()
int_1: ap.Int = ap.Int(10)
result: ap.Boolean = int_1 == 10
assert result
```

## 非等値条件の比較のオペレーター

`!=`のオペレーターを使って非等値条件の比較を行うことができます。

```py
# runnable
import apysc as ap

ap.Stage()
int_1: ap.Int = ap.Int(10)
result: ap.Boolean = int_1 != 15
assert result
```

## 未満条件の比較のオペレーター

`<`のオペレーターを使って未満条件の比較を行うことができます。

```py
# runnable
import apysc as ap

ap.Stage()
int_1: ap.Int = ap.Int(10)
result: ap.Boolean = int_1 < 11
assert result
```

## 以下条件の比較のオペレーター

`<=`のオペレーターを使って以下条件の比較を行うことができます。

```py
# runnable
import apysc as ap

ap.Stage()
int_1: ap.Int = ap.Int(10)
result: ap.Boolean = int_1 <= 10
assert result
```

## 超過条件の比較のオペレーター

`>`のオペレーターを使って超過条件の比較を行うことができます。

```py
# runnable
import apysc as ap

ap.Stage()
int_1: ap.Int = ap.Int(10)
result: ap.Boolean = int_1 > 9
assert result
```

## 以上条件の比較のオペレーター

`>=`のオペレーターを使って以上条件の比較を行うことができます。

```py
# runnable
import apysc as ap

ap.Stage()
int_1: ap.Int = ap.Int(10)
result: ap.Boolean = int_1 >= 10
assert result
```