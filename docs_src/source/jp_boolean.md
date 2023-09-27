<span class="inconspicuous-txt">※この翻訳ドキュメントはスクリプトによって出力・同期されています。内容が怪しそうな場合は<a href="https://github.com/simon-ritchie/apysc/issues" target="_blank">GitHubにissue</a>を追加したり[英語の原文](https://simon-ritchie.github.io/apysc/en/boolean.html)の確認をお願いします。</span>

# Boolean クラス

このページでは`Boolean`クラスについて説明します。

事前に以下のページを確認しておくと読み進める上で役に立つかもしれません:

- [なぜapyscではPythonのビルトインのデータの型を使用していないのか](jp_why_apysc_doesnt_use_python_builtin_data_type.md)

## Boolean クラスの概要

`Boolean`クラスはapyscの真偽値のクラスです。コンストラクタの引数には以下のコード例のように`bool`や`Boolean`の値を受け付けます:

```py
# runnable
import apysc as ap

_ = ap.Stage()
bool_1: ap.Boolean = ap.Boolean(True)
assert bool_1

bool_2: ap.Boolean = ap.Boolean(False)
assert not bool_2

bool_3: ap.Boolean = ap.Boolean(bool_1)
assert bool_3
```

## Boolクラスのエイリアスの特記事項

`Bool`クラスは`Boolean`クラスのエイリアスとなります。`Boolean`クラスと同じ挙動をします。

```py
# runnable
import apysc as ap

_ = ap.Stage()
assert ap.Boolean == ap.Bool
assert ap.Boolean(True) == ap.Bool(True)
```

## Boolean クラスの比較制御

`Boolean`クラスの比較のインターフェイスはPythonビルトインの`bool`クラスの値のように動作します。

等値の比較のオペレーター（`==`）を使って`Boolean`の値と比較することができ、以下のコード例のように`Boolean`や`bool`、`int`、`Int`などの型との比較を行うことができます:

```py
# runnable
import apysc as ap

_ = ap.Stage()
bool_1: ap.Boolean = ap.Boolean(True)
assert bool_1 == True  # noqa
assert bool_1 == ap.Boolean(True)
assert bool_1 == 1
assert bool_1 == ap.Int(1)
```

同様に以下のコード例のように非等値のオペレーター（`!=`）もサポートされています。

```py
# runnable
import apysc as ap

_ = ap.Stage()
bool_1: ap.Boolean = ap.Boolean(True)
assert bool_1 != False  # noqa
assert bool_1 != ap.Boolean(False)
assert bool_1 != 0
assert bool_1 != ap.Int(0)
```

以下のコードのように比較のオペレーターを省略して使うこともできます:

```py
# runnable
import apysc as ap

_ = ap.Stage()
bool_1: ap.Boolean = ap.Boolean(True)
assert bool_1

bool_2: ap.Boolean = ap.Boolean(False)
assert not bool_2
```

## Boolean の値を反転させる

`not_`属性は値が反転した`Boolean`の値を返却します:

```py
# runnable
import apysc as ap

_ = ap.Stage()
bool_1: ap.Boolean = ap.Boolean(True)
bool_2: ap.Boolean = bool_1.not_
assert not bool_2

bool_3: ap.Boolean = bool_2.not_
assert bool_3
```

## Boolean クラスのコンストラクタのAPI

<span class="inconspicuous-txt">特記事項: このAPIドキュメントはドキュメントビルド用のスクリプトによって自動で生成・同期されています。そのためもしかしたらこの節の内容は前節までの内容と重複している場合があります。</span>

**[インターフェイスの構造]** `__init__(self, value: Union[bool, typing_extensions.Literal[0, 1], apysc._type.int.Int, ForwardRef('Boolean')], *, variable_name_suffix: str = '', skip_init_substitution_expression_appending: bool = False) -> None`<hr>

**[インターフェイス概要]**

apyscライブラリのための真偽値のクラスです。<hr>

**[引数]**

- `value`: Boolean or Int or bool or int
  - 真偽値の初期値。整数の場合は0か1が受け付けられます。

- `variable_name_suffix`: str, default ""
  - JavaScript上の変数のサフィックスの設定です。この設定はJavaScriptのデバッグ時に役立つことがあります。

- `skip_init_substitution_expression_appending`: bool, default False
  - 初期値の代入のコード表現をスキップするかどうかの真偽値です。このオプションはクラス内部の実装で使用されます。

<hr>

**[特記事項]**

BoolクラスはBooleanクラスのエイリアスであり、Booleanクラスと同じように動作します。<hr>

**[コードサンプル]**

```py
>>> import apysc as ap
>>> _ = ap.Stage()
>>> bool_val_1: ap.Boolean = ap.Boolean(True)
>>> bool_val_1
Boolean(True)

>>> bool_val_2: ap.Bool = ap.Bool(True)
>>> bool_val_2
Boolean(True)
```

<hr>

**[関連資料]**

- [True_ と False_ の各定数](https://simon-ritchie.github.io/apysc/jp/jp_true_and_false.html)

## value 属性のAPI

<span class="inconspicuous-txt">特記事項: このAPIドキュメントはドキュメントビルド用のスクリプトによって自動で生成・同期されています。そのためもしかしたらこの節の内容は前節までの内容と重複している場合があります。</span>

**[インターフェイス概要]**

現在の真偽値の値を取得します。<hr>

**[返却値]**

- `value`: bool
  - 現在の真偽値の値。

<hr>

**[コードサンプル]**

```py
>>> import apysc as ap
>>> _ = ap.Stage()
>>> bool_val: ap.Boolean = ap.Boolean(True)
>>> bool_val.value = False
>>> bool_val.value
False

>>> bool_val.value = ap.Boolean(True)
>>> bool_val.value
True
```

<hr>

**[関連資料]**

- [apyscの基本的なデータクラスの value インターフェイス](https://simon-ritchie.github.io/apysc/jp/jp_fundamental_data_classes_value_interface.html)

## not_ 属性のAPI

<span class="inconspicuous-txt">特記事項: このAPIドキュメントはドキュメントビルド用のスクリプトによって自動で生成・同期されています。そのためもしかしたらこの節の内容は前節までの内容と重複している場合があります。</span>

**[インターフェイス概要]**

否定条件を加えた真偽値の値を取得します。<hr>

**[返却値]**

- `result`: Boolean
  - 反転（否定）させたBoolean型の値。

<hr>

**[コードサンプル]**

```py
>>> import apysc as ap
>>> _ = ap.Stage()
>>> bool_val: ap.Boolean = ap.Boolean(True)
>>> bool_val.not_
Boolean(False)

>>> bool_val.value = False
>>> bool_val.not_
Boolean(True)
```