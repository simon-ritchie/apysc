<span class="inconspicuous-txt">※この翻訳ドキュメントはスクリプトによって出力・同期されています。内容が怪しそうな場合は<a href="https://github.com/simon-ritchie/apysc/issues" target="_blank">GitHubにissue</a>を追加したり[英語の原文](https://simon-ritchie.github.io/apysc/en/string_addition_and_multiplication.html)の確認をお願いします。</span>

# String クラスの加算と乗算の各オペレーション

このページでは`String`クラスの加算と乗算のオペレーションについて説明します。

## 加算

`String`クラスの加算のオペレーション（`+`）は連結された`String`型の値を返却します。

```py
# runnable
import apysc as ap

ap.Stage()
string_1: ap.String = ap.String("Hello")
string_2: ap.String = string_1 + " World!"
assert string_2 == "Hello World!"
assert isinstance(string_2, ap.String)
```

また、`+=`のオペレーターもサポートしています:

```py
# runnable
import apysc as ap

ap.Stage()
string_1: ap.String = ap.String("Hello")
string_1 += " World!"
assert string_1 == "Hello World!"
```

`String`の値とPythonのビルトインの`str`の値によるオペレーションもサポートしています。`String`の値同士のオペレーションも同様です。

```py
# runnable
import apysc as ap

ap.Stage()
string_1: ap.String = ap.String("Hello")
string_2: ap.String = ap.String(" World!")
string_3: ap.String = string_1 + string_2
assert string_3 == "Hello World!"
```

一方で`str`の値と`String`の値の場合（左側を`str`の値にする場合）はサポートしていません。例えば以下のコード例ではエラーとなります:

```py
import apysc as ap

ap.Stage()
string_1: ap.String = ap.String(" World!")
string_2: ap.String = "Hello" + string_1
```

```
TypeError: must be str, not String
```

## 乗算

`String`クラスの乗算のオペレーション（`*`）はPythonビルトインの文字列のように値を繰り返した文字列を返却します。

```py
# runnable
import apysc as ap

ap.Stage()
string_1: ap.String = ap.String("Hello")
string_2: ap.String = string_1 * 3
assert string_2 == "HelloHelloHello"
```

`int`もしくは`Int`型の値を右側の値として受け付けることができます:

```py
# runnable
import apysc as ap

ap.Stage()
string_1: ap.String = ap.String("Hello")
int_1: ap.Int = ap.Int(3)
string_2: ap.String = string_1 * int_1
assert string_2 == "HelloHelloHello"
```