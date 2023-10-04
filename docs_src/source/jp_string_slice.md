<span class="inconspicuous-txt">※この翻訳ドキュメントはスクリプトによって出力・同期されています。内容が怪しそうな場合は<a href="https://github.com/simon-ritchie/apysc/issues" target="_blank">GitHubにissue</a>を追加したり[英語の原文](https://simon-ritchie.github.io/apysc/en/string_slice.html)の確認をお願いします。</span>

# String クラスの slice メソッド

このページでは`String`クラスの`slice`メソッドについて説明します。

## メソッド概要

`slice`メソッドはインデックスの開始と終了の指定値を使って文字列をスライス（文字列の一部の抽出を）します。

## 基本的な使い方

`slice`メソッドは`start`と`end`の2つの引数を必要とします。

`start`引数はスライスの開始インデックスです。

同様に、`end`引数はスライスの終点のインデックスの指定となります。スライス範囲の最後はこのインデックス（ただしこのインデックス自体は含みません）が使われます。

```py
# runnable
import apysc as ap

stage: ap.Stage = ap.Stage(
    stage_width=0,
    stage_height=0,
    background_color=ap.Color("#333"),
    stage_elem_id="stage",
)

string: ap.String = ap.String("012345")
result_string: ap.String = string.slice(start=0)
ap.assert_equal(result_string, "012345")

result_string = string.slice(start=1)
ap.assert_equal(result_string, "12345")

result_string = string.slice(start=0, end=2)
ap.assert_equal(result_string, "01")

result_string = string.slice(start=2, end=4)
ap.assert_equal(result_string, "23")

result_string = string.slice(start=-2)
ap.assert_equal(result_string, "45")

result_string = string.slice(start=-3, end=-1)
ap.assert_equal(result_string, "34")

ap.save_overall_html(dest_dir_path="string_slice_basic_usage/")
```

<iframe src="static/string_slice_basic_usage/index.html" width="0" height="0"></iframe>

## slice メソッドのAPI

<span class="inconspicuous-txt">特記事項: このAPIドキュメントはドキュメントビルド用のスクリプトによって自動で生成・同期されています。そのためもしかしたらこの節の内容は前節までの内容と重複している場合があります。</span>

**[インターフェイスの構造]** `slice(self, *, start: Union[int, ForwardRef('Int')], end: Union[int, ForwardRef('Int'), NoneType] = None, variable_name_suffix: str = '') -> 'String'`<hr>

**[インターフェイス概要]**

指定された引数の範囲に基づいてスライスされた文字列を取得します。<hr>

**[引数]**

- `start`: Union[int, "Int"]
  - スライス範囲の開始インデックス。

- `end`: Optional[Union[int, "Int"]], optional
  - スライス範囲の終了インデックス。もしもこの引数が指定されなかった場合、このメソッドは終了位置のスライスをスキップします。

- `variable_name_suffix`: str, default ""
  - JavaScript上の変数のサフィックスの設定です。この設定はJavaScriptのデバッグ時に役立つことがあります。

<hr>

**[返却値]**

- `result`: String
  - スライス結果の文字列。

<hr>

**[コードサンプル]**

```py
>>> import apysc as ap
>>> stage: ap.Stage = ap.Stage(
...     stage_width=0,
...     stage_height=0,
...     background_color=ap.Color("#333"),
...     stage_elem_id="stage",
... )
>>> string: ap.String = ap.String("012345")
>>> result_string: ap.String = string.slice(start=0)
>>> result_string
String("012345")

>>> result_string = string.slice(start=1)
>>> result_string
String("12345")

>>> result_string = string.slice(start=0, end=2)
>>> result_string
String("01")

>>> result_string = string.slice(start=2, end=4)
>>> result_string
String("23")

>>> result_string = string.slice(start=-2)
>>> result_string
String("45")

>>> result_string = string.slice(start=-3, end=-1)
>>> result_string
String("34")
```