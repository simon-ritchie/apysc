<span class="inconspicuous-txt">※この翻訳ドキュメントはスクリプトによって出力・同期されています。内容が怪しそうな場合は<a href="https://github.com/simon-ritchie/apysc/issues" target="_blank">GitHubにissue</a>を追加したり[英語の原文](https://simon-ritchie.github.io/apysc/en/assert_arrays_equal_and_arrays_not_equal.html)の確認をお願いします。</span>

# assert_arrays_equal と assert_arrays_not_equal インターフェイス

このページでは`assert_arrays_equal`と`assert_arrays_not_equal`関数の各インターフェイスについて説明します。

## 各インターフェイスの概要

`assert_arrays_equal`関数のインターフェイスは2つの配列の値が一致していることをチェックします。逆に`assert_arrays_not_equal`関数は2つの配列の値が一致していないことをチェックします。

## 関連資料

- [JavaScriptの各アサーションのインターフェイスの基本的な挙動](jp_assertion_basic_behavior.md)

## 基本的な使い方

`assert_arrays_equal`と`assert_arrays_not_equal`のインターフェイスは共に`left`と`right`という2つの引数を必要とします。`msg`引数は省略可です。

引数にはPythonビルトインの`list`の値もしくはapyscの`Array`の値を指定することができます。

以下のコードで例では`assert_arrays_equal`関数を使って値が一致していることを確認しています:

```py
# runnable
import apysc as ap

stage: ap.Stage = ap.Stage(
    stage_width=0, stage_height=0, background_color='#333',
    stage_elem_id='stage')

arr_1: ap.Array = ap.Array([1, 2, 3])
ap.assert_arrays_equal(
    left=[1, 2, 3], right=arr_1, msg='Values are not equal!')

ap.save_overall_html(
    dest_dir_path='assert_arrays_equal_basic_usage_1/')
```

```
[assert_arrays_equal]
Left value: [1, 2, 3] right value: arr_2
```

<iframe src="static/assert_arrays_equal_basic_usage_1/index.html" width="0" height="0"></iframe>

以下のコード例では`assert_arrays_equal`関数を使って値が一致しておらずチェックが失敗していることを確認しています。

```py
# runnable
import apysc as ap

stage: ap.Stage = ap.Stage(
    stage_width=0, stage_height=0, background_color='#333',
    stage_elem_id='stage')

arr_1: ap.Array = ap.Array([1, 2, 3])
ap.assert_arrays_equal(
    left=[1, 2], right=arr_1, msg='Values are not equal!')

ap.save_overall_html(
    dest_dir_path='assert_arrays_equal_basic_usage_2/')
```

```
[assert_arrays_equal]
Left value: [1, 2] right value: arr_2
...
Assertion failed: Values are not equal!
```

<iframe src="static/assert_arrays_equal_basic_usage_2/index.html" width="0" height="0"></iframe>

以下のコード例では`assert_arrays_not_equal`関数を使って値が一致していないためチェックを通っていることを確認しています:

```py
# runnable
import apysc as ap

stage: ap.Stage = ap.Stage(
    stage_width=0, stage_height=0, background_color='#333',
    stage_elem_id='stage')

arr_1: ap.Array = ap.Array([1, 2, 3])
ap.assert_arrays_not_equal(
    left=[1, 2], right=arr_1, msg='Values are equal!')

ap.save_overall_html(
    dest_dir_path='assert_arrays_not_equal_basic_usage_1/')
```

<iframe src="static/assert_arrays_not_equal_basic_usage_1/index.html" width="0" height="0"></iframe>

## assert_equal と assert_not_equal の各インターフェイスにおける特記事項

もしも`assert_equal`もしくは`assert_not_equal`のインターフェイスに`Array`の値が指定された場合、自動的にそれらのインターフェイスの代わりに`assert_arrays_equal`と`assert_arrays_not_equal`のインターフェイスが使用されます。

```py
# runnable
import apysc as ap

stage: ap.Stage = ap.Stage(
    stage_width=0, stage_height=0, background_color='#333',
    stage_elem_id='stage')

arr_1: ap.Array = ap.Array([1, 2, 3, 4, 5])
ap.assert_equal(
    left=[1, 2, 3, 4, 5], right=arr_1, msg='Values are equal!')

ap.save_overall_html(
    dest_dir_path='assert_arrays_equal_notes_for_the_assert_equal/')
```

```
[assert_arrays_equal]
Left value: [1, 2, 3, 4, 5] right value: arr_2
```

<iframe src="static/assert_arrays_equal_notes_for_the_assert_equal/index.html" width="0" height="0"></iframe>

## assert_arrays_equal API

<span class="inconspicuous-txt">特記事項: このAPIドキュメントはドキュメントビルド用のスクリプトによって自動で生成・同期されています。そのためもしかしたらこの節の内容は前節までの内容と重複している場合があります。</span>

**[インターフェイスの構造]** `assert_arrays_equal(left: Any, right: Any, *, msg: str = '') -> None`<hr>

**[インターフェイス概要]** JavaScript上での配列の等値条件のチェックを行うインターフェイスです。<hr>

**[引数]**

- `left`: *
  - 比較用の左辺の値。

- `right`: *
  - 比較用の右辺の値。

- `msg`: str, optional
  - チェックに失敗した際に表示するメッセージ。

<hr>

**[特記事項]**

このインターフェイスは`Array`クラスの値の比較時には`assert_equal`インターフェイスの代わりに使用されます（JavaScript上ではPythonのリストのように直接配列の比較が行えないため代わりにこのインターフェイスが使用されます）。<hr>

**[コードサンプル]**

```py
>>> import apysc as ap
>>> arr_1: ap.Array = ap.Array([1, 2, 3])
>>> arr_2: ap.Array = ap.Array([1, 2, 3])
>>> ap.assert_arrays_equal(arr_1, arr_2)
```

## assert_arrays_not_equal API

<span class="inconspicuous-txt">特記事項: このAPIドキュメントはドキュメントビルド用のスクリプトによって自動で生成・同期されています。そのためもしかしたらこの節の内容は前節までの内容と重複している場合があります。</span>

**[インターフェイスの構造]** `assert_arrays_not_equal(left: Any, right: Any, *, msg: str = '') -> None`<hr>

**[インターフェイス概要]** JavaScript上での配列の非等値条件のチェックを行うインターフェイスです。<hr>

**[引数]**

- `left`: *
  - 比較用の左辺の値。

- `right`: *
  - 比較用の右辺の値。

- `msg`: str, optional
  - チェックに失敗した際に表示するメッセージ。

<hr>

**[特記事項]**

このインターフェイスは`Array`クラスの値の比較時には`assert_not_equal`インターフェイスの代わりに使用されます（JavaScript上ではPythonのリストのように直接配列の比較が行えないため代わりにこのインターフェイスが使用されます）。<hr>

**[コードサンプル]**

```py
>>> import apysc as ap
>>> arr_1: ap.Array = ap.Array([1, 2, 3])
>>> arr_2: ap.Array = ap.Array([4, 5, 6])
>>> ap.assert_arrays_not_equal(arr_1, arr_2)
```