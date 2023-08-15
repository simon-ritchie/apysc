<span class="inconspicuous-txt">※この翻訳ドキュメントはスクリプトによって出力・同期されています。内容が怪しそうな場合は<a href="https://github.com/simon-ritchie/apysc/issues" target="_blank">GitHubにissue</a>を追加したり[英語の原文](https://simon-ritchie.github.io/apysc/en/assert_equal_and_not_equal.html)の確認をお願いします。</span>

# assert_equal と assert_not_equal インターフェイス

このページでは`assert_equal`と`assert_not_equal`関数の各インターフェイスについて説明します。

## 各インターフェイスの概要

`assert_equal`関数のインターフェイスは2つのJavaScript上の値が等値かどうかをチェックします。逆に`assert_not_equal`関数のインターフェイスは2つの値が等値ではないことをチェックします。

## 関連資料

- [JavaScriptの各アサーションのインターフェイスの基本的な挙動](jp_assertion_basic_behavior.md)

## 基本的な使い方

`assert_equal`と`assert_not_equal`インターフェイスは`left`と`right`の各引数の指定を必要とします。`msg`引数は省略可です。

もしも`left`引数の値と`right`引数の値が一致していない場合、`assert_equal`関数によるチェックは失敗しブラウザ上のコンソールにエラーメッセージが表示されます。

```py
# runnable
import apysc as ap

stage: ap.Stage = ap.Stage(
    stage_width=0,
    stage_height=0,
    background_color=ap.Color("#333"),
    stage_elem_id="stage",
)

int_1: ap.Int = ap.Int(10)
ap.assert_equal(left=11, right=int_1, msg="Values are not equal!")

ap.save_overall_html(dest_dir_path="assert_equal_basic_usage/")
```

```
[assert_equal]
Left-side variable name: i_11
Left value: 11 right value: 10
...
Assertion failed: Values are not equal!
```

<iframe src="static/assert_equal_basic_usage/index.html" width="0" height="0"></iframe>

`assert_not_equal`インターフェイスも同様の引数を持っており、もし`left`引数の値が`right`引数の値と等値の場合チェック処理は失敗します:

```py
# runnable
import apysc as ap

stage: ap.Stage = ap.Stage(
    stage_width=0,
    stage_height=0,
    background_color=ap.Color("#333"),
    stage_elem_id="stage",
)

int_1: ap.Int = ap.Int(10)
ap.assert_not_equal(left=10, right=int_1, msg="Values are equal!")

ap.save_overall_html(dest_dir_path="assert_not_equal_basic_usage/")
```

```
[assert_not_equal]
Right-side variable name: i_11
Left value: 10 right value: 10
...
Assertion failed: Values are equal!
```

<iframe src="static/assert_not_equal_basic_usage/index.html" width="0" height="0"></iframe>

## assert_equal API

<span class="inconspicuous-txt">特記事項: このAPIドキュメントはドキュメントビルド用のスクリプトによって自動で生成・同期されています。そのためもしかしたらこの節の内容は前節までの内容と重複している場合があります。</span>

**[インターフェイスの構造]** `assert_equal(left: Any, right: Any, *, msg: str = '') -> None`<hr>

**[インターフェイス概要]**

等値条件のためのJavaScript上のアサーションのインターフェイスです。<hr>

**[引数]**

- `left`: *
  - 比較用の左辺の値。

- `right`: *
  - 比較用の右辺の値。

- `msg`: str, optional
  - チェックに失敗した際に表示するメッセージ。

<hr>

**[特記事項]**

 ・もしも引数にArrayやlistの値が指定された場合、このインターフェイスの処理の代わりにassert_arrays_equal関数が呼ばれます。<br> ・もしも引数にDictionaryやdictの値が指定された場合、このインターフェイスの処理の代わりにassert_dicts_equal関数が呼ばれます。<hr>

**[コードサンプル]**

```py
>>> import apysc as ap
>>> int_1: ap.Int = ap.Int(10)
>>> int_2: ap.Int = ap.Int(10)
>>> ap.assert_equal(int_1, int_2)
```

## assert_not_equal API

<span class="inconspicuous-txt">特記事項: このAPIドキュメントはドキュメントビルド用のスクリプトによって自動で生成・同期されています。そのためもしかしたらこの節の内容は前節までの内容と重複している場合があります。</span>

**[インターフェイスの構造]** `assert_not_equal(left: Any, right: Any, *, msg: str = '') -> None`<hr>

**[インターフェイス概要]**

非等値条件のためのJavaScript上のアサーションのインターフェイスです。<hr>

**[引数]**

- `left`: *
  - 比較用の左辺の値。

- `right`: *
  - 比較用の右辺の値。

- `msg`: str, optional
  - チェックに失敗した際に表示するメッセージ。

<hr>

**[特記事項]**

 ・もしも引数にArrayやlistの値が指定された場合、このインターフェイスの処理の代わりにassert_arrays_not_equal関数が呼ばれます。<br> ・もしも引数にDictionaryやdictの値が指定された場合、このインターフェイスの代わりにassert_dicts_not_equal関数が呼ばれます。<hr>

**[コードサンプル]**

```py
>>> import apysc as ap
>>> int_1: ap.Int = ap.Int(10)
>>> int_2: ap.Int = ap.Int(11)
>>> ap.assert_not_equal(int_1, int_2)
```