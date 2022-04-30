<span class="inconspicuous-txt">※この翻訳ドキュメントはスクリプトによって出力・同期されています。内容が怪しそうな場合は<a href="https://github.com/simon-ritchie/apysc/issues" target="_blank">GitHubにissue</a>を追加したり[英語の原文](../en/assert_dicts_equal_and_dicts_not_equal.html)の確認をお願いします。</span>

# assert_dicts_equal と assert_dicts_not_equal インターフェイス

このページでは`assert_dicts_equal`と`assert_dicts_not_equal`の各関数のインターフェイスについて説明します。

## 各インターフェイスの概要

`assert_dicts_equal`関数のインターフェイスは指定された2つの辞書（`Dictionary`型など）の値が一致しているかをチェックします。逆に`assert_dicts_not_equal`関数のインターフェイスは指定された2つの辞書の値が一致していないことをチェックします。

## 関連資料

- [JavaScriptの各アサーションのインターフェイスの基本的な挙動](jp_assertion_basic_behavior.md)

## 基本的な使い方

`assert_dicts_equal`と`assert_dicts_not_equal`の各インターフェイスは`left`と`right`引数を必要とします。`msg`引数は省略可です。

各インターフェイスにはPythonビルトインの`dict`やapyscの`Dictionary`の値を引数として指定することができます。

以下の例では`assert_dicts_equal`関数を使って値が同じ辞書に対してチェックを行っています（チェックは通ります）。

```py
# runnable
import apysc as ap

stage: ap.Stage = ap.Stage(
    stage_width=0, stage_height=0, background_color='#333',
    stage_elem_id='stage')

dict_val: ap.Dictionary = ap.Dictionary({'a': 10, 'b': 20})
ap.assert_dicts_equal(
    left={'a': 10, 'b': 20}, right=dict_val,
    msg='Values are not equal!')

ap.save_overall_html(
    dest_dir_path='assert_dicts_equal_basic_usage_1/')
```

```
[assert_dicts_equal]
Left value: {a: 10, b: 20} right value: dct_1
```

<iframe src="static/assert_dicts_equal_basic_usage_1/index.html" width="0" height="0"></iframe>

以下の例では`assert_dicts_equal`関数を使って値が一致していない辞書に対してチェックを行っています（チェックは失敗します）。

```py
# runnable
import apysc as ap

stage: ap.Stage = ap.Stage(
    stage_width=0, stage_height=0, background_color='#333',
    stage_elem_id='stage')

dict_val: ap.Dictionary = ap.Dictionary({'a': 10, 'b': 20})
ap.assert_dicts_equal(
    left={'a': 30}, right=dict_val, msg='Values are not equal!')

ap.save_overall_html(
    dest_dir_path='assert_dicts_equal_basic_usage_2/')
```

```
[assert_dicts_equal]
Left value: {a: 30} right value: dct_1
...
Assertion failed: Values are not equal!
```

<iframe src="static/assert_dicts_equal_basic_usage_2/index.html" width="0" height="0"></iframe>

以下の例では`assert_dicts_not_equal`関数を使って値が一致していない辞書に対してチェックを行っています（チェックは通ります）。

```py
# runnable
import apysc as ap

stage: ap.Stage = ap.Stage(
    stage_width=0, stage_height=0, background_color='#333',
    stage_elem_id='stage')

dict_val: ap.Dictionary = ap.Dictionary({'a': 10, 'b': 20})
ap.assert_dicts_not_equal(
    left={'a': 30}, right=dict_val, msg='Values are equal!')

ap.save_overall_html(
    dest_dir_path='assert_dicts_not_equal_basic_usage_1/')
```

```
[assert_dicts_not_equal]
Left value: {a: 30} right value: dct_1
```

<iframe src="static/assert_dicts_not_equal_basic_usage_1/index.html" width="0" height="0"></iframe>

## assert_equal と assert_not_equal の各インターフェイスにおける特記事項

もし`assert_equal`もしくは`assert_not_equal`のインターフェイスの引数へ`Dictionary`の値が指定された場合、自動的に`assert_dicts_equal`もしくは`assert_dicts_not_equal`のインターフェイスがそれらのインターフェイスの代わりに呼ばれます。

```py
# runnable
import apysc as ap

stage: ap.Stage = ap.Stage(
    stage_width=0, stage_height=0, background_color='#333',
    stage_elem_id='stage')

dict_val: ap.Dictionary = ap.Dictionary({'a': 30})
ap.assert_equal(
    left={'a': 30}, right=dict_val,
    msg='Values are not equal!')

ap.save_overall_html(
    dest_dir_path='assert_dicts_equal_notes_for_assert_equal/')
```

```
[assert_dicts_equal]
Left value: {a: 30} right value: dct_1
```

<iframe src="static/assert_dicts_equal_notes_for_assert_equal/index.html" width="0" height="0"></iframe>

## assert_dicts_equal API

<span class="inconspicuous-txt">特記事項: このAPIドキュメントはドキュメントビルド用のスクリプトによって自動で生成・同期されています。そのためもしかしたらこの節の内容は前節までの内容と重複している場合があります。</span>

**[インターフェイスの構造]** `assert_dicts_equal(left:Any, right:Any, *, msg:str='') -> None`<hr>

**[インターフェイス概要]** JavaScript上での辞書の等値条件のチェックを行うインターフェイスです。<hr>

**[引数]**

- `left`: *
  - 比較用の左辺の値。

- `right`: *
  - 比較用の右辺の値。

- `msg`: str, optional
  - チェックに失敗した際に表示するメッセージ。

<hr>

**[特記事項]**

このインターフェイスは`assert_equal`関数での`Dictionary`のクラスの値の比較時には代わりに使用されます（JavaScriptではPythonと異なり辞書の値を直接比較できないため）。<hr>

**[コードサンプル]**

```py
>>> import apysc as ap
>>> dict_1: ap.Dictionary = ap.Dictionary({'a': 10})
>>> dict_2: ap.Dictionary = ap.Dictionary({'a': 10})
>>> ap.assert_dicts_equal(dict_1, dict_2)
```

## assert_dicts_not_equal API

<span class="inconspicuous-txt">特記事項: このAPIドキュメントはドキュメントビルド用のスクリプトによって自動で生成・同期されています。そのためもしかしたらこの節の内容は前節までの内容と重複している場合があります。</span>

**[インターフェイスの構造]** `assert_dicts_not_equal(left:Any, right:Any, *, msg:str='') -> None`<hr>

**[インターフェイス概要]** JavaScript上での辞書の非等値のチェックを行うインターフェイスです。<hr>

**[引数]**

- `left`: *
  - 比較用の左辺の値。

- `right`: *
  - 比較用の右辺の値。

- `msg`: str, optional
  - チェックに失敗した際に表示するメッセージ。

<hr>

**[特記事項]**

このインターフェイスは`assert_not_equal`関数での`Dictionary`クラスの値の比較時には代わりに使用されます（JavaScriptではPythonと異なり辞書の値を直接比較できないため）。<hr>

**[コードサンプル]**

```py
>>> import apysc as ap
>>> dict_1: ap.Dictionary = ap.Dictionary({'a': 10})
>>> dict_2: ap.Dictionary = ap.Dictionary({'a': 20})
>>> ap.assert_dicts_not_equal(dict_1, dict_2)
```