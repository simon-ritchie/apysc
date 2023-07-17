<span class="inconspicuous-txt">※この翻訳ドキュメントはスクリプトによって出力・同期されています。内容が怪しそうな場合は<a href="https://github.com/simon-ritchie/apysc/issues" target="_blank">GitHubにissue</a>を追加したり[英語の原文](https://simon-ritchie.github.io/apysc/en/int_and_number_arithmetic_operations.html)の確認をお願いします。</span>

# Int と Number クラスの基本的な計算制御

このページでは`Int`や`Number`の各クラスの加算や乗算などの基本的な計算制御について説明します。

## 共通の挙動

`Int`や`Number`の各値は以下のコード例のように`int`や`float`などのPythonビルトインの値と計算することができます:

```py
# runnable
import apysc as ap

ap.Stage()
int_1: ap.Int = ap.Int(10)
int_1 = int_1 + 20
assert int_1 == 30
```

また、同じ型同士（例 : `Int`と`Int`同士など）での計算も同様にサポートしています:

```py
# runnable
import apysc as ap

ap.Stage()
int_1: ap.Int = ap.Int(10)
int_2: ap.Int = ap.Int(20)
int_1 = int_1 + int_2
assert int_1 == 30
```

計算で左側の値がPythonビルトインの値の場合はサポートしていません。例えば以下のコードではエラーとなります:

```py
import apysc as ap

ap.Stage()
int_1: ap.Int = ap.Int(10)

# This will raise the error!
int_1 = 20 + int_1
```

```
TypeError: unsupported operand type(s) for +: 'int' and 'Int'
```

## 加算

`+`のオペレーターを使って各値の加算処理を行うことができます。

```py
# runnable
import apysc as ap

ap.Stage()
int_1: ap.Int = ap.Int(10)
int_1 = int_1 + 20
assert int_1 == 30
```

```py
# runnable
import apysc as ap

ap.Stage()
int_1: ap.Int = ap.Int(10)
int_2: ap.Int = ap.Int(20)
int_1 = int_1 + int_2
assert int_1 == 30
```

```py
# runnable
import apysc as ap

ap.Stage()
int_1: ap.Int = ap.Int(10) + ap.Int(20)
assert int_1 == 30
```

`+=`のオペレーターも同じように使用することができます。

```py
# runnable
import apysc as ap

ap.Stage()
int_1: ap.Int = ap.Int(10)
int_1 += 20
assert int_1 == 30
```

```py
# runnable
import apysc as ap

ap.Stage()
int_1: ap.Int = ap.Int(10)
int_2: ap.Int = ap.Int(20)
int_1 += int_2
assert int_1 == 30
```

## 減算

`-`のオペレーターを使って各値の減算を行うことができます。

```py
# runnable
import apysc as ap

ap.Stage()
int_1: ap.Int = ap.Int(30)
int_1 = int_1 - 10
assert int_1 == 20
```

```py
# runnable
import apysc as ap

ap.Stage()
int_1: ap.Int = ap.Int(30)
int_2: ap.Int = ap.Int(20)
int_1 = int_1 - int_2
assert int_1 == 10
```

`-=`のオペレーターも同様に使用することができます。

```py
# runnable
import apysc as ap

ap.Stage()
int_1: ap.Int = ap.Int(50)
int_1 -= 30
assert int_1 == 20
```

## 乗算

`*`のオペレーターを使って各値を乗算することができます。

```py
# runnable
import apysc as ap

ap.Stage()
int_1: ap.Int = ap.Int(10)
int_1 = int_1 * 3
assert int_1 == 30
```

```py
# runnable
import apysc as ap

ap.Stage()
int_1: ap.Int = ap.Int(10)
int_2: ap.Int = ap.Int(5)
int_1 = int_1 * int_2
assert int_1 == 50
```

`*=`のオペレーターを使うこともできます。

```py
# runnable
import apysc as ap

ap.Stage()
int_1: ap.Int = ap.Int(10)
int_1 *= 3
assert int_1 == 30
```

## 除算

`/`のオペレーターを使って各値の除算を行うことができます。返却値は`Int`の整数ではなく`Number`の浮動小数点数になります。

```py
# runnable
import apysc as ap

ap.Stage()
int_1: ap.Int = ap.Int(10)
number_1: ap.Number = int_1 / 4
assert number_1 == 2.5
```

```py
# runnable
import apysc as ap

ap.Stage()
int_1: ap.Int = ap.Int(10)
int_2: ap.Int = ap.Int(4)
number_1: ap.Number = int_1 / int_2
assert number_1 == 2.5
```

`/=`のオペレーターを使うこともできます。

```py
# runnable
import apysc as ap

ap.Stage()
number_1: ap.Number = ap.Number(10)
number_1 /= 4
assert number_1 == 2.5
```

## 切り捨て除算

`//`のオペレーターで除算と浮動小数点数の切り捨てを行うことができます。返却値は`Number`型の浮動小数点数ではなく`Int`の整数となります。

```py
# runnable
import apysc as ap

ap.Stage()
int_1: ap.Int = ap.Int(10)
int_1 = int_1 // 4
assert int_1 == 2
```

## 剰余

`%`のオペレーターを使って剰余の計算を行うことができます。

```py
# runnable
import apysc as ap

ap.Stage()
int_1: ap.Int = ap.Int(10)
int_2: int = int_1 % 3
assert int_2 == 1
```

```py
# runnable
import apysc as ap

ap.Stage()
number_1: ap.Number = ap.Number(10.5)
number_2: ap.Number = number_1 % 3
assert number_2 == 1.5
```