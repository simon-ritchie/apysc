<span class="inconspicuous-txt">※この翻訳ドキュメントはスクリプトによって出力・同期されています。内容が怪しそうな場合は<a href="https://github.com/simon-ritchie/apysc/issues" target="_blank">GitHubにissue</a>を追加したり[英語の原文](../en/if.html)の確認をお願いします。</span>

# If クラス

このページでは`If`クラスについて説明します。

このページを読み進める前に以下のページを確認しておくと役に立つかもしれません（apyscでは基本的なデータクラスと同様の理由で`If`クラスを使用しています）:

- [なぜapyscではPythonのビルトインのデータの型を使用していないのか](jp_why_apysc_doesnt_use_python_builtin_data_type.md)

## If クラスの概要

`If`クラスはapyscの分岐制御のためのクラスです。このクラスはPythonビルトインの`if`キーワードと似たような形で動作します。

## 基本的な使い方

`If`クラスは以下のコード例のように`with`ステートメントと共に使用する必要があります:

```py
# runnable
import apysc as ap

condition: ap.Boolean = ap.Boolean(True)
with ap.If(condition):
    ...
```

`If`クラスのコンストラクタの引数には条件としての`Boolean`の値の指定が必要になります。

## 関連資料

- [Elif クラス](jp_elif.md)
- [Else クラス](jp_else.md)

- [分岐条件の各クラスのスコープ内変数の復元設定](jp_branch_instruction_variables_reverting_setting.md)

## If クラスのコンストラクタのAPI

<span class="inconspicuous-txt">特記事項: このAPIドキュメントはドキュメントビルド用のスクリプトによって自動で生成・同期されています。そのためもしかしたらこの節の内容は前節までの内容と重複している場合があります。</span>

**[インターフェイスの構造]** `__init__(self, condition:Union[apysc._type.boolean.Boolean, NoneType], *, locals_:Union[Dict[str, Any], NoneType]=None, globals_:Union[Dict[str, Any], NoneType]=None) -> None`<hr>

**[インターフェイス概要]** if文の分岐制御の表現を追加するためのクラス。<hr>

**[引数]**

- `condition`: Boolean or None
  - 判定に使われるBooleanの真偽値。

- `locals_`: dict or None, default None
  - 現在のスコープの各ローカル変数。指定する場合にはlocals()関数の値をごの引数に指定してください。もし指定された場合、このインターフェイスは`If`のスコープの終了時に対象のVariableNameInterfaceクラスの各ローカル変数のインスタンスの値をスコープの開始前の時点に復元します。この設定は`If`のスコープ内の処理でPython上の各ローカル変数の値を更新したくない場合などに便利なことがあります。

- `globals_`: dict or None, default None
  - 現在のスコープの各グローバル変数。設定する場合にはglobal()関数の値をこの引数に指定してください。この設定はlocals_引数と同じように動作します。

<hr>

**[コードサンプル]**

```py
>>> import apysc as ap
>>> int_val: ap.Int = ap.Int(10)
>>> condition: ap.Boolean = int_val >= 10
>>> with ap.If(condition):
...     ap.trace('Int value is greater than equal 10!')
```

<hr>

**[関連資料]**

- [分岐条件の各クラスのスコープ内変数の復元設定](https://simon-ritchie.github.io/apysc/jp_branch_instruction_variables_reverting_setting.html)