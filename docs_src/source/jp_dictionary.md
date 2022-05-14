<span class="inconspicuous-txt">※この翻訳ドキュメントはスクリプトによって出力・同期されています。内容が怪しそうな場合は<a href="https://github.com/simon-ritchie/apysc/issues" target="_blank">GitHubにissue</a>を追加したり[英語の原文](https://simon-ritchie.github.io/apysc/en/dictionary.html)の確認をお願いします。</span>

# Dictionary クラス

このページでは`Dictionary`クラスについて説明します。

事前に以下のページを確認しておくと読み進める上で役に立つかもしれません:

- [なぜapyscではPythonのビルトインのデータの型を使用していないのか](jp_why_apysc_doesnt_use_python_builtin_data_type.md)

## Dictionaryクラスの概要

`Dictionary`クラスはapyscの辞書用のクラスです。ごのクラスはPythonビルトインの`dict`の値のように動作します。

## コンストラクタメソッド

`Dictionary`のコンストラクタではPythonビルトインの`dict`もしくはapyscの`Dictionary`の値を必要とします:

```py
# runnable
import apysc as ap

dict_1: ap.Dictionary = ap.Dictionary({'a': 10})
assert dict_1 == {'a': 10}

dict_2: ap.Dictionary = ap.Dictionary(dict_1)
assert dict_1 == dict_2
```

## 値のsetterのインターフェイス

`Dictionary`の値はPythonのビルトインの`dict`の値と同じようにインデックスを使って更新することができます:

```py
# runnable
import apysc as ap

dict_1: ap.Dictionary = ap.Dictionary({'a': 10})
dict_1['a'] = 20
assert dict_1 == {'a': 20}
```

## 値のgetterのインターフェイス

`Dictionary`の値の取得も同様にインデックスを使って行うことができます:

```py
# runnable
import apysc as ap

int_1: ap.Int = ap.Int(10)
dict_1: ap.Dictionary = ap.Dictionary({'a': int_1})
int_2: ap.Int = dict_1['a']
assert isinstance(int_2, ap.Int)
assert int_2 == 10
```

## getterのインターフェイスの特記事項

もしも`Dictionary`の値が指定されたキーを持たない場合、取り出される値は`AnyValue`型の値となります。この挙動はJavaScript上でのハンドラでの動的な更新処理などを使う際に便利な時があります。

```py
# runnable
import apysc as ap

int_1: ap.Int = ap.Int(10)
dict_1: ap.Dictionary = ap.Dictionary({'a': int_1})
retrieved_val: ap.AnyValue = dict_1['b']
assert isinstance(retrieved_val, ap.AnyValue)
```

## 値の削除のインターフェイス

`Dictionary`の値は以下のコード例のように`del`ステートメントで削除することができます。

```py
# runnable
import apysc as ap

int_1: ap.Int = ap.Int(10)
dict_1: ap.Dictionary = ap.Dictionary({'a': int_1})
del dict_1['a']
assert dict_1 == {}
```

## Dictionary クラスのコンストラクタのAPI

<span class="inconspicuous-txt">特記事項: このAPIドキュメントはドキュメントビルド用のスクリプトによって自動で生成・同期されています。そのためもしかしたらこの節の内容は前節までの内容と重複している場合があります。</span>

**[インターフェイスの構造]** `__init__(self, value: Union[Dict[~_K, ~_V], ForwardRef('Dictionary')]) -> None`<hr>

**[インターフェイス概要]** apyscで使用する辞書のクラスです。<hr>

**[引数]**

- `value`: dict or Dictionary
  - 辞書の初期値。

<hr>

**[コードサンプル]**

```py
>>> import apysc as ap
>>> dictionary: ap.Dictionary = ap.Dictionary({'a': 10})
>>> dictionary
Dictionary({'a': 10})

>>> dictionary['a']
10

>>> dictionary['b'] = 20
>>> dictionary['b']
20
```

<hr>

**[関連資料]**

- [Dictionary クラスのジェネリックの型設定](https://simon-ritchie.github.io/apysc/jp_dictionary_generic.html)

## value 属性のAPI

<span class="inconspicuous-txt">特記事項: このAPIドキュメントはドキュメントビルド用のスクリプトによって自動で生成・同期されています。そのためもしかしたらこの節の内容は前節までの内容と重複している場合があります。</span>

**[インターフェイス概要]** 現在の辞書の値を取得します。<hr>

**[返却値]**

- `value`: dict
  - 現在の辞書の値。

<hr>

**[コードサンプル]**

```py
>>> import apysc as ap
>>> dictionary: ap.Dictionary = ap.Dictionary({})
>>> dictionary.value = {'a': 10}
>>> dictionary.value
{'a': 10}
```

<hr>

**[関連資料]**

- [apyscの基本的なデータクラスの value インターフェイス](https://simon-ritchie.github.io/apysc/jp_fundamental_data_classes_value_interface.html)