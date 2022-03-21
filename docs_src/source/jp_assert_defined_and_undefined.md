<span class="inconspicuous-txt">※この翻訳ドキュメントはスクリプトによって出力・同期されています。内容が怪しそうな場合は<a href="https://github.com/simon-ritchie/apysc/issues" target="_blank">GitHubにissue</a>を追加したり[英語の原文](assert_defined_and_undefined.md)の確認をお願いします。</span>

# assert_defined と assert_undefined のインターフェイス

このページでは`assert_defined`と`assert_undefined`の関数の各インターフェイスについて説明します。

## 各インターフェイスの概要

`assert_defined`関数のインターフェイスは指定された値が定義済みかどうか（初期化されているか）をチェックします。逆に`assert_undefined`関数は指定された値が定義されていない（`undefine`）状態や削除済みかどうかなどをチェックします。

## 関連資料

- [JavaScriptの各アサーションのインターフェイスの基本的な挙動](jp_assertion_basic_behavior.md)

## 基本的な使い方

`assert_defined`と`assert_undefined`の各インターフェイスは共に`value`引数が必要になります。`msg`引数は省略可です。

以下のコード例では初期化されている値に対して`assert_defined`関数でチェックを行っています（チェックを通ります）:

```py
# runnable
import apysc as ap

stage: ap.Stage = ap.Stage(
    stage_width=0, stage_height=0, background_color='#333',
    stage_elem_id='stage')

int_val: ap.Int = ap.Int(10)
ap.assert_defined(
    value=int_val, msg='Value is not defined!')

ap.save_overall_html(
    dest_dir_path='assert_defined_basic_usage_1/')
```

```
[assert_defined]
Right-side variable name: i_11
Left value: other than undefined right value: 10
```

<iframe src="static/assert_defined_basic_usage_1/index.html" width="0" height="0"></iframe>

以下のコード例では削除の済みの値に対して`assert_defined`関数でチェックをしています（チェックは失敗します）:

```py
# runnable
import apysc as ap

stage: ap.Stage = ap.Stage(
    stage_width=0, stage_height=0, background_color='#333',
    stage_elem_id='stage')

int_val: ap.Int = ap.Int(10)
ap.append_js_expression(
    expression=f'{int_val.variable_name} = undefined;')
ap.assert_defined(
    value=int_val, msg='Value is not defined!')

ap.save_overall_html(
    dest_dir_path='assert_defined_basic_usage_2/')
```

```
[assert_defined]
Right-side variable name: i_11
Left value: other than undefined right value: undefined
...
Assertion failed: Value is not defined!
```

<iframe src="static/assert_defined_basic_usage_2/index.html" width="0" height="0"></iframe>

以下のコード例では削除済みの値に対して`assert_undefined`関数でチェックを行っています（チェックは通ります）:

```py
# runnable
import apysc as ap

stage: ap.Stage = ap.Stage(
    stage_width=0, stage_height=0, background_color='#333',
    stage_elem_id='stage')

int_val: ap.Int = ap.Int(10)
ap.append_js_expression(
    expression=f'{int_val.variable_name} = undefined;')
ap.assert_undefined(
    value=int_val, msg='Value is defined!')

ap.save_overall_html(
    dest_dir_path='assert_undefined_basic_usage_1/')
```

```
[assert_undefined]
Right-side variable name: i_11
Left value: undefined right value: undefined
```

<iframe src="static/assert_undefined_basic_usage_1/index.html" width="0" height="0"></iframe>

## assert_defined API

<span class="inconspicuous-txt">特記事項: このAPIドキュメントはドキュメントビルド用のスクリプトによって自動で生成・同期されています。そのためもしかしたらこの節の内容は前節までの内容と重複している場合があります。</span>

**[インターフェイスの構造]** `assert_defined(value:Any, *, msg:str='') -> None`<hr>

**[Interface summary]** JavaScriptでの値が定義済みかどうかのチェックを行うインターフェイスです。<hr>

**[引数]**

- `value`: *
  - チェック対象の値。

- `msg`: str, optional
  - チェックに失敗した際に表示するメッセージ。

<hr>

**[コードサンプル]**

```py
>>> import apysc as ap
>>> int_val: ap.Int = ap.Int(10)
>>> ap.assert_defined(int_val)
```

## assert_undefined API

<span class="inconspicuous-txt">特記事項: このAPIドキュメントはドキュメントビルド用のスクリプトによって自動で生成・同期されています。そのためもしかしたらこの節の内容は前節までの内容と重複している場合があります。</span>

**[インターフェイスの構造]** `assert_undefined(value:Any, *, msg:str='') -> None`<hr>

**[インターフェイス概要]** JavaScriptでの値が未定義かどうかのチェックを行うインターフェイスです。<hr>

**[引数]**

- `value`: *
  - チェック対象の値。

- `msg`: str, optional
  - チェックに失敗した際に表示するメッセージ。

<hr>

**[コードサンプル]**

```py
>>> import apysc as ap
>>> int_val: ap.Int = ap.Int(10)
>>> ap.append_js_expression(
...     expression=f'{int_val.variable_name} = undefined;')
>>> ap.assert_undefined(int_val)
```