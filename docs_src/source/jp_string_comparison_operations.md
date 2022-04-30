<span class="inconspicuous-txt">※この翻訳ドキュメントはスクリプトによって出力・同期されています。内容が怪しそうな場合は<a href="https://github.com/simon-ritchie/apysc/issues" target="_blank">GitHubにissue</a>を追加したり[英語の原文](../en/string_comparison_operations.html)の確認をお願いします。</span>

# String クラスの比較の各オペレーション

このページでは`String`クラスの`=`や`>=`などの比較のオペレーションについて説明します。

## 比較のオペレーションの返却値の型

`String`クラスの比較の各オペレーションはPyhtonビルトインの`bool`の値ではなく`Boolean`型の値となります。

```py
# runnable
import apysc as ap

string_1: ap.String = ap.String('Hello')
result: ap.Boolean = string_1 == 'Hello'
assert result
assert isinstance(result, ap.Boolean)
```

## 受け付けられる右側の値の型

以下のコード例のように`str`もしくは`String`型の比較対象の値（比較の右側の値）を受け付けることができます:

```py
# runnable
import apysc as ap

string_1: ap.String = ap.String('Hello')
result: ap.Boolean = string_1 == 'Hello'
assert result
```

```py
# runnable
import apysc as ap

string_1: ap.String = ap.String('Hello')
string_2: ap.String = ap.String('Hello')
result: ap.Boolean = string_1 == string_2
assert result
```

## 等値条件の比較

`==`のオペレーターを使って等値条件の比較を行うことができます。

```py
# runnable
import apysc as ap

string_1: ap.String = ap.String('Hello')
result: ap.Boolean = string_1 == 'Hello'
assert result
```

## 非等値条件の比較

`!=`のオペレーターを使って非等値条件の比較を行うことができます。

```py
# runnable
import apysc as ap

string_1: ap.String = ap.String('Hello')
result: ap.Boolean = string_1 != 'World'
assert result
```

## 未満もしくは超過条件の比較

未満、以下、超過、以上の比較の処理をPythonビルトインの`str`の値のように`<`、`<=`、`>`、`>=`のオペレーターを使っておこなをことができます。ごの処理は日付や日時などの文字列比較などで役に立つことがあります。

```py
# runnable
import apysc as ap

string_1: ap.String = ap.String('1970-01-05')
result: ap.Boolean = string_1 < '1970-01-06'
assert result
```

```py
# runnable
import apysc as ap

string_1: ap.String = ap.String('1970-01-05')
result: ap.Boolean = string_1 <= '1970-01-05'
assert result
```

```py
# runnable
import apysc as ap

string_1: ap.String = ap.String('1970-01-05')
result: ap.Boolean = string_1 > '1970-01-04'
assert result
```

```py
# runnable
import apysc as ap

string_1: ap.String = ap.String('1970-01-05')
result: ap.Boolean = string_1 >= '1970-01-05'
assert result
```