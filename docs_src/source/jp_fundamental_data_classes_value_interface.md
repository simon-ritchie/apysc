<span class="inconspicuous-txt">※この翻訳ドキュメントはスクリプトによって出力・同期されています。内容が怪しそうな場合は<a href="https://github.com/simon-ritchie/apysc/issues" target="_blank">GitHubにissue</a>を追加したり[英語の原文](fundamental_data_classes_value_interface.md)の確認をお願いします。</span>

# apysc の基本的なデータ型の value インターフェイス。

このページではapyscの`Int`や`Number`、`String`などの基本的なデータクラスの`value`インターフェイスについて説明します。

## インターフェイス概要

`value`のgetterのインターフェイスは各データクラスの値を返却します。setterのインターフェイスではそれらの値の更新を行います。

返却値は基本的に`int`や`float`、`str`などのPythonビルトインの値になります。

## getterのインターフェイスの基本的な使い方

`value`のgetterインターフェイスではPythonのビルトインの値を返却します。

```py
# runnable
import apysc as ap

int_1: ap.Int = ap.Int(10)
value = int_1.value
assert isinstance(value, int)
```

```py
# runnable
import apysc as ap

number_1: ap.Number = ap.Number(10.5)
value = number_1.value
assert isinstance(value, float)
```

## setterのインターフェイスの基本的な使い方

apyscの基本的なデータクラスにおける`value`のsetterのインターフェイスではそれらの値を更新することができます。Pythonのビルトインの値やapyscの同じ型の値を指定することができます:

```py
# runnable
import apysc as ap

int_1: ap.Int = ap.Int(10)
int_1.value = 20
assert int_1 == 20
```

```py
# runnable
import apysc as ap

int_1: ap.Int = ap.Int(10)
int_1.value = ap.Int(20)
assert int_1 == 20
```