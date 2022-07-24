<span class="inconspicuous-txt">※この翻訳ドキュメントはスクリプトによって出力・同期されています。内容が怪しそうな場合は<a href="https://github.com/simon-ritchie/apysc/issues" target="_blank">GitHubにissue</a>を追加したり[英語の原文](https://simon-ritchie.github.io/apysc/en/else.html)の確認をお願いします。</span>

# Else クラス

このページでは`Else`クラスについて説明します。

このページを読み進める前に以下のページを確認しておくと役に立つかもしれません（apyscでは`Else`クラスを以下のデータ型のケースと同じ理由で使用しています）:

- [なぜapyscではPythonのビルトインのデータの型を使用していないのか](jp_why_apysc_doesnt_use_python_builtin_data_type.md)

## Else クラスの概要

`Else`クラスはapyscの条件分岐の指定用のクラスです。このクラスはPythonビルトインの`else`キーワードと同じように動作します。

## 基本的な使い方

`Else`クラスは`with`ステートメントとセットで使用する必要があります。`Else`クラスのステートメントは`If`もしくは`Elif`クラスのステートメントの直後でのみ使用することができます。

```py
# runnable
import apysc as ap

condition: ap.Boolean = ap.Boolean(False)
int_1: ap.Int = ap.Int(10)

with ap.If(condition):
    int_1 += 10
with ap.Else():
    int_1 += 20
```

## 特記事項

もしも`If`もしくは`Elif`クラスと`Else`クラスのステートメントの間にコードを挿入するとエラーとなります:

```py
import apysc as ap

condition: ap.Boolean = ap.Boolean(False)
int_1: ap.Int = ap.Int(10)

with ap.If(condition):
    int_1 += 10
# If there is a code implementation between the `If` and `Else`, then
# exceptions will be raised.
int_2: ap.Int = ap.Int(20)
with ap.Else():
    int_1 += 20
```

```
ValueError: Else interface can only use right after If or Elif interfaces.
```

## 関連資料

- [If クラス](jp_if.md)
- [Elif クラス](jp_elif.md)

- [分岐条件の各クラスのスコープ内変数の復元設定](jp_branch_instruction_variables_reverting_setting.md)

## Else クラスのコンストラクタのAPI

<span class="inconspicuous-txt">特記事項: このAPIドキュメントはドキュメントビルド用のスクリプトによって自動で生成・同期されています。そのためもしかしたらこの節の内容は前節までの内容と重複している場合があります。</span>

**[インターフェイスの構造]** `__init__(self, *, locals_: Union[Dict[str, Any], NoneType] = None, globals_: Union[Dict[str, Any], NoneType] = None) -> None`<hr>

**[インターフェイス概要]** elseの条件分岐のコード表現を追加するためのクラスです。<hr>

**[引数]**

- `locals_`: dict or None, default None
  - 現在のスコープの各ローカル変数の値。利用する場合にはlocals()関数をこの引数へ指定してください。もし設定された場合には`Else`のスコープの最後にVariableNameInterfaceクラスを継承したクラスの各変数（例 : Spriteなど）の設定は復元されます。この設定は`Else`クラスのスコープ内で変数を更新したくない場合などに便利なことがあります。

- `globals_`: dict or None, default None
  - 現在のスコープの各グローバル変数。設定する場合にはglobal()関数の値をこの引数に指定してください。この設定はlocals_引数と同じように動作します。

<hr>

**[特記事項]**

 ・このクラスは`If`もしくは`Elif`クラスのステートメントの直後にのみ使用することができます。<hr>

**[コードサンプル]**

```py
>>> import apysc as ap
>>> int_val: ap.Int = ap.Int(10)
>>> with ap.If(int_val >= 11):
...     ap.trace("Value is greater than equal 11.")
...
>>> with ap.Else():
...     ap.trace("Value is less than 11.")
...
```

<hr>

**[関連資料]**

- [分岐条件の各クラスのスコープ内変数の復元設定](https://simon-ritchie.github.io/apysc/en/jp_branch_instruction_variables_reverting_setting.html)