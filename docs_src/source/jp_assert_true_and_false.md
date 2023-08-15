<span class="inconspicuous-txt">※この翻訳ドキュメントはスクリプトによって出力・同期されています。内容が怪しそうな場合は<a href="https://github.com/simon-ritchie/apysc/issues" target="_blank">GitHubにissue</a>を追加したり[英語の原文](https://simon-ritchie.github.io/apysc/en/assert_true_and_false.html)の確認をお願いします。</span>

# assert_true と assert_false インターフェイス

このページでは`assert_true`と`assert_false`関数の各インターフェイスについて説明します。

## 各インターフェイスの概要

`assert_true`関数のインターフェイスは指定された`Boolean`の値が真（true）であることをチェックします。逆に`assert_false`関数のインターフェイスは指定された`Boolean`の値が偽（false）であることをチェックします。

## 関連資料

- [JavaScriptの各アサーションのインターフェイスの基本的な挙動](jp_assertion_basic_behavior.md)

## 基本的な使い方

`assert_true`と`assert_false`の各インターフェイスは`value`引数を必要とします。`type_strict`と`msg`引数は省略可です。`type_strict`引数のデフォルト値は`True`となります。

もしも`type_strict`引数に`True`が指定された場合チェック処理はJavaScriptの厳密な型の比較（`===`による比較）によって行われます。たとえばもし`value`引数の値が`Int(1)`で且つ`type_strict`引数が`True`の場合チェック処理は真偽値と整数（`Int`）間の比較となるため失敗します。逆に`type_strict`が`False`で且つ値が`Int(1)`であれば`assert_true`関数によるチェック処理は通ります。

これらのインターフェイスによるチェック結果はブラウザ上のコンソールに表示されます。

以下の`assert_true`関数と`Boolean(True)`の値を使用した処理のコード例ではチェックを通ります:

```py
# runnable
import apysc as ap

stage: ap.Stage = ap.Stage(
    stage_width=0,
    stage_height=0,
    background_color=ap.Color("#333"),
    stage_elem_id="stage",
)

bool_1: ap.Boolean = ap.Boolean(True)
ap.assert_true(bool_1, msg="Boolean value is not True!")

ap.save_overall_html(dest_dir_path="assert_true_basic_usage_1/")
```

```
[assert_true]
Right-side variable name: b_3
Left value: true right value: true
```

<iframe src="static/assert_true_basic_usage_1/index.html" width="0" height="0"></iframe>

以下の`assert_true`関数と`Boolean(False)`の値を使った処理ではチェックが失敗します:

```py
# runnable
import apysc as ap

stage: ap.Stage = ap.Stage(
    stage_width=0,
    stage_height=0,
    background_color=ap.Color("#333"),
    stage_elem_id="stage",
)

bool_1: ap.Boolean = ap.Boolean(False)
ap.assert_true(bool_1, msg="Boolean value is not True!")

ap.save_overall_html(dest_dir_path="assert_true_basic_usage_2/")
```

```
[assert_true]
Right-side variable name: b_3
Left value: true right value: false
...
Assertion failed: Boolean value is not True!
```

<iframe src="static/assert_true_basic_usage_2/index.html" width="0" height="0"></iframe>

以下の`assert_true`関数と`Int(1)`の値を使い、`type_strict`に`True`を指定した例ではチェックが失敗します:

```py
# runnable
import apysc as ap

stage: ap.Stage = ap.Stage(
    stage_width=0,
    stage_height=0,
    background_color=ap.Color("#333"),
    stage_elem_id="stage",
)

int_1: ap.Int = ap.Int(1)
ap.assert_true(int_1, type_strict=True, msg="Value is not Boolean(True)!")

ap.save_overall_html(dest_dir_path="assert_true_basic_usage_3/")
```

```
[assert_true]
Right-side variable name: i_11
Left value: true right value: 1
...
Assertion failed: Value is not Boolean(True)!
```

<iframe src="static/assert_true_basic_usage_3/index.html" width="0" height="0"></iframe>

以下の`assert_true`関数と`Int(1)`の値を使い`type_strict`に`False`を設定した処理ではチェックが通ります:

```py
# runnable
import apysc as ap

stage: ap.Stage = ap.Stage(
    stage_width=0,
    stage_height=0,
    background_color=ap.Color("#333"),
    stage_elem_id="stage",
)

int_1: ap.Int = ap.Int(1)
ap.assert_true(int_1, type_strict=False, msg="Value is not True!")

ap.save_overall_html(dest_dir_path="assert_true_basic_usage_4/")
```

```
[assert_true]
Right-side variable name: i_11
Left value: true right value: 1
```

<iframe src="static/assert_true_basic_usage_4/index.html" width="0" height="0"></iframe>

以下の`assert_false`関数と`Boolean(False)`の値を使った処理ではチェックを通ります:

```py
# runnable
import apysc as ap

stage: ap.Stage = ap.Stage(
    stage_width=0,
    stage_height=0,
    background_color=ap.Color("#333"),
    stage_elem_id="stage",
)

bool_1: ap.Boolean = ap.Boolean(False)
ap.assert_false(bool_1, msg="Value is not False!")

ap.save_overall_html(dest_dir_path="assert_false_basic_usage_1/")
```

```
[assert_false]
Right-side variable name: b_3
Left value: false right value: false
```

<iframe src="static/assert_false_basic_usage_1/index.html" width="0" height="0"></iframe>

## assert_true API

<span class="inconspicuous-txt">特記事項: このAPIドキュメントはドキュメントビルド用のスクリプトによって自動で生成・同期されています。そのためもしかしたらこの節の内容は前節までの内容と重複している場合があります。</span>

**[インターフェイスの構造]** `assert_true(value: Any, *, type_strict: bool = True, msg: str = '') -> None`<hr>

**[インターフェイス概要]**

真偽値の真の値のためのJavaScript上のアサーションのインターフェイスです。<hr>

**[引数]**

- `value`: *
  - チェック対象の値。

- `type_strict`: bool, default True
  - 厳密な型でのチェックを行うかどうかの設定です。たとえばtype_strictにTrueを指定した場合は整数の1ではテストは失敗します。逆にtype_strictがFalseの場合整数の1はテストを通過します。

- `msg`: str, optional
  - チェックに失敗した際に表示するメッセージ。

<hr>

**[コードサンプル]**

```py
>>> import apysc as ap
>>> int_val: ap.Int = ap.Int(10)
>>> boolean: ap.Boolean = int_val == 10
>>> ap.assert_true(boolean)
```

## assert_false API

<span class="inconspicuous-txt">特記事項: このAPIドキュメントはドキュメントビルド用のスクリプトによって自動で生成・同期されています。そのためもしかしたらこの節の内容は前節までの内容と重複している場合があります。</span>

**[インターフェイスの構造]** `assert_false(value: Any, *, type_strict: bool = True, msg: str = '') -> None`<hr>

**[インターフェイス概要]**

真偽値の偽の値のためのJavaScript上のアサーションのインターフェイスです。<hr>

**[引数]**

- `value`: *
  - チェック対象の値。

- `type_strict`: bool, default True
  - 厳密な型でのチェックを行うかどうかの設定です。たとえばtype_strictにTrueを指定した場合は整数の0ではテストは失敗します。逆にtype_strictがFalseの場合整数の0はテストを通過します。

- `msg`: str, optional
  - チェックに失敗した際に表示するメッセージ。

<hr>

**[コードサンプル]**

```py
>>> import apysc as ap
>>> int_val: ap.Int = ap.Int(10)
>>> boolean: ap.Boolean = int_val == 11
>>> ap.assert_false(boolean)
```