<span class="inconspicuous-txt">※この翻訳ドキュメントはスクリプトによって出力・同期されています。内容が怪しそうな場合は<a href="https://github.com/simon-ritchie/apysc/issues" target="_blank">GitHubにissue</a>を追加したり[英語の原文](https://simon-ritchie.github.io/apysc/en/assert_greater_and_greater_equal.html)の確認をお願いします。</span>

# assert_greater と assert_greater_equal の各インターフェイス

このページでは`assert_greater`と`assert_greater_equal`関数の各インターフェイスについて説明します。

## 各インターフェイスの概要

`assert_greater`関数のインターフェイスでは1つ目に指定された値が2つ目に指定された値よりも大きいことをチェックします。

似たような形で、`assert_greater_equal`関数では最初に指定された値が2つ目の値よりも大きいかもしくは同値なことをチェックします。

## 関連資料

- [JavaScriptの各アサーションのインターフェイスの基本的な挙動](jp_assertion_basic_behavior.md)

## 基本的な使い方

`assert_greater`と`assert_greater_equal`インターフェイスは`left`と`right`の引数を必要とします。

これらの引数はPythonビルトインの`int`や`float`、apyscの`Int`や`Number`などの数値の値のみ受け付けます。

`msg`引数は省略可です。

このインターフェイスはアサーションが失敗した際に`msg`（message）引数の値をブラウザのコンソール上に表示します。

```py
# runnable
import apysc as ap

stage: ap.Stage = ap.Stage(
    stage_width=0, stage_height=0, background_color="#333", stage_elem_id="stage"
)
int_val_1: ap.Int = ap.Int(10)
int_val_2: ap.Int = ap.Int(9)
ap.assert_greater(left=int_val_1, right=int_val_2, msg="Assertion failed")

int_val_3: ap.Int = ap.Int(10)
ap.assert_greater_equal(left=int_val_1, right=int_val_3, msg="Assertion failed")

ap.save_overall_html(dest_dir_path="assert_greater_and_greater_equal_basic_usage_1/")
```

<iframe src="static/assert_greater_and_greater_equal_basic_usage_1/index.html" width="0" height="0"></iframe>

`以下の例ではアサーションが失敗し、`Assertion failed`というメッセージがブラウザ上のコンソールに表示されます:

```py
# runnable
import apysc as ap

stage: ap.Stage = ap.Stage(
    stage_width=0, stage_height=0, background_color="#333", stage_elem_id="stage"
)
int_val_1: ap.Int = ap.Int(9)
int_val_2: ap.Int = ap.Int(10)
ap.assert_greater(left=int_val_1, right=int_val_2, msg="Assertion failed")

ap.save_overall_html(dest_dir_path="assert_greater_and_greater_equal_basic_usage_2/")
```

<iframe src="static/assert_greater_and_greater_equal_basic_usage_2/index.html" width="0" height="0"></iframe>

## assert_greater のAPI

<span class="inconspicuous-txt">特記事項: このAPIドキュメントはドキュメントビルド用のスクリプトによって自動で生成・同期されています。そのためもしかしたらこの節の内容は前節までの内容と重複している場合があります。</span>

**[インターフェイスの構造]** `assert_greater(left: Union[int, float, apysc._type.int.Int, apysc._type.number.Number], right: Union[int, float, apysc._type.int.Int, apysc._type.number.Number], *, msg: str = '') -> None`<hr>

**[インターフェイス概要]**

JavaScriptの超過条件のアサーションのためのインターフェイスです。<hr>

**[引数]**

- `left`: Union[int, float, Int, Number]
  - 比較用の左辺の値（大きい側の値）。

- `right`: Union[int, float, Int, Number]
  - 比較用の右辺の値（小さい側の値）。

- `msg`: str, optional
  - チェックに失敗した際に表示するメッセージ。

<hr>

**[コードサンプル]**

```py
>>> import apysc as ap
>>> int_val_1: ap.Int = ap.Int(10)
>>> int_val_2: ap.Int = ap.Int(9)
>>> ap.assert_greater(left=int_val_1, right=int_val_2)
```

## assert_greater_equal のAPI

<span class="inconspicuous-txt">特記事項: このAPIドキュメントはドキュメントビルド用のスクリプトによって自動で生成・同期されています。そのためもしかしたらこの節の内容は前節までの内容と重複している場合があります。</span>

**[インターフェイスの構造]** `assert_greater_equal(left: Union[int, float, apysc._type.int.Int, apysc._type.number.Number], right: Union[int, float, apysc._type.int.Int, apysc._type.number.Number], *, msg: str = '') -> None`<hr>

**[インターフェイス概要]**

JavaScriptの以上の条件のアサーションのためのインターフェイスです。<hr>

**[引数]**

- `left`: Union[int, float, Int, Number]
  - 比較用の左辺の値（大きい側の値）。

- `right`: Union[int, float, Int, Number]
  - 比較用の右辺の値（小さい側の値）。

- `msg`: str, optional
  - チェックに失敗した際に表示するメッセージ。

<hr>

**[コードサンプル]**

```py
>>> import apysc as ap
>>> int_val_1: ap.Int = ap.Int(10)
>>> int_val_2: ap.Int = ap.Int(9)
>>> ap.assert_greater_equal(left=int_val_1, right=int_val_2)
>>> int_val_3: ap.Int = ap.Int(10)
>>> ap.assert_greater_equal(left=int_val_1, right=int_val_3)
```