<span class="inconspicuous-txt">※この翻訳ドキュメントはスクリプトによって出力・同期されています。内容が怪しそうな場合は<a href="https://github.com/simon-ritchie/apysc/issues" target="_blank">GitHubにissue</a>を追加したり[英語の原文](https://simon-ritchie.github.io/apysc/en/elif.html)の確認をお願いします。</span>

# Elif クラス

このページでは`Elif`クラスについて説明します。

このページを読み進める前に以下のページをご確認いただくと役に立つかもしれません（`Elif`クラスも他のデータのクラスと同じ理由で使われています）:

- [なぜapyscではPythonのビルトインのデータの型を使用していないのか](jp_why_apysc_doesnt_use_python_builtin_data_type.md)

## Elif クラスの概要

`Elif`クラスはapyscの分岐条件用のクラスです。このクラスはPythonのビルトインの`elif`のキーワードと同じように動作します。

## 基本的な使い方

`Elif`クラスは`with`ステートメントと共に使う必要があります。また、`Elif`クラスは`If`や`Elif`クラスのステートメントの直後にのみ使用することができます。

```py
# runnable
import apysc as ap

int_1: ap.Int = ap.Int(10)

condition_1: ap.Boolean = ap.Boolean(False)
condition_2: ap.Boolean = ap.Boolean(True)
with ap.If(condition_1):
    int_1 += 20
with ap.Elif(condition_2):
    int_1 += 30
```

## 特記事項

もし`If`（もしくは`Elif`）クラスと`Elif`クラスのステートメント間にコードを挟んだ場合エラーとなります:

```py
import apysc as ap

int_1: ap.Int = ap.Int(10)

condition_1: ap.Boolean = ap.Boolean(False)
condition_2: ap.Boolean = ap.Boolean(True)
with ap.If(condition_1):
    int_1 += 20
# Code inserting between the `If` and `Elif` will raise an exception.
int_2: ap.Int = ap.Int(30)
with ap.Elif(condition_2):
    int_1 += 30
```

```
ValueError: Elif interface can only use right after If or Elif interfaces.
```

また、`Elif`のコンストラクタにて直接`Boolean`の値の条件値を作成したり比較表現を行うことはできません。例えば以下のコードでもエラーとなります:

```py
import apysc as ap

int_1: ap.Int = ap.Int(10)

condition_1: ap.Boolean = ap.Boolean(False)
condition_2: ap.Boolean = ap.Boolean(True)
with ap.If(condition_1):
    int_1 += 20
with ap.Elif(int_1 == 10):
    int_1 += 30
```

```
ValueError: Elif interface can only use right after If or Elif interfaces.

Maybe you are using Int or String, or anything-else comparison expression at Elif constructor (e.g., `with Elif(any_value == 10, ...):`).
Currently, that specifying expression directly is not supported, so please define conditions separately as follows:
condition: Boolean = any_value == 10
...
with Elif(condition, ...):
```

## 関連資料

- [If クラス](jp_if.md)
- [Else クラス](jp_else.md)

- [分岐条件の各クラスのスコープ内変数の復元設定](jp_branch_instruction_variables_reverting_setting.md)

## Elif クラスのコンストラクタのAPI

<span class="inconspicuous-txt">特記事項: このAPIドキュメントはドキュメントビルド用のスクリプトによって自動で生成・同期されています。そのためもしかしたらこの節の内容は前節までの内容と重複している場合があります。</span>

**[インターフェイスの構造]** `__init__(self, condition: Union[apysc._type.boolean.Boolean, NoneType], *, locals_: Union[Dict[str, Any], NoneType] = None, globals_: Union[Dict[str, Any], NoneType] = None) -> None`<hr>

**[インターフェイス概要]** A class to append the `else if` branch instruction expression.<hr>

**[引数]**

- `condition`: Boolean or None
  - 判定に使われるBooleanの真偽値。

- `locals_`: dict or None, default None
  - 現在のスコープの各ローカル変数。locals()関数の値を引数に指定してください。もしも指定された場合には`Elif`のスコープの終了字にこのインターフェイスはVariableNameInterfaceクラスを継承した各変数（例 : `Sprite`クラスなど）の値をスコープ前の状態に復元します。この設定は`Elif`スコープ内のコードで各変数を更新したくない場合に役立ちます。

- `globals_`: dict or None, default None
  - 現在のスコープの各グローバル変数。設定する場合にはglobal()関数の値をこの引数に指定してください。この設定はlocals_引数と同じように動作します。

<hr>

**[特記事項]**

 ・現在apyscでは条件値をコンストラクタ内で直接作成することはできません。<br> ・このクラスは`If`や`Elif`クラスによるステートメントの直後でのみ使用することができます。<hr>

**[コードサンプル]**

```py
>>> # You can avoid notes exception by predefining condition
>>> # value, as follows:
>>> import apysc as ap
>>> any_value: ap.Int = ap.Int(10)
>>> condition_1: ap.Boolean = any_value >= 10
>>> condition_2: ap.Boolean = any_value >= 5
>>> with ap.If(condition_1):
...     # Do something here
...     pass
...
>>> with ap.Elif(condition_2):
...     # Do something else here
...     pass
...
```

<hr>

**[関連資料]**

- [分岐条件の各クラスのスコープ内変数の復元設定](https://simon-ritchie.github.io/apysc/en/jp_branch_instruction_variables_reverting_setting.html)