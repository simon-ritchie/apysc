<span class="inconspicuous-txt">※この翻訳ドキュメントはスクリプトによって出力・同期されています。内容が怪しそうな場合は<a href="https://github.com/simon-ritchie/apysc/issues" target="_blank">GitHubにissue</a>を追加したり[英語の原文](https://simon-ritchie.github.io/apysc/en/array.html)の確認をお願いします。</span>

# Array クラス

このページでは`Array`クラスについて説明します。

事前に以下のページを確認しておくと読み進める上で役に立つかもしれません:

- [なぜapyscではPythonのビルトインのデータの型を使用していないのか](jp_why_apysc_doesnt_use_python_builtin_data_type.md)

## Array クラスとは

`Array`クラスはapyscの配列のクラスです。このクラスはPythonビルトインの`list`のように動作します。

## コンストラクタメソッド

`Array`クラスのコンストラクタでは`list`や`tuple`、`range`、`Array`などのイテラブルなオブジェクトが引数に必要となります。

```py
# runnable
import apysc as ap

ap.Stage()
arr_from_list: ap.Array = ap.Array([1, 2, 3])
assert arr_from_list == [1, 2, 3]

arr_from_tuple: ap.Array = ap.Array((4, 5, 6))
assert arr_from_tuple == [4, 5, 6]

other_arr: ap.Array = ap.Array([7, 8, 9])
arr_from_arr: ap.Array = ap.Array(other_arr)
assert arr_from_arr == [7, 8, 9]
```

## ジェネリックの型アノテーション

もし`Array`クラスの値の型が一意な場合は配列に対してジェネリックの型の指定を行うことができます。この型アノテーションはIDE上などで便利なケースがあります（型チェックのライブラリなどを使う場合に）。

```py
# runnable
import apysc as ap

ap.Stage()
arr: ap.Array[int] = ap.Array([1, 2])
int_val: int = arr.pop()
assert isinstance(int_val, int)
```

## fixed_value_type 引数について

コンストラクタの`fixed_value_type`引数は省略可能な引数になっています。

もし指定された場合、`__getitem__`メソッド（`arr[5]`などの配列の添え字のインターフェイスが該当します）などの配列の値に関係した各インターフェイスが指定された型のインスタンスを返却するケースが発生するようになります

この返却処理はPythonランタイム上で配列の添え字が配列の長さを越える場合などに発生するようになります。

```py
# runnable
import apysc as ap

ap.Stage(
    stage_width=100,
    stage_height=50,
    background_color=ap.Color("#333"),
    stage_elem_id="stage",
)
arr: ap.Array[ap.Int] = ap.Array([ap.Int(10)], fixed_value_type=ap.Int)

# Index 5 is out of bounds on the Python runtime,
# but since the `fixed_value_type` is the `ap.Int`,
# this interface returns an `ap.Int` value.
int_value: ap.Int = arr[5]
assert isinstance(int_value, ap.Int)
```

## 関連資料

- [基本的なデータクラスの共通の value インターフェイス](jp_fundamental_data_classes_value_interface.md)
- [Array クラスの append と push のインターフェイス](jp_array_append_and_push.md)

- [Array クラスの extend と concat のインターフェイス](jp_array_extend_and_concat.md)
- [Array クラスの insert と insert_at のインターフェイス](jp_array_insert_and_insert_at.md)

- [Array クラスの pop インターフェイス](jp_array_pop.md)
- [Array クラスの remove と remove_at のインターフェイス](jp_array_remove_and_remove_at.md)

- [Array クラスの sort インターフェイス](jp_array_sort.md)
- [Array クラスの reverse インターフェイス](jp_array_reverse.md)

- [Array クラスの slice インターフェイス](jp_array_slice.md)
- [Array クラスの length (配列の長さ取得) のインターフェイス](jp_array_length.md)

- [Array クラスの join (値の連結文字列生成) のインターフェイス](jp_array_join.md)
- [Array クラスの index_of (値のインデックス取得) のインターフェイス](jp_array_index_of.md)

- [Array クラスの比較の各インターフェイス](jp_array_comparison.md)

## Array クラスのコンストラクタのAPI

<span class="inconspicuous-txt">特記事項: このAPIドキュメントはドキュメントビルド用のスクリプトによって自動で生成・同期されています。そのためもしかしたらこの節の内容は前節までの内容と重複している場合があります。</span>

**[インターフェイスの構造]** `__init__(self, value: Union[List[~_ArrValue], tuple, range, ForwardRef('Array')], *, fixed_value_type: Union[Type[apysc._loop.initialize_with_base_value_interface.InitializeWithBaseValueInterface], NoneType] = None, variable_name_suffix: str = '', skip_init_substitution_expression_appending: bool = False) -> None`<hr>

**[インターフェイス概要]**

apyscライブラリの配列を扱うためのクラスです。<hr>

**[引数]**

- `value`: Array or list or tuple or range
  - 配列の初期値。

- `fixed_value_type`: Optional[Type[InitializeWithBaseValueInterface]], optional
  - 配列の値の固定の型。この引数は`ap.Int`、`ap.String`、`ap.Rectangle`などのapyscの型のみ設定することができます。もし指定された場合、`__getitem__`などのメソッド（`arr[5]`などの配列の添え字のインターフェイスが該当します）が指定された型のインスタンスを返却するケースが発生するようになります。

- `variable_name_suffix`: str, default ""
  - JavaScript上の変数のサフィックスの設定です。この設定はJavaScriptのデバッグ時に役立つことがあります。

- `skip_init_substitution_expression_appending`: bool, default False
  - 初期値の代入のコード表現をスキップするかどうかの真偽値です。このオプションはクラス内部の実装で使用されます。

<hr>

**[コードサンプル]**

```py
>>> import apysc as ap
>>> _ = ap.Stage()
>>> arr: ap.Array = ap.Array([1, 2, 3])
>>> arr
Array([1, 2, 3])

>>> arr[0]
1

>>> arr[1]
2

>>> arr = ap.Array((4, 5, 6))
>>> arr
Array([4, 5, 6])

>>> arr = ap.Array(range(3))
>>> arr
Array([0, 1, 2])
```

<hr>

**[関連資料]**

- [Array クラスの比較の各インターフェイス](https://simon-ritchie.github.io/apysc/jp/jp_array_comparison.html)

## value 属性のAPI

<span class="inconspicuous-txt">特記事項: このAPIドキュメントはドキュメントビルド用のスクリプトによって自動で生成・同期されています。そのためもしかしたらこの節の内容は前節までの内容と重複している場合があります。</span>

**[インターフェイス概要]**

現在の配列の値を取得します。<hr>

**[返却値]**

- `value`: list
  - 現在の配列の値。

<hr>

**[コードサンプル]**

```py
>>> import apysc as ap
>>> _ = ap.Stage()
>>> arr: ap.Array = ap.Array([1, 2, 3])
>>> arr.value = [4, 5, 6]
>>> arr.value
[4, 5, 6]
```

<hr>

**[関連資料]**

- [apyscの基本的なデータクラスの value インターフェイス](https://simon-ritchie.github.io/apysc/jp/jp_fundamental_data_classes_value_interface.html)