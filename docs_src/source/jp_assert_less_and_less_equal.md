<span class="inconspicuous-txt">※この翻訳ドキュメントはスクリプトによって出力・同期されています。内容が怪しそうな場合は<a href="https://github.com/simon-ritchie/apysc/issues" target="_blank">GitHubにissue</a>を追加したり[英語の原文](https://simon-ritchie.github.io/apysc/en/assert_less_and_less_equal.html)の確認をお願いします。</span>

# assert_less と assert_less_equal の各インターフェイス

このページでは`assert_less`と`assert_less_equal`関数の各インターフェイスについて説明します。

## 各インターフェイスの概要

`assert_less`関数のインターフェイスは1つ目に指定された値が2つ目の値よりも小さいことをチェックします。

似たような形で、`assert_less_equal`関数では最初に指定された値が2つ目に指定された値よりも小さいかもしくは同値なことをチェックします。

## 関連資料

- [JavaScriptの各アサーションのインターフェイスの基本的な挙動](jp_assertion_basic_behavior.md)

## 基本的な使い方

`assert_less`と`assert_less_equal`のインターフェイスは`left`引数と`right`引数の指定を必要とします。

これらの値はPythonビルトインの`int`や`float`、apyscの`Int`や`Number`などの数値の値のみを受け付けます。

`msg`引数は省略可です。

もしアサーションが失敗した場合には指定された`msg`

```py
# runnable
import apysc as ap

stage: ap.Stage = ap.Stage(
    stage_width=0, stage_height=0, background_color="#333", stage_elem_id="stage"
)
int_val_1: ap.Int = ap.Int(10)
int_val_2: ap.Int = ap.Int(9)
ap.assert_less(left=int_val_1, right=int_val_2, msg="Assertion failed")

ap.assert_less_equal(left=int_val_1, right=10, msg="Assertion failed")

ap.save_overall_html(dest_dir_path="assert_less_and_less_equal_basic_usage_1/")
```

<iframe src="static/assert_less_and_less_equal_basic_usage_1/index.html" width="0" height="0"></iframe>

以下の例ではアサーションは失敗し、`Assertion failed`というメッセージがブラウザのコンソール上に表示されます:

```py
# runnable
import apysc as ap

stage: ap.Stage = ap.Stage(
    stage_width=0, stage_height=0, background_color="#333", stage_elem_id="stage"
)
int_val_1: ap.Int = ap.Int(9)
int_val_2: ap.Int = ap.Int(9)
ap.assert_less(left=int_val_1, right=int_val_2, msg="Assertion failed")

ap.save_overall_html(dest_dir_path="assert_less_and_less_equal_basic_usage_2/")
```

<iframe src="static/assert_less_and_less_equal_basic_usage_2/index.html" width="0" height="0"></iframe>

## assert_less のAPI

<span class="inconspicuous-txt">特記事項: このAPIドキュメントはドキュメントビルド用のスクリプトによって自動で生成・同期されています。そのためもしかしたらこの節の内容は前節までの内容と重複している場合があります。</span>

**[インターフェイスの構造]** `assert_less(left: Union[int, float, apysc._type.int.Int, apysc._type.number.Number], right: Union[int, float, apysc._type.int.Int, apysc._type.number.Number], *, msg: str = '') -> None`<hr>

**[インターフェイス概要]**

JavaScriptの未満条件のアサーションのインターフェイスです。<hr>

**[引数]**

- `left`: Union[int, float, Int, Number]
  - 比較用の左辺側の値（小さい側の値）。

- `right`: Union[int, float, Int, Number]
  - 比較用の右辺側の値（大きい側の値）。

- `msg`: str, optional
  - チェックに失敗した際に表示するメッセージ。

<hr>

**[コードサンプル]**

```py
>>> import apysc as ap
>>> int_val_1: ap.Int = ap.Int(9)
>>> int_val_2: ap.Int = ap.Int(10)
>>> ap.assert_greater_equal(left=int_val_1, right=int_val_2)
```

## assert_less_equal のAPI

<span class="inconspicuous-txt">特記事項: このAPIドキュメントはドキュメントビルド用のスクリプトによって自動で生成・同期されています。そのためもしかしたらこの節の内容は前節までの内容と重複している場合があります。</span>

**[インターフェイスの構造]** `assert_less_equal(left: Union[int, float, apysc._type.int.Int, apysc._type.number.Number], right: Union[int, float, apysc._type.int.Int, apysc._type.number.Number], *, msg: str = '') -> None`<hr>

**[インターフェイス概要]**

JavaScriptの以下条件のアサーションのインターフェイスです。<hr>

**[引数]**

- `left`: Union[int, float, Int, Number]
  - 比較用の左辺側の値（小さい側の値）。

- `right`: Union[int, float, Int, Number]
  - 比較用の右辺側の値（大きい側の値）。

- `msg`: str, optional
  - チェックに失敗した際に表示するメッセージ。

<hr>

**[コードサンプル]**

```py
>>> import apysc as ap
>>> int_val_1: ap.Int = ap.Int(9)
>>> int_val_2: ap.Int = ap.Int(10)
>>> ap.assert_greater_equal(left=int_val_1, right=int_val_2)
>>> int_val_3: ap.Int = ap.Int(9)
>>> ap.assert_greater_equal(left=int_val_1, right=int_val_3)
```