<span class="inconspicuous-txt">※この翻訳ドキュメントはスクリプトによって出力・同期されています。内容が怪しそうな場合は<a href="https://github.com/simon-ritchie/apysc/issues" target="_blank">GitHubにissue</a>を追加したり[英語の原文](branch_instruction_variables_reverting_setting.md)の確認をお願いします。</span>

# 各分岐制御のクラスのスコープ内の変数値の復元設定

このページでは`If`や`Elif`、`Else`などの分岐制御の各クラスのスコープ内の変数の復元設定について説明します。

## 各インターフェイスのwithステートメント内のコードの実行について

これらのインターフェイスでは条件に罹らわず各分岐箇所の（JavaScriptのコード出力のために）コードが実行され、Python上での変数の値が更新されます。

例えば以下のコード例では条件は`False`となっていますがPython上の値は20に更新されます:

```py
# runnable
import apysc as ap

condition: ap.Boolean = ap.Boolean(False)
int_1: ap.Int = ap.Int(10)

with ap.If(condition):
    int_1 += 10
assert int_1 == 20
```

この部分はJavaScriptへ変換されたコード上では条件を満たさないため実行されません。

## スコープ内の変数の復元設定

`If`や`Elif`、`Else`などのクラスは`locals_`と`globals_`の引数の省略可能なオプションを持っています（基本的に設定する場合にはビルトインの`locals()`関数と`globals()`関数の値を設定します）。これらの引数へ値が設定された場合にはスコープ内の各変数が`If`クラスなどのそれぞれのスコープが終了した時点でスコープ前の段階に復元されます。

このインターフェイスのオプションは各分岐の箇所でPythonの変数を更新したく無い場合などに役に立つケースがあります。

```py
# runnable
import apysc as ap

condition: ap.Boolean = ap.Boolean(False)
int_1: ap.Int = ap.Int(10)

with ap.If(condition, locals_=locals(), globals_=globals()):
    int_1 += 10
assert int_1 == 10
```

## 関連資料

- [If クラス](jp_if.md)
- [Elif クラス](jp_elif.md)

- [Else クラス](jp_else.md)