<span class="inconspicuous-txt">※この翻訳ドキュメントはスクリプトによって出力・同期されています。内容が怪しそうな場合は<a href="https://github.com/simon-ritchie/apysc/issues" target="_blank">GitHubにissue</a>を追加したり[英語の原文](https://simon-ritchie.github.io/apysc/en/string.html)の確認をお願いします。</span>

# String クラス

このページでは`String`クラスについて説明します。

事前に以下のページを確認しておくと読み進める上で役に立つかもしれません:

- [なぜapyscではPythonのビルトインのデータの型を使用していないのか](jp_why_apysc_doesnt_use_python_builtin_data_type.md)

## String クラスの概要

`String`クラスはapyscの文字列用のクラスです。このクラスは以下のコード例のようにコンストラクタの引数に`str`もしくは`String`型の値を受け付けます:

```py
# runnable
import apysc as ap

ap.Stage()
string_1: ap.String = ap.String("Hello")
assert string_1 == "Hello"

string_2: ap.String = ap.String(string_1)
assert string_2 == "Hello"
```

## String クラスの各インターフェイス

`String`クラスの各インターフェイスの詳細については以下の資料などをご確認ください:

- [String クラスの比較制御](jp_string_comparison_operations.md)
- [String クラスの加算と乗算の制御](jp_string_addition_and_multiplication.md)

## String クラスのコンストラクタのAPI

<span class="inconspicuous-txt">特記事項: このAPIドキュメントはドキュメントビルド用のスクリプトによって自動で生成・同期されています。そのためもしかしたらこの節の内容は前節までの内容と重複している場合があります。</span>

**[インターフェイスの構造]** `__init__(self, value: Union[str, ForwardRef('String')], *, variable_name_suffix: str = '', skip_init_substitution_expression_appending: bool = False) -> None`<hr>

**[インターフェイス概要]**

apyscライブラリにおける文字列用のクラスです。<hr>

**[引数]**

- `value`: String or str
  - 文字列の値の初期値。

- `variable_name_suffix`: str, default ""
  - JavaScript上の変数のサフィックスの設定です。この設定はJavaScriptのデバッグ時に役立つことがあります。

- `skip_init_substitution_expression_appending`: bool, default False
  - 初期値の代入のコード表現をスキップするかどうかの真偽値です。このオプションはクラス内部の実装で使用されます。

<hr>

**[特記事項]**

`Str`クラスは`String`クラスのエイリアスとなります。<hr>

**[コードサンプル]**

```py
>>> import apysc as ap
>>> _ = ap.Stage()
>>> string: ap.String = ap.String("Hello")
>>> string
String("Hello")

>>> string += " World!"
>>> string
String("Hello World!")
```

<hr>

**[関連資料]**

- [String クラスの比較制御](https://simon-ritchie.github.io/apysc/jp/jp_string_comparison_operations.html)
- [String クラスの加算と乗算の制御](https://simon-ritchie.github.io/apysc/jp/jp_string_addition_and_multiplication.html)

## value 属性のAPI

<span class="inconspicuous-txt">特記事項: このAPIドキュメントはドキュメントビルド用のスクリプトによって自動で生成・同期されています。そのためもしかしたらこの節の内容は前節までの内容と重複している場合があります。</span>

**[インターフェイス概要]**

現在の文字列の値を取得します。<hr>

**[返却値]**

- `value`: str
  - 現在の文字列の値。

<hr>

**[コードサンプル]**

```py
>>> import apysc as ap
>>> _ = ap.Stage()
>>> string: ap.String = ap.String("Hello")
>>> string.value = "World!"
>>> string.value
'World!'
```

<hr>

**[関連資料]**

- [apyscの基本的なデータクラスの value インターフェイス](https://simon-ritchie.github.io/apysc/jp/jp_fundamental_data_classes_value_interface.html)